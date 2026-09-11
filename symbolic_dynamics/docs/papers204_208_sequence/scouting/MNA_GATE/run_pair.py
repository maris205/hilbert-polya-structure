#!/usr/bin/env python3
"""Actual source-only pair and raw comparisons, complete non-secret provenance."""
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import sysconfig
import time

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
GATE = ROOT/'docs/papers204_208_sequence/scouting/MNA_GATE'
ENV = {'PATH':'/usr/bin:/bin','LANG':'C.UTF-8','LC_ALL':'C.UTF-8','TZ':'UTC'}

def pin(path):
    p = Path(path)
    return {'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'bytes':p.stat().st_size}

def save(path,obj):
    Path(path).write_text(json.dumps(obj,sort_keys=True,indent=2)+'\n')

def command(folder,argv):
    folder.mkdir()
    save(folder/'attempt.json', {'argv':argv,'cwd':str(ROOT),'environment':ENV,
                               'started_epoch':time.time(),'timeout_seconds':60})
    start=time.time()
    try:
        p=subprocess.run(argv,cwd=ROOT,env=ENV,stdout=subprocess.PIPE,stderr=subprocess.PIPE,timeout=60)
        output,error,code,timeout=p.stdout,p.stderr,p.returncode,False
    except subprocess.TimeoutExpired as exc:
        output,error,code,timeout=exc.stdout or b'',exc.stderr or b'',None,True
    (folder/'stdout.raw').write_bytes(output)
    (folder/'stderr.raw').write_bytes(error)
    receipt={'argv':argv,'cwd':str(ROOT),'environment':ENV,'started_epoch':start,
             'finished_epoch':time.time(),'exit':code,'timed_out':timeout,
             'stdout':pin(folder/'stdout.raw'),'stderr':pin(folder/'stderr.raw')}
    save(folder/'receipt.json',receipt)
    if code != 0:
        raise RuntimeError(('actual_command_failed',receipt))
    return output

def inventory(paths):
    return {str(p):pin(p) for p in sorted(set(map(Path,paths)),key=str)}

def main():
    pair=GATE/'evidence/pair01'
    pair.mkdir()
    executable=str(Path(sys.executable).resolve())
    cache=pair/'cache_must_remain_absent'
    if cache.exists():
        raise RuntimeError('source-only cache path already exists')
    # Broad known-input superset: all stdlib source and extension files, no site packages.
    stdlib=Path(sysconfig.get_path('stdlib'))
    runtime=[Path(executable),Path('/usr/bin/cmp'),Path('/usr/bin/ldd')]
    for directory,subdirs,files in os.walk(stdlib):
        subdirs[:]=[d for d in subdirs if d not in ('site-packages','__pycache__','test','tests','idle_test')]
        runtime.extend(Path(directory)/name for name in files if name.endswith(('.py','.so')))
    shared=[str(p) for p in runtime if p.suffix=='.so']
    ldd=command(pair/'00_ldd',[str(Path('/usr/bin/ldd')),executable,'/usr/bin/cmp']+shared)
    links=sorted({str(Path(os.fsdecode(x)).resolve()) for x in re.findall(rb'(/[^\s()]+)',ldd)
                  if Path(os.fsdecode(x)).is_file()})
    # Re-resolve bytes explicitly rather than treating textual symlink aliases as files.
    runtime.extend(Path(x) for x in links)
    science=[GATE/name for name in ('verify.py','run_observed.py','run_pair.py','INPUT_PINS.sha256','INPUT_ROLES.json')]
    frozen=[]
    for line in (GATE/'INPUT_PINS.sha256').read_text().splitlines():
        sha,rel=line.split('  ',1)
        path=ROOT/rel
        if pin(path)['sha256'] != sha:
            raise RuntimeError(('frozen input mismatch',rel))
        frozen.append(path)
    before=inventory(runtime+science+frozen)
    save(pair/'inputs_before.json',before)
    save(pair/'configuration.json', {'executable':executable,'stdlib':str(stdlib),'environment':ENV,
                                    'interpreter_flags':['-I','-S','-B','-X','pycache_prefix='+str(cache)],
                                    'strace_available':shutil.which('strace'),
                                    'runtime_role':'known_stdlib_source_and_extension_superset_plus_ldd',
                                    'known_inputs':len(before)})
    argv=[executable,'-I','-S','-B','-X','pycache_prefix='+str(cache),
          str(GATE/'run_observed.py'),str(GATE/'verify.py')]
    out1=command(pair/'01_verify',argv+[str(pair/'runtime01.json')])
    out2=command(pair/'02_verify',argv+[str(pair/'runtime02.json')])
    canonical=GATE/'CANONICAL.json'
    if canonical.exists():
        raise RuntimeError('refuse overwriting any earlier canonical')
    canonical.write_bytes(out1)
    command(pair/'03_cmp_canonical_1',['/usr/bin/cmp',str(pair/'01_verify/stdout.raw'),str(canonical)])
    command(pair/'04_cmp_canonical_2',['/usr/bin/cmp',str(pair/'02_verify/stdout.raw'),str(canonical)])
    command(pair/'05_cmp_pair',['/usr/bin/cmp',str(pair/'01_verify/stdout.raw'),str(pair/'02_verify/stdout.raw')])
    after=inventory(before)
    save(pair/'inputs_after.json',after)
    if before != after:
        raise RuntimeError('known-input drift')
    observed_rows=[]
    for name in ('runtime01.json','runtime02.json'):
        observed=json.loads((pair/name).read_text())
        for path,record in observed['files'].items():
            if path.startswith('/proc/'):
                continue
            if path not in before:
                raise RuntimeError(('observed file outside before capsule',name,path))
            if before[path] != record:
                raise RuntimeError(('observed file changed',name,path))
        observed_rows.append({'runtime':name,'observed_file_count':len(observed['files']),
                              'all_nonproc_files_in_before_capsule':True})
    if cache.exists():
        raise RuntimeError('bytecode cache unexpectedly exists')
    data=json.loads(out1)
    summary={'status':'PASS','role':'actual_independent_source_only_pair',
             'known_inputs_unchanged':len(before),'commands':6,
             'stdout':pin(canonical),'checks_each':data['check_count'],'states_each':data['state_count'],
             'runtime_observations':observed_rows,'raw_comparisons':3,
             'OS_syscall_trace':'UNAVAILABLE_strace_not_installed',
             'runtime_limit':'Python opens/modules/proc maps observed, not complete OS file syscall tracing'}
    save(pair/'RESULT.json',summary)
    print(json.dumps(summary,sort_keys=True,indent=2))

if __name__=='__main__':
    main()
