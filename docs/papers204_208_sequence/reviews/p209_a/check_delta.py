"""One-time documentary delta audit. No mathematical/build/view execution."""
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import time

BASE = Path(__file__).resolve().parent
ROOT = BASE.parents[3]
QA = ROOT / 'docs/papers204_208_sequence/qa'
PAPER = ROOT / 'papers/209-ordered-fibre-threading'
FROZEN = PAPER / 'frozen_round0'
PAIR = QA / 'root_replays/p209_a_strict/root_a_pair_01'
LAUNCH = PAIR.parent / 'launcher_root_a_pair_01'
PREP = QA / 'p209_a_root_preparation'
RESPONSE = QA.parent / 'P209_A_RESPONSE.md'
AUDIT = BASE / 'delta_check_01'
ENV = {'PATH': '/usr/bin:/bin', 'LANG': 'C.UTF-8', 'LC_ALL': 'C.UTF-8', 'TZ': 'UTC'}
OLD_SEAL = '7105dd2c22a7fb8df5586a59880fdc47e26f62f2d7573d3f08570eda5c62fb0c'
assert dict(os.environ) == ENV and sys.flags.isolated and sys.flags.no_site
assert sys.flags.dont_write_bytecode and sys.flags.optimize == 0
assert Path.cwd() == ROOT and not AUDIT.exists()
assert not (BASE / 'INITIAL_REVIEW_SEAL.sha256').exists()
assert not (BASE / 'DELTA.md').exists()
AUDIT.mkdir()


def digest(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda: stream.read(1048576), b''):
            h.update(block)
    return h.hexdigest()


def save(name, value):
    with (AUDIT / name).open('x') as stream:
        stream.write(json.dumps(value, indent=2, sort_keys=True) + '\n')


def obj(path):
    return json.loads(Path(path).read_bytes())


save('ATTEMPT.json', {'argv': sys.orig_argv, 'cwd': str(Path.cwd()),
    'env': dict(os.environ), 'flags': str(sys.flags), 'started_epoch': time.time(),
    'script_sha256': digest(__file__), 'phase': 'ACTUAL_DOCUMENTARY_DELTA_AUDIT'})
assert digest(BASE / 'SHA256SUMS') == OLD_SEAL
shutil.copyfile(BASE / 'SHA256SUMS', BASE / 'INITIAL_REVIEW_SEAL.sha256')
assert digest(BASE / 'INITIAL_REVIEW_SEAL.sha256') == OLD_SEAL

expected = {}
roles = []


def add(path, wanted=None):
    path = Path(path)
    name = str(path)
    assert path.is_absolute() and path.is_file()
    h = digest(path) if wanted is None else wanted
    assert name not in expected or expected[name] == h, name
    expected[name] = h


def manifest(path, count=None, wanted=None, complete=False):
    path = Path(path)
    if wanted is not None:
        assert digest(path) == wanted, str(path)
    add(path, wanted)
    rows = {}
    for line in path.read_text().splitlines():
        h, name = line.split('  ', 1)
        p = Path(name)
        assert re.fullmatch('[0-9a-f]{64}', h)
        assert not p.is_absolute() and '..' not in p.parts and name not in rows
        assert name != path.name and not (path.parent / name).is_symlink()
        rows[name] = h
        add(path.parent / name, h)
    if count is not None:
        assert len(rows) == count, str(path)
    if complete:
        assert set(rows) == {p.relative_to(path.parent).as_posix()
            for p in path.parent.rglob('*') if p.is_file() and p != path}
    roles.append({'manifest': str(path), 'sha256': digest(path),
        'payloads': len(rows), 'complete_at_current_path': complete})
    return rows


old_rows = manifest(BASE / 'INITIAL_REVIEW_SEAL.sha256', 1227, OLD_SEAL)
manifest(BASE / 'INITIAL_ARTIFACTS.sha256', 1226)
for p in sorted(BASE.rglob('SHA256SUMS')):
    if p != BASE / 'SHA256SUMS':
        manifest(p, complete=True)
manifest(FROZEN / 'SHA256SUMS', 1989,
    '0f77871539b374027ab42910471cc74cefcd570e214a8242ac0a30c7a83e70ba', True)
