#!/usr/bin/env python3
"""Read-only exact-no-change B delta audit; never runs mathematical code.

Historical package paths FINDINGS.json and SHA256SUMS resolve to preserved
initial aliases. REPORT.md stays unchanged and also has an exact alias.
All subprocess output below is from actual read-only hash/byte checks.
"""
from datetime import datetime, timezone
from hashlib import sha256
import json
from pathlib import Path
import subprocess
import sys


BASE = Path(__file__).resolve().parents[4]
B = BASE / 'docs/papers204_208_sequence/reviews/p207_b'
PAPER = BASE / 'papers/207-upper-neighbor-rank-dynamics'
FREEZE = PAPER / 'frozen_round1'
REPLAY = BASE / 'docs/papers204_208_sequence/qa/root_replays/p207_b_controlled'
RESPONSE = BASE / 'docs/papers204_208_sequence/P207_B_RESPONSE.md'
UTILITY = BASE / 'docs/papers204_208_sequence/qa/replay_p207_review.py'
UTILITY_AUDIT = BASE / 'docs/papers204_208_sequence/qa/P207_B_INITIAL_ARTIFACT_AUDIT.md'
INITIAL_MANIFEST = '6f103d933c8135563b00734d8850ce36bf2fc47aa504d669e01cf6c99ef29074'
RESPONSE_HASH = 'd1e3f7b0ede25f375269ebedaa84c12558f7055322dfe905379974e05dbd3244'
FREEZE_HASH = '8d134689f8c07f9bcac65b4576a5bfca2e073ece6281f9d893148f12adb43f5d'
CANONICAL_HASH = 'b7206f01180dcbe5eca24dbaec67cc96ae5dc80f86004455d382e7723c786fda'
CHECKS = 0
CONSUMED = {}
COMMANDS = []


def check(condition, message):
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(message)


def info(raw):
    return {'sha256': sha256(raw).hexdigest(), 'bytes': len(raw)}


def read(path):
    path = path.resolve()
    raw = path.read_bytes()
    key = str(path.relative_to(BASE)) if BASE in path.parents else str(path)
    entry = info(raw)
    if key in CONSUMED:
        check(CONSUMED[key] == entry, 'changed during consumption: ' + key)
    CONSUMED[key] = entry
    return raw


def pins(path):
    rows = []
    for line in read(path).decode().splitlines():
        digest, name = line.split('  ', 1)
        rel = Path(name)
        check(len(digest) == 64 and all(c in '0123456789abcdef' for c in digest), 'bad digest')
        check(not rel.is_absolute() and '..' not in rel.parts, 'bad relative path')
        rows.append((name, digest))
    check(len(rows) == len(dict(rows)), 'duplicate pin path')
    return rows


def verify_rows(rows, base, aliases=None):
    aliases = aliases or {}
    for name, digest in rows:
        path = base / aliases.get(name, name)
        check(info(read(path))['sha256'] == digest, 'pin mismatch: ' + str(path))


def execute(command, cwd):
    child = subprocess.run(command, cwd=cwd, capture_output=True)
    COMMANDS.append({'command': command, 'cwd': str(cwd), 'exit': child.returncode,
                     'stdout': child.stdout.decode(), 'stderr': child.stderr.decode()})
    check(child.returncode == 0 and not child.stderr, 'actual command failed: ' + str(command))
    return child.stdout


