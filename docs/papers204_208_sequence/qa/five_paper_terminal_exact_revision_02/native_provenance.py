#!/usr/bin/env python3
"""Source-fixed original native gates; no old program is imported or executed.

verify is called by the actual exact-five driver before package reception.
Only archived native metadata is read until all three owned captures close.
binding does not select paths, commands or statuses: these are fixed below.
"""
from hashlib import sha256
import json
import math
from pathlib import Path
import shlex

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
QA = ROOT / 'docs/papers204_208_sequence/qa'
PAPER = ROOT / 'papers/210-weakly-increasing-run-aggregation'
ENV = {'PATH': '/usr/bin:/bin', 'LANG': 'C.UTF-8', 'LC_ALL': 'C.UTF-8', 'TZ': 'UTC'}
PY = ['/usr/bin/python3.10', '-I', '-S', '-B']
ENV_ARGV = ['/usr/bin/env', '-i', *[k + '=' + v for k, v in ENV.items()]]
FOUR = QA / 'five_paper_terminal_component_run_02'
FOUR_PREP = QA / 'five_paper_terminal_gate_revision_01'
LAUNCH_PREP = QA / 'five_paper_terminal_component_launch_revision_01'
LAUNCH_SEAL = 'd86a67b5b2fd43230b4259090bb3df8a8d5a39c19fbe849ba4326682d253f9d2'
FOUR_SEAL = '3863616519c14cc2f70d92deced93d745978a34f7e90f78aed5f00dd12ca8238'
FOUR_BINDING = 'b722f61ae2abcc4220a99473b6d9bb104962b52ea509c258f976c0136d08affd'
FOUR_OUTPUT = '7eda9f4c4452d3d1dc0656ca592cef8e7783a120ccada3fd671cc2238aaf6ebe'
FOUR_STATUS = 'PASS_NATIVE_FOUR_COMPLETED_COMPONENT_NOT_FIVE_PAPER_ACCEPTANCE'
CHILD_STATUS = 'FOUR_COMPLETED_COMPONENT_PASS_P210_NOT_ASSESSED_NOT_FIVE_PAPER_PASS'
# prefix, session, raw completion bytes, SHA256 of complete original output.
NATIVES = (
 ('FIVE_FOUR_COMPONENT_RUN02_ROOT', 21492, 1030, 'd11f4a57d57c687c35c151c9c8ac5c3403ef5c70998626d33a06eb8845e9001b'),
 ('FIVE_FOUR_COMPONENT02_ORIGINALS_ROOT', 45261, 29822, '4f4e4f8bb40707a50d091baf4756516bd7cd33fc028844b96940b4fb264dc807'),
 ('P210_ARTIFACT03_ROOT', 16560, 686, '55ea53528c87d12e86b6519218f3f362c5227239d18a6cf7ddd4c8a86120b017'),
 ('P210_ARTIFACT_ROOT_READ', 53600, 1321, 'c13430f65214c55b968063e86cc17dcfa7e968df10cefd8e7bb416329427779b'),
 ('P210_LIFECYCLE01_ROOT', 5316, 685, '701e169962d67425c9078f9b2f8c42e834168ee5cc694a61a29e8c4a9b9509ec'),
 ('P210_LIFECYCLE_ROOT_READ', 93071, 763, '6e21b53cf1a356463f30f3627d21141b77bba66e51bca6425aba97878496ca56'))
# capture/preparation/recorder/reader/seal/timeout/report/checks/keys/output seal.
P210 = (
 ('p210_terminal_artifact_03', 'p210_terminal_artifact_revision_03', 'record_p210_artifact_03.py',
  'inspect_p210_artifact.py', '8efef29aee07210eee9ec95a1d3df51d4539f33d3189991cd1b42a98a508d3dd',
  1800, 'ARTIFACT_REPORT.json', 5838453, 122149, '0fc403270819cdb74c1d14a2aac39169af7ee7029e3c85a9f5f25aa082e11c7c'),
 ('p210_terminal_lifecycle_01', 'p210_terminal_lifecycle_preparation', 'record_p210_lifecycle_01.py',
  'inspect_p210_lifecycle.py', '0745224b3f793ac4fe7a68ebc5c66a68e2649a7fb475b8deaf70ecd3bfdb4714',
  600, 'LIFECYCLE_REPORT.json', 28659, 2319, '9e6cd4cb8b56eeeb1aa39f34c63b43375e39013a66421c2cc7b00d54c01b90e4'))


