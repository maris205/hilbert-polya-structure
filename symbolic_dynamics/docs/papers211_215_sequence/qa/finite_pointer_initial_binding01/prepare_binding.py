"""Root exact single pointer pilot binding; source bytes only, no science.

Binding/pin/state mechanics are disclosed reuse of earlier root bindings.
The submitted producer is neither compiled nor imported by this helper.
"""
from hashlib import sha256
import json
import os
from pathlib import Path

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
QA = ROOT/'docs/papers211_215_sequence/qa'
OUT = QA/'finite_pointer_initial_binding01'
SCIENCE = ROOT/'docs/papers211_215_sequence/scouting/finite_pointer_pilot_preparation01'
PREP = QA/'finite_pointer_runtime_preparation01'
OLD = QA/'p211_runtime_preparation'
ATTEMPT = QA/'root_replays/finite_pointer_initial01'
READS = {}
CHECKS = 0

def need(ok,label):
    global CHECKS
    CHECKS += 1
    if not ok: raise AssertionError(label)

def raw(p):
    p=Path(p); b=p.read_bytes()
    v={'bytes':len(b),'sha256':sha256(b).hexdigest(),'resolved':str(p.resolve(strict=True)),
       'symlink':os.readlink(p) if p.is_symlink() else None}
    need(str(p) not in READS or READS[str(p)]==v,('unchanged whole input',str(p)))
    READS[str(p)]=v
    return b

def pin(p,expected=None):
    p=Path(p); raw(p); value=READS[str(p)]
    if expected is not None:
        need(all(value[k]==v for k,v in expected.items()),('complete exact pin',str(p)))
    return value

def doc(p): return json.loads(raw(p))

def state(p,with_bytes=True):
    p=Path(p)
    row={'lexists':os.path.lexists(p),'exists':p.exists(),'is_file':p.is_file(),
         'is_dir':p.is_dir(),'is_character_device':p.is_char_device(),'resolved':str(p.resolve()),
         'symlink':os.readlink(p) if p.is_symlink() else None}
    if p.is_char_device():
        s=p.stat();row['character_device']={'major':os.major(s.st_rdev),'minor':os.minor(s.st_rdev),'mode':s.st_mode}
    if with_bytes and p.is_file():
        v=pin(p);row.update({k:v[k] for k in ('bytes','sha256')})
    return row

def seal(base,count,digest):
    pin(base/'MANIFEST.sha256',{'sha256':digest})
    names=set()
    for line in raw(base/'MANIFEST.sha256').decode().splitlines():
        h,n=line.split('  ',1)
        need(n not in names and not Path(n).is_absolute() and '..' not in Path(n).parts and n!='MANIFEST.sha256','exact nonself seal')
        pin(base/n,{'sha256':h});names.add(n)
    need(len(names)==count and names|{'MANIFEST.sha256'}=={p.relative_to(base).as_posix() for p in base.rglob('*') if p.is_file()},'whole sealed source preparation')

def write(n,v):
    with (OUT/n).open('xb') as f:f.write((json.dumps(v,sort_keys=True,indent=2,allow_nan=False)+'\n').encode())

need(Path.cwd()==ROOT and Path(__file__).resolve()==OUT/'prepare_binding.py','literal root-owned binding helper')
need(not os.path.lexists(ATTEMPT) and ATTEMPT.parent.resolve(strict=True)==ATTEMPT.parent,'new physical sole pilot attempt')
need(not os.path.lexists(OUT/'BINDING.json') and not os.path.lexists(OUT/'UNADOPTED_CANONICAL.json'),'new binding and absent unadopted target')
source=pin(SCIENCE/'pointer_pilot.py',{'bytes':27518,'sha256':'9b3c22ad86b36f5dece45d47de03d3cc309f05c46c40a152aec49dc8a0262cbb'})
params=pin(SCIENCE/'PARAMETERS.json',{'bytes':415,'sha256':'f71aff49cb7b4fda75851992a85ce3150cd8f69f1dd5a4512bb6e7b3afe08a16'})
parameters=doc(SCIENCE/'PARAMETERS.json')
need(parameters=={'schema_version':'finite-pointer-parameters-v1','role':'single-bounded-author-pilot','label_convention':'one_based',
     'state_order':'lexicographic_(u,v,f(1),...,f(n))','boxes':[{'n':1,'state_count':1},{'n':2,'state_count':16},{'n':3,'state_count':243},{'n':4,'state_count':4096}],
     'box_count':4,'total_state_count':4356,'allow_box_extension':False},'unchanged original four-box parameter contract')
seal(SCIENCE,7,'828b135ed4aefbb9d0a1f030e52b48c45c32288ff05d6ea413946bcbcf104a75')
seal(PREP,64,'bb71a0b54f367f3c1116263081f06f37817677ed334788c1b1950227ba1f07f7')
for keyfile,count in [(QA/'pointer_pilot_source_root/INPUTS.json',21),(QA/'pointer_runtime_root/run02/READ_INPUTS.json',198)]:
    key=doc(keyfile);need(len(key)==count,'entire accepted source/runtime reception key')
    for p,v in key.items():pin(p,v)
