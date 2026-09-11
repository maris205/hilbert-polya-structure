"""Static original JSON/emitters intake only; never imports target modules.

Reads actual role-specific schemas and remaining auditor data dereferences.
Checks immutable packages in place and makes only small selected source/record
copies. No scientific verifier, target audit, lifecycle, guard or builder runs.
"""
from collections import Counter
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
FINAL = PAPER / 'qa_final'
ENV = {'PATH': '/usr/bin:/bin', 'LANG': 'C.UTF-8', 'LC_ALL': 'C.UTF-8', 'TZ': 'UTC'}
PACKAGES = [
    ('p209_terminal_artifact_preparation', 347, '3250ea718e5b0f358a8a54ba2365a53732d637a2f9686c017e1767e4cdcc7e51'),
    ('p209_terminal_artifact_revision_01', 418, '855aba017f5a369c09696272579897324bbd906892b353d17f0c9eb6d7fcbcc5'),
    ('p209_terminal_artifact_revision_02', 79, '6e9c86fad5802ed82df5ffa78e3f7d7bc9c3bec00a04892c96e002db121ed6ed'),
    ('p209_terminal_artifact/initial_01', 8, 'deb48a3ed612ad9e292436e2037a879df37a0a5e2204594702f436c73bbe4b04'),
    ('p209_terminal_artifact/initial_02', 8, '89ab791251744f3aa96911f871f108268c2ebb7e5e1da55329eea45eb70bbc96'),
    ('p209_terminal_artifact/initial_03', 8, '45f4751ce36bfdfd432b2b5193ef23c8c7b91fa109b88cc4e305fd59234af921')]
CONTROLS = {
    ROOT / 'SYMBOLIC_DYNAMICS_STATE.md': '736e3f648bc6dda583254dcc58f49fc764043c30ea464ec524fac04f2ec67265',
    BATCH / 'PIPELINE_STATE.md': '70de1375b0b55339408b7399178a17f91f3058b3f068faa7c395ab633e525b47',
    BATCH / 'GIT_SYNC_RECEIPT.md': '303e1ad876f35fc6715d896f2979fd212f64aeb686ebd8ee1e2d649e9628b230',
    PAPER / 'PAPER_MANIFEST.sha256': '84337036dead70c7680aed5678ed770505b1caa0184b5f405d353c4d9a811c77',
    PAPER / 'ROOT_LIFECYCLE.md': '5d0381c67eb47234f19c962ffd55a1ad00f6617129c64bda62ff5736f24b87e4'}
PINS, SHAPES, OBS, CMPS = {}, {}, {}, []


def raw(path):
    path = Path(path)
    data = path.read_bytes()
    value = {'sha256': sha256(data).hexdigest(), 'bytes': len(data)}
    assert str(path) not in PINS or PINS[str(path)] == value, str(path)
    PINS[str(path)] = value
    return data


def fields(values):
    return [{'fields': list(key), 'rows': count} for key, count in sorted(Counter(
        tuple(sorted(row)) if isinstance(row, dict) else (type(row).__name__,) for row in values).items())]


def shape(value):
    if isinstance(value, dict):
        if len(value) > 100 or (value and all(str(k).startswith('/') for k in value)):
            return {'kind': 'mapping', 'rows': len(value), 'fieldsets': fields(value.values())}
        return {k: shape(v) for k, v in value.items() if k != 'maps'}
    if isinstance(value, list):
        return {'kind': 'list', 'rows': len(value), 'fieldsets': fields(value),
                'values': value if len(value) <= 12 and all(not isinstance(v, (dict, list)) for v in value) else None}
    return value


def obj(path):
    value = json.loads(raw(path))
    SHAPES[str(path)] = shape(value)
    return value


def note(key, condition, details=None):
    assert key not in OBS
    OBS[key] = {'matched': bool(condition), 'details': details}


def save(name, data):
    path = HERE / name
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('xb') as stream:
        stream.write(data)


def dump(name, value):
    save(name, (json.dumps(value, sort_keys=True, indent=2) + '\n').encode())


def pair(base, first, second):
    a, b = obj(base / first), obj(base / second)
    note(str(base / first) + ' == ' + second, a == b, {'rows': len(a)})
    return a


