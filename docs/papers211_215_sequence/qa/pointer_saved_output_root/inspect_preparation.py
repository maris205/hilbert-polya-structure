"""Root documentary reception of the fully read 548-line author receiver.

No producer/receiver imports, compilation, AST parsing, semantic execution,
or saved-output reads. These checks do not authorize a new pilot.
"""
from hashlib import sha256
import json
import os
from pathlib import Path
import re

ROOT=Path('/root/autodl-tmp/symbolic_dynamics')
QA=ROOT/'docs/papers211_215_sequence/qa'
HERE=QA/'pointer_saved_output_root'
PREP=QA/'finite_pointer_output_receiver_preparation01'
PILOT=ROOT/'docs/papers211_215_sequence/scouting/finite_pointer_pilot_preparation01'
READS={};CHECKS=0

def need(x,label):
    global CHECKS
    CHECKS+=1
    if not x:raise AssertionError(label)

def pin(raw):return {'bytes':len(raw),'sha256':sha256(raw).hexdigest()}

def read(p):
    p=Path(p);need(p.resolve()==p and p.is_file(),('physical file',str(p)))
    raw=p.read_bytes();key=pin(raw)
    need(str(p) not in READS or READS[str(p)]==key,('unchanged complete input',str(p)))
    READS[str(p)]=key
    return raw

def obj(p):return json.loads(read(p))

read(Path(__file__))
manifest=read(PREP/'MANIFEST.sha256')
need(pin(manifest)=={'bytes':869,'sha256':'75809307f24c8b6fc7d3e6874318b864664992960e06bce75b62c739d80904cc'},'exact frozen preparation seal')
rows={}
for line in manifest.decode().splitlines():
    m=re.fullmatch(r'([0-9a-f]{64})  ([^/]+)',line);need(m is not None,'strict flat manifest')
    h,n=m.groups();need(n not in rows and n not in ('.','..','MANIFEST.sha256'),'unique nonself payload')
    need(pin(read(PREP/n))['sha256']==h,('complete payload',n));rows[n]=READS[str(PREP/n)]
need(len(rows)==10 and sum(v['bytes'] for v in rows.values())==130190 and
     {p.name for p in PREP.iterdir()}==set(rows)|{'MANIFEST.sha256'},'whole eleven-file source-only preparation')
pins=obj(PREP/'SOURCE_INPUT_PINS.json')['inputs'];need(len(pins)==10,'complete original control set')
for p,key in pins.items():need(pin(read(p))['sha256']==key['sha256'],('entire source control pin',p))
status=obj(PREP/'PREPARATION_STATUS.json');source=read(PREP/'receive_output.py')
need(pin(source)=={'bytes':28425,'sha256':'24b996e02ce31fe08b89fcd4f260937a9ce67cb16838d8e0350dcdc4d10c559d'}
     and len(source.splitlines())==548,'exact completely read source')
need(status['receiver_source']=={'path':str(PREP/'receive_output.py'),**pin(source),'lines':548}
     and status['saved_stdout_path'] is None and status['binding_path'] is None,'prepared source remains unbound')
need(all(status[k] is False for k in ('binding_created','receiver_imported','receiver_executed','producer_imported_compiled_or_executed',
    'producer_AST_parsed','saved_stdout_opened','canonical_created','peer_check_performed'))
    and status['scientific_helper_calls']==status['scientific_executions']==0,'no fabricated preparation run or peer check')
records=obj(PREP/'NATIVE_DOCUMENTARY_RECORDS.json')['records'];need(len(records)==4,'all selected actual documentary records')
for record in records:
    need(set(record)=={'request','result'} and type(record['result']['exit_code']) is int and record['result']['exit_code']==0
         and 'session_id' not in record['result'] and type(record['result']['output']) is str,'actual settled documentary record shape')
science=read(PILOT/'pointer_pilot.py');lines=science.splitlines(keepends=True)
runtime=read(QA/'pointer_runtime_root/RECEPTION.md')
raw0=records[0]['result']['output'].encode();prefix=b''.join(lines[:210])
need(raw0.startswith(runtime) and raw0.endswith(prefix),'whole actual first source read endpoints')
wcpart=raw0[len(runtime):-len(prefix)].decode().splitlines();names=['pointer_pilot.py','PARAMETERS.json','OUTPUT_SCHEMA.md','CLAIM_PREDICATES.md','PLAN.md']
need(len(wcpart)==6,'complete actual wc rows')
total=0
for line,name in zip(wcpart,names):
    m=re.fullmatch(r'\s*(\d+) (.+)',line);need(m is not None,'exact native wc row')
    size=len(read(PILOT/name).splitlines());need(int(m[1])==size and m[2]==str((PILOT/name).relative_to(ROOT)),'current entire text line census')
    total+=size
