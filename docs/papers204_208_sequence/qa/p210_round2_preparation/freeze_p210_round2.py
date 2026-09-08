#!/usr/bin/env python3
"""One-time P210 Round2, disabled without an actual externally bound B closure.

Adapted from the accepted Round1 freezer; no old program is imported or run.
A binding contract is not an acceptance. All actual binding, role, manifest,
link and disk checks precede the first target mkdir. No live file is updated.
"""
from collections import Counter
from hashlib import sha256
import json
import os
from pathlib import Path
import re
import shutil
import sys
import traceback
from urllib.parse import unquote

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
BATCH = ROOT / 'docs/papers204_208_sequence'
QA = BATCH / 'qa'
PAPER = ROOT / 'papers/210-weakly-increasing-run-aggregation'
ROUND0, ROUND1 = PAPER / 'frozen_round0', PAPER / 'frozen_round1'
TARGET = PAPER / 'frozen_round2'
PREPARATION = QA / 'p210_round2_preparation'
REVIEW = BATCH / 'reviews/p210_b'
PAIR = QA / 'root_replays/p210_b_strict_pair_01'
AUTHOR_SEAL = 'b0c72e401acaf50acb611dc27f2ff1c45e3ad6e1b547218b48d13be8c82a0f6c'
ROUND0_SEAL = 'e8446cd17b1a283c74f9a6b4ced413b9e30810396c3d30f936ac2986ce790e26'
ROUND1_SEAL = 'be54b79806d90f22037cee877f92074e744b2ef27bcc0b6b2e4f8dfa658446e0'
INITIAL_B_SEAL = '81b5f97a6b25d6f9e82db87001da1a54668c01268038694d4b8a3b61006b02c3'
INITIAL_FINDINGS = '0db9eea2a59a6bfb01b5ce3dbd57c84aa2cb84ab4ac952e2a72829a3f56f5bbb'
INITIAL_DELTA = '6b59ce7b8f12206a5fe9f761e1aa1d3990c8fa66451961cd9645db63d5d9d618'
PAIR_SEAL = '54cdd8ca9a00374f53a82e7f84a47fdd91f3fcde8b1519b027b98c7925ace181'
B_CANONICAL = 'fbddce4cc05761bd0eed959d57b6de32b9cde38f23128872189a7e64349cfab2'
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
READ_PINS = {}
COMPARISONS = []


def require(value, message):
    if not value:
        raise AssertionError(message)


def file_bytes(path):
    path = Path(path)
    require(path.is_absolute() and path.is_file() and not path.is_symlink() and path.resolve() == path,
            'exact regular nonsymlink input path: ' + str(path))
    data = path.read_bytes()
    row = dict(sha256=sha256(data).hexdigest(), size=len(data), real=str(path.resolve()), symlink=None)
    key = str(path)
    require(key not in READ_PINS or READ_PINS[key] == row, 'input changed while freezing: ' + key)
    READ_PINS[key] = row
    return data


def digest(path):
    return sha256(file_bytes(path)).hexdigest()


def load(path):
    return json.loads(file_bytes(path))


def safe(name):
    path = Path(name)
    require(bool(name) and path.as_posix() == name and not path.is_absolute() and
            '..' not in path.parts and '.' not in path.parts, 'strict contained relative name')
    return path


def manifest_rows(path):
    data = file_bytes(path)
    require(data.endswith(b'\n'), 'complete manifest final newline')
    rows = {}
    for line in data.decode('utf-8').splitlines():
        match = re.fullmatch(r'([0-9a-f]{64})  (.+)', line)
        require(match is not None, 'strict manifest row')
        value, name = match.groups()
        safe(name)
        require(name not in rows, 'duplicate manifest name')
        rows[name] = value
    return rows


def read_manifest(path, base):
    rows = manifest_rows(path)
    for name, value in rows.items():
        require(digest(base / safe(name)) == value, 'manifest referent: ' + str(base / name))
    return rows


