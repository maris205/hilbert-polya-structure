"""Root read-only complete P209 Round2 physical/provenance closure.

No freezer main, science, build or render is executed. All historical rows
retain their original bases. V2 corrects only the unsupported expectation
that two live central indexes were consumed: the complete actual 9996-path
freezer map consumes neither live index, and all its keys remain unchanged.
The real V1 failure and original code remain preserved.
"""
from hashlib import sha256
import json
from pathlib import Path
import re
import runpy
import subprocess
from urllib.parse import unquote

R = Path('/root/autodl-tmp/symbolic_dynamics')
Q = R/'docs/papers204_208_sequence/qa'
P = R/'papers/209-ordered-fibre-threading'
T = P/'frozen_round2'
D = runpy.run_path(str(Q/'inspect_p209_a_initial.py'))
pin,obj,manifest = (D[n] for n in ('pin','obj','manifest'))
pin(__file__)
prep = Q/'p209_round2_preparation'
assert pin(prep/'SHA256SUMS')['sha256'] == '84fc65f40ca65ed4ec555cd398860e314fe2195bc7f88766d3fbde70a4bb458d'
assert len(manifest(prep/'SHA256SUMS',complete=True)) == 13
F = runpy.run_path(str(prep/'freeze_p209_round2.py'),run_name='root_definitions_not_freezer_main')
core = manifest(P/'frozen_round1/SHA256SUMS',complete=True)
older = manifest(P/'frozen_round0/SHA256SUMS',complete=True)
author = manifest(P/'AUTHOR_MANIFEST.sha256')
seal = manifest(T/'SHA256SUMS',complete=True)
assert (len(core),len(older),len(author),len(seal)) == (2003,1989,1985,2021)
assert all(core[n] == seal[n] == h for n,h in older.items())
assert all(core[n] == seal[n] == h for n,h in author.items())
assert manifest(T/'AUTHOR_MANIFEST.sha256') == author
assert pin(P/'AUTHOR_MANIFEST.sha256')['sha256'] == F['AUTHOR_SEAL']
assert pin(P/'frozen_round1/SHA256SUMS')['sha256'] == F['ROUND1_SEAL']
assert pin(T/'SHA256SUMS')['sha256'] == 'ac2a6d8fa6c659dab943940ffb7d887fd8781ca07526172370e60d5fea4f5b8d'
accepted,external,counts,initial = F['accepted_b'](core)
v = obj(T/'ROUND2_PROVENANCE.json')
assert v['schema'] == 'p209-round2-provenance-v1'
assert v['core_payload_pins'] == core and v['accepted_root_assertions'] == accepted
assert v['accepted_evidence_counts'] == counts
assert v['accepted_review_and_root_manifest_referents'] == external
assert v['author_payloads_preserved'] == 1985 and v['round1_core_payloads_copied'] == 2003
assert v['historical_round0_round1_metadata_and_adapters_unchanged'] is True
assert v['environment'] == D['ENV'] and v['cwd'] == str(R)
assert v['launch_argv'] == [str(prep/'freeze_p209_round2.py'),'freeze-round2-after-accepted-b']
assert v['launch_orig_argv'] == ['/usr/bin/python3.10','-I','-S','-B','-X',
    'pycache_prefix='+str(T/'never_created_freezer_cache'),*v['launch_argv']]
assert not (T/'never_created_freezer_cache').exists()
assert pin(T/'ROUND2_FREEZE_ADAPTER.py')['sha256'] == v['freezer_sha256'] == pin(prep/'freeze_p209_round2.py')['sha256']
assert v['original_round1_freezer_sha256'] == pin(T/'ROUND1_FREEZE_ADAPTER.py')['sha256'] == F['R1_FREEZER']

anchors = v['anchor_mapping']
assert set(anchors) == set(F['ANCHORS']) and len(anchors) == 15
for name,row in anchors.items():
    assert row == {'original_path':str(F['ANCHORS'][name]),'physical_path':'ROUND2_ACCEPTANCE/'+name,
                   'sha256':pin(T/'ROUND2_ACCEPTANCE'/name)['sha256']}
    assert pin(row['original_path'])['sha256'] == row['sha256']
whole = v['prior_whole_paper_manifest']
assert whole['original_referent_base'] == str(P) and whole['payloads'] == 5982
assert whole['physical_path'] == str(T/whole['physical_relative_path'])
assert whole['sha256'] == F['PRIOR_WHOLE_SEAL'] == pin(whole['physical_path'])['sha256']
assert manifest(Path(whole['physical_path']),base=P) == whole['original_referent_pins']
assert whole['complete_current_paper_after_round2'] is False
assert whole['exact_whole_tree_checked_before_creation'] is True
assert whole['original_referents_and_manifest_bytes_rechecked_after_creation'] is True
outside = {p.relative_to(P).as_posix() for p in P.rglob('*') if p.is_file() and not p.is_relative_to(T)}
assert outside == set(whole['original_referent_pins']) | {'PAPER_MANIFEST.sha256'}

