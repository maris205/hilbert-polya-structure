#!/usr/bin/python3.10
"""One exact recoverable root move of our timed-out add's orphan lock."""
from pathlib import Path
from hashlib import sha256
import json
import os
import subprocess
import time

QA = Path('/root/autodl-tmp/symbolic_dynamics/docs/papers204_208_sequence/qa')
REPO = Path('/root/symbolic-dynamics-private-sync-20260907')
LOCK = REPO / '.git/index.lock'
OUT = Path('/root/symbolic-dynamics-private-sync-evidence-20260907/stage_revision_01_lock_preservation')
DEST = OUT / 'index.lock.failed-stage-01'
ENV = {'PATH': '/usr/bin:/bin', 'LANG': 'C', 'LC_ALL': 'C', 'TZ': 'UTC'}

def measure(path):
    st = path.lstat()
    assert path.is_file() and not path.is_symlink()
    return {'path': str(path), 'bytes': st.st_size, 'sha256': sha256(path.read_bytes()).hexdigest(),
            'device': st.st_dev, 'inode': st.st_ino, 'mtime_ns': st.st_mtime_ns, 'mode': st.st_mode}

def owners():
    held, active, races = [], [], 0
    for proc in Path('/proc').iterdir():
        if not proc.name.isdigit():
            continue
        try:
            argv = (proc/'cmdline').read_bytes().split(b'\0')
            exe = Path(os.fsdecode(argv[0])).name if argv and argv[0] else ''
            # Inspect only relevant identity, never record unrelated argument values.
            if exe in {'git', 'ssh', 'git-receive-pack', 'git-upload-pack', 'git-pack-objects', 'git-index-pack'}:
                cwd = (proc/'cwd').resolve()
                if str(REPO).encode() in argv or cwd == REPO or cwd.is_relative_to(REPO):
                    active.append({'pid': int(proc.name), 'executable_basename': exe, 'cwd': str(cwd)})
            for fd in (proc/'fd').iterdir():
                try:
                    if os.readlink(fd) == str(LOCK):
                        held.append({'pid': int(proc.name), 'fd': fd.name})
                except FileNotFoundError:
                    races += 1
        except (FileNotFoundError, ProcessLookupError):
            races += 1
    return {'lock_fd_holders': held, 'active_owned_git_processes': active,
            'vanished_process_or_fd_races': races, 'epoch': time.time()}

def save(name, data):
    with (OUT/name).open('x') as stream:
        json.dump(data, stream, sort_keys=True, indent=2)
        stream.write('\n')

def main():
    recorded = json.loads((QA/'p210_checkpoint_stage_revision_01/FAILED_RESIDUE_PINS.actual.json').read_bytes())
    wanted = recorded['pins'][0]
    assert wanted['path'] == str(LOCK) and wanted['bytes'] == 0
    assert wanted['inode'] == 8613190901 and wanted['device'] == 99
    assert wanted['mtime_ns'] == 1788791779973320571 and wanted['mode'] == 33188
    assert wanted['sha256'] == sha256(b'').hexdigest()
    assert measure(LOCK) == wanted and not OUT.exists() and not OUT.is_symlink()
    before = owners()
    assert before['lock_fd_holders'] == before['active_owned_git_processes'] == []
    assert measure(LOCK) == wanted
    OUT.mkdir()
    save('BEFORE.actual.json', {'source_pin': wanted, 'owners': before,
         'source_evidence': str(QA/'p210_checkpoint_stage_revision_01/FAILED_RESIDUE_PINS.actual.json')})
    # Repeat immediately before the one exact owned-file move.
    immediate = owners()
    assert immediate['lock_fd_holders'] == immediate['active_owned_git_processes'] == []
    assert measure(LOCK) == wanted and not DEST.exists()
    argv = ['/usr/bin/mv', '--no-clobber', '--', str(LOCK), str(DEST)]
    save('ATTEMPT.actual.json', {'argv': argv, 'cwd': str(QA), 'environment': ENV,
         'started_epoch': time.time(), 'native_exit': None, 'immediate_owners': immediate})
    run = subprocess.run(argv, cwd=QA, env=ENV, capture_output=True, timeout=60, check=False)
    save('NATIVE_RESULT.actual.json', {'argv': argv, 'native_exit': run.returncode,
         'stdout': run.stdout.decode(), 'stderr': run.stderr.decode(), 'ended_epoch': time.time()})
    assert run.returncode == 0 and run.stdout == run.stderr == b'' and not os.path.lexists(LOCK)
    kept = measure(DEST)
    assert {k:v for k,v in kept.items() if k != 'path'} == {k:v for k,v in wanted.items() if k != 'path'}
    result = {'status': 'ROOT_CONFIRMED_EXACT_ORPHAN_LOCK_PRESERVATION', 'source': str(LOCK),
              'preserved_path': str(DEST), 'source_pin': wanted, 'preserved_pin': kept,
              'no_live_holders_immediately_before_move': True,
              'actual_native_exit': 0, 'no_deleted_bytes': True,
              'scope': 'Exact zero-byte orphan index lock moved recoverably; timed-out evidence and both temporary object residues untouched.'}
    save('ROOT_PRESERVATION.actual.json', result)
    print(json.dumps(result, sort_keys=True))

if __name__ == '__main__':
    main()
