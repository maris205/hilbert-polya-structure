"""B initial evidence audit, not a mathematical verifier or execution reenactment."""
import collections
import gzip
import hashlib
import json
import os
from pathlib import Path
import re
import sys
import time

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
HERE = Path(__file__).resolve().parent
PAPER = ROOT / 'papers/210-weakly-increasing-run-aggregation'
FROZEN = PAPER / 'frozen_round1'
A = ROOT / 'docs/papers204_208_sequence/reviews/p210_a'
ENV = {'PATH': '/usr/bin:/bin', 'LANG': 'C.UTF-8', 'LC_ALL': 'C.UTF-8', 'TZ': 'UTC'}
assert dict(os.environ) == ENV
assert sys.flags.isolated and sys.flags.no_site and sys.dont_write_bytecode and sys.flags.optimize == 0
assert sys.pycache_prefix and not Path(sys.pycache_prefix).exists()
started = time.time()
checks = 0
reads, roles, commands, comparisons = {}, collections.defaultdict(set), [], []


def demand(ok, label):
    global checks
    checks += 1
    if not ok:
        raise AssertionError(label)


def pin(path, role):
    path = Path(path)
    name = str(path)
    roles[role].add(name)
    if name not in reads:
        demand(path.is_file(), 'physical file: ' + name)
        h = hashlib.sha256()
        with path.open('rb') as stream:
            for block in iter(lambda: stream.read(1 << 20), b''):
                h.update(block)
        reads[name] = dict(real=str(path.resolve()), sha256=h.hexdigest(), size=path.stat().st_size,
                           symlink=os.readlink(path) if path.is_symlink() else None)
    return reads[name]


def read(path, role='evidence_json'):
    pin(path, role)
    with (gzip.open(path, 'rt') if str(path).endswith('.gz') else Path(path).open()) as stream:
        return json.load(stream)


def expect(path, sha, role):
    demand(pin(path, role)['sha256'] == sha, 'sha256: ' + str(path))


def fullcmp(left, right, role):
    pin(left, role)
    pin(right, role)
    demand(Path(left).read_bytes() == Path(right).read_bytes(), 'complete byte equality: ' + str(left))
    comparisons.append(dict(left=str(left), right=str(right), role=role,
                            method='complete Python byte equality, not native cmp', equal=True))


def manifest(path, base, count, exact=False, aliases=None):
    pin(path, 'manifests')
    entries = {}
    for line in path.read_text().splitlines():
        sha, name = line.split('  ', 1)
        demand(bool(re.fullmatch('[0-9a-f]{64}', sha)) and name not in entries, 'manifest syntax/uniqueness')
        relative = Path(name)
        demand(not relative.is_absolute() and '..' not in relative.parts, 'safe relative manifest entry')
        entries[name] = sha
        target = base / name
        target = aliases.get(str(target), target) if aliases else target
        expect(target, sha, 'manifest_referents')
    demand(len(entries) == count, 'manifest count: ' + str(path))
    if exact:
        actual = {str(p.relative_to(base)) for p in base.rglob('*') if p.is_file() and p != path}
        demand(set(entries) == actual, 'exact physical manifest coverage: ' + str(base))
    return entries


expect(FROZEN / 'SHA256SUMS', 'be54b79806d90f22037cee877f92074e744b2ef27bcc0b6b2e4f8dfa658446e0', 'round1_seal')
frozen_entries = manifest(FROZEN / 'SHA256SUMS', FROZEN, 508, True)
input_entries = manifest(HERE / 'INPUT_PINS.sha256', ROOT, 509)
demand(set(input_entries) == {str(p.relative_to(ROOT)) for p in FROZEN.rglob('*') if p.is_file()}, 'all 509 B input pins')
prov = read(FROZEN / 'ROUND1_PROVENANCE.json', 'round1_provenance')
demand(prov['round0_external_aliases'] == [], 'no unrecorded old prefix aliases')
demand(len(prov['initial_review_aliases']) == 2, 'exactly two initial A aliases')
aliases = {}
for row in prov['initial_review_aliases']:
    expect(row['physical_path'], row['sha256'], 'exact_initial_A_alias')
    aliases[row['original_path']] = Path(row['physical_path'])
demand(set(aliases) == {str(A / 'DELTA.md'), str(A / 'SHA256SUMS')}, 'no generic alias fallback')
for key, count in [('round1_core_link_map', 57), ('acceptance_anchor_link_map', 14)]:
    demand(len(prov[key]) == count, key + ' exact count')
    for row in prov[key]:
        doc = FROZEN / row['document']
        pin(doc, key)
        demand(row['href'] in doc.read_text(), 'literal link exists in pinned document')
        expect(row['physical_target'], row['sha256'], key)
        if 'document_sha256' in row:
            expect(doc, row['document_sha256'], 'linked_document')
        if 'round0_physical_target' in row:
            expect(row['round0_physical_target'], row['sha256'], 'linked_round0_original')
