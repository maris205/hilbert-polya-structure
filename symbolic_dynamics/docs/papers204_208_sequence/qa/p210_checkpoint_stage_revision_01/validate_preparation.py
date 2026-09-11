#!/usr/bin/env python3
"""Static adaptation audit plus read-only current pins; never runs continuation."""
from pathlib import Path
import ast
import hashlib
import json
import os
import subprocess
import time
from inspect_failure import owned_processes, file_state
from pin_residue import holders

HERE=Path(__file__).resolve().parent
SOURCE=Path('/root/autodl-tmp/symbolic_dynamics')
ORIGINAL=HERE.parent/'p210_checkpoint_preparation'
DEST=Path('/root/symbolic-dynamics-private-sync-20260907')
EVIDENCE=Path('/root/symbolic-dynamics-private-sync-evidence-20260907')


def sha(p):
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
    out=HERE/'validation_01'
    out.mkdir()
    source_pins=[]
    parsed={}
    for p in sorted(HERE.glob('*.py')):
        body=p.read_text()
        parsed[p.name]=ast.parse(body,filename=str(p))
        compile(body,str(p),'exec')
        source_pins.append({'path':p.name,'sha256':sha(p),'lines':len(body.splitlines()),'syntax_only':True})
    for name in ('execute.py','process_support.py'):
        tree=parsed[name]
        assert not any(isinstance(n,ast.Constant) and isinstance(n.value,bytes) and n.value in (b'\\0',b'\\t') for n in ast.walk(tree)),name
        assert not any(isinstance(n,ast.Call) and isinstance(n.func,ast.Attribute) and n.func.attr in ('remove','unlink','rename','rmdir','rmtree') for n in ast.walk(tree)),name
        for n in ast.walk(tree):
            if isinstance(n,ast.Call) and isinstance(n.func,ast.Attribute) and n.func.attr=='Popen':
                assert any(k.arg=='start_new_session' and isinstance(k.value,ast.Constant) and k.value.value is True for k in n.keywords)
    phase_assignment=next(n for n in parsed['execute.py'].body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='PHASES' for t in n.targets))
    assert ast.literal_eval(phase_assignment.value)==('stage','commit','push')
    for n in ast.walk(parsed['execute.py']):
        if isinstance(n,ast.Call) and isinstance(n.func,ast.Name) and n.func.id=='git':
            literals=[a.value for a in n.args if isinstance(a,ast.Constant) and isinstance(a.value,str)]
            assert not set(literals)&{'clone','reset','clean','gc','repack','read-tree','update-index'},literals
            if 'push' in literals:
                assert not any('force' in x or x=='-f' for x in literals)
    argv=['git','diff','--no-index','--',str(ORIGINAL/'execute.py'),str(HERE/'execute.py')]
    env=dict(os.environ,GIT_OPTIONAL_LOCKS='0',GIT_TERMINAL_PROMPT='0')
    start=time.time()
    run=subprocess.run(argv,stdout=subprocess.PIPE,stderr=subprocess.PIPE,env=env,timeout=45)
    assert run.returncode==1 and not run.stderr
    (out/'SOURCE_DELTA.diff').write_bytes(run.stdout)
    (out/'SOURCE_DELTA.stderr.raw').write_bytes(run.stderr)
    dump(out/'SOURCE_DIFF_NATIVE.actual.json',{'argv':argv,'exit':run.returncode,'start_epoch':start,'end_epoch':time.time(),
          'stdout_sha256':sha(out/'SOURCE_DELTA.diff'),'stderr_sha256':sha(out/'SOURCE_DELTA.stderr.raw'),
          'environment_overrides_only':{'GIT_OPTIONAL_LOCKS':'0','GIT_TERMINAL_PROMPT':'0'}})
    originals=json.loads((HERE/'inspection_01/ORIGINAL_INPUT_PINS.json').read_text())
    for p in originals:
        assert sha(Path(p['path']))==p['sha256'],p['path']
    inspected=json.loads((HERE/'inspection_01/RESULT.actual.json').read_text())
    assert file_state(DEST/'.git/index')==inspected['stable_index']
    residues=json.loads((HERE/'FAILED_RESIDUE_PINS.actual.json').read_text())
    receipt=EVIDENCE/'stage_revision_01_lock_preservation/ROOT_PRESERVATION.actual.json'
    assert sha(receipt)=='208b59678887f7741403dc3110d0585f10b730ceca94788203d3bc92403fa00e'
    assert not (DEST/'.git/index.lock').exists()
    kept=file_state(Path(residues['proposed_lock_archive']))
    old=residues['pins'][0]
    assert all(kept[k]==v for k,v in old.items() if k!='path')
    assert not owned_processes() and not holders()
    for row in residues['pins'][1:]:
        state=file_state(Path(row['path']))
        assert all(state[k]==v for k,v in row.items()),row['path']
    root_pins=[]
    for p in sorted(receipt.parent.rglob('*')):
        if p.is_file():
            root_pins.append({'path':str(p),'bytes':p.stat().st_size,'sha256':sha(p)})
    for name in ('preserve_p210_stale_index_lock.py','P210_CHECKPOINT_LOCK_PRESERVATION_ROOT_LAUNCH.actual.json'):
        p=HERE.parent/name
        root_pins.append({'path':str(p),'bytes':p.stat().st_size,'sha256':sha(p)})
    native=json.loads((receipt.parent/'NATIVE_RESULT.actual.json').read_text())
    assert native['native_exit']==0 and native['stdout']==native['stderr']==''
    assert native['argv']==['/usr/bin/mv','--no-clobber','--',str(DEST/'.git/index.lock'),residues['proposed_lock_archive']]
    dump(out/'ROOT_LOCK_PRESERVATION_INPUT_PINS.json',root_pins)
    expected=json.loads((ORIGINAL/'preparation_01/EXPECTED_BLOBS.json').read_text())
    for row in expected:
        for base in (SOURCE,DEST):
            p=base/row['path']
            assert p.is_file() and not p.is_symlink() and p.stat().st_size==row['bytes'] and sha(p)==row['sha256'],str(p)
    assert file_state(DEST/'.git/index')==inspected['stable_index'] and not owned_processes()
    assert not any((EVIDENCE/(name+'_revision_01')).exists() for name in ('stage','commit','push'))
    result={'status':'STATIC_REVISION_PREPARATION_PASS_NO_CONTINUATION_EXECUTION','source_pins':source_pins,
            'scope_sha256':sha(ORIGINAL/'preparation_01/SCOPE.json'),
            'inspection_sha256':sha(HERE/'inspection_01/RESULT.actual.json'),
            'residue_pins_sha256':sha(HERE/'FAILED_RESIDUE_PINS.actual.json'),
            'root_lock_preservation_receipt':str(receipt),'root_lock_preservation_receipt_sha256':sha(receipt),
            'original_failure_pins_unchanged':len(originals),'root_preservation_pins':len(root_pins),
            'source_and_overlay_files_rehashed':len(expected),'source_payload_bytes_each':sum(r['bytes'] for r in expected),
            'index_still_exact_baseline':True,'original_object_residues_unchanged':True,
            'new_phase_directories_absent':True,'continuation_executions':0,'git_writes_by_preparer':0,
            'lock_move_was_actual_root_action_not_preparer_action':True,
            'remaining_overlay_bytes':os.statvfs('/root').f_bavail*os.statvfs('/root').f_frsize,
            'remaining_overlay_reservation_bytes':3*658584369+1024**3}
    dump(out/'RESULT.actual.json',result)
    print(json.dumps({k:v for k,v in result.items() if k!='source_pins'},sort_keys=True))


if __name__=='__main__':
    main()
