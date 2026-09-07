"""Root static/original closure of sealed revision04, not a target execution.
No prepared/historical auditor, recorder, lifecycle or science is imported.
Fresh subprocesses are exactly three raw diff comparisons.
"""
import argparse
import ast
from datetime import datetime, timezone
from hashlib import sha256
import json
import os
from pathlib import Path
import re
import subprocess
import sys

ROOT=Path('/root/autodl-tmp/symbolic_dynamics')
BATCH=ROOT/'docs/papers204_208_sequence'
BASE=BATCH/'qa/p209_terminal_artifact_revision_04'
OLD=BATCH/'qa/p209_terminal_artifact_revision_03'
PAPER=ROOT/'papers/209-ordered-fibre-threading'
ENV={'PATH':'/usr/bin:/bin','LANG':'C.UTF-8','LC_ALL':'C.UTF-8','TZ':'UTC'}
WATCH={}
CODE_ALIASES={}

def read(path):
    path=Path(path); assert path.is_file(),str(path)
    if path.is_relative_to(ROOT): assert not path.is_symlink(),str(path)
    raw=path.read_bytes(); value={'sha256':sha256(raw).hexdigest(),'bytes':len(raw)}
    assert str(path) not in WATCH or WATCH[str(path)]==value,str(path)
    WATCH[str(path)]=value; return raw

def obj(path): return json.loads(read(path))

def pin(path,value):
    value={'sha256':value} if isinstance(value,str) else value
    path=CODE_ALIASES.get((str(path),value['sha256']),Path(path))
    read(path)
    for key in ('sha256','bytes'):
        if key in value: assert WATCH[str(path)][key]==value[key],(str(path),key)

def manifest(base,count,digest):
    pin(base/'SHA256SUMS',digest); entries={}
    for line in read(base/'SHA256SUMS').decode().splitlines():
        m=re.fullmatch(r'([0-9a-f]{64})  (.+)',line); assert m
        wanted,name=m.groups(); path=Path(name)
        assert name not in entries and name!='SHA256SUMS' and not path.is_absolute() and '..' not in path.parts
        entries[name]=wanted; pin(base/name,wanted)
    paths=list(base.rglob('*')); assert not any(p.is_symlink() for p in paths)
    assert len(entries)==count and {p.relative_to(base).as_posix() for p in paths if p.is_file()}==set(entries)|{'SHA256SUMS'}

