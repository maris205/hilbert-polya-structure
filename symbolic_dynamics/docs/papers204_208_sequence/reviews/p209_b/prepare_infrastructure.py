"""Mechanical, disclosed adaptation of A's runtime/build recorder only."""
from pathlib import Path
import difflib, hashlib, json, shutil
W=Path('/root/autodl-tmp/symbolic_dynamics')
B=W/'docs/papers204_208_sequence/reviews/p209_b'
A=W/'docs/papers204_208_sequence/reviews/p209_a'
def digest(p): return hashlib.sha256(p.read_bytes()).hexdigest()
original=B/'infrastructure_originals'
original.mkdir()
changes=[]
for name in ['record_review.py','launch_review.py','bootstrap.py']:
    source=A/name
    shutil.copy2(source,original/name)
    body=source.read_text()
    adapted=body
    if name=='record_review.py':
        adapted=adapted.replace('frozen_round0','frozen_round1').replace('0f77871539b374027ab42910471cc74cefcd570e214a8242ac0a30c7a83e70ba','c93e16cf20d2eb87f3b454fbdb3576e52c6c79fb74c8712a277efeab7e60ce57').replace('EXACT_ROUND0_SEAL','EXACT_ROUND1_SEAL')
        adapted=adapted.replace('"INDEPENDENCE_COMMITMENT.md", "COMMITMENT_PINS.sha256"','"INDEPENDENCE_DESIGN.md", "INDEPENDENCE_COMMITMENT.sha256", "intake.py"')
        adapted=adapted.replace('"p209-review-a-independent-v1"','"p209-b-ports-constructive-carrier-v1"')
        adapted=adapted.replace('b["state_count"]','b["states"]').replace('b["records"]','b["rows"]')
        adapted=adapted.replace('("n", "state_count", "partition_count", "maximum_fibre", "extremizer_ranks")','("n", "states", "recurrent", "image_size", "max_inverse")')
    adapted=adapted.replace('PASS_REVIEW_A_', 'PASS_REVIEW_B_').replace('P209 A actual', 'P209 B actual')
    (B/name).write_text(adapted)
    changes.extend(difflib.unified_diff(body.splitlines(keepends=True),adapted.splitlines(keepends=True),fromfile='infrastructure_originals/'+name,tofile=name))
    compile(adapted,str(B/name),'exec')
(B/'ADAPTATION.diff').write_text(''.join(changes))
(B/'INFRASTRUCTURE_INPUT_PINS.sha256').write_text(''.join(digest(A/name)+'  '+str((A/name).relative_to(W))+'\n' for name in ['record_review.py','launch_review.py','bootstrap.py']))
(B/'PARAMETERS.json').write_text(json.dumps({'n_values':list(range(6)),'total_states':3414,'CLI':['--max-n','5'],'scope':'Original boxes only; no manuscript expansion','schema':'p209-b-ports-constructive-carrier-v1'},indent=2)+'\n')
print(json.dumps({'status':'PREPARED_NOT_EXECUTED','copies':{name:digest(original/name) for name in ['record_review.py','launch_review.py','bootstrap.py']},'adapted':{name:digest(B/name) for name in ['record_review.py','launch_review.py','bootstrap.py']},'diff_sha256':digest(B/'ADAPTATION.diff')},sort_keys=True))
