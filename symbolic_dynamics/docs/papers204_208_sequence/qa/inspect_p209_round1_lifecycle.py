"""Scoped post-Round1 rollup/control lifecycle check, not a new review."""
from pathlib import Path
import json
import runpy

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
BATCH = ROOT / 'docs/papers204_208_sequence'
QA = BATCH / 'qa'
PAPER = ROOT / 'papers/209-ordered-fibre-threading'
R1 = PAPER / 'frozen_round1'
A = BATCH / 'reviews/p209_a'
helper = QA / 'inspect_p209_a_initial.py'
D = runpy.run_path(str(helper), run_name='lifecycle_read_helpers_not_main')
pin, obj, manifest = (D[name] for name in ('pin', 'obj', 'manifest'))
def h(path):
    return pin(path)['sha256']
pin(helper); pin(Path(__file__))
aliases = {
    (str(PAPER / 'PAPER_MANIFEST.sha256'), 'cd8b345c2e8c7e71afa9d2d2d64e6ca74332828b4447e43ba6894c5a8398a4b2'): R1 / 'ROUND1_ACCEPTANCE/PRE_ROUND1_PAPER_MANIFEST.sha256',
    (str(BATCH / 'GIT_SYNC_RECEIPT.md'), 'af1754c9d6095c0f943b75fe7b9819ebd2b7c4db9609930ca7feccf2934786da'): QA / 'central_lifecycle_p209_a/GIT_SYNC_RECEIPT.before.md',
    (str(BATCH / 'GIT_SYNC_RECEIPT.md'), '2f6998d2986831fa8776e31e9d336497e6ab37b114d1b13ef94879f3e2271c24'): QA / 'central_lifecycle_p209_round1/GIT_SYNC_RECEIPT.before.md',
}
resolved_aliases = {}
def resolve(path, expected):
    if h(path) == expected:
        return Path(path)
    physical = aliases.get((str(path), expected))
    assert physical is not None and h(physical) == expected, str(path)
    resolved_aliases[(str(path), expected)] = str(physical)
    return physical
for (_, expected), physical in aliases.items():
    assert h(physical) == expected
assert len(manifest(QA / 'central_lifecycle_p209_round1/SHA256SUMS', complete=True)) == 5
assert len(manifest(QA / 'central_lifecycle_p209_a/SHA256SUMS', complete=True)) == 3
assert h(R1 / 'SHA256SUMS') == 'c93e16cf20d2eb87f3b454fbdb3576e52c6c79fb74c8712a277efeab7e60ce57'
r1 = manifest(R1 / 'SHA256SUMS', complete=True)
assert len(r1) == 2003
whole = manifest(PAPER / 'PAPER_MANIFEST.sha256', complete=True)
prior = manifest(R1 / 'ROUND1_ACCEPTANCE/PRE_ROUND1_PAPER_MANIFEST.sha256', base=PAPER)
assert len(whole) == 5982 and len(prior) == 3978
assert all(whole[name] == value for name, value in prior.items())
additions = {name: value for name, value in whole.items() if name not in prior}
assert additions == {'frozen_round1/' + name: value for name,value in r1.items()} | {'frozen_round1/SHA256SUMS': h(R1/'SHA256SUMS')}
assert len(manifest(PAPER / 'frozen_round0/SHA256SUMS', complete=True)) == 1989
assert len(manifest(PAPER / 'AUTHOR_MANIFEST.sha256')) == 1985
assert h(A / 'SHA256SUMS') == 'dbc1f31fd1ba6324f421bed5b78bd1566b641e21d3d552630e688ab5cea7c7b3'
assert len(manifest(A / 'SHA256SUMS', complete=True)) == 1342
assert len(manifest(A / 'INITIAL_REVIEW_SEAL.sha256')) == 1227
counts = {}
for label, path, count in [('accepted_a_delta', A / 'delta_check_02/INPUTS_BEFORE.json', 124214),
                           ('original_a_closure', A / 'initial_audit_01/CURRENT_INPUT_CLOSURE.json', 120491)]:
    values = obj(path)
    assert len(values) == count
    if label == 'accepted_a_delta':
        assert values == obj(A / 'delta_check_02/INPUTS_AFTER.json')
    for origin,value in values.items():
        resolve(origin,value)
    counts[label] = len(values)
meta = obj(R1 / 'ROUND1_PROVENANCE.json')
for origin,value in meta['all_source_inputs_before_and_rechecked_after'].items():
    resolve(origin,value)
for origin,value in meta['accepted_review_and_root_manifest_referents'].items():
    resolve(origin,value)
for row in meta['round1_core_link_map'] + meta['acceptance_and_historical_anchor_link_map']:
    resolve(row['physical_target'],row['sha256'])
counts['round1_freezer_input_paths'] = len(meta['all_source_inputs_before_and_rechecked_after'])
# Full earlier byte pins plus explicit configuration-presence/source-inventory
# checks preserve the accepted mathematical/build reuse key. No producer runs.
modes = [D['settings_and_commands'](A / ('review_' + mode + '_01'), mode) for mode in ('pair','build')]
for path in list(D['READS']):
    pin(path, fresh=True)
assert manifest(PAPER / 'PAPER_MANIFEST.sha256', complete=True) == whole
print(json.dumps({'status':'PASS_P209_ROUND1_ROLLUP_AND_EXACT_LIFECYCLE_MAPPING',
    'whole_paper_payloads':len(whole),'whole_paper_manifest_sha256':h(PAPER/'PAPER_MANIFEST.sha256'),
    'prior_whole_payloads':len(prior),'only_added_round1_paths':len(additions),
    'unchanged_round1_payloads':len(r1),'input_sets':counts,
    'actual_used_exact_aliases':[{'original_path':key[0],'original_sha256':key[1],'physical_path':value} for key,value in sorted(resolved_aliases.items())],
    'all_declared_documentary_aliases':[{'original_path':key[0],'original_sha256':key[1],'physical_path':str(value)} for key,value in sorted(aliases.items())],
    'unchanged_review_runtime_build_modes':modes,'actual_current_read_paths_checked_twice':len(D['READS']),
    'scope':'Lifecycle-only original-pin/exact-history and rollup validation after prior accepted full gate; not new mathematics, review, build, render or page view.'},indent=2,sort_keys=True))