for path, sha in prov['round0_external_original_pins'].items():
    expect(path, sha, '33_exact_round0_external_originals')
demand(len(prov['round0_external_original_pins']) == 33, '33 external originals')
for name, sha in prov['core_payload_pins'].items():
    expect(FROZEN / name, sha, '493_unchanged_core')
    fullcmp(FROZEN / name, PAPER / 'frozen_round0' / name, '493_round0_round1_full_copy')
demand(len(prov['core_payload_pins']) == 493, '493 core payloads')
expect(PAPER / 'frozen_round0/SHA256SUMS', prov['round0_manifest_sha256'], 'round0_seal')
author_entries = manifest(FROZEN / 'AUTHOR_MANIFEST.sha256', FROZEN, 489)
for name, sha in author_entries.items():
    expect(PAPER / name, sha, '489_live_author_still_unchanged')
expect(A / 'SHA256SUMS', 'f6b92663cb2a7909f85a25a892ee4433ccd6177e84c07bf7ceccc9555b191f6d', 'accepted_A_seal')
manifest(A / 'SHA256SUMS', A, 552, True)
initial_a = manifest(A / 'history/initial_before_delta/SHA256SUMS', A, 484, aliases=aliases)
for path, sha in prov['accepted_review_and_root_manifest_referents'].items():
    expect(path, sha, '611_accepted_A_root_referents')
demand(len(prov['accepted_review_and_root_manifest_referents']) == 611, '611 accepted referents')
for row in prov['anchors'].values():
    expect(FROZEN / row['physical_path'], row['sha256'], 'frozen_acceptance_anchor')
    # The pre-Round1 lifecycle/whole manifest are explicitly historical, not current path assertions.
    if row['original_path'] not in {str(PAPER / 'ROOT_LIFECYCLE.md'), str(PAPER / 'PAPER_MANIFEST.sha256')}:
        expect(row['original_path'], row['sha256'], 'unchanged_acceptance_original')

for path in [A / 'pair02/tools/evidence.py', A / 'pair02/tools/runtime_probe.py',
             ROOT / 'docs/papers204_208_sequence/qa/p210_a_strict_preparation/run_pair.py',
             ROOT / 'docs/papers204_208_sequence/qa/p210_checkpoint_identity_revision_01/process_support.py',
             ROOT / 'docs/papers204_208_sequence/qa/batch_terminal_build_preparation/build_four.py']:
    pin(path, 'disclosed_infrastructure_originals_read')
for path in HERE.glob('*.py'):
    pin(path, 'B_program_sources')
for path in (HERE / 'instrumentation').glob('*.py'):
    pin(path, 'B_program_sources')
first = read(HERE / 'COMMITMENT.actual.json')
for name, sha in first['files'].items():
    expect(HERE / ('history/verify.initial_reconstructed.py' if name == 'verify.py' else name), sha, 'initial_commitment_exact_role')
for file in ['COMPLETE_SOURCE_COMMITMENT.actual.json', 'PRE_COMPARISON_PROOF_CODE_COMMITMENT.actual.json']:
    data = read(HERE / file)
    for name, sha in data.get('files', data.get('pins')).items():
        expect(HERE / name, sha, 'complete_precomparison_commitments')
fullcmp(HERE / 'verify.py', HERE / 'verify.committed.py', 'physical_committed_science')
for label in ['produce01', 'pair01']:
    for name in ['verify.py', 'PARAMETERS.json', 'COMPLETE_SOURCE_COMMITMENT.actual.json']:
        fullcmp(HERE / name, HERE / label / 'source' / name, 'science_source_copy')
    fullcmp(HERE / 'CANONICAL.json', HERE / label / 'commands/run_1/stdout', 'canonical_from_actual_stdout')
fullcmp(HERE / 'CANONICAL.json', HERE / 'pair01/commands/run_2/stdout', 'second_native_canonical')
fullcmp(HERE / 'CANONICAL.json', HERE / 'pair01/source/CANONICAL.json', 'pair_canonical_input')

