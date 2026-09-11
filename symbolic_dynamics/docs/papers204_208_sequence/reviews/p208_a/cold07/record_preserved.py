"""Review A evidence recorder. Artifacts are created by this pinned program."""
from pathlib import Path
import hashlib, json, os, subprocess, sys, time, shutil
import sysconfig

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
OUT = ROOT / 'docs/papers204_208_sequence/reviews/p208_a'
FREEZE = ROOT / 'papers/208-original-snapshot-triangulation-sweeps/frozen_round0'

def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def dump(p, x):
    Path(p).write_text(json.dumps(x, indent=2, sort_keys=True) + '\n')

def pins(paths):
    return {str(Path(p).resolve()): sha(p) for p in sorted(set(map(str, paths)))}

def command(argv, cwd, env, prefix):
    start = time.time_ns()
    p = subprocess.run(argv, cwd=cwd, env=env, capture_output=True)
    Path(str(prefix)+'.stdout').write_bytes(p.stdout)
    Path(str(prefix)+'.stderr').write_bytes(p.stderr)
    r = dict(argv=argv, cwd=str(cwd), env=env, exit=p.returncode,
             start_ns=start, end_ns=time.time_ns(), stdout=str(prefix)+'.stdout',
             stderr=str(prefix)+'.stderr')
    dump(str(prefix)+'.json', r)
    if p.returncode:
        raise RuntimeError(r)
    return r

def initial():
    files = sorted(p for p in FREEZE.rglob('*') if p.is_file())
    assert len(files) == 488
    assert sha(FREEZE/'SHA256SUMS') == '12dca26eeb68503737846c633170bd427101648c21a9e89ef710d9ddaef01ace'
    for line in (FREEZE/'SHA256SUMS').read_text().splitlines():
        h, rel = line.split('  ',1)
        assert sha(FREEZE/rel) == h, rel
    (OUT/'INPUT_PINS.sha256').write_text(''.join(f'{sha(p)}  {p.relative_to(ROOT)}\n' for p in files))
    context = [ROOT/p for p in ['SYMBOLIC_DYNAMICS_STATE.md', 'docs/papers204_208_sequence/PIPELINE_STATE.md', '.agents/skills/symbolic-dynamics-research/SKILL.md', 'docs/research_state/WORKFLOW.md', 'docs/papers204_208_sequence/ARTIFACT_CONTRACT.md', 'docs/papers197_201_sequence/HOSTILE_REVIEW_PROTOCOL.md']]
    dump(OUT/'CONTEXT_AT_ASSIGNMENT.json', pins(context))
    dump(OUT/'INITIAL_PIN_RECEIPT.json', dict(time_ns=time.time_ns(), frozen_files=488,
         chronology='Before substantive frozen-manuscript/proof/code inspection; instructions and directory listing already read.',
         recorder_sha256=sha(__file__), input_pins_sha256=sha(OUT/'INPUT_PINS.sha256')))
    print('PASS: 487 frozen referents + immutable manifest pinned before substantive inspection.')

ENV={'PATH':'/usr/local/bin:/usr/bin:/bin','LANG':'C','LC_ALL':'C','TZ':'UTC',
     'PYTHONHASHSEED':'0','PYTHONOPTIMIZE':'0','PYTHONDONTWRITEBYTECODE':'1'}

WRAPPER="""import sys, pathlib, json, hashlib
assert sys.flags.optimize==0 and sys.flags.isolated==1 and sys.flags.no_site==1 and sys.dont_write_bytecode
assert sys.pycache_prefix and not pathlib.Path(sys.pycache_prefix).exists()
p=pathlib.Path('verify.py')
exec(compile(p.read_bytes(),str(p),'exec',optimize=0),{'__name__':'__main__','__file__':str(p)})
modules={str(pathlib.Path(m.__file__).resolve()):hashlib.sha256(pathlib.Path(m.__file__).read_bytes()).hexdigest() for m in tuple(sys.modules.values()) if getattr(m,'__file__',None) and pathlib.Path(m.__file__).is_file()}
assert not pathlib.Path(sys.pycache_prefix).exists()
pathlib.Path(sys.argv[1]).write_text(json.dumps({'flags':{'optimize':sys.flags.optimize,'isolated':sys.flags.isolated,'no_site':sys.flags.no_site,'dont_write_bytecode':sys.dont_write_bytecode},'pycache_prefix':sys.pycache_prefix,'executable':sys.executable,'version':sys.version,'modules':modules},sort_keys=True,indent=2)+'\\n')
"""

def configuration():
    base=[Path('/etc/ld.so.cache'),Path('/etc/ld.so.conf'),Path('/etc/ld.so.preload')]
    base+=list(Path('/etc/ld.so.conf.d').glob('*'))
    base+=list((Path(sysconfig.get_path('stdlib'))/'site-packages').glob('*.pth'))
    return [p for p in base if p.is_file()]

