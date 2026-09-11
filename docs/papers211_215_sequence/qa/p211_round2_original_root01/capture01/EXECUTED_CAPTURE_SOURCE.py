#!/usr/bin/python3.10
"""Unexecuted capture preparation; disclosed derivative of root recheck.py.

One separately authorized invocation of the unchanged stdout-only receiver.
No recorder, science, build, extra native comparison or helper import occurs.
All rich metadata is parsed/compared as Python integers, never via JavaScript.
Only prior803 exact host aliases may be read; no host directory is scanned.
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

ROOT=Path('/root/autodl-tmp/symbolic_dynamics')
QA=ROOT/'docs/papers211_215_sequence/qa'
C=QA/'p211_round2_original_capture_preparation01'
P=QA/'p211_round2_original_receiver_preparation01'
A=QA/'p211_round2_physical_independent01'
R=QA/'p211_round2_root_reception01'
DEST=QA/'p211_round2_original_root01'
OUT=DEST/'capture01'
AUTH=DEST/'AUTHORITY.md'
SOURCE=P/'receive_originals.py'
SELF=C/'capture_originals.py'
ENV={'PATH':'/usr/bin:/bin','LANG':'C.UTF-8','LC_ALL':'C.UTF-8','TZ':'UTC'}
ARGV=['/usr/bin/python3.10','-I','-S','-B',str(SOURCE)]
SOURCE_PIN={'bytes':40810,'sha256':'b18694cdfbfbb204814428ebf95330449080a7a954cc81d0251b508f1fbb3bcd'}
P_SEAL={'bytes':347,'sha256':'4d53e0b2ab6fdf01616db7d5cfe74093b18b2da547df69e172092a0ee3d253f7'}
OLD_KEY={'bytes':4197613,'sha256':'2b787b6114c88ca2a77972c3cca562e1a0fa6d77febed55f569f52bf097a611f'}
P_NAMES={'receive_originals.py','ORIGINAL_PINS.json','SOURCE_METADATA.md','PREPARATION_NATIVE.json','SHA256SUMS'}
C_NAMES={'capture_originals.py','DERIVATION.diff','DERIVATION_NATIVE.json','DISABLED_SPEC.json',
         'SOURCE_METADATA.md','ORIGINAL_PINS.json','PREPARATION_NATIVE.json','SHA256SUMS'}
READS={}
HOST=set()
CHECKS=0
ACTIVE=False

def need(ok,label):
    global CHECKS
    CHECKS+=1
    if not ok:
        raise AssertionError(label)

def pin(raw):
    return {'bytes':len(raw),'sha256':sha256(raw).hexdigest()}

def meta(s):
    return {k:getattr(s,'st_'+v) for k,v in (
        ('mode','mode'),('device','dev'),('inode','ino'),('uid','uid'),('gid','gid'),
        ('nlink','nlink'),('size','size'),('mtime_ns','mtime_ns'),('ctime_ns','ctime_ns'))}

def rich(p):
    p=Path(p)
    need(p.is_absolute() and (p.is_relative_to(ROOT) or str(p) in HOST),'exact allowed input alias')
    ls,st=p.lstat(),p.stat()
    need(stat.S_ISREG(st.st_mode),'ordinary resolved input')
    resolved=str(p.resolve(strict=True))
    link=os.readlink(p) if stat.S_ISLNK(ls.st_mode) else None
    if p.is_relative_to(ROOT):
        need(resolved==str(p) and link is None,'ordinary workspace original')
    raw=p.read_bytes()
    value={**pin(raw),'resolved':resolved,'symlink':link,'stat':meta(st),'lstat':meta(ls)}
    need(meta(p.lstat())==value['lstat'] and meta(p.stat())==value['stat'] and
         str(p.resolve(strict=True))==resolved and len(raw)==st.st_size,'whole rich read stable')
    need(str(p) not in READS or READS[str(p)]==value,('whole repeated input key',str(p)))
    READS[str(p)]=value
    return raw,value

def read(p):
    return rich(p)[0]

def obj(p):
    return json.loads(read(p))

def rich_schema(v):
    need(set(v)=={'bytes','sha256','resolved','symlink','stat','lstat'},'full rich schema')
    need(type(v['bytes']) is int and v['bytes']>=0 and isinstance(v['sha256'],str) and
         re.fullmatch('[0-9a-f]{64}',v['sha256']) is not None,'exact byte pin schema')
    need(isinstance(v['resolved'],str) and Path(v['resolved']).is_absolute() and
         (v['symlink'] is None or isinstance(v['symlink'],str)),'full resolution schema')
    for field in ('stat','lstat'):
        need(set(v[field])=={'mode','device','inode','uid','gid','nlink','size','mtime_ns','ctime_ns'} and
             all(type(n) is int for n in v[field].values()),'all stat fields are exact Python integers')

def put(name,value):
    need(ACTIVE and '/' not in name,'exclusive flat new capture output only')
    raw=value if isinstance(value,bytes) else (json.dumps(value,sort_keys=True,indent=2)+'\n').encode()
    with (OUT/name).open('xb') as f:
        f.write(raw)
        f.flush()
        os.fsync(f.fileno())

def tree(base,names):
    actual=set()
    ids=set()
    for p in base.rglob('*'):
        s=p.lstat()
        need(not stat.S_ISLNK(s.st_mode) and (stat.S_ISDIR(s.st_mode) or stat.S_ISREG(s.st_mode)),
             'ordinary complete workspace tree')
        if stat.S_ISREG(s.st_mode):
            need(s.st_nlink==1 and (s.st_dev,s.st_ino) not in ids,'separate ordinary payload inode')
            ids.add((s.st_dev,s.st_ino))
            actual.add(str(p.relative_to(base)))
    need(actual==set(names),('whole exact original file membership',str(base)))
    expected_dirs={str(p) for n in names for p in Path(n).parents if str(p)!='.'}
    need({str(p.relative_to(base)) for p in base.rglob('*') if p.is_dir()}==expected_dirs,'whole exact directory membership')

def sealed(base,names,expected):
    tree(base,names)
    raw=read(base/'SHA256SUMS')
    need(pin(raw)==expected and raw.endswith(b'\n'),'whole original preparation seal')
    found={}
    for line in raw.decode().splitlines():
        m=re.fullmatch(r'([0-9a-f]{64})  (.+)',line)
        need(m is not None,'complete seal grammar')
        h,n=m.groups()
        need(n in names-{'SHA256SUMS'} and n not in found,'exact nonself payload')
        need(pin(read(base/n))['sha256']==h,('whole sealed payload',n))
        found[n]=h
    need(set(found)==names-{'SHA256SUMS'} and
         raw==''.join(found[n]+'  '+n+'\n' for n in sorted(found)).encode(),'entire sorted nonself seal')
    return raw

def original_trees(pins):
    for base,count in ((A,76),(R,19)):
        names={str(Path(p).relative_to(base)) for p in pins if Path(p).is_relative_to(base)}
        need(len(names)==count,'exact original package census')
        tree(base,names)

def check_inputs(old,preparation,expected):
    for p,v in old.items():
        rich_schema(v)
        need(rich(p)[1]==v,('complete historical4896 key',p))
    for p,v in preparation['pins'].items():
        need(pin(read(p))==v,('complete107 original workspace byte pins',p))
    for p in sorted(expected):
        rich(p)
    original_trees(preparation['pins'])
    sealed(P,P_NAMES,P_SEAL)
    need(pin(read(SOURCE))==SOURCE_PIN,'entire unchanged original receiver source')

def invoke():
    executable=rich(ARGV[0])[1]
    attempt={'argv':ARGV,'cwd':str(ROOT),'environment':ENV,'stdin':'subprocess.DEVNULL',
        'timeout_seconds':180,'started_epoch_ns':time.time_ns(),'executable_full_key':executable,
        'source_pin':SOURCE_PIN,'capture_source_pin':pin(read(SELF)),'authority_pin':pin(read(AUTH)),
        'scope':'one stdout-only original receiver; no recorder/science/build/helper import'}
    put('01_receiver.ATTEMPT.json',attempt)
    code,error,state=None,None,'captured'
    try:
        result=subprocess.run(ARGV,cwd=ROOT,env=ENV,stdin=subprocess.DEVNULL,capture_output=True,timeout=180)
        out,err,code=result.stdout,result.stderr,result.returncode
    except subprocess.TimeoutExpired as e:
        out,err=e.stdout or b'',e.stderr or b''
        error={'type':type(e).__name__,'message':str(e)}
        state='partial_at_timeout; no exit invented'
    except OSError as e:
        out,err=b'',b''
        error={'type':type(e).__name__,'message':str(e)}
        state='launch_failed_or_unknown; no exit invented'
    put('01_receiver.stdout.raw',out)
    put('01_receiver.stderr.raw',err)
    native={**attempt,'ended_epoch_ns':time.time_ns(),'native_exit_code':code,'exception':error,
            'stream_capture_status':state,'stdout':pin(out),'stderr':pin(err)}
    put('01_receiver.NATIVE.json',native)
    need(rich(ARGV[0])[1]==executable,'entire native executable key closes')
    return out,err,native

def result_scope(whole,expected):
    fixed={'status':'PASS_ORIGINAL_PHYSICAL_DOCUMENTARY_CLOSURE_PENDING_ROOT_DECISION',
        'read_paths':4917,'independent_payloads':75,'independent_files':76,'all_attempt_original_rich_paths':4829,
        'root_before_after_rich_paths':4896,'external_original_input_rows':4820,'closing_native_commands':4,
        'closing_saved_checks':60196,'closing_outer_checks':60198,'preseal_payloads':74,'selected_native_reads':36,
        'final_closing_records':5,'new_science':0,'new_builds':0,'new_page_views':0,'new_helper_or_shell_subprocesses':0,
        'new_independent_physical_design':False,'root_acceptance':False,'terminal_authority':False,
        'paper_complete':False,'external':'OWNER_AMBER / HOLD_EXTERNAL'}
    extras={'checks','preserved_attempts','complete_source_bindings','actual_root_recheck','actual_outer_envelopes',
            'current_report_links','whole_independent_seal','whole_independent_stdout','READ_INPUTS'}
    need(set(whole)==set(fixed)|extras and all(type(whole[k]) is type(v) and whole[k]==v for k,v in fixed.items()),
         'all exact receiver result fields and authority limits')
    need(type(whole['checks']) is int and whole['checks']>0,'actual receiver checks not pre-invented')
    closing=obj(A/'closing01/RESULT.json')
    need(whole['preserved_attempts']==closing['attempts'] and len(whole['preserved_attempts'])==5,
         'all5 exact historical attempt records and failure points')
    need(whole['complete_source_bindings']==closing['complete_source_bindings'] and
         len(whole['complete_source_bindings'])==9,'all9 entire source-read bindings')
    need(whole['actual_root_recheck']==obj(R/'RECHECK_RESULT.json'),'whole actual previous root result')
    need(whole['whole_independent_seal']==pin(read(A/'SHA256SUMS')) and
         whole['whole_independent_stdout']==pin(read(A/'run05/CHECKS.stdout.raw')),'entire original seal/raw output pins')
    reads=obj(A/'NATIVE_READS.json')['records']
    closes=obj(A/'CLOSING_NATIVE.json')['records']
    read_ids=[r['record_id'] for r in reads]
    close_ids=[r['record_id'] for r in closes]
    labels=['original_R1_derivation','original_static_check']+['original_correction_'+str(i) for i in range(1,5)]+[
        'original_root_capture_correction']+['actual_attempt_'+str(i) for i in range(1,6)]+[
        'selected_read_'+n for n in read_ids]+['closing_'+n for n in close_ids]+[
        'actual_root_complete_recheck','actual_root_truncated_closing_navigation']
    envelopes=whole['actual_outer_envelopes']
    need(len(read_ids)==36 and len(close_ids)==5 and len(labels)==len(envelopes)==55 and
         [e['label'] for e in envelopes]==labels,'all55 native envelopes in complete original order')
    derivation=obj(A/'DERIVATION_NATIVE.json')
    corrections=obj(A/'CORRECTIONS_NATIVE.json')
    records=[derivation['record'],derivation['own_static'],*corrections['source_diffs'],
        corrections['root_actual_capture_correction'],*corrections['attempts'],*reads,*closes,
        obj(R/'RECHECK_TOOL_NATIVE.json'),obj(R/'NAVIGATION_TRUNCATED_CLOSING_READ.json')]
    need(len(records)==55,'all55 actual original native records consumed')
    exit1=set(labels[:1]+labels[2:11]+['selected_read_capture_correction_diff',
              'closing_failed_preseal_saved_vs_outer_count'])
    for e,record in zip(envelopes,records):
        label=e['label']
        need(set(e)=={'label','exit_code','polls','truncated','request_pin','whole_saved_output'},'whole envelope projection')
        need(type(e['exit_code']) is int and e['exit_code']==(2 if label=='selected_read_paths' else 1 if label in exit1 else 0),
             'all actual historical exits including four receiver failures')
        need(type(e['polls']) is int and e['polls']>=0 and type(e['truncated']) is bool and
             e['truncated']==(label in {'selected_read_paths','actual_root_truncated_closing_navigation'}),
             'only two exact historical truncation exceptions')
        returns=[record['result']]+[p['result'] for p in record.get('polls',[])]
        need(e=={'label':label,'exit_code':returns[-1]['exit_code'],'polls':len(returns)-1,
            'truncated':returns[0]['output'].startswith('Warning: truncated output'),
            'request_pin':pin(json.dumps(record['request'],sort_keys=True).encode()),
            'whole_saved_output':pin(''.join(r['output'] for r in returns).encode())},
            'entire native projection binds all actual request/result/poll bytes')
        for field in ('request_pin','whole_saved_output'):
            v=e[field]
            need(set(v)=={'bytes','sha256'} and type(v['bytes']) is int and v['bytes']>=0 and
                 re.fullmatch('[0-9a-f]{64}',v['sha256']) is not None,'entire native output/request pin schema')
    links=[]
    for href in re.findall(r'\[[^\]]*\]\(([^)]+)\)',read(A/'REPORT.md').decode()):
        if re.match(r'^[a-z]+:',href):
            continue
        p=(A/href.split('#',1)[0]).resolve(strict=True)
        need(str(p) in expected,'exact already-closed current report target')
        links.append({'href':href,'path':str(p),'pin':pin(read(p))})
    need(whole['current_report_links']==links,'all current ordered report link closures')
    key=whole['READ_INPUTS']
    need(len(key)==4917 and set(key)==expected,'complete independently enumerated receiver read scope')
    for p,v in key.items():
        rich_schema(v)
        need(v==READS[p]==rich(p)[1],('entire helper rich key equals exact capture pre/post',p))

def main():
    global HOST,ACTIVE
    need(Path.cwd()==ROOT and dict(os.environ)==ENV and Path(__file__).absolute()==SELF,
         'exact original capture path/cwd and literal ENV4')
    need(sys.executable=='/usr/bin/python3.10' and sys.version_info[:2]==(3,10) and
         sys.flags.isolated==sys.flags.no_site==sys.flags.dont_write_bytecode==1,
         'actual isolated Python3.10 capture flags')
    need(len(sys.argv)==4 and sys.argv[1]==str(AUTH) and re.fullmatch('[1-9][0-9]*',sys.argv[2]) and
         re.fullmatch('[0-9a-f]{64}',sys.argv[3]),'required exact authority path/bytes/hash CLI binding')
    authority=read(AUTH)
    need(pin(authority)=={'bytes':int(sys.argv[2]),'sha256':sys.argv[3]},'entire root authority CLI byte pin')
    blocks=re.findall(r'^```json\n(.*?)\n```$',authority.decode(),re.MULTILINE|re.DOTALL)
    need(len(blocks)==1,'one exact root authority JSON block')
    grant=json.loads(blocks[0])
    own_source=read(SELF)
    expected_grant={'schema':'p211-round2-original-root-one-use-v1','authorized':True,'one_use':True,
        'capture_source':str(SELF),'capture_source_pin':pin(own_source),
        'capture_preparation_seal':pin(read(C/'SHA256SUMS')),'receiver_source':str(SOURCE),
        'receiver_source_pin':SOURCE_PIN,'receiver_preparation_seal':P_SEAL,
        'output':str(OUT),'argv':ARGV,'cwd':str(ROOT),'environment':ENV,'timeout_seconds':180,
        'new_science':0,'new_builds':0,'new_page_views':0,'terminal_authority':False,
        'physical_acceptance':False,'paper_complete':False,'external':'OWNER_AMBER / HOLD_EXTERNAL'}
    need(json.dumps(grant,sort_keys=True)==json.dumps(expected_grant,sort_keys=True),
        'entire finite root grant semantics; no substituted source or broadened action')
    need(DEST.is_dir() and DEST.resolve(strict=True)==DEST and not DEST.is_symlink(),'ordinary root-owned parent')
    OUT.mkdir(mode=0o700,parents=False,exist_ok=False)
    ACTIVE=True
    put('EXECUTED_CAPTURE_SOURCE.py',own_source)
    put('EXECUTED_RECEIVER_SOURCE.py',read(SOURCE))
    put('AUTHORITY.snapshot.md',authority)
    sealed(C,C_NAMES,grant['capture_preparation_seal'])
    sealed(P,P_NAMES,P_SEAL)
    preparation=obj(P/'ORIGINAL_PINS.json')
    need(preparation['schema']=='p211-root-original-receiver-preparation-byte-pins-v1' and
         preparation['entries']==len(preparation['pins'])==107 and preparation['independent_files']==76 and
         preparation['root_recheck_files']==19 and preparation['explicit_extra_workspace_files']==12 and
         all(Path(p).is_absolute() and Path(p).is_relative_to(ROOT) for p in preparation['pins']),
         'all107 exact original workspace preparation pins')
    before_raw,after_raw=read(R/'RECHECK_INPUTS_BEFORE.json'),read(R/'RECHECK_INPUTS_AFTER.json')
    need(before_raw==after_raw and pin(before_raw)==OLD_KEY,'both entire historical4896 raw input keys')
    old=json.loads(before_raw)
    passing=obj(A/'run05/CHECKS.stdout.raw')
    HOST={p for p in old if not Path(p).is_relative_to(ROOT)}
    need(len(old)==4896 and len(HOST)==803 and HOST=={p for p in passing['READ_INPUTS'] if not Path(p).is_relative_to(ROOT)},
         'only same exact803 prior host aliases; no host directory discovery')
    expected=set(old)|set(preparation['pins'])|{str(SOURCE),str(P/'ORIGINAL_PINS.json')}
    need(len(expected)==4917 and set(ARGV[:1])<=HOST,'whole independently enumerated4917 receiver scope and executable alias')
    check_inputs(old,preparation,expected)
    prior=dict(READS)
    need(len(prior)==4929,'complete capture original rich scope including both preparations and authority')
    put('CAPTURE_INPUTS_BEFORE.json',prior)
    put('SOURCE_METADATA.json',{'capture':{'path':str(SELF),'pin':pin(own_source),'rich_key':prior[str(SELF)]},
        'receiver':{'path':str(SOURCE),'pin':SOURCE_PIN,'rich_key':prior[str(SOURCE)]},
        'authority':{'path':str(AUTH),'pin':pin(authority),'rich_key':prior[str(AUTH)]},
        'receiver_preparation_seal':P_SEAL,'capture_preparation_seal':grant['capture_preparation_seal'],
        'expected_receiver_read_paths':4917,'whole_historical_read_paths':4896,'exact_original_host_aliases':803})
    out,err,native=invoke()
    check_inputs(old,preparation,expected)
    sealed(C,C_NAMES,grant['capture_preparation_seal'])
    for p,v in prior.items():
        need(rich(p)[1]==v,('entire capture key post-execution closure',p))
    need(READS==prior,'entire before/after capture rich key exactly unchanged')
    put('CAPTURE_INPUTS_AFTER.json',READS)
    need(native['exception'] is None and type(native['native_exit_code']) is int and
         native['native_exit_code']==0 and native['stream_capture_status']=='captured' and err==b'',
         'actual sole receiver complete native success; any failed raw/native already preserved')
    whole=json.loads(out)
    result_scope(whole,expected)
    need(READS==prior,'all returned helper-key validation reads were pre-bound and stable')
    put('RECEIVER_RESULT.json',{k:v for k,v in whole.items() if k!='READ_INPUTS'})
    put('RECEIVER_INPUTS.json',whole['READ_INPUTS'])
    result={'status':'PASS_ROOT_ORIGINAL_RECEIVER_CAPTURE_PENDING_SEPARATE_ROOT_DECISION',
        'capture_checks':CHECKS,'capture_read_paths':len(READS),'receiver_checks':whole['checks'],
        'receiver_read_paths':4917,'whole_receiver_stdout':pin(out),'native_invocations':1,'native_exit_code':0,
        'independent_payloads':75,'independent_files':76,'original_root_files':19,'receiver_preparation_files':5,
        'original_workspace_pin_rows':107,'historical_root_rich_paths':4896,'exact_host_aliases':803,
        'historical_outer_envelopes':55,'source':SOURCE_PIN,'capture_source':pin(own_source),'authority':pin(authority),
        'new_science':0,'new_builds':0,'new_page_views':0,'new_independent_design':False,'root_acceptance':False,
        'terminal_authority':False,'paper_complete':False,'external':'OWNER_AMBER / HOLD_EXTERNAL'}
    put('CAPTURE_RESULT.json',result)
    return result

if __name__=='__main__':
    try:
        result=main()
    except Exception:
        result={'status':'FAIL_ORIGINAL_ROOT_CAPTURE_PRESERVE_ALL_ATTEMPTS','checks':CHECKS,
                'traceback':traceback.format_exc(),'READ_INPUTS_PARTIAL':READS,'capture_directory_created':ACTIVE}
        if ACTIVE:
            put('FAILURE.json',result)
        print(json.dumps(result,sort_keys=True))
        raise SystemExit(1)
    print(json.dumps(result,sort_keys=True))
