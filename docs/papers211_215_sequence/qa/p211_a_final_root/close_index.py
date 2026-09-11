"""Change-sensitive final acceptance/index closure; no scientific execution."""
from pathlib import Path
from hashlib import sha256
import json
import os
import re

ROOT=Path('/root/autodl-tmp/symbolic_dynamics')
B=ROOT/'docs/papers211_215_sequence'
HERE=Path(__file__).resolve().parent
keys={};checks=0
def need(ok,label):
    global checks
    checks+=1
    assert ok,label
def read(p):
    p=Path(p);data=p.read_bytes()
    k={'sha256':sha256(data).hexdigest(),'bytes':len(data),'resolved':str(p.resolve()),'symlink':os.readlink(p) if p.is_symlink() else None}
    need(str(p) not in keys or keys[str(p)]==k,'stable complete key')
    keys[str(p)]=k
    return data
def obj(p):return json.loads(read(p))
def pin(p,k):
    read(p);p=str(p)
    for name,value in k.items():
        if name=='resolved_path':need(keys[p]['resolved']==value,'resolved original')
        elif name=='mode':need(oct(Path(p).stat().st_mode&0o777)==value,'original mode')
        else:need(keys[p][name]==value,('original key field',p,name))
read(__file__)
for path,n in [(HERE/'run01/READ_INPUTS.json',1688),(B/'scouting/root_reception/transport_network_nonlinear/CLOSURE_INPUTS.json',150)]:
    rows=obj(path);need(len(rows)==n,'complete accepted ledger')
    for p,k in rows.items():pin(p,k)
controls=obj(B/'qa/control_before_a_final/MAPPING.json');need(len(controls)==2,'two exact historical controls')
routes={r['logical_path']:r for r in controls}
for r in controls:pin(r['physical_original'],r['pin'])
old=obj(B/'scouting/root_reception/ordered_algebra_memory/FINAL_INPUTS.json')
need(len(old)==163,'complete previous negative closure key')
for p,k in old.items():
    if p in routes:
        need({name:k[name] for name in ['sha256','bytes']}==routes[p]['pin'],'exact old navigation keys')
        pin(routes[p]['physical_original'],routes[p]['pin'])
    else:pin(p,k)
capture=obj(B/'qa/control_before_a_final/RESULT.json')
tool=obj(B/'qa/control_before_a_final/NATIVE01.json')
need(tool['result']['exit_code']==0 and json.loads(tool['result']['output'])==capture,'actual whole control copy result')
need(capture['mapping']==controls and len(capture['actual_native_commands'])==4,'exact actual cp/cmp census')
for row in capture['actual_native_commands']:
    need(row['exit_code']==0,'actual control native success')
    for which in ['stdout','stderr']:
        data=read(B/'qa/control_before_a_final'/(row['label']+'.'+which+'.raw'))
        need(data==b'' and {'bytes':len(data),'sha256':sha256(data).hexdigest()}==row[which],'actual control raw streams')
docs=[ROOT/'SYMBOLIC_DYNAMICS_STATE.md',B/'PIPELINE_STATE.md',HERE/'RECEPTION.md',B/'scouting/root_reception/TRANSPORT_NETWORK_NONLINEAR_RECEPTION.md']
links=[]
for p in docs:
    body=read(p).decode()
    for target in re.findall(r'\]\(([^)]+)\)',body):
        if target.startswith(('https:','http:','mailto:','#')):continue
        path=(p.parent/target.split('#')[0]).resolve()
        need(path.exists(),('actual local document link',str(p),target));links.append({'origin':str(p),'target':target,'resolved':str(path)})
need('P211_A_ACCEPTED_ROUND1_PENDING' in read(docs[0]).decode() and 'P211_A_ACCEPTED_ROUND1_PENDING' in read(docs[1]).decode(),'new actual phase agrees')
need(not (ROOT/'papers/211-kernel-image-projection-feedback/frozen_round1').exists(),'no unexecuted Round1 claim')
for p,k in list(keys.items()):pin(p,k)
result={'status':'PASS_POST_A_ACCEPTANCE_INDEX_CLOSURE','checks':checks,'read_paths':len(keys),'accepted_A_keys_unchanged':1688,'negative_reception_keys_unchanged':150,'previous_negative_keys_received':163,'exact_physical_navigation_substitutions':controls,'local_links_checked':len(links),'new_scientific_runs':0,'new_builds':0,'new_page_views':0,'retained':1,'completed':0,'open_seats':4,'closed_attempts':41,'round1_pending':True}
for name,v in [('POST_INDEX_KEYS.json',keys),('POST_INDEX_RESULT.json',result),('POST_INDEX_LINKS.json',links)]:
    with (HERE/name).open('xb') as f:f.write((json.dumps(v,sort_keys=True,indent=2)+'\n').encode())
print(json.dumps(result,sort_keys=True))
