#!/usr/bin/env python3
"""Static metadata closure only: no executor import, Git call or mutation."""
from pathlib import Path
import ast
import hashlib
import json

HERE=Path(__file__).resolve().parent


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
    assert not (HERE/'SHA256SUMS').exists()
    assert not Path('/root/symbolic-dynamics-private-sync-accepted-20260907.git').exists()
    scope=json.loads((HERE/'SCOPE.json').read_text())
    assert not Path(scope['new_evidence']).exists()
    sources=[]
    for p in sorted(HERE.glob('*.py')):
        tree=ast.parse(p.read_text(),filename=str(p))
        compile(tree,str(p),'exec')
        sources.append({'path':p.name,'bytes':p.stat().st_size,'sha256':sha(p)})
    parsed=ast.parse((HERE/'execute.py').read_text())
    operations=[]
    for node in ast.walk(parsed):
        if isinstance(node,ast.Call) and isinstance(node.func,ast.Name) and node.func.id=='git':
            values=[a.value for a in node.args if isinstance(a,ast.Constant)]
            operations.append(values)
            assert not any(v in ('add','clone','reset','checkout','clean','gc','repack','config') for v in values)
        if isinstance(node,ast.Call) and isinstance(node.func,ast.Attribute):
            assert node.func.attr not in ('unlink','rmdir','rename','replace','rmtree')
    code=(HERE/'execute.py').read_text()
    assert "choices=('build','push')" in code and "'commit-tree',tree,'-p',BASE" in code
    assert "git(BARE,'update-ref','refs/heads/main',commit,BASE)" in code
    assert "'push','origin',commit+':refs/heads/main'" in code and '--force' not in code
    rows=json.loads((HERE/'SELECTED_PATHS.json').read_text())
    excluded=json.loads((HERE/'EXCLUDED_PATHS.json').read_text())
    assert len(rows)==2013 and len(excluded)==306
    assert sum(r['change']=='A' for r in rows)==2009 and sum(r['change']=='M' for r in rows)==4
    assert max(r['bytes'] for r in rows)==6471668
    pins=json.loads((HERE/'PRESERVED_INPUT_PINS.json').read_text())
    assert len(pins)==624
    for row in pins:
        assert Path(row['path']).stat().st_size==row['bytes'] and sha(Path(row['path']))==row['sha256']
    unique={r['git_blob_sha1']:r for r in rows}
    result={'status':'STATIC_BARE_REVISION_PREPARATION_PASS_NO_EXECUTION','source_pins':sources,'native_git_operations_in_source':operations,
            'selected_paths':len(rows),'additions':2009,'modifications':4,'excluded_paths':len(excluded),
            'selected_bytes':sum(r['bytes'] for r in rows),'unique_selected_objects':len(unique),
            'unique_selected_bytes':sum(r['bytes'] for r in unique.values()),'largest_selected_blob_bytes':6471668,
            'preserved_input_pins_rechecked':len(pins),'executor_imports_or_executions':0,'git_calls':0}
    dump(HERE/'STATIC_VALIDATION.actual.json',result)
    assert (HERE/'README.md').is_file()
    paths=sorted(p for p in HERE.rglob('*') if p.is_file())
    assert not any(p.is_symlink() for p in paths)
    with (HERE/'SHA256SUMS').open('x') as f:
        for p in paths:
            f.write(sha(p)+'  '+p.relative_to(HERE).as_posix()+'\n')
    print(json.dumps({**result,'seal_payloads':len(paths),'seal_sha256':sha(HERE/'SHA256SUMS')},sort_keys=True))


if __name__=='__main__':
    main()
