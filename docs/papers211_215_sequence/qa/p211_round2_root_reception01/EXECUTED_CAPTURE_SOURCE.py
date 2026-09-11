#!/usr/bin/python3.10
"""Root's explicit complete-source documentary reuse, never a recorder run.

The 1138-line receiver was fully read. This capture follows the accepted
Round1 recheck mechanism; source, whole original output, package membership,
all full rich input keys and actual raw comparison are bound independently.
All new outputs are exclusive in this new root directory. ENV4 is literal.
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
HERE=QA/'p211_round2_root_reception01'
A=QA/'p211_round2_physical_independent01'
SOURCE=A/'receive_physical05.py'
ENV={'PATH':'/usr/bin:/bin','LANG':'C.UTF-8','LC_ALL':'C.UTF-8','TZ':'UTC'}
READS={}
CHECKS=0
def need(x,label):
    global CHECKS
    CHECKS+=1
    if not x:
        raise AssertionError(label)
def pin(raw):
    return {'bytes':len(raw),'sha256':sha256(raw).hexdigest()}
def meta(s):
    return {k:getattr(s,'st_'+v) for k,v in (
        ('mode','mode'),('device','dev'),('inode','ino'),('uid','uid'),('gid','gid'),
        ('nlink','nlink'),('size','size'),('mtime_ns','mtime_ns'),('ctime_ns','ctime_ns'))}
def rich(p):
    p=Path(p)
    ls,st=p.lstat(),p.stat()
    need(stat.S_ISREG(st.st_mode),('ordinary resolved file',str(p)))
    resolved=str(p.resolve(strict=True))
    link=os.readlink(p) if stat.S_ISLNK(ls.st_mode) else None
    if p.is_relative_to(ROOT):
        need(resolved==str(p) and link is None,('ordinary workspace file',str(p)))
    raw=p.read_bytes()
    key={**pin(raw),'resolved':resolved,'symlink':link,'stat':meta(st),'lstat':meta(ls)}
    need(meta(p.lstat())==key['lstat'] and meta(p.stat())==key['stat'] and
         str(p.resolve(strict=True))==resolved and len(raw)==st.st_size,'whole rich read stable')
    need(str(p) not in READS or READS[str(p)]==key,('repeated original full key',str(p)))
    READS[str(p)]=key
    return raw,key
def read(p):
    return rich(p)[0]
def put(name,v):
    raw=v if isinstance(v,bytes) else (json.dumps(v,sort_keys=True,indent=2)+'\n').encode()
    with (HERE/name).open('xb') as f:
        f.write(raw)
        f.flush()
        os.fsync(f.fileno())
def package():
    raw=read(A/'SHA256SUMS')
    need(pin(raw)=={'bytes':6880,'sha256':'f1eac068f6f8dea79ae9cda7028b671a2d5e792af5836c2f15f84b0a09c82e39'},'entire final independent seal')
    rows={}
    need(raw.endswith(b'\n'),'full manifest LF')
    for line in raw.decode().splitlines():
        m=re.fullmatch(r'([0-9a-f]{64})  (.+)',line)
        need(m is not None,'manifest syntax')
        h,n=m.groups()
        need(n not in rows and n!='SHA256SUMS' and not Path(n).is_absolute() and
             all(x not in ('','.','..') for x in n.split('/')),'exact safe nonself membership')
        need(pin(read(A/n))['sha256']==h,('all independent payloads',n))
        rows[n]=h
    names=set()
    for p in A.rglob('*'):
        need(not p.is_symlink() and (p.is_dir() or p.is_file()),'ordinary complete independent tree')
        if p.is_file():
            names.add(str(p.relative_to(A)))
    need(len(rows)==75 and names==set(rows)|{'SHA256SUMS'},'all 75 payloads / 76 files')
    return raw
def command(label,argv,timeout):
    executable=rich(Path(argv[0]))[1]
    a={'argv':argv,'cwd':str(ROOT),'environment':ENV,'stdin':'subprocess.DEVNULL',
       'timeout_seconds':timeout,'started_epoch':time.time(),'executable_full_key':executable}
    put(label+'.ATTEMPT.json',a)
    error,code,state=None,None,'captured'
    try:
        r=subprocess.run(argv,cwd=ROOT,env=ENV,stdin=subprocess.DEVNULL,capture_output=True,timeout=timeout)
        out,err,code=r.stdout,r.stderr,r.returncode
    except subprocess.TimeoutExpired as e:
        out,err=e.stdout or b'',e.stderr or b''
        error={'type':type(e).__name__,'message':str(e)}
        state='partial_at_timeout; no exit invented'
    except OSError as e:
        out,err=b'',b''
        error={'type':type(e).__name__,'message':str(e)}
        state='launch_failed_or_unknown; no exit invented'
    put(label+'.stdout.raw',out)
    put(label+'.stderr.raw',err)
    n={**a,'ended_epoch':time.time(),'native_exit_code':code,'exception':error,'stream_capture_status':state,
       'stdout':pin(out),'stderr':pin(err)}
    put(label+'.NATIVE.json',n)
    need(error is None and type(code) is int and code==0 and err==b'',('actual complete native success',label))
    need(rich(Path(argv[0]))[1]==executable,'whole native tool unchanged')
    return out,n

need(Path.cwd()==ROOT and dict(os.environ)==ENV,'actual literal cwd and ENV4; no ambient collection')
read(Path(__file__).absolute())
read(HERE/'AUTHORITY.md')
put('EXECUTED_CAPTURE_SOURCE.py',read(Path(__file__).absolute()))
seal=package()
source=read(SOURCE)
need(pin(source)=={'bytes':77479,'sha256':'ad8bd8890f9d5415d2a0499485415cb42858eca9c48b04cdecaf7b9c4c0c0e9d'},'exact fully read receiver source')
raw=read(A/'run05/CHECKS.stdout.raw')
need(pin(raw)=={'bytes':3430632,'sha256':'ff715a36ffd80ada101e64bf39085606155d7ea3c87beefe80555910fee84fdc'},'entire actual independent output')
whole=json.loads(raw)
need(whole['checks']==488474 and whole['receiver_read_paths']==4821 and len(whole['READ_INPUTS'])==4821,'entire original physical input key')
allowed=set(whole['READ_INPUTS'])
for p,v in whole['READ_INPUTS'].items():
    need(rich(Path(p))[1]==v,('all accepted original rich rows before execution',p))
put('RECHECK_INPUTS_BEFORE.json',READS)
out,native=command('01_recheck',['/usr/bin/python3.10','-I','-S','-B',str(SOURCE)],180)
need(out==raw and json.loads(out)==whole,'entire original and recheck raw bytes and JSON identical')
compared,cmpnative=command('02_compare',['/usr/bin/cmp','--',str(A/'run05/CHECKS.stdout.raw'),str(HERE/'01_recheck.stdout.raw')],60)
need(compared==b'','actual native whole raw comparison')
for p,v in whole['READ_INPUTS'].items():
    need(rich(Path(p))[1]==v,('all accepted original rich rows after execution',p))
need(package()==seal and read(SOURCE)==source,'whole original seal/source unchanged after recheck')
for p,v in dict(READS).items():
    need(rich(Path(p))[1]==v,('complete root capture original key closes',p))
put('RECHECK_INPUTS_AFTER.json',READS)
result={'status':'PASS_ROOT_EXPLICIT_COMPLETE_PHYSICAL_RECEIVER_RECHECK_PENDING_ORIGINAL_RECEPTION',
        'root_capture_checks':CHECKS,'root_capture_read_paths':len(READS),'reused_receiver_checks':488474,
        'reused_receiver_read_paths':4821,'independent_payloads':75,'independent_files':76,
        'whole_raw_output':pin(out),'native_cmp_exit':cmpnative['native_exit_code'],
        'source':pin(source),'independent_seal':pin(seal),'new_science':0,'new_builds':0,'new_page_views':0,
        'paper_complete':False,'new_independent_design':False,'terminal_authority':False,
        'external':'OWNER_AMBER / HOLD_EXTERNAL'}
put('RECHECK_RESULT.json',result)
print(json.dumps(result,sort_keys=True))
