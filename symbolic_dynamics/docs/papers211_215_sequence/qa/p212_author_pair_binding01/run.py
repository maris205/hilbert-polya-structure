"""Author SOURCE_ONLY proposal: root capture of one separately bound P212 pair.

The native/settlement core is explicitly reused from the accepted P212
infrastructure. This controller never executes a scientific source itself.
Scientific execution occurs only in the root-bound adapter child.
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
HERE=QA/'p212_author_pair_binding01'
PREP=QA/'p212_runtime_preparation01'
ENTRY=HERE/'entry01'
ATTEMPT=QA/'root_replays/p212_author_pair_01'
PAPER=ROOT/'papers/212-closed-pointer-orbits'
ENV={'PATH':'/usr/bin:/bin','LANG':'C.UTF-8','LC_ALL':'C.UTF-8','TZ':'UTC'}

def need(ok,label):
    if not ok: raise AssertionError(label)

def ordinary(p):
    p=Path(p)
    need(p.is_absolute() and p.resolve(strict=True)==p and p.is_file() and not p.is_symlink(),'physical_bound_input:'+str(p))
    return p.read_bytes()

def pin(p,k):
    raw=ordinary(p)
    need(len(raw)==k['bytes'] and sha256(raw).hexdigest()==k['sha256'],'exact_bound_bytes:'+str(p))
    return raw

need(len(sys.argv)==3 and Path.cwd()==ROOT and dict(os.environ)==ENV,'actual_root_controller_interface_ENV4')
binding_path=Path(sys.argv[1])
need(binding_path==HERE/'BINDING.json','exact_binding_path')
raw=ordinary(binding_path)
need(sha256(raw).hexdigest()==sys.argv[2],'actual_binding_digest')
binding=json.loads(raw)
need(binding['approved'] is True and binding['mode']=='pair' and binding['role']=='author','sole_approved_pair_role')
need(binding['root_authority_decision']=='AUTHORIZE_ONE_P212_AUTHOR_STRICT_PAIR_NO_ADOPTION','actual_root_authority')
need(binding['attempt']==str(ATTEMPT) and binding['purpose']=='P212_AUTHOR_MANUSCRIPT','exact_attempt_role')
capture=binding['root_capture']
need(capture['entry']==str(ENTRY) and capture['environment']==ENV and capture['timeout_seconds']==1200,'exact_outer_capture')
need(capture['controller']['path']==str(HERE/'run.py'),'bound_controller_source')
controller=pin(HERE/'run.py',capture['controller'])
need(set(binding['adapter_sources'])=={str(PREP/n) for n in ('runtime_core.py','p212_runtime.py')},'two_exact_adapter_sources')
source_bytes={p:pin(p,k) for p,k in binding['adapter_sources'].items()}
pin(binding['runtime_lock']['path'],binding['runtime_lock'])
for k in binding['capsule_files']+binding['provenance_inputs']: pin(k['path'],k)
need(not os.path.lexists(ENTRY) and not os.path.lexists(ATTEMPT),'fresh_capture_and_runtime_outputs')
need(binding['canonical']['path']==str(PAPER/'CANONICAL.json'),'fixed_accepted_canonical')
canonical=pin(PAPER/'CANONICAL.json',binding['canonical'])
need(not os.path.lexists(PAPER/'canonical.stdout.json'),'historical_canonical_alias_absent')
argv=['/usr/bin/python3.10','-I','-S','-B','-X','pycache_prefix='+str(ATTEMPT/'never_created_outer_cache'),str(PREP/'p212_runtime.py'),'outer',str(binding_path),sys.argv[2],str(ATTEMPT)]
need(capture['outer_argv_without_binding_digest']==argv[:9]+argv[10:],'exact_outer_startup_vector')
core=types.ModuleType('_p212_root_pair_capture_core')
core.__file__=str(PREP/'runtime_core.py')
sys.modules[core.__name__]=core
exec(compile(source_bytes[core.__file__],core.__file__,'exec'),core.__dict__)
need(core.ENV==ENV,'accepted_core_ENV4')
ENTRY.mkdir(mode=0o700)
(ENTRY/'commands').mkdir()
core.OUT,core.COMMANDS,core.UNFINALIZED_NATIVE=ENTRY,[],[]
core.write_bytes(ENTRY/'EXECUTED_CONTROLLER.py',controller)
core.write_bytes(ENTRY/'BINDING_ORIGINAL.json',raw)
paths=[str(HERE/'run.py'),str(binding_path),binding['runtime_lock']['path'],binding['canonical']['path'],*binding['adapter_sources'],*[k['path'] for k in binding['capsule_files']+binding['provenance_inputs']]]
paths=sorted(set(paths))
before={p:core.rich(p) for p in paths}
core.write_json(ENTRY/'INPUTS_BEFORE.json',before)
errors=[]
try:
    stdout=core.command('AUTHOR_PAIR',['/usr/bin/env','-i',*[k+'='+v for k,v in ENV.items()],*argv],timeout=1200,cwd=ROOT)
    returned=json.loads(stdout)
    need(returned['status']=='PASS' and returned['attempt']==str(ATTEMPT),'actual_outer_stage_complete_success')
    outer=json.loads((ATTEMPT/'outer/RESULT.json').read_bytes())
    need(outer['status']=='PASS' and outer['mode']=='pair' and outer['role']=='author','actual_outer_role')
    recorder=json.loads((ATTEMPT/'recorder/RESULT.json').read_bytes())
    need(recorder['status']=='PASS' and recorder['mode']=='pair' and recorder['role']=='author','actual_recorder_role')
    need([r['label'] for r in recorder['commands']]==['00_copy_0','00_copy_1','01_ldd_before','03_verify_01','03_verify_02','04_canonical_1','04_canonical_2','05_pair','06_ldd_after'],'actual_pair_command_census')
    need(recorder['output']['actual_raw_comparisons']==3 and [r['path'] for r in recorder['output']['raw_stdout']]==[str(ATTEMPT/'recorder/commands'/n/'stdout.raw') for n in ('03_verify_01','03_verify_02')],'actual_pair_two_streams_three_comparisons')
    need(ordinary(PAPER/'CANONICAL.json')==canonical and not os.path.lexists(PAPER/'canonical.stdout.json'),'canonical_raw_bytes_unchanged_no_adoption')
except BaseException as exc:
    errors.append({'type':type(exc).__name__,'error':repr(exc),'traceback':traceback.format_exc()})
try:
    after={p:core.rich(p) for p in paths}
    core.write_json(ENTRY/'INPUTS_AFTER.json',after)
    need(before==after,'entire_root_bound_source_authority_key_unchanged')
except BaseException as exc:
    errors.append({'stage':'root_input_closure','type':type(exc).__name__,'error':repr(exc)})
result={'status':'FAIL_PRESERVED' if errors else 'CAPTURED_STRICT_PAIR_PENDING_COMPLETE_RECEPTION','errors':errors,'commands':core.COMMANDS,'attempt':str(ATTEMPT),'canonical_adopted':False,'complete_pair_reception_completed':False,'scope':'Root outer native capture only, not scientific-output acceptance or another producer invocation.'}
core.write_json(ENTRY/'RESULT.json',result)
seal=core.seal() if not core.UNFINALIZED_NATIVE else None
print(json.dumps({'status':result['status'],'errors':errors,'entry':str(ENTRY),'attempt':str(ATTEMPT),'seal':seal,'root_native_commands':len(core.COMMANDS),'canonical_adopted':False},sort_keys=True),flush=True)
sys.exit(1 if errors else 0)
