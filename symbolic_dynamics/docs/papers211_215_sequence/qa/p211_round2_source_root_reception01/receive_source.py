#!/usr/bin/python3.10
"""Receive prepared source and independent metadata audit; no operational use."""
from hashlib import sha256
import json
import os
from pathlib import Path
import re
import shlex
import stat
import subprocess

ROOT=Path('/root/autodl-tmp/symbolic_dynamics')
HERE=Path(__file__).absolute().parent
PREP=ROOT/'docs/papers211_215_sequence/qa/p211_round2_preparation01'
AUDIT=ROOT/'docs/papers211_215_sequence/qa/p211_round2_source_audit01'
ENV={'PATH':'/usr/bin:/bin','LANG':'C.UTF-8','LC_ALL':'C.UTF-8','TZ':'UTC'}
inputs,checks,commands={},[],[]

def need(ok,label):
    checks.append(label)
    if not ok: raise AssertionError(label)

def bytepin(raw): return {'bytes':len(raw),'sha256':sha256(raw).hexdigest()}

def get(p):
    p=Path(p); a=p.lstat()
    need(stat.S_ISREG(a.st_mode) and p.resolve()==p,('ordinary original',str(p)))
    raw=p.read_bytes(); b=p.lstat()
    fs=('st_mode','st_dev','st_ino','st_nlink','st_uid','st_gid','st_size','st_mtime_ns','st_ctime_ns')
    aa,bb=({k:getattr(s,k) for k in fs} for s in (a,b))
    need(aa==bb and len(raw)==a.st_size,('stable original read',str(p)))
    return raw,{**bytepin(raw),'stat':bb}

def read(p):
    raw,key=get(p); p=str(p)
    need(p not in inputs or inputs[p]==key,('unchanged repeated original',p))
    inputs[p]=key
    return raw

def obj(p): return json.loads(read(p))

def pin(p): return bytepin(read(p))

def sums(raw):
    need(raw.endswith(b'\n'),'manifest newline')
    rows={}
    for line in raw.decode().splitlines():
        m=re.fullmatch(r'([0-9a-f]{64})  (.+)',line);need(m is not None,'manifest syntax')
        h,n=m.groups();need(n not in rows and not Path(n).is_absolute() and '..' not in Path(n).parts,'unique relative manifest')
        rows[n]=h
    return rows

def native(argv,cwd=ROOT):
    need(argv[0] in ('/usr/bin/sha256sum','/usr/bin/node'),'documentary native only')
    read(Path(argv[0]).resolve())
    request={'argv':argv,'cwd':str(cwd),'environment':ENV,'stdin':'DEVNULL','timeout_seconds':40}
    label='%02d'%len(commands)
    with (HERE/('COMMAND_'+label+'_ATTEMPT.json')).open('xb') as f:f.write((json.dumps(request,sort_keys=True,indent=2)+'\n').encode())
    actual=subprocess.run(argv,cwd=cwd,env=ENV,stdin=subprocess.DEVNULL,capture_output=True,timeout=40)
    for name,raw in (('stdout',actual.stdout),('stderr',actual.stderr)):
        with (HERE/('COMMAND_'+label+'_'+name+'.raw')).open('xb') as f:f.write(raw)
    record={**request,'exit_code':actual.returncode,'stdout':bytepin(actual.stdout),'stderr':bytepin(actual.stderr),'label':label}
    with (HERE/('COMMAND_'+label+'_NATIVE.json')).open('xb') as f:f.write((json.dumps(record,sort_keys=True,indent=2)+'\n').encode())
    commands.append(record)
    need(actual.returncode==0 and actual.stderr==b'',('actual documentary native',label))
    return actual.stdout

def package(base,count,seal):
    need(pin(base/'SHA256SUMS')['sha256']==seal,('literal seal',str(base)))
    rows=sums(read(base/'SHA256SUMS'))
    need(len(rows)==count and 'SHA256SUMS' not in rows,'nonself payload census')
    seen=set();dirs={'.'}
    for p in base.rglob('*'):
        need(p.resolve()==p and not p.is_symlink(),'no original tree aliases')
        n=str(p.relative_to(base))
        if p.is_file():seen.add(n)
        else:need(p.is_dir(),'ordinary package entry');dirs.add(n)
    need(seen==set(rows)|{'SHA256SUMS'},'complete original file inventory')
    want={'.'}
    for n in seen:want.update(str(p) for p in Path(n).parents)
    need(dirs==want,'complete directory inventory without extras')
    for n,h in rows.items():need(pin(base/n)['sha256']==h,('complete payload hash',str(base),n))
    need(native(['/usr/bin/sha256sum','-c','SHA256SUMS'],base)==''.join(n+': OK\n' for n in rows).encode(),'complete actual native manifest stream')
    return rows

