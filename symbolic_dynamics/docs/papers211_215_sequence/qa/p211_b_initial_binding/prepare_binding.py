"""Root B-only initial binding, disclosed A binding infrastructure reuse."""
import ast
from hashlib import sha256
import json
import math
import os
from pathlib import Path

ROOT=Path('/root/autodl-tmp/symbolic_dynamics')
QA=ROOT/'docs/papers211_215_sequence/qa'
REVIEW=ROOT/'docs/papers211_215_sequence/reviews/p211_b'
OUT=Path(__file__).resolve().parent
PREP=QA/'p211_runtime_preparation'
RECEPTION=QA/'p211_b_root_reception'
ATTEMPT=QA/'root_replays/p211_b_initial_01'
READS={}
def raw(path):
    p=Path(path)
    data=p.read_bytes()
    assert str(p) not in READS or READS[str(p)]==data
    READS[str(p)]=data
    return data
def pin(path,expected=None):
    p=Path(path)
    data=raw(p)
    row={'sha256':sha256(data).hexdigest(),'bytes':len(data),'resolved':str(p.resolve(strict=True)),
         'symlink':os.readlink(p) if p.is_symlink() else None}
    expected={'sha256':expected} if isinstance(expected,str) else expected
    assert expected is None or all(row[k]==expected[k] for k in row if k in expected),str(p)
    return row
def doc(path): return json.loads(raw(path))
def write(name,value):
    with (OUT/name).open('xb') as f: f.write((json.dumps(value,sort_keys=True,indent=2,allow_nan=False)+'\n').encode())

assert OUT==QA/'p211_b_initial_binding'
assert not (OUT/'BINDING.json').exists() and not os.path.lexists(ATTEMPT) and not os.path.lexists(REVIEW/'CANONICAL.json')
assert ATTEMPT.parent.resolve(strict=True)==ATTEMPT.parent
source=pin(REVIEW/'verify.py','6888ea1df1c20e4786c3582a61fcc5c7d6c8901d9e322d16dc50b047786c5fa7')
params_pin=pin(REVIEW/'parameters.json','214b1832a5aae184bd0617334307d87cdcb51f29d2b41983593bdae2d5fc2cac')
parameters=doc(REVIEW/'parameters.json')
tree=ast.parse(raw(REVIEW/'verify.py'))
assert [n.names[0].name for n in tree.body if isinstance(n,ast.Import)]==['itertools','json','math','sys']
assert not any(isinstance(n,ast.ImportFrom) for n in ast.walk(tree))
decl=[n for n in tree.body if isinstance(n,ast.Assign) and isinstance(n.targets[0],ast.Name) and n.targets[0].id=='EXPECTED_PARAMETERS']
assert len(decl)==1 and ast.literal_eval(decl[0].value)==parameters
assert parameters['n_values']==list(range(1,8)) and parameters['expected_total_states']==2353
lock_path=PREP/'discovery02/RUNTIME_LOCK.json'
lock_pin=pin(lock_path,'1499a93909e39b49c16408985053936b7eb7efcf664e91fd75fa77de607be2ab')
lock=doc(lock_path)
assert len(lock['files'])==122
for p,r in lock['files'].items(): pin(p,r)
adapter={str(PREP/n):pin(PREP/n,h) for n,h in (
    ('runtime_core.py','2fd41cfac779f8d5f4e23089fcc9f2b6b041cbebe19e7003b2db6b4815909934'),
    ('p211_runtime.py','bff2dcf25ee846b04eac0bbd46eb7b3e58c728c6d7e8e9ce591c9cef1ae4e421'))}
pin(RECEPTION/'PREPARATION_RESULT.json','90d9ddd43553546657a22298c8d0540b04f57fbd3c25188e0b83241587c47cde')
pin(RECEPTION/'PREPARATION_NATIVE01.json','99adc5a15b66a730034e72e5b5e6dd204fc40a6440b6878e63b2230027c2ec4c')
received=doc(RECEPTION/'PREPARATION_RESULT.json')
native=doc(RECEPTION/'PREPARATION_NATIVE01.json')
assert native['result']['exit_code']==0 and json.loads(native['result']['output'])==received
assert received['status']=='PASS_ROOT_B_PREPARATION_ORIGINALS' and received['payloads']==19 and received['checks']==2318
assert doc(RECEPTION/'BUILD_REUSE_NATIVE01.json')['result']['exit_code']==0
pin(REVIEW/'PREPARATION_SHA256SUMS','7a55db3d72952dac3bf77ea0f0bf82989606296684561ef468ea67ca2ff9850f')
pin(RECEPTION/'inspect_production.py','d932d090a675b076eb518eca4bd97c0a6bb7900952e58b978089b527b684f77a')
pin(RECEPTION/'inspect_saved_output.py','badab401dc3ef08873a0a9a33fc6d61b22db8bc3b56d1dba276b4f215bd2487f')
provenance_paths=set()
for p,w in doc(RECEPTION/'PREPARATION_READ_INPUTS.json').items():
    pin(p,w)
    provenance_paths.add(p)
