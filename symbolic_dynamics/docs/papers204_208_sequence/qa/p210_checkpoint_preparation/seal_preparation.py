#!/usr/bin/env python3
"""Seal completed preparation only; never imports or invokes its executor."""
from pathlib import Path
import ast
import hashlib
import json

HERE = Path(__file__).resolve().parent


def sha(path):
    h = hashlib.sha256()
    with path.open('rb') as f:
        for b in iter(lambda: f.read(1024*1024), b''):
            h.update(b)
    return h.hexdigest()


def main():
    result = json.loads((HERE/'validation_01/RESULT.actual.json').read_text())
    assert result['status']=='STATIC_PREPARATION_PASS_EXECUTOR_NOT_RUN'
    assert result['clone_copy_stage_commit_push_executions']==0
    for item in result['sources']:
        assert sha(HERE/item['path'])==item['sha256'], item['path']
    assert sha(HERE/'preparation_01/SCOPE.json')==result['scope_sha256']
    ast.parse(Path(__file__).read_text())
    assert (HERE/'README.md').is_file()
    assert not Path('/root/symbolic-dynamics-private-sync-20260907').exists()
    assert not Path('/root/symbolic-dynamics-private-sync-evidence-20260907').exists()
    files = sorted(p for p in HERE.rglob('*') if p.is_file())
    assert not (HERE/'SHA256SUMS').exists()
    assert not any(p.is_symlink() for p in files)
    with (HERE/'SHA256SUMS').open('x') as f:
        for p in files:
            f.write(sha(p)+'  '+p.relative_to(HERE).as_posix()+'\n')
    print(json.dumps({'status':'PREPARATION_SEALED_ONLY','payloads':len(files),
          'payload_bytes':sum(p.stat().st_size for p in files), 'seal_sha256':sha(HERE/'SHA256SUMS'),
          'scope_sha256':result['scope_sha256'],'executor_executions':0},sort_keys=True))


if __name__=='__main__':
    main()
