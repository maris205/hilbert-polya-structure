#!/usr/bin/env python3
"""Read-only, document-only P210 completion-lifecycle follow-up.

The initial artifact gate must already have actual root acceptance. This
reader checks the sole rolling lifecycle/manifest transition and its actual
evidence. It does not rerun or import the initial reader, science or builds,
and does not claim a fresh host dependency or visual review.
"""
from collections import Counter
from hashlib import sha256
import gzip
import json
import os
from pathlib import Path
import re
import shlex
import sys
import traceback
from urllib.parse import unquote

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
QA = ROOT / 'docs/papers204_208_sequence/qa'
PAPER = ROOT / 'papers/210-weakly-increasing-run-aggregation'
PREP = QA / 'p210_terminal_lifecycle_preparation'
INITIAL_PREP = QA / 'p210_terminal_artifact_revision_03'
INITIAL = QA / 'p210_terminal_artifact_03'
HISTORY = QA / 'p210_precompletion_controls_01'
CACHE = QA / 'p210_terminal_lifecycle_01/never_created_reader_cache'
ENV = {'PATH': '/usr/bin:/bin', 'LANG': 'C.UTF-8', 'LC_ALL': 'C.UTF-8', 'TZ': 'UTC'}
OLD = {
    str(PAPER / 'ROOT_LIFECYCLE.md'): {
        'sha256': 'e0b3bbd041d2fea0c66f8f11d113b8505a06463f0ea3bf629823746f403b7449', 'bytes': 4323},
    str(PAPER / 'PAPER_MANIFEST.sha256'): {
        'sha256': 'e821f92af0393af33308cce5667b24a93d183ed662a62b9232f25f15cb139ea2', 'bytes': 256888}}
CHECKS, SEEN, USED_OLD, PACKAGES = Counter(), {}, set(), {}

def ck(ok, label, detail=''):
    CHECKS[label] += 1
    if not ok:
        raise AssertionError((label, detail))

def value(path):
    row = pin(path)
    return {'sha256': row['sha256'], 'bytes': row['size']}

def file_key(path):
    p = Path(path)
    ck(p.is_file(), 'physical_file', str(p))
    h = sha256()
    with p.open('rb') as stream:
        for block in iter(lambda: stream.read(1 << 20), b''):
            h.update(block)
    return {'real': str(p.resolve()), 'sha256': h.hexdigest(), 'size': p.stat().st_size,
            'symlink': os.readlink(p) if p.is_symlink() else None}

def pin(path, expected=None, force=False):
    name = str(Path(path))
    if force or name not in SEEN:
        value = file_key(path)
        ck(name not in SEEN or value == SEEN[name], 'read_key_stability', name)
        SEEN[name] = value
    value = SEEN[name]
    if expected is not None:
        if isinstance(expected, str):
            ck(value['sha256'] == expected, 'expected_sha256', name)
        elif set(expected) == {'real', 'sha256', 'size', 'symlink'}:
            ck(value == expected, 'exact_physical_ledger_key', name)
        else:
            ck(value['sha256'] == expected['sha256'], 'expected_record_sha256', name)
            size = expected.get('bytes', expected.get('size'))
            ck(size is None or value['size'] == size, 'expected_record_size', name)
    return value

def raw(path):
    expected = pin(path)
    value = Path(path).read_bytes()
    ck(len(value) == expected['size'] and sha256(value).hexdigest() == expected['sha256'],
       'full_decoded_input_raw_stability', str(path))
    return value

def obj(path):
    value = raw(path)
    return json.loads(gzip.decompress(value) if str(path).endswith('.gz') else value)

def physical(base):
    files = set()
    for p in base.rglob('*'):
        ck(not p.is_symlink(), 'no_workspace_package_symlink', str(p))
        if p.is_file():
            files.add(p.relative_to(base).as_posix())
    return files

def stripped_links(content):
    content = re.sub(r'(?ms)^[ ]{0,3}(`{3,}|~{3,})[^\n]*\n.*?^[ ]{0,3}\1[ \t]*$', '\n\n', content)
    content = re.sub(r'(?:\A|\n\n)(?:(?: {4}|\t)[^\n]*(?:\n|$))+', '\n\n', content)
    content = re.sub(r'(`+)(?:(?!\1)[\s\S])*?\1', ' ', content)
    return re.findall(r'\[[^\]]*\]\(([^)]+)\)', content)


