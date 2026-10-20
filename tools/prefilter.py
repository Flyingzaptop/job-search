"""Merge data/raw/*.jsonl, dedupe and drop obvious misfits -> data/candidates.jsonl (cheap keyword pass before LLM scoring)."""
import json, re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SENIOR = re.compile(r"\b(senior|sr\.?|lead|principal|staff|director|head of|manager|kierownik|dyrektor|architect|ekspert)\b", re.I)
GERMAN = re.compile(r"(deutsch|german (skills|language|c1|b2)|fließend|verhandlungssicher|sehr gute deutschkenntnisse)", re.I)
RELEVANT = re.compile(r"(automat|robot|plc|mechani|mechatron|konstrukt|design engineer|cad|solidworks|fea|cfd|maintenance|utrzymani|"
                      r"python|machine learning|\bml\b|\bai\b|data|llm|qa|test|support|intern|trainee|praktyk|staż|stażyst|junior|student|"
                      r"engineer|inżynier|technik)", re.I)

seen, keys, out = set(), set(), []
for f in sorted((ROOT / "data" / "raw").glob("*.jsonl")):
    for line in f.open():
        r = json.loads(line)
        k = (r["title"] or "").lower().strip(), (r["company"] or "").lower().strip()
        if r["id"] in seen or k in keys: continue
        seen.add(r["id"]); keys.add(k)
        title, text = r["title"] or "", r.get("text") or ""
        if SENIOR.search(title) or not RELEVANT.search(title): continue
        if GERMAN.search(text) or (r["source"] == "arbeitnow" and re.search(r"\b(m/w/d|w/m/d)\b", title) and not re.search(r"[a-z]{3,} engineer", title, re.I)): continue
        out.append(r)
with open(ROOT / "data" / "candidates.jsonl", "w") as fh:
    for r in out: fh.write(json.dumps(r, ensure_ascii=False) + "\n")
from collections import Counter
print(len(out), Counter(r["source"] for r in out))
