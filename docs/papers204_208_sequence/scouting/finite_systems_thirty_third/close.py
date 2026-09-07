#!/usr/bin/env python3
"""Documentary closure only; does not execute or import the scientific map."""
import hashlib
import json
import pathlib
import re
import sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import record_v2
from record import ROOT, OWN, digest

receipts = sorted((OWN / 'commands').glob('*/receipt.json'))
references = 0
distinct = set()
commands = []
for receipt_path in receipts:
    folder = receipt_path.parent
    receipt = json.loads(receipt_path.read_text())
    before = json.loads((folder / 'inputs_before.json').read_text())
    after = json.loads((folder / 'inputs_after.json').read_text())
    paths = json.loads((folder / 'pathset.json').read_text())
    assert receipt['label'] == folder.name
    assert paths == sorted(set(paths)) == sorted(before) == sorted(after)
    assert len(paths) == receipt['input_count']
    assert before == after and receipt['unchanged']
    assert receipt['exit'] == 0, folder.name
    assert receipt['argv'] and receipt['cwd'] == str(ROOT)
    assert receipt['recorder_sha256'] == digest(OWN / 'record.py')
    for name in paths:
        assert digest(ROOT / name) == before[name], name
    for channel in ('stdout', 'stderr'):
        assert digest(folder / (channel + '.raw')) == receipt[channel + '_sha256']
    references += len(paths)
    distinct.update(paths)
    commands.append(dict(label=folder.name, inputs=len(paths), exit=receipt['exit']))

scope = json.loads((OWN / 'SELECTED_ORIGINALS_SCOPED.json').read_text())
assert len(scope) == 1219
assert all(record_v2.original(p) for p in scope)
assert not any('/scouting/' + lane + '/' in p for p in scope
               for lane in ('order_geometry_tenth', 'order_geometry_tenth_desk', 'finite_systems_twentieth'))
for label in ('06_oriented_square', '23_cancellation_circulant'):
    receipt = json.loads((OWN / 'commands' / label / 'receipt.json').read_text())
    assert receipt['argv'][0:4] == ['rg', '-n', '-i', '--']
    assert receipt['argv'][5:] == scope

aliases = json.loads((OWN / 'CONTROL_ALIASES.json').read_text())
for row in aliases['aliases']:
    assert digest(OWN / row['local_copy']) == row['sha256']

canonical = (OWN / 'CANONICAL.raw').read_bytes()
assert canonical == (OWN / 'commands/10_pilot_a/stdout.raw').read_bytes()
assert canonical == (OWN / 'commands/11_pilot_b/stdout.raw').read_bytes()
lines = canonical.decode().splitlines()
assert len(lines) == 845
assert sum(line.startswith('STATE ') for line in lines) == 760
assert lines[-1] == 'DONE states checks 760 2852'
assert not list(OWN.rglob('__pycache__'))

links = 0
for path in sorted(OWN.rglob('*.md')):
    for target in re.findall(r'\]\(([^)]+)\)', path.read_text()):
        if target.startswith(('http://', 'https://', '#')):
            continue
        candidate = target.split('#', 1)[0]
        if not candidate:
            continue
        # Frozen controls retain their historical workspace-relative links.
        if path.parent.name == 'controls':
            continue
        assert (path.parent / candidate).exists(), (path, target)
        links += 1

print(json.dumps(dict(status='DOCUMENTARY_PASS_NOT_REVIEW_OR_ADMISSION',
    completed_native_commands=len(receipts), input_references=references,
    distinct_current_input_paths=len(distinct), refined_originals=len(scope),
    controls=3, canonical_lines=len(lines), complete_state_rows=760,
    structural_checks_per_run=2852, raw_compare_commands=['12_raw_canonical_cmp',
    '15_run_a_raw_canonical_cmp','16_run_b_raw_canonical_cmp'], local_links=links,
    commands=commands), indent=2, sort_keys=True))
