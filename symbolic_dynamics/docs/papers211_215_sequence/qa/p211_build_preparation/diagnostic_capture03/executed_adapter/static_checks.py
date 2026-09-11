#!/usr/bin/env python3
"""AST and synthetic-FLS classification checks only; zero native build calls."""
import ast
import json
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
scope = {'__name__': 'p211_static_source', '__file__': str(HERE / 'build_p211.py')}
exec(compile((HERE / 'build_p211.py').read_bytes(), str(HERE / 'build_p211.py'), 'exec'), scope)


def main():
    checks = []
    names = ('build_core.py', 'prepare_build.py', 'build_p211.py', 'launch_build.py', 'static_checks.py')
    for name in names:
        tree = ast.parse((HERE / name).read_bytes(), filename=str(HERE / name))
        forbidden = [n for n in ast.walk(tree) if isinstance(n, ast.Call) and
                     isinstance(n.func, ast.Attribute) and n.func.attr in
                     ('unlink', 'rmdir', 'rmtree', 'rename')]
        assert not forbidden, name + ': destructive/overwrite call'
        # str.replace is used for cwd templates and command labels; it is not
        # a filesystem overwrite. The fully read source has no Path/os.replace.
        overwrite = [n for n in ast.walk(tree) if isinstance(n, ast.Call) and
                     isinstance(n.func, ast.Attribute) and n.func.attr == 'replace' and
                     isinstance(n.func.value, ast.Name) and n.func.value.id == 'os']
        assert not overwrite, name + ': os.replace'
        checks.append({'check': 'AST_NO_DELETE_RENAME_OR_OS_REPLACE', 'file': name, 'passed': True,
                       'limit': 'Not a dataflow proof; root must read all source.'})
    assert len(scope['ENV8']) == 8 and 'HOME' not in scope['ENV8']
    assert scope['source_graph']()['bibliography_style'] == 'amsplain'
    assert [x[0] for x in scope['FOUR_COMMANDS']] == ['pass1', 'bibtex', 'pass2', 'pass3']
    assert all('-no-shell-escape' in argv for label, argv in scope['FOUR_COMMANDS'] if label != 'bibtex')
    checks.append({'check': 'ENV8_GRAPH_FOUR_COMMANDS', 'passed': True})
    # This is a pure parser fixture. Existing source files are not consumed;
    # input events reference only synthetic generated-before/output roles.
    cold = Path('/nonexistent_p211_static_fixture')
    blank = {name: {'present': False} for name in scope['GENERATED']}
    before = dict(blank)
    before['main.bbl'] = {'present': True, 'bytes': 3, 'sha256': 'a' * 64}
    after = dict(before)
    after['main.aux'] = {'present': True, 'bytes': 4, 'sha256': 'b' * 64}
    raw = ('PWD ' + str(cold) + '\nOUTPUT main.aux\nINPUT main.aux\n'
           'INPUT main.bbl\nINPUT ./main.bbl\n').encode()
    parsed = scope['classify_fls'](raw, cold, {}, before, after, {})
    assert parsed['roles']['GENERATED_EARLIER_OUTPUT_SAME_PASS'] == 1
    assert parsed['roles']['GENERATED_BEFORE'] == 2
    assert parsed['count'] == 5
    checks.append({'check': 'FLS_ORDER_AND_DUPLICATES', 'passed': True})
    rejected = 0
    for raw in (b'INPUT main.aux\n', b'INPUT unknown.aux\n', b'OUTPUT main.tex\n',
                b'OUTPUT /tmp/not_owned_output\n'):
        try:
            scope['classify_fls'](raw, cold, {}, blank, blank, {})
        except RuntimeError:
            rejected += 1
    assert rejected == 4
    checks.append({'check': 'FLS_UNKNOWN_OR_UNGENERATED_REFUSALS', 'passed': True, 'cases': rejected})
    future = Path('/nonexistent_p211_static_binding')
    relative_path = future / 'inner/source_only/texmf'
    binding = {'output': str(future), 'cwd_relative_configuration':
               {str(relative_path): scope['entry'](relative_path)}}
    lock = {'cwd_relative_absence_roles': {'TEXMFHOME':
            {'relative': 'texmf', 'required_state': 'ABSENT'}},
            'selector_specs': {}, 'entries': {}}
    specs, expected = scope['configuration_key'](binding, lock)
    assert set(specs) == {str(relative_path)} and expected[str(relative_path)]['present'] is False
    binding['cwd_relative_configuration'] = {}
    try:
        scope['configuration_key'](binding, lock)
    except RuntimeError:
        checks.append({'check': 'CWD_RELATIVE_ABSENCE_REQUIRES_EXACT_ROOT_BINDING', 'passed': True})
    else:
        raise AssertionError('Missing relative configuration role accepted')
    try:
        scope['binding_inputs'](HERE / 'BINDING.pending.json')
    except RuntimeError as error:
        assert 'PENDING_ROOT_BINDING' in str(error)
        checks.append({'check': 'PENDING_BINDING_REFUSES_BEFORE_OUTPUT_OR_CHILD', 'passed': True})
    else:
        raise AssertionError('Pending binding accepted')
    print(json.dumps({'status': 'STATIC_ONLY_NO_BUILD', 'checks': checks,
                      'native_children': 0, 'tex_compilations': 0,
                      'scientific_executions': 0, 'acceptance': False}, sort_keys=True))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
