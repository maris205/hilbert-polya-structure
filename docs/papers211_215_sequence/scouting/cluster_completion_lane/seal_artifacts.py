#!/usr/bin/env python3
"""Single-use author artifact seal, deliberately not a scientific verifier."""
from pathlib import Path
import hashlib
import json

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
OUT = ROOT / 'docs/papers211_215_sequence/scouting/cluster_completion_lane'
MANIFEST = OUT / 'MANIFEST.sha256'
AUDIT = OUT / 'AUTHOR_ARTIFACT_CHECK.json'
assert not MANIFEST.exists() and not AUDIT.exists(), 'Preserve existing seals.'
def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

receipt = json.loads((OUT / 'NATIVE_RECEIPT.json').read_text())
assert receipt['script_sha256'] == sha(OUT / 'capture_native.py')
commands = receipt['commands']
assert len(commands) == 9
assert [c['returncode'] for c in commands] == [0, 0, 0, 0, 0, 0, 22, 0, 0]
for command in commands:
    for channel in ['stdout', 'stderr']:
        entry = command[channel]
        path = OUT / entry['path']
        assert sha(path) == entry['sha256']
        assert path.stat().st_size == entry['bytes']
    if 'stdout_copy' in command:
        assert (OUT / command['stdout_copy']).read_bytes() == (OUT / command['stdout']['path']).read_bytes()
before = (OUT / 'INPUT_PINS.sha256').read_bytes()
assert before == (OUT / 'INPUT_AFTER.sha256').read_bytes()
pins = before.decode().splitlines()
assert len(pins) == 5
for line in pins:
    expected, relative = line.split('  ', 1)
    assert sha(ROOT / relative) == expected, relative
assert commands[-1]['name'] == '10_raw_pin_comparison'
assert b'http_code=401\n' in (OUT / 'raw/07_primary_pdf.stdout').read_bytes()
assert b'size_download=0\n' in (OUT / 'raw/07_primary_pdf.stdout').read_bytes()
assert not (OUT / 'raw/08_primary_text.stdout').exists()
AUDIT.write_text(json.dumps({
    'kind': 'author artifact check only; not independent review',
    'historical_input_pins_checked': 5,
    'native_command_records_checked': 9,
    'native_successes': 8,
    'preserved_native_failures': {'07_primary_pdf': {'returncode': 22, 'http_code': 401}},
    'historical_before_after': 'byte-equal, also native cmp exit zero',
    'scientific_runs': 0,
    'literal_attempts': 1,
    'repeated_literals': 1,
    'fresh_candidates': 0,
    'retained_candidates': 0,
    'reserves': 0,
    'new_paper_numbers': 0,
}, indent=2) + '\n')
paths = sorted(p for p in OUT.rglob('*') if p.is_file() and p != MANIFEST)
MANIFEST.write_text(''.join(f'{sha(p)}  {p.relative_to(OUT)}\n' for p in paths))
assert set(OUT.rglob('*')) >= set(paths)
print(json.dumps({'payload_files': len(paths),
    'payload_bytes': sum(p.stat().st_size for p in paths),
    'historical_pins': len(pins), 'manifest_sha256': sha(MANIFEST),
    'manifest_excludes': ['MANIFEST.sha256'], 'scientific_runs': 0}))
