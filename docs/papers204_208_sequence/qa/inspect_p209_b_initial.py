"""Root full initial-B original/current-dependency closure, not a producer."""
from pathlib import Path
import json
import runpy
import subprocess

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
QA = ROOT / 'docs/papers204_208_sequence/qa'
BATCH = QA.parent
B = BATCH / 'reviews/p209_b'
A = BATCH / 'reviews/p209_a'
PAPER = ROOT / 'papers/209-ordered-fibre-threading'
R1 = PAPER / 'frozen_round1'
SEAL = 'd88b831e60414d47ae0b2afb2583b73d02fc9764877a00952f4a9d90d13488ea'
ENV = {'PATH': '/usr/bin:/bin', 'LANG': 'C.UTF-8', 'LC_ALL': 'C.UTF-8', 'TZ': 'UTC'}
helper = QA / 'inspect_p209_a_initial.py'
D = runpy.run_path(str(helper), run_name='root_b_read_helpers_only_not_main')
pin, obj, manifest, checkpin = (D[name] for name in ('pin','obj','manifest','checkpin'))
pin(helper); pin(__file__)

def h(path):
    return pin(path)['sha256']

assert h(B / 'SHA256SUMS') == SEAL
outer = manifest(B / 'SHA256SUMS', complete=True)
assert len(outer) == 1298
preseal = obj(B / 'PRESEAL_CHECK.json')
assert preseal['status'] == 'PASS_ORIGINAL_PACKAGE_PRESEAL'
assert preseal['delta_status'] == 'UNASSESSED'
for name, row in preseal['nested_seals'].items():
    path = B / name / 'SHA256SUMS'
    assert h(path) == row['sha256']
    assert len(manifest(path, complete=True)) == row['payloads']
assert len(preseal['nested_seals']) == 10
assert h(R1 / 'SHA256SUMS') == 'c93e16cf20d2eb87f3b454fbdb3576e52c6c79fb74c8712a277efeab7e60ce57'
frozen = manifest(R1 / 'SHA256SUMS', complete=True)
inputs = manifest(B / 'INPUT_PINS.sha256', base=ROOT)
assert len(frozen) == 2003 and len(inputs) == 2004
assert set(inputs) == {p.relative_to(ROOT).as_posix() for p in R1.rglob('*') if p.is_file()}
assert len(manifest(PAPER / 'PAPER_MANIFEST.sha256', complete=True)) == 5982
assert len(manifest(PAPER / 'frozen_round0/SHA256SUMS', complete=True)) == 1989
assert len(manifest(PAPER / 'AUTHOR_MANIFEST.sha256')) == 1985
assert len(manifest(R1 / 'AUTHOR_MANIFEST.sha256')) == 1985
assert h(A / 'SHA256SUMS') == 'dbc1f31fd1ba6324f421bed5b78bd1566b641e21d3d552630e688ab5cea7c7b3'
assert len(manifest(A / 'SHA256SUMS', complete=True)) == 1342

aliases = {}
def alias(origin, value, physical):
    assert h(physical) == value
    aliases.setdefault((str(origin), value), str(physical))

roles = obj(B / 'assignment_context/ROLES.json')
assert len(roles) == 10
for row in roles:
    alias(row['original'], row['sha256'], row['preserved'])
lifecycle = QA / 'central_lifecycle_p209_round1'
assert len(manifest(lifecycle / 'SHA256SUMS', complete=True)) == 5
for row in obj(lifecycle / 'CAPTURE.actual.json')['copies']:
    alias(row['original_path'], row['sha256'], row['physical_path'])
r = obj(R1 / 'ROUND1_PROVENANCE.json')
assert len(r['anchor_mapping']) == 11
for row in r['anchor_mapping'].values():
    alias(row['original_path'], row['sha256'], R1 / row['physical_path'])
assert len(r['historical_external_resolution']) == 132
for row in r['historical_external_resolution'].values():
    alias(row['original_path'], row['sha256'], row['round1_physical_path'])
resolved = {}
def resolve(origin, value):
    key = (str(origin), value)
    physical = aliases.get(key, str(origin))
    assert h(physical) == value, (origin, physical)
    if physical != str(origin):
        resolved[key] = physical
    return physical

