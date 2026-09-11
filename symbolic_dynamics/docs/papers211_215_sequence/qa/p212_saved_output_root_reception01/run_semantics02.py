"""Root owns one saved-output receiver native process, never a producer.

Forward adaptation of the accepted P212 root initial capture controller.
The unchanged accepted runtime core retains full native streams/settlement.
"""
from hashlib import sha256
import json
import os
from pathlib import Path
import sys
import traceback
import types

ROOT=Path('/root/autodl-tmp/symbolic_dynamics')
QA=ROOT/'docs/papers211_215_sequence/qa'
OWN=QA/'p212_saved_output_root_reception01'
ATTEMPT=OWN/'initial02'
CORE=QA/'p212_runtime_preparation01/runtime_core.py'
ENV={'PATH':'/usr/bin:/bin','LANG':'C.UTF-8','LC_ALL':'C.UTF-8','TZ':'UTC'}

def need(ok,s):
    if not ok: raise AssertionError(s)

def value(raw):
    return {'bytes':len(raw),'sha256':sha256(raw).hexdigest()}

def physical(p):
    p=Path(p)
    need(p.is_file() and not p.is_symlink() and p.resolve(strict=True)==p,'physical source byte input')
    return p.read_bytes()

need(len(sys.argv)==3 and Path.cwd()==ROOT and dict(os.environ)==ENV,'exact root controller argv/cwd/ENV4')
binding_path=Path(sys.argv[1]);need(binding_path==OWN/'RUNTIME_BINDING02.json','exact runtime binding')
raw=physical(binding_path);need(sha256(raw).hexdigest()==sys.argv[2],'actual runtime binding digest')
b=json.loads(raw)
need(b['approved'] is True and b['role']=='P212_INITIAL_SAVED_OUTPUT_RECEPTION','one actual saved-output authority')
need(b['authority']=='AUTHORIZE_ONE_SAVED_OUTPUT_RECONSTRUCTION_NO_PRODUCER_NO_ADOPTION','literal root authority')
need(b['attempt']==str(ATTEMPT) and b['capture']==str(ATTEMPT/'node_capture'),'exact fresh output roles')
need(not os.path.lexists(ATTEMPT),'exclusive fresh runtime attempt')
for n in ('CANONICAL.json','canonical.stdout.json'):
    need(not os.path.lexists(ROOT/'papers/212-closed-pointer-orbits'/n),'unadopted canonical names')
controller=physical(OWN/'run_semantics02.py')
need(value(controller)=={k:b['input_pins'][str(OWN/'run_semantics02.py')][k] for k in ('bytes','sha256')},'exact controller self pin')
core_raw=physical(CORE);need(value(core_raw)=={k:b['input_pins'][str(CORE)][k] for k in ('bytes','sha256')},'exact accepted capture core')
core=types.ModuleType('_p212_saved_output_root_core');core.__file__=str(CORE);sys.modules[core.__name__]=core
exec(compile(core_raw,str(CORE),'exec'),core.__dict__)
need(core.ENV==ENV,'unchanged accepted native core settings')
node_lock=json.loads(physical(b['node_lock']['path']))
paths={**b['controlled_python_files'],**node_lock['files'],**b['input_pins']}
paths[str(binding_path)]=core.rich(binding_path)
before={p:core.rich(p) for p in paths}
need(before==paths,'all loader/runtime/source inputs pinned before child launch')
need(core.value(b['node_lock']['path'])==b['node_lock']['pin'],'whole actual Node lock')
ATTEMPT.mkdir(mode=0o700);(ATTEMPT/'commands').mkdir()
core.OUT,core.COMMANDS,core.UNFINALIZED_NATIVE=ATTEMPT,[],[]
core.write_bytes(ATTEMPT/'EXECUTED_CONTROLLER.py',controller)
core.write_bytes(ATTEMPT/'RUNTIME_BINDING_ORIGINAL.json',raw)
core.write_json(ATTEMPT/'INPUTS_BEFORE.json',before)
errors=[];receipt=None
try:
    core.command('01_ldd_before',['/usr/bin/ldd','/usr/bin/node'],timeout=60,cwd=ROOT)
    argv=['/usr/bin/env','-i',*[k+'='+v for k,v in ENV.items()],'/usr/bin/node','--require',b['preload'],b['receiver'],'--binding',b['binding']]
    stdout=core.command('02_saved_output',argv,timeout=300,cwd=ROOT)
    receipt=json.loads(stdout)
    need(receipt['status']=='COMPLETE_SAVED_OUTPUT_SEMANTICS_CHECKED','actual complete semantic result')
    need(receipt['scientific_producer_invocations']==receipt['submitted_code_imports']==receipt['canonical_accesses']==receipt['filesystem_writes']==0,'saved-only receiver boundary')
    runtime=json.loads((ATTEMPT/'node_capture/RESULT.json').read_bytes())
    need(runtime['status']=='PASS_BOUNDED_NODE_RECEIVER_RUNTIME' and runtime['errors']==[],'actual preloaded Node closure')
except BaseException as e:
    errors.append({'type':type(e).__name__,'error':repr(e),'traceback':traceback.format_exc()})
try:
    core.command('03_ldd_after',['/usr/bin/ldd','/usr/bin/node'],timeout=60,cwd=ROOT)
    after={p:core.rich(p) for p in paths};core.write_json(ATTEMPT/'INPUTS_AFTER.json',after)
    need(after==before,'complete root runtime/source key unchanged')
    for n in ('CANONICAL.json','canonical.stdout.json'):
        need(not os.path.lexists(ROOT/'papers/212-closed-pointer-orbits'/n),'canonical roles remain absent')
except BaseException as e:
    errors.append({'stage':'closing','type':type(e).__name__,'error':repr(e)})
result={'status':'FAIL_PRESERVED' if errors else 'CAPTURED_COMPLETE_SAVED_OUTPUT_SEMANTICS_PENDING_ROOT_RECEPTION',
    'errors':errors,'commands':core.COMMANDS,'receiver_receipt':receipt,'attempt':str(ATTEMPT),
    'scientific_producer_invocations':0,'canonical_adopted':False,'independent_manuscript_review':False,
    'scope':'Actual author-side saved-output reconstruction in one separately bound Node process. Native core explicitly reused; not another producer or strict pair.'}
core.write_json(ATTEMPT/'RESULT.json',result)
seal=core.seal() if not core.UNFINALIZED_NATIVE else None
print(json.dumps({'status':result['status'],'errors':errors,'attempt':str(ATTEMPT),'seal':seal,'native_commands':len(core.COMMANDS),
                  'scientific_producer_invocations':0,'canonical_adopted':False},sort_keys=True),flush=True)
sys.exit(1 if errors else 0)
