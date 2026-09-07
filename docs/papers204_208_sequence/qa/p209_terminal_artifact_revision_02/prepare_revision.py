"""Replace-once mechanical assembly and source-only validation for revision 02.

No target module is imported or executed. Only cmp/diff subprocesses are used.
All writes are new exclusive files under this single owned preparation path.
"""
import ast
from hashlib import sha256
import json
from pathlib import Path
import subprocess

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
HERE = Path(__file__).resolve().parent
OLD = ROOT / 'docs/papers204_208_sequence/qa/p209_terminal_artifact_revision_01'
ENV = {'PATH': '/usr/bin:/bin', 'LANG': 'C.UTF-8', 'LC_ALL': 'C.UTF-8', 'TZ': 'UTC'}


def save(name, data):
    with (HERE / name).open('xb') as stream: stream.write(data)


def dump(name, data):
    save(name, (json.dumps(data, indent=2, sort_keys=True) + '\n').encode())


def functions(source):
    tree = ast.parse(source)
    compile(tree, '<static-only>', 'exec', dont_inherit=True, optimize=0)
    return {node.name: ast.get_source_segment(source, node) for node in tree.body if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))}


def main():
    assert HERE == ROOT / 'docs/papers204_208_sequence/qa/p209_terminal_artifact_revision_02'
    assert not (HERE / 'audit_p209.py').exists()
    old_path = "PREPARATION = BATCH / 'qa/p209_terminal_artifact_revision_01'"
    new_path = "PREPARATION = BATCH / 'qa/p209_terminal_artifact_revision_02'"
    append_failure = '''    # Revision 01 and its real initial_02 failure are an additional immutable
    # historical layer. They are not replaced by this new prepared attempt.
    previous = BATCH / 'qa/p209_terminal_artifact_revision_01'
    pin(previous / 'SHA256SUMS',
        '855aba017f5a369c09696272579897324bbd906892b353d17f0c9eb6d7fcbcc5')
    manifest(previous, count=418)
    second = OUT / 'initial_02'
    pin(second / 'SHA256SUMS', '89ab791251744f3aa96911f871f108268c2ebb7e5e1da55329eea45eb70bbc96')
    manifest(second, count=8)
    for snapshot, source in [('executed_auditor_snapshot.py', 'audit_p209.py'),
                             ('executed_recorder_snapshot.py', 'record_audit.py')]:
        ck(read(second / snapshot) == read(previous / source),
           'second_failed_exact_executed_sources', snapshot)
    row, attempt = j(second / 'COMMAND.json'), j(second / 'ATTEMPT.json')
    expected = ['/usr/bin/python3.10', '-I', '-S', '-B', '-X',
                'pycache_prefix=' + str(second / 'unused_pycache'),
                str(previous / 'audit_p209.py'), 'terminal-artifact-after-actual-views']
    ck(row['exit_code'] == 1 and row['status'] == 'COMPLETED' and row['failure'] is None
       and row['inputs_unchanged'] and row['unused_cache_absent'] and not (second / 'unused_pycache').exists()
       and row['argv'] == expected and row['cwd'] == str(ROOT) and row['environment'] == ENV,
       'second_failed_child_remains_failure', 'real initial_02 exit one; not a gate PASS')
    ck(attempt['status'] == 'ATTEMPTED' and attempt['exit_code'] is None and
       all(attempt[k] == row[k] for k in ('argv', 'cwd', 'environment', 'started_utc')),
       'second_failed_prespawn_record', 'original fields')
    exact_pair(second, 'INPUTS_BEFORE.json', 'INPUTS_AFTER.json', 10, historical=True)
    for stream in ('stdout', 'stderr'):
        pin(second / ('audit.' + stream), row[stream])
    ck(read(second / 'audit.stdout') == b'' and
       h(second / 'audit.stderr') == '87df565befc65ce9d96c25cf6e28f470521bea9207750c17ee1123ed6384c09b',
       'second_failed_full_raw_streams', 'unchanged 871-byte initial census A traceback')
    execution = BATCH / 'qa/P209_TERMINAL_ARTIFACT_INITIAL_02.failed.actual.json'
    pin(execution, 'cb4872647ea63e9e2e9253dcb7d11d090947f8399c497a358239223241f9e602')
    outer = j(execution)
    ck(outer['completion']['exit_code'] == 1 and
       read(second / 'audit.stderr').decode() in outer['completion']['output'],
       'second_failed_root_wrapper_remains_failure', 'both original child and root wrapper remain exit one')
    return {'revision': 'p209_terminal_artifact_revision_02', 'original_preparation_payloads': 347,
            'previous_revision_payloads': 418, 'preserved_initial_02_payloads': 8,
            'second_child_exit': 1, 'second_wrapper_exit': 1,
'''
    old_return = "    return {'revision': 'p209_terminal_artifact_revision_01', 'original_preparation_payloads': 347,\n"
    initial_old = "        ck(initial['delta_status'] == 'UNASSESSED', 'initial_census_remains_initial', letter)"
    initial_new = """        expected_initial = {'a': 'NOT_YET_SUBMITTED_OR_ASSESSED', 'b': 'UNASSESSED'}
        ck(initial['delta_status'] == expected_initial[letter], 'initial_census_remains_initial', letter)"""
    recorder_old_tail = "              ROOT/'docs/papers204_208_sequence/qa/P209_TERMINAL_ARTIFACT_INITIAL_01.failed.actual.json']"
    recorder_new_tail = """              ROOT/'docs/papers204_208_sequence/qa/P209_TERMINAL_ARTIFACT_INITIAL_01.failed.actual.json',
              ROOT/'docs/papers204_208_sequence/qa/p209_terminal_artifact_revision_01/SHA256SUMS',
              BASE/'initial_02/SHA256SUMS',
              ROOT/'docs/papers204_208_sequence/qa/P209_TERMINAL_ARTIFACT_INITIAL_02.failed.actual.json']"""
    recipes = {
        'audit_p209.py': [(old_path, new_path), (old_return, append_failure), (initial_old, initial_new)],
        'record_audit.py': [
            ("if sys.argv[1:] != ['initial_02']:", "if sys.argv[1:] != ['initial_03']:"),
            ("Require the new revision_01 initial_02 attempt", "Require the new revision_02 initial_03 attempt"),
            ("and PREP==ROOT/'docs/papers204_208_sequence/qa/p209_terminal_artifact_revision_01'",
             "and PREP==ROOT/'docs/papers204_208_sequence/qa/p209_terminal_artifact_revision_02'"),
            (recorder_old_tail, recorder_new_tail)],
        'lifecycle_audit.py': [(old_path, new_path)]}
    allowed_changes = {'audit_p209.py': {'revision_originals_and_failure', 'reviews'},
                       'record_audit.py': {'main'}, 'lifecycle_audit.py': set()}
    edits, checks, commands = {}, {}, []
    all_diffs = b''
    for name, replacements in recipes.items():
        original = OLD / name
        preserved = HERE / 'original_snapshot' / original.relative_to(ROOT)
        before = original.read_bytes()
        assert before == preserved.read_bytes()
        after = before.decode()
        edits[name] = []
        for old, new in replacements:
            assert after.count(old) == 1, (name, old)
            after = after.replace(old, new, 1)
            edits[name].append({'old': old, 'new': new, 'required_old_occurrences': 1})
        save(name, after.encode())
        old_functions, new_functions = functions(before.decode()), functions(after)
        assert set(old_functions) == set(new_functions)
        changed = {k for k in old_functions if old_functions[k] != new_functions[k]}
        assert changed == allowed_changes[name], (name, changed)
        checks[name] = {'original_sha256': sha256(before).hexdigest(), 'prepared_sha256': sha256(after.encode()).hexdigest(),
            'lines': len(after.splitlines()), 'function_count': len(old_functions), 'changed_functions': sorted(changed),
            'literal_unchanged_functions': sorted(set(old_functions) - changed),
            'literal_function_source_comparisons': {k: {'original_sha256': sha256(old_functions[k].encode()).hexdigest(),
                'prepared_sha256': sha256(new_functions[k].encode()).hexdigest(), 'equal': old_functions[k] == new_functions[k]} for k in old_functions}}
        argv = ['/usr/bin/diff', '-u', '--', str(preserved), str(HERE / name)]
        run = subprocess.run(argv, cwd=ROOT, env=ENV, capture_output=True, check=False)
        assert run.returncode == 1 and run.stdout and run.stderr == b''
        save(name + '.diff', run.stdout); save(name + '.diff.stderr', run.stderr)
        all_diffs += run.stdout
        commands.append({'argv': argv, 'cwd': str(ROOT), 'env': ENV, 'exit_code': run.returncode,
                         'stdout_path': name + '.diff', 'stdout_sha256': sha256(run.stdout).hexdigest(),
                         'stderr_path': name + '.diff.stderr', 'stderr_sha256': sha256(run.stderr).hexdigest()})
    save('ADAPTATION.diff', all_diffs)
    dump('SOURCE_EDITS.json', edits); dump('SOURCE_FUNCTION_CHECKS.json', checks); dump('DIFF_COMMANDS.json', commands)
    print(json.dumps({'status': 'PREPARED_SOURCE_ONLY_NOT_EXECUTED',
        'sources': {k: {n: v[n] for n in ('lines', 'prepared_sha256', 'changed_functions')} for k, v in checks.items()},
        'actual_raw_diff_exits': [r['exit_code'] for r in commands], 'target_executions': 0}, sort_keys=True))


if __name__ == '__main__': main()
