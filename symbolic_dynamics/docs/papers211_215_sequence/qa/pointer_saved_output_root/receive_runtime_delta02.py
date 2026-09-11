"""Receive the exact four-hunk source correction; execute no received code."""
import ast
from hashlib import sha256
import json
from pathlib import Path
import re
import shlex

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
QA = ROOT/'docs/papers211_215_sequence/qa'
HERE = QA/'pointer_saved_output_root'
PREP = QA/'finite_pointer_initial_runtime_reception02'
OLD = QA/'finite_pointer_initial_runtime_reception01'
READS = {}
CHECKS = 0

def need(ok, detail):
    global CHECKS
    CHECKS += 1
    if not ok:
        raise AssertionError(detail)

def raw(path):
    path = Path(path)
    need(path.is_absolute() and path.is_file() and path.resolve()==path, str(path))
    data = path.read_bytes()
    need(str(path) not in READS or READS[str(path)]==data, ('stable',str(path)))
    READS[str(path)] = data
    return data

def val(data):
    return {'bytes':len(data),'sha256':sha256(data).hexdigest()}

def doc(path):
    return json.loads(raw(path))

def pins(path, base, count, digest=None, complete=False):
    data = raw(path)
    need(digest is None or sha256(data).hexdigest()==digest, 'exact manifest')
    names = []
    for line in data.decode().splitlines():
        h,n = line.split('  ',1)
        need(re.fullmatch('[0-9a-f]{64}',h) and n not in names and not Path(n).is_absolute() and '..' not in Path(n).parts, 'safe unique pin')
        need(sha256(raw(base/n)).hexdigest()==h, ('whole input',n))
        names.append(n)
    need(len(names)==count,'exact pin count')
    if complete:
        need({str(p.relative_to(base)) for p in base.rglob('*') if p.is_file()}==set(names)|{path.name},'whole physical package')
    return names

members = pins(PREP/'SHA256SUMS',PREP,5,'dba11d00a8fac940e46bc91dd4c871b716118b92796239f783890fcf459a9569',True)
pins(PREP/'INPUTS.sha256',ROOT,8)
oldnames = pins(OLD/'SHA256SUMS',OLD,9,'44ea091871b62f2e5889f6ec644ddc1acb56163b8791d077309080870e343ddd',True)
failed = HERE/'runtime_execution01'
failnames = pins(failed/'SHA256SUMS',failed,10,'019a2cbab0c81dc0ac4c77432f64bdb5ce331f7a3001069961f4ab1194d4b56b',True)
accepted = doc(HERE/'RUNTIME_PREPARATION_RESULT.json')
need(sha256(raw(HERE/'RUNTIME_PREPARATION_RESULT.json')).hexdigest()=='6f24bfab6a38961474b9edd29d6c7abd732107276eb66eed4c776b71dba0effc','previous full reception')
for p,w in accepted['READ_INPUTS'].items():
    need(val(raw(p))==w,('entire unchanged prior reception key',p))
old,new = raw(OLD/'inspect_initial.py'),raw(PREP/'inspect_initial.py')
need(val(new)=={'bytes':39410,'sha256':'ee52f54c6197cb6137397437d7bbd2883e53275e531fd9a6ebaccc1835b91154'},'new source')
patch = raw(PREP/'DELTA.diff').splitlines(keepends=True)
need(patch[0].startswith(b'--- '+str((OLD/'inspect_initial.py').relative_to(ROOT)).encode()+b'\t') and patch[1].startswith(b'+++ '+str((PREP/'inspect_initial.py').relative_to(ROOT)).encode()+b'\t'),'native paths')
oldlines = old.splitlines(keepends=True)
rebuilt, pos, i, hunks = [],0,2,0
while i<len(patch):
    m = re.fullmatch(rb'@@ -(\d+),(\d+) \+(\d+),(\d+) @@\n',patch[i])
    need(m is not None,'exact hunk header')
    a,ac,b,bc = map(int,m.groups())
    rebuilt.extend(oldlines[pos:a-1])
    need(len(rebuilt)==b-1,'exact new offset')
    before,after = [],[]
    i += 1
    while i<len(patch) and not patch[i].startswith(b'@@'):
        line = patch[i]
        need(line[:1] in (b' ',b'-',b'+'),'hunk type')
        if line[:1] in (b' ',b'-'): before.append(line[1:])
        if line[:1] in (b' ',b'+'): after.append(line[1:])
        i += 1
    need(before==oldlines[a-1:a-1+ac] and len(before)==ac and len(after)==bc,'entire old hunk reconstruction')
    rebuilt.extend(after)
    pos = a-1+ac
    hunks += 1
