#!/usr/bin/env python3
"""AST and existing strict-pair documentary data only. Never import/run receiver."""
import ast
import copy
from datetime import datetime
from hashlib import sha256
import json
from pathlib import Path
import re
import sysconfig

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
QA = ROOT / 'docs/papers204_208_sequence/qa'
HERE = QA / 'p210_b_strict_receiver_revision_01'
PREP = QA / 'p210_b_strict_preparation'
OUT = QA / 'root_replays/p210_b_strict_pair_01'
B = ROOT / 'docs/papers204_208_sequence/reviews/p210_b'
ENV = {'PATH':'/usr/bin:/bin','LANG':'C.UTF-8','LC_ALL':'C.UTF-8','TZ':'UTC'}
PINS, CHECKS = {}, []


def raw(path):
    data = Path(path).read_bytes()
    PINS[str(path)] = {'bytes':len(data),'sha256':sha256(data).hexdigest()}
    return data


def obj(path):
    return json.loads(raw(path))


def ck(test, label):
    CHECKS.append(label)
    if not test:
        raise AssertionError(label)


def funcs(tree):
    return {n.name:n for n in tree.body if isinstance(n,ast.FunctionDef)}


def assigned(tree, name):
    return next(n.value for n in tree.body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id==name for t in n.targets))


def manifest_rows(path):
    return dict((n,h) for h,n in (re.fullmatch(r'([a-f0-9]{64})  (.+)',line).groups() for line in raw(path).decode().splitlines()))


class NormalizeConfig(ast.NodeTransformer):
    def visit_FunctionDef(self, node):
        node=self.generic_visit(node);node.name='configuration'
        node.body=[n for n in node.body if not(isinstance(n,ast.Expr) and isinstance(n.value,ast.Constant) and isinstance(n.value.value,str))]
        return node
    def visit_Assign(self,node):
        if any(isinstance(t,ast.Name) and t.id=='ldd' for t in node.targets):
            node.value=ast.parse("raw('/usr/bin/ldd').decode()",mode='eval').body
        return self.generic_visit(node)
    def visit_Name(self,node):
        if node.id=='value': return ast.Name(id='val',ctx=node.ctx)
        if node.id=='lexists': return ast.parse('os.path.lexists',mode='eval').body
        return node


