"""Bounded documentary closure, actual PDF cmp and optional preflight."""
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import time

BASE = Path(__file__).resolve().parent
ROOT = BASE.parents[3]
FREEZE = ROOT / 'papers/209-ordered-fibre-threading/frozen_round0'
OUT = BASE / 'auxiliary_01'
SCRIPT = Path('/root/autodl-tmp/.codex/plugins/cache/ars-codex/ars-codex/0.1.28/skills/academic-research-suite/ars/scripts/pdf_read_preflight.py')
PDF = BASE / 'review_build_01/cold_build/main.pdf'
ENV = {'PATH': '/usr/bin:/bin', 'LANG': 'C.UTF-8', 'LC_ALL': 'C.UTF-8', 'TZ': 'UTC'}
assert dict(os.environ) == ENV and not OUT.exists()
OUT.mkdir()
def info(path):
    path = Path(path)
    return {'sha256': hashlib.sha256(path.read_bytes()).hexdigest(), 'bytes': path.stat().st_size}
def save(name, value):
    with (OUT / name).open('x') as stream:
        stream.write(json.dumps(value, sort_keys=True, indent=2) + '\n')
inputs = [Path(__file__), SCRIPT, SCRIPT.with_name('audit_snapshot.py'), PDF, FREEZE / 'main.pdf', FREEZE / 'FROZEN_LINK_MAP.json', FREEZE / 'SHA256SUMS', BASE / 'INPUT_PINS.sha256', Path('/usr/bin/python3.10'), Path('/usr/bin/cmp')]
mapping = json.loads((FREEZE / 'FROZEN_LINK_MAP.json').read_bytes())
inputs += [Path(p) for p in mapping['external_input_pins']]
inputs += [Path(r['physical_target']) for r in mapping['links']]
for line in (BASE / 'INPUT_PINS.sha256').read_text().splitlines():
    digest, name = line.split('  ', 1)
    inputs.append(ROOT / name)
    assert info(ROOT / name)['sha256'] == digest
before = {str(p): info(p) for p in sorted(set(inputs))}
save('INPUTS_BEFORE.json', before)
for path, digest in mapping['external_input_pins'].items():
    assert info(path)['sha256'] == digest
for row in mapping['links']:
    assert info(row['physical_target'])['sha256'] == row['sha256']
    assert row['href'] in (FREEZE / row['document']).read_text()
save('FROZEN_LINK_CLOSURE.json', {'status': 'PASS_PINNED_TARGETS', 'links': len(mapping['links']), 'external_paths': len(mapping['external_input_pins']), 'scope': 'Every mapped original link target checked; historical author seal uses explicit alias; this is not a semantic review of all external targets.'})
records = []
for tag, argv in [('pdf_cmp', ['/usr/bin/cmp', '--', str(PDF), str(FREEZE / 'main.pdf')]),
                  ('pdf_preflight', ['/usr/bin/python3.10', '-S', '-B', str(SCRIPT), str(PDF), '--output', str(OUT / 'PDF_PREFLIGHT.json')])]:
    row = {'argv': argv, 'cwd': str(OUT), 'env': ENV, 'exit': None, 'started_epoch': time.time(), 'stdout': tag + '.stdout', 'stderr': tag + '.stderr'}
    save(tag + '.attempt.json', row)
    with (OUT / row['stdout']).open('xb') as stdout, (OUT / row['stderr']).open('xb') as stderr:
        process = subprocess.run(argv, cwd=OUT, env=ENV, stdout=stdout, stderr=stderr)
    row.update(exit=process.returncode, finished_epoch=time.time(), stdout_pin=info(OUT / row['stdout']), stderr_pin=info(OUT / row['stderr']))
    save(tag + '.command.json', row)
    records.append(row)
after = {name: info(name) for name in before}
save('INPUTS_AFTER.json', after)
assert before == after
save('RECEIPT.json', {'status': 'RECORDED', 'inputs_unchanged': True, 'inputs': len(before), 'commands': records, 'preflight': json.loads((OUT / 'PDF_PREFLIGHT.json').read_bytes()) if (OUT / 'PDF_PREFLIGHT.json').exists() else None, 'scope': 'Auxiliary script availability and exact document pins, not a new mathematical/build producer or OS-hermetic trace.'})
files = sorted(p for p in OUT.rglob('*') if p.is_file())
with (OUT / 'SHA256SUMS').open('x') as stream:
    stream.write(''.join(info(p)['sha256'] + '  ' + p.relative_to(OUT).as_posix() + '\n' for p in files))
print(json.dumps({'status': 'RECORDED', 'commands': [r['exit'] for r in records], 'payloads': len(files), 'preflight': json.loads((OUT / 'PDF_PREFLIGHT.json').read_bytes()) if (OUT / 'PDF_PREFLIGHT.json').exists() else None}, sort_keys=True))
