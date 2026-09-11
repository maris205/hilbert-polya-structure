#!/usr/bin/env python3
"""Bounded AST/data-only revision audit; no inspected code execution/import."""
import ast
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
QA = ROOT / 'docs/papers204_208_sequence/qa'
HERE = QA / 'p210_terminal_launch_revision_01'
OLD = QA / 'p210_terminal_launch_preparation'
BUILD = QA / 'p210_terminal_build_revision_01'
KEYS, CHECKS = {}, []


def ck(value, label):
    if not value:
        raise AssertionError(label)
    CHECKS.append(label)


def key(body):
    return {'sha256': hashlib.sha256(body).hexdigest(), 'bytes': len(body)}


def raw(path):
    ck(path.resolve() == path and path.is_file() and not path.is_symlink(), 'physical explicit file ' + str(path))
    body = path.read_bytes()
    KEYS[str(path)] = key(body)
    return body


def package(base, wanted, count):
    body, names = raw(base / 'SHA256SUMS'), set()
    ck(key(body)['sha256'] == wanted, 'exact actual preparation seal ' + str(base))
    for row in body.decode().splitlines():
        digest, name = row.split('  ', 1)
        p = Path(name)
        ck(len(digest) == 64 and set(digest) <= set('0123456789abcdef') and p.parts and p.as_posix() == name and
           not p.is_absolute() and '..' not in p.parts and name != 'SHA256SUMS' and name not in names, 'safe nonself member')
        ck(key(raw(base / name))['sha256'] == digest, 'exact actual payload ' + name)
        names.add(name)
    paths = list(base.rglob('*'))
    ck(not any(p.is_symlink() for p in paths) and len(names) == count and names ==
       {p.relative_to(base).as_posix() for p in paths if p.is_file() and p.name != 'SHA256SUMS' or
        p.is_file() and p.name == 'SHA256SUMS' and p.parent != base}, 'complete physical preparation census')


