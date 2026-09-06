"""Source-only candidate executions, raw outputs, runtime/input/environment pins."""
from pathlib import Path
import hashlib
import json
import os
import shutil
import subprocess
import sys
import time

HERE=Path(__file__).resolve().parent
ROOT=Path('/root/autodl-tmp/symbolic_dynamics')

def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()

def pins():
    rows=[]
    for name in ('INPUT_PINS.sha256','HISTORY_PINS.sha256'):
        if not (HERE/name).exists(): continue
        for line in (HERE/name).read_text().splitlines():
            h,p=line.split('  ',1)
            actual=sha(ROOT/p)
            rows.append({'manifest':name,'path':p,'expected':h,'actual':actual,'pass':h==actual})
    return rows

def main():
    label=sys.argv[1]
    assert label.replace('_','').isalnum()
    dest=HERE/label
    assert not dest.exists(), 'preserve previous executions'
    dest.mkdir()
    shutil.copy2(HERE/'verify.py',dest/'verify.py')
    exe=Path(sys.executable).resolve()
    before=pins()
    assert all(x['pass'] for x in before)
    env={'PATH':str(exe.parent)+':/usr/bin:/bin','LC_ALL':'C','LANG':'C',
         'TZ':'UTC','PYTHONHASHSEED':'0','PYTHONDONTWRITEBYTECODE':'1',
         'SOURCE_DATE_EPOCH':'1788652800'}
    runtime_code="import sys,json; print(json.dumps({'executable':sys.executable,'version':sys.version,'flags':repr(sys.flags),'optimize':sys.flags.optimize,'debug':__debug__,'isolated':sys.flags.isolated,'dont_write_bytecode':sys.dont_write_bytecode,'path':sys.path},sort_keys=True)); assert sys.flags.optimize==0 and __debug__ and sys.flags.isolated==1 and sys.dont_write_bytecode"
    runtime_cmd=[str(exe),'-I','-B','-c',runtime_code]
    probe=subprocess.run(runtime_cmd,cwd=dest,env=env,capture_output=True)
    (dest/'runtime.stdout').write_bytes(probe.stdout)
    (dest/'runtime.stderr').write_bytes(probe.stderr)
    assert probe.returncode==0
    cmd=[str(exe),'-I','-B','verify.py']
    start=time.time()
    run=subprocess.run(cmd,cwd=dest,env=env,capture_output=True)
    (dest/'stdout.json').write_bytes(run.stdout)
    (dest/'stderr.txt').write_bytes(run.stderr)
    after=pins()
    comparisons=[]
    canonical=HERE/'CANONICAL.json'
    if run.returncode==0:
        if not canonical.exists():
            canonical.write_bytes(run.stdout)
        compare_cmd=['/usr/bin/cmp',str(dest/'stdout.json'),str(canonical)]
        cmp_result=subprocess.run(compare_cmd,cwd=dest,env=env,capture_output=True)
        (dest/'cmp.stdout').write_bytes(cmp_result.stdout)
        (dest/'cmp.stderr').write_bytes(cmp_result.stderr)
        comparisons.append({'command':compare_cmd,'exit':cmp_result.returncode,'kind':'raw byte cmp','canonical_sha256':sha(canonical)})
    record={'label':label,'cwd':str(dest),'source_only_initial_files':['verify.py'],
            'source_sha256_before':sha(HERE/'verify.py'),'copied_source_sha256_after':sha(dest/'verify.py'),
            'recorder_sha256':sha(Path(__file__)),'interpreter':str(exe),'interpreter_sha256':sha(exe),
            'environment':env,'runtime_command':runtime_cmd,'runtime_exit':probe.returncode,
            'command':cmd,'exit':run.returncode,'elapsed_seconds':time.time()-start,
            'stdout_sha256':sha(dest/'stdout.json'),'stderr_sha256':sha(dest/'stderr.txt'),
            'input_before':before,'input_after':after,'comparisons':comparisons,
            'note':'-I ignores PYTHONHASHSEED but deterministic code explicitly sorts all set outputs; no hidden imports or input files.'}
    (dest/'RECORD.json').write_text(json.dumps(record,sort_keys=True,indent=2)+'\n')
    assert all(x['pass'] for x in after)
    print(json.dumps({'label':label,'exit':run.returncode,'stdout_sha256':record['stdout_sha256'],'elapsed':record['elapsed_seconds'],'input_count':len(before),'comparison_exits':[c['exit'] for c in comparisons]}))
    sys.exit(run.returncode)

if __name__=='__main__': main()
