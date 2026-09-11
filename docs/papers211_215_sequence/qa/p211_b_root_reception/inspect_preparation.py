"""Root B source-preparation reception. No scientific module is executed."""
import ast
from hashlib import sha256
import json
from pathlib import Path
import re
import shlex

ROOT=Path('/root/autodl-tmp/symbolic_dynamics')
QA=ROOT/'docs/papers211_215_sequence/qa'
REVIEW=ROOT/'docs/papers211_215_sequence/reviews/p211_b'
FREEZE=ROOT/'papers/211-kernel-image-projection-feedback/frozen_round1'
OUT=Path(__file__).resolve().parent
READS={}
CHECKS=0

def need(ok, why):
    global CHECKS
    CHECKS+=1
    if not ok: raise AssertionError(why)

def raw(path):
    p=Path(path)
    need(p.is_absolute() and p.is_file() and not p.is_symlink(),('physical',str(p)))
    data=p.read_bytes()
    need(str(p) not in READS or READS[str(p)]==data,('stable',str(p)))
    READS[str(p)]=data
    return data

def identity(data):
    return {'bytes':len(data),'sha256':sha256(data).hexdigest()}

def pin(path, expected=None):
    row=identity(raw(path))
    expected={'sha256':expected} if isinstance(expected,str) else expected
    need(expected is None or all(row[k]==v for k,v in expected.items()),('exact pin',str(path)))
    return row

def doc(path): return json.loads(raw(path))

def pins(path,base,absolute=False):
    result={}
    for line in raw(path).decode().splitlines():
        m=re.fullmatch('([0-9a-f]{64})  (.+)',line)
        need(m is not None,'pin syntax')
        h,n=m.groups()
        need(n not in result and '..' not in Path(n).parts and (absolute or not Path(n).is_absolute()),'safe unique name')
        if Path(n).is_absolute():
            need(n in ['/root/autodl-tmp/.codex/skills/'+s+'/SKILL.md' for s in ('proof-writer','research-review')],'only two disclosed absolute skill pins')
        result[n]=pin(base/n,h)
    return result

def native(row,code=0):
    need(set(row)=={'request','result'},'whole native request/result envelope')
    r=row['result']
    need(type(r['exit_code']) is int and r['exit_code']==code and 'session_id' not in r and isinstance(r['chunk_id'],str),'complete actual exit')
    need(row['request'].get('workdir',str(ROOT)) in (str(ROOT),str(FREEZE)),'exact documented cwd')
    return r['output']

def write(name,value):
    with (OUT/name).open('xb') as f: f.write((json.dumps(value,sort_keys=True,indent=2)+'\n').encode())

manifest=pin(REVIEW/'PREPARATION_SHA256SUMS','7a55db3d72952dac3bf77ea0f0bf82989606296684561ef468ea67ca2ff9850f')
payloads=pins(REVIEW/'PREPARATION_SHA256SUMS',REVIEW)
need(len(payloads)==19 and sum(r['bytes'] for r in payloads.values())==866505,'entire 19 preparation payloads')
need({str(p.relative_to(REVIEW)) for p in REVIEW.rglob('*') if p.is_file()}==set(payloads)|{'PREPARATION_SHA256SUMS'},'exact physical capsule, no later roles')
frozen=pins(REVIEW/'INPUT_PINS.sha256',ROOT)
external=pins(REVIEW/'EXTERNAL_READ_PINS.sha256',ROOT,True)
need(len(frozen)==84 and len(external)==50,'complete input populations')
need(set(frozen)=={str(p.relative_to(ROOT)) for p in FREEZE.rglob('*') if p.is_file()},'all exact Round1 files')
fp=pins(FREEZE/'SHA256SUMS',FREEZE)
need(len(fp)==83,'whole physical Round1 manifest')
pin(FREEZE/'SHA256SUMS','582630470c6d1b423f818ed566ed4b699865c04b30543aa502d4556011dd6828')
meta=doc(REVIEW/'evidence/PREPARATION_METADATA_CHECKS01.json')
need(native(meta['external_pin_command']).encode()==raw(REVIEW/'EXTERNAL_READ_PINS.sha256'),'whole actual external pin collection')
need(native(meta['final_native_reads'][2])==''.join(n+': OK\n' for n in frozen),'whole actual final 84 recheck')
for row in meta['final_native_reads'][:2]:
    argv=shlex.split(row['request']['cmd'])
    a,b=map(int,re.fullmatch('(\d+),(\d+)p',argv[2]).groups())
    need(native(row).encode()==b''.join(raw(ROOT/argv[3]).splitlines(keepends=True)[a-1:b]),'whole source metadata displayed bytes')
