#!/usr/bin/env python3
"""Independent physical Round2 receiver; never imports the freezer or science."""
from collections import Counter
from pathlib import Path
import hashlib
import json
import os
import re
import subprocess
import sys
import traceback
from urllib.parse import unquote

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
QA = ROOT / 'docs/papers204_208_sequence/qa'
P = ROOT / 'papers/210-weakly-increasing-run-aggregation'
R1, R2 = P / 'frozen_round1', P / 'frozen_round2'
B = ROOT / 'docs/papers204_208_sequence/reviews/p210_b'
PAIR = QA / 'root_replays/p210_b_strict_pair_01'
PREP = QA / 'p210_round2_preparation'
OUT = QA / 'p210_round2_root_reception'
R1_SEAL = 'be54b79806d90f22037cee877f92074e744b2ef27bcc0b6b2e4f8dfa658446e0'
AUTHOR_SEAL = 'b0c72e401acaf50acb611dc27f2ff1c45e3ad6e1b547218b48d13be8c82a0f6c'
PAIR_SEAL = '54cdd8ca9a00374f53a82e7f84a47fdd91f3fcde8b1519b027b98c7925ace181'
INITIAL_B_SEAL = '81b5f97a6b25d6f9e82db87001da1a54668c01268038694d4b8a3b61006b02c3'
INITIAL_FINDINGS = '0db9eea2a59a6bfb01b5ce3dbd57c84aa2cb84ab4ac952e2a72829a3f56f5bbb'
INITIAL_DELTA = '6b59ce7b8f12206a5fe9f761e1aa1d3990c8fa66451961cd9645db63d5d9d618'
ENV = {'PATH': '/usr/bin:/bin', 'LANG': 'C.UTF-8', 'LC_ALL': 'C.UTF-8', 'TZ': 'UTC'}
ROLE_ANCHORS = {
    'round1_manifest': 'ROUND1_CORE_MANIFEST.sha256',
    'review_manifest': 'B_REVIEW_MANIFEST.sha256',
    'accepted_delta': 'B_ACCEPTED_DELTA.md',
    'initial_findings': 'B_INITIAL_FINDINGS.json',
    'current_findings': 'B_CURRENT_FINDINGS.json',
    'review_input_pins': 'B_INPUT_PINS.sha256',
    'response': 'ROOT_B_RESPONSE.md',
    'root_final_closure': 'ROOT_B_FINAL_CLOSURE.json',
    'root_pair_manifest': 'ROOT_B_PAIR_MANIFEST.sha256',
    'prior_whole_manifest': 'PRE_ROUND2_PAPER_MANIFEST.sha256',
    'prior_lifecycle': 'PRE_ROUND2_ROOT_LIFECYCLE.md',
    'initial_review_manifest': 'B_INITIAL_REVIEW_MANIFEST.sha256',
    'initial_delta': 'B_INITIAL_DELTA.md',
}
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

def selected(document, selector):
    need(isinstance(selector, list) and selector, 'literal nonempty selected actual field')
    for key in selector:
        need((isinstance(document, dict) and type(key) is str and key in document) or
             (isinstance(document, list) and type(key) is int and 0 <= key < len(document)), 'exact existing JSON field/index')
        document = document[key]
    return document