def rows(path):
    parsed = {}
    for line in raw(path).decode().splitlines():
        match = re.fullmatch(r'([0-9a-f]{64})  (.+)', line)
        ck(match is not None, 'strict two-space manifest syntax', str(path))
        digest, name = match.groups()
        relative = Path(name)
        ck(not relative.is_absolute() and relative.as_posix() == name and
           not any(part in {'.', '..'} for part in relative.parts) and name not in parsed,
           'unique bounded manifest member', name)
        parsed[name] = digest
    return parsed

def package(base, expected, count, manifest='SHA256SUMS'):
    pin(base / manifest, expected)
    members = rows(base / manifest)
    ck(len(members) == count and manifest not in members and
       physical(base) == set(members) | {manifest}, 'complete nonself package', str(base))
    PACKAGES[str(base)] = set(members) | {manifest}
    for name, digest in members.items():
        pin(base / name, digest)
    return members

def exact_old_or_current(path, expected):
    ck(set(expected) == {'sha256', 'bytes'} and
       re.fullmatch('[0-9a-f]{64}', expected['sha256']) is not None and
       type(expected['bytes']) is int and expected['bytes'] >= 0,
       'exact two-field original pin schema', path)
    target = Path(path)
    if path in OLD and expected == OLD[path]:
        target = HISTORY / target.name
        USED_OLD.add(path)
    return pin(target, expected)

def current_runtime():
    ck(Path.cwd() == ROOT and Path(__file__) == PREP / 'inspect_p210_lifecycle.py' and
       dict(os.environ) == ENV and sys.flags.isolated == sys.flags.no_site == 1 and
       sys.dont_write_bytecode is True and sys.pycache_prefix == str(CACHE) and
       not os.path.lexists(CACHE), 'isolated read-only documentary invocation')
    ck(sys.path == ['/usr/lib/python310.zip', '/usr/lib/python3.10', '/usr/lib/python3.10/lib-dynload'],
       'exact system-only documentary module path')
    return dict(argv=sys.argv, cwd=str(Path.cwd()), environment=dict(os.environ),
        executable=sys.executable, cache=str(CACHE), cache_absent=True,
        isolated=sys.flags.isolated, no_site=sys.flags.no_site,
        no_bytecode=sys.dont_write_bytecode, module_search_path=sys.path)

def normal_root_native(prefix, source, session, extra=()):
    launch = obj(QA / (prefix + '_LAUNCH.actual.json'))
    completed = obj(QA / (prefix + '_COMPLETION.actual.json'))
    ck(type(session) is int and session > 0 and launch['cwd'] == str(ROOT) and
       launch['result']['output'] == '' and 'exit_code' not in launch['result'] and
       launch['result']['session_id'] == completed['session_id'] == session and
       completed['launch_record'] == prefix + '_LAUNCH.actual.json' and
       completed['result']['exit_code'] == 0 and 'session_id' not in completed['result'] and
       shlex.split(launch['command']) == ['/usr/bin/python3.10', '-I', '-S', '-B', str(source), *extra],
       'actual normal-zero native closure before any corresponding output-package hash', prefix)
    return completed

def all_actual_native_closures(binding):
    normal_root_native('P210_ARTIFACT03_ROOT', QA / 'record_p210_artifact_03.py', 16560,
        ('--expected-artifact-preparation-sha256', binding['initial_artifact']['preparation_seal']['sha256']))
    normal_root_native('P210_ARTIFACT_ROOT_READ', QA / 'receive_p210_initial_artifact.py', 53600)
    preserved = obj(QA / 'P210_PRECOMPLETION_CONTROLS_ROOT.actual.json')
    ck(preserved['cwd'] == str(ROOT) and preserved['result']['exit_code'] == 0 and
       'session_id' not in preserved['result'] and shlex.split(preserved['command']) ==
       ['/usr/bin/python3.10', '-I', '-S', '-B', str(QA / 'preserve_p210_precompletion_controls.py')],
       'actual direct normal-zero preservation before historical-copy hashes')
    normal_root_native('P210_COMPLETION_LIFECYCLE_REFRESH_ROOT',
        QA / 'refresh_p210_completion_whole_manifest.py',
        binding['documentary_transition']['refresh_native_session'])

