#!/usr/bin/env python3
"""Revision02 AST/data-only check; never load or execute task-program code."""
import ast
import hashlib
import json
import os
from pathlib import Path

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
QA = ROOT / 'docs/papers204_208_sequence/qa'
PREP = QA / 'p210_terminal_launch_revision_02'
checks = 0

def check(value, label):
    global checks
    checks += 1
    if not value:
        raise RuntimeError(label)

def pin(path):
    raw = Path(path).read_bytes()
    return {'sha256': hashlib.sha256(raw).hexdigest(), 'bytes': len(raw)}

def package(spec):
    base = Path(spec['path'])
    seal = base / 'SHA256SUMS'
    check(pin(seal) == spec['seal'], 'actual seal')
    result = {}
    for line in seal.read_text().splitlines():
        digest, name = line.split('  ', 1)
        path = base / name
        check(path.resolve() == path and not path.is_symlink() and str(path) not in result, 'physical unique member')
        result[str(path)] = pin(path)
        check(result[str(path)]['sha256'] == digest, 'complete payload')
    check(len(result) == spec['payloads'] and set(result) ==
          {str(p) for p in base.rglob('*') if p.is_file() and p != seal}, 'complete nonself membership')
    result[str(seal)] = pin(seal)
    return result

contract = json.loads((PREP / 'INPUT_CONTRACT.json').read_bytes())
source = PREP / 'launch_p210_terminal.py'
old = QA / 'p210_terminal_launch_revision_01/launch_p210_terminal.py'
check(pin(source) == {k: contract['source'][k] for k in ('sha256', 'bytes')} and
      len(source.read_text().splitlines()) == contract['source']['lines'] == 389, 'final actual source')
check(pin(old) == contract['preserved_original_outer']['source'], 'immutable prior source')
old_ast, new_ast = ast.parse(old.read_bytes()), ast.parse(source.read_bytes())
check(len(old_ast.body) == len(new_ast.body), 'same top-level census')
changed = []
for index, (left, right) in enumerate(zip(old_ast.body, new_ast.body)):
    if ast.dump(left) == ast.dump(right):
        check(True, 'unchanged node')
        continue
    if index == 0:
        check(isinstance(right, ast.Expr) and isinstance(right.value, ast.Constant), 'documentary string only')
        changed.append('module_docstring')
    elif isinstance(left, ast.Assign):
        check(isinstance(right, ast.Assign) and ast.dump(left.targets[0]) == ast.dump(right.targets[0]) and
              isinstance(right.targets[0], ast.Name) and right.targets[0].id in {'PREP', 'OUT', 'BUILDER_PREP'},
              'only three literal path assignments')
        check(isinstance(left.value, ast.BinOp) and isinstance(right.value, ast.BinOp) and
              ast.dump(left.value.left) == ast.dump(right.value.left) and
              ast.dump(left.value.op) == ast.dump(right.value.op) and
              left.value.right.value[:-2] == right.value.right.value[:-2] and
              left.value.right.value.endswith('01') and right.value.right.value.endswith('02'), 'only path revision')
        changed.append(right.targets[0].id)
    else:
        check(isinstance(left, ast.FunctionDef) and isinstance(right, ast.FunctionDef) and
              left.name == right.name == 'final_builder_binding', 'only binding function')
        changed.append('final_builder_binding')
check(set(changed) == {'module_docstring', 'PREP', 'OUT', 'BUILDER_PREP', 'final_builder_binding'}, 'exact changed set')
diff_native = json.loads((PREP / 'SOURCE_DELTA_NATIVE.actual.json').read_bytes())
check(diff_native['result']['exit_code'] == 1 and diff_native['result']['output'].encode() ==
      (PREP / 'SOURCE_DELTA.diff').read_bytes(), 'actual complete GNU difference raw bytes')
package(contract['preserved_original_outer'])
pins = {}
for role in contract['package_roles'].values():
    for path, value in package(role).items():
        check(path not in pins or pins[path] == value, 'package conflict')
        pins[path] = value
for path, value in contract['extra_originals'].items():
    check(pin(path) == value, 'exact extra original')
    pins[path] = value
capture = Path(contract['package_roles']['actual_preflight_capture']['path'])
data = json.loads((capture / 'stdout').read_bytes())
result = json.loads((capture / 'RESULT.json').read_bytes())
attempt = json.loads((capture / 'ATTEMPT.json').read_bytes())
spawn = json.loads((capture / 'SPAWN.json').read_bytes())
check(result['original_wait_exit_code'] == result['cleanup_wait_exit_code'] == 0 and
      result['timed_out'] is False and result['wait_error'] is None and result['cleanup_events'] == [] and
      result['child_reaped'] is True and result['process_group_absent'] is True, 'actual clean preflight')
try:
    os.killpg(result['pid'], 0)
except ProcessLookupError:
    absent = True
else:
    absent = False
