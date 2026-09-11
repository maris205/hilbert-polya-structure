#!/usr/bin/python3.10
"""Root read-only original reception; evaluates no submitted source."""
import hashlib
import json
import os
from pathlib import Path
import re
import stat
import subprocess

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
QA = ROOT / 'docs/papers211_215_sequence/qa'
OLD = QA / 'p211_build_preparation'
NEW = QA / 'p211_build_revision01'
AUDIT = QA / 'p211_build_independent_audit'
OUT = Path(__file__).resolve().parent
PAPER = ROOT / 'papers/211-kernel-image-projection-feedback'
NAMES = ('build_core.py', 'prepare_build.py', 'build_p211.py', 'launch_build.py', 'static_checks.py')
ENV4 = {'PATH': '/usr/bin:/bin', 'LANG': 'C.UTF-8', 'LC_ALL': 'C.UTF-8', 'TZ': 'UTC'}
ENV8 = {**ENV4, 'SOURCE_DATE_EPOCH': '1788825600', 'FORCE_SOURCE_DATE': '1', 'openin_any': 'p', 'openout_any': 'p'}
reads, mappings, manifests, commands = {}, [], {}, []
checks = 0


def check(test, label):
    global checks
    if not test:
        raise AssertionError(label)
    checks += 1


def pin(raw):
    return {'sha256': hashlib.sha256(raw).hexdigest(), 'bytes': len(raw)}


def read(path):
    path = Path(path)
    check(path.is_file(), ('read file', str(path)))
    raw = path.read_bytes()
    value = pin(raw)
    check(str(path) not in reads or reads[str(path)] == value, ('read drift', str(path)))
    reads[str(path)] = value
    return raw


def pairs(rows):
    result = {}
    for key, value in rows:
        check(key not in result, ('duplicate json key', key))
        result[key] = value
    return result


def data(path):
    return json.loads(read(path), object_pairs_hook=pairs,
                      parse_constant=lambda x: (_ for _ in ()).throw(ValueError(x)))


def put(name, value):
    path = OUT / name
    path.parent.mkdir(parents=True, exist_ok=True)
    raw = value if isinstance(value, bytes) else (json.dumps(value, sort_keys=True, indent=2) + '\n').encode()
    with path.open('xb') as stream:
        stream.write(raw)


def manifest(path, expected=None):
    raw = read(path)
    if expected:
        check(pin(raw)['sha256'] == expected, ('sealed manifest', str(path)))
    entries = {}
    for line in raw.decode().splitlines():
        match = re.fullmatch(r'([a-f0-9]{64})  (.+)', line)
        check(match is not None, 'manifest syntax')
        digest, name = match.groups()
        check(name not in entries and name != path.name and not Path(name).is_absolute()
              and '..' not in Path(name).parts, 'manifest path')
        entries[name] = digest
    actual = {p.relative_to(path.parent).as_posix() for p in path.parent.rglob('*') if p.is_file()}
    check(actual == set(entries) | {path.name}, ('complete inventory', str(path)))
    for name, digest in entries.items():
        p = path.parent / name
        check(not p.is_symlink() and pin(read(p))['sha256'] == digest, ('manifest member', str(p)))
    manifests[str(path)] = len(entries)
    return entries


def entry(path, members=False):
    p = Path(path)
    value = {'path': str(p), 'present': os.path.lexists(p), 'symlink': p.is_symlink(), 'resolved': str(p.resolve())}
    if p.is_symlink():
        value['link'] = os.readlink(p)
    if value['present']:
        s = p.stat()
        if stat.S_ISREG(s.st_mode):
            value.update(kind='file', **pin(read(p)))
        elif stat.S_ISDIR(s.st_mode):
            value['kind'] = 'directory'
            if members:
                value['members'] = sorted(q.name for q in p.iterdir())
        elif stat.S_ISCHR(s.st_mode):
            value.update(kind='character_device', major=os.major(s.st_rdev), minor=os.minor(s.st_rdev))
        else:
            value.update(kind='other', mode=stat.S_IFMT(s.st_mode))
    return value


manifest(OLD / 'SHA256SUMS', '5fa2620b27e04f0d07f9b72434f801a948e95d7df884d2e46a915c42028bd042')
manifest(NEW / 'DOCUMENTARY_SHA256SUMS', '3aa7db50e9d6039686db3b647e50b9bd021f7b6b3785103888e7f58489176b30')
manifest(AUDIT / 'SHA256SUMS', '394ade8814a31fae9b02bab1f2d4415d1b8257c7485a991df0b89bbe69f0ca64')
for base in (OLD, NEW):
    for p in sorted(base.rglob('SHA256SUMS')):
        if p != OLD / 'SHA256SUMS':
            manifest(p)