def physical(base):
    entries = list(base.rglob('*'))
    require(all(not path.is_symlink() for path in entries), 'no symlinks in exact bounded package: ' + str(base))
    return {path.relative_to(base).as_posix() for path in entries if path.is_file()}


def complete_manifest(base):
    rows = read_manifest(base / 'SHA256SUMS', base)
    require('SHA256SUMS' not in rows and physical(base) == set(rows) | {'SHA256SUMS'},
            'complete nonself bounded package: ' + str(base))
    return rows


def raw_equal(left, right, role):
    a, b = file_bytes(left), file_bytes(right)
    require(a == b, 'complete raw-byte equality: ' + role)
    COMPARISONS.append(dict(role=role, left=str(left), right=str(right), bytes=len(a),
                           method='complete Python bytes comparison; not a native cmp command', equal=True))

def select(value, selector):
    require(isinstance(selector, list) and selector and
            all(type(part) in (str, int) for part in selector), 'nonempty literal JSON selector, never code')
    for part in selector:
        require((isinstance(value, dict) and type(part) is str and part in value) or
                (isinstance(value, list) and type(part) is int and 0 <= part < len(value)),
                'actual selected JSON field/index must exist')
        value = value[part]
    return value


def binding_inputs(path, expected_hash):
    """This interface does not predict any final B filename or output schema."""
    path = Path(path)
    require(path.is_absolute() and path.is_relative_to(QA) and
            not path.is_relative_to(PREPARATION) and path.name == 'FINAL_B_BINDING.json',
            'externally supplied root-owned FINAL_B_BINDING.json outside sealed preparation')
    require(re.fullmatch('[0-9a-f]{64}', expected_hash) is not None and digest(path) == expected_hash,
            'actual binding required and explicitly hash-bound before creation')
    binding = load(path)
    require(binding['schema'] == 'p210-round2-actual-final-b-binding-v1' and binding['paper'] == 'P210' and
            binding['bound_by'] == '/root' and binding['status'] == 'BOUND_AFTER_ACTUAL_B_ACCEPTANCE_AND_ROOT_FINAL_CLOSURE',
            'not a placeholder, initial verdict, schema contract or prospective acceptance')
    roles = binding['roles']
    require(set(roles) == set(ROLE_ANCHORS), 'exact thirteen small actual source roles')
    fixed = {'round1_manifest': ROUND1 / 'SHA256SUMS', 'review_manifest': REVIEW / 'SHA256SUMS',
             'initial_findings': REVIEW / 'FINDINGS.json',
             'review_input_pins': REVIEW / 'INPUT_PINS.sha256', 'response': BATCH / 'P210_B_RESPONSE.md',
             'root_pair_manifest': PAIR / 'SHA256SUMS', 'prior_whole_manifest': PAPER / 'PAPER_MANIFEST.sha256',
             'prior_lifecycle': PAPER / 'ROOT_LIFECYCLE.md'}
    review_roles = {'accepted_delta', 'initial_findings', 'current_findings', 'initial_review_manifest', 'initial_delta'}
    for role, row in roles.items():
        require(set(row) == {'path', 'sha256', 'bytes'} and type(row['bytes']) is int and 0 < row['bytes'] <= 4 * 1024 * 1024,
                'literal small-file role pin; no nested inventory snapshot')
        source = Path(row['path'])
        require(source.is_absolute() and source.is_relative_to(ROOT), 'actual workspace role')
        require(role not in fixed or source == fixed[role], 'fixed actual role directory/name')
        require(role not in review_roles or source.is_relative_to(REVIEW), 'actual B role stays inside its review')
        require(role != 'root_final_closure' or
                (source.is_relative_to(QA) and not source.is_relative_to(PREPARATION) and source != path),
                'separate actual root final closure, no self-binding')
        data = file_bytes(source)
        require(len(data) == row['bytes'] and sha256(data).hexdigest() == row['sha256'], 'actual role byte pin: ' + role)
    for role, value in {'round1_manifest': ROUND1_SEAL, 'initial_review_manifest': INITIAL_B_SEAL,
                        'initial_findings': INITIAL_FINDINGS, 'initial_delta': INITIAL_DELTA,
                        'root_pair_manifest': PAIR_SEAL}.items():
        require(roles[role]['sha256'] == value, 'immutable actual earlier role: ' + role)
    require(roles['accepted_delta']['sha256'] != INITIAL_DELTA and
            roles['current_findings']['sha256'] != INITIAL_FINDINGS and
            roles['review_manifest']['sha256'] != INITIAL_B_SEAL, 'initial pending package cannot bind accepted B')
    require(type(binding['review_manifest_entries']) is int and 407 < binding['review_manifest_entries'] <= 10000,
            'actual final review cardinality, not an initial or unlimited host inventory')
    origins = binding['markdown_origins']
    require(set(origins) == {'accepted_delta', 'initial_delta', 'response', 'prior_lifecycle'},
            'exact four Markdown source-origin roles')
    for role, name in origins.items():
        origin = Path(name)
        expected = REVIEW / 'DELTA.md' if role == 'initial_delta' else Path(roles[role]['path'])
        require(origin == expected or (role == 'accepted_delta' and origin == REVIEW / 'DELTA.md'),
                'only actual source origin or disclosed original B DELTA origin')
    current = load(Path(roles['current_findings']['path']))
    accepted = load(Path(roles['root_final_closure']['path']))
    selectors = binding['selectors']
    value = binding['reviewer_acceptance_value']
    require(value is True or (type(value) is str and bool(value.strip())), 'actual accepted-state value supplied only by root')
    expected_review = {'reviewer': '/root/p210_b_reviewer', 'accepted_delta': value,
                       'open_critical': 0, 'open_major': 0, 'open_minor': 0}
    expected_root = {'paper': 'P210', 'input_round': 1, 'reviewer_delta_accepted': True,
        'root_original_inspection_complete': True, 'root_replay_closure_complete': True,
        'current_open_findings': 0, 'unchanged_author_payloads': 489, 'unchanged_round1_payloads': 508,
        'initial_review_payloads_preserved': 407, 'author_manifest_sha256': AUTHOR_SEAL,
        'round1_manifest_sha256': ROUND1_SEAL, 'review_manifest_entries': binding['review_manifest_entries']}
    for name, role in {'review_manifest_sha256': 'review_manifest', 'delta_sha256': 'accepted_delta',
            'findings_sha256': 'initial_findings', 'current_findings_sha256': 'current_findings',
            'response_sha256': 'response', 'root_pair_manifest_sha256': 'root_pair_manifest',
            'prior_whole_manifest_sha256': 'prior_whole_manifest', 'prior_lifecycle_sha256': 'prior_lifecycle'}.items():
        expected_root[name] = roles[role]['sha256']
    require(set(selectors) == {'reviewer.' + k for k in expected_review} |
            {'root.' + k for k in expected_root} | {'root.evidence'}, 'all and only required actual semantic selectors')
    for namespace, document, expected in [('reviewer', current, expected_review), ('root', accepted, expected_root)]:
        for name, expected_value in expected.items():
            observed = select(document, selectors[namespace + '.' + name])
            require(type(observed) is type(expected_value) and observed == expected_value,
                    'actual accepted semantic field: ' + namespace + '.' + name)
    evidence = select(accepted, selectors['root.evidence'])
    require(isinstance(evidence, dict) and len(evidence) >= 2, 'actual root evidence path/hash object')
    for name, value in evidence.items():
        p = Path(name)
        require(p.is_absolute() and p.is_relative_to(ROOT) and p not in
                {path, Path(roles['root_final_closure']['path'])}, 'no circular root/binding evidence')
        require(type(value) is str and re.fullmatch('[0-9a-f]{64}', value) is not None and
                digest(p) == value, 'all explicitly named actual root evidence pins')
    delta = file_bytes(Path(roles['accepted_delta']['path'])).decode()
    require(roles['response']['sha256'] in delta and 'ACCEPT' in delta.upper(),
            'actual accepted delta names this exact response digest')
    return binding


