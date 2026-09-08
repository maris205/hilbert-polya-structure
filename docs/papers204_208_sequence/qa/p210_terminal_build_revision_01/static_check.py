#!/usr/bin/env python3
"""Independent AST/data-only final binding check. No task module import/execution."""
import ast
import difflib
import hashlib
import json
from pathlib import Path

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
QA = ROOT / 'docs/papers204_208_sequence/qa'
PREP = QA / 'p210_terminal_build_revision_01'
OLD = QA / 'p210_terminal_build_preparation'
PAPER = ROOT / 'papers/210-weakly-increasing-run-aggregation'
checks, inputs = 0, {}

def need(value, label):
    global checks
    checks += 1
    if not value:
        raise RuntimeError(label)

def read(path):
    need(path.resolve() == path and not path.is_symlink(), 'physical input')
    raw = path.read_bytes()
    value = {'sha256': hashlib.sha256(raw).hexdigest(), 'bytes': len(raw)}
    need(str(path) not in inputs or inputs[str(path)] == value, 'stable input')
    inputs[str(path)] = value
    return raw

def js(path):
    return json.loads(read(path))

baseline = js(PREP / 'ACTUAL_BINDING_BASELINE.actual.json')
native = js(PREP / 'ACTUAL_BINDING_NATIVE.actual.json')
need(native['launch']['session_id'] == 60603 and native['launch']['output'] == '' and
     native['completion']['exit_code'] == 0 and json.loads(native['completion']['output']) == baseline,
     'complete actual capture original return')
need(baseline['status'] == 'PASS_READ_ONLY_ACTUAL_BINDING_CAPTURE' and baseline['checks'] == 8137 and
     baseline['named_paths_reread_twice'] == 1606 and len(baseline['complete_input_pins']) == 1606 and
     baseline['no_builder_gate_or_old_program_execution'] is True and
     baseline['no_host_ledger_entry_expansion'] is True, 'actual capture scope')
contract = js(PREP / 'INPUT_CONTRACT.json')
need(contract == baseline['contract'], 'exact actual-derived final contract')
for name, expected in baseline['complete_input_pins'].items():
    if name == str(PREP / 'INPUT_CONTRACT.json'):
        continue
    read(Path(name))
    need(inputs[name] == expected, 'complete captured current originals unchanged')
old_source, new_source = read(OLD / 'build_p210.py').decode(), read(PREP / 'build_p210.py').decode()
need(len(old_source.splitlines()) == 512 and len(new_source.splitlines()) == 711, 'complete source lengths')
old_tree, tree = ast.parse(old_source), ast.parse(new_source)
compile(tree, str(PREP / 'build_p210.py'), 'exec')  # Compile AST only; never execute code.
need(not any(isinstance(n, ast.ImportFrom) and n.module and 'build_p210' in n.module for n in ast.walk(tree)),
     'no task imports')
def funcs(t):
    return {node.name: node for node in ast.walk(t) if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))}
old_functions, new_functions = funcs(old_tree), funcs(tree)
generic = ['require', 'pin', 'save', 'save_ledger', 'manifest', 'entry', 'inventory', 'coverage',
           'observed', 'command', 'libraries']
for name in generic + ['originals']:
    need(ast.dump(old_functions[name], include_attributes=False) ==
         ast.dump(new_functions[name], include_attributes=False), 'unchanged accepted helper ' + name)
expected_main = ast.parse(ast.get_source_segment(old_source, old_functions['main']).replace(
    "cold = out / label", "cold = out / ('cold_build_' + str(number))").replace(
    "out / (ident + '_cold_build_' + str(n)) / 'main.pdf'", "out / ('cold_build_' + str(n)) / 'main.pdf'")).body[0]
need(ast.dump(expected_main, include_attributes=False) ==
     ast.dump(new_functions['main'], include_attributes=False), 'complete main only two physical directory corrections')
old_assign = {n.targets[0].id: ast.dump(n.value) for n in old_tree.body
              if isinstance(n, ast.Assign) and len(n.targets) == 1 and isinstance(n.targets[0], ast.Name)}
new_assign = {n.targets[0].id: ast.dump(n.value) for n in tree.body
              if isinstance(n, ast.Assign) and len(n.targets) == 1 and isinstance(n.targets[0], ast.Name)}
need(set(old_assign) == set(new_assign) and
     all(old_assign[k] == new_assign[k] for k in old_assign if k != 'PREP'), 'exact runtime/constants except preparation path')
