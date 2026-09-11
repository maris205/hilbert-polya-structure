"""Final static original/recipe/field check. Target modules never execute.

Only syntax parsing/compilation, literal dictionary inspection, data comparisons
and native cmp/diff run. Full runtime, link, dependency and lifecycle traversal
remain the future root-owned auditor's obligations.
"""
import ast
from datetime import datetime, timezone
from hashlib import sha256
import json
import os
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
BATCH = ROOT / 'docs/papers204_208_sequence'
HERE = Path(__file__).resolve().parent
OLD = BATCH / 'qa/p209_terminal_artifact_revision_02'
PAPER = ROOT / 'papers/209-ordered-fibre-threading'
ENV = {'PATH': '/usr/bin:/bin', 'LANG': 'C.UTF-8', 'LC_ALL': 'C.UTF-8', 'TZ': 'UTC'}


def info(path):
    data = Path(path).read_bytes()
    return {'sha256': sha256(data).hexdigest(), 'bytes': len(data)}


def js(path):
    return json.loads(Path(path).read_bytes())


def save(name, data):
    with (HERE / name).open('xb') as stream:
        stream.write(data)


def dump(name, value):
    save(name, (json.dumps(value, sort_keys=True, indent=2) + '\n').encode())


def functions(source):
    tree = ast.parse(source)
    return {node.name: ast.get_source_segment(source, node) for node in tree.body if isinstance(node, ast.FunctionDef)}


def package(base, count, digest):
    assert info(base / 'SHA256SUMS')['sha256'] == digest
    rows = {}
    for line in (base / 'SHA256SUMS').read_text().splitlines():
        match = re.fullmatch(r'([0-9a-f]{64})  (.+)', line)
        assert match
        value, name = match.groups()
        assert name not in rows and not Path(name).is_absolute() and '..' not in Path(name).parts
        rows[name] = value
    assert len(rows) == count
    assert all(not path.is_symlink() for path in base.rglob('*'))
    physical = {path.relative_to(base).as_posix() for path in base.rglob('*') if path.is_file()}
    assert set(rows) == physical - {'SHA256SUMS'}
    assert all(info(base / name)['sha256'] == value for name, value in rows.items())
    return {'payloads': len(rows), 'seal_sha256': digest, 'complete_nonself': True, 'preserved_in_place': True}


def emitter_dictionary(path, role):
    tree = ast.parse(Path(path).read_bytes())
    main = next(node for node in tree.body if isinstance(node, ast.FunctionDef) and node.name == 'main')
    if role == 'author':
        dictionaries = [node.value for node in ast.walk(main) if isinstance(node, ast.Assign)
                        and any(isinstance(t, ast.Name) and t.id == 'result' for t in node.targets)]
    else:
        dictionaries = [node.args[0] for node in ast.walk(main) if isinstance(node, ast.Call)
                        and isinstance(node.func, ast.Attribute) and isinstance(node.func.value, ast.Name)
                        and node.func.value.id == 'json' and node.func.attr == 'dumps']
    assert len(dictionaries) == 1 and isinstance(dictionaries[0], ast.Dict)
    node = dictionaries[0]
    keys = [ast.literal_eval(key) for key in node.keys]
    constants = {key: value.value for key, value in zip(keys, node.values) if isinstance(value, ast.Constant)}
    return set(keys), constants


