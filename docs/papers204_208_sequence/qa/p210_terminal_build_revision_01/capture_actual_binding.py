#!/usr/bin/env python3
"""Read-only actual-binding data capture; never imports or executes task sources."""
import hashlib
import json
from pathlib import Path
import re

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
QA = ROOT / 'docs/papers204_208_sequence/qa'
PAPER = ROOT / 'papers/210-weakly-increasing-run-aggregation'
PREP = QA / 'p210_terminal_build_revision_01'
B = QA.parent / 'reviews/p210_b'
pins = {}
checks = 0

def need(ok, label):
    global checks
    checks += 1
    if not ok:
        raise RuntimeError(label)

def key(path):
    raw = path.read_bytes()
    return {'sha256': hashlib.sha256(raw).hexdigest(), 'bytes': len(raw)}

def read(path):
    need(path.resolve() == path and not path.is_symlink(), 'physical ' + str(path))
    value = key(path)
    need(str(path) not in pins or pins[str(path)] == value, 'stable repeated input')
    pins[str(path)] = value
    return path.read_bytes()

def js(path):
    return json.loads(read(path))

old_recipe = js(PREP / 'INPUT_CONTRACT.json')
need(old_recipe['stage'] == 'PRELIMINARY_UNBOUND_NO_EXECUTION', 'actual unbound baseline')
original_roles = {
    'root_b': QA / 'P210_B_ROOT_DELTA_INSPECTION.actual.json',
    'b_current': B / 'CURRENT_FINDINGS.json',
    'b_findings': B / 'FINDINGS.json',
    'b_delta': B / 'DELTA.md',
    'b_initial_manifest': B / 'history/initial_before_delta/SHA256SUMS',
    'b_initial_delta': B / 'history/initial_before_delta/DELTA.md',
    'b_response': QA.parent / 'P210_B_RESPONSE.md',
    'author_manifest': PAPER / 'AUTHOR_MANIFEST.sha256',
    'round2_binding': QA / 'p210_round2_binding/FINAL_B_BINDING.json',
    'round2_provenance': PAPER / 'frozen_round2/ROUND2_PROVENANCE.json',
    'round2_reception': QA / 'p210_round2_root_reception/ROOT_RECEPTION.json',
    'round2_metadata': QA / 'P210_ROUND2_ROOT_METADATA.actual.json',
    'round2_root_report': QA / 'P210_ROUND2_ROOT_INSPECTION.md',
    'root_b_report': QA / 'P210_B_ROOT_DELTA_INSPECTION.md',
    'lifecycle': PAPER / 'ROOT_LIFECYCLE.md',
    'whole': PAPER / 'PAPER_MANIFEST.sha256',
    'prior_lifecycle': PAPER / 'frozen_round2/ROUND2_ACCEPTANCE/PRE_ROUND2_ROOT_LIFECYCLE.md',
    'prior_whole': PAPER / 'frozen_round2/ROUND2_ACCEPTANCE/PRE_ROUND2_PAPER_MANIFEST.sha256',
    'lifecycle_refresh': QA / 'P210_ROUND2_LIFECYCLE_REFRESH.actual.json',
}
prefixes = {
    'b_final': 'P210_B_FINAL_ORIGINALS_ROOT',
    'b_strict': 'P210_B_STRICT_ROOT',
    'b_strict_reception': 'P210_B_STRICT_ORIGINALS_ROOT',
    'round2_freeze': 'P210_ROUND2_ROOT_FREEZE',
    'round2_inspection': 'P210_ROUND2_ROOT_INSPECTION',
    'lifecycle_refresh': 'P210_ROUND2_LIFECYCLE_REFRESH_ROOT',
}
for role, stem in prefixes.items():
    for suffix in ('launch', 'completion'):
        original_roles[role + '_' + suffix] = QA / (stem + '_' + suffix.upper() + '.actual.json')
root_b = js(original_roles['root_b'])
for index, (name, digest) in enumerate(sorted(root_b['evidence'].items())):
    path = Path(name)
    need(hashlib.sha256(read(path)).hexdigest() == digest, 'actual B root evidence')
    original_roles['root_b_evidence_' + str(index)] = path
roles = {role: {'path': str(path), **key(path)} for role, path in original_roles.items()}
for path in original_roles.values():
    read(path)
