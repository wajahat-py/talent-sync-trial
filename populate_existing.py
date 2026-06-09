import anthropic
import requests
import json
import re

SUPABASE_URL = ""

SUPABASE_KEY = ""

ANTHROPIC_KEY = ""

headers = {
    "apikey": SUPABASE_KEY,
    "Authorization": f"Bearer {SUPABASE_KEY}",
    "Content-Type": "application/json"
}

# Fetch all processed replies
resp = requests.get(
    f"{SUPABASE_URL}/rest/v1/processed_replies?select=contact_id,reply_text,interest",
    headers=headers
)
replies = resp.json()
print(f"Found {len(replies)} replies to backfill")

client = anthropic.Anthropic(api_key=ANTHROPIC_KEY)

for reply in replies:
    contact_id = reply["contact_id"]
    reply_text = reply["reply_text"]
    interest = reply["interest"]

    print(f"Processing {contact_id}...")

    message = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=256,
        system="You are a JSON-only response bot. Respond with raw valid JSON only. No markdown, no code blocks, no explanation. Your response must start with { and end with }.",
        messages=[
            {
                "role": "user",
                "content": f"Given this reply from a potential collaborator and their classified interest level, write one sentence explaining why they were classified as '{interest}'.\n\nReply: {reply_text}\n\nReturn only this JSON:\n{{\"reasoning\": \"\"}}"
            }
        ]
    )

    raw = message.content[0].text.strip()
    # Strip markdown fences if present
    raw = re.sub(r'```json\n?', '', raw)
    raw = re.sub(r'```', '', raw)
    raw = raw.strip()

    print(f"  Raw response: {raw}")

    if not raw:
        print(f"  Empty response for {contact_id}, skipping")
        continue

    parsed = json.loads(raw)
    reasoning = parsed.get("reasoning", "")

    # Update contact interest_reason
    update_resp = requests.patch(
        f"{SUPABASE_URL}/rest/v1/contacts?contact_id=eq.{contact_id}",
        headers=headers,
        json={"interest_reason": reasoning}
    )

    print(f"  Updated {contact_id}: {reasoning}")

print("Backfill complete.")