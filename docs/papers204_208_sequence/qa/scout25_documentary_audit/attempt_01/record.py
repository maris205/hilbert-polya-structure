"""Record one real, read-only audit; writes only this owned audit package."""
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import time

BASE = Path(__file__).resolve().parent
ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
ENV = {'PATH': '/usr/bin:/bin', 'LANG': 'C.UTF-8', 'LC_ALL': 'C.UTF-8', 'TZ': 'UTC'}


def pin(p):
    data = Path(p).read_bytes()
    return {'sha256': hashlib.sha256(data).hexdigest(), 'bytes': len(data)}


def save(p, value):
    with p.open('x') as out:
        out.write(json.dumps(value, indent=2, sort_keys=True) + '\n')


def main():
    assert dict(os.environ) == ENV
    assert sys.flags.isolated and sys.flags.no_site and sys.flags.dont_write_bytecode and sys.flags.optimize == 0
    assert sys.pycache_prefix and not Path(sys.pycache_prefix).exists()
    assert sys.argv[1:] and len(sys.argv) == 2
    label = sys.argv[1]
    assert label.startswith('attempt_') and label.replace('_', '').isalnum()
    out = BASE / label
    out.mkdir(exist_ok=False)
    originals = [BASE / 'inspect.py', BASE / 'record.py', Path('/usr/bin/python3.10')]
    before = {str(p): pin(p) for p in originals}
    save(out / 'PINS.before.json', before)
    for name in ('inspect.py', 'record.py'):
        shutil.copyfile(BASE / name, out / name)
    source_seal = ROOT / 'docs/papers204_208_sequence/scouting/finite_systems_twenty_fifth/SHA256SUMS'
    shutil.copyfile(source_seal, out / 'SCOUT_ORIGINAL_SHA256SUMS')
    argv = ['/usr/bin/python3.10', '-I', '-S', '-B', '-X',
        'pycache_prefix=' + str(out / 'never_created_child_cache'), str(out / 'inspect.py')]
    save(out / 'ATTEMPT.json', {'argv': argv, 'cwd': str(ROOT), 'environment': ENV,
        'started_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
        'recorder_orig_argv': sys.orig_argv, 'recorder_cwd': os.getcwd(),
        'scope': 'One actual read-only documentary audit; no scout producer rerun.'})
    with (out / 'stdout').open('xb') as stdout, (out / 'stderr').open('xb') as stderr:
        child = subprocess.Popen(argv, cwd=ROOT, env=ENV, stdout=stdout, stderr=stderr)
        try:
            code = child.wait()
        except BaseException:
            child.terminate()
            try:
                child.wait(timeout=5)
            except subprocess.TimeoutExpired:
                child.kill()
                child.wait()
            raise
    after = {str(p): pin(p) for p in originals}
    save(out / 'PINS.after.json', after)
    result = {'exit': code, 'stdout': pin(out / 'stdout'), 'stderr': pin(out / 'stderr'),
        'source_and_interpreter_before_after_equal': before == after,
        'completed_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}
    save(out / 'RESULT.json', result)
    ok = code == 0 and before == after
    report = json.loads((out / 'stdout').read_text()) if ok else None
    if report:
        assert report['status'] == 'PASS_DOCUMENTARY_AUDIT'
        assert all(pin(p) == expected for p, expected in report['current_read_set'].items())
    save(out / 'RECORDER_RECEIPT.json', {'status': 'PASS_DOCUMENTARY_AUDIT_RECORDED' if ok else 'FAIL_RETAINED',
        'child_exit': code, 'child_result': result, 'parent_full_child_read_set_recheck': bool(report),
        'new_science_or_downloads': 0, 'complete_package_seal_excludes_only': 'SHA256SUMS'})
    assert not (BASE / 'SHA256SUMS').exists(), 'Never overwrite previous audit seal'
    files = sorted(p for p in BASE.rglob('*') if p.is_file())
    assert all(not p.is_symlink() for p in files)
    with (BASE / 'SHA256SUMS').open('x') as manifest:
        manifest.write(''.join(pin(p)['sha256'] + '  ' + p.relative_to(BASE).as_posix() + '\n' for p in files))
    print(json.dumps({'status': 'PASS_DOCUMENTARY_AUDIT_RECORDED' if ok else 'FAIL_RETAINED',
        'child_exit': code, 'checks': report['checks'] if report else None,
        'current_read_files': report['current_read_files'] if report else None,
        'payload_files': len(files), 'manifest': pin(BASE / 'SHA256SUMS'),
        'original_failures_remain': [22, 60, 28, 60] if report else None}, sort_keys=True))
    raise SystemExit(0 if ok else (code or 1))


if __name__ == '__main__':
    main()