check(absent and result['pid'] == spawn['pid'] == spawn['process_group_id'] == 777535, 'actual group currently absent')
check(result['inputs_before'] == result['inputs_after'] == attempt['inputs_before'] and
      result['inputs_unchanged'] is True and len(result['inputs_before']) == 5, 'actual recorder stable map')
check(result['argv'] == attempt['argv'] and result['cwd'] == attempt['cwd'] == str(ROOT) and
      result['environment'] == attempt['environment'] and attempt['timeout_seconds'] == 600 and
      attempt['start_new_session'] is True, 'actual invocation')
check(data['status'] == 'PASS_P210_FINAL_SCHEMA_PREFLIGHT_ONLY' and
      data['output_created'] is False and data['terminal_acceptance'] is False and
      data['child_commands'] == data['host_inventory_collections'] == data['new_science_build_view_executions'] == 0,
      'actual preflight only')
check(data['original_input_count'] == len(data['original_input_pins']) == 1619 and
      len(data['final_schema_binding_return']['required_input_pins']) == 1594 and
      all(data['original_input_pins'].get(p) == v for p, v in data['final_schema_binding_return']['required_input_pins'].items()),
      'complete actual original map and final subset')
for mapping in (result['inputs_before'], data['original_input_pins']):
    for path, value in mapping.items():
        check(path not in pins or pins[path] == value, 'map conflict')
        pins[path] = value
check(len(pins) == contract['required_input_union_count'] == 1631, 'exact binding union')
for path, value in pins.items():
    check(Path(path).resolve() == Path(path) and not Path(path).is_symlink() and pin(path) == value, 'all current pins')
launch = json.loads((QA / 'P210_TERMINAL_PREFLIGHT02_ROOT_LAUNCH.actual.json').read_bytes())
completion = json.loads((QA / 'P210_TERMINAL_PREFLIGHT02_ROOT_COMPLETION.actual.json').read_bytes())
reception = json.loads((QA / 'P210_TERMINAL_PREFLIGHT02_ROOT_RECEPTION.actual.json').read_bytes())
native = json.loads(completion['result']['output'])
check(launch['result']['session_id'] == completion['session_id'] == 78288 and
      launch['result']['output'] == '' and completion['result']['chunk_id'] == '11728b' and
      completion['result']['exit_code'] == 0, 'actual native chain')
check(native == {'status': 'PASS_ACTUAL_P210_PREFLIGHT_CAPTURE', 'output': str(capture),
      'original_wait_exit_code': 0, 'stdout': pin(capture / 'stdout'), 'stderr': pin(capture / 'stderr'),
      'result': pin(capture / 'RESULT.json'), 'seal': pin(capture / 'SHA256SUMS'),
      'original_input_count': 1619, 'terminal_acceptance': False}, 'complete reconstructed native summary')
check((capture / 'stderr').read_bytes() == b'' and all(result[k] == native[k] for k in ('stdout', 'stderr')) and
      (capture / 'executed_source.py').read_bytes() == (QA / 'record_p210_terminal_preflight_02.py').read_bytes(),
      'actual independent full streams and executed recorder bytes')
accepted = json.loads(reception['result']['output'])
check(reception['result']['exit_code'] == 0 and reception['result']['chunk_id'] == 'dd97dc' and
      accepted['status'] == 'PASS_ROOT_ACTUAL_PREFLIGHT02_FULL_RAW_ORIGINAL_RECEPTION' and
      accepted['all_actual_input_pins_rehashed'] == 1619 and accepted['full_final_binding_required_pins'] == 1594 and
      accepted['capture_seal'] == native['seal'] and accepted['complete_raw_stdout'] == native['stdout'] and
      accepted['complete_raw_stderr'] == native['stderr'], 'existing real root reception')
check(not os.path.lexists(contract['prospective_outer_output']) and
      not os.path.lexists(contract['prospective_builder_output']), 'fresh future outputs remain absent')
for path, value in pins.items():
    check(pin(path) == value, 'complete second pin reread')
print(json.dumps({'status': 'PASS_P210_OUTER02_MINIMAL_AST_AND_ACTUAL_PREFLIGHT_DATA_ONLY',
      'checks': checks, 'source': pin(source), 'source_lines': 389, 'changed_nodes': changed,
      'required_input_union_count': len(pins), 'raw_original_input_count': 1619,
      'final_semantic_subset_count': 1594, 'contract': pin(PREP / 'INPUT_CONTRACT.json'),
      'complete_source_delta': pin(PREP / 'SOURCE_DELTA.diff'),
      'package_roles': contract['package_roles'], 'extra_originals': contract['extra_originals'],
      'actual_preflight_parent_session': 78288, 'actual_preflight_original_exit_code': 0,
      'actual_preflight_builder_group_currently_absent': absent,
      'source_program_imports_or_executions': 0, 'builder_or_recorder_or_receiver_or_refusal_executions': 0,
      'new_builds': 0, 'new_page_views': 0, 'host_key_maps_expanded': 0,
      'outer_execution': 'NOT_EXECUTED', 'terminal_acceptance': False}, sort_keys=True, indent=2))
