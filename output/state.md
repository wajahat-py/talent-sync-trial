# Talent Sync Pipeline — State File

## Last Run
- **Run ID:** run_20260609_142731
- **Started:** 2026-06-09T18:27:31.498Z
- **Completed:** 2026-06-09T18:27:47.861Z

## This Run
- **Total Events In Feed:** 38
- **Unique Events Processed:** 5
- **Dead Lettered:** 1
- **Flagged For Review:** 0
- **Replies Classified:** 2

### Event Type Breakdown
- **reply.received:** 2
- **contact.created:** 1
- **contact.updated:** 1
- **contact.archived:** 1

## Overall System State
- **Contacts In Roster:** 8
- **Total Dead Lettered (all runs):** 3
- **Total Pending Review (all runs):** 2

## Conflict Resolution Rule
When two events update the same field with the same timestamp, the event with the lexicographically larger event_id wins.

## Dead Letter Log (all time)
- **evt_010** (contact.updated): malformed_payload: missing or invalid contact_id in payload
- **evt_020** (talent.vibe_check): unknown_event_type
- **evt_033** (contact.archived): unknown_event_type

## Review Queue (pending review)
- **c_sara** (evt_019): confidence 0.65
- **c_tomas** (evt_028): confidence 0.65

## Roster Snapshot
| Contact | Rate | Stage | Interest | Interest Reason | Doc Link |
|---|---|---|---|---|---|
| c_anika | 50 | contacted | interested | Collaborator explicitly mentions PocketCFO by exact name and expresses clear enthusiasm with specific feature interest (runway math), indicating strong alignment. | https://github.com/wajahat-py/talent-sync-trial/blob/main/docs/pocketcfo-prd.md |
| c_bob | 48 | contacted | interested | They explicitly expressed enthusiasm ('sounds exactly like the kind of build I've been hoping for'), confirmed commitment ('count me in'), provided specific availability, and demonstrated engagement by identifying a concrete starting point for the project. | https://github.com/wajahat-py/talent-sync-trial/blob/main/docs/voiceloop-prd.md |
| c_diego | 36 | contacted | interested | They explicitly confirmed interest with 'Count me in', demonstrated direct expertise alignment by stating growth for voice products is their specialty, and made a concrete commitment to dedicate 10 hours per week starting immediately. | no doc found |
| c_jamie | 55 | contacted | declined | They explicitly declined the opportunity due to existing commitments through August and stated they will pass. | null |
| c_lena | 50 | null | interested | They explicitly stated 'I'm in' and demonstrated direct relevant experience in personal finance tooling, the core domain of PocketCFO. | https://github.com/wajahat-py/talent-sync-trial/blob/main/docs/pocketcfo-prd.md |
| c_marco | 42 | null | pending | null | null |
| c_sara | 38 | contacted | declined | Collaborator explicitly declined the opportunity citing current workload constraints this quarter. | null |
| c_tomas | 46 | contacted | needs_review | The reply shows genuine interest and relevant expertise in design systems for health/fitness, but lacks specific commitment details such as availability, scope of work, or concrete next steps needed to move forward. | no doc found |
