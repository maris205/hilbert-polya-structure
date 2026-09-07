"""Static source/schema inspection only. Prepared auditors are never imported."""
import importlib.util
import json
from pathlib import Path
import sys

ROOT=Path('/root/autodl-tmp/symbolic_dynamics')
BASE=ROOT/'docs/papers204_208_sequence/qa/p209_terminal_artifact_preparation'
spec=importlib.util.spec_from_file_location('owned_preparation_recording_only',BASE/'prepare_inputs.py')
rec=importlib.util.module_from_spec(spec);spec.loader.exec_module(rec)

PROGRAM=r'''import ast,json
from pathlib import Path
R=Path('/root/autodl-tmp/symbolic_dynamics')
B=R/'docs/papers204_208_sequence/qa/p209_terminal_artifact_preparation'
paths=[p for p in B.glob('*.py')]
syntax={}
for p in paths:
 t=ast.parse(p.read_text(),filename=str(p));compile(t,str(p),'exec')
 syntax[p.name]={'lines':len(p.read_text().splitlines()),'functions':[n.name for n in t.body if isinstance(n,ast.FunctionDef)]}
def shape(x):
 if isinstance(x,dict):return {k:('dict:'+str(len(v)) if isinstance(v,dict) else 'list:'+str(len(v)) if isinstance(v,list) else v) for k,v in x.items()}
 return type(x).__name__
paths={
 'round1':R/'papers/209-ordered-fibre-threading/frozen_round1/ROUND1_PROVENANCE.json',
 'A_failed':R/'docs/papers204_208_sequence/reviews/p209_a/delta_check_01/EXECUTION.actual.json',
 'A_original':R/'docs/papers204_208_sequence/reviews/p209_a/initial_audit_01/CURRENT_INPUT_CLOSURE.json',
 'A_delta_before':R/'docs/papers204_208_sequence/reviews/p209_a/delta_check_02/INPUTS_BEFORE.json',
 'B_intake':R/'docs/papers204_208_sequence/reviews/p209_b/delta_intake_01/INTAKE_RESULT.json',
 'author_pair':R/'docs/papers204_208_sequence/qa/root_replays/p209_author_strict/root_author_pair_01/RECEIPT.json',
 'B_pair':R/'docs/papers204_208_sequence/qa/root_replays/p209_b_strict/root_b_pair_01/RECEIPT.json'}
facts={}
for name,p in paths.items():
 x=json.loads(p.read_bytes())
 if name=='round1':facts[name]={'schema':x['schema'],'prior_whole':x['prior_whole_paper_manifest'],'anchor_keys':list(x['anchor_mapping'])};facts[name]['prior_whole']=shape(facts[name]['prior_whole'])
 elif name in ('A_original','A_delta_before'):facts[name]={'count':len(x),'first_key':next(iter(x)),'first_value':next(iter(x.values()))}
 elif name=='B_intake':facts[name]={'shape':shape(x),'first_copy':x['copies'][0]}
 elif name.endswith('pair'):facts[name]={'shape':shape(x),'result':shape(x['result']),'replay':shape(x['result']['replays'][0])}
 else:facts[name]=shape(x)
print(json.dumps({'status':'PASS_STATIC_SYNTAX_AND_ORIGINAL_SCHEMA_INSPECTION','syntax':syntax,'facts':facts,'target_auditor_executions':0},indent=2,sort_keys=True))
'''

if __name__=='__main__':
    assert sys.argv[1:]==['initial']
    paths=list(BASE.glob('*.py'))+[BASE/'original_snapshot/audit_p208.py']
    paths += [ROOT/p for p in (
      'papers/209-ordered-fibre-threading/frozen_round1/ROUND1_PROVENANCE.json',
      'docs/papers204_208_sequence/reviews/p209_a/delta_check_01/EXECUTION.actual.json',
      'docs/papers204_208_sequence/reviews/p209_a/initial_audit_01/CURRENT_INPUT_CLOSURE.json',
      'docs/papers204_208_sequence/reviews/p209_a/delta_check_02/INPUTS_BEFORE.json',
      'docs/papers204_208_sequence/reviews/p209_b/delta_intake_01/INTAKE_RESULT.json',
      'docs/papers204_208_sequence/qa/root_replays/p209_author_strict/root_author_pair_01/RECEIPT.json',
      'docs/papers204_208_sequence/qa/root_replays/p209_b_strict/root_b_pair_01/RECEIPT.json')]
    result,raw=rec.command('static_initial',['/usr/bin/python3.10','-I','-S','-B','-c',PROGRAM],paths,0)
    value=json.loads(raw);rec.save(BASE/'INITIAL_STATIC_CHECK.json',value)
    print(raw.decode())
