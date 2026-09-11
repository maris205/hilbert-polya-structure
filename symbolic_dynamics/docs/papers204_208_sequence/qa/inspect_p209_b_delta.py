"""Root final B original/delta closure; no scientific or build execution.

The main process separately inspects the original review and actual delta,
including failed/corrected infrastructure. This checks their complete bytes,
dependency roles and actual commands, then emits measured acceptance data.
The expected final seal and count are supplied only after reviewer sealing.
"""
import ast
import json
import os
from pathlib import Path
import re
import runpy
import subprocess
import sys

R = Path('/root/autodl-tmp/symbolic_dynamics')
Q = R / 'docs/papers204_208_sequence/qa'
B = Q.parent / 'reviews/p209_b'
P = R / 'papers/209-ordered-fibre-threading'
F = P / 'frozen_round1'
PREP = Q / 'p209_b_root_preparation'
PAIR = Q / 'root_replays/p209_b_strict/root_b_pair_01'
LAUNCH = PAIR.parent / 'launcher_root_b_pair_01'
D = runpy.run_path(str(Q / 'inspect_p209_a_initial.py'))
pin, obj, manifest = (D[n] for n in ('pin','obj','manifest'))
ENV = D['ENV']
INITIAL = 'd88b831e60414d47ae0b2afb2583b73d02fc9764877a00952f4a9d90d13488ea'
OLD_DELTA = '282dc2ab3f0021abeca145c20b76d0e0ef10e0b0e9948a173a24e6ead05b1400'
RESPONSE = 'c2cab3d26ddd9f5e5ba7e31dc0f3afa1c8d06510fd1276294cae33c63cdbc1f8'
ALIASES, USED = {}, {}


def h(p):
    return pin(p)['sha256']


def prior_result(name):
    raw = obj(Q / name)
    if 'parsed_stdout' in raw:
        assert raw['actual_completion']['exit_code'] == 0
        return raw['parsed_stdout']
    assert raw['completion']['exit_code'] == 0
    return json.loads(raw['completion']['output'])


def alias(origin, value, physical):
    assert h(physical) == value
    ALIASES.setdefault((str(origin), value), str(physical))


def resolve(origin, expected):
    origin = str(origin)
    value = expected if isinstance(expected, str) else expected['sha256']
    target = ALIASES.get((origin, value), origin)
    actual = pin(target)
    assert actual['sha256'] == value, (origin, value, target)
    if not isinstance(expected, str):
        assert 'error' not in expected and actual['bytes'] == expected['bytes']
        if target == origin:
            assert set(expected) <= set(actual) and all(actual[k] == v for k,v in expected.items())
    if target != origin:
        USED[(origin, value)] = target
    return target


def maps(folder, before, after, expected_count):
    a = obj(folder / before)
    assert a == obj(folder / after) and len(a) == expected_count
    for origin, expected in a.items():
        resolve(origin, expected)
    return a


def command(folder, tag, expected_exit, expected_env=ENV):
    row = obj(folder / (tag + '.command.json'))
    attempt = obj(folder / (tag + '.attempt.json'))
    assert all(attempt[k] == row[k] for k in ('argv','cwd','env','stdout','stderr'))
    assert row['env'] == expected_env and row['exit'] == expected_exit
    assert row['process_outcome'] == 'COMPLETED' and row['spawn_error'] is None
    assert row['cleanup'] == [] and row['start_new_session'] is True
    assert row['started_epoch'] <= row['finished_epoch']
    for stream in ('stdout','stderr'):
        resolve(folder / row[stream], row[stream + '_info'])
    samples = obj(folder / (tag + '.maps.json'))
    observed = sorted({p for sample in samples['samples'] for p in sample['mapped_files']})
    for sample in samples['samples']:
        paths = sorted({str(Path(line.split(None,5)[5]).resolve())
                        for line in sample['maps'].splitlines()
                        if len(line.split(None,5)) == 6 and line.split(None,5)[5].startswith('/')})
        assert paths == sample['mapped_files']
    for p in observed:
        pin(p)
    return row, observed


