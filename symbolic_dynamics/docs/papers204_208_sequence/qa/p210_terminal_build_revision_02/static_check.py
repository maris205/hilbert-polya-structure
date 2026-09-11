#!/usr/bin/env python3
"""AST/data-only minimal revision02 check; no builder/preflight/old-code execution."""
import ast
import difflib
import hashlib
import json
import os
from pathlib import Path
ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
QA = ROOT / 'docs/papers204_208_sequence/qa'
OLD = QA / 'p210_terminal_build_revision_01'
NEW = QA / 'p210_terminal_build_revision_02'
PAPER = ROOT / 'papers/210-weakly-increasing-run-aggregation'
inputs, checks = {}, 0
def need(value, label):
    global checks
    checks += 1
    if not value:
        raise RuntimeError(label)
def read(path):
    body = path.read_bytes()
    value = {'sha256': hashlib.sha256(body).hexdigest(), 'bytes': len(body)}
    need(path.resolve() == path and not path.is_symlink(), 'physical original')
    need(str(path) not in inputs or inputs[str(path)] == value, 'stable repeated original')
    inputs[str(path)] = value
    return body
def js(path):
    return json.loads(read(path))
seal = read(OLD / 'SHA256SUMS')
need(hashlib.sha256(seal).hexdigest() == '37c6e8f996dc693ebd8280faf4705d35db8d04fbc19bb306de264ca56af972e7', 'old sealed preparation')
rows = seal.decode().splitlines()
need(len(rows) == 19, 'old exact 19 seal')
for row in rows:
    sha, name = row.split('  ', 1)
    need(hashlib.sha256(read(OLD / name)).hexdigest() == sha, 'old sealed payload unchanged')
source1, source2 = read(OLD / 'build_p210.py').decode(), read(NEW / 'build_p210.py').decode()
tree1, tree2 = ast.parse(source1), ast.parse(source2)
compile(tree2, str(NEW / 'build_p210.py'), 'exec')
need(len(source1.splitlines()) == 711 and len(source2.splitlines()) == 726, 'exact source lengths')
def functions(tree):
    return {n.name:n for n in ast.walk(tree) if isinstance(n, ast.FunctionDef)}
f1, f2 = functions(tree1), functions(tree2)
need(set(f1) == set(f2), 'no added/removed/renamed function')
unchanged = sorted(set(f1) - {'main', 'final_schema_binding'})
for name in unchanged:
    need(ast.dump(f1[name]) == ast.dump(f2[name]), 'whole unchanged function ' + name)
main2 = ast.parse(ast.get_source_segment(source2, f2['main'])).body[0]
flag = [n for n in main2.body if isinstance(n, ast.Expr) and isinstance(n.value, ast.Call) and
        isinstance(n.value.func, ast.Attribute) and n.value.func.attr == 'add_argument' and
        n.value.args and isinstance(n.value.args[0], ast.Constant) and n.value.args[0].value == '--preflight-only']
branch = [n for n in main2.body if isinstance(n, ast.If) and isinstance(n.test, ast.Attribute) and
          isinstance(n.test.value, ast.Name) and n.test.value.id == 'args' and n.test.attr == 'preflight_only']
need(len(flag) == len(branch) == 1, 'single explicit flag and branch')
need(ast.literal_eval(flag[0].value.keywords[0].value) == 'store_true', 'flag is explicit opt-in')
body = main2.body
originals_index = next(i for i,n in enumerate(body) if isinstance(n, ast.Assign) and isinstance(n.value, ast.Call) and
                       isinstance(n.value.func, ast.Name) and n.value.func.id == 'originals')
mkdir_index = next(i for i,n in enumerate(body) if isinstance(n, ast.Expr) and isinstance(n.value, ast.Call) and
                   isinstance(n.value.func, ast.Attribute) and n.value.func.attr == 'mkdir')
need(originals_index < body.index(branch[0]) < mkdir_index and isinstance(branch[0].body[-1], ast.Return) and
     ast.literal_eval(branch[0].body[-1].value) == 0, 'actual gate precedes preflight return before output mkdir')
need(not any(isinstance(n, ast.Call) and ((isinstance(n.func, ast.Attribute) and n.func.attr in
     {'mkdir','Popen','run','write_bytes','write_text','unlink'}) or
     (isinstance(n.func, ast.Name) and n.func.id in {'inventory','command','exec','eval'})) for n in ast.walk(branch[0])),
     'read-only preflight branch no side effects or host collection')
main2.body = [n for n in body if n not in flag + branch]
need(ast.dump(main2) == ast.dump(f1['main']), 'complete old main unchanged after exactly flag and early branch removal')
gate_old = ast.get_source_segment(source1, f1['final_schema_binding'])
gate_new = ast.get_source_segment(source2, f2['final_schema_binding'])
old_line = "            provenance['raw_byte_comparisons'] == 1016, 'Actual Round2 accepted binding and provenance')"
new_lines = """            isinstance(provenance['raw_byte_comparisons'], list) and len(provenance['raw_byte_comparisons']) == 1016 and
            all(set(row) == {'bytes', 'equal', 'left', 'method', 'right', 'role'} and row['equal'] is True and
                type(row['bytes']) is int and row['bytes'] >= 0 and Path(row['left']).is_absolute() and
                Path(row['right']).is_absolute() and isinstance(row['role'], str) and
                row['method'] == 'complete Python bytes comparison; not a native cmp command'
                for row in provenance['raw_byte_comparisons']), 'Actual Round2 accepted binding and provenance')"""