def native_cmp(first, second, purpose):
    raw(first); raw(second)
    argv = ['/usr/bin/cmp', '--', str(first), str(second)]
    run = subprocess.run(argv, cwd=ROOT, env=ENV, capture_output=True, check=False)
    row = {'argv': argv, 'cwd': str(ROOT), 'env': ENV, 'exit_code': run.returncode,
           'stdout': run.stdout.decode(), 'stderr': run.stderr.decode(), 'purpose': purpose}
    CMPS.append(row)
    assert run.returncode == 0 and run.stdout == run.stderr == b'', row


def protected_packages():
    result = {}
    for name, count, expected in PACKAGES:
        base = BATCH / 'qa' / name
        seal = raw(base / 'SHA256SUMS')
        assert sha256(seal).hexdigest() == expected, name
        rows = {}
        for line in seal.decode().splitlines():
            match = re.fullmatch(r'([0-9a-f]{64})  (.+)', line)
            assert match, name
            digest, rel = match.groups()
            assert rel not in rows and not Path(rel).is_absolute() and '..' not in Path(rel).parts
            rows[rel] = digest
        physical = {p.relative_to(base).as_posix() for p in base.rglob('*') if p.is_file()}
        assert len(rows) == count and set(rows) == physical - {'SHA256SUMS'}, name
        assert all(not p.is_symlink() for p in base.rglob('*'))
        for rel, digest in rows.items():
            assert sha256(raw(base / rel)).hexdigest() == digest, (name, rel)
        result[name] = {'payloads': count, 'seal_sha256': expected, 'complete_nonself': True, 'preserved_in_place': True}
    return result


def modern(base, filename='ALL_COMMAND_RECORDS.json'):
    entries = obj(base / filename)
    for entry in entries:
        folder, tag, row = Path(entry['folder']), entry['tag'], entry['command']
        real = obj(folder / (tag + '.command.json'))
        attempt = obj(folder / (tag + '.attempt.json'))
        samples = obj(folder / (tag + '.maps.json'))
        note(str(folder / tag), real == row and all(attempt[k] == row[k] for k in ('argv', 'cwd', 'env', 'stdout', 'stderr'))
             and row['exit'] == 0 and row['process_outcome'] == 'COMPLETED' and row['spawn_error'] is None
             and row['cleanup'] == [] and row['env'] == ENV and
             sorted({p for sample in samples['samples'] for p in sample['mapped_files']}) == entry['mapped_files'],
             {'exit': row['exit'], 'attempt_keys': sorted(attempt), 'command_keys': sorted(row)})
    return entries


