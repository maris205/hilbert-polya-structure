"""Root archive inspection only: never import or execute KIP scientific code."""
from pathlib import Path
import hashlib
import json
import shlex

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
SCOUT = ROOT / 'docs/papers211_215_sequence/scouting'
D = SCOUT / 'finite_semigroup_lane'
P = SCOUT / 'finite_semigroup_pilot'
S = SCOUT / 'kip_source_desk'

def pin(raw):
    return {'bytes':len(raw), 'sha256':hashlib.sha256(raw).hexdigest()}

def expected(row):
    return {key:row[key] for key in ('bytes','sha256')}

def blob(path):
    return Path(path).read_bytes()

def document(path):
    return json.loads(blob(path))

def inventory(folder, name, count, total, seal):
    raw = blob(folder / name)
    assert pin(raw)['sha256'] == seal
    if name.endswith('.json'):
        data = json.loads(raw)
        assert data['self_excluded'] == name
        rows = data['files']
    else:
        rows = []
        for line in raw.decode().splitlines():
            digest, rel = line.split('  ', 1)
            rows.append({'path':rel, 'sha256':digest, 'bytes':len(blob(folder / rel))})
    result = {}
    for row in rows:
        rel = row['path']
        assert rel not in result and not Path(rel).is_absolute() and '..' not in Path(rel).parts
        result[rel] = blob(folder / rel)
        assert pin(result[rel]) == expected(row), rel
    actual = set()
    for path in folder.rglob('*'):
        assert not path.is_symlink(), str(path)
        if path.is_file() and path != folder / name:
            actual.add(path.relative_to(folder).as_posix())
    assert actual == result.keys()
    assert len(result) == count and sum(map(len,result.values())) == total
    return result

contracts = [(D,'MANIFEST.json',39,519632,'fd8115b4d7fa76db0323b35234859146cb090f6af03aa69164c9fe4e27ebcbae'),
 (P,'MANIFEST.json',119,16633767,'552ae5468b57bcb2e0fa5ebf7b382c53d6345cc07f406888a059dbf91c96ccbe'),
 (S,'MANIFEST.sha256',12,246158,'ee311f5f09e0f5b722825345a83aef4793507097d8b8e95c1b9d2dc5f01f3197')]
d, p, s = [inventory(*args) for args in contracts]
history = json.loads(d['HISTORY_PINS.json'])
assert len(history) == 15
for row in history:
    assert row['raw_equal_at_capture'] is True
    assert blob(ROOT / row['source']) == d[row['snapshot']]
    assert pin(d[row['snapshot']]) == expected(row)
assert b''.join(d[row['snapshot']] for row in history) == d['native/01.stdout']
for n in (1,2,3):
    stem = f'native/{n:02}'
    receipt = json.loads(d[stem + '.json'])
    assert receipt['exit_code'] == 0 and receipt['started_ns'] <= receipt['finished_ns']
    for stream in ('stdout','stderr'):
        assert pin(d[stem + '.' + stream]) == receipt[stream]
assert json.loads(d['native/01.json'])['argv'] == ['cat',*[row['snapshot'] for row in history]]

# Exact pre-science lock and unchanged sealed desk, with no retrospective repair.
for rel, raw in d.items():
    assert raw == p['lock/desk/' + rel]
assert blob(D / 'MANIFEST.json') == p['lock/desk/MANIFEST.json']
lock = json.loads(p['PRE_EXECUTION_PINS.json'])
assert lock['producer_invocations_so_far'] == 0 and len(lock['rows']) == 98
assert lock['desk_manifest'] == pin(blob(D / 'MANIFEST.json'))
assert lock['environment'] == {'PATH':'/usr/bin:/bin','LANG':'C','LC_ALL':'C','TZ':'UTC'}
assert lock['timeout_seconds'] == 60 and lock['executable'] == '/usr/bin/python3.10'
allowed, frozen_paths = {}, set()
for row in lock['rows']:
    assert row['frozen'] not in frozen_paths
    frozen_paths.add(row['frozen'])
    assert blob(row['origin']) == p[row['frozen']]
    assert pin(p[row['frozen']]) == expected(row)
    allowed[str(Path(row['origin']).resolve())] = expected(row)
    allowed[str((P / row['frozen']).resolve())] = expected(row)
for name in ('producer.py','run_pilot.py','runtime_probe.py','freeze.py','audit.py','AUTHORIZATION.md'):
    assert p[name] == p['lock/' + name]
