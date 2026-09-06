"""One-shot evidence audit and complete directory-relative nonself seal."""
import hashlib
import json
from pathlib import Path
import subprocess
import sys

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
BASE = Path(__file__).resolve().parent


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_json(path):
    return json.loads(path.read_text())


def command(args, cwd):
    result = subprocess.run(args, cwd=cwd, capture_output=True, text=True)
    receipt = {'command': args, 'cwd': str(cwd), 'exit_code': result.returncode,
               'stdout': result.stdout, 'stderr': result.stderr}
    assert result.returncode == 0, receipt
    return receipt


def audit():
    assert not (BASE / 'AUDIT_RECEIPT.json').exists()
    audits = []
    for directory in (BASE, BASE / 'd2lc_theorem'):
        before = read_json(directory / 'PAIR_INPUTS_BEFORE.json')
        after = read_json(directory / 'PAIR_INPUTS_AFTER.json')
        assert before == after
        assert all(sha(ROOT / p) == value for p, value in before.items())
        pair = read_json(directory / 'PAIR_RECEIPT.json')
        assert pair['success'] and pair['all_live_inputs_unchanged']
        assert pair['live_input_count'] == len(before)
        checks = [command(['/usr/bin/cmp', str(directory / 'execution_01/stdout.json'),
                           str(directory / 'execution_02/stdout.json')], directory),
                  command(['/usr/bin/cmp', str(directory / 'CANONICAL.json'),
                           str(directory / 'execution_01/stdout.json')], directory),
                  command(['/usr/bin/sha256sum', '-c', str(directory / 'HISTORICAL_INPUT_SHA256SUMS')], ROOT)]
        runs = []
        for number in (1, 2):
            run = directory / f'execution_{number:02d}'
            receipt = read_json(run / 'COMMAND_RECEIPT.json')
            assert receipt['exit_code'] == 0 and receipt['unchanged_inputs']
            assert sha(run / 'stdout.json') == receipt['stdout_sha256']
            assert sha(run / 'stderr.txt') == receipt['stderr_sha256']
            assert (run / 'stderr.txt').read_bytes() == b''
            checks.extend([command(['/usr/bin/cmp', str(run / 'INPUTS_BEFORE_SHA256SUMS'),
                                    str(run / 'INPUTS_AFTER_SHA256SUMS')], run),
                           command(['/usr/bin/sha256sum', '-c', 'INPUTS_BEFORE_SHA256SUMS'], run)])
            runtime_before = read_json(run / 'RUNTIME_BEFORE.json')
            runtime_after = read_json(run / 'RUNTIME_AFTER.json')
            assert runtime_before == runtime_after
            assert all(sha(Path(p)) == value for p, value in runtime_before['files'].items())
            assert 'optimize=0' in runtime_before['flags']
            assert 'isolated=1' in runtime_before['flags']
            assert 'dont_write_bytecode=1' in runtime_before['flags']
            runs.append({'run': number, 'pinned_input_files': receipt['input_files'],
                         'pinned_runtime_files': len(runtime_before['files']),
                         'runtime_before_after_and_live_match': True,
                         'runtime_executable': runtime_before['executable'],
                         'runtime_version': runtime_before['version'],
                         'stdout_sha256': receipt['stdout_sha256']})
        result = read_json(directory / 'CANONICAL.json')
        audits.append({'scope': str(directory.relative_to(BASE)) or '.',
                       'live_input_count': len(before), 'runs': runs,
                       'checks': checks, 'summary': {key: result[key] for key in
                       ('literal_maps_executed', 'complete_boxes', 'state_map_pairs', 'assertions')}})
    original = read_json(BASE / 'CANONICAL.json')
    sidecar = read_json(BASE / 'd2lc_theorem/CANONICAL.json')
    assert (original['literal_maps_executed'], original['complete_boxes'], original['state_map_pairs'],
            original['assertions']) == (3, 26, 46819, 276701)
    assert (sidecar['new_literal_maps'], sidecar['new_boxes'], sidecar['state_map_pairs'],
            sidecar['assertions']) == (0, 0, 33867, 581373)
    old_graph = {row['parameters'][0]: row for row in original['rows'] if row['map'] == 'D2LC'}
    for row in sidecar['rows']:
        assert row['integer_arrow_sha256'] == old_graph[row['n']]['integer_arrow_sha256']
        assert row['depth_histogram'] == old_graph[row['n']]['depth_histogram']
    value = {'role': 'AUTHOR_ARTIFACT_AUDIT_NOT_INDEPENDENT_REVIEW', 'success': True,
             'pair_count': 2, 'numerical_process_count': 4, 'scope_audits': audits,
             'no_new_boxes_in_sidecar': True}
    (BASE / 'AUDIT_RECEIPT.json').write_text(json.dumps(value, sort_keys=True, indent=2) + '\n')
    print(json.dumps({'success': True, 'pairs': 2, 'processes': 4,
                      'runtime_file_counts': [r['pinned_runtime_files'] for a in audits for r in a['runs']]}))
    for row in original['rows']:
        print('| ' + ' | '.join(map(str, [row['map'], 'x'.join(map(str, row['parameters'])),
                    row['states'], row['image_size'], row['max_tail'], row['max_period'],
                    row['max_fibre'], row['max_fibre_target_count']])) + ' |')


def seal():
    manifest = BASE / 'SHA256SUMS'
    assert not manifest.exists()
    assert read_json(BASE / 'AUDIT_RECEIPT.json')['success']
    files = sorted(p for p in BASE.rglob('*') if p.is_file() and p != manifest)
    assert not any(p.is_symlink() for p in BASE.rglob('*'))
    manifest.write_text(''.join(f'{sha(p)}  {p.relative_to(BASE)}\n' for p in files))
    check = command(['/usr/bin/sha256sum', '-c', 'SHA256SUMS'], BASE)
    assert len(check['stdout'].splitlines()) == len(files)
    assert sorted(p for p in BASE.rglob('*') if p.is_file() and p != manifest) == files
    print(json.dumps({'success': True, 'manifest': str(manifest), 'file_count': len(files),
                      'manifest_sha256': sha(manifest), 'check_command': check['command'],
                      'check_cwd': check['cwd'], 'check_exit_code': check['exit_code'],
                      'check_stdout_lines': len(check['stdout'].splitlines()),
                      'check_stdout_sha256': hashlib.sha256(check['stdout'].encode()).hexdigest(),
                      'check_stderr': check['stderr']}, sort_keys=True))


if __name__ == '__main__':
    assert sys.flags.optimize == 0
    assert len(sys.argv) == 2 and sys.argv[1] in ('audit', 'seal')
    audit() if sys.argv[1] == 'audit' else seal()
