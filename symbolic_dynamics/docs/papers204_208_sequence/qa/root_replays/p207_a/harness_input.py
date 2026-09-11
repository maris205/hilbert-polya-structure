#!/usr/bin/env python3
"""Root's new cold replay pair of a closed P207 review, without review writes.

Scoped schema adapter for SHA256SUMS + workspace-relative INPUT_PINS.sha256.
This is root reproduction of nonauthor evidence, not another independent
review. The original review recorder and all prior generic tools stay intact.
"""
from datetime import datetime, timezone
from hashlib import sha256
import json
import os
from pathlib import Path
import platform
import subprocess
import sys


SETTINGS = {'LC_ALL':'C','TZ':'UTC','PYTHONHASHSEED':'0',
            'PYTHONDONTWRITEBYTECODE':'1','PYTHONSAFEPATH':'1'}


def info(path):
    raw = path.read_bytes()
    return {'sha256':sha256(raw).hexdigest(),'bytes':len(raw)}


def snapshot(folder):
    return {str(p.relative_to(folder)):info(p) for p in sorted(folder.rglob('*'))
            if p.is_file() and '__pycache__' not in p.parts}


def main():
    if len(sys.argv) != 3:
        raise SystemExit('expected REVIEW_PACKAGE NEW_OUTPUT_DIRECTORY')
    workspace = Path(__file__).resolve().parents[3]
    package, out = map(lambda p:Path(p).resolve(),sys.argv[1:])
    if package.name not in ('p207_a','p207_b'):
        raise SystemExit('adapter scoped to P207 A/B')
    for name in ('SHA256SUMS','INPUT_PINS.sha256','verify.py','CANONICAL.json'):
        if not (package/name).is_file():
            raise SystemExit('closed package role missing: '+name)
    if package == out or package in out.parents:
        raise SystemExit('root replay cannot write inside the review')
    out.mkdir(parents=True,exist_ok=False)
    before = snapshot(package)
    env = dict(os.environ)
    env.pop('PYTHONPATH',None)
    env.pop('PYTHONHOME',None)
    env.update(SETTINGS)
    commands = []

    def execute(command,cwd,stem):
        child = subprocess.run(command,cwd=cwd,env=env,capture_output=True)
        for suffix,raw in (('stdout',child.stdout),('stderr',child.stderr)):
            with (out/(stem+'.'+suffix)).open('xb') as stream:
                stream.write(raw)
        row = {'command':command,'cwd':str(cwd),'exit':child.returncode,
               'stdout':info(out/(stem+'.stdout')),'stderr':info(out/(stem+'.stderr'))}
        commands.append(row)
        return child

    for name,cwd in (('SHA256SUMS',package),('INPUT_PINS.sha256',workspace)):
        execute(['sha256sum','-c',str(package/name)],cwd,name)
    executable = str(Path(sys.executable).resolve())
    execute([executable,'--version'],out,'python_version')
    execute(['ldd',executable],out,'python_link_dependencies')
    for name in ('verify.py','CANONICAL.json'):
        with (out/name).open('xb') as stream:
            stream.write((package/name).read_bytes())
    runs = []
    if all(row['exit'] == 0 for row in commands):
        for label in ('run1','run2'):
            child = execute([executable,'-B',str(out/'verify.py')],out,label)
            parsed = json.loads(child.stdout) if child.returncode == 0 else {}
            execute(['cmp',str(out/'CANONICAL.json'),str(out/(label+'.stdout'))],out,label+'.cmp')
            runs.append({'label':label,'assertions':parsed.get('assertions'),
                         'producer_status':parsed.get('status'),
                         'empty_stderr':not child.stderr})
        execute(['cmp',str(out/'run1.stdout'),str(out/'run2.stdout')],out,'pair.cmp')
    after = snapshot(package)
    passed = (before == after and len(runs) == 2 and
              all(row['exit'] == 0 for row in commands) and
              all(row['assertions'] and row['producer_status'] == 'PASS' and
                  row['empty_stderr'] for row in runs))
    receipt = {'kind':'ACTUAL_ROOT_COLD_REPLAY_OF_NONAUTHOR_REVIEW_NOT_ADDITIONAL_REVIEW',
               'utc':datetime.now(timezone.utc).isoformat(),'review':str(package),
               'harness':info(Path(__file__)),'environment':SETTINGS,
               'python':{'executable':executable,'file':info(Path(executable)),
                         'version':sys.version,'platform':platform.platform()},
               'before_package_files':before,'after_package_files':after,
               'package_unchanged':before == after,'commands':commands,'runs':runs,
               'pass':passed}
    with (out/'RECEIPT.json').open('x') as stream:
        json.dump(receipt,stream,sort_keys=True,indent=2)
        stream.write('\n')
    print(json.dumps({'pass':passed,'runs':runs,'receipt':str(out/'RECEIPT.json')},indent=2))
    raise SystemExit(0 if passed else 1)


if __name__ == '__main__':
    main()
