#!/usr/bin/python3.10
"""Bounded stdout-only physical R2 receiver; no submitted imports/execution.

Disclosed forward adaptation of accepted R1 receiver rich-read, exact-tree,
seal and native-receipt primitives. R2 binding/host/setting logic is explicit
new documentary code, not a copied PASS or a scientific verifier.
"""
from hashlib import sha256
import copy
import json
import os
from pathlib import Path, PurePosixPath
import re
import stat
import traceback
from urllib.parse import unquote

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
QA = ROOT/'docs/papers211_215_sequence/qa'
HERE = QA/'p211_round2_physical_independent01'
CONTROL = QA/'p211_round2_binding_root01'
ENTRY = CONTROL/'entry01'
REFRESH = CONTROL/'refresh02'
EXEC = QA/'p211_round2_execution01'
PREP = QA/'p211_round2_preparation01'
DRAFT = QA/'p211_round2_binding_root/disabled_selection01'
PAPER = ROOT/'papers/211-kernel-image-projection-feedback'
R0, R1, R2 = (PAPER/('frozen_round'+str(i)) for i in range(3))
B = ROOT/'docs/papers211_215_sequence/reviews/p211_b'
OLD_RECEIVER = QA/'p211_round1_reception_preparation02/receive_round1.py'
ENV = {'PATH':'/usr/bin:/bin','LANG':'C.UTF-8','LC_ALL':'C.UTF-8','TZ':'UTC'}
TOOLS = {'/usr/bin/cp','/usr/bin/cmp','/usr/bin/sha256sum','/usr/bin/python3.10'}
SOURCE_PIN = {'bytes':38416,'sha256':'a333faaf97653f9c8eae008b31389599727bcee446abe2ea80bf379d2fb44a01'}
BINDING_PIN = {'bytes':5207468,'sha256':'419aa3a0d3ec77e09f45596fe52bf42cb0b82ce4e8b42f2ba4384c91feee27d1'}
EMPTY = {
 'docs/papers211_215_sequence/qa/root_replays/p211_a_initial_01':('child01/commands',),
 'docs/papers211_215_sequence/qa/root_replays/p211_a_pair_01':('child01/commands','child02/commands'),
 'docs/papers211_215_sequence/qa/p211_runtime_preparation':('discovery01/empty_probe_capsule','discovery02/empty_probe_capsule','tests01/existing_cache','tests02/existing_cache','tests02/fixture_initial/child01/commands','tests02/fixture_pair/child01/commands','tests02/fixture_pair/child02/commands'),
 'docs/papers211_215_sequence/qa/root_replays/p211_b_initial_01':('child01/commands',),
 'docs/papers211_215_sequence/qa/root_replays/p211_b_pair_01':('child01/commands','child02/commands'),
}
TOP = set('''freeze.py BINDING.json ROOT_INVOCATION_ATTEMPT.json PROCESS_CONTEXT.json EXECUTED_FREEZE_SOURCE.py BINDING_PIN.json HOST_REUSE_BOUNDARY.json SOURCE_TREES_BEFORE.json SOURCE_INPUTS_BEFORE.json EXTERNAL_INPUTS_BEFORE.json EXTERNAL_TREES_BEFORE.json NATIVE_TOOLS_BEFORE.json INHERITED_ORIGINAL_KEYS.json DECLARED_PIN_LIST_BASES.json DECLARED_JSON_PIN_BASES.json MARKDOWN_LINK_MAP.json SOURCE_SELECTION.json SOURCE_INPUTS_AFTER.json SOURCE_TREES_AFTER.json EXTERNAL_INPUTS_AFTER.json EXTERNAL_TREES_AFTER.json NATIVE_TOOLS_AFTER.json PARENT_RUNTIME_AFTER.json READ_INPUTS_BEFORE.json READ_INPUTS_AFTER.json FROZEN_ORIGIN_MAP.json FROZEN_TREE.json EXTERNAL_REFERENCES.json NATIVE_COMMANDS.json RESULT.json ROOT_PRODUCT_NATIVE01.json SHA256SUMS'''.split())
READS, TREES, STATES, PHASES = {}, {}, {}, []
HOST_FILES, HOST_STATES = set(TOOLS), set()
CHECKS = 0


def need(ok, label):
    global CHECKS
    CHECKS += 1
    if not ok:
        raise AssertionError(label)


def pin(raw):
    return {'bytes':len(raw),'sha256':sha256(raw).hexdigest()}


def bytepin(row):
    return {k:row[k] for k in ('bytes','sha256')}


def metadata(s):
    return {k:getattr(s,'st_'+v) for k,v in (
        ('mode','mode'),('device','dev'),('inode','ino'),('uid','uid'),('gid','gid'),
        ('nlink','nlink'),('size','size'),('mtime_ns','mtime_ns'),('ctime_ns','ctime_ns'))}


def relative(name):
    need(isinstance(name,str) and name and '\\' not in name and
         not any(c in name for c in '\x00\r\n\t') and
         not PurePosixPath(name).is_absolute() and PurePosixPath(name).as_posix()==name and
         all(p not in ('','..','.') for p in name.split('/')),('relative path',name))
    return name


def workspace(name):
    return ROOT/relative(name)


def permit_files(paths):
    for spelling in paths:
        p = Path(spelling)
        need(p.is_absolute() and str(p)==spelling,('absolute recorded file',spelling))
        if not p.is_relative_to(ROOT):
            accepted_instruction_files={
                '/root/autodl-tmp/.codex/skills/paper-compile/SKILL.md',
                '/root/autodl-tmp/.codex/skills/proof-writer/SKILL.md',
                '/root/autodl-tmp/.codex/skills/research-review/SKILL.md'}
            need(spelling in accepted_instruction_files or
                 not any(p.is_relative_to(Path(b)) for b in ('/root','/proc','/sys','/dev')),
                 ('no private/ambient/special host file collection; only three accepted instruction-file exceptions',spelling))
            HOST_FILES.add(spelling)


def fresh(path):
    p = Path(path)
    need(p.is_absolute() and (p.is_relative_to(ROOT) or str(p) in HOST_FILES),('explicit file scope',str(p)))
    ls = p.lstat()
    rs = p.stat()
    resolved = str(p.resolve(strict=True))
    link = os.readlink(p) if stat.S_ISLNK(ls.st_mode) else None
    need(stat.S_ISREG(rs.st_mode),('regular resolved file',str(p)))
    if p.is_relative_to(ROOT):
        need(link is None and resolved==str(p),('ordinary workspace file including parents',str(p)))
    raw = p.read_bytes()
    need(metadata(ls)==metadata(p.lstat()) and metadata(rs)==metadata(p.stat()) and
         resolved==str(p.resolve(strict=True)) and link==(os.readlink(p) if p.is_symlink() else None) and
         len(raw)==rs.st_size,('whole rich read stable',str(p)))
    return raw,{**pin(raw),'resolved':resolved,'symlink':link,'stat':metadata(rs),'lstat':metadata(ls)}


def read(path):
    p = Path(path)
    raw,key = fresh(p)
    need(str(p) not in READS or READS[str(p)]==key,('repeated full rich read',str(p)))
    READS[str(p)] = key
    return raw


def obj(path):
    return json.loads(read(path))


def pinned(path, expected):
    raw = read(path)
    need(pin(raw)==bytepin(expected),('original bytes unchanged',str(path)))
    if 'resolved' in expected:
        need({k:READS[str(path)][k] for k in ('bytes','sha256','resolved','symlink')}==expected,
             ('full original four-field key',str(path)))
    if 'stat' in expected:
        need({**pin(raw),'stat':READS[str(path)]['stat']}==expected and
             READS[str(path)]['resolved']==str(path) and READS[str(path)]['symlink'] is None,
             ('full original ordinary rich stat key',str(path)))
    return raw


def rich(path):
    read(path)
    row = READS[str(path)]
    need(row['resolved']==str(path) and row['symlink'] is None,'ordinary rich role')
    return {**bytepin(row),'stat':row['stat']}


def four(path):
    read(path)
    return {k:READS[str(path)][k] for k in ('bytes','sha256','resolved','symlink')}


def ordinary_dir(path):
    p = Path(path)
    s = p.lstat()
    need(p.is_absolute() and p.is_relative_to(ROOT) and p.resolve()==p and stat.S_ISDIR(s.st_mode),
         ('ordinary scoped directory',str(p)))
    return s


def inventory(base,names,prune=(),empty=(),remember=True):
    names,prune,empty = tuple(sorted(names)),tuple(sorted(prune)),tuple(empty)
    need(len(set(names))==len(names) and len(set(empty))==len(empty),'unique inventory names')
    need(empty==EMPTY.get(str(base.relative_to(ROOT)),()) or not empty,'only literal external empties')
    need(not empty or not prune,'no empty allowance with prune')
    dirs={'.'}
    for name in names:
        dirs.update(str(p) for p in PurePosixPath(relative(name)).parents)
    empty_parents={'.'}
    for name in empty:
        empty_parents.update(str(p) for p in PurePosixPath(relative(name)).parents)
    need(not set(empty)&(set(names)|dirs|empty_parents),'empty roles nonoverlapping')
    dirs.update(empty_parents|set(empty))
    rows={'.':{'kind':'directory','stat':metadata(ordinary_dir(base))}}
    omitted={}
    def walk(directory):
        for p in sorted(directory.iterdir()):
            n=relative(str(p.relative_to(base)))
            s=p.lstat()
            if n in prune:
                omitted[n]={'kind':'directory','stat':metadata(ordinary_dir(p))}
            elif stat.S_ISDIR(s.st_mode):
                rows[n]={'kind':'directory','stat':metadata(ordinary_dir(p))}
                if n in empty:
                    need(not any(p.iterdir()),('literal directory actually empty',str(p)))
                walk(p)
            else:
                need(stat.S_ISREG(s.st_mode) and p.resolve()==p,'no symlink/special tree entry')
                rows[n]={'kind':'file','stat':metadata(s)}
    walk(base)
    need({n for n,r in rows.items() if r['kind']=='file'}==set(names) and
         {n for n,r in rows.items() if r['kind']=='directory'}==dirs and set(omitted)==set(prune),
         ('exact complete physical tree',str(base)))
    result={'entries':rows,'pruned_exact_subtrees':omitted,'declared_empty_directories':list(empty)}
    if remember:
        key=(str(base),names,prune,empty)
        need(key not in TREES or TREES[key]==result,('rich tree repeat',str(base)))
        TREES[key]=result
    return result


