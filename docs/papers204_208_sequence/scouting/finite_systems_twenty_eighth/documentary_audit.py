#!/usr/bin/env python3
"""Documentary checks only; never executes a finite-system rule or scientific code.

The at-time pins remain immutable. A current byte comparison is explicitly not
an at-time physical snapshot. Known prohibited source paths are not opened again.
"""
import argparse
from collections import Counter, defaultdict
import hashlib
import json
from pathlib import Path
import re
import sys

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
LANE = Path(__file__).resolve().parent
OLD_RECEIPT = 'af1754c9d6095c0f943b75fe7b9819ebd2b7c4db9609930ca7feccf2934786da'
PROTECTED = re.compile(r'/(?:208-|209-|order_geometry_tenth(?:_desk)?/|finite_systems_nineteenth/|p208_|p209_|OFS|FTH)', re.I)


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read(path):
    return json.loads(path.read_text())


def files():
    return sorted(p for p in LANE.rglob('*') if p.is_file())


def check_seal():
    seal = LANE / 'SHA256SUMS'
    rows = {}
    for line in seal.read_text().splitlines():
        digest, name = line.split('  ', 1)
        assert re.fullmatch('[0-9a-f]{64}', digest), name
        assert not Path(name).is_absolute() and '..' not in Path(name).parts, name
        assert name not in rows and name != 'SHA256SUMS', name
        rows[name] = digest
    expected = {str(p.relative_to(LANE)) for p in files() if p != seal}
    assert expected == set(rows), {'missing': sorted(expected-set(rows)), 'extra': sorted(set(rows)-expected)}
    for name, digest in rows.items():
        p = LANE / name
        assert not p.is_symlink() and sha(p) == digest, name
    return {'status': 'PASS_COMPLETE_NONSELF_PAYLOAD_SEAL', 'payload_files': len(rows),
            'sha256sums_sha256': sha(seal), 'sha256sums_bytes': seal.stat().st_size,
            'limitation': 'Byte identity and complete directory coverage only, not proof or gate acceptance.'}


