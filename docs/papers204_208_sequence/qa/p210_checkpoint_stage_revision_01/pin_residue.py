#!/usr/bin/env python3
"""Read-only exact failed-residue pins and all-process lock-holder scan."""
from pathlib import Path
import hashlib
import json
import os
import time

HERE=Path(__file__).resolve().parent
DEST=Path('/root/symbolic-dynamics-private-sync-20260907')
LOCK=DEST/'.git/index.lock'
TEMPS=[DEST/'.git/objects/pack/tmp_pack_58p3V5',DEST/'.git/objects/96/tmp_obj_f76Bfi']


def sha(p):
    h=hashlib.sha256()
    with p.open('rb') as f:
        for b in iter(lambda:f.read(1024*1024),b''):
            h.update(b)
    return h.hexdigest()


def holders():
    found=[]
    for proc in Path('/proc').iterdir():
        if not proc.name.isdigit():
            continue
        try:
            for fd in (proc/'fd').iterdir():
                try:
                    target=os.readlink(fd)
                    if target in {str(LOCK),*(str(p) for p in TEMPS)}:
                        found.append({'pid':int(proc.name),'comm':(proc/'comm').read_text().strip(),
                                      'fd':fd.name,'exact_target':target})
                except (OSError,ProcessLookupError,PermissionError):
                    pass
        except (OSError,ProcessLookupError,PermissionError):
            pass
    return found


def main():
    before=holders()
    assert not before,'live holder requires root inspection; no move is allowed'
    pins=[]
    for p in [LOCK,*TEMPS]:
        s=p.stat()
        assert p.is_file() and not p.is_symlink()
        pins.append({'path':str(p),'bytes':s.st_size,'sha256':sha(p),'device':s.st_dev,
                     'inode':s.st_ino,'mtime_ns':s.st_mtime_ns,'mode':s.st_mode})
        assert p.stat().st_size==s.st_size and p.stat().st_mtime_ns==s.st_mtime_ns
    after=holders()
    assert not after
    result={'status':'READ_ONLY_EXACT_RESIDUE_PINS','pins':pins,'all_process_exact_fd_holders_before':before,
            'all_process_exact_fd_holders_after':after,'epoch':time.time(),'signals_moves_deletions':0,
            'proposed_lock_archive':'/root/symbolic-dynamics-private-sync-evidence-20260907/stage_revision_01_lock_preservation/index.lock.failed-stage-01',
            'only_lock_may_be_proposed_for_recoverable_root_move':True,'temporary_object_files_must_remain_at_original_paths':True}
    with (HERE/'FAILED_RESIDUE_PINS.actual.json').open('x') as f:
        json.dump(result,f,sort_keys=True,indent=2)
        f.write('\n')
    print(json.dumps(result,sort_keys=True))


if __name__=='__main__':
    main()