def sums(raw,nonself=True):
    need(raw.endswith(b'\n'),'complete manifest final LF')
    rows={}
    for line in raw.decode().splitlines():
        match=re.fullmatch(r'([a-f0-9]{64})  (.+)',line)
        need(match is not None,('manifest syntax',line))
        digest,name=match.groups()
        if nonself:
            relative(name)
        need(name not in rows and (not nonself or name!='SHA256SUMS'),'distinct nonself row')
        rows[name]=digest
    need(bool(rows),'nonempty manifest')
    return rows


def seal(base,expected=None,empty=()):
    raw=read(base/'SHA256SUMS')
    rows=sums(raw)
    if expected is not None:
        need(rows=={n:v['sha256'] for n,v in expected.items()},('complete bound manifest',str(base)))
    inventory(base,set(rows)|{'SHA256SUMS'},empty=empty)
    size=0
    for n,h in rows.items():
        b=read(base/n)
        need(pin(b)['sha256']==h,('all manifest payload bytes',str(base/n)))
        size+=len(b)
    return {'path':str(base)+'/','payloads':len(rows),'files':len(rows)+1,'payload_bytes':size,'seal':pin(raw)}


def outer_native(path,saved=None,expected_cmd=None):
    n=obj(path)
    need(set(n)=={'request','result','polls'},('outer envelope schema',str(path)))
    if expected_cmd is not None:
        need(n['request']['cmd']==expected_cmd,('exact outer command',str(path)))
    if 'workdir' in n['request']:
        need(n['request']['workdir']==str(ROOT),'explicit root workdir')
    pending=n['result'].get('session_id')
    stream=n['result']['output']
    if pending is not None:
        need('exit_code' not in n['result'] and len(n['polls'])>0,'actual yielded session then completion')
    else:
        need(not n['polls'],'no invented polls after synchronous completion')
    final=n['result']
    for poll in n['polls']:
        need(poll['request']['session_id']==pending and poll['request'].get('chars','')=='','same actual polled session')
        final=poll['result']
        stream+=final['output']
        pending=final.get('session_id')
    need(final.get('exit_code')==0 and 'session_id' not in final,'actual final successful outer return')
    need('Warning: truncated output' not in stream and 'tokens truncated' not in stream,'no claim to truncated outer stream')
    if saved is not None:
        need(json.loads(stream)==saved,('whole original outer output/saved JSON',str(path)))
    return n,stream.encode()


def native(directory,label,argv,cwd,expected_stdout,tools=None,timeout=60,entry=False):
    attempt_path=directory/(label+'.ATTEMPT.json') if entry else directory/'ATTEMPT.json'
    receipt_path=directory/(label+'.NATIVE.json') if entry else directory/'NATIVE.json'
    attempt,receipt=obj(attempt_path),obj(receipt_path)
    fixed={'argv':argv,'cwd':str(cwd),'environment':ENV,'stdin':'subprocess.DEVNULL','timeout_seconds':timeout}
    if tools is not None:
        fixed['executable_key']=tools[argv[0]]
    need(set(attempt)==set(fixed)|{'started_epoch'} and all(attempt[k]==v for k,v in fixed.items()),
         ('entire exact native attempt',label))
    extra={'ended_epoch','native_exit_code','exception','stream_capture_status','stdout','stderr'}
    if not entry:
        extra.add('record_directory')
    need(set(receipt)==set(attempt)|extra and all(receipt[k]==v for k,v in attempt.items()),
         ('native receipt binds every attempt field',label))
    need(type(receipt['native_exit_code']) is int and receipt['native_exit_code']==0 and
         receipt['exception'] is None and receipt['stream_capture_status']=='captured' and
         receipt['started_epoch']<=receipt['ended_epoch'] and
         receipt['ended_epoch']-receipt['started_epoch']<=timeout,'successful recorded bounded native return')
    if not entry:
        need(receipt['record_directory']=='commands/'+label,'exact internal raw directory')
    for field,expected in (('stdout',expected_stdout),('stderr',b'')):
        name=label+'.'+field+'.raw' if entry else field+'.raw'
        raw=read(directory/name)
        key={'path':name,**pin(raw)} if entry else pin(raw)
        need(receipt[field]==key and raw==expected,('whole actual raw stream bytes',label,field))
    return receipt


def configure_host_scope(lock,build_config,build_key,accepted,recorder):
    permit_files(list(accepted)+list(lock['files'])+list(build_key)+list(recorder))
    permit_files(p for p,v in build_config.items() if v.get('kind')=='file')
    permit_files(p for p,v in lock['configuration']['paths'].items() if v.get('is_file'))
    for p in list(build_config)+list(lock['configuration']['paths'])+list(lock['loader_search_directory_states']):
        HOST_STATES.add(p)
    for p,v in lock['configuration']['memberships'].items():
        HOST_STATES.add(p)
        HOST_STATES.update(str(Path(p)/n) for n in v['members'])


def runtime_state(spelling,with_bytes=True):
    p=Path(spelling)
    need(p.is_relative_to(ROOT) or spelling in HOST_STATES,'explicit runtime configuration path')
    row={'lexists':os.path.lexists(p),'exists':p.exists(),'is_file':p.is_file(),'is_dir':p.is_dir(),
         'is_character_device':p.is_char_device(),'resolved':str(p.resolve()),
         'symlink':os.readlink(p) if p.is_symlink() else None}
    if p.is_char_device():
        st=p.stat()
        row['character_device']={'major':os.major(st.st_rdev),'minor':os.minor(st.st_rdev),'mode':st.st_mode}
    if with_bytes and p.is_file():
        row.update(pin(read(p)))
    return row


def settings(lock,build_config):
    current={}
    for p,v in lock['configuration']['paths'].items():
        row=runtime_state(p)
        need(row==v,('whole runtime configuration',p))
        current['runtime:'+p]=row
    for p,v in lock['configuration']['memberships'].items():
        base=Path(p)
        members={child.name:runtime_state(str(child),False) for child in sorted(base.iterdir())} if base.is_dir() else {}
        row={'directory':runtime_state(p,False),'members':members}
        need(row==v,('whole exact runtime membership',p))
        current['membership:'+p]=row
    for p,v in lock['loader_search_directory_states'].items():
        row=runtime_state(p,False)
        need(row==v,('whole loader-directory state',p))
        current['loader:'+p]=row
    for spelling,v in build_config.items():
        p=Path(spelling)
        need(p.is_relative_to(ROOT) or spelling in HOST_STATES,'explicit build configuration path')
        row={'path':spelling,'present':p.exists(),'resolved':str(p.resolve()),'symlink':p.is_symlink()}
        if p.is_symlink():
            row['link']=os.readlink(p)
        if p.exists():
            mode=p.stat().st_mode
            if stat.S_ISREG(mode):
                row.update({'kind':'file',**pin(read(p))})
            elif stat.S_ISDIR(mode):
                row['kind']='directory'
                if 'members' in v:
                    row['members']=sorted(x.name for x in p.iterdir())
            elif stat.S_ISCHR(mode):
                row.update({'kind':'character_device','major':os.major(p.stat().st_rdev),'minor':os.minor(p.stat().st_rdev)})
            else:
                need(False,('unexpected build config object',spelling))
        need(row==v,('whole build configuration original schema',spelling))
        current['build:'+spelling]=row
    return current


def mark(name,**values):
    PHASES.append({'phase':name,'checks_so_far':CHECKS,**values})


def audit():
    need(Path.cwd()==ROOT,'actual literal document-audit cwd')
    read(Path(__file__).absolute())
    read(HERE/'capture04.py')
    read(HERE/'PLAN.md')
    need(pin(read(OLD_RECEIVER))['sha256']=='21d16d2560eeb68420a3c37c9a3fda98dcbcb0ea1043dc80cd36a81e24fef06e','exact disclosed accepted receiver lineage')
    source=pinned(PREP/'freeze.py',SOURCE_PIN)
    need(source==read(EXEC/'freeze.py')==read(EXEC/'EXECUTED_FREEZE_SOURCE.py'),'all prepared/placed/executed recorder source bytes')
    binding=json.loads(pinned(EXEC/'BINDING.json',BINDING_PIN))
    need(read(EXEC/'BINDING.json')==read(CONTROL/'enabled01/BINDING.json') and obj(EXEC/'BINDING_PIN.json')==BINDING_PIN,'complete actual enabled binding bytes')
    need(binding['schema']=='p211-round2-root-binding-v1' and binding['enabled'] is True and
         binding['execution_directory']==str(EXEC.relative_to(ROOT)) and binding['execution_source_pin']==SOURCE_PIN,'exact actual R2 binding interface')
    need(binding['root_authorization']=={'issuer':'/root','decision':'AUTHORIZE_PHYSICAL_P211_ROUND2_FROM_ACCEPTED_FINAL_B',
         'record':{'path':str((CONTROL/'PHYSICAL_AUTHORITY.md').relative_to(ROOT)),
                   'pin':{'bytes':3070,'sha256':'09b290c6695c03ca3430bd08866118605548e39d691e6f9453ee4a6a94b82232'}}},'actual separate root authority identity')
    need(not os.path.lexists(PAPER/'qa_final'),'terminal outputs still absent during physical reception')
    accepted_path=QA/'p211_b_final_root/INPUTS.json'
    accepted_raw=read(accepted_path)
    need(pin(accepted_raw)['sha256']=='c78f32fa33e73c428f3915a2f9b49cd5926289e93f9ca32fc28a86b5a4fc9509','entire accepted B-key identity')
    accepted=json.loads(accepted_raw)
    lock_path=QA/'p211_runtime_preparation/discovery02/RUNTIME_LOCK.json'
    lock_raw=read(lock_path)
    need(pin(lock_raw)['sha256']=='1499a93909e39b49c16408985053936b7eb7efcf664e91fd75fa77de607be2ab','entire unchanged runtime-lock identity')
    lock=json.loads(lock_raw)
    build_key_path=QA/'p211_initial_build_independent_reception/run01/READ_INPUTS_BEFORE.json'
    build_key_raw=read(build_key_path)
    need(pin(build_key_raw)['sha256']=='5f817fdaddaa204ef59557431211692b3fa4857d2bc9296b3eac2f43c4c6a479','entire accepted build-key identity')
    build_key=json.loads(build_key_raw)
    build_config_path=QA/'p211_initial_build_01/inner/CONFIGURATION_BEFORE.json'
    build_config_raw=read(build_config_path)
    need(pin(build_config_raw)['sha256']=='8af5322df346fc99c5272478690e1cbd52c55c28dbbaa0c61d8e471f772f8af8','whole original build-configuration identity')
    build_config=json.loads(build_config_raw)
    configure_host_scope(lock,build_config,build_key,accepted,binding['recorder_runtime_file_pins'])
    need((len(accepted),sum(not Path(p).is_relative_to(ROOT) for p in accepted),len(lock['files']),
          len(lock['configuration']['paths']),len(lock['configuration']['memberships']),len(lock['loader_search_directory_states']),
          len(build_key),len(build_config))==(1785,801,122,69,5,9,1299,843),'complete exact host/runtime/build scope')
    initial_settings=settings(lock,build_config)
    mark('accepted_source_authority_and_exact_host_scope',host_file_allowlist=len(HOST_FILES))
    # Remaining phases are below; all helper activity is documentary and read-only.
    return receive_bound_execution(binding,accepted,lock,build_key,build_config,initial_settings)