need(re.fullmatch(r'\s*'+str(total)+r' total',wcpart[-1]) is not None,'actual total wc')
need(records[1]['result']['output'].encode()==b''.join(lines[210:]),'complete remaining scientific source byte read; no import')
need(records[2]['result']['output'].encode()==b''.join(read(PILOT/n) for n in ['OUTPUT_SCHEMA.md','CLAIM_PREDICATES.md','PLAN.md','PARAMETERS.json']),
     'complete four schema/predicate/plan/parameter native bytes')
requests=[
    "sed -n '1,200p' docs/papers211_215_sequence/qa/pointer_runtime_root/RECEPTION.md\nwc -l docs/papers211_215_sequence/scouting/finite_pointer_pilot_preparation01/{pointer_pilot.py,PARAMETERS.json,OUTPUT_SCHEMA.md,CLAIM_PREDICATES.md,PLAN.md}\nsed -n '1,210p' docs/papers211_215_sequence/scouting/finite_pointer_pilot_preparation01/pointer_pilot.py",
    "sed -n '211,420p' docs/papers211_215_sequence/scouting/finite_pointer_pilot_preparation01/pointer_pilot.py\nsed -n '421,650p' docs/papers211_215_sequence/scouting/finite_pointer_pilot_preparation01/pointer_pilot.py",
    "sed -n '1,200p' docs/papers211_215_sequence/scouting/finite_pointer_pilot_preparation01/OUTPUT_SCHEMA.md\nsed -n '1,150p' docs/papers211_215_sequence/scouting/finite_pointer_pilot_preparation01/CLAIM_PREDICATES.md\nsed -n '1,150p' docs/papers211_215_sequence/scouting/finite_pointer_pilot_preparation01/PLAN.md\nsed -n '1,60p' docs/papers211_215_sequence/scouting/finite_pointer_pilot_preparation01/PARAMETERS.json']
for i,cmd in enumerate(requests):need(records[i]['request']=={'cmd':cmd,'max_output_tokens':[14000,15500,14500][i]},'actual complete source request')
doc=obj(PREP/'DOCUMENTARY_CHECK.json');need(json.loads(records[3]['result']['output'])==doc,'actual complete documentary result equality')
need(doc['checks']==30 and doc['syntax_AST_nodes']==6518 and doc['inputs_before']==doc['inputs_after']
     and set(doc['inputs_before'])==set(pins),'entire original static result key')
for p,v in doc['inputs_before'].items():need(pin(read(p))==v,'complete original static input bytes')
cache=PREP/'never_created_documentary_cache'
need(records[3]['request']=={'cmd':'/usr/bin/env -i PATH=/usr/bin:/bin LANG=C.UTF-8 LC_ALL=C.UTF-8 TZ=UTC /usr/bin/python3.10 -I -S -B -X pycache_prefix='+str(cache)+' '+str(PREP/'check_preparation.py'),
    'workdir':str(ROOT),'max_output_tokens':6500} and not os.path.lexists(cache),'actual source-only syntax check context, not receiver execution')
need(doc['receiver_pin']==pin(source) and doc['receiver_lines']==548 and doc['receiver_imports_or_executions']==doc['receiver_semantic_function_calls']==
     doc['producer_parses_compilations_imports_or_executions']==doc['saved_output_reads']==doc['scientific_executions']==0,'source-only actual scope')
for p,v in dict(READS).items():need(pin(read(p))==v,('whole before/after original byte set',p))
result={'status':'PASS_ROOT_COMPLETE_SAVED_OUTPUT_RECEIVER_SOURCE_RECEPTION','checks':CHECKS,'read_paths':len(READS),'payloads':10,
        'original_pins':10,'receiver_source':pin(source),'receiver_lines':548,'actual_documentary_records':4,
        'source_and_contract_fully_read_by_root':True,'receiver_executions':0,'saved_output_reads':0,'producer_executions':0,
        'binding':'PENDING_FULL_ACTUAL_RUNTIME_RECEPTION','admission':'NOT_DECIDED','external':'HOLD_EXTERNAL','inputs':READS}
with (HERE/'PREPARATION_RESULT.json').open('x') as stream:json.dump(result,stream,indent=2,sort_keys=True);stream.write('\n')
print(json.dumps({k:v for k,v in result.items() if k!='inputs'},sort_keys=True))
