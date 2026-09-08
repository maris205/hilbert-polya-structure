"""Read-only sealed-author integrity audit, not a scientific replay.

No SPR update, reverse recurrence, orbit traversal or fibre formula is
implemented or executed. Stored record columns are only reconciled with
the author's own archived summary and byte commitments.
"""
from collections import Counter
import gzip
import hashlib
import json
from pathlib import Path

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
LANE = ROOT / 'docs/papers211_215_sequence/scouting/arithmetic_lane'
MANIFEST_SHA = 'c1c920f98824d52df489e2dfcde8375e7ec7787f2f8def9ae090fdf082515056'
pins = {}
checks = 0


def demand(condition, message):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(message)


def pin(path):
    path = Path(path)
    key = str(path.relative_to(ROOT)) if path.is_relative_to(ROOT) else str(path)
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    if key in pins:
        demand(pins[key] == digest, ['input drift', key])
    pins[key] = digest
    return digest


def manifest(path, count, restricted=False):
    pin(path)
    lines = path.read_text().splitlines()
    demand(len(lines) == count, ['manifest count', path.name, len(lines)])
    seen = set()
    for line in lines:
        digest, sep, name = line.partition('  ')
        demand(sep == '  ' and len(digest) == 64, ['manifest syntax', line])
        demand(name not in seen, ['duplicate key', name])
        seen.add(name)
        item = ROOT / name
        demand(item.is_file() and not item.is_symlink(), ['input type', name])
        if restricted:
            demand(item.is_relative_to(LANE), ['author key outside lane', name])
        demand(pin(item) == digest, ['manifest digest', name])
    return seen


demand(pin(LANE / 'SHA256SUMS') == MANIFEST_SHA, 'author seal differs')
manifest(LANE / 'SHA256SUMS', 52, restricted=True)
manifest(LANE / 'HISTORICAL_INPUT_PINS.sha256', 10)
extra = [
    '.agents/skills/symbolic-dynamics-research/SKILL.md',
    'docs/research_state/WORKFLOW.md',
    'docs/papers211_215_sequence/PROBLEM_ANCHOR.md',
    'docs/papers197_201_sequence/PROBLEM_ANCHOR.md',
    'docs/papers197_201_sequence/HOSTILE_REVIEW_PROTOCOL.md',
    'docs/papers204_208_sequence/ARTIFACT_CONTRACT.md',
    'docs/papers187_191_sequence/scouting/algebra_lane/replacement/HISTORY_COLLISION.md',
    'papers/174-minimum-pivot-mobius-feedback/NARRATIVE_REPORT.md',
    'papers/174-minimum-pivot-mobius-feedback/SOURCE_VERIFICATION.md',
]
for name in extra:
    pin(ROOT / name)
for name in ['research-review', 'novelty-check']:
    pin(Path('/root/autodl-tmp/.codex/skills') / name / 'SKILL.md')

receipt = json.loads((LANE / 'sole_pilot/receipt.json').read_bytes())
demand(receipt['inputs_before'] == receipt['inputs_after'], 'author declared input delta')
for name, digest in receipt['inputs_before'].items():
    demand(pin(LANE / name) == digest, ['explicit scientific input differs', name])
demand(receipt['exit_code'] == 0 and not receipt['timed_out'], 'archived subprocess failed')
demand(receipt['end_unix_ns'] >= receipt['start_unix_ns'], 'negative duration')
demand(receipt['elapsed_seconds'] ==
       (receipt['end_unix_ns'] - receipt['start_unix_ns']) / 1e9, 'duration mismatch')
for name, info in receipt['outputs'].items():
    path = LANE / 'sole_pilot' / name
    demand(path.stat().st_size == info['bytes'] and pin(path) == info['sha256'],
           ['output mismatch', name])
demand((LANE / 'sole_pilot/stderr.raw').read_bytes() == b'', 'author stderr is not empty')

stdout = (LANE / 'sole_pilot/stdout.raw').read_bytes()
transcript = [json.loads(line) for line in stdout.splitlines()]
demand(len(transcript) == 37, 'transcript line count')
demand(transcript[0]['n'] == [1, 2, 3, 4, 5] and
       transcript[0]['M'] == [0, 1, 2, 3, 4, 5, 6], 'declared box list')
archive = gzip.decompress((LANE / 'sole_pilot/state_records.jsonl.gz').read_bytes())
demand(hashlib.sha256(archive).hexdigest() == transcript[-1]['records_uncompressed_sha256'],
       'uncompressed record commitment')
lines = iter(archive.splitlines(keepends=True))
states_total = 0
box_summaries = []
for row in transcript[1:-1]:
    n, M = row['n'], row['M']
    demand(json.loads(next(lines)) == {'box': [n, M]}, ['marker', n, M])
    digest = hashlib.sha256()
    height_hist, fibre_hist = Counter(), Counter()
    previous = None
    max_h, first_h, max_d, max_targets = -1, None, -1, []
    for ordinal in range(row['states']):
        raw = next(lines)
        digest.update(raw)
        record = json.loads(raw)
        demand(isinstance(record, list) and len(record) == 4, ['record schema', n, M, ordinal])
        x, image, h, indegree = record
        demand(len(x) == n and len(image) == n, ['column arity', n, M, ordinal])
        demand(all(type(v) is int and 0 <= v <= M for v in x + image),
               ['column value range', n, M, ordinal])
        demand(type(h) is int and h >= 0 and type(indegree) is int and indegree >= 0,
               ['stored statistics type', n, M, ordinal])
        demand(previous is None or previous < x, ['archived lex order', n, M, ordinal])
        previous = x
        height_hist[str(h)] += 1
        fibre_hist[str(indegree)] += 1
        if h > max_h:
            max_h, first_h = h, x
        if indegree > max_d:
            max_d, max_targets = indegree, [x]
        elif indegree == max_d:
            max_targets.append(x)
    demand(digest.hexdigest() == row['per_state_records_sha256'], ['box bytes', n, M])
    demand(dict(height_hist) == row['height_histogram'], ['stored height histogram', n, M])
    demand(dict(fibre_hist) == row['fibre_histogram'], ['stored degree histogram', n, M])
    demand([max_h, first_h, max_d, max_targets] ==
           [row['max_height'], row['first_max_height_witness'], row['max_fibre'], row['all_max_fibre_targets']],
           ['stored extrema summary', n, M])
    box_summaries.append({'n': n, 'M': M, 'archived_records': row['states']})
    states_total += row['states']
demand(next(lines, None) is None, 'extra archive lines')
demand(states_total == transcript[-1]['states'] == 34636, 'record total')
demand(len(box_summaries) == transcript[-1]['boxes'] == 35, 'box total')
for key, digest in list(pins.items()):
    path = Path(key) if key.startswith('/') else ROOT / key
    demand(hashlib.sha256(path.read_bytes()).hexdigest() == digest, ['end input drift', key])
print(json.dumps({'kind': 'sealed_author_integrity_only', 'status': 'PASS',
                  'checks': checks, 'pins': pins, 'pin_count': len(pins),
                  'box_summaries': box_summaries, 'archived_states': states_total,
                  'archive_bytes': len(archive), 'new_scientific_runs': 0,
                  'limits': 'No map/orbit/theorem recomputation; no hermetic runtime closure or scientific reuse certification.'},
                 sort_keys=True, indent=2))
