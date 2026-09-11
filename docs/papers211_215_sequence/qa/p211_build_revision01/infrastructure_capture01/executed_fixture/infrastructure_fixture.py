#!/usr/bin/env python3
"""BLD-I1 infrastructure fixture: audit-hook refusal and one ordinary child.

No TeX/science, explicit fork, escaped writer or unkillable-process exercise.
The refusal subtree remains UNCLOSED. Only the enclosing fixture process is
known settled; a documentary package snapshot is not a native subtree seal.
"""
import argparse
import json
import os
from pathlib import Path
import sys
import traceback

HERE = Path(__file__).resolve().parent
exec(compile((HERE / 'build_core.py').read_bytes(), str(HERE / 'build_core.py'), 'exec'))


class AuditHookBeforeHandle(BaseException):
    pass


def exercise(out):
    require(out.parent.parent == PREP and out.name == 'cases' and
            out.parent.name.startswith('infrastructure_capture') and
            out.resolve() == out and not os.path.lexists(out), 'New owned fixture cases')
    out.mkdir()
    unknown = out / 'unknown_launch'
    unknown.mkdir()
    deny = {'active': True, 'events': 0}
    child_argv = [str(PYTHON), '-I', '-S', '-B', '-c',
                  "import os; os.write(1, b'known stdout\\n'); os.write(2, b'known stderr\\n')"]

    def hook(event, args):
        if event == 'subprocess.Popen' and deny['active']:
            deny['events'] += 1
            require(args[0] == str(PYTHON) and args[1] == child_argv and
                    args[3] == ENV8, 'Exact controlled Popen audit event')
            write_new(unknown / 'AUDIT_EVENT.json', {
                'event': event, 'executable': args[0], 'argv': args[1],
                'cwd': str(args[2]), 'environment': args[3],
                'action': 'RAISE_BASEEXCEPTION_BEFORE_POPEN_HANDLE_RETURN',
                'fixture_scope': 'Controlled audit hook; no explicit fork or escaped-writer test.'})
            raise AuditHookBeforeHandle('BLD-I1 controlled refusal at subprocess.Popen audit event')

    sys.addaudithook(hook)
    try:
        run_native(unknown, 'refused_before_handle', child_argv, out, timeout=20)
    except RuntimeError as error:
        require('UNCLOSED_NATIVE_STREAMS' in str(error), 'Expected unknown outcome refusal')
        refusal = str(error)
    else:
        raise AssertionError('No-handle exception obtained a finalized receipt')
    finally:
        deny['active'] = False
    work = unknown / 'commands/refused_before_handle'
    unclosed = json.loads((work / 'UNCLOSED.json').read_bytes())
    require(deny['events'] == 1 and (work / 'ATTEMPT.json').is_file(), 'Actual refusal attempt/event')
    require(unclosed['native_handle_received'] is False and
            unclosed['launch_outcome'] == 'UNKNOWN_NO_NATIVE_HANDLE' and
            unclosed['wrapper_reason'] == 'NO_NATIVE_HANDLE_UNKNOWN_LAUNCH' and
            unclosed['native_exit_code'] is None and unclosed['streams_settled'] is False and
            'AuditHookBeforeHandle' in unclosed['error'] and 'streams' not in unclosed,
            'No-handle outcome must remain explicitly unknown and unfinalized')
    require(not (work / 'RECEIPT.json').exists() and not (work / 'SPAWNED.json').exists() and
            not (work / 'INPUTS_AFTER.json').exists(), 'Unknown attempt must not finalize')
    require(incomplete_native(unknown) == [str(work)], 'Incomplete attempt guard')
    try:
        seal(unknown)
    except RuntimeError as error:
        require('Unsettled subtree prevents seal' in str(error), 'Expected native seal refusal')
        native_seal_refusal = str(error)
    else:
        raise AssertionError('Unknown subtree obtained a native seal')
    require(not (unknown / 'SHA256SUMS').exists(), 'No unknown native subtree manifest')

    known = out / 'known_settlement'
    known.mkdir()
    row, raw = run_native(known, 'ordinary_stdout_stderr', child_argv, out, timeout=20)
    require(row['successful'] and row['native_handle_received'] and
            row['launch_outcome'] == 'KNOWN_NATIVE_HANDLE' and
            row['native_exit_code'] == 0 and row['wrapper_reason'] == 'NATIVE_EXIT' and
            row['streams_settled'] and row['remaining_session_members'] == [] and
            row['owned_session_interventions'] == [] and raw == b'known stdout\n',
            'Ordinary known-handle positive path')
    known_work = known / 'commands/ordinary_stdout_stderr'
    require((known_work / 'stderr.raw').read_bytes() == b'known stderr\n' and
            row['streams']['stdout.raw'] == pin(known_work / 'stdout.raw') and
            row['streams']['stderr.raw'] == pin(known_work / 'stderr.raw'), 'Actual known raw streams')
    require(incomplete_native(known) == [], 'Known path complete')
    write_new(known / 'RESULT.json', {'status': 'KNOWN_HANDLE_ORDINARY_STREAMS_SETTLED',
              'native': row, 'tex_compilations': 0, 'scientific_executions': 0})
    known_seal = seal(known)
    # This models the production parent/subtree check, not just a local
    # marker check. The known sibling does not discharge the unknown child.
    require(incomplete_native(out) == [str(work)] and list(out.rglob('UNCLOSED.json')),
            'Unknown child must survive parent incomplete/UNCLOSED check')
    try:
        seal(out)
    except RuntimeError as error:
        require('Unsettled subtree prevents seal' in str(error), 'Parent native seal refusal')
        parent_seal_refusal = str(error)
    else:
        raise AssertionError('Parent bypassed unknown native child')
    write_new(out / 'RESULT.json', {
        'status': 'EXPECTED_UNKNOWN_REFUSAL_AND_KNOWN_HANDLE_FIXTURES_PASS',
        'refusal_error': refusal, 'unknown_native_seal_refused': native_seal_refusal,
        'parent_native_seal_refused': parent_seal_refusal, 'known_seal': known_seal,
        'unknown_subtree_state': 'UNCLOSED_UNCHANGED_NO_RECEIPT_NO_FINAL_STREAM_PINS',
        'positive_path': 'One ordinary stdout/stderr child, native exit 0, no intervention.',
        'controlled_audit_events': deny['events'], 'native_children_created_by_refused_call': 0,
        'interpretation': 'Controlled CPython audit event raises before native creation; recorder conservatively stays UNKNOWN.',
        'tex_compilations': 0, 'scientific_executions': 0, 'build_acceptance': False,
        'limitations': ['Not escaped, detached, unkillable or unknown-writer settlement testing.',
                       'Passing assertions do not close the intentionally UNCLOSED native subtree.']})
    print((out / 'RESULT.json').read_text(), end='')
    return 0