def main():
    check(sys.flags.optimize == 0 and __debug__, 'assertions disabled')
    check(info(read(RESPONSE))['sha256'] == RESPONSE_HASH, 'wrong actual response')
    initial = pins(B / 'SHA256SUMS.initial')
    check(len(initial) == 118, 'wrong initial payload census')
    check(info(read(B / 'SHA256SUMS.initial'))['sha256'] == INITIAL_MANIFEST, 'initial seal changed')
    aliases = {'FINDINGS.json': 'FINDINGS.initial.json'}
    verify_rows(initial, B, aliases)
    check(read(B / 'REPORT.md') == read(B / 'REPORT.initial.md'), 'initial report changed')
    initial_findings = json.loads(read(B / 'FINDINGS.initial.json'))
    check(initial_findings['accepted_delta'] is False and not initial_findings['findings'], 'not initial finding record')
    freeze_rows = pins(FREEZE / 'SHA256SUMS')
    check(len(freeze_rows) == 105, 'wrong freeze payload census')
    check(info(read(FREEZE / 'SHA256SUMS'))['sha256'] == FREEZE_HASH, 'wrong frozen manifest')
    actual_freeze = {str(p.relative_to(FREEZE)) for p in FREEZE.rglob('*') if p.is_file()}
    check(actual_freeze == set(dict(freeze_rows)) | {'SHA256SUMS'}, 'freeze has missing/extra files')
    verify_rows(freeze_rows, FREEZE)
    verify_rows(freeze_rows, PAPER)
    freeze_pins = pins(B / 'INPUT_PINS.sha256')
    check(len(freeze_pins) == 106, 'wrong initial freeze pins')
    check(set(dict(freeze_pins)) == {str((FREEZE / n).relative_to(BASE)) for n in actual_freeze}, 'freeze pin paths incomplete')
    verify_rows(freeze_pins, BASE)
    groups = {}
    for name, count in [('CONTEXT_PINS.sha256', 144), ('SUPPLEMENTAL_READ_PINS.sha256', 7), ('PAGE_VIEW_PINS.sha256', 7)]:
        rows = pins(B / name)
        check(len(rows) == count, 'wrong context count: ' + name)
        verify_rows(rows, BASE)
        groups[name] = rows
    verify_rows(pins(B / 'cold_build_01/SOURCE_INPUTS.sha256'), B / 'cold_build_01')
    receipt = json.loads(read(REPLAY / 'RECEIPT.json'))
    check(receipt['pass'] is True and receipt['failure'] is None and receipt['package_unchanged'] is True, 'root receipt failed')
    check(receipt['review'] == str(B), 'wrong review path')
    check(receipt['structural_checks'] == {'complete_nonself_package_entries': 118, 'exact_freeze_inputs': 106}, 'wrong root structural census')
    snapshot = receipt['before_package_files']
    check(snapshot == receipt['after_package_files'] and len(snapshot) == 119, 'root snapshots unequal')
    check(set(snapshot) == set(dict(initial)) | {'SHA256SUMS'}, 'root original inventory mismatch')
    historical_aliases = {'FINDINGS.json': 'FINDINGS.initial.json', 'SHA256SUMS': 'SHA256SUMS.initial'}
    for name, expected in snapshot.items():
        check(info(read(B / historical_aliases.get(name, name))) == expected, 'root snapshot differs: ' + name)
    check(info(read(REPLAY / 'harness_input.py')) == receipt['harness'], 'root harness pin differs')
    check(read(UTILITY) == read(REPLAY / 'harness_input.py'), 'live/copied root utility differs')
    check(info(read(Path(receipt['python']['executable']))) == receipt['python']['file'], 'runtime binary differs')
    check(receipt['python_flags'] == ['-I', '-B'], 'wrong recorded flags')
    check(receipt['environment_overrides'] == {'LC_ALL':'C', 'PYTHONDONTWRITEBYTECODE':'1', 'PYTHONHASHSEED':'0', 'PYTHONSAFEPATH':'1', 'TZ':'UTC'}, 'wrong overrides')
    check(read(REPLAY / 'verify.py') == read(B / 'verify.py'), 'root verifier differs')
    canonical = read(B / 'CANONICAL.json')
    check(info(canonical) == {'sha256': CANONICAL_HASH, 'bytes': 1558382}, 'wrong canonical')
    check(read(REPLAY / 'CANONICAL.json') == canonical, 'root canonical differs')
    stems = ['SHA256SUMS.before', 'INPUT_PINS.sha256.before', 'CONTEXT_PINS.sha256.before',
             'python_version', 'python_runtime_flags', 'python_link_dependencies', 'run1',
             'run1.cmp', 'run2', 'run2.cmp', 'pair.cmp', 'INPUT_PINS.sha256.after',
             'CONTEXT_PINS.sha256.after', 'SHA256SUMS.after']
    check(len(receipt['commands']) == len(stems) == 14, 'wrong root command census')
    expected_pins = {'SHA256SUMS': initial, 'INPUT_PINS.sha256': freeze_pins,
                     'CONTEXT_PINS.sha256': groups['CONTEXT_PINS.sha256']}
    for row, stem in zip(receipt['commands'], stems):
        stdout = read(REPLAY / (stem + '.stdout'))
        stderr = read(REPLAY / (stem + '.stderr'))
        check(row['exit'] == 0 and not stderr, 'root command failed: ' + stem)
        check(row['stdout'] == info(stdout) and row['stderr'] == info(stderr), 'root raw stream mismatch')
        if stem.endswith(('.before', '.after')):
            name = stem.rsplit('.', 1)[0]
            expected_stdout = ''.join(n + ': OK\n' for n, _ in expected_pins[name]).encode()
            check(stdout == expected_stdout, 'root pin output incomplete')
            check(row['command'] == ['sha256sum', '-c', str(B / name)], 'wrong root pin command')
            check(row['cwd'] == str(B if name == 'SHA256SUMS' else BASE), 'wrong root pin cwd')
        else:
            check(row['cwd'] == str(REPLAY), 'wrong root command cwd')
        if stem in ('run1', 'run2'):
            check(row['command'] == [receipt['python']['executable'], '-I', '-B', str(REPLAY / 'verify.py')], 'wrong actual producer command')
            parsed = json.loads(stdout)
            check(parsed['assertions'] == 2158999 and parsed['status'] == 'PASS', 'wrong root math result')
            check(stdout == canonical, 'root output not raw canonical')
        if stem.endswith('.cmp'):
            left, right = ((REPLAY / 'run1.stdout', REPLAY / 'run2.stdout') if stem == 'pair.cmp'
                           else (REPLAY / 'CANONICAL.json', REPLAY / (stem.split('.')[0] + '.stdout')))
            check(row['command'] == ['cmp', str(left), str(right)] and not stdout, 'wrong root byte comparison')
    flags = json.loads(read(REPLAY / 'python_runtime_flags.stdout'))
    check(flags == {'debug':True, 'ignore_environment':1, 'isolated':1, 'no_user_site':1, 'optimize':0}, 'root actual flags fail')
    check(receipt['commands'][3]['command'] == [receipt['python']['executable'], '-I', '-B', '--version'], 'version command differs')
    check(receipt['commands'][4]['command'][:4] == [receipt['python']['executable'], '-I', '-B', '-c'], 'probe command differs')
    check(receipt['commands'][5]['command'] == ['ldd', receipt['python']['executable']], 'ldd command differs')
    check(receipt['runs'] == [{'assertions':2158999, 'empty_stderr':True, 'label':label, 'producer_status':'PASS'} for label in ('run1','run2')], 'root run fields differ')
    for p in REPLAY.rglob('*'):
        if p.is_file():
            read(p)
    audit_present = UTILITY_AUDIT.is_file()
    if audit_present:
        read(UTILITY_AUDIT)
    read(Path(__file__))
    for name in ['INPUT_PINS.sha256', 'CONTEXT_PINS.sha256', 'SUPPLEMENTAL_READ_PINS.sha256', 'PAGE_VIEW_PINS.sha256']:
        execute(['sha256sum', '-c', str(B / name)], BASE)
    execute(['sha256sum', '-c', str(FREEZE / 'SHA256SUMS')], FREEZE)
    execute(['sha256sum', '-c', str(FREEZE / 'SHA256SUMS')], PAPER)
    for left, right in [(REPLAY/'run1.stdout', B/'CANONICAL.json'), (REPLAY/'run2.stdout', B/'CANONICAL.json'),
                        (REPLAY/'run1.stdout', REPLAY/'run2.stdout'), (B/'INPUT_PINS.sha256', B/'INPUT_PINS.after.sha256'),
                        (B/'REPORT.md', B/'REPORT.initial.md'), (B/'cold_build_01/main.pdf', FREEZE/'main.pdf')]:
        execute(['cmp', str(left), str(right)], BASE)
    before = dict(CONSUMED)
    after = {}
    for key in before:
        path = Path(key) if Path(key).is_absolute() else BASE / key
        after[key] = info(path.read_bytes())
        check(after[key] == before[key], 'dependency changed during delta audit: ' + key)
    print(json.dumps({'kind':'ACTUAL_READ_ONLY_B_DELTA_INTEGRITY_AUDIT_NOT_NEW_MATHEMATICS_OR_VIEWS',
                      'utc':datetime.now(timezone.utc).isoformat(), 'pass':True, 'checks':CHECKS,
                      'counts':{'initial_payload':118,'root_initial_physical_package':119,'freeze_physical':106,
                                'live_scientific':105,'context':144,'supplement':7,'page_pins':7,
                                'root_commands':14,'root_new_runs':2,'assertions_per_root_run':2158999},
                      'historical_aliases':historical_aliases,'utility_audit_present':audit_present,
                      'consumed_inputs_before':before,'consumed_inputs_after':after,
                      'actual_delta_commands':COMMANDS}, sort_keys=True, indent=2))


if __name__ == '__main__':
    main()
