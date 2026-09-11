"""Root reception of actual controller placement and full host-reuse records.

Documentary only; separate full physical receiver covers recorder/frozen data.
"""
from hashlib import sha256
import json
import os
from pathlib import Path

ROOT=Path('/root/autodl-tmp/symbolic_dynamics')
QA=ROOT/'docs/papers211_215_sequence/qa'
CONTROL=QA/'p211_round1_binding_root'
ENTRY=CONTROL/'entry02'
EXEC=QA/'p211_round1_execution01'
PREP=QA/'p211_round1_reception_preparation02'
ENV={'PATH':'/usr/bin:/bin','LANG':'C.UTF-8','LC_ALL':'C.UTF-8','TZ':'UTC'}
READS={}; CHECKS=0

def need(ok,label):
    global CHECKS
    CHECKS+=1
    if not ok:raise AssertionError(label)

def pin(raw):return {'bytes':len(raw),'sha256':sha256(raw).hexdigest()}

def read(p):
    p=Path(p);need(p.resolve()==p and p.is_file(),('ordinary original',str(p)))
    raw=p.read_bytes();value=pin(raw)
    need(str(p) not in READS or READS[str(p)]==value,('unchanged original',str(p)))
    READS[str(p)]=value
    return raw

def obj(p):return json.loads(read(p))

def check(p,value):need(pin(read(p))==value,('exact original bytes',str(p)))

def seal(base,count,digest):
    raw=read(base/'SHA256SUMS');need(pin(raw)['sha256']==digest,'exact accepted manifest')
    names=set()
    for line in raw.decode().splitlines():
        h,n=line.split('  ',1);need(n not in names and n!='SHA256SUMS','exact nonself names')
        need(pin(read(base/n))['sha256']==h,('complete sealed payload',n));names.add(n)
    need(len(names)==count and names|{'SHA256SUMS'}=={p.relative_to(base).as_posix() for p in base.rglob('*') if p.is_file()},'whole exact sealed membership')
    return names

read(Path(__file__))
source=QA/'p211_round1_adapter02/freeze.py'
binding=CONTROL/'selection02/BINDING_READY.json'
sp={'bytes':37756,'sha256':'0b43b429aa7381d138e81d5c849b0c9925c5f94107f044c94419150c3b059b1a'}
bp={'bytes':1558101,'sha256':'d2ba1a6df64919a4d0a1e402c5797c2a5277bcb99374822a683ac699cc29d44c'}
check(source,sp);check(binding,bp)
need(read(CONTROL/'invoke02.py')==read(ENTRY/'EXECUTED_CONTROLLER.py'),'full actually executed root controller bytes')
need(obj(ENTRY/'INPUT_PINS.json')=={'source':sp,'binding':bp,'controller':pin(read(CONTROL/'invoke02.py'))},'actual controller/start pins')
known={'EXECUTED_CONTROLLER.py','INPUT_PINS.json','RESULT.json'}
last=0
for name,src,dst in [('source',source,EXEC/'freeze.py'),('binding',binding,EXEC/'BINDING.json')]:
    need(read(src)==read(dst),'complete physical starter bytes')
    need(src.stat().st_ino!=dst.stat().st_ino and dst.stat().st_nlink==1,'non-hardlinked separate starter')
    for verb,argv in [('copy',['/usr/bin/cp','-p','--',str(src),str(dst)]),('compare',['/usr/bin/cmp','--',str(src),str(dst)])]:
        label=verb+'_'+name
        known.update(label+'.'+suffix for suffix in ('ATTEMPT.json','NATIVE.json','stdout.raw','stderr.raw'))
        attempt=obj(ENTRY/(label+'.ATTEMPT.json'));native=obj(ENTRY/(label+'.NATIVE.json'))
        fixed={'argv':argv,'cwd':str(ROOT),'environment':ENV,'stdin':'subprocess.DEVNULL','timeout_seconds':60}
        need(set(attempt)==set(fixed)|{'started_epoch'} and all(attempt[k]==v for k,v in fixed.items()),'exact placement request')
        need(set(native)==set(attempt)|{'ended_epoch','native_exit_code','exception','stream_capture_status','stdout','stderr'}
             and all(native[k]==v for k,v in attempt.items()),'full actual placement return')
        need(type(native['native_exit_code']) is int and native['native_exit_code']==0 and native['exception'] is None
             and native['stream_capture_status']=='captured' and last<=native['started_epoch']<=native['ended_epoch'],'actual successful ordered native')
        for stream in ('stdout','stderr'):
            n=label+'.'+stream+'.raw';raw=read(ENTRY/n)
            need(raw==b'' and native[stream]=={'path':n,**pin(raw)},'all four placement raw stream pairs')
        last=native['ended_epoch']
need({p.name for p in ENTRY.iterdir()}==known,'exact19-file placement tree')
actual=obj(CONTROL/'INVOCATION_NATIVE02.json')
need(actual['request']['cmd']=='/usr/bin/python3.10 -I -S -B docs/papers211_215_sequence/qa/p211_round1_binding_root/invoke02.py'
     and actual['request']['workdir']==str(ROOT),'actual product controller invocation')