def core_inputs(binding):
    require(digest(ROUND1 / 'SHA256SUMS') == ROUND1_SEAL and
            digest(ROUND0 / 'SHA256SUMS') == ROUND0_SEAL, 'both earlier immutable freeze seals')
    core, original = complete_manifest(ROUND1), complete_manifest(ROUND0)
    require(len(core) == 508 and len(original) == 493 and all(core.get(k) == v for k, v in original.items()) and
            not any(part.startswith('frozen_round') for name in core for part in safe(name).parts),
            'exact508 nonnested Round1 core preserving493 original payloads')
    require(digest(PAPER / 'SHA256SUMS') == digest(PAPER / 'AUTHOR_MANIFEST.sha256') == AUTHOR_SEAL,
            'unchanged live author seals')
    author = read_manifest(PAPER / 'AUTHOR_MANIFEST.sha256', PAPER)
    require(len(author) == 489 and read_manifest(ROUND1 / 'AUTHOR_MANIFEST.sha256', ROUND1) == author,
            'exact489 unchanged author roles')
    for name in author:
        raw_equal(PAPER / name, ROUND1 / name, 'unchanged live/Round1 author: ' + name)
    roles = binding['roles']
    require(digest(PAPER / 'PAPER_MANIFEST.sha256') == roles['prior_whole_manifest']['sha256'] and
            digest(PAPER / 'ROOT_LIFECYCLE.md') == roles['prior_lifecycle']['sha256'],
            'actual bound pre-Round2 live documentary bytes')
    prior = read_manifest(PAPER / 'PAPER_MANIFEST.sha256', PAPER)
    require(len(prior) == 1496 and physical(PAPER) == set(prior) | {'PAPER_MANIFEST.sha256'},
            'complete1496 current whole manifest BEFORE creation only')
    prior_tree = physical(PAPER)
    live = prior_tree - {'frozen_round0/' + n for n in physical(ROUND0)} - {'frozen_round1/' + n for n in physical(ROUND1)}
    require(live == set(author) | {'SHA256SUMS', 'AUTHOR_MANIFEST.sha256', 'ROOT_ADOPTION.md',
            'ROOT_LIFECYCLE.md', 'PAPER_MANIFEST.sha256'}, 'no terminal or unexpected live paper files')
    return core, author, prior, prior_tree


