"""Pull job listings from keyed APIs into data/raw/*.jsonl (normalized fields). Keys come from .env."""
import json, os, sys, time, urllib.parse, urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "data" / "raw"
for line in ((ROOT / ".env").read_text().splitlines() if (ROOT / ".env").exists() else []):  # else keys come from environment secrets
    if "=" in line:
        k, v = line.split("=", 1); os.environ.setdefault(k, v)

def http(url, data=None, headers=None, method=None):
    req = urllib.request.Request(url, data=data, headers=headers or {}, method=method)
    with urllib.request.urlopen(req, timeout=120) as r:
        return json.loads(r.read())

RUN = os.environ.get("RUN_TAG", "")  # dated output so earlier pulls are kept

def save(name, rows):
    with open(RAW / f"{name}{RUN}.jsonl", "w") as f:
        for r in rows: f.write(json.dumps(r, ensure_ascii=False) + "\n")
    print(f"{name}: {len(rows)}")

def jooble():
    key = os.environ["JOOBLE_API_KEY"]
    queries = [
        ("automation engineer", "Poland"), ("PLC programmer", "Poland"), ("robotics engineer", "Poland"),
        ("mechanical engineer intern", "Poland"), ("design engineer junior", "Poland"),
        ("junior python developer remote", "remote"), ("machine learning intern remote", "remote"),
        ("AI automation engineer remote", "remote"), ("junior mechanical design engineer remote", "remote"),
        ("CAD designer remote", "remote"),
    ]
    rows = []
    for kw, loc in queries:
        body = json.dumps({"keywords": kw, "location": loc, "ResultOnPage": "100"}).encode()
        d = http(f"https://jooble.org/api/{key}", body, {"Content-Type": "application/json"})
        for j in d.get("jobs", []):
            rows.append({"source": "jooble", "id": f"jooble:{j['id']}", "query": kw, "title": j["title"],
                         "company": j.get("company"), "location": j.get("location"), "type": j.get("type"),
                         "salary": j.get("salary"), "posted": (j.get("updated") or "")[:10],
                         "url": j["link"], "text": j.get("snippet", "")})
    save("jooble", rows)

def fantastic():
    key = os.environ["FANTASTIC_JOBS_API_KEY"]
    titles = ('"Automation" OR "Robotics" OR "PLC" OR "Mechanical" OR "Design Engineer" OR "Intern" OR '
              '"Trainee" OR "Python" OR "Machine Learning" OR "Junior"')
    q = urllib.parse.urlencode({"time_frame": "7d", "limit": "100", "title": titles, "location": '"Poland"'})
    d = http(f"https://data.fantastic.jobs/v1/active-ats?{q}", headers={"Authorization": f"Bearer {key}"})
    rows = [{"source": "fantastic", "id": f"fantastic:{j['id']}", "title": j["title"], "company": j.get("organization"),
             "location": ", ".join(j.get("locations_alt") or []), "type": j.get("location_type"),
             "salary": j.get("salary"), "posted": (j.get("date_posted") or "")[:10], "url": j["url"],
             "text": " | ".join(f"{k[3:]}: {j[k]}" for k in ("ai_experience_level", "ai_work_arrangement",
             "ai_work_arrangement_office_days", "ai_job_language", "ai_key_skills", "ai_requirements_summary",
             "ai_core_responsibilities") if j.get(k))[:4000]} for j in d]
    save("fantastic", rows)

