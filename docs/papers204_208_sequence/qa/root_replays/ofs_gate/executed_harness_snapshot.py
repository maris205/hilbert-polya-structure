#!/usr/bin/env python3
"""Root-only scoped OFS gate pair; sealed gate and old recorders stay unchanged."""
from datetime import datetime, timezone
from hashlib import sha256
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import traceback

ROOT = Path(__file__).resolve().parents[3]
GATE = ROOT/'docs/papers204_208_sequence/scouting/OFS_GATE'
OUT = ROOT/'docs/papers204_208_sequence/qa/root_replays/ofs_gate'

def info(p):
    raw = p.read_bytes()
    return {'bytes':len(raw), 'sha256':sha256(raw).hexdigest()}

def capture():
    result = {}
    manifest = GATE/'SHA256SUMS'
    rows = [line.split('  ', 1) for line in manifest.read_text().splitlines()]
    assert len(rows) == 87 and len({name for digest, name in rows}) == 87
    assert {name for digest, name in rows} == {str(p.relative_to(GATE)) for p in GATE.rglob('*') if p.is_file() and p != manifest}
    for digest, name in rows:
        p = GATE/name
        assert not p.is_symlink() and not Path(name).is_absolute() and '..' not in Path(name).parts
        value = info(p)
        assert value['sha256'] == digest, name
        result[str(p.relative_to(ROOT))] = value
    result[str(manifest.relative_to(ROOT))] = info(manifest)
    counts = []
    for name in ['INPUT_PINS.sha256', 'HISTORY_PINS.sha256']:
        rows = [line.split('  ',1) for line in (GATE/name).read_text().splitlines()]
        counts.append(len(rows))
        for digest, relative in rows:
            p = ROOT/relative
            assert not p.is_symlink() and not Path(relative).is_absolute() and '..' not in Path(relative).parts
            value = info(p)
            assert value['sha256'] == digest, relative
            assert relative not in result or result[relative] == value
            result[relative] = value
    assert counts == [135,14]
    return result

def save(p, raw):
    with p.open('xb') as stream:
        stream.write(raw)

def main():
    OUT.mkdir(parents=True, exist_ok=False)
    start = datetime.now(timezone.utc).isoformat()
    executable = Path(sys.executable).resolve()
    environment = {'PATH':str(executable.parent)+':/usr/bin:/bin','LC_ALL':'C','LANG':'C','TZ':'UTC',
                   'PYTHONDONTWRITEBYTECODE':'1','SOURCE_DATE_EPOCH':'1788652800'}
    commands, runs = [], []
    before, after, failure = {}, {}, None
    inputs_before = {'python':info(executable),'harness':info(Path(__file__).resolve())}
    save(OUT/'executed_harness_snapshot.py',Path(__file__).read_bytes())
    def execute(command, cwd, label):
        child = subprocess.run(command,cwd=cwd,env=environment,capture_output=True)
        save(OUT/(label+'.stdout'),child.stdout)
        save(OUT/(label+'.stderr'),child.stderr)
        commands.append({'command':command,'cwd':str(cwd),'exit':child.returncode,
                         'stdout':{'path':label+'.stdout',**info(OUT/(label+'.stdout'))},
                         'stderr':{'path':label+'.stderr',**info(OUT/(label+'.stderr'))}})
        assert child.returncode == 0, label
        return child
    probe = "import collections,functools,itertools,math,hashlib,json,sys,pathlib; print(json.dumps({'flags':repr(sys.flags),'optimize':sys.flags.optimize,'debug':__debug__,'isolated':sys.flags.isolated,'version':sys.version,'loaded_files':{k:{'path':str(pathlib.Path(m.__file__).resolve()),'sha256':hashlib.sha256(pathlib.Path(m.__file__).read_bytes()).hexdigest()} for k,m in sorted(sys.modules.items()) if getattr(m,'__file__',None) and pathlib.Path(m.__file__).is_file()}},sort_keys=True)); assert __debug__ and sys.flags.optimize==0 and sys.flags.isolated==1"
    try:
        before = capture()
        save(OUT/'INPUTS_BEFORE.json',(json.dumps(before,sort_keys=True,indent=2)+'\n').encode())
        execute([str(executable),'-I','-B','-c',probe],OUT,'runtime_before')
        execute(['/usr/bin/ldd',str(executable)],OUT,'linked_libraries')
        for label in ['run1','run2']:
            folder = OUT/label
            folder.mkdir()
            shutil.copy2(GATE/'verify.py',folder/'verify.py')
            assert list(folder.iterdir()) == [folder/'verify.py']
            assert info(folder/'verify.py') == info(GATE/'verify.py')
            child = execute([str(executable),'-I','-B','verify.py'],folder,label)
            data = json.loads(child.stdout)
            assert data['total_assertions'] == 628980
            assert [row['n'] for row in data['rows']] == list(range(3,11))
            assert sum(row['states'] for row in data['rows']) == 2055
            assert sum(len(row['states']) for row in data['full_graph_and_source_sets']) == 2055
            assert not child.stderr
            assert info(folder/'verify.py') == info(GATE/'verify.py')
            execute(['/usr/bin/cmp',str(OUT/(label+'.stdout')),str(GATE/'CANONICAL.json')],OUT,label+'_canonical_cmp')
            runs.append({'label':label,'assertions':628980,'states':2055,'initial_files':['verify.py'],
                         'code':info(folder/'verify.py'),'empty_stderr':True})
        execute(['/usr/bin/cmp',str(OUT/'run1.stdout'),str(OUT/'run2.stdout')],OUT,'pair_cmp')
        execute([str(executable),'-I','-B','-c',probe],OUT,'runtime_after')
        execute(['/usr/bin/cmp',str(OUT/'runtime_before.stdout'),str(OUT/'runtime_after.stdout')],OUT,'runtime_cmp')
        after = capture()
        assert before == after
    except BaseException as error:
        failure = {'type':type(error).__name__,'message':str(error)}
        save(OUT/'exception.txt',traceback.format_exc().encode())
    inputs_after = {'python':info(executable),'harness':info(Path(__file__).resolve())}
    passed = failure is None and before == after and inputs_before == inputs_after and len(runs) == 2
    receipt = {'status':'PASS_ROOT_OFS_GATE_REPLAY_PAIR' if passed else 'FAIL','failure':failure,
               'started_utc':start,'ended_utc':datetime.now(timezone.utc).isoformat(),
               'kind':'ROOT_REPRODUCTION_OF_NONAUTHOR_CANDIDATE_EVIDENCE_NOT_ANOTHER_REVIEW',
               'chronology':'Root first read author/gate proof before this capture; this is a fresh pre-execution capture, not a retroactive pre-first-read pin.',
               'environment':environment,'execution_inputs_before':inputs_before,'execution_inputs_after':inputs_after,
               'referents_before':before,'referents_after':after,'referents_stable':before==after,
               'commands':commands,'runs':runs,'canonical':info(GATE/'CANONICAL.json'),
               'runtime_limit':'Actual flags, interpreter, loaded probe files and ldd recorded; not a hermetic historical library reconstruction.',
               'external':'HOLD_EXTERNAL'}
    save(OUT/'RECEIPT.json',(json.dumps(receipt,sort_keys=True,indent=2)+'\n').encode())
    print(json.dumps({'status':receipt['status'],'runs':runs,'referents':len(before),'commands':len(commands),'failure':failure},indent=2))
    raise SystemExit(0 if passed else 1)

if __name__ == '__main__':
    main()