def command_list(folder, filename, exits):
    rows = obj(folder / filename)
    assert len(rows) == len(exits)
    for entry, wanted in zip(rows, exits):
        where, tag = Path(entry['folder']), entry['tag']
        assert where.is_relative_to(folder)
        row, observed = command(where, tag, wanted)
        assert entry['command'] == row and entry['mapped_files'] == observed
    return rows


def settings(folder, attempt):
    assert attempt['env'] == ENV and attempt['cwd'] == str(R)
    assert attempt['executable'] == '/usr/bin/python3.10'
    assert not attempt['cache_exists'] and not Path(attempt['pycache_prefix']).exists()
    assert attempt['pycache_prefix'] == str(folder / 'never_created_parent_cache')
    assert all(t in attempt['flags'] for t in ('isolated=1','no_site=1','dont_write_bytecode=1','optimize=0'))
    for p in attempt['mapped_files']:
        pin(p)
    for row in attempt['modules'].values():
        for key in ('file','origin'):
            p = row.get(key)
            if p and Path(p).is_file():
                pin(p)


def configuration(folder):
    old = obj(folder / 'CONFIGURATION_BEFORE.json')
    assert old == obj(folder / 'CONFIGURATION_AFTER.json')
    for p, v in old['optional'].items():
        path = Path(p)
        assert path.exists() == v['exists'] and path.is_file() == v['is_file']
        assert str(path.resolve()) == v['resolved']
        if path.is_file():
            resolve(path, {k:v[k] for k in ('sha256','bytes')})
    for p, names in old['directories'].items():
        path = Path(p)
        assert (sorted(str(x) for x in path.rglob('*') if x.is_file()) if path.is_dir() else None) == names
    return old


def runtime_inventory(folder):
    old = obj(folder / 'RUNTIME_BEFORE.json')
    assert old == obj(folder / 'RUNTIME_AFTER.json')
    stdroot = Path('/usr/lib/python3.10')
    std = set()
    for base, dirs, names in os.walk(stdroot):
        dirs[:] = [n for n in dirs if n not in {'site-packages','dist-packages','__pycache__'}]
        std.update(str(Path(base)/n) for n in names if not n.endswith(('.pyc','.pyo')))
    assert std == {p for p in old if Path(p).is_relative_to(stdroot)}
    libs = set()
    for root in map(Path, ('/usr/lib/x86_64-linux-gnu','/usr/lib64','/usr/local/lib')):
        if root.is_dir():
            it = root.glob('*') if str(root) == '/usr/local/lib' else root.rglob('*')
            libs.update(str(p) for p in it if p.is_file() and (p.name.endswith('.so') or '.so.' in p.name))
    prior_libs = {p for p in old if (Path(p).name.endswith('.so') or '.so.' in Path(p).name)
                  and (Path(p).is_relative_to('/usr/lib/x86_64-linux-gnu')
                       or Path(p).is_relative_to('/usr/lib64') or Path(p).parent == Path('/usr/local/lib'))}
    assert libs == prior_libs
    for p, row in old.items():
        resolve(p, row)
    return {'runtime_paths':len(old),'stdlib_inventory':len(std),'potential_libraries':len(libs)}


