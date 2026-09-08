#!/usr/bin/env python3
"""Root physical Round1 reception only; no science/build/view or lifecycle write."""
from pathlib import Path
import hashlib
import json
import re
import subprocess
import sys

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
QA = ROOT / 'docs/papers204_208_sequence/qa'
P = ROOT / 'papers/210-weakly-increasing-run-aggregation'
R0, R1 = P / 'frozen_round0', P / 'frozen_round1'
A = ROOT / 'docs/papers204_208_sequence/reviews/p210_a'
PAIR = QA / 'root_replays/p210_a_strict_pair_01'
PREP = QA / 'p210_round1_preparation'
ENV = {'PATH': '/usr/bin:/bin', 'LANG': 'C.UTF-8', 'LC_ALL': 'C.UTF-8', 'TZ': 'UTC'}
PINS, NATIVES = {}, []
CHECKS = 0


def need(value, message):
    global CHECKS
    CHECKS += 1
    if not value:
        raise AssertionError(message)


def read(path):
    path = Path(path)
    need(path.is_absolute() and path.is_file() and not path.is_symlink() and path.resolve() == path, 'exact regular path ' + str(path))
    data = path.read_bytes()
    key = {'sha256': hashlib.sha256(data).hexdigest(), 'size': len(data), 'real': str(path), 'symlink': None}
    need(str(path) not in PINS or PINS[str(path)] == key, 'same input during reception ' + str(path))
    PINS[str(path)] = key
    return data


def digest(path):
    return hashlib.sha256(read(path)).hexdigest()


def load(path):
    return json.loads(read(path))


def rows(path):
    data = read(path)
    need(data.endswith(b'\n'), 'manifest final newline')
    result = {}
    for line in data.decode().splitlines():
        match = re.fullmatch(r'([0-9a-f]{64})  (.+)', line)
        need(match is not None, 'exact manifest format')
        value, name = match.groups()
        p = Path(name)
        need(not p.is_absolute() and '..' not in p.parts and p.as_posix() == name and name not in result, 'safe unique manifest name')
        result[name] = value
    return result


def physical(base):
    found = list(base.rglob('*'))
    need(all(not p.is_symlink() for p in found), 'bounded package no symlinks')
    return {p.relative_to(base).as_posix() for p in found if p.is_file()}


def package(base, seal, count):
    need(digest(base / 'SHA256SUMS') == seal, 'exact accepted seal ' + str(base))
    result = rows(base / 'SHA256SUMS')
    need(len(result) == count and physical(base) == set(result) | {'SHA256SUMS'}, 'complete nonself package ' + str(base))
    for name, value in result.items():
        need(digest(base / name) == value, 'complete payload ' + name)
    return result


def native(argv, cwd):
    p = subprocess.run(argv, cwd=cwd, env=ENV, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=60)
    NATIVES.append({'argv': argv, 'cwd': str(cwd), 'environment': ENV, 'exit': p.returncode,
                    'stdout_utf8': p.stdout.decode(), 'stderr_utf8': p.stderr.decode(),
                    'stdout_sha256': hashlib.sha256(p.stdout).hexdigest(), 'stderr_sha256': hashlib.sha256(p.stderr).hexdigest()})
    need(p.returncode == 0 and not p.stderr, 'actual full native checksum/raw comparison')


