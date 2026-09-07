"""Final documentary closure and own nonself seal, no target execution."""
import ast
from datetime import datetime, timezone
from hashlib import sha256
import json
import os
from pathlib import Path
import sys

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
BASE = ROOT / 'docs/papers204_208_sequence/qa/p209_terminal_artifact_revision_01'
ENV = {'PATH': '/usr/bin:/bin', 'LANG': 'C.UTF-8', 'LC_ALL': 'C.UTF-8', 'TZ': 'UTC'}


def info(p):
    p = Path(p); raw = p.read_bytes()
    return {'sha256': sha256(raw).hexdigest(), 'bytes': len(raw), 'resolved': str(p.resolve()),
            'symlink': os.readlink(p) if p.is_symlink() else None}


def j(p):
    return json.loads(Path(p).read_bytes())


def save(p, raw):
    with p.open('xb') as stream:
        stream.write(raw)


def main():
    assert sys.argv[1:] == ['seal'] and not (BASE / 'SHA256SUMS').exists()
    static = j(BASE / 'STATIC_RESULT.json')
    assert static['status'] == 'PASS_STATIC_REVISION_SOURCE_AND_ORIGINAL_CLOSURE_NOT_EXECUTED'
    receipt = j(BASE / 'checks/static_01/RECEIPT.json')
    assert receipt['exit_code'] == 0 and receipt['inputs_unchanged'] is True
    assert (BASE / 'checks/static_01/stderr').read_bytes() == b''
    for stream in ('stdout', 'stderr'):
        got = info(BASE / 'checks/static_01' / stream)
        assert {k: got[k] for k in ('sha256', 'bytes')} == receipt[stream]
    before = j(BASE / 'checks/static_01/INPUTS_BEFORE.json')
    assert before == j(BASE / 'checks/static_01/INPUTS_AFTER.json')
    for path, pin in before.items():
        got = info(path)
        assert {k: got[k] for k in ('sha256', 'bytes')} == pin
    inputs = j(BASE / 'IMMUTABLE_PACKAGE_INPUTS.json')
    assert len(inputs) == 2033 and inputs == {p: info(p) for p in inputs}
    for source, pin in j(BASE / 'ORIGINAL_INPUTS.json').items():
        got = info(pin['physical'])
        assert got['sha256'] == pin['sha256'] and got['bytes'] == pin['bytes'] and got['symlink'] is None
    for name, pins in static['source_changes'].items():
        assert info(BASE / name) == pins['new']
    diffs = j(BASE / 'DIFF_COMMANDS.json')
    assert len(diffs) == 3 and all(r['exit_code'] == 1 and r['stderr'] == '' for r in diffs)
    assert (BASE / 'ADAPTATION.diff').read_text() == ''.join(r['stdout'] for r in diffs)
    for row in diffs:
        for p, pin in row['inputs_before'].items():
            assert info(p) == pin
        assert row['inputs_before'] == row['inputs_after']
        name = Path(row['argv'][-1]).name
        assert (BASE / 'diffs' / (name + '.diff')).read_text() == row['stdout']
    docs = (BASE / 'README.md').read_text()
    assert all(pins['new']['sha256'] in docs for pins in static['source_changes'].values())
    assert '389' in docs and '2,033' in docs and '26 Python' in docs
    assert 'Round1' in docs and 'reaffirmed' in docs and 'Round2' in docs and 'newly registered' in docs
    initial = ROOT / 'docs/papers204_208_sequence/qa/p209_terminal_artifact'
    assert not (initial / 'initial_02').exists() and not (initial / 'lifecycle_before').exists()
    assert j(initial / 'initial_01/COMMAND.json')['exit_code'] == 1
    files = sorted(p for p in BASE.rglob('*') if p.is_file())
    all_before = {str(p): info(p) for p in files}
    parsed = []
    for p in files:
        assert not p.is_symlink() and '__pycache__' not in p.parts and p.suffix not in ('.pyc', '.pyo')
        if p.suffix == '.py':
            code = p.read_text(); compile(ast.parse(code, filename=str(p)), str(p), 'exec', optimize=0)
            parsed.append(str(p.relative_to(BASE)))
        elif p.suffix == '.json':
            j(p)
    assert all_before == {str(p): info(p) for p in files}
    summary = {'status': 'PASS_FINAL_DOCUMENTARY_CLOSURE_NOT_TARGET_EXECUTION',
        'utc': datetime.now(timezone.utc).isoformat(), 'source_changes': static['source_changes'],
        'all_python_sources_final_parsed_without_execution': parsed,
        'original_copies': 389, 'actual_cmp_commands': 389, 'immutable_paths_rechecked': 2033,
        'full_raw_diffs_verified': 3, 'actual_static_child_exit': 0,
        'initial_01_child_exit_still': 1, 'initial_02_exists': False,
        'auditor_lifecycle_guard_science_build_view_executions': 0,
        'full_current_package_inputs_before': all_before,
        'full_current_package_inputs_after': {str(p): info(p) for p in files}}
    save(BASE / 'FINAL_DOCUMENT_CHECK.json', (json.dumps(summary, sort_keys=True, indent=2) + '\n').encode())
    all_files = sorted(p for p in BASE.rglob('*') if p.is_file())
    pins = {p.relative_to(BASE).as_posix(): info(p) for p in all_files}
    save(BASE / 'SHA256SUMS', ''.join(v['sha256'] + '  ' + n + '\n' for n, v in pins.items()).encode())
    assert set(p.relative_to(BASE).as_posix() for p in BASE.rglob('*') if p.is_file()) == set(pins) | {'SHA256SUMS'}
    assert pins == {n: info(BASE / n) for n in pins}
    print(json.dumps({'status': 'SEALED_REVISION_01_PREPARATION_NOT_TARGET_EXECUTION',
        'payloads': len(pins), 'total_files': len(pins) + 1, 'manifest': info(BASE / 'SHA256SUMS'),
        'python_sources_final_parsed_not_executed': len(parsed), 'static_child_exit': 0,
        'immutable_paths_rechecked': 2033, 'initial_01_still_failure': True, 'initial_02_created': False,
        'auditor_lifecycle_guard_science_build_view_executions': 0}, sort_keys=True, indent=2))


if __name__ == '__main__':
    assert sys.flags.isolated and sys.flags.no_site and sys.dont_write_bytecode and not sys.flags.optimize
    assert dict(os.environ) == ENV and Path.cwd() == ROOT
    main()
