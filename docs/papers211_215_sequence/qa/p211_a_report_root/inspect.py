"""Receive A's immutable report-stage originals; no scientific execution."""
from pathlib import Path
from hashlib import sha256
import json
import os
import re
import shlex
ROOT=Path('/root/autodl-tmp/symbolic_dynamics')
QA=ROOT/'docs/papers211_215_sequence/qa'
A=ROOT/'docs/papers211_215_sequence/reviews/p211_a'
HERE=Path(__file__).resolve().parent
keys={};checks=0
def need(ok,label):
 global checks
 checks+=1
 assert ok,label
def read(path):
 p=Path(path);b=p.read_bytes();k={'sha256':sha256(b).hexdigest(),'bytes':len(b),'resolved':str(p.resolve(strict=True)),'symlink':os.readlink(p) if p.is_symlink() else None}
 need(str(p) not in keys or keys[str(p)]==k,'stable rich key');keys[str(p)]=k
 return b
def pairs(rows):
 d={}
 for k,v in rows:need(k not in d,('duplicate JSON',k));d[k]=v
 return d
def obj(p):return json.loads(read(p),object_pairs_hook=pairs)
def pin(p,k):
 read(p);actual=keys[str(Path(p))];need(all(actual[x]==v for x,v in k.items()),('whole exact key',str(p)))
def manifest(path,base,count,full=False):
 out={}
 for line in read(path).decode().splitlines():
  m=re.fullmatch(r'([0-9a-f]{64})  (.+)',line);need(m is not None,'sha syntax');h,r=m.groups()
  need(r not in out and not Path(r).is_absolute() and '..' not in Path(r).parts,'safe unique manifest');pin(base/r,{'sha256':h});out[r]=h
 need(len(out)==count,('whole manifest count',str(path)))
 if full:need({p.relative_to(base).as_posix() for p in base.rglob('*') if p.is_file()}==set(out)|{path.name} and not any(p.is_symlink() for p in base.rglob('*')),'complete physical inventory')
 return out
