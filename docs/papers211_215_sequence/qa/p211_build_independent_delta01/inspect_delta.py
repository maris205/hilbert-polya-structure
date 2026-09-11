#!/usr/bin/python3.10
"""Independent read-only BLD-I1 delta audit; never import/execute submitted code."""
import ast
from hashlib import sha256
import json
from pathlib import Path
import re
import subprocess
import time

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
QA = ROOT / 'docs/papers211_215_sequence/qa'
REV = QA / 'p211_build_revision01'
OLD = QA / 'p211_build_preparation'
AUD = QA / 'p211_build_independent_audit'
OUT = Path(__file__).resolve().parent
NAMES = ['build_core.py', 'prepare_build.py', 'build_p211.py', 'launch_build.py', 'static_checks.py']
ENV4 = {'PATH': '/usr/bin:/bin', 'LANG': 'C.UTF-8', 'LC_ALL': 'C.UTF-8', 'TZ': 'UTC'}
ENV8 = {**ENV4, 'SOURCE_DATE_EPOCH': '1788825600', 'FORCE_SOURCE_DATE': '1', 'openin_any': 'p', 'openout_any': 'p'}
selected = {p for d in (REV, AUD) for p in d.rglob('*') if p.is_file()}
selected.update(OLD / n for n in NAMES + ['README.md', 'SHA256SUMS', 'discovery05/DEPENDENCY_LOCK.candidate.json'])
selected.update([Path('/usr/lib/python3.10/subprocess.py'),
                 ROOT / '.agents/skills/symbolic-dynamics-research/SKILL.md',
                 Path('/root/autodl-tmp/.codex/skills/paper-compile/SKILL.md')])
reads, checks, native = {}, [], []


def pin(raw):
    return {'bytes': len(raw), 'sha256': sha256(raw).hexdigest()}


def read(p):
    assert p in selected and p.is_file() and not p.is_symlink(), str(p)
    raw = p.read_bytes()
    row = pin(raw)
    if str(p) in reads:
        assert reads[str(p)] == row, ('input drift', str(p))
    reads[str(p)] = row
    return raw


def data(p):
    return json.loads(read(p))


def write(name, raw):
    p = OUT / name
    assert p.is_relative_to(OUT)
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open('xb') as stream:
        stream.write(raw)


def dump(name, row):
    write(name, (json.dumps(row, sort_keys=True, indent=2) + '\n').encode())


def check(condition, label):
    if not condition:
        raise AssertionError(label)
    checks.append(label)


def manifest(p, expected, full=True):
    entries = {}
    for line in read(p).decode().splitlines():
        match = re.fullmatch(r'([0-9a-f]{64})  (.+)', line)
        assert match, str(p)
        digest, name = match.groups()
        assert name not in entries and name != p.name and not Path(name).is_absolute() and '..' not in Path(name).parts
        entries[name] = digest
    check(len(entries) == expected, 'manifest payload count ' + str(p))
    if full:
        inventory = {q.relative_to(p.parent).as_posix() for q in p.parent.rglob('*') if q.is_file()}
        check(inventory == set(entries) | {p.name}, 'manifest complete nonself inventory ' + str(p))
    count = 0
    for name, digest in entries.items():
        q = p.parent / name
        if q in selected:
            check(pin(read(q))['sha256'] == digest, 'manifest bytes ' + str(q))
            count += 1
        elif full:
            raise AssertionError(('unselected full manifest payload', str(q)))
    return {'path': str(p), 'pin': pin(read(p)), 'declared_payloads': expected, 'verified_payloads': count}


for p in sorted(selected):
    read(p)
dump('READ_INPUTS_BEFORE.json', reads)
expected_seals = [(REV / 'DOCUMENTARY_SHA256SUMS', '3aa7db50e9d6039686db3b647e50b9bd021f7b6b3785103888e7f58489176b30'),
                  (AUD / 'SHA256SUMS', '394ade8814a31fae9b02bab1f2d4415d1b8257c7485a991df0b89bbe69f0ca64'),
                  (OLD / 'SHA256SUMS', '5fa2620b27e04f0d07f9b72434f801a948e95d7df884d2e46a915c42028bd042')]
for p, digest in expected_seals:
    check(pin(read(p))['sha256'] == digest, 'exact supplied manifest pin ' + str(p))
manifests = [manifest(REV / 'DOCUMENTARY_SHA256SUMS', 290), manifest(AUD / 'SHA256SUMS', 50),
             manifest(OLD / 'SHA256SUMS', 891, False)]
for name, count in [('diagnostic_capture01', 61), ('discovery01', 187), ('infrastructure_capture01/cases/known_settlement', 8)]:
    manifests.append(manifest(REV / name / 'SHA256SUMS', count))