def accepted_b(binding, core):
    roles = binding['roles']
    review, pair = complete_manifest(REVIEW), complete_manifest(PAIR)
    require(len(review) == binding['review_manifest_entries'] and len(pair) == 59 and
            digest(REVIEW / 'SHA256SUMS') == roles['review_manifest']['sha256'] and
            digest(PAIR / 'SHA256SUMS') == PAIR_SEAL, 'complete actual final B and original59 root pair')
    old = manifest_rows(Path(roles['initial_review_manifest']['path']))
    require(len(old) == 407 and old['DELTA.md'] == INITIAL_DELTA and old['FINDINGS.json'] == INITIAL_FINDINGS,
            'actual immutable407 initial B payloads')
    aliases = binding['initial_review_aliases']
    require(isinstance(aliases, dict) and set(aliases) <= {'DELTA.md'},
            'only initial DELTA may move; all other406 initial payloads remain at the same paths')
    for name, value in old.items():
        target = aliases.get(name, name)
        safe(target)
        require(target in review and review[target] == value and digest(REVIEW / target) == value,
                'every initial407 payload physically retained: ' + name)
    for name, role in [('DELTA.md', 'initial_delta'), ('FINDINGS.json', 'initial_findings')]:
        require(Path(roles[role]['path']) == REVIEW / aliases.get(name, name), 'bound initial document exact physical role')
    expected_inputs = {str((ROUND1 / name).relative_to(ROOT)): value for name, value in core.items()}
    expected_inputs[str((ROUND1 / 'SHA256SUMS').relative_to(ROOT))] = ROUND1_SEAL
    require(read_manifest(REVIEW / 'INPUT_PINS.sha256', ROOT) == expected_inputs, 'exact509 actual B reviewed Round1 inputs')
    receipt = load(PAIR / 'RESULT.json')
    require(receipt['status'] == 'PASS_ROOT_P210_B_STRICT_PAIR' and receipt['role'] == 'p210_b' and
            receipt['errors'] == [] and receipt['known_input_count'] == 3558 and len(receipt['commands']) == 10 and
            receipt['raw_canonical_comparisons'] == 2 and receipt['raw_pair_comparisons'] == 1,
            'actual unchanged root B strict pair, not a new scientific execution')
    require([row['checks'] for row in receipt['results']] == [51129, 51129] and
            all(row['stdout'] == {'bytes': 6475161, 'sha256': B_CANONICAL} for row in receipt['results']),
            'two original strict B canonical result identities')
    raw_equal(PAIR / 'commands/03_verify_01/stdout.raw', REVIEW / 'CANONICAL.json', 'root first complete original B stdout')
    raw_equal(PAIR / 'commands/03_verify_02/stdout.raw', REVIEW / 'CANONICAL.json', 'root second complete original B stdout')
    require(digest(REVIEW / 'CANONICAL.json') == B_CANONICAL, 'unchanged actual independent B canonical')
    return {str(base / name): value for base, rows in [(REVIEW, review), (PAIR, pair)] for name, value in rows.items()}


