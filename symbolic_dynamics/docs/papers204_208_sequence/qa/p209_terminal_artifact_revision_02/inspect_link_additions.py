"""Compare original static link layout with only three approved origin additions.

The complete original line scan remains unchanged; exact archived origin
tables change only semantic source directories. No target function is run.
"""
from collections import Counter
from hashlib import sha256
import json
from pathlib import Path
from urllib.parse import unquote

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
BATCH = ROOT / 'docs/papers204_208_sequence'
HERE = Path(__file__).resolve().parent
PAPER = ROOT / 'papers/209-ordered-fibre-threading'
A, B = [BATCH / ('reviews/p209_' + c) for c in ('a', 'b')]
PINS = {}


def read(path):
    path = Path(path); raw = path.read_bytes()
    value = {'sha256': sha256(raw).hexdigest(), 'bytes': len(raw)}
    assert str(path) not in PINS or PINS[str(path)] == value
    PINS[str(path)] = value
    return raw


def data(path): return json.loads(read(path))


def main():
    old = data(HERE / 'LINK_LAYOUT.json')
    for path, value in old['original_inputs_before'].items():
        read(path); assert PINS[path] == value
    additions, groups = {}, {}
    for attempt in ('delta_check_01', 'delta_check_02'):
        for original, row in data(A / attempt / 'RESPONSE_ORIGINALS_AND_COPIES.json').items():
            copy = Path(row['copy'])
            assert copy == A / attempt / 'exact_response_inputs' / Path(original).name
            assert sha256(read(copy)).hexdigest() == row['sha256']
            additions[str(copy)] = original; groups[str(copy)] = 'A01' if attempt.endswith('01') else 'A02'
    mapping = data(PAPER / 'source_context/MAPPING.json')
    assert PINS[str(PAPER / 'source_context/MAPPING.json')]['sha256'] == 'cc642a35e810b072e9cd4dcc8a9353e6fe0afc9f3c68eb2ff5546f876089245f'
    for original, row in mapping.items():
        if row['snapshot'].startswith('source_context/workspace/'):
            assert row['snapshot'] == 'source_context/workspace/' + Path(original).relative_to(ROOT).as_posix()
            copy = PAPER / row['snapshot']; read(copy)
            assert PINS[str(copy)] == {k: row[k] for k in ('sha256', 'bytes')}
            additions[str(copy)] = original; groups[str(copy)] = 'author_workspace'
    roles = data(B / 'delta_check_01/EXACT_HISTORY_ALIASES.json')
    for name, digest in [('PAPER_STATUS.md', '304c24e871a27bd02bcd6db231abc37870fb263a01d4c081289bdd53e8718a73'),
                         ('ROOT_ADOPTION.md', '8f82ae0af7156131f14e9e6e849198f8b1c98564760c30d4bc121b50cf34f82e')]:
        copy = B / 'delta_check_01/response_anchors' / name; original = str(PAPER / name)
        assert roles[original + ' @ ' + digest] == str(copy) and sha256(read(copy)).hexdigest() == digest
        additions[str(copy)] = original; groups[str(copy)] = 'B01'
    comparisons, missing, fixed = [], [], Counter()
    for row in old['links']:
        source = additions.get(row['document']) if not row['explicit_table'] else None
        target = row['href'].strip().strip('<>').split('#', 1)[0]
        destination = (Path(source).parent / unquote(target)).resolve() if source else Path(row['destination'])
        current = {**row, 'destination': str(destination), 'exists': destination.exists(),
                   'semantic_origin': source or row['semantic_origin']}
        if source:
            comparisons.append({'before': row, 'after': current, 'origin_group': groups[row['document']]})
        if not row['exists'] and current['exists']: fixed[groups[row['document']]] += 1
        if not current['exists']: missing.append(current)
    assert len(old['missing']) == 176 and fixed == {'A01': 9, 'B01': 10, 'author_workspace': 157}
    assert missing == []
    after = {p: {'sha256': sha256(Path(p).read_bytes()).hexdigest(), 'bytes': Path(p).stat().st_size} for p in PINS}
    assert after == PINS
    result = {'scope': __doc__, 'status': 'STATIC_EXACT_ORIGIN_ADDITIONS_RESOLVE_RECORDED_MISSING_LINKS',
              'all_original_documents_unchanged': True, 'recorded_documents': old['documents'],
              'complete_line_scan_local_links_recomputed': len(old['links']), 'frozen_link_tables_unchanged': True,
              'old_missing': len(old['missing']), 'resolved_by_exact_origin': dict(fixed), 'remaining_missing': missing,
              'registered_origin_roles_by_group': dict(Counter(groups.values())), 'origin_comparisons': comparisons,
              'inputs_before': PINS, 'inputs_after': after, 'target_executions': 0, 'artifact_gate_result': 'NOT_EXECUTED'}
    with (HERE / 'LINK_ADDITIONS_RESULT.json').open('x') as stream: json.dump(result, stream, sort_keys=True, indent=2); stream.write('\n')
    print(json.dumps({k: result[k] for k in ('status', 'recorded_documents', 'complete_line_scan_local_links_recomputed',
        'old_missing', 'resolved_by_exact_origin', 'remaining_missing', 'registered_origin_roles_by_group')}, sort_keys=True))


if __name__ == '__main__': main()
