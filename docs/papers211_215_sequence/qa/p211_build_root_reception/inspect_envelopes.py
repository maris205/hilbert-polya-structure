#!/usr/bin/python3.10
"""Full saved envelope/result/runtime binding, no submitted execution."""
import hashlib
import json
from pathlib import Path
import shlex

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
QA = ROOT / 'docs/papers211_215_sequence/qa'
OUT = Path(__file__).resolve().parent
OLD, NEW = QA / 'p211_build_preparation', QA / 'p211_build_revision01'
checks, reads = 0, {}


def check(x, label):
    global checks
    if not x:
        raise AssertionError(label)
    checks += 1


def pin(raw):
    return {'sha256': hashlib.sha256(raw).hexdigest(), 'bytes': len(raw)}


def read(path):
    path = Path(path)
    raw = path.read_bytes()
    v = pin(raw)
    check(str(path) not in reads or reads[str(path)] == v, ('drift', str(path)))
    reads[str(path)] = v
    return raw


def data(path):
    return json.loads(read(path))


def put(name, row):
    with (OUT / name).open('xb') as f:
        f.write((json.dumps(row, sort_keys=True, indent=2) + '\n').encode())


def complete_output(raw, directory):
    observed, expected = json.loads(raw), data(directory / 'RESULT.json')
    if 'seal' in observed:
        seal = observed.pop('seal')
        manifest = read(directory / 'SHA256SUMS')
        check(seal == {'payloads': len(manifest.splitlines()), 'manifest': pin(manifest)}, 'full attached seal')
    check(observed == expected, ('entire actual output JSON binding', str(directory)))
    return expected


def command_envelope(launch, completion, directory, exit_code):
    first = launch['returned']
    if 'session_id' in first:
        check(completion['request']['session_id'] == first['session_id'], 'actual continued session')
        last = completion['returned']
        raw = first['output'] + last['output']
    else:
        check(completion is None, 'direct completion has no invented poll')
        last, raw = first, first['output']
    check(last['exit_code'] == exit_code, 'actual native product exit')
    result = complete_output(raw, directory)
    argv = shlex.split(launch['request']['cmd'])
    check(argv[:2] == ['/usr/bin/env', '-i'] and launch['request']['workdir'] == str(ROOT), 'actual product environment/cwd')
    return result


old = data(OLD / 'NATIVE_TOOL_ENVELOPES.json')
for row in old['diagnostics']:
    number = row['number']
    command_envelope(row['launch'], row.get('completion'), OLD / ('diagnostic_capture' + number),
                     1 if number in ('01', '02', '03') else 0)
new = data(NEW / 'NATIVE_TOOL_ENVELOPES.json')
command_envelope(new['fixture_launch'], None, NEW / 'infrastructure_capture01', 0)
command_envelope(new['diagnostic_launch'], new['diagnostic_completion'], NEW / 'diagnostic_capture01', 0)
check(new['independent_original_report_read']['returned']['output'].encode() ==
      read(QA / 'p211_build_independent_audit/REPORT.md'), 'complete actual original report read')

# The parsed process output and report list must identify the same real native
# attempts, not just list equal counts or statuses.
results, native_embedded = 0, 0
for base in (OLD, NEW):
    for path in sorted(base.rglob('RESULT.json')):
        row = data(path)
        for key in ('native_commands',):
            for native in row.get(key, []):
                actual = path.parent / 'commands' / native['label'] / 'RECEIPT.json'
                check(native == data(actual), 'embedded full native receipt')
                native_embedded += 1
        results += 1
    for path in sorted(base.glob('diagnostic_capture*/commands/discovery/stdout.raw')):
        receipt = data(path.with_name('RECEIPT.json'))
        directory = Path(receipt['argv'][-1])
        complete_output(read(path), directory)
for name, directory in [('fixture_process', NEW / 'infrastructure_capture01/cases')]:
    complete_output(read(NEW / 'infrastructure_capture01/commands' / name / 'stdout.raw'), directory)

lock = data(NEW / 'discovery01/DEPENDENCY_LOCK.candidate.json')
coverage = {v['resolved']: {k: v[k] for k in ('sha256', 'bytes')}
            for v in lock['entries'].values() if v.get('kind') == 'file'}
coverage.update({str(NEW / name): p for name, p in lock['code_observations'].items()})
runtime_count = 0
for path in (NEW / 'discovery01/PARENT_RUNTIME_EARLY.json', NEW / 'discovery01/PARENT_RUNTIME_LATE.json',
             NEW / 'diagnostic_capture01/PARENT_RUNTIME_AFTER.json', NEW / 'diagnostic_capture01/ENTERED.json'):
    sample = data(path)
    if 'runtime' in sample:
        sample = sample['runtime']
    check(sample['environment'] == lock['environment'] and sample['cwd'] == str(ROOT)
          and sample['locale_ctype'] == 'C.UTF-8' and sample['sys_path'] ==
          ['/usr/lib/python310.zip', '/usr/lib/python3.10', '/usr/lib/python3.10/lib-dynload'], 'actual parent settings')
    check(all(s in sample['flags'] for s in ('optimize=0,', 'dont_write_bytecode=1,', 'no_site=1,', 'isolated=1,')), 'isolated flags')
    check(pin(sample['maps_raw'].encode()) == sample['maps_pin'], 'entire maps original')
    actual_maps = set()
    for line in sample['maps_raw'].splitlines():
        columns = line.split(None, 5)
        if len(columns) == 6 and columns[5].startswith('/'):
            actual_maps.add(str(Path(columns[5]).resolve()))
    check(actual_maps == set(sample['mapped_files']), 'full map path census')
    for p, v in sample['mapped_files'].items():
        check(coverage.get(p) == v == pin(read(p)), 'mapped dependency pin')
    for v in sample['modules'].values():
        expected = {k: v[k] for k in ('sha256', 'bytes')}
        check(not v['path'].endswith(('.pyc', '.pyo')) and coverage.get(v['path']) == expected == pin(read(v['path'])), 'module dependency pin')
    runtime_count += 1
for path, value in reads.items():
    check(pin(Path(path).read_bytes()) == value, 'all supplement inputs unchanged')
put('ENVELOPE_INPUTS.json', reads)
put('ENVELOPE_RESULT.json', {'status': 'FULL_SAVED_ENVELOPES_AND_REVISED_RUNTIME_BINDINGS_PASS',
                            'checks': checks, 'read_paths': len(reads), 'product_completions': 7,
                            'result_files': results, 'embedded_native_receipts': native_embedded,
                            'revised_parent_runtime_samples': runtime_count,
                            'new_science_or_build': 0, 'new_native_children': 0,
                            'limits': 'Bounded recorded observations, not live unknown-writer or OS trace.'})
print((OUT / 'ENVELOPE_RESULT.json').read_text(), end='')
