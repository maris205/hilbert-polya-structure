#!/usr/bin/env python3
"""P208 scoped author producer: exclusive output paths, complete raw evidence.

Usage: python -I -B record_author.py initial LABEL
       python -I -B record_author.py pair LABEL
The initial command creates CANONICAL.json only after a successful producer.
The pair command never changes that canonical. No outside package is written.
"""
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import time

BASE = Path(__file__).resolve().parent
PYTHON = Path(sys.executable).resolve()
CMP = Path('/usr/bin/cmp')
LDD = Path('/usr/bin/ldd')
ENV = {'PATH': '/usr/bin:/bin', 'LANG': 'C.UTF-8', 'LC_ALL': 'C.UTF-8',
       'TZ': 'UTC', 'PYTHONHASHSEED': '0'}
PROBE = r'''
import collections, functools, hashlib, itertools, json, math, os, platform, sys
from pathlib import Path
assert sys.flags.optimize == 0 and sys.flags.isolated == 1
assert sys.dont_write_bytecode
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


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def dump(path, obj):
    with path.open('x', encoding='utf-8') as f:
        json.dump(obj, f, indent=2, sort_keys=True)
        f.write('\n')


def inputs():
    """All currently present author inputs, excluding products and evidence runs."""
    out = {}
    excluded = {'qa_author', 'qa_build', 'frozen_round0', 'frozen_round1',
                'frozen_round2', '__pycache__'}
    for p in sorted(BASE.rglob('*')):
        rel = p.relative_to(BASE)
        if (p.is_file() and not excluded.intersection(rel.parts)
                and p.name not in {'main.pdf', 'AUTHOR_EXECUTION.md',
                                   'BUILD_REPORT.md', 'AUTHOR_HANDOFF.md',
                                   'AUTHOR_MANIFEST.sha256'}):
            out[str(rel)] = digest(p)
    return out


def tool_pins():
    return {str(p): digest(p) for p in (PYTHON, CMP, LDD, Path(__file__).resolve())}


def library_pins(raw):
    # ldd contains ASLR addresses; retain raw output but compare resolved bytes.
    result = {}
    for token in re.findall(r'/[^\s()]+', raw.read_text()):
        p = Path(token).resolve()
        if p.is_file():
            result[str(p)] = digest(p)
    return result


def execute(root, label, argv, cwd):
    start = time.time_ns()
    with (root / (label + '.stdout')).open('xb') as out:
        with (root / (label + '.stderr')).open('xb') as err:
            child = subprocess.run(argv, cwd=cwd, env=ENV, stdout=out, stderr=err,
                                   check=False)
    row = {'label': label, 'argv': [str(a) for a in argv], 'cwd': str(cwd),
           'environment': ENV, 'start_ns': start, 'end_ns': time.time_ns(),
           'exit_code': child.returncode,
           'stdout': label + '.stdout', 'stderr': label + '.stderr',
           'stdout_sha256': digest(root / (label + '.stdout')),
           'stderr_sha256': digest(root / (label + '.stderr'))}
    dump(root / (label + '.command.json'), row)
    return row


def main():
    if len(sys.argv) != 3 or sys.argv[1] not in {'initial', 'pair'}:
        raise SystemExit('usage: record_author.py initial|pair LABEL')
    mode, label = sys.argv[1:]
    if not label or any(c not in 'abcdefghijklmnopqrstuvwxyz0123456789_-' for c in label):
        raise SystemExit('unsafe label')
    assert sys.flags.optimize == 0 and sys.flags.isolated == 1
    assert sys.dont_write_bytecode
    canonical = BASE / 'CANONICAL.json'
    if mode == 'initial' and canonical.exists():
        raise SystemExit('canonical exists; preserve it, use a disclosed new version')
    if mode == 'pair' and not canonical.is_file():
        raise SystemExit('canonical missing')
    parent = BASE / 'qa_author'
    parent.mkdir(exist_ok=True)
    root = parent / label
    root.mkdir()  # exclusive: never reuse or erase a run
    before = inputs()
    dump(root / 'INPUTS_BEFORE.json', before)
    snapshot = root / 'input_snapshot'
    snapshot.mkdir()
    for rel in before:
        dest = snapshot / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(BASE / rel, dest)
        assert digest(dest) == before[rel]
    tools_before = tool_pins()
    dump(root / 'TOOLS_BEFORE.json', tools_before)
    commands, runs = [], []
    expected_producers = 1 if mode == 'initial' else 2
    failure = None
    libraries_before = {}
    try:
        # Pre-execution capture, not a retroactive pre-first-read claim.
        commands.append(execute(root, 'runtime_before', [str(PYTHON), '-I', '-B', '-c', PROBE], root))
        commands.append(execute(root, 'ldd_before', [str(LDD), str(PYTHON)], root))
        libraries_before = library_pins(root / 'ldd_before.stdout')
        dump(root / 'LIBRARIES_BEFORE.json', libraries_before)
        if any(c['exit_code'] != 0 for c in commands):
            raise RuntimeError('pre-producer runtime/dynamic-link probe failed')
        if not libraries_before or 'not found' in (root / 'ldd_before.stdout').read_text():
            raise RuntimeError('empty or unresolved dynamic-library dependency set')
        for number in range(1, 2 if mode == 'initial' else 3):
            run = root / ('source_only_%02d' % number)
            run.mkdir()
            shutil.copyfile(BASE / 'verify.py', run / 'verify.py')
            initial_files = {p.name: digest(p) for p in run.iterdir() if p.is_file()}
            assert initial_files == {'verify.py': before['verify.py']}
            dump(root / ('SOURCE_ONLY_%02d_BEFORE.json' % number), initial_files)
            row = execute(root, 'producer_%02d' % number,
                          [str(PYTHON), '-I', '-B', 'verify.py'], run)
            commands.append(row)
            runs.append({'directory': str(run.relative_to(root)),
                         'initial_files': initial_files,
                         'final_files': {p.name: digest(p) for p in run.iterdir() if p.is_file()},
                         'producer': row})
            if row['exit_code']:
                raise RuntimeError('producer failed; evidence retained')
            assert (root / row['stderr']).stat().st_size == 0
            payload = json.loads((root / row['stdout']).read_bytes())
            assert payload['total_states'] == 2055
            assert len(payload['rows']) == 8
            assert sum(len(r['complete_graph_and_sources']) for r in payload['rows']) == 2055
            assert isinstance(payload['assertions'], int) and payload['assertions'] > 0
            runs[-1]['parsed_assertions'] = payload['assertions']
            runs[-1]['parsed_states'] = payload['total_states']
            assert runs[-1]['initial_files'] == runs[-1]['final_files']
            if mode == 'initial':
                with canonical.open('xb') as f:
                    f.write((root / row['stdout']).read_bytes())
            commands.append(execute(root, 'cmp_canonical_%02d' % number,
                                    [str(CMP), str(canonical), str(root / row['stdout'])], root))
        if mode == 'pair':
            commands.append(execute(root, 'cmp_pair',
                           [str(CMP), str(root / 'producer_01.stdout'),
                            str(root / 'producer_02.stdout')], root))
    except BaseException as error:
        failure = {'type': type(error).__name__, 'message': str(error)}
        raise
    finally:
        commands.append(execute(root, 'runtime_after', [str(PYTHON), '-I', '-B', '-c', PROBE], root))
        commands.append(execute(root, 'ldd_after', [str(LDD), str(PYTHON)], root))
        commands.append(execute(root, 'cmp_runtime',
                       [str(CMP), str(root / 'runtime_before.stdout'),
                        str(root / 'runtime_after.stdout')], root))
        libraries_after = library_pins(root / 'ldd_after.stdout')
        dump(root / 'LIBRARIES_AFTER.json', libraries_after)
        after = inputs()
        dump(root / 'INPUTS_AFTER.json', after)
        expected_after = dict(before)
        if mode == 'initial' and canonical.exists():
            expected_after['CANONICAL.json'] = digest(canonical)
        tools_after = tool_pins()
        dump(root / 'TOOLS_AFTER.json', tools_after)
        record = {'role': 'author_not_independent_review', 'mode': mode,
                  'pre_execution_not_pre_first_read': True,
                  'input_pins_before': before, 'input_pins_after': after,
                  'expected_only_canonical_creation': mode == 'initial',
                  'inputs_unchanged_as_declared': after == expected_after,
                  'tools_unchanged': tools_before == tools_after,
                  'resolved_libraries_unchanged': libraries_before == libraries_after,
                  'dynamic_dependencies_resolved': bool(libraries_after) and
                       'not found' not in (root / 'ldd_after.stdout').read_text(),
                  'expected_producer_count': expected_producers,
                  'actual_producer_count': len(runs),
                  'parsed_assertion_counts': [r.get('parsed_assertions') for r in runs],
                  'all_source_copies_unchanged': all(r['initial_files'] == r['final_files']
                                                    for r in runs),
                  'validation_exception': failure,
                  'commands': commands, 'runs': runs,
                  'all_child_exits_zero': all(c['exit_code'] == 0 for c in commands),
                  'canonical_sha256': digest(canonical) if canonical.exists() else None,
                  'runtime_limit': 'Actual probe module pins and dynamic-library resolver output; '
                                   'not a hermetic historical OS or library reconstruction.'}
        record['status'] = 'AUTHOR_EXECUTION_PASS' if (
            failure is None and record['all_child_exits_zero'] and
            record['inputs_unchanged_as_declared'] and record['tools_unchanged'] and
            record['resolved_libraries_unchanged'] and record['dynamic_dependencies_resolved'] and
            record['all_source_copies_unchanged'] and len(runs) == expected_producers and
            all(isinstance(v, int) and v > 0 for v in record['parsed_assertion_counts'])
        ) else 'AUTHOR_EXECUTION_FAILED'
        dump(root / 'RECEIPT.json', record)
    assert record['status'] == 'AUTHOR_EXECUTION_PASS'
    assert record['all_child_exits_zero']
    assert record['inputs_unchanged_as_declared'] and record['tools_unchanged']
    assert record['resolved_libraries_unchanged']
    assert all(r['initial_files'] == r['final_files'] for r in runs)
    print(json.dumps({'receipt': str(root / 'RECEIPT.json'),
                      'mode': mode, 'status': 'AUTHOR_EXECUTION_PASS',
                      'canonical_sha256': record['canonical_sha256']}, indent=2))


if __name__ == '__main__':
    main()
