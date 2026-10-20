"""Pull job listings from keyed APIs into data/raw/*.jsonl (normalized fields). Keys come from .env."""
import json, os, sys, time, urllib.parse, urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "data" / "raw"
for line in (ROOT / ".env").read_text().splitlines():
    if "=" in line:
        k, v = line.split("=", 1); os.environ.setdefault(k, v)

def http(url, data=None, headers=None, method=None):
    req = urllib.request.Request(url, data=data, headers=headers or {}, method=method)
    with urllib.request.urlopen(req, timeout=120) as r:
        return json.loads(r.read())

def save(name, rows):
    with open(RAW / f"{name}.jsonl", "w") as f:
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
    q = urllib.parse.urlencode({"time_frame": "7d", "limit": "200", "title": titles, "location": '"Poland"'})
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
    apify_linkedin(urls, out="linkedin2", cap="1.9")

if __name__ == "__main__":
    for name in sys.argv[1:] or ["jooble", "fantastic", "arbeitnow", "remotive", "apify_linkedin"]:
        try: globals()[name]()
        except Exception as e: print(f"{name}: FAILED {e!r}")
