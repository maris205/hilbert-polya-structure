#!/usr/bin/env python3
"""Root-owned raw recorder for the exact-five current-rich-key gate.

Literal adaptation of the root preflight recorder; preserves original wait,
separate full raw streams, source snapshot and immutable input pins. The
exact-five reader reads existing evidence only. This is not a new build,
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
PREP = QA / 'five_paper_terminal_exact_revision_02'
SOURCE = QA / 'record_five_terminal_exact_02.py'
OUT = QA / 'five_paper_terminal_exact_run_02'
TERMINAL_SEALS = (QA / 'batch_terminal_builds_01/SHA256SUMS',
    ROOT / 'papers/208-original-snapshot-triangulation-sweeps/qa_final/SHA256SUMS',
    ROOT / 'papers/209-ordered-fibre-threading/qa_final/SHA256SUMS',
    ROOT / 'papers/210-weakly-increasing-run-aggregation/qa_final/SHA256SUMS')
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
    parser.add_argument('--expected-five-preparation-sha256', required=True)
    args = parser.parse_args()
    assert Path(__file__) == SOURCE and Path.cwd() == ROOT
    assert not os.path.lexists(OUT) and all(p.is_file() for p in TERMINAL_SEALS)
    assert pin(PREP / 'SHA256SUMS')['sha256'] == args.expected_five_preparation_sha256
    argv = ['/usr/bin/python3.10', '-I', '-S', '-B', '-X',
            'pycache_prefix=' + str(OUT / 'never_created_reader_cache'), str(PREP / 'inspect_five.py'),
            '--expected-preparation-sha256', args.expected_five_preparation_sha256]
    prep_files = sorted(p for p in PREP.rglob('*') if p.is_file())
    assert prep_files and all(not p.is_symlink() and p.resolve() == p for p in prep_files)
    inputs = {str(p): pin(p) for p in (SOURCE, *prep_files, *TERMINAL_SEALS,
              ROOT / 'SYMBOLIC_DYNAMICS_STATE.md', QA.parent / 'PIPELINE_STATE.md',
              QA.parent / 'FINAL_THEOREM_CONTRACTS.md',
              QA / 'P210_LIFECYCLE_ROOT_ACCEPTANCE.actual.json', Path('/usr/bin/python3.10'))}
    OUT.mkdir(mode=0o700)
    save(OUT / 'executed_source.py', SOURCE.read_bytes())
    save(OUT / 'ATTEMPT.json', {'argv': argv, 'cwd': str(ROOT), 'environment': ENV,
         'inputs_before': inputs, 'timeout_seconds': 1800, 'start_new_session': True,
         'started_epoch': time.time(), 'all_five_terminal_evidence_present_before': True})
    events, timed_out, original_wait, wait_error = [], False, None, None
    with (OUT / 'FIVE_REPORT.json').open('xb') as stdout, (OUT / 'stderr').open('xb') as stderr:
        proc = subprocess.Popen(argv, cwd=ROOT, env=ENV, stdout=stdout, stderr=stderr, start_new_session=True)
        save(OUT / 'SPAWN.json', {'pid': proc.pid, 'process_group_id': proc.pid, 'spawned_epoch': time.time()})
        try:
            original_wait = proc.wait(timeout=1800)
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
        print(json.dumps({'status': 'UNCLOSED_EXACT_FIVE_NO_SEAL', 'output': str(OUT)}))
        return 1
    result = {'argv': argv, 'cwd': str(ROOT), 'environment': ENV, 'pid': proc.pid,
        'original_wait_exit_code': original_wait, 'cleanup_wait_exit_code': proc.returncode,
        'timed_out': timed_out, 'wait_error': wait_error, 'cleanup_events': events, 'child_reaped': proc.returncode is not None,
        'process_group_absent': absent, 'inputs_before': inputs, 'inputs_after': after,
        'inputs_unchanged': inputs == after, 'stdout': pin(OUT / 'FIVE_REPORT.json'), 'stderr': pin(OUT / 'stderr'),
        'all_five_terminal_evidence_present_after': all(p.is_file() for p in TERMINAL_SEALS), 'finished_epoch': time.time()}
    save(OUT / 'RESULT.json', result)
    clean = original_wait == 0 and not timed_out and wait_error is None and not events and absent and inputs == after and all(p.is_file() for p in TERMINAL_SEALS) and not os.path.lexists(OUT / 'never_created_reader_cache')
    raw = (OUT / 'FIVE_REPORT.json').read_bytes()
    data = json.loads(raw) if clean else None
    passed = clean and data['schema'] == 'exact-five-current-rich-key-gate-v1' and data['status'] == 'PASS_EXACT_FIVE_GATE_ROOT_ACCEPTANCE_PENDING' and data['papers'] == ['P205', 'P207', 'P208', 'P209', 'P210'] and data['retained_papers'] == data['individually_root_accepted_papers'] == 5 and data['current_open_findings'] == 0 and data['reused_strict_author_A_B_pairs'] == 15 and data['reused_terminal_source_only_builds'] == 10 and data['reused_actual_prior_root_page_views'] == 27 and data['complete_current_rich_file_reads'] == 2 and data['new_scientific_runs'] == data['new_builds'] == data['new_views'] == data['new_manuscript_reviews'] == data['reader_file_writes'] == data['old_auditors_or_writers_imported_or_executed'] == 0 and data['root_acceptance'] is data['five_paper_completion'] is False and data['external'] == 'OWNER_AMBER / HOLD_EXTERNAL' and (OUT / 'stderr').read_bytes() == b''
    if passed:
        rows = sorted(p for p in OUT.rglob('*') if p.is_file())
        save(OUT / 'SHA256SUMS', ''.join(pin(p)['sha256'] + '  ' + p.relative_to(OUT).as_posix() + '\n' for p in rows).encode())
    print(json.dumps({'status': 'PASS_ACTUAL_EXACT_FIVE_CAPTURE' if passed else 'FAILED_OR_UNCLOSED_EXACT_FIVE_CAPTURE',
        'output': str(OUT), 'original_wait_exit_code': original_wait, 'stdout': result['stdout'], 'stderr': result['stderr'],
        'result': pin(OUT / 'RESULT.json'), 'seal': pin(OUT / 'SHA256SUMS') if passed else None,
        'checks': data['checks'] if passed else None,
        'current_path_keys': data['complete_current_file_keys'] if passed else None,
        'root_acceptance': False, 'five_paper_completion': False}, sort_keys=True))
    return 0 if passed else 1

if __name__ == '__main__':
    sys.exit(main())
