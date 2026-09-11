"""Root final documentary reception; no source/helper import or child process."""
from hashlib import sha256
import json
import os
from pathlib import Path
import re
import stat
ROOT=Path('/root/autodl-tmp/symbolic_dynamics')
Q=ROOT/'docs/papers211_215_sequence/qa'
H=Q/'p211_round2_original_root01'
C=H/'capture01'
P=Q/'p211_round2_original_capture_preparation01'
R=Q/'p211_round2_original_receiver_preparation01'
N=0
def need(v,label):
    global N
    N+=1
    if not v: raise AssertionError(label)
def pin(b): return {'bytes':len(b),'sha256':sha256(b).hexdigest()}
def meta(s):
    return {k:getattr(s,'st_'+v) for k,v in (('mode','mode'),('device','dev'),('inode','ino'),('uid','uid'),('gid','gid'),('nlink','nlink'),('size','size'),('mtime_ns','mtime_ns'),('ctime_ns','ctime_ns'))}
def rich(p):
    p=Path(p); ls,st=p.lstat(),p.stat();raw=p.read_bytes()
    need(stat.S_ISREG(st.st_mode),'ordinary resolved file')
    v={**pin(raw),'resolved':str(p.resolve(strict=True)),'symlink':os.readlink(p) if p.is_symlink() else None,'stat':meta(st),'lstat':meta(ls)}
    need(meta(p.lstat())==v['lstat'] and meta(p.stat())==v['stat'] and str(p.resolve(strict=True))==v['resolved'],'whole rich read stable')
    return raw,v
def obj(p): return json.loads(Path(p).read_bytes())
env={'PATH':'/usr/bin:/bin','LANG':'C.UTF-8','LC_ALL':'C.UTF-8','TZ':'UTC'}
need(Path.cwd()==ROOT and dict(os.environ)==env,'actual root final documentary environment')
before=(C/'CAPTURE_INPUTS_BEFORE.json').read_bytes()
need(before==(C/'CAPTURE_INPUTS_AFTER.json').read_bytes(),'entire pre/post raw key identical')
keys=json.loads(before)
need(len(keys)==4929 and sum(not Path(p).is_relative_to(ROOT) for p in keys)==803,'whole bound4929 and host803')
for p,v in keys.items(): need(rich(p)[1]==v,('complete current rich original',p))
spec=obj(P/'DISABLED_SPEC.json')
need(set(p.name for p in C.iterdir())==set(spec['successful_output_files']) and len(spec['successful_output_files'])==13,'entire thirteen-file actual capture')
files={}
for p in C.iterdir():
    need(p.is_file() and not p.is_symlink() and p.stat().st_nlink==1,'ordinary exclusive capture output')
    files[p.name]=pin(rich(p)[0])
for name,source in [('EXECUTED_CAPTURE_SOURCE.py',P/'capture_originals.py'),('EXECUTED_RECEIVER_SOURCE.py',R/'receive_originals.py'),('AUTHORITY.snapshot.md',H/'AUTHORITY.md')]:
    need((C/name).read_bytes()==source.read_bytes(),('whole actual captured source/authority',name))
