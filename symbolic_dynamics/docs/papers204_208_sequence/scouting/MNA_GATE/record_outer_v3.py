#!/usr/bin/env python3
"""Capture a named gate documentary producer's entire actual outer streams."""
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import time

root=Path('/root/autodl-tmp/symbolic_dynamics')
gate=root/'docs/papers204_208_sequence/scouting/MNA_GATE'
name=sys.argv[1]
if name not in ('pair_v3','audit_final'):
    raise ValueError('unassigned producer')
script={'pair_v3':'run_pair_v3.py','audit_final':'audit_final.py'}[name]
folder=gate/'evidence'/('outer_'+name)
folder.mkdir()
env={'PATH':'/usr/bin:/bin','LANG':'C.UTF-8','LC_ALL':'C.UTF-8','TZ':'UTC'}
argv=[str(Path(sys.executable).resolve()),'-I','-S','-B',str(gate/script)]
start=time.time()
(folder/'attempt.json').write_text(json.dumps({'argv':argv,'cwd':str(root),'environment':env,
                                            'started_epoch':start},sort_keys=True,indent=2)+'\n')
try:
    process=subprocess.run(argv,cwd=root,env=env,stdout=subprocess.PIPE,stderr=subprocess.PIPE,timeout=60)
    out,err,code=process.stdout,process.stderr,process.returncode
except subprocess.TimeoutExpired as exc:
    out,err,code=exc.stdout or b'',exc.stderr or b'',None
(folder/'stdout.raw').write_bytes(out)
(folder/'stderr.raw').write_bytes(err)
record={'argv':argv,'cwd':str(root),'environment':env,'started_epoch':start,'finished_epoch':time.time(),
        'exit':code,'stdout':{'bytes':len(out),'sha256':hashlib.sha256(out).hexdigest()},
        'stderr':{'bytes':len(err),'sha256':hashlib.sha256(err).hexdigest()},
        'script_sha256':hashlib.sha256((gate/script).read_bytes()).hexdigest()}
(folder/'receipt.json').write_text(json.dumps(record,sort_keys=True,indent=2)+'\n')
print(json.dumps(record,sort_keys=True,indent=2))
sys.exit(code if code is not None else 124)
