"""Root documentary integrity audit only; never imports/runs scientific code."""
from pathlib import Path
from hashlib import sha256
import json
import re

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
BASE = ROOT/'docs/papers211_215_sequence/scouting/finite_word_tree_new_desk'

def digest(data):
    return {'sha256': sha256(data).hexdigest(), 'bytes': len(data)}

def rows(raw):
    assert raw.endswith(b'\n')
    found = {}
    for line in raw.decode().splitlines():
        match = re.fullmatch(r'([0-9a-f]{64})  (.+)', line)
        assert match, line
        pin, name = match.groups()
        path = Path(name)
        assert path.parts and not path.is_absolute() and '..' not in path.parts
        assert name not in found and name != 'MANIFEST.sha256'
        found[name] = pin
    return found

manifest = (BASE/'MANIFEST.sha256').read_bytes()
payloads = rows(manifest)
actual = set()
for path in BASE.rglob('*'):
    assert not path.is_symlink(), str(path)
    if path.is_file():
        actual.add(path.relative_to(BASE).as_posix())
assert actual == set(payloads) | {'MANIFEST.sha256'}
assert len(payloads) == 5
before = {name: (BASE/name).read_bytes() for name in payloads}
assert all(sha256(before[name]).hexdigest() == pin for name, pin in payloads.items())
historical = rows(before['HISTORICAL_INPUT_PINS.sha256'])
assert len(historical) == 3
originals = {name: (ROOT/name).read_bytes() for name in historical}
assert all(sha256(originals[name]).hexdigest() == pin for name, pin in historical.items())
old = json.loads(before['OLD_READ_RECORDS.json'])
document = json.loads(before['DOCUMENTARY_CHECK.json'])
primary = json.loads(before['PRIMARY_RETURNS.json'])
assert len(old) == 6 and len(document['rereads']) == 4 and len(primary) == 2
assert document['old_archive_decoded_equal'] is True
assert document['primary_archive_decoded_equal'] is True
assert document['jq_availability_failure']['exit_code'] == 1
assert document['pins']['exit_code'] == 0
assert document['pins']['output'] == ''.join(name+': OK\n' for name in historical)
excerpts = []
for index, record in enumerate(old):
    result = record['result']
    assert result['exit_code'] == 0
    assert record['cwd'] == str(ROOT)
    if index < 4:
        match = re.fullmatch(r"sed -n '(\d+),(\d+)p' (.+)", record['cmd'])
        assert match
        start, end, name = match.groups()
        assert name in originals
        excerpt = ''.join(originals[name].decode().splitlines(keepends=True)[int(start)-1:int(end)])
        assert result['output'] == excerpt
        repeat = document['rereads'][index]
        assert repeat['cmd'] == record['cmd'] and repeat['result']['exit_code'] == 0
        assert repeat['result']['output'] == excerpt
        excerpts.append({'path': name, 'first_line': int(start), 'last_line': int(end),
                         'decoded_utf8_excerpt': digest(excerpt.encode())})
    elif index == 4:
        assert result['output'] == before['HISTORICAL_INPUT_PINS.sha256'].decode()
    else:
        assert record['cmd'] == 'df -B1 .'
for item in primary:
    assert isinstance(item['request'], dict) and isinstance(item['returned'], str)
    assert 'https://arxiv.org/html/' in item['returned']
assert all((ROOT/name).read_bytes() == content for name, content in originals.items())
assert all((BASE/name).read_bytes() == content for name, content in before.items())
assert (BASE/'MANIFEST.sha256').read_bytes() == manifest
print(json.dumps({'status': 'PASS_WORD_TREE_DOCUMENTARY_RECEPTION',
 'scope': 'Complete saved payloads/pins and decoded native excerpt bindings; not new science or raw HTTP verification.',
 'payloads': len(payloads), 'payload_bytes': sum(map(len,before.values())),
 'manifest': digest(manifest), 'historical_inputs': len(historical),
 'old_command_records': len(old), 'repeated_excerpts': len(excerpts),
 'provider_return_batches': len(primary), 'excerpts': excerpts,
 'failed_jq_native_exit_preserved': 1, 'new_literals': 0, 'new_science': 0,
 'closed_attempt_increment': 0}, sort_keys=True, indent=2))
