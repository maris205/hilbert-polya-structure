"""Actual static preparation checks and nonself sealing; no auditor imports."""
import ast
import hashlib
import importlib.util
import json
from pathlib import Path
import sys

ROOT=Path('/root/autodl-tmp/symbolic_dynamics')
BASE=ROOT/'docs/papers204_208_sequence/qa/p209_terminal_artifact_preparation'
spec=importlib.util.spec_from_file_location('owned_documentary_preparation_recorder',BASE/'prepare_inputs.py')
rec=importlib.util.module_from_spec(spec);spec.loader.exec_module(rec)

STATIC=r'''import ast,hashlib,json
from pathlib import Path
R=Path('/root/autodl-tmp/symbolic_dynamics')
B=R/'docs/papers204_208_sequence/qa/p209_terminal_artifact_preparation'
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def source_functions(p):
 source=p.read_text();tree=ast.parse(source,filename=str(p));compile(tree,str(p),'exec')
 return source,tree,{n.name:ast.get_source_segment(source,n) for n in tree.body if isinstance(n,ast.FunctionDef)}
syntax={}
for p in sorted(B.rglob('*.py')):
 source,tree,functions=source_functions(p)
 syntax[str(p.relative_to(B))]={'sha256':digest(p),'lines':len(source.splitlines()),'function_count':len(functions)}
old=source_functions(B/'original_snapshot/audit_p208.py')[2]
new_source,new_tree,new=source_functions(B/'audit_p209.py')
generic=['ck','label','read','j','h','safe','pin','manifest_rows','physical','manifest','alias','maps','config','pair_map','command','actual_auditor_runtime']
assert all(old[n]==new[n] for n in generic)
life=source_functions(B/'lifecycle_audit.py')[2]
shared=generic+['rich_pin','exact_map','exact_pair','declared_runtime_names','terminal_resource_key','modern_presence','stripped_links']
assert all(new[n]==life[n] for n in shared)
imports=[n.name for t in new_tree.body if isinstance(t,ast.Import) for n in t.names]
assert not any(n in imports for n in ('subprocess','importlib','runpy','shutil'))
assert all(not(isinstance(t,ast.Call) and isinstance(t.func,ast.Name) and t.func.id in ('exec','eval','compile','__import__')) for t in ast.walk(new_tree))
assert 'completion_result' in new['review_dependency_keys']
assert new_source[new_source.index('# P209-specific replacement sections'):]==(B/'p209_specific.py.fragment').read_text()
facts={}
paths={
 'A_current':R/'docs/papers204_208_sequence/reviews/p209_a/CURRENT_FINDINGS.json',
 'B_current':R/'docs/papers204_208_sequence/reviews/p209_b/CURRENT_FINDINGS.json',
 'A_failed':R/'docs/papers204_208_sequence/reviews/p209_a/delta_check_01/EXECUTION.actual.json',
 'A_root':R/'docs/papers204_208_sequence/qa/P209_A_ROOT_DELTA_INSPECTION.actual.json',
 'B_root':R/'docs/papers204_208_sequence/qa/P209_B_ROOT_DELTA_INSPECTION.actual.json',
 'terminal_builder':R/'papers/209-ordered-fibre-threading/qa_final/BUILD_EXECUTION.json',
 'terminal_launcher':R/'docs/papers204_208_sequence/qa/root_replays/p209_terminal_strict/launcher_terminal_pair_01/RECEIPT.json'}
for name,p in paths.items():
 if not p.is_file():facts[name]={'present_at_static_inspection':False};continue
 x=json.loads(p.read_bytes())
 facts[name]={'sha256':digest(p),'keys':list(x),'schema':x.get('schema'),'status':x.get('status')}
 if name=='A_failed':facts[name]['completion_exit']=x['completion_result']['exit_code'];assert facts[name]['completion_exit']==1
 if name=='terminal_builder':
  facts[name]['build_keys']=list(x['builds'][0]);facts[name]['command_keys']=list(x['commands'][0])
  facts[name]['command_labels']=[v['label'] for v in x['commands']]
 if name=='terminal_launcher':facts[name]['outer_closure_keys']=list(x['recorder_closure'])
print(json.dumps({'status':'PASS_STATIC_SYNTAX_LITERAL_HELPERS_AND_SCHEMA_INSPECTION',
 'syntax':syntax,'exact_unchanged_P208_helper_blocks':generic,'exact_shared_P209_lifecycle_blocks':shared,
 'auditor_imports':imports,'facts':facts,'target_auditor_executions':0,'new_builds':0,'new_views':0},indent=2,sort_keys=True))
'''

