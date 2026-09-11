#!/usr/bin/env python3
"""Documentary hashing and syntax-AST parsing of the NEW receiver only.

No receiver/producer module or function is imported or executed. The unchanged
producer is hashed as opaque bytes, never parsed or compiled. No output is read.
"""
import ast
from hashlib import sha256
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
checks = 0

def need(test, message):
    global checks
    checks += 1
    if not test:
        raise AssertionError(message)

def pin(path):
    path = Path(path)
    need(path.is_file() and not path.is_symlink(), 'ordinary documentary input')
    data = path.read_bytes()
    return {'sha256': sha256(data).hexdigest(), 'bytes': len(data)}

def main():
    declaration = json.loads((HERE / 'SOURCE_INPUT_PINS.json').read_bytes())
    expected = declaration['inputs']
    need(len(expected) == 10, 'ten fixed source/control inputs')
    before = {path: pin(path) for path in expected}
    need(all(before[path]['sha256'] == row['sha256'] for path, row in expected.items()), 'all declared original pins')
    status = json.loads((HERE / 'PREPARATION_STATUS.json').read_bytes())
    need(status['saved_stdout_path'] is None and status['binding_path'] is None and
         status['binding_created'] is False and status['receiver_executed'] is False and
         status['saved_stdout_opened'] is False, 'preparation remains unbound and unexecuted')
    source = HERE / 'receive_output.py'
    data = source.read_bytes()
    need(pin(source) == {k: status['receiver_source'][k] for k in ('sha256', 'bytes')}, 'frozen new receiver source')
    need(len(data.splitlines()) == 548, 'complete new receiver source lines')
    # ast.parse is syntax-only. No compile-to-executable-bytecode, eval, exec,
    # importlib, runpy or receiver function call is used in this checker.
    tree = ast.parse(data, filename=str(source))
    imports = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            imports.extend(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom):
            imports.extend(node.module + '.' + alias.name for alias in node.names)
    need(sorted(imports) == ['fractions.Fraction', 'hashlib.sha256', 'json', 'os', 'pathlib.Path', 'sys'],
         'exact stdlib-only receiver import statements')
    forbidden = [node.func.id for node in ast.walk(tree) if isinstance(node, ast.Call) and
                 isinstance(node.func, ast.Name) and node.func.id in ('exec', 'eval', 'compile', '__import__')]
    need(not forbidden, 'receiver contains no dynamic scientific source loading calls')
    main_node = next(node for node in tree.body if isinstance(node, ast.FunctionDef) and node.name == 'main')
    approval_lines = [node.lineno for node in ast.walk(main_node) if isinstance(node, ast.Call) and
                      isinstance(node.func, ast.Name) and node.func.id == 'need' and node.args and
                      isinstance(node.args[-1], ast.Constant) and node.args[-1].value == 'ROOT_APPROVAL_REQUIRED']
    report_lines = [node.lineno for node in ast.walk(main_node) if isinstance(node, ast.Call) and
                    isinstance(node.func, ast.Name) and node.func.id == 'inspect_report']
    need(len(approval_lines) == len(report_lines) == 1 and approval_lines[0] < report_lines[0],
         'documented textual approval-before-report ordering')
    after = {path: pin(path) for path in expected}
    need(after == before and source.read_bytes() == data, 'all selected inputs and receiver unchanged')
    print(json.dumps({'status': 'PASS_DOCUMENTARY_SOURCE_PREPARATION_ONLY', 'checks': checks,
          'inputs_before': before, 'inputs_after': after,
          'receiver_pin': pin(source), 'receiver_lines': len(data.splitlines()),
          'syntax_AST_nodes': sum(1 for _ in ast.walk(tree)),
          'receiver_function_names': [node.name for node in tree.body if isinstance(node, ast.FunctionDef)],
          'receiver_import_statements': imports,
          'textual_approval_line': approval_lines[0], 'textual_report_inspection_line': report_lines[0],
          'receiver_imports_or_executions': 0, 'receiver_semantic_function_calls': 0,
          'producer_parses_compilations_imports_or_executions': 0,
          'saved_output_reads': 0, 'scientific_executions': 0,
          'limitations': 'Syntax and source integrity only; textual ordering is not a runtime authorization test. No saved-output behavior has been tested.'},
          sort_keys=True, indent=2))


if __name__ == '__main__':
    main()
