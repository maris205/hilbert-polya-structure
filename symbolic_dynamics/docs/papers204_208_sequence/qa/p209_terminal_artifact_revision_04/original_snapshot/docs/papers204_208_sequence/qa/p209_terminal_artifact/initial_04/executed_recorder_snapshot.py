"""Future root-only documentary auditor recorder; adaptation of P208 recorder.

No execution occurs during preparation. Each invocation creates one new
P209 artifact attempt, preserves full streams even on a failed child, then
seals only that attempt. Initial package reports/outer seals are root-owned.
"""
from datetime import datetime, timezone
from hashlib import sha256
import json
import os
from pathlib import Path
import subprocess
import sys

PREP=Path(__file__).resolve().parent
ROOT=Path('/root/autodl-tmp/symbolic_dynamics')
BASE=ROOT/'docs/papers204_208_sequence/qa/p209_terminal_artifact'
SOURCE=PREP/'audit_p209.py'
ENV={'PATH':'/usr/bin:/bin','LANG':'C.UTF-8','LC_ALL':'C.UTF-8','TZ':'UTC'}

def info(path):
    raw=Path(path).read_bytes()
    return {'bytes':len(raw),'sha256':sha256(raw).hexdigest()}

def save(path,raw):
    with Path(path).open('xb') as stream:stream.write(raw)

def dump(path,value):
    save(path,(json.dumps(value,sort_keys=True,indent=2)+'\n').encode())

def main():
    if sys.argv[1:] != ['initial_04']:
        raise RuntimeError('Require the new revision_03 initial_04 attempt')
    if not(sys.flags.optimize==0 and sys.flags.isolated and sys.flags.no_site and sys.dont_write_bytecode
           and dict(os.environ)==ENV and Path.cwd()==ROOT and Path(sys.executable).resolve()==Path('/usr/bin/python3.10')
           and PREP==ROOT/'docs/papers204_208_sequence/qa/p209_terminal_artifact_revision_03'
           and Path(__file__).resolve()==PREP/'record_audit.py'):
        raise RuntimeError('Require exact prepared path, system interpreter, -I -S -B, clean ENV and workspace cwd')
    required=[ROOT/'papers/209-ordered-fibre-threading/PAPER_MANIFEST.sha256',
              ROOT/'papers/209-ordered-fibre-threading/ROOT_LIFECYCLE.md',
              ROOT/'docs/papers204_208_sequence/qa/P209_TERMINAL_ROOT_VIEWS.actual.json',
              PREP/'SHA256SUMS',SOURCE,Path(__file__),Path(sys.executable).resolve(),
              ROOT/'docs/papers204_208_sequence/qa/p209_terminal_artifact_preparation/SHA256SUMS',
              BASE/'initial_01/SHA256SUMS',
              ROOT/'docs/papers204_208_sequence/qa/P209_TERMINAL_ARTIFACT_INITIAL_01.failed.actual.json',
              ROOT/'docs/papers204_208_sequence/qa/p209_terminal_artifact_revision_01/SHA256SUMS',
              BASE/'initial_02/SHA256SUMS',
              ROOT/'docs/papers204_208_sequence/qa/P209_TERMINAL_ARTIFACT_INITIAL_02.failed.actual.json',
              ROOT/'docs/papers204_208_sequence/qa/p209_terminal_artifact_revision_02/SHA256SUMS',
              BASE/'initial_03/SHA256SUMS',
              ROOT/'docs/papers204_208_sequence/qa/P209_TERMINAL_ARTIFACT_INITIAL_03.failed.actual.json']
    before={str(p):info(p) for p in required}
    BASE.mkdir(exist_ok=True)
    target=BASE/sys.argv[1];target.mkdir(exist_ok=False)
    save(target/'executed_auditor_snapshot.py',SOURCE.read_bytes())
    save(target/'executed_recorder_snapshot.py',Path(__file__).read_bytes())
    dump(target/'INPUTS_BEFORE.json',before)
    cache=target/'unused_pycache'
    argv=['/usr/bin/python3.10','-I','-S','-B','-X','pycache_prefix='+str(cache),str(SOURCE),
          'terminal-artifact-after-actual-views']
    attempt={'argv':argv,'cwd':str(ROOT),'environment':ENV,'started_utc':datetime.now(timezone.utc).isoformat(),
             'status':'ATTEMPTED','exit_code':None}
    dump(target/'ATTEMPT.json',attempt)
    failure=None
    try:
        child=subprocess.run(argv,cwd=ROOT,env=ENV,capture_output=True,check=False)
        exit_code,stdout,stderr=child.returncode,child.stdout,child.stderr
    except OSError as exc:
        failure=repr(exc);exit_code=127;stdout=b'';stderr=str(exc).encode()
    save(target/'audit.stdout',stdout);save(target/'audit.stderr',stderr)
    after={str(p):info(p) for p in required};dump(target/'INPUTS_AFTER.json',after)
    row={**attempt,'status':'COMPLETED' if failure is None else 'SPAWN_FAILED','failure':failure,
         'ended_utc':datetime.now(timezone.utc).isoformat(),'exit_code':exit_code,
         'unused_cache_absent':not cache.exists(),'inputs_unchanged':before==after,
         'stdout':info(target/'audit.stdout'),'stderr':info(target/'audit.stderr'),
         'role':'Actual documentary auditor attempt only; no new mathematical/build/view execution.'}
    dump(target/'COMMAND.json',row)
    files=[p for p in sorted(target.rglob('*')) if p.is_file()]
    save(target/'SHA256SUMS',''.join(info(p)['sha256']+'  '+p.relative_to(target).as_posix()+'\n' for p in files).encode())
    print(json.dumps(row,indent=2,sort_keys=True))
    if exit_code: print(stderr.decode(errors='replace'),file=sys.stderr)
    elif before!=after or cache.exists():raise RuntimeError('Recorder inputs/cache changed; attempt retained')
    else:
        result=json.loads(stdout)
        assert result['status']=='PASS_P209_TERMINAL_ARTIFACT_GATE'
        print(json.dumps({k:result[k] for k in ('status','checks','all_consumed_input_count')},sort_keys=True))
    raise SystemExit(exit_code)

if __name__=='__main__':main()
