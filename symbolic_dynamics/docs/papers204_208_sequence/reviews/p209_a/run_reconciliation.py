"""Record one post-commitment schema-adapter execution and actual cmp."""
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import time

BASE = Path(__file__).resolve().parent
ROOT = BASE.parents[3]
FREEZE = ROOT / 'papers/209-ordered-fibre-threading/frozen_round0'
OUT = BASE / 'reconciliation_01'
ENV = {'PATH': '/usr/bin:/bin', 'LANG': 'C.UTF-8', 'LC_ALL': 'C.UTF-8', 'TZ': 'UTC'}
assert not OUT.exists()
assert sys.flags.no_site and sys.flags.isolated and sys.flags.optimize == 0 and sys.dont_write_bytecode
assert dict(os.environ) == ENV
OUT.mkdir()
def info(path):
    path = Path(path)
    return {'sha256': hashlib.sha256(path.read_bytes()).hexdigest(), 'bytes': path.stat().st_size}
def save(name, data):
    with (OUT / name).open('x') as stream:
        stream.write(json.dumps(data, indent=2, sort_keys=True) + '\n')
baseline = BASE / 'review_pair_01/ALL_INPUTS_INCLUDING_CAPSULES_BEFORE.json'
names = list(json.loads(baseline.read_bytes()))
names += [str(p) for p in (Path(__file__), BASE / 'reconcile.py', baseline, BASE / 'CANONICAL.json', FREEZE / 'CANONICAL.json')]
before = {name: info(name) for name in sorted(set(names))}
save('INPUTS_BEFORE.json', before)
records = []
commands = [('reconcile', ['/usr/bin/python3.10', '-I', '-S', '-B', '-X', 'pycache_prefix=' + str(OUT / 'never_created_cache'), str(BASE / 'reconcile.py'), str(FREEZE / 'CANONICAL.json'), str(BASE / 'CANONICAL.json')]),
            ('projection_cmp', ['/usr/bin/cmp', '--', str(OUT / 'author_projection.json'), str(OUT / 'reviewer_projection.json')])]
for tag, argv in commands:
    row = {'argv': argv, 'env': ENV, 'cwd': str(OUT), 'exit': None, 'started_epoch': time.time(), 'stdout': tag + '.stdout', 'stderr': tag + '.stderr'}
    save(tag + '.attempt.json', row)
    with (OUT / row['stdout']).open('xb') as stdout, (OUT / row['stderr']).open('xb') as stderr:
        child = subprocess.run(argv, cwd=OUT, env=ENV, stdout=stdout, stderr=stderr)
    row.update(exit=child.returncode, finished_epoch=time.time(), stdout_pin=info(OUT / row['stdout']), stderr_pin=info(OUT / row['stderr']))
    save(tag + '.command.json', row)
    records.append(row)
    if child.returncode:
        break
after = {name: info(name) for name in before}
save('INPUTS_AFTER.json', after)
okay = before == after and len(records) == 2 and all(r['exit'] == 0 for r in records) and not (OUT / 'never_created_cache').exists()
save('RECEIPT.json', {'status': 'PASS' if okay else 'FAIL_PRESERVED', 'inputs': len(before), 'inputs_unchanged': before == after, 'commands': records, 'scope': 'Postcommitment adapter execution; conservative prior runtime closure retained and rehashed, no fresh OS trace or new mathematical producer.'})
files = sorted(p for p in OUT.rglob('*') if p.is_file())
with (OUT / 'SHA256SUMS').open('x') as stream:
    stream.write(''.join(info(p)['sha256'] + '  ' + p.relative_to(OUT).as_posix() + '\n' for p in files))
print(json.dumps({'status': 'PASS' if okay else 'FAIL_PRESERVED', 'inputs': len(before), 'payloads': len(files), 'output': str(OUT)}, sort_keys=True))
raise SystemExit(0 if okay else 1)
