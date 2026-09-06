"""Seal this actual initial review, without manufacturing a delta."""
from pathlib import Path
import hashlib,json,time,sys
ROOT=Path('/root/autodl-tmp/symbolic_dynamics')
OUT=ROOT/'docs/papers204_208_sequence/reviews/p208_a'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def dump(p,x):p.write_text(json.dumps(x,sort_keys=True,indent=2)+'\n')
def main():
    assert not (OUT/'DELTA.md').exists(), 'initial stage only'
    assert not (OUT/'SHA256SUMS').exists(), 'do not overwrite a historical initial seal'
    audit=json.loads((OUT/'artifact_inspection02/audit.stdout').read_text())
    assert audit['status']=='PASS' and audit['author_records_compared']==2055
    rows=[]
    for name in ['INPUT_PINS.sha256','HISTORY_CONTEXT_PINS.sha256']:
        for line in (OUT/name).read_text().splitlines():
            h,rel=line.split('  ',1)
            rows.append(dict(pin_list=name,path=rel,expected=h,current=sha(ROOT/rel)))
    assert all(r['expected']==r['current'] for r in rows)
    old=json.loads((OUT/'CONTEXT_AT_ASSIGNMENT.json').read_text())
    context=[]
    recovered=OUT/'assignment_context_recovery/historical'
    for absolute,h in old.items():
        p=Path(absolute);rel=p.relative_to(ROOT)
        preserved=recovered/rel
        context.append(dict(path=str(rel),assignment_sha256=h,current_sha256=sha(p),
            changed_since_assignment=sha(p)!=h,
            later_recovered_copy=str(preserved.relative_to(OUT)) if preserved.exists() else None))
        if preserved.exists():assert sha(preserved)==h
        else:assert sha(p)==h
    dump(OUT/'FINAL_INPUT_CHECK.json',dict(status='PASS',time_ns=time.time_ns(),
        pinned_rows=len(rows),frozen_and_historical_checks=rows,mutable_assignment_context=context,
        reading_limit='A pin is an integrity referent, not an assertion that every listed body was read.'))
    pagefiles=[p for label in ['build01','build02','build03']
        for p in [OUT/label/'source_only/main.pdf',*sorted((OUT/label/'pages').glob('*.png'))]]
    assert len(pagefiles)==24
    dump(OUT/'PAGE_INPUT_PINS.json',{str(p.relative_to(OUT)):sha(p) for p in pagefiles})
    finding=json.loads((OUT/'FINDINGS.json').read_text())
    assert not finding['delta_accepted'] and sum(finding['census']['open'].values())==0
    required=['REPORT.md','SOURCE_AND_PROOF.md','verify.py','CANONICAL.json','REPLAY_LOG.md',
        'BUILD_REPORT.md','INPUT_PINS.sha256','FINDINGS.json','PAGE_VIEWS.md']
    assert all((OUT/p).is_file() for p in required)
    paths=[p for p in OUT.rglob('*') if p.is_file()]
    receipt=OUT/'INITIAL_SEAL_RECEIPT.json'
    assert receipt not in paths
    dump(receipt,dict(status='PASS_INITIAL_REPORT_SEALED_NOT_DELTA_ACCEPTED',
        time_ns=time.time_ns(),seal_program_sha256=sha(__file__),
        nonself_referents=len(paths)+1,
        scope='Every file under this review directory except its own SHA256SUMS, including failures and raw evidence.'))
    paths=sorted(p for p in OUT.rglob('*') if p.is_file() and p!=OUT/'SHA256SUMS')
    (OUT/'SHA256SUMS').write_text(''.join(f'{sha(p)}  {p.relative_to(OUT)}\n' for p in paths))
    assert len(paths)==json.loads(receipt.read_text())['nonself_referents']
    declared={}
    for line in (OUT/'SHA256SUMS').read_text().splitlines():
        h,rel=line.split('  ',1);assert sha(OUT/rel)==h;declared[rel]=h
    assert set(declared)=={str(p.relative_to(OUT)) for p in OUT.rglob('*')
        if p.is_file() and p!=OUT/'SHA256SUMS'}
    print(json.dumps(dict(status='PASS',manifest_sha256=sha(OUT/'SHA256SUMS'),
        nonself_referents=len(paths),canonical_sha256=sha(OUT/'CANONICAL.json'),
        verifier_sha256=sha(OUT/'verify.py'),recorder_sha256=sha(OUT/'record.py'),
        build_program_sha256=sha(OUT/'build.py'),
        artifact_assertions=audit['assertions']),sort_keys=True,indent=2))
if __name__=='__main__':main()
