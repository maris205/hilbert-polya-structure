#!/usr/bin/python3.10
"""Close the five actual owned documentary attempts and native source pins.

Only this new audit's metadata/raw artifacts are written. No submitted
Python, recorder, scientific verifier or build program is executed.
"""
from hashlib import sha256
import json
import os
from pathlib import Path
import re
import stat
import subprocess
import time

ROOT=Path('/root/autodl-tmp/symbolic_dynamics')
QA=ROOT/'docs/papers211_215_sequence/qa'
HERE=QA/'p211_round2_physical_independent01'
OUT=HERE/'closing01'
ENV={'PATH':'/usr/bin:/bin','LANG':'C.UTF-8','LC_ALL':'C.UTF-8','TZ':'UTC'}
READS={}
checks=0
def need(ok,label):
    global checks
    checks+=1
    if not ok:
        raise AssertionError(label)
def pin(raw):
    return {'bytes':len(raw),'sha256':sha256(raw).hexdigest()}
def read(p):
    p=Path(p)
    need(p.is_file(),('file',str(p)))
    raw=p.read_bytes()
    value=pin(raw)
    need(str(p) not in READS or READS[str(p)]==value,('read byte stability',str(p)))
    READS[str(p)]=value
    return raw
def obj(p):
    return json.loads(read(p))
def meta(s):
    return {k:getattr(s,'st_'+v) for k,v in (
        ('mode','mode'),('device','dev'),('inode','ino'),('uid','uid'),('gid','gid'),
        ('nlink','nlink'),('size','size'),('mtime_ns','mtime_ns'),('ctime_ns','ctime_ns'))}
def full(p):
    p=Path(p)
    ls,st=p.lstat(),p.stat()
    raw=read(p)
    value={**pin(raw),'resolved':str(p.resolve(strict=True)),'symlink':os.readlink(p) if p.is_symlink() else None,
           'stat':meta(st),'lstat':meta(ls)}
    need(meta(p.lstat())==value['lstat'] and meta(p.stat())==value['stat'],'full local stat stability')
    return value
def put(p,v):
    raw=v if isinstance(v,bytes) else (json.dumps(v,sort_keys=True,indent=2)+'\n').encode()
    with p.open('xb') as stream:
        stream.write(raw)
def apply_diff(old,patch):
    """Exact in-memory unified-diff replay, never an on-disk patch."""
    lines=patch.decode().splitlines(keepends=True)
    need(lines[0].startswith('--- ') and lines[1].startswith('+++ '),'whole unified headers')
    original=old.decode().splitlines(keepends=True)
    result=[]
    cursor=0
    i=2
    while i<len(lines):
        m=re.match(r'^@@ -(\d+)(?:,(\d+))? \+(\d+)(?:,(\d+))? @@',lines[i])
        need(m is not None,('whole actual hunk header',lines[i]))
        old_start,old_count,new_start,new_count=[int(x) if x is not None else 1 for x in m.groups()]
        start=old_start-1 if old_count else old_start
        need(cursor<=start<=len(original),'ordered old hunk interval')
        result.extend(original[cursor:start])
        cursor=start
        need(len(result)==(new_start-1 if new_count else new_start),'exact new hunk position')
        i+=1
        removed=added=0
        while i<len(lines) and not lines[i].startswith('@@ '):
            line=lines[i]
            need(line[:1] in (' ','-','+'),'complete newline-terminated hunk lines')
            if line[0] in (' ','-'):
                need(cursor<len(original) and original[cursor]==line[1:],'entire old hunk bytes')
                cursor+=1
                removed+=1
            if line[0] in (' ','+'):
                result.append(line[1:])
                added+=1
            i+=1
        need((removed,added)==(old_count,new_count),'complete hunk counts')
    result.extend(original[cursor:])
    return ''.join(result).encode()