source=pin(REVIEW/'verify.py','6888ea1df1c20e4786c3582a61fcc5c7d6c8901d9e322d16dc50b047786c5fa7')
parameters_pin=pin(REVIEW/'parameters.json','214b1832a5aae184bd0617334307d87cdcb51f29d2b41983593bdae2d5fc2cac')
tree=ast.parse(raw(REVIEW/'verify.py'))
need([n.names[0].name for n in tree.body if isinstance(n,ast.Import)]==['itertools','json','math','sys'],'static imports')
need(not any(isinstance(n,ast.ImportFrom) for n in ast.walk(tree)),'no local imports')
decl=[n for n in tree.body if isinstance(n,ast.Assign) and isinstance(n.targets[0],ast.Name) and n.targets[0].id=='EXPECTED_PARAMETERS']
parameters=doc(REVIEW/'parameters.json')
need(len(decl)==1 and ast.literal_eval(decl[0].value)==parameters and len(parameters)==13,'entire literal parameter object')
need(parameters['n_values']==list(range(1,8)) and parameters['expected_total_states']==2353 and parameters['carrier_sizes']==[1,3,10,35,126,462,1716],'same seven original carriers')
view=doc(REVIEW/'evidence/BUILD_VIEW_NATIVE01.json')
need(len(view['comparisons'])==10,'ten actual comparisons')
for row in view['comparisons']:
    args=shlex.split(row['request']['cmd'])
    need(args[:2]==['cmp','--'] and len(args)==4 and native(row)=='','actual empty successful raw comparison')
    need(raw(ROOT/args[2])==raw(ROOT/args[3]),'complete source/PDF raw pair')
args=shlex.split(view['hash_return']['request']['cmd'])
need(args[:2]==['sha256sum','--'] and len(args)==8,'six viewed image/PDF hashes')
need(native(view['hash_return'])==''.join(pin(ROOT/n)['sha256']+'  '+n+'\n' for n in args[2:]),'entire actual hash output')
need(len(view['view_request_metadata'])==5,'five actual reviewer view metadata rows')
for i,row in enumerate(view['view_request_metadata'],1):
    path=QA/'p211_initial_build_01/inner/pages'/('page-%04d.png'%i)
    need(row['request']=={'path':str(path)} and row['result']=={'detail':'high','image_returned':True},'actual separate B image view metadata, not this checker viewing')
    pin(path)
build=doc(OUT/'BUILD_REUSE_NATIVE01.json')
need(build['request']=={'cmd':'/usr/bin/python3.10 -I -S -B docs/papers211_215_sequence/reviews/p211_a/inspect_build_reuse.py','workdir':str(ROOT),'max_output_tokens':6000},'exact current full-key root invocation')
buildraw=native(build)
need(buildraw.encode()==raw(OUT/'BUILD_REUSE_STDOUT01.raw') and buildraw==doc(QA/'p211_a_root_reception/BUILD_REUSE_NATIVE01.json')['result']['output'],'entire actual old/current build result identical')
bd=json.loads(buildraw)
need(bd['checks']==5974 and bd['prior_read_key_entries_checked_twice']==1299 and bd['configuration_entries_checked_twice']==843,'whole inherited build dependency key')
pin(bd['executed_checker']['path'],bd['executed_checker']['pin'])
browser=[]
for i in range(1,6):
    p=REVIEW/'sources'/('web%02d.json'%i)
    d=doc(p)
    need(isinstance(d['request'],dict) and d['request']['response_length']=='long','actual primary request')
    s=d.get('tool_result',d.get('result'))
    need(isinstance(s,str) and 'Source: open(' in s and 'Total lines:' in s,'actual browser returned text, not raw HTTP')
    browser.append({'path':str(p),'pin':pin(p),'decoded_characters':len(s)})
