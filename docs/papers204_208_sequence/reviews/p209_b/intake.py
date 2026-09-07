from pathlib import Path
import hashlib, json, shutil
W=Path('/root/autodl-tmp/symbolic_dynamics')
B=W/'docs/papers204_208_sequence/reviews/p209_b'
F=W/'papers/209-ordered-fibre-threading/frozen_round1'
def h(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
    assert h(F/'SHA256SUMS')=='c93e16cf20d2eb87f3b454fbdb3576e52c6c79fb74c8712a277efeab7e60ce57'
    entries={s[66:]:s[:64] for s in (F/'SHA256SUMS').read_text().splitlines()}
    actual={str(p.relative_to(F)) for p in F.rglob('*') if p.is_file() and p.name!='SHA256SUMS'}
    # Nested manifest names are payloads too.
    actual={str(p.relative_to(F)) for p in F.rglob('*') if p.is_file() and p!=F/'SHA256SUMS'}
    assert set(entries)==actual
    assert len(entries)==2003
    for p,d in entries.items(): assert h(F/p)==d,p
    all_files=sorted([F/p for p in entries]+[F/'SHA256SUMS'])
    (B/'INPUT_PINS.sha256').write_text(''.join(h(p)+'  '+str(p.relative_to(W))+'\n' for p in all_files))
    controls=['AGENTS.md','SYMBOLIC_DYNAMICS_STATE.md','.agents/skills/symbolic-dynamics-research/SKILL.md','docs/research_state/WORKFLOW.md','docs/papers204_208_sequence/PIPELINE_STATE.md','docs/papers204_208_sequence/ARTIFACT_CONTRACT.md','docs/papers204_208_sequence/PROBLEM_ANCHOR.md','docs/papers197_201_sequence/HOSTILE_REVIEW_PROTOCOL.md','docs/papers204_208_sequence/qa/P209_A_ROOT_DELTA_INSPECTION.md','docs/papers204_208_sequence/qa/P209_ROUND1_ROOT_INSPECTION.md']
    records=[]
    for rel in controls:
        p=W/rel; q=B/'assignment_context'/rel
        q.parent.mkdir(parents=True,exist_ok=True); shutil.copy2(p,q)
        records.append({'original':str(p),'preserved':str(q),'sha256':h(q)})
    (B/'assignment_context/ROLES.json').write_text(json.dumps(records,indent=2)+'\n')
    print(json.dumps({'status':'PASS','freeze_payloads':2003,'input_pins':len(all_files),'controls_preserved':len(records),'pin_sha256':h(B/'INPUT_PINS.sha256')},sort_keys=True))
if __name__=='__main__': main()
