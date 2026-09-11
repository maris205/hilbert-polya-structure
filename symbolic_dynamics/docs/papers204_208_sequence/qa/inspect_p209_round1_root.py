"""Independent read-only physical Round1 closure; does not call the freezer."""
from pathlib import Path
import hashlib
import json
import re
import subprocess

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
PAPER = ROOT / 'papers/209-ordered-fibre-threading'
ROUND0, ROUND1 = PAPER / 'frozen_round0', PAPER / 'frozen_round1'
BATCH = ROOT / 'docs/papers204_208_sequence'
pins = {}

def read(path):
    p = Path(path)
    assert p.is_file() and not p.is_symlink(), str(p)
    data = p.read_bytes()
    value = hashlib.sha256(data).hexdigest()
    assert str(p) not in pins or pins[str(p)] == value, str(p)
    pins[str(p)] = value
    return data

def digest(path):
    return hashlib.sha256(read(path)).hexdigest()

def load(path):
    return json.loads(read(path))

def manifest(path, base, complete=False):
    entries = {}
    for line in read(path).decode().splitlines():
        value, name = line.split('  ', 1)
        p = Path(name)
        assert re.fullmatch('[0-9a-f]{64}', value) and name not in entries
        assert not p.is_absolute() and p.as_posix() == name and '..' not in p.parts
        assert digest(base / p) == value
        entries[name] = value
    if complete:
        all_paths = list(base.rglob('*'))
        assert all(not p.is_symlink() for p in all_paths)
        assert {p.relative_to(base).as_posix() for p in all_paths if p.is_file()} == set(entries) | {path.name}
        assert path.parent == base and path.name not in entries
    return entries

assert digest(ROUND1 / 'SHA256SUMS') == 'c93e16cf20d2eb87f3b454fbdb3576e52c6c79fb74c8712a277efeab7e60ce57'
r1 = manifest(ROUND1 / 'SHA256SUMS', ROUND1, True)
r0 = manifest(ROUND0 / 'SHA256SUMS', ROUND0, True)
author = manifest(PAPER / 'AUTHOR_MANIFEST.sha256', PAPER)
assert len(r1) == 2003 and len(r0) == 1989 and len(author) == 1985
assert all(r1.get(name) == value for name, value in r0.items())
assert manifest(ROUND1 / 'AUTHOR_MANIFEST.sha256', ROUND1) == author
assert all(r0[name] == value for name, value in author.items())
meta = load(ROUND1 / 'ROUND1_PROVENANCE.json')
assert meta['schema'] == 'p209-round1-provenance-v2'
assert meta['core_payload_pins'] == r0
assert meta['historical_core_status_and_metadata_unchanged'] is True
assert meta['author_payloads_preserved'] == 1985 and meta['round0_core_payloads_copied'] == 1989
for name, value in meta['all_source_inputs_before_and_rechecked_after'].items():
    assert digest(name) == value
for name, value in meta['accepted_review_and_root_manifest_referents'].items():
    assert digest(name) == value
for name, row in meta['anchor_mapping'].items():
    assert row['physical_path'] == 'ROUND1_ACCEPTANCE/' + name
    assert digest(row['original_path']) == digest(ROUND1 / row['physical_path']) == row['sha256']
assert len(meta['anchor_mapping']) == 11
history = meta['historical_external_resolution']
old_history = load(ROUND0 / 'FROZEN_LINK_MAP.json')['external_input_pins']
assert set(history) == set(old_history) and len(history) == 132
used = 0
for origin, row in history.items():
    assert row['sha256'] == old_history[origin]
    assert digest(row['physical_path']) == digest(row['round1_physical_path']) == row['sha256']
    assert digest(origin) == row['current_original_sha256']
    if row['copy_relative']:
        assert row['mode'] == 'exact-historical-alias'
        assert row['round1_physical_path'] == str(ROUND1 / row['copy_relative'])
        used += 1
assert used == meta['physical_historical_alias_payloads'] == 1
for row in meta['round1_core_link_map'] + meta['acceptance_and_historical_anchor_link_map']:
    assert digest(row['physical_target']) == row['sha256']
