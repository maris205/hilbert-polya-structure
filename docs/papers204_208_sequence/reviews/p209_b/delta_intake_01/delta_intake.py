"""Preserve exact original roles before B delta assessment; no acceptance."""
import hashlib
import json
from pathlib import Path
import shutil
import sys

W=Path('/root/autodl-tmp/symbolic_dynamics')
B=W/'docs/papers204_208_sequence/reviews/p209_b'
Q=W/'docs/papers204_208_sequence/qa'
SEAL='d88b831e60414d47ae0b2afb2583b73d02fc9764877a00952f4a9d90d13488ea'
DELTA='282dc2ab3f0021abeca145c20b76d0e0ef10e0b0e9948a173a24e6ead05b1400'


def h(p): return hashlib.sha256(p.read_bytes()).hexdigest()


def main():
    out=Path(sys.argv[1]); assert out==B/'delta_intake_01'
    assert h(B/'SHA256SUMS')==SEAL and h(B/'DELTA.md')==DELTA
    entries={line[66:]:line[:64] for line in (B/'SHA256SUMS').read_text().splitlines()}
    assert len(entries)==1298 and entries['DELTA.md']==DELTA
    for name,digest in entries.items(): assert h(B/name)==digest,name
    for name,source,digest in [('INITIAL_REVIEW_SEAL.sha256','SHA256SUMS',SEAL),('INITIAL_DELTA.md','DELTA.md',DELTA)]:
        target=B/name
        assert not target.exists()
        shutil.copyfile(B/source,target)
        assert h(target)==digest and target.read_bytes()==(B/source).read_bytes()
    context=out/'context'; context.mkdir()
    sources=[W/'AGENTS.md',W/'SYMBOLIC_DYNAMICS_STATE.md',
             W/'docs/papers204_208_sequence/PIPELINE_STATE.md',
             W/'.agents/skills/symbolic-dynamics-research/SKILL.md',
             W/'docs/research_state/WORKFLOW.md',
             W/'docs/papers204_208_sequence/ARTIFACT_CONTRACT.md',
             W/'docs/papers197_201_sequence/HOSTILE_REVIEW_PROTOCOL.md',
             Path('/root/autodl-tmp/.codex/skills/research-review/SKILL.md'),
             W/'docs/papers204_208_sequence/P209_B_RESPONSE.md',
             Q/'P209_B_ROOT_INITIAL_INSPECTION.md']
    sources += [Q/name for name in ['P209_B_EXACT_NOCHANGE_CHECK.actual.json',
                'P209_B_ROOT_PAIR_INSPECTION.actual.json','P209_B_ROOT_PAIR_EXECUTION.actual.json',
                'P209_B_ROOT_PAIR_PREPARATION.actual.json','P209_B_ROOT_INITIAL_INSPECTION.actual.json']]
    rows=[]
    for index,p in enumerate(sources):
        digest=h(p)
        target=context/(str(index).zfill(2)+'_'+p.name)
        shutil.copyfile(p,target)
        assert h(target)==digest==h(p) and p.read_bytes()==target.read_bytes()
        rows.append({'original':str(p),'physical':str(target),'sha256':digest,'bytes':p.stat().st_size})
    expected={str(W/'docs/papers204_208_sequence/P209_B_RESPONSE.md'):'c2cab3d26ddd9f5e5ba7e31dc0f3afa1c8d06510fd1276294cae33c63cdbc1f8',
              str(Q/'P209_B_ROOT_INITIAL_INSPECTION.md'):'bc209cf12ebe228d845d022e244da3605916c53ea371e592d1556336be5f96f9'}
    assert all(next(r['sha256'] for r in rows if r['original']==p)==v for p,v in expected.items())
    result={'status':'PASS_EXACT_INITIAL_PRESERVATION_AND_INTAKE','initial_payloads_checked':len(entries),
            'initial_seal_sha256':SEAL,'initial_delta_sha256':DELTA,'copies':rows,
            'initial_report_and_census_unchanged':True,'current_delta_status':'UNASSESSED',
            'acceptance_performed':False,'new_math_build_render_view':False}
    (out/'INTAKE_RESULT.json').write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
    print(json.dumps(result,sort_keys=True))


if __name__=='__main__':main()