rebuilt.extend(oldlines[pos:])
need(hunks==4 and b''.join(rebuilt)==new,'complete old/new byte derivation')
a,b = ast.parse(old),ast.parse(new)
functions = lambda t:{n.name:ast.dump(n) for n in t.body if isinstance(n,ast.FunctionDef)}
fa,fb = functions(a),functions(b)
need(set(fa)==set(fb) and [k for k in fa if fa[k]!=fb[k]]==['audit'] and len(fa)==21,'twenty untouched functions')
globals_only = lambda t:[ast.dump(n) for n in t.body if not isinstance(n,ast.FunctionDef) and not (isinstance(n,ast.Assign) and any(isinstance(v,ast.Name) and v.id=='HERE' for v in n.targets))]
need(globals_only(a)==globals_only(b),'all other globals unchanged')
native = doc(PREP/'NATIVE.json')
need(set(native)=={'status','failure_original_reads','historical_classification_and_seals','diff','static_and_pins'},'whole native record shape')
rows = native['failure_original_reads']+native['historical_classification_and_seals']+[native['diff']]+native['static_and_pins']
need(len(rows)==11,'all actual native records')
for row in rows:
    need(set(row)=={'request','result'} and 'session_id' not in row['result'] and isinstance(row['result']['chunk_id'],str),'complete native envelope')
    need(row['result']['exit_code']==(1 if row is native['diff'] else 0),'actual exit')
    cmd = shlex.split(row['request']['cmd'])
    output = row['result']['output']
    if cmd[:2]==['sed','-n']:
        x,y = map(int,re.fullmatch('(\d+),(\d+)p',cmd[2]).groups())
        need(output.encode()==b''.join(raw(ROOT/cmd[3]).splitlines(keepends=True)[x-1:y]),'whole saved read bytes')
    elif cmd[0]=='diff':
        need(output.encode()==raw(PREP/'DELTA.diff'),'whole actual diff')
    elif cmd[0]=='sha256sum':
        if '-c' in cmd:
            names = oldnames if Path(row['request']['workdir'])==OLD else failnames
            need(output==''.join(n+': OK\n' for n in names),'whole actual seal check')
        else:
            need(output==''.join(sha256(raw(ROOT/n)).hexdigest()+'  '+n+'\n' for n in cmd[1:]),'whole actual pin collection')
    elif cmd[0]=='test':
        need(output=='' and cmd==['test','!','-e',str(PREP.relative_to(ROOT))],'historical absence check only')
    else:
        need(cmd[:5]==['/usr/bin/python3.10','-I','-S','-B','-c'] and len(cmd)==6,'fully read source-only documentary snippet')
        j=json.loads(output)
        need(j['checker_invocations']==j['producer_invocations']==0,'no received execution')
lock=doc(QA/'finite_pointer_runtime_preparation01/discovery02/RUNTIME_LOCK.json')
binding=doc(QA/'finite_pointer_initial_binding01/BINDING.json')
project={p:r for p,r in lock['files'].items() if Path(p).is_relative_to(ROOT)}
need(len(lock['files'])==129 and set(project)=={str(QA/'p211_runtime_preparation'/n) for n in ('p211_runtime.py','runtime_core.py')} and all(r==binding['adapter_sources'][p] for p,r in project.items()),'exact 129=127+2 partition')
need(all(not Path(r['resolved']).is_relative_to(ROOT) for p,r in lock['files'].items() if p not in project),'host aliases outside project')
raw(Path(__file__).resolve())
for p,d in list(READS.items()): need(Path(p).read_bytes()==d,('final unchanged',p))
result={'status':'PASS_ROOT_COMPLETE_POINTER_RUNTIME_DELTA02_SOURCE_ONLY','checks':CHECKS,'payloads':5,'input_pins':8,'native_records':11,'full_hunks':4,'unchanged_other_functions':20,'source':val(new),'read_paths':len(READS),'READ_INPUTS':{p:val(d) for p,d in sorted(READS.items())},'received_checker_executions':0,'producer_executions':0}
with (HERE/'RUNTIME_DELTA02_RESULT.json').open('xb') as stream:
    stream.write((json.dumps(result,sort_keys=True,indent=2)+'\n').encode())
print(json.dumps({k:v for k,v in result.items() if k!='READ_INPUTS'},sort_keys=True))
