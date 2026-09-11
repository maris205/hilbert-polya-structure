"""Read-only evidence inspection; no dynamical code or author imports."""
from pathlib import Path, PurePosixPath
from html.parser import HTMLParser
import hashlib
import json

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
SCOUT = ROOT / 'docs/papers211_215_sequence/scouting'


def pin(data):
    return {'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()}


def safe(base, name):
    rel = PurePosixPath(name)
    assert not rel.is_absolute() and '..' not in rel.parts and str(rel) == name
    path = base / name
    assert path.is_file() and not path.is_symlink()
    return path


def read(path):
    return json.loads(path.read_bytes())


def check_list(base, path, count):
    rows = []
    for line in path.read_text().splitlines():
        digest, name = line.split('  ', 1)
        result = pin(safe(base, name).read_bytes())
        assert result['sha256'] == digest, name
        rows.append({'path': name, **result})
    assert len(rows) == len({r['path'] for r in rows}) == count
    return rows


def check_seal(base, name, count):
    rows = check_list(base, base / name, count)
    assert not any(p.is_symlink() for p in base.rglob('*'))
    assert {str(p.relative_to(base)) for p in base.rglob('*') if p.is_file()} == {
        name, *(r['path'] for r in rows)}
    return {'payloads': len(rows), 'bytes': sum(r['bytes'] for r in rows),
            'seal': pin((base / name).read_bytes())}


cluster = SCOUT / 'cluster_completion_lane'
cluster_result = check_seal(cluster, 'MANIFEST.sha256', 30)
check_list(ROOT, cluster / 'INPUT_PINS.sha256', 5)
receipt = read(cluster / 'NATIVE_RECEIPT.json')
assert receipt['script_sha256'] == pin((cluster / 'capture_native.py').read_bytes())['sha256']
assert receipt['python']['sha256'] == pin(Path(receipt['python']['path']).read_bytes())['sha256']
for row in receipt['tools'].values():
    assert row['sha256'] == pin(Path(row['path']).read_bytes())['sha256']
commands = receipt['commands']
assert len(commands) == 9
assert [r['returncode'] for r in commands] == [0, 0, 0, 0, 0, 0, 22, 0, 0]
raw_slices = 0
for row in commands:
    assert row['cwd'] == str(ROOT) and 'exception' not in row
    for stream in ('stdout', 'stderr'):
        entry = row[stream]
        assert pin(safe(cluster, entry['path']).read_bytes()) == {k: entry[k] for k in ('bytes', 'sha256')}
    stdout = (cluster / row['stdout']['path']).read_bytes()
    stderr = (cluster / row['stderr']['path']).read_bytes()
    if 'stdout_copy' in row:
        assert stdout == (cluster / row['stdout_copy']).read_bytes()
    argv = row['argv']
    if Path(argv[0]).name == 'sed':
        first, last = map(int, argv[2][:-1].split(','))
        assert stdout == b''.join((ROOT / argv[3]).read_bytes().splitlines(keepends=True)[first-1:last])
        raw_slices += 1
    elif Path(argv[0]).name == 'rg':
        assert argv[1:3] == ['-n', 'CLU']
        expected = b''.join(str(i).encode() + b':' + line for i, line in
                            enumerate((ROOT / argv[3]).read_bytes().splitlines(keepends=True), 1)
                            if b'CLU' in line)
        assert stdout == expected
        assert len(stdout.splitlines()) == 10
        raw_slices += 1
    if row['returncode'] == 22:
        assert b'http_code=401\n' in stdout and b'size_download=0\n' in stdout
        assert b'401' in stderr
    else:
        assert stderr == b''
assert raw_slices == 5
assert (cluster / 'INPUT_PINS.sha256').read_bytes() == (cluster / 'INPUT_AFTER.sha256').read_bytes()
assert not (cluster / 'hone2025_original.pdf').exists()
assert not (cluster / 'raw/08_primary_text.stdout').exists()
cluster_result.update({'history_inputs': 5, 'raw_original_excerpt_pairs': 5,
                       'native_commands': commands, 'native_failed_http': 401})

gcd = SCOUT / 'common_sum_gcd_lane'
gcd_result = check_seal(gcd, 'SHA256SUMS', 31)
check_list(ROOT, gcd / 'HISTORICAL_INPUTS.sha256', 5)
evidence = gcd / 'evidence01'
originals = read(evidence / 'original_capture.json')
assert len(originals) == 5 and sum(r['bytes'] for r in originals) == 72293
for row in originals:
    data = safe(ROOT, row['path']).read_bytes()
    assert data == safe(evidence / 'originals', row['path']).read_bytes()
    assert pin(data) == {k: row[k] for k in ('bytes', 'sha256')}
gcd_commands = []
for path in sorted(evidence.glob('*.command.json')):
    stem = path.name.removesuffix('.command.json')
    command, result = read(path), read(evidence / (stem + '.result.json'))
    assert command['cwd'] == str(ROOT) and result['returncode'] == 0
    for stream in ('stdout', 'stderr'):
        assert pin((evidence / (stem + '.' + stream)).read_bytes()) == {
            k: result[stream + '_' + k] for k in ('bytes', 'sha256')}
    assert (evidence / (stem + '.stderr')).read_bytes() == b''
    gcd_commands.append({'stem': stem, **command, **result})
assert len(gcd_commands) == 3
receipt = read(evidence / 'RECEIPT.json')
assert receipt['native_returncodes'] == [0, 0, 0]
assert receipt['scientific_executions'] == receipt['pilot_states'] == 0


class TextFragments(HTMLParser):
    def __init__(self):
        super().__init__()
        self.fragments = []

    def handle_data(self, value):
        if value.strip():
            self.fragments.append(value.strip())


assert len(receipt['sources']) == 2
for source, stem in zip(receipt['sources'], ('02_harris_louwsma', '03_corrales_valencia')):
    raw = (evidence / (stem + '.html')).read_bytes()
    assert source['returncode'] == 0 and source['present']
    assert pin(raw) == {k: source[k] for k in ('bytes', 'sha256')}
    parser = TextFragments()
    parser.feed(raw.decode('utf-8', errors='replace'))
    expected = ('\n'.join(parser.fragments) + '\n').encode()
    assert expected == (evidence / (stem + '.txt')).read_bytes()
    assert len(expected) == source['text_bytes'] and b'arithmetical' in expected.lower()
gcd_result.update({'historical_raw_pairs': 5, 'historical_bytes': 72293,
                   'native_commands': gcd_commands, 'source_raw_text_derivation_pairs': 2,
                   'sources': receipt['sources']})

print(json.dumps({'status': 'PASS_NEGATIVE_ARTIFACT_ONLY', 'cluster': cluster_result,
                  'gcd': gcd_result, 'new_scientific_executions': 0,
                  'limits': 'No science, independent manuscript review, complete source coverage, or hermetic runtime claim.'},
                 indent=2, sort_keys=True))
