"""Read-only author artifact and original-output audit; never calls step()."""
import ast
import hashlib
import itertools
import json
import math
from pathlib import Path
import re
import sys

ROOT=Path('/root/autodl-tmp/symbolic_dynamics')
BASE=ROOT/'docs/papers204_208_sequence/scouting/finite_systems_twenty_seventh'
counts={'pin_rows':0,'receipt_streams':0,'snapshots':0,'map_rows':0,
        'independent_support_targets':0,'cycle_rows':0,'manifest_payloads':0}
observed={}
aliases={}

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def check(condition,label):
    if not condition:
        raise AssertionError(label)

def read(path):
    raw=path.read_bytes()
    observed[str(path)]=hashlib.sha256(raw).hexdigest()
    return raw

def getjson(path):
    return json.loads(read(path))

for record in sorted((BASE/'history').glob('*.json')):
    data=getjson(record)
    check(data['equal'] and data['before']==data['after'],f'snapshot equality {record}')
    for row in data['copies']:
        copy=BASE/row['copy']
        check(digest(copy)==row['sha256']==row['copy_sha256'],f'physical copy {copy}')
        observed[str(copy)]=row['sha256']
        aliases[(row['path'],row['sha256'])]=copy
        counts['snapshots']+=1
old_git='docs/papers204_208_sequence/GIT_SYNC_RECEIPT.md'
old_hash='af1754c9d6095c0f943b75fe7b9819ebd2b7c4db9609930ca7feccf2934786da'
old_copy=BASE/'history/recovered_git_receipt/docs/papers204_208_sequence/qa/central_lifecycle_p209_a/GIT_SYNC_RECEIPT.before.md'
check(digest(old_copy)==old_hash,'exact recovered old Git receipt')
aliases[(old_git,old_hash)]=old_copy

def resolve(name,expected):
    path=Path(name)
    actual=path if path.is_absolute() else ROOT/path
    if actual.is_file() and digest(actual)==expected:
        observed[str(actual)]=expected
        return actual
    rel=str(actual.relative_to(ROOT)) if actual.is_relative_to(ROOT) else str(actual)
    alias=aliases.get((rel,expected))
    check(alias is not None,f'no exact original/alias for {name}: {expected}')
    check(digest(alias)==expected,f'alias changed {alias}')
    observed[str(alias)]=expected
    return alias

def visit(value):
    if isinstance(value,dict):
        if isinstance(value.get('path'),str) and re.fullmatch('[0-9a-f]{64}',str(value.get('sha256',''))):
            path=resolve(value['path'],value['sha256'])
            if 'resolved' in value:
                check(str(path.resolve())==value['resolved'],f'changed symlink {path}')
            counts['pin_rows']+=1
        for child in value.values():
            visit(child)
    elif isinstance(value,list):
        for child in value:
            visit(child)

for path in sorted(BASE.rglob('*.json')):
    data=getjson(path)
    visit(data)
    if isinstance(data,dict) and 'argv' in data and 'stdout_sha256' in data:
        for kind in ['stdout','stderr']:
            output=path.parent/f'{kind}.bin'
            check(hashlib.sha256(read(output)).hexdigest()==data[f'{kind}_sha256'],f'command stream {output}')
            counts['receipt_streams']+=1
        check(data['exit']==0 and data.get('inputs_equal',True),f'command status {path}')
        if (path.parent/'inputs_before.json').exists():
            check(getjson(path.parent/'inputs_before.json')==getjson(path.parent/'inputs_after.json'),
                  f'before/after lists {path}')

selected=read(BASE/'evidence/selected_paths.txt').decode().splitlines()
initial=getjson(BASE/'evidence/discovery_pins.json')
check(selected==[row['path'] for row in initial] and len(selected)==5390,'complete selected discovery list')
for label in ['structural','score_refinement','gcd_flow']:
    receipt=getjson(BASE/f'evidence/{label}/receipt.json')
    check(receipt['argv'][:4]==['rg','-n','-i','--'],'content-search command prefix')
    check(receipt['argv'][5:]==selected,'entire exact search argv path list')
    check([row['path'] for row in getjson(BASE/f'evidence/{label}/inputs_before.json')]==selected,
          'entire search before pins')

canonical=read(BASE/'execution/CANONICAL.txt')
check(canonical==read(BASE/'execution/run_1/stdout.bin')==read(BASE/'execution/run_2/stdout.bin'),
      'actual raw pair/canonical equality')
