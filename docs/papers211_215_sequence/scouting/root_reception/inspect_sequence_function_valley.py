"""Read-only root artifact reception; no candidate or historical evaluator."""
from pathlib import Path, PurePosixPath
import hashlib
import json
import re

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
SCOUT = ROOT / 'docs/papers211_215_sequence/scouting'


def sha(data):
    return hashlib.sha256(data).hexdigest()


def pin(path):
    data = path.read_bytes()
    return {'bytes': len(data), 'sha256': sha(data)}


def read(path):
    return json.loads(path.read_bytes())


def safe(base, rel):
    parts = PurePosixPath(rel)
    assert not parts.is_absolute() and '..' not in parts.parts and str(parts) == rel
    path = base / rel
    assert path.is_file() and not path.is_symlink(), path
    return path


def text_pins(base, manifest):
    rows = {}
    for line in manifest.read_text().splitlines():
        digest, rel = line.split('  ', 1)
        assert re.fullmatch('[0-9a-f]{64}', digest) and rel not in rows
        assert sha(safe(base, rel).read_bytes()) == digest, rel
        rows[rel] = digest
    return rows


def full_seal(base, name, expected):
    if name.endswith('.json'):
        entries = read(base / name)['files']
        rows = {}
        for entry in entries:
            rel = entry['path']
            assert rel not in rows and rel != name
            assert pin(safe(base, rel)) == {k: entry[k] for k in ('bytes', 'sha256')}
            rows[rel] = entry['sha256']
    else:
        rows = text_pins(base, base / name)
    all_paths = list(base.rglob('*'))
    assert not any(p.is_symlink() for p in all_paths)
    actual = {str(p.relative_to(base)) for p in all_paths if p.is_file() and p.name != name}
    assert set(rows) == actual and len(rows) == expected
    return {'payloads': len(rows), 'payload_bytes': sum((base / r).stat().st_size for r in rows),
            'seal': pin(base / name)}


sequence = SCOUT / 'sequence_combinatorics_lane'
seq = full_seal(sequence, 'MANIFEST.sha256', 11)
seq['historical_pins'] = len(text_pins(ROOT, sequence / 'HISTORY_INPUTS.sha256'))
assert seq['historical_pins'] == 12
# These stored outputs are discovery/documentation, including original failures
# and originally truncated displays. Reading metadata does not assert body review.
native_reads = read(sequence / 'evidence/NATIVE_READS.json')
seq['native_categories'] = {key: len(value) if isinstance(value, list) else type(value).__name__
                            for key, value in native_reads.items()}

function = SCOUT / 'finite_function_lane'
fun = full_seal(function, 'SHA256SUMS', 35)
history = text_pins(ROOT, function / 'HISTORICAL_INPUTS.sha256')
copies = read(function / 'evidence01/original_capture.json')
assert len(history) == len(copies) == 9 and set(history) == {r['path'] for r in copies}
for row in copies:
    original = safe(ROOT, row['path'])
    copied = safe(function / 'evidence01/originals', row['path'])
    assert original.read_bytes() == copied.read_bytes()
    assert pin(original) == {k: row[k] for k in ('bytes', 'sha256')}
    assert row['sha256'] == history[row['path']] and row['raw_equal'] is True
commands = sorted((function / 'evidence01').glob('*.command.json'))
assert len(commands) == 4
for path in commands:
    stem = str(path)[:-len('.command.json')]
    result = read(Path(stem + '.result.json'))
    assert result['returncode'] == 0
    for field in ('stdout', 'stderr'):
        raw = Path(stem + '.' + field).read_bytes()
        assert len(raw) == result[field + '_bytes'] and sha(raw) == result[field + '_sha256']
receipt = read(function / 'evidence01/RECEIPT.json')
assert receipt['command_returncodes'] == [0] * 4
assert receipt['historical_input_count'] == 9 and receipt['historical_input_bytes'] == 88470
assert receipt['scientific_executions'] == receipt['pilot_boxes'] == 0
fun.update(historical_pins=9, raw_copy_pairs=9, native_commands=4,
           native_argv=[read(p)['argv'] for p in commands])

valley = SCOUT / 'valley_absorption_lane'
val = full_seal(valley, 'MANIFEST.json', 41)
inputs = read(valley / 'INPUT_PINS.json')['inputs']
assert len(inputs) == len({r['source'] for r in inputs}) == 8
for row in inputs:
    original, copied = safe(ROOT, row['source']), safe(valley, row['snapshot'])
    assert original.read_bytes() == copied.read_bytes()
    assert pin(original) == {k: row[k] for k in ('bytes', 'sha256')}
commands = read(valley / 'native/COMMANDS.json')
assert len(commands) == 7 and [r['exit'] for r in commands] == [0] * 6 + [22]
for i, record in enumerate(commands, 1):
    assert read(valley / f'native/{i:02d}.record.json') == record
    assert record['timeout'] is False and record['cwd'] == str(valley)
    assert pin(Path(record['executable'])) == record['executable_pin']
    safe(valley, record['stdout']).read_bytes()
    safe(valley, record['stderr']).read_bytes()
    if record['argv'][0] == 'sed':
        first, last = map(int, record['argv'][2][:-1].split(','))
        expected = b''.join(Path(record['argv'][3]).read_bytes().splitlines(keepends=True)[first-1:last])
        assert expected == (valley / record['stdout']).read_bytes()
receipt = read(valley / 'native/CAPTURE_RECEIPT.json')
assert receipt['producer'] == pin(valley / 'capture.py')
assert receipt['python_pin'] == pin(Path(receipt['python']))
assert receipt['commands'] == 7 and receipt['scientific_runs'] == 0
assert receipt['inputs_before_after_unchanged_and_raw_equal_copies'] == 8
assert not (valley / 'sources/huffman_1952.pdf').exists()
assert b'406' in (valley / 'native/07.stderr').read_bytes()
val.update(raw_copy_pairs=8, native_commands=7, native_exits=[r['exit'] for r in commands],
           raw_original_stdout_slices=2)

print(json.dumps({'status': 'PASS_NEGATIVE_ARTIFACT_RECEPTION_ONLY',
                  'sequence': seq, 'function': fun, 'valley': val,
                  'scientific_runs': 0,
                  'limits': 'Post-read integrity/raw comparisons only. No hermetic runtime, new science, novelty clearance, candidate gate or manuscript acceptance.'},
                 indent=2, sort_keys=True))
