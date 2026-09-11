"""Root-only read-only original-artifact inspection, not scientific execution."""
from pathlib import Path
import hashlib
import json
from html.parser import HTMLParser

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
SCOUT = ROOT / 'docs/papers211_215_sequence/scouting'

def sha(data):
    return hashlib.sha256(data).hexdigest()

def pins(path, base):
    result = {}
    for line in path.read_text().splitlines():
        digest, rel = line.split('  ', 1)
        assert len(digest) == 64 and rel not in result
        assert not Path(rel).is_absolute() and '..' not in Path(rel).parts
        data = (base / rel).read_bytes()
        assert sha(data) == digest, rel
        result[rel] = data
    return result

def inventory(folder, name, count, total, seal):
    assert sha((folder / name).read_bytes()) == seal
    rows = pins(folder / name, folder)
    actual = set()
    for path in folder.rglob('*'):
        assert not path.is_symlink()
        if path.is_file() and path != folder / name:
            actual.add(path.relative_to(folder).as_posix())
    assert actual == rows.keys()
    assert len(rows) == count and sum(map(len, rows.values())) == total
    return rows

f = SCOUT / 'finite_lattice_arithmetic_lane'
frows = inventory(f, 'SHA256SUMS', 26, 174091,
    '50088d6e504fba93baf9f5d6b501d292cd838cb6e9a94378298383525127a455')
fh = pins(f / 'HISTORICAL_INPUTS.sha256', ROOT)
assert len(fh) == 3
originals = json.loads(frows['evidence01/original_capture.json'])
assert [row['path'] for row in originals] == list(fh)
for row in originals:
    data = fh[row['path']]
    assert frows['evidence01/originals/' + row['path']] == data
    assert (row['sha256'], row['bytes'], row['raw_equal']) == (sha(data), len(data), True)
fcodes = []
for rel in sorted(x for x in frows if x.endswith('.command.json')):
    command = json.loads(frows[rel])
    stem = rel.removesuffix('.command.json')
    result = json.loads(frows[stem + '.result.json'])
    assert command['cwd'] == str(ROOT) and command['argv']
    assert command['started_utc'] <= result['ended_utc']
    fcodes.append(result['returncode'])
    for stream in ('stdout', 'stderr'):
        data = frows[stem + '.' + stream]
        assert (len(data), sha(data)) == (result[stream + '_bytes'], result[stream + '_sha256'])
assert fcodes == [0, 0, 0]
assert frows['evidence01/02_historical_pins.stdout'] == ''.join(rel + ': OK\n' for rel in fh).encode()
fr = json.loads(frows['evidence01/RECEIPT.json'])
assert fr['native_returncodes'] == fcodes and fr['scientific_executions'] == 0
assert fr['historical_bytes'] == sum(map(len, fh.values())) == 30555
class Extract(HTMLParser):
    def __init__(self):
        super().__init__()
        self.items = []
    def handle_data(self, text):
        if text.strip():
            self.items.append(text.strip())
parser = Extract()
parser.feed(frows['evidence01/root_formula.html'].decode('utf-8', errors='replace'))
assert ('\n'.join(parser.items) + '\n').encode() == frows['evidence01/root_formula.txt']
for ext, role in [('html', 'html'), ('txt', 'text')]:
    data = frows['evidence01/root_formula.' + ext]
    assert (len(data), sha(data)) == (fr['source'][role + '_bytes'], fr['source'][role + '_sha256'])

p = SCOUT / 'planar_matching_lane'
prows = inventory(p, 'MANIFEST.sha256', 30, 194133,
    '569de512bca6e25647056e3478be317b8bd78bd5f8a4ccc085725fa042069e56')
ph = pins(p / 'HISTORICAL_INPUT_PINS.sha256', ROOT)
assert len(ph) == 6
pr = json.loads(prows['native01/RECEIPT.json'])
assert pr['cwd'] == str(ROOT) and pr['scientific_executions'] == pr['git_commands'] == 0
assert sha(prows['capture_native.py']) == pr['collector_sha256']
for tool in [pr['python'], *pr['tools'].values()]:
    assert sha(Path(tool['path']).read_bytes()) == tool['sha256']
assert len(pr['commands']) == 9
for cmd in pr['commands']:
    assert cmd['exit_code'] == 0 and cmd['start_unix_ns'] <= cmd['end_unix_ns']
    assert cmd['argv'][0] in [v['path'] for v in pr['tools'].values()]
    for stream in ('stdout', 'stderr'):
        ref = cmd[stream]
        data = prows['native01/' + ref['path']]
        assert (len(data), sha(data)) == (ref['size'], ref['sha256'])
    assert prows['native01/' + cmd['stderr']['path']] == b''
assert prows['native01/01_historical_before.stdout'] == prows['native01/08_historical_after.stdout'] == prows['HISTORICAL_INPUT_PINS.sha256']
for tag, rel, spans in [
    ('02_p130_excerpt', list(ph)[0], [(1,310)]),
    ('03_p144_excerpt', list(ph)[1], [(1,270),(285,353)]),
    ('04_old_m01_excerpt', list(ph)[2], [(44,177)]),
    ('05_old_motzkin_excerpt', list(ph)[3], [(65,88)]),
]:
    lines = ph[rel].splitlines(keepends=True)
    expected = b''.join(b''.join(lines[a-1:b]) for a,b in spans)
    assert expected == prows['native01/' + tag + '.stdout']
assert pr['commands'][-1]['argv'] == ['/usr/bin/cmp', '-s',
    str(p / 'native01/01_historical_before.stdout'), str(p / 'native01/08_historical_after.stdout')]
assert prows['native01/09_historical_raw_cmp.stdout'] == b''
# Re-read complete seals/history at end; no author code is imported or executed.
assert inventory(f, 'SHA256SUMS', 26, 174091, sha((f/'SHA256SUMS').read_bytes())) == frows
assert inventory(p, 'MANIFEST.sha256', 30, 194133, sha((p/'MANIFEST.sha256').read_bytes())) == prows
assert pins(f / 'HISTORICAL_INPUTS.sha256', ROOT) == fh
assert pins(p / 'HISTORICAL_INPUT_PINS.sha256', ROOT) == ph
print(json.dumps({'status':'PASS_ROOT_ARTIFACT_ONLY',
 'lattice':{'payloads':26,'bytes':174091,'original_raw_pairs':3,'native_exit_codes':fcodes,'derived_source_raw_pairs':1},
 'planar':{'payloads':30,'bytes':194133,'history_pins':6,'native_exit_codes':[0]*9,'old_excerpt_raw_pairs':4,'checksum_raw_pair':True},
 'scientific_executions':0,'builds':0,'visual_reviews':0,'git_commands':0}, sort_keys=True))