for key, count in [('all_source_inputs_before_and_rechecked_after',5956),
                   ('accepted_review_and_root_manifest_referents',1814)]:
    assert len(r[key]) == count
    for origin, value in r[key].items():
        resolve(origin,value)
for key, count in [('round1_core_link_map',243),('acceptance_and_historical_anchor_link_map',16)]:
    assert len(r[key]) == count
    for row in r[key]:
        resolve(row['physical_target'],row['sha256'])
old = r['prior_whole_paper_manifest']
assert old['original_referent_base'] == str(PAPER)
assert not old['complete_current_paper_after_round1']
old_entries = manifest(old['physical_path'], base=PAPER)
assert old_entries == old['original_referent_pins'] and len(old_entries) == 3978

def metadata_map(folder, before_name, after_name, count=None):
    before = obj(folder / before_name)
    assert before == obj(folder / after_name)
    if count is not None:
        assert len(before) == count
    for origin, expected in before.items():
        assert 'error' not in expected and {'sha256','bytes'} <= set(expected)
        physical = resolve(origin,expected['sha256'])
        actual = pin(physical)
        assert actual['bytes'] == expected['bytes']
        if physical == origin:
            assert set(expected) <= set(actual)
            assert all(actual[k] == v for k,v in expected.items())
    return before

audit_folder = B / 'artifact_audit_03'
doc = metadata_map(audit_folder,'DOCUMENTARY_INPUTS_BEFORE.json','DOCUMENTARY_INPUTS_AFTER.json',127544)
audit_result = obj(audit_folder / 'AUDIT_RESULT.json')
assert audit_result['status'] == 'PASS_DOCUMENTARY_ROLE_AND_DEPENDENCY_AUDIT'
assert audit_result['documentary_inputs_before_and_after'] == len(doc)
assert audit_result['explicit_historical_resolutions'] == 13
assert audit_result['delta_status'] == 'UNASSESSED'
assert obj(audit_folder / 'CONFIGURATION_RECHECK_BEFORE.json') == obj(audit_folder / 'CONFIGURATION_RECHECK_AFTER.json')
assert len(obj(audit_folder / 'EXACT_HISTORICAL_RESOLUTION.json')) == 13

def commands(folder, count, exits):
    rows = obj(folder / 'ALL_COMMAND_RECORDS.json')
    assert len(rows) == count
    for entry, wanted in zip(rows,exits):
        directory, tag, row = Path(entry['folder']),entry['tag'],entry['command']
        assert directory.is_relative_to(folder)
        assert obj(directory / (tag + '.command.json')) == row
        attempt = obj(directory / (tag + '.attempt.json'))
        assert all(attempt[k] == row[k] for k in ('argv','cwd','env','stdout','stderr'))
        assert row['process_outcome'] == 'COMPLETED' and row['exit'] == wanted
        assert row['spawn_error'] is None and row['cleanup'] == []
        expected_env = ENV
        if folder.name == 'review_build_01' and Path(row['cwd']) == folder / 'cold_build':
            expected_env = {**ENV,'SOURCE_DATE_EPOCH':'1788652800','FORCE_SOURCE_DATE':'1','openin_any':'p','openout_any':'p'}
            expected_env.update({key:str(folder / ('never_created_' + key.lower())) for key in ('TEXMFHOME','TEXMFCONFIG','TEXMFVAR')})
        assert row['env'] == expected_env
        for stream in ('stdout','stderr'):
            checkpin(directory / row[stream], row[stream + '_info'])
        samples = obj(directory / (tag + '.maps.json'))
        observed = sorted({p for sample in samples['samples'] for p in sample['mapped_files']})
        assert observed == entry['mapped_files']
    return len(rows)