def replay(label, produce=False):
    dest=OUT/label;dest.mkdir()
    shutil.copyfile(__file__,dest/'record_preserved.py')
    run=dest/'source_only';run.mkdir()
    shutil.copyfile(OUT/'verify.py',run/'verify.py')
    inputs=[p for p in FREEZE.rglob('*') if p.is_file()]+[OUT/'verify.py',OUT/'kernel.py',OUT/'record.py',OUT/'INPUT_PINS.sha256']
    if not produce:inputs.append(OUT/'CANONICAL.json')
    before=pins(inputs);dump(dest/'INPUTS_BEFORE.json',before)
    std=Path(sysconfig.get_path('stdlib'))
    fixed_tools=[Path(sys.executable).resolve(),Path('/usr/bin/cmp'),Path('/usr/bin/ldd'),Path('/bin/bash')]
    runtime=list(fixed_tools)
    runtime += [p for p in std.rglob('*') if p.is_file() and 'site-packages' not in p.parts and '__pycache__' not in p.parts]
    # Python site startup is enabled under -I; pin its already-imported modules too.
    runtime += [Path(m.__file__).resolve() for m in tuple(sys.modules.values()) if getattr(m,'__file__',None) and Path(m.__file__).is_file()]
    # All candidate Python source/extension files are inventoried before execution.
    dump(dest/'RUNTIME_INVENTORY_BEFORE.json',pins(runtime))
    dump(dest/'TOOLS_BEFORE.json',pins(fixed_tools))
    config=pins(configuration());dump(dest/'CONFIG_BEFORE.json',config)
    command(['/usr/bin/ldd',str(Path(sys.executable).resolve())],run,ENV,dest/'python_ldd')
    linked=[]
    for token in (dest/'python_ldd.stdout').read_text().split():
        if token.startswith('/') and Path(token).is_file():linked.append(token)
    for name in ['cmp','bash']:
        command(['/usr/bin/ldd','/usr/bin/'+name],run,ENV,dest/(name+'_ldd'))
        raw=(dest/(name+'_ldd.stdout')).read_text();assert 'not found' not in raw
        linked.extend(t for t in raw.split() if t.startswith('/') and Path(t).is_file())
    # Shared objects used by any stdlib extension can be selected before actual import.
    extensions=[str(p) for p in runtime if str(p).endswith('.so')]
    if extensions:
        command(['/usr/bin/ldd',*extensions],run,ENV,dest/'extensions_ldd')
        for token in (dest/'extensions_ldd.stdout').read_text().split():
            if token.startswith('/') and Path(token).is_file():linked.append(token)
    dump(dest/'LIBRARIES_BEFORE.json',pins(linked))
    dump(dest/'LAUNCH_INPUTS.json',dict(recorder_sha256=sha(__file__),wrapper=WRAPPER,env=ENV,source_only_files=['verify.py'],verify_sha256=sha(run/'verify.py')))
    cache=dest/'unused_bytecode_cache';assert not cache.exists()
    command([sys.executable,'-I','-S','-B','-X','pycache_prefix='+str(cache),'-c',WRAPPER,str(dest/'CONSUMED_RUNTIME.json')],run,ENV,dest/'producer')
    if produce:shutil.copyfile(dest/'producer.stdout',OUT/'CANONICAL.json')
    command(['/usr/bin/cmp',str(dest/'producer.stdout'),str(OUT/'CANONICAL.json')],run,ENV,dest/'canonical_cmp')
    after=pins(inputs);dump(dest/'INPUTS_AFTER.json',after);assert before==after
    consumed=json.loads((dest/'CONSUMED_RUNTIME.json').read_text())['modules']
    inventory=json.loads((dest/'RUNTIME_INVENTORY_BEFORE.json').read_text())
    # Imports are exact files, never stale bytecode; source-only verifier is separately pinned.
    for p,h in consumed.items():assert inventory.get(p)==h,(p,'not pinned before')
    dump(dest/'RUNTIME_CONSUMED_AFTER.json',pins(consumed));assert pins(consumed)==consumed
    dump(dest/'TOOLS_AFTER.json',pins(fixed_tools));assert pins(fixed_tools)==json.loads((dest/'TOOLS_BEFORE.json').read_text())
    dump(dest/'LIBRARIES_AFTER.json',pins(linked));assert pins(linked)==json.loads((dest/'LIBRARIES_BEFORE.json').read_text())
    dump(dest/'CONFIG_AFTER.json',pins(config));assert pins(config)==config
    assert sha(run/'verify.py')==sha(OUT/'verify.py')
    dump(dest/'RECEIPT.json',dict(status='PASS',assertions=json.loads((dest/'producer.stdout').read_text())['assertions'],
        canonical_sha256=sha(OUT/'CANONICAL.json'),source_only_before=['verify.py'],source_only_after=sorted(p.name for p in run.iterdir()),
        full_input_count=len(inputs),runtime_consumed_count=len(consumed),libraries_count=len(set(linked))))
    print(label,'PASS')

if __name__ == '__main__':
    if sys.argv[1] == 'initial': initial()
    elif sys.argv[1]=='replay':replay(sys.argv[2],len(sys.argv)>3 and sys.argv[3]=='produce')
