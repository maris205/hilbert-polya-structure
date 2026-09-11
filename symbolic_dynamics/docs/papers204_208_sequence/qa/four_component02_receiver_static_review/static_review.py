#!/usr/bin/env python3
"""Independent AST and actual documentary data review; no receiver executes."""
import ast
import gzip
from hashlib import sha256
import json
from pathlib import Path
import re

ROOT=Path('/root/autodl-tmp/symbolic_dynamics')
QA=ROOT/'docs/papers204_208_sequence/qa'
HERE=QA/'four_component02_receiver_static_review'
OUT=QA/'five_paper_terminal_component_run_02'
CHECKER=QA/'five_paper_terminal_gate_revision_01'
LAUNCHER=QA/'five_paper_terminal_component_launch_revision_01'
PINS,CHECKS={},[]


def raw(path):
    b=Path(path).read_bytes();PINS[str(path)]={'sha256':sha256(b).hexdigest(),'bytes':len(b)};return b


def obj(path):
    return json.loads(raw(path))


def ck(test,label):
    CHECKS.append(label)
    if not test:raise AssertionError(label)


def rows(path):
    return dict((n,h) for h,n in (re.fullmatch(r'([0-9a-f]{64})  (.+)',x).groups() for x in raw(path).decode().splitlines()))


