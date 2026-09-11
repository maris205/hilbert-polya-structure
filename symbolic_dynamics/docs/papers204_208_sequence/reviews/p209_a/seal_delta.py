"""One-time append-only delta closure and regenerated complete outer manifest."""
import hashlib
import json
import os
from pathlib import Path
import re
import sys
import time

BASE = Path(__file__).resolve().parent
ROOT = BASE.parents[3]
AUDIT = BASE / 'delta_final_audit_01'
ENV = {'PATH': '/usr/bin:/bin', 'LANG': 'C.UTF-8', 'LC_ALL': 'C.UTF-8', 'TZ': 'UTC'}
OLD = '7105dd2c22a7fb8df5586a59880fdc47e26f62f2d7573d3f08570eda5c62fb0c'
assert dict(os.environ) == ENV and Path.cwd() == ROOT
assert sys.flags.isolated and sys.flags.no_site and sys.flags.dont_write_bytecode
assert sys.flags.optimize == 0 and not AUDIT.exists()


def digest(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda: stream.read(1048576), b''):
            h.update(block)
    return h.hexdigest()


def obj(path):
    return json.loads(Path(path).read_bytes())


def save(name, value):
    with (AUDIT / name).open('x') as stream:
        stream.write(json.dumps(value, indent=2, sort_keys=True) + '\n')


assert digest(BASE / 'SHA256SUMS') == OLD
assert (BASE / 'SHA256SUMS').read_bytes() == (BASE / 'INITIAL_REVIEW_SEAL.sha256').read_bytes()
AUDIT.mkdir()
save('ATTEMPT.json', {'argv': sys.orig_argv, 'env': dict(os.environ),
    'cwd': str(Path.cwd()), 'flags': str(sys.flags), 'script_sha256': digest(__file__),
    'started_epoch': time.time(), 'scope': 'Final local artifact closure, successful-delta input reuse and manifest regeneration only. No mathematical/build/render/view execution.'})
preseal = {p.relative_to(BASE).as_posix(): digest(p) for p in sorted(BASE.rglob('*'))
    if p.is_file() and p != BASE / 'SHA256SUMS'}
save('PRESEAL_PAYLOADS.json', preseal)
initial = {}
for line in (BASE / 'INITIAL_REVIEW_SEAL.sha256').read_text().splitlines():
    h, n = line.split('  ', 1)
    p = Path(n)
    assert re.fullmatch('[0-9a-f]{64}', h) and not p.is_absolute() and '..' not in p.parts
    assert n not in initial and n != 'SHA256SUMS'
    initial[n] = h
    assert digest(BASE / n) == h, n
assert len(initial) == 1227
before = obj(BASE / 'delta_check_02/INPUTS_BEFORE.json')
after = obj(BASE / 'delta_check_02/INPUTS_AFTER.json')
assert before == after and len(after) == 124214
for p, h in after.items():
    assert digest(p) == h, p
original = obj(BASE / 'FINDINGS.json')
current = obj(BASE / 'CURRENT_FINDINGS.json')
assert original['phase'] == 'INITIAL_REVIEW'
assert original['delta_status'] == 'NOT_YET_SUBMITTED_OR_ASSESSED'
assert current['verdict'] == current['delta_status'] == 'ACCEPTED_EXACT_NOCHANGE_DELTA'
assert original['findings'] == current['findings'] == []
assert original['current_open_counts'] == current['current_open_counts'] == {'critical': 0, 'major': 0, 'minor': 0}
assert digest(BASE / 'REPORT.md') == digest(BASE / 'INITIAL_REPORT.md') == '9cb053c4b09a74521bfe9d68df1e728dd88fe9441fc939be52dd61c2da879c51'
assert digest(ROOT / 'docs/papers204_208_sequence/P209_A_RESPONSE.md') == current['response_sha256'] == '3b84c6c6a39b890562a63fbcb76a1a1fdf683886b9f6670b4bdd05544c6e9459'
assert obj(BASE / 'delta_check_01/EXECUTION.actual.json')['completion_result']['exit_code'] == 1
assert obj(BASE / 'delta_check_02/EXECUTION.actual.json')['completion_result']['exit_code'] == 0
assert obj(BASE / 'auxiliary_01/PDF_PREFLIGHT.json')['verdict'] == 'UNAVAILABLE'
assert obj(BASE / 'delta_check_02/RESULT.json')['status'] == 'PASS_EXACT_NOCHANGE_DELTA_INPUT_CLOSURE'
assert not (BASE / 'delta_check_01/RESULT.json').exists()
for n, h in preseal.items():
    assert digest(BASE / n) == h, n
save('RESULT.json', {'status': 'PASS_FINAL_DELTA_ORIGINAL_AND_INPUT_CLOSURE',
    'preseal_payloads_rechecked': len(preseal), 'initial_payloads_preserved': len(initial),
    'successful_delta_input_paths_rechecked': len(after),
    'historical_dependency_pins': 120491, 'same_path_historical_pins': 120490,
    'exact_historical_documentary_aliases': 1, 'omitted_or_refreshed_original_pins': 0,
    'initial_manifest_preserved_sha256': OLD,
    'original_report_and_findings_roles_unchanged': True,
    'failed_documentary_audit_preserved_exit': 1, 'corrected_documentary_audit_actual_exit': 0,
    'current_open_counts': current['current_open_counts'],
    'delta_sha256': digest(BASE / 'DELTA.md'), 'current_findings_sha256': digest(BASE / 'CURRENT_FINDINGS.json'),
    'optional_preflight_remains': 'UNAVAILABLE',
    'scope': 'Artifact/input recheck only. No new mathematical producer, compiler, renderer or page view; no physical Round1.'})
payloads = sorted(p for p in BASE.rglob('*') if p.is_file() and p != BASE / 'SHA256SUMS')
assert not any(p.is_symlink() for p in payloads)
assert digest(BASE / 'INITIAL_REVIEW_SEAL.sha256') == OLD
assert digest(BASE / 'SHA256SUMS') == OLD
with (BASE / 'SHA256SUMS').open('w') as stream:
    stream.write(''.join(digest(p) + '  ' + p.relative_to(BASE).as_posix() + '\n' for p in payloads))
names = set()
for line in (BASE / 'SHA256SUMS').read_text().splitlines():
    h, n = line.split('  ', 1)
    assert n not in names and n != 'SHA256SUMS'
    names.add(n)
    assert digest(BASE / n) == h
assert names == {p.relative_to(BASE).as_posix() for p in BASE.rglob('*')
    if p.is_file() and p != BASE / 'SHA256SUMS'}
assert all(digest(BASE / n) == h for n, h in initial.items())
print(json.dumps({'status': 'SEALED_ACTUAL_ACCEPTED_A_DELTA', 'payloads': len(payloads),
    'seal_sha256': digest(BASE / 'SHA256SUMS'),
    'initial_seal_alias_sha256': digest(BASE / 'INITIAL_REVIEW_SEAL.sha256'),
    'original_payloads_preserved': len(initial), 'delta_sha256': digest(BASE / 'DELTA.md'),
    'current_findings_sha256': digest(BASE / 'CURRENT_FINDINGS.json'),
    'current_open_counts': current['current_open_counts'], 'input_paths_rechecked': len(after),
    'preflight': 'UNAVAILABLE', 'failed_audit_01_preserved': True,
    'physical_round1_created': False}, sort_keys=True))
