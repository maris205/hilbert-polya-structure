#!/usr/bin/env python3
"""Metadata-only fixed receiver inputs after root reports actual bare push PASS."""
from pathlib import Path
import ast
import hashlib
import json

HERE=Path(__file__).resolve().parent
QA=HERE.parent
EVIDENCE=Path('/root/symbolic-dynamics-private-sync-evidence-20260907')
NEWEXEC=EVIDENCE/'remote_size_revision_01'
BARE=Path('/root/symbolic-dynamics-private-sync-accepted-20260907.git')
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
    assert not (HERE/'SHA256SUMS').exists() and not (NEWEXEC/'root_receiver_01').exists()
    push=json.loads((NEWEXEC/'push/RESULT.actual.json').read_text())
    build=json.loads((NEWEXEC/'build/RESULT.actual.json').read_text())
    assert push['status']==build['status']=='PASS' and push['actual_remote_confirmed'] is True
    assert push['divergence']==[0,0] and push['commit']==build['commit'] and push['tree']==build['tree']
    assert push['base']=='a380d24718fec4ef27365f44e96fb7ffa2b0fd10'
    assert push['captured_source_preserved']=='1f028072dc408a7d4404a7276f22f8666ba81801'
    groups=[]
    paths=set()
    for base in [QA/n for n in ('p210_checkpoint_preparation','p210_checkpoint_stage_revision_01','p210_checkpoint_identity_revision_01','p210_checkpoint_remote_size_revision_01')]+[EVIDENCE/n for n in PHASES]+[EVIDENCE/'stage_revision_01_lock_preservation',NEWEXEC/'build',NEWEXEC/'push']:
        files=sorted(p for p in base.rglob('*') if p.is_file())
        assert files and not any(p.is_symlink() for p in files)
        groups.append({'base':str(base),'files':[p.relative_to(base).as_posix() for p in files]})
        paths.update(files)
    # Freeze only these actual contemporary root receipts, not future outputs.
    flat=sorted(QA.glob('P210_CHECKPOINT_*.json'))
    paths.update(flat)
    paths.add(QA/'preserve_p210_stale_index_lock.py')
    paths.update(BARE/n for n in ('config','HEAD','index','objects/info/alternates'))
    assert not any(p.is_relative_to(HERE) or p.is_relative_to(NEWEXEC/'root_receiver_01') for p in paths)
    pins=[{'path':str(p),'bytes':p.stat().st_size,'sha256':sha(p)} for p in sorted(paths)]
    dump(HERE/'INPUT_PINS.json',pins)
    counts={n:len(list((EVIDENCE/n).glob('command_*.actual.json'))) for n in PHASES}
    counts.update({'bare_build':build['commands'],'bare_push':push['commands']})
    assert [counts[n] for n in PHASES]==[12,19,10,7,19,8,21,10]
    for name in ('build','push'):
        assert len(list((NEWEXEC/name).glob('command_*.actual.json')))==counts['bare_'+name]
    sources=[]
    for p in sorted(HERE.glob('*.py')):
        parsed=ast.parse(p.read_text(),filename=str(p))
        compile(parsed,str(p),'exec')
        sources.append({'path':p.name,'bytes':p.stat().st_size,'sha256':sha(p)})
    receiver_ast=ast.parse((HERE/'receive.py').read_text())
    readonly_operations=[]
    for node in ast.walk(receiver_ast):
        if isinstance(node,ast.Call) and isinstance(node.func,ast.Name) and node.func.id=='git':
            assert isinstance(node.args[0],ast.Name) and node.args[0].id in ('BARE','DEST','MIRROR')
            assert isinstance(node.args[1],ast.Constant)
            operation=node.args[1].value
            assert operation in ('rev-parse','rev-list','status','show-ref','diff','ls-tree','ls-files','cat-file','ls-remote','show')
            assert not (node.args[0].id=='BARE' and operation=='status')
            readonly_operations.append({'repository_role':node.args[0].id,'operation':operation})
    binding={'status':'PREPARED_AFTER_ACTUAL_BARE_PUSH_ROOT_EXECUTION_REQUIRED','baseline':push['base'],
             'captured_source_commit':push['captured_source_preserved'],'commit':push['commit'],'tree':push['tree'],
             'corrective_scope_sha256':push['scope_sha256'],'receiver_sha256':sha(HERE/'receive.py'),
             'input_pins_sha256':sha(HERE/'INPUT_PINS.json'),'physical_groups':groups,
             'native_counts':counts,'contemporaneous_root_receipts':[str(p) for p in flat]}
    dump(HERE/'INPUT_BINDING.json',binding)
    result={'status':'METADATA_FINALIZATION_PASS_RECEIVER_NOT_EXECUTED','source_pins':sources,
            'preserved_input_pins':len(pins),'physical_groups':len(groups),'contemporaneous_root_receipts':len(flat),
            'native_phase_records':sum(counts.values()),'commit':push['commit'],'tree':push['tree'],
            'static_readonly_operations':readonly_operations,
            'receiver_imports_or_executions':0,'git_calls':0,'moving_live_manuscript_or_control_reads':0}
    dump(HERE/'FINALIZATION.actual.json',result)
    assert (HERE/'README.md').is_file()
    payloads=sorted(p for p in HERE.rglob('*') if p.is_file())
    with (HERE/'SHA256SUMS').open('x') as f:
        for p in payloads:
            f.write(sha(p)+'  '+p.relative_to(HERE).as_posix()+'\n')
    print(json.dumps({**result,'seal_payloads':len(payloads),'seal_sha256':sha(HERE/'SHA256SUMS')},sort_keys=True))


if __name__=='__main__':
    main()