pool = list(reads)


def resolve_pin(path, expected):
    wanted = {k: expected[k] for k in ('sha256', 'bytes')}
    p = Path(path)
    if p.is_file() and pin(p.read_bytes()) == wanted:
        read(p)
        return p
    candidates = [Path(k) for k in pool if Path(k).name == p.name and reads[k] == wanted]
    if p.name in ('SYMBOLIC_DYNAMICS_STATE.md', 'PIPELINE_STATE.md'):
        candidates.insert(0, QA / 'control_author_runtime_accepted01' / p.name)
    candidates = [q for q in candidates if q.is_file() and pin(q.read_bytes()) == wanted]
    check(bool(candidates), ('missing exact historical original', str(path), wanted))
    selected = sorted(set(candidates))[0]
    check(pin(read(selected)) == wanted, 'historical exact bytes')
    mappings.append({'original_path': str(path), 'pin': wanted, 'physical_copy': str(selected)})
    return selected


native_count, failed_count, raw_count, unknown = 0, 0, 0, []
for base in (OLD, NEW):
    for p in sorted(base.rglob('ATTEMPT.json')):
        a = data(p)
        receipt = p.with_name('RECEIPT.json')
        if not receipt.exists():
            check(base == NEW and p.parent.name == 'refused_before_handle', 'only deliberate unknown attempt')
            u = data(p.with_name('UNCLOSED.json'))
            check(u['native_handle_received'] is False and u['native_exit_code'] is None and
                  u['streams_settled'] is False and u['launch_outcome'] == 'UNKNOWN_NO_NATIVE_HANDLE'
                  and 'streams' not in u and not p.with_name('INPUTS_AFTER.json').exists()
                  and not p.with_name('SPAWNED.json').exists(), 'unclosed branch remains unfinalized')
            unknown.append(str(p.parent))
            continue
        r = data(receipt)
        check(all(r[k] == value for k, value in a.items()), 'literal native attempt binding')
        check(r['environment'] == ENV8 and r['streams_settled'] is True
              and r['remaining_session_members'] == [] and r['owned_session_interventions'] == [], 'native settled session')
        before, after = data(p.with_name('INPUTS_BEFORE.json')), data(p.with_name('INPUTS_AFTER.json'))
        check(before == after and r['direct_inputs_equal'] is True, 'all native direct keys unchanged')
        for path, value in before.items():
            if value.get('kind') == 'file':
                resolve_pin(path, value)
        spawned = data(p.with_name('SPAWNED.json'))
        check(spawned['pid'] == spawned['session'] and
              a['attempted_epoch'] <= spawned['spawned_epoch'] <= r['ended_epoch'], 'native identity and order')
        for stream in ('stdout.raw', 'stderr.raw'):
            check(pin(read(p.with_name(stream))) == r['streams'][stream], 'complete native raw stream')
            raw_count += 1
        check(r['successful'] == (r['error'] is None and r['native_exit_code'] in a['expected_exit_codes']), 'real exit versus success')
        if not r['successful']:
            failed_count += 1
        native_count += 1
check(native_count == 144 and failed_count == 3 and len(unknown) == 1, 'complete native outcome census')
for p in (NEW / 'infrastructure_capture01', NEW / 'infrastructure_capture01/cases',
          NEW / 'infrastructure_capture01/cases/unknown_launch'):
    check(not (p / 'SHA256SUMS').exists(), 'refused native seal not replaced')
fixture = data(NEW / 'infrastructure_capture01/RESULT.json')
check(fixture['status'] == 'FIXTURE_PROCESS_SETTLED_DOCUMENTARY_SNAPSHOT_PERMITTED'
      and fixture['native_subtree_acceptance'] is False, 'documentary versus native scope')
known = NEW / 'infrastructure_capture01/cases/known_settlement/commands/ordinary_stdout_stderr'
check(read(known / 'stdout.raw') == b'known stdout\n' and read(known / 'stderr.raw') == b'known stderr\n', 'actual ordinary child bytes')

lock_path = NEW / 'discovery01/DEPENDENCY_LOCK.candidate.json'
check(pin(read(lock_path))['sha256'] == 'bb89d966250b0552a47784a5c4aa0d2aaf5b36bc9057fc177a5e552b9bf042ec', 'revised candidate immutable')
lock = data(lock_path)
check(lock['environment'] == ENV8 and len(lock['entries']) == 840 and
      set(lock['entries']) == set(lock['selector_specs']) == set(lock['selection_reasons']), 'complete bounded selector')