def anchors_for(binding, binding_path):
    anchors = {name: Path(binding['roles'][role]['path']) for role, name in ROLE_ANCHORS.items()}
    anchors['FINAL_B_BINDING.json'] = Path(binding_path)
    require(len(anchors) == 14 and sum(path.stat().st_size for path in anchors.values()) <= 16 * 1024 * 1024,
            'fourteen small physical acceptance/history anchors, never B host inventories')
    return anchors


def links(core, binding, anchors):
    prior = load(ROUND1 / 'ROUND1_PROVENANCE.json')
    old = prior['round1_core_link_map'] + prior['acceptance_anchor_link_map']
    require(prior['schema'] == 'p210-round1-provenance-v1' and len(old) == 71 and
            prior['round0_external_aliases'] == [], 'accepted original71 Round1 links, no new historical fallback')
    occurrences = Counter((name, href) for name in core if name.endswith('.md') for href in markdown_links(ROUND1 / name))
    require(occurrences == Counter((row['document'], row['href']) for row in old),
            'all actual carried-core Markdown link occurrences match original roles')
    rebuilt = []
    for row in old:
        source = Path(row['physical_target'])
        require(digest(source) == row['sha256'], 'exact original Round1 link target before copying')
        inside = source.is_relative_to(ROUND1)
        target = TARGET / source.relative_to(ROUND1) if inside else source
        rebuilt.append(dict(document=row['document'], document_sha256=core[row['document']], href=row['href'],
            round1_physical_target=str(source), physical_target=str(target), sha256=row['sha256'],
            mode='physical-unchanged-Round1-copy' if inside else 'unchanged-exact-external-role', previous_role=row))
    external = prior['round0_external_original_pins']
    require(len(external) == 33, 'all33 earlier external original keys retained')
    for name, value in external.items():
        require(digest(Path(name)) == value, 'no substitute for an original external key')
    origins = {(str(ROUND1 / name), value): TARGET / name for name, value in core.items()}
    for name, value in core.items():
        if (PAPER / name).is_file():
            require(digest(PAPER / name) == value, 'actual live named carried-core byte identity')
            origins[(str(PAPER / name), value)] = TARGET / name
    origins[(str(PAPER / 'SHA256SUMS'), AUTHOR_SEAL)] = TARGET / 'AUTHOR_MANIFEST.sha256'
    for name, source in anchors.items():
        origins[(str(source), digest(source))] = TARGET / 'ROUND2_ACCEPTANCE' / name
    anchor_links = []
    for role, origin_name in binding['markdown_origins'].items():
        name, source = ROLE_ANCHORS[role], Path(binding['roles'][role]['path'])
        origin = Path(origin_name)
        for href in markdown_links(source):
            original_target = (origin.parent / unquote(href.split('#', 1)[0])).resolve()
            require(original_target.is_relative_to(ROOT) and original_target.is_file(),
                    'new anchor link must resolve to an actual bounded workspace file')
            value = digest(original_target)
            target = origins.get((str(original_target), value), original_target)
            anchor_links.append(dict(document='ROUND2_ACCEPTANCE/' + name, source_bytes_path=str(source),
                original_document=str(origin), href=href, original_target=str(original_target),
                physical_target=str(target), sha256=value,
                mode='explicit-current-core-or-anchor' if target != original_target else 'exact-current-original-document-origin'))
    return rebuilt, anchor_links, external