receipts = {}
for folder, out, err in [('preflight','runtime_probe.stdout.json','runtime_probe.stderr.txt'),
 ('execution_01','stdout.jsonl','stderr.txt'),
 ('postrun_diagnostic_v2','audit_recapture.stdout.txt','audit_recapture.stderr.txt')]:
    name = 'AUDIT_RECAPTURE_NATIVE_RECEIPT.json' if folder.startswith('postrun') else 'NATIVE_RECEIPT.json'
    r = json.loads(p[folder + '/' + name])
    receipts[folder] = r
    assert r['cwd'] == str(P) and r['started_ns'] <= r['finished_ns']
    for key, file in [('stdout',out),('stderr',err)]:
        assert pin(p[folder + '/' + file]) == r[key]
    assert r['environment'] == lock['environment']
probe_r, run, diag_r = [receipts[k] for k in ('preflight','execution_01','postrun_diagnostic_v2')]
assert probe_r['argv'] == [lock['executable'],'-I','-S','-B',str(P/'lock/runtime_probe.py')]
assert probe_r['native_exit'] == 0
assert probe_r['finished_ns'] <= lock['frozen_ns'] <= run['started_ns'] <= run['finished_ns'] <= diag_r['started_ns']
assert run['argv'] == [lock['executable'],'-I','-S','-B',str(P/'lock/producer.py')]
assert run['scientific_producer_invocations'] == 1 and run['native_exit'] == 0
assert run['timed_out'] is False and run['launch_error'] is None
assert run['elapsed_seconds'] == (run['finished_ns']-run['started_ns'])/10**9 < 60
assert run['pre_execution_pins_before'] == run['pre_execution_pins_after'] == pin(p['PRE_EXECUTION_PINS.json'])
assert run['all_locked_inputs_unchanged'] is True
assert len(run['input_pins_before']) == 98 and run['input_pins_before'] == run['input_pins_after']
for row, observed in zip(lock['rows'],run['input_pins_before']):
    assert observed == {'origin':row['origin'],'frozen':row['frozen'],'origin_pin':expected(row),'frozen_pin':expected(row)}
assert run['launcher_source'] == {'path':str(P/'lock/run_pilot.py'),**pin(p['lock/run_pilot.py'])}
assert 'launcher_environment' not in run
assert len(p['execution_01/stdout.jsonl']) == 731379 and p['execution_01/stderr.txt'] == b''

# Read/reconcile the complete saved relation. No literal successor is calculated.
records = [json.loads(line) for line in p['execution_01/stdout.jsonl'].splitlines()]
kinds = [r['kind'] for r in records]
assert len(records) == 2363 and kinds[0] == 'contract' and kinds[-2:] == ['runtime','complete']
assert set(kinds) == {'contract','state','box','runtime','complete'}
assert all(kinds.count(k)==1 for k in ('contract','runtime','complete'))
head, child, complete = records[0], records[-2], records[-1]
assert head['n_values'] == list(range(1,8)) and head['expected_total_states'] == 2353
assert head['contract'] == {'path':str(P/'lock/desk/PREPILOT_CONTRACT.md'),**pin(d['PREPILOT_CONTRACT.md'])}
assert head['proof'] == {'path':str(P/'lock/desk/PROOF_PACKAGE.md'),**pin(d['PROOF_PACKAGE.md'])}
boxes = [r for r in records if r['kind']=='box']
states = [r for r in records if r['kind']=='state']
assert [r['n'] for r in boxes] == list(range(1,8)) and len(states) == 2353
for n,size,box in zip(range(1,8),(1,3,10,35,126,462,1716),boxes):
    rows = [r for r in states if r['n']==n]
    table = {tuple(r['source']):r for r in rows}
    assert len(rows) == len(table) == box['states'] == size
    assert list(table) == sorted(table)
    reverse = {key:[] for key in table}
    for source,row in table.items():
        assert len(source)==n and list(source)==sorted(source) and min(source)>=1 and max(source)<=n
        assert tuple(row['successor']) in table
        reverse[tuple(row['successor'])].append(list(source))
        assert row['decoded_predecessors'] == row['predecessors'] == sorted(row['predecessors'])
        assert row['laurent_count'] == len(row['predecessors'])
        assert row['target_in_image'] == bool(row['predecessors'])
        assert row['height'] == row['predicted_height'] and row['period'] == 1
        assert row['cycle'] == [row['terminal']]
    assert all(sorted(reverse[key])==table[key]['predecessors'] for key in table)
    assert sum(r['laurent_count'] for r in rows) == box['inverse_mass'] == size
    assert box['image'] == sum(bool(r['predecessors']) for r in rows)
    assert box['maximum_height'] == max(r['height'] for r in rows) == box['theorem_height']
    assert box['maximum_fibre_is_descriptive_only'] is True
