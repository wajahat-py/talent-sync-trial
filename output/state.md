# Talent Sync Pipeline — State File

## Last Run
- **Run ID:** run_20260609_050619
- **Started:** 2026-06-09T09:06:19.536Z
- **Completed:** 2026-06-09T09:06:28.326Z

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
- **c_tomas** (evt_028): confidence 0.65
- **c_sara** (evt_019): confidence 0.65

## Roster Snapshot
| Contact | Rate | Stage | Interest | Interest Reason | Doc Link |
|---|---|---|---|---|---|
| c_anika | 50 | contacted | pending | null | null |
| c_bob | 45 | contacted | interested | null | https://github.com/wajahat-py/talent-sync-trial/blob/main/docs/voiceloop-prd.md |
| c_diego | 36 | contacted | interested | null | no doc found |
| c_jamie | 55 | contacted | declined | null | null |
| c_lena | 50 | null | interested | null | https://github.com/wajahat-py/talent-sync-trial/blob/main/docs/pocketcfo-prd.md |
| c_sara | 38 | contacted | needs_review | null | null |
| c_tomas | 46 | contacted | needs_review | null | no doc found |
