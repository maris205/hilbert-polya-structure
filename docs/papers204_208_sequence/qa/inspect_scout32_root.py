"""Root original/doc/data closure of sealed negative Scout32, no map run."""
from hashlib import sha256
import json
from pathlib import Path
import runpy
import subprocess

R=Path('/root/autodl-tmp/symbolic_dynamics')
Q=R/'docs/papers204_208_sequence/qa'
B=R/'docs/papers204_208_sequence/scouting/finite_systems_thirty_second'
D=runpy.run_path(str(Q/'inspect_p209_a_initial.py'))
pin,obj,manifest=(D[n] for n in ('pin','obj','manifest'))
pin(__file__)
assert pin(B/'SHA256SUMS')['sha256']=='9ff941dc2b32672857b8d20fac3d102162f6839511c8ee9f1f1b819b5615c666'
assert len(manifest(B/'SHA256SUMS',complete=True))==153
F=runpy.run_path(str(B/'audit.py'),run_name='readonly_original_path_predicate_not_recorder_main')
selected=obj(B/'SELECTED_ORIGINALS.json')
assert selected==sorted(set(selected)) and len(selected)==1253
assert all(F['original'](p) for p in selected)
searches={'03_broad_structures','04_graph_inclusion','06_precise_graph_operators','12_lonesum_history'}
commands=[]
inputs_count=0
folders=sorted((B/'commands').iterdir())
assert len(folders)==22
for folder in folders:
    c=obj(folder/'receipt.json');before=obj(folder/'inputs_before.json')
    assert before==obj(folder/'inputs_after.json')
    assert obj(folder/'pathset.json')==sorted(before)
    assert c['label']==folder.name and c['cwd']==str(R) and c['exit']==0 and c['unchanged']
    assert c['input_count']==len(before) and c['recorder_sha256']==pin(B/'audit.py')['sha256']
    for path,h in before.items():assert pin(R/path)['sha256']==h;inputs_count+=1
    for name in ('stdout','stderr'):assert c[name+'_sha256']==pin(folder/(name+'.raw'))['sha256']
    if folder.name in searches:
        assert sorted(before)==selected and c['argv'][:4]==['rg','-n','-i','--'] and c['argv'][5:]==selected
    commands.append({'label':folder.name,'argv':c['argv'],'exit':c['exit'],'input_count':len(before)})
pilot=B/'commands/08_oni_pilot_a/stdout.raw'
raw=pilot.read_bytes()
assert pin(pilot)['sha256']=='396d74daa2819cbc46fbee132210ebd67ca6ee78e8924795b2756eef3bb8b1c1'
assert raw==(B/'commands/09_oni_pilot_b/stdout.raw').read_bytes()
records=[json.loads(line) for line in raw.splitlines()]
assert records[-1]['checks']==5500 and records[-1]['total_states']==1100
summaries=[row for row in records if row['kind']=='summary']
assert [row['n'] for row in summaries]==list(range(6))
assert [row['states'] for row in summaries]==[1,1,2,8,64,1024]
assert [row['fixed'] for row in summaries]==[1,1,2,8,49,402]
assert [row['image'] for row in summaries]==[1,1,2,8,49,462]
assert [row['max_tail'] for row in summaries]==[0,0,0,0,1,2]
assert [row['max_fibre'] for row in summaries]==[1,1,1,1,5,38]
for n in range(6):
    states=[row for row in records if row['kind']=='state' and row['n']==n]
    size=1<<(n*(n-1)//2)
    assert [row['source'] for row in states]==list(range(size))
    parents={k:[] for k in range(size)}
    for row in states:parents[row['target']].append(row['source'])
    assert all(len(parents[row['source']])==row['indegree'] for row in states)
states5={row['source']:row for row in records if row['kind']=='state' and row['n']==5}
assert [states5[k]['target'] for k in (59,571,955)]==[571,955,955]
side=B/'commands/21_same_data_inverse/stdout.raw'
assert pin(side)['sha256']=='406f451052d554615388a2917437924e45acedfa5e4ae2e6531b405b32f15ef0'
rows=[json.loads(line) for line in side.read_bytes().splitlines()]
assert len(rows[:-1])==rows[-1]['complete_bipartite_or_empty_targets']==128
assert rows[-1]['checks']==3277 and rows[-1]['status']=='PASS same recorded data only'
closure=[json.loads(line) for line in (B/'commands/22_documentary_closure/stdout.raw').read_bytes().splitlines()]
assert closure[-1]=={'status':'PASS documentary closure only','commands':21,
    'recorded_input_rows':5039,'selected_originals':1253,'checks':5226}
comparisons=[]
pairs=[(pilot,B/'commands/09_oni_pilot_b/stdout.raw'),
       (B/'commands/11_p143_original/stdout.raw',R/'papers/143-boolean-row-inclusion-residual/main.tex')]
for name in ('SYMBOLIC_DYNAMICS_STATE','PIPELINE_STATE','GIT_SYNC_RECEIPT'):
    pairs.append((B/'controls'/(name+'.md'),Q/'central_lifecycle_p209_b_initial'/(name+'.before.md')))
for a,b in pairs:
    argv=['/usr/bin/cmp','--',str(a),str(b)]
    for p in (a,b):pin(p)
    proc=subprocess.run(argv,cwd=R,env=D['ENV'],capture_output=True)
    assert proc.returncode==0 and proc.stdout==proc.stderr==b''
    comparisons.append({'argv':argv,'cwd':str(R),'environment':D['ENV'],'exit':proc.returncode,
                        'stdout':proc.stdout.decode(),'stderr':proc.stderr.decode()})
for path in list(D['READS']):pin(path,fresh=True)
print(json.dumps({'status':'PASS_ROOT_SCOUT32_ORIGINAL_NEGATIVE_CLOSURE','disposition':'NO_PROMOTION',
    'payloads':153,'manifest_sha256':pin(B/'SHA256SUMS')['sha256'],'commands':len(commands),
    'recorded_input_rows':inputs_count,'selected_originals':len(selected),'searches':len(searches),
    'recorded_pilot_states':1100,'recorded_checks_per_run':5500,'recorded_same_data_checks':3277,
    'recorded_inverse_subfamily_targets':128,'all_current_read_paths_twice':len(D['READS']),
    'actual_root_raw_comparisons':comparisons,
    'primary_body_scope':'Actually read archived Dumas-Perez introduction/section2 and Brewbaker sections1-3.2; physical PDFs/full extractions pinned. No new live web discovery or PDF visual review claimed.',
    'boundary':'No ONI or new scientific producer execution, no larger pilot, no independent candidate/manuscript gate, no global novelty inference. The complete fixed class/generic edge clock and bipartite inverse are deducted classical mechanisms; full temporal residual and all-target inverse/extremum remain unproved.',
    'external':'HOLD_EXTERNAL'},indent=2,sort_keys=True))
