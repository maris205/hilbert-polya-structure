"""Root read-only full documentary closure of scout31; no science execution."""
import json
from pathlib import Path
import re
import runpy
import subprocess

R = Path('/root/autodl-tmp/symbolic_dynamics')
Q = R / 'docs/papers204_208_sequence/qa'
B = Q.parent / 'scouting/finite_systems_thirty_first'
D = runpy.run_path(str(Q / 'inspect_p209_a_initial.py'))
pin, obj, manifest = (D[n] for n in ('pin', 'obj', 'manifest'))
pin(__file__)
seal = '20ff7310ad67598a9428de97a3e8239afa5f6707831e3351c84ac3b70a8e0615'
assert pin(B / 'SHA256SUMS')['sha256'] == seal
outer = manifest(B / 'SHA256SUMS', complete=True)
assert len(outer) == 143
old = obj(B / 'SELECTED_ORIGINALS.json')
new = obj(B / 'SELECTED_ORIGINALS_V2.json')
assert len(old) == len(set(old)) == 1701 and len(new) == len(set(new)) == 1335
assert set(new) <= set(old)
protected = [p for p in old if re.match(r'papers/(208|209)-', p)]
builds = [p for p in old if any('build' in x.lower() for x in Path(p).parts[:-1])]
assert len(protected) == 22 and len(builds) == 119
for p in new:
    parts = Path(p).parts
    assert not re.match(r'papers/(208|209)-', p)
    assert not any(any(x in v.lower() for x in ('p208','p209','paper208','paper209','ofs','fth')) for v in parts)
    assert not any(any(x in v.lower() for x in ('review','qa','build','compile','frozen','freeze','snapshot','runtime','generated','extracted','commands','history','historical','source','search','archive','controls')) for v in parts[:-1])
    assert not set(parts) & {'finite_systems_nineteenth','order_geometry_tenth','order_geometry_tenth_desk'}
recorders = {pin(B / n)['sha256'] for n in ('audit_v1.py','audit_v2.py','audit.py')}
commands, searches, comparisons = [], [], []
rows = 0
for path in sorted((B / 'commands').glob('*/receipt.json')):
    folder = path.parent
    r = obj(path)
    pre = obj(folder / 'inputs_before.json')
    post = obj(folder / 'inputs_after.json')
    assert pre == post and r['unchanged'] and len(pre) == r['input_count']
    assert r['recorder_sha256'] in recorders
    assert r['cwd'] == str(R) and r['label'] == folder.name
    assert r['started_epoch'] <= r['finished_epoch']
    a = r['argv']
    for p, h in pre.items():
        assert pin(R / p)['sha256'] == h, p
    rows += len(pre)
    for stream in ('stdout','stderr'):
        assert pin(folder / (stream + '.raw'))['sha256'] == r[stream + '_sha256']
    assert r['exit'] == (1 if folder.name == '18_corrected_scope_pathaudit' else 0)
    if folder.name != '10_download_captive':
        assert pin(folder / 'stderr.raw')['bytes'] == 0
    if a[:4] == ['rg','-n','-i','--']:
        selected = new if folder.name == '17_strict_coupling' else old
        assert a[5:] == selected and list(pre) == selected
        searches.append({'label':folder.name, 'input_paths':len(selected), 'pattern':a[4]})
    if a[0] == 'sed':
        assert len(pre) == 1 and list(pre) == [a[3]]
        lo, hi = map(int, a[2].rstrip('p').split(','))
        raw = (R / a[3]).read_bytes().splitlines(keepends=True)
        assert (folder / 'stdout.raw').read_bytes() == b''.join(raw[lo-1:hi])
    if a[0] == 'cmp':
        assert len(a) == 3 and list(pre) == a[1:]
        assert pin(R / a[1])['sha256'] == pin(R / a[2])['sha256']
        assert pin(folder / 'stdout.raw')['bytes'] == 0
        argv = ['/usr/bin/cmp','--',str(R/a[1]),str(R/a[2])]
        proc = subprocess.run(argv, cwd=R, env=D['ENV'], capture_output=True)
        comparisons.append({'argv':argv,'exit':proc.returncode,'stdout':proc.stdout.decode(),'stderr':proc.stderr.decode()})
        assert proc.returncode == 0
    commands.append({'receipt':str(path),'receipt_pin':pin(path),'argv_entries':len(a),'inputs':len(pre),'exit':r['exit']})
assert len(commands) == 25 and len(searches) == 6 and len(comparisons) == 4
closure = obj(B / 'commands/25_documentary_closure/stdout.raw')
assert closure['status'] == 'PASS_DOCUMENTARY_CHECK_ONLY'
assert closure['completed_receipts_checked'] == 24
assert closure['recorded_before_after_input_rows_checked'] == rows - 1 == 9859
assert closure['original_scope_failure_protected_paths'] == protected
assert closure['original_scope_failure_build_paths'] == len(builds)
assert closure['child_exits'] == [{'label':Path(c['receipt']).parent.name,'exit':c['exit']} for c in commands[:-1]]
assert closure['scientific_executions'] == closure['pilots'] == 0
controls = Q / 'central_lifecycle_p209_b_initial'
for name in ('SYMBOLIC_DYNAMICS_STATE.md','PIPELINE_STATE.md','GIT_SYNC_RECEIPT.md'):
    original = B / 'controls' / name
    alias = controls / (name.removesuffix('.md') + '.before.md')
    assert pin(original)['sha256'] == pin(alias)['sha256']
    argv = ['/usr/bin/cmp','--',str(original),str(alias)]
    proc = subprocess.run(argv, cwd=R, env=D['ENV'], capture_output=True)
    comparisons.append({'argv':argv,'exit':proc.returncode,'stdout':proc.stdout.decode(),'stderr':proc.stderr.decode()})
    assert proc.returncode == 0
for p in list(D['READS']):
    pin(p, fresh=True)
assert manifest(B / 'SHA256SUMS', complete=True) == outer
print(json.dumps({'status':'PASS_ROOT_SCOUT31_COMPLETE_ORIGINAL_CLOSURE',
    'seal_sha256':seal,'sealed_payloads':143,'documentary_commands':commands,
    'original_input_rows_currently_rehashed':rows,'full_content_searches':searches,
    'initial_protected_access_paths':protected,'initial_build_copy_paths':119,
    'corrected_original_paths':1335,'actual_new_root_raw_comparisons':comparisons,
    'current_read_paths_twice':len(D['READS']),'scientific_executions':0,'pilots':0,
    'reviewer_eligibility':'P209_INELIGIBLE_UNCHANGED',
    'disposition':'NO_PROMOTION_TEMPORAL_CAPTIVE_BALLISTIC_WRAPPER',
    'boundary':'Original evidence closure only. Old scope failure remains. No fresh science, full-paper source audit, independent review or novelty clearance.'}, indent=2, sort_keys=True))