def receive_assembly(disabled,external):
    result=obj(CONTROL/'assembly01/RESULT.json')
    draft_result=obj(DRAFT/'RESULT.json')
    draft_key=obj(DRAFT/'INPUTS.json')
    need(result['actual']==draft_result and draft_result['checks']==114227 and
         (draft_result['external_files'],draft_result['external_trees'],draft_result['workspace_read_paths'])==(3104,33,3107),
         'actual complete disabled assembly result')
    need(disabled['enabled'] is False and disabled['root_authorization']=={'issuer':None,'decision':None,'record':None},'original disabled authority remains absent')
    need(len(draft_key)==3107,'entire actual assembly key')
    for p,key in draft_key.items():
        pinned(workspace(p),key)
    before,after=obj(CONTROL/'assembly01/INPUTS_BEFORE.json'),obj(CONTROL/'assembly01/INPUTS_AFTER.json')
    need(set(before)<=set(after) and len(after)==result['capture_inputs']==3134,'complete source capture key without omissions')
    for p,key in after.items():
        need(p not in before or before[p]==key,'all original precapture rows retained')
        pinned(Path(p),key)
    attempt,native_row=obj(CONTROL/'assembly01/ATTEMPT.json'),obj(CONTROL/'assembly01/RECEIPT.json')
    argv=['/usr/bin/python3.10','-I','-S','-B',str(QA/'p211_round2_binding_preparation01/assemble_disabled.py'),'--write-disabled-draft']
    fixed={'argv':argv,'cwd':str(ROOT),'environment':ENV}
    need(all(attempt[k]==v==native_row[k] for k,v in fixed.items()) and attempt['decision']=='AUTHORIZE_ONE_DISABLED_P211_ROUND2_ASSEMBLY' and
         attempt['stdin']=='empty pipe' and attempt['timeout_ms']==60000 and
         native_row['started_utc']==attempt['started_utc']<=native_row['ended_utc'],'whole actual documentary assembly scope/time')
    need(native_row['status']==0 and native_row['signal'] is None and native_row['error'] is None,'actual documentary assembly exit')
    for f in ('stdout','stderr'):
        raw=read(CONTROL/'assembly01'/(f+'.raw'))
        need(pin(raw)==native_row[f],'all assembly raw bytes pinned')
        need(json.loads(raw)==draft_result if f=='stdout' else raw==b'','whole assembly original stdout/result and stderr')
    outer_native(CONTROL/'ASSEMBLY_NATIVE02.json',result,
                 'env -i PATH=/usr/bin:/bin LANG=C.UTF-8 LC_ALL=C.UTF-8 TZ=UTC /usr/bin/node docs/papers211_215_sequence/qa/p211_round2_binding_root01/assemble_capture.js')
    failed=obj(CONTROL/'FAILED_ASSEMBLY_NATIVE01.json')
    need(failed['result']['exit_code']==1 and failed['polls']==[] and
         'at Object.<anonymous>' in failed['result']['output'] and 'assemble_capture.js:12:41' in failed['result']['output'],
         'real pre-assembly controller failure retained')
    bad=read(CONTROL/'FAILED_ASSEMBLE_CAPTURE01.js')
    good=read(CONTROL/'assemble_capture.js')
    old=b'assert.deepStrictEqual(process.env,ENV)'
    new=b'assert.deepStrictEqual({...process.env},ENV)'
    evidence_reads=b"read(HERE+'ASSEMBLY_CAPTURE_CORRECTION01.md');read(HERE+'FAILED_ASSEMBLY_NATIVE01.json');read(HERE+'FAILED_ASSEMBLE_CAPTURE01.js');"+bytes([10])
    need(good.count(evidence_reads)==1 and bad.count(old)==1 and
         bad.replace(old,new)==good.replace(evidence_reads,b''),
         'exact ENV4 comparison correction plus three explicit retained-evidence reads; no other source delta')
    read(CONTROL/'ASSEMBLY_CAPTURE_CORRECTION01.md')
    read(CONTROL/'FAILED_ASSEMBLY_SOURCE_COPY01.json')
    # Accepted source reception is an input; validate its actual raw evidence,
    # without re-adjudicating the same agent's older source audit.
    base=CONTROL/'source_reception01'
    accepted=obj(base/'RESULT.json')
    need(accepted['status']=='PASS_ROOT_BINDING_SOURCE_RECEPTION_ONLY' and len(accepted['commands'])==4,'actual source-reception role')
    source_rows=[]
    for expected in accepted['commands']:
        d=base/'commands'/expected['label']
        a,n=obj(d/'ATTEMPT.json'),obj(d/'RECEIPT.json')
        need(n==expected and all(a[k]==n[k] for k in ('label','argv','cwd','environment','started_utc')) and
             a['environment']==ENV and a['stdin']=='pipe empty' and a['timeout_ms']==60000 and
             n['status']==0 and n['signal'] is None and n['error'] is None and n['started_utc']<=n['ended_utc'],
             'all original source reception command records')
        for f in ('stdout','stderr'):
            raw=read(d/(f+'.raw'))
            need(pin(raw)==n[f] and (f!='stderr' or raw==b''),'whole original source-reception raw streams')
        source_rows.append(n)
    need(all(source_rows[i]['ended_utc']<=source_rows[i+1]['started_utc'] for i in range(3)),'actual source-reception command chronology')
    need(read(base/'INDEPENDENT_ORIGINAL_STDOUT.raw')==read(base/'commands/03_disclosed_unchanged_metadata_reuse/stdout.raw'),
         'archived prior independent stdout and root explicit reuse whole raw equality only')
    outer_native(base/'ROOT_NATIVE01.json',accepted)


def original_path(spelling,base=''):
    need(isinstance(spelling,str) and spelling and '\\' not in spelling and
         not any(c in spelling for c in '\x00\r\n\t'),'bounded original path spelling')
    p=PurePosixPath(spelling)
    if p.is_absolute():
        need(str(p)==spelling and all(x not in ('','..','.') for x in p.parts[1:]),'normalized absolute original spelling')
        return Path(spelling)
    return (ROOT if not base else workspace(base))/relative(spelling)