need(actual['result']['session_id']==94096 and actual['result']['output']=='' and len(actual['polls'])==1
     and actual['polls'][0]['exit_code']==0 and not actual['polls'][0].get('session_id'),'actual yielded invocation settled success')
summary=obj(ENTRY/'RESULT.json')
need(json.loads(actual['polls'][0]['output'])==summary and summary['native_exit_code']==0
     and summary['exception'] is None and summary['stream_capture_status']=='captured'
     and summary['execution_payloads']==508 and summary['physical_freeze_accepted'] is False,'whole actual enclosing output correspondence')
check(EXEC/'SHA256SUMS',summary['execution_manifest'])
check(EXEC/'root.stdout.raw',summary['outer_stdout']);check(EXEC/'root.stderr.raw',summary['outer_stderr'])
outer=obj(EXEC/'ROOT_INVOCATION_NATIVE.json')
need(last<=outer['started_epoch'] and outer['source_pin']==sp and outer['binding_pin']==bp,'placement precedes exact recorder invocation')
need(json.loads(read(EXEC/'root.stdout.raw'))==obj(EXEC/'RESULT.json'),'full actual recorder stdout equality')
for phase in ('precopy','postcopy'):
    r=obj(CONTROL/(phase.upper()+'_NATIVE02.json'));expected=obj(CONTROL/(phase+'02')/'RESULT.json')
    need(r['request']['cmd']=='/usr/bin/python3.10 -I -S -B docs/papers211_215_sequence/qa/p211_round1_binding_root/recheck02.py '+phase
         and r['request']['workdir']==str(ROOT) and r['result']['exit_code']==0 and r['polls']==[]
         and json.loads(r['result']['output'])==expected,'actual whole fresh host/settings evidence')
    need(expected['phase']==phase and expected['checks']==8224 and expected['read_paths']==1723
         and expected['accepted_key_entries']==1688 and expected['outside_workspace_entries']==799
         and expected['runtime_files']==122 and expected['runtime_configuration_paths']==69
         and expected['runtime_memberships']==5 and expected['runtime_loader_directory_states']==9,'full host/settings populations')
    build=obj(CONTROL/('BUILD_'+phase.upper()+'_NATIVE02.json'));old=obj(QA/'p211_a_final_root/BUILD_REUSE_NATIVE01.json')
    need(all(build['request'][k]==old['request'][k] for k in ('cmd','workdir')) and build['result']['exit_code']==0
         and build['polls']==[] and build['result']['output']==old['result']['output'],'whole fresh accepted build-key output')
    need(json.loads(build['result']['output'])['checks']==5974,'complete actual build check count')
seal(PREP,8,'556f22fc196006bb4b7a800ca10af7e921666523495f16a8afd9d3f3f7dc3aa0')
check(PREP/'receive_round1.py',{'bytes':37766,'sha256':'21d16d2560eeb68420a3c37c9a3fda98dcbcb0ea1043dc80cd36a81e24fef06e'})
for line in read(PREP/'INPUTS.sha256').decode().splitlines():
    h,n=line.split('  ',1);need(pin(read(ROOT/n))['sha256']==h,'receiver preparation actual original pin')
static=obj(PREP/'STATIC_PREPARATION_NATIVE.json')['records']
need(len(static)==3 and all(r['result']['exit_code']==0 for r in static),'actual three static preparation envelopes')
s=json.loads(static[0]['result']['output'])
need(s['source']['sha256']==pin(read(PREP/'receive_round1.py'))['sha256'] and s['changed_functions']==['audit','inventory','schema_ok','seal']
     and s['receiver_or_recorder_invocations']==0,'source-only actual static scope')
final=obj(PREP/'FINAL_PREPARATION_NATIVE.json')['records'];need(len(final)==2 and all(r['result']['exit_code']==0 for r in final),'actual final preparation native records')
f=json.loads(final[0]['result']['output']);need(f['checks']==42 and f['input_pins']==14,'actual final preparation scope')
for n,v in f['owned_preseal_files'].items():check(PREP/n,v)
diff=obj(PREP/'DERIVATION_NATIVE.json')
need(diff['receiver']['result']['exit_code']==1 and diff['receiver']['result']['output'].encode()==read(PREP/'DERIVATION.diff'),'complete actual receiver source diff')
for p,v in dict(READS).items():check(Path(p),v)
print(json.dumps({'status':'PASS_ROOT_ACTUAL_PLACEMENT_AND_COMPLETE_HOST_PROVENANCE','checks':CHECKS,'read_paths':len(READS),
                  'placement_commands':4,'recorder_native_commands_received_here':0,'complete_recorder_reception':'SEPARATE_FULL_RECEIVER_REQUIRED',
                  'new_scientific_executions':0,'new_builds':0,'new_page_views':0,'inputs':READS},sort_keys=True))
