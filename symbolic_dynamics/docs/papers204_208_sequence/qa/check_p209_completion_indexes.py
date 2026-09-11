#!/usr/bin/env python3
"""Read-only status/index closure after P209's actual final acceptance.

Rechecks paper/review bytes and exact historical controls; no scientific,
build, view or earlier auditor execution. Snapshot seal is checked too.
"""
from hashlib import sha256
import json
from pathlib import Path
import re
from urllib.parse import unquote

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
BATCH = ROOT / 'docs/papers204_208_sequence'
SNAP = BATCH / 'qa/central_lifecycle_p209_complete'
PAPER = ROOT / 'papers/209-ordered-fibre-threading'
READS = {}


def raw(path):
    assert path.is_file() and not path.is_symlink(), str(path)
    data = path.read_bytes()
    value = {'bytes': len(data), 'sha256': sha256(data).hexdigest()}
    assert str(path) not in READS or READS[str(path)] == value
    READS[str(path)] = value
    return data


def manifest(base, name, count, expected=None):
    data = raw(base / name)
    if expected:
        assert sha256(data).hexdigest() == expected
    rows = {}
    for line in data.decode().splitlines():
        match = re.fullmatch(r'([0-9a-f]{64})  (.+)', line)
        assert match is not None
        digest, relative = match.groups()
        path = Path(relative)
        assert relative not in rows and not path.is_absolute() and '..' not in path.parts
        rows[relative] = digest
    assert len(rows) == count and name not in rows
    assert {str(p.relative_to(base)) for p in base.rglob('*') if p.is_file()} == set(rows) | {name}
    for relative, digest in rows.items():
        assert sha256(raw(base / relative)).hexdigest() == digest
    return {'base': str(base), 'manifest': name, 'payloads': count, 'sha256': sha256(data).hexdigest()}


def main():
    gate = json.loads(raw(BATCH / 'qa/P209_LIFECYCLE_ROOT_INSPECTION.actual.json'))
    result = json.loads(gate['completion']['output'])
    assert gate['completion']['exit_code'] == 0
    assert result['status'] == 'PASS_ROOT_P209_FINAL_LIFECYCLE_ORIGINAL_INSPECTION'
    seals = [manifest(PAPER, 'PAPER_MANIFEST.sha256', 8231, 'b79aaf55710b067a3a96fa7779d34ab6a788190e4aa67dce473da7e0a74c8773'),
             manifest(BATCH / 'qa/p209_terminal_artifact', 'SHA256SUMS', 62, 'c6d10fac378e6c1dfefa831a16cc3d9deb1e404cf0d3e75120628212af75bd3c'),
             manifest(BATCH / 'reviews/p209_a', 'SHA256SUMS', 1342),
             manifest(BATCH / 'reviews/p209_b', 'SHA256SUMS', 1472),
             manifest(SNAP, 'SHA256SUMS', 6)]
    preserved = json.loads(raw(SNAP / 'PRESERVATION.actual.json'))
    assert preserved['status'] == 'PASS_FOUR_EXACT_PREUPDATE_COPIES'
    aliases = []
    for record in preserved['copies']:
        physical = Path(record['copy'])
        assert physical.parent == SNAP
        assert sha256(raw(physical)).hexdigest() == record['expected_sha256']
        assert record['before'] == record['copy_pin'] == record['after']
        assert record['exit_code'] == 0 and record['stdout'] == record['stderr'] == ''
        aliases.append({'original': record['original'], 'copy': str(physical), 'sha256': record['expected_sha256']})
    old = raw(SNAP / 'FINAL_THEOREM_CONTRACTS.md').decode()
    new = raw(BATCH / 'FINAL_THEOREM_CONTRACTS.md').decode()
    old_science = old[old.index('Proof contributors: root and `/root/nineteenth_finite_scout`'):old.index('Paper path: `papers/209-ordered-fibre-threading/`.')]
    new_science = new[new.index('Proof contributors: root and `/root/nineteenth_finite_scout`'):new.index('Paper path: `papers/209-ordered-fibre-threading/`.')]
    assert old_science == new_science and '## P210' not in new
    old_prefix = old.split('## P209')[0].replace('three completed papers', 'four completed papers')
    assert new.split('## P209')[0] == old_prefix
    docs = [ROOT / 'SYMBOLIC_DYNAMICS_STATE.md', BATCH / 'PIPELINE_STATE.md',
            BATCH / 'FINAL_THEOREM_CONTRACTS.md', BATCH / 'GIT_SYNC_RECEIPT.md', SNAP / 'README.md',
            BATCH / 'qa/P209_LIFECYCLE_ROOT_INSPECTION.md']
    docs += [BATCH / ('scouting/' + name + '_ROOT_INSPECTION.md') for name in
             ('THIRTY_SEVENTH', 'THIRTY_EIGHTH', 'THIRTY_NINTH', 'FORTIETH', 'FORTY_FIRST')]
    links = []
    for document in docs:
        text = raw(document).decode()
        assert 'HOLD_EXTERNAL' in text
        text = re.sub(r'(?ms)^```[^\n]*\n.*?^```[ \t]*$', '', text)
        text = re.sub(r'`[^`\n]+`', '', text)
        for href in re.findall(r'\[[^\]]*\]\(([^)]+)\)', text):
            name = href.strip().strip('<>').split('#', 1)[0]
            if not name or re.match(r'[a-zA-Z][a-zA-Z0-9+.-]*:', name):
                continue
            target = (document.parent / unquote(name)).resolve()
            assert target.exists(), (str(document), href)
            links.append({'document': str(document), 'href': href, 'target': str(target)})
    before = dict(READS)
    for name in before:
        raw(Path(name))
    assert before == READS
    print(json.dumps({'status': 'PASS_P209_COMPLETION_INDEX_AND_UNCHANGED_SCIENCE_CLOSURE',
        'complete_papers': ['P205', 'P207', 'P208', 'P209'], 'unfilled_seats': 1,
        'mna_admitted': False, 'manifests': seals, 'original_control_aliases': aliases,
        'p209_contract_science_unchanged': True, 'prior_contracts_unchanged_except_count': True,
        'documents': len(docs), 'local_links': len(links), 'links': links,
        'read_paths_rechecked': len(before), 'read_map_sha256': sha256(json.dumps(before, sort_keys=True).encode()).hexdigest(),
        'new_scientific_build_or_view_executions': 0, 'external_status': 'HOLD_EXTERNAL'}, sort_keys=True, indent=2))


if __name__ == '__main__':
    main()
