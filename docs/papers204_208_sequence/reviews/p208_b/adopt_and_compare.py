"""Adopt actual producer stdout verbatim and run the nonmutating field adapter."""
from pathlib import Path
import hashlib
import json
import subprocess
import sys

ROOT=Path('/root/autodl-tmp/symbolic_dynamics')
BASE=ROOT/'docs/papers204_208_sequence/reviews/p208_b'
ENV={'PATH':'/root/miniconda3/bin:/usr/bin:/bin','LANG':'C','LC_ALL':'C','TZ':'UTC'}
OUT=BASE/'payload_comparison'
OUT.mkdir(exist_ok=False)
canonical=BASE/'CANONICAL.json';assert not canonical.exists()
canonical.write_bytes((BASE/'development_pair/run_1.stdout').read_bytes())
def run(name,args):
    p=subprocess.run(args,cwd=ROOT,env=ENV,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    (OUT/(name+'.stdout')).write_bytes(p.stdout);(OUT/(name+'.stderr')).write_bytes(p.stderr)
    (OUT/(name+'.command.json')).write_text(json.dumps({'argv':args,'cwd':str(ROOT),'environment':ENV,'exit_code':p.returncode},indent=2)+'\n')
    assert p.returncode==0,(name,p.returncode)
for i in (1,2):run(f'cmp_adopted_{i}',['/usr/bin/cmp','-s',str(canonical),str(BASE/f'development_pair/run_{i}.stdout')])
run('compare',[sys.executable,'-I','-S','-B','-X','pycache_prefix='+str(BASE/'unused_comparison_cache_01'),str(BASE/'compare_payloads.py')])
print(json.dumps({'status':'PASS','canonical_sha256':hashlib.sha256(canonical.read_bytes()).hexdigest(),
                 'comparison':json.loads((OUT/'compare.stdout').read_text())['checks']},sort_keys=True))
