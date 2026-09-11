"""Receive the complete documentary audit and its same-key root replay."""
from pathlib import Path
from hashlib import sha256
import base64
import json
import os
import re

ROOT=Path('/root/autodl-tmp/symbolic_dynamics')
HERE=Path(__file__).resolve().parent
AUDIT=ROOT/'docs/papers211_215_sequence/qa/transport_network_nonlinear_artifact_audit'
checks=0;keys={}
def need(ok,label):
    global checks
    checks+=1
    assert ok,label
def read(p):
    p=Path(p);b=p.read_bytes()
    k={'bytes':len(b),'sha256':sha256(b).hexdigest(),'resolved_path':str(p.resolve()),'mode':oct(p.stat().st_mode&0o777)}
    need(not p.is_symlink() and p.is_file(),'ordinary received file')
    need(str(p) not in keys or keys[str(p)]==k,'stable reception key')
    keys[str(p)]=k
    return b
def obj(p):return json.loads(read(p))
def stream(row):
    if 'base64' in row:b=base64.b64decode(row['base64'],validate=True)
    else:b=row['text'].encode('utf-8')
    need(len(b)==row['bytes'] and sha256(b).hexdigest()==row['sha256'],'whole lossless stream')
    return b

read(__file__)
rows={}
for line in read(AUDIT/'MANIFEST.sha256').decode().splitlines():
    m=re.fullmatch(r'([0-9a-f]{64})  (.+)',line);need(m is not None,'manifest grammar')
    h,r=m.groups();need(r not in rows and not Path(r).is_absolute() and '..' not in Path(r).parts,'safe unique manifest')
    need(sha256(read(AUDIT/r)).hexdigest()==h,'complete payload hash');rows[r]=h
need(len(rows)==7 and {p.relative_to(AUDIT).as_posix() for p in AUDIT.rglob('*') if p.is_file()}==set(rows)|{'MANIFEST.sha256'},'whole seven-payload audit inventory')
old=obj(AUDIT/'AUDIT_RESULT.json');new=obj(HERE/'AUDIT_ROOT_STDOUT.json')
for v in [old,new]:
    need(v['status']=='ARTIFACT_INTEGRITY_PASS_WITH_DISCLOSED_LIMITS' and v['assertions_checked']==836 and v['new_failures']==[],'actual complete successful result')
    need(v['science_executions']==v['science_imports']==v['network_requests']==0,'documentary only')
    ik=v['input_key'];declared={k:x for k,x in ik.items() if k not in ['sha256','definition']}
    need(sha256(json.dumps(declared,sort_keys=True,ensure_ascii=False,separators=(',',':')).encode()).hexdigest()==ik['sha256']==v['after_input_key_sha256'],'complete declared key hash')
    need(v['inputs_unchanged_after'] and len(ik['input_files'])==138,'full 138-file actual key')
    for row in ik['input_files']:
        read(row['path']);need(keys[row['path']]=={k:row[k] for k in keys[row['path']]},'all original key fields')
    need(not (ROOT/'docs/papers211_215_sequence/scouting/resource_allocation_lane/INTAKE.md').exists(),'historical missing-path observation unchanged')
    need(len(v['new_documentary_processes'])==6,'six actual child records')
    for p in v['new_documentary_processes']:
        need(p['returncode']==0 and p['cwd']==str(ROOT) and p['environment']==ik['environment'],'native process settlement')
        need(p['started_unix_ns']<=p['finished_unix_ns'],'native chronology')
        stream(p['stdout']);need(stream(p['stderr'])==b'','actual empty stderr')
        read(p['executable']['path']);need(keys[p['executable']['path']]=={k:p['executable'][k] for k in keys[p['executable']['path']]},'whole executable pin')
# Exactly the actual six child timestamp pairs differ. All other result fields
# (including every observed raw child byte, command and key) must agree.
def without_times(v):
    v=json.loads(json.dumps(v))
    for p in v['new_documentary_processes']:
        del p['started_unix_ns'];del p['finished_unix_ns']
    return v
need(without_times(old)==without_times(new),'whole prior/current result comparison excluding only twelve child timestamps')
e=obj(AUDIT/'EXECUTION.json');n=e['native_execution'];need(n['returncode']==0 and e['capture_tool_metadata']['exit_code']==0,'actual auditor original settlement')
need(n['argv']==old['input_key']['entry_argv'] and n['cwd']==str(ROOT) and n['environment']==old['input_key']['environment'],'original actual invocation binding')
need(n['stdout']['path']=='AUDIT_RESULT.json' and n['stdout']['sha256']==sha256(read(AUDIT/'AUDIT_RESULT.json')).hexdigest() and n['stdout']['bytes']==135044 and stream(n['stderr'])==b'','original raw output binding')
n=obj(HERE/'AUDIT_ROOT_NATIVE.json');need(n['returncode']==0 and stream(n['stdout'])==read(HERE/'AUDIT_ROOT_STDOUT.json') and stream(n['stderr'])==b'','actual root raw output binding')
need(n['argv']==old['input_key']['entry_argv'] and n['cwd']==str(ROOT) and n['environment']==old['input_key']['environment'],'root actual argv/cwd/environment')
need(n['inputs_before']==n['inputs_after'],'root wrapper source key bracket')
for p,k in n['inputs_before'].items():
    read(p);need(keys[p]['sha256']==k['sha256'] and keys[p]['bytes']==k['bytes'] and keys[p]['resolved_path']==k['resolved'],'root wrapper exact current pins')
t=obj(HERE/'AUDIT_ROOT_TOOL.json');need(t['result']['exit_code']==0,'root actual tool settled')
printed=json.loads(t['result']['output']);need(printed['stdout_key']['sha256']==sha256(read(HERE/'AUDIT_ROOT_STDOUT.json')).hexdigest() and printed['native_key']['sha256']==sha256(read(HERE/'AUDIT_ROOT_NATIVE.json')).hexdigest(),'root actual tool binds original raw records')
for p,k in list(keys.items()):read(p);need(keys[p]==k,'final unchanged key')
result={'status':'PASS_ROOT_THREE_ZERO_LITERAL_ARTIFACT_RECEPTION','checks':checks,'read_paths':len(keys),
        'original_audit_payloads':7,'desk_payloads':[40,11,4],'desk_full_files':58,
        'same_complete_input_key':old['input_key']['sha256'],'received_original_input_files':138,
        'actual_root_documentary_assertions':836,'actual_root_documentary_children':6,
        'new_scientific_runs':0,'new_literal_attempts':0,
        'comparison_scope':'All result fields equal except exactly the six documentary children\u2019s start/end timestamps; child raw stdout/stderr bytes equal exactly. No missing nonlinear historical provenance is reconstructed.'}
for name,v in [('CLOSURE_INPUTS.json',keys),('CLOSURE_RESULT.json',result)]:
    with (HERE/name).open('xb') as f:f.write((json.dumps(v,sort_keys=True,indent=2)+'\n').encode())
print(json.dumps(result,sort_keys=True))
