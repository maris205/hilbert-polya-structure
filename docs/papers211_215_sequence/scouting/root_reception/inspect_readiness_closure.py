"""Scoped root integrity checks only; never imports or executes science."""
from pathlib import Path
import hashlib
import json
import re
import shlex

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
B = ROOT/'docs/papers211_215_sequence'
P = B/'qa/runtime_readiness'
C = B/'scouting/finite_closure_incidence_residual'

def raw(path):
    return Path(path).read_bytes()

def sha(value):
    return hashlib.sha256(value).hexdigest()

def seal(folder,name,count,total,digest):
    assert sha(raw(folder/name)) == digest
    payload = {}
    for line in raw(folder/name).decode().splitlines():
        h, rel = line.split('  ',1)
        assert rel not in payload and not Path(rel).is_absolute() and '..' not in Path(rel).parts
        payload[rel] = raw(folder/rel)
        assert sha(payload[rel]) == h
    members = set()
    for file in folder.rglob('*'):
        assert not file.is_symlink()
        if file.is_file() and file != folder/name:
            members.add(file.relative_to(folder).as_posix())
    assert members == payload.keys() and len(payload) == count and sum(map(len,payload.values())) == total
    return payload

def input_rows(text,count):
    rows = [line.split('  ',1) for line in text.splitlines()]
    assert len(rows) == count and len({row[1] for row in rows}) == count
    for h,rel in rows:
        assert sha(raw(ROOT/rel)) == h
    return rows

def excerpt(row):
    assert row['result']['exit_code'] == 0
    args = shlex.split(row['cmd'])
    assert args[:2] == ['sed','-n'] and len(args) == 4 and args[2].endswith('p')
    a,b = map(int,args[2][:-1].split(','))
    assert row['result']['output'] == ''.join(raw(ROOT/args[3]).decode().splitlines(keepends=True)[a-1:b])

def apply_recorded_diff(row):
    assert row['result']['exit_code'] == 1
    args = shlex.split(row['cmd'])
    assert args[:2] == ['diff','-u'] and len(args) == 4
    old,new = [raw(ROOT/x).decode().splitlines(keepends=True) for x in args[2:]]
    diff = row['result']['output'].splitlines(keepends=True)
    assert diff[0].startswith('--- '+args[2]+'\t') and diff[1].startswith('+++ '+args[3]+'\t')
    cursor = 0
    result = []
    index = 2
    while index < len(diff):
        m = re.match(r'@@ -(\d+)(?:,(\d+))? \+(\d+)(?:,(\d+))? @@',diff[index])
        assert m, diff[index]
        a,na,b,nb = int(m[1]),int(m[2] or 1),int(m[3]),int(m[4] or 1)
        start = a-1 if na else a
        result.extend(old[cursor:start]); cursor = start
        before,newcount = cursor,0
        assert len(result) == (b-1 if nb else b)
        index += 1
        while index < len(diff) and not diff[index].startswith('@@ '):
            line = diff[index]; index += 1
            assert line[0] in ' +-'
            if line[0] in ' -':
                assert old[cursor] == line[1:]
                cursor += 1
            if line[0] in ' +':
                result.append(line[1:]); newcount += 1
        assert cursor-before == na and newcount == nb
    result.extend(old[cursor:])
    assert result == new

specs = [(P,'MANIFEST.sha256',5,105360,'5c75ee41642a1c9f886f345c00d1323f1c72395713d0db3f1898a404f97990f7'),
 (C,'MANIFEST.sha256',4,93370,'3a61b5a404d9141b191cbce2c9048788bc9f22e93970233ce380f6594f4cebb8')]
p,c = [seal(*x) for x in specs]
pt = p['INPUTPINS.sha256'].decode(); rows = input_rows(pt,23)
identity = json.loads(p['IDENTITY_CHECKS.json'])
for key in ('before','after'):
    assert identity[key]['result']['exit_code'] == 0 and identity[key]['result']['output'] == pt
    assert shlex.split(identity[key]['cmd']) == ['sha256sum',*[rel for h,rel in rows]]
assert len(identity['comparisons']) == 5
for row in identity['comparisons']:
    assert row['result']['exit_code'] == 0 and row['result']['output'] == ''
    args = shlex.split(row['cmd'])
    assert args[:2] == ['/usr/bin/cmp','--'] and len(args) == 4
    assert raw(ROOT/args[2]) == raw(ROOT/args[3])
assert len(identity['expected_source_diffs']) == 2
for row in identity['expected_source_diffs']:
    apply_recorded_diff(row)
warnings = json.loads(p['PRESEAL_CHECKS.json'])
old = warnings['format_warning_preserved']
assert old['initial_inputpins_decoded_ascii'] == pt+'\n'
assert old['readback_result']['output'] == pt+'\n' and old['readback_result']['exit_code'] == 0
clean = ''.join(rel+': OK\n' for h,rel in rows)
assert old['result']['exit_code'] == 0 and old['result']['output'] == clean+'sha256sum: WARNING: 1 line is improperly formatted\n'
assert warnings['corrected_pin_check']['result']['exit_code'] == 0
assert warnings['corrected_pin_check']['result']['output'] == clean

ct = c['INPUTPINS.sha256'].decode(); rows = input_rows(ct,10)
reads = json.loads(c['OLD_READ_RECORDS.json'])
for key in ('hash_before','hash_after'):
    assert reads[key]['result']['exit_code'] == 0 and reads[key]['result']['output'] == ct
    assert shlex.split(reads[key]['cmd']) == ['sha256sum',*[rel for h,rel in rows]]
assert len(reads['closing_excerpts']) == 6 and len(reads['additional_excerpts']) == 3
for row in reads['closing_excerpts']+reads['additional_excerpts']:
    excerpt(row)
assert [seal(*x) for x in specs] == [p,c]
print(json.dumps({'status':'PASS_ROOT_PLAN_AND_ZERO_LITERAL_ARCHIVES',
 'readiness_payloads':5,'readiness_bytes':105360,'readiness_input_pins':23,
 'native_source_cmp_bindings':5,'old_source_diff_hunks_reconstructed':2,
 'initial_pin_warning_preserved':True,'closure_payloads':4,'closure_bytes':93370,
 'closure_old_pins':10,'closure_original_excerpt_pairs':9,
 'new_science':0,'new_builds':0,'new_closed_literals':0,
 'runtime_adapter_approved':False},sort_keys=True))