def apify_linkedin(urls=None, out="linkedin", cap="1.5"):
    tok = os.environ["APIFY_TOKEN"]
    base = "https://www.linkedin.com/jobs/search/?"
    def u(kw, loc, extra): return base + urllib.parse.urlencode({"keywords": kw, "location": loc, **extra})
    entry = {"f_E": "1,2"}  # internship, entry level
    urls = urls or [
        u('automation engineer OR PLC OR robotics OR automatyk', "Wrocław, Dolnośląskie, Poland", {**entry, "distance": "50"}),
        u('mechanical engineer OR design engineer OR konstruktor OR CAD', "Wrocław, Dolnośląskie, Poland", {**entry, "distance": "50"}),
        u('python OR machine learning OR AI OR data', "Wrocław, Dolnośląskie, Poland", {**entry, "distance": "25"}),
        u('automation engineer OR mechanical engineer OR robotics', "Poland", {**entry, "f_WT": "2,3"}),
        u('mechanical design OR CAD OR FEA OR CFD', "Worldwide", {**entry, "f_WT": "2"}),
        u('python OR machine learning OR AI engineer', "European Union", {**entry, "f_WT": "2"}),
    ]
    inp = {"urls": urls, "datePosted": "anyTime", "scrapeCompany": False, "limitPerSource": 100,
           "splitByLocation": False, "autoConvertToAiSearch": False}
    run = http(f"https://api.apify.com/v2/acts/curious_coder~linkedin-jobs-scraper/runs?token={tok}&maxTotalChargeUsd={cap}",
               json.dumps(inp).encode(), {"Content-Type": "application/json"})["data"]
    while run["status"] in ("READY", "RUNNING"):
        time.sleep(15)
        run = http(f"https://api.apify.com/v2/actor-runs/{run['id']}?token={tok}")["data"]
    print("apify run", run["status"], run.get("usageTotalUsd"))
    items = http(f"https://api.apify.com/v2/datasets/{run['defaultDatasetId']}/items?token={tok}&clean=1")
    rows = [{"source": "linkedin", "id": f"linkedin:{j.get('id')}", "title": j.get("title"),
             "company": j.get("companyName"), "location": j.get("location"),
             "type": j.get("workplaceType") or j.get("employmentType"), "salary": j.get("salary") or j.get("salaryInfo"),
             "posted": str(j.get("postedAt") or "")[:10], "url": j.get("link") or j.get("applyUrl"),
             "text": (j.get("descriptionText") or j.get("description") or "")[:4000],
             "level": j.get("seniorityLevel"), "applicants": j.get("applicantsCount")} for j in items]
    save(out, rows)

def arbeitnow():
    rows = []
    for p in range(1, 6):
        d = http(f"https://www.arbeitnow.com/api/job-board-api?page={p}")
        for j in d["data"]:
            rows.append({"source": "arbeitnow", "id": f"arbeitnow:{j['slug']}", "title": j["title"],
                         "company": j["company_name"], "location": j["location"],
                         "type": "remote" if j.get("remote") else ",".join(j.get("job_types", [])),
                         "posted": time.strftime("%Y-%m-%d", time.gmtime(j["created_at"])), "url": j["url"],
                         "text": j["description"][:4000]})
    save("arbeitnow", rows)

def remotive():
    d = http("https://remotive.com/api/remote-jobs")
    rows = [{"source": "remotive", "id": f"remotive:{j['id']}", "title": j["title"], "company": j["company_name"],
             "location": j.get("candidate_required_location"), "type": "remote", "salary": j.get("salary"),
             "posted": j["publication_date"][:10], "url": j["url"], "text": j["description"][:4000]}
            for j in d["jobs"]]
    save("remotive", rows)

def apify_linkedin2():
    """Round 2: many narrow local queries (round 1 showed local LinkedIn is the best source)."""
    base = "https://www.linkedin.com/jobs/search/?"
    loc = "Wrocław, Dolnośląskie, Poland"
    def u(kw, dist="50", extra=None):
        return base + urllib.parse.urlencode({"keywords": kw, "location": loc, "distance": dist, "f_E": "1,2", **(extra or {})})
    urls = [
        u("staż inżynier OR praktyki techniczne OR internship engineering"),
        u("R&D engineer OR inżynier R&D OR product development"),
        u("test engineer OR validation engineer OR inżynier testów"),
        u("mechatronik OR mechatronics OR robot programmer OR programista robotów"),
        u("process engineer OR inżynier procesu OR technolog OR manufacturing engineer"),
        u("FEA OR CAE OR simulation engineer OR symulacje"),
        u("junior python OR data analyst OR machine learning intern"),
        u("PLM OR CAD support OR engineering tools OR application engineer"),
        u("automation engineer OR mechanical engineer", "100", {"f_WT": "2,3"}),
    ]
    apify_linkedin(urls, out="linkedin2", cap="1.0")


