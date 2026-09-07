"""Root complete negative-desk evidence check; no matrix rule executes."""
from pathlib import Path
import hashlib
import json
import runpy

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
BASE = ROOT / 'docs/papers204_208_sequence/scouting/finite_systems_twenty_eighth'
SEAL = '6c35eb1e6204bc91acb64016dde6efc98f84cfc5ed8ed0f0a0daa4cb3ee5a376'
pins = {}
def read(path):
    p = Path(path)
    assert p.is_file(), str(p)
    raw = p.read_bytes()
    row = (hashlib.sha256(raw).hexdigest(), str(p.resolve()))
    assert str(p) not in pins or pins[str(p)] == row, str(p)
    pins[str(p)] = row
    return raw
def h(path):
    return hashlib.sha256(read(path)).hexdigest()
def obj(path):
    return json.loads(read(path))
def closure():
    assert h(BASE/'SHA256SUMS') == SEAL
    rows = {}
    for line in read(BASE/'SHA256SUMS').decode().splitlines():
        value,name=line.split('  ',1)
        p=Path(name)
        assert not p.is_absolute() and '..' not in p.parts and name not in rows and name!='SHA256SUMS'
        assert not (BASE/p).is_symlink() and h(BASE/p)==value
        rows[name]=value
    entries=list(BASE.rglob('*'))
    assert all(not p.is_symlink() for p in entries)
    assert {p.relative_to(BASE).as_posix() for p in entries if p.is_file()}==set(rows)|{'SHA256SUMS'}
    assert len(rows)==327
    return rows
before=closure()
namespace=runpy.run_path(str(BASE/'documentary_audit.py'),run_name='root_readonly_functions')
structural=namespace['audit']('')
assert structural['status']=='PASS_DOCUMENTARY_STRUCTURE_WITH_EXPLICIT_LIMITATIONS'
assert structural['errors']==[] and structural['unresolved_historical_bytes']==[]
assert structural['snapshot_manifests']==13 and structural['physical_snapshot_rows']==42
assert structural['discovery_scope_failure_unique_files']==42
physical={}
references={}
def remember(row):
    if row.get('exists') and 'sha256' in row:
        references[(row['path'],row['sha256'])]=row.get('bytes')
for path in sorted((BASE/'history').glob('*/PIN_MANIFEST.json')):
    for row in obj(path)['files']:
        copy=BASE/row['physical_copy']
        assert h(copy)==row['before']['sha256']==row['after']['sha256']==row['copy']['sha256']
        for phase in ('before','after','copy'):
            remember(row[phase]);physical[(row[phase]['path'],row[phase]['sha256'])]=copy
physical[(str(ROOT/'docs/papers204_208_sequence/GIT_SYNC_RECEIPT.md'),'af1754c9d6095c0f943b75fe7b9819ebd2b7c4db9609930ca7feccf2934786da')]=BASE/'history/controls/docs/papers204_208_sequence/qa/central_lifecycle_p209_a/GIT_SYNC_RECEIPT.before.md'
for folder in sorted((BASE/'discovery').iterdir()):
    for phase in ('BEFORE','AFTER'):
        for row in obj(folder/f'PINS_{phase}.json'):
            remember(row)
for folder in sorted((BASE/'commands').iterdir()):
    result=obj(folder/'result.json')
    for phase in ('before','after'):
        for row in result['pins_'+phase]:
            remember(row)
    for stream in ('stdout','stderr'):
        assert h(folder/(stream+'.txt'))==result[stream+'_sha256']
resolved_counts={'exact_physical':0,'current_exact':0}
for key,length in sorted(references.items()):
    path=physical.get(key,Path(key[0]))
    assert h(path)==key[1],key
    assert length is None or len(read(path))==length
    resolved_counts['exact_physical' if key in physical else 'current_exact']+=1
assert len(structural['protected_inputs_not_reopened'])==42
for row in structural['protected_inputs_not_reopened']:
    assert h(row['path'])==row['expected_sha256']
assert closure()==before
for name,value in list(pins.items()):
    read(name)
    assert pins[name]==value
print(json.dumps({'status':'PASS_ROOT_SCOUT28_ORIGINAL_CLOSURE_NO_PROMOTION',
    'payloads':len(before),'seal_sha256':SEAL,
    'actual_unchanged_documentary_auditor_result':structural,
    'root_complete_reference_keys_checked':len(references),
    'root_resolution_counts':resolved_counts,
    'root_also_hashed_all_42_protected_references':True,
    'current_read_paths_checked_twice':len(pins),
    'scope':'Root documentary and original-byte closure of a negative one-literal desk. No matrix producer/pilot, full old-corpus proof reread, new source clearance or reinstated scout reviewer eligibility.'},indent=2,sort_keys=True))
