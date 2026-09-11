"""Receive unexecuted pointer sources and documentary originals; no code import."""
from pathlib import Path
from hashlib import sha256
import difflib
import json
import os
import re
import shlex

ROOT=Path('/root/autodl-tmp/symbolic_dynamics')
SCOUT=ROOT/'docs/papers211_215_sequence/scouting'
P=SCOUT/'finite_pointer_pilot_preparation01'
HERE=Path(__file__).resolve().parent
keys={};checks=0
def need(ok,label):
    global checks
    checks+=1
    assert ok,label
def read(p):
    p=Path(p);b=p.read_bytes()
    k={'bytes':len(b),'sha256':sha256(b).hexdigest(),'resolved':str(p.resolve()),'symlink':os.readlink(p) if p.is_symlink() else None}
    need(str(p) not in keys or keys[str(p)]==k,'unchanged full read key')
    keys[str(p)]=k
    return b
def obj(p):return json.loads(read(p))
def sums(base,name,count,digest):
    raw=read(base/name);need(sha256(raw).hexdigest()==digest,'bound complete manifest')
    out={}
    for line in raw.decode().splitlines():
        m=re.fullmatch(r'([0-9a-f]{64})  (.+)',line);need(m is not None,'strict sha syntax')
        h,r=m.groups();need(r not in out and r!=name and not Path(r).is_absolute() and '..' not in Path(r).parts,'safe nonself row')
        need(sha256(read(base/r)).hexdigest()==h,'exact payload');out[r]=h
    need(len(out)==count,'complete payload count')
    need({p.relative_to(base).as_posix() for p in base.rglob('*') if p.is_file()}==set(out)|{name} and not any(p.is_symlink() for p in base.rglob('*')),'whole unchanged physical inventory')
    return out
