# Triage brief (Haiku)

Repo: C:\Users\r3d_flzp\Desktop\job-search (Windows). Queue: data/apply_queue_2026-10-27.jsonl (one JSON per line; read only your rows by line number, do NOT edit the queue file).
Write ONLY your output file: data/apply_triage/batch_<N>.json (create the folder if missing) - a JSON array, one object per row.

Candidate: Denis, student, wants entry-level/junior/intern/trainee IT, Python, QA, support, automation/PLC work; contract must be UoP/UZ (employment/mandate contract). B2B-only, freelance, contractor = skip. Schedule: part-time or flexible, remote anywhere or hybrid/onsite Wroclaw only. Onsite in another city = skip.

For each row open `url` (use curl.exe or Invoke-WebRequest or WebFetch; for himalayas.app jobs look for the real application link on the page / in its API field applicationLink; for justjoin.it offers use https://api.justjoin.it/v2/user-panel/offers/<slug> or the page text and the "Apply" button target). Find out:
- alive: true/false (404, "expired", "no longer accepting" = false)
- employer: real company name (not an aggregator)
- contract: "UoP"/"UZ"/"B2B"/"unknown" (justjoin shows contract types; if both UoP and B2B listed, say "UoP+B2B")
- location_ok: true/false/unknown (remote OK, or Wroclaw; else false)
- apply_url: the URL of the actual application form (employer ATS: Traffit, eRecruiter, Lever, Greenhouse, SmartRecruiters, Workable, Recruitee, justjoin native, company site). If the only way to apply is an aggregator that is not the employer's own page (alignerr, flexjobs, builtin, swooped, aijobs, contra, arc.dev, talentdays) and you cannot find the employer's own page, apply_url=null.
- platform: short name of the form system
- needs_login: true/false (account wall)
- captcha_seen: true/false/unknown
- languages: PL/EN of the posting
- verdict: "go" (alive + UoP/UZ-or-unknown-but-not-B2B-only + location ok + real apply_url), or "skip" with reason
- note: <=20 words (key requirements: years of experience asked, languages, tech stack, anything odd like required portfolio, salary question)

Be factual. If you cannot verify something, write "unknown", never guess. Do not submit anything, do not type personal data anywhere. Report back with one line: file written and counts of go/skip.

Row object keys: id, company, title, employer, alive, contract, location_ok, apply_url, platform, needs_login, captcha_seen, languages, verdict, note.