need(Path.cwd()==ROOT and not OUT.exists() and not (HERE/'INPUTS.sha256').exists(),'exclusive closing output only')
versions=[('',HERE,'receive_physical.py','capture_once.py'),
          *[(str(i).zfill(2),HERE/('run'+str(i).zfill(2)),'receive_physical'+str(i).zfill(2)+'.py','capture'+str(i).zfill(2)+'.py') for i in range(2,6)]]
expected_checks=[372,159491,159491,159617,488474]
attempts=[]
union={}
for i,(suffix,d,source_name,capture_name) in enumerate(versions):
    attempt,native=obj(d/'CHECKS_ATTEMPT.json'),obj(d/'CHECKS_NATIVE.json')
    source,capture=read(HERE/source_name),read(HERE/capture_name)
    need(source==read(d/'EXECUTED_RECEIVER_SOURCE.py') and capture==read(d/'EXECUTED_CAPTURE_SOURCE.py'),'complete actual owned executed-source snapshots')
    need(attempt['source_pin']==pin(source) and attempt['capture_source_pin']==pin(capture),'whole source pins for every actual attempt')
    need(attempt['argv']==['/usr/bin/python3.10','-I','-S','-B',str(HERE/source_name)] and
         attempt['cwd']==str(ROOT) and attempt['environment']==ENV and attempt['stdin']=='subprocess.DEVNULL' and
         attempt['timeout_seconds']==180,'all actual owned attempt scopes')
    need(all(native[k]==v for k,v in attempt.items()) and native['exception'] is None and
         native['stream_capture_status']=='captured' and native['started_epoch']<=native['ended_epoch'] and
         native['native_exit_code']==(0 if i==4 else 1),'every actual native exit preserved')
    raw=read(d/'CHECKS.stdout.raw')
    stderr=read(d/'CHECKS.stderr.raw')
    need(native['stdout']=={'path':'CHECKS.stdout.raw',**pin(raw)} and
         native['stderr']=={'path':'CHECKS.stderr.raw',**pin(stderr)} and stderr==b'','every actual owned raw stream pin')
    outcome=json.loads(raw)
    need(outcome['checks']==expected_checks[i],'original actual check counts')
    key=outcome['READ_INPUTS'] if i==4 else outcome['READ_INPUTS_PARTIAL']
    for p,v in key.items():
        need(p not in union or union[p]==v,'all repeated partial/final original rich keys agree')
        union[p]=v
    saved=obj(d/'RESULT.json')
    if i==4:
        need(saved=={**{k:v for k,v in outcome.items() if k!='READ_INPUTS'},
                     'whole_helper_stdout':native['stdout'],'whole_input_key_entries':len(key)},'whole actual successful compact result projection')
        passing=outcome
    else:
        need(saved['status']=='FAIL_DOCUMENTARY_ATTEMPT_PRESERVED' and saved['native_exit_code']==1 and
             saved['stdout']==native['stdout'] and saved['stderr']==native['stderr'] and outcome['traceback'],
             'all failed compact results and complete tracebacks retained')
    attempts.append({'version':i+1,'directory':str(d.relative_to(HERE)),'checks':outcome['checks'],'input_paths':len(key),
                     'native_exit_code':native['native_exit_code'],'stdout':pin(raw),'source':pin(source)})
for p,v in union.items():
    need(full(Path(p))==v,('all current original/partial/final full rich entries',p))
need(len(passing['READ_INPUTS'])==4821 and passing['checks']==488474,'exact actual successful independent scope')

derivation=obj(HERE/'DERIVATION_NATIVE.json')
need(derivation['record']['result']['exit_code']==1 and read(HERE/'DERIVATION.diff')==derivation['record']['result']['output'].encode(),
     'entire actual R1 derivation raw diff retained')
