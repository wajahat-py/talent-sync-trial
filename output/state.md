# Talent Sync Pipeline — State File

## Last Run
- **Run ID:** run_20260609_034027
- **Started:** 2026-06-09T07:40:27.329Z
- **Completed:** 2026-06-09T07:40:58.131Z

## What Was Processed
- **Unique Events Processed:** 28
- **Contacts In Roster:** 7
- **Replies Classified:** 6
- **Dead Lettered:** 2
- **Flagged For Review:** 2

## Conflict Resolution Rule
When two events update the same field with the same timestamp, the event with the lexicographically larger event_id wins.

## Dead Letter Log
- **evt_010** (contact.updated): malformed_payload: missing or invalid contact_id in payload
- **evt_020** (talent.vibe_check): unknown_event_type

## Review Queue
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
