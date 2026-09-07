"""Close only revision04; preserve exact helper history and native failures."""
from hashlib import sha256
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
EXPECTED = {'scope01': 1, 'inspect01': 0, 'prepare01': 0, 'validate01': 1, 'validate02': 0}


def info(path):
    data = Path(path).read_bytes()
    return {'sha256': sha256(data).hexdigest(), 'bytes': len(data)}


def obj(path):
    return json.loads(Path(path).read_bytes())


def dump(name, value):
    with (HERE / name).open('x') as f:
        json.dump(value, f, indent=2, sort_keys=True)
        f.write('\n')


def main():
    assert HERE.name == 'p209_terminal_artifact_revision_04' and not (HERE / 'SHA256SUMS').exists()
    aliases, roles, current = {}, [], {}
    for label, name, reason in [
        ('scope01', 'documentary.py', 'Original scope checker genuinely found four origin-predicate failures; later inspector explicitly classifies and tests only those four roles.'),
        ('validate01', 'validate_revision.py', 'Static validator corrected its exact manifest-label assertion and uses distinct native output filenames for the retry.')]:
        base = HERE / 'commands' / label
        original, frozen = HERE / name, base / (name + '.at_execution')
        pin = obj(base / 'INPUTS_BEFORE.json')[str(original)]
        assert pin == obj(base / 'INPUTS_AFTER.json')[str(original)] == info(frozen)
        aliases[(str(original), pin['sha256'])] = frozen
        roles.append({'original_path': str(original), 'sha256': pin['sha256'], 'bytes': pin['bytes'], 'physical_path': str(frozen),
                      'actual_command': str(base / 'COMMAND.json'), 'role': 'exact_same_command_executing_helper_snapshot', 'reason': reason})
    receipts, occurrences = [], 0
    for label, exit_code in EXPECTED.items():
        base = HERE / 'commands' / label
        row, attempt = obj(base / 'COMMAND.json'), obj(base / 'ATTEMPT.json')
        before, after = obj(base / 'INPUTS_BEFORE.json'), obj(base / 'INPUTS_AFTER.json')
        assert before == after and len(before) == row['input_count'] and row['inputs_unchanged']
        assert row['exit_code'] == exit_code and row['status'] == 'COMPLETED' and row['failure'] is None
        assert attempt['status'] == 'ATTEMPTED' and attempt['exit_code'] is None
        assert all(attempt[k] == row[k] for k in ('argv', 'cwd', 'environment', 'started_utc', 'scope'))
        for stream in ('stdout', 'stderr'):
            assert info(base / (stream + '.raw')) == row[stream]
        for path, wanted in before.items():
            selected = aliases.get((path, wanted['sha256']), Path(path))
            actual = current.setdefault(str(selected), info(selected))
            assert actual == wanted, (label, path, str(selected))
            occurrences += 1
        receipts.append({'command': label, 'exit_code': exit_code, 'input_count': len(before), 'inputs_unchanged': True,
                         'stdout': row['stdout'], 'stderr': row['stderr']})
    static = obj(HERE / 'STATIC_RESULT.json')
    assert static['status'] == 'PASS_STATIC_PREPARATION_ONLY_NOT_ARTIFACT_GATE'
    for path, wanted in static['original_inputs_after'].items():
        actual = current.setdefault(path, info(path))
        assert actual == wanted
    after = {p: info(p) for p in current}
    assert after == current
    dump('CODE_HISTORY_ROLES.json', roles)
    dump('CLOSURE_CURRENT_INPUTS.json', {'before': current, 'after': after, 'unchanged': True})
    dump('CLOSURE_CHECK.json', {'status': 'PASS_NATIVE_DOCUMENTARY_CLOSURE_NOT_TARGET_GATE', 'commands': receipts,
        'recorded_input_occurrences': occurrences, 'distinct_current_physical_inputs': len(current),
        'current_input_maps': 'CLOSURE_CURRENT_INPUTS.json', 'helper_history_roles': roles,
        'original_paths_rechecked': static['original_input_paths'], 'target_executions': 0,
        'initial05_created': False, 'lifecycle_executions': 0, 'new_science_build_views': 0})
    paths = sorted(p for p in HERE.rglob('*') if p.is_file())
    assert not any(p.is_symlink() for p in HERE.rglob('*'))
    with (HERE / 'SHA256SUMS').open('x') as f:
        for path in paths:
            f.write(info(path)['sha256'] + '  ' + path.relative_to(HERE).as_posix() + '\n')
    print(json.dumps({'complete_nonself_payloads': len(paths), 'manifest_sha256': info(HERE / 'SHA256SUMS')['sha256'],
                      'current_input_paths_rechecked_twice': len(current), 'historical_input_occurrences': occurrences,
                      'target_executions': 0}, sort_keys=True))


if __name__ == '__main__':
    main()