out=(C/'01_receiver.stdout.raw').read_bytes();whole=json.loads(out)
need((C/'01_receiver.stderr.raw').read_bytes()==b'','actual receiver empty stderr')
returned=obj(C/'RECEIVER_INPUTS.json')
need(returned==whole['READ_INPUTS'] and len(returned)==4917,'whole receiver rich key')
for p,v in returned.items():need(v==keys[p],('every receiver original rich row',p))
need(obj(C/'RECEIVER_RESULT.json')=={k:v for k,v in whole.items() if k!='READ_INPUTS'},'entire saved receiver projection')
native=obj(C/'01_receiver.NATIVE.json');attempt=obj(C/'01_receiver.ATTEMPT.json')
need(all(native[k]==v for k,v in attempt.items()),'entire actual attempt/native fields')
need(native['native_exit_code']==0 and native['exception'] is None and native['stream_capture_status']=='captured','actual sole receiver native success')
need(native['stdout']==pin(out) and native['stderr']==pin(b'') and native['environment']==env and native['cwd']==str(ROOT) and native['stdin']=='subprocess.DEVNULL' and native['timeout_seconds']==180,'full actual native command contract')
need(native['argv']==['/usr/bin/python3.10','-I','-S','-B',str(R/'receive_originals.py')],'exact sole original receiver argv')
need(native['executable_full_key']==keys['/usr/bin/python3.10'] and native['source_pin']==pin((R/'receive_originals.py').read_bytes()) and native['capture_source_pin']==pin((P/'capture_originals.py').read_bytes()) and native['authority_pin']==pin((H/'AUTHORITY.md').read_bytes()),'whole native original input bindings')
need(type(native['started_epoch_ns']) is int and type(native['ended_epoch_ns']) is int and native['started_epoch_ns']<native['ended_epoch_ns'],'complete integer native clock')
capture=obj(C/'CAPTURE_RESULT.json');tool=obj(H/'CAPTURE_TOOL_NATIVE.json')
results=[tool['result']]+[p['result'] for p in tool['polls']]
need(tool['request']['cmd']=='/usr/bin/env -i PATH=/usr/bin:/bin LANG=C.UTF-8 LC_ALL=C.UTF-8 TZ=UTC /usr/bin/python3.10 -I -S -B '+str(P/'capture_originals.py')+' '+str(H/'AUTHORITY.md')+' 2895 c21e2b7ac4ce8016839b77b4db3bac193d6534091e320ac98a636dde9be81910' and tool['request']['workdir']==str(ROOT) and tool['request']['login'] is False,'entire actual product command/cwd')
for i,r in enumerate(results):
    need(isinstance(r['output'],str) and not r['output'].startswith('Warning:'),'entire untruncated tool output')
    if i+1<len(results):need('exit_code' not in r and tool['polls'][i]['request']['session_id']==r['session_id'],'actual session continuation')
need(results[-1]['exit_code']==0 and 'session_id' not in results[-1],'actual completed outer native')
need(json.loads(''.join(r['output'] for r in results))==capture,'entire actual outer stdout matches captured result')
need(capture['capture_checks']==238353 and capture['capture_read_paths']==4929 and capture['receiver_checks']==whole['checks']==334208 and capture['receiver_read_paths']==4917 and capture['whole_receiver_stdout']==pin(out),'complete actual result/output counts and digest')
need(capture['native_invocations']==1 and capture['native_exit_code']==0 and not capture['root_acceptance'] and not capture['terminal_authority'] and not capture['paper_complete'],'accurate historical capture boundary')
for base,count in [(Q/'p211_round2_physical_independent01',76),(Q/'p211_round2_root_reception01',19),(R,5),(P,8)]:
    actual={str(p) for p in base.rglob('*') if p.is_file()}; expected={p for p in keys if Path(p).is_relative_to(base)}
    need(actual==expected and len(actual)==count,'full original package membership')
    for p in base.rglob('*'):need(not p.is_symlink() and (p.is_dir() or p.is_file()),'ordinary original tree')
sourcekeys=obj(H/'SOURCE_INPUTS.json')
for p,v in sourcekeys.items(): need(pin(rich(p)[0])==v,('full source-reception key',p))
source_native=obj(H/'SOURCE_ROOT_NATIVE.json')
need(source_native['result']['exit_code']==0 and json.loads(source_native['result']['output'])==obj(H/'SOURCE_RESULT.json'),'actual complete source native/result')
for p,v in keys.items():need(rich(p)[1]==v,('whole final key closes',p))
result={'status':'PASS_ROOT_COMPLETE_ROUND2_ORIGINAL_RECEPTION','checks':N,'original_rich_paths':4929,'receiver_rich_paths':4917,'source_byte_paths':len(sourcekeys),'capture_files':13,'whole_capture_output_files':files,'actual_capture_checks':238353,'actual_receiver_checks':334208,'actual_receiver_stdout':pin(out),'native_receiver_invocations':1,'all55_historical_envelopes_received':True,'physical_round2_root_accepted':True,'new_science':0,'new_builds':0,'new_page_views':0,'new_independent_design':False,'terminal_authority':False,'paper_complete':False,'external':'OWNER_AMBER / HOLD_EXTERNAL'}
print(json.dumps(result,sort_keys=True))
