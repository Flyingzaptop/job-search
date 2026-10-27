"""Build a designed, ATS-safe CV PDF (single reading column, real text) from cv/content2/<name>.json via headless Chromium.

Content: {"file": "...pdf", "lang": "en|pl", "name", "role", "contacts": [..], "summary": "...",
          "projects": [{"name", "sub", "stack", "bullets": [..], "link"}], "experience": [{"title", "org", "dates", "bullets": [..]}],
          "skills": [{"label", "items"}], "education": [{"title", "dates", "text"}], "extras": [{"label", "text"}],
          "labels": {"summary": ..., "projects": ..., ...}, "max_pages": 2, "must_contain": [], "must_not_contain": []}
Usage: python3 tools/cv/build_cv2.py cv/content2/IT_EN.json [...]
"""
import json, os, subprocess, sys
from html import escape as e
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "cv" / "out2"
EMAIL = "r3dflzp.ns@gmail.com"
INTER = Path("/usr/share/fonts/opentype/inter")
LABELS = {
    "en": {"summary": "Profile", "projects": "Selected projects", "experience": "Experience", "skills": "Skills", "education": "Education", "extras": "Languages and availability"},
    "pl": {"summary": "Profil", "projects": "Wybrane projekty", "experience": "Doświadczenie", "skills": "Umiejętności", "education": "Wykształcenie", "extras": "Języki i dostępność"},
}
CSS = f"""
@font-face {{ font-family: CVInter; src: url('file://{INTER}/Inter-Regular.otf'); font-weight: 400; }}
@font-face {{ font-family: CVInter; src: url('file://{INTER}/Inter-Medium.otf'); font-weight: 500; }}
@font-face {{ font-family: CVInter; src: url('file://{INTER}/Inter-SemiBold.otf'); font-weight: 600; }}
@font-face {{ font-family: CVInter; src: url('file://{INTER}/Inter-Bold.otf'); font-weight: 700; }}
@font-face {{ font-family: CVInter; src: url('file:///usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf'); font-weight: 400; unicode-range: U+0021-002F, U+003A-0040, U+005B-0060, U+007B-007E, U+2013, U+2014; }}
@font-face {{ font-family: CVInter; src: url('file:///usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf'); font-weight: 500; unicode-range: U+0021-002F, U+003A-0040, U+005B-0060, U+007B-007E, U+2013, U+2014; }}
@font-face {{ font-family: CVInter; src: url('file:///usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf'); font-weight: 600; unicode-range: U+0021-002F, U+003A-0040, U+005B-0060, U+007B-007E, U+2013, U+2014; }}
@font-face {{ font-family: CVInter; src: url('file:///usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf'); font-weight: 700; unicode-range: U+0021-002F, U+003A-0040, U+005B-0060, U+007B-007E, U+2013, U+2014; }}
@page {{ size: A4; margin: 11mm 0 9mm; }}
@page :first {{ margin-top: 0; }}
* {{ box-sizing: border-box; }}
body {{ font-feature-settings: 'calt' 0, 'ccmp' 0, 'liga' 0; font-variant-ligatures: none; margin: 0; font: 400 8.7pt/1.36 CVInter, Arial, sans-serif; color: #17222d; }}
header {{ background: #12263a; color: #fff; padding: 7mm 15mm 5mm; }}
h1 {{ margin: 0; font: 700 23pt/1.05 CVInter, Arial, sans-serif; letter-spacing: -.01em; }}
.role {{ margin: 3mm 0 0; font-weight: 500; font-size: 10.6pt; color: #8fd3e8; }}
.contacts {{ margin: 3.2mm 0 0; font-size: 8.6pt; color: #d6e2ec; }}
.contacts span + span::before {{ content: "  |  "; color: #5f7a91; }}
main {{ padding: 3mm 15mm 0; }}
section {{ margin-top: 3.2mm; }}
h2 {{ margin: 0 0 2mm; font: 700 8.4pt/1.2 CVInter, Arial, sans-serif; letter-spacing: .12em; text-transform: uppercase; color: #0d6a8c; border-bottom: 1.2px solid #c9d8e3; padding-bottom: 1.2mm; }}
.summary {{ font-size: 9.6pt; line-height: 1.5; margin: 0; }}
.item {{ margin-bottom: 2.6mm; break-inside: avoid; }}
.row {{ display: flex; justify-content: space-between; gap: 6mm; align-items: baseline; }}
.t {{ font-weight: 650; font-weight: 600; font-size: 10pt; }}
.sub {{ color: #4b5b69; }}
.d {{ color: #4b5b69; white-space: nowrap; font-size: 8.6pt; }}
.stack {{ margin: .6mm 0 1.2mm; font-size: 8.4pt; color: #0d6a8c; font-weight: 500; }}
ul {{ margin: 0; padding-left: 4.2mm; }}
li {{ margin: 0 0 .9mm; padding-left: .5mm; }}
li::marker {{ color: #0d6a8c; }}
.link {{ font-size: 8.4pt; color: #4b5b69; margin-top: .6mm; }}
.sk {{ display: grid; grid-template-columns: 30mm 1fr; gap: 1.4mm 4mm; }}
.sk b {{ font-weight: 600; }}
"""

