"""Exclusive exact assembly from immutable revision03; native diff only.

The changes are the measured-page key, four named A semantic origins, the
mechanical current revision path/label and preservation of the actual fourth
failure. No target module or extracted target function is executed.
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
HERE = BATCH / 'qa/p209_terminal_artifact_revision_04'
OLD = BATCH / 'qa/p209_terminal_artifact_revision_03'
ENV = {'PATH': '/usr/bin:/bin', 'LANG': 'C.UTF-8', 'LC_ALL': 'C.UTF-8', 'TZ': 'UTC'}


def save(name, data):
    with (HERE / name).open('xb') as f:
        f.write(data)


def dump(name, value):
    save(name, (json.dumps(value, sort_keys=True, indent=2) + '\n').encode())


def funcs(source):
    tree = ast.parse(source)
    compile(tree, '<static-source-not-executed>', 'exec', dont_inherit=True, optimize=0)
    return {n.name: ast.get_source_segment(source, n) for n in tree.body if isinstance(n, ast.FunctionDef)}


def main():
    assert Path(__file__).resolve() == HERE / 'prepare_revision.py' and Path.cwd() == ROOT and dict(os.environ) == ENV
    assert sys.flags.isolated and sys.flags.no_site and sys.dont_write_bytecode and not sys.flags.optimize
    assert not (BATCH / 'qa/p209_terminal_artifact/initial_05').exists()
    inspected = json.loads((HERE / 'ORIGINAL_PREDICATE_INSPECTION.json').read_bytes())
    assert inspected['inputs_unchanged'] and len(inspected['unmatched_predicates']) == 4
    assert len(inspected['corrected_links']['named_four_role_corrections']) == 4
    old_path = "PREPARATION = BATCH / 'qa/p209_terminal_artifact_revision_03'"
    new_path = "PREPARATION = BATCH / 'qa/p209_terminal_artifact_revision_04'"
    failure = '''    # Preserve revision03 and the real initial04 root-view schema failure.
    # This appended documentary layer does not alter any older failure branch.
    revision03 = BATCH / 'qa/p209_terminal_artifact_revision_03'
    pin(revision03 / 'SHA256SUMS',
        '4863c739ce8189f19e484f33fd5b42ce8f69f3b292f42768ba638108c105a743')
    manifest(revision03, count=47)
    fourth = OUT / 'initial_04'
    pin(fourth / 'SHA256SUMS', 'bf5d128c27762025552fc730ba363e05a44874e28b2b2857d02db3fa2c8c4c7d')
    manifest(fourth, count=8)
    for snapshot, source in [('executed_auditor_snapshot.py', 'audit_p209.py'),
                             ('executed_recorder_snapshot.py', 'record_audit.py')]:
        ck(read(fourth / snapshot) == read(revision03 / source),
           'fourth_failed_exact_executed_sources', snapshot)
    row, attempt = j(fourth / 'COMMAND.json'), j(fourth / 'ATTEMPT.json')
    expected = ['/usr/bin/python3.10', '-I', '-S', '-B', '-X',
                'pycache_prefix=' + str(fourth / 'unused_pycache'),
                str(revision03 / 'audit_p209.py'), 'terminal-artifact-after-actual-views']
    ck(row['exit_code'] == 1 and row['status'] == 'COMPLETED' and row['failure'] is None
       and row['inputs_unchanged'] and row['unused_cache_absent'] and not (fourth / 'unused_pycache').exists()
       and row['argv'] == expected and row['cwd'] == str(ROOT) and row['environment'] == ENV,
       'fourth_failed_child_remains_failure', 'real initial_04 exit one; no reconstructed page view')
    ck(attempt['status'] == 'ATTEMPTED' and attempt['exit_code'] is None and
       all(attempt[k] == row[k] for k in ('argv', 'cwd', 'environment', 'started_utc')),
       'fourth_failed_prespawn_record', 'original fields')
    exact_pair(fourth, 'INPUTS_BEFORE.json', 'INPUTS_AFTER.json', 16, historical=True)
    for stream in ('stdout', 'stderr'):
        pin(fourth / ('audit.' + stream), row[stream])
    ck(read(fourth / 'audit.stdout') == b'' and len(read(fourth / 'audit.stderr')) == 652 and
       h(fourth / 'audit.stderr') == 'cffcade469b9bc33938a9102303db6a4fb7dd675943b58abe77645469a45881f',
       'fourth_failed_full_raw_streams', 'unchanged complete KeyError page_count traceback')
    execution = BATCH / 'qa/P209_TERMINAL_ARTIFACT_INITIAL_04.failed.actual.json'
    pin(execution, '483bac2c8955b9958ed02eb3741ed8bbeda6c48f36ad1ae9f1996fe26d32a340')
    outer = j(execution)
    ck(outer['completion']['exit_code'] == 1 and
       read(fourth / 'audit.stderr').decode() in outer['completion']['output'],
       'fourth_failed_root_wrapper_remains_failure', 'both original child and root wrapper remain exit one')
    return {'revision': 'p209_terminal_artifact_revision_04', 'original_preparation_payloads': 347,
            'preserved_revision_03_payloads': 47, 'preserved_initial_04_payloads': 8,
            'fourth_child_exit': 1, 'fourth_wrapper_exit': 1,
'''
    old_origin = """            pin(copied, row['sha256'])
            ck(str(copied) not in origins or origins[str(copied)] == source,
"""
    new_origin = """            pin(copied, row['sha256'])
            # Four named Round2 identity-input pins are not document origins.
            # Their exact A source/copy rows supply the semantic origin; no
            # other conflict, path or hash is exempted from the original check.
            exact_self_origin_roles = {
                ('delta_check_01', 'P209_A_RESPONSE.md'):
                    (BATCH / 'P209_A_RESPONSE.md', '3b84c6c6a39b890562a63fbcb76a1a1fdf683886b9f6670b4bdd05544c6e9459'),
                ('delta_check_02', 'P209_A_RESPONSE.md'):
                    (BATCH / 'P209_A_RESPONSE.md', '3b84c6c6a39b890562a63fbcb76a1a1fdf683886b9f6670b4bdd05544c6e9459'),
                ('delta_check_01', 'P209_A_ROOT_INITIAL_INSPECTION.md'):
                    (BATCH / 'qa/P209_A_ROOT_INITIAL_INSPECTION.md', 'c095b7365d9083b83f6cd802ea6a3c9fa372a8b670ba9b28ae11e29d562fe690'),
                ('delta_check_02', 'P209_A_ROOT_INITIAL_INSPECTION.md'):
                    (BATCH / 'qa/P209_A_ROOT_INITIAL_INSPECTION.md', 'c095b7365d9083b83f6cd802ea6a3c9fa372a8b670ba9b28ae11e29d562fe690')}
            role_key = (attempt0, copied.name)
            if role_key in exact_self_origin_roles:
                named_source, named_digest = exact_self_origin_roles[role_key]
                ck(source == named_source and row['sha256'] == named_digest and origins.get(str(copied)) == copied,
                   'exact_four_A_identity_pin_semantic_origin_roles', role_key)
                origins[str(copied)] = source
            ck(str(copied) not in origins or origins[str(copied)] == source,
"""
    old_tail = "              ROOT/'docs/papers204_208_sequence/qa/P209_TERMINAL_ARTIFACT_INITIAL_03.failed.actual.json']"
    new_tail = """              ROOT/'docs/papers204_208_sequence/qa/P209_TERMINAL_ARTIFACT_INITIAL_03.failed.actual.json',
              ROOT/'docs/papers204_208_sequence/qa/p209_terminal_artifact_revision_03/SHA256SUMS',
              BASE/'initial_04/SHA256SUMS',
              ROOT/'docs/papers204_208_sequence/qa/P209_TERMINAL_ARTIFACT_INITIAL_04.failed.actual.json']"""
    edits = {
        'audit_p209.py': [(old_path, new_path),
            ("    return {'revision': 'p209_terminal_artifact_revision_03', 'original_preparation_payloads': 347,\n", failure),
            ("and record['page_count'] == 4 and record['open_visual_findings'] == 0", "and record['measured_page_count'] == 4 and record['open_visual_findings'] == 0"),
            (old_origin, new_origin)],
        'record_audit.py': [("if sys.argv[1:] != ['initial_04']:", "if sys.argv[1:] != ['initial_05']:"),
            ('Require the new revision_03 initial_04 attempt', 'Require the new revision_04 initial_05 attempt'),
            ("and PREP==ROOT/'docs/papers204_208_sequence/qa/p209_terminal_artifact_revision_03'", "and PREP==ROOT/'docs/papers204_208_sequence/qa/p209_terminal_artifact_revision_04'"),
            (old_tail, new_tail)],
        'lifecycle_audit.py': [(old_path, new_path)]}
    allowed = {'audit_p209.py': {'revision_originals_and_failure', 'root_page_views', 'pages_and_links'},
               'record_audit.py': {'main'}, 'lifecycle_audit.py': set()}
    sources, recipes, native = {}, {}, []
    for name, changes in edits.items():
        original = OLD / name
        copy = HERE / 'original_snapshot' / original.relative_to(ROOT)
        before = original.read_bytes()
        assert copy.read_bytes() == before
        after = before.decode()
        recipes[name] = []
        for old, new in changes:
            assert after.count(old) == 1, (name, old)
            after = after.replace(old, new, 1)
            recipes[name].append({'old': old, 'new': new, 'required_old_occurrences': 1})
        save(name, after.encode())
        oldf, newf = funcs(before.decode()), funcs(after)
        assert set(oldf) == set(newf)
        changed = {n for n in oldf if oldf[n] != newf[n]}
        assert changed == allowed[name]
        sources[name] = {'original_sha256': sha256(before).hexdigest(), 'prepared_sha256': sha256(after.encode()).hexdigest(),
            'changed_functions': sorted(changed), 'unchanged_function_count': len(oldf) - len(changed),
            'literal_function_comparisons': {n: {'equal': oldf[n] == newf[n], 'original_sha256': sha256(oldf[n].encode()).hexdigest(),
                                                'prepared_sha256': sha256(newf[n].encode()).hexdigest()} for n in oldf}}
        argv = ['/usr/bin/diff', '-u', '--', str(copy), str(HERE / name)]
        child = subprocess.run(argv, cwd=ROOT, env=ENV, capture_output=True, check=False)
        save(name + '.diff', child.stdout)
        save(name + '.diff.stderr', child.stderr)
        assert child.returncode == 1 and child.stdout and child.stderr == b''
        native.append({'argv': argv, 'cwd': str(ROOT), 'env': ENV, 'exit_code': child.returncode,
                       'stdout_path': name + '.diff', 'stdout_sha256': sha256(child.stdout).hexdigest(),
                       'stderr_path': name + '.diff.stderr', 'stderr_sha256': sha256(child.stderr).hexdigest()})
    dump('SOURCE_EDITS.json', recipes)
    dump('SOURCE_FUNCTION_CHECKS.json', sources)
    dump('DIFF_COMMANDS.json', native)
    print(json.dumps({'status': 'PREPARED_REVISION04_NOT_EXECUTED', 'sources': sources, 'native_diff_exits': [r['exit_code'] for r in native], 'initial05_created': False}, sort_keys=True))


if __name__ == '__main__':
    main()