records=[]
for i in (1,2): records+=doc(REVIEW/'evidence'/('PREPARATION_NATIVE_READS%02d.json'%i))['records']
need(len(records)==92,'all actual preparation native read records')
failures=[]
historical=[]
raw_compared=[]
for index,row in enumerate(records):
    code=row['result']['exit_code']
    need(code in (0,2),'only successful reads or disclosed navigation failure')
    output=native(row,code)
    args=shlex.split(row['request']['cmd'])
    if code==2:
        need(row['result']['chunk_id'] in ('91a644','d4af00','752c8f') and 'No such file or directory' in output,'three preserved real navigation failures')
        failures.append(index)
    elif args[:2]==['sed','-n']:
        need(len(args)==4,'literal narrow sed')
        path=ROOT/args[3]
        if path in (ROOT/'docs/papers211_215_sequence/PIPELINE_STATE.md',REVIEW/'PREPARATION.md'):
            historical.append({'index':index,'path':str(path),'reason':'historical navigation/preparation text, not a current input or scientific premise'})
            continue
        a,b=map(int,re.fullmatch('(\d+),(\d+)p',args[2]).groups())
        need(output.encode()==b''.join(raw(path).splitlines(keepends=True)[a-1:b]),('whole stable displayed read',index))
        raw_compared.append(index)
    elif args[0]=='sha256sum':
        if '-c' in args:
            need(output==''.join(n+': OK\n' for n in fp),'whole first frozen check')
        else:
            names=[n for n in args[1:] if n!='--']
            need(output==''.join(pin(ROOT/n)['sha256']+'  '+n+'\n' for n in names),'whole hash read')
    elif args[0]=='cmp':
        need(output=='' and raw(ROOT/args[-2])==raw(ROOT/args[-1]),'whole archived actual cmp')
    else:
        need(args[0] in ('rg','find','test','wc'),'only source/navigation commands, no interpreter')
        historical.append({'index':index,'command':row['request']['cmd'],'reason':'archived historical inventory/navigation observation, not rerun or science'})
need(len(failures)==3,'entire failure census')
pin(OUT/'inspect_saved_output.py','badab401dc3ef08873a0a9a33fc6d61b22db8bc3b56d1dba276b4f215bd2487f')
pin(OUT/'RECEIVER_STATIC_NATIVE01.json')
pin(Path(__file__).resolve())
for p,data in READS.items(): need(Path(p).read_bytes()==data,('all consumed inputs unchanged',p))
write('PREPARATION_READ_INPUTS.json',{p:identity(d) for p,d in sorted(READS.items())})
result={'status':'PASS_ROOT_B_PREPARATION_ORIGINALS','checks':CHECKS,'actual_read_paths':len(READS),'payloads':19,'payload_bytes':866505,'preparation_manifest':manifest,'complete_frozen_inputs':84,'complete_external_inputs':50,'capsule':{'source':source,'parameters':parameters_pin},'native_records':92,'whole_stable_sed_outputs':raw_compared,'preserved_navigation_failures':failures,'historical_observations_not_current_input_checks':historical,'actual_source_pdf_comparisons':10,'received_B_view_metadata':5,'root_new_views':0,'fresh_browser_returns':browser,'full_build_reuse_checks':5974,'full_build_result_equal':True,'scientific_execution_or_import':False,'canonical_absent':not (REVIEW/'CANONICAL.json').exists(),'scope':'Complete preparation capsule/current stable keys and actual records; no B scientific run or verdict. Historical source reads remain archived observations, not recomputed results.'}
write('PREPARATION_RESULT.json',result)
print(json.dumps(result,sort_keys=True))