def build(path):
    s = json.loads(Path(path).read_text(encoding="utf-8"))
    L = {**LABELS[s.get("lang", "en")], **s.get("labels", {})}
    h = [f"<!doctype html><html lang='{s.get('lang', 'en')}'><head><meta charset='utf-8'><title>{e(s['name'])} - CV</title><style>{CSS}</style></head><body>"]
    h.append(f"<header><h1>{e(s['name'])}</h1><p class='role'>{e(s['role'])}</p><p class='contacts'>" + "".join(f"<span>{e(c)}</span>" for c in s["contacts"]) + "</p></header><main>")
    h.append(f"<section><h2>{e(L['summary'])}</h2><p class='summary'>{e(s['summary'])}</p></section>")
    if s.get("projects"):
        h.append(f"<section><h2>{e(L['projects'])}</h2>")
        for p in s["projects"]:
            h.append(f"<div class='item'><div class='row'><span class='t'>{e(p['name'])}" + (f" <span class='sub'>| {e(p['sub'])}</span>" if p.get("sub") else "") + "</span>" + (f"<span class='d'>{e(p['link'])}</span>" if p.get("link") else "") + "</div>")
            if p.get("stack"): h.append(f"<div class='stack'>{e(p['stack'])}</div>")
            h.append("<ul>" + "".join(f"<li>{e(b)}</li>" for b in p["bullets"]) + "</ul>")
            h.append("</div>")
        h.append("</section>")
    if s.get("experience"):
        h.append(f"<section><h2>{e(L['experience'])}</h2>")
        for x in s["experience"]:
            h.append(f"<div class='item'><div class='row'><span class='t'>{e(x['title'])} <span class='sub'>| {e(x['org'])}</span></span><span class='d'>{e(x['dates'])}</span></div><ul>" + "".join(f"<li>{e(b)}</li>" for b in x["bullets"]) + "</ul></div>")
        h.append("</section>")
    if s.get("skills"):
        h.append(f"<section><h2>{e(L['skills'])}</h2><div class='sk'>" + "".join(f"<b>{e(k['label'])}</b><span>{e(k['items'])}</span>" for k in s["skills"]) + "</div></section>")
    if s.get("education"):
        h.append(f"<section><h2>{e(L['education'])}</h2>")
        for x in s["education"]:
            h.append(f"<div class='item'><div class='row'><span class='t'>{e(x['title'])}</span><span class='d'>{e(x['dates'])}</span></div><div>{e(x['text'])}</div></div>")
        h.append("</section>")
    if s.get("extras"):
        h.append(f"<section><h2>{e(L['extras'])}</h2><div class='sk'>" + "".join(f"<b>{e(k['label'])}</b><span>{e(k['text'])}</span>" for k in s["extras"]) + "</div></section>")
    h.append("</main></body></html>")
    OUT.mkdir(exist_ok=True)
    html_path = OUT / (Path(s["file"]).stem + ".html"); html_path.write_text("".join(h), encoding="utf-8")
    pdf = OUT / s["file"]
    js = f"""const {{ chromium }} = require('playwright'); (async()=>{{ const b=await chromium.launch(); const p=await b.newPage();
      await p.goto('file://{html_path}'); await p.evaluate(()=>document.fonts.ready);
      await p.pdf({{path:'{pdf}', format:'A4', printBackground:true, preferCSSPageSize:true}}); await b.close(); }})();"""
    subprocess.run(["node", "-e", js], check=True, env={**os.environ, "NODE_PATH": subprocess.check_output(["npm", "root", "-g"], text=True).strip()})
    import pdfplumber, pypdfium2 as pdfium
    with pdfplumber.open(pdf) as d:
        pages, text = len(d.pages), " ".join(p.extract_text() or "" for p in d.pages)
    problems = [f"pages {pages} > {s.get('max_pages', 2)}"] if pages > s.get("max_pages", 2) else []
    problems += [f"missing: {t}" for t in [EMAIL, *s.get("must_contain", [])] if t not in text]
    problems += [f"forbidden: {t}" for t in s.get("must_not_contain", []) if t in text]
    for i, pg in enumerate(pdfium.PdfDocument(str(pdf))):
        pg.render(scale=1.5).to_pil().save(OUT / f"{pdf.stem}-p{i + 1}.png")
    print(f"{pdf.name}: {pages} page(s)", "OK" if not problems else "PROBLEMS: " + "; ".join(problems))
    return not problems

if __name__ == "__main__":
    sys.exit(0 if all([build(p) for p in sys.argv[1:]]) else 1)