def receive_original_maps_and_documents(binding,selection,external,evidence,host_ref):
    def resolve(row,logical,value):
        need(set(row)=={'kind','physical_path','accepted_resolution_reference'},'whole original resolution schema')
        if row['kind']=='WORKSPACE_FILE':
            n=relative(row['physical_path'])
            need(logical.is_relative_to(ROOT) and n in external and external[n]['pin']==value,'entire workspace original pin resolution')
            if workspace(n)!=logical:
                need(row['accepted_resolution_reference'] is not None,'historical substitution has actual accepted source')
            if row['accepted_resolution_reference'] is not None:
                evidence(row['accepted_resolution_reference'])
            pinned(workspace(n),value)
        else:
            need(row['kind']=='HOST_SEPARATE_ROOT' and not logical.is_relative_to(ROOT) and
                 row['physical_path']==str(logical) and row['accepted_resolution_reference']==host_ref,
                 'original host absolute spelling and actual root refresh preserved')
            pinned(logical,value)
        return {'logical_path':str(logical),'pin':value,**row}
    roles={
      'round1_all_reads':('p211_round1_execution01/READ_INPUTS_AFTER.json','DIRECT_BYTE_PIN_WITH_CONTEXT',2255,4),
      'round1_all_external':('p211_round1_execution01/EXTERNAL_REFERENCES.json','WRAPPED_EXTERNAL_PIN',2164,0),
      'whole_final_b_root_inputs':('p211_b_final_root/INPUTS.json','DIRECT_BYTE_PIN_WITH_CONTEXT',1785,801)}
    need(set(binding['inherited_input_keys'])==set(roles),'exact three complete original map roles')
    rebuilt,counts={},[]
    for role,(relative_path,layout,count,host_count) in roles.items():
        spec=binding['inherited_input_keys'][role]
        need(evidence(spec['reference'])==QA/relative_path and spec['entry_layout']==layout,'literal original key schema/path')
        original=obj(QA/relative_path)
        need(len(original)==count and set(original)==set(spec['resolutions']),'every original map entry resolved once')
        mapped={}
        for logical,entry in original.items():
            value=entry['pin'] if layout=='WRAPPED_EXTERNAL_PIN' else entry
            row=spec['resolutions'][logical]
            mapped[logical]={'original_entry':entry,'resolution':resolve(row,original_path(logical),bytepin(value))}
            if layout=='DIRECT_BYTE_PIN_WITH_CONTEXT':
                # These actual accepted physical originals remain available;
                # do not silently reinterpret their rich fields on a copy.
                pinned(Path(logical),value)
        need(sum(r['kind']=='HOST_SEPARATE_ROOT' for r in spec['resolutions'].values())==host_count,'exact old map host split')
        rebuilt[role]={'reference':spec['reference'],'entry_layout':layout,'rows':mapped}
        counts.append({'role':role,'rows':count,'host':host_count})
    need(obj(EXEC/'INHERITED_ORIGINAL_KEYS.json')==rebuilt,'whole three maps independently rebuilt with all original fields')
    list_records,list_counts=[],[]
    expected_counts={'review_a/EXTERNAL_READ_PINS.sha256':(32,0),'review_a/INPUT_PINS.sha256':(33,0),
                     'review_b/DELTA_INPUT_PINS.sha256':(1774,801),'review_b/EXTERNAL_READ_PINS.sha256':(50,2),
                     'review_b/INPUT_PINS.sha256':(84,0),'review_b/RECEPTION_INPUT_PINS.sha256':(515,122)}
    need({s['document'] for s in binding['pin_list_bases']}==set(expected_counts)=={n for n in selection if n.endswith('.sha256')} and
         len(binding['pin_list_bases'])==6,'every copied mixed-base input list exactly once')
    for spec in binding['pin_list_bases']:
        n=spec['document']
        need(spec['base']=='','all six original mixed lists retain workspace base')
        evidence(spec['accepted_origin_reference'])
        parsed=sums(read(workspace(selection[n]['source'])),False)
        need(set(parsed)==set(spec['resolutions']),'whole original mixed-base list membership')
        mapped={}
        for spelling,digest in parsed.items():
            r=spec['resolutions'][spelling]
            need(set(r)=={'pin','resolution'} and r['pin']['sha256']==digest,'exact unchanged original list digest')
            mapped[spelling]=resolve(r['resolution'],original_path(spelling),r['pin'])
        h=sum(r['kind']=='HOST_SEPARATE_ROOT' for r in mapped.values())
        need((len(mapped),h)==expected_counts[n],'entire original list count and host split')
        list_records.append({'document':n,'original_base':'','accepted_origin_reference':spec['accepted_origin_reference'],'rows':mapped})
        list_counts.append({'document':n,'rows':len(mapped),'host':h})
    need(obj(EXEC/'DECLARED_PIN_LIST_BASES.json')==list_records,'all six original-base resolution tables independently rebuilt')
    by_original={str(workspace(r['original_document'])):n for n,r in selection.items()}
    need(len(by_original)==len(selection),'unique unchanged original document origins')
    md=binding['document_origins']
    need(set(md)=={n for n in selection if n.endswith('.md')} and len(md)==35,'all 35 Markdown original roles')
    ordered_count=0
    for n,spec in md.items():
        original=workspace(spec['original_document'])
        need(spec['original_document']==selection[n]['original_document'],'exact unchanged Markdown origin')
        evidence(spec['accepted_origin_reference'])
        body=read(workspace(selection[n]['source'])).decode()
        need(re.search(r'(?m)^\s{0,3}\[[^\]\n]+\]:',body) is None and
             re.search(r'\[[^\]\n]*\]\[[^\]\n]*\]',body) is None,'no unsupported reference-link syntax')
        actual=[]
        for match in re.finditer(r'!?\[[^\]\n]*\]\(([^)\n]+)\)',body):
            href=match.group(1).strip().strip('<>')
            if re.match(r'^[A-Za-z][A-Za-z0-9+.-]*:',href) or href.startswith('#'):
                continue
            target=unquote(href.split('#',1)[0])
            need(target and '\\' not in target and not any(c in target for c in '\x00\r\n\t'),'bounded inline local href')
            logical=Path(os.path.abspath(original.parent/target))
            need(logical.is_relative_to(ROOT),'unchanged local href stays workspace')
            actual.append((href,str(logical.relative_to(ROOT))))
        need(actual==[(r['href'],r['logical_target']) for r in spec['local_links']],'entire ordered local href list')
        ordered_count+=len(actual)
        for row in spec['local_links']:
            dest=by_original.get(str(workspace(row['logical_target'])))
            if dest is not None:
                need(row['kind']=='copied' and row['target']==dest,'exact copied original-document target')
            else:
                evidence(row['accepted_resolution_reference'])
                if row['kind']=='external_file':
                    need(row['target'] in external,'whole external link file consumed')
                else:
                    need(row['kind']=='external_directory','explicit complete external directory link')
                    base=workspace(row['target'])
                    inventory(base,row['directory_files'])
                    need({str((base/relative(x)).relative_to(ROOT)) for x in row['directory_files']}<=set(external),'all external directory-link members consumed')
    need(ordered_count==140 and obj(EXEC/'MARKDOWN_LINK_MAP.json')==md,'140 full ordered unchanged local links and original metadata')
    jd=binding['json_pin_bases']
    need(set(jd)=={n for n in selection if n.endswith('.json')} and len(jd)==57,'all 57 original JSON roles only')
    for n,spec in jd.items():
        need(spec['original_document']==selection[n]['original_document'] and isinstance(spec['scope_note'],str) and spec['scope_note'],
             'unchanged per-schema JSON scope note/origin')
        if spec['base']:
            relative(spec['base'])
        evidence(spec['accepted_origin_and_schema_reference'])
    need(obj(EXEC/'DECLARED_JSON_PIN_BASES.json')==jd,'exact original JSON field/base metadata retained')
    mark('all_inherited_maps_lists_and_original_document_roles',maps=counts,lists=list_counts,markdown=35,ordered_links=140,json_origins=57)
    return {'maps':counts,'lists':list_counts,'markdown_origins':35,'ordered_local_links':140,'json_origins':57,
            'json_semantics':'original accepted role metadata only; no scientific or manuscript interpretation'}


def receive_runtime(binding,lock):
    resolved={}
    for spelling,value in lock['files'].items():
        pinned(Path(spelling),value)
        physical=value['resolved']
        need(physical not in resolved or resolved[physical]==bytepin(value),'all runtime aliases agree on complete bytes')
        resolved[physical]=bytepin(value)
    need(len(resolved)==114 and binding['recorder_runtime_file_pins']==resolved,'exact unchanged 122 original spellings to 114 resolved recorder pins')
    for p,value in resolved.items():
        pinned(Path(p),value)
    need(set(binding['native_tool_pins'])==TOOLS,'exact four native tool byte roles')
    tb,ta=obj(EXEC/'NATIVE_TOOLS_BEFORE.json'),obj(EXEC/'NATIVE_TOOLS_AFTER.json')
    need(tb==ta and set(ta)==TOOLS,'whole native tool rich key before/after')
    for p,value in binding['native_tool_pins'].items():
        pinned(Path(p),value)
        need(ta[p]==rich(Path(p)),'full current native tool stat identity')
    samples=[]
    expected_keys={'argv','cwd','environment','flags','mapped_files','maps_pin','maps_raw','modules','pycache_prefix','scope','sys_path'}
    argv=['/usr/bin/python3.10','-I','-S','-B',str(EXEC/'freeze.py'),'--binding',str(EXEC/'BINDING.json')]
    for name in ('PROCESS_CONTEXT.json','PARENT_RUNTIME_AFTER.json'):
        s=obj(EXEC/name)
        need(set(s)==expected_keys and s['argv']==argv and s['cwd']==str(ROOT) and s['environment']==ENV and
             s['sys_path']==['/usr/lib/python310.zip','/usr/lib/python3.10','/usr/lib/python3.10/lib-dynload'] and
             s['pycache_prefix'] is None,'whole actually recorded isolated parent settings')
        flags=dict(re.findall(r'(\w+)=([^,)]+)',s['flags']))
        need(all(flags.get(k)=='1' for k in ('isolated','no_site','dont_write_bytecode','ignore_environment','no_user_site')) and
             flags.get('optimize')=='0' and flags.get('hash_randomization')=='1','actual complete relevant parent flags')
        need(pin(s['maps_raw'].encode())==s['maps_pin'],'complete actually persisted maps bytes')
        mapped=set()
        previous_end=0
        segments=0
        for line in s['maps_raw'].splitlines():
            columns=line.split(None,5)
            need(len(columns) in (5,6),'whole recorded maps row syntax')
            bounds=columns[0].split('-')
            need(len(bounds)==2 and all(re.fullmatch('[0-9a-f]+',v) for v in bounds) and
                 re.fullmatch(r'[r-][w-][x-][ps]',columns[1]) and re.fullmatch('[0-9a-f]+',columns[2]) and
                 re.fullmatch('[0-9a-f]+:[0-9a-f]+',columns[3]) and columns[4].isdigit(),'complete maps row fields')
            start,end=map(lambda x:int(x,16),bounds)
            need(previous_end<=start<end,'ordered nonoverlapping recorded maps segments')
            previous_end=end
            segments+=1
            if len(columns)==6 and columns[5].startswith('/'):
                p=Path(columns[5])
                need(str(p.resolve())==str(p) and str(p) in s['mapped_files'],'every observed mapped file exact declared resolved spelling')
                pinned(p,s['mapped_files'][str(p)])
                st=READS[str(p)]['stat']
                major,minor=(int(x,16) for x in columns[3].split(':'))
                need(int(columns[4])==st['inode'] and (major,minor)==(os.major(st['device']),os.minor(st['device'])),
                     'actual recorded mapped inode/device matches pinned physical file')
                mapped.add(str(p))
        need(mapped==set(s['mapped_files']) and len(mapped)==11,'entire observed mapped-file membership')
        for p,value in s['mapped_files'].items():
            need(resolved.get(p)==value,'every actual mapped dependency was prebound')
        for module,row in s['modules'].items():
            need(set(row)=={'path','pin'} and not row['path'].endswith(('.pyc','.pyo')),'whole source-only module row')
            p=Path(row['path'])
            need(str(p.resolve())==str(p),'exact resolved original module spelling')
            pinned(p,row['pin'])
            need((p==EXEC/'freeze.py' and module=='__main__' and row['pin']==SOURCE_PIN) or resolved.get(str(p))==row['pin'],
                 'every observed imported module prebound or exact executed main source')
        need(len(s['modules'])==50,'entire actual parent file-backed module set')
        samples.append(s)
        mark('actual_runtime_'+name,modules=len(s['modules']),mapped_files=len(mapped),segments=segments,raw_maps_pin=s['maps_pin'])
    stable=expected_keys-{'maps_raw','maps_pin'}
    need({k:samples[0][k] for k in stable}=={k:samples[1][k] for k in stable},'entire parent runtime/settings module and mapped-file pins unchanged')
    return {'original_spellings':122,'resolved_pins':114,'host_resolved':sum(not Path(p).is_relative_to(ROOT) for p in resolved),
            'samples':2,'modules_each':50,'mapped_files_each':11,'maps_raw_pins':[s['maps_pin'] for s in samples],
            'raw_maps_equal':samples[0]['maps_raw']==samples[1]['maps_raw'],
            'scope':'two actual snapshots and entire declared key; no child-map/transient/hermetic trace or new dependency discovery'}