def accepted_roles(binding):
    need(binding['schema'] == 'p210-round2-actual-final-b-binding-v1' and binding['paper'] == 'P210' and
         binding['bound_by'] == '/root' and binding['status'] == 'BOUND_AFTER_ACTUAL_B_ACCEPTANCE_AND_ROOT_FINAL_CLOSURE',
         'actually supplied final B binding, never initial pending or a template')
    roles = binding['roles']
    need(set(roles) == set(ROLE_ANCHORS), 'thirteen actual pinned source roles')
    for name, role in roles.items():
        data = read(Path(role['path']))
        need(len(data) == role['bytes'] and hashlib.sha256(data).hexdigest() == role['sha256'], 'full actual role pin: ' + name)
    need(roles['round1_manifest']['path'] == str(R1 / 'SHA256SUMS') and roles['round1_manifest']['sha256'] == R1_SEAL and
         roles['review_manifest']['path'] == str(B / 'SHA256SUMS') and roles['root_pair_manifest']['path'] == str(PAIR / 'SHA256SUMS') and
         roles['root_pair_manifest']['sha256'] == PAIR_SEAL and roles['initial_review_manifest']['sha256'] == INITIAL_B_SEAL and
         roles['initial_findings']['path'] == str(B / 'FINDINGS.json') and
         roles['initial_findings']['sha256'] == INITIAL_FINDINGS and roles['initial_delta']['sha256'] == INITIAL_DELTA,
         'original role identities unchanged')
    current = load(Path(roles['current_findings']['path']))
    root = load(Path(roles['root_final_closure']['path']))
    reviewer_expected = {'reviewer': '/root/p210_b_reviewer', 'accepted_delta': binding['reviewer_acceptance_value'],
                         'open_critical': 0, 'open_major': 0, 'open_minor': 0}
    root_expected = {'paper': 'P210', 'input_round': 1, 'reviewer_delta_accepted': True,
        'root_original_inspection_complete': True, 'root_replay_closure_complete': True,
        'current_open_findings': 0, 'unchanged_author_payloads': 489, 'unchanged_round1_payloads': 508,
        'initial_review_payloads_preserved': 407, 'author_manifest_sha256': AUTHOR_SEAL,
        'round1_manifest_sha256': R1_SEAL, 'review_manifest_entries': binding['review_manifest_entries']}
    for name, role in {'review_manifest_sha256': 'review_manifest', 'delta_sha256': 'accepted_delta',
            'findings_sha256': 'initial_findings', 'current_findings_sha256': 'current_findings',
            'response_sha256': 'response', 'root_pair_manifest_sha256': 'root_pair_manifest',
            'prior_whole_manifest_sha256': 'prior_whole_manifest', 'prior_lifecycle_sha256': 'prior_lifecycle'}.items():
        root_expected[name] = roles[role]['sha256']
    for label, obj, expected in [('reviewer', current, reviewer_expected), ('root', root, root_expected)]:
        for key, value in expected.items():
            observed = selected(obj, binding['selectors'][label + '.' + key])
            need(type(observed) is type(value) and observed == value, 'actual accepted semantic role: ' + label + '.' + key)
    evidence = selected(root, binding['selectors']['root.evidence'])
    need(isinstance(evidence, dict) and len(evidence) >= 2, 'actual root evidence map')
    for path, value in evidence.items():
        need(digest(Path(path)) == value, 'actual root final evidence referent')
    return roles


def markdown_hrefs(path):
    return [href for raw in re.findall(r'\[[^\]]*\]\(([^)]+)\)', read(path).decode())
            if (href := raw.strip().strip('<>')) and not href.startswith(('https://', 'http://', 'mailto:', '#'))
            and href.split('#', 1)[0]]


