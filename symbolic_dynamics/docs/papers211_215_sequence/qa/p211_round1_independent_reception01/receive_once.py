#!/usr/bin/python3.10
"""One root-authorized documentary receiver invocation, with exclusive raw capture.

Only this new reception directory is writable. No retry, recorder or science.
The large receiver stdout remains raw bytes; it is never sent through JS JSON.
"""
from hashlib import sha256
import json
import os
from pathlib import Path
import re
import stat
import subprocess
import sys
import time
import traceback

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
QA = ROOT/'docs/papers211_215_sequence/qa'
HERE = QA/'p211_round1_independent_reception01'
PREP = QA/'p211_round1_reception_preparation02'
EXEC = QA/'p211_round1_execution01'
SOURCE = PREP/'receive_round1.py'
HOST = QA/'p211_round1_binding_root/postcopy02/RESULT.json'
ENV = {'PATH':'/usr/bin:/bin','LANG':'C.UTF-8','LC_ALL':'C.UTF-8','TZ':'UTC'}
SOURCE_PIN = {'bytes':37766,'sha256':'21d16d2560eeb68420a3c37c9a3fda98dcbcb0ea1043dc80cd36a81e24fef06e'}
PREP_SEAL = '556f22fc196006bb4b7a800ca10af7e921666523495f16a8afd9d3f3f7dc3aa0'
EXEC_SEAL = '858999190e1e16f07752aa0c4a9e6ca967bf7b4dee61eaa3c33ee2b47f141c30'
HOST_SHA = '04a123c5c7e9bba267ce380d387be7e4789f4a777d9c62bb5b7ed2f418630c77'
ARGV = ['/usr/bin/python3.10','-I','-S','-B',str(SOURCE),
        '--root-host-evidence',str(HOST.relative_to(ROOT)),'--root-host-sha256',HOST_SHA]
before = {}
started = False


def need(ok, label):
    if not ok:
        raise AssertionError(label)


def pin(raw):
    return {'bytes':len(raw),'sha256':sha256(raw).hexdigest()}


def meta(s):
    return {k:getattr(s,'st_'+v) for k,v in [('mode','mode'),('device','dev'),
        ('inode','ino'),('uid','uid'),('gid','gid'),('nlink','nlink'),
        ('size','size'),('mtime_ns','mtime_ns'),('ctime_ns','ctime_ns')]}


def fresh(path):
    need(path.is_absolute() and path.resolve()==path and stat.S_ISREG(path.lstat().st_mode),
         ('ordinary physical input',str(path)))
    prior = meta(path.lstat())
    raw = path.read_bytes()
    later = meta(path.lstat())
    need(prior==later and later['size']==len(raw),('read stability',str(path)))
    return raw,{**pin(raw),'stat':later}


def read(path):
    raw,key = fresh(path)
    name = str(path)
    need(name not in before or before[name]==key,('input drift',name))
    before[name] = key
    return raw


def put(name, value):
    need(isinstance(name,str) and Path(name).name==name and name not in ('.','..'),
         'write only one explicit new owned basename')
    raw = value if isinstance(value,bytes) else (json.dumps(value,sort_keys=True,indent=2)+'\n').encode()
    with (HERE/name).open('xb') as stream:
        stream.write(raw)