lockpath = REV / 'discovery01/DEPENDENCY_LOCK.candidate.json'
check(pin(read(lockpath))['sha256'] == 'bb89d966250b0552a47784a5c4aa0d2aaf5b36bc9057fc177a5e552b9bf042ec', 'exact revision candidate')
new, old = data(lockpath), data(OLD / 'discovery05/DEPENDENCY_LOCK.candidate.json')
check(new['status'] == 'CANDIDATE_ONLY_PENDING_ROOT_BINDING' and data(REV / 'BINDING.pending.json')['status'] == 'PENDING_ROOT_BINDING', 'no author self-authorization')
check(new['environment'] == old['environment'] == ENV8 and 'HOME' not in ENV8, 'unchanged literal ENV8')
check(new['source_observations'] == old['source_observations'] and len(new['source_observations']) == 9, 'nine unchanged source metadata pins, no source-body read')
check(len(new['entries']) == 840 and sum(v.get('kind') == 'file' for v in new['entries'].values()) == 795, '840 path spellings 795 files')
check(len(new['ldd_elf_inputs']) == 33 and new['ldd_elf_inputs'] == old['ldd_elf_inputs'], '33 unchanged selected ELF paths')
check(set(new['entries']) == set(new['selector_specs']) == set(new['selection_reasons']), 'all entries selectors reasons share exact keys')
check(new['entries'] == data(REV / 'discovery01/CONFIGURATION_AFTER_SELECTION.json'), 'complete saved configuration equality')
nk, ok = set(new['entries']), set(old['entries'])
delta = {'added': sorted(nk-ok), 'removed': sorted(ok-nk), 'changed': [p for p in sorted(nk & ok) if new['entries'][p] != old['entries'][p]]}
check(delta == {'added': [str(REV / 'prepare_build.py')], 'removed': [str(OLD / 'prepare_build.py')], 'changed': []}, 'only observed prepare module path relocates')
for name, role in new['cwd_relative_absence_roles'].items():
    check({k: role[k] for k in ('raw', 'relative', 'required_state')} == {k: old['cwd_relative_absence_roles'][name][k] for k in ('raw', 'relative', 'required_state')} and role['required_state'] == 'ABSENT' and not role['diagnostic_entry']['present'], 'unchanged separate future-cwd absence role ' + name)
check(len(new['cwd_relative_absence_roles']) == 3, 'three future-cwd roles')
for folder in ('discovery01', 'diagnostic_capture01'):
    for kind, field in [('CODE', 'code_observations'), ('SOURCES', 'source_observations')]:
        check(data(REV / folder / (kind + '_BEFORE.json')) == data(REV / folder / (kind + '_AFTER.json')) == new[field], 'saved before-after lock equality ' + folder + ':' + kind)
for name in NAMES:
    check(pin(read(REV / name)) == pin(read(REV / 'diagnostic_capture01/executed_adapter' / name)) == new['code_observations'][name], 'physical current executed code equality ' + name)
for name in ('prepare_build.py', 'build_p211.py'):
    check(read(REV / name) == read(OLD / name), 'byte-unchanged production component ' + name)

receipts = sorted(p for p in selected if p.is_relative_to(REV) and p.name == 'RECEIPT.json')
attempts = sorted(p for p in selected if p.is_relative_to(REV) and p.name == 'ATTEMPT.json')
unknown = REV / 'infrastructure_capture01/cases/unknown_launch/commands/refused_before_handle'
check(len(receipts) == 34 and len(attempts) == 35, '34 complete receipts 35 attempts')
saved = []
for p in receipts:
    row, attempted, spawned = data(p), data(p.with_name('ATTEMPT.json')), data(p.with_name('SPAWNED.json'))
    check(all(row[k] == v for k, v in attempted.items()), 'literal attempted fields retained ' + str(p))
    check(row['native_handle_received'] and row['launch_outcome'] == 'KNOWN_NATIVE_HANDLE' and row['native_exit_code'] in row['expected_exit_codes'] and row['successful'] and row['error'] is None and row['wrapper_reason'] == 'NATIVE_EXIT', 'known successful native result ' + str(p))
    check(row['streams_settled'] and row['remaining_session_members'] == [] and row['owned_session_interventions'] == [] and row['environment'] == ENV8, 'settled owned session exact ENV8 ' + str(p))
    check(spawned['pid'] == spawned['session'] and attempted['attempted_epoch'] <= spawned['spawned_epoch'] <= row['ended_epoch'], 'actual spawned identity ordered timestamps ' + str(p))
    check(row['direct_inputs_equal'] and data(p.with_name('INPUTS_BEFORE.json')) == data(p.with_name('INPUTS_AFTER.json')), 'direct input before-after closure ' + str(p))
    for stream in ('stdout.raw', 'stderr.raw'):
        check(pin(read(p.with_name(stream))) == row['streams'][stream], 'full saved raw stream ' + str(p) + ':' + stream)
    saved.append({'path': str(p), 'argv': row['argv'], 'native_exit_code': row['native_exit_code'], 'streams': row['streams']})