assert complete['total_states']==2353 and complete['scientific_producer_invocations']==1
assert complete['assertion_total']==14523
assert complete['assertions'] == {key:sum(b['assertions'][key] for b in boxes) for key in head['categories']}
assert list(complete['assertions'].values()) == [2360,2360,2360,2353,2353,2360,377]
assert sum(complete['assertions'].values()) == 14523

probe = json.loads(p['preflight/runtime_probe.stdout.json'])
assert child['environment'] == probe['environment'] == lock['environment']
observations = [('preflight_probe',probe,52),('scientific_child',child,38),('launcher',run['launcher_runtime'],54)]
missing_by_role = {}
diagnosis = json.loads(p['postrun_diagnostic_v2/DIAGNOSIS.json'])
for role,obs,count in observations:
    assert len(obs['file_pins'])==count
    missing=[]
    for row in obs['file_pins']:
        assert pin(blob(row['path'])) == expected(row)
        if allowed.get(str(Path(row['path']).resolve())) != expected(row):
            missing.append(row)
    missing_by_role[role] = [r['path'] for r in missing]
    assert diagnosis['runtime_comparison'][role] == {'observed_file_count':count,'observed_mapped_paths':obs['mapped_runtime_paths'],'not_prelocked':missing}
assert missing_by_role == {'preflight_probe':[],'scientific_child':[],
 'launcher':['/usr/lib/locale/C.utf8/LC_CTYPE','/usr/lib/x86_64-linux-gnu/gconv/gconv-modules.cache']}
assert diagnosis['strict_observed_runtime_prelock_status']=='FAIL_PRESERVED'
assert diagnosis['hermetic_or_strict_replay_certified'] is False
assert diag_r['argv']==[lock['executable'],'-I','-S','-B',str(P/'lock/audit.py'),'audit']
assert diag_r['native_exit']==1 and diag_r['scientific_producer_invocations_in_this_diagnostic']==0
assert diag_r['retrospective_original_receipt'] is False
for key,rel in [('source','lock/audit.py'),('diagnostic_driver','artifact_closeout_v2.py')]:
    assert diag_r[key]=={'path':str(P/rel),**pin(p[rel])}
assert p['postrun_diagnostic_v2/audit_recapture.stdout.txt']==b''
assert len(p['postrun_diagnostic_v2/audit_recapture.stderr.txt'])==535
assert p['postrun_diagnostic_v2/audit_recapture.stderr.txt'].endswith(b"AssertionError: ('unfrozen observed runtime file', '/usr/lib/locale/C.utf8/LC_CTYPE')\n")

# Source desk tool returns are decoded text, not invented separate raw streams.
history_text=s['HISTORICAL_INPUT_PINS.sha256'].decode()
for line in history_text.splitlines():
    digest,rel=line.split('  ',1)
    assert pin(blob(ROOT/rel))['sha256']==digest
assert len(history_text.splitlines())==8
source_returns=json.loads(s['READONLY_TOOL_RETURNS.json'])['records']
assert len(source_returns)==7
for r in source_returns:
    assert r['result']['exit_code']==0
    args=shlex.split(r['cmd'])
    if args[0]=='sed':
        assert args[1]=='-n' and args[2].endswith('p') and len(args)==4
        first,last=map(int,args[2][:-1].split(','))
        lines=blob(ROOT/args[3]).decode().splitlines(keepends=True)
        assert r['result']['output']==''.join(lines[first-1:last])
    else:
        assert args[0]=='sha256sum' and r['result']['output']==history_text
after=json.loads(s['INPUT_IDENTITY_CHECK.json'])['after']
assert after['result']['exit_code']==0 and after['result']['output']==history_text
assert len([rel for rel in s if rel.startswith('sources/')])==8
for args,old in zip(contracts,(d,p,s)):
    assert inventory(*args)==old
print(json.dumps({'status':'PASS_ROOT_ARCHIVE_ONLY_WITH_STRICT_FAILURE_RETAINED',
 'desk_payloads':39,'history_raw_pairs':15,'desk_native_exits':[0,0,0],
 'pilot_payloads':119,'prelock_rows':98,'original_state_records':2353,
 'original_assertions':14523,'original_science_exit':0,'new_science_runs':0,
 'strict_prelock_status':'FAIL_PRESERVED','runtime_missing_by_role':missing_by_role,
 'source_payloads':12,'source_history_pins':8,'decoded_old_slices':6,
 'source_browser_returns':8,'manuscript_reviews':0,'git_commands':0},sort_keys=True))
