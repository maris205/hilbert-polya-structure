"""Preparation-only JSON schema/projection intake, never executes target code.

This reads original recorded data, records its shapes and selected equality
relationships, and protects old packages. It does not import, compile, invoke,
or recreate the artifact auditor. Its observations are not a gate result.
"""
from collections import Counter
from datetime import datetime, timezone
from hashlib import sha256
import json
from pathlib import Path
import re
import subprocess

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
BATCH = ROOT / 'docs/papers204_208_sequence'
HERE = Path(__file__).resolve().parent
PAPER = ROOT / 'papers/209-ordered-fibre-threading'
FINAL = PAPER / 'qa_final'
OLD = BATCH / 'qa/p209_terminal_artifact_revision_01'
ENV = {'PATH': '/usr/bin:/bin', 'LANG': 'C.UTF-8', 'LC_ALL': 'C.UTF-8', 'TZ': 'UTC'}
PINS, SCHEMAS, OBSERVATIONS = {}, {}, {}


def raw(path):
    path = Path(path)
    data = path.read_bytes()
    value = {'sha256': sha256(data).hexdigest(), 'bytes': len(data)}
    assert str(path) not in PINS or PINS[str(path)] == value
    PINS[str(path)] = value
    return data


def obj(path):
    data = json.loads(raw(path))
    SCHEMAS[str(path)] = shape(data)
    return data


def shape(data):
    if isinstance(data, dict):
        if len(data) > 100 or (data and all(str(k).startswith('/') for k in data)):
            return {'kind': 'mapping', 'rows': len(data), 'value_fieldsets': fields(data.values())}
        return {k: shape(v) for k, v in data.items() if k != 'maps'}
    if isinstance(data, list):
        return {'kind': 'list', 'rows': len(data), 'value_fieldsets': fields(data),
                'scalar_values': data if len(data) <= 12 and all(not isinstance(v, (dict, list)) for v in data) else None}
    return data


def fields(rows):
    counts = Counter(tuple(sorted(v)) if isinstance(v, dict) else (type(v).__name__,) for v in rows)
    return [{'fields': list(k), 'rows': v} for k, v in sorted(counts.items())]


def pair(base, first, second):
    a, b = obj(base / first), obj(base / second)
    OBSERVATIONS[str(base / first) + ' == ' + second] = {'equal': a == b, 'rows': len(a)}
    return a


def protected_packages():
    packages = [
        ('p209_terminal_artifact_preparation', 347, '3250ea718e5b0f358a8a54ba2365a53732d637a2f9686c017e1767e4cdcc7e51'),
        ('p209_terminal_artifact_revision_01', 418, '855aba017f5a369c09696272579897324bbd906892b353d17f0c9eb6d7fcbcc5'),
        ('p209_terminal_artifact/initial_01', 8, 'deb48a3ed612ad9e292436e2037a879df37a0a5e2204594702f436c73bbe4b04'),
        ('p209_terminal_artifact/initial_02', 8, '89ab791251744f3aa96911f871f108268c2ebb7e5e1da55329eea45eb70bbc96')]
    result = {}
    for name, count, digest in packages:
        base = BATCH / 'qa' / name
        seal = raw(base / 'SHA256SUMS')
        assert sha256(seal).hexdigest() == digest
        rows = {}
        for line in seal.decode().splitlines():
            match = re.fullmatch(r'([0-9a-f]{64})  (.+)', line)
            assert match
            want, rel = match.groups()
            assert rel not in rows and not Path(rel).is_absolute() and '..' not in Path(rel).parts
            rows[rel] = want
        actual = {p.relative_to(base).as_posix() for p in base.rglob('*') if p.is_file()}
        assert len(rows) == count and set(rows) == actual - {'SHA256SUMS'}
        assert all(not p.is_symlink() for p in base.rglob('*'))
        for rel, want in rows.items():
            assert sha256(raw(base / rel)).hexdigest() == want
        result[name] = {'payloads': len(rows), 'sha256': digest, 'complete_nonself': True}
    return result