def main():
    started = datetime.now(timezone.utc).isoformat()
    assert HERE == BATCH / 'qa/p209_terminal_artifact_revision_03'
    assert dict(os.environ) == ENV and Path.cwd() == ROOT
    assert sys.flags.isolated == sys.flags.no_site == 1 and sys.flags.optimize == 0 and sys.dont_write_bytecode
    assert not (HERE / 'STATIC_RESULT.json').exists() and not (HERE / 'SHA256SUMS').exists()
    assert not (BATCH / 'qa/p209_terminal_artifact/initial_04').exists()
    intake = js(HERE / 'SCHEMA_PROJECTIONS.json')
    inputs = js(HERE / 'INTAKE_INPUTS_BEFORE.json')
    assert inputs == js(HERE / 'INTAKE_INPUTS_AFTER.json')
    assert intake['unmatched_observations'] == {} and intake['all_original_inputs_unchanged'] is True
    assert intake['original_input_paths'] == len(inputs) == 1881 and len(intake['json_shapes']) == 986
    for path in (Path('/usr/bin/diff'), Path('/usr/bin/cmp'), Path(sys.executable).resolve()):
        value = info(path)
        assert str(path) not in inputs or inputs[str(path)] == value
        inputs[str(path)] = value
    before = {path: info(path) for path in inputs}
    assert before == inputs
    for path, digest in intake['new_live_control_pins'].items():
        assert info(path)['sha256'] == digest
    original_packages = {name: package(BATCH / 'qa' / name, row['payloads'], row['seal_sha256'])
                         for name, row in intake['protected_packages'].items()}
    actual_cmp = []
    for index, row in enumerate(intake['selected_physical_copies']):
        wanted = {key: row[key] for key in ('sha256', 'bytes')}
        assert info(row['original']) == info(row['copy']) == wanted
        argv = ['/usr/bin/cmp', '--', row['original'], row['copy']]
        run = subprocess.run(argv, cwd=ROOT, env=ENV, capture_output=True, check=False)
        assert run.returncode == 0 and run.stdout == run.stderr == b''
        actual_cmp.append({'argv': argv, 'cwd': str(ROOT), 'env': ENV, 'exit_code': run.returncode,
                           'stdout': run.stdout.decode(), 'stderr': run.stderr.decode()})
    recorded = intake['actual_native_cmp_commands']
    assert len(recorded) == 19 and all(row['exit_code'] == 0 and row['stdout'] == row['stderr'] == '' for row in recorded)
    recipe = js(HERE / 'SOURCE_EDITS.json')
    comparisons = js(HERE / 'SOURCE_FUNCTION_CHECKS.json')
    changes, source_pins, diff_commands = {}, {}, []
    expected_changes = {'audit_p209.py': {'revision_originals_and_failure', 'strict_replays'},
                        'record_audit.py': {'main'}, 'lifecycle_audit.py': set()}
    for name, replacements in recipe.items():
        old = (OLD / name).read_text()
        reconstructed = old
        for row in replacements:
            assert reconstructed.count(row['old']) == row['required_old_occurrences'] == 1
            reconstructed = reconstructed.replace(row['old'], row['new'], 1)
        actual = (HERE / name).read_text()
        assert reconstructed == actual
        f0, f1 = functions(old), functions(actual)
        assert set(f0) == set(f1)
        changed = {key for key in f0 if f0[key] != f1[key]}
        assert changed == expected_changes[name]
        for key in f0:
            result = {'original_sha256': sha256(f0[key].encode()).hexdigest(),
                      'prepared_sha256': sha256(f1[key].encode()).hexdigest(), 'equal': f0[key] == f1[key]}
            assert result == comparisons[name]['literal_function_source_comparisons'][key]
        changes[name] = {'changed': sorted(changed), 'unchanged': len(f0) - len(changed)}
        source_pins[name] = info(HERE / name)
        assert source_pins[name]['sha256'] == comparisons[name]['prepared_sha256']
    strict = functions((HERE / 'audit_p209.py').read_text())['strict_replays']
    assert 'payload.get(' not in strict and "payload['status']" not in strict
    assert strict.count("child['status'] == 'PASS'") == 1
    assert strict.count("read(folder / 'producer.stdout') == read(base / 'CANONICAL.json')") == 1
    recorder_tree = ast.parse((HERE / 'record_audit.py').read_bytes())
    required_nodes = [node.value for node in ast.walk(recorder_tree) if isinstance(node, ast.Assign)
                      and any(isinstance(target, ast.Name) and target.id == 'required' for target in node.targets)]
    assert len(required_nodes) == 1 and isinstance(required_nodes[0], ast.List) and len(required_nodes[0].elts) == 16
    tree = ast.parse((HERE / 'audit_p209.py').read_bytes())
    strict_node = next(node for node in tree.body if isinstance(node, ast.FunctionDef) and node.name == 'strict_replays')
    contract_nodes = [node.value for node in ast.walk(strict_node) if isinstance(node, ast.Assign)
                      and any(isinstance(target, ast.Name) and target.id == 'canonical_fields' for target in node.targets)]
    assert len(contract_nodes) == 1 and isinstance(contract_nodes[0], ast.Subscript)
    # Literal data extraction only: no target function, predicate or AST body is executed.
    contracts = ast.literal_eval(contract_nodes[0].value)
    fields = {}
    for role, expected_count in [('author', 98278), ('a', 135605), ('b', 54794)]:
        base = PAPER if role == 'author' else BATCH / ('reviews/p209_' + role)
        canonical = js(base / 'CANONICAL.json')
        emitter_keys, emitter_constants = emitter_dictionary(base / 'verify.py', role)
        scalars = {key: value for key, value in canonical.items() if key != 'boxes'}
        assert scalars == contracts[role]
        assert set(canonical) == emitter_keys == set(contracts[role]) | {'boxes'}
        assert all(canonical[key] == value for key, value in emitter_constants.items())
        assert canonical['checks'] == expected_count
        state_field = 'states' if role == 'b' else 'state_count'
        census = [{key: box[key] for key in ('n', state_field)} for box in canonical['boxes']]
        assert [box['n'] for box in census] == list(range(6))
        assert [box[state_field] for box in census] == [1, 1, 4, 27, 256, 3125]
        assert sum(box[state_field] for box in census) == 3414
        fields[role] = {'canonical_path': str(base / 'CANONICAL.json'), 'canonical_pin': info(base / 'CANONICAL.json'),
            'verifier_path': str(base / 'verify.py'), 'verifier_pin': info(base / 'verify.py'),
            'bootstrap_pin': info(base / 'bootstrap.py'), 'original_emitter_keys': sorted(emitter_keys),
            'original_emitter_literal_constants': emitter_constants, 'prepared_exact_non_box_scalars': contracts[role],
            'actual_top_level_keys': sorted(canonical), 'actual_non_box_scalars': scalars,
            'state_field': state_field, 'actual_original_box_census': census, 'sum_states': 3414,
            'top_level_status_present': 'status' in canonical,
            'interpretation': 'Documentary comparison of original emitter and recorded JSON; no scientific execution.'}
    for record in js(HERE / 'DIFF_COMMANDS.json'):
        run = subprocess.run(record['argv'], cwd=ROOT, env=ENV, capture_output=True, check=False)
        assert run.returncode == 1 and run.stdout == (HERE / record['stdout_path']).read_bytes() and run.stderr == b''
        name = Path(record['argv'][-1]).name
        out, err = 'final_diff_' + name + '.stdout', 'final_diff_' + name + '.stderr'
        save(out, run.stdout); save(err, run.stderr)
        diff_commands.append({'argv': record['argv'], 'cwd': str(ROOT), 'env': ENV, 'exit_code': run.returncode,
            'stdout': {'path': out, **info(HERE / out)}, 'stderr': {'path': err, **info(HERE / err)}})
    parsed = []
    for path in sorted(HERE.rglob('*.py')):
        compile(ast.parse(path.read_bytes(), filename=str(path)), str(path), 'exec', dont_inherit=True, optimize=0)
        parsed.append(path.relative_to(HERE).as_posix())
    failed = BATCH / 'qa/p209_terminal_artifact/initial_03'
    command = js(failed / 'COMMAND.json')
    wrapper_path = BATCH / 'qa/P209_TERMINAL_ARTIFACT_INITIAL_03.failed.actual.json'
    assert info(wrapper_path)['sha256'] == '816cb77c887baca09e28a6a71b9c25fafadd2942bca587e20bd4a8ca4cf0581e'
    assert command['exit_code'] == js(wrapper_path)['completion']['exit_code'] == 1
    assert command['inputs_unchanged'] is True and command['unused_cache_absent'] is True
    assert js(failed / 'INPUTS_BEFORE.json') == js(failed / 'INPUTS_AFTER.json')
    assert len(js(failed / 'INPUTS_BEFORE.json')) == 13
    assert (failed / 'audit.stdout').read_bytes() == b''
    assert info(failed / 'audit.stderr') == {'sha256': '33820efd46d6cc2adf5c8c1ad27c6f4eb25f054e4607c0306f8409fe352c4077', 'bytes': 674}
    assert (failed / 'audit.stderr').read_text() in js(wrapper_path)['completion']['output']
    assert not (BATCH / 'qa/p209_terminal_artifact/initial_04').exists()
    after = {path: info(path) for path in before}
    assert after == before
    dump('CANONICAL_FIELD_CHECKS.json', fields)
    result = {'schema': 'p209-terminal-artifact-revision03-static-preparation-v1',
        'status': 'PASS_STATIC_PREPARATION_ONLY_NOT_ARTIFACT_GATE', 'started_utc': started,
        'ended_utc': datetime.now(timezone.utc).isoformat(), 'original_input_paths': len(before),
        'original_inputs_before': before, 'original_inputs_after': after, 'all_original_inputs_unchanged': True,
        'complete_original_package_rechecks': original_packages,
        'selected_copies_rechecked': len(actual_cmp), 'fresh_native_copy_comparisons': actual_cmp,
        'retained_intake_native_comparisons': len(recorded), 'source_pins': source_pins,
        'literal_function_changes': changes, 'fresh_native_complete_diffs': diff_commands,
        'canonical_field_checks': 'CANONICAL_FIELD_CHECKS.json',
        'exact_role_keysets_and_non_box_scalars_match_original_emitters_and_records': True,
        'actual_original_census_per_role': [0, 1, 2, 3, 4, 5], 'actual_states_per_role': 3414,
        'python_sources_parsed_compiled_not_executed': parsed,
        'initial03_child_exit': 1, 'initial03_wrapper_exit': 1, 'initial04_created': False,
        'future_recorder_exact_required_input_count': 16,
        'target_auditor_lifecycle_guard_executions': 0, 'new_science_build_render_views': 0,
        'new_live_control_key': intake['new_live_control_pins'], 'new_historical_aliases': 0,
        'limitations': ['Static source/data preparation only, not a future full artifact gate result.',
                       'Original schema inspector raw-compared canonicals but omitted their JSON shapes.',
                       'No real runtime/dependency/link traversal, lifecycle execution, scientific replay, build or view ran.',
                       'The known input set is rechecked; this is not an OS-hermetic or continuous-observation claim.'],
        'external': 'OWNER_AMBER / HOLD_EXTERNAL'}
    dump('STATIC_RESULT.json', result)
    print(json.dumps({'status': result['status'], 'original_input_paths': len(before), 'copies': len(actual_cmp),
        'role_field_checks': sorted(fields), 'function_changes': changes, 'source_pins': source_pins,
        'target_executions': 0, 'initial04_created': False}, sort_keys=True))


if __name__ == '__main__':
    main()
