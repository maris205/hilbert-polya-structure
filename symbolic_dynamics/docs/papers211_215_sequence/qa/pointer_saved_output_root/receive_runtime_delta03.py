"""Exact path-identity correction reception; no received checker execution."""
import ast
import difflib
from hashlib import sha256
import json
from pathlib import Path
import re
import shlex

ROOT=Path('/root/autodl-tmp/symbolic_dynamics')
QA=ROOT/'docs/papers211_215_sequence/qa'
HERE=QA/'pointer_saved_output_root'
PREP=QA/'finite_pointer_initial_runtime_reception03'
OLD=QA/'finite_pointer_initial_runtime_reception02'
READS={}
CHECKS=0
def need(ok,why):
    global CHECKS
    CHECKS+=1
    if not ok: raise AssertionError(why)
def raw(p):
    p=Path(p)
    need(p.is_absolute() and p.is_file() and p.resolve()==p,'physical input')
    d=p.read_bytes()
    need(str(p) not in READS or READS[str(p)]==d,'stable input')
    READS[str(p)]=d
    return d
def val(d): return {'bytes':len(d),'sha256':sha256(d).hexdigest()}
def doc(p): return json.loads(raw(p))
def pins(p,base,count,sha=None):
    d=raw(p)
    need(sha is None or val(d)['sha256']==sha,'exact seal')
    names=[]
    for line in d.decode().splitlines():
        h,n=line.split('  ',1)
        need(re.fullmatch('[0-9a-f]{64}',h) and n not in names and not Path(n).is_absolute() and '..' not in Path(n).parts,'safe row')
        need(val(raw(base/n))['sha256']==h,('whole input',n))
        names.append(n)
    need(len(names)==count,'entire count')
    return names
members=pins(PREP/'SHA256SUMS',PREP,5,'b258bfcb39be45d23b07a3a1a0d6c8b4ee4d42fec2c2ee0d5e03b261a42467d3')
need({p.name for p in PREP.iterdir()}==set(members)|{'SHA256SUMS'},'entire new physical package')
inputs=pins(PREP/'INPUTS.sha256',ROOT,5)
prior=doc(HERE/'RUNTIME_DELTA02_RESULT.json')
need(val(raw(HERE/'RUNTIME_DELTA02_RESULT.json'))['sha256']=='9cff6d45544711274e8d8ce78ac242f337bee6d36a8a1da7a5b42f1ed97bbb93','accepted complete prior source reception')
for p,w in prior['READ_INPUTS'].items(): need(val(raw(p))==w,('entire prior key unchanged',p))
old=raw(OLD/'inspect_initial.py').decode()
new=raw(PREP/'inspect_initial.py').decode()
need(val(new.encode())=={'bytes':39649,'sha256':'6eb51dbad9a0b647020c03abd65823cf2b820f32b6452a69d5d9c8003b6e0450'},'exact received source')
wrong='            ordinary[resolved] = basic(pin(p,allowed[resolved]))\n'
correct="            actual = pin(p,allowed[name])\n            target = pin(resolved,allowed[resolved])\n            need(actual['resolved']==resolved and basic(actual)==basic(target),\n                 'ordinary original and resolved identities share exact content')\n            ordinary[resolved] = basic(target)\n"
need(old.count(wrong)==1 and new==old.replace("HERE = QA/'finite_pointer_initial_runtime_reception02'","HERE = QA/'finite_pointer_initial_runtime_reception03'").replace(wrong,correct),'complete exact two-site source derivation')
delta=raw(PREP/'DELTA.diff').decode()
need(delta.splitlines(keepends=True)[2:]==list(difflib.unified_diff(old.splitlines(keepends=True),new.splitlines(keepends=True)))[2:],'entire native hunk reconstruction')
a,b=ast.parse(old),ast.parse(new)
fs=lambda t:{n.name:ast.dump(n) for n in t.body if isinstance(n,ast.FunctionDef)}
fa,fb=fs(a),fs(b)
need(set(fa)==set(fb) and [k for k in fa if fa[k]!=fb[k]]==['check_opens'] and len(fa)==21,'twenty other functions exact')
native=doc(PREP/'NATIVE.json')
need(len(native)==9,'complete eight native records plus scope')
for name,row in native.items():
    if name=='status': continue
    need(set(row)=={'request','result'} and row['request']['workdir']==str(ROOT) and 'session_id' not in row['result'],'complete actual native record')
    need(row['result']['exit_code']==(127 if name=='unavailable_metadata_reader' else 1 if name=='complete_diff' else 0),'actual native exit')
    output=row['result']['output']
    if name=='unavailable_metadata_reader': need(output=='/bin/bash: line 1: jq: command not found\n','preserved jq failure')
    elif name=='complete_diff': need(output==delta,'actual entire diff')
    elif name=='actual_root_native_read': need(output.encode()==raw(HERE/'RUNTIME_EXECUTION_NATIVE02.json'),'entire original actual root invocation')
    elif name in ('source_pin','historical_pin_collection'):
        args=shlex.split(row['request']['cmd'])[1:]
        need(output==''.join(val(raw(ROOT/n))['sha256']+'  '+n+'\n' for n in args),'entire native pins')
    elif name=='historical_pin_check': need(output==''.join(n+': OK\n' for n in inputs),'whole original input checks')
    elif name=='archived_failure_metadata':
        failed=doc(HERE/'runtime_execution02/commands/01_receive_initial_runtime/stdout.raw')
        link=failed['READ_INPUTS_PARTIAL']['/lib64/ld-linux-x86-64.so.2']
        target=failed['READ_INPUTS_PARTIAL'][link['resolved']]
        want={k:failed[k] for k in ('status','checks','traceback','producer_invocations_in_this_audit','scientific_output_json_parses')}
        want.update({'link_identity':link,'target_identity':target,'archived_content_equal':all(link[k]==target[k] for k in ('sha256','bytes')),'archived_path_metadata_equal':link==target,'inspection_scope':'archived failed receiver metadata only; no current host read or receiver execution'})
        need(json.loads(output)==want,'whole archived failure metadata reconstruction')
    elif name=='source_only_static':
        j=json.loads(output)
        calls=sorted(({'line':n.lineno,'args':[ast.unparse(x) for x in n.args]} for n in ast.walk(b) if isinstance(n,ast.Call) and isinstance(n.func,ast.Name) and n.func.id=='pin'),key=lambda r:r['line'])
        need(j['complete_pin_call_census']==calls and j['changed_function_ast']==['check_opens'] and j['unchanged_other_functions']==20 and j['checker_invocations']==j['producer_invocations']==j['scientific_output_body_reads']==0,'whole static call census and exact scope')
    else: raise AssertionError(name)
raw(Path(__file__).resolve())
for p,d in READS.items(): need(Path(p).read_bytes()==d,('final unchanged',p))
result={'status':'PASS_ROOT_COMPLETE_POINTER_RUNTIME_DELTA03_SOURCE_ONLY','checks':CHECKS,'source':val(new.encode()),'payloads':5,'input_pins':5,'native_records':8,'full_hunks':2,'read_paths':len(READS),'READ_INPUTS':{p:val(d) for p,d in sorted(READS.items())},'received_checker_executions':0,'producer_executions':0}
with (HERE/'RUNTIME_DELTA03_RESULT.json').open('xb') as f: f.write((json.dumps(result,sort_keys=True,indent=2)+'\n').encode())
print(json.dumps({k:v for k,v in result.items() if k!='READ_INPUTS'},sort_keys=True))
