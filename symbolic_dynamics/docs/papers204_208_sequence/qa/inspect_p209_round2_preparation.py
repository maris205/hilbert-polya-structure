"""Root read-only Round2 preparation/actual-acceptance preflight.

Imports only the fully read infrastructure freezer's definitions, never its
main or any scientific module. Its precreation checks do not create files.
"""
from hashlib import sha256
import json
from pathlib import Path
import runpy
import subprocess

R = Path('/root/autodl-tmp/symbolic_dynamics')
Q = R/'docs/papers204_208_sequence/qa'
B = Q/'p209_round2_preparation'
D = runpy.run_path(str(Q/'inspect_p209_a_initial.py'))
pin,obj,manifest = (D[n] for n in ('pin','obj','manifest'))
pin(__file__)
assert pin(B/'SHA256SUMS')['sha256'] == '84fc65f40ca65ed4ec555cd398860e314fe2195bc7f88766d3fbde70a4bb458d'
seal = manifest(B/'SHA256SUMS',complete=True)
assert len(seal) == 13
assert pin(B/'freeze_p209_round2.py')['sha256'] == '787357029ae3d4f50c1a9998a3b1e4fe9377786cc06cb024e3a7a96ef95b46c7'
static = obj(B/'STATIC_CHECK.execution.json')
assert static['completion_result']['exit_code'] == 0
report = json.loads(static['completion_result']['output'])
assert report['status'] == 'PASS_STATIC_PREPARATION_ONLY'
assert report['source_sha256'] == pin(B/'freeze_p209_round2.py')['sha256']
assert report['source_lines'] == 510 and report['rechecked_input_paths'] == 9332
assert report['input_map_storage'].startswith('Digest and count only;')
rows = report['actual_commands']
assert [c['exit'] for c in rows] == [0]*7+[1]
actual = []
for row in rows:
    assert row['inputs_before'] == row['inputs_after']
    assert row['cwd'] == str(R) and row['environment'] == D['ENV']
    assert row['outcome'] == 'COMPLETED' and row['stderr'] == ''
    for p,value in row['inputs_before'].items():
        assert pin(p)['sha256'] == value
    argv = row['argv']
    if row['exit'] == 0:
        assert argv[:2] == ['/usr/bin/cmp','--'] and row['stdout'] == ''
    else:
        assert row['stdout'].encode() == (B/'ADAPTATION.diff').read_bytes()
        headers = row['stdout'].splitlines()[:2]
        argv = ['/usr/bin/diff','-u','--label',headers[0][4:],'--label',headers[1][4:],*argv[2:]]
    process = subprocess.run(argv,cwd=R,env=D['ENV'],capture_output=True)
    assert process.returncode == row['exit'] and process.stderr == b''
    assert process.stdout == row['stdout'].encode()
    actual.append({'argv':argv,'exit':process.returncode,'stdout_sha256':sha256(process.stdout).hexdigest(),
                   'stdout_bytes':len(process.stdout),'stderr':process.stderr.decode(),
                   'stdout_role':'Empty cmp output or the separately preserved complete ADAPTATION.diff with explicit archival header labels.'})
F = runpy.run_path(str(B/'freeze_p209_round2.py'),run_name='root_readonly_precreation_checks_not_main')
assert not F['TARGET'].exists() and not F['TARGET'].is_symlink()
assert len(F['complete_manifest'](B)) == 13
core,author,whole,preexisting = F['core_inputs']()
accepted,external,counts,initial = F['accepted_b'](core)
prior,history,copies = F['historical_resolution'](core,accepted,initial)
historical_links,anchor_links = F['link_mapping'](core,prior,history)
assert accepted['review_manifest_entries'] == 1472
assert accepted['review_manifest_sha256'] == 'ab9f2cc94fb0b6eb112290bc9687a4d8479f5b832810f7a7c28013737e838d16'
assert len(copies) == 1 and len(F['ANCHORS']) == 15
assert len(preexisting) == 5983
for path,value in list(F['READ_PINS'].items()):
    assert pin(path)['sha256'] == value
for path in list(D['READS']):
    pin(path,fresh=True)
assert F['complete_manifest'](B) == seal and not F['TARGET'].exists()
print(json.dumps({'status':'PASS_ROOT_ROUND2_PREPARATION_AND_ACTUAL_ACCEPTANCE_PREFLIGHT',
    'preparation_payloads':13,'preparation_sha256':pin(B/'SHA256SUMS')['sha256'],
    'freezer_sha256':pin(B/'freeze_p209_round2.py')['sha256'],
    'actual_accepted_B_root_gate_sha256':pin(Q/'P209_B_ROOT_DELTA_INSPECTION.actual.json')['sha256'],
    'actual_accepted_B_review_payloads':counts['accepted_review_payloads'],
    'core_payloads':len(core),'unchanged_author_payloads':len(author),
    'preexisting_paper_files':len(preexisting),'historical_role_keys':len(history),
    'physical_new_alias_copies':{n:{'physical':str(p),'sha256':v} for n,(p,v) in copies.items()},
    'historical_links':len(historical_links),'new_anchor_links':len(anchor_links),
    'all_current_read_paths_checked_twice':len(D['READS']),
    'actual_root_source_comparisons_and_diff':actual,'target_absent':True,
    'boundary':'Read-only original/static/actual-acceptance preflight; no freezer main/refusal test, physical Round2, mathematical producer, build or page view.'},indent=2,sort_keys=True))