def capture(out):
    require(out.parent == PREP and re.fullmatch(r'infrastructure_capture[0-9]+', out.name) and
            out.resolve() == out and not os.path.lexists(out), 'New owned fixture capture')
    require(dict(os.environ) == ENV8 and sys.flags.isolated and sys.flags.no_site and
            sys.dont_write_bytecode and not sys.flags.optimize, 'Exact fixture ENV8/flags')
    out.mkdir()
    source_names = ('build_core.py', 'infrastructure_fixture.py')
    before = {name: pin(HERE / name) for name in source_names}
    write_new(out / 'SOURCES_BEFORE.json', before)
    executed = out / 'executed_fixture'
    executed.mkdir()
    for name in source_names:
        write_new(executed / name, (HERE / name).read_bytes())
        require(pin(executed / name) == before[name], 'Exact executed fixture source snapshot')
    write_new(out / 'ENTERED.json', {'mode': 'PURE_INFRASTRUCTURE_NO_BUILD',
              'argv': sys.orig_argv, 'environment': dict(os.environ), 'cwd': str(Path.cwd()),
              'product_native_context': 'ACTUAL_ROOT_TOOL_SESSION_COMPLETION_REQUIRED'})
    child = [str(PYTHON), '-I', '-S', '-B', str(HERE / 'infrastructure_fixture.py'),
             '--exercise', str(out / 'cases')]
    row, raw = run_native(out, 'fixture_process', child, ROOT,
                          [HERE / name for name in source_names], timeout=60)
    require(row['successful'] and row['streams_settled'] and
            row['remaining_session_members'] == [] and row['owned_session_interventions'] == [],
            'Actual fixture process must complete and owned session be quiescent')
    after = {name: pin(HERE / name) for name in source_names}
    write_new(out / 'SOURCES_AFTER.json', after)
    require(after == before, 'Fixture source before/after closure')
    fixture = json.loads((out / 'cases/RESULT.json').read_bytes())
    require(fixture['status'] == 'EXPECTED_UNKNOWN_REFUSAL_AND_KNOWN_HANDLE_FIXTURES_PASS',
            'Expected actual fixture assertions')
    pending = incomplete_native(out)
    require(len(pending) == 1 and pending[0].endswith('/refused_before_handle'),
            'Intentional unknown attempt retained under capture parent')
    try:
        seal(out)
    except RuntimeError as error:
        require('Unsettled subtree prevents seal' in str(error), 'Capture native seal refusal')
        refusal = str(error)
    else:
        raise AssertionError('Capture parent obtained native seal across UNKNOWN child')
    result = {'status': 'FIXTURE_PROCESS_SETTLED_DOCUMENTARY_SNAPSHOT_PERMITTED',
              'native_fixture_process': row, 'source_before_after_equal': True,
              'unknown_native_attempts': pending, 'capture_native_seal_refusal': refusal,
              'native_subtree_acceptance': False, 'build_acceptance': False,
              'tex_compilations': 0, 'scientific_executions': 0,
              'documentary_scope': 'After actual fixture-process completion and owned-session quiescence only; not a native seal of the refused subtree.'}
    write_new(out / 'RESULT.json', result)
    print(json.dumps(result, sort_keys=True))
    return 0


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    choice = parser.add_mutually_exclusive_group(required=True)
    choice.add_argument('--capture', type=Path)
    choice.add_argument('--exercise', type=Path)
    args = parser.parse_args()
    raise SystemExit(capture(args.capture) if args.capture is not None else exercise(args.exercise))
