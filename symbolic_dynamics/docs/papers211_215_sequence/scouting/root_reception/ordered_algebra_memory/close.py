"""Post-index documentary closure; no scientific program is executed."""
from pathlib import Path
from hashlib import sha256
import json
import re

ROOT=Path('/root/autodl-tmp/symbolic_dynamics')
HERE=Path(__file__).resolve().parent
key={}; checks=0
def need(ok,label):
    global checks
    checks+=1
    assert ok,label
def pin(raw):return {'bytes':len(raw),'sha256':sha256(raw).hexdigest()}
def read(p):
    p=Path(p).resolve();raw=p.read_bytes();v=pin(raw)
    need(str(p) not in key or key[str(p)]==v,'stable close reads');key[str(p)]=v
    return raw
def obj(p):return json.loads(read(p))
read(__file__)
old=obj(HERE/'INPUTS.json')
need(len(old)==67,'full previous input population')
for path,v in old.items():need(pin(read(path))==v,('unchanged accepted original',path))
result=obj(HERE/'RESULT.json');correction=obj(HERE/'RESULT_SCOPE_CORRECTION.json')
need(pin(read(HERE/'RESULT.json'))['sha256']==correction['original_result_sha256'],'additive field correction binds original')
need(correction['closed_literal_attempt_delta']==1 and correction['new_admitted_candidates']==0,'count semantics')
native=obj(HERE/'NATIVE03.json')
need(native['result']['exit_code']==0 and json.loads(native['result']['output'])==result,'actual complete successful stdout')
for name in ['NATIVE01.json','NATIVE02.json']:
    need(obj(HERE/name)['result']['exit_code']==1,'failed receiver retained')
control=HERE/'control_before_reception'
mapping=obj(control/'MAPPING.json');need(len(mapping)==2,'two physical historical controls')
cr=obj(control/'RESULT.json')
need(cr['mapping']==mapping and len(cr['actual_native_commands'])==4,'full recorded control map')
need(json.loads(obj(control/'NATIVE01.json')['result']['output'])==cr,'actual physical capture stdout')
for row in mapping:need(pin(read(row['physical_original']))==row['pin'],'exact prior navigation bytes')
for r in cr['actual_native_commands']:
    label=r['label'];need(obj(control/(label+'.ATTEMPT.json'))=={k:v for k,v in r.items() if k not in ['ended_epoch','exit_code','stdout','stderr']},'actual request')
    need(obj(control/(label+'.RECEIPT.json'))==r and r['exit_code']==0,'actual receipt')
    for stream in ['stdout','stderr']:
        raw=read(control/(label+'.'+stream+'.raw'));need(raw==b'' and pin(raw)==r[stream],'complete raw stream')
links=0
for path in [HERE.parent/'ORDERED_ALGEBRA_MEMORY_RECEPTION.md',ROOT/'SYMBOLIC_DYNAMICS_STATE.md',ROOT/'docs/papers211_215_sequence/PIPELINE_STATE.md']:
    body=read(path).decode()
    for href in re.findall(r'\]\(([^\n)]+)\)',body):
        if '://' in href or href.startswith('#'):continue
        target=(path.parent/href.split('#')[0]).resolve();need(target.is_file(),('current complete link',str(path),href));links+=1
    if path.name=='PIPELINE_STATE.md':need('Closed literal attempts: 41.' in body,'current exact count')
    if path.name=='SYMBOLIC_DYNAMICS_STATE.md':need('累计41关闭' in body,'root exact count')
paper=ROOT/'papers/211-kernel-image-projection-feedback';frozen=paper/'frozen_round0'
lines=read(frozen/'SHA256SUMS').decode().splitlines();need(len(lines)==32,'accepted P211 freeze population')
for line in lines:
    h,rel=line.split('  ',1);a=read(frozen/rel);b=read(paper/rel)
    need(a==b and sha256(a).hexdigest()==h,'unchanged full live/frozen author bytes')
for p,v in list(key.items()):need(pin(Path(p).read_bytes())==v,'closing current key')
out={'status':'PASS_POST_INDEX_NEGATIVE_RECEPTION_CLOSURE','checks':checks,'key_paths':len(key),'accepted_original_key_count':67,'author_live_frozen_pairs':32,'current_document_links':links,'physical_prior_controls':2,'closed_attempts':41,'retained':1,'completed':0,'open_seats':4,'scientific_executions':0}
for name,value in [('FINAL_INPUTS.json',key),('FINAL_RESULT.json',out)]:
    with (HERE/name).open('xb') as f:f.write((json.dumps(value,sort_keys=True,indent=2)+'\n').encode())
print(json.dumps(out,sort_keys=True))