def main():
    began = datetime.now(timezone.utc).isoformat()
    assert HERE == BATCH / 'qa/p209_terminal_artifact_revision_03'
    assert dict(os.environ) == ENV and Path.cwd() == ROOT
    assert sys.flags.isolated == sys.flags.no_site == 1 and sys.flags.optimize == 0 and sys.dont_write_bytecode
    assert not (HERE / 'SCHEMA_PROJECTIONS.json').exists()
    assert not (BATCH / 'qa/p209_terminal_artifact/initial_04').exists()
    raw(Path(__file__).resolve()); raw(Path(sys.executable).resolve()); raw(Path('/usr/bin/cmp'))
    protected = protected_packages()
    for path, wanted in CONTROLS.items():
        assert sha256(raw(path)).hexdigest() == wanted
    selected = [OLD / n for n in ('audit_p209.py', 'record_audit.py', 'lifecycle_audit.py')]
    for name in ('README.md', 'REMAINING_SCHEMA_INSPECTION.md', 'inspect_schema.py', 'prepare_revision.py',
                 'finish_revision.py', 'audit_p209.py.diff', 'record_audit.py.diff', 'lifecycle_audit.py.diff'):
        raw(OLD / name)
    failure = BATCH / 'qa/p209_terminal_artifact/initial_03'
    selected += [failure / n for n in ('COMMAND.json', 'ATTEMPT.json', 'audit.stderr')]
    wrapper_path = BATCH / 'qa/P209_TERMINAL_ARTIFACT_INITIAL_03.failed.actual.json'
    selected.append(wrapper_path)
    command, attempt, wrapper = obj(failure / 'COMMAND.json'), obj(failure / 'ATTEMPT.json'), obj(wrapper_path)
    note('real_initial03_failure_preserved', command['exit_code'] == wrapper['completion']['exit_code'] == 1
         and command['stdout']['bytes'] == 0 and command['stderr'] == {'bytes': 674, 'sha256': '33820efd46d6cc2adf5c8c1ad27c6f4eb25f054e4607c0306f8409fe352c4077'}
         and raw(failure / 'audit.stdout') == b'' and raw(failure / 'audit.stderr').decode() in wrapper['completion']['output'])
    assert PINS[str(wrapper_path)]['sha256'] == '816cb77c887baca09e28a6a71b9c25fafadd2942bca587e20bd4a8ca4cf0581e'
    note('real_initial03_prespawn_shared_fields', attempt['status'] == 'ATTEMPTED' and attempt['exit_code'] is None
         and all(attempt[k] == command[k] for k in ('argv', 'cwd', 'environment', 'started_utc')))
    pair(failure, 'INPUTS_BEFORE.json', 'INPUTS_AFTER.json')
    canonical_projections = {}
    for role, count, expected_status in [('author', 98278, 'PASS_ROOT_AUTHOR_PAIR'), ('a', 135605, 'PASS_ROOT_REVIEW_A_PAIR'),
                                        ('b', 54794, 'PASS_ROOT_REVIEW_B_PAIR')]:
        base = PAPER if role == 'author' else BATCH / ('reviews/p209_' + role)
        selected += [base / 'verify.py', base / 'bootstrap.py']
        data = obj(base / 'CANONICAL.json')
        canonical_projections[role] = {'path': str(base / 'CANONICAL.json'), **PINS[str(base / 'CANONICAL.json')],
            'top_level_keys': sorted(data), 'scalars': {k: v for k, v in data.items() if k != 'boxes'},
            'box_fields': fields(data['boxes']), 'boxes': [{k: box[k] for k in ('n', 'state_count', 'states') if k in box}
                                                         for box in data['boxes']]}
        rr = BATCH / ('qa/root_replays/p209_' + role + '_strict/root_' + role + '_pair_01')
        launcher = rr.parent / ('launcher_root_' + role + '_pair_01')
        rec = obj(rr / 'RECEIPT.json')
        note(role + '_root_receipt', rec['status'] == expected_status and rec['mode'] == 'pair'
             and rec['failures'] == [] and rec['result']['canonical_adopted'] is False)
        for name in ('PARENT_BEFORE.json', 'PARENT_AFTER.json', 'LINKAGE.json', 'OBSERVED_CLOSURE.json'):
            obj(rr / name)
        inputs = pair(rr, 'ALL_INPUTS_INCLUDING_CAPSULES_BEFORE.json', 'ALL_INPUTS_AFTER.json')
        runtime = pair(rr, 'RUNTIME_BEFORE.json', 'RUNTIME_AFTER.json')
        pair(rr, 'CONFIGURATION_BEFORE.json', 'CONFIGURATION_AFTER.json')
        note(role + '_runtime_rows_match_inputs', all(inputs.get(k) == v for k, v in runtime.items()))
        entries = modern(rr)
        note(role + '_command_count', len(entries) == 85)
        for label in ('replay_01', 'replay_02'):
            folder = rr / label
            child = obj(folder / 'RECEIPT.json')
            note(role + '_' + label + '_child_success_and_closure', child['status'] == 'PASS'
                 and child['failure'] is None and child['inputs_unchanged'] is True
                 and child['checks'] == count and child['total_states'] == 3414
                 and child['source_only_initial_names'] == ['bootstrap.py', 'verify.py']
                 and child['closure']['uncovered'] == child['closure']['bytecode'] == [])
            pair(folder, 'INPUTS_BEFORE.json', 'INPUTS_AFTER.json')
            native_cmp(folder / 'producer.stdout', base / 'CANONICAL.json', 'unchanged complete raw canonical; no science execution')
            child_payload = obj(folder / 'producer.stdout')
            note(role + '_' + label + '_canonical_shape', sorted(child_payload) == sorted(data) and child_payload['checks'] == count)
            for when in ('before', 'after'):
                obs = obj(folder / ('child.' + when + '.json'))
                note(role + '_' + label + '_' + when + '_actual_child_fields', obs['env'] == ENV and obs['optimize'] == 0
                     and obs['isolated'] == obs['no_site'] == 1 and obs['dont_write_bytecode'] is True and obs['cache_exists'] is False)
            for name in ('bootstrap.py', 'verify.py'):
                note(role + '_' + label + '_' + name + '_same_source', raw(folder / 'source_inputs' / name) == raw(base / name))
        launch = obj(launcher / 'RECEIPT.json')
        note(role + '_launcher_fields', launch['status'] == 'PASS_ROOT_LAUNCH' and launch['exit'] == 0
             and launch['outcome'] == 'COMPLETED' and launch['failure'] is None and launch['inputs_unchanged'] is True
             and launch['cache_absent'] is True and launch['env'] == ENV and launch['cwd'] == str(ROOT)
             and launch['recorder_closure']['payloads'] == 462 and launch['recorder_closure']['status'] == expected_status)
        pair(launcher, 'INPUTS_BEFORE.json', 'INPUTS_AFTER.json')
        note(role + '_launcher_stdout_status', obj(launcher / 'recorder.stdout')['status'] == expected_status)
    b = BATCH / 'reviews/p209_b'
    reconciled = obj(b / 'auxiliary_01/reconcile.stdout')
    note('normalized_reconciliation_schema_fields', reconciled['status'] == 'PASS_FULL_MATHEMATICAL_PAYLOAD_RECONCILIATION'
         and reconciled['row_count'] == 3414 and reconciled['checks'] == 78548 and len(reconciled['rows']) == 3414
         and all(row['status'] == 'ALL_EQUAL' for row in reconciled['rows']))
    note('normalized_reconciliation_command_count', len(modern(b / 'auxiliary_01')) == 4)
    pair(b / 'auxiliary_01', 'INPUTS_BEFORE.json', 'INPUTS_AFTER.json')
    inventory = {stem: pair(FINAL, stem + '_BEFORE.json', stem + '_AFTER.json') for stem in
                 ('INPUTS', 'RUNTIME', 'TEX_INVENTORY', 'CONFIGURATION', 'LIBRARIES', 'CONSUMED_TEX', 'RECORDER_INPUTS')}
    build = obj(FINAL / 'BUILD_EXECUTION.json')
    note('terminal_inventory_count_fields', tuple(len(inventory[n]) for n in ('INPUTS', 'RUNTIME', 'TEX_INVENTORY',
         'CONFIGURATION', 'LIBRARIES', 'CONSUMED_TEX')) == tuple(build[k] for k in ('input_count', 'runtime_count',
         'tex_inventory_count', 'configuration_count', 'resolved_link_file_count', 'consumed_tex_count')))
    note('terminal_pair_summary', build['status'] == 'PASS_P209_TERMINAL_BUILD_PAIR_NOT_VIEWED' and build['failures'] == []
         and build['command_census_complete'] is True and len(build['commands']) == 32 and len(build['builds']) == 2)
    for row in build['commands']:
        native = obj(FINAL / (row['label'] + '.command.json'))
        attempt = obj(FINAL / (row['label'] + '.attempt.json'))
        note('terminal_' + row['label'] + '_command_attempt', row == native and row['exit_code'] == 0
             and row['status'] == 'COMPLETED' and row['cleanup'] == [] and row['start_new_session'] is True
             and attempt['status'] == 'ATTEMPTED' and attempt['exit_code'] is None
             and all(row[k] == attempt[k] for k in ('argv', 'cwd', 'environment', 'started_utc')))
    covered = dict(inventory['INPUTS'])
    for key in ('RUNTIME', 'LIBRARIES', 'RECORDER_INPUTS'):
        covered.update(inventory[key])
    covered.update({v['resolved']: {k: v[k] for k in ('sha256', 'bytes')}
                    for v in inventory['CONFIGURATION'].values() if v['is_file']})
    for phase in ('BEFORE', 'AFTER'):
        obs = obj(FINAL / ('RECORDER_RUNTIME_' + phase + '.json'))
        note('terminal_parent_' + phase + '_maps_and_modules', all(covered.get(k) == v for k, v in obs['mapped_files'].items())
             and all(covered.get(v['path']) == {k: v[k] for k in ('sha256', 'bytes')} for v in obs['modules'].values()))
    obj(FINAL / 'USER_ROOTS_AFTER.json'); obj(FINAL / 'GENERATED_LOCAL_TEX_INPUTS.json')
    for number in (1, 2):
        for suffix in ('SOURCE_ONLY_INITIAL', 'USER_ROOTS_BEFORE', 'MEASURED_PDF', 'DIAGNOSTICS'):
            obj(FINAL / ('cold_build_' + str(number) + '_' + suffix + '.json'))
        for passno in (1, 2, 3):
            obj(FINAL / ('cold_build_' + str(number) + '_pass' + str(passno) + '_TEX_INPUTS.json'))
    launcher = BATCH / 'qa/root_replays/p209_terminal_strict/launcher_terminal_pair_01'
    obj(launcher / 'RECEIPT.json')
    stdout = obj(launcher / 'recorder.stdout')
    note('terminal_outer_stdout_fields', all(build.get(k) == v for k, v in stdout.items()))
    outer_inputs = pair(launcher, 'INPUTS_BEFORE.json', 'INPUTS_AFTER.json')
    coverage = {v['resolved']: {k: v[k] for k in ('sha256', 'bytes', 'resolved')} for v in outer_inputs.values()}
    for phase in ('BEFORE', 'AFTER'):
        obs = obj(launcher / ('LAUNCHER_RUNTIME_' + phase + '.json'))
        note('terminal_launcher_' + phase + '_maps_and_modules', all(coverage.get(k) == v for k, v in obs['mapped_files'].items())
             and all(coverage.get(v['path']) == {k: v[k] for k in ('sha256', 'bytes', 'resolved')} for v in obs['modules'].values()))
    obj(BATCH / 'qa/P209_TERMINAL_ROOT_VIEWS.actual.json')
    for number in (0, 1, 2):
        obj(PAPER / ('frozen_round' + str(number)) / ('FROZEN_LINK_MAP.json' if number == 0 else 'ROUND' + str(number) + '_PROVENANCE.json'))
    a = BATCH / 'reviews/p209_a'
    for attempt in ('delta_check_01', 'delta_check_02'):
        obj(a / attempt / 'RESPONSE_ORIGINALS_AND_COPIES.json')
    obj(PAPER / 'source_context/MAPPING.json')
    obj(b / 'delta_check_01/EXACT_HISTORY_ALIASES.json')
    obj(b / 'assignment_context/ROLES.json'); obj(b / 'delta_intake_01/INTAKE_RESULT.json')
    copies = []
    for source in selected:
        target = HERE / 'original_snapshot' / source.relative_to(ROOT)
        save(target.relative_to(HERE), raw(source))
        native_cmp(source, target, 'small exact selected original copy')
        copies.append({'original': str(source), 'copy': str(target), **PINS[str(source)]})
    before = {key: value for key, value in PINS.items() if not Path(key).is_relative_to(HERE)}
    after = {key: {'sha256': sha256(Path(key).read_bytes()).hexdigest(), 'bytes': Path(key).stat().st_size} for key in before}
    assert after == before
    result = {'schema': 'p209-revision03-original-schema-intake-v1', 'started_utc': began,
              'ended_utc': datetime.now(timezone.utc).isoformat(), 'protected_packages': protected,
              'canonical_role_projections': canonical_projections, 'json_shapes': SHAPES, 'observations': OBS,
              'unmatched_observations': {k: v for k, v in OBS.items() if not v['matched']},
              'selected_physical_copies': copies, 'actual_native_cmp_commands': CMPS,
              'all_original_inputs_unchanged': True, 'original_input_paths': len(before),
              'new_live_control_pins': {str(k): v for k, v in CONTROLS.items()},
              'target_auditor_lifecycle_guard_executions': 0, 'new_science_build_render_views': 0,
              'scope': 'Static original schemas, byte comparisons, and known fields only; no future artifact acceptance.'}
    dump('INTAKE_INPUTS_BEFORE.json', before); dump('INTAKE_INPUTS_AFTER.json', after)
    dump('SCHEMA_PROJECTIONS.json', result)
    print(json.dumps({'status': 'RECORDED_ORIGINAL_SCHEMAS_NOT_ARTIFACT_GATE', 'input_paths': len(before),
                      'schema_records': len(SHAPES), 'copies': len(copies), 'actual_cmp_calls': len(CMPS),
                      'unmatched': result['unmatched_observations'], 'target_executions': 0}, sort_keys=True))


if __name__ == '__main__':
    main()