def envelope(r):
    need(isinstance(r['request'],dict) and isinstance(r['request']['cmd'],str),'original native request dictionary')
    x=r['result'];need(type(x['exit_code']) is int and isinstance(x['output'],str) and isinstance(x['chunk_id'],str) and 'session_id' not in x,'actual completed envelope')
    return x

def receive_diff(row):
    r=envelope(row);need(r['exit_code']==1,'native changed-source diff exit')
    args=shlex.split(row['request']['cmd']);need(args[:2]==['diff','-u'],'literal source diff')
    names=[n for n in args[2:] if n!='--'];need(len(names)==2,'two actual source files')
    old,new=(read(ROOT/n).splitlines(keepends=True) for n in names)
    lines=r['output'].encode().splitlines(keepends=True)
    need(lines[0].startswith(('--- '+names[0]+'\t').encode()) and lines[1].startswith(('+++ '+names[1]+'\t').encode()),'exact diff source header roles')
    # Header timestamps are preserved unchanged as archival bytes. Hunk bodies
    # are fully checked against both actual file versions, not normalized text.
    i,oi,ni,hunks=2,0,0,0
    while i<len(lines):
        m=re.match(rb'@@ -(\d+)(?:,(\d+))? \+(\d+)(?:,(\d+))? @@',lines[i]);need(m is not None,'complete hunk header')
        os_,oc,ns,nc=int(m[1]),int(m[2] or b'1'),int(m[3]),int(m[4] or b'1')
        ostart=os_-1 if oc else os_;nstart=ns-1 if nc else ns
        need(old[oi:ostart]==new[ni:nstart],'all omitted unchanged intervals')
        oi,ni=ostart,nstart;i+=1;od,nd=0,0
        while i<len(lines) and not lines[i].startswith(b'@@ '):
            tag,body=lines[i][:1],lines[i][1:]
            need(tag in (b' ',b'-',b'+'),'exact ordinary newline-terminated diff body')
            if tag in (b' ',b'-'):need(oi<len(old) and old[oi]==body,'actual complete old hunk bytes');oi+=1;od+=1
            if tag in (b' ',b'+'):need(ni<len(new) and new[ni]==body,'actual complete new hunk bytes');ni+=1;nd+=1
            i+=1
        need((od,nd)==(oc,nc),'declared whole hunk counts');hunks+=1
    need(old[oi:]==new[ni:] and hunks>0,'complete diff tail')
    return {'sources':names,'hunks':hunks,'raw_stdout':bytepin(r['output'].encode())}

read(Path(__file__).absolute())
prep=package(PREP,22,'41a9e4a8203acee181b91e21e6985e521d43a1c303f7a697bfdb5d9306a60d21')
audit=package(AUDIT,8,'65b5689878baf206f92c4d31d39bae432d044187f89f75f7548a388e1eafe7ae')
external=sums(read(AUDIT/'INPUTS.sha256'));need(len(external)==187,'complete independent external pin census')
for n,h in external.items():need(pin(ROOT/n)['sha256']==h,('actual independent external original',n))
expected_pin_output=''.join(n+': OK\n' for n in external).encode()
need(native(['/usr/bin/sha256sum','-c',str((AUDIT/'INPUTS.sha256').relative_to(ROOT))])==expected_pin_output,'full actual 187-file native pin stream')
stored=obj(AUDIT/'NATIVE_CHECKS.json')['records']
need(len(stored)==4 and all(envelope(r)['exit_code']==0 for r in stored),'all original independent checks')
old=next(r for r in stored if r['key']=='r2audit_metadata_check01')
old_result=json.loads(old['result']['output'])
need(old_result['check_count']==924 and old_result['status']=='METADATA_CHECKS_PASS_NOT_OPERATIONAL_AUTHORIZATION' and all(r['ok'] for r in old_result['checks']),'actual full independent documentary result')
for n,p in old_result['actual_scoped_input_pins'].items():need(pin(ROOT/n)==p,('whole original checker input key',n))
actual=native(['/usr/bin/node',str((AUDIT/'audit_metadata.js').relative_to(ROOT))])
need(actual==old['result']['output'].encode(),'disclosed reuse: entire actual original checker stdout bytes')
need(json.loads(actual)==old_result,'same complete documentary checks no semantic truncation')
diffs=obj(AUDIT/'NATIVE_DIFFS.json')
need(len(diffs['complete_records'])==6,'six independent full source diffs')
diff_result=[receive_diff(r) for r in diffs['complete_records']]
prepared=obj(PREP/'NATIVE_SOURCE_DIFFS.json')['records']
need(len(prepared)==6,'six preparation source diffs')
for a,b in zip(prepared,diffs['complete_records']):need(envelope(a)['exit_code']==1 and a['result']['output']==b['result']['output'],'both actual full native diff streams identical')
closing=obj(PREP/'NATIVE_CLOSING_METADATA.json')
for r in closing['full_actual_final_source_reads']:
    result=envelope(r);m=re.fullmatch(r"sed -n '1,2000p' '([^']+)'",r['request']['cmd']);need(m is not None,'exact preparation source-read command')
    need(result['exit_code']==0 and result['output'].encode()==read(ROOT/m[1]),'entire actual preparation source bytes')