modes = []
for mode, count, runtime_count, command_count in [('pair',5160,3133,85),('build',120360,4598,125)]:
    folder = B / ('review_' + mode + '_01')
    receipt = obj(folder / 'RECEIPT.json')
    assert receipt['status'] == 'PASS_REVIEW_B_' + mode.upper() and not receipt['failures']
    metadata_map(folder,'ALL_INPUTS_INCLUDING_CAPSULES_BEFORE.json','ALL_INPUTS_AFTER.json',count)
    assert receipt['known_all_inputs_including_capsules'] == count
    metadata_map(folder,'RUNTIME_BEFORE.json','RUNTIME_AFTER.json',runtime_count)
    cfg = obj(folder / 'CONFIGURATION_BEFORE.json')
    assert cfg == obj(folder / 'CONFIGURATION_AFTER.json')
    for path, item in cfg['optional'].items():
        p = Path(path)
        assert p.exists() == item['exists'] and p.is_file() == item['is_file']
        assert str(p.resolve()) == item['resolved']
        if p.is_file():
            checkpin(p,{k:item[k] for k in ('sha256','bytes')})
    for path, names in cfg['directories'].items():
        p = Path(path)
        assert (sorted(str(q) for q in p.rglob('*') if q.is_file()) if p.is_dir() else None) == names
    for phase in ('BEFORE','AFTER'):
        obs = obj(folder / ('PARENT_' + phase + '.json'))
        assert obs['env'] == ENV and obs['cwd'] == str(ROOT)
        assert obs['optimization'] == 0 and not obs['cache_exists']
        assert obs['pycache_prefix'] == str(folder / 'never_created_parent_cache')
    closed = obj(folder / 'OBSERVED_CLOSURE.json')
    assert not closed['uncovered'] and not closed['bytecode']
    commands(folder,command_count,[0]*command_count)
    if mode == 'pair':
        assert receipt['result']['canonical_adopted'] is True
        for name in ('replay_01','replay_02'):
            capsule = folder / name
            child = obj(capsule / 'RECEIPT.json')
            assert child['status'] == 'PASS' and child['checks'] == 54794 and child['total_states'] == 3414
            assert child['source_only_initial_names'] == ['bootstrap.py','verify.py']
            for source in child['source_only_initial_names']:
                assert h(B / source) == h(capsule / 'source_inputs' / source)
            for phase in ('before','after'):
                obs = obj(capsule / ('child.' + phase + '.json'))
                assert obs['env'] == ENV and obs['cwd'] == str(capsule)
                assert obs['optimize'] == 0 and obs['isolated'] == obs['no_site'] == 1
                assert obs['dont_write_bytecode'] and not obs['cache_exists']
                assert obs['pycache_prefix'] == str(capsule / 'never_created_child_cache')
    else:
        assert receipt['result']['pages'] == 4 and receipt['result']['embedded_fonts'] == 20
        assert not any(receipt['result']['diagnostics'].values())
        tex = obj(folder / 'TEX_RESOURCES_BEFORE.json')
        assert tex == obj(folder / 'TEX_RESOURCES_AFTER.json') and len(tex['files']) == 113733
        assert {str(p) for root in tex['roots'] if Path(root).is_dir() for p in Path(root).rglob('*') if p.is_file()} == set(tex['files'])
        for path, exists in tex['roots'].items():
            assert Path(path).exists() == exists
        sources = obj(folder / 'SOURCE_ONLY_INITIAL.json')
        assert len(sources) == 8
        for path,value in sources.items():
            checkpin(path,value)
            checkpin(R1 / Path(path).relative_to(folder / 'cold_build'),{k:value[k] for k in ('sha256','bytes')})
        consumed = obj(folder / 'CONSUMED_TEX.json')
        assert len(consumed) == 131
        for path,value in consumed.items():
            checkpin(path,value)
        for phase in ('BEFORE','AFTER'):
            assert all(not item['exists'] and not Path(item['path']).exists() for item in obj(folder / ('USER_ROOTS_' + phase + '.json')).values())
    launcher = B / ('launcher_review_' + mode + '_01')
    launch = obj(launcher / 'RECEIPT.json')
    assert launch['status'] == 'PASS_LAUNCH' and launch['exit'] == 0 and launch['inputs_unchanged'] and launch['cache_absent']
    metadata_map(launcher,'INPUTS_BEFORE.json','INPUTS_AFTER.json',7)
    for stream in ('recorder.stdout','recorder.stderr'):
        checkpin(launcher / stream,launch[stream + '_pin'])
    modes.append({'mode':mode,'known_inputs':count,'runtime_files':runtime_count,'commands':command_count})

