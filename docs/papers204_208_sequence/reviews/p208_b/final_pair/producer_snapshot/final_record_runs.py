"""Final strict pair infrastructure; earlier recorder/executions remain untouched.

Executes only B science. Imported old recorder supplies generic pin helpers.
Source execution and all observed map files have explicit pre/post coverage.
"""
from pathlib import Path
import hashlib
import json
import os
import subprocess
import sys
import time
import uuid

BASE=Path('/root/autodl-tmp/symbolic_dynamics/docs/papers204_208_sequence/reviews/p208_b')
ROOT=BASE.parents[3]
assert ROOT==Path('/root/autodl-tmp/symbolic_dynamics')
# Source-only infrastructure reuse, not a scientific implementation import.
ns={'__name__':'infrastructure_helpers','__file__':str(BASE/'record_runs.py')}
exec(compile((BASE/'record_runs.py').read_bytes(),str(BASE/'record_runs.py'),'exec',optimize=0),ns)
sha,write,pinset=ns['sha'],ns['write'],ns['pinset']
ENV=ns['ENV']
OUT=BASE/'final_pair'
OBSERVED={}
def runtime():
    report={'version':sys.version,'flags':repr(sys.flags),'path':sys.path,
            'pycache_prefix':sys.pycache_prefix,'environment':dict(os.environ),
            'executable':sys.executable,'modules':{}}
    for name,m in sorted(sys.modules.items()):
        p=getattr(m,'__file__',None);spec=getattr(m,'__spec__',None)
        report['modules'][name]={'file':p,'origin':getattr(spec,'origin',None),
          'loader':type(getattr(spec,'loader',None)).__name__,
          'sha256':sha(p) if p and Path(p).is_file() else None}
    raw=Path('/proc/self/maps').read_text();report['maps_raw']=raw
    report['map_files']=pinset(line.split(None,5)[5] for line in raw.splitlines()
                               if len(line.split(None,5))==6 and line.split(None,5)[5].startswith('/'))
    return report
def command(name,args):
    start=time.time();snapshots=[];last=None
    with (OUT/(name+'.stdout')).open('xb') as stdout,(OUT/(name+'.stderr')).open('xb') as stderr:
        child=subprocess.Popen(args,cwd=ROOT,env=ENV,stdout=stdout,stderr=stderr)
        while child.poll() is None:
            try:raw=Path(f'/proc/{child.pid}/maps').read_text()
            except (FileNotFoundError,ProcessLookupError,PermissionError):raw=''
            if raw and raw!=last:
                snapshots.append(raw);last=raw
                for line in raw.splitlines():
                    parts=line.split(None,5)
                    if len(parts)==6 and parts[5].startswith('/') and Path(parts[5]).is_file():
                        OBSERVED[parts[5]]=sha(parts[5])
            time.sleep(.005)
        code=child.wait()
    write(OUT/(name+'.command.json'),{'argv':[str(x) for x in args],'cwd':str(ROOT),
         'environment':ENV,'exit_code':code,'seconds':time.time()-start,
         'stdout_sha256':sha(OUT/(name+'.stdout')),'stderr_sha256':sha(OUT/(name+'.stderr')),
         'observed_maps':len(snapshots)})
    write(OUT/(name+'.maps.json'),snapshots)
    assert code==0,('preserved failed command',name,code)
    return (OUT/(name+'.stdout')).read_text()
