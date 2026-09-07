"""Exact original-box pair with source capsules and a runtime superset.

Not a hermeticity claim: no syscall tracer is available, and dynamic-file
coverage is reported for observed Python modules plus declared link/config
inputs rather than asserted for every possible operating-system access.
"""
import hashlib
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys
import time

ROOT=Path('/root/autodl-tmp/symbolic_dynamics')
BASE=ROOT/'docs/papers204_208_sequence/scouting/finite_systems_twenty_seventh'
OUT=BASE/'execution'
ENV={'PATH':'/root/miniconda3/bin:/usr/bin:/bin','LANG':'C.UTF-8','LC_ALL':'C.UTF-8'}

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def emit(path,data):
    path.parent.mkdir(parents=True,exist_ok=True)
    with path.open('xb') as stream:
        stream.write(data)

def js(path,value):
    emit(path,(json.dumps(value,indent=2,ensure_ascii=False)+'\n').encode())

def pins(paths):
    return [{'path':str(p),'resolved':str(p.resolve()),'sha256':digest(p)} for p in sorted(set(paths))]

def run(label,argv,inputs=()):
    dest=OUT/label
    dest.mkdir(parents=True,exist_ok=False)
    before=pins(inputs)
    js(dest/'inputs_before.json',before)
    started=time.time_ns()
    try:
        result=subprocess.run(argv,cwd=ROOT,env=ENV,stdin=subprocess.DEVNULL,
                              capture_output=True,close_fds=True)
        code=result.returncode
        stdout,stderr=result.stdout,result.stderr
    except OSError as error:
        code=None
        stdout,stderr=b'',repr(error).encode()
    emit(dest/'stdout.bin',stdout)
    emit(dest/'stderr.bin',stderr)
    after=pins(inputs)
    js(dest/'inputs_after.json',after)
    js(dest/'receipt.json',{'argv':argv,'cwd':str(ROOT),'env':ENV,'exit':code,
       'stdin':'DEVNULL','close_fds':True,'started_ns':started,'finished_ns':time.time_ns(),
       'inputs_equal':before==after,'input_count':len(before),
       'stdout_sha256':digest(dest/'stdout.bin'),'stderr_sha256':digest(dest/'stderr.bin')})
    print(json.dumps({'label':label,'exit':code,'inputs':len(before),'equal':before==after,
                      'stdout_bytes':len(stdout),'stderr_bytes':len(stderr)}),flush=True)
    if code!=0 or before!=after:
        raise RuntimeError(f'failed command/input check: {label}')
    return stdout,stderr

OUT.mkdir(parents=True,exist_ok=False)
source_names=['INTAKE.md','PREPILOT_PROOF.md','PREPILOT_SOURCE.md','pilot.py','run_pair.py']
source_paths=[BASE/name for name in source_names]
source_before=pins(source_paths)
js(OUT/'source_inputs_before.json',source_before)
for name in source_names:
    emit(OUT/'source_inputs'/name,(BASE/name).read_bytes())
source_after=pins(source_paths)
js(OUT/'source_inputs_after.json',source_after)
if source_before!=source_after:
    raise RuntimeError('source input changed while physically copying')

stdlib=Path('/root/miniconda3/lib/python3.12')
rg=Path('/usr/lib/node_modules/@openai/codex/node_modules/@openai/codex-linux-x64/vendor/x86_64-unknown-linux-musl/codex-path/rg')
raw,_=run('stdlib_discovery',[str(rg),'--files','-g','*.py','-g','*.so',
       '-g','!site-packages/**','-g','!__pycache__/**',str(stdlib)])
runtime=sorted(Path(name) for name in raw.decode().splitlines()
               if '/site-packages/' not in name and '/__pycache__/' not in name)
if not runtime:
    raise RuntimeError('empty runtime superset')
emit(OUT/'stdlib_selected_paths.txt',(''.join(str(p)+'\n' for p in runtime)).encode())
js(OUT/'stdlib_selection.json',{'declared_root':str(stdlib),'selected_count':len(runtime),
       'extensions':['.py','.so'],'excluded_path_components':['site-packages','__pycache__'],
       'scope':'stdlib source/extension superset; isolated no-site, fresh absent pycache prefix'})
python=Path('/root/miniconda3/bin/python3')
math_modules=sorted(p for p in runtime if p.name.startswith('math.') and p.suffix=='.so')
if len(math_modules)!=1:
    raise RuntimeError('unexpected math extension selection')
linked=[]
ldd=shutil.which('ldd',path=ENV['PATH'])
if not ldd:
    raise RuntimeError('ldd unavailable')