read(__file__)
pin(A/'REPORT_STAGE_SHA256SUMS',{'sha256':'f6385b69c079eea88502baf5513091ea25cffdc2c7927aeb7ca20835edb5e531'})
stage=manifest(A/'REPORT_STAGE_SHA256SUMS',A,41,True)
need(sum(keys[str(A/p)]['bytes'] for p in stage)==1980184,'whole reporting payload bytes')
manifest(A/'PREPARATION_SHA256SUMS',A,20)
manifest(A/'INPUT_PINS.sha256',ROOT,33)
manifest(A/'EXTERNAL_READ_PINS.sha256',ROOT,32)
paper=ROOT/'papers/211-kernel-image-projection-feedback';freeze=paper/'frozen_round0'
author=manifest(freeze/'SHA256SUMS',freeze,32,True)
for rel,h in author.items():need(read(paper/rel)==read(freeze/rel),'whole unchanged author live/frozen')
need(not os.path.lexists(A/'DELTA.md') and not os.path.lexists(A/'SHA256SUMS'),'no preaccepted delta/final manifest')
f=obj(A/'FINDINGS.json')
need(f['recommendation']=='PASS_NO_REPAIR_REQUESTED' and f['current_open_total']==f['new_A_findings_total']==0 and f['findings']==[],'exact actual finding census')
need(all(f['census'][s]=={'open':0,'resolved':0} for s in ['Critical','Major','Minor']),'complete severity census')
need(not f['delta_received'] and not f['delta_accepted'],'delta remains genuinely pending')
need({r['id'] for r in f['inherited_findings']}=={'m01','m02'} and all(r['status']=='RESOLVED_BEFORE_A_IMPLEMENTATION_VERIFIED' for r in f['inherited_findings']),'inherited findings distinct')
received=[]
for mode,pop,expected_checks in [('initial',323,176456),('pair',360,312961),('closure',454,9575)]:
 folder=A/'evidence'/('runtime_'+mode+('_reception01' if mode!='closure' else '01'))
 result=obj(folder/'RESULT.json');ledger=obj(folder/('READ_INPUTS.json'))
 need(len(ledger)==pop and result['checks']==expected_checks,'exact actual artifact census')
 for p,k in ledger.items():pin(p,k)
 cap=obj(A/'evidence'/('RUNTIME_'+mode.upper()+('_RECEPTION_NATIVE01.json' if mode!='closure' else '_NATIVE01.json')))
 parts=[cap['result']]+[x['result'] for x in cap['polls']]
 need(parts[-1]['exit_code']==0 and not parts[-1].get('session_id'),'actual settled reviewer tool')
 printed=json.loads(''.join(x['output'] for x in parts));need(printed['result_sha256']==sha256(read(folder/'RESULT.json')).hexdigest() and printed['checks']==expected_checks and printed['status']==result['status'],'whole actual tool/result binding')
 args=shlex.split(cap['request']['cmd']);need(args[:4]==['/usr/bin/python3','-I','-S','-B'] and cap['request']['workdir']==str(ROOT),'actual reviewer receiver entry')
 if mode!='closure':
  binding=QA/('p211_a_'+mode+'_binding/BINDING.json')
  need(args[4:]==[str(A/'receive_runtime_records.py'),str(binding),sha256(read(binding)).hexdigest(),str(binding.parent/'PRODUCTION_TOOL_INVOCATION.json'),str(folder)],'all exact receiver argv')
  need(result['new_scientific_producer_invocations']==result['new_builds']==result['new_native_commands_from_receiver']==0,'not new science')
  manifest(binding.parent/'SHA256SUMS',binding.parent,17 if mode=='initial' else 10,True)
  run=QA/('root_replays/p211_a_'+mode+'_01');manifest(run/'SHA256SUMS',run,77 if mode=='initial' else 104,True)
 else:need(args[4:]==[str(A/'close_runtime_reception.py')] and result['new_scientific_producers']==result['new_builds']==result['new_page_views']==0,'exact closure entry/boundary')
 received.append({'mode':mode,'checks':expected_checks,'paths':pop})
root_key=obj(QA/'p211_a_binding_closure/INPUTS.json');need(len(root_key)==441,'whole accepted root runtime key')
for p,k in root_key.items():pin(p,k)
for name in ['REPORT.md','REPORT_HANDOFF.md','REPLAY_LOG.md','RUNTIME_EVIDENCE_ACCEPTANCE.md','RUNTIME_RECEPTION_SCOPE.md','SOURCE_AND_PROOF.md','BUILD_REPORT.md']:read(A/name)
static=obj(A/'evidence/REPORT_STATIC_NATIVE01.json')
need(static['result']['exit_code']==0,'actual static report check')
for p,k in list(keys.items()):pin(p,k)
result={'status':'PASS_ROOT_A_REPORT_STAGE_ORIGINAL_RECEPTION','checks':checks,'read_paths':len(keys),'immutable_report_payloads':41,'immutable_report_payload_bytes':1980184,'preparation_payloads_unchanged':20,'live_frozen_author_pairs_unchanged':32,'frozen_input_pins':33,'external_input_pins':32,'received_runtime_records':received,'original_root_runtime_inputs':441,'open_findings':0,'delta_accepted':False,'new_scientific_executions':0,'new_builds':0,'new_page_views':0,'scope':'Prior root actual strict pair and full semantic inspections reused under unchanged full keys; this receives the reviewer report and all original artifact evidence, not a new mathematical review or future delta approval.'}
for name,v in [('INPUTS.json',keys),('RESULT.json',result)]:
 with (HERE/name).open('xb') as f:f.write((json.dumps(v,sort_keys=True,indent=2)+'\n').encode())
print(json.dumps(result,sort_keys=True))