old=read(QA/'p211_round1_reception_preparation02/receive_round1.py')
need(apply_diff(old,read(HERE/'DERIVATION.diff'))==read(HERE/'receive_physical.py'),'whole original R1-to-new source derivation replay')
corrections=obj(HERE/'CORRECTIONS_NATIVE.json')
need(len(corrections['source_diffs'])==4 and len(corrections['attempts'])==5,'complete actual correction/attempt census')
for index,record in enumerate(corrections['source_diffs']):
    before='receive_physical.py' if index==0 else 'receive_physical'+str(index+1).zfill(2)+'.py'
    after='receive_physical'+str(index+2).zfill(2)+'.py'
    need(record['result']['exit_code']==1 and apply_diff(read(HERE/before),record['result']['output'].encode())==read(HERE/after),
         'each whole actual owned correction diff reconstructs the next exact source')
root_diff=corrections['root_actual_capture_correction']['result']['output'].encode()
need(apply_diff(read(QA/'p211_round2_binding_root01/FAILED_ASSEMBLE_CAPTURE01.js'),root_diff)==
     read(QA/'p211_round2_binding_root01/assemble_capture.js'),'entire actual root capture correction including three evidence reads')
for index,n in enumerate(corrections['attempts']):
    r=n['result']
    stream=r['output']
    session=r.get('session_id')
    for p in n.get('polls',[]):
        need(p['request']['session_id']==session and p['request']['chars']=='','entire actual same owned product session')
        r=p['result']
        session=r.get('session_id')
        stream+=r['output']
    need(r['exit_code']==(0 if index==4 else 1) and 'session_id' not in r,'all original outer final exits')
    emitted=json.loads(stream)
    d=versions[index][1]
    need(emitted['native']==obj(d/'CHECKS_NATIVE.json') and emitted['status']==obj(d/'RESULT.json')['status'],
         'whole actual outer tool output binds inner owned original receipt')

native_reads=obj(HERE/'NATIVE_READS.json')
need(len(native_reads['records'])==36,'complete selected actual native-read census')
records={r['record_id']:r for r in native_reads['records']}
def groups(ids):
    output=''.join(records[n]['result']['output'] for n in ids)
    result=[]
    for line in output.splitlines(keepends=True):
        m=re.match(r'^ *(\d+)\t(.*)',line)
        if m is None:
            continue
        number=int(m.group(1))
        if number==1:
            result.append([])
        need(result and number==len(result[-1])+1,'entire bounded numbered original source sequence')
        result[-1].append(line[line.index('\t')+1:])
    return [''.join(g).encode() for g in result]
specs=[
    (('source0','source1','source2'),0,QA/'p211_round2_execution01/freeze.py',687),
    (('source3',),0,QA/'p211_round2_binding_root01/invoke_round2.py',109),
    (('source3',),1,QA/'p211_round2_binding_root01/refresh02/recheck.py',157),
    (('receiver0','receiver1'),0,QA/'p211_round1_reception_preparation02/receive_round1.py',529),
    (('source4',),0,QA/'p211_round2_binding_root01/assemble_capture.js',46),
    (('source4',),1,QA/'p211_round2_binding_root01/seal_actual.js',32),
    (('source5',),0,QA/'p211_round2_binding_root01/prepare_enabled.js',72),
    (('build_source',),0,ROOT/'docs/papers211_215_sequence/reviews/p211_a/inspect_build_reuse.py',142),
    (('source_reception_source',),0,QA/'p211_round2_binding_root01/source_reception01/receive.js',102)]
source_bindings=[]
source_inputs=[]
for ids,index,target,count in specs:
    raw=groups(ids)[index]
    need(raw==read(target) and len(raw.splitlines())==count,'every entire original source-read output binding')
    source_bindings.append({'record_ids':ids,'group_index':index,'path':str(target),'lines':count,'pin':pin(raw)})
    source_inputs.append(raw)
extra_inputs=[QA/'p211_round2_binding_root01/ENABLED_BINDING_RECEPTION.md',QA/'p211_round2_binding_root01/HOST_PRECHECK_SCOPE.md']
external={p:{k:v[k] for k in ('bytes','sha256')} for p,v in passing['READ_INPUTS'].items() if not Path(p).is_relative_to(HERE)}
for p in extra_inputs:
    raw=read(p)
    need(str(p) not in external or external[str(p)]==pin(raw),'extra documentary input original agrees')
    external[str(p)]=pin(raw)