for label,path in [('python',python),('math',math_modules[0])]:
    raw,_=run('ldd_'+label,[ldd,str(path)],[path,Path(ldd)])
    for line in raw.decode().splitlines():
        match=re.search(r'(?:=>\s*)?(/[^\s]+)',line)
        if match:
            resolved=Path(match.group(1))
            if resolved.is_file():
                linked.append(resolved)
            else:
                raise RuntimeError(f'ldd referent absent: {resolved}')
config=[]
config_candidates=[Path('/etc/ld.so.cache'),Path('/etc/ld.so.preload'),Path('/root/miniconda3/lib/python312.zip')]
for directory in [Path('/usr/lib/locale/C.utf8'),Path('/usr/lib/locale/C.UTF-8')]:
    if directory.is_dir():
        config.extend(p for p in directory.rglob('*') if p.is_file())
for path in config_candidates:
    if path.is_file():
        config.append(path)
presence=[{'path':str(p),'exists':p.exists(),'is_file':p.is_file()} for p in config_candidates]
js(OUT/'config_presence_before.json',presence)
runtime=sorted(set(runtime+[python,Path(ldd),rg]+linked+config))
js(OUT/'runtime_inputs_before.json',pins(runtime))
capsules=[]
observed=[]
for serial in (1,2):
    capsule=OUT/f'capsule_{serial}'
    for name in source_names:
        emit(capsule/'source'/name,(OUT/'source_inputs'/name).read_bytes())
    local=[capsule/'source'/name for name in source_names]
    cache=capsule/'absent_pycache_prefix'
    if cache.exists():
        raise RuntimeError('cache prefix unexpectedly exists')
    args=[str(python),'-I','-S','-B','-X',f'pycache_prefix={cache}',str(capsule/'source'/'pilot.py')]
    stdout,stderr=run(f'run_{serial}',args,runtime+local+source_paths)
    if cache.exists():
        raise RuntimeError('no-bytecode command created its cache directory')
    module_rows=[]
    covered={p.resolve() for p in runtime+local+source_paths}
    for line in stderr.decode().splitlines():
        if line.startswith('MODULE '):
            _,name,path=line.split(' ',2)
            p=Path(path)
            row={'name':name,'path':path,'resolved':str(p.resolve()),
                 'sha256':digest(p),'covered':p.resolve() in covered}
            module_rows.append(row)
            if not row['covered']:
                raise RuntimeError(f'observed module unpinned: {path}')
    js(OUT/f'run_{serial}'/'observed_modules.json',module_rows)
    capsules.append({'serial':serial,'source_inputs':pins(local),
         'cache_prefix':str(cache),'cache_exists_after':cache.exists()})
    observed.extend(module_rows)
run('compare_pair',['/usr/bin/cmp',str(OUT/'run_1'/'stdout.bin'),str(OUT/'run_2'/'stdout.bin')],
    [OUT/'run_1'/'stdout.bin',OUT/'run_2'/'stdout.bin',Path('/usr/bin/cmp')])
emit(OUT/'CANONICAL.txt',(OUT/'run_1'/'stdout.bin').read_bytes())
for serial in (1,2):
    run(f'compare_canonical_{serial}',['/usr/bin/cmp',str(OUT/f'run_{serial}'/'stdout.bin'),str(OUT/'CANONICAL.txt')],
       [OUT/f'run_{serial}'/'stdout.bin',OUT/'CANONICAL.txt',Path('/usr/bin/cmp')])
after=pins(runtime)
js(OUT/'runtime_inputs_after.json',after)
after_presence=[{'path':str(p),'exists':p.exists(),'is_file':p.is_file()} for p in config_candidates]
js(OUT/'config_presence_after.json',after_presence)
before=json.loads((OUT/'runtime_inputs_before.json').read_text())
if before!=after or presence!=after_presence or source_before!=pins(source_paths):
    raise RuntimeError('pair runtime/config/source changed')
js(OUT/'PAIR_RECEIPT.json',{'status':'AUTHOR_ORIGINAL_BOX_PAIR_PASS',
    'boxes':33,'states':2743,'capsules':capsules,'runtime_files':len(runtime),
    'observed_module_rows':len(observed),'raw_pair_and_two_canonical_comparisons':True,
    'source_inputs_unchanged':True,'runtime_inputs_unchanged':True,
    'scope':'full stdout preserved, complete selected runtime superset and observed module closure; not syscall-hermetic or independent review',
    'canonical_sha256':digest(OUT/'CANONICAL.txt')})