manifest(PAPER / 'SHA256SUMS', 1985,
    '9fd20cd746f1ae03c22a87283313248ad79ffcfb9a0f1ea45458937dd5901a0e')
for line in (BASE / 'INPUT_PINS.sha256').read_text().splitlines():
    h, name = line.split('  ', 1)
    add(ROOT / name, h)
assert len((BASE / 'INPUT_PINS.sha256').read_text().splitlines()) == 1990
for p, h, count in ((PAIR, 'e1d7a773e1ed5c7ef347922926774f258dd42a096bafff4b50907d0e68a02728', 462),
                    (LAUNCH, 'c12927453cd0f09591a2d36f21c29e9baa3a6c7613a5e16a65198fd43641e3b6', 10),
                    (PREP, 'bcbf02f2fdfde47e21cee023cdad8a35aaa8230b4be8717962530e1da57feea2', 6)):
    manifest(p / 'SHA256SUMS', count, h, True)
for p in sorted(PAIR.rglob('SHA256SUMS')):
    if p != PAIR / 'SHA256SUMS':
        manifest(p, complete=True)

historical = obj(BASE / 'initial_audit_01/CURRENT_INPUT_CLOSURE.json')
assert len(historical) == 120491
mutable = str(QA.parent / 'GIT_SYNC_RECEIPT.md')
assert mutable in historical
recovery = QA / 'central_lifecycle_p209_a'
recovered_receipt = recovery / 'GIT_SYNC_RECEIPT.before.md'
assert digest(recovered_receipt) == historical[mutable] == 'af1754c9d6095c0f943b75fe7b9819ebd2b7c4db9609930ca7feccf2934786da'
manifest(recovery / 'SHA256SUMS', 3, complete=True)
save('HISTORICAL_PIN_ROLE_MAP.json', {
    'original_complete_pin_map': 'initial_audit_01/CURRENT_INPUT_CLOSURE.json',
    'original_pin_map_sha256': digest(BASE / 'initial_audit_01/CURRENT_INPUT_CLOSURE.json'),
    'original_path_count': len(historical),
    'same_path_recheck_count': len(historical) - 1,
    'excluded_current_paths': {},
    'exact_documentary_aliases': {mutable: {'original_sha256': historical[mutable],
        'preserved_exact_path': str(recovered_receipt),
        'reason': 'Exact old documentary bytes recovered by root from pushed Git object f8ee398cb7b0ddd5d1e5890543034a001cd2bc26. Not an at-time physical snapshot, pin refresh or scientific substitution. Full recovery receipt and its physical manifest are checked.'}},
    'initial_manifest_role': {'original_path': str(BASE / 'SHA256SUMS'),
        'preserved_exact_path': str(BASE / 'INITIAL_REVIEW_SEAL.sha256'),
        'original_sha256': OLD_SEAL, 'payload_count': 1227},
    'initial_payloads_remain_at_original_paths': True})
for p, h in historical.items():
    add(recovered_receipt if p == mutable else p, h)

assert digest(RESPONSE) == '3b84c6c6a39b890562a63fbcb76a1a1fdf683886b9f6670b4bdd05544c6e9459'
assert digest(QA / 'P209_A_ROOT_INITIAL_INSPECTION.md') == 'c095b7365d9083b83f6cd802ea6a3c9fa372a8b670ba9b28ae11e29d562fe690'
assert digest(PAPER / 'ROOT_ADOPTION.md') == '8f82ae0af7156131f14e9e6e849198f8b1c98564760c30d4bc121b50cf34f82e'
assert digest(PAPER / 'PAPER_STATUS.md') == '304c24e871a27bd02bcd6db231abc37870fb263a01d4c081289bdd53e8718a73'
docs = [RESPONSE] + [QA / n for n in (
    'P209_A_ROOT_INITIAL_INSPECTION.md', 'P209_A_ROOT_INITIAL_INSPECTION.actual.json',
    'P209_A_ROOT_PAIR_PREPARATION.actual.json', 'P209_A_ROOT_PAIR_INSPECTION.actual.json',
    'P209_A_EXACT_NOCHANGE_CHECK.actual.json', 'P209_A_ROOT_PREEXECUTION.actual.json',
    'inspect_p209_a_initial.py', 'inspect_p209_a_root_pair.py')]
