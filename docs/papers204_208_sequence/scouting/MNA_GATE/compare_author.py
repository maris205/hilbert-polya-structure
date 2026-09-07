#!/usr/bin/env python3
"""Compare full frozen author pilot records, never execute/import author code."""
import hashlib
import json
from pathlib import Path
import subprocess
import time

ROOT=Path('/root/autodl-tmp/symbolic_dynamics')
GATE=ROOT/'docs/papers204_208_sequence/scouting/MNA_GATE'
folder=GATE/'evidence/author_comparison'
folder.mkdir()
author=GATE/'inputs/author_lane40/commands/17_one_mna_pilot/stdout.raw'
canonical=GATE/'CANONICAL.json'
checks=0

def check(ok,detail):
    global checks
    checks+=1
    if not ok:
        raise AssertionError(detail)

def pin(p):
    data=p.read_bytes()
    return {'sha256':hashlib.sha256(data).hexdigest(),'bytes':len(data)}

before={str(p):pin(p) for p in (author,canonical,Path(__file__).resolve())}
records=[json.loads(line) for line in author.read_text().splitlines()]
independent=json.loads(canonical.read_text())
check(len(records)==4109,('record_count',len(records)))
check(records[0]['N_min']==1 and records[0]['N_max']==12,'original_box')
check(records[-1]['status']=='PASS' and records[-1]['total_states']==4095,'author_completion')
author_states={(r['N'],tuple(r['state'])):r for r in records if r['type']=='state'}
check(len(author_states)==4095,'unique_author_states')
check(len([r for r in records if r['type']=='summary'])==12,'12_summaries')
left,right=[],[]
author_summaries={r['N']:r for r in records if r['type']=='summary'}
summary_rows=[]
event_counts={'deleted_cut_A':0,'previous_round_right_block':0,'new_block_B':0}
for box in independent['boxes']:
    n=box['N']
    for row in box['states']:
        original=author_states[n,tuple(row['state'])]
        expected_keys={'type','N','state','next','tail','terminal','orbit','fibre','fibre_formula','image_threshold'}
        check(set(original)==expected_keys,('author_state_schema',n,row['state']))
        projection={'N':n,'state':row['state'],'next':row['next'],'tail':row['tail'],
                    'terminal':row['terminal'],'orbit':row['orbit'],'fibre':row['fibre'],
                    'fibre_formula':row['formula'],'image_threshold':row['minimum_first'] is not None}
        original_projection={k:v for k,v in original.items() if k!='type'}
        for key in projection:
            check(projection[key]==original_projection[key],('full_state_field',n,row['state'],key))
        left.append(original_projection)
        right.append(projection)
        for event in row['events']:
            event_counts['deleted_cut_A']+=len(event['deleted'])
            event_counts['new_block_B']+=len(event['created'])
            if event['t']>=2:
                event_counts['previous_round_right_block']+=len(event['deleted'])
    summary=box['summary']
    old=author_summaries[n]
    histogram={}
    for row in box['states']:
        key=str(row['tail'])
        histogram[key]=histogram.get(key,0)+1
    h=summary['max_tail']
    witness=[1] if h==0 else list(range(h,0,-1))+[n-h*(h+1)//2]
    orbit=next(r['orbit'] for r in box['states'] if r['state']==witness)
    projected={'type':'summary','N':n,'states':summary['state_count'],'image':summary['image_count'],
               'fixed':summary['fixed_count'],'max_tail':h,'bound':h,
               'tail_histogram':histogram,'max_tail_states':histogram[str(h)],
               'max_fibre':summary['max_fibre'],'max_fibre_targets':summary['max_fibre_targets'],
               'witness':witness,'witness_orbit':orbit}
    # Author uses cut-mask ordering for max-fibre targets; order is not scientific content.
    old_compare=dict(old)
    old_compare['max_fibre_targets']=sorted(old_compare['max_fibre_targets'])
    projected['max_fibre_targets']=sorted(projected['max_fibre_targets'])
    check(old_compare==projected,('complete_summary',n,old_compare,projected))
    summary_rows.append({'N':n,'all_summary_fields_match':True})
check(event_counts==records[-1]['event_checks'],'all_original_event_counts')
for name,data in [('AUTHOR_PROJECTION.json',left),('INDEPENDENT_PROJECTION.json',right)]:
    (folder/name).write_text(json.dumps(data,sort_keys=True,separators=(',',':'))+'\n')
argv=['/usr/bin/cmp',str(folder/'AUTHOR_PROJECTION.json'),str(folder/'INDEPENDENT_PROJECTION.json')]
start=time.time()
p=subprocess.run(argv,cwd=ROOT,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
(folder/'cmp.stdout.raw').write_bytes(p.stdout)
(folder/'cmp.stderr.raw').write_bytes(p.stderr)
after={path:pin(Path(path)) for path in before}
check(before==after,'comparison_input_stability')
result={'status':'PASS' if p.returncode==0 else 'FAIL','checks':checks,
        'role':'complete_frozen_author_to_independent_scientific_projection_not_original_raw_identity',
        'argv':argv,'cwd':str(ROOT),'started_epoch':start,'finished_epoch':time.time(),'exit':p.returncode,
        'inputs_before':before,'inputs_after':after,'matched_state_rows':len(left),
        'summary_rows':summary_rows,'event_counts':event_counts,
        'projection_pins':{name:pin(folder/name) for name in ('AUTHOR_PROJECTION.json','INDEPENDENT_PROJECTION.json')},
        'stdout':pin(folder/'cmp.stdout.raw'),'stderr':pin(folder/'cmp.stderr.raw')}
(folder/'RESULT.json').write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
check(p.returncode==0,'actual_raw_projection_cmp')
print(json.dumps(result,sort_keys=True,indent=2))