def verify(driver, binding):
    need, obj, raw, pin, byte_pin = driver.need, driver.obj, driver.raw, driver.pin, driver.byte_pin
    def rich(row):
        return dict(real=row['resolved'], sha256=row['sha256'], size=row['bytes'], symlink=row['symlink'])
    def encoded(value):
        return (json.dumps(value, sort_keys=True) + '\n').encode()
    def transport(value, running):
        need(set(value) == {'chunk_id', 'wall_time_seconds', 'original_token_count', 'output',
                           'session_id' if running else 'exit_code'}, 'complete untruncated native transport schema')
        need(type(value['wall_time_seconds']) in (int, float) and math.isfinite(value['wall_time_seconds']) and
             value['wall_time_seconds'] >= 0 and type(value['original_token_count']) is int and
             value['original_token_count'] >= 0 and type(value['output']) is str and
             type(value['chunk_id']) is str and value['chunk_id'], 'native wall/token/output metadata')
    parent_argv = PY + ['-X', 'pycache_prefix=' + str(FOUR / 'unused_launcher_cache'),
                        str(LAUNCH_PREP / 'launcher.py'), 'launch-four-completed-component', LAUNCH_SEAL]
    commands = [ENV_ARGV + parent_argv, ENV_ARGV + PY + ['-X',
        'pycache_prefix=' + str(QA / 'four_component02_receiver_unused_cache'), str(QA / 'receive_four_component02.py')]]
    for spec, kind in zip(P210, ('artifact', 'lifecycle')):
        commands.extend((PY + [str(QA / spec[2]), '--expected-' + kind + '-preparation-sha256', spec[4]],
                         PY + [str(QA / ('receive_p210_initial_artifact.py' if kind == 'artifact' else 'receive_p210_lifecycle.py'))]))
    completed = []
    for (prefix, session, size, digest), command in zip(NATIVES, commands):
        launch_name = prefix + '_LAUNCH.actual.json'
        launch, completion = obj(QA / launch_name), obj(QA / (prefix + '_COMPLETION.actual.json'))
        transport(launch['result'], True); transport(completion['result'], False)
        need(launch['cwd'] == str(ROOT) and shlex.split(launch['command']) == command and
             launch['result']['session_id'] == completion['session_id'] == session and
             launch['result']['output'] == '' and completion['launch_record'] == launch_name and
             type(completion['result']['exit_code']) is int and completion['result']['exit_code'] == 0,
             'source-fixed actual native launch and normal completion', prefix)
        body = completion['result']['output'].encode()
        need(len(body) == size and sha256(body).hexdigest() == digest,
             'entire original native stdout bytes, not parsed-subset equality', prefix)
        completed.append(completion)
    progress_name = 'FIVE_FOUR_COMPONENT_RUN02_ROOT_PROGRESS01.actual.json'
    progress = obj(QA / progress_name); transport(progress['result'], True)
    need(progress['launch_record'] == completed[0]['launch_record'] and
         progress['session_id'] == progress['result']['session_id'] == 21492 and
         completed[0]['prior_progress_records'] == [progress_name], 'entire four segmented native chain')
    event_bytes = (progress['result']['output'] + completed[0]['result']['output']).encode()
    events = [json.loads(line) for line in event_bytes.splitlines()]
    need(len(events) == 7 and b''.join(encoded(e) for e in events) == event_bytes,
         'six original heartbeat lines followed by complete final JSON')
    received = [None] + [json.loads(x['result']['output']) for x in completed[1:]]
    receipt, native, attempt, spawn = (obj(FOUR / n) for n in
        ('RECEIPT.json', 'NATIVE_RESULT.json', 'PRE_SPAWN_ATTEMPT.json', 'SPAWNED.json'))
    child_argv = PY + ['-X', 'pycache_prefix=' + str(FOUR / 'unused_checker_cache'),
        str(FOUR_PREP / 'four_completed.py'), '--expected-preparation-sha256', FOUR_SEAL,
        '--reuse-root-binding', str(FOUR_PREP / 'ROOT_REUSE_BINDING.json'), '--reuse-root-binding-sha256', FOUR_BINDING]
    expected = dict(argv=child_argv, cwd=str(ROOT), env=ENV, stdin='DEVNULL', stdout='checker.stdout',
                    stderr='checker.stderr', start_new_session=True, timeout_seconds=600, heartbeat_seconds=30)
    need(set(native) == set(expected) | {'exit', 'outcome', 'cleanup', 'heartbeats', 'started_epoch',
         'finished_epoch', 'process_group_settled', 'spawn_attempted', 'pid', 'process_group'} and
         all(native[k] == v for k, v in expected.items()) and
         attempt == dict(expected, exit=None, outcome='NOT_STARTED', cleanup=[], heartbeats=[],
                         started_epoch=native['started_epoch']), 'entire four child original pre-spawn context')
    need(type(native['exit']) is int and native['exit'] == 0 and native['outcome'] == 'COMPLETED' and
         native['process_group_settled'] is native['spawn_attempted'] is True and
         spawn['pid'] == spawn['process_group'] == native['pid'] == native['process_group'] == 770811 and
         spawn['argv'] == child_argv and spawn['start_new_session'] is True and
         native['started_epoch'] <= spawn['epoch'] <= native['finished_epoch'], 'four actual completed owned child')
    cleanup = native['cleanup']
    need(len(cleanup) == 1 and cleanup[0] == dict(epoch=cleanup[0]['epoch'], error=None,
         owned_process_group=770811, probe='killpg(pid,0)', state='ABSENT') and
         spawn['epoch'] <= cleanup[0]['epoch'] <= native['finished_epoch'], 'four absent group without cleanup signal')
    need(events[:-1] == native['heartbeats'] and all(e['pid'] == 770811 and
         e['status'] == 'FOUR_COMPONENT_NATIVE_RUNNING' and native['started_epoch'] <= e['epoch'] <= native['finished_epoch']
         for e in native['heartbeats']) and all(a['epoch'] < b['epoch'] for a, b in zip(events[:5], events[1:6])),
         'all six original heartbeats and ordered owned-child chronology')
    launcher = obj(FOUR / 'LAUNCHER_ATTEMPT.json')
    need(launcher['orig_argv'] == parent_argv and launcher['cwd'] == str(ROOT) and launcher['env'] == ENV and
         launcher['output'] == str(FOUR) and launcher['expected_launcher_preparation_sha256'] == LAUNCH_SEAL and
         launcher['checker_preparation_sha256'] == FOUR_SEAL and launcher['epoch'] <= native['started_epoch'], 'four parent invocation')
    need(receipt['native'] == native and receipt['status'] == FOUR_STATUS and receipt['failures'] == [] and
         receipt['checker_json_status'] == CHILD_STATUS and receipt['complete_checker_json'] == 'checker.stdout' and
         all(receipt[n] is True for n in ('known_inputs_unchanged', 'runtime_membership_unchanged',
             'scoped_inputs_unchanged', 'configuration_unchanged')), 'four complete settled receipt')
    captures = []
    for spec in P210:
        out, prep, source = QA / spec[0], QA / spec[1], QA / spec[2]
        result, attempt, spawn = (obj(out / n) for n in ('RESULT.json', 'ATTEMPT.json', 'SPAWN.json'))
        argv = PY + ['-X', 'pycache_prefix=' + str(out / 'never_created_reader_cache'),
                     str(prep / spec[3]), '--expected-preparation-sha256', spec[4]]
        need(set(result) == {'argv', 'cwd', 'environment', 'pid', 'original_wait_exit_code', 'cleanup_wait_exit_code',
             'timed_out', 'wait_error', 'cleanup_events', 'child_reaped', 'process_group_absent', 'inputs_before',
             'inputs_after', 'inputs_unchanged', 'stdout', 'stderr', 'paper_terminal_present_after', 'finished_epoch'} and
             type(result['original_wait_exit_code']) is type(result['cleanup_wait_exit_code']) is int and
             result['original_wait_exit_code'] == result['cleanup_wait_exit_code'] == 0 and
             result['timed_out'] is False and result['wait_error'] is None and result['cleanup_events'] == [] and
             result['child_reaped'] is result['process_group_absent'] is result['inputs_unchanged'] is
             result['paper_terminal_present_after'] is True, 'P210 original normal wait, not cleanup success', str(out))
        need(result['argv'] == argv and result['cwd'] == str(ROOT) and result['environment'] == ENV and
             result['inputs_before'] == result['inputs_after'] and len(result['inputs_before']) == 11 and
             attempt == dict(argv=argv, cwd=str(ROOT), environment=ENV, inputs_before=result['inputs_before'],
                 timeout_seconds=spec[5], start_new_session=True, started_epoch=attempt['started_epoch'], paper_terminal_present_before=True) and
             spawn == dict(pid=result['pid'], process_group_id=result['pid'], spawned_epoch=spawn['spawned_epoch']) and
             type(result['pid']) is int and result['pid'] > 0 and
             attempt['started_epoch'] <= spawn['spawned_epoch'] <= result['finished_epoch'], 'complete P210 recorder invocation and interval')
        inputs = {source, prep / spec[3], prep / 'ACTUAL_BINDING.json', prep / 'SHA256SUMS',
                  PAPER / 'qa_final/SHA256SUMS', PAPER / 'ROOT_LIFECYCLE.md', PAPER / 'PAPER_MANIFEST.sha256', Path(PY[0])}
        inputs.update((QA / 'p210_terminal_launch_02/SHA256SUMS', QA / 'P210_TERMINAL_ROOT_ACCEPTANCE.actual.json',
                       QA / 'p210_terminal_root_reception_01/ROOT_RECEPTION.json') if spec == P210[0] else
                      (QA / 'p210_terminal_artifact_03/SHA256SUMS', QA / 'P210_ARTIFACT_ROOT_ACCEPTANCE.actual.json',
                       QA / 'p210_terminal_artifact_03/ARTIFACT_REPORT.json'))
        need(set(result['inputs_before']) == set(map(str, inputs)), 'all eleven source-defined recorder inputs')
        captures.append((spec, out, prep, source, result))
    # ALL SIX natives and ALL THREE captures closed above. Full payload reception starts here.
    need(len(driver.manifest(FOUR, expected=FOUR_OUTPUT)) == 20, 'four complete physical capture package')
    need(raw(FOUR / 'executed_four_completed.py') == raw(FOUR_PREP / 'four_completed.py') and
         raw(FOUR / 'executed_launcher.py') == raw(LAUNCH_PREP / 'launcher.py'), 'four complete actual executed sources')
    for stem, suffix in (('SCOPED_INPUTS', '.json'), ('KNOWN_INPUTS', '.json.gz')):
        need(obj(FOUR / (stem + '_BEFORE' + suffix)) == obj(FOUR / (stem + '_AFTER' + suffix)) and
             raw(FOUR / (stem + '_BEFORE' + suffix)) == raw(FOUR / (stem + '_AFTER' + suffix)),
             'four complete original input interval bytes', stem)
    for name, value in receipt['streams'].items():
        pin(FOUR / name, rich(value))
    need(raw(FOUR / 'checker.stderr') == b'' and events[-1] == dict(checker_exit=0,
         checker_json_status=CHILD_STATUS, output=str(FOUR), output_seal=dict(manifest={
         **byte_pin(FOUR / 'SHA256SUMS'), 'resolved': str(FOUR / 'SHA256SUMS'), 'symlink': None}, payloads=20),
         status=FOUR_STATUS), 'four complete final native receipt and separate empty stderr')
    child = obj(FOUR / 'checker.stdout')
    need(received[1]['status'] == 'PASS_ROOT_FOUR_COMPONENT02_ORIGINAL_RECEPTION_NOT_FIVE_PAPER_ACCEPTANCE' and
         received[1]['actual_child_result'] == child and child['status'] == CHILD_STATUS and
         received[1]['actual_outer_session'] == 21492 and received[1]['actual_outer_exit'] == received[1]['actual_child_exit'] == 0,
         'actual four receiver bound to entire captured child')
    reports = []
    for index, (spec, out, prep, source, result) in enumerate(captures):
        need(len(driver.manifest(out, expected=spec[9])) == 6, 'complete six-payload P210 capture')
        for name, expected in result['inputs_before'].items():
            if index == 0 and name in {str(PAPER / n) for n in ('ROOT_LIFECYCLE.md', 'PAPER_MANIFEST.sha256')}:
                driver.historical_byte_pin(name, expected)
            else:
                pin(name, expected)
        need(raw(out / 'executed_source.py') == raw(source) and raw(out / 'stderr') == b'' and
             byte_pin(out / spec[6]) == result['stdout'] and byte_pin(out / 'stderr') == result['stderr'],
             'complete original recorder source and separate settled raw streams')
        report = obj(out / spec[6]); reports.append(report)
        need(raw(out / spec[6]) == (json.dumps(report, sort_keys=True, separators=(',', ':'), ensure_ascii=True) + '\n').encode() and
             report['checks'] == sum(report['checks_by_kind'].values()) == spec[7], 'entire canonical P210 raw report')
        kind, capture_status, report_status = ('artifact', 'PASS_ACTUAL_P210_ARTIFACT_INITIAL_CAPTURE',
             'PASS_P210_TERMINAL_ARTIFACT_INITIAL_LIFECYCLE_FOLLOWUP_PENDING') if index == 0 else ('lifecycle',
             'PASS_ACTUAL_P210_LIFECYCLE_FOLLOWUP_CAPTURE', 'PASS_P210_DOCUMENT_ONLY_LIFECYCLE_FOLLOWUP_ROOT_ACCEPTANCE_PENDING')
        summary = dict(status=capture_status, output=str(out), original_wait_exit_code=0, stdout=result['stdout'],
            stderr=result['stderr'], result=byte_pin(out / 'RESULT.json'), seal=byte_pin(out / 'SHA256SUMS'),
            checks=spec[7], current_path_keys=spec[8], **{kind + '_acceptance': False})
        need(completed[2 + 2 * index]['result']['output'].encode() == encoded(summary) and report['status'] == report_status and
             report['paper'] == 'P210' and report['external'] == 'OWNER_AMBER / HOLD_EXTERNAL' and
             report['root_acceptance'] is report['paper_completion'] is report['five_paper_completion'] is False and
             all(type(report[n]) is int and report[n] == 0 for n in ('new_scientific_runs', 'new_builds', 'new_views',
                 'new_manuscript_reviews', 'reader_file_writes', 'old_programs_imported_or_executed')), 'whole P210 native capture summary and bounded scope')
    for index, (kind, session, receiver_session, accept_sha) in enumerate((
        ('ARTIFACT', 16560, 53600, '8bce9e544454a4330469fa420141dad2a3abf8bd6de4f453c7c772b01bd146c8'),
        ('LIFECYCLE', 5316, 93071, '0abe8d585c350df13824fe599947217c288cc2eb0da582300a3ad795b32a356a'))):
        path = QA / ('P210_' + kind + '_ROOT_ACCEPTANCE.actual.json'); pin(path, accept_sha)
        acceptance, receiver = obj(path), received[3 + 2 * index]
        status = 'PASS_ROOT_P210_INITIAL_ARTIFACT_ORIGINALS_AND_COMPLETE_MAP' if index == 0 else 'PASS_ROOT_P210_LIFECYCLE_ORIGINAL_RECEPTION'
        field = 'actual' if index == 0 else 'original'
        need(receiver['status'] == status and receiver[field + '_native_session'] == session and receiver[field + '_native_exit'] == 0 and
             acceptance['native_session'] == session and acceptance['root_reception_session'] == receiver_session and
             acceptance['native_exit'] == acceptance['root_reception_exit'] == 0 and
             acceptance['root_reception_checks'] == receiver['checks'] and acceptance['root_original_inspection_complete'] is True and
             acceptance['paper_completion'] is bool(index) and acceptance['five_paper_completion'] is False and
             acceptance[kind.lower() + '_raw'] == receiver[kind.lower() + '_raw'] == captures[index][4]['stdout'] and
             acceptance[kind.lower() + '_seal'] == receiver[kind.lower() + '_seal'] == byte_pin(captures[index][1] / 'SHA256SUMS'),
             'actual separate P210 root acceptance and original receiver byte binding')
    return dict(native_sessions=[row[1] for row in NATIVES], normal_native_completions=6,
        settled_owned_captures=3, four_original_heartbeats=6, separate_empty_capture_stderr=3,
        native_closure_before_package_reception=True,
        original_receivers=[dict(path=str(QA / (NATIVES[i][0] + '_COMPLETION.actual.json')),
            pin=byte_pin(QA / (NATIVES[i][0] + '_COMPLETION.actual.json')), selector=['result', 'output'],
            status=received[i]['status']) for i in (1, 3, 5)],
        four_child=dict(path=str(FOUR / 'checker.stdout'), pin=byte_pin(FOUR / 'checker.stdout'), status=child['status']),
        p210_captures=[dict(path=str(out / spec[6]), pin=byte_pin(out / spec[6]), checks=spec[7],
            current_path_keys=spec[8], status=report['status'], payloads=6,
            seal=byte_pin(out / 'SHA256SUMS')) for (spec, out, prep, source, result), report in zip(captures, reports)],
        lifecycle_root_acceptance=dict(path=str(path), pin=byte_pin(path), status=acceptance['status'],
                                      paper_completion=True, five_paper_completion=False))