need(gate_old.count(old_line) == 1 and gate_old.replace(old_line, new_lines) == gate_new, 'entire actual gate only corrected list predicate')
assign1 = [n for n in tree1.body if isinstance(n, (ast.Import, ast.ImportFrom, ast.Assign, ast.AugAssign))]
assign2 = [n for n in tree2.body if isinstance(n, (ast.Import, ast.ImportFrom, ast.Assign, ast.AugAssign))]
for a,b in zip(assign1, assign2):
    if isinstance(a, ast.Assign) and isinstance(a.targets[0], ast.Name) and a.targets[0].id == 'PREP':
        need(ast.get_source_segment(source2,b) == "PREP = QA / 'p210_terminal_build_revision_02'", 'only new preparation path')
    else:
        need(ast.dump(a) == ast.dump(b), 'unchanged import/runtime/constant')
need(len(assign1) == len(assign2) and read(NEW / 'INPUT_CONTRACT.json') == read(OLD / 'INPUT_CONTRACT.json'),
     'all accepted contract bytes unchanged')
v = js(PAPER / 'frozen_round2/ROUND2_PROVENANCE.json')
records = v['raw_byte_comparisons']
need(type(records) is list and len(records) == 1016 and records != 1016, 'actual full list not old integer')
for row in records:
    need(set(row) == {'bytes','equal','left','method','right','role'} and row['equal'] is True and
         type(row['bytes']) is int and row['bytes'] >= 0 and Path(row['left']).is_absolute() and
         Path(row['right']).is_absolute() and isinstance(row['role'],str) and
         row['method'] == 'complete Python bytes comparison; not a native cmp command', 'exact actual comparison record')
launch = js(QA / 'P210_TERMINAL_OUTER_ROOT_LAUNCH.actual.json')
complete = js(QA / 'P210_TERMINAL_OUTER_ROOT_COMPLETION.actual.json')
diagnosis = js(QA / 'P210_TERMINAL_FAILURE01_ROOT_DIAGNOSIS.actual.json')
failed = QA / 'p210_terminal_launch_01'
record = js(failed / 'UNCLOSED.json')
need(launch['result']['session_id'] == complete['session_id'] == 31966 and launch['result']['output'] == '' and
     complete['result']['chunk_id'] == '46daf4' and complete['result']['exit_code'] == 1 and
     record['original_wait_exit_code'] == 1 and record['original_wait_outcome'] == 'COMPLETED' and
     record['builder_reaped'] is True and record['builder_group_absent'] is True and record['cleanup_events'] == [],
     'actual failed first native kept failed and settled')
need(diagnosis['result']['exit_code'] == 0 and diagnosis['result']['chunk_id'] == '5518df' and
     json.loads(diagnosis['result']['output'])['actual_field_type'] == 'list', 'actual independent root diagnosis')
need(read(failed / 'builder.stdout') == b'' and
     hashlib.sha256(read(failed / 'builder.stderr')).hexdigest() ==
     'c59d2d497b70ed822878033a04971b81753bb3851c6fe1759777fa6a0e9eb11b', 'actual separate failed streams preserved')
failure_files = sorted(f for f in failed.rglob('*') if f.is_file())
need(len(failure_files) == 9 and not (failed / 'SHA256SUMS').exists(), 'all nine failed originals remain unsealed')
for path in failure_files:
    read(path)
for path in (NEW / 'README.md', NEW / 'static_check.py', NEW / 'DIAGNOSIS_INITIAL_TRUNCATED_NATIVE.actual.json'):
    read(path)
need(not os.path.lexists(PAPER / 'qa_final') and not (NEW / 'SHA256SUMS').exists(), 'no build or premature final seal')
for name, value in list(inputs.items()):
    need({'sha256':hashlib.sha256(Path(name).read_bytes()).hexdigest(),'bytes':Path(name).stat().st_size} == value,
         'complete explicit original second read')
diff = ''.join(difflib.unified_diff(source1.splitlines(keepends=True),source2.splitlines(keepends=True),
    fromfile=str(OLD / 'build_p210.py'),tofile=str(NEW / 'build_p210.py')))
print(json.dumps({'status':'PASS_P210_REVISION02_MINIMAL_AST_DATA_ONLY_PREFLIGHT_PENDING',
    'checks':checks,'explicit_original_paths_rechecked_twice':len(inputs),'input_pins':inputs,
    'source':inputs[str(NEW / 'build_p210.py')],'source_lines':726,
    'source_delta':diff,'source_delta_lines':len(diff.splitlines()),'unchanged_function_names':unchanged,
    'actual_comparison_list_records_checked':1016,'actual_failure01_files_preserved':len(failure_files),
    'old_preparation_payloads_preserved':19,'actual_readonly_preflight_executions':0,
    'new_builder_old_program_science_build_view_executions':0,
    'root_must_execute_complete_actual_preflight_before_new_outer':True},sort_keys=True))
