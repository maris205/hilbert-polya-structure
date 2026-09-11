"""Root original receipt closure after the complete shared-source recheck.

No submitted source is imported/executed. Rich-key format follows the fully
read receiver/controller; the complete receiver has already run separately.
"""
from hashlib import sha256
import json
import os
from pathlib import Path
import re

ROOT=Path('/root/autodl-tmp/symbolic_dynamics')
QA=ROOT/'docs/papers211_215_sequence/qa'
HERE=QA/'p211_round1_root_reception'
A=QA/'p211_round1_independent_reception01'
PREP=QA/'p211_round1_reception_preparation02'
EXEC=QA/'p211_round1_execution01'
ENV={'PATH':'/usr/bin:/bin','LANG':'C.UTF-8','LC_ALL':'C.UTF-8','TZ':'UTC'}
READS={};CHECKS=0

def need(x,label):
    global CHECKS
    CHECKS+=1
    if not x:raise AssertionError(label)

def pin(raw):return {'bytes':len(raw),'sha256':sha256(raw).hexdigest()}

def read(p):
    p=Path(p);need(p.resolve()==p and p.is_file(),('physical file',str(p)))
    raw=p.read_bytes();key=pin(raw)
    need(str(p) not in READS or READS[str(p)]==key,('unchanged original',str(p)))
    READS[str(p)]=key
    return raw

def obj(p):return json.loads(read(p))

def rich(p):
    p=Path(p);s=p.stat();raw=read(p)
    return {**pin(raw),'stat':{k:getattr(s,'st_'+v) for k,v in [('mode','mode'),('device','dev'),('inode','ino'),
        ('uid','uid'),('gid','gid'),('nlink','nlink'),('size','size'),('mtime_ns','mtime_ns'),('ctime_ns','ctime_ns')]}}

def seal(base,count,digest):
    raw=read(base/'SHA256SUMS');need(pin(raw)['sha256']==digest,'fixed complete manifest')
    rows={}
    for line in raw.decode().splitlines():
        m=re.fullmatch(r'([0-9a-f]{64})  (.+)',line);need(m is not None,'manifest row')
        h,n=m.groups();need(n not in rows and n!='SHA256SUMS' and not Path(n).is_absolute()
            and all(x not in ('','.','..') for x in n.split('/')),'unique safe payload')
        need(pin(read(base/n))['sha256']==h,('every payload',n));rows[n]=h
    need(len(rows)==count and {p.relative_to(base).as_posix() for p in base.rglob('*') if p.is_file()}==set(rows)|{'SHA256SUMS'}
         and not any(p.is_symlink() for p in base.rglob('*')),'entire ordinary package membership')
    return rows

read(Path(__file__))
seal(A,19,'90a8e6a755561623d3aab3701dfa174e42b25de2affc2968677a71c4310d0798')
raw=read(A/'receiver.stdout.raw');rootraw=read(HERE/'recheck.stdout.raw')
need(raw==rootraw and len(raw)==2971096,'entire independent/root raw result identical')
whole=json.loads(raw)
need(whole['READ_INPUTS_BEFORE']==whole['READ_INPUTS_AFTER'] and len(whole['READ_INPUTS_AFTER'])==2763,'complete rich input key')
for p,key in whole['READ_INPUTS_AFTER'].items():need(rich(p)==key,('current complete receiver rich key',p))
controller=obj(A/'CONTROLLER_INPUTS_BEFORE.json')
need(controller==obj(A/'CONTROLLER_INPUTS_AFTER.json') and len(controller)==13,'all controller input keys')
for p,key in controller.items():need(rich(p)==key,('current controller rich key',p))
attempt,native=obj(A/'RECEIVER_ATTEMPT.json'),obj(A/'RECEIVER_NATIVE.json')
rootattempt,rootnative=obj(HERE/'RECHECK_ATTEMPT.json'),obj(HERE/'RECHECK_NATIVE.json')
need(attempt['argv']==rootattempt['argv'] and all(attempt[k]==rootattempt[k] for k in ('cwd','environment','stdin','timeout_seconds')),
     'actual same authorized exact argv and environment')
need(attempt['cwd']==str(ROOT) and attempt['environment']==ENV and attempt['stdin']=='subprocess.DEVNULL' and attempt['timeout_seconds']==900,'explicit controlled context')
need(set(native)==set(attempt)|{'ended_epoch','native_exit_code','exception','stream_capture_status','stdout','stderr'}
     and all(native[k]==v for k,v in attempt.items()),'whole independent native/attempt')
for n,at in ((native,attempt),(rootnative,rootattempt)):
    need(type(n['native_exit_code']) is int and n['native_exit_code']==0 and n['exception'] is None
         and n['started_epoch']<=n['ended_epoch'] and all(n[k]==v for k,v in at.items()),'actual settled success')
need(native['stream_capture_status']=='captured' and native['stdout']=={'path':'receiver.stdout.raw',**pin(raw)}
     and native['stderr']=={'path':'receiver.stderr.raw',**pin(read(A/'receiver.stderr.raw'))}
     and read(A/'receiver.stderr.raw')==read(HERE/'recheck.stderr.raw')==b''
     and rootnative['stdout']==pin(rootraw) and rootnative['stderr']==pin(b''),'entire actual raw streams')
source=read(PREP/'receive_round1.py');code=read(A/'receive_once.py')
need(source==read(A/'EXECUTED_RECEIVER_SOURCE.py') and pin(source)==attempt['source_pin']
     and code==read(A/'EXECUTED_CONTROLLER_SOURCE.py') and pin(code)==attempt['controller_pin'],'actual exact executed source bytes')
