"""Join candidates with LLM scores -> tracker/jobs.json (published next to the tracker page)."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
cand = {r["id"]: r for r in map(json.loads, (ROOT / "data" / "candidates.jsonl").open())}
scored = {}
for f in sorted((ROOT / "data").glob("scored_*.jsonl")):
    for line in f.open():
        line = line.strip()
        if not line: continue
        try: s = json.loads(line)
        except json.JSONDecodeError: continue
        if s.get("id") in cand: scored[s["id"]] = s
keep = ["id", "title", "company", "location", "posted", "url", "source"]
rows = [{**{k: cand[i].get(k) for k in keep}, **{k: v for k, v in s.items() if k != "id"}}
        for i, s in scored.items() if (s.get("score") or 0) >= 3]
rows.sort(key=lambda r: -(r.get("score") or 0))
(ROOT / "tracker" / "jobs.json").write_text(json.dumps(rows, ensure_ascii=False))
print(f"scored {len(scored)}/{len(cand)}, published {len(rows)}, 7+: {sum((r['score'] or 0) >= 7 for r in rows)}")