def main():
    ck(sys.argv[1:] == ['ast-data-only'] and sys.flags.isolated and sys.flags.no_site and
       sys.dont_write_bytecode and sys.flags.optimize == 0, 'isolated documentary-only invocation')
    package(OLD, '98303243b14d1c49853932e940fe35cd9b7064948eddfb765e6dd6d67f4e07be', 16)
    package(BUILD, '37c6e8f996dc693ebd8280faf4705d35db8d04fbc19bb306de264ca56af972e7', 19)
    old, new = raw(OLD / 'launch_p210_terminal.py').decode(), raw(HERE / 'launch_p210_terminal.py').decode()
    contract = json.loads(raw(HERE / 'INPUT_CONTRACT.json'))
    raw(HERE / 'README.md'); raw(HERE / 'static_check.py')
    for name in ('DOCUMENTARY_PATH_FAILURE_01.actual.json', 'BUILDER_SEAL_NATIVE.actual.json'):
        raw(HERE / name)
    ck(len(old.splitlines()) == 304 and len(new.splitlines()) == contract['source']['lines'] == 357 and
       key(new.encode()) == {k: contract['source'][k] for k in ('sha256', 'bytes')}, 'exact old/new source and contract')
    ot, nt = ast.parse(old), ast.parse(new)
    funcs = lambda tree: {n.name: n for n in tree.body if isinstance(n, ast.FunctionDef)}
    a, b = funcs(ot), funcs(nt)
    dump = lambda node: ast.dump(node, include_attributes=False)
    changed = sorted(name for name in a if dump(a[name]) != dump(b[name]))
    ck(set(a) == set(b) and changed == ['builder_closure', 'final_builder_binding'] == contract['changed_functions'],
       'exactly two functions changed; no helper added or removed')
    for name in sorted(set(a) - set(changed)):
        ck(dump(a[name]) == dump(b[name]), 'entire unchanged helper AST ' + name)
    bindings = lambda tree: {t.id: n.value for n in tree.body if isinstance(n, ast.Assign) for t in n.targets if isinstance(t, ast.Name)}
    oa, na = bindings(ot), bindings(nt)
    ck(set(oa) == set(na) and all(dump(oa[k]) == dump(na[k]) for k in oa if k != 'PREP'), 'all settings unchanged except preparation path')
    imports = lambda tree: [dump(n) for n in tree.body if isinstance(n, (ast.Import, ast.ImportFrom))]
    ck(imports(ot) == imports(nt), 'exact original imports, no execution shortcut')
    target = 'QA / \'p210_terminal_launch_revision_01\''
    ck(ast.get_source_segment(new, na['PREP']) == target, 'sole module path correction')
    closure = ast.get_source_segment(new, b['builder_closure'])
    expected = ast.get_source_segment(old, a['builder_closure']).replace(
        "    pins = manifest(BUILD_OUT)\n    result = json.loads((BUILD_OUT / 'RESULT.json').read_bytes())",
        "    result_raw = (BUILD_OUT / 'RESULT.json').read_bytes()\n    result = json.loads(result_raw)").replace(
        "    return {'manifest':", "    pins = manifest(BUILD_OUT)\n    require(pins[str(BUILD_OUT / 'RESULT.json')] == {\n        'sha256': hashlib.sha256(result_raw).hexdigest(), 'bytes': len(result_raw)},\n        'Verified manifest binds the exact RESULT bytes checked before hashing')\n    return {'manifest':")
    ck(dump(ast.parse(expected).body[0]) == dump(b['builder_closure']), 'entire closure exactly minimal no-hash ordering plus same-raw-key correction')
    ck(closure.index('group_absent(command') < closure.index('pins = manifest') < closure.index('hashlib.sha256(result_raw)') and
       closure.index("'Unclosed builder evidence present'") < closure.index('pins = manifest'), 'all groups/UNCLOSED checks precede any payload hash')
    gate = ast.get_source_segment(new, b['final_builder_binding'])
    ck('UNBOUND_' not in gate and not any(isinstance(n, ast.Call) and isinstance(n.func, ast.Name) and
       n.func.id in {'exec', 'eval', 'compile', '__import__', 'inventory', 'observed', 'main'} for n in ast.walk(b['final_builder_binding'])),
       'actual small gate, no unbound layer/old code/host inventory invocation')
    root_path = QA / 'P210_TERMINAL_BUILD_PREPARATION_ROOT.actual.json'
    root_native = json.loads(raw(root_path))
    ck(KEYS[str(root_path)] == {k: contract['actual_root_preparation'][k] for k in ('sha256', 'bytes')} and
       KEYS[str(root_path)]['sha256'] in gate, 'exact actual root gate byte identity')
    ck(root_native['launch']['session_id'] == 26258 and root_native['launch']['output'] == '' and
       root_native['completion']['chunk_id'] == '52c454' and root_native['completion']['exit_code'] == 0, 'actual root native original')
    accepted = json.loads(root_native['completion']['output'])
    ck(accepted['status'] == 'PASS_ROOT_P210_FINAL_BUILDER_SOURCE_AND_ACTUAL_BINDING_STATIC' and
       accepted['source'] == KEYS[str(BUILD / 'build_p210.py')] and accepted['source_lines'] == 711 and
       accepted['complete_package_count'] == 8 and accepted['named_roles'] == 41 and accepted['exact_original_input_union'] == 1594,
       'actual root-preparation/source schema; no eight-package reexecution')
    for name, value in accepted['preparation_documents'].items():
        ck(KEYS[str(BUILD / name)] == value, 'all eight actual root-read prep keys ' + name)
    js = lambda name: json.loads(raw(BUILD / name))
    recipe, baseline, capture, static, native = map(js, ('INPUT_CONTRACT.json', 'ACTUAL_BINDING_BASELINE.actual.json',
        'ACTUAL_BINDING_NATIVE.actual.json', 'STATIC_CHECK.actual.json', 'STATIC_NATIVE_RETURN.actual.json'))
    ck(recipe['schema'] == 'p210-terminal-build-actual-bound-contract-v1' and
       recipe['stage'] == 'ACTUAL_B_ROOT_DELTA_PHYSICAL_ROUND2_BOUND_NOT_EXECUTED' and
       recipe == baseline['contract'] and capture['launch']['session_id'] == 60603 and capture['launch']['output'] == '' and
       capture['completion']['exit_code'] == 0 and json.loads(capture['completion']['output']) == baseline,
       'complete actual capture/native/recipe equality')
    ck(baseline['checks'] == 8137 and baseline['named_paths_reread_twice'] == 1606 and
       native['result']['exit_code'] == 0 and json.loads(native['result']['output']) == static and static['checks'] == 6707 and
       static['named_current_inputs_rechecked_twice'] == 1610 and static['source'] == accepted['source'] and
       static['complete_current_input_pins'][str(BUILD / 'INPUT_CONTRACT.json')] == KEYS[str(BUILD / 'INPUT_CONTRACT.json')],
       'complete actual final static/native/source/contract equality')
    ck(not os.path.lexists(ROOT / 'papers/210-weakly-increasing-run-aggregation/qa_final') and
       not os.path.lexists(QA / 'p210_terminal_launch_01'), 'prospective outputs actually absent')
    old_path, new_path = str(OLD / 'launch_p210_terminal.py'), str(HERE / 'launch_p210_terminal.py')
    argv = ['/usr/bin/diff', '--minimal', '-u', '--label', old_path, '--label', new_path, old_path, new_path]
    diff = subprocess.run(argv, cwd=ROOT, capture_output=True, timeout=30, check=False)
    delta, original_lines, rebuilt, cursor = diff.stdout.decode(), old.splitlines(keepends=True), [], 0
    for line in delta.splitlines(keepends=True)[2:]:
        if line.startswith('@@ '):
            match = re.fullmatch(r'@@ -(\d+)(?:,\d+)? \+\d+(?:,\d+)? @@.*\n', line)
            ck(match is not None, 'strict actual diff hunk')
            start = int(match.group(1)) - 1; rebuilt.extend(original_lines[cursor:start]); cursor = start
        elif line.startswith((' ', '-')):
            ck(original_lines[cursor] == line[1:], 'exact old diff line ' + str(cursor + 1)); cursor += 1
            if line.startswith(' '): rebuilt.append(line[1:])
        else:
            ck(line.startswith('+'), 'actual new diff line prefix'); rebuilt.append(line[1:])
    rebuilt.extend(original_lines[cursor:])
    ck(diff.returncode == 1 and diff.stderr == b'' and ''.join(rebuilt) == new, 'complete actual minimal native diff reconstructs exact new source')
    for name, value in dict(KEYS).items():
        ck(key(Path(name).read_bytes()) == value, 'final uncached original reread ' + name)
    print(json.dumps({'status': 'PASS_P210_OUTER_REVISION_AST_AND_ACTUAL_PREPARATION_DATA_ONLY',
        'checks': len(CHECKS), 'check_labels': CHECKS, 'input_keys': KEYS, 'named_input_count': len(KEYS),
        'source': key(new.encode()), 'source_lines': len(new.splitlines()), 'changed_functions': changed,
        'unchanged_functions': sorted(set(a) - set(changed)), 'source_diff': delta,
        'source_diff_lines': len(delta.splitlines()), 'diff_native': {'argv': argv, 'cwd': str(ROOT),
        'exit_code': diff.returncode, 'stdout': delta, 'stderr': diff.stderr.decode()},
        'old_ordering_defect': 'CORRECTED_BY_EXACT_SOURCE_DIFF_NOT_A_RUNTIME_TEST',
        'actual_builder_preparation_payloads': 19, 'actual_root_preparation_native_exit': 0,
        'launcher_builder_receiver_refusal_executions': 0, 'page_views': 0, 'host_inventory_collections': 0,
        'eight_package_gate_reexecutions': 0, 'new_B_host_map': False, 'qa_final_created': False,
        'outer_output_created': False, 'external': 'OWNER_AMBER / HOLD_EXTERNAL'}, sort_keys=True, indent=2))


if __name__ == '__main__':
    main()
