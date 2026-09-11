#!/usr/bin/python3.10
"""Capture this directory's new read-only documentary helper exactly once.

No submitted source is imported or executed. No ambient environment is
recorded. Output files are exclusive; an actual failed attempt is retained.
"""
from hashlib import sha256
import json
from pathlib import Path
import subprocess
import time

ROOT=Path('/root/autodl-tmp/symbolic_dynamics')
HERE=ROOT/'docs/papers211_215_sequence/qa/p211_round2_physical_independent01'
OUT=HERE/'run05'
assert not OUT.exists()
OUT.mkdir(mode=0o700)
ENV={'PATH':'/usr/bin:/bin','LANG':'C.UTF-8','LC_ALL':'C.UTF-8','TZ':'UTC'}
def pin(raw):
    return {'bytes':len(raw),'sha256':sha256(raw).hexdigest()}
def put(name,value):
    raw=value if isinstance(value,bytes) else (json.dumps(value,sort_keys=True,indent=2)+'\n').encode()
    with (OUT/name).open('xb') as stream:
        stream.write(raw)
assert Path.cwd()==ROOT
for name in ('EXECUTED_RECEIVER_SOURCE.py','EXECUTED_CAPTURE_SOURCE.py','CHECKS_ATTEMPT.json',
             'CHECKS_NATIVE.json','CHECKS.stdout.raw','CHECKS.stderr.raw','RESULT.json'):
    assert not (OUT/name).exists(),name
receiver=HERE/'receive_physical05.py'
source,capture=receiver.read_bytes(),Path(__file__).read_bytes()
put('EXECUTED_RECEIVER_SOURCE.py',source)
put('EXECUTED_CAPTURE_SOURCE.py',capture)
argv=['/usr/bin/python3.10','-I','-S','-B',str(receiver)]
attempt={'argv':argv,'cwd':str(ROOT),'environment':ENV,'stdin':'subprocess.DEVNULL',
         'timeout_seconds':180,'started_epoch':time.time(),'source_pin':pin(source),'capture_source_pin':pin(capture),
         'scope':'only independently owned read-only documentary receiver; no submitted program execution'}
put('CHECKS_ATTEMPT.json',attempt)
code,error,state=None,None,'captured'
try:
    completed=subprocess.run(argv,cwd=ROOT,env=ENV,stdin=subprocess.DEVNULL,capture_output=True,timeout=180)
    stdout,stderr,code=completed.stdout,completed.stderr,completed.returncode
except subprocess.TimeoutExpired as exc:
    stdout,stderr=exc.stdout or b'',exc.stderr or b''
    error={'type':type(exc).__name__,'message':str(exc)}
    state='partial_at_timeout; no native exit invented'
except OSError as exc:
    stdout,stderr=b'',b''
    error={'type':type(exc).__name__,'message':str(exc)}
    state='launch_failed_or_unknown; no native exit invented'
put('CHECKS.stdout.raw',stdout)
put('CHECKS.stderr.raw',stderr)
native={**attempt,'ended_epoch':time.time(),'native_exit_code':code,'exception':error,'stream_capture_status':state,
        'stdout':{'path':'CHECKS.stdout.raw',**pin(stdout)},'stderr':{'path':'CHECKS.stderr.raw',**pin(stderr)}}
put('CHECKS_NATIVE.json',native)
if error is None and code==0 and not stderr:
    outcome=json.loads(stdout)
    result={k:v for k,v in outcome.items() if k!='READ_INPUTS'}
    result['whole_helper_stdout']=native['stdout']
    result['whole_input_key_entries']=len(outcome['READ_INPUTS'])
else:
    result={'status':'FAIL_DOCUMENTARY_ATTEMPT_PRESERVED','native_exit_code':code,'exception':error,
            'stdout':native['stdout'],'stderr':native['stderr']}
put('RESULT.json',result)
print(json.dumps({'status':result['status'],'checks':result.get('checks'),
                  'read_paths':result.get('receiver_read_paths'),'native':native},sort_keys=True))
raise SystemExit(0 if code==0 and error is None and not stderr else 1)
