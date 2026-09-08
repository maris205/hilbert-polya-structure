#!/usr/bin/env python3
"""Metadata-only finalization after root reports actual push completion.

No Git calls, receiver import/execution, object decompression or copied raw data.
"""
from pathlib import Path
import ast
import hashlib
import json

HERE=Path(__file__).resolve().parent
QA=HERE.parent
EVIDENCE=Path('/root/symbolic-dynamics-private-sync-evidence-20260907')
PHASES=('preflight','clone','copy','stage','stage_revision_01','commit_revision_01','commit_revision_02','push_revision_02')


def sha(p):
    assert p.is_file() and not p.is_symlink(),str(p)
    h=hashlib.sha256()
    with p.open('rb') as f:
        for b in iter(lambda:f.read(1024*1024),b''):
            h.update(b)
    return h.hexdigest()


def dump(p,obj):
    with p.open('x') as f:
        json.dump(obj,f,sort_keys=True,indent=2)
        f.write('\n')


def main():
    assert not (HERE/'SHA256SUMS').exists() and not (EVIDENCE/'root_receiver_01').exists()
    push=json.loads((EVIDENCE/'push_revision_02/RESULT.actual.json').read_text())
    assert push['status']=='PASS' and push['actual_remote_confirmed'] is True and push['divergence']==[0,0]
    assert (QA/'P210_CHECKPOINT_PUSH_REVISION02_ROOT_COMPLETION.actual.json').is_file()
    commit=json.loads((EVIDENCE/'commit_revision_02/RESULT.actual.json').read_text())
    assert commit['status']=='PASS' and commit['commit']==push['commit'] and commit['tree']==push['tree']
    assert push['tree']=='a26e19ee04c7a25fd0b0d00c67df784206baba4c'
    groups=[]
    paths=set()
    for base in [QA/n for n in ('p210_checkpoint_preparation','p210_checkpoint_stage_revision_01','p210_checkpoint_identity_revision_01')]+[EVIDENCE/n for n in PHASES]+[EVIDENCE/'stage_revision_01_lock_preservation']:
        files=sorted(p for p in base.rglob('*') if p.is_file())
        assert files and not any(p.is_symlink() for p in files)
        groups.append({'base':str(base),'files':[p.relative_to(base).as_posix() for p in files]})
        paths.update(files)
    # Fixed at finalization, never re-globbed to absorb future root receipts.
    root_flat=sorted(QA.glob('P210_CHECKPOINT_*.json'))
    assert all(p.is_file() and not p.is_symlink() for p in root_flat)
    paths.update(root_flat)
    paths.add(QA/'preserve_p210_stale_index_lock.py')
    assert not any(p.is_relative_to(HERE) or p.is_relative_to(EVIDENCE/'root_receiver_01') for p in paths)
    rows=[{'path':str(p),'bytes':p.stat().st_size,'sha256':sha(p)} for p in sorted(paths)]
    dump(HERE/'INPUT_PINS.json',rows)
    counts={n:len(list((EVIDENCE/n).glob('command_*.actual.json'))) for n in PHASES}
    assert [counts[n] for n in PHASES[:6]]==[12,19,10,7,19,8]
    assert counts['commit_revision_02']==21 and counts['push_revision_02']==push['commands']
    source_pins=[]
    for p in sorted(HERE.glob('*.py')):
        tree=ast.parse(p.read_text(),filename=str(p))
        compile(tree,str(p),'exec')
        source_pins.append({'path':p.name,'bytes':p.stat().st_size,'sha256':sha(p)})
    binding={'status':'PREPARED_AFTER_ACTUAL_PUSH_ROOT_EXECUTION_REQUIRED','phases':list(PHASES),
             'commit':push['commit'],'tree':push['tree'],'baseline':push['baseline'],
             'scope_sha256':push['scope_sha256'],'receiver_sha256':sha(HERE/'receive.py'),
             'input_pins_sha256':sha(HERE/'INPUT_PINS.json'),'physical_groups':groups,
             'native_counts':counts,'root_flat_inputs':[str(p) for p in root_flat]}
    dump(HERE/'INPUT_BINDING.json',binding)
    result={'status':'METADATA_FINALIZATION_PASS_RECEIVER_NOT_EXECUTED','source_pins':source_pins,
            'preserved_input_pins':len(rows),'physical_groups':len(groups),'root_flat_inputs':len(root_flat),
            'native_phase_commands':sum(counts.values()),'commit':push['commit'],'tree':push['tree'],
            'receiver_executions':0,'new_git_calls':0,'new_object_body_capture_bytes':0}
    dump(HERE/'FINALIZATION.actual.json',result)
    assert (HERE/'README.md').is_file()
    payloads=sorted(p for p in HERE.rglob('*') if p.is_file())
    with (HERE/'SHA256SUMS').open('x') as f:
        for p in payloads:
            f.write(sha(p)+'  '+p.relative_to(HERE).as_posix()+'\n')
    print(json.dumps({**result,'seal_payloads':len(payloads),'seal_sha256':sha(HERE/'SHA256SUMS')},sort_keys=True))


if __name__=='__main__':
    main()