lock_path=PREP/'discovery02/RUNTIME_LOCK.json'
lock_pin=pin(lock_path,{'bytes':146209,'sha256':'e2fd2189f639feff28a8ae499da011e9ea6e9cadf3eb99b60944f3209fdebd02'})
lock=doc(lock_path);need(len(lock['files'])==129,'complete accepted 129 runtime files')
for p,v in lock['files'].items():pin(p,v)
for p,v in lock['configuration']['paths'].items():need(state(p)==v,('current exact runtime configuration',p))
for p,v in lock['configuration']['memberships'].items():
    directory=Path(p);actual={'directory':state(p,False),'members':{}}
    if directory.is_dir():actual['members']={q.name:state(q,False) for q in sorted(directory.iterdir())}
    need(actual==v,('whole current configuration membership',p))
for p,v in lock['loader_search_directory_states'].items():need(state(p,False)==v,('current loader directory',p))
adapter={str(p):pin(p,{'sha256':h}) for p,h in (
    (PREP/'pointer_runtime.py','89bec42ec8ae827156ac32cd0c8213faef06387930152bee6b1be3a37e4e92bf'),
    (OLD/'p211_runtime.py','bff2dcf25ee846b04eac0bbd46eb7b3e58c728c6d7e8e9ce591c9cef1ae4e421'),
    (OLD/'runtime_core.py','2fd41cfac779f8d5f4e23089fcc9f2b6b041cbebe19e7003b2db6b4815909934'))}
for base in (QA/'pointer_pilot_source_root',QA/'pointer_runtime_root'):
    for p in sorted(base.rglob('*')):
        need(not p.is_symlink() and (p.is_dir() or p.is_file()),'ordinary root acceptance tree')
        if p.is_file():pin(p)
pin(Path(__file__));pin(OUT/'AUTHORIZATION.md')
equalities=[{'path':['schema_version'],'value':'finite-pointer-pilot-output-v1'},
            {'path':['role'],'value':'bounded-author-evidence-not-admission'},
            {'path':['parameters'],'value':parameters},
            {'path':['coefficient_arithmetic'],'value':'fractions.Fraction; t-degree <= 4; q-degree uncapped'},
            {'path':['summary','failed_count'],'value':0},{'path':['summary','failed_ids'],'value':[]},
            {'path':['summary','status'],'value':'PASS'}]
lengths=[{'path':['boxes'],'value':4}]
for i,(n,size) in enumerate(((1,1),(2,16),(3,243),(4,4096))):
    equalities.extend({'path':['boxes',i,k],'value':v} for k,v in (('n',n),('declared_state_count',size),('state_count',size)))
    lengths.extend({'path':['boxes',i,k],'value':size} for k in ('states','edges'))
binding=doc(PREP/'BINDING.pending.json')
binding.update({'approved':True,'run_authorized':True,'attempt':str(ATTEMPT),'execution_root':str(ATTEMPT.parent),
    'reviewed_static_source_import_closure':True,'reviewed_schema_and_parameters':True,
    'reviewed_full_runtime_source_lock_and_probe_records':True,'adapter_sources':adapter,
    'runtime_lock':{'path':str(lock_path),**lock_pin},
    'capsule_files':[{'name':'pointer_pilot.py','path':str(SCIENCE/'pointer_pilot.py'),**source},
                     {'name':'PARAMETERS.json','path':str(SCIENCE/'PARAMETERS.json'),**params}],
    'canonical':{'path':str(OUT/'UNADOPTED_CANONICAL.json'),'sha256':None,'bytes':None},
    'schema':{'top_keys':['schema_version','role','parameters','coefficient_arithmetic','core_series','boxes','checks','summary'],
              'equalities':equalities,'lengths':lengths},
    'timeouts':{'science':300,'native':60,'envelope':900},'pending':[],
    'root_authorization':{'issuer':'/root','record':str(OUT/'AUTHORIZATION.md'),'record_pin':pin(OUT/'AUTHORIZATION.md')},
    'root_execution_interface':'pinned compile/exec in a fresh guard child; explicit __name__/__file__/two positional argv/capsule cwd, not direct script startup',
    'root_boundary':'Exactly one initial 4356-state author pilot, no canonical adoption, pair, retry, larger box or admission. Whole saved-output semantics and same-reviewer E1 remain subsequent obligations.'})
for p,v in dict(READS).items():pin(p,v)
binding['provenance_inputs']=[{'path':p,**v} for p,v in sorted(READS.items())]
write('INPUTS_AT_BINDING.json',READS)
write('BINDING.json',binding)
bp=pin(OUT/'BINDING.json')
result={'status':'ROOT_EXACT_POINTER_INITIAL_BINDING_READY_NOT_EXECUTED','binding':{'path':str(OUT/'BINDING.json'),**bp},
        'attempt':str(ATTEMPT),'runtime_files':129,'input_keys':len(READS),'schema_equalities':len(equalities),'schema_lengths':len(lengths),
        'scientific_executions':0,'canonical_absent':not os.path.lexists(OUT/'UNADOPTED_CANONICAL.json')}
write('RESULT.json',result)
print(json.dumps(result,sort_keys=True))
