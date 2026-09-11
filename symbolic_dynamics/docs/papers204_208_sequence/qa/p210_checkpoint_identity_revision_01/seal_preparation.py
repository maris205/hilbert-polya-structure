#!/usr/bin/env python3
"""Seal this metadata-only identity preparation, excluding the seal itself."""
from pathlib import Path
import hashlib
import json

HERE=Path(__file__).resolve().parent
EVIDENCE=Path('/root/symbolic-dynamics-private-sync-evidence-20260907')


def sha(p):
    h=hashlib.sha256()
    with p.open('rb') as f:
        for b in iter(lambda:f.read(1024*1024),b''):
            h.update(b)
    return h.hexdigest()


def main():
    r=json.loads((HERE/'validation_01/RESULT.actual.json').read_text())
    assert r['status']=='STATIC_IDENTITY_PREPARATION_PASS_NO_CONTINUATION_EXECUTION'
    for row in r['source_pins']:
        assert sha(HERE/row['path'])==row['sha256']
    assert not any((EVIDENCE/(p+'_revision_02')).exists() for p in ('commit','push'))
    assert (HERE/'README.md').is_file() and not (HERE/'SHA256SUMS').exists()
    paths=sorted(p for p in HERE.rglob('*') if p.is_file())
    assert not any(p.is_symlink() for p in paths)
    with (HERE/'SHA256SUMS').open('x') as f:
        for p in paths:
            f.write(sha(p)+'  '+p.relative_to(HERE).as_posix()+'\n')
    print(json.dumps({'status':'IDENTITY_PREPARATION_SEALED_ONLY','payloads':len(paths),
                     'seal_sha256':sha(HERE/'SHA256SUMS'),'continuation_executions':0},sort_keys=True))


if __name__=='__main__':
    main()