def main():
    raw(Path(__file__))
    source=raw(HERE/'receive_p210_b_strict.py'); tree=ast.parse(source); new=funcs(tree)
    old=funcs(ast.parse(raw(QA/'p210_b_strict_receiver_static_review/inspect_p210_b_strict_pair.before_root_followup.py')))
    runner_tree=ast.parse(raw(PREP/'run_pair.py')); runner=funcs(runner_tree)
    ck(PINS[str(PREP/'run_pair.py')]['sha256']=='bacc8bf0351bdfbcc2bc671cd61131d6382fe5caccd00f02e3988afbf1d066d1','actual_sealed_623_line_runner')
    ck(all(ast.dump(new[n])==ast.dump(old[n]) for n in old if n!='main'),'all_eight_original_helpers_exact_AST')
    normal=lambda n:ast.dump(NormalizeConfig().visit(copy.deepcopy(n)))
    ck(normal(new['configuration_snapshot'])==normal(runner['configuration']),'complete_configuration_AST_matches_actual_generator_after_only_read_ledger_adaptations')
    for name in ('LIB_ROOTS','DATA_ROOTS','STDLIB','PYTHON'):
        ck(ast.dump(assigned(tree,name))==ast.dump(assigned(runner_tree,name)),'exact_configuration_global_'+name)
    forbidden={'write_bytes','write_text','mkdir','unlink','rename','rmdir','touch','system','popen','Popen','exec','eval','compile','__import__','run','check_call','check_output'}
    for n in ast.walk(tree):
        if isinstance(n,ast.Call):
            name=n.func.id if isinstance(n.func,ast.Name) else n.func.attr if isinstance(n.func,ast.Attribute) else None
            ck(name not in forbidden,'no_receiver_writer_process_or_dynamic_program_execution_call')
    ck(b"manifest(REVISION, sys.argv[2], 7)" in source and b'strict-B-actual-only' in source and b'never_created_receiver_cache' in source,'exact_self_seal_argv_source_only_preconditions')
    for name,digest in ast.literal_eval(assigned(tree,'ROOT_NATIVE_KEYS')).items():
        ck(sha256(raw(QA/name)).hexdigest()==digest,'actual_four_outer_native_record_pins')
    launch,completion,seal,preflight=[obj(QA/('P210_B_STRICT_ROOT_'+n+'.actual.json')) for n in ['LAUNCH','COMPLETION','SEAL','PREFLIGHT']]
    native=json.loads(completion['result']['output'])
    ck(set(launch)=={'role','command','result'} and launch['result']['output']=='' and launch['result']['session_id']==completion['session_id']==31521 and completion['result']['exit_code']==0,'actual_missing_wrapper_cwd_and_empty_then_single_JSON_native_zero')
    ck(native['closure']['payloads']==59 and native['closure']['manifest']['sha256']=='54cdd8ca9a00374f53a82e7f84a47fdd91f3fcde8b1519b027b98c7925ace181','actual_outer_bound_pair_seal')
    pair=manifest_rows(OUT/'SHA256SUMS');prep=manifest_rows(PREP/'SHA256SUMS');package=manifest_rows(B/'SHA256SUMS')
    ck(len(pair)==59 and len(prep)==4 and len(package)==407,'actual_manifest_schema_counts')
    ck(seal['command']=='/usr/bin/sha256sum -c SHA256SUMS' and seal['cwd']==str(OUT) and seal['result']['exit_code']==0 and seal['result']['output']==''.join(n+': OK\n' for n in pair),'full_actual_59_line_native_seal_output')
    ck(preflight['preparation_seal_check']['result']['exit_code']==0 and preflight['preparation_seal_check']['result']['output']==''.join(n+': OK\n' for n in prep),'full_actual_four_line_preparation_seal_output')
    entered=obj(OUT/'RUN_ENTERED.json');copies=obj(OUT/'SOURCE_ONLY_INITIAL.json');closure=obj(OUT/'PACKAGE_AND_PREPARATION_CLOSURE.json')
    parent=[str(Path('/usr/bin/python3.10')),'-I','-S','-B','-X','pycache_prefix='+str(OUT/'unused_parent_cache'),str(PREP/'run_pair.py'),'run','--role','p210_b','--expected-preparation-sha256','987367c15fae0bd4d34ebf6c97cd1ee2dc71d1f15782ec57d73f61a332d97eec']
    ck(entered['argv']==parent[6:] and entered['interpreter_argv']==parent and entered['cwd']==str(ROOT) and entered['environment']==ENV,'actual_run_entered_argv_environment_cwd_schema')
    ck(launch['command']==' '.join(['/usr/bin/env','-i','PATH=/usr/bin:/bin','LANG=C.UTF-8','LC_ALL=C.UTF-8','TZ=UTC']+parent),'exact_actual_outer_launch_command')
    for phase in ('before','after'):
        ck(obj(OUT/('observations/parent_'+phase+'.json'))['argv']==parent[6:],'actual_both_parent_observation_argv')
    ck(set(copies)=={'run_pair.py','verify.py','PARAMETERS.json'} and all(set(v)=={'origin','copy','sha256','bytes'} for v in copies.values()),'actual_source_only_three_record_shapes')
    for name,origin in [('run_pair.py',PREP/'run_pair.py'),('verify.py',B/'verify.py'),('PARAMETERS.json',B/'PARAMETERS.json')]:
        ck(copies[name]['origin']==str(origin) and copies[name]['copy']==str(OUT/'sources'/name),'exact_actual_source_origin_and_copy_roles')
    baseline=closure['before'];inputs=obj(PREP/'INPUT_PINS.json')['inputs'];resources=obj(OUT/'RESOURCE_NAMES_BEFORE.json');conf=obj(OUT/'CONFIGURATION_BEFORE.json');known=obj(OUT/'INPUTS_BEFORE.json')
    ck(closure['before']==closure['after'] and baseline['package_files']==sorted(str(B/n) for n in package)+[str(B/'SHA256SUMS')] and baseline['preparation_files']==sorted(str(PREP/n) for n in prep)+[str(PREP/'SHA256SUMS')],'exact_declared_complete_package_preparation_role_lists')
    base=set(baseline['package_files'])|set(baseline['preparation_files'])|set(resources)|set(inputs)|{v['copy'] for v in copies.values()}|{n for n,v in conf.items() if v['is_file']}
    # Resolve through the actual recorded rich keys, not by rereading host files.
    ck(base<=set(known) and base|{known[n]['resolved'] for n in base}==set(known) and len(known)==3558,'actual_3558_declared_known_union_using_recorded_resolved_roles')
    ck(known==obj(OUT/'INPUTS_AFTER.json') and resources==obj(OUT/'RESOURCE_NAMES_AFTER.json') and conf==obj(OUT/'CONFIGURATION_AFTER.json') and len(resources)==3121 and len(conf)==41,'complete_actual_archived_before_after_schema_equality_not_current_host_validation')
    result=obj(OUT/'RESULT.json');expect={};cmp=lambda a,b:['/usr/bin/cmp','--',str(a),str(b)]
    for label,a,b in [('00_cmp_runner_source',PREP/'run_pair.py',OUT/'sources/run_pair.py'),('01_cmp_verifier_source',B/'verify.py',OUT/'sources/verify.py'),('01a_cmp_parameters_source',B/'PARAMETERS.json',OUT/'sources/PARAMETERS.json')]:expect[label]=cmp(a,b)
    ldd=['/usr/bin/ldd','/usr/bin/python3.10','/usr/bin/cmp']+sorted(n for n in resources if n.startswith('/usr/lib/python3.10/') and n.endswith('.so'));expect['02_ldd_before']=ldd
    for n in ('01','02'):expect['03_verify_'+n]=['/usr/bin/python3.10','-I','-S','-B','-X','pycache_prefix='+str(OUT/('unused_child_'+n+'_cache')),str(OUT/'sources/run_pair.py'),'child',n,'p210_b']
    for n in ('01','02'):expect['04_cmp_canonical_'+n]=cmp(OUT/('commands/03_verify_'+n+'/stdout.raw'),B/'CANONICAL.json')
    expect['05_cmp_pair']=cmp(OUT/'commands/03_verify_01/stdout.raw',OUT/'commands/03_verify_02/stdout.raw');expect['06_ldd_after']=ldd
    ck([r['label'] for r in result['commands']]==list(expect),'actual_exact_ten_label_order')
    previous=datetime.fromisoformat(entered['started_utc']);owners=[]
    for rec in result['commands']:
        label=rec['label'];attempt=obj(OUT/'commands'/label/'ATTEMPT.json');receipt=obj(OUT/'commands'/label/'RECEIPT.json')
        ck(receipt=={k:v for k,v in rec.items() if k!='label'} and receipt['argv']==attempt['argv']==expect[label],'actual_complete_native_argv_and_record_identity')
        ck(attempt['timeout_seconds']==receipt['timeout_seconds']==(300 if label.startswith('03_verify_') else 60) and receipt['stdin']=='DEVNULL' and receipt['new_owned_session_requested'] is True and receipt['status']=='COMPLETED' and receipt['interrupted'] is False,'actual_timeout_stdin_and_completed_schema')
        begin,end=map(datetime.fromisoformat,(receipt['started_utc'],receipt['ended_utc']));ck(previous<=begin<=end<=datetime.fromisoformat(result['ended_utc']),'actual_native_chronology');previous=end
        settle=receipt['process_group_settlement'];ck(settle['owned_pgid']==settle['owned_sid']>0 and settle['quiescent'] is True and settle['signals']==[] and settle['native_returncode']==0 and settle['remaining_members']==[],'actual_positive_settled_owned_group');owners.append(settle['owned_pgid'])
    ck(len(set(owners))==10,'actual_ten_distinct_owned_groups')
    ck(obj(OUT/'COMMAND_CLOSURE.json')=={'command_count':10,'native_streams_rechecked':20,'scope':'Every entire recorded receipt, pre-spawn record and raw stream rechecked after the pair.'},'actual_complete_command_closure')
    for number in ('01','02'):
        child=obj(OUT/('observations/child_'+number+'.json'))
        ck(child['python_open_events']==[{'path':str(OUT/'sources'/name),'mode':'r','flags':524288} for name in ('verify.py','PARAMETERS.json')] and child['nonfile_open_paths_at_end']==[],'actual_complete_two_python_open_events_not_new_science')
    ck(result['results']==[{'number':n,'checks':51129,'stdout':{'sha256':'fbddce4cc05761bd0eed959d57b6de32b9cde38f23128872189a7e64349cfab2','bytes':6475161}} for n in ('01','02')],'actual_two_result_original_canonical_keys')
    return {'status':'PASS_AST_AND_ACTUAL_DOCUMENTARY_DATA_ONLY_RECEIVER_NOT_EXECUTED','checks':len(CHECKS),'check_labels':CHECKS,'receiver_source':PINS[str(HERE/'receive_p210_b_strict.py')],'receiver_lines':len(source.splitlines()),'documentary_files_read':len(PINS),'input_pins':PINS,'original_helpers_preserved':sorted(set(old)-{'main'}),'actual_pair_payloads':59,'actual_known_input_count':3558,'actual_resource_count':3121,'actual_configuration_count':41,'actual_outer_session':31521,'actual_native_commands':10,'receiver_imports_or_executions':0,'scientific_program_imports_or_executions':0,'new_host_file_hash_passes':0,'current_host_inventory_regeneration':0,'new_builds_or_views':0,'scope':'AST comparisons and existing actual documentary schemas/keys only; root must full-read and execute the receiver. This is not a pair or receiver PASS.'}


if __name__=='__main__':
    print(json.dumps(main(),sort_keys=True,indent=2))