def receive_native_and_key(binding,selection,external,r1,r1_all,b_all,a_sums,b_sums,live_names,manifest):
    tool_keys=obj(EXEC/'NATIVE_TOOLS_BEFORE.json')
    specs=[('live_round1_compare_%03d'%i,['/usr/bin/cmp','--',str(PAPER/n),str(R1/n)],ROOT,b'')
           for i,n in enumerate(live_names,1)]
    specs.extend([
        ('copy_unchanged_round1_payloads',['/usr/bin/cp','-p','--parents','--',*sorted(r1),str(R2)],R1,b''),
        ('copy_complete_final_b',['/usr/bin/cp','-p','--parents','--',*sorted(b_all),str(R2/'review_b')],B,b'')])
    specs.extend(('copy_compare_%05d'%i,['/usr/bin/cmp','--',str(workspace(row['source'])),str(R2/n)],ROOT,b'')
                 for i,(n,row) in enumerate(sorted(selection.items()),1))
    specs.extend([
        ('verify_outer_manifest',['/usr/bin/sha256sum','-c','SHA256SUMS'],R2,''.join(n+': OK\n' for n in sorted(selection)).encode()),
        ('verify_inner_a_manifest',['/usr/bin/sha256sum','-c','SHA256SUMS'],R2/'review_a',''.join(n+': OK\n' for n in a_sums).encode()),
        ('verify_inner_b_manifest',['/usr/bin/sha256sum','-c','SHA256SUMS'],R2/'review_b',''.join(n+': OK\n' for n in b_sums).encode())])
    need(len(specs)==160,'independently reconstructed complete 160-command sequence')
    commands,files,last_end=[],set(),0
    for label,argv,cwd,out in specs:
        directory=EXEC/'commands'/label
        receipt=native(directory,label,argv,cwd,out,tool_keys)
        need(last_end<=receipt['started_epoch'],'all internal operations actual sequential chronology')
        last_end=receipt['ended_epoch']
        commands.append(receipt)
        files.update('commands/'+label+'/'+n for n in ('ATTEMPT.json','NATIVE.json','stdout.raw','stderr.raw'))
    need(commands==obj(EXEC/'NATIVE_COMMANDS.json'),'entire original ordered aggregate native list')
    inventory(EXEC,TOP|files)
    invocation=obj(EXEC/'ROOT_INVOCATION_ATTEMPT.json')
    argv=['/usr/bin/python3.10','-I','-S','-B',str(EXEC/'freeze.py'),'--binding',str(EXEC/'BINDING.json')]
    need(invocation=={'argv':argv,'cwd':str(ROOT),'environment':ENV,'stdin':'subprocess.DEVNULL',
                      'source_pin':SOURCE_PIN,'binding_pin':BINDING_PIN},'exact actual pre-invocation dictionary without invented timestamps')
    need(read(CONTROL/'invoke_round2.py')==read(ENTRY/'EXECUTED_CONTROLLER.py'),'whole actual executed capture source snapshot')
    need(obj(ENTRY/'INPUT_PINS.json')=={'source':SOURCE_PIN,'binding':BINDING_PIN,'controller':pin(read(CONTROL/'invoke_round2.py'))},
         'complete original source/binding/controller pins')
    roots=[]
    for label,src,dst in (('source',PREP/'freeze.py',EXEC/'freeze.py'),('binding',CONTROL/'enabled01/BINDING.json',EXEC/'BINDING.json')):
        roots.append(native(ENTRY,'copy_'+label,['/usr/bin/cp','-p','--',str(src),str(dst)],ROOT,b'',entry=True))
        roots.append(native(ENTRY,'compare_'+label,['/usr/bin/cmp','--',str(src),str(dst)],ROOT,b'',entry=True))
        need(read(src)==read(dst),'whole actual root placed starter bytes')
    result=obj(EXEC/'RESULT.json')
    root_stdout=read(ENTRY/'ROOT_INVOCATION.stdout.raw')
    root_native=native(ENTRY,'ROOT_INVOCATION',argv,ROOT,root_stdout,timeout=900,entry=True)
    need(json.loads(root_stdout)==result,'whole actual root recorder stdout matches immutable pending result')
    need(all(roots[i]['ended_epoch']<=roots[i+1]['started_epoch'] for i in range(3)) and
         roots[-1]['ended_epoch']<=root_native['started_epoch']<=commands[0]['started_epoch']<=last_end<=root_native['ended_epoch'],
         'actual root placement and every recorder child temporally contained')
    entry_result=obj(ENTRY/'RESULT.json')
    expected_entry={'status':'ACTUAL_PHYSICAL_ROUND2_PENDING_ROOT_RECEPTION','native_exit_code':0,
                    'root_placement_commands':4,'recorder_native_commands':160,'actual_recorder_stdout':pin(root_stdout),
                    'source_pin':SOURCE_PIN,'binding_pin':BINDING_PIN,'execution_seal':'PENDING_ENCOMPASSING_PRODUCT_RETURN',
                    'postcopy_full_host_settings':'PENDING','science_runs':0,'paper_complete':False}
    need(entry_result==expected_entry,'whole actual controller pending result exact')
    expected_outer='env -i PATH=/usr/bin:/bin LANG=C.UTF-8 LC_ALL=C.UTF-8 TZ=UTC /usr/bin/python3.10 -I -S -B docs/papers211_215_sequence/qa/p211_round2_binding_root01/invoke_round2.py '+BINDING_PIN['sha256']
    outer,outer_bytes=outer_native(EXEC/'ROOT_PRODUCT_NATIVE01.json',entry_result,expected_outer)
    need(outer['result'].get('session_id')==43382 and len(outer['polls'])==1 and outer['result']['output']=='',
         'actual original product yield and single final completion retained')
    rb,ra=obj(EXEC/'READ_INPUTS_BEFORE.json'),obj(EXEC/'READ_INPUTS_AFTER.json')
    expected_read=({str(workspace(n)) for n in external}|{str(PAPER/n) for n in live_names}|{str(R1/n) for n in r1_all}|
                  {str(B/n) for n in b_all}|{str(R2/n) for n in set(selection)|{'SHA256SUMS'}}|TOOLS|
                  set(binding['recorder_runtime_file_pins'])|{str(EXEC/n) for n in ('freeze.py','BINDING.json','ROOT_INVOCATION_ATTEMPT.json')})
    need(rb==ra and set(ra)==expected_read and len(ra)==3421,'entire independently reconstructed exact 3421-entry recorder read key')
    for p,key in ra.items():
        pinned(Path(p),key)
    expected_result={'builds':0,'checks':200616,'complete_final_b_files':40,'complete_reused_host_keys_rehashed_by_recorder':False,
                     'execution_package_seal':'PENDING_ACTUAL_ROOT_INVOCATION_RETURN','external':'OWNER_AMBER / HOLD_EXTERNAL',
                     'files_with_manifest':124,'manifest':pin(manifest),'native_commands':160,'new_page_views':0,'paper_complete':False,
                     'payload_bytes':10518152,'payloads':123,'postcopy_complete_host_keys_and_settings_recheck':'PENDING_SEPARATE_ROOT_RECEPTION',
                     'read_paths':3421,'reviews':0,'round1_unchanged_payloads':83,'scientific_executions':0,
                     'status':'PHYSICAL_P211_ROUND2_CREATED_PENDING_ROOT_RECEPTION'}
    need(result==expected_result,'whole original recorder result exact census and pending authority preserved')
    entry_names={'EXECUTED_CONTROLLER.py','INPUT_PINS.json','RESULT.json','SHA256SUMS'}
    entry_names.update(label+'.'+n for label in ('copy_source','compare_source','copy_binding','compare_binding','ROOT_INVOCATION')
                       for n in ('ATTEMPT.json','NATIVE.json','stdout.raw','stderr.raw'))
    inventory(ENTRY,entry_names)
    need(len(entry_names)==24 and len(TOP|files)==672,'complete entry/execution layout without extras')
    mark('all_native_raw_and_whole_recorder_key',root_placements=4,root_invocations=1,inner=160,raw_streams=330,read_key=3421)
    return {'root_placement_records':4,'recorder_outer_records':1,'inner_records':160,'raw_streams':330,
            'root_invocation_start_epoch':root_native['started_epoch'],'root_invocation_end_epoch':root_native['ended_epoch'],
            'all_native_exit_codes':0,'all_stderr_bytes':0,'actual_root_stdout':pin(root_stdout),
            'actual_encompassing_tool_output':pin(outer_bytes),'actual_product_session':43382,
            'process_group_metadata':'not recorded by this bounded capture; not invented'}