check([str(p.parent) for p in attempts if not p.with_name('RECEIPT.json').is_file()] == [str(unknown)], 'only deliberately unknown attempt incomplete')
unclosed, event = data(unknown / 'UNCLOSED.json'), data(unknown.parent.parent / 'AUDIT_EVENT.json')
check(all(unclosed[k] == v for k, v in data(unknown / 'ATTEMPT.json').items()), 'unknown preserves attempted fields')
check(unclosed['native_handle_received'] is False and unclosed['launch_outcome'] == 'UNKNOWN_NO_NATIVE_HANDLE' and unclosed['native_exit_code'] is None and unclosed['streams_settled'] is False and unclosed['wrapper_reason'] == 'NO_NATIVE_HANDLE_UNKNOWN_LAUNCH', 'unknown classification remains conservative')
check('streams' not in unclosed and 'successful' not in unclosed and not any((unknown / n).exists() for n in ('SPAWNED.json', 'RECEIPT.json', 'INPUTS_AFTER.json')), 'no final stream pins receipt or after-inventory for unknown')
check('AuditHookBeforeHandle' in unclosed['error'] and '/usr/lib/python3.10/subprocess.py' in unclosed['error'] and event['argv'] == unclosed['argv'] and event['environment'] == ENV8 and event['event'] == 'subprocess.Popen', 'actual controlled audit event and traceback binding')
capture = REV / 'infrastructure_capture01'
cases, outer = data(capture / 'cases/RESULT.json'), data(capture / 'RESULT.json')
check(cases['unknown_native_seal_refused'] == cases['parent_native_seal_refused'] == outer['capture_native_seal_refusal'] == 'Unsettled subtree prevents seal', 'saved native seal refused at child and two parents')
check(not any((p / 'SHA256SUMS').exists() for p in (unknown.parent.parent, capture / 'cases', capture, REV)), 'no forbidden native seal exists')
check(outer['native_fixture_process'] == data(capture / 'commands/fixture_process/RECEIPT.json') and outer['native_fixture_process']['native_exit_code'] == 0 and not outer['native_subtree_acceptance'] and not outer['build_acceptance'], 'completed enclosing fixture does not accept unknown native subtree')
known = capture / 'cases/known_settlement/commands/ordinary_stdout_stderr'
check(read(known / 'stdout.raw') == b'known stdout\n' and read(known / 'stderr.raw') == b'known stderr\n' and data(known / 'RECEIPT.json')['native_exit_code'] == 0, 'ordinary positive control has exact raw bytes and native exit zero')
fixturepins = data(capture / 'SOURCES_BEFORE.json')
check(fixturepins == data(capture / 'SOURCES_AFTER.json') == {name: pin(read(REV / name)) for name in fixturepins} == {name: pin(read(capture / 'executed_fixture' / name)) for name in fixturepins}, 'fixture and core exact physical execution snapshots')

envelopes = data(REV / 'NATIVE_TOOL_ENVELOPES.json')
fl, dl, dc = [envelopes[k] for k in ('fixture_launch', 'diagnostic_launch', 'diagnostic_completion')]
check(fl['returned']['exit_code'] == 0 and 'session_id' not in fl['returned'] and json.loads(fl['returned']['output']) == outer, 'actual fixture tool completed zero with literal output')
check(dl['returned']['session_id'] == dc['request']['session_id'] == 55993 and dc['returned']['exit_code'] == 0, 'actual yielded diagnostic session settled zero')
diagnostic_output = json.loads(dc['returned']['output'])
check(diagnostic_output.pop('seal')['manifest'] == pin(read(REV / 'diagnostic_capture01/SHA256SUMS')) and diagnostic_output == data(REV / 'diagnostic_capture01/RESULT.json'), 'literal complete diagnostic tool output and native seal')
producer_tool = data(REV / 'DOCUMENTARY_AUDIT_TOOL_NATIVE.json')
check(producer_tool['returned']['exit_code'] == 0 and json.loads(producer_tool['returned']['output']) == data(REV / 'DOCUMENTARY_AUDIT.json'), 'producer documentary tool-output exactness, not independent acceptance')
check(envelopes['independent_original_report_read']['returned']['output'].encode() == read(AUD / 'REPORT.md'), 'producer read the unchanged original finding')
host = Path('/usr/lib/python3.10/subprocess.py')
check(pin(read(host)) == data(REV / 'DOCUMENTARY_AUDIT.json')['baseline_inputs'][str(host)] and pin(read(host))['sha256'] == '53bb0d0780e166ef4ae94f3b2a817a8aae49a84d899db1f4c31f933d429057d6', 'exact independently inspected installed subprocess source')
source = read(host).decode()
start = source.index('            sys.audit("subprocess.Popen"', source.index('"""Execute program (POSIX version)'))
check(start < source.index('                self._posix_spawn(', start) < source.index('                    self.pid = _posixsubprocess.fork_exec(', start), 'controlled POSIX audit event precedes both native creation branches')

