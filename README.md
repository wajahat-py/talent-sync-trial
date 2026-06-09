# Talent Sync Pipeline

> Built by Wajahat Hassan &nbsp;|&nbsp; n8n + Supabase + Claude + GitHub

---

## What This Does

Takes a stream of contact events from a GitHub repo, maintains a roster you can trust without checking it, and connects interested people to the right project doc automatically.

Real event streams are messy. Things arrive twice, out of order, with missing fields, or as free text that needs interpretation. This pipeline handles all of it. Every run ends with one summary email and four output files pushed to GitHub.

| | |
|---|---|
| **Input** | `talent-feed.json` in your GitHub repo + project docs in `docs/` |
| **Output** | Four files in `output/` after every run |

### Output Files

| File | Contents |
|---|---|
| `roster.json` | One row per contact, always current state |
| `dead_letter.json` | Every event that could not be processed, with a reason |
| `review_queue.json` | Replies the LLM was not confident enough to write as fact |
| `state.md` | What happened this run and the current system state |

---

## Stack

| Tool | Role |
|---|---|
| n8n (self-hosted) | Workflow orchestration |
| Supabase (Postgres) | Primary data store |
| Anthropic Claude Haiku | Reply classification |
| GitHub API | Input feed and output file delivery |
| Gmail | Summary notification |

### Why This Stack

**n8n over custom code**

n8n gives you a visual audit trail of every step. You can see exactly which node processed which event, when it ran, and what it returned. Changing the LLM prompt, adjusting the confidence threshold, or adding a new event type is a configuration change, not a deployment. For a pipeline you run repeatedly and want to modify over time, that matters.

**Supabase over Airtable or Notion**

The pipeline enforces rules a spreadsheet cannot. An update arriving before its contact exists needs to be queued and replayed in order. A duplicate event needs to be skipped without touching the roster. These are transactional guarantees that require a real database. Supabase gives you full Postgres with a REST API, a live table editor, and no extra tooling to configure.

**Claude Haiku**

Fast, accurate, and cheap for classification tasks. It handles the nuance needed to distinguish genuine interest from polite deflection, respects verbatim project name matching rules consistently, and returns clean JSON. Total API cost for classifying six replies is under five cents.

**GitHub for output**

The repo was already the input source. Using it for output as well means everything lives in one place. Output files are versioned automatically. Links are permanent and openable on any device including mobile.

---

## How to Test It

### Run the Pipeline

1. Open the **Talent Sync Pipeline** workflow in n8n
2. Click **Execute Workflow**
3. Check your inbox for the summary email
4. Open `output/roster.json` in the GitHub repo to verify the roster

### Test Idempotency

Run the workflow a second time without resetting the database. The roster must be identical to the first run. The state file should show:

```
Unique Events Processed: 0
```

### Reset for a Fresh Run

```sql
DELETE FROM review_queue;
DELETE FROM dead_letter_log;
DELETE FROM processed_replies;
DELETE FROM pending_updates;
DELETE FROM processed_events;
DELETE FROM contacts;
DELETE FROM pipeline_runs;
```

---

## How to Change the LLM Prompt

Open the **Classify Reply** HTTP Request node in n8n. The prompt is in the `content` field of the messages array.

### Change the Confidence Threshold

Find this line in the prompt:

```
If confidence is below 0.75 set interest to needs_review
```

Change `0.75` to your desired value. Then open the **Confidence Above Threshold?** IF node and update the value there to match.

### Add a New Project Doc

Add a line to the Available project docs section:

```
- newproject-doc.md → https://github.com/your-repo/blob/main/docs/newproject-doc.md
```

Then add the project name to the verbatim match rule and add a matching example to the examples section.

### Make Matching Stricter or Looser

The key rule controlling match strictness is:

```
No partial matches, no descriptions, no synonyms.
```

Remove this line to allow fuzzy matching. Add more non-match examples (like `'voice product'`, `'fitness app'`) to make it stricter.

---

## Conflict Resolution Rule

When two events update the same field with the same timestamp and different values, the event with the **lexicographically larger event_id wins**.

