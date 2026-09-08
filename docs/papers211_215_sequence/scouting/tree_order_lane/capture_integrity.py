"""Post-run artifact checks only; never imports or executes the pilot."""
import ast
import hashlib
import json
from pathlib import Path

base = Path(__file__).resolve().parent
root = base.parents[3]
originals = [
    'papers/114-rooted-forest-leaf-peeling/main.tex',
    'papers/144-leftmost-dyck-reassociation/main.tex',
    'papers/148-even-level-plane-tree-contraction/PROOF_PACKAGE.md',
    'papers/195-odd-side-least-neighbor-trees/main.tex',
    'papers/195-odd-side-least-neighbor-trees/PROOF_PACKAGE.md',
    'docs/papers197_201_sequence/scouting/graph_matching_lane/BREADTH_AND_KILL_LEDGER.md',
    'docs/papers197_201_sequence/scouting/final_seat_tree_lane_20260905/SOURCE_OWNER_AUDIT.md',
    'docs/papers162_166_sequence/scouting/root/SCOUT.md',
    'docs/papers162_166_sequence/scouting/geometry_group/SCOUT.md',
    'docs/papers162_166_sequence/scouting/geometry_group/verify_scout.py',
]


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


hist = {p: digest(root / p) for p in originals}
receipt = json.loads((base / 'execution_01/NATIVE_RECEIPT.json').read_text())
assert receipt['exit_code'] == 0 and not receipt['timed_out']
assert receipt['input_sha256_before'] == receipt['input_sha256_after']
for p, h in receipt['input_sha256_before'].items():
    assert digest(Path(p)) == h
for name in ('stdout', 'stderr'):
    p = base / 'execution_01' / (name + '.txt')
    assert digest(p) == receipt[name + '_sha256']
    assert p.stat().st_size == receipt[name + '_bytes']
rows = [ast.literal_eval(line) for line in
        (base / 'execution_01/stdout.txt').read_text().splitlines()]
summaries = [r for r in rows if r[0] == 'summary']
assert [r[2] for r in summaries] == [1, 1, 3, 16, 125, 1296]
state_rows = [r for r in rows if r[0] == 'state']
assert len(state_rows) == 1442
assert rows[-1] == ('PASS', 'author_tiny_pressure_only', 7222)
for n, count in zip(range(1, 7), (1, 1, 3, 16, 125, 1296)):
    nr = [r for r in state_rows if r[1] == n]
    assert [r[2] for r in nr] == list(range(count))
    assert all(0 <= r[4] < count for r in nr)
runtime = ast.literal_eval((base / 'execution_01/stderr.txt').read_text())
assert runtime[0] == 'runtime'
runtime_files = sorted({str(Path(p).resolve()) for _, p in runtime[3] if p})
assert len(runtime_files) == 7
postpins = {p: digest(Path(p)) for p in runtime_files}
postpins[str(Path('/usr/bin/python3').resolve())] = digest(Path('/usr/bin/python3').resolve())
assert hist == {p: digest(root / p) for p in originals}
assert postpins == {p: digest(Path(p)) for p in postpins}
(base / 'INPUT_PINS.sha256').write_text(''.join(h + '  ' + p + '\n' for p, h in sorted(hist.items())))
(base / 'RUNTIME_POST_PINS.sha256').write_text(''.join(h + '  ' + p + '\n' for p, h in sorted(postpins.items())))
report = {
    'status': 'PASS_ARTIFACT_ONLY',
    'historical_original_files': len(hist),
    'historical_sha256': hist,
    'runtime_post_only_files': len(postpins),
    'runtime_post_only_sha256': postpins,
    'full_state_record_count': len(state_rows),
    'full_summary_record_count': len(summaries),
    'scientific_executions_in_this_capture': 0,
    'scientific_run_count_total_in_lane': 1,
    'pilot_claimed_assertions': 7222,
    'source_runtime_limits': [
        'Runtime file pins are post-run only, not proved to be unchanged during pilot',
        'No interpreter/library snapshots, dynamic loader or process map capture',
        'Early discovery raw outputs were not completely captured locally',
        'No second execution or independent verifier',
        'No scientific replay is implied by parsing canonical rows',
    ],
}
(base / 'INTEGRITY_REPORT.json').write_text(json.dumps(report, indent=2, sort_keys=True) + '\n')
print(json.dumps(report, indent=2, sort_keys=True))
