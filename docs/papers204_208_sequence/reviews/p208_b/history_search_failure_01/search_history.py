"""Bounded read-only literal/mechanism search; snapshots before later prose reads."""
import hashlib
import json
from pathlib import Path
import subprocess
import re

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
BASE = ROOT/'docs/papers204_208_sequence/reviews/p208_b'
OUT = BASE/'history_context'
OUT.mkdir(exist_ok=False)
ENV = {'PATH':'/usr/bin:/bin','LANG':'C','LC_ALL':'C','TZ':'UTC'}
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def cmd(name,args):
    p = subprocess.run(args,cwd=ROOT,env=ENV,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    (OUT/(name+'.stdout')).write_bytes(p.stdout)
    (OUT/(name+'.stderr')).write_bytes(p.stderr)
    (OUT/(name+'.command.json')).write_text(json.dumps({'argv':args,'cwd':str(ROOT),'env':ENV,'exit_code':p.returncode},indent=2)+'\n')
    assert p.returncode in (0,1)
    return p.stdout.decode().splitlines()
names = cmd('inventory',['/usr/bin/rg','--files','papers','docs'])
paper,scouts=[],[]
for name in names:
    p=Path(name)
    if name.startswith('papers/') and p.suffix=='.tex':
        number=re.match(r'(\d+)-',p.parts[1])
        if number and int(number[1])<208 and not any(x.startswith(('frozen_','qa_','cold_build','source_only')) for x in p.parts):
            paper.append(name)
    if name.startswith('docs/') and '/scouting/' in name and p.suffix=='.md' and not any(x.startswith(('execution_','assignment_context')) for x in p.parts):
        scouts.append(name)
paths=sorted(set(paper+scouts))
before={name:sha(ROOT/name) for name in paths}
(OUT/'SEARCH_INPUTS_BEFORE.json').write_text(json.dumps(before,indent=2,sort_keys=True)+'\n')
patterns=[r'triangul|polygon|tamari|dyck|reassocia|root.rotation|leftmost.rotation',
          r'prefix.{0,30}freez|frozen.{0,20}(prefix|cherry)|binary.{0,20}(cut|choice)|ordered.{0,20}reset|edge.label|snapshot|persistent.label']
hits=set()
for i,pattern in enumerate(patterns):
    found=cmd('search_'+str(i),['/usr/bin/rg','-n','-i','--no-heading',pattern,*paths])
    for line in found:
        hits.add(line.split(':',1)[0])
for name in sorted(hits):
    dst=OUT/'snapshots'/name
    dst.parent.mkdir(parents=True,exist_ok=True)
    dst.write_bytes((ROOT/name).read_bytes())
after={name:sha(ROOT/name) for name in paths}
(OUT/'SEARCH_INPUTS_AFTER.json').write_text(json.dumps(after,indent=2,sort_keys=True)+'\n')
assert before==after
summary={'paper_tex_files':len(paper),'paper_numbers':sorted(set(int(Path(p).parts[1].split('-')[0]) for p in paper)),
         'scout_markdown_files':len(scouts),'total_inputs':len(paths),'matching_files_snapshotted':len(hits),
         'patterns':patterns,'read_scope':'Full input corpus was machine-searched; only selected matched original definitions/proofs are subsequently read by the reviewer.'}
(OUT/'SEARCH_SUMMARY.json').write_text(json.dumps(summary,indent=2,sort_keys=True)+'\n')
print(json.dumps(summary,sort_keys=True))