snapshots = AUDIT / 'exact_response_inputs'
snapshots.mkdir()
snapshot_map = {}
for p in docs:
    add(p)
    q = snapshots / p.name
    shutil.copyfile(p, q)
    assert digest(q) == expected[str(p)]
    add(q)
    snapshot_map[str(p)] = {'copy': str(q), 'sha256': expected[str(p)]}
save('RESPONSE_ORIGINALS_AND_COPIES.json', snapshot_map)
add(__file__)
add('/usr/bin/python3.10')
add('/usr/bin/cmp')
add('/usr/bin/env')

for folder in (PAIR, LAUNCH):
    before = obj(folder / ('ALL_INPUTS_INCLUDING_CAPSULES_BEFORE.json' if folder == PAIR else 'INPUTS_BEFORE.json'))
    after = obj(folder / ('ALL_INPUTS_AFTER.json' if folder == PAIR else 'INPUTS_AFTER.json'))
    assert before == after
    if folder == PAIR:
        assert len(before) == 5147
    for p, row in before.items():
        add(p, row['sha256'])
        assert Path(p).stat().st_size == row['bytes']


def measure():
    result = {}
    for p, h in sorted(expected.items()):
        actual = digest(p)
        result[p] = actual
        assert actual == h, p
    return result


first = measure()
save('INPUTS_BEFORE.json', first)
save('MANIFEST_ROLES.json', roles)
commands = obj(PAIR / 'ALL_COMMAND_RECORDS.json')
assert len(commands) == 85
for row in commands:
    folder, tag, cmd = Path(row['folder']), row['tag'], row['command']
    assert folder.is_relative_to(PAIR) and obj(folder / (tag + '.command.json')) == cmd
    attempt = obj(folder / (tag + '.attempt.json'))
    assert all(attempt[k] == cmd[k] for k in ('argv', 'cwd', 'env', 'stdout', 'stderr'))
    assert cmd['process_outcome'] == 'COMPLETED' and cmd['exit'] == 0
    assert cmd['spawn_error'] is None and cmd['cleanup'] == [] and cmd['env'] == ENV
    for stream in ('stdout', 'stderr'):
        p = folder / cmd[stream]
        assert digest(p) == cmd[stream + '_info']['sha256']
        assert p.stat().st_size == cmd[stream + '_info']['bytes']
pair_receipt = obj(PAIR / 'RECEIPT.json')
assert pair_receipt['status'] == 'PASS_ROOT_REVIEW_A_PAIR' and not pair_receipt['failures']
assert not pair_receipt['result']['canonical_adopted']
for label in ('replay_01', 'replay_02'):
    p = PAIR / label
    receipt = obj(p / 'RECEIPT.json')
    assert receipt['status'] == 'PASS' and receipt['checks'] == 135605 and receipt['total_states'] == 3414
    assert receipt['source_only_initial_names'] == ['bootstrap.py', 'verify.py']
    for name in receipt['source_only_initial_names']:
        assert digest(p / 'source_inputs' / name) == digest(BASE / name)
    for phase in ('before', 'after'):
        state = obj(p / ('child.' + phase + '.json'))
        assert state['env'] == ENV and state['cwd'] == str(p)
        assert state['optimize'] == 0 and state['isolated'] == state['no_site'] == 1
        assert state['dont_write_bytecode'] and not state['cache_exists']
        assert not Path(state['pycache_prefix']).exists()
launch = obj(LAUNCH / 'RECEIPT.json')
assert launch['status'] == 'PASS_ROOT_LAUNCH' and launch['exit'] == 0
assert launch['outcome'] == 'COMPLETED' and launch['failure'] is None
assert launch['env'] == ENV and launch['inputs_unchanged'] and launch['cache_absent']
for name in ('recorder.stdout', 'recorder.stderr'):
    assert digest(LAUNCH / name) == launch[name + '_pin']['sha256']
assert obj(LAUNCH / 'recorder.stdout')['status'] == pair_receipt['status']

