"""One root-owned import-only discovery capture using the accepted core.

No scientific file is read or imported. Exact fresh root authority must
precede this controller; the accepted core's command/settlement/unknown
outcome limits are unchanged and explicitly reused. This is not a new
independent infrastructure implementation or a scientific invocation.
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
HERE=QA/'p212_import_discovery_root01'
PREP=QA/'p212_runtime_preparation01'
ENTRY=HERE/'entry01'
ENV={'PATH':'/usr/bin:/bin','LANG':'C.UTF-8','LC_ALL':'C.UTF-8','TZ':'UTC'}

def need(ok,label):
    if not ok: raise AssertionError(label)

def ordinary(p):
    p=Path(p)
    need(p.is_absolute() and p.resolve(strict=True)==p and p.is_file() and not p.is_symlink() and p.stat().st_nlink==1,'exact_ordinary_input:'+str(p))
    return p.read_bytes()

def pin(p,k):
    b=ordinary(p)
    need(len(b)==k['bytes'] and sha256(b).hexdigest()==k['sha256'],'exact_input_pin:'+str(p))
    return b

need(len(sys.argv)==3 and Path.cwd()==ROOT and dict(os.environ)==ENV,'exact_root_controller_argv_cwd_ENV4')
approval_path=Path(sys.argv[1])
need(approval_path==HERE/'APPROVAL.json','literal_root_approval_path')
raw=ordinary(approval_path)
need(sha256(raw).hexdigest()==sys.argv[2],'actual_root_approval_digest')
approval=json.loads(raw)
need(approval['approved'] is True and approval['scope']=='IMPORT_ONLY_NO_SCIENTIFIC_SOURCE_READ' and approval['reviewed_all_preparation_sources'] is True,'actual_import_only_authority')
need(approval['root_authority_decision']=='AUTHORIZE_ONE_P212_IMPORT_ONLY_DISCOVERY_NO_SCIENCE','exact_root_decision')
capture=approval['root_capture']
need(capture['entry']==str(ENTRY) and capture['timeout_seconds']==300 and capture['environment']==ENV,'literal_capture_deadline_and_environment')
need(capture['controller']['path']==str(HERE/'run.py'),'literal_controller_source')
controller_raw=pin(HERE/'run.py',capture['controller'])
need(set(approval['source_inputs'])=={str(PREP/n) for n in ('runtime_core.py','p212_runtime.py','prepare_runtime.py')},'exact_three_accepted_runtime_sources')
source_bytes={p:pin(p,k) for p,k in approval['source_inputs'].items()}
for p,k in approval['lineage_inputs'].items(): pin(p,k)
for k in approval['provenance_inputs']:
    need(not Path(k['path']).is_relative_to(ROOT/'papers') and Path(k['path']).suffix in ('.md','.json','.sha256'),'documentary_authority_not_scientific_file')
    pin(k['path'],k)
discovery=Path(approval['output'])
need(discovery==QA/'p212_runtime_discovery01' and not os.path.lexists(discovery) and not os.path.lexists(ENTRY),'fresh_exact_import_and_capture_outputs')
argv=['/usr/bin/python3.10','-I','-S','-B','-X','pycache_prefix='+str(discovery/'never_created_preparer_cache'),str(PREP/'prepare_runtime.py'),str(approval_path),sys.argv[2]]
need(capture['child_argv_without_approval_digest']==argv[:-1],'exact_external_startup_interface')
# Only now bootstrap the exact accepted infrastructure core, never science.
core=types.ModuleType('_p212_root_import_capture_core')
core.__file__=str(PREP/'runtime_core.py')
sys.modules[core.__name__]=core
exec(compile(source_bytes[core.__file__],core.__file__,'exec'),core.__dict__)
need(core.ENV==ENV,'unchanged_core_ENV4')
ENTRY.mkdir(mode=0o700)
(ENTRY/'commands').mkdir()
core.OUT,core.COMMANDS,core.UNFINALIZED_NATIVE=ENTRY,[],[]
core.write_bytes(ENTRY/'EXECUTED_CONTROLLER.py',controller_raw)
core.write_bytes(ENTRY/'APPROVAL_ORIGINAL.json',raw)
inputs=[str(HERE/'run.py'),str(approval_path),*approval['source_inputs'],*approval['lineage_inputs'],*[k['path'] for k in approval['provenance_inputs']]]
need(len(inputs)==len(set(inputs)),'unique_root_capture_inputs')
before={p:core.rich(p) for p in inputs}
core.write_json(ENTRY/'INPUTS_BEFORE.json',before)
errors=[]
stdout=None
try:
    stdout=core.command('IMPORT_ONLY_DISCOVERY',['/usr/bin/env','-i',*[k+'='+v for k,v in ENV.items()],*argv],timeout=300,cwd=ROOT)
    returned=json.loads(stdout)
    need(returned['status']=='PASS_PREPARATION_ONLY' and returned['errors']==[] and returned['output']==str(discovery),'actual_import_only_preparer_complete_success')
    actual=json.loads((discovery/'RESULT.json').read_bytes())
    need(actual['status']=='PASS_PREPARATION_ONLY' and actual['scientific_executions']==0 and actual['science_sources_read_or_imported']==[],'actual_discovery_no_scientific_action')
    need(len(actual['commands'])==12,'exact_twelve_preparer_commands')
except BaseException as exc:
    errors.append({'type':type(exc).__name__,'error':repr(exc),'traceback':traceback.format_exc()})
try:
    after={p:core.rich(p) for p in inputs}
    core.write_json(ENTRY/'INPUTS_AFTER.json',after)
    need(after==before,'entire_root_source_authority_before_after_key')
except BaseException as exc:
    errors.append({'stage':'root_input_closure','type':type(exc).__name__,'error':repr(exc)})
result={'status':'FAIL_PRESERVED' if errors else 'CAPTURED_IMPORT_DISCOVERY_PENDING_ROOT_COMPLETE_RECEPTION',
        'errors':errors,'commands':core.COMMANDS,'scientific_executions':0,
        'runtime_lock_accepted':False,'canonical_created':False,
        'limits':'Actual root outer capture and import preparation only. No scientific source read/import or semantic acceptance. Full discovery/native/dependency reception still required. Inherited core settlement/unknown outcome limits unchanged.'}
core.write_json(ENTRY/'RESULT.json',result)
seal=core.seal() if not core.UNFINALIZED_NATIVE else None
print(json.dumps({'status':result['status'],'errors':errors,'entry':str(ENTRY),'seal':seal,'root_native_commands':len(core.COMMANDS),'scientific_executions':0},sort_keys=True),flush=True)
sys.exit(1 if errors else 0)