def main():
    assert sys.flags.optimize==0 and sys.flags.isolated and sys.flags.no_site and sys.dont_write_bytecode
    assert sys.pycache_prefix and not Path(sys.pycache_prefix).exists()
    OUT.mkdir(exist_ok=False)
    before_runtime=runtime();write(OUT/'RECORDER_RUNTIME_BEFORE.json',before_runtime)
    paths=ns['snapshot_paths']()
    context=json.loads((BASE/'SOURCE_CONTEXT_PINS.json').read_text())['paths']
    for p,row in context.items():
        assert sha(p)==row['sha256']==sha(BASE/row['snapshot'])
        paths.add(p);paths.add(str(BASE/row['snapshot']))
    paths|={str(Path(p).resolve()) for p in list(paths)}
    paths|=set(before_runtime['map_files'])
    paths|={i['file'] for i in before_runtime['modules'].values() if i['sha256']}
    # This is a relevant-input superset, not a claim that all stdlib was used.
    libraries=set();links=[]
    std=Path(ns['sysconfig'].get_path('stdlib'))
    roots=[Path(sys.executable).resolve(),Path('/usr/bin/cmp'),Path('/bin/bash').resolve()]
    for i,p in enumerate(roots+sorted(std.glob('lib-dynload/*.so'))):
        raw=command(f'ldd_{i:03d}',['/usr/bin/ldd',str(p)])
        assert 'not found' not in raw
        aliases=[]
        for token in raw.split():
            if token.startswith('/') and Path(token).is_file():
                aliases.append(token);libraries.add(str(Path(token).resolve()));paths.add(token)
        links.append({'target':str(p),'aliases':aliases})
    paths|=libraries
    cfg=ns['configuration']()
    paths|={p for p,row in cfg.items() if row['exists'] and Path(p).is_file()}
    before=pinset(paths)
    write(OUT/'INPUTS_BEFORE.json',before);write(OUT/'CONFIG_BEFORE.json',cfg)
    write(OUT/'LINK_DEPENDENCIES.json',links)
    # Retain actual B producer bytes, not just mutable absolute hashes.
    snap=OUT/'producer_snapshot';snap.mkdir()
    for p in sorted(BASE.glob('*.py')):
        with (snap/p.name).open('xb') as f:f.write(p.read_bytes())
    runs=[]
    for number in (1,2):
        prefix=OUT/('unused_pycache_'+uuid.uuid4().hex);assert not prefix.exists()
        args=[sys.executable,'-I','-S','-B','-X','pycache_prefix='+str(prefix),
              str(BASE/'runtime_probe.py'),str(BASE/'verify.py'),str(OUT/f'run_{number}.runtime.json')]
        command(f'run_{number}',args)
        report=json.loads((OUT/f'run_{number}.runtime.json').read_text())
        consumed=ns['consume'](report)
        missing={p:h for p,h in consumed.items() if before.get(p)!=h or sha(p)!=h}
        write(OUT/f'run_{number}.coverage.json',{'consumed':consumed,'missing':missing})
        assert not missing and report['cache_prefix_still_absent']
        assert not any(p.endswith('.pyc') for p in consumed)
        runs.append({'number':number,'exit_code':0,'pycache_prefix':str(prefix),
                     'consumed_files':len(consumed),'stdout_sha256':sha(OUT/f'run_{number}.stdout')})
    command('cmp_pair',['/usr/bin/cmp','-s',str(OUT/'run_1.stdout'),str(OUT/'run_2.stdout')])
    for i in (1,2):command(f'cmp_canonical_{i}',['/usr/bin/cmp','-s',str(OUT/f'run_{i}.stdout'),str(BASE/'CANONICAL.json')])
    after=pinset(paths);write(OUT/'INPUTS_AFTER.json',after)
    write(OUT/'CONFIG_AFTER.json',ns['configuration']())
    assert before==after and cfg==ns['configuration']()
    after_runtime=runtime();write(OUT/'RECORDER_RUNTIME_AFTER.json',after_runtime)
    used={**before_runtime['map_files'],**after_runtime['map_files'],**OBSERVED}
    for r in (before_runtime,after_runtime):
        used.update({i['file']:i['sha256'] for i in r['modules'].values() if i['sha256']})
    missing={p:h for p,h in used.items() if before.get(p)!=h or sha(p)!=h}
    write(OUT/'RECORDER_AND_OBSERVED_MAP_COVERAGE.json',{'consumed_or_observed':used,'missing':missing})
    assert not missing,missing
    assert not Path(sys.pycache_prefix).exists()
    receipt={'status':'PASS','runs':runs,'input_count':len(before),'configuration_count':len(cfg),
       'resolved_ldd_files':len(libraries),'raw_ldd_aliases':len(set(p for r in links for p in r['aliases'])),
       'recorder_and_observed_map_files':len(used),'comparisons':[0,0,0],
       'unchanged_complete_input_set':True,'source_only':True,'optimization':0,
       'limit':'Complete observed maps and consumed Python files covered; map sampling is not a syscall trace or hermetic historical OS claim.'}
    write(OUT/'RECEIPT.json',receipt);print(json.dumps(receipt,sort_keys=True))
if __name__=='__main__':main()
