"""Exclusive replace-once assembly; no target or extracted target function runs.

All source edits are reconstructed from the immutable revision02 originals.
Only native diff executes. AST/source comparison and compile do not execute
the target auditor, recorder or lifecycle module.
"""
import ast
from hashlib import sha256
import json
import os
from pathlib import Path
import subprocess
import sys

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
BATCH = ROOT / 'docs/papers204_208_sequence'
HERE = Path(__file__).resolve().parent
OLD = BATCH / 'qa/p209_terminal_artifact_revision_02'
ENV = {'PATH': '/usr/bin:/bin', 'LANG': 'C.UTF-8', 'LC_ALL': 'C.UTF-8', 'TZ': 'UTC'}


def save(name, raw):
    with (HERE / name).open('xb') as stream:
        stream.write(raw)


def dump(name, value):
    save(name, (json.dumps(value, indent=2, sort_keys=True) + '\n').encode())


def funcs(source):
    tree = ast.parse(source)
    compile(tree, '<static-only-not-executed>', 'exec', dont_inherit=True, optimize=0)
    return {node.name: ast.get_source_segment(source, node) for node in tree.body if isinstance(node, ast.FunctionDef)}


def main():
    assert HERE == BATCH / 'qa/p209_terminal_artifact_revision_03'
    assert dict(os.environ) == ENV and Path.cwd() == ROOT
    assert sys.flags.isolated == sys.flags.no_site == 1 and sys.flags.optimize == 0 and sys.dont_write_bytecode
    assert not (HERE / 'audit_p209.py').exists()
    assert not (BATCH / 'qa/p209_terminal_artifact/initial_04').exists()
    old_path = "PREPARATION = BATCH / 'qa/p209_terminal_artifact_revision_02'"
    new_path = "PREPARATION = BATCH / 'qa/p209_terminal_artifact_revision_03'"
    old_return = "    return {'revision': 'p209_terminal_artifact_revision_02', 'original_preparation_payloads': 347,\n"
    new_failure = '''    # Revision 02 and the real initial_03 schema failure remain immutable in
    # place; this correction does not replace either earlier preparation.
    revision02 = BATCH / 'qa/p209_terminal_artifact_revision_02'
    pin(revision02 / 'SHA256SUMS',
        '6e9c86fad5802ed82df5ffa78e3f7d7bc9c3bec00a04892c96e002db121ed6ed')
    manifest(revision02, count=79)
    third = OUT / 'initial_03'
    pin(third / 'SHA256SUMS', '45f4751ce36bfdfd432b2b5193ef23c8c7b91fa109b88cc4e305fd59234af921')
    manifest(third, count=8)
    for snapshot, source in [('executed_auditor_snapshot.py', 'audit_p209.py'),
                             ('executed_recorder_snapshot.py', 'record_audit.py')]:
        ck(read(third / snapshot) == read(revision02 / source),
           'third_failed_exact_executed_sources', snapshot)
    row, attempt = j(third / 'COMMAND.json'), j(third / 'ATTEMPT.json')
    expected = ['/usr/bin/python3.10', '-I', '-S', '-B', '-X',
                'pycache_prefix=' + str(third / 'unused_pycache'),
                str(revision02 / 'audit_p209.py'), 'terminal-artifact-after-actual-views']
    ck(row['exit_code'] == 1 and row['status'] == 'COMPLETED' and row['failure'] is None
       and row['inputs_unchanged'] and row['unused_cache_absent'] and not (third / 'unused_pycache').exists()
       and row['argv'] == expected and row['cwd'] == str(ROOT) and row['environment'] == ENV,
       'third_failed_child_remains_failure', 'real initial_03 exit one; no default canonical PASS')
    ck(attempt['status'] == 'ATTEMPTED' and attempt['exit_code'] is None and
       all(attempt[k] == row[k] for k in ('argv', 'cwd', 'environment', 'started_utc')),
       'third_failed_prespawn_record', 'original fields')
    exact_pair(third, 'INPUTS_BEFORE.json', 'INPUTS_AFTER.json', 13, historical=True)
    for stream in ('stdout', 'stderr'):
        pin(third / ('audit.' + stream), row[stream])
    ck(read(third / 'audit.stdout') == b'' and len(read(third / 'audit.stderr')) == 674 and
       h(third / 'audit.stderr') == '33820efd46d6cc2adf5c8c1ad27c6f4eb25f054e4607c0306f8409fe352c4077',
       'third_failed_full_raw_streams', 'unchanged complete KeyError status traceback')
    execution = BATCH / 'qa/P209_TERMINAL_ARTIFACT_INITIAL_03.failed.actual.json'
    pin(execution, '816cb77c887baca09e28a6a71b9c25fafadd2942bca587e20bd4a8ca4cf0581e')
    outer = j(execution)
    ck(outer['completion']['exit_code'] == 1 and
       read(third / 'audit.stderr').decode() in outer['completion']['output'],
       'third_failed_root_wrapper_remains_failure', 'both original child and root wrapper remain exit one')
    return {'revision': 'p209_terminal_artifact_revision_03', 'original_preparation_payloads': 347,
            'preserved_revision_02_payloads': 79, 'preserved_initial_03_payloads': 8,
            'third_child_exit': 1, 'third_wrapper_exit': 1,
'''
    old_canonical = "            ck(payload['status'] == 'PASS' and payload['checks'] == count, 'strict_actual_canonical_count', role)"
    new_canonical = '''            # Exact original emitter contracts differ by role. Reviewer A has
            # no top-level status field; success is independently required in
            # the real child receipt above, and full raw equality is unchanged.
            canonical_fields = {
                'author': {'schema': 'p209-author-v1', 'status': 'PASS', 'checks': 98278,
                           'total_states': 3414,
                           'scope': 'Exhaustive n=0,...,5 only; finite pressure, not all-size proof.',
                           'entrance_field_scope': 'Observed orbit index only; no all-size clock claim.'},
                'a': {'schema': 'p209-review-a-independent-v1', 'checks': 135605},
                'b': {'schema': 'p209-b-ports-constructive-carrier-v1', 'status': 'PASS',
                      'checks': 54794, 'states': 3414, 'max_n': 5}}[role]
            ck(type(payload) is dict and set(payload) == set(canonical_fields) | {'boxes'}
               and all(payload[key] == value for key, value in canonical_fields.items())
               and payload['checks'] == count,
               'strict_exact_role_canonical_schema_and_scalars', role)
            state_field = 'states' if role == 'b' else 'state_count'
            boxes = payload['boxes']
            ck(type(boxes) is list and [box['n'] for box in boxes] == list(range(6))
               and [box[state_field] for box in boxes] == [1, 1, 4, 27, 256, 3125]
               and sum(box[state_field] for box in boxes) == 3414,
               'strict_exact_original_canonical_census', role)'''
    old_tail = "              ROOT/'docs/papers204_208_sequence/qa/P209_TERMINAL_ARTIFACT_INITIAL_02.failed.actual.json']"
    new_tail = """              ROOT/'docs/papers204_208_sequence/qa/P209_TERMINAL_ARTIFACT_INITIAL_02.failed.actual.json',
              ROOT/'docs/papers204_208_sequence/qa/p209_terminal_artifact_revision_02/SHA256SUMS',
              BASE/'initial_03/SHA256SUMS',
              ROOT/'docs/papers204_208_sequence/qa/P209_TERMINAL_ARTIFACT_INITIAL_03.failed.actual.json']"""
    recipes = {
        'audit_p209.py': [(old_path, new_path), (old_return, new_failure), (old_canonical, new_canonical)],
        'record_audit.py': [
            ("if sys.argv[1:] != ['initial_03']:", "if sys.argv[1:] != ['initial_04']:"),
            ('Require the new revision_02 initial_03 attempt', 'Require the new revision_03 initial_04 attempt'),
            ("and PREP==ROOT/'docs/papers204_208_sequence/qa/p209_terminal_artifact_revision_02'",
             "and PREP==ROOT/'docs/papers204_208_sequence/qa/p209_terminal_artifact_revision_03'"),
            (old_tail, new_tail)],
        'lifecycle_audit.py': [(old_path, new_path)]}
    allowed = {'audit_p209.py': {'revision_originals_and_failure', 'strict_replays'},
               'record_audit.py': {'main'}, 'lifecycle_audit.py': set()}
    edits, checks, commands, combined = {}, {}, [], b''
    intake = json.loads((HERE / 'SCHEMA_PROJECTIONS.json').read_bytes())
    assert intake['unmatched_observations'] == {}
    for name, replacements in recipes.items():
        source = OLD / name
        copy = HERE / 'original_snapshot' / source.relative_to(ROOT)
        before = source.read_bytes()
        assert before == copy.read_bytes()
        after = before.decode()
        edits[name] = []
        for old, new in replacements:
            assert after.count(old) == 1, (name, old)
            after = after.replace(old, new, 1)
            edits[name].append({'old': old, 'new': new, 'required_old_occurrences': 1})
        save(name, after.encode())
        oldf, newf = funcs(before.decode()), funcs(after)
        assert set(oldf) == set(newf)
        changed = {key for key in oldf if oldf[key] != newf[key]}
        assert changed == allowed[name], (name, changed)
        checks[name] = {'original_sha256': sha256(before).hexdigest(), 'prepared_sha256': sha256(after.encode()).hexdigest(),
            'lines': len(after.splitlines()), 'function_count': len(oldf), 'changed_functions': sorted(changed),
            'literal_unchanged_functions': sorted(set(oldf) - changed),
            'literal_function_source_comparisons': {key: {'original_sha256': sha256(oldf[key].encode()).hexdigest(),
                'prepared_sha256': sha256(newf[key].encode()).hexdigest(), 'equal': oldf[key] == newf[key]} for key in oldf}}
        argv = ['/usr/bin/diff', '-u', '--', str(copy), str(HERE / name)]
        run = subprocess.run(argv, cwd=ROOT, env=ENV, capture_output=True, check=False)
        assert run.returncode == 1 and run.stdout and run.stderr == b''
        save(name + '.diff', run.stdout); save(name + '.diff.stderr', run.stderr)
        commands.append({'argv': argv, 'cwd': str(ROOT), 'env': ENV, 'exit_code': run.returncode,
                         'stdout_path': name + '.diff', 'stdout_sha256': sha256(run.stdout).hexdigest(),
                         'stderr_path': name + '.diff.stderr', 'stderr_sha256': sha256(run.stderr).hexdigest()})
        combined += run.stdout
    save('ADAPTATION.diff', combined)
    dump('SOURCE_EDITS.json', edits); dump('SOURCE_FUNCTION_CHECKS.json', checks); dump('DIFF_COMMANDS.json', commands)
    print(json.dumps({'status': 'PREPARED_SOURCE_ONLY_NOT_EXECUTED',
        'sources': {name: {key: row[key] for key in ('lines', 'prepared_sha256', 'changed_functions')} for name, row in checks.items()},
        'native_diff_exits': [row['exit_code'] for row in commands], 'target_executions': 0}, sort_keys=True))


if __name__ == '__main__':
    main()