import re, html as _html
from concurrent.futures import ThreadPoolExecutor
ENTRY = re.compile(r"junior|\bjr\b|intern|trainee|stażyst|\bstaż|praktyk|entry|graduate|młodsz|working student|werkstudent|apprentice|associate|early career|new grad", re.I)
UA = {"User-Agent": "Mozilla/5.0"}
def _txt(s): return re.sub(r"\s+", " ", _html.unescape(re.sub(r"<[^>]+>", " ", s or ""))).strip()

def justjoin():
    """justjoin.it open candidate API: all junior/intern offers in Poland (list + detail body for the text)."""
    items, off = [], 0
    while True:
        d = http(f"https://justjoin.it/api/candidate-api/offers?experienceLevels=junior&experienceLevels=intern&from={off}", headers=UA)
        items += d["data"]
        nxt = (d.get("meta") or {}).get("next", {}).get("cursor")
        if not nxt or not d["data"] or off > 2000: break
        off = nxt
    def row(j):
        try: body = http(f"https://justjoin.it/api/candidate-api/offers/{j['slug']}", headers=UA).get("body", "")
        except Exception: body = ""
        sal = "; ".join(f"{e.get('type')} {e.get('from')}-{e.get('to')} {e.get('currency')}" for e in j.get("employmentTypes", []) if e.get("from"))
        return {"source": "justjoin", "id": f"justjoin:{j['slug']}", "title": j["title"], "company": j["companyName"],
                "location": ", ".join(sorted({l.get("city") or "" for l in j.get("locations", [])}) or [j.get("city") or ""]),
                "type": f"{j.get('workplaceType')}, {j.get('workingTime')}", "salary": sal, "posted": (j.get("publishedAt") or "")[:10],
                "url": f"https://justjoin.it/job-offer/{j['slug']}", "text": f"{j.get('workplaceType')} | {j.get('workingTime')} | {j.get('experienceLevel')} | " + _txt(body)[:3800]}
    with ThreadPoolExecutor(8) as ex: rows = list(ex.map(row, items))
    save("justjoin", rows)

def himalayas():
    rows, seen = [], set()
    def get(a):
        q, sen, page = a
        try: return http(f"https://himalayas.app/jobs/api/search?q={urllib.parse.quote(q)}&seniority={sen}&sort=recent&page={page+1}", headers=UA)
        except Exception: return {}
    qs = [(q, sen, pg) for q in ["python", "automation", "machine learning", "QA", "support engineer", "data analyst", "mechanical", "robotics", "AI", "IT support", "intern"] for sen in ("Entry-level", "Intern") for pg in range(2)]
    with ThreadPoolExecutor(6) as ex: results = list(ex.map(get, qs))
    if True:
        if True:
            for d in results:
                for j in d.get("jobs", []):
                    k = j.get("guid") or j.get("applicationLink") or j["title"] + j["companyName"]
                    if k in seen: continue
                    seen.add(k)
                    rows.append({"source": "himalayas", "id": f"himalayas:{k}", "title": j["title"], "company": j["companyName"],
                                 "location": ", ".join(j.get("locationRestrictions") or ["Worldwide"]), "type": "remote", "salary": j.get("minSalary"),
                                 "posted": time.strftime("%Y-%m-%d", time.gmtime(j["pubDate"])) if isinstance(j.get("pubDate"), (int, float)) else "",
                                 "url": j.get("applicationLink") or j.get("guid"), "text": f"remote | {j.get('seniority')} | tz {j.get('timezoneRestrictions')} | " + _txt(j.get("description") or j.get("excerpt"))[:3800]})
    save("himalayas", rows)

def jobicy():
    rows, seen = [], set()
    for tag in ["python", "automation", "machine-learning", "support", "qa", "data", "engineering", "ai"]:
        for geo in ("europe", "poland", "anywhere"):
            try: d = http(f"https://jobicy.com/api/v2/remote-jobs?count=50&tag={tag}&geo={geo}", headers=UA)
            except Exception: continue
            for j in d.get("jobs", []):
                if j["id"] in seen or not (ENTRY.search(j["jobTitle"]) or str(j.get("jobLevel", "")).lower() in ("junior", "entry", "any")): continue
                seen.add(j["id"])
                rows.append({"source": "jobicy", "id": f"jobicy:{j['id']}", "title": j["jobTitle"], "company": j["companyName"], "location": j.get("jobGeo"),
                             "type": "remote", "posted": (j.get("pubDate") or "")[:10], "url": j["url"],
                             "text": f"remote | {j.get('jobLevel')} | " + _txt(j.get("jobDescription") or j.get("jobExcerpt"))[:3800]})
    save("jobicy", rows)