gate = new_functions['final_schema_binding']
need(not any(isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute) and
             n.func.attr in ('Popen', 'run', 'mkdir', 'write_bytes', 'write_text', 'unlink', 'exec_module')
             for n in ast.walk(gate)), 'actual gate read-only no subprocess/mutation')
need(not any(isinstance(n, ast.Call) and isinstance(n.func, ast.Name) and
             n.func.id in ('exec', 'eval', '__import__', 'inventory', 'observed', 'main') for n in ast.walk(gate)),
     'no old execution or host inventory in actual gate')
roles, packages = contract['final_schema_binding']['roles'], contract['final_schema_binding']['manifests']
need(len(roles) == 41 and len(packages) == 8 and sum(v['payloads'] for v in packages.values()) == 1560,
     'exact actual package/role census')
documents = {}
for role, row in roles.items():
    body = read(Path(row['path']))
    need(inputs[row['path']] == {k: row[k] for k in ('sha256', 'bytes')}, 'exact role bytes')
    if row['path'].endswith('.json'):
        documents[role] = json.loads(body)
r = documents['root_b']; c = documents['b_current']; p = documents['round2_provenance']; a = documents['round2_reception']
need(r['schema'] == 'p210-b-root-delta-closure-v1' and r['status'] == 'ROOT_ACCEPTED_B_DELTA_ORIGINAL_CLOSURE_PASS' and
     r['reviewer_delta_accepted'] is True and r['root_original_inspection_complete'] is True and
     r['root_replay_closure_complete'] is True and r['current_open_findings'] == 0, 'actual root B semantic shape')
need(c['reviewer'] == r['reviewer'] == '/root/p210_b_reviewer' and c['accepted_delta'] is True and
     c['current_open_counts'] == {'Critical': 0, 'Major': 0, 'Minor': 0} and
     c['reviewer_infrastructure_resolved_counts']['Minor'] == 2 and c['inherited_A_findings']['resolved_Major'] == 1,
     'same actual B reviewer/history')
expected_native = {
 'b_final': (7664, '74c60b', 'PASS_ROOT_P210_B_FINAL_SAME_REVIEWER_DELTA_AND_ORIGINAL_RECEPTION'),
 'b_strict': (31521, '9c6226', 'PASS_ROOT_P210_B_STRICT_PAIR'),
 'b_strict_reception': (69598, '4a723b', 'PASS_ROOT_P210_B_STRICT_PAIR_ORIGINAL_RECEPTION_REVISION_01'),
 'round2_freeze': (6427, '94eb4f', 'PASS_PHYSICAL_P210_ROUND2'),
 'round2_inspection': (34834, 'edee33', 'PASS_ROOT_PHYSICAL_P210_ROUND2_RECEPTION'),
 'lifecycle_refresh': (42389, '64070b', 'PASS_P210_ROUND2_LIFECYCLE_AND_WHOLE_MANIFEST_REFRESH')}
outputs = {}
for role, (session, chunk, status) in expected_native.items():
    launch, completion = documents[role + '_launch'], documents[role + '_completion']
    need(launch['result']['session_id'] == completion['session_id'] == session and
         launch['result']['output'] == '' and completion['result']['chunk_id'] == chunk and
         completion['result']['exit_code'] == 0 and completion['launch_record'] == Path(roles[role + '_launch']['path']).name,
         'exact actual six native original chains')
    outputs[role] = json.loads(completion['result']['output'])
    need(outputs[role]['status'] == status, 'exact actual native success schema')
need(outputs['b_strict']['checks_each'] == [51129, 51129] and outputs['b_strict']['errors'] == [] and
     outputs['b_strict']['closure'] == {'manifest': packages['b_pair']['seal'], 'payloads': 59}, 'strict actual pair data')
need(outputs['b_final']['phase_reception']['common_keys'] == 121013 and
     outputs['b_final']['current_extra_key_count'] == 44 and
     outputs['b_final']['physical_paths_fully_reread_twice'] == 121057 and
     outputs['b_final']['B_final_manifest'] == packages['b_review']['seal'], 'actual B final native data')
need(p['schema'] == 'p210-round2-provenance-v1' and p['actual_final_b_binding'] == documents['round2_binding'] and
     len(p['anchors']) == 14 and len(p['core_payload_pins']) == 508 and
     len(p['full_source_input_pins_before_and_reread_after']) == 2077 and
     len(a['complete_input_pins']) == 2603 and a['checks'] == 38968 and
     a['round2_manifest_sha256'] == packages['round2']['seal']['sha256'], 'actual Round2 schemas')
