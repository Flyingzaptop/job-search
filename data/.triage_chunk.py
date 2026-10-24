import json,sys
start=int(sys.argv[1]); decs=[]
for line in sys.stdin.read().strip().splitlines():
    d,_,r=line.partition('|'); decs.append((d.strip(),r.strip()))
lines=open('/home/user/job-search/data/triage_in_0.jsonl',encoding='utf-8').read().splitlines()
chunk=lines[start-1:start-1+len(decs)]
assert len(chunk)==len(decs), (len(chunk),len(decs))
with open('/home/user/job-search/data/triage_out_0.jsonl','a',encoding='utf-8') as f:
    for l,(d,r) in zip(chunk,decs):
        j=json.loads(l)
        f.write(json.dumps({"id":j["id"],"triage":d,"reason":r},ensure_ascii=False)+"\n")
print("wrote",len(decs))
