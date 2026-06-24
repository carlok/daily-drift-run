# Daily Drift Trace Automation Prompt

Run one Daily Drift trace for this repository.

Follow the repository rules in `README.md` and the template in
`templates/trace.md`. Create exactly one new dated folder under
`days/YYYY-MM-DD-slug/` for today's date. The slug should be short, concrete,
and based on what the run actually became.

Start by checking whether a trace for today already exists under
`days/YYYY-MM-DD-*/`. If today's trace already exists, do nothing else: create
no duplicate, make no edits, perform no fixes, do not commit, do not push, and
do not send email. Just report that today's trace already exists.

If today's trace does not already exist, start from the previous trace's Seed
if useful, but do not force continuity. Choose one public encounter unless
today is explicitly a silence, local-material, or self-contained experiment
day. Public encounters can be web pages, essays, docs, papers, repos, archives,
manuals, images, or other public materials. Cite sources with links or
bibliographic notes.

Produce a lightly curated `trace.md` with these sections:

- Departure
- Encounter
- Residue
- Made
- Seed

Optional files are allowed only if they genuinely serve the day: code, notes,
diagrams, screenshots, data, quotes-with-commentary, sketches, failed attempts,
or odd formats. Do not make a code artifact by default. Do not make an essay by
default. Preserve uncertainty and unfinished edges while keeping the trace
understandable to a stranger.

After creating the day packet:

- Update `journal.md` in reverse chronological order.
- Update `README.md` Latest Trace to point to the new trace.
- Verify local Markdown links resolve.
- If any HTML or code artifact was created, run the smallest reasonable syntax
  or smoke check.
- Commit the changes with message: `Add daily drift trace for YYYY-MM-DD`.
- Push to `origin main`.
- Send the email notification from the official main local checkout:
  `/Users/carlo/Documents/varie/hacks/scratch/llm/free_llm`.
  Run `python3 scripts/notify_daily_trace.py` there after ensuring that checkout
  contains the pushed trace. The script reads ignored local files `.env` and
  `recipients.json`, which live in that official checkout rather than in the
  Codex worktree. It sends one separate email per recipient, with that
  recipient in `To`. If the day packet has a single Markdown artifact, the
  email body should point directly to that Markdown file. If sending fails,
  report the failure clearly and do not retry blindly.

Do not backfill missed days.

Keep the same conversation to not pollute with many chat and change just once
in a while.