prior = obj(P/'frozen_round1/ROUND1_PROVENANCE.json')
required = {}
def need(origin,value,role):
    required.setdefault((str(origin),value),set()).add(role)
for role in ('all_source_inputs_before_and_rechecked_after','accepted_review_and_root_manifest_referents'):
    for origin,value in prior[role].items():need(origin,value,'round1:'+role)
for row in prior['anchor_mapping'].values():need(row['original_path'],row['sha256'],'round1:physical-acceptance-anchor')
for row in prior['historical_external_resolution'].values():need(row['original_path'],row['sha256'],'round1:historical-external')
for role in ('round1_core_link_map','acceptance_and_historical_anchor_link_map'):
    for row in prior[role]:need(row['physical_target'],row['sha256'],'round1:'+role)
for origin,value in obj(T/'FROZEN_LINK_MAP.json')['external_input_pins'].items():need(origin,value,'round0:historical-external')
for name,value in initial.items():need(F['REVIEW']/name,value,'B:immutable-initial-payload')
need(F['REVIEW']/'SHA256SUMS',F['B_INITIAL_SEAL'],'B:immutable-initial-complete-seal')
history = v['historical_input_resolution']
assert len(history) == len(required) == 7307
resolved = {}
copies = {}
for row in history:
    key = (row['original_path'],row['sha256'])
    assert key in required and key not in resolved and row['roles'] == sorted(required[key])
    source,target = Path(row['physical_source']),Path(row['round2_physical_path'])
    assert source.is_absolute() and target.is_absolute() and source.resolve() == source and target.resolve() == target
    assert pin(source)['sha256'] == pin(target)['sha256'] == key[1]
    mode = row['mode']
    if source.is_relative_to(P/'frozen_round1'):
        n = source.relative_to(P/'frozen_round1').as_posix()
        assert core[n] == key[1] and target == T/n
        assert mode in ('preserved-round1-core-alias','round1-core-remapped-to-round2')
    elif mode == 'exact-new-acceptance-anchor-alias':
        matching = [n for n,p in F['ANCHORS'].items() if p == source]
        assert len(matching) == 1 and target == T/'ROUND2_ACCEPTANCE'/matching[0]
    elif mode == 'exact-new-historical-alias':
        assert row['copy_relative'] == 'ROUND2_HISTORICAL_ALIASES/001_GIT_SYNC_RECEIPT.md'
        assert source == Q/'central_lifecycle_p209_round1/GIT_SYNC_RECEIPT.before.md'
        assert key == (str(Q.parent/'GIT_SYNC_RECEIPT.md'),'2f6998d2986831fa8776e31e9d336497e6ab37b114d1b13ef94879f3e2271c24')
        assert target == T/row['copy_relative'] and len(manifest(source.parent/'SHA256SUMS',complete=True)) > 0
        copies[row['copy_relative']] = key[1]
    else:
        assert mode == 'unchanged-original' and source == target == Path(key[0])
    if mode != 'exact-new-historical-alias':assert row['copy_relative'] is None
    if mode in ('unchanged-original','round1-core-remapped-to-round2'):
        assert row['current_original_sha256'] == key[1]
    else:assert row['current_original_sha256'] != key[1]
    resolved[key] = row
assert len(copies) == 1
expected = dict(core)
expected.update({'ROUND2_ACCEPTANCE/'+n:row['sha256'] for n,row in anchors.items()})
expected.update(copies)
for n in ('ROUND2_FREEZE_ADAPTER.py','ROUND2_PROVENANCE.json'):expected[n] = pin(T/n)['sha256']
assert seal == expected

hist_links = []
for role in ('round1_core_link_map','acceptance_and_historical_anchor_link_map'):
    for row in prior[role]:
        target = resolved[(row['physical_target'],row['sha256'])]['round2_physical_path']
        hist_links.append({**row,'source_role':role,'round1_physical_target':row['physical_target'],'physical_target':target})
assert v['round2_historical_link_map'] == hist_links and len(hist_links) == 259
_,newlinks = F['link_mapping'](core,prior,history)
assert newlinks == v['acceptance_and_historical_anchor_link_map'] and len(newlinks) == 39
for row in hist_links+newlinks:assert pin(row['physical_target'])['sha256'] == row['sha256']