def exact_links(core, binding, provenance):
    old = load(R1 / 'ROUND1_PROVENANCE.json')
    prior = old['round1_core_link_map'] + old['acceptance_anchor_link_map']
    need(len(prior) == 71 and old['round0_external_aliases'] == [], 'original71 explicitly recorded R1 links')
    seen = Counter((name, href) for name in core if name.endswith('.md') for href in markdown_hrefs(R1 / name))
    need(seen == Counter((row['document'], row['href']) for row in prior), 'complete actual core link occurrence census')
    mapped = []
    for row in prior:
        original = Path(row['physical_target'])
        need(digest(original) == row['sha256'], 'unchanged original R1 mapped target')
        inside = original.is_relative_to(R1)
        physical_target = R2 / original.relative_to(R1) if inside else original
        mapped.append(dict(document=row['document'], document_sha256=core[row['document']], href=row['href'],
            round1_physical_target=str(original), physical_target=str(physical_target), sha256=row['sha256'],
            mode='physical-unchanged-Round1-copy' if inside else 'unchanged-exact-external-role', previous_role=row))
    need(mapped == provenance['round2_historical_link_map'], 'all original roles migrated exactly once, not guessed origins')
    origins = {(str(R1 / name), value): R2 / name for name, value in core.items()}
    for name, value in core.items():
        if (P / name).is_file():
            need(digest(P / name) == value, 'live named core byte identity')
            origins[(str(P / name), value)] = R2 / name
    origins[(str(P / 'SHA256SUMS'), AUTHOR_SEAL)] = R2 / 'AUTHOR_MANIFEST.sha256'
    for role in provenance['anchors'].values():
        origins[(role['original_path'], role['sha256'])] = R2 / role['physical_path']
    anchors = []
    for role, origin_name in binding['markdown_origins'].items():
        name, source = ROLE_ANCHORS[role], Path(binding['roles'][role]['path'])
        for href in markdown_hrefs(source):
            original = (Path(origin_name).parent / unquote(href.split('#', 1)[0])).resolve()
            need(original.is_relative_to(ROOT) and original.is_file(), 'actual file target at the exact supplied origin')
            value = digest(original)
            target = origins.get((str(original), value), original)
            anchors.append(dict(document='ROUND2_ACCEPTANCE/' + name, source_bytes_path=str(source),
                original_document=origin_name, href=href, original_target=str(original), physical_target=str(target),
                sha256=value, mode='explicit-current-core-or-anchor' if target != original else 'exact-current-original-document-origin'))
    need(anchors == provenance['acceptance_anchor_link_map'], 'entire new anchor link map independently rebuilt')
    all_rows = mapped + anchors
    actual = Counter((name, href) for name in physical(R2) if name.endswith('.md') for href in markdown_hrefs(R2 / name))
    need(actual == Counter((row['document'], row['href']) for row in all_rows), 'all actual final Markdown links covered, no omitted document')
    for row in all_rows:
        need(digest(Path(row['physical_target'])) == row['sha256'], 'all current physical final link bytes')
    need(provenance['round0_external_original_pins'] == old['round0_external_original_pins'] and
         len(old['round0_external_original_pins']) == 33, 'all33 original external key roles')
    for path, value in old['round0_external_original_pins'].items():
        need(digest(Path(path)) == value, 'every unchanged original external byte key')
    return len(mapped), len(anchors)


