"""Independent read-only PRE packet bindings; no mathematical execution."""
from pathlib import Path, PurePosixPath
import hashlib
import json

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
BASE = ROOT / 'docs/papers211_215_sequence/scouting/parallel_run_erasure_lane'
EVIDENCE = BASE / 'evidence01'


def pin(path):
    raw = path.read_bytes()
    return {'bytes': len(raw), 'sha256': hashlib.sha256(raw).hexdigest()}


def safe(base, name):
    rel = PurePosixPath(name)
    assert not rel.is_absolute() and '..' not in rel.parts and str(rel) == name
    path = base / name
    assert path.is_file() and not path.is_symlink()
    return path


assert not any(p.is_symlink() for p in BASE.rglob('*'))
manifest = {}
for line in (BASE / 'SHA256SUMS').read_text().splitlines():
    digest, name = line.split('  ', 1)
    assert name not in manifest
    assert pin(safe(BASE, name))['sha256'] == digest
    manifest[name] = digest
assert len(manifest) == 31
assert {str(p.relative_to(BASE)) for p in BASE.rglob('*') if p.is_file()} == {
    'SHA256SUMS', *manifest}
originals = json.loads((EVIDENCE / 'original_capture.json').read_bytes())
assert len(originals) == len({r['path'] for r in originals}) == 5
for row in originals:
    source = safe(ROOT, row['path'])
    assert pin(source) == {k: row[k] for k in ('bytes', 'sha256')}
    assert source.read_bytes() == safe(EVIDENCE / 'originals', row['path']).read_bytes()
    assert row['raw_equal'] is True
assert (BASE / 'HISTORICAL_INPUTS.sha256').read_bytes() == ''.join(
    r['sha256'] + '  ' + r['path'] + '\n' for r in originals).encode()
native = []
for command_path in sorted(EVIDENCE.glob('*.command.json')):
    row = json.loads(command_path.read_bytes())
    name = command_path.name.removesuffix('.command.json')
    result = json.loads((EVIDENCE / (name + '.result.json')).read_bytes())
    assert row['cwd'] == str(ROOT) and result['returncode'] == 0
    streams = {}
    for stream in ('stdout', 'stderr'):
        path = EVIDENCE / (name + '.' + stream)
        streams[stream] = pin(path)
        assert streams[stream] == {'bytes': result[stream + '_bytes'],
                                   'sha256': result[stream + '_sha256']}
    assert (EVIDENCE / (name + '.stderr')).read_bytes() == b''
    native.append({'command': row, 'result': result, 'streams': streams})
assert len(native) == 4
assert [Path(r['command']['argv'][0]).name for r in native] == ['rg', 'sha256sum', 'curl', 'pdftotext']
assert (EVIDENCE / '02_historical_pins.stdout').read_bytes() == ''.join(
    r['path'] + ': OK\n' for r in originals).encode()
receipt = json.loads((EVIDENCE / 'RECEIPT.json').read_bytes())
assert receipt['native_returncodes'] == [0, 0, 0, 0]
assert receipt['scientific_executions'] == 0 and receipt['literal_attempts'] == 1
assert receipt['historical_originals'] == receipt['historical_raw_pairs'] == 5
assert receipt['historical_bytes'] == sum(r['bytes'] for r in originals)
for ext, name in [('pdf', 'pdf'), ('txt', 'text')]:
    assert pin(EVIDENCE / ('1261.' + ext)) == {
        'bytes': receipt['source'][name + '_bytes'],
        'sha256': receipt['source'][name + '_sha256']}
assert (EVIDENCE / '1261.pdf').read_bytes().startswith(b'%PDF-')
print(json.dumps({'status': 'PASS_NEGATIVE_ARCHIVE_ONLY', 'payloads': 31,
                  'payload_bytes': sum(pin(BASE / n)['bytes'] for n in manifest),
                  'seal': pin(BASE / 'SHA256SUMS'), 'historical_raw_pairs': 5,
                  'native': native, 'actual_checksum_output_raw_pair': True,
                  'scientific_executions': 0,
                  'limits': 'No mathematical replay, source extraction rerun, page viewing or hermetic-runtime claim.'},
                 indent=2, sort_keys=True))
