"""Bounded documentary capture, not a scientific producer or hermetic runner."""
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
BASE = ROOT / 'docs/papers204_208_sequence/scouting/finite_systems_twenty_sixth'

def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def emit(p, data):
    p.parent.mkdir(parents=True, exist_ok=True)
    if p.exists():
        raise RuntimeError(f'refusing overwrite: {p}')
    p.write_bytes(data)

def js(p, value):
    emit(p, (json.dumps(value, indent=2, ensure_ascii=False)+'\n').encode())

def command(label, argv):
    target=BASE/'evidence'/label
    target.mkdir(parents=True, exist_ok=False)
    r=subprocess.run(argv,cwd=ROOT,capture_output=True)
    emit(target/'stdout.bin',r.stdout)
    emit(target/'stderr.bin',r.stderr)
    js(target/'receipt.json',{'argv':argv,'cwd':str(ROOT),'exit':r.returncode,
       'stdout_sha256':digest(target/'stdout.bin'),'stderr_sha256':digest(target/'stderr.bin')})
    return r

def snapshot(paths, label):
    result=[]
    for name in paths:
        p=ROOT/name
        q=BASE/'history'/label/name
        emit(q,p.read_bytes())
        result.append({'origin':name,'snapshot':str(q.relative_to(BASE)),
                       'sha256':digest(q),'unchanged_at_capture':digest(p)==digest(q)})
    js(BASE/'history'/f'{label}.json',result)

def search():
    exclusions=['/reviews/','/qa/','/frozen','/source_context/','/history_inputs/',
       '/historical_','/snapshots/','/history/','/runtime','/__pycache__/',
       '/finite_systems_twenty_sixth/','/208-original-snapshot-triangulation-sweeps/',
       '/209-ordered-fibre-threading/','/OFS_GATE/','/FTH_GATE/']
    r=command('discovery_paths',['rg','--files','papers','docs'])
    names=sorted(n for n in r.stdout.decode().splitlines()
        if n.endswith(('.md','.tex')) and not any(x in n for x in exclusions))
    emit(BASE/'evidence'/'selected_paths.txt', ('\n'.join(names)+'\n').encode())
    js(BASE/'evidence'/'search_scope.json',{'extensions':['.md','.tex'],
         'exclusions':exclusions,'count':len(names),'limit':'bounded selected surface; not exhaustive historical proof clearance'})
    before=[{'path':n,'sha256':digest(ROOT/n)} for n in names]
    js(BASE/'evidence'/'search_inputs_before.json',before)
    query='subspace|lattice polynomial|matrix pair|AB,BA|AB, BA|noncommutative|multiset rewrit|gcd.*lcm|Bulgarian|incidence.*dynamics|Steiner|matroid|quasigroup|Nielsen|Hurwitz|polarization'
    r=command('history_search',['rg','-n','-i','--',query,*names])
    after=[{'path':n,'sha256':digest(ROOT/n)} for n in names]
    js(BASE/'evidence'/'search_inputs_after.json',after)
    js(BASE/'evidence'/'search_comparison.json',{'same':before==after,'count':len(names),
        'query':query,'exit':r.returncode})
    control=['AGENTS.md','SYMBOLIC_DYNAMICS_STATE.md','docs/research_state/WORKFLOW.md',
       'docs/research_state/HISTORY_AND_CAVEATS.md','docs/papers204_208_sequence/PIPELINE_STATE.md',
       'docs/papers204_208_sequence/PROBLEM_ANCHOR.md']
    snapshot(control,'controls')
    pins=[]
    for name in ['rg','python3','pdftotext','curl']:
        p=shutil.which(name)
        pins.append({'name':name,'path':p,'resolved':str(Path(p).resolve()) if p else None,
                     'sha256':digest(Path(p)) if p else None})
    js(BASE/'evidence'/'named_tool_pins.json',pins)
    print(json.dumps({'selected':len(names),'search_exit':r.returncode,'unchanged':before==after}))

def focused(label='focused', query=r'self[- ]commutator|skew[- ]symmetric|A\s*\+\s*\[A|A\+AA|A \+ AA'):
    names=(BASE/'evidence'/'selected_paths.txt').read_text().splitlines()
    before=[{'path':n,'sha256':digest(ROOT/n)} for n in names]
    js(BASE/'evidence'/f'{label}_inputs_before.json',before)
    r=command(f'{label}_search',['rg','-n','-i','--',query,*names])
    after=[{'path':n,'sha256':digest(ROOT/n)} for n in names]
    js(BASE/'evidence'/f'{label}_inputs_after.json',after)
    js(BASE/'evidence'/f'{label}_comparison.json',{'same':before==after,
        'count':len(names),'query':query,'exit':r.returncode})
    snapshot(['SYMBOLIC_DYNAMICS_STATE.md','docs/papers204_208_sequence/PIPELINE_STATE.md'],
             f'{label}_controls')
    print(json.dumps({'selected':len(names),'search_exit':r.returncode,'unchanged':before==after}))

if __name__=='__main__':
    if sys.argv[1]=='search': search()
    elif sys.argv[1]=='focused': focused()
    elif sys.argv[1]=='structural': focused('structural',r'tournament|cyclic triangle|largest.{0,45}smallest|smallest.{0,45}largest|doubl.{0,25}pile|pile.{0,25}doubl|extrem.{0,25}redistribut|Euclidean.{0,25}solitaire|balancing')
    elif sys.argv[1]=='snapshot': snapshot(sys.argv[3:],sys.argv[2])
    elif sys.argv[1]=='command':
        r=command(sys.argv[2],sys.argv[3:]); print(json.dumps({'exit':r.returncode,'stdout_bytes':len(r.stdout),'stderr_bytes':len(r.stderr)}))
    elif sys.argv[1]=='seal':
        paths=sorted(p for p in BASE.rglob('*') if p.is_file() and p.name!='SHA256SUMS')
        emit(BASE/'SHA256SUMS', ''.join(f'{digest(p)}  {p.relative_to(BASE)}\n' for p in paths).encode())
        print(json.dumps({'payloads':len(paths)}))
