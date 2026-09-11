#!/usr/bin/env python3
"""Root original-byte inspection of the actual MNA pair; no science executes.

Fresh children compare three existing raw outputs only. Full consumed-path
ledgers are written exclusively here; the pair and old gate remain untouched.
"""
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
HERE = ROOT / 'docs/papers204_208_sequence/qa/mna_root_pair_execution'
PAIR = ROOT / 'docs/papers204_208_sequence/qa/root_replays/mna_gate_pair_01'
PREP = ROOT / 'docs/papers204_208_sequence/qa/mna_root_pair_preparation'
GATE = ROOT / 'docs/papers204_208_sequence/scouting/MNA_GATE'
ENV = {'PATH': '/usr/bin:/bin', 'LANG': 'C.UTF-8', 'LC_ALL': 'C.UTF-8', 'TZ': 'UTC'}
PINS, CMPS, CHECKS = {}, [], 0

def check(ok, detail):
    global CHECKS
    CHECKS += 1
    if not ok:
        raise AssertionError(detail)

def metadata(raw):
    return {'sha256': hashlib.sha256(raw).hexdigest(), 'bytes': len(raw)}

def raw(path):
    path = Path(path)
    check(path.is_absolute() and '..' not in path.parts and not str(path).startswith('/proc/'), ('safe_read', str(path)))
    body = path.read_bytes()
    record = metadata(body)
    check(str(path) not in PINS or PINS[str(path)] == record, ('read_drift', str(path)))
    PINS[str(path)] = record
    return body

def read(path):
    return json.loads(raw(path))

def pin(path, expected):
    got = metadata(raw(path))
    check(got == expected, ('full_pin', str(path), expected, got))

def seal(base, expected, count):
    body = raw(base / 'SHA256SUMS')
    check(metadata(body)['sha256'] == expected, ('assigned_seal', str(base)))
    names = {}
    for line in body.decode().splitlines():
        match = re.fullmatch(r'([0-9a-f]{64})  (.+)', line)
        check(match is not None, 'seal_syntax')
        sha, name = match.groups()
        check(not Path(name).is_absolute() and '..' not in Path(name).parts and name not in names and name != 'SHA256SUMS', ('nonself_name', name))
        names[name] = sha
        check(metadata(raw(base / name))['sha256'] == sha, ('sealed_payload', name))
    physical = set()
    for path in base.rglob('*'):
        check(not path.is_symlink(), ('package_symlink', str(path)))
        if path.is_file():
            physical.add(path.relative_to(base).as_posix())
    check(len(names) == count and physical == set(names) | {'SHA256SUMS'}, ('complete_nonself', str(base)))

def capture(folder):
    a, r = read(folder / 'ATTEMPT.json'), read(folder / 'RECEIPT.json')
    check({p.name for p in folder.iterdir()} == {'ATTEMPT.json', 'RECEIPT.json', 'stdout.raw', 'stderr.raw'}, 'native_physical_four')
    for key in ('argv', 'cwd', 'environment', 'started_utc', 'timeout_seconds'):
        check(a[key] == r[key], ('attempt_receipt_field', str(folder), key))
    check(r['cwd'] == str(ROOT) and r['environment'] == ENV and r['started_utc'] <= r['ended_utc'], 'native_context_time')
    check(r['exit_code'] == r['wrapper_exit_code'] == 0 and r['spawned'] and r['streams_complete'] and not r['timed_out'] and r['failure'] is None, ('native_success', str(folder)))
    for name in ('stdout', 'stderr'):
        pin(folder / (name + '.raw'), r[name])
    check(raw(folder / 'stderr.raw') == b'', 'empty_native_stderr')
    return r

def sample(obj, known, cache):
    check(obj['environment'] == ENV and obj['executable'] == '/usr/bin/python3.10' and obj['cwd'] == str(ROOT), 'sample_runtime_context')
    check(obj['sys_path'] == ['/usr/lib/python310.zip', '/usr/lib/python3.10', '/usr/lib/python3.10/lib-dynload'] and obj['pycache_prefix'] == str(cache) and not obj['cache_lexists'] and not os.path.lexists(cache), 'sample_cold_import_context')
    check(all(s in obj['flags'] for s in ('optimize=0', 'isolated=1', 'no_site=1', 'dont_write_bytecode=1')), 'sample_cold_flags')
    check(metadata(obj['proc_maps'].encode()) == {'sha256': obj['proc_maps_sha256'], 'bytes': obj['proc_maps_bytes']}, 'full_recorded_volatile_maps')
    mapped = set()
    for line in obj['proc_maps'].splitlines():
        fields = line.split(None, 5)
        if len(fields) == 6 and fields[5].startswith('/'):
            check(not fields[5].endswith(' (deleted)'), 'no_deleted_map')
            mapped.add(str(Path(fields[5]).resolve(strict=True)))
    check(mapped == set(obj['mapped_files']), 'complete_map_path_reconstruction')
    files = list(obj['mapped_files'].items()) + [(v['path'], {k: v[k] for k in ('sha256', 'bytes')}) for v in obj['modules'].values()]
    for path, record in files:
        check(path in known and {k: known[path][k] for k in ('sha256', 'bytes')} == record and Path(path).suffix not in ('.pyc', '.pyo'), ('observed_known_input', path))
        pin(path, record)