need(len(external)==4820,'all 4818 external successful-reader inputs plus two actual root scope receipts')
raw_manifest=''.join(v['sha256']+'  '+p+'\n' for p,v in sorted(external.items())).encode()
OUT.mkdir(mode=0o700)
put(HERE/'INPUTS.sha256',raw_manifest)
commands=[]
def command(label,argv,stdin,expected_stdout,origin=None):
    d=OUT/label
    d.mkdir(mode=0o700)
    if stdin is not None:
        put(d/'stdin.raw',stdin)
    attempt={'argv':argv,'cwd':str(ROOT),'environment':ENV,'stdin':'saved stdin.raw bytes' if stdin is not None else 'subprocess.DEVNULL',
             'input_pin':pin(stdin) if stdin is not None else None,'origin':origin,'timeout_seconds':60,'started_epoch':time.time(),
             'tool_pin':pin(read(argv[0]))}
    put(d/'ATTEMPT.json',attempt)
    code,error,state=None,None,'captured'
    try:
        if stdin is None:
            r=subprocess.run(argv,cwd=ROOT,env=ENV,stdin=subprocess.DEVNULL,capture_output=True,timeout=60)
        else:
            r=subprocess.run(argv,cwd=ROOT,env=ENV,input=stdin,capture_output=True,timeout=60)
        out,err,code=r.stdout,r.stderr,r.returncode
    except subprocess.TimeoutExpired as exc:
        out,err=exc.stdout or b'',exc.stderr or b''
        error={'type':type(exc).__name__,'message':str(exc)}
        state='partial_at_timeout; no exit invented'
    except OSError as exc:
        out,err=b'',b''
        error={'type':type(exc).__name__,'message':str(exc)}
        state='launch_failed_or_unknown; no exit invented'
    put(d/'stdout.raw',out)
    put(d/'stderr.raw',err)
    receipt={**attempt,'ended_epoch':time.time(),'native_exit_code':code,'exception':error,'stream_capture_status':state,
             'stdout':pin(out),'stderr':pin(err)}
    put(d/'NATIVE.json',receipt)
    commands.append({'label':label,**receipt})
    need(error is None and code==0 and out==expected_stdout and err==b'','actual complete native closing comparison/hash check')
for number,index in enumerate((0,1,3),1):
    spec=specs[index]
    command('%02d_source_cmp'%number,['/usr/bin/cmp','-',str(spec[2])],source_inputs[index],b'',source_bindings[index])
expected_sha=''.join(p+': OK\n' for p in sorted(external)).encode()
command('04_external_pins',['/usr/bin/sha256sum','-c',str(HERE/'INPUTS.sha256')],None,expected_sha,
        {'manifest':str(HERE/'INPUTS.sha256'),'pin':pin(raw_manifest),'rows':len(external)})
for p,v in union.items():
    need(full(Path(p))==v,('every old/current own attempt original still full-rich unchanged',p))
result={'status':'PASS_OWN_FAILURE_PRESERVATION_COMPLETE_SOURCE_BINDINGS_AND_NATIVE_CLOSURE',
        'checks':checks,'attempts':attempts,'all_attempt_original_rich_paths':len(union),
        'successful_main_checks':488474,'successful_main_paths':4821,'external_input_rows':len(external),
        'manifest_pin':pin(raw_manifest),'complete_source_bindings':source_bindings,'native_commands':commands,
        'original_derivation_bytes':len(read(HERE/'DERIVATION.diff')),'submitted_execution':False,
        'science':False,'build':False,'manuscript_review':False,'terminal_authority':False}
put(OUT/'RESULT.json',result)
print(json.dumps({'status':result['status'],'checks':checks,'rich_paths':len(union),'external_input_rows':len(external),
                  'complete_source_bindings':len(source_bindings),'native_commands':len(commands),
                  'result':{'path':str(OUT/'RESULT.json'),**pin(read(OUT/'RESULT.json'))}},sort_keys=True))
