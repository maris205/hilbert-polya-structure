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
import traceback


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
    expected_package = workspace/'docs/papers204_208_sequence/reviews'/package.name
    allowed_outputs = workspace/'docs/papers204_208_sequence/qa/root_replays'
    if package != expected_package or allowed_outputs not in out.parents:
        raise SystemExit('only exact P207 review packages and root replay descendants are allowed')
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

    executable = str(Path(sys.executable).resolve())
    runs = []
    failure = None
    structural = {}
    context_name = ('CONTEXT_SOURCE_PINS.sha256' if package.name == 'p207_a'
                    else 'CONTEXT_PINS.sha256')
    pin_names = ['INPUT_PINS.sha256', context_name]
    try:
        listed = []
        for line in (package/'SHA256SUMS').read_text().splitlines():
            digest,relative = line.split('  ',1)
            path = Path(relative)
            if len(digest) != 64 or path.is_absolute() or '..' in path.parts:
                raise ValueError('invalid directory-relative package manifest entry')
            listed.append(relative)
        actual = set(before)-{'SHA256SUMS'}
        if len(listed) != len(set(listed)) or set(listed) != actual:
            raise ValueError('incomplete or duplicated nonself package manifest')
        freeze = workspace/'papers/207-upper-neighbor-rank-dynamics'/(
            'frozen_round0' if package.name == 'p207_a' else 'frozen_round1')
        expected_freeze_names = {str(p.relative_to(workspace)) for p in freeze.rglob('*') if p.is_file()}
        pinned = [line.split('  ',1)[1] for line in (package/'INPUT_PINS.sha256').read_text().splitlines()]
        if len(pinned) != len(set(pinned)) or set(pinned) != expected_freeze_names or not expected_freeze_names:
            raise ValueError('review input pins do not cover exactly the expected physical freeze')
        structural = {'complete_nonself_package_entries':len(listed),'exact_freeze_inputs':len(pinned)}
        execute(['sha256sum','-c',str(package/'SHA256SUMS')],package,'SHA256SUMS.before')
        for name in pin_names:
            execute(['sha256sum','-c',str(package/name)],workspace,name+'.before')
        execute([executable,'-I','-B','--version'],out,'python_version')
        probe = 'import json,sys; print(json.dumps({"optimize":sys.flags.optimize,"debug":__debug__,"isolated":sys.flags.isolated,"no_user_site":sys.flags.no_user_site,"ignore_environment":sys.flags.ignore_environment},sort_keys=True))'
        flags = execute([executable,'-I','-B','-c',probe],out,'python_runtime_flags')
        if json.loads(flags.stdout) != {'optimize':0,'debug':True,'isolated':1,'no_user_site':1,'ignore_environment':1}:
            raise RuntimeError('isolated runtime flags do not preserve assertions')
        execute(['ldd',executable],out,'python_link_dependencies')
        if any(row['exit'] for row in commands):
            raise RuntimeError('a pre-run pin or runtime command failed')
        for name in ('verify.py','CANONICAL.json'):
            with (out/name).open('xb') as stream:
                stream.write((package/name).read_bytes())
        with (out/'harness_input.py').open('xb') as stream:
            stream.write(Path(__file__).read_bytes())
        for label in ('run1','run2'):
            child = execute([executable,'-I','-B',str(out/'verify.py')],out,label)
            parsed = json.loads(child.stdout) if child.returncode == 0 else {}
            execute(['cmp',str(out/'CANONICAL.json'),str(out/(label+'.stdout'))],out,label+'.cmp')
            runs.append({'label':label,'assertions':parsed.get('assertions'),
                         'producer_status':parsed.get('status'),
                         'empty_stderr':not child.stderr})
        execute(['cmp',str(out/'run1.stdout'),str(out/'run2.stdout')],out,'pair.cmp')
        for name in pin_names:
            execute(['sha256sum','-c',str(package/name)],workspace,name+'.after')
        execute(['sha256sum','-c',str(package/'SHA256SUMS')],package,'SHA256SUMS.after')
    except BaseException as error:
        failure = {'type':type(error).__name__,'message':str(error)}
        with (out/'exception.txt').open('x') as stream:
            stream.write(traceback.format_exc())
    try:
        after = snapshot(package)
    except BaseException as error:
        after = {}
        failure = {'type':type(error).__name__,'message':str(error)}
    passed = (not failure and before == after and len(runs) == 2 and
              all(row['exit'] == 0 for row in commands) and
              all(type(row['assertions']) is int and row['assertions'] > 0 and row['producer_status'] == 'PASS' and
                  row['empty_stderr'] for row in runs))
    receipt = {'kind':'ACTUAL_ROOT_COLD_REPLAY_OF_NONAUTHOR_REVIEW_NOT_ADDITIONAL_REVIEW',
               'utc':datetime.now(timezone.utc).isoformat(),'review':str(package),
               'harness':info(Path(__file__)),'environment_overrides':SETTINGS,
               'python_flags':['-I','-B'],'failure':failure,'structural_checks':structural,
               'role_limit':'replay and dependency integrity only, not manuscript delta or terminal acceptance',
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
