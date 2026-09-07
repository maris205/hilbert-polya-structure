"""Root original/static closure for exact revision03, not target execution.

Checks the sealed preparer's native records, exact replace-once delta, original
emitter shapes and all pinned originals. Only three native diff comparisons run.
No target auditor, verifier, builder, renderer or lifecycle function is imported.
"""
import argparse
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
BASE = BATCH / 'qa/p209_terminal_artifact_revision_03'
OLD = BATCH / 'qa/p209_terminal_artifact_revision_02'
PAPER = ROOT / 'papers/209-ordered-fibre-threading'
ENV = {'PATH': '/usr/bin:/bin', 'LANG': 'C.UTF-8', 'LC_ALL': 'C.UTF-8', 'TZ': 'UTC'}
WATCH = {}


def read(path):
    p = Path(path)
    assert p.is_file(), str(p)
    if p.is_relative_to(ROOT): assert not p.is_symlink(), str(p)
    data = p.read_bytes()
    row = {'sha256': sha256(data).hexdigest(), 'bytes': len(data)}
    assert str(p) not in WATCH or WATCH[str(p)] == row, str(p)
    WATCH[str(p)] = row
    return data


def j(path): return json.loads(read(path))


def pin(path, row):
    p = Path(path); read(p)
    want = {'sha256': row} if isinstance(row, str) else row
    for key in ('sha256', 'bytes'):
        if key in want: assert WATCH[str(p)][key] == want[key], (str(p), key)


def pins(rows):
    for path, value in rows.items(): pin(path, value)


def manifest(base, count, digest):
    pin(base / 'SHA256SUMS', digest); rows = {}
    for line in read(base / 'SHA256SUMS').decode().splitlines():
        match = re.fullmatch(r'([0-9a-f]{64})  (.+)', line); assert match
        value, rel = match.groups(); path = Path(rel)
        assert rel not in rows and rel != 'SHA256SUMS'
        assert not path.is_absolute() and '..' not in path.parts
        rows[rel] = value; pin(base / rel, value)
    physical = set()
    for path in base.rglob('*'):
        assert not path.is_symlink(), str(path)
        if path.is_file(): physical.add(path.relative_to(base).as_posix())
    assert len(rows) == count and physical == set(rows) | {'SHA256SUMS'}, str(base)
    return rows


def functions(raw):
    tree = ast.parse(raw)
    compile(tree, '<source-only>', 'exec', dont_inherit=True, optimize=0)
    return {n.name: ast.get_source_segment(raw, n) for n in tree.body if isinstance(n, ast.FunctionDef)}