def markdown_links(path):
    result = []
    for href in re.findall(r'\[[^\]]*\]\(([^)]+)\)', file_bytes(path).decode()):
        href = href.strip().strip('<>')
        if href.startswith(('https://', 'http://', 'mailto:', '#')) or not href.split('#', 1)[0]:
            continue
        result.append(href)
    return result


def write_new(path, data):
    require(path.is_relative_to(TARGET) and path != TARGET and path.resolve() == path and
            not path.is_symlink(), 'write stays within exact nonsymlink new Round2 target')
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('xb') as stream:
        stream.write(data)


def copy_one(source, target, value):
    data = file_bytes(source)
    require(sha256(data).hexdigest() == value, 'exact planned copy source')
    write_new(target, data)
    raw_equal(source, target, 'physical-copy:' + str(target.relative_to(TARGET)))


def main():
    created = False
    try:
        require(len(sys.argv) == 8 and sys.argv[1] == 'freeze-round2-after-accepted-b' and
                sys.argv[2] == '--final-b-binding' and sys.argv[4] == '--expected-final-b-binding-sha256' and
                sys.argv[6] == '--expected-preparation-sha256', 'explicit actual binding and independently checked preparation digests')
        binding_path, binding_hash, preparation_hash = Path(sys.argv[3]), sys.argv[5], sys.argv[7]
        require(Path(__file__).resolve() == PREPARATION / 'freeze_p210_round2.py' and Path.cwd() == ROOT,
                'fixed new source and workspace')
        require(set(os.environ) == set(ENV), 'exact four environment names; inherited secret values are not read')
        require(all(os.environ[name] == value for name, value in ENV.items()), 'exact four safe environment values')
        require(sys.flags.isolated and sys.flags.no_site and sys.flags.dont_write_bytecode and sys.flags.optimize == 0 and
                Path(sys.executable).resolve() == Path('/usr/bin/python3.10'), 'isolated source-only system Python')
        require(sys.pycache_prefix == str(TARGET / 'never_created_freezer_cache') and
                not os.path.lexists(sys.pycache_prefix), 'explicit absent unwritten cache')
        require(not os.path.lexists(TARGET), 'existing Round2 is refused, never overwritten or retried')
        binding = binding_inputs(binding_path, binding_hash)
        require(re.fullmatch('[0-9a-f]{64}', preparation_hash) is not None and
                digest(PREPARATION / 'SHA256SUMS') == preparation_hash, 'explicit complete preparation digest')
        complete_manifest(PREPARATION)
        direct = load(PREPARATION / 'INPUT_PINS.json')
        require(direct['schema'] == 'p210-round2-unbound-preparation-direct-input-pins-v1',
                'preparation pins are existing immutable inputs, never a future acceptance')
        for name, value in direct['pins'].items():
            data = file_bytes(Path(name))
            require(sha256(data).hexdigest() == value['sha256'] and len(data) == value['bytes'], 'exact immutable direct input')
        digest(Path('/usr/bin/python3.10'))
        core, author, prior_whole, prior_tree = core_inputs(binding)
        accepted_external = accepted_b(binding, core)
        anchors = anchors_for(binding, binding_path)
        core_links, anchor_links, external = links(core, binding, anchors)
        source = Path(__file__).resolve()
        selfhash = digest(source)
        anchor_pins = {name: digest(path) for name, path in anchors.items()}
        required_bytes = sum((ROUND1 / name).stat().st_size for name in core) + sum(path.stat().st_size for path in anchors.values()) + source.stat().st_size
        require(shutil.disk_usage(PAPER).free > required_bytes + 32 * 1024 * 1024,
                'exact one-core-copy size plus32MiB metadata/failure margin')
        before = dict(READ_PINS)
        # FIRST filesystem mutation; no unbound or not-yet-accepted run reaches it.
        TARGET.mkdir()
        created = True
        for name, value in sorted(core.items()):
            copy_one(ROUND1 / name, TARGET / safe(name), value)
        for name, path in anchors.items():
            copy_one(path, TARGET / 'ROUND2_ACCEPTANCE' / name, anchor_pins[name])
        copy_one(source, TARGET / 'ROUND2_FREEZE_ADAPTER.py', selfhash)
        require(read_manifest(TARGET / 'AUTHOR_MANIFEST.sha256', TARGET) == author, 'all physical author alias referents')
        for row in core_links + anchor_links:
            require(digest(Path(row['physical_target'])) == row['sha256'], 'all new physical/original link target bytes')
        require(complete_manifest(ROUND1) == core and read_manifest(PAPER / 'PAPER_MANIFEST.sha256', PAPER) == prior_whole,
                'old Round1 and whole-manifest referents unchanged, not a new whole-tree claim')
        require(physical(PAPER) - {'frozen_round2/' + n for n in physical(TARGET)} == prior_tree,
                'every preexisting paper file/membership preserved')
        require(binding_inputs(binding_path, binding_hash) == binding and accepted_b(binding, core) == accepted_external,
                'complete actual accepted role and package closure unchanged after copies')
        require(links(core, binding, anchors) == (core_links, anchor_links, external), 'all original/new link roles unchanged')
        for name, value in before.items():
            file_bytes(Path(name))
            require(READ_PINS[name] == value, 'full uncached unchanged original inputs after copies')
        metadata = dict(schema='p210-round2-provenance-v1',
            scope='Physical Round2 after actual same-B acceptance and root final closure, not terminal/paper/batch acceptance',
            author_payloads_preserved=489, round1_core_payloads_copied=508, acceptance_anchor_payloads=14,
            author_manifest_sha256=AUTHOR_SEAL, round0_manifest_sha256=ROUND0_SEAL, round1_manifest_sha256=ROUND1_SEAL,
            actual_final_b_binding_path=str(binding_path), actual_final_b_binding_sha256=binding_hash,
            actual_final_b_binding=binding, accepted_root_closure_sha256=binding['roles']['root_final_closure']['sha256'],
            core_payload_pins=core, accepted_review_and_root_manifest_referents=accepted_external,
            anchors={name: dict(original_path=str(anchors[name]), physical_path='ROUND2_ACCEPTANCE/' + name, sha256=value)
                     for name, value in anchor_pins.items()},
            anchor_markdown_origins={ROLE_ANCHORS[role]: origin for role, origin in binding['markdown_origins'].items()},
            initial_review_aliases=binding['initial_review_aliases'], round1_external_aliases=[],
            round0_external_original_pins=external, round2_historical_link_map=core_links, acceptance_anchor_link_map=anchor_links,
            prior_whole_manifest=dict(original_path=str(PAPER / 'PAPER_MANIFEST.sha256'), original_referent_base=str(PAPER),
                sha256=binding['roles']['prior_whole_manifest']['sha256'], physical_anchor='ROUND2_ACCEPTANCE/PRE_ROUND2_PAPER_MANIFEST.sha256',
                original_referent_pins=prior_whole, complete_before_creation_only=True, current_whole_manifest_after_creation=False),
            prior_lifecycle=dict(original_path=str(PAPER / 'ROOT_LIFECYCLE.md'), sha256=binding['roles']['prior_lifecycle']['sha256'],
                physical_anchor='ROUND2_ACCEPTANCE/PRE_ROUND2_ROOT_LIFECYCLE.md', old_whole_manifest_row='ROOT_LIFECYCLE.md',
                role='exact pre-Round2 body; later root changes use this precise physical old-byte role'),
            full_source_input_pins_before_and_reread_after=before, unchanged_source_input_count=len(before),
            freezer_origin=str(source), freezer_sha256=selfhash, preparation_sha256=preparation_hash,
            launch_argv=sys.argv, launch_orig_argv=sys.orig_argv, environment=ENV, cwd=str(ROOT), raw_byte_comparisons=COMPARISONS,
            limits=['All508 Round1 payloads copied once, including earlier historical maps and accepted A anchors unchanged.',
                'Only14 small B/initial/root/prior-live/binding anchors added; no recursive paper or host inventory snapshots.',
                'Initial407 B payloads and all actual failures retained; inherited A Major and B infrastructure limits not erased.',
                'Binding selectors receive actual future-final filenames/fields after root acceptance; no initial PASS substitutes.',
                'Known manifest referents reread, not the nested B host-ledger paths. No science/build/view or old program execution.',
                'Root separately owns later lifecycle/whole-manifest updates, terminal builds/views and paper/five-paper gates.'],
            external='OWNER_AMBER / HOLD_EXTERNAL')
        write_new(TARGET / 'ROUND2_PROVENANCE.json', (json.dumps(metadata, sort_keys=True, indent=2) + '\n').encode())
        expected = dict(core)
        expected.update({'ROUND2_ACCEPTANCE/' + name: value for name, value in anchor_pins.items()})
        expected.update({'ROUND2_FREEZE_ADAPTER.py': selfhash, 'ROUND2_PROVENANCE.json': digest(TARGET / 'ROUND2_PROVENANCE.json')})
        require(len(expected) == 524 and physical(TARGET) == set(expected), 'exact524 nonself payloads before seal')
        for name, value in expected.items():
            require(digest(TARGET / name) == value, 'every completed physical payload')
        for name, value in before.items():
            file_bytes(Path(name))
            require(READ_PINS[name] == value, 'final uncached original key check before seal')
        write_new(TARGET / 'SHA256SUMS', ''.join(value + '  ' + name + '\n' for name, value in sorted(expected.items())).encode())
        require(complete_manifest(TARGET) == expected, 'complete final nonself Round2 seal')
        print(json.dumps(dict(status='PASS_PHYSICAL_P210_ROUND2', payloads=524, physical_files=525,
            manifest_sha256=digest(TARGET / 'SHA256SUMS'), core_payloads=508, author_payloads_preserved=489,
            acceptance_anchor_payloads=14, actual_final_b_binding_sha256=binding_hash, freezer_sha256=selfhash,
            preparation_sha256=preparation_hash, unchanged_before_after_inputs=len(before), core_link_roles=len(core_links),
            anchor_link_roles=len(anchor_links), complete_raw_byte_comparisons=len(COMPARISONS),
            no_live_lifecycle_or_whole_manifest_update=True, boundary='No science/build/view; terminal/paper/five-paper gates remain.'),
            sort_keys=True, indent=2))
        return 0
    except BaseException:
        failure = dict(status='FAIL_ROUND2_PRESERVED' if created else 'REFUSED_BEFORE_ROUND2_CREATION',
            target_created_by_this_invocation=created, traceback=traceback.format_exc(), known_read_pins=READ_PINS,
            raw_byte_comparisons=COMPARISONS, no_completion_or_acceptance_inferred=True, no_rollback_or_retry=True)
        if created and not (TARGET / 'SHA256SUMS').exists():
            write_new(TARGET / 'ROUND2_FAILURE.json', (json.dumps(failure, sort_keys=True, indent=2) + '\n').encode())
        print(json.dumps(failure, sort_keys=True, indent=2))
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
