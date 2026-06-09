# PocketCFO — PRD (v1)

## One-liner
A personal-finance copilot for freelancers: connects to your accounts, watches cash flow, and answers "can I afford X?" with real numbers instead of vibes.

## Problem
Freelancers with lumpy income can't use normal budgeting apps — monthly category budgets break when you're paid 3x in March and 0x in April. They need runway thinking, not envelope thinking.

## Target user
Independent contractors and studio freelancers, 1-person LLCs, income $40-200k, paid irregularly across 2-5 clients.

## MVP scope
1. Bank + card connection (read-only) via Plaid
2. Income smoothing: rolling 6-month effective monthly income
3. Runway view: months of survival at current burn, updated daily
4. "Can I afford X?" — one input box, answer with the math shown
5. Tax set-aside tracker (estimated quarterly, auto-computed %)

## Explicitly NOT in MVP
- Invoicing
- Payments of any kind (read-only forever in v1)
- Crypto accounts
- Business-entity accounting (this is personal cash flow)

## Stack
- iOS: React Native (Expo)
- Data: Plaid → Supabase
- Reasoning: Claude over a computed financial-state JSON (never raw transactions)
- Charts: Victory Native

## Open roles
- Frontend: the runway view and afford-it flow are the product — needs someone strong
- Backend: Plaid sync worker, smoothing math, state computation
- Growth: freelancer communities, "screenshot your runway" loop

## Milestones
- M1 (wk 1-2): Plaid connect → runway number on screen
- M2 (wk 3-4): afford-it Q&A + tax set-aside
- M3 (wk 5-6): TestFlight, 20 freelancers