def main():
    global started
    need(Path.cwd()==ROOT and Path(__file__).absolute()==HERE/'receive_once.py','literal new controller location/cwd')
    need(set(p.name for p in HERE.iterdir())=={'receive_once.py','PLAN.md','INITIAL_PIN_NATIVE.json'},'exclusive reception starts with three preparation files')
    need(dict(os.environ)==ENV and sys.executable=='/usr/bin/python3.10' and
         sys.flags.isolated==sys.flags.no_site==sys.flags.dont_write_bytecode==1,'actual isolated controller environment')
    controller_raw = read(Path(__file__).absolute())
    put('EXECUTED_CONTROLLER_SOURCE.py',controller_raw)
    source_raw = read(SOURCE)
    need(pin(source_raw)==SOURCE_PIN,'exact root-authorized receiver source')
    put('EXECUTED_RECEIVER_SOURCE.py',source_raw)
    prep_raw = read(PREP/'SHA256SUMS')
    need(pin(prep_raw)['sha256']==PREP_SEAL,'exact sealed complete receiver preparation')
    members = {}
    for line in prep_raw.decode('utf-8').splitlines():
        m = re.fullmatch(r'([0-9a-f]{64})  ([^/\\\x00\r\n\t]+)',line)
        need(m is not None,'strict flat preparation manifest row')
        digest,name = m.groups()
        need(name not in members and name not in ('.','..','SHA256SUMS'),'unique nonself preparation member')
        members[name] = digest
        need(pin(read(PREP/name))['sha256']==digest,('entire sealed preparation payload',name))
    need(len(members)==8 and {p.name for p in PREP.iterdir()}==set(members)|{'SHA256SUMS'},'complete9 ordinary preparation files')
    execution_raw = read(EXEC/'SHA256SUMS')
    need(pin(execution_raw)['sha256']==EXEC_SEAL,'exact completed509-file execution package seal')
    host_raw = read(HOST)
    need(pin(host_raw)['sha256']==HOST_SHA,'root-authorized separate host record identity; no semantic host acceptance')
    interpreter = read(Path('/usr/bin/python3.10'))
    put('PREPARATION_INPUT_MANIFEST.sha256',prep_raw)
    put('EXECUTION_INPUT_MANIFEST.sha256',execution_raw)
    put('INPUT_SEAL_ORIGINS.json',{'preparation':{'original':str(PREP/'SHA256SUMS'),'pin':pin(prep_raw),'original_base':str(PREP)},
        'execution':{'original':str(EXEC/'SHA256SUMS'),'pin':pin(execution_raw),'original_base':str(EXEC)},
        'source':{'original':str(SOURCE),'pin':SOURCE_PIN},'root_postcopy_host':{'original':str(HOST),'pin':pin(host_raw),'scope':'whole record bytes only; host/settings acceptance external root'}})
    put('CONTROLLER_INPUTS_BEFORE.json',before)
    request = {'argv':ARGV,'cwd':str(ROOT),'environment':ENV,'stdin':'subprocess.DEVNULL',
               'timeout_seconds':900,'started_epoch':time.time(),'source_pin':SOURCE_PIN,
               'controller_pin':pin(controller_raw),'interpreter_pin':pin(interpreter),
               'preparation_manifest_pin':pin(prep_raw),'execution_manifest_pin':pin(execution_raw),
               'root_host_record_pin':pin(host_raw)}
    put('RECEIVER_ATTEMPT.json',request)
    native_exit,exception,capture = None,None,'captured'
    started = True
    try:
        actual = subprocess.run(ARGV,cwd=ROOT,env=ENV,stdin=subprocess.DEVNULL,
                                capture_output=True,timeout=900)
        stdout,stderr,native_exit = actual.stdout,actual.stderr,actual.returncode
    except subprocess.TimeoutExpired as exc:
        stdout,stderr = exc.stdout or b'',exc.stderr or b''
        exception = {'type':type(exc).__name__,'message':str(exc)}
        capture = 'captured_partial_at_timeout; no exit code invented'
    except OSError as exc:
        stdout,stderr = b'',b''
        exception = {'type':type(exc).__name__,'message':str(exc)}
        capture = 'not_launched; streams unavailable'
    put('receiver.stdout.raw',stdout)
    put('receiver.stderr.raw',stderr)
    native = {**request,'ended_epoch':time.time(),'native_exit_code':native_exit,
              'exception':exception,'stream_capture_status':capture,
              'stdout':{'path':'receiver.stdout.raw',**pin(stdout)},
              'stderr':{'path':'receiver.stderr.raw',**pin(stderr)}}
    put('RECEIVER_NATIVE.json',native)
    after = {p:fresh(Path(p))[1] for p in sorted(before)}
    put('CONTROLLER_INPUTS_AFTER.json',after)
    need(after==before,'complete controller original rich input key unchanged')
    need(exception is None and type(native_exit) is int and native_exit==0 and stderr==b'',
         'one actual documentary invocation succeeded; any failure must stop')
    actual_result = json.loads(stdout)
    need(actual_result['schema']=='p211_round1_documentary_receiver_v2' and
         actual_result['status']=='PASS_PHYSICAL_DOCUMENTARY_SCOPE_HOST_ACCEPTANCE_EXTERNAL_ROOT',
         'actual complete documentary result schema/scope')
    need(actual_result['READ_INPUTS_BEFORE']==actual_result['READ_INPUTS_AFTER'],
         'whole receiver rich before/after key remains present in raw JSON')
    summary = {k:actual_result[k] for k in ('schema','status','checks','payloads','round1_files',
        'native_child_records','native_child_raw_streams','native_root_records',
        'declared_external_empty_directories','external_files','recorder_read_paths',
        'receiver_read_paths','execution_files','recorder_dereferences_complete_host_key',
        'receiver_dereferences_799_host_referents','submitted_programs_executed',
        'scientific_executions','builds','page_views','manuscript_reviews','paper_complete','external')}
    summary.update({'actual_receiver_native_exit':native_exit,'receiver_stdout':pin(stdout),
                    'receiver_stderr':pin(stderr),'controller_original_read_paths':len(before),
                    'complete_receiver_preparation_files':9,'execution_manifest':pin(execution_raw),
                    'preparation_manifest':pin(prep_raw),'whole_result_path':'receiver.stdout.raw',
                    'root_postcopy_host_evidence':actual_result['root_postcopy_host_evidence'],
                    'reception_package_seal':'PENDING_ACTUAL_CONTROLLER_TOOL_RETURN_AND_READ_ONLY_RECEPTION'})
    put('SCOPED_RESULT.json',summary)
    print(json.dumps(summary,sort_keys=True))


if __name__=='__main__':
    try:
        main()
    except BaseException:
        failure = {'status':'FAILED_PRESERVE_ONE_RECEPTION_ATTEMPT_NO_RETRY',
                   'receiver_invocation_attempted':started,'traceback':traceback.format_exc(),
                   'receiver_source_pin':SOURCE_PIN,'controller_input_paths':len(before)}
        if not (HERE/'CONTROLLER_FAILURE.json').exists():
            put('CONTROLLER_FAILURE.json',failure)
        print(json.dumps(failure,sort_keys=True))
        raise SystemExit(1)
