#!/usr/bin/env python3
"""Fresh root reproduction of P208's sealed author evidence, not a review.

The older P207 and OFS recorders remain unchanged. This scoped recorder
consumes P208's explicit author seal and starts two separate code-only dirs.
"""
from datetime import datetime, timezone
from hashlib import sha256
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys
import traceback

ROOT = Path(__file__).resolve().parents[3]
PAPER = ROOT / 'papers/208-original-snapshot-triangulation-sweeps'
OUT = ROOT / 'docs/papers204_208_sequence/qa/root_replays/p208_author'
PYTHON = Path(sys.executable).resolve()
TOOLS = [PYTHON, Path('/usr/bin/cmp'), Path('/usr/bin/ldd'), Path(__file__).resolve()]
ENV = {'PATH': '/usr/bin:/bin', 'LANG': 'C.UTF-8', 'LC_ALL': 'C.UTF-8',
       'TZ': 'UTC', 'PYTHONHASHSEED': '0'}
PROBE = r'''
import collections, functools, hashlib, itertools, json, math, os, platform, sys
from pathlib import Path
assert sys.flags.optimize == 0 and sys.flags.isolated == 1 and sys.dont_write_bytecode
files = {}
for name, module in sorted(sys.modules.items()):
    origin = getattr(module, '__file__', None)
    if origin and Path(origin).is_file():
        p = Path(origin).resolve()
        files[name] = {'path': str(p), 'sha256': hashlib.sha256(p.read_bytes()).hexdigest()}
print(json.dumps({'version': sys.version, 'executable': str(Path(sys.executable).resolve()),
    'flags': repr(sys.flags), 'optimize': sys.flags.optimize, 'isolated': sys.flags.isolated,
    'dont_write_bytecode': sys.dont_write_bytecode, 'platform': platform.platform(),
    'environment': dict(sorted(os.environ.items())), 'module_files': files},
    sort_keys=True, indent=2))
'''


def info(path):
    raw = path.read_bytes()
    return {'bytes': len(raw), 'sha256': sha256(raw).hexdigest()}


def save(path, raw):
    with path.open('xb') as stream:
        stream.write(raw)


def dump(path, value):
    save(path, (json.dumps(value, sort_keys=True, indent=2) + '\n').encode())


def capture():
    manifest = PAPER / 'AUTHOR_MANIFEST.sha256'
    result = {}
    for line in manifest.read_text().splitlines():
        digest, name = line.split('  ', 1)
        rel = Path(name)
        assert not rel.is_absolute() and '..' not in rel.parts and rel.parts
        key = rel.as_posix()
        assert key not in result and key != manifest.name
        path = PAPER / rel
        assert path.is_file() and not path.is_symlink()
        value = info(path)
        assert value['sha256'] == digest, key
        result[key] = value
    for name in ['verify.py', 'CANONICAL.json', 'record_author.py', 'AUTHOR_EXECUTION.md',
                 'main.tex', 'math_commands.tex', 'references.bib', 'PROOF_PACKAGE.md',
                 'SOURCE_AUDIT.md', 'VERIFICATION_SCOPE.md']:
        assert name in result, name
    result[manifest.name] = info(manifest)
    origins = (PAPER / 'provenance/INPUT_ORIGINS.sha256').read_text().splitlines()
    assert len(origins) == 7
    for line in origins:
        digest, name = line.split('  ', 1)
        rel = Path(name)
        assert not rel.is_absolute() and '..' not in rel.parts and rel.parts
        path = ROOT / rel
        assert path.is_file() and not path.is_symlink()
        value = info(path)
        assert value['sha256'] == digest, name
        key = 'workspace_origin:' + rel.as_posix()
        assert key not in result
        result[key] = value
    return result


def libraries(path):
    raw = path.read_text()
    assert 'not found' not in raw
    result = {}
    for name in re.findall(r'/[^\s()]+', raw):
        p = Path(name).resolve()
        if p.is_file():
            result[str(p)] = info(p)
    assert result, 'no resolved dynamic libraries'
    return result