def reconstruct_refresh_labels(phase,accepted,r1,lock):
    """Independent finite event reconstruction of the fully read refresh source.

    This does not import/execute that source. Labels include every read,
    exact key check, all original stat checks and both configuration passes.
    """
    labels=['exact_phase','physical_workspace_cwd','exclusive_new_documentary_output',
            'physical_R2_terminal_not_started' if phase=='precopy' else 'postcopy_before_terminal_build']
    first_reads={}
    def event_read(p):
        p=str(p)
        first_reads.setdefault(p,None)
        labels.append('same_full_read:'+p)
    def event_pin(p):
        event_read(p)
        labels.append('whole_original_key:'+str(p))
    def setting_events():
        for p,row in lock['configuration']['paths'].items():
            if row['is_file']:
                event_read(p)
            labels.append('whole_config:'+p)
        labels.extend('entire_membership:'+p for p in lock['configuration']['memberships'])
        labels.extend('loader_directory:'+p for p in lock['loader_search_directory_states'])
    key_path=QA/'p211_b_final_root/INPUTS.json'
    r1_path=QA/'p211_round1_execution01/READ_INPUTS_AFTER.json'
    event_read(REFRESH/'recheck.py')
    event_pin(key_path)
    event_read(key_path)
    labels.append('all_1785_B_entries_801_host')
    for p in accepted:
        event_pin(p)
    event_pin(r1_path)
    event_read(r1_path)
    labels.extend(['entire_R1_key_schema','exact_four_R1_host_rows'])
    for p in r1:
        event_read(p)
        labels.extend(['ordinary_R1_host_tool:'+p,'whole_original_R1_full_stat:'+p])
    labels.append('accepted_B_pair_binding_is_original_key_input')
    event_read(QA/'p211_b_pair_binding/BINDING.json')
    event_pin(QA/'p211_runtime_preparation/discovery02/RUNTIME_LOCK.json')
    event_read(QA/'p211_runtime_preparation/discovery02/RUNTIME_LOCK.json')
    labels.append('whole_unchanged_122_69_5_9_runtime_scope')
    for p in lock['files']:
        event_pin(p)
    setting_events()
    event_read(REFRESH/('BUILD_'+phase.upper()+'_NATIVE01.json'))
    event_read(QA/'p211_b_final_root/BUILD_REUSE_NATIVE01.json')
    labels.extend(['actual_complete_new_build_reuse_native','entire_original_and_new_build_output_bytes_equal',
                   'actual_full_build_dependency_recheck_not_build'])
    first_pass=list(first_reads)
    for p in first_pass:
        event_pin(p)
    for p in r1:
        event_read(p)
        labels.extend(['ordinary_R1_host_tool:'+p,'post_whole_R1_full_stat:'+p])
    setting_events()
    return labels,set(first_reads)


def receive_refresh_and_build(binding,accepted,lock,build_key,build_config,evidence):
    r1_path=QA/'p211_round1_execution01/READ_INPUTS_AFTER.json'
    r1=obj(r1_path)
    need(len(r1)==2255 and sum(not Path(p).is_relative_to(ROOT) for p in r1)==4,'all original R1 stat rows and exact four host tools')
    for p,key in accepted.items():
        need(set(key)=={'bytes','sha256','resolved','symlink'},'unchanged accepted B full key schema')
        pinned(Path(p),key)
    for p,key in r1.items():
        pinned(Path(p),key)
    for p,key in lock['files'].items():
        pinned(Path(p),key)
    for name in ('p211_author_pair_binding/BINDING.json','p211_a_pair_binding/BINDING.json','p211_b_pair_binding/BINDING.json'):
        pair=obj(QA/name)
        lock_ref=pair['runtime_lock']
        need(lock_ref['path']==str(QA/'p211_runtime_preparation/discovery02/RUNTIME_LOCK.json'),'same entire accepted author/A/B runtime lock')
        pinned(Path(lock_ref['path']),{k:lock_ref[k] for k in ('bytes','sha256','resolved','symlink')})
    endpoints={}
    old_build=obj(QA/'p211_b_final_root/BUILD_REUSE_NATIVE01.json')
    need(old_build['result']['exit_code']==0 and 'session_id' not in old_build['result'],'accepted original complete build comparator output')
    old_build_raw=old_build['result']['output'].encode()
    old_summary=json.loads(old_build_raw)
    for phase in ('precopy','postcopy'):
        d=REFRESH/(phase+'01')
        result=obj(d/'RESULT.json')
        original_key=obj(d/'READ_INPUTS.json')
        labels=obj(d/'CHECK_LABELS.json')
        expected_labels,expected_paths=reconstruct_refresh_labels(phase,accepted,r1,lock)
        need(labels==expected_labels and len(labels)==result['checks']==24347,'all 24347 original root refresh check labels exactly reconstructed')
        need(set(original_key)==expected_paths and len(original_key)==result['read_paths']==3359,'entire fresh refresh input set independently reconstructed')
        for p,key in original_key.items():
            pinned(Path(p),key)
        expected_cmd='env -i PATH=/usr/bin:/bin LANG=C.UTF-8 LC_ALL=C.UTF-8 TZ=UTC /usr/bin/python3 -I -S -B docs/papers211_215_sequence/qa/p211_round2_binding_root01/refresh02/recheck.py '+phase
        outer_native(REFRESH/(phase.upper()+'_NATIVE01.json'),result,expected_cmd)
        expected={'status':'PASS_COMPLETE_ACCEPTED_KEY_HOST_RUNTIME_AND_BUILD_SETTINGS_RECHECK','phase':phase,'checks':24347,'read_paths':3359,
                  'accepted_full_key':{'path':str(QA/'p211_b_final_root/INPUTS.json'),'pin':four(QA/'p211_b_final_root/INPUTS.json')},
                  'accepted_key_entries':1785,'outside_workspace_entries':801,'r1_full_schema_entries':2255,
                  'r1_all_original_rows_full_stat_checked_twice':2255,'r1_host_rows_full_stat_checked_twice':4,
                  'runtime_files':122,'runtime_configuration_paths':69,'runtime_memberships':5,'runtime_loader_directory_states':9,
                  'configuration_passes':2,'build_file_keys_checked_twice':1299,'build_configurations_checked_twice':843,
                  'build_native_reference':str(REFRESH/('BUILD_'+phase.upper()+'_NATIVE01.json')),
                  'new_scientific_runs':0,'new_builds':0,'new_page_views':0,'round2_received':False,'binding_authorized_by_this_script':False,
                  'limits':'Complete old key/settings recheck only. All original R1 physical rich rows checked without substitution. Physical R2 still requires separate actual binding/reception. No baseline extension or ambient environment capture.'}
        need(result==expected,'whole original pending root refresh result reconstructed')
        build_native,build_raw=outer_native(REFRESH/('BUILD_'+phase.upper()+'_NATIVE01.json'))
        need(build_raw==old_build_raw and all(build_native['request'][k]==old_build['request'][k] for k in ('cmd','workdir')),
             'entire original/pre/post build comparator output bytes and command identity')
        need(json.loads(build_raw)==old_summary,'complete actual build comparator structured identity')
        endpoints[phase]={'result':result,'key':original_key,'native_output_pin':pin(build_raw)}
    before,after=endpoints['precopy']['key'],endpoints['postcopy']['key']
    pre_native=str(REFRESH/'BUILD_PRECOPY_NATIVE01.json')
    post_native=str(REFRESH/'BUILD_POSTCOPY_NATIVE01.json')
    need(set(before)-set(after)=={pre_native} and set(after)-set(before)=={post_native} and
         all(before[p]==after[p] for p in set(before)&set(after)),'whole 3358 common pre/post rich alias keys unchanged; only literal phase-native path differs')
    # Independently receive all actual build reuse dependencies and original
    # schemas. The accepted comparator itself is not executed again here.
    build=QA/'p211_initial_build_01'
    mapping_path=QA/'p211_initial_build_adoption01/HISTORICAL_MAPPING.json'
    mapping=obj(mapping_path)
    historical={row['logical_path']:row for row in mapping}
    need(len(historical)==len(mapping),'unique accepted build historical mappings')
    substitutions={}
    for p,expected in build_key.items():
        if p in historical:
            row=historical[p]
            need(row['pin']==expected,'exact accepted original build navigation key')
            physical=Path(row['physical_original'])
            substitutions[p]=str(physical)
        else:
            physical=Path(p)
        pinned(physical,expected)
    need(len(substitutions)==2,'only two accepted original build navigation substitutions')
    for relative_path in ('inner/CONFIGURATION_AFTER.json','outer/CONFIGURATION_BEFORE.json','outer/CONFIGURATION_AFTER.json'):
        need(obj(build/relative_path)==build_config,'all four complete original 843-entry build configuration snapshots')
    build_binding_path=QA/'p211_initial_build_binding01/BINDING.json'
    build_binding=obj(build_binding_path)
    lock_ref=build_binding['dependency_lock']
    derived=json.loads(pinned(Path(lock_ref['path']),lock_ref['pin']))
    need(len(derived['entries'])==840 and all(build_config.get(p)==v for p,v in derived['entries'].items()),
         'all 840 old bound native/ELF/TeX/configuration entries unchanged')
    need(len(derived['ldd_elf_inputs'])==33 and all(p in derived['entries'] and derived['entries'][p].get('kind')=='file' for p in derived['ldd_elf_inputs']),
         'entire original 33-entry native/ELF input role retained and content checked')
    need(build_binding['environment']==derived['environment'] and len(build_binding['environment'])==8,'whole accepted source-build settings unchanged')
    need(build_binding['source_pins']==derived['source_observations'] and len(build_binding['source_pins'])==9 and
         build_binding['adapter_pins']==derived['code_observations'],'all nine source and five adapter dependency roles unchanged')
    for p,v in build_binding['cwd_relative_configuration'].items():
        need(build_config.get(p)==v and v['present'] is False,'all three exact cwd-relative original configuration roles remain absent')
    sources={}
    for n,key in build_binding['source_pins'].items():
        pinned(R0/n,key)
        need(read(R0/n)==read(build/'inner/source_only'/n),'whole reviewed-to-built original source bytes')
        sources[n]=key
    measurements=obj(build/'inner/RESULT.json')['measurements']
    pinned(R0/'main.pdf',measurements['pdf'])
    need(read(R0/'main.pdf')==read(build/'inner/source_only/main.pdf') and measurements['pages']==5,'unchanged actual initial PDF bytes; not a new view')
    for page in measurements['renders']:
        pinned(Path(page['image']),page['pin'])
    manifest_rows={name:seal(base) for name,base in (
        ('build',build),('initial_build_audit',QA/'p211_initial_build_independent_reception'),('freeze',R0))}
    need(tuple(manifest_rows[n]['payloads'] for n in ('build','initial_build_audit','freeze'))==(362,18,32),'all three accepted complete build/freeze package inventories')
    checker=ROOT/'docs/papers211_215_sequence/reviews/p211_a/inspect_build_reuse.py'
    expected_summary={
      'status':'UNCHANGED_ACCEPTED_BUILD_KEY_CHECKED','scientific_execution':False,'fresh_build':False,
      'visual_claim_source':'separate actual reviewer view, not this checksum program','checks':5974,
      'prior_read_key_entries_checked_twice':1299,'prior_read_key':{'path':str(QA/'p211_initial_build_independent_reception/run01/READ_INPUTS_BEFORE.json'),
        'pin':pin(read(QA/'p211_initial_build_independent_reception/run01/READ_INPUTS_BEFORE.json'))},
      'historical_mapping':{'path':str(mapping_path),'pin':pin(read(mapping_path))},'exact_navigation_substitutions':substitutions,
      'configuration_entries_checked_twice':843,'configuration_key':{'path':str(build/'inner/CONFIGURATION_BEFORE.json'),'pin':pin(read(build/'inner/CONFIGURATION_BEFORE.json'))},
      'binding':{'path':str(build_binding_path),'pin':pin(read(build_binding_path))},'dependency_lock':lock_ref,
      'sources':sources,'pdf':measurements['pdf'],'render_pins':measurements['renders'],
      'manifests':{n:r['seal'] for n,r in manifest_rows.items()},'environment_of_reused_build':build_binding['environment'],
      'executed_checker':{'path':str(checker),'pin':pin(read(checker))}}
    need(expected_summary==old_summary,'entire actual accepted/pre/post build result independently rebuilt from original dependencies')
    mark('full_root_refresh_and_build_dependencies',endpoints=2,checks_each=24347,full_keys_each=3359,
         original_B=1785,original_B_host=801,all_R1_stat=2255,build_keys=1299,build_configurations=843)
    return {'endpoints':2,'root_checks_each':24347,'root_input_paths_each':3359,'whole_check_labels_reconstructed':True,
            'common_pre_post_original_keys':3358,'only_phase_specific_paths':[pre_native,post_native],
            'accepted_B_keys':1785,'accepted_B_host_keys':801,'all_original_R1_stat_keys':2255,'runtime':{'files':122,'paths':69,'memberships':5,'loader_states':9},
            'accepted_build_keys':1299,'accepted_build_configurations':843,'accepted_build_native_elf_inputs':33,
            'whole_original_pre_post_build_stdout_pin':pin(old_build_raw),'accepted_build_comparator_checks':5974,
            'new_build_comparator_executions_by_this_receiver':0}