trees = {name: ast.parse(read(REV / name), filename=str(REV / name)) for name in NAMES + ['infrastructure_fixture.py']}
core = read(REV / 'build_core.py').decode()
check('settled, members, interventions = False, [], []' in core and "reason = 'NO_NATIVE_HANDLE_UNKNOWN_LAUNCH'" in core, 'new recorder defaults unknown not settled')
check(core.index('    if not settled:') < core.index("    row['streams'] =") < core.index("    write_new(work / 'RECEIPT.json', row)"), 'unknown rejection dominates final hashing and receipt')
for name in ('build_p211.py', 'launch_build.py'):
    check('UNCLOSED.json' in read(REV / name).decode() and any(isinstance(n, ast.Call) and isinstance(n.func, ast.Name) and n.func.id == 'incomplete_native' for n in ast.walk(trees[name])), 'existing inner/outer unknown and incomplete guards ' + name)


def command(label, argv, expected):
    row = {'argv': argv, 'cwd': str(ROOT), 'environment': ENV4, 'expected_exit_codes': expected,
           'started_epoch': time.time(), 'scope': 'Read-only byte comparison/diff; no submitted execution.'}
    dump('native/' + label + '/ATTEMPT.json', row)
    result = subprocess.run(argv, cwd=ROOT, env=ENV4, stdin=subprocess.DEVNULL, capture_output=True, timeout=30)
    write('native/' + label + '/stdout.raw', result.stdout)
    write('native/' + label + '/stderr.raw', result.stderr)
    row.update(ended_epoch=time.time(), native_exit_code=result.returncode, stdout=pin(result.stdout), stderr=pin(result.stderr))
    dump('native/' + label + '/RECEIPT.json', row)
    native.append(row)
    check(result.returncode in expected and result.stderr == b'', 'fresh native actual outcome ' + label)
    return result


for index, name in enumerate(NAMES):
    command(str(index) + '_cmp', ['/usr/bin/cmp', str(REV / name), str(REV / 'diagnostic_capture01/executed_adapter' / name)], [0])
    folder = REV / 'diagnostic_capture01/commands' / ('diff_' + name.replace('.', '_'))
    row = data(folder / 'RECEIPT.json')
    check(row['argv'] == ['/usr/bin/diff', '-u', str(OLD / name), str(REV / name)], 'literal final-original delta argv ' + name)
    actual = command(str(index) + '_diff', row['argv'], [row['native_exit_code']])
    check(actual.stdout == read(folder / 'stdout.raw') and actual.stderr == read(folder / 'stderr.raw'), 'every fresh delta byte equals archived native delta ' + name)
before = dict(reads)
for p in sorted(selected):
    read(p)
check(reads == before, 'all complete read inputs stable before-after')
dump('READ_INPUTS_AFTER.json', reads)
dump('SAVED_NATIVE_CENSUS.json', saved)
dump('CHECKS.json', checks)
result = {'status': 'BLD_I1_RESOLVED_FOR_REVISION01_PENDING_EXACT_ROOT_BINDING',
          'original_finding': 'Major/open remains unchanged for original preparation',
          'new_concrete_blockers': [], 'checks': len(checks), 'read_files': len(reads),
          'read_bytes': sum(v['bytes'] for v in reads.values()), 'manifests': manifests,
          'candidate': {'path': str(lockpath), 'pin': pin(read(lockpath))},
          'configuration_entry_delta': delta, 'complete_saved_native_receipts': len(receipts),
          'deliberately_unknown_attempts': 1, 'fresh_native_readonly_commands': len(native),
          'independence': 'Same independent auditor; submitted code AST/read only, no execution/import; root separately receives science and host lock.',
          'documentary_not_native_seal': True, 'tex_compilations': 0, 'scientific_executions': 0,
          'renderings': 0, 'build_acceptance': False, 'terminal_acceptance': False}
dump('RESULT.json', result)
print(json.dumps(result, sort_keys=True))