def functions(raw):
    tree=ast.parse(raw); compile(tree,'<static-only>','exec',dont_inherit=True,optimize=0)
    return {n.name:ast.get_source_segment(raw,n) for n in tree.body if isinstance(n,ast.FunctionDef)}

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--payloads',required=True,type=int); p.add_argument('--sha256',required=True)
    args=p.parse_args(); assert args.payloads>0 and re.fullmatch(r'[0-9a-f]{64}',args.sha256)
    began=datetime.now(timezone.utc).isoformat()
    for path in (Path(__file__),Path(sys.executable),Path('/usr/bin/diff')): read(path)
    manifest(BASE,args.payloads,args.sha256)
    history_roles=obj(BASE/'CODE_HISTORY_ROLES.json')
    exact_helpers={
        ('scope01','documentary.py'):'06b01cd9ed39ada29f8a1e94a5a1f40fa16e5593892015125df3be0709abc53c',
        ('validate01','validate_revision.py'):'00fcb48b9af0ec25fc30ac409abbf090e55265064cd7157c71196e05c5adfee3'}
    assert len(history_roles)==2
    for row in history_roles:
        command=Path(row['actual_command']); original=Path(row['original_path']); physical=Path(row['physical_path'])
        key=(command.parent.name,original.name)
        assert key in exact_helpers and row['sha256']==exact_helpers[key]
        assert original==BASE/key[1] and command==BASE/'commands'/key[0]/'COMMAND.json'
        assert physical==command.parent/(original.name+'.at_execution')
        assert row['role']=='exact_same_command_executing_helper_snapshot'
        assert obj(command.parent/'INPUTS_BEFORE.json')[str(original)]==obj(command.parent/'INPUTS_AFTER.json')[str(original)]=={'sha256':row['sha256'],'bytes':row['bytes']}
        pin(physical,row); CODE_ALIASES[(str(original),row['sha256'])]=physical
    scope=obj(BASE/'SCOPE.json'); intake=obj(BASE/'ORIGINAL_PREDICATE_INSPECTION.json'); final=obj(BASE/'STATIC_RESULT.json')
    assert final['schema']=='p209-revision04-static-preparation-v1' and final['status']=='PASS_STATIC_PREPARATION_ONLY_NOT_ARTIFACT_GATE'
    assert final['original_inputs_before']==final['original_inputs_after'] and final['all_original_inputs_unchanged']
    assert len(final['original_inputs_before'])==final['original_input_paths']
    for path,value in final['original_inputs_before'].items(): pin(path,value)
    for name,data in [('scope',scope),('intake',intake)]:
        assert data['input_pins']==data['inputs_after'] and data['inputs_unchanged']
        for path,value in data['input_pins'].items(): pin(path,value)
        for row in data['pin_checks']:
            assert row['matched']; pin(row['physical_path'],row['wanted']); pin(row['physical_path'],row['actual'])
        assert len(data['unmatched_predicates'])==4 and data['unmatched_predicates']==[r for r in data['checks'] if not r['matched']]
        assert all(row['predicate']=='same_explicit_document_origin' for row in data['unmatched_predicates'])
    assert scope['unmatched_predicates']==intake['unmatched_predicates']
    original_packages=intake['original_packages']; assert len(original_packages)==8
    for row in original_packages:
        assert row['complete_nonself'] and row['manifest_name']=='SHA256SUMS'
        manifest(Path(row['base']),row['payloads'],row['sha256'])
    corrected=intake['corrected_links']; assert corrected['resolved_links']==intake['links']['resolved_links']
    assert len(corrected['resolved_links'])==corrected['local_links']==1534
    for row in corrected['resolved_links']:
        path=Path(row['target']); assert path.exists()
        if 'sha256' in row: pin(path,row['sha256'])
    roles=obj(BASE/'EXACT_FOUR_A_ORIGIN_ROLES.json')
    assert roles==corrected['named_four_role_corrections']==final['exact_four_A_origin_roles'] and len(roles)==4
    expected_names={(a,n) for a in ('delta_check_01','delta_check_02') for n in ('P209_A_RESPONSE.md','P209_A_ROOT_INITIAL_INSPECTION.md')}
    assert {(r['attempt'],Path(r['copy_path']).name) for r in roles}==expected_names
    history=obj(PAPER/'frozen_round2/ROUND2_PROVENANCE.json')['historical_input_resolution']
    for r in roles:
        source,copied=Path(r['original_path']),Path(r['copy_path'])
        assert r['correct_source_origin']==str(source) and r['previous_alias_derived_origin']==str(copied)
        assert copied==BATCH/'reviews/p209_a'/r['attempt']/'exact_response_inputs'/source.name
        assert obj(r['source_copy_table'])[str(source)]=={'copy':str(copied),'sha256':r['sha256']}
        matching=[v for v in history if v['original_path']==str(copied) and v['round2_physical_path']==str(copied)]
        assert matching==[r['round2_identity_role']] and matching[0]['sha256']==r['sha256']
        pin(copied,r['sha256']); pin(source,r['sha256'])
    views=obj(BATCH/'qa/P209_TERMINAL_ROOT_VIEWS.actual.json')
    assert views==intake['views']['actual_original_record']==final['root_view_field_binding']['actual_original_values']
    assert views['measured_page_count']==4 and 'page_count' not in views and views['open_visual_findings']==0
    assert views['schema']=='p209-terminal-root-every-page-view-v1' and views['status']=='ROOT_ACTUALLY_VIEWED_ALL_FOUR_FINAL_PAGES_PASS'
    pin(PAPER/'qa_final/SHA256SUMS',views['terminal_manifest_sha256']); pin(PAPER/'qa_final/cold_build_1/main.pdf',views['pdf_sha256'])
    assert [row['page'] for row in views['pages']]==list(range(1,5))
    for row in views['pages']:
        pin(row['path'],row['sha256']); assert row['actually_displayed_and_viewed'] and row['observation'].strip()
    assert views['retained_nonblocking_diagnostic'] is None
    recipe=obj(BASE/'SOURCE_EDITS.json'); comparisons=obj(BASE/'SOURCE_FUNCTION_CHECKS.json')
    allowed={'audit_p209.py':{'revision_originals_and_failure','root_page_views','pages_and_links'},'record_audit.py':{'main'},'lifecycle_audit.py':set()}
    assert set(recipe)==set(allowed); unchanged={}
    for name,edits in recipe.items():
        old=read(OLD/name).decode(); new=read(BASE/name).decode(); made=old
        assert read(OLD/name)==read(BASE/'original_snapshot'/(OLD/name).relative_to(ROOT))
        for edit in edits:
            assert made.count(edit['old'])==edit['required_old_occurrences']==1
            made=made.replace(edit['old'],edit['new'],1)
        assert made==new
        first,second=functions(old),functions(new); assert set(first)==set(second)
        changed={key for key in first if first[key]!=second[key]}; assert changed==allowed[name]
        unchanged[name]=len(first)-len(changed)
        imports=lambda s:[ast.dump(n) for n in ast.parse(s).body if isinstance(n,(ast.Import,ast.ImportFrom))]
        assert imports(old)==imports(new)
        row=comparisons[name]
        assert row['changed_functions']==sorted(changed) and row['unchanged_function_count']==unchanged[name]
        for key in first:
            assert row['literal_function_comparisons'][key]=={'equal':first[key]==second[key],
                'original_sha256':sha256(first[key].encode()).hexdigest(),'prepared_sha256':sha256(second[key].encode()).hexdigest()}
        assert final['prepared_sources'][name]['changed_functions']==sorted(changed)
        pin(OLD/name,final['prepared_sources'][name]['original_pin']); pin(BASE/name,final['prepared_sources'][name]['prepared_pin'])
    assert unchanged=={'audit_p209.py':32,'record_audit.py':3,'lifecycle_audit.py':36}
    original_views=functions(read(OLD/'audit_p209.py').decode())['root_page_views']
    prepared_functions=functions(read(BASE/'audit_p209.py').decode())
    assert prepared_functions['root_page_views']==original_views.replace("record['page_count']","record['measured_page_count']",1)
    assert "source == named_source and row['sha256'] == named_digest and origins.get(str(copied)) == copied" in prepared_functions['pages_and_links']
    copies=intake['selected_native_copy_comparisons']; assert len(copies)==final['source_copies']==19
    for row in copies:
        pin(row['original'],row['pin']); pin(row['copy'],row['pin']); assert read(row['original'])==read(row['copy'])
        assert row['argv']==['/usr/bin/cmp','--',row['original'],row['copy']] and row['cwd']==str(ROOT) and row['env']==ENV
        assert row['exit_code']==0 and row['stdout']==row['stderr']==''
    assert len(final['fresh_native_copy_comparisons'])==19
    for row in final['fresh_native_copy_comparisons']:
        assert row['exit_code']==0 and row['environment']==ENV and row['cwd']==str(ROOT)
        assert read(row['argv'][2])==read(row['argv'][3])
        for stream in ('stdout','stderr'):
            pin(BASE/row[stream]['path'],row[stream]); assert read(BASE/row[stream]['path'])==b''
    commands=sorted((BASE/'commands').glob('*/COMMAND.json'))
    assert {p.parent.name for p in commands}=={'scope01','inspect01','prepare01','validate01','validate02'}
    native=[]; frozen_source_aliases=[{k:r[k] for k in ('original_path','physical_path','sha256')} for r in history_roles]
    for path in commands:
        folder=path.parent; r=obj(path); before=obj(folder/'INPUTS_BEFORE.json')
        assert before==obj(folder/'INPUTS_AFTER.json') and r['inputs_unchanged'] and len(before)==r['input_count']
        assert r['environment']==ENV and r['cwd']==str(ROOT) and r['status']=='COMPLETED' and r['failure'] is None
        assert r['exit_code']==(1 if folder.name in {'scope01','validate01'} else 0)
        attempt=obj(folder/'ATTEMPT.json'); assert attempt['status']=='ATTEMPTED' and attempt['exit_code'] is None
        assert all(attempt[k]==r[k] for k in ('argv','cwd','environment','started_utc','scope'))
        assert r['started_utc']<=r['ended_utc']
        script=Path(r['argv'][4]); assert r['argv'][:4]==['/usr/bin/python3.10','-I','-S','-B']
        for original,value in before.items():
            pin(original,value)
        for source in (script,BASE/'record_documentary.py'):
            frozen=folder/(source.name+'.at_execution'); pin(frozen,before[str(source)])
        for stream in ('stdout','stderr'): pin(folder/(stream+'.raw'),r[stream])
        if r['exit_code']==0: assert read(folder/'stderr.raw')==b''
        else: assert read(folder/'stderr.raw') and r['stderr']['bytes']>0
        native.append({'label':folder.name,'inputs':len(before),'exit':r['exit_code'],'stdout_bytes':r['stdout']['bytes'],'stderr_bytes':r['stderr']['bytes']})
    closure=obj(BASE/'CLOSURE_CURRENT_INPUTS.json'); assert closure['before']==closure['after'] and closure['unchanged']
    for path,value in closure['before'].items(): pin(path,value)
    census=obj(BASE/'CLOSURE_CHECK.json')
    assert census['status']=='PASS_NATIVE_DOCUMENTARY_CLOSURE_NOT_TARGET_GATE'
    assert census['distinct_current_physical_inputs']==len(closure['before']) and census['recorded_input_occurrences']==sum(r['inputs'] for r in native)
    diffs=[]; initial=obj(BASE/'DIFF_COMMANDS.json'); assert len(initial)==len(final['fresh_native_diffs'])==3
    final_by_argv={tuple(row['argv']):row for row in final['fresh_native_diffs']}
    assert len(final_by_argv)==3 and set(final_by_argv)=={tuple(row['argv']) for row in initial}
    for row in initial:
        last=final_by_argv[tuple(row['argv'])]
        assert row['argv']==last['argv'] and row['exit_code']==last['exit_code']==1
        assert row['cwd']==last['cwd']==str(ROOT) and row['env']==last['environment']==ENV
        for stream in ('stdout','stderr'):
            pin(BASE/row[stream+'_path'],row[stream+'_sha256']); pin(BASE/last[stream]['path'],last[stream])
            assert read(BASE/row[stream+'_path'])==read(BASE/last[stream]['path'])
        run=subprocess.run(row['argv'],cwd=ROOT,env=ENV,capture_output=True,check=False)
        assert run.returncode==1 and run.stdout==read(BASE/row['stdout_path']) and run.stderr==b''
        diffs.append({'argv':row['argv'],'exit':1,'stdout':run.stdout.decode(),'stderr':''})
    parsed=[]
    for path in sorted(BASE.rglob('*.py')):
        compile(ast.parse(read(path)),str(path),'exec',dont_inherit=True,optimize=0); parsed.append(path.relative_to(BASE).as_posix())
    assert set(final['parsed_compiled_only'])<=set(parsed)
    for number in range(1,5):
        folder=BATCH/'qa/p209_terminal_artifact'/f'initial_{number:02d}'
        r=obj(folder/'COMMAND.json'); assert r['exit_code']==1 and r['inputs_unchanged'] and r['unused_cache_absent']
        assert obj(folder/'INPUTS_BEFORE.json')==obj(folder/'INPUTS_AFTER.json') and read(folder/'audit.stdout')==b''
        wrapper=obj(BATCH/'qa'/f'P209_TERMINAL_ARTIFACT_INITIAL_{number:02d}.failed.actual.json')
        assert wrapper['completion']['exit_code']==1 and read(folder/'audit.stderr').decode() in wrapper['completion']['output']
    assert final['target_audit_recorder_lifecycle_executions']==final['science_build_render_views']==0 and not final['initial05_created']
    for name,state in final['current_lifecycle_future_inputs_absent_not_synthesized'].items():
        assert state=={'exists':False,'is_file':False,'is_dir':False} and not Path(name).exists()
    for name,value in WATCH.items():
        raw=Path(name).read_bytes(); assert value=={'sha256':sha256(raw).hexdigest(),'bytes':len(raw)},name
    print(json.dumps({'status':'PASS_ROOT_REVISION04_COMPLETE_STATIC_ORIGINAL_PREFLIGHT_NOT_TARGET_EXECUTION',
        'started_utc':began,'ended_utc':datetime.now(timezone.utc).isoformat(),'revision_payloads':args.payloads,
        'revision_manifest_sha256':args.sha256,'original_inputs_checked':final['original_input_paths'],
        'all_current_paths_rechecked_twice':len(WATCH),'read_map_sha256':sha256(json.dumps(WATCH,sort_keys=True).encode()).hexdigest(),
        'original_packages':original_packages,'native_documentary_attempts':native,'exact_failed_source_aliases':frozen_source_aliases,
        'original_physical_copies_checked':19,'archived_native_copy_comparisons':38,'named_A_semantic_origin_roles':4,
        'resolved_links_unchanged_by_named_correction':1534,'root_original_view_field_checked':'measured_page_count=4',
        'literal_unchanged_functions':unchanged,'python_sources_parsed_only':len(parsed),'fresh_actual_raw_diffs':diffs,
        'all_four_original_target_failures_preserved':True,'target_science_build_view_lifecycle_executions':0,
        'owner':'OWNER_AMBER','external_status':'HOLD_EXTERNAL'},sort_keys=True,indent=2))

if __name__=='__main__':
    assert sys.flags.isolated and sys.flags.no_site and sys.dont_write_bytecode and not sys.flags.optimize
    assert dict(os.environ)==ENV and Path.cwd()==ROOT
    main()
