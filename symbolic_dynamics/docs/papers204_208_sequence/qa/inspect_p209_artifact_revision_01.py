"""Root read-only original/static preflight; never imports target infrastructure."""
import ast
from datetime import datetime, timezone
from hashlib import sha256
import json
import os
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
BATCH = ROOT / 'docs/papers204_208_sequence'
BASE = BATCH / 'qa/p209_terminal_artifact_revision_01'
OLD = BATCH / 'qa/p209_terminal_artifact_preparation'
FAILED = BATCH / 'qa/p209_terminal_artifact/initial_01'
ENV = {'PATH': '/usr/bin:/bin', 'LANG': 'C.UTF-8', 'LC_ALL': 'C.UTF-8', 'TZ': 'UTC'}
WATCH = {}


def info(p):
    p = Path(p)
    raw = p.read_bytes()
    return {'sha256': sha256(raw).hexdigest(), 'bytes': len(raw),
            'resolved': str(p.resolve()), 'symlink': os.readlink(p) if p.is_symlink() else None}


def read(p):
    p = Path(p); got = info(p)
    if str(p) in WATCH:
        assert WATCH[str(p)] == got, str(p)
    WATCH[str(p)] = got
    return p.read_bytes()


def j(p):
    return json.loads(read(p))


def pin(p, value):
    read(p); got = WATCH[str(p)]
    expected = {'sha256': value} if isinstance(value, str) else value
    assert all(got[k] == v for k, v in expected.items()), (str(p), expected, got)


def manifest(base, count, digest):
    pin(base / 'SHA256SUMS', digest)
    rows = {}
    for line in read(base / 'SHA256SUMS').decode().splitlines():
        match = re.fullmatch(r'([0-9a-f]{64})  (.+)', line)
        assert match
        value, rel = match.groups(); path = Path(rel)
        assert not path.is_absolute() and '..' not in path.parts and rel not in rows
        assert rel != 'SHA256SUMS'
        rows[rel] = value; pin(base / rel, value)
    files = set()
    for path in base.rglob('*'):
        assert not path.is_symlink()
        if path.is_file():
            files.add(path.relative_to(base).as_posix())
    assert len(rows) == count and files == set(rows) | {'SHA256SUMS'}
    return rows


def check_map(values):
    for path, value in values.items():
        pin(Path(path), value)


def funcs(raw):
    return {n.name: ast.get_source_segment(raw, n) for n in ast.parse(raw).body
            if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))}