def initial_capture(binding):
    spec = binding['initial_artifact']
    ck(spec['preparation_path'] == str(INITIAL_PREP) and spec['capture_path'] == str(INITIAL) and
       spec['preparation_seal'] == {'sha256': '8efef29aee07210eee9ec95a1d3df51d4539f33d3189991cd1b42a98a508d3dd', 'bytes': 799},
       'actual third artifact preparation identity')
    launch = obj(QA / 'P210_ARTIFACT03_ROOT_LAUNCH.actual.json')
    completed = obj(QA / 'P210_ARTIFACT03_ROOT_COMPLETION.actual.json')
    ck(launch['cwd'] == str(ROOT) and launch['result']['output'] == '' and
       launch['result']['session_id'] == completed['session_id'] == 16560 and
       completed['launch_record'] == 'P210_ARTIFACT03_ROOT_LAUNCH.actual.json' and
       completed['result']['exit_code'] == 0 and
       shlex.split(launch['command']) == ['/usr/bin/python3.10', '-I', '-S', '-B',
           str(QA / 'record_p210_artifact_03.py'), '--expected-artifact-preparation-sha256',
           spec['preparation_seal']['sha256']], 'actual normal-zero initial native closure before accepting capture')
    package(INITIAL_PREP, spec['preparation_seal'], 9)
    package(INITIAL, spec['capture_seal'], 6)
    attempt, spawn, result = (obj(INITIAL / name) for name in ('ATTEMPT.json', 'SPAWN.json', 'RESULT.json'))
    argv = ['/usr/bin/python3.10', '-I', '-S', '-B', '-X',
        'pycache_prefix=' + str(INITIAL / 'never_created_reader_cache'),
        str(INITIAL_PREP / 'inspect_p210_artifact.py'), '--expected-preparation-sha256',
        spec['preparation_seal']['sha256']]
    ck(attempt == dict(argv=argv, cwd=str(ROOT), environment=ENV, inputs_before=result['inputs_before'],
       timeout_seconds=1800, start_new_session=True, started_epoch=attempt['started_epoch'],
       paper_terminal_present_before=True), 'entire original initial capture attempt')
    ck(set(result) == {'argv', 'cwd', 'environment', 'pid', 'original_wait_exit_code',
       'cleanup_wait_exit_code', 'timed_out', 'wait_error', 'cleanup_events', 'child_reaped',
       'process_group_absent', 'inputs_before', 'inputs_after', 'inputs_unchanged', 'stdout',
       'stderr', 'paper_terminal_present_after', 'finished_epoch'} and result['argv'] == argv and
       result['cwd'] == str(ROOT) and result['environment'] == ENV and
       result['original_wait_exit_code'] == result['cleanup_wait_exit_code'] == 0 and
       result['timed_out'] is False and result['wait_error'] is None and result['cleanup_events'] == [] and
       result['child_reaped'] is result['process_group_absent'] is result['inputs_unchanged'] is
       result['paper_terminal_present_after'] is True and result['inputs_before'] == result['inputs_after'] and
       type(result['pid']) is int and result['pid'] > 0 and
       result['finished_epoch'] >= spawn['spawned_epoch'] >= attempt['started_epoch'] and
       spawn == dict(pid=result['pid'], process_group_id=result['pid'], spawned_epoch=spawn['spawned_epoch']) and
       not os.path.lexists(INITIAL / 'never_created_reader_cache'),
       'entire initial capture result normal wait, settled child and no cleanup')
    ck(len(result['inputs_before']) == 11, 'all original initial capture inputs')
    for name, expected in result['inputs_before'].items():
        exact_old_or_current(name, expected)
    ck(raw(INITIAL / 'executed_source.py') == raw(QA / 'record_p210_artifact_03.py') and
       result['stdout'] == value(INITIAL / 'ARTIFACT_REPORT.json') and
       result['stderr'] == value(INITIAL / 'stderr') and raw(INITIAL / 'stderr') == b'',
       'full original captured source and separate raw streams')
    report = obj(INITIAL / 'ARTIFACT_REPORT.json')
    ck(report['schema'] == 'p210-terminal-artifact-reader-revision-03' and
       report['status'] == 'PASS_P210_TERMINAL_ARTIFACT_INITIAL_LIFECYCLE_FOLLOWUP_PENDING' and
       report['paper'] == 'P210' and report['checks'] == sum(report['checks_by_kind'].values()) and
       report['checks'] > 0 and
       all(report[name] == 0 for name in ('new_scientific_runs', 'new_builds', 'new_views',
          'new_manuscript_reviews', 'reader_file_writes', 'old_programs_imported_or_executed')) and
       report['root_acceptance'] is report['paper_completion'] is report['five_paper_completion'] is False and
       report['external'] == 'OWNER_AMBER / HOLD_EXTERNAL', 'actual initial PASS remains bounded')
    pending = report['pending_lifecycle_and_whole']
    ck(pending['lifecycle'] == OLD[str(PAPER / 'ROOT_LIFECYCLE.md')] and
       pending['whole_manifest'] == OLD[str(PAPER / 'PAPER_MANIFEST.sha256')] and
       pending['current_whole_payloads'] == 2244 and pending['current_paper_complete'] is False,
       'original initial PASS binds exactly the two preserved pending control values')
    expected_native = dict(status='PASS_ACTUAL_P210_ARTIFACT_INITIAL_CAPTURE', output=str(INITIAL),
        original_wait_exit_code=0, stdout=result['stdout'], stderr=result['stderr'],
        result=value(INITIAL / 'RESULT.json'), seal=spec['capture_seal'], checks=report['checks'],
        current_path_keys=report['complete_current_key_reconstruction']['complete_keys'], artifact_acceptance=False)
    ck(completed['result']['output'] == json.dumps(expected_native, sort_keys=True) + '\n',
       'entire actual normal-zero parent stdout equals complete original capture summary')
    accepted = obj(QA / 'P210_ARTIFACT_ROOT_ACCEPTANCE.actual.json')
    ck(accepted == spec['root_acceptance_complete_value'] and accepted['root'] == '/root' and
       accepted['schema'] == 'p210-root-initial-artifact-acceptance-v1' and
       accepted['status'] == 'ROOT_ACCEPTED_P210_INITIAL_ARTIFACT_LIFECYCLE_FOLLOWUP_PENDING' and
       accepted['paper'] == 'P210' and accepted['external'] == 'OWNER_AMBER / HOLD_EXTERNAL' and
       accepted['native_session'] == 16560 and accepted['native_exit'] == 0 and
       accepted['root_original_inspection_complete'] is accepted['complete_current_map_reconstructed'] is True and
       accepted['source_fully_read'] is True and accepted['source_reviewed_lines'] == 2344 and
       accepted['initial_gate_checks'] == report['checks'] == 5838453 and
       accepted['current_file_keys'] == report['complete_current_key_reconstruction']['complete_keys'] == 122149 and
       accepted['complete_current_map'] == report['complete_current_key_reconstruction']['canonical_map'] and
       accepted['artifact_raw'] == value(INITIAL / 'ARTIFACT_REPORT.json') and
       accepted['artifact_seal'] == spec['capture_seal'] and
       accepted['root_reception_session'] == 53600 and accepted['root_reception_exit'] == 0 and
       accepted['root_reception_checks'] == 734743 and accepted['root_direct_paths'] == 336 and
       accepted['root_additional_whole_host_content_passes'] == 0 and
       accepted['paper_completion'] is accepted['five_paper_completion'] is False,
       'actual independent root acceptance full exact value and complete original map scope')
    root_completed = obj(QA / 'P210_ARTIFACT_ROOT_READ_COMPLETION.actual.json')
    root_value = spec['root_original_reception_complete_value']
    ck(root_completed['result']['output'] == json.dumps(root_value, sort_keys=True) + '\n' and
       root_value['status'] == 'PASS_ROOT_P210_INITIAL_ARTIFACT_ORIGINALS_AND_COMPLETE_MAP' and
       root_value['complete_current_map'] == accepted['complete_current_map'] and
       root_value['artifact_raw'] == accepted['artifact_raw'] and root_value['artifact_seal'] == accepted['artifact_seal'] and
       root_value['checks'] == accepted['root_reception_checks'] and root_value['current_file_keys'] == 122149,
       'entire actual independent root native original-reception stdout')
    for name, expected in accepted['input_pins'].items():
        exact_old_or_current(name, expected)
    ck(USED_OLD == set(OLD), 'exact two historical triples used, no generic lifecycle alias')
    return report