current = {p: entry(p, spec['members']) for p, spec in lock['selector_specs'].items()}
check(current == lock['entries'] == data(NEW / 'discovery01/CONFIGURATION_AFTER_SELECTION.json'), 'fresh exact 840-entry key')
check(sum(v.get('kind') == 'file' for v in current.values()) == 795 and len(lock['ldd_elf_inputs']) == 33, 'file and ELF counts')
check(set(lock['cwd_relative_absence_roles']) == {'TEXMFHOME', 'TEXMFCONFIG', 'TEXMFVAR'}, 'future three roots')
for name in NAMES:
    check(pin(read(NEW / name)) == lock['code_observations'][name] ==
          pin(read(NEW / 'diagnostic_capture01/executed_adapter' / name)), 'revised current code exact')
for name, expected in lock['source_observations'].items():
    check(pin(read(PAPER / name)) == expected, 'nine actual source byte pins')
for path, expected in lock['historical_inputs'].items():
    resolve_pin(path, expected)
for label, value in lock['queries'].items():
    work = NEW / 'discovery01/commands' / label
    check(data(work / 'RECEIPT.json')['argv'] == lock['query_commands'][label], 'literal query argv')
    raw = read(work / 'stdout.raw').decode()
    if isinstance(value, str):
        check(raw.strip().replace(str(NEW / 'discovery01'), '{COMMAND_CWD}') == value, 'effective query raw binding')
    else:
        found = {name: [] for name in value['names']}
        for line in raw.splitlines():
            check(Path(line).name in found and line in current, 'lookup line selected')
            found[Path(line).name].append(line)
        check(found == value['resolutions'], 'all lookup original resolutions')

for base, capture, baseline in ((OLD, 'diagnostic_capture05', OLD / 'history/diagnostic01_source'),
                                (NEW, 'diagnostic_capture01', OLD)):
    for name in NAMES:
        argv = ['/usr/bin/diff', '-u', str(baseline / name), str(base / name)]
        result = subprocess.run(argv, cwd=ROOT, env=ENV4, stdin=subprocess.DEVNULL, capture_output=True, timeout=30)
        label = base.name + '_' + name
        put('native/' + label + '/stdout.raw', result.stdout)
        put('native/' + label + '/stderr.raw', result.stderr)
        row = {'argv': argv, 'cwd': str(ROOT), 'environment': ENV4, 'native_exit_code': result.returncode,
               'stdout': pin(result.stdout), 'stderr': pin(result.stderr)}
        put('native/' + label + '/RECEIPT.json', row)
        commands.append(row)
        check(result.returncode in (0, 1) and result.stderr == b'', 'actual native diff outcome')
        check(result.stdout == read(base / capture / 'commands' / ('diff_' + name.replace('.', '_')) / 'stdout.raw'), 'entire actual saved native diff')

audit_before = data(AUDIT / 'READ_INPUTS_BEFORE.json')
check(audit_before == data(AUDIT / 'READ_INPUTS_AFTER.json') and len(audit_before) == 271, 'independent original selected key')
for path, expected in audit_before.items():
    resolve_pin(path, expected)
for p in sorted((AUDIT / 'native').glob('*/RECEIPT.json')):
    row = data(p)
    for stream in ('stdout', 'stderr'):
        check(pin(read(p.with_name(stream + '.raw'))) == row[stream], 'independent actual native raw')
    check(row['native_exit_code'] in row['expected_exit_codes'], 'independent actual native exit')
result = data(AUDIT / 'RESULT.json')
tool = data(AUDIT / 'TOOL_RETURN.actual.json')
check(tool['exit_code'] == 0 and json.loads(tool['output']) == result, 'independent actual tool body binding')
check(result['open_findings'] == ['BLD-I1'], 'original finding stays historically open')
for path, value in list(reads.items()):
    check(pin(Path(path).read_bytes()) == value, ('full reception read key unchanged', path))
put('READ_INPUTS.json', reads)
put('HISTORICAL_MAPPINGS.json', mappings)
put('RESULT.json', {'status': 'ROOT_BUILD_PREPARATION_ORIGINALS_CHECKED_PENDING_SAME_AUDITOR_DELTA',
                   'checks': checks, 'read_paths': len(reads), 'manifests': manifests,
                   'native_receipts': native_count, 'native_raw_streams': raw_count,
                   'preserved_failed_native_commands': failed_count, 'intentional_unknown': unknown,
                   'fresh_native_diffs': len(commands), 'live_configuration_entries': len(current),
                   'scientific_executions': 0, 'TeX_builds': 0, 'submitted_code_evaluations': 0})
print((OUT / 'RESULT.json').read_text(), end='')
