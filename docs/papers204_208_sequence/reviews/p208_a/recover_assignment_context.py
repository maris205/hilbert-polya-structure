"""Later recovery of contemporaneously pinned documentary context, not pre-read copies."""
from pathlib import Path
import runpy,json,sys,time,hashlib
OUT=Path('/root/autodl-tmp/symbolic_dynamics/docs/papers204_208_sequence/reviews/p208_a')
ROOT=Path('/root/autodl-tmp/symbolic_dynamics')
MIRROR=Path('/root/autodl-tmp/hilbert-polya-structure')
shared=runpy.run_path(str(OUT/'record.py'))
command,pins,dump=[shared[k] for k in ('command','pins','dump')]
dest=OUT/'assignment_context_recovery';dest.mkdir()
before=pins([__file__,OUT/'record.py',OUT/'CONTEXT_AT_ASSIGNMENT.json','/usr/bin/git',sys.executable]);dump(dest/'INPUTS_BEFORE.json',before)
old=json.loads((OUT/'CONTEXT_AT_ASSIGNMENT.json').read_text())
env={'PATH':'/usr/bin:/bin','LANG':'C','LC_ALL':'C','TZ':'UTC'}
commit='076cfbd45446e4a803de495d009f186a54bea503'
for i,rel in enumerate(['SYMBOLIC_DYNAMICS_STATE.md','docs/papers204_208_sequence/PIPELINE_STATE.md']):
    command(['/usr/bin/git','show',commit+':'+rel],MIRROR,env,dest/('git_show_%d'%i))
    raw=(dest/('git_show_%d.stdout'%i)).read_bytes();assert hashlib.sha256(raw).hexdigest()==old[str(ROOT/rel)]
    p=dest/'historical'/rel;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(raw)
dump(dest/'INPUTS_AFTER.json',pins(before));assert pins(before)==before
dump(dest/'RECEIPT.json',dict(status='PASS',commit=commit,time_ns=time.time_ns(),
    scope='Exact later retrieval of original documentary bytes, matched against contemporaneous assignment pins. No claim these copies existed before reading; live root/batch indexes have since changed.'))
print('PASS exact historical context recovered from private committed objects; contemporaneous pins match.')