def main():
    expected_seal, expected_count = sys.argv[1:]
    assert re.fullmatch('[0-9a-f]{64}', expected_seal) and expected_seal != INITIAL
    expected_count = int(expected_count)
    pin(__file__); pin(Q / 'inspect_p209_a_initial.py')
    assert h(B/'SHA256SUMS') == expected_seal
    outer = manifest(B/'SHA256SUMS', complete=True)
    assert len(outer) == expected_count
    preseal = obj(B/'PRESEAL_DELTA.json')
    assert preseal['status'] == 'PASS_ACCEPTED_DELTA_PRESEAL'
    assert preseal['delta_status'] == 'ACCEPTED_EXACT_NOCHANGE_DELTA'
    assert preseal['delta_consumed_paths_rehashed_twice'] == 128227
    assert preseal['wrapper_inputs_rehashed_twice'] == 5166
    assert preseal['full_delta_map_sha256'] == h(B/'delta_check_02/INPUTS_FULL_BEFORE.json')
    assert set(preseal['payload_inputs_before_and_rechecked_after']) == set(outer) - {'PRESEAL_DELTA.json'}
    for name, row in preseal['payload_inputs_before_and_rechecked_after'].items():
        assert pin(B/name) == row
    assert len(preseal['nested_seals']) == 13
    for name, row in preseal['nested_seals'].items():
        assert h(B/name/'SHA256SUMS') == row['sha256']
        assert len(manifest(B/name/'SHA256SUMS',complete=True)) == row['payloads']
    executed = obj(B/'DELTA_CHECK_EXECUTION.actual.json')
    assert executed['actual_exit_code'] == 0 and executed['actual_working_directory'] == str(R)
    actual_outer = json.loads(executed['actual_output'])
    assert actual_outer['status'] == 'PASS' and actual_outer['failure'] is None
    assert actual_outer['seal']['sha256'] == h(B/'delta_check_02/SHA256SUMS')
    assert actual_outer['seal']['payloads'] == 64
    inner = []
    for path in sorted(B.rglob('SHA256SUMS')):
        if path != B/'SHA256SUMS':
            inner.append({'path':str(path),'payloads':len(manifest(path,complete=True)),'sha256':h(path)})
    assert h(B/'INITIAL_REVIEW_SEAL.sha256') == INITIAL and h(B/'INITIAL_DELTA.md') == OLD_DELTA
    initial = {}
    for line in (B/'INITIAL_REVIEW_SEAL.sha256').read_text().splitlines():
        value, name = line.split('  ',1)
        assert re.fullmatch('[0-9a-f]{64}',value) and name not in initial
        assert not Path(name).is_absolute() and '..' not in Path(name).parts
        physical = 'INITIAL_DELTA.md' if name == 'DELTA.md' else name
        assert h(B/physical) == value == outer[physical]
        initial[name] = value
    assert len(initial) == 1298
    assert h(B/'REPORT.md') == '089f10c004f933f17db0a701e161b5d19edb3c74f9c3896348fad5711f109f12'
    assert h(B/'FINDINGS.json') == '395340caae7a758f1791b71f684c8c11fb82ccbfa383d98c83141b9e8cf74e17'
    old_root = prior_result('P209_B_ROOT_INITIAL_INSPECTION.actual.json')
    assert old_root['status'] == 'PASS_ROOT_B_INITIAL_COMPLETE_ORIGINAL_CLOSURE'
    assert old_root['review_payloads'] == 1298 and old_root['full_documentary_inputs'] == 127544
    old_aliases = obj(B/'artifact_audit_03/EXACT_HISTORICAL_RESOLUTION.json')
    assert old_aliases == {v['original_path']+' @ '+v['sha256']:v['physical_path'] for v in old_root['actual_resolved_historical_aliases']}
    for key, target in old_aliases.items():
        origin, value = key.rsplit(' @ ',1); alias(origin,value,target)
    alias(B/'SHA256SUMS',INITIAL,B/'INITIAL_REVIEW_SEAL.sha256')
    alias(B/'DELTA.md',OLD_DELTA,B/'INITIAL_DELTA.md')
    intake = obj(B/'delta_intake_01/INTAKE_RESULT.json')
    assert intake['status'] == 'PASS_EXACT_INITIAL_PRESERVATION_AND_INTAKE'
    assert not intake['acceptance_performed'] and len(intake['copies']) == 15
    for row in intake['copies']:
        alias(row['original'],row['sha256'],row['physical'])
        assert pin(row['physical'])['bytes'] == row['bytes']
    for foldername, count in [('delta_check_01',128155),('delta_check_02',128227)]:
        folder = B/foldername
        for name in ('PAPER_MANIFEST.sha256','ROOT_ADOPTION.md','PAPER_STATUS.md'):
            alias(P/name,h(folder/'response_anchors'/name),folder/'response_anchors'/name)
        declared = obj(folder/'EXACT_HISTORY_ALIASES.json')
        # Each attempt has its own exact same-byte response anchor paths.
        expected = {o+' @ '+v:t for (o,v),t in ALIASES.items()}
        for name in ('PAPER_MANIFEST.sha256','ROOT_ADOPTION.md','PAPER_STATUS.md'):
            expected[str(P/name)+' @ '+h(folder/'response_anchors'/name)] = str(folder/'response_anchors'/name)
        assert declared == expected and len(declared) == 32
        for key, target in declared.items():
            origin,value = key.rsplit(' @ ',1); assert h(target) == value
        maps(folder,'INPUTS_FULL_BEFORE.json','INPUTS_FULL_AFTER.json',count)
        maps(folder,'INPUTS_BEFORE.json','INPUTS_AFTER.json',5166)
        settings(folder,obj(folder/'ATTEMPT.json'))
        rows = command_list(folder,'ALL_COMMAND_RECORDS.json',[0]*8)
        assert all(e['command']['argv'][:2] == ['/usr/bin/cmp','--'] for e in rows)
        child, observed = command(folder,'documentary_child',0)
        assert child['cwd'] == str(folder)
        assert child['argv'] == ['/usr/bin/python3.10','-I','-S','-B','-X',
            'pycache_prefix='+str(folder/'never_created_child_cache'),
            str(B/('check_delta.py' if foldername.endswith('01') else 'check_delta_v2.py')),str(folder)]
        assert not (folder/'never_created_child_cache').exists()
        result = obj(folder/'DELTA_EVIDENCE_RESULT.json')
        assert obj(folder/'documentary_child.stdout') == result
        assert result['status'] == 'PASS_EXACT_NOCHANGE_DELTA_EVIDENCE'
        assert result['delta_full_input_paths'] == count and result['all_inputs_unchanged']
        assert result['counts']['all_original_documentary_pins_retained'] == 127544
        assert result['accepted_decision_not_written_by_checker'] is True
        assert result['actual_raw_comparisons'] == 8 and result['used_aliases'] == 8
        assert result['new_delta_mathematical_producers'] == result['new_delta_builds_renders_views'] == 0
        assert obj(folder/'CONFIGURATION_BEFORE.json') == obj(folder/'CONFIGURATION_AFTER.json')
        if foldername.endswith('01'):
            failed = obj(folder/'OUTER_FAILURE.actual.json')
            closure = obj(folder/'CLOSURE_AFTER_FAILURE.json')
            assert failed['actual_exit_code'] == 1 and 'FileExistsError' in failed['actual_output']
            assert 'ALL_COMMAND_RECORDS.json' in failed['actual_output']
            assert closure['actual_outer_exit'] == 1 and closure['actual_child_exit'] == 0
            assert not (folder/'RECEIPT.json').exists()
        else:
            wrapper = command_list(folder,'WRAPPER_COMMAND_RECORDS.json',[0])
            assert wrapper[0]['command'] == child and wrapper[0]['mapped_files'] == observed
            receipt = obj(folder/'RECEIPT.json')
            assert receipt['status'] == 'PASS' and receipt['failure'] is None
            assert receipt['inputs_unchanged'] and receipt['inputs'] == 5166
    original_dependencies = maps(B/'artifact_audit_03','DOCUMENTARY_INPUTS_BEFORE.json','DOCUMENTARY_INPUTS_AFTER.json',127544)
    maps(B/'delta_intake_01','INPUTS_BEFORE.json','INPUTS_AFTER.json',5166)
    settings(B/'delta_intake_01',obj(B/'delta_intake_01/ATTEMPT.json'))
    command_list(B/'delta_intake_01','ALL_COMMAND_RECORDS.json',[0])
    frozen = manifest(F/'SHA256SUMS',complete=True)
    assert len(frozen) == 2003 and h(F/'SHA256SUMS') == 'c93e16cf20d2eb87f3b454fbdb3576e52c6c79fb74c8712a277efeab7e60ce57'
    author = manifest(P/'AUTHOR_MANIFEST.sha256')
    assert len(author) == 1985 and author == manifest(F/'AUTHOR_MANIFEST.sha256')
    assert len(manifest(P/'PAPER_MANIFEST.sha256',complete=True)) == 5982
    assert len(manifest(B/'INPUT_PINS.sha256',base=R)) == 2004
    assert len(manifest(PREP/'SHA256SUMS',complete=True)) == 57
    assert len(manifest(PAIR/'SHA256SUMS',complete=True)) == 462
    assert len(manifest(LAUNCH/'SHA256SUMS',complete=True)) == 10
    root = prior_result('P209_B_ROOT_PAIR_INSPECTION.actual.json')
    assert root['status'] == 'PASS_ROOT_NEW_B_PAIR_FULL_CLOSURE'
    assert root['checks_each'] == 54794 and root['known_pair_inputs'] == 5164
    maps(PAIR,'ALL_INPUTS_INCLUDING_CAPSULES_BEFORE.json','ALL_INPUTS_AFTER.json',5164)
    maps(LAUNCH,'INPUTS_BEFORE.json','INPUTS_AFTER.json',2026)
    command_list(PAIR,'ALL_COMMAND_RECORDS.json',[0]*85)
    runtimes = []
    for folder in (B/'review_pair_01',B/'review_build_01',PAIR):
        configuration(folder)
        runtimes.append({'folder':str(folder),**runtime_inventory(folder)})
    tex = obj(B/'review_build_01/TEX_RESOURCES_BEFORE.json')
    assert tex == obj(B/'review_build_01/TEX_RESOURCES_AFTER.json') and len(tex['files']) == 113733
    assert all(Path(p).exists() == v for p,v in tex['roots'].items())
    assert {str(p) for root in tex['roots'] if Path(root).is_dir() for p in Path(root).rglob('*') if p.is_file()} == set(tex['files'])
    for p,v in tex['files'].items(): resolve(p,v)
    current = obj(B/'CURRENT_FINDINGS.json')
    assert current['schema'] == 'p209-manuscript-review-findings-v1'
    assert current['reviewer'] == '/root/p209_b_reviewer' and current['input_round'] == 1
    assert current['delta_status'] == 'ACCEPTED_EXACT_NOCHANGE_DELTA'
    assert current['current_open_counts'] == {'critical':0,'major':0,'minor':0} and current['findings'] == []
    assert current['scientific_inputs_changed'] is False
    assert current['response_sha256'] == h(Q.parent/'P209_B_RESPONSE.md') == RESPONSE
    assert current['initial_complete_manifest_sha256'] == INITIAL
    assert current['initial_complete_manifest_role'] == 'INITIAL_REVIEW_SEAL.sha256'
    assert obj(B/'FINDINGS.json')['delta_status'] == 'UNASSESSED'
    assert '**ACCEPTED_EXACT_NOCHANGE_DELTA.' in (B/'DELTA.md').read_text()
    comparisons = []
    for a,b in [(PAIR/'replay_01/producer.stdout',PAIR/'replay_02/producer.stdout'),
                (PAIR/'replay_01/producer.stdout',B/'CANONICAL.json'),
                (PAIR/'replay_02/producer.stdout',B/'CANONICAL.json'),
                (P/'main.pdf',F/'main.pdf'),(P/'AUTHOR_MANIFEST.sha256',F/'AUTHOR_MANIFEST.sha256')]:
        argv = ['/usr/bin/cmp','--',str(a),str(b)]
        proc = subprocess.run(argv,cwd=R,env=ENV,capture_output=True)
        comparisons.append({'argv':argv,'exit':proc.returncode,'stdout':proc.stdout.decode(),'stderr':proc.stderr.decode()})
        assert proc.returncode == 0
    source_diffs = []
    original_diff = (B/'DELTA_ADAPTATION.diff').read_text()
    parts = re.split(r'(?m)(?=^--- )',original_diff)
    parts = [part for part in parts if part]
    assert len(parts) == 2
    for old,new,expected in zip(('check_delta.py','launch_delta.py'),
                               ('check_delta_v2.py','launch_delta_v2.py'),parts):
        a,b = (B/old).read_text(),(B/new).read_text()
        fa = {n.name:n for n in ast.parse(a).body if isinstance(n,ast.FunctionDef)}
        fb = {n.name:n for n in ast.parse(b).body if isinstance(n,ast.FunctionDef)}
        assert fa.keys() == fb.keys()
        assert {n for n in fa if ast.dump(fa[n]) != ast.dump(fb[n])} == {'main'}
        labels = expected.splitlines()[:2]
        argv = ['/usr/bin/diff','-u','--label',labels[0][4:],'--label',labels[1][4:],str(B/old),str(B/new)]
        proc = subprocess.run(argv,cwd=R,env=ENV,capture_output=True)
        source_diffs.append({'argv':argv,'exit':proc.returncode,'stdout':proc.stdout.decode(),'stderr':proc.stderr.decode(),
            'label_scope':'Explicit archived header labels, not newly observed timestamps; full generated diff bytes compared to original stored portion.'})
        assert proc.returncode == 1 and proc.stderr == b'' and proc.stdout == expected.encode()
    gate_aliases = [
        {'original_path':str(Q.parent/'GIT_SYNC_RECEIPT.md'),
         'sha256':'2f6998d2986831fa8776e31e9d336497e6ab37b114d1b13ef94879f3e2271c24',
         'physical_path':str(Q/'central_lifecycle_p209_round1/GIT_SYNC_RECEIPT.before.md')},
        {'original_path':str(B/'SHA256SUMS'),'sha256':INITIAL,'physical_path':str(B/'INITIAL_REVIEW_SEAL.sha256')},
        {'original_path':str(B/'DELTA.md'),'sha256':OLD_DELTA,'physical_path':str(B/'INITIAL_DELTA.md')}]
    for row in gate_aliases:
        assert h(row['original_path']) != row['sha256'] == h(row['physical_path'])
    for p in list(D['READS']): pin(p,fresh=True)
    assert manifest(B/'SHA256SUMS',complete=True) == outer
    print(json.dumps({'schema':'p209-b-root-delta-closure-v1',
        'status':'ROOT_ACCEPTED_B_DELTA_ORIGINAL_CLOSURE_PASS','paper':'P209','input_round':1,'round1_path':str(F),
        'reviewer_delta_accepted':True,'root_original_inspection_complete':True,'root_replay_closure_complete':True,
        'current_open_findings':0,'unchanged_author_payloads':len(author),'unchanged_round1_payloads':len(frozen),
        'author_manifest_sha256':h(P/'AUTHOR_MANIFEST.sha256'),'round1_manifest_sha256':h(F/'SHA256SUMS'),
        'review_manifest_sha256':expected_seal,'review_manifest_entries':len(outer),'delta_sha256':h(B/'DELTA.md'),
        'initial_findings_sha256':h(B/'FINDINGS.json'),'current_findings_sha256':h(B/'CURRENT_FINDINGS.json'),
        'response_sha256':RESPONSE,'root_pair_manifest_sha256':h(PAIR/'SHA256SUMS'),
        'root_launcher_manifest_sha256':h(LAUNCH/'SHA256SUMS'),'historical_input_aliases':gate_aliases,
        'historical_alias_field_scope':'Only actually drifted roles required by the Round1-to-Round2 source/initial-B closure; all other documented roles were also checked separately.',
        'initial_payloads_preserved':1298,'initial_same_path_payloads':1297,'initial_delta_exact_aliases':1,
        'complete_nested_manifests':inner,'original_documentary_dependencies':len(original_dependencies),
        'successful_delta_full_input_paths':128227,'failed_delta_full_input_paths':128155,
        'all_current_read_paths_checked_twice':len(D['READS']),'rechecked_runtime_inventories':runtimes,
        'preserved_outer_failure_exit':1,'successful_outer_exit':0,'actual_root_raw_comparisons':comparisons,
        'actual_root_source_differences':source_diffs,
        'inspection_script_sha256':h(__file__),
        'scope':'Full original/current-dependency closure and actual raw comparisons. Prior successful root B mathematical pair is explicitly reused with unchanged complete scientific/runtime/build keys. No new science/build/render/view, physical Round2 or terminal completion in this command.'},indent=2,sort_keys=True))


if __name__ == '__main__':
    main()
