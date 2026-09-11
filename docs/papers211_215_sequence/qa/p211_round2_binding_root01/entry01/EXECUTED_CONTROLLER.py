"""Root one-shot physical Round2 placement/capture; no science or retry.

Disclosed scoped adaptation of the fully read accepted R1 invoke02.py.
The new attempt dictionary exactly matches the new received R2 contract;
actual start/end timestamps belong in native records, not that dictionary.
Unknown launch outcome remains unknown; no successful seal on failed child.
The encompassing product tool return is retained separately after this exits.
"""
from hashlib import sha256
import json
import os
from pathlib import Path
import subprocess
import sys
import time

ROOT=Path('/root/autodl-tmp/symbolic_dynamics')
QA=ROOT/'docs/papers211_215_sequence/qa'
HERE=QA/'p211_round2_binding_root01'
CONTROL=HERE/'entry01'
EXEC=QA/'p211_round2_execution01'
SOURCE=QA/'p211_round2_preparation01/freeze.py'
BINDING=HERE/'enabled01/BINDING.json'
FROZEN=ROOT/'papers/211-kernel-image-projection-feedback/frozen_round2'
ENV={'PATH':'/usr/bin:/bin','LANG':'C.UTF-8','LC_ALL':'C.UTF-8','TZ':'UTC'}
SOURCE_PIN={'bytes':38416,'sha256':'a333faaf97653f9c8eae008b31389599727bcee446abe2ea80bf379d2fb44a01'}
EMPTIES={
 'docs/papers211_215_sequence/qa/root_replays/p211_a_initial_01':['child01/commands'],
 'docs/papers211_215_sequence/qa/root_replays/p211_a_pair_01':['child01/commands','child02/commands'],
 'docs/papers211_215_sequence/qa/p211_runtime_preparation':['discovery01/empty_probe_capsule','discovery02/empty_probe_capsule','tests01/existing_cache','tests02/existing_cache','tests02/fixture_initial/child01/commands','tests02/fixture_pair/child01/commands','tests02/fixture_pair/child02/commands'],
 'docs/papers211_215_sequence/qa/root_replays/p211_b_initial_01':['child01/commands'],
 'docs/papers211_215_sequence/qa/root_replays/p211_b_pair_01':['child01/commands','child02/commands']}

def need(ok,label):
    if not ok: raise AssertionError(label)

def pin(raw):
    return {'bytes':len(raw),'sha256':sha256(raw).hexdigest()}

def put(path,value):
    raw=value if isinstance(value,bytes) else (json.dumps(value,sort_keys=True,indent=2)+'\n').encode()
    with path.open('xb') as stream: stream.write(raw)

def run(label,argv,target,timeout=60,empty=True):
    request={'argv':argv,'cwd':str(ROOT),'environment':ENV,'stdin':'subprocess.DEVNULL','timeout_seconds':timeout,'started_epoch':time.time()}
    put(target/(label+'.ATTEMPT.json'),request)
    code,error,state=None,None,'captured'
    try:
        r=subprocess.run(argv,cwd=ROOT,env=ENV,stdin=subprocess.DEVNULL,capture_output=True,timeout=timeout)
        stdout,stderr,code=r.stdout,r.stderr,r.returncode
    except subprocess.TimeoutExpired as exc:
        stdout,stderr=exc.stdout or b'',exc.stderr or b''
        error={'type':type(exc).__name__,'message':str(exc)}
        state='captured_partial_at_timeout; no exit code invented'
    except OSError as exc:
        stdout,stderr=b'',b''
        error={'type':type(exc).__name__,'message':str(exc)}
        state='unknown_launch_outcome_without_native_handle; streams unavailable'
    put(target/(label+'.stdout.raw'),stdout);put(target/(label+'.stderr.raw'),stderr)
    native={**request,'ended_epoch':time.time(),'native_exit_code':code,'exception':error,'stream_capture_status':state,
            'stdout':{'path':label+'.stdout.raw',**pin(stdout)},'stderr':{'path':label+'.stderr.raw',**pin(stderr)}}
    put(target/(label+'.NATIVE.json'),native)
    need(error is None and code==0 and not stderr and (not empty or not stdout),('actual native operation',label))
    return stdout,native

