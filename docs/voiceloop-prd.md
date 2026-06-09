# VoiceLoop — PRD (v1)

## One-liner
A voice-first daily journal for iOS: you ramble for two minutes, VoiceLoop turns it into a structured entry — mood, highlights, people mentioned, open loops — and surfaces patterns weekly.

## Problem
Journaling sticks for almost nobody because typing is friction. Voice memos pile up unprocessed. People want the reflection benefits without the writing habit.

## Target user
Busy professionals 25-45 who already talk to their phone (voice notes, Siri) but never re-read or act on anything they capture.

## MVP scope
1. Record or import a voice memo (≤5 min)
2. Transcription → structured entry: summary, mood score, people, places, open loops
3. Daily entry view + calendar history
4. Weekly digest: recurring themes, unresolved loops, mood trend
5. Push reminder at user-chosen time

## Explicitly NOT in MVP
- Social/sharing of any kind
- Android
- Real-time conversation mode
- Therapy-adjacent advice (liability — digest stays descriptive)

## Stack
- iOS: React Native (Expo)
- Transcription: Whisper API
- Structuring: Claude (single extraction prompt, JSON out)
- Backend: lightweight — Supabase + one queue worker
- Push: Expo notifications

## Open roles
- Backend: ingestion pipeline + digest worker (the API layer)
- Design: entry view + digest, calm not clinical
- Growth: App Store + short-form clips of weekly digests

## Milestones
- M1 (wk 1-2): record → transcript → structured entry, ugly UI
- M2 (wk 3-4): history + digest + push
- M3 (wk 5-6): polish, TestFlight cohort of 25
