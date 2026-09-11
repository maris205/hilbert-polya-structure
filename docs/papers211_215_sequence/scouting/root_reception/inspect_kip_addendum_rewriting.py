"""Read-only root source/negative-desk reception; no scientific evaluation."""
from pathlib import Path
import hashlib
import json
import shlex
import datetime

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
SCOUT = ROOT / 'docs/papers211_215_sequence/scouting'
A = SCOUT / 'kip_candidate_gate_source_addendum'
R = SCOUT / 'finite_rewriting_residual_lane'
G = SCOUT / 'kip_candidate_gate'

def raw(path):
    return Path(path).read_bytes()

def pin(value):
    return {'bytes':len(value), 'sha256':hashlib.sha256(value).hexdigest()}

def verify(row):
    value = raw(row['path'])
    assert pin(value) == {key:row[key] for key in ('bytes','sha256')}
    return value

def inventory(folder, name, count, total, digest):
    assert pin(raw(folder/name))['sha256'] == digest
    entries = {}
    for line in raw(folder/name).decode().splitlines():
        h, rel = line.split('  ',1)
        assert rel not in entries and not Path(rel).is_absolute() and '..' not in Path(rel).parts
        value = raw(folder/rel)
        assert pin(value)['sha256'] == h
        entries[rel] = value
    members = set()
    for path in folder.rglob('*'):
        assert not path.is_symlink()
        if path.is_file() and path != folder/name:
            members.add(path.relative_to(folder).as_posix())
    assert members == entries.keys() and len(entries) == count and sum(map(len,entries.values())) == total
    return entries

specs = [(A,'SHA256SUMS',22,1237420,'36dd5dfaef11e2b12c41d9c3f63a4f7ed68586c34d983b4035a4d100dfcc7095'),
 (R,'MANIFEST.sha256',4,69708,'5b4d0f8505049cc598aa42bc639e6a68e4ab075eb9daa84363fa1961ec9a74dd'),
 (G,'SHA256SUMS',78,2017173,'11cc87ac615849ae33718ff63edde8b43b6456343d046e4d2a19717e41eebeda')]
a,r,g = [inventory(*x) for x in specs]
p = json.loads(a['SOURCE_PINS.json'])
assert p['scientific_invocations'] == 0
assert p['gate_before'] == p['gate_after'] == {'manifest':{'path':str(G/'SHA256SUMS'),**pin(raw(G/'SHA256SUMS'))},
 'payload_files':78,'payload_bytes':2017173}
assert len(p['historical_anchors']) == 2
for row in p['historical_anchors']:
    assert row['raw_equal'] is True and verify(row['source']) == verify(row['copy'])
assert [row['version'] for row in p['sources']] == ['v1','v3']
for row, errsize in zip(p['sources'],(633,712)):
    body = verify(row['body'])
    receipt = json.loads(a[row['native_receipt']])
    assert receipt['exit_code'] == 0 and receipt['cwd'] == str(A)
    assert datetime.datetime.fromisoformat(receipt['started_utc']) <= datetime.datetime.fromisoformat(receipt['ended_utc'])
    assert receipt['argv'] == ['curl','--fail','--location','--max-time','30','--output',row['body']['path'],row['url']]
    assert row['url'] == 'https://arxiv.org/html/2604.15497'+row['version']
    assert verify(receipt['stdout']) == b'' and len(verify(receipt['stderr'])) == errsize
    assert b'<html' in body and b'2604.15497'+row['version'].encode() in body
assert len(p['browser_records']) == 7
for row in p['browser_records']:
    record = json.loads(verify(row['container']))
    assert record['tool'] == 'web.run'
    text = record['returned_text'].encode()
    assert pin(text) == {'bytes':row['decoded_utf8_bytes'],'sha256':row['decoded_utf8_sha256']}

pins = r['HISTORICAL_INPUT_PINS.sha256'].decode()
assert len(pins.splitlines()) == 3
for line in pins.splitlines():
    h,rel = line.split('  ',1)
    assert pin(raw(ROOT/rel))['sha256'] == h
records = json.loads(r['OLD_READ_RECORDS.json'])['records']
assert len(records) == 4
for row in records:
    assert row['result']['exit_code'] == 0
    args = shlex.split(row['cmd'])
    if args[0] == 'sed':
        assert args[1] == '-n' and len(args) == 4 and args[2].endswith('p')
        start,end = map(int,args[2][:-1].split(','))
        assert row['result']['output'] == ''.join(raw(ROOT/args[3]).decode().splitlines(keepends=True)[start-1:end])
    else:
        assert args[0] == 'sha256sum' and row['result']['output'] == pins
assert [inventory(*x) for x in specs] == [a,r,g]
print(json.dumps({'status':'PASS_ROOT_SOURCE_AND_ZERO_LITERAL_ORIGINALS',
 'addendum_payloads':22,'addendum_bytes':1237420,'original_gate_unchanged':78,
 'anchor_raw_pairs':2,'native_download_bindings':2,'decoded_browser_returns':7,
 'rewriting_payloads':4,'rewriting_bytes':69708,'history_pins':3,
 'decoded_native_records':4,'decoded_original_slice_pairs':3,
 'new_science':0,'new_closed_attempts':0},sort_keys=True))