def main():
    check(sys.flags.isolated == sys.flags.no_site == sys.flags.dont_write_bytecode == 1 and sys.flags.optimize == 0, 'inspector_flags')
    raw(Path(__file__).resolve())
    seal(PAIR, '3a5e964b14738093160c2f52910dc682f4ea76f81ad1bcc782383bb166c5fdc0', 56)
    seal(PREP, '3fce5fb3ce11f27f03d55828acb4522f69e03e55cafd4b2d02ac924b17f1bbf2', 4)
    seal(GATE, '5e15111b5dc6b4a585126e32fc59752b10cba8605f846d225e9efa26c656dc34', 309)
    for mode in ('preflight', 'run'):
        receipt = capture(HERE / (mode + '_01'))
        check(receipt['inputs_before'] == receipt['inputs_after'] and receipt['inputs_unchanged'], 'parent_inputs')
        for name, wanted in receipt['inputs_before'].items():
            pin(name, wanted)
        check(receipt['argv'][-7] == mode, ('parent_exact_mode', mode))
    result = read(PAIR / 'RESULT.json')
    summary = read(HERE / 'run_01/stdout.raw')
    check(result['status'] == summary['status'] == 'PASS_ROOT_MNA_SOURCE_ONLY_PAIR' and result['errors'] == summary['errors'] == [], 'actual_parent_child_pass')
    check(summary['closure'] == {'payloads': 56, 'manifest': metadata(raw(PAIR / 'SHA256SUMS'))}, 'parent_full_seal_identity')
    known = read(PAIR / 'INPUTS_BEFORE.json')
    check(len(known) == summary['known_inputs'] == result['known_input_count'] == 4237 and known == read(PAIR / 'INPUTS_AFTER.json'), '4237_exact_before_after')
    check(raw(PAIR / 'INPUTS_BEFORE.json') == raw(PAIR / 'INPUTS_AFTER.json'), 'raw_known_ledger_identity')
    for name, record in known.items():
        pin(name, {k: record[k] for k in ('sha256', 'bytes')})
        check(str(Path(name).resolve(strict=True)) == record['resolved'] and (os.readlink(name) if Path(name).is_symlink() else None) == record['symlink'], ('known_resolution', name))
    old = read(PAIR / 'ORIGINAL_997_BEFORE.json')
    check(len(old) == 997 and old == read(PAIR / 'ORIGINAL_997_AFTER.json') == read(GATE / 'evidence/pair03/inputs_before.json') == read(GATE / 'evidence/pair03/inputs_after.json'), 'original_997_exact_preservation')
    for name, record in old.items():
        check(name in known and {k: known[name][k] for k in ('sha256', 'bytes')} == record, 'all_original_keys_in_new_capsule')
    for stem in ('RESOURCE_NAMES', 'CONFIGURATION'):
        check(raw(PAIR / (stem + '_BEFORE.json')) == raw(PAIR / (stem + '_AFTER.json')), ('raw_dependency_configuration_membership', stem))
    closure = read(PAIR / 'GATE_AND_PREPARATION_CLOSURE.json')
    check(closure['before'] == closure['after'] and closure['original_input_count'] == 997, 'full_gate_preparation_closure')
    for name in ('run_pair.py', 'verify.py'):
        origin = (PREP if name == 'run_pair.py' else GATE) / name
        check(raw(origin) == raw(PAIR / 'sources' / name), ('source_only_raw', name))
    labels = ['00_cmp_runner_source', '01_cmp_verifier_source', '02_ldd_before', '03_verify_01', '03_verify_02', '04_cmp_canonical_01', '04_cmp_canonical_02', '05_cmp_pair', '06_ldd_after']
    check(sorted(p.name for p in (PAIR / 'commands').iterdir()) == labels and [r['label'] for r in result['commands']] == labels, 'nine_actual_command_census')
    receipts = {}
    for row in result['commands']:
        receipt = capture(PAIR / 'commands' / row['label'])
        check(receipt == {k: v for k, v in row.items() if k != 'label'}, 'full_inner_receipt_identity')
        receipts[row['label']] = receipt
    canonical = raw(GATE / 'CANONICAL.json')
    for number in ('01', '02'):
        cache = PAIR / ('unused_child_' + number + '_cache')
        obj = read(PAIR / ('observations/child_' + number + '.json'))
        check(obj['status'] == 'RETURNED' and obj['source'] == {'path': str(PAIR / 'sources/verify.py'), **metadata(raw(GATE / 'verify.py'))}, 'executed_copied_verifier')
        check(receipts['03_verify_' + number]['argv'] == ['/usr/bin/python3.10', '-I', '-S', '-B', '-X', 'pycache_prefix=' + str(cache), str(PAIR / 'sources/run_pair.py'), 'child', number], 'actual_exact_child_argv')
        for phase in ('before', 'after'):
            sample(obj[phase], known, cache)
        paths = {str((Path(row['path']) if Path(row['path']).is_absolute() else ROOT / row['path']).resolve()) for row in obj['python_open_events']}
        check(paths == set(obj['opened_ordinary_files']) and not obj['nonfile_open_paths_at_end'] and not obj['volatile_open_paths'], 'actual_complete_open_event_file_set_no_absent_or_volatile_probes')
        for name, record in obj['opened_ordinary_files'].items():
            check(name in known and {k: known[name][k] for k in ('sha256', 'bytes')} == record, 'python_open_in_before_capsule')
            pin(name, record)
        output = raw(PAIR / ('commands/03_verify_' + number + '/stdout.raw'))
        check(output == canonical, 'full_output_raw_identity')
        data = json.loads(output)
        check(data['status'] == 'PASS' and data['N_min'] == 1 and data['N_max'] == 12 and data['state_count'] == 4095 and data['check_count'] == sum(data['checks'].values()) == 115680, 'complete_recorded_fixed_box_census')
    for phase in ('before', 'after'):
        sample(read(PAIR / ('observations/parent_' + phase + '.json')), known, PAIR / 'unused_parent_cache')
    linked = read(PAIR / 'LINKED_RUNTIME.json')
    for phase in ('before', 'after'):
        output = raw(PAIR / ('commands/' + ('02' if phase == 'before' else '06') + '_ldd_' + phase + '/stdout.raw'))
        paths = sorted({str(Path(os.fsdecode(x)).resolve()) for x in re.findall(rb'(/[^\s()]+)', output) if Path(os.fsdecode(x)).is_file()})
        check(paths == linked[phase] and b'not found' not in output and all(p in known for p in paths), 'full_ldd_output_reconstruction')
    check(linked['before'] == linked['after'], 'ldd_membership_stable')
    first, second = [PAIR / ('commands/03_verify_' + n + '/stdout.raw') for n in ('01', '02')]
    for left, right in [(first, GATE / 'CANONICAL.json'), (second, GATE / 'CANONICAL.json'), (first, second)]:
        argv = ['/usr/bin/cmp', '--', str(left), str(right)]
        p = subprocess.run(argv, cwd=ROOT, env=ENV, capture_output=True, timeout=30, check=False)
        CMPS.append({'argv': argv, 'exit_code': p.returncode, 'stdout_utf8': p.stdout.decode(), 'stderr_utf8': p.stderr.decode()})
        check(p.returncode == 0 and p.stdout == p.stderr == b'', 'fresh_raw_comparison')
    before = dict(sorted(PINS.items()))
    after = {name: metadata(Path(name).read_bytes()) for name in before}
    check(before == after, 'all_consumed_paths_rechecked_unchanged')
    ledger = {'before': before, 'after': after}
    target = HERE / 'PAIR_ROOT_READS.json'
    with target.open('x') as stream:
        stream.write(json.dumps(ledger, sort_keys=True, indent=2) + '\n')
    report = {'status': 'PASS_ROOT_ACTUAL_PAIR_ORIGINAL_INSPECTION', 'checks': CHECKS,
        'pair_payloads': 56, 'preparation_payloads': 4, 'gate_payloads': 309, 'known_inputs': 4237,
        'original_preserved_inputs': 997, 'actual_commands': 9, 'checks_each': 115680, 'states_each': 4095,
        'full_consumed_paths_checked_twice': len(before), 'read_ledger': metadata(target.read_bytes()),
        'fresh_raw_comparisons': CMPS, 'limits': ['No new scientific execution; actual root pair originals and raw outputs checked.', 'No OS/startup/continuous tracing or independent theorem review.', 'No admission, manuscript review, central or Git edit.']}
    with (HERE / 'PAIR_ROOT_INSPECTION.json').open('x') as stream:
        stream.write(json.dumps(report, sort_keys=True, indent=2) + '\n')
    print(json.dumps(report, sort_keys=True, indent=2))

if __name__ == '__main__':
    main()