pattern=re.compile(r'^MAP (\d+) (\d+) (\([^)]*\)) (\([^)]*\)) (\d+) (\d+) (\d+)$')
boxes={}
cycles={}
total=None
for line in canonical.decode().splitlines():
    if line.startswith('MAP '):
        match=pattern.fullmatch(line)
        check(match is not None,'MAP schema')
        n,mass=int(match[1]),int(match[2])
        x,y=ast.literal_eval(match[3]),ast.literal_eval(match[4])
        row=(y,int(match[5]),int(match[6]),int(match[7]))
        box=boxes.setdefault((n,mass),{})
        check(x not in box,'duplicate original map row')
        box[x]=row
        counts['map_rows']+=1
    elif line.startswith('CYCLE '):
        _,n,mass,body=line.split(' ',3)
        cycles.setdefault((int(n),int(mass)),[]).append(ast.literal_eval(body))
        counts['cycle_rows']+=1
    elif line.startswith('TOTAL '):
        total=line
expected={(n,mass) for n,cap in [(3,12),(4,10),(5,8)] for mass in range(cap+1)}
check(set(boxes)==expected and counts['map_rows']==2743,'only original 33 boxes/2743 states')
check(total=='TOTAL 33 2743 23329 (1,) 10','actual producer total')
for (n,mass),box in boxes.items():
    check(len(box)==math.comb(n+mass-1,n-1),'complete original carrier count')
    incoming={x:set() for x in box}
    observed_cycles=set()
    for x,(y,tail,period,indegree) in box.items():
        check(len(x)==n and all(isinstance(a,int) and a>=0 for a in x) and sum(x)==mass,
              'valid original source')
        check(y in box,'original successor in carrier')
        incoming[y].add(x)
        positions={}
        orbit=[]
        at=x
        while at not in positions:
            positions[at]=len(orbit)
            orbit.append(at)
            at=box[at][0]
        prefix=positions[at]
        cycle=tuple(orbit[prefix:])
        start=min(range(len(cycle)),key=lambda j:cycle[j])
        cycle=cycle[start:]+cycle[:start]
        observed_cycles.add(cycle)
        check((tail,period)==(prefix,len(cycle)),'canonical graph tail/period')
    check(observed_cycles==set(cycles[(n,mass)]),'complete canonical cycle listing')
    for y,(successor,tail,period,indegree) in box.items():
        check(len(incoming[y])==indegree,'canonical target indegree')
        if any(y[j]>0 and y[(j+1)%n]>0 for j in range(n)):
            continue
        choices=[]
        positive=[j for j in range(n) if y[j]>0]
        for j in positive:
            eligible=y[(j-2)%n]==0
            choices.append([0]+([d for d in range(1,y[j]) if y[j]%d==0] if eligible else []))
        predicted=set()
        for values in itertools.product(*choices):
            source=list(y)
            for j,amount in zip(positive,values):
                source[j]-=amount
                source[(j-1)%n]+=amount
            predicted.add(tuple(source))
        check(predicted==incoming[y],'deductive independent-support source-set theorem')
        counts['independent_support_targets']+=1

if '--manifest' in sys.argv:
    manifest=BASE/'SHA256SUMS'
    entries=[]
    for line in read(manifest).decode().splitlines():
        expected_hash,name=line.split('  ',1)
        check(name!='SHA256SUMS','manifest excludes itself')
        path=BASE/name
        check(path.is_relative_to(BASE) and '..' not in Path(name).parts,'manifest path safety')
        check(digest(path)==expected_hash,f'manifest hash {name}')
        entries.append(name)
    actual=sorted(str(p.relative_to(BASE)) for p in BASE.rglob('*') if p.is_file() and p!=manifest)
    check(sorted(entries)==actual and len(set(entries))==len(entries),'complete nonself coverage')
    counts['manifest_payloads']=len(entries)

for name,expected_hash in observed.items():
    check(digest(Path(name))==expected_hash,f'consumed input changed after audit {name}')
print(json.dumps({'status':'PASS_AUTHOR_ARTIFACT_AND_ORIGINAL_OUTPUT_AUDIT','counts':counts,
    'unique_read_paths_rechecked':len(observed),'no_new_map_evaluation':True,
    'no_independent_gate':True,'historical_Git_receipt_recovery_not_at_time_capture':True},sort_keys=True))
