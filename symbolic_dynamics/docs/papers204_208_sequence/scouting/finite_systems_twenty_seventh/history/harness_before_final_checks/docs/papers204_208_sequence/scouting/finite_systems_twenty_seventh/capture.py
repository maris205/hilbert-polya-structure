"""Append-only bounded documentary capture; not a hermetic science runner."""
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
import time

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
BASE = ROOT / 'docs/papers204_208_sequence/scouting/finite_systems_twenty_seventh'

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
        dest=BASE/'history'/label/row['path']
        emit(dest, (ROOT/row['path']).read_bytes())
        rows.append({**row, 'copy':str(dest.relative_to(BASE)), 'copy_sha256':digest(dest)})
    after=pins(names)
    js(BASE/'history'/f'{label}.json', {'before':before,'after':after,'copies':rows,
       'equal':before==after and all(r['sha256']==r['copy_sha256'] for r in rows)})
    if not before==after or not all(r['sha256']==r['copy_sha256'] for r in rows):
        raise RuntimeError('historical input changed during capture')

def command(label, argv, inputs=()):
    dest=BASE/'evidence'/label
    dest.mkdir(parents=True, exist_ok=False)
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

def discover():
    control=['AGENTS.md','SYMBOLIC_DYNAMICS_STATE.md','docs/research_state/WORKFLOW.md',
       'docs/research_state/HISTORY_AND_CAVEATS.md','docs/papers204_208_sequence/PIPELINE_STATE.md',
       'docs/papers204_208_sequence/PROBLEM_ANCHOR.md',
       'docs/papers204_208_sequence/scouting/finite_systems_twenty_sixth/INTAKE.md',
       'docs/papers204_208_sequence/scouting/finite_systems_twenty_sixth/PROOF_PACKAGE.md',
       'docs/papers204_208_sequence/scouting/finite_systems_twenty_sixth/SOURCE_AND_HISTORY.md']
    snapshot('controls',control)
    code,raw=command('discovery',['rg','--files','papers','docs'])
    if code != 0:
        raise RuntimeError('discovery failed')
    exclusions=['/reviews/','/qa/','/frozen','/source_context/','/history_inputs/',
       '/historical_','/snapshots/','/history/','/runtime','/__pycache__/',
       '/finite_systems_twenty_seventh/','/208-','/209-','/OFS_GATE/','/FTH_GATE/',
       '/order_geometry_tenth/','/finite_systems_nineteenth/']
    names=sorted(n for n in raw.decode().splitlines()
       if n.endswith(('.md','.tex')) and not any(x in n for x in exclusions)
       and not any(x in Path(n).name for x in ['P208','P209']))
    emit(BASE/'evidence'/'selected_paths.txt',('\n'.join(names)+'\n').encode())
    js(BASE/'evidence'/'selection.json', {'extensions':['.md','.tex'],
       'excluded_path_substrings':exclusions,'excluded_basenames_containing':['P208','P209'],
       'count':len(names),'scope':'selected workspace papers/docs, not full worldwide/internal proof clearance'})
    js(BASE/'evidence'/'discovery_pins.json',pins(names))
    named=[]
    for name in ['rg','python3','curl']:
        actual=shutil.which(name)
        named.append({'name':name,'path':actual,'resolved':str(Path(actual).resolve()) if actual else None,
                      'sha256':digest(Path(actual)) if actual else None})
    js(BASE/'evidence'/'named_tools.json',named)
    print(json.dumps({'selected_count':len(names),'controls_copied':len(control)}))

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
    elif action=='seal':
        paths=sorted(p for p in BASE.rglob('*') if p.is_file() and p.name!='SHA256SUMS')
        emit(BASE/'SHA256SUMS',''.join(f'{digest(p)}  {p.relative_to(BASE)}\n' for p in paths).encode())
        print(json.dumps({'payloads':len(paths)}))
    else:
        raise RuntimeError(f'unknown action: {action}')