for n in ('inspect_production.py','inspect_saved_output.py','REUSE_SCOPE.md','PRODUCTION_ADAPTER_DIFF_NATIVE.json',
          'BUILD_REUSE_NATIVE01.json','BUILD_REUSE_STDOUT01.raw','PREPARATION_RESULT.json',
          'PREPARATION_READ_INPUTS.json','PREPARATION_NATIVE01.json','PREPARATION_RECEPTION.md','RECEIVER_STATIC_NATIVE01.json'):
    provenance_paths.add(str(RECEPTION/n))
for p in (QA/'p211_a_initial_binding/prepare_binding.py',QA/'p211_a_root_reception/inspect_production.py',
          QA/'p211_runtime_root_reception/RECEPTION.md',PREP/'MANIFEST.sha256',
          QA/'p211_runtime_independent_audit/MANIFEST.sha256',
          ROOT/'docs/papers211_215_sequence/P211_REVIEW_CONTRACT.md',Path(__file__).resolve()):
    provenance_paths.add(str(p))
provenance=[{'path':p,**pin(p)} for p in sorted(provenance_paths)]
equalities=[{'path':[k],'value':v} for k,v in (
    ('schema','p211-b-complete-path-certificate-v1'),('role','P211_REVIEW_B'),('parameters',parameters),
    ('carrier_count',7),('total_states',2353),('total_targets',2353),('total_edges',2353),
    ('hand_attack_checks',3),('status','FINITE_COMPLETE_PATH_CHECKS_PASS'),
    ('scope','original n=1..7 counterexample pressure; not all-n proof or manuscript acceptance'))]
lengths=[{'path':['carriers'],'value':7},{'path':['check_counts'],'value':12},{'path':['hand_boundary_attacks'],'value':3}]
for i,n in enumerate(parameters['n_values']):
    size=math.comb(2*n-1,n)
    height=0 if n==1 else (n+1)//2
    for k,v in (('n',n),('state_count',size),('height',height),('height_formula',height),('inverse_mass',size),('kernel_first_mass',size)):
        equalities.append({'path':['carriers',i,k],'value':v})
    for k,v in (('records',size),('successor_table',size),('composition_tables',height+2),
                ('first_fixed_epochs',size),('terminal_table',size),('fixed_ids',2**(n-1)),
                ('recurrent_ids',2**(n-1)),('check_counts',12)):
        lengths.append({'path':['carriers',i,k],'value':v})
binding={'format':'p211-runtime-binding-v1','approved':True,'purpose':'P211_MANUSCRIPT',
    'role':'B','mode':'initial','attempt':str(ATTEMPT),'reviewed_static_source_import_closure':True,
    'reviewed_schema_and_parameters':True,'declared_imports':['itertools','json','math','sys'],'local_helper_imports':[],
    'adapter_sources':adapter,'runtime_lock':{'path':str(lock_path),**lock_pin},'entry':'verify.py','parameters':'parameters.json',
    'capsule_files':[{'name':'verify.py','path':str(REVIEW/'verify.py'),**source},
                     {'name':'parameters.json','path':str(REVIEW/'parameters.json'),**params_pin}],
    'argv_template':['$ENTRY','--parameters','$PARAMETERS'],'parameter_locator':'explicit_absolute_argv',
    'canonical':{'path':str(REVIEW/'CANONICAL.json'),'sha256':None,'bytes':None},
    'schema':{'top_keys':['schema','role','parameters','carrier_count','carriers','total_states','total_targets','total_edges',
                          'check_counts','carrier_check_total','hand_attack_checks','hand_boundary_attacks','check_total','status','scope'],
              'equalities':equalities,'lengths':lengths},'success_stderr':'empty','timeouts':{'science':300,'native':60,'envelope':900},
    'provenance_inputs':provenance,
    'root_execution_interface':'pinned compile/exec within fresh adapter child, explicit main/file/argv/capsule cwd, not direct python verify.py',
    'root_canonical_policy':'No adoption before full recorded-output and closed-attempt reception; then exclusive raw copy and native comparison.',
    'root_math_boundary':'Independent B weak compositions, complete composition tables, boundary lifetimes and kernel-first inverse; original seven carriers, no source import during preparation.',
    'root_infrastructure_reuse':'Accepted unchanged runtime supports B; disclosed A binding/record-inspector mechanics, separate B-specific full saved-output receiver; not a new independent infrastructure review.'}
for p,d in READS.items(): assert Path(p).read_bytes()==d
write('INPUTS_AT_BINDING.json',{p:pin(p) for p in list(READS)})
write('BINDING.json',binding)
result={'status':'ROOT_B_INITIAL_BINDING_READY_NOT_EXECUTED','binding':{'path':str(OUT/'BINDING.json'),**pin(OUT/'BINDING.json')},
        'attempt':str(ATTEMPT),'input_file_keys':len(READS),'runtime_keys_checked':122,
        'schema_equalities':len(equalities),'schema_lengths':len(lengths),'scientific_source_invocations':0,
        'canonical_absent':not os.path.lexists(REVIEW/'CANONICAL.json')}
write('RESULT.json',result)
print(json.dumps(result,sort_keys=True))
