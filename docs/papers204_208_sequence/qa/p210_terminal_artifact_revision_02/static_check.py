#!/usr/bin/env python3
"""AST/source and named-data preparation check only; never execute the reader."""
import ast
import hashlib
import json
from pathlib import Path
import re

HERE = Path(__file__).resolve().parent
SOURCE = HERE / 'inspect_p210_artifact.py'


def digest(path):
    data = path.read_bytes()
    return {'sha256': hashlib.sha256(data).hexdigest(), 'bytes': len(data)}


def main():
    text = SOURCE.read_text()
    tree = ast.parse(text)
    meta = json.loads((HERE / 'SOURCE_INHERITANCE.json').read_bytes())
    original = Path(meta['verbatim_helpers']['source'])
    original_text = original.read_text()
    old = ast.parse(original_text)
    assert digest(original)['sha256'] == meta['verbatim_helpers']['source_sha256']
    functions = [node for node in tree.body if isinstance(node, ast.FunctionDef)]
    named = {node.name: node for node in functions}
    old_named = {node.name: node for node in old.body if isinstance(node, ast.FunctionDef)}
    assert len(functions) == len(named)
    inherited = {}
    for name in meta['verbatim_helpers']['functions']:
        current_segment = ast.get_source_segment(text, named[name])
        old_segment = ast.get_source_segment(original_text, old_named[name])
        assert current_segment == old_segment
        assert ast.dump(named[name], include_attributes=False) == ast.dump(old_named[name], include_attributes=False)
        inherited[name] = {'source_bytes_sha256': hashlib.sha256(current_segment.encode()).hexdigest(),
                           'exact_source_and_AST': True}
    def globals_by_name(document):
        return {target.id: ast.dump(node.value, include_attributes=False) for node in document.body
                if isinstance(node, ast.Assign) for target in node.targets if isinstance(target, ast.Name)}
    now_globals, old_globals = globals_by_name(tree), globals_by_name(old)
    for name in meta['verbatim_helpers']['globals']:
        assert now_globals[name] == old_globals[name]
    imports = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            imports.extend(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom):
            assert node.level == 0
            imports.append(node.module)
    assert set(imports) == {'ast', 'collections', 'datetime', 'gzip', 'hashlib', 'json', 'os', 'pathlib',
                            're', 'shlex', 'sys', 'sysconfig', 'traceback', 'urllib.parse'}
    forbidden_names = {'eval', 'exec', 'compile', '__import__'}
    forbidden_attributes = {'mkdir', 'makedirs', 'write_text', 'write_bytes', 'unlink', 'rename', 'replace',
                            'rmdir', 'remove', 'rmtree', 'copy', 'copyfile', 'run', 'Popen', 'system', 'kill', 'killpg'}
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call):
            continue
        assert not (isinstance(node.func, ast.Name) and node.func.id in forbidden_names)
        assert not (isinstance(node.func, ast.Attribute) and node.func.attr in forbidden_attributes)
        if isinstance(node.func, ast.Attribute) and node.func.attr == 'open':
            assert node.args and isinstance(node.args[0], ast.Constant) and node.args[0].value == 'rb'
        if (isinstance(node.func, ast.Attribute) and isinstance(node.func.value, ast.Name) and
                node.func.value.id == 're' and node.func.attr in {'search', 'findall', 'fullmatch', 'sub'} and
                node.args and isinstance(node.args[0], ast.Constant) and isinstance(node.args[0].value, str)):
            re.compile(node.args[0].value)
    assert {'main', 'bind_actual_terminal_documents', 'strict_pair', 'b_complete_reuse', 'round0_closure',
            'successive_round', 'terminal_build_package', 'terminal_complete_receiver_map',
            'current_pending_whole_and_links', 'final_current_closure', 'actual_terminal_outer',
            'actual_six_root_views'} <= set(named)
    final = json.loads((HERE / 'ACTUAL_BINDING.json').read_bytes())
    assert final['stage'] == 'ACTUAL_TERMINAL_ROOT_VIEWS_AND_FIRST_PENDING_LIFECYCLE_BOUND'
    assert final['root_acceptance'] is False and final['paper'] == 'P210'
    assert not any(isinstance(node, ast.Constant) and isinstance(node.value, str) and
                   node.value.startswith('UNBOUND_ACTUAL_TERMINAL_') for node in ast.walk(named['bind_actual_terminal_documents']))
    direct = {}
    for name, expected in final['named_input_pins'].items():
        path = Path(name)
        assert path.is_absolute() and path.is_file()
        direct[name] = digest(path)
        assert direct[name] == expected
    print(json.dumps({'status': 'PASS_AST_SOURCE_AND_NAMED_ACTUAL_DATA_ONLY_NOT_ARTIFACT_GATE',
        'source': digest(SOURCE), 'source_lines': len(text.splitlines()), 'function_count': len(functions),
        'imports': sorted(imports), 'verbatim_helpers': inherited,
        'verbatim_configuration_AST': meta['verbatim_helpers']['globals'],
        'complete_named_current_data_pins': direct,
        'reader_imported_or_executed': False, 'reader_function_calls': 0,
        'old_programs_imported_or_executed': 0, 'host_tree_walks_or_dependency_rehash_passes': 0,
        'new_science_runs': 0, 'new_builds': 0, 'new_views': 0,
        'root_acceptance': False, 'paper_completion': False, 'five_paper_completion': False}, sort_keys=True))


if __name__ == '__main__':
    main()