# Resolve actual before/after input roles, not by accepting arbitrary drift.
aliases = {(str(P/'PAPER_MANIFEST.sha256'),whole['sha256']):Path(whole['physical_path'])}
central = Q/'central_lifecycle_p209_b_delta'
assert len(manifest(central/'SHA256SUMS',complete=True)) == 5
for origin,name in ((R/'SYMBOLIC_DYNAMICS_STATE.md','SYMBOLIC_DYNAMICS_STATE.before.md'),
                    (Q.parent/'PIPELINE_STATE.md','PIPELINE_STATE.before.md')):
    physical = central/name
    aliases[(str(origin),pin(physical)['sha256'])] = physical
used = []
for origin,value in v['all_source_inputs_before_and_rechecked_after'].items():
    if pin(origin)['sha256'] != value:
        physical = aliases[(origin,value)]
        assert pin(physical)['sha256'] == value
        used.append({'original_path':origin,'sha256':value,'physical_path':str(physical)})
for origin,value in external.items():assert pin(origin)['sha256'] == value
for origin,value in list(F['READ_PINS'].items()):assert pin(origin)['sha256'] == value
assert used == [], 'actual freezer input map must have no changed dependencies'

execution = obj(Q/'P209_ROUND2_FREEZE.actual.json')
assert execution['completion']['exit_code'] == 0
actual = json.loads(execution['completion']['output'])
assert actual['status'] == 'PASS_PHYSICAL_P209_ROUND2' and actual['payloads'] == len(seal)
assert actual['manifest_sha256'] == pin(T/'SHA256SUMS')['sha256']
assert actual['raw_comparisons'] == v['raw_comparisons'] and len(actual['raw_comparisons']) == 4
comparisons = []
for row in actual['raw_comparisons']:
    assert row['argv'][:2] == ['/usr/bin/cmp','--'] and row['cwd'] == str(R) and row['environment'] == D['ENV']
    assert row['exit'] == 0 and row['outcome'] == 'COMPLETED' and row['stdout'] == row['stderr'] == ''
    for path in row['argv'][2:]:pin(path)
    proc = subprocess.run(row['argv'],cwd=R,env=D['ENV'],capture_output=True)
    assert proc.returncode == 0 and proc.stdout == proc.stderr == b''
    comparisons.append({'argv':row['argv'],'cwd':str(R),'environment':D['ENV'],'exit':proc.returncode,
                        'stdout':proc.stdout.decode(),'stderr':proc.stderr.decode()})
sources = ('main.tex','math_commands.tex','references.bib','sections/00_abstract.tex',
           'sections/01_setup.tex','sections/02_recurrence.tex','sections/03_inverse.tex','sections/04_scope.tex')
source_pins = {str(P/n):{k:pin(P/n)[k] for k in ('sha256','bytes')} for n in sources}
for n in sources:assert pin(P/n)['sha256'] == pin(T/n)['sha256'] == pin(P/'frozen_round1'/n)['sha256']
ag = obj(Q/'P209_A_ROOT_DELTA_INSPECTION.actual.json')
assert ag['current_open_findings'] == 0
for path in list(D['READS']):pin(path,fresh=True)
print(json.dumps({'schema':'p209-round2-root-physical-closure-v1',
    'status':'PASS_ROOT_ROUND2_COMPLETE_PHYSICAL_CLOSURE','paper':'P209','round':2,'current_open_findings':0,
    'round2_manifest_sha256':pin(T/'SHA256SUMS')['sha256'],'round2_payloads':len(seal),
    'accepted_A_root_gate_sha256':pin(Q/'P209_A_ROOT_DELTA_INSPECTION.actual.json')['sha256'],
    'accepted_B_root_gate_sha256':pin(Q/'P209_B_ROOT_DELTA_INSPECTION.actual.json')['sha256'],
    'source_pins':source_pins,'unchanged_author_payloads':len(author),'unchanged_round1_core_payloads':len(core),
    'acceptance_anchors':len(anchors),'history_path_hash_roles':len(history),'historical_links':len(hist_links),
    'new_anchor_links':len(newlinks),'actual_freezer_input_paths':len(v['all_source_inputs_before_and_rechecked_after']),
    'exact_later_central_aliases':used,'old_whole_manifest_original_base_checked_payloads':5982,
    'all_current_read_paths_checked_twice':len(D['READS']),'actual_new_raw_comparisons':comparisons,
    'boundary':'Physical/documentary original closure. No new mathematics, build, viewing or paper/batch completion. Old source-only runtime evidence is reused only through prior accepted root gates.',
    'external':'OWNER_AMBER / HOLD_EXTERNAL'},indent=2,sort_keys=True))