comparisons = [
    (BASE / 'SHA256SUMS', BASE / 'INITIAL_REVIEW_SEAL.sha256'),
    (PAPER / 'SHA256SUMS', FROZEN / 'AUTHOR_MANIFEST.sha256'),
    (PAPER / 'main.tex', FROZEN / 'main.tex'),
    (PAPER / 'main.pdf', FROZEN / 'main.pdf'),
    (PAPER / 'verify.py', FROZEN / 'verify.py'),
    (PAPER / 'CANONICAL.json', FROZEN / 'CANONICAL.json'),
    (PAPER / 'ROOT_ADOPTION.md', FROZEN / 'ROOT_ADOPTION.md'),
    (PAPER / 'PAPER_STATUS.md', FROZEN / 'PAPER_STATUS.md'),
    (BASE / 'REPORT.md', BASE / 'INITIAL_REPORT.md'),
    (PAIR / 'replay_01/producer.stdout', PAIR / 'replay_02/producer.stdout'),
    (PAIR / 'replay_01/producer.stdout', BASE / 'CANONICAL.json'),
    (PAIR / 'replay_02/producer.stdout', BASE / 'CANONICAL.json')]
for i, (a, b) in enumerate(comparisons, 1):
    assert str(a) in expected or a == BASE / 'SHA256SUMS'
    assert str(b) in expected
    tag = 'raw_cmp_%02d' % i
    argv = ['/usr/bin/cmp', '--', str(a), str(b)]
    save(tag + '.attempt.json', {'argv': argv, 'env': ENV, 'cwd': str(ROOT), 'started_epoch': time.time()})
    result = subprocess.run(argv, cwd=ROOT, env=ENV, capture_output=True)
    with (AUDIT / (tag + '.stdout')).open('xb') as stream:
        stream.write(result.stdout)
    with (AUDIT / (tag + '.stderr')).open('xb') as stream:
        stream.write(result.stderr)
    save(tag + '.command.json', {'argv': argv, 'env': ENV, 'cwd': str(ROOT),
        'exit': result.returncode, 'stdout_bytes': len(result.stdout), 'stderr_bytes': len(result.stderr),
        'stdout_sha256': digest(AUDIT / (tag + '.stdout')), 'stderr_sha256': digest(AUDIT / (tag + '.stderr')),
        'finished_epoch': time.time()})
    assert result.returncode == 0 and not result.stdout and not result.stderr
findings = obj(BASE / 'FINDINGS.json')
assert findings['findings'] == [] and not any(findings['current_open_counts'].values())
assert obj(BASE / 'auxiliary_01/PDF_PREFLIGHT.json')['verdict'] == 'UNAVAILABLE'
assert (BASE / 'PREFLIGHT_INITIAL_FAILURE.json').is_file()
second = measure()
save('INPUTS_AFTER.json', second)
assert first == second
assert digest(BASE / 'SHA256SUMS') == OLD_SEAL
assert all(digest(BASE / p) == h for p, h in old_rows.items())
save('RESULT.json', {'status': 'PASS_EXACT_NOCHANGE_DELTA_INPUT_CLOSURE',
    'actual_inputs_checked_before_and_after': len(expected),
    'historical_dependency_pins_rechecked': len(historical),
    'historical_same_path_checks': len(historical) - 1,
    'historical_exact_documentary_aliases': 1,
    'historical_omissions_or_refreshed_pins': 0,
    'initial_payloads_preserved': 1227, 'round0_inputs': 1990,
    'live_author_payloads_unchanged': 1985,
    'root_pair_payloads': 462, 'root_launcher_payloads': 10,
    'root_pair_known_inputs_unchanged': 5147, 'archived_root_commands_checked': 85,
    'new_raw_comparisons_exit_zero': len(comparisons),
    'current_open_counts': findings['current_open_counts'],
    'preflight_status_preserved': 'UNAVAILABLE', 'initial_preflight_failure_preserved': True,
    'boundary': 'Actual no-change byte/receipt inspection only. No new mathematical producer, build, render, page view or Round1. The reviewer decision follows in DELTA.md.'})
print(json.dumps(obj(AUDIT / 'RESULT.json'), sort_keys=True))
