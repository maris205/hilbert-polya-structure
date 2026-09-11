#!/usr/bin/env python3
"""Static identity-only amendment validation; never import the executor."""
from pathlib import Path
import ast
import hashlib
import json
import subprocess
import time

HERE=Path(__file__).resolve().parent
REV=HERE.parent/'p210_checkpoint_stage_revision_01'
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
    for p in sorted(HERE.glob('*.py')):
        code=p.read_text()
        tree=ast.parse(code,filename=str(p))
        compile(tree,str(p),'exec')
        source_pins.append({'path':p.name,'bytes':p.stat().st_size,'sha256':sha(p)})
    source=(HERE/'execute.py').read_text()
    parsed=ast.parse(source)
    phase_assignment=[n for n in parsed.body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='PHASES' for t in n.targets)]
    assert len(phase_assignment)==1 and ast.literal_eval(phase_assignment[0].value)==('commit','push')
    git_calls=[]
    for node in ast.walk(parsed):
        if isinstance(node,ast.Call) and isinstance(node.func,ast.Name) and node.func.id=='git':
            values=[a.value for a in node.args if isinstance(a,ast.Constant)]
            git_calls.append(values)
            assert not any(v in ('add','clone','read-tree','reset','checkout','clean','gc','repack','config') for v in values)
        if isinstance(node,ast.Call) and isinstance(node.func,ast.Attribute):
            assert node.func.attr not in ('unlink','rmdir','rename','replace','rmtree')
    assert sha(HERE/'process_support.py')==sha(REV/'process_support.py')=='8ce99e3b7684123c5a04d99d8fa5cee98bd4e8e8b9bca7f7a4dd5dc93b5dde7c'
    assert "'user.name=mariswang', '-c', 'user.email=wangliang.f@gmail.com'" in source
    assert "GIT_AUTHOR_NAME','GIT_AUTHOR_EMAIL','GIT_COMMITTER_NAME','GIT_COMMITTER_EMAIL" in source
    assert "'commit_revision_02/RESULT.actual.json'" in source and "args.phase + '_revision_02'" in source
    assert "'stage_revision_01/RESULT.actual.json'" in source
    assert "identity == ['mariswang','wangliang.f@gmail.com','mariswang','wangliang.f@gmail.com']" in source
    pins=json.loads((HERE/'IDENTITY_INPUT_PINS.json').read_text())
    originals=json.loads((REV/'inspection_01/ORIGINAL_INPUT_PINS.json').read_text())
    assert len(pins)==118 and len(originals)==266
    for row in pins+originals:
        p=Path(row['path'])
        assert p.is_file() and not p.is_symlink() and sha(p)==row['sha256'],str(p)
    residues=json.loads((REV/'FAILED_RESIDUE_PINS.actual.json').read_text())
    for row in residues['pins'][1:]:
        p=Path(row['path'])
        assert p.stat().st_size==row['bytes'] and sha(p)==row['sha256'],str(p)
    assert not any((EVIDENCE/(p+'_revision_02')).exists() for p in ('commit','push'))
    argv=['git','diff','--no-index','--no-ext-diff','--',str(REV/'execute.py'),str(HERE/'execute.py')]
    start=time.time()
    r=subprocess.run(argv,stdout=subprocess.PIPE,stderr=subprocess.PIPE,timeout=30)
    (out/'SOURCE_DELTA.diff').write_bytes(r.stdout)
    (out/'SOURCE_DELTA.stderr.raw').write_bytes(r.stderr)
    dump(out/'SOURCE_DELTA.actual.json',{'argv':argv,'exit':r.returncode,'start_epoch':start,'end_epoch':time.time(),
         'stdout_sha256':sha(out/'SOURCE_DELTA.diff'),'stderr_sha256':sha(out/'SOURCE_DELTA.stderr.raw')})
    assert r.returncode==1 and not r.stderr
    result={'status':'STATIC_IDENTITY_PREPARATION_PASS_NO_CONTINUATION_EXECUTION','source_pins':source_pins,
            'executor_sha256':sha(HERE/'execute.py'),'support_byte_identical_to_accepted_revision':True,
            'source_delta_lines':len(r.stdout.splitlines()),'git_calls':git_calls,
            'identity_input_pins_checked':len(pins),'original_failed_input_pins_checked':len(originals),
            'failed_object_residues_checked':2,'accepted_stage_not_reexecuted':True,
            'new_git_mutations':0,'new_executor_imports_or_executions':0,
            'native_diff_exit':r.returncode,'identity_inspection_sha256':sha(HERE/'inspection_01/RESULT.actual.json')}
    dump(out/'RESULT.actual.json',result)
    print(json.dumps(result,sort_keys=True))


if __name__=='__main__':
    main()
