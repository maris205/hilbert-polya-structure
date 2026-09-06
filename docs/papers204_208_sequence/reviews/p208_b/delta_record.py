"""Exclusive actual command/stream recorder for B's documentary-only delta."""
from pathlib import Path
import hashlib
import json
import subprocess
import sys
import time
import uuid
BASE=Path('/root/autodl-tmp/symbolic_dynamics/docs/papers204_208_sequence/reviews/p208_b')
ROOT=BASE.parents[3]
mode=sys.argv[1]
assert mode in ('prepare','audit01','audit02')
out=BASE/('delta_prepare_execution' if mode=='prepare' else 'delta/'+mode)
out.mkdir(exist_ok=False)
prefix=out/('unused_pycache_'+uuid.uuid4().hex)
assert not prefix.exists()
args=[sys.executable,'-I','-S','-B','-X','pycache_prefix='+str(prefix),str(BASE/'delta_review.py'),mode]
env={'PATH':'/root/miniconda3/bin:/usr/bin:/bin','LANG':'C','LC_ALL':'C','TZ':'UTC'}
start=time.time()
with (out/'audit.stdout').open('xb') as stdout,(out/'audit.stderr').open('xb') as stderr:
    child=subprocess.run(args,cwd=ROOT,env=env,stdout=stdout,stderr=stderr)
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
with (out/'COMMAND.json').open('x') as f:
    json.dump({'argv':args,'cwd':str(ROOT),'environment':env,'exit_code':child.returncode,
        'seconds':time.time()-start,'stdout_sha256':sha(out/'audit.stdout'),
        'stderr_sha256':sha(out/'audit.stderr'),'unused_cache_absent':not prefix.exists()},f,sort_keys=True,indent=2);f.write('\n')
print(json.dumps({'mode':mode,'exit_code':child.returncode,'stdout':(out/'audit.stdout').read_text(),
                  'stderr':(out/'audit.stderr').read_text()},sort_keys=True))
raise SystemExit(child.returncode)