origins=obj(A/'INPUT_SEAL_ORIGINS.json')
for role,base,name,count,digest in [('preparation',PREP,'PREPARATION_INPUT_MANIFEST.sha256',8,'556f22fc196006bb4b7a800ca10af7e921666523495f16a8afd9d3f3f7dc3aa0'),
    ('execution',EXEC,'EXECUTION_INPUT_MANIFEST.sha256',508,'858999190e1e16f07752aa0c4a9e6ca967bf7b4dee61eaa3c33ee2b47f141c30')]:
    seal(base,count,digest);r=read(base/'SHA256SUMS')
    need(read(A/name)==r and origins[role]=={'original':str(base/'SHA256SUMS'),'original_base':str(base),'pin':pin(r)},'complete original manifest base/copy')
summary=obj(A/'SCOPED_RESULT.json')
tool=obj(A/'TOOL_NATIVE.json');poll=tool['polls'][0]
need(tool['request']=={'cmd':'/usr/bin/env -i PATH=/usr/bin:/bin LANG=C.UTF-8 LC_ALL=C.UTF-8 TZ=UTC /usr/bin/python3.10 -I -S -B '+str(A/'receive_once.py'),
    'workdir':str(ROOT),'login':False,'yield_time_ms':1000,'max_output_tokens':7000}
    and tool['initial_result']['session_id']==16768 and tool['initial_result']['output']=='' and len(tool['polls'])==1
    and poll['request']=={'session_id':16768,'chars':'','yield_time_ms':1000,'max_output_tokens':7000}
    and poll['result']['exit_code']==0 and json.loads(poll['result']['output'])==summary,'complete actual independent tool correspondence')
rt=obj(HERE/'RECHECK_TOOL_NATIVE.json');rp=rt['polls'][0]
need(rt['result']['session_id']==84135 and rt['result']['output']=='' and len(rt['polls'])==1 and rp['result']['exit_code']==0
     and json.loads(rp['result']['output'])==obj(HERE/'RECHECK_RESULT.json'),'complete actual root tool correspondence')
cmpat=obj(HERE/'COMPARE_ATTEMPT.json');cmpn=obj(HERE/'COMPARE_NATIVE.json')
need(cmpat['argv']==['/usr/bin/cmp','--',str(A/'receiver.stdout.raw'),str(HERE/'recheck.stdout.raw')]
     and all(cmpn[k]==v for k,v in cmpat.items()) and type(cmpn['native_exit_code']) is int and cmpn['native_exit_code']==0
     and cmpn['started_epoch']<=cmpn['ended_epoch'] and read(HERE/'compare.stdout.raw')==read(HERE/'compare.stderr.raw')==b''
     and cmpn['stdout']==cmpn['stderr']==pin(b''),'actual whole raw native comparison')
validation=obj(A/'VALIDATION_NATIVE.json');v=json.loads(validation['initial_result']['output'])
need(validation['initial_result']['exit_code']==0 and validation['polls']==[] and v['checks']==13763
     and v['receiver_raw_stdout']==pin(raw) and v['receiver_rich_current_paths']==2763 and v['controller_rich_current_paths']==13,
     'actual original complete post-reception validation; source fully read separately')
initial=obj(A/'INITIAL_PIN_NATIVE.json')['record']
need(initial['result']['exit_code']==0,'actual initial hash request')
for line in initial['result']['output'].splitlines():
    h,n=line.split('  ',1);need(pin(read(ROOT/n))['sha256']==h,'actual original initial pin rows')
outer=obj(HERE/'OUTER_RECEPTION_NATIVE01.json')
o=json.loads(outer['result']['output'])
need(outer['result']['exit_code']==0 and o['checks']==430 and o['read_paths']==60,'actual root outer/host record reception')
for p,key in o['inputs'].items():need(pin(read(p))==key,('unchanged received outer provenance',p))
links=[]
for name in ('PLAN.md','RECEPTION.md'):
    for href in re.findall(r'!?\[[^\]\n]*\]\(([^)\n]+)\)',read(A/name).decode()):
        need(not re.match(r'[A-Za-z][A-Za-z0-9+.-]*:',href),'bounded package-local link')
        target=(A/href.split('#',1)[0]).resolve();need(target.is_relative_to(A) and target.is_file(),'complete local receipt links')
        read(target);links.append(href)
need(len(links)==17,'all receipt local links')
for p,key in dict(READS).items():need(pin(read(p))==key,('entire final original byte key',p))
result={'status':'PASS_ROOT_COMPLETE_ROUND1_ORIGINAL_RECEPTION','checks':CHECKS,'read_paths':len(READS),
    'independent_payloads':19,'independent_receiver_checks':108176,'root_reused_receiver_checks':108176,
    'complete_raw_bytes':len(raw),'raw_cmp_native_exit':0,'receiver_rich_paths':2763,'controller_rich_paths':13,
    'outer_host_reception_checks':430,'copied_payloads':83,'copied_files_with_manifest':84,
    'new_scientific_executions':0,'new_builds':0,'new_page_views':0,'new_manuscript_reviews':0,
    'paper_complete':False,'external':'HOLD_EXTERNAL','inputs':READS}
with (HERE/'ORIGINALS_RESULT.json').open('x') as stream:
    json.dump(result,stream,sort_keys=True,indent=2);stream.write('\n')
print(json.dumps({k:v for k,v in result.items() if k!='inputs'},sort_keys=True))
