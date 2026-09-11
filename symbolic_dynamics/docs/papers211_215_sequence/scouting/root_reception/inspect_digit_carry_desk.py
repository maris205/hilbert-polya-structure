"""Root documentary reception only; no scientific implementation is imported."""
from pathlib import Path
from hashlib import sha256
import json
import re

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
BASE = ROOT/'docs/papers211_215_sequence/scouting/digit_carry_fresh_desk'


def digest(raw):
    return {'sha256': sha256(raw).hexdigest(), 'bytes': len(raw)}


def rows(raw):
    assert raw.endswith(b'\n')
    result = {}
    for line in raw.decode().splitlines():
        match = re.fullmatch(r'([0-9a-f]{64})  (.+)', line)
        assert match, line
        pin, name = match.groups()
        path = Path(name)
        assert path.parts and not path.is_absolute() and '..' not in path.parts
        assert name not in result and name != 'MANIFEST.sha256'
        result[name] = pin
    return result


manifest = (BASE/'MANIFEST.sha256').read_bytes()
payloads = rows(manifest)
actual = set()
for path in BASE.rglob('*'):
    assert not path.is_symlink(), str(path)
    if path.is_file():
        actual.add(path.relative_to(BASE).as_posix())
assert actual == set(payloads) | {'MANIFEST.sha256'} and len(payloads) == 5
before = {name: (BASE/name).read_bytes() for name in payloads}
assert all(sha256(before[name]).hexdigest() == pin for name, pin in payloads.items())
historical = rows(before['HISTORICAL_INPUT_PINS.sha256'])
assert len(historical) == 4
originals = {name: (ROOT/name).read_bytes() for name in historical}
assert all(sha256(originals[name]).hexdigest() == pin for name, pin in historical.items())
old = json.loads(before['OLD_READ_RECORDS.json'])['records']
doc = json.loads(before['DOCUMENTARY_CHECK.json'])
primary = json.loads(before['PRIMARY_RETURNS.json'])
assert len(old) == len(doc['old_excerpt_comparisons']) == 4
excerpts = []
for record, repeat in zip(old, doc['old_excerpt_comparisons']):
    name, start, end = record['path'], record['start'], record['end']
    assert name in originals and 1 <= start <= end
    request, native = record['request'], record['returned']
    assert request['workdir'] == str(ROOT)
    assert request['cmd'] == f"sed -n '{start},{end}p' {name}"
    assert native['exit_code'] == 0
    excerpt = ''.join(originals[name].decode().splitlines(keepends=True)[start-1:end])
    assert native['output'] == excerpt
    assert repeat == {'id': record['id'], 'path': name, 'range': [start, end],
                      'read_again_exit_code': 0, 'decoded_output_equal': True}
    excerpts.append({'path': name, 'first_line': start, 'last_line': end,
                     'decoded_utf8_excerpt': digest(excerpt.encode())})
assert len(doc['readbacks']) == 2
for readback in doc['readbacks']:
    assert readback['name'] in ('OLD_READ_RECORDS.json', 'PRIMARY_RETURNS.json')
    assert readback['exit_code'] == 0 and readback['equal'] is True
    assert readback['request']['workdir'] == str(BASE)
    assert readback['request']['cmd'] == "sed -n '1,999p' " + readback['name']
pins = doc['historical_pin_recheck']
assert pins['request']['workdir'] == str(ROOT)
assert pins['request']['cmd'] == 'sha256sum -c ' + str((BASE/'HISTORICAL_INPUT_PINS.sha256').relative_to(ROOT))
assert pins['returned']['exit_code'] == 0
assert pins['returned']['output'] == ''.join(name+': OK\n' for name in historical)
failure = doc['packaging_failure']
assert failure['request']['workdir'] == str(BASE) and failure['returned']['exit_code'] == 1
assert 'No such file or directory' in failure['returned']['output']
assert len(primary['discovery_queries']) == 7 and len(primary['failure_excerpts']) == 4
body = primary['selected_primary_return']['returned']
assert len(primary['selected_primary_return']['request']['open']) == 2
assert isinstance(body, str) and 'L581:' in body and 'L128@P3:' in body and 'L192@P4:' in body
assert set(primary['reference_url_map'].values()) == {
    'https://arxiv.org/html/1503.08816', 'https://www.math.ias.edu/~goresky/MWC.pdf'}
for failed in primary['failure_excerpts']:
    assert isinstance(failed['parent_request'], dict)
    assert failed['selection']['method'] == 'exact substring separated by provider separator; no normalization'
    assert 'Internal Error' in failed['returned_excerpt'] or 'Checking your browser' in failed['returned_excerpt']
assert len(primary['read_limits']) == 4
assert all((ROOT/name).read_bytes() == content for name, content in originals.items())
assert all((BASE/name).read_bytes() == content for name, content in before.items())
assert (BASE/'MANIFEST.sha256').read_bytes() == manifest
print(json.dumps({'status': 'PASS_DIGIT_CARRY_DOCUMENTARY_RECEPTION',
    'scope': 'Complete saved payloads, historical bytes, native decoded excerpts and bounded source returns; no new science or raw HTTP equality.',
    'payloads': len(payloads), 'payload_bytes': sum(map(len, before.values())),
    'manifest': digest(manifest), 'historical_inputs': len(historical),
    'old_native_commands': len(old), 'repeated_excerpt_claims_checked': 4,
    'actual_pin_native_commands': 1, 'preserved_packaging_failure_native_commands': 1,
    'provider_return_batches': 1, 'provider_failure_excerpts': 4, 'discovery_queries': 7,
    'excerpts': excerpts, 'new_literals': 0, 'new_science': 0,
    'closed_attempt_increment': 0}, sort_keys=True, indent=2))