need(len(sys.argv)==2 and len(sys.argv[1])==64,'exact independently supplied binding digest')
need(Path.cwd()==ROOT and dict(os.environ)==ENV and sys.flags.isolated==1 and sys.flags.no_site==1 and sys.flags.dont_write_bytecode==1,'exact controller interface ENV4')
need(not any(os.path.lexists(p) for p in (CONTROL,EXEC,FROZEN,FROZEN.parent/'qa_final')),'new exact control/execution/frozen outputs')
for p in (SOURCE,BINDING):
    need(p.is_file() and not p.is_symlink() and p.resolve()==p,'ordinary accepted source/binding')
raw=BINDING.read_bytes();binding_pin=pin(raw)
need(binding_pin['sha256']==sys.argv[1] and pin(SOURCE.read_bytes())==SOURCE_PIN,'exact source and independent actual binding digest')
binding=json.loads(raw)
need(binding['schema']=='p211-round2-root-binding-v1' and binding['enabled'] is True and binding['root_authorization']['issuer']=='/root' and binding['root_authorization']['decision']=='AUTHORIZE_PHYSICAL_P211_ROUND2_FROM_ACCEPTED_FINAL_B','separate actual physical authority')
need(binding['execution_source_pin']==SOURCE_PIN and binding['execution_directory']==str(EXEC.relative_to(ROOT)),'literal bound source and destination')
for row in binding['external_inputs']:
    p=ROOT/row['physical_path']
    need(p.is_file() and not p.is_symlink() and p.resolve()==p and pin(p.read_bytes())==row['pin'],('entire external pre-entry key',str(p)))
for t in binding['external_trees']:
    base=ROOT/t['root'];files,dirs=set(),{'.'}
    for p in base.rglob('*'):
        need(p.resolve()==p and not p.is_symlink() and (p.is_dir() or p.is_file()),'ordinary complete selected tree')
        (dirs if p.is_dir() else files).add(p.relative_to(base).as_posix())
    need(t['empty_directories']==EMPTIES.get(t['root'],[]),'exact per-root historical empty list')
    parents={'.'}|set(t['empty_directories'])
    for n in t['files']+t['empty_directories']: parents.update(p.as_posix() for p in Path(n).parents)
    need(files==set(t['files']) and dirs==parents,('entire exact pre-entry tree',t['root']))
    for n in t['empty_directories']: need(not any((base/n).iterdir()),'actually empty named directory')
CONTROL.mkdir();put(CONTROL/'EXECUTED_CONTROLLER.py',Path(__file__).read_bytes())
put(CONTROL/'INPUT_PINS.json',{'source':SOURCE_PIN,'binding':binding_pin,'controller':pin(Path(__file__).read_bytes())})
EXEC.mkdir()
for label,source,destination in [('source',SOURCE,EXEC/'freeze.py'),('binding',BINDING,EXEC/'BINDING.json')]:
    run('copy_'+label,['/usr/bin/cp','-p','--',str(source),str(destination)],CONTROL)
    run('compare_'+label,['/usr/bin/cmp','--',str(source),str(destination)],CONTROL)
    need(source.read_bytes()==destination.read_bytes(),'actual full source/binding placement bytes')
argv=['/usr/bin/python3.10','-I','-S','-B',str(EXEC/'freeze.py'),'--binding',str(EXEC/'BINDING.json')]
attempt={'argv':argv,'cwd':str(ROOT),'environment':ENV,'stdin':'subprocess.DEVNULL','source_pin':SOURCE_PIN,'binding_pin':binding_pin}
put(EXEC/'ROOT_INVOCATION_ATTEMPT.json',attempt)
stdout,native=run('ROOT_INVOCATION',argv,CONTROL,timeout=900,empty=False)
need(json.loads(stdout)==json.loads((EXEC/'RESULT.json').read_bytes()),'whole actual recorder stdout/result equality')
need(json.loads(stdout)['status']=='PHYSICAL_P211_ROUND2_CREATED_PENDING_ROOT_RECEPTION','actual pending-root success only')
# No execution self-seal yet: the actual encompassing product return and full
# root postchecks must first be retained. This follows the new R2 contract.
summary={'status':'ACTUAL_PHYSICAL_ROUND2_PENDING_ROOT_RECEPTION','native_exit_code':native['native_exit_code'],
         'root_placement_commands':4,'recorder_native_commands':json.loads(stdout)['native_commands'],
         'actual_recorder_stdout':pin(stdout),'source_pin':SOURCE_PIN,'binding_pin':binding_pin,
         'execution_seal':'PENDING_ENCOMPASSING_PRODUCT_RETURN','postcopy_full_host_settings':'PENDING',
         'science_runs':0,'paper_complete':False}
put(CONTROL/'RESULT.json',summary);print(json.dumps(summary,sort_keys=True))