def main():
    assert sys.flags.optimize == 0 and sys.flags.isolated == 1 and sys.dont_write_bytecode
    OUT.mkdir(parents=True, exist_ok=False)
    save(OUT / 'executed_harness_snapshot.py', Path(__file__).read_bytes())
    start = datetime.now(timezone.utc).isoformat()
    commands, runs, failures = [], [], []
    before, after, tools_before, tools_after, libs_before, libs_after = {}, {}, {}, {}, {}, {}

    def execute(label, argv, cwd):
        began = datetime.now(timezone.utc).isoformat()
        child = subprocess.run(argv, cwd=cwd, env=ENV, capture_output=True, check=False)
        save(OUT / (label + '.stdout'), child.stdout)
        save(OUT / (label + '.stderr'), child.stderr)
        row = {'label': label, 'argv': argv, 'cwd': str(cwd), 'environment': ENV,
               'started_utc': began, 'ended_utc': datetime.now(timezone.utc).isoformat(),
               'exit_code': child.returncode,
               'stdout': {'path': label + '.stdout', **info(OUT / (label + '.stdout'))},
               'stderr': {'path': label + '.stderr', **info(OUT / (label + '.stderr'))}}
        commands.append(row)
        dump(OUT / (label + '.command.json'), row)
        assert child.returncode == 0, (label, child.returncode)
        return child

    def record_failure(phase, error):
        failures.append({'phase': phase, 'type': type(error).__name__, 'message': str(error)})
        save(OUT / (phase + '_exception.txt'), traceback.format_exc().encode())

    try:
        before = capture()
        dump(OUT / 'INPUTS_BEFORE.json', before)
        tools_before = {str(p): info(p) for p in TOOLS}
        dump(OUT / 'TOOLS_BEFORE.json', tools_before)
        execute('runtime_before', [str(PYTHON), '-I', '-B', '-c', PROBE], OUT)
        execute('ldd_before', ['/usr/bin/ldd', str(PYTHON)], OUT)
        libs_before = libraries(OUT / 'ldd_before.stdout')
        dump(OUT / 'LIBRARIES_BEFORE.json', libs_before)
        for label in ['run1', 'run2']:
            folder = OUT / label
            folder.mkdir()
            shutil.copyfile(PAPER / 'verify.py', folder / 'verify.py')
            initial = {p.name: info(p) for p in folder.iterdir()}
            assert initial == {'verify.py': before['verify.py']}
            child = execute(label, [str(PYTHON), '-I', '-B', 'verify.py'], folder)
            assert not child.stderr
            data = json.loads(child.stdout)
            assert data['total_states'] == data['total_decoded_predecessors'] == 2055
            assert [r['n'] for r in data['rows']] == list(range(3, 11))
            assert sum(r['states'] for r in data['rows']) == 2055
            assert sum(len(r['complete_graph_and_sources']) for r in data['rows']) == 2055
            assert isinstance(data['assertions'], int) and data['assertions'] > 0
            final = {p.name: info(p) for p in folder.iterdir()}
            assert initial == final
            execute(label + '_canonical_cmp', ['/usr/bin/cmp', str(PAPER / 'CANONICAL.json'),
                                                str(OUT / (label + '.stdout'))], OUT)
            runs.append({'label': label, 'initial_files': initial, 'final_files': final,
                         'assertions': data['assertions'], 'states': data['total_states'],
                         'empty_stderr': True})
        execute('pair_cmp', ['/usr/bin/cmp', str(OUT / 'run1.stdout'), str(OUT / 'run2.stdout')], OUT)
    except BaseException as error:
        record_failure('producer_phase', error)
    try:
        execute('runtime_after', [str(PYTHON), '-I', '-B', '-c', PROBE], OUT)
        execute('ldd_after', ['/usr/bin/ldd', str(PYTHON)], OUT)
        libs_after = libraries(OUT / 'ldd_after.stdout')
        dump(OUT / 'LIBRARIES_AFTER.json', libs_after)
        execute('runtime_cmp', ['/usr/bin/cmp', str(OUT / 'runtime_before.stdout'),
                               str(OUT / 'runtime_after.stdout')], OUT)
        after = capture()
        dump(OUT / 'INPUTS_AFTER.json', after)
        tools_after = {str(p): info(p) for p in TOOLS}
        dump(OUT / 'TOOLS_AFTER.json', tools_after)
        assert before == after and before
        assert tools_before == tools_after and tools_before
        assert libs_before == libs_after and libs_before
    except BaseException as error:
        record_failure('closure_phase', error)
    passed = (not failures and len(runs) == 2 and len(commands) == 10
              and all(c['exit_code'] == 0 for c in commands)
              and before == after and tools_before == tools_after and libs_before == libs_after)
    receipt = {'status': 'PASS_ROOT_P208_AUTHOR_REPLAY_PAIR' if passed else 'FAIL',
               'kind': 'ROOT_REPRODUCTION_OF_AUTHOR_EVIDENCE_NOT_AN_INDEPENDENT_REVIEW',
               'chronology': 'Actual capture before these executions, after root read the author manuscript and verifier.',
               'started_utc': start, 'ended_utc': datetime.now(timezone.utc).isoformat(),
               'environment': ENV, 'inputs_before': before, 'inputs_after': after,
               'tools_before': tools_before, 'tools_after': tools_after,
               'libraries_before': libs_before, 'libraries_after': libs_after,
               'commands': commands, 'runs': runs, 'failures': failures,
               'runtime_limit': 'Actual same-import module probes and resolved interpreter libraries; not a hermetic historical OS reconstruction.',
               'external': 'HOLD_EXTERNAL'}
    dump(OUT / 'RECEIPT.json', receipt)
    seal = ''.join(f"{info(p)['sha256']}  {p.relative_to(OUT).as_posix()}\n"
                   for p in sorted(OUT.rglob('*')) if p.is_file())
    save(OUT / 'SHA256SUMS', seal.encode())
    print(json.dumps({'status': receipt['status'], 'commands': len(commands), 'runs': runs,
                      'input_count': len(before), 'failures': failures}, indent=2))
    raise SystemExit(0 if passed else 1)


if __name__ == '__main__':
    main()