for name,count,exits in [('auxiliary_01',5168,[0,0,0,0]),('artifact_audit_01',5169,[1]),
                       ('artifact_audit_02',5169,[1]),('artifact_audit_03',5169,[0,0])]:
    folder = B / name
    before = metadata_map(folder,'INPUTS_BEFORE.json','INPUTS_AFTER.json',count)
    receipt = obj(folder / 'RECEIPT.json')
    assert receipt['inputs_unchanged'] and receipt['inputs'] == len(before)
    assert receipt['status'] == ('PASS' if all(x == 0 for x in exits) else 'FAIL_PRESERVED')
    commands(folder,len(exits),exits)
reconciled = obj(B / 'auxiliary_01/reconcile.stdout')
assert reconciled['status'] == 'PASS_FULL_MATHEMATICAL_PAYLOAD_RECONCILIATION'
assert reconciled['checks'] == 78548 and reconciled['row_count'] == 3414
assert len(reconciled['rows']) == 3414 and all(row['status'] == 'ALL_EQUAL' for row in reconciled['rows'])
findings = obj(B / 'FINDINGS.json')
assert findings['findings'] == [] and not any(findings['current_open_counts'].values())
assert findings['delta_status'] == 'UNASSESSED' and len(findings['resolved_audit_events']) == 2
assert '**UNASSESSED' in (B / 'DELTA.md').read_text()
assert h(B / 'verify.py') == 'd5fd105ddfc162323f06cd530fbd696b0093643a7a0c24c64747cd9c9be30467'
assert h(B / 'CANONICAL.json') == '612e1463162deba868cf7cf81d61c8f017713f9b28c4c38b81b00d376bac992c'
pairs = [(B/'review_pair_01/replay_01/producer.stdout',B/'review_pair_01/replay_02/producer.stdout')]
pairs += [(B/('review_pair_01/'+s+'/producer.stdout'),B/'CANONICAL.json') for s in ('replay_01','replay_02')]
pairs += [(B/'auxiliary_01'/s,B/'auxiliary_01'/t) for s,t in [('author_projection.json','B_to_author_projection.json'),('A_projection.json','B_to_A_projection.json')]]
pairs.append((B/'review_build_01/cold_build/main.pdf',R1/'main.pdf'))
pairs += [(B/('review_build_01/cold_build/pages/page-'+str(i)+'.png'),R1/('author_build_01/cold_build/pages/page-'+str(i)+'.png')) for i in range(1,5)]
comparisons = []
for left,right in pairs:
    argv = ['/usr/bin/cmp','--',str(left),str(right)]
    process = subprocess.run(argv,cwd=ROOT,env=ENV,capture_output=True)
    comparisons.append({'argv':argv,'exit':process.returncode,'stdout':process.stdout.decode(),'stderr':process.stderr.decode()})
    assert process.returncode == 0
for path in list(D['READS']):
    pin(path,fresh=True)
assert manifest(B/'SHA256SUMS',complete=True) == outer
print(json.dumps({'status':'PASS_ROOT_B_INITIAL_COMPLETE_ORIGINAL_CLOSURE','seal_sha256':SEAL,
    'review_payloads':len(outer),'round1_payloads':len(frozen),'frozen_input_pins':len(inputs),
    'complete_nested_manifests':len(preseal['nested_seals']),'full_documentary_inputs':len(doc),
    'all_current_read_paths_checked_twice':len(D['READS']),'modes':modes,
    'preserved_failed_audits':2,'full_reconciliation_rows':3414,'reconciliation_checks':78548,
    'actual_root_raw_comparisons':comparisons,
    'actual_resolved_historical_aliases':[{'original_path':key[0],'sha256':key[1],'physical_path':value} for key,value in sorted(resolved.items())],
    'current_open_findings':0,'delta_status':'UNASSESSED',
    'boundary':'Root archive/current-dependency inspection and raw comparisons; not a new mathematical producer, build, render or page view. New strict root B pair and exact delta still required.'},indent=2,sort_keys=True))