> **Example:** `evt_012` beats `evt_011` when both update `rate_usd_hr` for `c_diego` at `2026-06-02T08:30:00Z`. Final rate is 36.

Each field tracks its own timestamp independently. An older event can still apply if it touches a field that has never been set. This is correct for PATCH-based updates where each event is a partial change, not a full snapshot.

---

## What Breaks First at 10x Volume

| Bottleneck | What Happens | Fix |
|---|---|---|
| Sequential event processing | The loop processes one event at a time. At 320+ events this becomes slow. | Queue-based worker system with parallel processing and database-level locking per contact_id |
| LLM cost and latency | One API call per reply does not scale. | Batch multiple classifications into one call, or route only ambiguous replies to the LLM |
| Per-field timestamp tracking | Ten extra columns per contact works now but grows unwieldy with more field types. | Separate `field_history` table with one row per field change |
| GitHub file writes | GET-then-PUT pattern adds latency per run. | Asynchronous file delivery or dedicated storage service |
| Single LLM prompt | Harder to tune without breaking existing classifications as reply diversity grows. | Routing layer that selects from multiple specialized prompts |

---

## Strengths

### Per-Field Timestamp Tracking
Most pipelines use one `last_updated` timestamp per row. This pipeline tracks a separate timestamp and event_id per field. An older event can still win if it touches a field that was never set. This eliminates an entire class of data loss bugs that occur with partial updates and makes the pipeline correct for PATCH-based event streams.

### Fail-Loud Dead-Lettering
Every unprocessable event is logged with its full payload and a specific reason. Nothing disappears silently. The pipeline always keeps running regardless of individual event failures.

### Full LLM Output Storage
Every reply classification stores the complete model response as JSONB in `processed_replies`. This made the Part B change order possible: adding `interest_reason` required one SQL backfill and zero re-processing. It also supports debugging, auditing, and future model evaluation.

### Two-Layer Idempotency
**Layer 1:** `processed_events` table. Any seen event_id is skipped immediately before any processing occurs.

**Layer 2:** Per-field timestamp comparison. Even if an event bypasses layer one, it cannot overwrite a field with an older value.

Running the same feed a hundred times produces the exact same result.

---

## Future Improvements

### Richer Input Validation
The current validator checks envelope fields structurally. A production system would add per-event-type schema validation, for example ensuring `contact.created` always includes name, role, and a positive rate. Configurable rules would let new event types be added without code changes and produce more specific dead-letter reasons.

### Infrastructure Error Workflow
The pipeline handles event-level failures gracefully via dead-lettering but does not yet handle infrastructure failures like a dropped database connection or a failed GitHub write mid-run. A production system would wrap the full pipeline in an error boundary that catches unexpected failures, persists the partial run state, and sends a failure notification email with the run ID, the stage where it failed, and the last successfully processed event.

### Pending Reply Handling
If a reply arrives before its contact exists, it is queued in `pending_updates`. The current flush logic handles contact updates only. A future improvement routes pending replies through the full LLM classification step after the contact is created.

## Multiple Replies Per Contact
The current pipeline uses last-reply-wins semantics. When a contact sends more than one reply, the latest classification overwrites the previous one on the contact row. The full reply history is preserved in processed_replies but only the most recent interest and interest_reason are reflected in the roster. A production system would fetch all replies for a contact, pass them together to the LLM as a conversation thread, and produce a holistic classification that accounts for how the person's position evolved over time. Alternatively, a second reply that contradicts the first could automatically trigger a human review flag rather than silently overwriting the previous classification.

### Embedding-Based Doc Matching
The current approach requires verbatim project name matches. A production system would use embedding similarity via Supabase pgvector to match replies to docs even when the project name is paraphrased or misspelled.

### Review Queue Resolution Flow
The review queue stores flagged replies but has no resolution workflow. A production system would include a simple interface for Brock to mark items reviewed, automatically updating the contact roster when resolved.

### Multi-Agent Architecture
The natural evolution is separate agents for ingestion, classification, context retrieval, and notification. Each can be scaled and updated independently. The current modular design supports this transition without a rewrite.

---

*Talent Sync Pipeline — Wajahat Hassan*