def receive_bound_execution(binding,accepted,lock,build_key,build_config,initial_settings):
    external={r['physical_path']:r for r in binding['external_inputs']}
    need(len(external)==len(binding['external_inputs'])==3180,'all distinct actual enabled external rows')
    need(obj(EXEC/'EXTERNAL_REFERENCES.json')==external,'whole archived external selection')
    eb,ea=obj(EXEC/'EXTERNAL_INPUTS_BEFORE.json'),obj(EXEC/'EXTERNAL_INPUTS_AFTER.json')
    need(eb==ea and set(ea)==set(external),'whole external rich before/after identity')
    for n,row in external.items():
        p=workspace(n)
        need(set(row)=={'physical_path','pin','roles'} and row['roles'] and not p.is_relative_to(EXEC) and
             not p.is_relative_to(R2),'scoped distinct original external row')
        pinned(p,row['pin'])
        need(ea[n]==rich(p),('current entire rich external original',n))
    def evidence(ref):
        need(set(ref)=={'path','pin'} and ref['path'] in external and external[ref['path']]['pin']==ref['pin'],
             ('entire actual evidence consumed',ref.get('path')))
        return workspace(ref['path'])
    for ref in binding['acceptance_references'].values():
        evidence(ref)
    evidence(binding['root_authorization']['record'])
    need(evidence(binding['preparation_manifest'])==PREP/'SHA256SUMS' and
         evidence(binding['base_source'])==QA/'p211_round1_adapter02/freeze.py' and
         evidence(binding['intended_inventory'])==PREP/'INTENDED_INVENTORY.json','literal accepted source/lineage/inventory roles')
    host=binding['host_reuse_boundary']
    need(obj(EXEC/'HOST_REUSE_BOUNDARY.json')==host and
         host['mode']=='ROOT_SEPARATE_COMPLETE_HOST_KEYS_AND_SETTINGS_RECHECK' and
         host['postcopy_root_recheck_required'] is True and host['recorder_rehashes_complete_reused_host_keys'] is False,
         'unchanged explicit recorder/full-host boundary')
    for field in ('complete_host_key_references','accepted_settings_references','precopy_recheck_references'):
        need(isinstance(host[field],list) and bool(host[field]),'nonempty complete host evidence list')
        for ref in host[field]:
            evidence(ref)
    host_ref={'path':str((REFRESH/'precopy01/RESULT.json').relative_to(ROOT)),'pin':pin(read(REFRESH/'precopy01/RESULT.json'))}
    need(host['precopy_recheck_references']==[host_ref],'all host resolutions cite actual consumed fresh precopy')
    trees={}
    for spec in binding['external_trees']:
        need(set(spec)=={'root','files','empty_directories','manifest','accepted_scope_reference'},'whole external tree schema')
        base=workspace(spec['root'])
        need(str(base) not in trees and spec['empty_directories']==list(EMPTY.get(spec['root'],())),'distinct exact per-root empty list')
        evidence(spec['accepted_scope_reference'])
        need({str((base/relative(n)).relative_to(ROOT)) for n in spec['files']}<=set(external),'all exact tree bytes consumed')
        trees[str(base)]=inventory(base,spec['files'],empty=spec['empty_directories'])
        if spec['manifest'] is not None:
            need(spec['manifest']=='SHA256SUMS','literal full nonself external seal')
            seal(base,empty=spec['empty_directories'])
    need(len(trees)==39 and sum(len(v['declared_empty_directories']) for v in trees.values())==13,'39 exact original scopes with 13 named empty leaves')
    need(obj(EXEC/'EXTERNAL_TREES_BEFORE.json')==trees==obj(EXEC/'EXTERNAL_TREES_AFTER.json'),'all current/full-rich historical external trees')
    enabled_result=obj(CONTROL/'enabled01/RESULT.json')
    enabled_inputs=obj(CONTROL/'enabled01/INPUTS.json')
    need(set(enabled_inputs)=={str(workspace(n)) for n in external} and enabled_result['read_paths']==3180,'entire enablement input set equals actual external selection')
    for p,key in enabled_inputs.items():
        pinned(Path(p),key)
    outer_native(CONTROL/'ENABLED_BINDING_NATIVE01.json',enabled_result,
                 'env -i PATH=/usr/bin:/bin LANG=C.UTF-8 LC_ALL=C.UTF-8 TZ=UTC /usr/bin/node docs/papers211_215_sequence/qa/p211_round2_binding_root01/prepare_enabled.js')
    need(enabled_result['binding']==BINDING_PIN and enabled_result['checks']==131525 and
         enabled_result['host_resolution_rows_bound']==1730 and enabled_result['physical_round2_created'] is False and
         enabled_result['scientific_runs']==0,'actual enabled result role not physical execution')
    disabled=obj(DRAFT/'BINDING_DISABLED_DRAFT.json')
    reversed_binding=copy.deepcopy(binding)
    reversed_binding['enabled']=False
    reversed_binding['root_authorization']={'issuer':None,'decision':None,'record':None}
    reversed_binding['host_reuse_boundary']['precopy_recheck_references']=[]
    reversed_binding['external_inputs']=disabled['external_inputs']
    reversed_binding['external_trees']=disabled['external_trees']
    host_rows=0
    for spec in reversed_binding['inherited_input_keys'].values():
        for row in spec['resolutions'].values():
            if row['kind']=='HOST_SEPARATE_ROOT':
                need(row['accepted_resolution_reference']==host_ref,'all inherited host refs use actual fresh original')
                row['accepted_resolution_reference']=None
                host_rows+=1
    for spec in reversed_binding['pin_list_bases']:
        for row in spec['resolutions'].values():
            if row['resolution']['kind']=='HOST_SEPARATE_ROOT':
                need(row['resolution']['accepted_resolution_reference']==host_ref,'all mixed-list host refs use actual fresh original')
                row['resolution']['accepted_resolution_reference']=None
                host_rows+=1
    need(reversed_binding==disabled and host_rows==1730,'whole reverse delta, no other original field changed')
    old_external={r['physical_path']:r for r in disabled['external_inputs']}
    need(len(old_external)==3104 and all(external.get(n)==v for n,v in old_external.items()),'all original external roles/pins unchanged')
    need(binding['external_trees'][:33]==disabled['external_trees'] and len(disabled['external_trees'])==33,'33 original whole tree specs retained in order')
    extra_roots={str(p.relative_to(ROOT)) for p in (QA/'p211_round2_binding_preparation01',QA/'p211_round2_binding_source_audit01',CONTROL/'source_reception01',CONTROL/'assembly01',DRAFT,REFRESH/'precopy01')}
    need({t['root'] for t in binding['external_trees'][33:]}==extra_roots,'six and only six authorized new sealed scopes')
    receive_assembly(disabled,external)
    mark('whole_enabled_binding_and_39_external_trees',external_files=3180,original_trees=33,new_trees=6,host_reference_rows=host_rows)
    selected=obj(PREP/'INTENDED_INVENTORY.json')
    need(selected['schema']=='p211-round2-intended-inventory-v1' and selected['target']==str(R2.relative_to(ROOT)) and
         (selected['payload_count'],selected['payload_bytes'],selected['total_file_count_with_future_outer_manifest'])==(123,10518152,124),'entire intended physical selection')
    r1_original=obj(QA/'p211_round1_execution01/SOURCE_SELECTION.json')
    selection={}
    for row in selected['rows']:
        n=relative(row['destination'])
        need(n not in selection and n!='SHA256SUMS','unique nonself physical role')
        if row['role']=='UNCHANGED_ROUND1_PAYLOAD':
            need(row['source']==str((R1/n).relative_to(ROOT)) and n in r1_original and
                 row['pin']==r1_original[n]['pin'] and row['original_document']==r1_original[n]['original_document'],'unaltered whole accepted Round1 role')
        else:
            need(row['role']=='COMPLETE_FINAL_B_PACKAGE' and n.startswith('review_b/') and
                 row['source']==str((B/n.removeprefix('review_b/')).relative_to(ROOT))==row['original_document'],'complete literal final B role')
        selection[n]={k:row[k] for k in ('source','original_document','pin','role')}
    need(obj(EXEC/'SOURCE_SELECTION.json')==selection and len(selection)==123,'entire independently rebuilt source selection')
    r1={n:r['pin'] for n,r in selection.items() if r['role']=='UNCHANGED_ROUND1_PAYLOAD'}
    b_all={n.removeprefix('review_b/'):r['pin'] for n,r in selection.items() if r['role']=='COMPLETE_FINAL_B_PACKAGE'}
    need((len(r1),len(b_all),sum(r['pin']['bytes'] for r in selection.values()))==(83,40,10518152),'83 plus B40 exact byte arithmetic')
    r1_seal={'bytes':8048,'sha256':'582630470c6d1b423f818ed566ed4b699865c04b30543aa502d4556011dd6828'}
    need(pin(read(R1/'SHA256SUMS'))==r1_seal and b_all['SHA256SUMS']==
         {'bytes':3549,'sha256':'45b7c0337259da2fccb078cf4d7b84ec7228a16a6bf6089167c19a26c477ca46'},'two exact historical manifests retained')
    seal(R1,r1)
    b_sums=sums(read(B/'SHA256SUMS'))
    seal(B,{n:v for n,v in b_all.items() if n!='SHA256SUMS'})
    expected={n:r['pin'] for n,r in selection.items()}
    seal(R2,expected)
    a_sums=sums(read(R1/'review_a/SHA256SUMS'))
    need(read(R2/'review_a/SHA256SUMS')==read(R1/'review_a/SHA256SUMS') and
         read(R2/'review_b/SHA256SUMS')==read(B/'SHA256SUMS'),'both inner manifests unchanged raw')
    manifest=''.join(expected[n]['sha256']+'  '+n+'\n' for n in sorted(expected)).encode()
    need(read(R2/'SHA256SUMS')==manifest,'new exact sorted nonself outer bytes')
    sb,sa=obj(EXEC/'SOURCE_INPUTS_BEFORE.json'),obj(EXEC/'SOURCE_INPUTS_AFTER.json')
    need(sb==sa and set(sa)=={'round1','b','live'},'entire historical rich source before/after')
    live_names=sorted(n for n in r1 if not n.startswith('review_a/'))
    need(len(live_names)==32,'unchanged author32')
    r1_all={**r1,'SHA256SUMS':r1_seal}
    for role,base,keys in (('round1',R1,r1_all),('b',B,b_all),('live',PAPER,{n:r1[n] for n in live_names})):
        need(set(sa[role])==set(keys),'whole source role membership')
        for n,key in keys.items():
            pinned(base/n,key)
            need(sa[role][n]==rich(base/n),('entire actual historical source stat',role,n))
    for n in live_names:
        need(read(PAPER/n)==read(R0/n)==read(R1/n)==read(R2/n),('four original author byte copies',n))
    origins,inodes=[],set()
    for n,row in sorted(selection.items()):
        src,dst=workspace(row['source']),R2/n
        need(read(src)==read(dst),'entire source/destination raw equality')
        sk,dk=rich(src),rich(dst)
        inode=(dk['stat']['device'],dk['stat']['inode'])
        need(inode!=(sk['stat']['device'],sk['stat']['inode']) and inode not in inodes and dk['stat']['nlink']==1,'all distinct non-hardlinked new payloads')
        inodes.add(inode)
        origins.append({'relative_name':n,'role':row['role'],'original_path':row['source'],
                        'original_document':row['original_document'],'frozen_path':str(dst.relative_to(ROOT)),
                        'pin':row['pin'],'source_key':sk,'frozen_key':dk})
    need(obj(EXEC/'FROZEN_ORIGIN_MAP.json')==origins,'all 123 complete rich origin rows independently rebuilt')
    outer_stat=rich(R2/'SHA256SUMS')['stat']
    need(outer_stat['nlink']==1 and (outer_stat['device'],outer_stat['inode']) not in inodes,'separate ordinary outer manifest')
    frozen_tree=inventory(R2,set(expected)|{'SHA256SUMS'})
    need(obj(EXEC/'FROZEN_TREE.json')==frozen_tree,'whole current 124-file rich frozen tree')
    tb,ta=obj(EXEC/'SOURCE_TREES_BEFORE.json'),obj(EXEC/'SOURCE_TREES_AFTER.json')
    need(set(tb)==set(ta)=={'round1','b','live'},'whole source tree roles')
    for role,base,keys in (('round1',R1,r1_all),('b',B,b_all)):
        need(tb[role]==ta[role]==inventory(base,keys),'unchanged full source trees')
    live=inventory(PAPER,live_names,('frozen_round0','frozen_round1','frozen_round2'))
    need(ta['live']==live,'exact current live tree with three literal frozen prunes')
    lb,la=tb['live'],ta['live']
    need(lb['declared_empty_directories']==la['declared_empty_directories']==[] and
         set(lb['pruned_exact_subtrees'])=={'frozen_round0','frozen_round1'},'strict precopy literal prunes')
    for name in ('frozen_round0','frozen_round1'):
        need(lb['pruned_exact_subtrees'][name]==la['pruned_exact_subtrees'][name],'old frozen root rich metadata unchanged')
    need(la['pruned_exact_subtrees']['frozen_round2']==frozen_tree['entries']['.'],'new prune accounted by full physical tree')
    need({n:v for n,v in lb['entries'].items() if n!='.'}=={n:v for n,v in la['entries'].items() if n!='.'},'all live descendants full stat unchanged')
    allowed={'size','mtime_ns','ctime_ns','nlink'}
    need({k:v for k,v in lb['entries']['.']['stat'].items() if k not in allowed}==
         {k:v for k,v in la['entries']['.']['stat'].items() if k not in allowed},'only four permitted live-parent metadata changes')
    mark('complete_physical_123_payloads_and_original_rich_trees',payloads=123,payload_bytes=10518152,frozen_files=124)
    inheritance=receive_original_maps_and_documents(binding,selection,external,evidence,host_ref)
    runtime=receive_runtime(binding,lock)
    native_summary=receive_native_and_key(binding,selection,external,r1,r1_all,b_all,a_sums,b_sums,live_names,manifest)
    host_summary=receive_refresh_and_build(binding,accepted,lock,build_key,build_config,evidence)
    packaging=obj(CONTROL/'PACKAGING_RESULT.json')
    actual_packaging={name:seal(base) for name,base in (('execution',EXEC),('controller',ENTRY),('postcopy',REFRESH/'postcopy01'),('enabled',CONTROL/'enabled01'))}
    need(packaging=={'status':'ACTUAL_EXECUTION_PACKAGED_PENDING_COMPLETE_ROOT_INDEPENDENT_RECEPTION',**actual_packaging,'paper_complete':False,'science_runs':0},'entire actual packaging result independently rebuilt')
    need((actual_packaging['execution']['payloads'],actual_packaging['execution']['files'],actual_packaging['execution']['payload_bytes'])==(671,672,24888014),'complete original execution package census')
    outer_native(CONTROL/'PACKAGING_NATIVE01.json',packaging,
                 'env -i PATH=/usr/bin:/bin LANG=C.UTF-8 LC_ALL=C.UTF-8 TZ=UTC /usr/bin/node docs/papers211_215_sequence/qa/p211_round2_binding_root01/seal_actual.js')
    read(CONTROL/'seal_actual.js')
    need(settings(lock,build_config)==initial_settings,'all runtime/build settings whole final equality')
    before=dict(READS)
    for p,key in before.items():
        need(fresh(Path(p))[1]==key,('every receiver original closes with full rich metadata',p))
    tree_summaries=[]
    for (base,names,prune,empty),tree in list(TREES.items()):
        need(inventory(Path(base),names,prune,empty,False)==tree,('whole receiver-observed rich tree final closure',base))
        tree_summaries.append({'root':base,'files':len(names),'entries':len(tree['entries']),'prunes':list(prune),
                               'empty_directories':list(empty),'full_inventory_json_pin':pin(json.dumps(tree,sort_keys=True,separators=(',',':')).encode())})
    mark('whole_key_settings_tree_and_execution_final_closure',input_paths=len(before),tree_roles=len(tree_summaries))
    return {'schema':'p211-r2-independent-physical-documentary-receiver-v1',
            'status':'PASS_PHYSICAL_ROUND2_DOCUMENTARY_RECEPTION_PENDING_ROOT_DECISION',
            'checks':CHECKS,'receiver_read_paths':len(before),'recorder_read_paths':3421,
            'payloads':123,'frozen_files':124,'execution_files':672,'external_files':3180,'external_trees':39,
            'native':native_summary,'inheritance':inheritance,'recorder_runtime':runtime,'host_refresh':host_summary,
            'packaging':actual_packaging,'phases':PHASES,'READ_INPUTS':before,'RICH_TREE_SUMMARIES':tree_summaries,
            'configuration_snapshot_pin':pin(json.dumps(initial_settings,sort_keys=True,separators=(',',':')).encode()),
            'configuration_schemas':['unchanged runtime state/complete memberships/loader states','unchanged build path/present/kind/member schema'],
            'submitted_programs_executed':0,'scientific_executions':0,'builds':0,'page_views':0,'manuscript_reviews':0,
            'paper_complete':False,'terminal_authority':False,'external':'OWNER_AMBER / HOLD_EXTERNAL',
            'limits':['Prior source and disabled-binder audits by this same agent are accepted root inputs, not new independent re-adjudication.',
                      'Received bounded subprocess capture has no PID/PGID/SID or escaped-descendant certification; none is invented.',
                      'Recorder maps/imports are two observations, not transient or child-wide OS tracing; no host/runtime baseline is extended.',
                      'Actual outer tool records preserve returned chunks and session completion; no new encompassing wall-clock timestamps are invented.',
                      'Original JSON role metadata is preserved, not a fresh scientific per-field or manuscript validation.',
                      'No submitted recorder, assembler, scientific verifier or build comparator is executed by this independent receiver.']}


if __name__=='__main__':
    try:
        outcome=audit()
    except BaseException:
        print(json.dumps({'status':'FAIL_DOCUMENTARY_SCOPE_PRESERVE_ALL_ORIGINALS','checks':CHECKS,
                          'phases':PHASES,'traceback':traceback.format_exc(),'READ_INPUTS_PARTIAL':READS},sort_keys=True))
        raise SystemExit(1)
    print(json.dumps(outcome,sort_keys=True))