def native(directory, expected):
    attempt = read(directory / 'ATTEMPT.json', 'native_attempt')
    result = read(directory / 'RESULT.json', 'native_result')
    demand(attempt['environment'] == ENV, 'safe exact child environment')
    demand(type(result['native_returncode']) is int and result['native_returncode'] == expected, 'actual native integer return')
    for name in ['stdout', 'stderr']:
        record = pin(directory / name, 'native_full_raw_stream')
        expected_sha = result[name]['sha256'] if name in result else result[name + '_sha256']
        demand(record['sha256'] == expected_sha, 'native full raw stream binding')
        if name in result:
            demand(record['size'] == result[name]['bytes'], 'native raw size')
    settlement = result.get('settlement', result.get('process_group_settlement'))
    demand(settlement['quiescent'] and not any(r['state'] != 'Z' for r in settlement['remaining_members']), 'owned group settled')
    demand(result['owned_sid'] == result['owned_pgid'] == result.get('pid', result.get('native_pid')), 'native owner identity')
    demand(result.get('end_ns', result.get('ended_epoch')) >= attempt.get('start_ns', attempt.get('started_epoch')), 'chronological attempt/result')
    for arg in attempt['argv']:
        if arg.startswith('pycache_prefix='):
            demand(not Path(arg.split('=', 1)[1]).exists(), 'native absent cache remained absent')
    commands.append(dict(directory=str(directory), argv=attempt['argv'], cwd=attempt['cwd'],
                         environment=ENV, native_returncode=expected))


for directory in sorted((HERE / 'native').iterdir()):
    if (directory / 'RESULT.json').is_file():
        native(directory, 1 if directory.name in {'build01', 'audit01'} else 0)
for label in ['produce01', 'pair01', 'build01', 'build02']:
    for directory in sorted((HERE / label / 'commands').iterdir()):
        native(directory, 0)

def mapfiles(raw):
    return [Path(row.split(None, 5)[5]) for row in raw.splitlines()
            if len(row.split(None, 5)) == 6 and row.split(None, 5)[5].startswith('/')]


replay_keys = {}
for label in ['produce01', 'pair01', 'build02']:
    folder = HERE / label
    before = read(folder / 'INPUTS_BEFORE.json.gz', 'runtime_before_ledger')
    after = read(folder / 'INPUTS_AFTER.json.gz', 'runtime_after_ledger')
    demand(before == after, 'full files/configuration/membership unchanged: ' + label)
    demand(before['membership'] == sorted(before['files']), 'exact inventory membership')
    for path, expected in before['files'].items():
        demand(pin(path, 'full_current_dependency_reread') == expected, 'full dependency physical key: ' + path)
    for path, expected in before['configuration'].items():
        p = Path(path)
        actual = dict(lexists=os.path.lexists(p), exists=p.exists(), is_file=p.is_file(), is_dir=p.is_dir(),
                      resolved=str(p.resolve()), symlink=os.readlink(p) if p.is_symlink() else None)
        demand(actual == expected, 'configuration/presence still exact: ' + path)
    known = {row['real'] for row in before['files'].values()}
    for phase in ['BEFORE', 'AFTER']:
        sample = read(folder / ('PARENT_MAPS_' + phase + '.json'), 'driver_runtime_observation')
        observed = mapfiles(sample['raw']) + [Path(p) for p in sample['modules'].values() if p]
        for p in observed:
            if p.is_file():
                demand(str(p.resolve()) in known, 'observed parent input included')
    for runtime in sorted(folder.glob('runtime_*.json')):
        sample = read(runtime, 'scientific_runtime_observation')
        demand(sample['settings']['environment'] == ENV, 'actual scientific environment')
        flags = sample['settings']['flags']
        demand(all(s in flags for s in ['optimize=0', 'dont_write_bytecode=1', 'no_site=1', 'isolated=1']), 'actual source-only unoptimized flags')
        observed = list(map(Path, sample['existing_reads'])) + mapfiles(sample['maps_before']) + mapfiles(sample['maps_after'])
        observed += [Path(p) for p in sample['modules'].values() if p]
        for p in observed:
            if p.is_file():
                demand(str(p.resolve()) in known, 'observed child input included')
                demand(p.suffix not in {'.pyc', '.pyo'} and not any(v in p.parts for v in ['site-packages', 'dist-packages']), 'no forbidden observed child input')
    payloads = read(folder / 'PAYLOADS.json', 'run_nonself_payload_inventory')
    for path, expected in payloads.items():
        demand(pin(path, 'run_payload_referent') == expected, 'run payload unchanged: ' + path)
    report = read(folder / 'REPORT.json', 'run_report')
    demand(report['status'] == 'PASS' and report['checks_passed'] and report['changed_inputs'] == [], 'actual passing run')
    demand(report['input_count'] == len(before['files']), 'report ledger count')
    replay_keys[label] = dict(before=str(folder / 'INPUTS_BEFORE.json.gz'), after=str(folder / 'INPUTS_AFTER.json.gz'),
                             files=len(before['files']), configuration=len(before['configuration']),
                             parent_before=str(folder / 'PARENT_MAPS_BEFORE.json'), parent_after=str(folder / 'PARENT_MAPS_AFTER.json'),
                             actual_scientific_observations=list(map(str, sorted(folder.glob('runtime_*.json')))))