def commands(base, filename):
    entries = obj(base / filename)
    comparisons = []
    for entry in entries:
        folder, tag, row = Path(entry['folder']), entry['tag'], entry['command']
        recorded = obj(folder / (tag + '.command.json'))
        attempt = obj(folder / (tag + '.attempt.json'))
        samples = obj(folder / (tag + '.maps.json'))
        comparisons.append({'tag': tag, 'embedded_equal': row == recorded,
            'attempt_shared_fields_equal': all(attempt[k] == row[k] for k in ('argv', 'cwd', 'env', 'stdout', 'stderr')),
            'exit': row['exit'], 'outcome': row['process_outcome'], 'spawn_error': row['spawn_error'],
            'cleanup': row['cleanup'], 'env': row['env'],
            'map_union_equal': sorted({p for s in samples['samples'] for p in s['mapped_files']}) == entry['mapped_files']})
    OBSERVATIONS[str(base / filename)] = comparisons


def main():
    began = datetime.now(timezone.utc).isoformat()
    assert HERE == BATCH / 'qa/p209_terminal_artifact_revision_02'
    assert not (HERE / 'SCHEMA_PROJECTIONS.json').exists()
    protected = protected_packages()
    selected = [OLD / n for n in ('audit_p209.py', 'record_audit.py', 'lifecycle_audit.py')]
    failed = BATCH / 'qa/p209_terminal_artifact/initial_02'
    selected += sorted(p for p in failed.rglob('*') if p.is_file())
    selected += [BATCH / 'qa/P209_TERMINAL_ARTIFACT_INITIAL_02.failed.actual.json']
    for letter in ('a', 'b'):
        base = BATCH / ('reviews/p209_' + letter)
        selected += [base / n for n in ('FINDINGS.json', 'CURRENT_FINDINGS.json')]
        selected.append(BATCH / ('qa/P209_' + letter.upper() + '_ROOT_DELTA_INSPECTION.actual.json'))
        for path in selected[-3:]: obj(path)
    for source in selected: raw(source)
    copies, comparisons = [], []
    for source in selected:
        target = HERE / 'original_snapshot' / source.relative_to(ROOT)
        target.parent.mkdir(parents=True, exist_ok=True)
        with target.open('xb') as stream: stream.write(raw(source))
        argv = ['/usr/bin/cmp', '--', str(source), str(target)]
        run = subprocess.run(argv, cwd=ROOT, env=ENV, capture_output=True, check=False)
        comparisons.append({'argv': argv, 'cwd': str(ROOT), 'env': ENV, 'exit_code': run.returncode,
                            'stdout': run.stdout.decode(), 'stderr': run.stderr.decode()})
        assert run.returncode == 0 and run.stdout == run.stderr == b''
        copies.append({'original': str(source), 'copy': str(target), **PINS[str(source)]})
    a, b = [BATCH / ('reviews/p209_' + letter) for letter in ('a', 'b')]
    pair(a / 'delta_check_02', 'INPUTS_BEFORE.json', 'INPUTS_AFTER.json')
    pair(b / 'delta_check_02', 'INPUTS_FULL_BEFORE.json', 'INPUTS_FULL_AFTER.json')
    obj(a / 'initial_audit_01/CURRENT_INPUT_CLOSURE.json')
    pair(b / 'artifact_audit_03', 'DOCUMENTARY_INPUTS_BEFORE.json', 'DOCUMENTARY_INPUTS_AFTER.json')
    for base, rel in [(a, 'delta_check_01/EXECUTION.actual.json'), (b, 'delta_check_01/CLOSURE_AFTER_FAILURE.json'),
                      (b, 'delta_check_02/DELTA_EVIDENCE_RESULT.json'), (b, 'delta_check_02/RECEIPT.json')]: obj(base / rel)
    commands(b / 'delta_check_02', 'WRAPPER_COMMAND_RECORDS.json')
    commands(b / 'delta_check_02', 'ALL_COMMAND_RECORDS.json')
    pair(b / 'delta_check_02', 'INPUTS_BEFORE.json', 'INPUTS_AFTER.json')
    for role in ('author', 'a', 'b'):
        rr = BATCH / ('qa/root_replays/p209_' + role + '_strict/root_' + role + '_pair_01')
        launcher = rr.parent / ('launcher_root_' + role + '_pair_01')
        for name in ('RECEIPT.json', 'PARENT_BEFORE.json', 'PARENT_AFTER.json', 'LINKAGE.json', 'OBSERVED_CLOSURE.json'): obj(rr / name)
        inputs = pair(rr, 'ALL_INPUTS_INCLUDING_CAPSULES_BEFORE.json', 'ALL_INPUTS_AFTER.json')
        runtime = pair(rr, 'RUNTIME_BEFORE.json', 'RUNTIME_AFTER.json')
        pair(rr, 'CONFIGURATION_BEFORE.json', 'CONFIGURATION_AFTER.json')
        OBSERVATIONS[role + '_runtime_entire_values_in_inputs'] = all(inputs.get(k) == v for k, v in runtime.items())
        commands(rr, 'ALL_COMMAND_RECORDS.json')
        for child in ('replay_01', 'replay_02'):
            for name in ('RECEIPT.json', 'child.before.json', 'child.after.json'): obj(rr / child / name)
            pair(rr / child, 'INPUTS_BEFORE.json', 'INPUTS_AFTER.json')
            base = PAPER if role == 'author' else BATCH / ('reviews/p209_' + role)
            OBSERVATIONS[role + '_' + child + '_full_raw_canonical_equal'] = raw(rr / child / 'producer.stdout') == raw(base / 'CANONICAL.json')
        obj(launcher / 'RECEIPT.json'); obj(launcher / 'recorder.stdout')
        pair(launcher, 'INPUTS_BEFORE.json', 'INPUTS_AFTER.json')
    reconciliation = obj(b / 'auxiliary_01/reconcile.stdout')
    OBSERVATIONS['reconciliation_recorded_row_statuses'] = dict(Counter(row['status'] for row in reconciliation['rows']))
    commands(b / 'auxiliary_01', 'ALL_COMMAND_RECORDS.json')
    pair(b / 'auxiliary_01', 'INPUTS_BEFORE.json', 'INPUTS_AFTER.json')
    inventory = {}
    for stem in ('INPUTS', 'RUNTIME', 'TEX_INVENTORY', 'CONFIGURATION', 'LIBRARIES', 'CONSUMED_TEX', 'RECORDER_INPUTS'):
        inventory[stem] = pair(FINAL, stem + '_BEFORE.json', stem + '_AFTER.json')
    for name in ('RECORDER_RUNTIME_BEFORE.json', 'RECORDER_RUNTIME_AFTER.json', 'GENERATED_LOCAL_TEX_INPUTS.json', 'USER_ROOTS_AFTER.json'): obj(FINAL / name)
    build = obj(FINAL / 'BUILD_EXECUTION.json')
    terminal_rows = []
    for row in build['commands']:
        command = obj(FINAL / (row['label'] + '.command.json'))
        attempt = obj(FINAL / (row['label'] + '.attempt.json'))
        terminal_rows.append({'label': row['label'], 'embedded_equal': row == command,
            'attempt_fields_equal': all(row[k] == attempt[k] for k in ('argv', 'cwd', 'environment', 'started_utc')),
            'exit_code': row['exit_code'], 'status': row['status'], 'stderr_bytes': row['stderr']['bytes'],
            'cwd': row['cwd'], 'environment': row['environment']})
    OBSERVATIONS['terminal_commands'] = terminal_rows
    covered = dict(inventory['INPUTS'])
    for key in ('RUNTIME', 'LIBRARIES', 'RECORDER_INPUTS'): covered.update(inventory[key])
    covered.update({v['resolved']: {k: v[k] for k in ('sha256', 'bytes')} for v in inventory['CONFIGURATION'].values() if v['is_file']})
    for phase in ('BEFORE', 'AFTER'):
        obs = obj(FINAL / ('RECORDER_RUNTIME_' + phase + '.json'))
        OBSERVATIONS['terminal_parent_' + phase + '_maps_equal'] = all(covered.get(k) == v for k, v in obs['mapped_files'].items())
        OBSERVATIONS['terminal_parent_' + phase + '_modules_equal'] = all(covered.get(v['path']) == {k: v[k] for k in ('sha256', 'bytes')} for v in obs['modules'].values())
    for number in (1, 2):
        for suffix in ('SOURCE_ONLY_INITIAL', 'USER_ROOTS_BEFORE', 'MEASURED_PDF', 'DIAGNOSTICS'):
            obj(FINAL / ('cold_build_' + str(number) + '_' + suffix + '.json'))
        for passno in (1, 2, 3):
            obj(FINAL / ('cold_build_' + str(number) + '_pass' + str(passno) + '_TEX_INPUTS.json'))
    launcher = BATCH / 'qa/root_replays/p209_terminal_strict/launcher_terminal_pair_01'
    obj(launcher / 'RECEIPT.json')
    stdout = obj(launcher / 'recorder.stdout')
    OBSERVATIONS['terminal_outer_stdout_all_fields_equal'] = all(build.get(k) == v for k, v in stdout.items())
    outer_inputs = pair(launcher, 'INPUTS_BEFORE.json', 'INPUTS_AFTER.json')
    outer = {v['resolved']: {k: v[k] for k in ('sha256', 'bytes', 'resolved')} for v in outer_inputs.values()}
    for phase in ('BEFORE', 'AFTER'):
        obs = obj(launcher / ('LAUNCHER_RUNTIME_' + phase + '.json'))
        OBSERVATIONS['terminal_launcher_' + phase + '_maps_equal'] = all(outer.get(k) == v for k, v in obs['mapped_files'].items())
        OBSERVATIONS['terminal_launcher_' + phase + '_modules_equal'] = all(outer.get(v['path']) == {k: v[k] for k in ('sha256', 'bytes', 'resolved')} for v in obs['modules'].values())
    obj(BATCH / 'qa/P209_TERMINAL_ROOT_VIEWS.actual.json')
    for number in (0, 1, 2):
        obj(PAPER / ('frozen_round' + str(number)) / ('FROZEN_LINK_MAP.json' if number == 0 else 'ROUND' + str(number) + '_PROVENANCE.json'))
    obj(a / 'delta_check_02/RESPONSE_ORIGINALS_AND_COPIES.json')
    obj(b / 'assignment_context/ROLES.json'); obj(b / 'delta_intake_01/INTAKE_RESULT.json')
    after = {str(path): {'sha256': sha256(Path(path).read_bytes()).hexdigest(), 'bytes': Path(path).stat().st_size} for path in PINS}
    assert after == PINS
    result = {'scope': __doc__, 'started_utc': began, 'ended_utc': datetime.now(timezone.utc).isoformat(),
              'protected_packages_before': protected, 'all_inputs_unchanged': True,
              'source_data_records': len(SCHEMAS), 'physical_copies': copies,
              'actual_cmp_commands': comparisons, 'json_shapes': SCHEMAS, 'observations': OBSERVATIONS,
              'target_auditor_lifecycle_guard_executions': 0, 'new_science_build_render_views': 0}
    for name, data in [('SCHEMA_INPUTS_BEFORE.json', PINS), ('SCHEMA_INPUTS_AFTER.json', after), ('SCHEMA_PROJECTIONS.json', result)]:
        with (HERE / name).open('x') as stream: json.dump(data, stream, indent=2, sort_keys=True); stream.write('\n')
    print(json.dumps({'status': 'RECORDED_STATIC_SCHEMA_PROJECTIONS_NOT_ARTIFACT_GATE', 'input_paths': len(PINS),
                      'schema_records': len(SCHEMAS), 'copies': len(copies), 'all_inputs_unchanged': True}, sort_keys=True))


if __name__ == '__main__': main()