bases = {
    'b_review': (B, 441),
    'b_pair': (QA / 'root_replays/p210_b_strict_pair_01', 59),
    'round1': (PAPER / 'frozen_round1', 508),
    'round2': (PAPER / 'frozen_round2', 524),
    'round2_preparation': (QA / 'p210_round2_preparation', 11),
    'round2_reception': (QA / 'p210_round2_root_reception', 1),
    'b_final_preparation': (QA / 'p210_b_final_reception_preparation', 12),
    'b_strict_preparation': (QA / 'p210_b_strict_preparation', 4),
}
manifests = {}
for role, (base, count) in bases.items():
    seal = base / 'SHA256SUMS'
    rows = read(seal).decode().splitlines()
    need(len(rows) == count, 'manifest count ' + role)
    found = set()
    for row in rows:
        digest, name = row.split('  ', 1)
        relative = Path(name)
        need(re.fullmatch('[0-9a-f]{64}', digest) and relative.as_posix() == name and
             relative.parts and not relative.is_absolute() and '..' not in relative.parts and
             name != 'SHA256SUMS' and name not in found, 'safe member')
        found.add(name)
        need(hashlib.sha256(read(base / name)).hexdigest() == digest, 'complete manifest ' + name)
    entries = list(base.rglob('*'))
    need(not any(path.is_symlink() for path in entries) and found ==
         {path.relative_to(base).as_posix() for path in entries if path.is_file() and path != seal},
         'complete physical membership ' + role)
    manifests[role] = {'path': str(base), 'payloads': count, 'seal': key(seal)}
r2 = PAPER / 'frozen_round2'
for name, expected in old_recipe['historical_round1_source_baseline']['source_pins'].items():
    for base in (PAPER, PAPER / 'frozen_round1', r2):
        need(key(base / name) == expected, 'unchanged exact ten sources')
        read(base / name)
for base in (PAPER, PAPER / 'frozen_round1', r2):
    need(key(base / 'main.pdf') == old_recipe['historical_round1_source_baseline']['pdf_pin'], 'accepted PDF equality')
    read(base / 'main.pdf')
native_shapes = {}
for role in prefixes:
    launch = js(original_roles[role + '_launch'])
    completion = js(original_roles[role + '_completion'])
    need(completion['result']['exit_code'] == 0 and type(completion['result']['exit_code']) is int,
         'actual native success ' + role)
    need(completion['launch_record'] == original_roles[role + '_launch'].name and
         completion['session_id'] == launch['result']['session_id'], 'actual session chain ' + role)
    need(launch['result']['output'] == '', 'actual empty initial stdout chunk ' + role)
    output = json.loads(completion['result']['output'])
    native_shapes[role] = {'session_id': completion['session_id'], 'chunk_id': completion['result']['chunk_id'],
        'status': output['status'], 'complete_output_keys': sorted(output),
        'launch_outer_cwd': launch.get('cwd', 'NOT_RECORDED_DO_NOT_RETROFILL')}
need(not (PAPER / 'qa_final').exists(), 'no terminal execution')
for name, expected in pins.items():
    need(key(Path(name)) == expected, 'complete second read ' + name)
paper = {'paper': str(PAPER), 'freeze': str(r2), 'round': 2,
    'freeze_manifest': key(r2 / 'SHA256SUMS'), 'freeze_payloads': 524,
    'source_names': old_recipe['historical_round1_source_baseline']['source_names'],
    'source_pins': old_recipe['historical_round1_source_baseline']['source_pins'],
    'pdf_pin': old_recipe['historical_round1_source_baseline']['pdf_pin'],
    'pages': 6, 'underfull': []}
contract = {
    'schema': 'p210-terminal-build-actual-bound-contract-v1',
    'stage': 'ACTUAL_B_ROOT_DELTA_PHYSICAL_ROUND2_BOUND_NOT_EXECUTED',
    'infrastructure_pins': old_recipe['infrastructure_pins'],
    'final_schema_binding': {'roles': roles, 'manifests': manifests, 'papers': {'P210': paper}},
    'physical_build_directory_names': ['cold_build_1', 'cold_build_2'],
    'boundary': 'Exact actual root-gate originals and sealed package bytes, not another B host-key audit; no imported old program or scientific execution. Current lifecycle/whole are preterminal anchors, never a complete-whole assertion after qa_final creation. Six pages remain to be measured from actual Round2 PDF before build; actual final page views remain a separate gate.',
}
print(json.dumps({'status': 'PASS_READ_ONLY_ACTUAL_BINDING_CAPTURE', 'checks': checks,
    'named_paths_reread_twice': len(pins), 'complete_input_pins': pins,
    'actual_native_shapes': native_shapes, 'contract': contract,
    'old_builder': key(PREP / 'build_p210.py'), 'no_builder_gate_or_old_program_execution': True,
    'no_host_ledger_entry_expansion': True}, sort_keys=True))