def main():
    need(len(sys.argv) == 12 and sys.argv[1] == 'inspect-round2' and
         sys.argv[2] == '--final-b-binding' and sys.argv[4] == '--expected-final-b-binding-sha256' and
         sys.argv[6] == '--expected-preparation-sha256' and sys.argv[8] == '--freeze-completion' and
         sys.argv[10] == '--expected-freeze-completion-sha256', 'explicit actual binding/preparation/native completion')
    binding_path, binding_hash, prep_hash = Path(sys.argv[3]), sys.argv[5], sys.argv[7]
    completion_path, completion_hash = Path(sys.argv[9]), sys.argv[11]
    need(Path(__file__).resolve() == PREP / 'inspect_p210_round2.py' and Path.cwd() == ROOT and
         sys.flags.isolated and sys.flags.no_site and sys.flags.dont_write_bytecode and sys.flags.optimize == 0 and
         Path(sys.executable).resolve() == Path('/usr/bin/python3.10'), 'fixed separate read-only source/interpreter')
    need(set(os.environ) == set(ENV) and all(os.environ[k] == v for k, v in ENV.items()), 'exact safe ENV4 only')
    need(sys.pycache_prefix == str(OUT / 'never_created_receiver_cache') and not os.path.lexists(sys.pycache_prefix) and
         not os.path.lexists(OUT), 'absent exact receiver output/cache; never replace')
    for value in (binding_hash, prep_hash, completion_hash):
        need(re.fullmatch('[0-9a-f]{64}', value) is not None, 'explicit real SHA256')
    need(binding_path.is_absolute() and binding_path.is_relative_to(QA) and
         not binding_path.is_relative_to(PREP) and binding_path.name == 'FINAL_B_BINDING.json' and
         digest(binding_path) == binding_hash, 'actual external final-B binding identity')
    binding = load(binding_path)
    roles = accepted_roles(binding)
    need(digest(completion_path) == completion_hash, 'actual root native completion exact bytes')
    completed = load(completion_path)
    result = completed['result']
    need(type(result['exit_code']) is int and result['exit_code'] == 0, 'actual root freezer native zero')
    actual = json.loads(result['output'])
    need(actual['status'] == 'PASS_PHYSICAL_P210_ROUND2' and actual['payloads'] == 524 and
         actual['physical_files'] == 525 and actual['actual_final_b_binding_sha256'] == binding_hash and
         actual['preparation_sha256'] == prep_hash, 'actual physical result with exact prior acceptance, not proposed census')
    core = package(R1, R1_SEAL, 508)
    frozen = package(R2, actual['manifest_sha256'], 524)
    review = package(B, roles['review_manifest']['sha256'], binding['review_manifest_entries'])
    package(PAIR, PAIR_SEAL, 59)
    prep = package(PREP, prep_hash, len(rows(PREP / 'SHA256SUMS')))
    provenance = load(R2 / 'ROUND2_PROVENANCE.json')
    need(provenance['schema'] == 'p210-round2-provenance-v1' and provenance['core_payload_pins'] == core and
         provenance['round1_core_payloads_copied'] == 508 and provenance['author_payloads_preserved'] == 489 and
         provenance['acceptance_anchor_payloads'] == 14, 'exact core/author/anchor census')
    need(provenance['actual_final_b_binding'] == binding and provenance['actual_final_b_binding_sha256'] == binding_hash and
         provenance['preparation_sha256'] == prep_hash and provenance['round1_external_aliases'] == [], 'exact actual binding and no global aliases')
    expected, raw_comparisons = dict(core), 0
    for name, value in core.items():
        need(frozen[name] == value and read(R1 / name) == read(R2 / name), 'all508 complete original core bytes: ' + name)
        raw_comparisons += 1
    expected_anchor_sources = {name: roles[role]['path'] for role, name in ROLE_ANCHORS.items()}
    expected_anchor_sources['FINAL_B_BINDING.json'] = str(binding_path)
    need(set(provenance['anchors']) == set(expected_anchor_sources), 'only fourteen small actual history/acceptance anchors')
    for name, role in provenance['anchors'].items():
        target = R2 / role['physical_path']
        need(role['physical_path'] == 'ROUND2_ACCEPTANCE/' + name and role['original_path'] == expected_anchor_sources[name],
             'exact acceptance role source/physical target')
        need(read(Path(role['original_path'])) == read(target) and digest(target) == role['sha256'], 'complete anchor source/copy bytes: ' + name)
        expected[role['physical_path']] = role['sha256']
        raw_comparisons += 1
    source = PREP / 'freeze_p210_round2.py'
    need(digest(source) == actual['freezer_sha256'] == provenance['freezer_sha256'] and
         read(source) == read(R2 / 'ROUND2_FREEZE_ADAPTER.py'), 'exact executed source and complete physical copy')
    raw_comparisons += 1
    expected['ROUND2_FREEZE_ADAPTER.py'] = digest(source)
    expected['ROUND2_PROVENANCE.json'] = digest(R2 / 'ROUND2_PROVENANCE.json')
    need(frozen == expected and raw_comparisons == 523, 'all and only524 payloads and523 actual source/copy comparisons')
    initial = rows(Path(roles['initial_review_manifest']['path']))
    need(len(initial) == 407 and provenance['initial_review_aliases'] == binding['initial_review_aliases'] and
         set(binding['initial_review_aliases']) <= {'DELTA.md'}, 'initial DELTA role only; other406 same-path initial payloads')
    for name, value in initial.items():
        physical_name = binding['initial_review_aliases'].get(name, name)
        need(review.get(physical_name) == value and digest(B / physical_name) == value, 'every407 initial B payload retained')
    reviewed = rows(Path(roles['review_input_pins']['path']))
    expected_reviewed = {str((R1 / name).relative_to(ROOT)): value for name, value in core.items()}
    expected_reviewed[str((R1 / 'SHA256SUMS').relative_to(ROOT))] = R1_SEAL
    need(reviewed == expected_reviewed, 'all509 actual B starting Round1 inputs')
    core_links, anchor_links = exact_links(core, binding, provenance)
    for path, value in provenance['accepted_review_and_root_manifest_referents'].items():
        need(digest(Path(path)) == value, 'entire accepted B/rootpair file referent, no nested host expansion')
    for path, value in provenance['full_source_input_pins_before_and_reread_after'].items():
        read(Path(path))
        need(PINS[path] == value, 'every actual original consumed freezer key')
    old = rows(R2 / 'ROUND2_ACCEPTANCE/PRE_ROUND2_PAPER_MANIFEST.sha256')
    need(len(old) == 1496 and old == provenance['prior_whole_manifest']['original_referent_pins'] and
         provenance['prior_whole_manifest']['complete_before_creation_only'] is True and
         provenance['prior_whole_manifest']['current_whole_manifest_after_creation'] is False, 'old whole manifest is prior-scope only')
    for name, value in old.items():
        need(digest(P / name) == value, 'unchanged original whole-paper referent before lifecycle refresh')
    need(physical(P) == set(old) | {'PAPER_MANIFEST.sha256'} | {'frozen_round2/' + name for name in physical(R2)},
         'exact extended current paper membership, not a refreshed whole manifest')
    for base in (R1, R2, B, PAIR, PREP):
        native(['/usr/bin/sha256sum', '--check', 'SHA256SUMS'], base)
    native(['/usr/bin/cmp', str(R2 / 'AUTHOR_MANIFEST.sha256'), str(P / 'AUTHOR_MANIFEST.sha256')], ROOT)
    before = dict(PINS)
    for path, value in before.items():
        read(Path(path))
        need(PINS[path] == value, 'final complete uncached unchanged input key')
    report = dict(status='PASS_ROOT_PHYSICAL_P210_ROUND2_RECEPTION', checks=CHECKS,
        current_input_count=len(PINS), complete_input_pins=PINS, actual_native_commands=NATIVES,
        payloads=524, physical_files=525, core_payloads=508, author_payloads=489, acceptance_anchors=14,
        full_raw_copy_comparisons=raw_comparisons, core_links=core_links, anchor_links=anchor_links,
        round0_external_originals=33, round2_manifest_sha256=actual['manifest_sha256'],
        actual_final_b_binding_sha256=binding_hash, actual_freeze_completion_sha256=completion_hash,
        current_open_findings=0, no_science_build_view_review_execution=True,
        limits='Physical documentary reception only. Initial407 B and inherited A/failure history retained. Old1496 complete before Round2 only. Later lifecycle/whole refresh, terminal build/view and paper/five-paper gates remain.')
    need(not os.path.lexists(OUT), 'new receiver output remains absent before exclusive creation')
    OUT.mkdir()
    data = (json.dumps(report, sort_keys=True, indent=2) + '\n').encode()
    with (OUT / 'ROOT_RECEPTION.json').open('xb') as f:
        f.write(data)
    seal = (hashlib.sha256(data).hexdigest() + '  ROOT_RECEPTION.json\n').encode()
    with (OUT / 'SHA256SUMS').open('xb') as f:
        f.write(seal)
    need((OUT / 'ROOT_RECEPTION.json').read_bytes() == data, 'actual complete result stored unchanged')
    summary = {k: v for k, v in report.items() if k not in ('complete_input_pins', 'actual_native_commands')}
    summary.update(native_commands_all_zero=len(NATIVES), full_result_path=str(OUT / 'ROOT_RECEPTION.json'),
                   root_reception_manifest_sha256=hashlib.sha256(seal).hexdigest())
    print(json.dumps(summary, sort_keys=True, indent=2))


if __name__ == '__main__':
    try:
        main()
    except BaseException:
        print(json.dumps(dict(status='FAIL_ROOT_PHYSICAL_P210_ROUND2_RECEPTION_NO_ACCEPTANCE',
            traceback=traceback.format_exc(), checks_completed=CHECKS, actual_native_commands=NATIVES,
            known_input_pins=PINS, no_rollback_or_retry=True), sort_keys=True, indent=2))
        raise SystemExit(1)