assert len(meta['round1_core_link_map']) == 243
assert len(meta['acceptance_and_historical_anchor_link_map']) == 16
prior = meta['prior_whole_paper_manifest']
assert prior['complete_current_paper_after_round1'] is False
assert prior['original_referent_base'] == str(PAPER)
assert digest(prior['physical_path']) == digest(prior['original_path']) == prior['sha256']
assert manifest(Path(prior['physical_path']), PAPER) == prior['original_referent_pins']
assert len(prior['original_referent_pins']) == 3978
accepted = meta['accepted_root_assertions']
assert accepted == load(ROUND1 / 'ROUND1_ACCEPTANCE/ROOT_DELTA_CLOSURE.actual.json')
assert accepted['status'] == 'ROOT_ACCEPTED_A_DELTA_ORIGINAL_CLOSURE_PASS'
assert accepted['current_open_findings'] == 0
for rel, count in [('reviews/p209_a',1342), ('qa/root_replays/p209_a_strict/root_a_pair_01',462), ('qa/root_replays/p209_a_strict/launcher_root_a_pair_01',10), ('qa/p209_round1_preparation_v2',9), ('qa/p209_round1_preparation',10)]:
    assert len(manifest(BATCH / rel / 'SHA256SUMS', BATCH / rel, True)) == count
assert digest(ROUND1 / 'ROUND1_FREEZE_ADAPTER.py') == meta['freezer_sha256'] == digest(meta['freezer_origin'])
assert meta['environment'] == {'PATH':'/usr/bin:/bin','LANG':'C.UTF-8','LC_ALL':'C.UTF-8','TZ':'UTC'}
assert meta['launch_orig_argv'][0:4] == ['/usr/bin/python3.10','-I','-S','-B']
assert not (ROUND1 / 'never_created_freezer_cache').exists()
assert len(meta['raw_comparisons']) == 3 and all(row['exit'] == 0 and row['outcome'] == 'COMPLETED' and row['stdout'] == row['stderr'] == '' for row in meta['raw_comparisons'])
comparisons = []
for a,b in ((PAPER/'main.pdf',ROUND1/'main.pdf'), (ROUND0/'main.pdf',ROUND1/'main.pdf'), (ROUND0/'SHA256SUMS',ROUND1/'ROUND1_ACCEPTANCE/ROUND0_CORE_MANIFEST.sha256'), (PAPER/'SHA256SUMS',ROUND1/'AUTHOR_MANIFEST.sha256')):
    argv = ['/usr/bin/cmp','--',str(a),str(b)]
    digest('/usr/bin/cmp')
    p = subprocess.run(argv, cwd=ROOT, env=meta['environment'], capture_output=True)
    comparisons.append({'argv':argv,'exit':p.returncode,'stdout':p.stdout.decode(),'stderr':p.stderr.decode()})
    assert p.returncode == 0 and p.stdout == p.stderr == b''
assert manifest(ROUND1/'SHA256SUMS',ROUND1,True) == r1
assert manifest(ROUND0/'SHA256SUMS',ROUND0,True) == r0
for name,value in list(pins.items()):
    assert digest(name) == value
print(json.dumps({'status':'PASS_ROOT_PHYSICAL_P209_ROUND1_CLOSURE',
    'round1_payloads':len(r1),'round1_manifest_sha256':digest(ROUND1/'SHA256SUMS'),
    'unchanged_round0_payloads':len(r0),'unchanged_author_payloads':len(author),
    'acceptance_anchors':11,'physical_historical_aliases':used,'core_links':243,'anchor_links':16,
    'before_after_freezer_inputs_checked':len(meta['all_source_inputs_before_and_rechecked_after']),
    'current_read_paths_checked_twice':len(pins),'raw_comparisons':comparisons,
    'current_git_observation_sha256':history[str(BATCH/'GIT_SYNC_RECEIPT.md')]['current_original_sha256'],
    'prior_whole_manifest_physical_anchor':prior['physical_path'],
    'scope':'Physical/documentary closure, no new mathematical producer/build/view. Accepted A evidence unchanged; B and terminal gates remain.'},indent=2,sort_keys=True))