def audit(excluded_command):
    errors = []
    references = defaultdict(list)
    physical = {}
    snapshot_count = snapshot_rows = 0

    def expect(ok, message):
        if not ok:
            errors.append(message)

    def remember(pin, label):
        if pin.get('exists') and 'sha256' in pin:
            references[(pin['path'], pin['sha256'])].append(label)

    for manifest in sorted((LANE / 'history').glob('*/PIN_MANIFEST.json')):
        snapshot_count += 1
        for i, row in enumerate(read(manifest)['files']):
            snapshot_rows += 1
            label = f'{manifest.relative_to(LANE)}:files[{i}]'
            before, after, copied = row['before'], row['after'], row['copy']
            target = LANE / row['physical_copy']
            expect(target.is_file() and not target.is_symlink(), label + ': missing/nonregular copy')
            expect(before['path'] == after['path'], label + ': path changed')
            expect(before['sha256'] == after['sha256'] == copied['sha256'] == sha(target), label + ': byte mismatch')
            expect(before['bytes'] == after['bytes'] == copied['bytes'] == target.stat().st_size, label + ': length mismatch')
            expect(Path(copied['path']) == target, label + ': physical path mismatch')
            physical[(before['path'], before['sha256'])] = row['physical_copy']
            physical[(copied['path'], copied['sha256'])] = row['physical_copy']
            remember(before, label + ':before')
            remember(after, label + ':after')

    # This is the exact historic path/hash alias supported by root's actual
    # recovery receipt, not a generic licence to substitute mutable controls.
    old = LANE / 'history/controls/docs/papers204_208_sequence/qa/central_lifecycle_p209_a/GIT_SYNC_RECEIPT.before.md'
    recovery_path = LANE / 'history/git_recovery/docs/papers204_208_sequence/qa/central_lifecycle_p209_a/GIT_OBJECT_RECOVERY.actual.json'
    recovery = read(recovery_path)
    recovered = json.loads(recovery['result']['output'])
    expect(recovery['result']['exit_code'] == 0 and recovered['git_exit'] == 0 and recovered['raw_comparison']['exit'] == 0, 'historic receipt: original recovery exit')
    expect(recovered['expected_sha256'] == recovered['git_stdout_sha256'] == OLD_RECEIPT == sha(old), 'historic receipt: wrong exact bytes')
    physical[(str(ROOT / 'docs/papers204_208_sequence/GIT_SYNC_RECEIPT.md'), OLD_RECEIPT)] = str(old.relative_to(LANE))

    discovery = []
    all_protected = set()
    for directory in sorted((LANE / 'discovery').iterdir()):
        scope = read(directory / 'scope.json')
        argv = read(directory / 'ARGV.json')
        result = read(directory / 'RESULT.json')
        before, after = read(directory / 'PINS_BEFORE.json'), read(directory / 'PINS_AFTER.json')
        filename_command = read(directory / 'filenames.command.json')
        filename_list = (directory / 'filenames.stdout.txt').read_text().splitlines()
        flags = re.I if scope.get('case_insensitive', False) else 0
        excluded = re.compile(scope['regex_exclusions'], flags)
        expected_files = sorted(p for p in filename_list if not excluded.search('/'+p))
        expect(scope['files'] == expected_files, directory.name + ': enumeration/scope mismatch')
        expect(argv[:4] == ['rg', '-n', '-i', '--'] and argv[5:] == scope['files'], directory.name + ': exact search argv mismatch')
        expect(filename_command['cwd'] == str(ROOT) and filename_command['exit_code'] == 0, directory.name + ': filename command failed')
        expected_paths = [str(ROOT / p) for p in scope['files']]
        expect([p['path'] for p in before] == expected_paths == [p['path'] for p in after], directory.name + ': pin coverage mismatch')
        pin_changes = [i for i, pair in enumerate(zip(before, after)) if pair[0] != pair[1]]
        expect(not pin_changes, directory.name + ': at-time source changes')
        stdout = (directory / 'stdout.txt').read_bytes()
        stderr = (directory / 'stderr.txt').read_bytes()
        expect(result['stdout_bytes'] == len(stdout) and result['stderr_bytes'] == len(stderr), directory.name + ': raw stream lengths')
        expect(result['exit_code'] in (0, 1), directory.name + ': content command failed')
        for phase, pins in [('before', before), ('after', after)]:
            for pin in pins:
                remember(pin, f'discovery/{directory.name}/{phase}')
        protected = [p for p in scope['files'] if PROTECTED.search('/'+p)]
        all_protected.update(protected)
        hit_lines = stdout.decode().splitlines()
        protected_hits = [line for line in hit_lines if PROTECTED.search('/'+line.split(':', 1)[0])]
        if directory.name == 'corrected_final':
            expect(not protected, 'corrected_final: known prohibited scope not absent')
        else:
            expect(bool(protected), directory.name + ': original scope failure unexpectedly vanished')
        discovery.append({'name': directory.name, 'case_insensitive_exclusions': bool(flags),
                          'searched_files': len(scope['files']), 'hit_lines': len(hit_lines),
                          'exit_code': result['exit_code'], 'stderr_bytes': len(stderr),
                          'before_after_identical': not pin_changes,
                          'protected_files_in_original_scope': protected,
                          'protected_hit_lines_count': len(protected_hits),
                          'pattern': argv[4]})

    commands = []
    command_pin_changes = []
    for directory in sorted((LANE / 'commands').iterdir()):
        if directory.name == excluded_command:
            continue
        invocation = read(directory / 'invocation.json')
        result = read(directory / 'result.json')
        for key in ('argv', 'cwd', 'utc_before', 'pins_before', 'capture_runtime'):
            expect(invocation[key] == result[key], str(directory.relative_to(LANE)) + ': changed invocation ' + key)
        expect(result['cwd'] == str(ROOT), directory.name + ': cwd mismatch')
        expect(isinstance(result['argv'], list) and bool(result['argv']), directory.name + ': no argv')
        for stream in ('stdout', 'stderr'):
            expect(sha(directory / (stream+'.txt')) == result[stream+'_sha256'], directory.name + ': '+stream+' changed')
        if result['pins_before'] != result['pins_after']:
            command_pin_changes.append(directory.name)
        for phase in ('before', 'after'):
            for pin in result['pins_'+phase]:
                remember(pin, f'commands/{directory.name}/{phase}')
        commands.append({'name': directory.name, 'exit_code': result['exit_code'],
                         'explicit_pin_count': len(result['pins_before']),
                         'nonhermetic': result['capture_runtime']['nonhermetic']})
    expect(not command_pin_changes, 'captured explicit command pins changed: '+repr(command_pin_changes))

    # Current resolution is a separate later observation. Do not reopen known
    # prohibited scientific inputs merely to make this documentary audit green.
    resolutions = Counter()
    unavailable, skipped, live = [], [], {}
    for (name, expected), labels in sorted(references.items()):
        if (name, expected) in physical:
            resolutions['exact_physical_copy'] += 1
            continue
        if PROTECTED.search(name):
            skipped.append({'path': name, 'expected_sha256': expected, 'recorded_in': labels})
            resolutions['protected_not_reopened'] += 1
            continue
        p = Path(name)
        if name not in live:
            live[name] = sha(p) if p.is_file() else None
        if live[name] == expected:
            resolutions['later_current_byte_match_not_snapshot'] += 1
        else:
            resolutions['historical_bytes_unresolved'] += 1
            unavailable.append({'path': name, 'expected_sha256': expected,
                                'current_sha256': live[name], 'recorded_in': labels})

    partial = LANE / 'history/nearby_originals'
    expect(partial.is_dir() and not (partial/'PIN_MANIFEST.json').exists(), 'original partial snapshot not preserved')
    expect((LANE/'FAILED_SNAPSHOT_01.md').is_file(), 'original failed snapshot record missing')
    preflight = read(LANE/'sources/konyagin.preflight.json')
    expect(preflight['verdict'] == 'UNAVAILABLE' and 'pypdf-not-installed' in ' '.join(preflight['warnings']), 'actual PDF preflight limitation changed')
    return {'status': 'PASS_DOCUMENTARY_STRUCTURE_WITH_EXPLICIT_LIMITATIONS' if not errors else 'FAIL_DOCUMENTARY_STRUCTURE',
            'errors': errors, 'snapshot_manifests': snapshot_count, 'physical_snapshot_rows': snapshot_rows,
            'discoveries': discovery, 'discovery_scope_failure_unique_files': len(all_protected),
            'commands': commands, 'completed_commands_checked': len(commands),
            'currently_open_command_excluded': excluded_command,
            'explicit_command_pin_changes': command_pin_changes,
            'unique_path_hash_references': len(references), 'later_resolution_counts': dict(resolutions),
            'unresolved_historical_bytes': unavailable, 'protected_inputs_not_reopened': skipped,
            'exact_old_receipt_sha256': OLD_RECEIPT,
            'actual_pdf_preflight_verdict': preflight['verdict'],
            'scientific_literals': 1, 'scientific_pilots': 0, 'scientific_producer_runs': 0,
            'limitations': ['Original three searches crossed a known P208 author-source boundary; reviewer eligibility not established.',
                           'At-time hash equality is not a physical at-time snapshot or hermeticity proof.',
                           'Unresolved historic references, if any, are retained rather than refreshed.',
                           'The active capture command cannot check its own future result; the final payload seal covers it.',
                           'This audit does not verify mathematical truth, source ownership, novelty, visual integrity or any research gate.']}


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument('--audit', action='store_true')
    mode.add_argument('--write-seal', action='store_true')
    mode.add_argument('--verify-seal', action='store_true')
    parser.add_argument('--exclude-command', default='')
    args = parser.parse_args()
    if args.audit:
        result = audit(args.exclude_command)
        print(json.dumps(result, indent=2))
        sys.exit(bool(result['errors']))
    elif args.write_seal:
        seal = LANE/'SHA256SUMS'
        assert not seal.exists(), 'Do not overwrite an existing seal.'
        payload = files()
        assert all(not p.is_symlink() for p in payload), 'Symlink payload is not a physical copy.'
        seal.write_text(''.join(f'{sha(p)}  {p.relative_to(LANE)}\n' for p in payload))
        print(json.dumps(check_seal(), indent=2))
    else:
        print(json.dumps(check_seal(), indent=2))
