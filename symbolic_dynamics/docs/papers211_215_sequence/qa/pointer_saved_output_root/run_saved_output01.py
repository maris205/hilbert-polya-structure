"""Root exact binding and one settled saved-output reception, no producer.

Uses the accepted native capture core, not submitted science. All source
and host dependencies are checked before/after. Controller maps/modules
are discrete samples; no child tracing or OS hermeticity is claimed.
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
HERE=QA/'pointer_saved_output_root'
OUT=HERE/'semantic_execution01'
SOURCE=QA/'finite_pointer_output_receiver_preparation01/receive_output.py'
CORE=QA/'p211_runtime_preparation/runtime_core.py'
ENV={'PATH':'/usr/bin:/bin','LANG':'C.UTF-8','LC_ALL':'C.UTF-8','TZ':'UTC'}
PINS={
    SOURCE:'24b996e02ce31fe08b89fcd4f260937a9ce67cb16838d8e0350dcdc4d10c559d',
    CORE:'2fd41cfac779f8d5f4e23089fcc9f2b6b041cbebe19e7003b2db6b4815909934',
    HERE/'PREPARATION_RESULT02.json':'37bdfebfc56bb27817761b86d6a8cf41e4c6fa3a725979e2d084798136bcace3',
    HERE/'runtime_execution03/commands/01_receive_initial_runtime/stdout.raw':'2ae24cae018189a520c3b014dbd295210c2c63c4c9e1bbe1855f4c87b399aad9',
    HERE/'RUNTIME_EXECUTION_NATIVE03.json':'2d52ed3c471fbd5a2539a9db296d88ed056d136b92706749401e48ae2d2adb82',
    HERE/'runtime_execution03/RESULT.json':'12640f591da660e6494f08ea68bf17b8f3e1627ace738d134ac30d7a2aed4e51'}
for p,h in PINS.items(): assert sha256(p.read_bytes()).hexdigest()==h
assert Path.cwd()==ROOT and dict(os.environ)==ENV and sys.executable=='/usr/bin/python3.10'
assert sys.flags.isolated==sys.flags.no_site==1 and sys.flags.optimize==0 and sys.dont_write_bytecode
assert not os.path.lexists(OUT) and sys.pycache_prefix==str(HERE/'never_created_semantic_controller_cache01') and not os.path.lexists(sys.pycache_prefix)
core=types.ModuleType('_pointer_saved_native_core')
core.__file__=str(CORE)
sys.modules[core.__name__]=core
exec(compile(CORE.read_bytes(),str(CORE),'exec'),core.__dict__)
source_prep=core.read_json(HERE/'PREPARATION_RESULT02.json')
runtime=core.read_json(HERE/'runtime_execution03/commands/01_receive_initial_runtime/stdout.raw')
native=core.read_json(HERE/'RUNTIME_EXECUTION_NATIVE03.json')
parts=[native['result']]+[r['result'] for r in native['polls']]
assert parts[-1]['exit_code']==0 and not parts[-1].get('session_id')
control=json.loads(''.join(p['output'] for p in parts))
assert control['status']==runtime['status']=='PASS_POINTER_INITIAL_RUNTIME_RECORDS_ONLY_SCIENTIFIC_OUTPUT_UNREAD'
assert runtime['checks']==72746 and runtime['receiver_read_paths']==319 and runtime['received_scientific_native_commands']==1
assert runtime['READ_INPUTS_BEFORE']==runtime['READ_INPUTS_AFTER']
assert runtime['complete_payloads']==77 and runtime['scientific_output_json_parses']==runtime['scientific_output_nonhash_body_reads']==0
assert source_prep['status']=='PASS_ROOT_COMPLETE_SAVED_OUTPUT_RECEIVER_SOURCE_RECEPTION' and source_prep['read_paths']==22
core.manifest(HERE/'runtime_execution03',expected='d23c0506c2a05fdea5b37a2d157171c43bf470c370eedcc684718d83ed813a19',count=10)
key={**runtime['READ_INPUTS_AFTER'],**source_prep['inputs']}
for p in [*PINS,Path(__file__).resolve(),HERE/'runtime_execution03/SHA256SUMS',HERE/'SOURCE_AND_GATE_RECEPTION.md']:
    key[str(p)]=core.rich(p)
for p,w in key.items():
    actual=core.rich(p)
    assert all(actual[k]==v for k,v in w.items())
stdout=runtime['scientific_stdout_opaque_pin']
assert stdout=={'path':str(QA/'root_replays/finite_pointer_initial01/recorder/commands/03_verify_01/stdout.raw'),'bytes':10366275,'sha256':'45dc800a60a2d26da492a528f4a54c9a94a755338f598e8ccc161a9d719bb2b1'}
assert core.value(stdout['path'])=={k:stdout[k] for k in ('sha256','bytes')}
OUT.mkdir(mode=0o700)
(OUT/'commands').mkdir()
core.OUT=OUT
binding={'format':'finite-pointer-saved-output-binding-v1','approved':True,
    'root_received_source_runtime_and_native_evidence':True,
    'receiver_source':{'path':str(SOURCE),**core.value(SOURCE)},'saved_stdout':stdout,
    'accepted_producer':{'sha256':'9b3c22ad86b36f5dece45d47de03d3cc309f05c46c40a152aec49dc8a0262cbb','bytes':27518},
    'accepted_parameters':{'sha256':'f71aff49cb7b4fda75851992a85ce3150cd8f69f1dd5a4512bb6e7b3afe08a16','bytes':415},
    'execution':{'cwd':str(ROOT),'pycache_prefix':str(OUT/'never_created_receiver_cache')},
    'canonical_adoption_authorized':False,'retry_authorized':False,'admission_authorized':False}
assert len(binding)==11
core.write_json(OUT/'BINDING.json',binding)
binding_pin=core.rich(OUT/'BINDING.json')
key[str(OUT/'BINDING.json')]=binding_pin
before={p:core.rich(p) for p in key}
core.write_json(OUT/'INPUTS_BEFORE.json',before)
allowed={str(Path(p).resolve()) for p in before}
def sample(phase):
    row=core.ordinary_sample()
    for item in list(row['modules'].values())+[{'path':p,**r} for p,r in row['mapped_files'].items()]:
        assert item['path'] in allowed and core.value(item['path'])=={k:item[k] for k in ('sha256','bytes')}
    assert row['environment']==ENV and row['cwd']==str(ROOT) and not row['cache_lexists']
    core.write_json(OUT/('CONTROLLER_'+phase+'.json'),{**row,'interpreter_argv':sys.orig_argv})
argv=['/usr/bin/python3.10','-I','-S','-B','-X','pycache_prefix='+binding['execution']['pycache_prefix'],str(SOURCE),str(OUT/'BINDING.json'),binding_pin['sha256']]
core.write_json(OUT/'AUTHORIZATION.json',{'issuer':'/root','source':core.rich(SOURCE),'binding':{'path':str(OUT/'BINDING.json'),**binding_pin},
    'argv':argv,'cwd':str(ROOT),'environment':ENV,'timeout_seconds':900,
    'source_reception':core.rich(HERE/'PREPARATION_RESULT02.json'),'runtime_reception':core.rich(HERE/'runtime_execution03/RESULT.json'),
    'scope':'One complete saved-output reception; author-authored receiver executed by root. No producer, canonical adoption, admission, retry or independent manuscript review.'})
sample('BEFORE')
code=0
try:
    data=core.command('01_receive_saved_output',argv,timeout=900,cwd=ROOT)
    result=json.loads(data)
    assert result['status']=='PASS_SAVED_OUTPUT_RECEPTION_ONLY' and result['states']==4356 and result['producer_invocations']==0 and result['canonical_adoption'] is False
    assert result['saved_stdout']==stdout and len(result['boxes'])==4
except BaseException:
    code=1
    result={'status':'FAIL_ROOT_SAVED_OUTPUT_RECEPTION_PRESERVE','traceback':traceback.format_exc(),'producer_invocations':0}
finally:
    after={p:core.rich(p) for p in before}
    core.write_json(OUT/'INPUTS_AFTER.json',after)
    assert before==after and not os.path.lexists(binding['execution']['pycache_prefix']) and not os.path.lexists(sys.pycache_prefix)
    sample('AFTER')
core.write_json(OUT/'RESULT.json',result)
seal=core.seal()
print(json.dumps({'status':result['status'],'attempt':str(OUT),'exit_code':code,'actual_receiver_invocations':1,'producer_invocations':0,'result':core.value(OUT/'RESULT.json'),'seal':seal},sort_keys=True))
raise SystemExit(code)
