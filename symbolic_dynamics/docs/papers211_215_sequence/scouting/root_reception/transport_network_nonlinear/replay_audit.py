"""Disclosed reuse of the fully read documentary auditor; no science."""
from pathlib import Path
from hashlib import sha256
import base64
import json
import subprocess
import time

ROOT=Path('/root/autodl-tmp/symbolic_dynamics')
HERE=Path(__file__).resolve().parent
AUDIT=ROOT/'docs/papers211_215_sequence/qa/transport_network_nonlinear_artifact_audit/audit.py'
def pin(p):
    p=Path(p);b=p.read_bytes()
    return {'bytes':len(b),'sha256':sha256(b).hexdigest(),'resolved':str(p.resolve())}
def stream(b):
    return {'bytes':len(b),'sha256':sha256(b).hexdigest(),'base64':base64.b64encode(b).decode()}
argv=['/usr/bin/python3.10','-I','-S','-B',str(AUDIT)]
env={'LANG':'C','LC_ALL':'C','PATH':'/usr/bin:/bin','TZ':'UTC'}
before={str(p):pin(p) for p in [Path(__file__),AUDIT,Path(argv[0])]}
started=time.time_ns()
r=subprocess.run(argv,cwd=ROOT,env=env,stdin=subprocess.DEVNULL,stdout=subprocess.PIPE,stderr=subprocess.PIPE,timeout=240,check=False)
record={'argv':argv,'cwd':str(ROOT),'environment':env,'started_unix_ns':started,
        'finished_unix_ns':time.time_ns(),'returncode':r.returncode,
        'stdout':stream(r.stdout),'stderr':stream(r.stderr),'inputs_before':before,
        'inputs_after':{p:pin(p) for p in before},
        'scope':'Reuses the entire existing read-only documentary auditor; its six child operations are not scientific programs.'}
for name,data in [('AUDIT_ROOT_STDOUT.json',r.stdout),('AUDIT_ROOT_NATIVE.json',(json.dumps(record,indent=2,sort_keys=True)+'\n').encode())]:
    with (HERE/name).open('xb') as f:f.write(data)
assert r.returncode==0 and not r.stderr and record['inputs_after']==before
v=json.loads(r.stdout)
assert v['new_failures']==[] and v['inputs_unchanged_after'] and v['science_executions']==0
print(json.dumps({'status':v['status'],'checks':v['assertions_checked'],'input_key':v['input_key']['sha256'],
                  'new_documentary_processes':len(v['new_documentary_processes']),
                  'stdout_key':pin(HERE/'AUDIT_ROOT_STDOUT.json'),'native_key':pin(HERE/'AUDIT_ROOT_NATIVE.json')},sort_keys=True))