def main():
    need(Path.cwd() == ROOT and sys.flags.no_site and sys.flags.dont_write_bytecode and sys.flags.optimize == 0, 'root read-only source execution')
    digest(Path(__file__).resolve())
    completed = load(QA / 'P210_ROUND1_ROOT_FREEZE_COMPLETION.actual.json')
    result = completed['result']
    need(result['exit_code'] == 0, 'actual root freezer completed native zero')
    actual = json.loads(result['output'])
    need(actual['status'] == 'PASS_PHYSICAL_P210_ROUND1' and actual['payloads'] == 508 and actual['physical_files'] == 509, 'actual physical result not static proposal')
    need(actual['accepted_root_closure_sha256'] == '38e5ca5009a583f5b126a29b60a98d9a936e28cf62d4c800310b98fec49d1650', 'actual accepted-A root gate')
    core = package(R0, 'e8446cd17b1a283c74f9a6b4ced413b9e30810396c3d30f936ac2986ce790e26', 493)
    frozen = package(R1, actual['manifest_sha256'], 508)
    package(A, 'f6b92663cb2a7909f85a25a892ee4433ccd6177e84c07bf7ceccc9555b191f6d', 552)
    package(PAIR, '9b30c2a3fc93874e4eaafdec345d9894f95aa36b7e9d764bd54646cfe5c7d6fb', 59)
    package(PREP, 'b0d105ac1d40785cb9e3e4cf4ca0d299dd4f3df6cfba1f429ff3aafd8dfda7e3', 6)
    provenance = load(R1 / 'ROUND1_PROVENANCE.json')
    need(provenance['schema'] == 'p210-round1-provenance-v1' and provenance['core_payload_pins'] == core, 'all unchanged core roles')
    need(provenance['author_payloads_preserved'] == 489 and provenance['round0_core_payloads_copied'] == 493 and provenance['acceptance_anchor_payloads'] == 13, 'exact copied role counts')
    need(provenance['round0_external_aliases'] == [], 'no generic historical fallback')
    need(len(provenance['anchors']) == 13 and len(provenance['round1_core_link_map']) == 57 and len(provenance['acceptance_anchor_link_map']) == 14, 'complete link and anchor maps')
    expected = dict(core)
    raw_comparisons = 0
    for name, value in core.items():
        need(frozen[name] == value and read(R0 / name) == read(R1 / name), 'complete original core bytes ' + name)
        raw_comparisons += 1
    for name, role in provenance['anchors'].items():
        target = R1 / role['physical_path']
        need(role['physical_path'] == 'ROUND1_ACCEPTANCE/' + name, 'exact physical acceptance path')
        need(read(Path(role['original_path'])) == read(target) and digest(target) == role['sha256'], 'complete current acceptance anchor bytes ' + name)
        expected[role['physical_path']] = role['sha256']
        raw_comparisons += 1
    source = PREP / 'freeze_p210_round1.py'
    need(digest(source) == actual['freezer_sha256'] == '2be483fc6a03be1e64bce7f800a301a0e5b398fa6107cb4678c5c891eb5b23fd', 'exact actually executed source')
    need(read(source) == read(R1 / 'ROUND1_FREEZE_ADAPTER.py'), 'physical freezer copy full bytes')
    raw_comparisons += 1
    expected['ROUND1_FREEZE_ADAPTER.py'] = digest(source)
    expected['ROUND1_PROVENANCE.json'] = digest(R1 / 'ROUND1_PROVENANCE.json')
    need(frozen == expected, 'all and only508 actual payloads')
    accepted = load(QA / 'P210_A_ROOT_DELTA_INSPECTION.actual.json')
    need(provenance['accepted_root_assertions'] == accepted and accepted['current_open_findings'] == 0 and accepted['resolved_major_findings'] == 1, 'exact actual census preserved')
    for path, value in provenance['round0_external_original_pins'].items():
        need(digest(Path(path)) == value, 'all33 original external roles')
    for role in provenance['round1_core_link_map'] + provenance['acceptance_anchor_link_map']:
        need(digest(Path(role['physical_target'])) == role['sha256'], 'all71 exact physical/original link targets')
    for path, value in provenance['accepted_review_and_root_manifest_referents'].items():
        need(digest(Path(path)) == value, 'all accepted A/rootpair referents')
    for path, value in provenance['full_source_input_pins_before_and_reread_after'].items():
        read(Path(path))
        need(PINS[path] == value, 'every actual freezer original full key')
    old = rows(R1 / 'ROUND1_ACCEPTANCE/PRE_ROUND1_PAPER_MANIFEST.sha256')
    need(len(old) == 987 and old == provenance['prior_whole_manifest']['original_referent_pins'], 'exact old987 membership no current whole claim')
    for name, value in old.items():
        need(digest(P / name) == value, 'unchanged pre-lifecycle old referent')
    need(physical(P) == set(old) | {'PAPER_MANIFEST.sha256'} | {'frozen_round1/' + name for name in physical(R1)}, 'exact extended paper tree before lifecycle update')
    for base in (R0, R1, A, PAIR, PREP):
        native(['/usr/bin/sha256sum', '--check', 'SHA256SUMS'], base)
    native(['/usr/bin/cmp', str(R1 / 'AUTHOR_MANIFEST.sha256'), str(P / 'AUTHOR_MANIFEST.sha256')], ROOT)
    before = dict(PINS)
    for path, value in before.items():
        read(Path(path))
        need(PINS[path] == value, 'final complete uncached original reread')
    report = {'status': 'PASS_ROOT_PHYSICAL_P210_ROUND1_RECEPTION', 'checks': CHECKS,
        'current_input_count': len(PINS), 'complete_input_pins': PINS, 'actual_native_commands': NATIVES,
        'payloads': 508, 'physical_files': 509, 'core_payloads': 493, 'author_payloads': 489,
        'acceptance_anchors': 13, 'full_raw_copy_comparisons': raw_comparisons,
        'core_links': 57, 'anchor_links': 14, 'round0_external_originals': 33,
        'round1_manifest_sha256': actual['manifest_sha256'], 'current_open_findings': 0,
        'resolved_major_findings': 1, 'limits': 'Physical documentary reception only; no new science/build/view/review. Old987 complete before Round1 only. Lifecycle/whole refresh and distinct B plus terminal/batch gates remain.'}
    out = QA / 'p210_round1_root_reception'
    need(not out.exists() and not out.is_symlink(), 'new root-only output, no overwrite')
    out.mkdir()
    data = (json.dumps(report, sort_keys=True, indent=2) + '\n').encode()
    with (out / 'ROOT_RECEPTION.json').open('xb') as f:
        f.write(data)
    seal = (hashlib.sha256(data).hexdigest() + '  ROOT_RECEPTION.json\n').encode()
    with (out / 'SHA256SUMS').open('xb') as f:
        f.write(seal)
    need((out / 'ROOT_RECEPTION.json').read_bytes() == data, 'new full actual result preserved byte exactly')
    summary = {k: v for k, v in report.items() if k not in ('complete_input_pins', 'actual_native_commands')}
    summary['native_commands_all_zero'] = len(NATIVES)
    summary['full_result_path'] = str(out / 'ROOT_RECEPTION.json')
    summary['root_reception_manifest_sha256'] = hashlib.sha256(seal).hexdigest()
    print(json.dumps(summary, sort_keys=True, indent=2))


if __name__ == '__main__':
    main()