historical = {str(PAPER / 'ROOT_LIFECYCLE.md'): roles['prior_lifecycle']['path'],
              str(PAPER / 'PAPER_MANIFEST.sha256'): roles['prior_whole']['path']}
for name, row in p['anchors'].items():
    actual = PAPER / 'frozen_round2' / row['physical_path']
    origin = Path(historical.get(row['original_path'], row['original_path']))
    need(actual == PAPER / 'frozen_round2/ROUND2_ACCEPTANCE' / name and read(actual) == read(origin) and
         inputs[str(actual)]['sha256'] == row['sha256'], 'all fourteen exact historical/current anchors')
native_bases = [Path(packages[name]['path']) for name in ('round1', 'round2', 'b_review', 'b_pair', 'round2_preparation')]
need(len(a['actual_native_commands']) == 6, 'exact native six')
for index, row in enumerate(a['actual_native_commands']):
    need(row['exit'] == 0 and row['stderr_utf8'] == '' and row['environment'] ==
         {'PATH': '/usr/bin:/bin', 'LANG': 'C.UTF-8', 'LC_ALL': 'C.UTF-8', 'TZ': 'UTC'}, 'actual native separate stream/env')
    for label in ('stdout', 'stderr'):
        need(hashlib.sha256(row[label + '_utf8'].encode()).hexdigest() == row[label + '_sha256'], 'full raw native stream')
    if index < 5:
        base = native_bases[index]
        need(row['argv'] == ['/usr/bin/sha256sum', '--check', 'SHA256SUMS'] and row['cwd'] == str(base) and
             row['stdout_utf8'] == ''.join(line.split('  ', 1)[1] + ': OK\n' for line in read(base / 'SHA256SUMS').decode().splitlines()),
             'actual full manifest native stdout')
    else:
        need(row['argv'] == ['/usr/bin/cmp', str(PAPER / 'frozen_round2/AUTHOR_MANIFEST.sha256'),
             str(PAPER / 'AUTHOR_MANIFEST.sha256')] and row['stdout_utf8'] == '' and row['cwd'] == str(ROOT),
             'actual cmp native')
refresh = documents['lifecycle_refresh']
need({k:v for k,v in refresh.items() if k != 'native'} == outputs['lifecycle_refresh'] and
     refresh['current_payloads'] == 2021 and refresh['new_lifecycle_sha256'] == roles['lifecycle']['sha256'] and
     refresh['new_whole_sha256'] == roles['whole']['sha256'], 'actual preterminal lifecycle/whole anchors')
need(refresh['native']['stdout'] == ''.join(row.split('  ', 1)[1] + ': OK\n'
     for row in read(Path(roles['whole']['path'])).decode().splitlines()) and
     refresh['native']['stderr'] == '' and refresh['native']['exit'] == 0, 'complete actual prior whole native')
for name, expected in list(inputs.items()):
    need({'sha256': hashlib.sha256(Path(name).read_bytes()).hexdigest(), 'bytes': Path(name).stat().st_size} == expected,
         'second complete current reread')
need(not (PAPER / 'qa_final').exists() and not (PREP / 'SHA256SUMS').exists(), 'not executed or prematurely sealed')
difference = ''.join(difflib.unified_diff(old_source.splitlines(keepends=True), new_source.splitlines(keepends=True),
    fromfile=str(OLD / 'build_p210.py'), tofile=str(PREP / 'build_p210.py')))
print(json.dumps({'status': 'PASS_P210_ACTUAL_BINDING_AST_AND_DATA_ONLY', 'checks': checks,
    'named_current_inputs_rechecked_twice': len(inputs), 'complete_current_input_pins': inputs,
    'source': inputs[str(PREP / 'build_p210.py')], 'source_lines': 711,
    'unchanged_generic_helpers': generic, 'originals_ast_unchanged': True,
    'main_only_two_physical_directory_corrections': True, 'new_actual_gate_only': True,
    'source_delta': difference, 'source_delta_lines': len(difference.splitlines()),
    'actual_baseline_checks': 8137, 'actual_baseline_paths': 1606,
    'actual_package_payloads': 1560, 'actual_roles': 41,
    'builder_gate_old_programs_science_build_view_executions': 0,
    'host_ledger_entries_expanded': 0, 'preterminal_whole_after_output_completeness_assertion': False}, sort_keys=True))