def preserved_control_evidence(spec):
    preserved = obj(HISTORY / 'PRESERVATION.actual.json')
    before = obj(HISTORY / 'INPUTS_BEFORE.json')
    ck(before == obj(HISTORY / 'INPUTS_AFTER.json') == preserved['complete_input_pins'] and
       set(before) == set(OLD) | {str(QA / 'preserve_p210_precompletion_controls.py'), '/usr/bin/cp', '/usr/bin/cmp'},
       'all five original preservation input fields and stable interval')
    for name, expected in before.items():
        exact_old_or_current(name, expected)
    commands = []
    copies = {}
    for name in ('ROOT_LIFECYCLE.md', 'PAPER_MANIFEST.sha256'):
        original, copy = PAPER / name, HISTORY / name
        copies[str(original)] = dict(physical=str(copy), **OLD[str(original)])
        for argv in (['/usr/bin/cp', '--no-clobber', '--', str(original), str(copy)],
                     ['/usr/bin/cmp', '--', str(original), str(copy)]):
            commands.append(dict(argv=argv, cwd=str(ROOT), environment=ENV, exit_code=0, stdout='', stderr=''))
    ck(preserved == dict(status='PASS_TWO_ACTUAL_P210_PRECOMPLETION_CONTROLS_PRESERVED',
       copies=copies, commands=commands, complete_input_pins=before, inputs_unchanged=True, old_whole_payloads=2244,
       scope='Two exact physical documentary copies only. No live edit, new science/build/view, lifecycle refresh or artifact acceptance.',
       external='OWNER_AMBER / HOLD_EXTERNAL'), 'entire physical preservation receipt and four actual cp/cmp commands')
    ck(raw(HISTORY / 'executed_source.py') == raw(QA / 'preserve_p210_precompletion_controls.py'),
       'complete actual preservation executed-source bytes')
    native = obj(QA / 'P210_PRECOMPLETION_CONTROLS_ROOT.actual.json')
    ck(native['result']['output'] == json.dumps(dict(status=preserved['status'], copies=copies,
       native_commands=commands, payloads=7, seal=spec['preserved_controls_seal']), sort_keys=True) + '\n',
       'entire actual preservation parent stdout and seven-payload seal')

