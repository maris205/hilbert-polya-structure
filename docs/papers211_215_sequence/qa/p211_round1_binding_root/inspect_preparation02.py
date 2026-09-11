"""Root exact adapter02 documentary reception; no recorder/science execution."""
from hashlib import sha256
import json
from pathlib import Path
import re

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
QA = ROOT/'docs/papers211_215_sequence/qa'
HERE = QA/'p211_round1_binding_root'
PREP = QA/'p211_round1_adapter02'
OLD = QA/'p211_round1_adapter01'
READS = {}
CHECKS = 0

def need(ok, label):
    global CHECKS
    CHECKS += 1
    if not ok:
        raise AssertionError(label)

def read(p):
    p = Path(p)
    need(p.resolve() == p and p.is_file(), ('ordinary exact path',str(p)))
    b = p.read_bytes()
    v = {'bytes':len(b),'sha256':sha256(b).hexdigest()}
    need(str(p) not in READS or READS[str(p)] == v, ('unchanged input',str(p)))
    READS[str(p)] = v
    return b

def obj(p):
    return json.loads(read(p))

def check(p, v):
    read(p)
    need(all(READS[str(p)][k] == x for k,x in v.items()), ('exact input pin',str(p)))

def seal(base, count, digest):
    check(base/'SHA256SUMS', {'sha256':digest})
    names = []
    for line in read(base/'SHA256SUMS').decode().splitlines():
        h,n = line.split('  ',1)
        need(n not in names and n != 'SHA256SUMS' and not Path(n).is_absolute() and '..' not in Path(n).parts, 'nonself names')
        check(base/n, {'sha256':h}); names.append(n)
    need(len(names) == count and set(names)|{'SHA256SUMS'} == {p.relative_to(base).as_posix() for p in base.rglob('*') if p.is_file()}, 'complete exact package')
    return names

def native(row, exit_code=0):
    need(row['request']['workdir'].startswith(str(ROOT)) and row['result']['exit_code'] == exit_code
         and not row['result'].get('session_id'), 'actual settled native request/result')
    return row['result']['output']

read(Path(__file__))
names = seal(PREP,12,'ca0a44dd201954c0e426b47036bc87e1a1e9b60dd7117428c8bfb86f03fc0f32')
need(sum(READS[str(PREP/n)]['bytes'] for n in names) == 246215,'exact payload bytes')
seal(OLD,16,'a8b177ff6c92c630b82868d2ac537cbd49f6461b7e1f50b31f328bab09495fb8')
check(PREP/'freeze.py',{'bytes':37756,'sha256':'0b43b429aa7381d138e81d5c849b0c9925c5f94107f044c94419150c3b059b1a'})
inputs = read(PREP/'INPUTS.sha256').decode().splitlines()
need(len(inputs) == 18,'all source metadata pins')
for line in inputs:
    h,n = line.split('  ',1); check(ROOT/n, {'sha256':h})
static_runs = obj(PREP/'NATIVE_STATIC_CHECKS.json')
need(len(static_runs) == 1, 'one actual static run')
static = json.loads(native(static_runs[0]))
need(static['checks'] == len(static['check_labels']) == 202 and len(static['inputs']) == 14
     and static['recorder_executions'] == static['scientific_executions'] == static['physical_copies'] == 0,'source-only actual scope')
for n,v in static['inputs'].items():
    check(ROOT/n,v)
diffs = obj(PREP/'DERIVATION_NATIVE.json')
need(len(diffs) == 3 and read(PREP/'DERIVATION.diff').decode() == ''.join(native(r,1) for r in diffs), 'all exact native diff stdout')
for name,row in zip(('freeze.py','BINDING.schema.json','BINDING_PENDING.json'),diffs):
    need(row['request']['cmd'] == 'diff -u '+str((OLD/name).relative_to(ROOT))+' '+str((PREP/name).relative_to(ROOT)), 'exact diff operands')
    old,new = read(OLD/name).decode().splitlines(keepends=True),read(PREP/name).decode().splitlines(keepends=True)
    oi=ni=0
    for line in row['result']['output'].splitlines(keepends=True)[2:]:
        if line.startswith('@@ '):
            m=re.match(r'@@ -(\d+)(?:,\d+)? \+(\d+)(?:,\d+)? @@',line)
            need(m is not None,'hunk syntax')
            a,b=int(m[1])-1,int(m[2])-1
            need(old[oi:a] == new[ni:b],'whole interhunk bytes'); oi,ni=a,b
        elif line.startswith(' '):
            need(old[oi] == new[ni] == line[1:],'whole context bytes'); oi+=1; ni+=1
        elif line.startswith('-'):
            need(old[oi] == line[1:],'removed bytes'); oi+=1
        elif line.startswith('+'):
            need(new[ni] == line[1:],'added bytes'); ni+=1
        else:
            raise AssertionError('unsupported diff line')
    need(old[oi:] == new[ni:], 'entire source suffix')
preseal=obj(PREP/'PRESEAL_NATIVE.json')
ps=json.loads(native(preseal['preseal']))
need(ps['checks'] == 140 and ps['payloads'] == 11 and ps['payload_bytes'] == 237347, 'actual full preseal')
for n,v in ps['pins'].items(): check(PREP/n,v)
for row in preseal['input_and_predecessor_manifest_checks']:
    lines = inputs if row['request']['cmd'].endswith('INPUTS.sha256') else read(OLD/'SHA256SUMS').decode().splitlines()
    need(native(row) == ''.join(l.split('  ',1)[1]+': OK\n' for l in lines),'complete native hash lines')
archive=obj(PREP/'NATIVE_PREPARATION_READS.json')
need(len(archive['reads']) == 12,'all actual read envelopes')
for i,row in enumerate(archive['reads']):
    raw=native(row,2 if i == 11 else 0)
    if i not in (6,11):
        m=re.fullmatch(r"sed -n '(\d+),(\d+)p' (.+)",row['request']['cmd'])
        need(m is not None,'exact archived source slice request')
        body=read(ROOT/m[3]).decode().splitlines(keepends=True)
        need(raw == ''.join(body[int(m[1])-1:int(m[2])]),'full actual source read slice')
for key in ('original_pin_query','input_pin_query'):
    row=archive[key]; raw=native(row)
    parts=row['request']['cmd'].split()
    need(parts[0] == 'sha256sum','native hash query')
    expected=''
    for n in parts[1:]:
        read(ROOT/n); expected+=READS[str(ROOT/n)]['sha256']+'  '+n+'\n'
    need(raw == expected,'all raw native hash lines')
review=obj(PREP/'INDEPENDENT_STATIC_RECEPTION.json')
need(review['verdict'] == 'NO_BLOCKING_CODE_SCHEMA_MISMATCH_FOUND'
     and review['binding_or_execution_acceptance'] is False and review['manuscript_review'] is False,'actual static-review scope only')
for n,h in review['reviewed_pins'].items(): check(PREP/n,{'sha256':h})
need(obj(PREP/'BINDING_PENDING.json')['enabled'] is False,'no filled pending binding')
for p,v in dict(READS).items():check(Path(p),v)
result={'status':'PASS_ROOT_COMPLETE_ADAPTER02_SOURCE_DOCUMENTARY_RECEPTION','checks':CHECKS,'read_paths':len(READS),'payloads':12,'payload_bytes':246215,
        'recorder_executions':0,'scientific_executions':0,'binding_accepted':False,
        'scope':'Full 651-line source, schema, plan and checker read separately by root; documentary byte/native reception only.',
        'inputs':READS}
print(json.dumps(result,sort_keys=True))
