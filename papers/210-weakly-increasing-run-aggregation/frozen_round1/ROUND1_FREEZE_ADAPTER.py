#!/usr/bin/env python3
"""One-time physical P210 Round1, root only after a hash-bound ACTUAL closure.

Infrastructure adapted after full reading of P210 Round0 and P209 Round1 V2.
No original program is imported/executed. Every gate precedes target creation.
Copies use exclusive creation and complete byte comparisons, not hash equality
described as byte comparison. No live author/lifecycle/whole seal is updated.
"""
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
ROUND0 = PAPER / 'frozen_round0'
TARGET = PAPER / 'frozen_round1'
PREPARATION = QA / 'p210_round1_preparation'
REVIEW = BATCH / 'reviews/p210_a'
RESPONSE = BATCH / 'P210_A_RESPONSE.md'
ACCEPTANCE = QA / 'P210_A_ROOT_DELTA_INSPECTION.actual.json'
PAIR = QA / 'root_replays/p210_a_strict_pair_01'
INITIAL_HISTORY = REVIEW / 'history/initial_before_delta'
AUTHOR_SEAL = 'b0c72e401acaf50acb611dc27f2ff1c45e3ad6e1b547218b48d13be8c82a0f6c'
ROUND0_SEAL = 'e8446cd17b1a283c74f9a6b4ced413b9e30810396c3d30f936ac2986ce790e26'
PRIOR_WHOLE_SEAL = '9c092df8a673debea2697f6213e92002b8fb575b336a8821f5c18fdb0a79e727'
PRIOR_LIFECYCLE = 'bf11c369b64eb1d76b4d0dfc0afe603f0970049b1e0f2bb4a0b1533355da5a32'
INITIAL_A_SEAL = 'e60d352a6520dd5f56b01035912ce753bb1a669c7368ce0a999ff56a72ff966d'
INITIAL_DELTA = '835047cc14c04de6057a93b993b6f21dd57e77f1ce8e83afba7dce0af8e2445e'
FINAL_A_SEAL = 'f6b92663cb2a7909f85a25a892ee4433ccd6177e84c07bf7ceccc9555b191f6d'
FINAL_DELTA = 'fa03852f5366d6a0e4fd5a202dfb57e6d6887e8b858a14576ed82e810011d123'
CURRENT_FINDINGS = 'f3d5a14b62b880f79fc5c98fa44f9ba98415ebf111e30f6e5eee64a8e4984e7b'
INITIAL_FINDINGS = 'd07a58bf9e8fb650078a072421a33446556eb218c59ea465cb5a78a52a506f02'
RESPONSE_SHA = '829acdc6048f1aa9b9dcbe0d1195bb935c3ea8ed84154dc2b2abc24ef2a17b66'
PAIR_SEAL = '9b30c2a3fc93874e4eaafdec345d9894f95aa36b7e9d764bd54646cfe5c7d6fb'
A_CANONICAL = 'd96ed0240dec421d78cdbfb013869680c91685c1848ea2ee030a71f86ab7aa74'
ORIGINAL_SOURCES = {
    QA / 'freeze_p210_round0.py': '5c71b3546a04d46d34feaf32ef2c6aee359c031a6e7c46556c0714c5ac6aa250',
    QA / 'p209_round1_preparation_v2/freeze_p209_round1.py': '19cf0898e201f25dc5724233ff1cdef59d8a0001d6239fe5d15aeb9212f63c44',
}
ENV = {'PATH': '/usr/bin:/bin', 'LANG': 'C.UTF-8', 'LC_ALL': 'C.UTF-8', 'TZ': 'UTC'}
ANCHORS = {
    'ROUND0_CORE_MANIFEST.sha256': ROUND0 / 'SHA256SUMS',
    'A_REVIEW_MANIFEST.sha256': REVIEW / 'SHA256SUMS',
    'A_DELTA.md': REVIEW / 'DELTA.md',
    'A_INITIAL_FINDINGS.json': REVIEW / 'FINDINGS.json',
    'A_CURRENT_FINDINGS.json': REVIEW / 'CURRENT_FINDINGS.json',
    'A_INPUT_PINS.sha256': REVIEW / 'INPUT_PINS.sha256',
    'ROOT_RESPONSE.md': RESPONSE,
    'ROOT_DELTA_CLOSURE.actual.json': ACCEPTANCE,
    'ROOT_PAIR_MANIFEST.sha256': PAIR / 'SHA256SUMS',
    'PRE_ROUND1_PAPER_MANIFEST.sha256': PAPER / 'PAPER_MANIFEST.sha256',
    'PRE_ROUND1_ROOT_LIFECYCLE.md': PAPER / 'ROOT_LIFECYCLE.md',
    'A_INITIAL_REVIEW_MANIFEST.sha256': INITIAL_HISTORY / 'SHA256SUMS',
    'A_INITIAL_DELTA.md': INITIAL_HISTORY / 'DELTA.md',
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


def initial_review_aliases():
    return [dict(original_path=str(REVIEW / name), sha256=value, physical_path=str(INITIAL_HISTORY / name))
            for name, value in [('DELTA.md', INITIAL_DELTA), ('SHA256SUMS', INITIAL_A_SEAL)]]


def root_acceptance(expected_hash):
    require(re.fullmatch('[0-9a-f]{64}', expected_hash) is not None, 'explicit root closure SHA256 required')
    require(digest(ACCEPTANCE) == expected_hash, 'actual root closure differs from explicit invocation hash')
    accepted = load(ACCEPTANCE)
    required = dict(schema='p210-a-root-delta-closure-v1', status='ROOT_ACCEPTED_A_DELTA_ORIGINAL_CLOSURE_PASS',
        paper='P210', input_round=0, current_open_findings=0, resolved_major_findings=1,
        unchanged_author_payloads=489, unchanged_round0_payloads=493, author_manifest_sha256=AUTHOR_SEAL,
        round0_manifest_sha256=ROUND0_SEAL, initial_review_payloads_preserved=484,
        prior_whole_manifest_sha256=PRIOR_WHOLE_SEAL, prior_lifecycle_sha256=PRIOR_LIFECYCLE,
        review_manifest_entries=552, review_manifest_sha256=FINAL_A_SEAL, delta_sha256=FINAL_DELTA,
        findings_sha256=INITIAL_FINDINGS, current_findings_sha256=CURRENT_FINDINGS,
        response_sha256=RESPONSE_SHA, root_pair_manifest_sha256=PAIR_SEAL)
    for key, value in required.items():
        require(type(accepted.get(key)) is type(value) and accepted[key] == value, 'exact root attestation field: ' + key)
    for key in ('reviewer_delta_accepted', 'root_original_inspection_complete', 'root_replay_closure_complete'):
        require(accepted.get(key) is True, 'root actual completed prerequisite: ' + key)
    require(accepted.get('initial_review_aliases') == initial_review_aliases(), 'only exact two A initial-document aliases, NOT Round0 aliases')
    require(not accepted.get('historical_input_aliases', []), 'no Round0 historical-alias fallback is authorized')
    evidence = accepted.get('evidence')
    require(isinstance(evidence, dict) and len(evidence) >= 2, 'actual root evidence path/hash object')
    for path, value in evidence.items():
        origin = Path(path)
        require(origin.is_absolute() and origin.is_relative_to(ROOT) and origin != ACCEPTANCE and
                re.fullmatch('[0-9a-f]{64}', value) is not None, 'exact root evidence key, no circular self-attestation')
        require(digest(origin) == value, 'actual root evidence bytes: ' + path)
    return accepted


def core_inputs():
    require(digest(ROUND0 / 'SHA256SUMS') == ROUND0_SEAL, 'immutable Round0 seal')
    core = complete_manifest(ROUND0)
    require(len(core) == 493 and not any(part.startswith('frozen_round') for name in core for part in safe(name).parts), 'exact493 non-nested core')
    require(digest(PAPER / 'SHA256SUMS') == digest(PAPER / 'AUTHOR_MANIFEST.sha256') == AUTHOR_SEAL, 'both immutable author seals')
    author = read_manifest(PAPER / 'AUTHOR_MANIFEST.sha256', PAPER)
    require(len(author) == 489 and read_manifest(ROUND0 / 'AUTHOR_MANIFEST.sha256', ROUND0) == author, 'exact489 author live/frozen roles')
    expected = dict(author)
    expected.update({'AUTHOR_MANIFEST.sha256': AUTHOR_SEAL, 'ROOT_ADOPTION.md': digest(PAPER / 'ROOT_ADOPTION.md'),
        'FREEZE_ADAPTER.py': ORIGINAL_SOURCES[QA / 'freeze_p210_round0.py'],
        'FROZEN_LINK_MAP.json': digest(ROUND0 / 'FROZEN_LINK_MAP.json')})
    require(core == expected, 'all and only original Round0 additions')
    for name in author:
        raw_equal(PAPER / name, ROUND0 / name, 'unchanged live/frozen author: ' + name)
    for path, value in ORIGINAL_SOURCES.items():
        require(digest(path) == value, 'original infrastructure source unchanged: ' + str(path))
    require(digest(PAPER / 'PAPER_MANIFEST.sha256') == PRIOR_WHOLE_SEAL and
            digest(PAPER / 'ROOT_LIFECYCLE.md') == PRIOR_LIFECYCLE, 'exact PRE-Round1 whole seal and lifecycle')
    prior = read_manifest(PAPER / 'PAPER_MANIFEST.sha256', PAPER)
    require(len(prior) == 987 and physical(PAPER) == set(prior) | {'PAPER_MANIFEST.sha256'}, 'old987 whole manifest complete BEFORE creation only')
    live = physical(PAPER) - {'frozen_round0/' + name for name in physical(ROUND0)}
    require(live == set(author) | {'SHA256SUMS', 'AUTHOR_MANIFEST.sha256', 'ROOT_ADOPTION.md', 'ROOT_LIFECYCLE.md', 'PAPER_MANIFEST.sha256'},
            'no unexpected live paper files before Round1')
    return core, author, prior, live


def accepted_a(accepted, core):
    for path in ANCHORS.values():
        digest(path)
    require(digest(REVIEW / 'SHA256SUMS') == FINAL_A_SEAL and digest(PAIR / 'SHA256SUMS') == PAIR_SEAL, 'accepted A/rootpair fixed seals')
    review, pair = complete_manifest(REVIEW), complete_manifest(PAIR)
    require(len(review) == accepted['review_manifest_entries'] == 552 and len(pair) == 59, 'entire final552 A and root59 packages')
    for field, path in [('delta_sha256', REVIEW / 'DELTA.md'), ('findings_sha256', REVIEW / 'FINDINGS.json'),
            ('current_findings_sha256', REVIEW / 'CURRENT_FINDINGS.json'), ('response_sha256', RESPONSE)]:
        require(digest(path) == accepted[field], 'actual accepted role: ' + field)
    require('ACCEPTED_EXACT_NO_CHANGE_DELTA' in file_bytes(REVIEW / 'DELTA.md').decode() and
            RESPONSE_SHA in file_bytes(REVIEW / 'DELTA.md').decode(), 'same-A exact accepted response wording')
    initial = load(REVIEW / 'FINDINGS.json')
    current = load(REVIEW / 'CURRENT_FINDINGS.json')
    census = {'Critical': {'open': 0, 'resolved': 0}, 'Major': {'open': 0, 'resolved': 1},
              'Minor': {'open': 0, 'resolved': 0}, 'total_open': 0, 'total_resolved': 1}
    require(initial['schema'] == 'p210-a-findings-v1' and initial['round'] == 'A_initial' and
            initial['reviewer'] == '/root/p210_a_reviewer' and initial['census'] == census, 'immutable initial findings schema/census')
    require(current['schema'] == 'p210-a-current-findings-v1' and current['round'] == 'A_same_process_exact_delta' and
            current['reviewer'] == '/root/p210_a_reviewer' and current['verdict'] == 'ACCEPTED_EXACT_NO_CHANGE_DELTA' and
            current['response'] == '../../P210_A_RESPONSE.md' and current['response_sha256'] == RESPONSE_SHA and
            current['initial_findings_sha256'] == INITIAL_FINDINGS and current['census'] == census and
            current['findings'] == initial['findings'], 'actual current census preserves entire resolved E1, not an empty generic census')
    require(len(current['findings']) == 1 and current['findings'][0]['id'] == 'P210-A-E1' and
            current['findings'][0]['status'] == 'resolved' and current['findings'][0]['changed_scientific_inputs'] == [] and
            'remain unavailable' in current['findings'][0]['historical_loss_not_repaired'], 'honest resolved Major and permanent historical losses')
    for row in initial_review_aliases():
        require(digest(Path(row['physical_path'])) == row['sha256'], 'exact preserved initial A alias')
    old = manifest_rows(INITIAL_HISTORY / 'SHA256SUMS')
    require(len(old) == 484 and old.get('DELTA.md') == INITIAL_DELTA, 'entire original484 initial review membership')
    projected = {}
    for name, value in old.items():
        physical_name = 'history/initial_before_delta/DELTA.md' if name == 'DELTA.md' else name
        require(review.get(physical_name) == value and digest(REVIEW / physical_name) == value, 'exact initial payload preserved: ' + name)
        projected[physical_name] = value
    projected['history/initial_before_delta/SHA256SUMS'] = INITIAL_A_SEAL
    require(read_manifest(REVIEW / 'INITIAL_PRESERVED_PINS.sha256', REVIEW) == projected, 'all485 projected original roles, no generic alias')
    expected_inputs = {str((ROUND0 / name).relative_to(ROOT)): value for name, value in core.items()}
    expected_inputs[str((ROUND0 / 'SHA256SUMS').relative_to(ROOT))] = ROUND0_SEAL
    require(read_manifest(REVIEW / 'INPUT_PINS.sha256', ROOT) == expected_inputs, 'exact494 actual reviewed inputs')
    receipt = load(PAIR / 'RESULT.json')
    require(receipt['status'] == 'PASS_ROOT_P210_A_STRICT_PAIR' and receipt['role'] == 'p210_a' and
            receipt['errors'] == [] and receipt['known_input_count'] == 3634 and len(receipt['commands']) == 10 and
            receipt['raw_canonical_comparisons'] == 2 and receipt['raw_pair_comparisons'] == 1, 'actual fixed root strict pair result')
    require([row['checks'] for row in receipt['results']] == [133978, 133978] and
            all(row['stdout'] == {'bytes': 703850, 'sha256': A_CANONICAL} for row in receipt['results']), 'two original root science outputs')
    raw_equal(PAIR / 'commands/03_verify_01/stdout.raw', REVIEW / 'CANONICAL.json', 'root first full canonical stdout')
    raw_equal(PAIR / 'commands/03_verify_02/stdout.raw', REVIEW / 'CANONICAL.json', 'root second full canonical stdout')
    require(digest(REVIEW / 'CANONICAL.json') == A_CANONICAL, 'unchanged independent canonical')
    external = {str(base / name): value for base, rows in [(REVIEW, review), (PAIR, pair)] for name, value in rows.items()}
    return external


def links(core):
    old = load(ROUND0 / 'FROZEN_LINK_MAP.json')
    require(old['historical_author_manifest_sha256'] == AUTHOR_SEAL and old['author_payloads'] == 489 and
            len(old['external_input_pins']) == 33 and len(old['links']) == 57, 'original exact R0 map scope')
    for path, value in old['external_input_pins'].items():
        require(digest(Path(path)) == value, 'all33 R0 external originals remain exact; no alias fallback: ' + path)
    rebuilt = []
    for name in sorted(core):
        if not name.endswith('.md'):
            continue
        origin = Path(old['exact_document_origin_roles'].get(name, str(PAPER / name)))
        for href in markdown_links(ROUND0 / name):
            candidate = (origin.parent / unquote(href.split('#', 1)[0])).resolve()
            if candidate == PAPER / 'SHA256SUMS':
                physical_target, value, mode = ROUND0 / 'AUTHOR_MANIFEST.sha256', AUTHOR_SEAL, 'exact-author-seal-alias'
            elif candidate.is_relative_to(PAPER) and candidate.relative_to(PAPER).as_posix() in core:
                relative = candidate.relative_to(PAPER).as_posix()
                physical_target, value, mode = ROUND0 / relative, core[relative], 'physical-copied-input'
            else:
                require(str(candidate) in old['external_input_pins'], 'no undeclared old link origin')
                physical_target, value, mode = candidate, old['external_input_pins'][str(candidate)], 'external-exact-original-origin'
            rebuilt.append(dict(document=name, document_sha256=core[name], exact_markdown_origin=str(origin), href=href,
                mode=mode, physical_target=str(physical_target), sha256=value))
    require(rebuilt == old['links'], 'all57 complete original Markdown link roles reconstructed without prefix fallback')
    core_links = []
    for row in rebuilt:
        old_target = Path(row['physical_target'])
        inside = old_target.is_relative_to(ROUND0)
        physical_target = TARGET / old_target.relative_to(ROUND0) if inside else old_target
        core_links.append({**row, 'round0_physical_target': str(old_target), 'physical_target': str(physical_target),
                           'round1_mode': 'physical-unchanged-core-copy' if inside else 'unchanged-exact-external-original'})
    origins = {str(ROUND0 / name): (TARGET / name, value) for name, value in core.items()}
    for name, value in core.items():
        if (PAPER / name).is_file():
            require(digest(PAPER / name) == value, 'live named core origin unchanged')
            origins[str(PAPER / name)] = (TARGET / name, value)
    origins[str(PAPER / 'SHA256SUMS')] = (TARGET / 'AUTHOR_MANIFEST.sha256', AUTHOR_SEAL)
    for name, source in ANCHORS.items():
        origins[str(source)] = (TARGET / 'ROUND1_ACCEPTANCE' / name, digest(source))
    anchor_links = []
    for name, source in ANCHORS.items():
        if source.suffix != '.md':
            continue
        document_origin = REVIEW / 'DELTA.md' if name == 'A_INITIAL_DELTA.md' else source
        for href in markdown_links(source):
            target = (document_origin.parent / unquote(href.split('#', 1)[0])).resolve()
            if str(target) in origins:
                physical_target, value = origins[str(target)]
                mode = 'explicit-core-or-anchor'
            else:
                require(target.is_file(), 'anchor link must be an actual file, not an unbounded directory inventory')
                physical_target, value, mode = target, digest(target), 'exact-current-original-document-origin'
            anchor_links.append(dict(document='ROUND1_ACCEPTANCE/' + name, source_bytes_path=str(source),
                original_document=str(document_origin), href=href, original_target=str(target), physical_target=str(physical_target), sha256=value, mode=mode))
    return core_links, anchor_links, old['external_input_pins']


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
            not path.is_symlink(), 'write stays within exact nonsymlink new Round1 target')
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
        require(len(sys.argv) == 4 and sys.argv[1:3] == ['freeze-round1-after-accepted-a', '--expected-root-closure-sha256'], 'explicit root-only one-time invocation')
        require(Path(__file__).resolve() == PREPARATION / 'freeze_p210_round1.py' and Path.cwd() == ROOT, 'fixed source and workspace')
        require(set(os.environ) == set(ENV), 'exact four-key empty launcher environment; no inherited secret values read')
        require(all(os.environ[name] == value for name, value in ENV.items()), 'exact safe four environment values')
        require(sys.flags.isolated and sys.flags.no_site and sys.flags.dont_write_bytecode and sys.flags.optimize == 0 and
                Path(sys.executable).resolve() == Path('/usr/bin/python3.10'), 'isolated unoptimized source-only system interpreter')
        require(sys.pycache_prefix == str(TARGET / 'never_created_freezer_cache') and not Path(sys.pycache_prefix).exists(), 'explicit absent cache never written')
        require(not TARGET.exists() and not TARGET.is_symlink(), 'existing freeze refused; never retry/overwrite')
        accepted = root_acceptance(sys.argv[3])
        complete_manifest(PREPARATION)
        direct = load(PREPARATION / 'INPUT_PINS.json')
        require(direct['schema'] == 'p210-round1-preparation-direct-input-pins-v1' and
                direct['expected_root_closure_sha256'] == sys.argv[3] and
                direct['pins'].get(str(ACCEPTANCE)) == sys.argv[3], 'direct preparation binds actual root closure')
        for path, value in direct['pins'].items():
            require(digest(Path(path)) == value, 'explicit preparation input pin')
        digest(Path('/usr/bin/python3.10'))
        core, author, prior_whole, live = core_inputs()
        accepted_external = accepted_a(accepted, core)
        core_links, anchor_links, old_external = links(core)
        source = Path(__file__).resolve()
        selfhash = digest(source)
        anchors = {name: digest(path) for name, path in ANCHORS.items()}
        required_bytes = sum((ROUND0 / name).stat().st_size for name in core) + sum(path.stat().st_size for path in ANCHORS.values()) + source.stat().st_size
        require(shutil.disk_usage(PAPER).free > required_bytes + 32 * 1024 * 1024, 'bounded copy needs payload bytes plus32MiB metadata/failure margin')
        before = dict(READ_PINS)
        # FIRST filesystem mutation. Every real acceptance, pin, membership,
        # complete-manifest and exact-link gate above must have already passed.
        TARGET.mkdir()
        created = True
        for name, value in sorted(core.items()):
            copy_one(ROUND0 / name, TARGET / safe(name), value)
        for name, path in ANCHORS.items():
            copy_one(path, TARGET / 'ROUND1_ACCEPTANCE' / name, anchors[name])
        copy_one(source, TARGET / 'ROUND1_FREEZE_ADAPTER.py', selfhash)
        require(read_manifest(TARGET / 'AUTHOR_MANIFEST.sha256', TARGET) == author, 'physical author alias referents unchanged')
        for row in core_links + anchor_links:
            require(digest(Path(row['physical_target'])) == row['sha256'], 'every new physical/original link target')
        require(complete_manifest(ROUND0) == core and read_manifest(PAPER / 'PAPER_MANIFEST.sha256', PAPER) == prior_whole,
                'old R0 and original whole-manifest bytes/referents unchanged, not a current whole-tree claim')
        require(physical(PAPER) - {'frozen_round0/' + name for name in physical(ROUND0)} -
                {'frozen_round1/' + name for name in physical(TARGET)} == live, 'all preexisting live membership unchanged')
        require(root_acceptance(sys.argv[3]) == accepted and accepted_a(accepted, core) == accepted_external, 'complete accepted evidence unchanged after copies')
        require(links(core) == (core_links, anchor_links, old_external), 'all original and anchor links unchanged after copies')
        for path, value in before.items():
            file_bytes(Path(path))
            require(READ_PINS[path] == value, 'full uncached before/after input pin equality')
        metadata = dict(schema='p210-round1-provenance-v1', scope='Physical Round1 after actual same-A acceptance and root closure; no B/terminal/paper/batch acceptance',
            author_payloads_preserved=489, round0_core_payloads_copied=493, acceptance_anchor_payloads=13,
            author_manifest_sha256=AUTHOR_SEAL, round0_manifest_sha256=ROUND0_SEAL,
            accepted_root_closure_sha256=sys.argv[3], accepted_root_assertions=accepted,
            core_payload_pins=core, accepted_review_and_root_manifest_referents=accepted_external,
            anchors={name: dict(original_path=str(ANCHORS[name]), physical_path='ROUND1_ACCEPTANCE/' + name, sha256=value) for name, value in anchors.items()},
            anchor_markdown_origins={name: str(REVIEW / 'DELTA.md' if name == 'A_INITIAL_DELTA.md' else path)
                for name, path in ANCHORS.items() if path.suffix == '.md'},
            initial_review_aliases=initial_review_aliases(), round0_external_aliases=[],
            round0_external_original_pins=old_external, round1_core_link_map=core_links, acceptance_anchor_link_map=anchor_links,
            prior_whole_manifest=dict(original_path=str(PAPER / 'PAPER_MANIFEST.sha256'), original_referent_base=str(PAPER), sha256=PRIOR_WHOLE_SEAL,
                physical_anchor='ROUND1_ACCEPTANCE/PRE_ROUND1_PAPER_MANIFEST.sha256', original_referent_pins=prior_whole,
                complete_before_creation_only=True, current_whole_manifest_after_creation=False),
            prior_lifecycle=dict(original_path=str(PAPER / 'ROOT_LIFECYCLE.md'), sha256=PRIOR_LIFECYCLE,
                physical_anchor='ROUND1_ACCEPTANCE/PRE_ROUND1_ROOT_LIFECYCLE.md',
                role='exact pre-Round1 body including historical pending language; later root updates use this precise old-byte alias',
                old_whole_manifest_row='ROOT_LIFECYCLE.md'),
            full_source_input_pins_before_and_reread_after=before, unchanged_source_input_count=len(before),
            freezer_origin=str(source), freezer_sha256=selfhash, original_infrastructure_sources={str(path): value for path, value in ORIGINAL_SOURCES.items()},
            launch_argv=sys.argv, launch_orig_argv=sys.orig_argv, environment=ENV, cwd=str(ROOT), raw_byte_comparisons=COMPARISONS,
            limits=['All493 core bytes and author/status/old link map retained unchanged.',
                'Two initial A document aliases are separate from Round0 external roles; no R0 alias fallback exists.',
                'One resolved Major E1 retained; authenticated old recorder and three old starts remain unavailable.',
                'No science, build, view, original checker/recorder/auditor execution or external request.',
                'Root owns later live ROOT_LIFECYCLE and PAPER_MANIFEST refreshes, using exact physical pre-update anchors.',
                'Full current package bytes rechecked here; scientific/runtime validity is established by actual prior root closure, not recomputed here.'],
            external='OWNER_AMBER / HOLD_EXTERNAL')
        write_new(TARGET / 'ROUND1_PROVENANCE.json', (json.dumps(metadata, sort_keys=True, indent=2) + '\n').encode())
        expected = dict(core)
        expected.update({'ROUND1_ACCEPTANCE/' + name: value for name, value in anchors.items()})
        expected.update({'ROUND1_FREEZE_ADAPTER.py': selfhash, 'ROUND1_PROVENANCE.json': digest(TARGET / 'ROUND1_PROVENANCE.json')})
        require(len(expected) == 508 and physical(TARGET) == set(expected), 'exact508 nonself physical Round1 payloads before seal')
        for name, value in expected.items():
            require(digest(TARGET / name) == value, 'every completed physical payload')
        for path, value in before.items():
            file_bytes(Path(path))
            require(READ_PINS[path] == value, 'final uncached original input recheck before seal')
        write_new(TARGET / 'SHA256SUMS', ''.join(value + '  ' + name + '\n' for name, value in sorted(expected.items())).encode())
        require(complete_manifest(TARGET) == expected, 'complete actual final nonself seal')
        print(json.dumps(dict(status='PASS_PHYSICAL_P210_ROUND1', payloads=508, physical_files=509,
            manifest_sha256=digest(TARGET / 'SHA256SUMS'), core_payloads=493, author_payloads_preserved=489,
            acceptance_anchor_payloads=13, accepted_root_closure_sha256=sys.argv[3], freezer_sha256=selfhash,
            unchanged_before_after_inputs=len(before), core_link_roles=len(core_links), anchor_link_roles=len(anchor_links),
            unchanged_round0_external_paths=len(old_external), complete_raw_byte_comparisons=len(COMPARISONS),
            no_live_lifecycle_or_whole_manifest_update=True, boundary='No science/build/view; distinct B and terminal/batch gates remain.'), sort_keys=True, indent=2))
        return 0
    except BaseException:
        failure = dict(status='FAIL_ROUND1_PRESERVED' if created else 'REFUSED_BEFORE_ROUND1_CREATION',
            target_created_by_this_invocation=created, traceback=traceback.format_exc(), known_read_pins=READ_PINS,
            raw_byte_comparisons=COMPARISONS, no_completion_or_acceptance_inferred=True, no_rollback_or_retry=True)
        if created and not (TARGET / 'SHA256SUMS').exists():
            write_new(TARGET / 'ROUND1_FAILURE.json', (json.dumps(failure, sort_keys=True, indent=2) + '\n').encode())
        print(json.dumps(failure, sort_keys=True, indent=2))
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
