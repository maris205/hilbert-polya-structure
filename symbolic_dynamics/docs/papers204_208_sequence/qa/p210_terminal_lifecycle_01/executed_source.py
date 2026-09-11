#!/usr/bin/env python3
"""Root-owned raw recorder for the P210 document-only lifecycle follow-up reader.

Literal adaptation of the root preflight recorder; preserves original wait,
separate full raw streams, source snapshot and immutable input pins. The
lifecycle reader reads existing evidence only. This is not a new build,
scientific replay, visual review or root acceptance.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import signal
import subprocess
import sys
import time

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
QA = ROOT / 'docs/papers204_208_sequence/qa'
PREP = QA / 'p210_terminal_lifecycle_preparation'
SOURCE = QA / 'record_p210_lifecycle_01.py'
OUT = QA / 'p210_terminal_lifecycle_01'
TERMINAL = ROOT / 'papers/210-weakly-increasing-run-aggregation/qa_final'
ENV = {'PATH': '/usr/bin:/bin', 'LANG': 'C.UTF-8', 'LC_ALL': 'C.UTF-8', 'TZ': 'UTC'}

def pin(path):
    data = Path(path).read_bytes()
    return {'sha256': hashlib.sha256(data).hexdigest(), 'bytes': len(data)}

def save(path, value):
    data = value if isinstance(value, bytes) else (json.dumps(value, sort_keys=True, indent=2) + '\n').encode()
    with path.open('xb') as stream:
        stream.write(data)

def group_absent(pid):
    try:
        os.killpg(pid, 0)
        return False
    except ProcessLookupError:
        return True

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--expected-lifecycle-preparation-sha256', required=True)
    args = parser.parse_args()
    assert Path(__file__) == SOURCE and Path.cwd() == ROOT
    assert not os.path.lexists(OUT) and (TERMINAL / 'SHA256SUMS').is_file()
    assert pin(PREP / 'SHA256SUMS')['sha256'] == args.expected_lifecycle_preparation_sha256
    argv = ['/usr/bin/python3.10', '-I', '-S', '-B', '-X',
            'pycache_prefix=' + str(OUT / 'never_created_reader_cache'), str(PREP / 'inspect_p210_lifecycle.py'),
            '--expected-preparation-sha256', args.expected_lifecycle_preparation_sha256]
    inputs = {str(p): pin(p) for p in (SOURCE, PREP / 'inspect_p210_lifecycle.py',
              PREP / 'ACTUAL_BINDING.json', PREP / 'SHA256SUMS', TERMINAL / 'SHA256SUMS',
              QA / 'p210_terminal_artifact_03/SHA256SUMS',
              QA / 'P210_ARTIFACT_ROOT_ACCEPTANCE.actual.json',
              TERMINAL.parent / 'ROOT_LIFECYCLE.md', TERMINAL.parent / 'PAPER_MANIFEST.sha256',
              QA / 'p210_terminal_artifact_03/ARTIFACT_REPORT.json', Path('/usr/bin/python3.10'))}
    OUT.mkdir(mode=0o700)
    save(OUT / 'executed_source.py', SOURCE.read_bytes())
    save(OUT / 'ATTEMPT.json', {'argv': argv, 'cwd': str(ROOT), 'environment': ENV,
         'inputs_before': inputs, 'timeout_seconds': 600, 'start_new_session': True,
         'started_epoch': time.time(), 'paper_terminal_present_before': True})
    events, timed_out, original_wait, wait_error = [], False, None, None
    with (OUT / 'LIFECYCLE_REPORT.json').open('xb') as stdout, (OUT / 'stderr').open('xb') as stderr:
        proc = subprocess.Popen(argv, cwd=ROOT, env=ENV, stdout=stdout, stderr=stderr, start_new_session=True)
        save(OUT / 'SPAWN.json', {'pid': proc.pid, 'process_group_id': proc.pid, 'spawned_epoch': time.time()})
        try:
            original_wait = proc.wait(timeout=600)
        except subprocess.TimeoutExpired:
            timed_out = True
        except BaseException as exc:
            wait_error = repr(exc)
        if not group_absent(proc.pid):
            for sig in (signal.SIGTERM, signal.SIGKILL):
                try:
                    os.killpg(proc.pid, sig)
                    events.append({'signal': int(sig), 'sent': True})
                except ProcessLookupError:
                    events.append({'signal': int(sig), 'sent': False, 'already_absent': True})
                try:
                    proc.wait(timeout=5)
                except subprocess.TimeoutExpired:
                    pass
                if group_absent(proc.pid):
                    break
    after = {name: pin(name) for name in inputs}
    absent = group_absent(proc.pid)
    if proc.returncode is None or not absent:
        save(OUT / 'UNCLOSED.json', {'pid': proc.pid, 'original_wait_exit_code': original_wait,
            'cleanup_wait_exit_code': proc.returncode, 'process_group_absent': absent,
            'timed_out': timed_out, 'wait_error': wait_error, 'cleanup_events': events,
            'scope': 'Unsettled owned process; no final stream hashes or package seal.'})
        print(json.dumps({'status': 'UNCLOSED_P210_LIFECYCLE_NO_SEAL', 'output': str(OUT)}))
        return 1
    result = {'argv': argv, 'cwd': str(ROOT), 'environment': ENV, 'pid': proc.pid,
        'original_wait_exit_code': original_wait, 'cleanup_wait_exit_code': proc.returncode,
        'timed_out': timed_out, 'wait_error': wait_error, 'cleanup_events': events, 'child_reaped': proc.returncode is not None,
        'process_group_absent': absent, 'inputs_before': inputs, 'inputs_after': after,
        'inputs_unchanged': inputs == after, 'stdout': pin(OUT / 'LIFECYCLE_REPORT.json'), 'stderr': pin(OUT / 'stderr'),
        'paper_terminal_present_after': (TERMINAL / 'SHA256SUMS').is_file(), 'finished_epoch': time.time()}
    save(OUT / 'RESULT.json', result)
    clean = original_wait == 0 and not timed_out and wait_error is None and not events and absent and inputs == after and (TERMINAL / 'SHA256SUMS').is_file() and not os.path.lexists(OUT / 'never_created_reader_cache')
    raw = (OUT / 'LIFECYCLE_REPORT.json').read_bytes()
    data = json.loads(raw) if clean else None
    passed = clean and data['status'] == 'PASS_P210_DOCUMENT_ONLY_LIFECYCLE_FOLLOWUP_ROOT_ACCEPTANCE_PENDING' and data['new_scientific_runs'] == data['new_builds'] == data['new_views'] == data['new_manuscript_reviews'] == data['reader_file_writes'] == data['old_programs_imported_or_executed'] == 0 and data['root_acceptance'] is data['paper_completion'] is data['five_paper_completion'] is False and (OUT / 'stderr').read_bytes() == b''
    if passed:
        rows = sorted(p for p in OUT.rglob('*') if p.is_file())
        save(OUT / 'SHA256SUMS', ''.join(pin(p)['sha256'] + '  ' + p.relative_to(OUT).as_posix() + '\n' for p in rows).encode())
    print(json.dumps({'status': 'PASS_ACTUAL_P210_LIFECYCLE_FOLLOWUP_CAPTURE' if passed else 'FAILED_OR_UNCLOSED_P210_LIFECYCLE_FOLLOWUP_CAPTURE',
        'output': str(OUT), 'original_wait_exit_code': original_wait, 'stdout': result['stdout'], 'stderr': result['stderr'],
        'result': pin(OUT / 'RESULT.json'), 'seal': pin(OUT / 'SHA256SUMS') if passed else None,
        'checks': data['checks'] if passed else None,
        'current_path_keys': data['current_path_keys'] if passed else None,
        'lifecycle_acceptance': False}, sort_keys=True))
    return 0 if passed else 1

if __name__ == '__main__':
    sys.exit(main())
