"""Append-only documentary recorder, adapted from sealed scout 27, not hermetic."""
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
import time

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
BASE = ROOT / 'docs/papers204_208_sequence/scouting/finite_systems_twenty_ninth'

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def emit(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('xb') as stream:
        stream.write(data)

def js(path, value):
    emit(path, (json.dumps(value, indent=2, ensure_ascii=False)+'\n').encode())

def pins(names):
    return [{'path':name, 'sha256':digest(ROOT/name)} for name in names]

def snapshot(label, names):
    before=pins(names)
    rows=[]
    for row in before:
        name=row['path'].lstrip('/') if Path(row['path']).is_absolute() else row['path']
        dest=BASE/'history'/label/name
        emit(dest, (ROOT/row['path']).read_bytes())
        rows.append({**row, 'copy':str(dest.relative_to(BASE)), 'copy_sha256':digest(dest)})
    after=pins(names)
    equal=before==after and all(r['sha256']==r['copy_sha256'] for r in rows)
    js(BASE/'history'/f'{label}.json', {'before':before,'after':after,'copies':rows,'equal':equal})
    if not equal:
        raise RuntimeError('historical input changed during capture; failed record retained')

def command(label, argv, inputs=()):
    dest=BASE/'evidence'/label
    dest.mkdir(parents=True, exist_ok=False)
    inputs=sorted(set([str(BASE.relative_to(ROOT)/'capture.py'),*inputs]))
    before=pins(inputs)
    js(dest/'inputs_before.json',before)
    started=time.time_ns()
    try:
        result=subprocess.run(argv,cwd=ROOT,capture_output=True)
        code=result.returncode
        stdout,stderr=result.stdout,result.stderr
    except OSError as error:
        code=None
        stdout,stderr=b'',repr(error).encode()
    emit(dest/'stdout.bin',stdout)
    emit(dest/'stderr.bin',stderr)
    after=pins(inputs)
    js(dest/'inputs_after.json',after)
    js(dest/'receipt.json', {'argv':argv,'cwd':str(ROOT),'exit':code,
       'started_ns':started,'finished_ns':time.time_ns(),
       'stdout_sha256':digest(dest/'stdout.bin'),'stderr_sha256':digest(dest/'stderr.bin'),
       'inputs_equal':before==after,'input_count':len(inputs),
       'scope':'documentary subprocess capture; inherited environment, not hermetic'})
    print(json.dumps({'label':label,'exit':code,'stdout_bytes':len(stdout),
                      'stderr_bytes':len(stderr),'input_count':len(inputs),'inputs_equal':before==after}))
    return code,stdout

EXCLUSIONS=['/reviews/','/qa/','/frozen','/source_context/','/history_inputs/',
 '/historical_','/snapshots/','/history/','/runtime','/__pycache__/',
 '/finite_systems_twenty_ninth/','/finite_systems_twenty_eighth/',
 '/208-','/209-','/ofs_gate/','/fth_gate/',
 '/order_geometry_tenth/','/order_geometry_tenth_desk/',
 '/finite_systems_tenth/','/finite_systems_nineteenth/']

def selected(name):
    low=name.lower()
    batch='docs/papers204_208_sequence/'
    return (low.endswith(('.md','.tex')) and not any(x in low for x in EXCLUSIONS)
       and not any(x in Path(low).name for x in ['p208','p209','ofs','fth'])
       and (not low.startswith(batch) or low.startswith(batch+'scouting/')))

def discover():
    code,raw=command('discovery',['rg','--files','papers','docs'])
    if code != 0:
        raise RuntimeError('discovery failed')
    allnames=raw.decode().splitlines()
    names=sorted(n for n in allnames if selected(n))
    emit(BASE/'evidence'/'selected_paths.txt',('\n'.join(names)+'\n').encode())
    emit(BASE/'evidence'/'excluded_paths.txt',('\n'.join(sorted(set(allnames)-set(names)))+'\n').encode())
    js(BASE/'evidence'/'selection.json', {'extensions':['.md','.tex'],
       'excluded_path_substrings_casefolded':EXCLUSIONS,
       'excluded_basenames_containing_casefolded':['p208','p209','ofs','fth'],
       'additional_exclusion':'all current-batch root documentary files outside scouting; controls read via exact captured bytes',
       'count':len(names),'discovered_count':len(allnames),
       'scope':'explicit selected workspace papers/docs; no full internal or worldwide clearance'})
    js(BASE/'evidence'/'discovery_pins.json',pins(names))
    named=[]
    for name in ['rg','python3','curl','pdftotext','cmp']:
        actual=shutil.which(name)
        named.append({'name':name,'path':actual,'resolved':str(Path(actual).resolve()) if actual else None,
                      'sha256':digest(Path(actual)) if actual else None})
    js(BASE/'evidence'/'named_tools.json',named)
    print(json.dumps({'selected_count':len(names),'discovered_count':len(allnames)}))

if __name__=='__main__':
    action=sys.argv[1]
    if action=='discover':
        discover()
    elif action=='search':
        names=(BASE/'evidence'/'selected_paths.txt').read_text().splitlines()
        command(sys.argv[2],['rg','-n','-i','--',sys.argv[3],*names],names)
    elif action=='snapshot':
        snapshot(sys.argv[2],sys.argv[3:])
        print(json.dumps({'copied':len(sys.argv[3:]),'label':sys.argv[2]}))
    elif action=='command':
        command(sys.argv[2],sys.argv[3:])
    elif action=='checked':
        inputs=sorted(str(p.relative_to(ROOT)) for p in BASE.rglob('*') if p.is_file())
        command(sys.argv[2],sys.argv[3:],inputs)
    elif action=='seal':
        paths=sorted(p for p in BASE.rglob('*') if p.is_file() and p!=BASE/'SHA256SUMS')
        emit(BASE/'SHA256SUMS',''.join(f'{digest(p)}  {p.relative_to(BASE)}\n' for p in paths).encode())
        print(json.dumps({'payloads':len(paths)}))
    else:
        raise RuntimeError(f'unknown action: {action}')