recorded=obj(AUDIT/'NATIVE_READS.json')['records'];need(len(recorded)==24,'whole independent selected read census')
source_bindings=[]
for r in recorded:
    result=envelope(r);need(result['exit_code']==0,'actual independent read exit')
    command=r['request']['cmd']
    if command.startswith('nl -ba '):
        assembled=b''
        for command_line in command.splitlines():
            m=re.fullmatch(r"nl -ba (\S+)(?: \| sed -n '(\d+),(\d+)p')?",command_line);need(m is not None,'exact numbered source read')
            raw=read(ROOT/m[1]);lines=raw.splitlines(keepends=True)
            numbered=[('%6d\t'%(i+1)).encode()+line for i,line in enumerate(lines)]
            if m[2]:numbered=numbered[int(m[2])-1:int(m[3])]
            assembled+=b''.join(numbered)
        need(result['output'].encode()==assembled,'entire independent numbered source output bytes')
        source_bindings.append(r['key'])
    elif command.startswith('cat ') and 'STATE' not in command:
        names=shlex.split(command)[1:]
        need(result['output'].encode()==b''.join(read(ROOT/n) for n in names),'entire independent plain original concatenation')
        source_bindings.append(r['key'])
close=obj(AUDIT/'CLOSING_NATIVE.json')
need(envelope(close['records'][0])['output'].encode()==expected_pin_output,'actual independent final 187-pin native output')
own=json.loads(envelope(close['records'][1])['output'])
for n,p in own['pins'].items():need(pin(AUDIT/n)==p,'all actual seven preseal own originals unchanged')
counts=obj(AUDIT/'FINDINGS.json')
need(counts['counts']=={'C':0,'M':0,'m':0} and counts['findings']==[] and counts['recommendation']=='GO_SOURCE_RECEPTION_AND_BINDING_PREPARATION_ONLY','actual zero confirmed source findings and limited recommendation')
before=dict(inputs);after={p:get(Path(p))[1] for p in sorted(before)}
need(before==after,'entire source/audit original rich key unchanged')
result={'status':'P211_ROUND2_SOURCE_AND_INDEPENDENT_AUDIT_RECEIVED_NOT_OPERATIONAL_AUTHORITY',
        'checks':len(checks),'check_labels':checks,'rich_paths':len(before),'inputs_before':before,'inputs_after':after,
        'preparation_payloads':22,'audit_payloads':8,'audit_total_bytes':sum(inputs[str(AUDIT/n)]['bytes'] for n in (*audit,'SHA256SUMS')),
        'original_independent_checks':924,'reused_full_output':bytepin(actual),'native_commands':commands,
        'full_source_diffs':diff_result,'independent_source_read_bindings':source_bindings,
        'scientific_executions':0,'submitted_source_executions':0,'host_reuse_acceptance':False,'physical_round2':False,
        'terminal_builds':0,'page_views':0,'external':'OWNER_AMBER / HOLD_EXTERNAL'}
with (HERE/'RESULT.json').open('xb') as f:f.write((json.dumps(result,sort_keys=True,indent=2)+'\n').encode())
print(json.dumps(result,sort_keys=True))
