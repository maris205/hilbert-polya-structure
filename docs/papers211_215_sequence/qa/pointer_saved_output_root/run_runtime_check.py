"""One root execution of the separately authored, completely received auditor.

The pinned prior native core supplies capture/settlement, not mathematics.
This invokes no scientific producer or saved-output semantic reconstruction.
"""
from hashlib import sha256
import json
import os
from pathlib import Path
import sys
import traceback
import types

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
QA = ROOT/'docs/papers211_215_sequence/qa'
HERE = QA/'pointer_saved_output_root'
OUT = HERE/'runtime_execution01'
SOURCE = QA/'finite_pointer_initial_runtime_reception01/inspect_initial.py'
CORE = QA/'p211_runtime_preparation/runtime_core.py'
LOCK = QA/'finite_pointer_runtime_preparation01/discovery02/RUNTIME_LOCK.json'
ENV = {'PATH':'/usr/bin:/bin','LANG':'C.UTF-8','LC_ALL':'C.UTF-8','TZ':'UTC'}
source_bytes = SOURCE.read_bytes()
core_bytes = CORE.read_bytes()
assert sha256(source_bytes).hexdigest()=='daf7b06a20252979c96cca9f13793ae0d3230cd65e30f5124ffff1a379c44bdc'
assert sha256(core_bytes).hexdigest()=='2fd41cfac779f8d5f4e23089fcc9f2b6b041cbebe19e7003b2db6b4815909934'
assert sha256(LOCK.read_bytes()).hexdigest()=='e2fd2189f639feff28a8ae499da011e9ea6e9cadf3eb99b60944f3209fdebd02'
assert sha256((HERE/'RUNTIME_PREPARATION_RESULT.json').read_bytes()).hexdigest()=='6f24bfab6a38961474b9edd29d6c7abd732107276eb66eed4c776b71dba0effc'
assert sha256((HERE/'RUNTIME_PREPARATION_NATIVE01.json').read_bytes()).hexdigest()=='079c1254d54ed04aeff8e4d6066e1effaf1c0aaa36b9df42489accec24d0a87a'
assert Path.cwd()==ROOT and dict(os.environ)==ENV and sys.executable=='/usr/bin/python3.10'
assert sys.flags.isolated==sys.flags.no_site==1 and sys.flags.optimize==0 and sys.dont_write_bytecode
assert not os.path.lexists(OUT) and sys.pycache_prefix==str(HERE/'never_created_runtime_controller_cache') and not os.path.lexists(sys.pycache_prefix)
core = types.ModuleType('_pointer_received_native_core')
core.__file__ = str(CORE)
sys.modules[core.__name__] = core
exec(compile(core_bytes,str(CORE),'exec'),core.__dict__)
OUT.mkdir(mode=0o700)
(OUT/'commands').mkdir()
core.OUT = OUT
lock = json.loads(LOCK.read_bytes())
accepted = json.loads((HERE/'RUNTIME_PREPARATION_RESULT.json').read_bytes())
key = {**lock['files'],**accepted['READ_INPUTS']}
for p in (Path(__file__).resolve(),CORE,LOCK,HERE/'RUNTIME_PREPARATION_RESULT.json',HERE/'RUNTIME_PREPARATION_NATIVE01.json'):
    key[str(p)] = core.rich(p)
before = {}
for p,expected in key.items():
    actual = core.rich(p)
    assert all(actual[k]==v for k,v in expected.items())
    before[p] = actual
core.write_json(OUT/'INPUTS_BEFORE.json',before)
allowed = {str(Path(p).resolve()) for p in before}

def sample(phase):
    row = core.ordinary_sample()
    for item in list(row['modules'].values()) + [{'path':p,**v} for p,v in row['mapped_files'].items()]:
        assert item['path'] in allowed and core.value(item['path'])=={k:item[k] for k in ('bytes','sha256')}
    assert row['environment']==ENV and row['cwd']==str(ROOT) and row['sys_path']==['/usr/lib/python310.zip','/usr/lib/python3.10','/usr/lib/python3.10/lib-dynload']
    assert not row['cache_lexists']
    core.write_json(OUT/('CONTROLLER_'+phase+'.json'),{**row,'interpreter_argv':sys.orig_argv})

sample('BEFORE')
argv = ['/usr/bin/python3.10','-I','-S','-B','-X','pycache_prefix='+str(OUT/'never_created_receiver_cache'),str(SOURCE),
        str(QA/'finite_pointer_initial_binding01/BINDING.json'),'7575bf8027327615dbe3a938b4fb50de6f8b7b241668346435369d99874e01ac',
        str(QA/'finite_pointer_initial_binding01/PRODUCTION_TOOL_INVOCATION.json')]
core.write_json(OUT/'AUTHORIZATION.json',{'issuer':'/root','source':core.rich(SOURCE),'source_reception':core.rich(HERE/'RUNTIME_PREPARATION_RESULT.json'),
    'auditor_author':'/root/round211_rational_scout/relation_primary_sources/lyndon_primary_check',
    'actual_executor':'/root','argv':argv,'cwd':str(ROOT),'environment':ENV,'timeout_seconds':900,
    'scope':'One read-only full runtime-evidence reception; no producer, semantic science, canonical, admission or retry.'})
code = 0
try:
    data = core.command('01_receive_initial_runtime',argv,timeout=900,cwd=ROOT)
    received = json.loads(data)
    assert received['status']=='PASS_POINTER_INITIAL_RUNTIME_RECORDS_ONLY_SCIENTIFIC_OUTPUT_UNREAD'
    assert received['complete_payloads']==77 and received['complete_files']==78 and received['native_commands']==7
    assert received['READ_INPUTS_BEFORE']==received['READ_INPUTS_AFTER'] and len(received['READ_INPUTS_BEFORE'])==received['receiver_read_paths']
    for p,wanted in received['READ_INPUTS_AFTER'].items():
        assert core.rich(p)==wanted
    assert received['scientific_output_nonhash_body_reads']==received['scientific_output_json_parses']==received['producer_invocations_in_this_audit']==0
    result = {k:v for k,v in received.items() if k not in ('READ_INPUTS_BEFORE','READ_INPUTS_AFTER')}
    result.update({'root_complete_current_key_reception':True,'actual_auditor_invocations':1,'auditor_authorship':'Separate reviewer authored; root executed; not a second independent mathematical review'})
except BaseException:
    code = 1
    result = {'status':'FAIL_ROOT_RUNTIME_RECEPTION_PRESERVE','traceback':traceback.format_exc(),'producer_invocations':0}
finally:
    after = {p:core.rich(p) for p in before}
    core.write_json(OUT/'INPUTS_AFTER.json',after)
    assert before==after and SOURCE.read_bytes()==source_bytes and CORE.read_bytes()==core_bytes
    assert not os.path.lexists(OUT/'never_created_receiver_cache') and not os.path.lexists(sys.pycache_prefix)
    sample('AFTER')
core.write_json(OUT/'RESULT.json',result)
seal = core.seal()
print(json.dumps({'status':result['status'],'checks':result.get('checks'),'receiver_read_paths':result.get('receiver_read_paths'),
    'attempt':str(OUT),'seal':seal,'root_native_commands':len(core.COMMANDS),'exit_code':code},sort_keys=True))
raise SystemExit(code)