demand(not (HERE / 'build01/REPORT.json').exists() and not (HERE / 'build01/INPUTS_AFTER.json.gz').exists(), 'failed build not promoted to closure')
demand('KeyError' in (HERE / 'native/build01/stderr').read_text(), 'retained actual first-build failure')
old = (HERE / 'instrumentation/evidence.py').read_text()
new = (HERE / 'instrumentation/evidence_build_v2.py').read_text()
demand(new == old.replace('for v in cap.before.values()', 'for v in cap.before["files"].values()'), 'one-line infrastructure-only build correction')
build = HERE / 'build02'
closure = read(build / 'FLS_CLOSURE.json')
demand(all(row['role'] != 'unresolved' for row in closure), 'all recorded FLS inputs classified')
for i in range(1, 5):
    folder = build / 'commands' / ('pass_' + str(i))
    before = read(folder / 'SOURCE_BEFORE.json', 'build_pass_prior_products')
    after = read(folder / 'SOURCE_AFTER.json', 'build_pass_after_products')
    for path, expected in after.items():
        source = Path(path)
        if source.name in ['main.log', 'main.fls', 'main.aux', 'main.bbl', 'main.blg', 'main.out', 'main.toc']:
            expect(folder / source.name, expected['sha256'], 'preserved_full_build_pass_product')
    for path in before:
        if Path(path).suffix in {'.tex', '.bib'}:
            demand(before[path] == after[path], 'source-only manuscript unchanged through each pass')
for path in sorted((build / 'source').rglob('*')):
    if path.suffix in {'.tex', '.bib'}:
        fullcmp(path, FROZEN / path.relative_to(build / 'source'), '10_source_only_build_copies')
fullcmp(build / 'source/main.pdf', FROZEN / 'main.pdf', 'B_round1_pdf_complete_bytes')
view = read(HERE / 'VIEW_build02.actual.json', 'actual_visual_observation_bindings')
demand(len(view['pages']) == 6 and {r['page'] for r in view['pages']} == set(range(1, 7)), 'six distinct actual page bindings')
expect(view['pdf_path'], view['pdf']['sha256'], 'actually_viewed_pdf')
for row in view['pages']:
    demand(row['actually_viewed'], 'human-facing visual inspection declaration')
    expect(row['image_path'], row['image']['sha256'], 'actually_viewed_page')
comparison = read(HERE / 'native/compare01/stdout', 'full_cross_schema_comparison')
demand(comparison['checks'] == 198189 and comparison['inputs_before'] == comparison['inputs_after'], 'full comparison actual checks and pins')
for path, expected in comparison['inputs_before'].items():
    rec = pin(path, 'semantic_comparison_inputs')
    demand(rec['sha256'] == expected['sha256'] and rec['size'] == expected['bytes'], 'cross-schema comparison original input')
canonical = read(HERE / 'CANONICAL.json', 'complete_B_canonical')
demand(canonical['checks'] == 51129 and sum(len(r['states']) for r in canonical['census']) == 4095, 'independent full original census')

def write(name, data):
    p = HERE / name
    with (gzip.open(p, 'xt') if p.suffix == '.gz' else p.open('x')) as stream:
        json.dump(data, stream, sort_keys=True, indent=2)
        stream.write('\n')


write('AUDIT_INPUTS.actual.json.gz', reads)
write('AUDIT_ROLES.actual.json', {role: sorted(paths) for role, paths in roles.items()})
write('REPLAY_KEYS.json', dict(schema='p210-b-runtime-consumable-keys-v1', ledgers=replay_keys,
      raw_native_command_directories=[row['directory'] for row in commands],
      boundary='Inner source-only scientific/driver runtime and complete declared resource-key snapshots, not OS/startup tracing of the outer native transport launcher.'))
write('AUDIT_COMPARISONS.actual.json', comparisons)
result = dict(status='PASS_INITIAL_EVIDENCE_AUDIT', checks=checks, full_byte_read_paths=len(reads),
              native_commands_checked=len(commands), full_python_byte_comparisons=len(comparisons),
              started_epoch=started, ended_epoch=time.time(), round1_physical_files=509,
              round1_core_links=57, acceptance_links=14, original_external_paths=33,
              accepted_A_payloads=552, initial_A_payloads=len(initial_a),
              current_manuscript_changes=False, accepted_delta=False,
              limitation='No reexecution of inherited A/root commands; no reconstruction of unavailable old recorder/start records; first failed build remains incomplete.')
write('AUDIT.actual.json', result)
print(json.dumps(result, sort_keys=True))