def emitter(path, role):
    tree = ast.parse(read(path))
    main = next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == 'main')
    if role == 'author':
        nodes = [n.value for n in ast.walk(main) if isinstance(n, ast.Assign)
                 and any(isinstance(t, ast.Name) and t.id == 'result' for t in n.targets)]
    else:
        nodes = [n.args[0] for n in ast.walk(main) if isinstance(n, ast.Call)
                 and isinstance(n.func, ast.Attribute) and isinstance(n.func.value, ast.Name)
                 and n.func.value.id == 'json' and n.func.attr == 'dumps']
    assert len(nodes) == 1 and isinstance(nodes[0], ast.Dict)
    keys = [ast.literal_eval(k) for k in nodes[0].keys]
    return set(keys), {k: v.value for k, v in zip(keys, nodes[0].values) if isinstance(v, ast.Constant)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--payloads', type=int, required=True)
    parser.add_argument('--sha256', required=True)
    args = parser.parse_args()
    assert args.payloads > 0 and re.fullmatch(r'[0-9a-f]{64}', args.sha256)
    began = datetime.now(timezone.utc).isoformat()
    read(Path(__file__)); read(Path(sys.executable)); read('/usr/bin/diff')
    manifest(BASE, args.payloads, args.sha256)
    result = j(BASE / 'STATIC_RESULT.json')
    assert result['status'] == 'PASS_STATIC_PREPARATION_ONLY_NOT_ARTIFACT_GATE'
    before = result['original_inputs_before']
    assert before == result['original_inputs_after'] and len(before) == result['original_input_paths']
    pins(before); pins(result['new_live_control_key'])
    for name, row in result['complete_original_package_rechecks'].items():
        assert row['complete_nonself'] and row['preserved_in_place']
        manifest(BATCH / 'qa' / name, row['payloads'], row['seal_sha256'])
    intake = j(BASE / 'SCHEMA_PROJECTIONS.json')
    originals = j(BASE / 'INTAKE_INPUTS_BEFORE.json')
    assert originals == j(BASE / 'INTAKE_INPUTS_AFTER.json') and len(originals) == 1881
    pins(originals)
    assert intake['all_original_inputs_unchanged'] and intake['unmatched_observations'] == {}
    assert all(row['matched'] for row in intake['observations'].values())
    assert len(intake['json_shapes']) == 986
    for path in intake['json_shapes']: j(path)
    copies = intake['selected_physical_copies']
    assert len(copies) == result['selected_copies_rechecked'] == 13
    copy_commands = result['fresh_native_copy_comparisons']
    assert len(copy_commands) == 13
    for copy, command in zip(copies, copy_commands):
        pin(copy['original'], copy); pin(copy['copy'], copy)
        assert read(copy['original']) == read(copy['copy'])
        assert command['argv'] == ['/usr/bin/cmp', '--', copy['original'], copy['copy']]
        assert command['cwd'] == str(ROOT) and command['env'] == ENV
        assert command['exit_code'] == 0 and command['stdout'] == command['stderr'] == ''
    archived = intake['actual_native_cmp_commands']
    assert len(archived) == result['retained_intake_native_comparisons'] == 19
    for command in archived:
        assert command['argv'][:2] == ['/usr/bin/cmp', '--'] and len(command['argv']) == 4
        assert command['cwd'] == str(ROOT) and command['env'] == ENV
        assert command['exit_code'] == 0 and command['stdout'] == command['stderr'] == ''
        assert read(command['argv'][2]) == read(command['argv'][3])
    expected = {'audit_p209.py': {'revision_originals_and_failure', 'strict_replays'},
                'record_audit.py': {'main'}, 'lifecycle_audit.py': set()}
    recipe = j(BASE / 'SOURCE_EDITS.json'); records = j(BASE / 'SOURCE_FUNCTION_CHECKS.json')
    assert set(recipe) == set(expected)
    unchanged = {}
    for name, edits in recipe.items():
        old = read(OLD / name).decode(); current = read(BASE / name).decode(); made = old
        assert read(OLD / name) == read(BASE / 'original_snapshot' / (OLD / name).relative_to(ROOT))
        for edit in edits:
            assert made.count(edit['old']) == edit['required_old_occurrences'] == 1
            made = made.replace(edit['old'], edit['new'], 1)
        assert made == current
        first, second = functions(old), functions(current)
        assert set(first) == set(second)
        changed = {key for key in first if first[key] != second[key]}
        assert changed == expected[name]
        imports = lambda raw: [ast.dump(n) for n in ast.parse(raw).body if isinstance(n, (ast.Import, ast.ImportFrom))]
        assert imports(old) == imports(current)
        unchanged[name] = len(first) - len(changed)
        assert result['literal_function_changes'][name] == {'changed': sorted(changed), 'unchanged': unchanged[name]}
        for key in first:
            assert records[name]['literal_function_source_comparisons'][key] == {
                'original_sha256': sha256(first[key].encode()).hexdigest(),
                'prepared_sha256': sha256(second[key].encode()).hexdigest(), 'equal': first[key] == second[key]}
        pin(BASE / name, result['source_pins'][name])
    assert unchanged == {'audit_p209.py': 33, 'record_audit.py': 3, 'lifecycle_audit.py': 36}
    auditor = ast.parse(read(BASE / 'audit_p209.py'))
    strict = next(n for n in auditor.body if isinstance(n, ast.FunctionDef) and n.name == 'strict_replays')
    contract_nodes = [n.value for n in ast.walk(strict) if isinstance(n, ast.Assign)
                      and any(isinstance(t, ast.Name) and t.id == 'canonical_fields' for t in n.targets)]
    assert len(contract_nodes) == 1 and isinstance(contract_nodes[0], ast.Subscript)
    contracts = ast.literal_eval(contract_nodes[0].value)
    field_records = j(BASE / 'CANONICAL_FIELD_CHECKS.json')
    for role, count in [('author', 98278), ('a', 135605), ('b', 54794)]:
        base = PAPER if role == 'author' else BATCH / ('reviews/p209_' + role)
        canonical = j(base / 'CANONICAL.json'); keys, constants = emitter(base / 'verify.py', role)
        assert set(canonical) == keys == set(contracts[role]) | {'boxes'}
        assert {k: v for k, v in canonical.items() if k != 'boxes'} == contracts[role]
        assert canonical['checks'] == count and all(canonical[k] == v for k, v in constants.items())
        row = field_records[role]; state_field = 'states' if role == 'b' else 'state_count'
        assert row['original_emitter_keys'] == sorted(keys) and row['original_emitter_literal_constants'] == constants
        assert row['prepared_exact_non_box_scalars'] == row['actual_non_box_scalars'] == contracts[role]
        assert row['actual_top_level_keys'] == sorted(canonical) and row['state_field'] == state_field
        assert row['top_level_status_present'] == ('status' in canonical) and row['sum_states'] == 3414
        assert row['actual_original_box_census'] == [{k: box[k] for k in ('n', state_field)} for box in canonical['boxes']]
        assert [box['n'] for box in canonical['boxes']] == list(range(6))
        assert [box[state_field] for box in canonical['boxes']] == [1, 1, 4, 27, 256, 3125]
        for name, key in [('CANONICAL.json', 'canonical_pin'), ('verify.py', 'verifier_pin'), ('bootstrap.py', 'bootstrap_pin')]: pin(base / name, row[key])
    diffs = []
    recorded_diffs = j(BASE / 'DIFF_COMMANDS.json')
    assert len(recorded_diffs) == len(result['fresh_native_complete_diffs']) == 3
    for row, final in zip(recorded_diffs, result['fresh_native_complete_diffs']):
        name = Path(row['argv'][-1]).name
        argv = ['/usr/bin/diff', '-u', '--', str(BASE / 'original_snapshot' / (OLD / name).relative_to(ROOT)), str(BASE / name)]
        assert row['argv'] == final['argv'] == argv
        assert row['cwd'] == final['cwd'] == str(ROOT) and row['env'] == final['env'] == ENV
        assert row['exit_code'] == final['exit_code'] == 1
        for stream in ('stdout', 'stderr'):
            pin(BASE / row[stream + '_path'], row[stream + '_sha256'])
            pin(BASE / final[stream]['path'], final[stream])
            assert read(BASE / row[stream + '_path']) == read(BASE / final[stream]['path'])
        child = subprocess.run(argv, cwd=ROOT, env=ENV, capture_output=True, check=False)
        assert child.returncode == 1 and child.stdout == read(BASE / row['stdout_path']) and child.stderr == b''
        diffs.append({'argv': argv, 'cwd': str(ROOT), 'environment': ENV, 'exit_code': 1,
                      'stdout': child.stdout.decode(), 'stderr': child.stderr.decode()})
    assert read(BASE / 'ADAPTATION.diff') == ''.join(row['stdout'] for row in diffs).encode()
    parsed = []
    for path in sorted(BASE.rglob('*.py')):
        compile(ast.parse(read(path), filename=str(path)), str(path), 'exec', dont_inherit=True, optimize=0)
        parsed.append(path.relative_to(BASE).as_posix())
    assert parsed == result['python_sources_parsed_compiled_not_executed']
    for number in ('01', '02', '03'):
        attempt = BATCH / ('qa/p209_terminal_artifact/initial_' + number)
        command = j(attempt / 'COMMAND.json')
        assert command['exit_code'] == 1 and command['inputs_unchanged'] and command['unused_cache_absent']
        assert j(attempt / 'INPUTS_BEFORE.json') == j(attempt / 'INPUTS_AFTER.json')
        assert read(attempt / 'audit.stdout') == b''
        wrapper = j(BATCH / ('qa/P209_TERMINAL_ARTIFACT_INITIAL_' + number + '.failed.actual.json'))
        assert wrapper['completion']['exit_code'] == 1
        assert read(attempt / 'audit.stderr').decode() in wrapper['completion']['output']
    assert not (BATCH / 'qa/p209_terminal_artifact/initial_04').exists()
    assert result['target_auditor_lifecycle_guard_executions'] == result['new_science_build_render_views'] == 0
    for path, value in WATCH.items():
        data = Path(path).read_bytes()
        assert value == {'sha256': sha256(data).hexdigest(), 'bytes': len(data)}, path
    print(json.dumps({'status': 'PASS_ROOT_REVISION03_COMPLETE_STATIC_ORIGINAL_PREFLIGHT_NOT_TARGET_EXECUTION',
        'started_utc': began, 'ended_utc': datetime.now(timezone.utc).isoformat(),
        'revision_payloads': args.payloads, 'revision_manifest_sha256': args.sha256,
        'original_paths_checked_twice': len(before), 'all_current_read_paths_checked_twice': len(WATCH),
        'read_map_sha256': sha256(json.dumps(WATCH, sort_keys=True).encode()).hexdigest(),
        'old_original_packages': result['complete_original_package_rechecks'],
        'original_physical_copies': 13, 'archived_native_cmp_commands': 32,
        'literal_unchanged_functions': unchanged, 'source_replace_once_and_imports_unchanged': True,
        'canonical_roles_and_original_emitters_checked': ['author', 'a', 'b'],
        'schema_records_read': 986, 'python_sources_static_only': len(parsed),
        'all_three_original_failures_unchanged': True, 'fresh_actual_raw_diffs': diffs,
        'target_science_build_view_lifecycle_executions': 0,
        'owner': 'OWNER_AMBER', 'external_status': 'HOLD_EXTERNAL'}, sort_keys=True, indent=2))


if __name__ == '__main__':
    assert sys.flags.isolated and sys.flags.no_site and sys.dont_write_bytecode and not sys.flags.optimize
    assert dict(os.environ) == ENV and Path.cwd() == ROOT
    main()