def remoteok():
    d = http("https://remoteok.com/api", headers=UA)[1:]
    rows = [{"source": "remoteok", "id": f"remoteok:{j['id']}", "title": j["position"], "company": j["company"], "location": j.get("location") or "Worldwide",
             "type": "remote", "salary": j.get("salary_min"), "posted": (j.get("date") or "")[:10], "url": j["url"],
             "text": "remote | " + ",".join(j.get("tags") or []) + " | " + _txt(j.get("description"))[:3800]} for j in d if ENTRY.search(j.get("position", ""))]
    save("remoteok", rows)

def smartrecruiters(companies=("BoschGroup", "ServiceNow"), countries=("pl", "de", "cz")):
    rows = []
    for c in companies:
        for cc in countries:
            off = 0
            while True:
                d = http(f"https://api.smartrecruiters.com/v1/companies/{c}/postings?country={cc}&limit=100&offset={off}", headers=UA)
                for j in d.get("content", []):
                    loc = j.get("location", {})
                    lvl = f"{j.get('experienceLevel', {}).get('id')} {j.get('typeOfEmployment', {}).get('id')}"
                    if not (ENTRY.search(j["name"]) or re.search(r"entry|intern|trainee|student", lvl, re.I)): continue
                    try: det = http(f"https://api.smartrecruiters.com/v1/companies/{c}/postings/{j['id']}", headers=UA)["jobAd"]["sections"]
                    except Exception: det = {}
                    body = " ".join(_txt(s.get("text")) for s in det.values() if isinstance(s, dict))
                    rows.append({"source": "smartrecruiters", "id": f"smartrecruiters:{j['id']}", "title": j["name"], "company": j["company"]["name"],
                                 "location": loc.get("fullLocation"), "type": "remote" if loc.get("remote") else ("hybrid" if loc.get("hybrid") else "onsite"),
                                 "posted": (j.get("releasedDate") or "")[:10], "url": f"https://jobs.smartrecruiters.com/{c}/{j['id']}",
                                 "text": f"{j.get('typeOfEmployment', {}).get('label')} | {j.get('experienceLevel', {}).get('label')} | " + body[:3800]})
                off += 100
                if off >= d.get("totalFound", 0): break
    save("smartrecruiters", rows)

def greenhouse_lever():
    """Remote-first companies' own boards (Greenhouse / Lever); only entry-level titles are kept."""
    cfg = json.loads((ROOT / "tools" / "search" / "ats_boards.json").read_text(encoding="utf-8"))
    rows = []
    for s in cfg["greenhouse"]:
        try: d = http(f"https://boards-api.greenhouse.io/v1/boards/{s}/jobs?content=true", headers=UA)
        except Exception: continue
        for j in d.get("jobs", []):
            if not ENTRY.search(j["title"]): continue
            rows.append({"source": "greenhouse", "id": f"greenhouse:{s}:{j['id']}", "title": j["title"], "company": s, "location": (j.get("location") or {}).get("name"),
                         "posted": (j.get("updated_at") or "")[:10], "url": j["absolute_url"], "text": _txt(j.get("content"))[:4000]})
    for s in cfg["lever"]:
        try: d = http(f"https://api.lever.co/v0/postings/{s}?mode=json", headers=UA)
        except Exception: continue
        for j in d:
            if not ENTRY.search(j["text"]): continue
            c = j.get("categories", {})
            rows.append({"source": "lever", "id": f"lever:{s}:{j['id']}", "title": j["text"], "company": s, "location": c.get("location"), "type": j.get("workplaceType"),
                         "posted": time.strftime("%Y-%m-%d", time.gmtime(j["createdAt"] / 1000)), "url": j["hostedUrl"], "text": (j.get("descriptionPlain") or "")[:4000]})
    save("ats_boards", rows)

if __name__ == "__main__":
    for name in sys.argv[1:] or ["jooble", "fantastic", "arbeitnow", "remotive", "apify_linkedin"]:
        try: globals()[name]()
        except Exception as e: print(f"{name}: FAILED {e!r}")
