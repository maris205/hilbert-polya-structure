"""Root complete terminal-preparation/original/current-acceptance preflight.

Only fully read infrastructure definitions are imported. The builder main,
launcher main, science producers, TeX, PDF tools and renderer are not run.
The actual documentary subprocesses below are only raw cmp and diff.
"""
from hashlib import sha256
import json
from pathlib import Path
import runpy
import subprocess

R = Path('/root/autodl-tmp/symbolic_dynamics')
Q = R/'docs/papers204_208_sequence/qa'
B = Q/'p209_terminal_preparation'
P = R/'papers/209-ordered-fibre-threading'
D = runpy.run_path(str(Q/'inspect_p209_a_initial.py'))
pin,obj,manifest = (D[n] for n in ('pin','obj','manifest'))
pin(__file__)
assert pin(B/'SHA256SUMS')['sha256'] == '983dba0c90f72a8ef7580f455780d5c2363d675c84e2e19f0c507c1f2ca7e616'
assert len(manifest(B/'SHA256SUMS',complete=True)) == 190
assert pin(B/'root_terminal_builds.py')['sha256'] == 'b2489d74647e72ccecbce9906a3f790e94712a724337271f0c99aa77a945dae1'
assert pin(B/'root_launch_terminal.py')['sha256'] == '773ffba4850783614366732d47ae54aa9ad73c947048e6e9013ba4d0d90ec462'
assert pin(B/'ADAPTATION_FINAL.diff')['sha256'] == '2cd5e90cc745dac12c013885e06185036e8cb09ff59f1897685af2d0d2f248e5'
A = runpy.run_path(str(B/'audit_preparation.py'),run_name='root_documentary_definitions_only')
documentary,reads = A['documentary_check']()
assert documentary['status'] == 'PASS_DOCUMENTARY_PREPARATION_CLOSURE_ONLY'
assert len(documentary['documentary_commands']) == 25
for p,row in reads.items():D['checkpin'](p,row)
for p,row in obj(B/'PREPARATION_READ_PINS.json').items():D['checkpin'](p,row)
for name in ('FINAL_STATIC_CHECK.json','PREPARATION_AUDIT.json','SOURCE_CAPTURE.json','DRAFT_REVISION.json'):
    assert obj(B/name)['builder_executions'] == 0 if 'builder_executions' in obj(B/name) else True
aliases = {(x['original_path'],x['sha256']):B/x['physical_path']
           for x in obj(B/'DRAFT_REVISION.json')['historical_input_aliases']}
actual = []
for row in documentary['documentary_commands']:
    folder = Path(row['path'])
    receipt = obj(folder/'RECEIPT.json')
    inputs = obj(folder/'INPUTS_BEFORE.json')
    argv = list(receipt['argv'])
    replacements = []
    for i,arg in enumerate(argv):
        if arg in inputs and pin(arg)['sha256'] != inputs[arg]['sha256']:
            physical = aliases[(arg,inputs[arg]['sha256'])]
            assert pin(physical)['sha256'] == inputs[arg]['sha256']
            replacements.append({'original_path':arg,'sha256':inputs[arg]['sha256'],'physical_path':str(physical)})
            argv[i] = str(physical)
    proc = subprocess.run(argv,cwd=R,env=D['ENV'],capture_output=True)
    assert proc.returncode == receipt['exit'] and proc.stderr == b''
    assert proc.stdout == (folder/'stdout').read_bytes()
    actual.append({'argv':argv,'cwd':str(R),'environment':D['ENV'],'exit':proc.returncode,
        'historical_command_input_aliases':replacements,'stdout_sha256':sha256(proc.stdout).hexdigest(),
        'stdout_bytes':len(proc.stdout),'full_stdout_exact_byte_storage':str(folder/'stdout'),
        'stdout_raw_bytes_compared_to_storage':True,'stderr':proc.stderr.decode()})
assert sum(x['exit']==0 for x in actual) == 19 and sum(x['exit']==1 for x in actual) == 6
F = runpy.run_path(str(B/'root_terminal_builds.py'),run_name='root_actual_acceptance_definitions_not_builder_main')
assert not F['OUT'].exists() and not (Q/'root_replays/p209_terminal_strict').exists()
science = F['science']()
for p,row in science.items():D['checkpin'](p,row)
whole = manifest(P/'PAPER_MANIFEST.sha256',complete=True)
assert len(whole) == 8004
assert len(manifest(P/'AUTHOR_MANIFEST.sha256')) == 1985
assert len(manifest(P/'frozen_round2/SHA256SUMS',complete=True)) == 2021
historical_whole = P/'frozen_round2/ROUND2_ACCEPTANCE/PRE_ROUND2_PAPER_MANIFEST.sha256'
assert pin(historical_whole)['sha256'] == '3e94a72637733ca46f7950f4feb8508fdf14b5ff6386c971821932ae9231e5a9'
assert len(manifest(historical_whole,base=P)) == 5982
for p in list(D['READS']):pin(p,fresh=True)
assert F['science']() == science and not F['OUT'].exists()
print(json.dumps({'status':'PASS_ROOT_P209_TERMINAL_PREPARATION_AND_ACTUAL_ACCEPTANCE_PREFLIGHT',
    'preparation_payloads':190,'preparation_manifest_sha256':pin(B/'SHA256SUMS')['sha256'],
    'source_copies':8,'original_copies':11,'original_documentary_commands':25,
    'whole_final_diff_sha256':pin(B/'ADAPTATION_FINAL.diff')['sha256'],
    'actual_new_documentary_comparisons':actual,'gated_science_documentary_inputs':len(science),
    'current_paper_complete_manifest_payloads':len(whole),
    'current_paper_complete_manifest_sha256':pin(P/'PAPER_MANIFEST.sha256')['sha256'],
    'old_whole_manifest_historical_payloads':5982,'all_current_read_paths_checked_twice':len(D['READS']),
    'round2_root_gate_sha256':pin(Q/'P209_ROUND2_ROOT_INSPECTION.actual.json')['sha256'],
    'terminal_output_roots_absent':True,'boundary':'Full original/static role inspection and read-only current acceptance function. No mathematical producer, launcher/builder main, TeX/PDF/render/view execution; no paper completion.'},indent=2,sort_keys=True))