def main():
    began = datetime.now(timezone.utc).isoformat()
    pin(Path(__file__), info(Path(__file__)))
    pin(Path(sys.executable), info(Path(sys.executable)))
    manifest(BASE, 418, '855aba017f5a369c09696272579897324bbd906892b353d17f0c9eb6d7fcbcc5')
    immutable = j(BASE / 'IMMUTABLE_PACKAGE_INPUTS.json')
    assert len(immutable) == 2033; check_map(immutable)
    originals = j(BASE / 'ORIGINAL_INPUTS.json'); assert len(originals) == 389
    controls = {str(ROOT / 'SYMBOLIC_DYNAMICS_STATE.md'), str(BATCH / 'PIPELINE_STATE.md'), str(BATCH / 'GIT_SYNC_RECEIPT.md')}
    control_drift = {}
    for source, row in originals.items():
        physical = BASE / 'original_snapshot' / Path(source).relative_to(ROOT)
        assert str(physical) == row['physical']
        pin(physical, {'sha256': row['sha256'], 'bytes': row['bytes'], 'symlink': None})
        read(source)
        if WATCH[source]['sha256'] != row['sha256']:
            assert source in controls
            control_drift[source] = {'original': row, 'actual': WATCH[source]}
        else:
            assert read(source) == read(physical)
    cmps = j(BASE / 'INTAKE_CMP_COMMANDS.json'); assert len(cmps) == 389
    seen = set()
    for row in cmps:
        source, physical = row['argv'][2:]
        assert row['argv'][:2] == ['/usr/bin/cmp', '--'] and source not in seen
        seen.add(source); assert physical == originals[source]['physical']
        assert row['exit_code'] == 0 and row['stdout'] == row['stderr'] == ''
        assert row['cwd'] == str(ROOT) and row['environment'] == ENV and row['inputs_unchanged']
        before = row['full_inputs_before']; assert before == row['full_inputs_after']
        assert set(before) == {source, physical}
        for path, value in before.items():
            if path in control_drift:
                pin(physical, {k: value[k] for k in ('sha256', 'bytes', 'symlink')})
            else:
                pin(path, value)
    assert seen == set(originals)
    for directory, count, digest in [
        (OLD, 347, '3250ea718e5b0f358a8a54ba2365a53732d637a2f9686c017e1767e4cdcc7e51'),
        (FAILED, 8, 'deb48a3ed612ad9e292436e2037a879df37a0a5e2204594702f436c73bbe4b04'),
        (BATCH / 'qa/central_lifecycle_p209_round1', 5, '2ecf22568096dffbf49213869d82e58f1a43d6506968f0753e6197b451558c22'),
        (BATCH / 'qa/central_lifecycle_p209_terminal_push', 5, 'e5b02d4594deba8e6bec8a5d31dac9b20dd2f40f8245be57dbf56bc5a39fad80')]:
        rows = manifest(directory, count, digest)
        assert rows == manifest(BASE / 'original_snapshot' / directory.relative_to(ROOT), count, digest)
    assert j(FAILED / 'COMMAND.json')['exit_code'] == 1
    assert j(FAILED / 'INPUTS_BEFORE.json') == j(FAILED / 'INPUTS_AFTER.json')
    assert read(FAILED / 'audit.stdout') == b''
    pin(FAILED / 'audit.stderr', '6c070f981a6b6f6ae05363e32f8047efda4f2a0e8c458f22dd9152990ccfb7cf')
    failure = j(BATCH / 'qa/P209_TERMINAL_ARTIFACT_INITIAL_01.failed.actual.json')
    assert failure['completion']['exit_code'] == 1
    assert read(FAILED / 'audit.stderr').decode() in failure['completion']['output']
    oldroot = j(BATCH / 'qa/P209_ARTIFACT_PREPARATION_ROOT_INSPECTION.actual.json')
    assert oldroot['completion']['exit_code'] == 0
    oldresult = json.loads(oldroot['completion']['output'])
    assert oldresult['status'] == 'PASS_ROOT_P209_ARTIFACT_PREPARATION_ORIGINAL_STATIC_CLOSURE_NOT_EXECUTED'
    assert oldresult['all_current_paths_checked_twice'] == 390
    edits = j(BASE / 'SOURCE_EDITS.json')['files']; diffs = j(BASE / 'DIFF_COMMANDS.json')
    assert set(edits) == {'audit_p209.py', 'record_audit.py', 'lifecycle_audit.py'} and len(diffs) == 3
    fresh = []; shared = {}
    for name, recipe in edits.items():
        assert recipe['original'] == str(OLD / name)
        old = read(OLD / name).decode(); expected = old; new = read(BASE / name).decode()
        for edit in recipe['edits']:
            assert expected.count(edit['old']) == 1
            expected = expected.replace(edit['old'], edit['new'], 1)
        assert expected == new
        oldfs, newfs = funcs(old), funcs(new)
        changed = {'audit_p209.py': {'main', 'load_aliases'}, 'record_audit.py': {'main'}, 'lifecycle_audit.py': set()}[name]
        assert {k for k in oldfs if oldfs[k] != newfs[k]} == changed
        assert set(newfs) - set(oldfs) == ({'revision_originals_and_failure'} if name == 'audit_p209.py' else set())
        shared[name] = len(set(oldfs) - changed)
        imports = lambda raw: [ast.dump(n) for n in ast.parse(raw).body if isinstance(n, (ast.Import, ast.ImportFrom))]
        assert imports(old) == imports(new)
        matches = [r for r in diffs if r['argv'] == ['/usr/bin/diff', '-u', '--', str(OLD / name), str(BASE / name)]]
        assert len(matches) == 1; row = matches[0]
        assert row['cwd'] == str(ROOT) and row['environment'] == ENV and row['exit_code'] == 1
        assert row['stderr'] == '' and row['inputs_unchanged']
        assert row['inputs_before'] == row['inputs_after']; check_map(row['inputs_before'])
        assert read(BASE / 'diffs' / (name + '.diff')) == row['stdout'].encode()
        started = datetime.now(timezone.utc).isoformat()
        child = subprocess.run(row['argv'], cwd=ROOT, env=ENV, capture_output=True, check=False)
        assert child.returncode == 1 and child.stdout == row['stdout'].encode() and not child.stderr
        fresh.append({'argv': row['argv'], 'cwd': str(ROOT), 'environment': ENV, 'started_utc': started,
                      'ended_utc': datetime.now(timezone.utc).isoformat(), 'exit_code': child.returncode,
                      'stdout': child.stdout.decode(), 'stderr': child.stderr.decode(),
                      'exact_preserved_raw_diff_match': True})
    assert shared == {'audit_p209.py': 32, 'record_audit.py': 3, 'lifecycle_audit.py': 36}
    assert read(BASE / 'ADAPTATION.diff') == ''.join(r['stdout'] for r in diffs).encode()
    static = j(BASE / 'STATIC_RESULT.json')
    assert static['status'] == 'PASS_STATIC_REVISION_SOURCE_AND_ORIGINAL_CLOSURE_NOT_EXECUTED'
    assert static['immutable_inputs_before'] == static['immutable_inputs_after'] == immutable
    folder = BASE / 'checks/static_01'; receipt = j(folder / 'RECEIPT.json'); attempt = j(folder / 'ATTEMPT.json')
    assert receipt['argv'] == ['/usr/bin/python3.10', '-I', '-S', '-B', str(BASE / 'static_revision.py')]
    assert receipt['cwd'] == str(ROOT) and receipt['environment'] == ENV
    assert receipt['exit_code'] == 0 and receipt['status'] == 'COMPLETED' and receipt['inputs_unchanged']
    assert attempt['exit_code'] is None and attempt['status'] == 'ATTEMPTED'
    assert all(attempt[k] == receipt[k] for k in ('argv', 'cwd', 'environment', 'started_utc'))
    for stream in ('stdout', 'stderr'):
        pin(folder / stream, receipt[stream])
    assert read(folder / 'stderr') == b''
    assert j(folder / 'stdout') == {k: v for k, v in static.items() if not k.startswith('immutable_inputs_')}
    before = j(folder / 'INPUTS_BEFORE.json'); assert before == j(folder / 'INPUTS_AFTER.json'); check_map(before)
    final = j(BASE / 'FINAL_DOCUMENT_CHECK.json')
    assert final['status'] == 'PASS_FINAL_DOCUMENTARY_CLOSURE_NOT_TARGET_EXECUTION'
    assert final['full_current_package_inputs_before'] == final['full_current_package_inputs_after']
    check_map(final['full_current_package_inputs_before'])
    parsed = []
    for path in sorted(BASE.rglob('*')):
        if path.is_file() and path.suffix == '.py':
            compile(ast.parse(read(path).decode(), filename=str(path)), str(path), 'exec', optimize=0)
            parsed.append(path.relative_to(BASE).as_posix())
        elif path.is_file() and path.suffix == '.json':
            j(path)
    assert parsed == final['all_python_sources_final_parsed_without_execution'] and len(parsed) == 27
    contract, previous = j(BASE / 'INPUT_CONTRACT.json'), j(OLD / 'INPUT_CONTRACT.json')
    for key in ('future_root_artifact_acceptance', 'initial_artifact_result_schema', 'lifecycle_sequence'):
        assert contract[key] == previous[key]
    assert contract['artifact_entry'] == ['record_audit.py', 'initial_02']
    for path in (BATCH / 'qa/p209_terminal_artifact/initial_02', BATCH / 'qa/p209_terminal_artifact/lifecycle_before',
                 BATCH / 'qa/P209_TERMINAL_ARTIFACT_ROOT_INSPECTION.actual.json'):
        assert not path.exists()
    assert all(info(path) == value for path, value in WATCH.items())
    print(json.dumps({'status': 'PASS_ROOT_P209_REVISION_01_COMPLETE_ORIGINAL_STATIC_PREFLIGHT_NOT_TARGET_EXECUTION',
        'started_utc': began, 'ended_utc': datetime.now(timezone.utc).isoformat(),
        'revision_payloads': 418, 'original_physical_copies': 389, 'archived_cmp_commands': 389,
        'immutable_original_keys_checked_twice': 2033, 'current_read_paths_checked_twice': len(WATCH),
        'current_read_map_sha256': sha256(json.dumps(WATCH, sort_keys=True).encode()).hexdigest(),
        'source_exact_replace_once_and_imports_pass': True, 'unchanged_functions': shared,
        'fresh_raw_diff_commands': fresh, 'python_sources_parsed_not_executed': 27,
        'original_failed_child_and_wrapper_exit': [1, 1], 'actual_static_child_exit': 0,
        'changed_root_control_aliases': control_drift,
        'target_auditor_lifecycle_guard_science_build_view_executions': 0,
        'owner': 'OWNER_AMBER', 'external_status': 'HOLD_EXTERNAL'}, sort_keys=True, indent=2))


if __name__ == '__main__':
    assert sys.flags.isolated and sys.flags.no_site and sys.dont_write_bytecode and not sys.flags.optimize
    assert dict(os.environ) == ENV and Path.cwd() == ROOT
    main()