read(__file__)
payload=sums(P,'MANIFEST.sha256',7,'828b135ed4aefbb9d0a1f030e52b48c45c32288ff05d6ea413946bcbcf104a75')
sums(SCOUT/'finite_local_state_fresh_desk','MANIFEST.sha256',5,'d6299f026e02195f145f33f819dcedb27b367c300280b3d3f7255fea1e136ada')
sums(SCOUT/'finite_graph_memory_fresh_desk','SHA256SUMS',5,'34b14033004d6bbc17fdaace81e47e50cea3ddfb27b56316e727fc08425ca503')
pins=obj(P/'SOURCE_INPUT_PINS.json');need(pins['path_base']==str(ROOT) and len(pins['records'])==17,'all seventeen declared source inputs')
need(len({r['path'] for r in pins['records']})==17,'unique input rows')
for r in pins['records']:need(sha256(read(ROOT/r['path'])).hexdigest()==r['sha256'],'whole prepared/original input pin')
params=obj(P/'PARAMETERS.json')
need(params['boxes']==[{'n':1,'state_count':1},{'n':2,'state_count':16},{'n':3,'state_count':243},{'n':4,'state_count':4096}] and params['total_state_count']==4356 and params['allow_box_extension'] is False,'exact bounded parameters without scientific evaluation')
native=obj(P/'NATIVE_PREPARATION_READS.json');rows=native['records']
need(len(rows)==20,'whole native record universe')
comparisons=[];historical=[]
for index,row in enumerate(rows,1):
    need(set(row)<= {'cmd','cwd','result'} and isinstance(row['cmd'],str),'actual cmd/result archive shape')
    argv=shlex.split(row['cmd']);cwd=Path(row.get('cwd',native['default_cwd_for_omitted_entries']))
    result=row['result'];old=result['output'].encode();need(result['exit_code']==(2 if index==2 else 0),'retained exact original exit census')
    current=None;scope='historical navigation observation, not replayed'
    if argv[0]=='sha256sum' and argv[1]!='-c':
        current=b''.join((sha256(read(cwd/name)).hexdigest()+'  '+name+'\n').encode() for name in argv[1:])
    elif argv[0]=='sha256sum':
        lines=read(cwd/argv[2]).decode().splitlines()
        current=''.join(line.split('  ',1)[1]+': OK\n' for line in lines).encode()
    elif argv[0]=='sed':
        need(argv[1]=='-n' and len(argv)==4,'exact sed shape')
        m=re.fullmatch(r'(\d+),(\d+)p',argv[2]);need(m is not None,'exact inclusive ranges')
        a,b=map(int,m.groups());current=b''.join(read(cwd/argv[3]).splitlines(keepends=True)[a-1:b])
    elif argv[0]=='tail':
        need(argv[1:3]==['-n','8'],'exact stated tail scope');current=b''.join(read(cwd/argv[3]).splitlines(keepends=True)[-8:])
    elif argv[0]=='cat':
        current=read(cwd/argv[1])
        if current!=old:
            need(index in (13,14) and argv[1] in ('CLAIM_PREDICATES.md','PLAN.md'),'only disclosed unsealed scope-clarification docs differ')
            diff=list(difflib.unified_diff(old.decode().splitlines(keepends=True),current.decode().splitlines(keepends=True),fromfile='archived pre-seal '+argv[1],tofile='sealed final '+argv[1]))
            need(not any(s.startswith('-') and not s.startswith('---') for s in diff),'only additive pre-seal documentation clarification')
            historical.append({'record':index,'document':argv[1],'archived_full_tool_output_bytes':len(old),'archived_full_tool_output_sha256':sha256(old).hexdigest(),'final_key':keys[str(cwd/argv[1])],'exact_text_diff':''.join(diff),'scope':'Old complete decoded tool text remains in original archive; final additions only disclose unexercised two-genuine-cycle cases, not new scientific predicates or a historical raw-file certificate.'})
            current=None;scope='exact preserved earlier document text plus additive final disclosure'
    else:need(argv[0] in ('rg','ls','df','command','readlink','wc'),'documentary command allowlist, never scientific entry')
    if current is not None:need(current==old,('entire current bytes/archived decoded-output equality',index));scope='current raw bytes equal archived tool-output UTF8 exactly'
    comparisons.append({'record':index,'cmd':row['cmd'],'requested_cwd':str(cwd),'exit_code':result['exit_code'],'archive_output_bytes':len(old),'archive_output_sha256':sha256(old).hexdigest(),'comparison_scope':scope})
need(b''.join(rows[i]['result']['output'].encode() for i in (7,8,9))==read(P/'pointer_pilot.py'),'three complete scientific-source text slices cover entire current source')
need(native['source_input_recheck']=={'comparison':'Exact sha256sum stdout against the earlier saved 17 source/input records in order','same':True,'exit_code':0} and rows[14]['result']['output']==rows[19]['result']['output'],'actual final seventeen-key bracket')
for p,k in list(keys.items()):read(p);need(keys[p]==k,'final full unchanged keys')
result={'status':'PASS_UNEXECUTED_POINTER_SCIENTIFIC_SOURCE_RECEPTION','checks':checks,'read_paths':len(keys),'preparation_payloads':7,'preparation_payload_bytes':sum(keys[str(P/r)]['bytes'] for r in payload),'declared_input_pins':17,'native_records':20,'preserved_preseal_document_additions':len(historical),'source_key':keys[str(P/'pointer_pilot.py')],'parameter_key':keys[str(P/'PARAMETERS.json')],'new_scientific_imports':0,'new_scientific_executions':0,'new_scientific_compilations':0,'runtime_binding_accepted':False,'admitted':False}
for name,v in [('INPUTS.json',keys),('RESULT.json',result),('DOCUMENTARY_RECORD_CHECKS.json',comparisons),('PRESEAL_DOCUMENT_ADDITIONS.json',historical)]:
    with (HERE/name).open('xb') as f:f.write((json.dumps(v,sort_keys=True,indent=2)+'\n').encode())
print(json.dumps(result,sort_keys=True))