def completion_refresh_evidence(spec, after):
    receipt = obj(QA / 'P210_COMPLETION_LIFECYCLE_REFRESH.actual.json')
    expected = dict(status='PASS_P210_COMPLETION_LIFECYCLE_AND_WHOLE_MANIFEST_REFRESH', old_payloads=2244,
        current_payloads=2244, physical_files=2245, added_files=0, deleted_files=0,
        sole_changed_old_payload='ROOT_LIFECYCLE.md', old_whole_sha256=OLD[str(PAPER / 'PAPER_MANIFEST.sha256')]['sha256'],
        old_lifecycle_sha256=OLD[str(PAPER / 'ROOT_LIFECYCLE.md')]['sha256'],
        new_lifecycle_sha256=spec['current_lifecycle']['sha256'], new_whole_sha256=spec['current_whole_manifest']['sha256'],
        terminal_sha256=value(PAPER / 'qa_final/SHA256SUMS')['sha256'],
        initial_artifact_root_acceptance_sha256=value(QA / 'P210_ARTIFACT_ROOT_ACCEPTANCE.actual.json')['sha256'],
        artifact_raw=value(INITIAL / 'ARTIFACT_REPORT.json'), artifact_seal=value(INITIAL / 'SHA256SUMS'),
        native=dict(argv=['/usr/bin/sha256sum', '--check', 'PAPER_MANIFEST.sha256'], cwd=str(PAPER),
            environment=ENV, exit=0, stdout=''.join(name + ': OK\n' for name in sorted(after)), stderr=''),
        source_sha256=value(QA / 'refresh_p210_completion_whole_manifest.py')['sha256'],
        scope='Mechanical rolling manifest plus documentary lifecycle only; all original/frozen science and qa_final bytes unchanged. No new science/build/view or final artifact/five-paper acceptance.')
    ck(receipt == expected, 'entire actual sole-lifecycle refresh receipt and complete 2244-line native stdout')
    completed = obj(QA / 'P210_COMPLETION_LIFECYCLE_REFRESH_ROOT_COMPLETION.actual.json')
    ck(completed['result']['output'] == json.dumps({key: value for key, value in expected.items() if key != 'native'},
       sort_keys=True, indent=2) + '\n', 'entire actual completion refresh parent stdout')

