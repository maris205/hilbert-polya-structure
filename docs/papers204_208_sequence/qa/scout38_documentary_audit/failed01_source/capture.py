"""New native documentary recorder. Only this QA directory is writable."""
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import time

sys.dont_write_bytecode = True
import check

HERE = Path(__file__).resolve().parent


def save(path, value):
    with path.open('x') as f:
        json.dump(value, f, indent=2, sort_keys=True)
        f.write('\n')


def snapshot(paths):
    return {str(p): dict(sha256=hashlib.sha256(check.read(p)).hexdigest(), bytes=p.stat().st_size) for p in paths}


def capture(label, argv, paths):
    assert label.replace('_', '').isalnum()
    target = HERE / label
    target.mkdir(exist_ok=False)
    before = snapshot(paths)
    save(target / 'inputs_before.json', before)
    invocation = dict(argv=argv, cwd=str(check.ROOT), start_epoch=time.time(), role='native_documentary_self_familiarity_not_independent_review')
    save(target / 'invocation.json', invocation)
    with (target / 'stdout.raw').open('xb') as out, (target / 'stderr.raw').open('xb') as err:
        run = subprocess.run(argv, cwd=check.ROOT, stdout=out, stderr=err, check=False)
    after = snapshot(paths)
    save(target / 'inputs_after.json', after)
    receipt = dict(invocation, exit_code=run.returncode, finish_epoch=time.time(), inputs_count=len(paths),
        inputs_unchanged=before == after, stdout=snapshot([target / 'stdout.raw']), stderr=snapshot([target / 'stderr.raw']))
    save(target / 'receipt.json', receipt)
    print(json.dumps(receipt, sort_keys=True))
    assert before == after
    return run.returncode


if __name__ == '__main__':
    assert len(sys.argv) == 3 and sys.argv[1] == 'check'
    label = sys.argv[2]
    raise SystemExit(capture(label, [sys.executable, '-B', str(HERE / 'check.py'), str(HERE / label)], check.all_inputs()))