def check():
    commands=[];diffs=[]
    pairs=[('audit',BASE/'original_snapshot/audit_p208.py',BASE/'audit_p209.py'),
           ('recorder',BASE/'original_snapshot/record_p208_audit.py',BASE/'record_audit.py'),
           ('lifecycle',BASE/'original_snapshot/p208_lifecycle_audit.py',BASE/'lifecycle_audit.py'),
           ('unexecuted_draft_fix',BASE/'draft_history/unexecuted_01/audit_p209.py',BASE/'audit_p209.py')]
    for tag,old,new in pairs:
        row,raw=rec.command('final_diff_'+tag,['/usr/bin/diff','-u','--',str(old),str(new)],[old,new],1)
        commands.append(row);diffs.append(raw)
    with (BASE/'ADAPTATION.diff').open('xb') as stream:stream.write(b'\n'.join(diffs))
    paths=sorted(p for p in BASE.rglob('*.py'))+[BASE/'p209_specific.py.fragment']
    paths += [ROOT/p for p in (
      'docs/papers204_208_sequence/reviews/p209_a/CURRENT_FINDINGS.json',
      'docs/papers204_208_sequence/reviews/p209_b/CURRENT_FINDINGS.json',
      'docs/papers204_208_sequence/reviews/p209_a/delta_check_01/EXECUTION.actual.json',
      'docs/papers204_208_sequence/qa/P209_A_ROOT_DELTA_INSPECTION.actual.json',
      'docs/papers204_208_sequence/qa/P209_B_ROOT_DELTA_INSPECTION.actual.json',
      'papers/209-ordered-fibre-threading/qa_final/BUILD_EXECUTION.json',
      'docs/papers204_208_sequence/qa/root_replays/p209_terminal_strict/launcher_terminal_pair_01/RECEIPT.json') if (ROOT/p).is_file()]
    row,raw=rec.command('final_static',['/usr/bin/python3.10','-I','-S','-B','-c',STATIC],paths,0)
    commands.append(row);rec.save(BASE/'FINAL_STATIC_CHECK.json',json.loads(raw))
    rec.save(BASE/'FINAL_CHECK_EXECUTIONS.json',commands)
    print(raw.decode())

def seal():
    assert not (BASE/'SHA256SUMS').exists()
    required=('README.md','ADAPTATION.diff','FINAL_STATIC_CHECK.json','FINAL_CHECK_EXECUTIONS.json',
              'INPUT_CONTRACT.json','audit_p209.py','record_audit.py','lifecycle_audit.py')
    assert all((BASE/n).is_file() for n in required)
    final=json.loads((BASE/'FINAL_STATIC_CHECK.json').read_bytes())
    assert final['status']=='PASS_STATIC_SYNTAX_LITERAL_HELPERS_AND_SCHEMA_INSPECTION' and final['target_auditor_executions']==0
    for name in ('audit_p209.py','record_audit.py','lifecycle_audit.py'):
        assert rec.info(BASE/name)['sha256']==final['syntax'][name]['sha256']
    originals=json.loads((BASE/'ORIGINAL_INPUTS.json').read_bytes())
    source_status={}
    for name,row in originals.items():
        copy=BASE/row['copy'];value=rec.info(copy)
        assert all(value[k]==row[k] for k in ('sha256','bytes'))
        current=rec.info(name)
        source_status[name]={'physical_copy':row['copy'],'snapshot_sha256':row['sha256'],
            'current_sha256':current['sha256'],'same_bytes_now':current['sha256']==row['sha256']}
    entries=sorted(p for p in BASE.rglob('*') if p.is_file())
    assert all(not p.is_symlink() for p in BASE.rglob('*'))
    before={str(p.relative_to(BASE)):rec.info(p) for p in entries}
    after={str(p.relative_to(BASE)):rec.info(p) for p in entries};assert before==after
    rec.save(BASE/'PRESEAL.json',{'status':'PASS_STATIC_PREPARATION_ONLY','payloads_before_this_record':len(before),
        'input_pins_before_and_after':before,'all_inputs_unchanged':True,'original_physical_snapshots':source_status,
        'target_auditor_executions':0,'scientific_executions':0,'builds':0,'renders':0,'page_views':0,
        'future_artifact_or_lifecycle_acceptance':False})
    payloads=sorted(p for p in BASE.rglob('*') if p.is_file())
    with (BASE/'SHA256SUMS').open('xb') as stream:
        stream.write(''.join(rec.info(p)['sha256']+'  '+p.relative_to(BASE).as_posix()+'\n' for p in payloads).encode())
    rows={line.split('  ',1)[1]:line.split('  ',1)[0] for line in (BASE/'SHA256SUMS').read_text().splitlines()}
    assert set(rows)=={p.relative_to(BASE).as_posix() for p in BASE.rglob('*') if p.is_file() and p.name!='SHA256SUMS'}
    assert all(rec.info(BASE/n)['sha256']==d for n,d in rows.items())
    print(json.dumps({'status':'PASS_SEALED_STATIC_PREPARATION_NOT_ARTIFACT_ACCEPTANCE','payloads':len(rows),
        'manifest_sha256':rec.info(BASE/'SHA256SUMS')['sha256'],'prepared_auditor_sha256':rec.info(BASE/'audit_p209.py')['sha256'],
        'prepared_recorder_sha256':rec.info(BASE/'record_audit.py')['sha256'],
        'prepared_lifecycle_sha256':rec.info(BASE/'lifecycle_audit.py')['sha256'],
        'target_auditor_executions':0},sort_keys=True,indent=2))

if __name__=='__main__':
    assert sys.flags.isolated and sys.flags.no_site and sys.dont_write_bytecode and sys.flags.optimize==0
    if sys.argv[1:]==['check']:check()
    elif sys.argv[1:]==['seal']:seal()
    else:raise RuntimeError('Require check or seal; only static preparation work is permitted')