def lifecycle_transition(binding, initial):
    spec = binding['documentary_transition']
    ck(spec['preserved_controls_path'] == str(HISTORY) and
       spec['current_lifecycle_path'] == str(PAPER / 'ROOT_LIFECYCLE.md') and
       spec['current_whole_manifest_path'] == str(PAPER / 'PAPER_MANIFEST.sha256'),
       'exact actual controls and current document paths')
    package(HISTORY, spec['preserved_controls_seal'], spec['preserved_controls_payloads'])
    ck(spec['preserved_controls_payloads'] == 7, 'exact two-control capture payload scope')
    preserved_control_evidence(spec)
    for original, expected in OLD.items():
        pin(HISTORY / Path(original).name, expected)
    before = rows(HISTORY / 'PAPER_MANIFEST.sha256')
    after = package(PAPER, spec['current_whole_manifest'], 2244, 'PAPER_MANIFEST.sha256')
    ck(len(before) == 2244 and set(before) == set(after) and
       before['ROOT_LIFECYCLE.md'] == OLD[str(PAPER / 'ROOT_LIFECYCLE.md')]['sha256'] and
       {name for name in before if before[name] != after[name]} == {'ROOT_LIFECYCLE.md'} and
       after['ROOT_LIFECYCLE.md'] == spec['current_lifecycle']['sha256'],
       'entire 2244-member whole manifest changes only one lifecycle row')
    pin(PAPER / 'ROOT_LIFECYCLE.md', spec['current_lifecycle'])
    completion_refresh_evidence(spec, after)
    ck(initial['actual_terminal_reused']['output_payloads'] == 222,
       'accepted original terminal scope remains two builds and 222 payloads')
    old_body = raw(HISTORY / 'ROOT_LIFECYCLE.md').decode()
    body = raw(PAPER / 'ROOT_LIFECYCLE.md').decode()
    ck('ARTIFACT_GATE_PENDING' in old_body and
       body.split('\n\n', 2)[1] == spec['exact_current_status_paragraph'] and
       'HOLD_EXTERNAL' in body and all(token in body for token in spec['required_current_lifecycle_tokens']),
       'actual current completion-lifecycle wording and unchanged external hold')
    links = []
    for source in (PAPER / 'ROOT_LIFECYCLE.md', QA / 'P210_ARTIFACT_ROOT_INSPECTION.md'):
        for href in stripped_links(raw(source).decode()):
            relative = href.strip().strip('<>').split('#', 1)[0]
            if not relative or re.match(r'[A-Za-z][A-Za-z0-9+.-]*:', relative):
                continue
            target = (source.parent / unquote(relative)).resolve()
            ck(target.is_relative_to(ROOT) and target.is_file(), 'genuine bounded local documentary link', href)
            links.append(dict(document=str(source), href=href, path=str(target), pin=pin(target)))
    ck(set(spec['required_lifecycle_link_targets']) <=
       {row['path'] for row in links if row['document'] == str(PAPER / 'ROOT_LIFECYCLE.md')} and
       {str(QA / 'P210_ARTIFACT_ROOT_ACCEPTANCE.actual.json'),
        str(QA / 'P210_ARTIFACT_ROOT_INSPECTION.md'), str(HISTORY / 'README.md')} <=
       set(spec['required_lifecycle_link_targets']), 'genuine current links include actual acceptance and physical prior controls')
    return dict(old_lifecycle=OLD[str(PAPER / 'ROOT_LIFECYCLE.md')],
        old_whole_manifest=OLD[str(PAPER / 'PAPER_MANIFEST.sha256')],
        current_lifecycle=spec['current_lifecycle'], current_whole_manifest=spec['current_whole_manifest'],
        old_payloads=len(before), current_payloads=len(after), physical_files=len(after) + 1,
        changed_payloads=['ROOT_LIFECYCLE.md'], genuine_documentary_links=links)

