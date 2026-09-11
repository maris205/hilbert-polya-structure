"""Seal the completed original B package; no scientific execution or delta."""
import hashlib
import json
import os
from pathlib import Path
import sys

W=Path('/root/autodl-tmp/symbolic_dynamics')
B=W/'docs/papers204_208_sequence/reviews/p209_b'
F=W/'papers/209-ordered-fibre-threading/frozen_round1'


def h(path):
    result=hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda:stream.read(1024*1024),b''): result.update(block)
    return result.hexdigest()


def check_manifest(path,base,complete=False):
    entries={}
    for line in path.read_text().splitlines():
        digest,name=line.split('  ',1)
        relative=Path(name)
        assert not relative.is_absolute() and '..' not in relative.parts
        assert name not in entries and len(digest)==64
        target=base/relative
        assert target!=path and not target.is_symlink() and h(target)==digest
        entries[name]=digest
    if complete:
        assert set(entries)=={p.relative_to(base).as_posix() for p in base.rglob('*')
                              if p.is_file() and p!=path}
    return entries


def main():
    assert sys.flags.isolated and sys.flags.no_site and sys.dont_write_bytecode and sys.flags.optimize==0
    assert dict(os.environ)=={'PATH':'/usr/bin:/bin','LANG':'C.UTF-8','LC_ALL':'C.UTF-8','TZ':'UTC'}
    assert not (B/'SHA256SUMS').exists() and not (B/'PRESEAL_CHECK.json').exists()
    required=['REPORT.md','FINDINGS.json','DELTA.md','verify.py','CANONICAL.json',
              'INPUT_PINS.sha256','REPLAY_LOG.md','SOURCE_AND_PROOF.md','BUILD_REPORT.md',
              'ARTIFACT_AUDIT.md','RECONCILIATION_AND_AUDIT_LOG.md']
    assert all((B/name).is_file() for name in required)
    census=json.loads((B/'FINDINGS.json').read_bytes())
    assert census['current_open_counts']=={'critical':0,'major':0,'minor':0}
    assert census['findings']==[] and census['delta_status']=='UNASSESSED'
    assert '**UNASSESSED' in (B/'DELTA.md').read_text()
    assert h(B/'verify.py')=='d5fd105ddfc162323f06cd530fbd696b0093643a7a0c24c64747cd9c9be30467'
    assert h(B/'CANONICAL.json')=='612e1463162deba868cf7cf81d61c8f017713f9b28c4c38b81b00d376bac992c'
    assert h(F/'SHA256SUMS')=='c93e16cf20d2eb87f3b454fbdb3576e52c6c79fb74c8712a277efeab7e60ce57'
    assert len(check_manifest(F/'SHA256SUMS',F,True))==2003
    assert len(check_manifest(B/'INPUT_PINS.sha256',W))==2004
    check_manifest(B/'INDEPENDENCE_COMMITMENT.sha256',B)
    nested={}
    for name in ['review_pair_01','review_pair_01/replay_01','review_pair_01/replay_02',
                 'launcher_review_pair_01','review_build_01','launcher_review_build_01',
                 'auxiliary_01','artifact_audit_01','artifact_audit_02','artifact_audit_03']:
        folder=B/name
        entries=check_manifest(folder/'SHA256SUMS',folder,True)
        nested[name]={'payloads':len(entries),'sha256':h(folder/'SHA256SUMS')}
    audit=json.loads((B/'artifact_audit_03/AUDIT_RESULT.json').read_bytes())
    wrapper=json.loads((B/'artifact_audit_03/RECEIPT.json').read_bytes())
    assert audit['status']=='PASS_DOCUMENTARY_ROLE_AND_DEPENDENCY_AUDIT'
    assert wrapper['status']=='PASS' and wrapper['inputs_unchanged']
    assert audit['delta_status']=='UNASSESSED'
    record={'status':'PASS_ORIGINAL_PACKAGE_PRESEAL','scope':'Documentary integrity, not fresh mathematics/build/view or delta acceptance.',
            'required_artifacts':required,'nested_seals':nested,'frozen_payloads':2003,'frozen_inputs':2004,
            'audit_result_sha256':h(B/'artifact_audit_03/AUDIT_RESULT.json'),
            'verifier_sha256':h(B/'verify.py'),'canonical_sha256':h(B/'CANONICAL.json'),
            'current_open_counts':census['current_open_counts'],'delta_status':'UNASSESSED',
            'external':'OWNER_AMBER / HOLD_EXTERNAL'}
    with (B/'PRESEAL_CHECK.json').open('x') as stream:
        json.dump(record,stream,sort_keys=True,indent=2);stream.write('\n')
    paths=sorted(p for p in B.rglob('*') if p.is_file())
    assert all(not p.is_symlink() for p in paths)
    with (B/'SHA256SUMS').open('x') as stream:
        for p in paths: stream.write(h(p)+'  '+p.relative_to(B).as_posix()+'\n')
    entries=check_manifest(B/'SHA256SUMS',B,True)
    print(json.dumps({'status':'PASS_SEALED_INITIAL_MANUSCRIPT_B','payloads':len(entries),
                      'seal_sha256':h(B/'SHA256SUMS'),'canonical_bytes':(B/'CANONICAL.json').stat().st_size,
                      'checks_per_process':54794,'states_per_process':3414,'processes':2,
                      'current_open_counts':census['current_open_counts'],'delta_status':'UNASSESSED',
                      'external':'OWNER_AMBER / HOLD_EXTERNAL'},sort_keys=True))


if __name__=='__main__': main()
