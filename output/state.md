# Talent Sync Pipeline — State File

## Last Run
- **Run ID:** run_20260609_055509
- **Started:** 2026-06-09T09:55:09.465Z
- **Completed:** 2026-06-09T09:55:46.266Z

## This Run
- **Total Events In Feed:** 32
- **Unique Events Processed:** 28
- **Dead Lettered:** 2
- **Flagged For Review:** 2
- **Replies Classified:** 6

### Event Type Breakdown
- **contact.created:** 7
- **contact.updated:** 14
- **reply.received:** 6
- **talent.vibe_check:** 1

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
| Contact | Rate | Stage | Interest | Doc Link |
|---|---|---|---|---|
| c_anika | 50 | contacted | pending | null |
| c_bob | 45 | contacted | interested | https://github.com/wajahat-py/talent-sync-trial/blob/main/docs/voiceloop-prd.md |
| c_diego | 36 | contacted | interested | no doc found |
| c_jamie | 55 | contacted | declined | null |
| c_lena | 50 | null | interested | https://github.com/wajahat-py/talent-sync-trial/blob/main/docs/pocketcfo-prd.md |
| c_sara | 38 | contacted | needs_review | null |
| c_tomas | 46 | contacted | needs_review | no doc found |