def main():
    ck(len(sys.argv) == 3 and sys.argv[1] == '--expected-preparation-sha256' and
       re.fullmatch('[0-9a-f]{64}', sys.argv[2]) is not None, 'explicit actual root-reviewed followup seal')
    runtime = current_runtime()
    preparation = rows(PREP / 'SHA256SUMS')
    package(PREP, sys.argv[2], len(preparation))
    binding = obj(PREP / 'ACTUAL_BINDING.json')
    ck(binding['schema'] == 'p210-document-only-lifecycle-actual-binding-v1' and
       binding['paper'] == 'P210' and binding['root_acceptance'] is False and
       binding['scope'] == 'ACTUAL_INITIAL_ARTIFACT_ROOT_ACCEPTED_AND_TWO_CONTROLS_PRESERVED_SOLE_LIFECYCLE_REFRESH',
       'actual post-artifact document-only input binding')
    all_actual_native_closures(binding)
    initial = initial_capture(binding)
    for name, expected in binding['named_current_input_pins'].items():
        pin(name, expected)
    transition = lifecycle_transition(binding, initial)
    # Only explicitly read documentary/scientific package bytes are rehashed.
    # No old full host map, resource scope or configuration is scanned here.
    before = dict(SEEN)
    for name, expected in sorted(before.items()):
        pin(name, expected, force=True)
    for name, expected in PACKAGES.items():
        ck(physical(Path(name)) == expected, 'final complete named-package membership remains identical', name)
    ck(before == SEEN and runtime == current_runtime(), 'all explicitly read current keys and invocation stable')
    report = dict(schema='p210-document-only-lifecycle-followup-v1',
        status='PASS_P210_DOCUMENT_ONLY_LIFECYCLE_FOLLOWUP_ROOT_ACCEPTANCE_PENDING',
        paper='P210', checks=sum(CHECKS.values()), checks_by_kind=dict(CHECKS),
        initial_artifact_raw=value(INITIAL / 'ARTIFACT_REPORT.json'),
        initial_artifact_complete_key_recipe_reference=dict(path=str(INITIAL / 'ARTIFACT_REPORT.json'),
            pin=value(INITIAL / 'ARTIFACT_REPORT.json'), selector=['complete_current_key_reconstruction']),
        exact_two_historical_control_roles=[dict(original_path=name, **OLD[name],
            physical_path=str(HISTORY / Path(name).name)) for name in sorted(OLD)],
        document_only_transition=transition, current_documentary_runtime=runtime,
        complete_current_read_keys=before, current_path_keys=len(before),
        old_programs_imported_or_executed=0, reader_file_writes=0,
        new_scientific_runs=0, new_builds=0, new_views=0, new_manuscript_reviews=0,
        host_dependency_tree_walks=0, root_acceptance=False, paper_completion=False,
        five_paper_completion=False, external='OWNER_AMBER / HOLD_EXTERNAL',
        limitations=['Only the actual rolling lifecycle/whole transition is newly checked.',
            'The initial accepted scientific/build/view evidence is unchanged within all 2244 paper payloads.',
            'No new full current-host dependency gate is claimed; the exact-five gate must still check its entire scope.',
            'Historical failures and all source, tracing and ownership limitations remain.'])
    print(json.dumps(report, sort_keys=True, separators=(',', ':'), ensure_ascii=True))

if __name__ == '__main__':
    try:
        main()
    except BaseException:
        print(json.dumps(dict(status='FAIL_P210_LIFECYCLE_FOLLOWUP_NO_ACCEPTANCE',
            checks_completed=sum(CHECKS.values()), traceback=traceback.format_exc(),
            reader_file_writes=0, new_scientific_runs=0, new_builds=0, new_views=0,
            root_acceptance=False, paper_completion=False, five_paper_completion=False), sort_keys=True))
        raise SystemExit(1)