def main():
    raw(Path(__file__))
    draft=raw(HERE/'receive_four_component02.before_root_corrections.py');tree=ast.parse(draft)
    accepted=ast.parse(raw(QA/'p208_p209_reuse_root_preparation/receive.py'))
    launcher_source=raw(LAUNCHER/'launcher.py');ast.parse(launcher_source)
    ck(sha256(draft).hexdigest()=='68f656ddb94532224b85531f4b7a626f3169c8253cc37b0ddce82da48bbdbf7b','exact_preserved_before_root_correction_source')
    ck(sha256(launcher_source).hexdigest()=='a78aa9d3c9ec1badb1c77c775d99d7b1f52689f65832e000f938acbd12036558','exact_actual_463_line_launcher_source')
    funcs=lambda t:{n.name:ast.dump(n) for n in t.body if isinstance(n,ast.FunctionDef)}
    a,b=funcs(accepted),funcs(tree);unchanged=sorted(n for n in a if a[n]==b.get(n))
    ck(set(a)==set(b) and set(a)-set(unchanged)=={'ledger','original_native','aliases_and_child','failure_preservation','main'},'only_five_receiver_functions_adapted')
    literal_issues=[{'line':n.lineno,'value':n.value} for n in ast.walk(tree) if isinstance(n,ast.Constant) and n.value in (': OK\\n','\\n')]
    ck(len(literal_issues)==2,'two_actual_literal_backslash_n_issues_before_correction')
    roots={n:obj(QA/('FIVE_FOUR_COMPONENT_RUN02_ROOT_'+n+'.actual.json')) for n in ['LAUNCH','PROGRESS01','COMPLETION','SEAL']}
    launch,progress,completion,seal=[roots[n] for n in ['LAUNCH','PROGRESS01','COMPLETION','SEAL']]
    native,receipt,attempt,spawned,parent_intent=[obj(OUT/n) for n in ['NATIVE_RESULT.json','RECEIPT.json','PRE_SPAWN_ATTEMPT.json','SPAWNED.json','LAUNCHER_ATTEMPT.json']]
    ck(launch['result']['session_id']==progress['session_id']==progress['result']['session_id']==completion['session_id']==21492 and launch['result']['output']=='' and type(completion['result']['exit_code']) is int and completion['result']['exit_code']==0,'actual_root_session_native_zero_and_complete_segment_chain')
    ck(progress['launch_record']==completion['launch_record']=='FIVE_FOUR_COMPONENT_RUN02_ROOT_LAUNCH.actual.json' and completion['prior_progress_records']==['FIVE_FOUR_COMPONENT_RUN02_ROOT_PROGRESS01.actual.json'],'exact_named_progress_chain')
    events=[json.loads(x) for x in (progress['result']['output']+completion['result']['output']).splitlines()]
    ck(len(events)==7 and events[:-1]==native['heartbeats'] and len(native['heartbeats'])==6,'all_six_actual_heartbeat_objects_and_final_output')
    ck(all(e['pid']==770811 and e['status']=='FOUR_COMPONENT_NATIVE_RUNNING' and native['started_epoch']<=e['epoch']<=native['finished_epoch'] for e in events[:-1]),'actual_heartbeat_owner_status_times')
    ck(receipt['native']==native and type(native['exit']) is int and native['exit']==0 and native['pid']==native['process_group']==spawned['pid']==spawned['process_group']==770811 and native['outcome']=='COMPLETED' and native['process_group_settled'] is True,'actual_successful_native_and_owned_group')
    ck(native['cleanup']==[{'epoch':native['cleanup'][0]['epoch'],'error':None,'owned_process_group':770811,'probe':'killpg(pid,0)','state':'ABSENT'}],'actual_absent_cleanup_no_signal_or_unknown')
    ck(all(attempt[k]==native[k] for k in ['argv','cwd','env','stdin','stdout','stderr','start_new_session','timeout_seconds','heartbeat_seconds','started_epoch']) and attempt['exit'] is None and attempt['outcome']=='NOT_STARTED' and attempt['cleanup']==attempt['heartbeats']==[],'actual_pre_spawn_fields_and_native_bindings')
    ck(native['timeout_seconds']==600 and native['heartbeat_seconds']==30 and parent_intent['orig_argv']==json.loads(json.dumps(parent_intent['orig_argv'])),'actual_timeout_and_parent_argv_schema')
    ck(receipt['new_reviews']==0 and receipt['p210_accepted'] is False and receipt['five_paper_acceptance'] is False and receipt['owner']=='OWNER_AMBER','four_actual_receipt_boundary_fields_to_add_explicitly')
    manifest=rows(OUT/'SHA256SUMS');ck(len(manifest)==20 and sha256(raw(OUT/'SHA256SUMS')).hexdigest()=='7eda9f4c4452d3d1dc0656ca592cef8e7783a120ccada3fd671cc2238aaf6ebe','actual_twenty_payload_manifest')
    for n,h in manifest.items():ck(sha256(raw(OUT/n)).hexdigest()==h,'actual_twenty_payload_file_key')
    expected_lf=''.join(n+': OK\n' for n in manifest);broken=''.join(n+': OK\\n' for n in manifest)
    ck(seal['result']['output']==expected_lf and seal['result']['output']!=broken and seal['result']['chunk_id']=='1c8942' and seal['result']['exit_code']==0,'actual_native_seal_output_requires_LF_not_literal_backslash_n')
    ledgers=[]
    for stage in ['BEFORE','AFTER']:
        p=OUT/('KNOWN_INPUTS_'+stage+'.json.gz');compressed=raw(p);decoded=gzip.decompress(compressed);meta=obj(OUT/('KNOWN_INPUTS_'+stage+'.meta.json'));data=json.loads(decoded)
        ck(compressed[:3]==b'\x1f\x8b\x08' and compressed[4:8]==b'\x00'*4 and meta['json']=={'sha256':sha256(decoded).hexdigest(),'bytes':len(decoded)} and meta['compressed']['sha256']==sha256(compressed).hexdigest(),'complete_lossless_gzip_and_decoded_meta_keys')
        ck(len(data)==meta['entries']==3266 and decoded==(json.dumps(data,sort_keys=True,separators=(',',':'))+'\n').encode() and all(set(v)=={'sha256','bytes','resolved','symlink'} for v in data.values()),'all3266_original_parent_key_shapes_and_exact_serialization')
        ledgers.append(data)
    ck(ledgers[0]==ledgers[1] and raw(OUT/'KNOWN_INPUTS_BEFORE.json.gz')==raw(OUT/'KNOWN_INPUTS_AFTER.json.gz'),'actual_complete_known_ledger_equal_bytes_and_data')
    known=ledgers[0];scoped=obj(OUT/'SCOPED_INPUTS_BEFORE.json');conf=obj(OUT/'CONFIGURATION_BEFORE.json');contract=obj(CHECKER/'FOUR_INPUTS.json');provenance=obj(LAUNCHER/'PROVENANCE.json')['inputs'];binding=obj(CHECKER/'ROOT_REUSE_BINDING.json')
    ck(scoped==obj(OUT/'SCOPED_INPUTS_AFTER.json') and conf==obj(OUT/'CONFIGURATION_AFTER.json'),'actual_full_scoped_configuration_before_after_equality')
    prep_rows=rows(LAUNCHER/'SHA256SUMS');checker_rows=rows(CHECKER/'SHA256SUMS')
    exactscope={'launcher_preparation':{str(LAUNCHER/n) for n in prep_rows}|{str(LAUNCHER/'SHA256SUMS')},'component_preparation':{str(CHECKER/n) for n in checker_rows}|{str(CHECKER/'SHA256SUMS')},'fixed_inputs':set(contract['fixed_inputs']),'actual_root_binding_and_live_ceiling_index':{binding['native'],binding['report'],str(ROOT/contract['current_index'])},'adaptation_inputs':set(provenance)}
    ck([len(exactscope[n]) for n in exactscope]==[6,15,54,3,75] and all(set(scoped[n])==names for n,names in exactscope.items()),'exact_scoped_6_15_54_3_75_names')
    ck(all(known[n]==v for group in scoped.values() for n,v in group.items()),'all_scoped_rich_keys_equal_actual_parent_known_roles')
    ck(all(all(scoped['fixed_inputs'][n][k]==v[k] for k in ('sha256','bytes')) for n,v in contract['fixed_inputs'].items()) and all(all(scoped['adaptation_inputs'][n][k]==v[k] for k in ('sha256','bytes')) for n,v in provenance.items()),'all54_fixed_and75_adaptation_original_pin_fields')
    stdlib=Path('/usr/lib/python3.10');libs=list(map(Path,['/usr/lib/x86_64-linux-gnu','/usr/lib64','/usr/local/lib']))
    runtime={'/usr/bin/python3.10','/usr/bin/env','/usr/bin/ldd','/bin/bash','/bin/sh'}
    for name in known:
        p=Path(name)
        if p.is_relative_to(stdlib) and not any(x in {'site-packages','dist-packages','__pycache__'} for x in p.parts) and p.suffix not in {'.pyc','.pyo'}:runtime.add(name)
        if any(p.is_relative_to(lib) and (lib!=Path('/usr/local/lib') or len(p.relative_to(lib).parts)==1) for lib in libs) and (p.name.endswith('.so') or '.so.' in p.name):runtime.add(name)
    runtime.update(n for n,v in conf['presence'].items() if v['is_file'])
    runtime.update(n for g in conf['directories'].values() for n,v in (g or {}).items() if v['is_file'])
    parent=obj(OUT/'PARENT_BEFORE.json');consumed=set(parent['mapped_files'])
    for row in parent['modules'].values():
        for n in [row.get('file'),row.get('origin')]:
            if n and n.startswith('/'):consumed.add(known[n]['resolved'] if n in known else n)
    ck(runtime|consumed|set().union(*exactscope.values())==set(known),'3266_union_matches_declared_runtime_selection_parent_sample_and_scoped_names_without_host_regeneration')
    aliases=contract['aliases'];allowed={}
    for row in aliases:
        ck(row['kind']=='documentary_exact_old_path_hash','original_documentary_not_scientific_alias_kind')
        for case in row['cases']:allowed[row['original']+' @ '+row['sha256']+' ['+case+']']=row['physical']
    child=obj(OUT/'checker.stdout');used=child['documentary_aliases_used']
    ck(len(aliases)==13 and sum(len(r['cases']) for r in aliases)==len(allowed)==18 and len(used)==14 and all(allowed.get(k)==v for k,v in used.items()),'13_declarations_18_cases_14_actual_used_roles')
    ck(child['checks']==10270582 and child['current_file_keys_reread']==142784 and child['complete_raw_comparisons_read_only']==20 and child['local_links_checked']==6312 and child['p210_accepted_by_this_component'] is False,'actual_received_child_counts_not_new_reexecution')
    revision=obj(CHECKER/'REVISION_PROVENANCE.json');ck(len(revision['inputs'])==53 and len(revision['unchanged_byte_copies'])==8,'actual_failure53_pins_and8_unchanged_copies')
    for n,row in revision['unchanged_byte_copies'].items():ck(raw(CHECKER/n)==raw(QA/'five_paper_terminal_gate_preparation'/n) and sha256(raw(CHECKER/n)).hexdigest()==row['sha256'],'eight_actual_unchanged_selector_contract_bytes')
    failed=obj(QA/'five_paper_terminal_component_run_01/checker.stdout');failedparent=obj(QA/'five_paper_terminal_component_run_01/RECEIPT.json')
    ck(failed['status']=='FOUR_COMPONENT_FAIL_NO_FIVE_PAPER_ACCEPTANCE' and failed['checks_completed']==8940156 and 'explicit-frozen-link-map' in failed['traceback'] and failedparent['native']['exit']==1 and obj(QA/'FIVE_FOUR_COMPONENT_ROOT_COMPLETION.actual.json')['result']['exit_code']==1,'actual_retained_failure_namespace_and_typed_role_cause')
    return {'status':'STATIC_REVIEW_IDENTIFIED_PRE_EXECUTION_CORRECTIONS_NO_RECEIVER_EXECUTION','checks':len(CHECKS),'check_labels':CHECKS,'source':PINS[str(HERE/'receive_four_component02.before_root_corrections.py')],'source_lines':len(draft.splitlines()),'unchanged_functions':unchanged,'literal_corrections':literal_issues,'scoped_group_counts':{n:len(v) for n,v in exactscope.items()},'declared_runtime_names_from_recorded_known_selection':len(runtime),'early_parent_consumed_names':len(consumed),'known_union_count':len(known),'unused_declared_alias_cases':sorted(set(allowed)-set(used)),'expected_receiver_raw_comparisons':13,'original_child_raw_comparisons_received':20,'documentary_input_count':len(PINS),'input_pins':PINS,'receiver_or_launcher_or_science_imports_and_executions':0,'current_host_file_hash_passes':0,'host_membership_regeneration':0,'child142784_ledger_reexpansion':0,'root_draft_mutations':0,'boundary':'Only the preserved pre-correction source and existing actual documentary records were inspected. Known membership is checked from original recorded roles; actual current host revalidation remains the root receiver execution.'}


if __name__=='__main__':
    print(json.dumps(main(),sort_keys=True,indent=2))
