# Talent Sync Pipeline — State File

## Last Run
- **Run ID:** run_20260609_060855
- **Started:** 2026-06-09T10:08:55.507Z
- **Completed:** 2026-06-09T10:09:04.198Z

## This Run
- **Total Events In Feed:** 32
- **Unique Events Processed:** 0
- **Dead Lettered:** 0
- **Flagged For Review:** 0
- **Replies Classified:** 0

### Event Type Breakdown
No events processed this run.

## Overall System State
- **Contacts In Roster:** 7
- **Total Dead Lettered (all runs):** 2
- **Total Pending Review (all runs):** 2

## Conflict Resolution Rule
When two events update the same field with the same timestamp, the event with the lexicographically larger event_id wins.

## Dead Letter Log (all time)
- **evt_010** (contact.updated): malformed_payload: missing or invalid contact_id in payload
- **evt_020** (talent.vibe_check): unknown_event_type

## Review Queue (pending review)
- **c_sara** (evt_019): confidence 0.65
- **c_tomas** (evt_028): confidence 0.65

## Roster Snapshot
| Contact | Rate | Stage | Interest | Interest Reason | Doc Link |
|---|---|---|---|---|---|
| c_anika | 50 | contacted | pending | null | null |
| c_bob | 45 | contacted | interested | They explicitly expressed enthusiasm ('sounds exactly like the kind of build I've been hoping for'), confirmed commitment ('count me in'), provided specific availability, and demonstrated engagement by identifying a concrete starting point for the project. | https://github.com/wajahat-py/talent-sync-trial/blob/main/docs/voiceloop-prd.md |
| c_diego | 36 | contacted | interested | They explicitly confirmed interest with 'Count me in', demonstrated direct expertise alignment by stating growth for voice products is their specialty, and made a concrete commitment to dedicate 10 hours per week starting immediately. | no doc found |
| c_jamie | 55 | contacted | declined | They explicitly declined the opportunity due to existing commitments through August and stated they will pass. | null |
| c_lena | 50 | null | interested | They explicitly stated 'I'm in' and demonstrated direct relevant experience in personal finance tooling, the core domain of PocketCFO. | https://github.com/wajahat-py/talent-sync-trial/blob/main/docs/pocketcfo-prd.md |
| c_sara | 38 | contacted | needs_review | The prospect shows genuine interest in the opportunity but their current unavailability and uncertain timeline ('let's see how the month goes') prevents a clear commitment, requiring manual review to determine appropriate follow-up strategy. | null |
| c_tomas | 46 | contacted | needs_review | The reply shows genuine interest and relevant expertise in design systems for health/fitness, but lacks specific commitment details such as availability, scope of work, or concrete next steps needed to move forward. | no doc found |
