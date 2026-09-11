"""Source/data/diff checks only. No target code imported or executed."""
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


def info(p):
    p = Path(p); raw = p.read_bytes()
    return {'sha256': sha256(raw).hexdigest(), 'bytes': len(raw), 'resolved': str(p.resolve()),
            'symlink': os.readlink(p) if p.is_symlink() else None}


def j(p):
    return json.loads(Path(p).read_bytes())


def save(p, raw):
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open('xb') as stream:
        stream.write(raw)


def dump(p, v):
    save(p, (json.dumps(v, sort_keys=True, indent=2) + '\n').encode())


def snap(p):
    return BASE / 'original_snapshot' / Path(p).relative_to(ROOT)


def functions(raw):
    tree = ast.parse(raw)
    return {n.name: ast.get_source_segment(raw, n) for n in tree.body
            if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))}


def manifest(base, name, count, digest=None):
    if digest is not None:
        assert info(base / name)['sha256'] == digest
    rows = {}
    for line in (base / name).read_text().splitlines():
        m = re.fullmatch(r'([0-9a-f]{64})  (.+)', line)
        assert m is not None
        h, rel = m.groups(); path = Path(rel)
        assert path.parts and not path.is_absolute() and '..' not in path.parts and rel not in rows
        rows[rel] = h
    actual = set()
    for p in base.rglob('*'):
        assert not p.is_symlink()
        if p.is_file():
            actual.add(p.relative_to(base).as_posix())
    assert name not in rows and len(rows) == count and set(rows) == actual - {name}
    for rel, h in rows.items():
        assert info(base / rel)['sha256'] == h
    return rows


def main():
    began = datetime.now(timezone.utc).isoformat()
    assert not (BASE / 'STATIC_RESULT.json').exists()
    originals = j(BASE / 'ORIGINAL_INPUTS.json')
    immutable = j(BASE / 'IMMUTABLE_PACKAGE_INPUTS.json')
    current_before = {p: info(p) for p in immutable}
    assert current_before == immutable and len(immutable) == 2033
    changed_controls = {}
    allowed_controls = {str(ROOT / 'SYMBOLIC_DYNAMICS_STATE.md'), str(BATCH / 'PIPELINE_STATE.md'),
                        str(BATCH / 'GIT_SYNC_RECEIPT.md')}
    assert len(originals) == 389
    for source, row in originals.items():
        assert row['physical'] == str(snap(source))
        got = info(row['physical'])
        assert got['sha256'] == row['sha256'] and got['bytes'] == row['bytes'] and got['symlink'] is None
        current = info(source)
        if current['sha256'] != row['sha256'] or current['bytes'] != row['bytes']:
            assert source in allowed_controls
            changed_controls[source] = {'original': row, 'now': current,
                'role': 'Separately advanced root control; exact original remains in snapshot and is not repinned.'}
    cmps = j(BASE / 'INTAKE_CMP_COMMANDS.json')
    assert len(cmps) == 389
    for row in cmps:
        assert row['argv'][:2] == ['/usr/bin/cmp', '--'] and row['exit_code'] == 0
        assert row['cwd'] == str(ROOT) and row['environment'] == ENV
        assert row['stdout'] == row['stderr'] == '' and row['inputs_unchanged'] is True
        assert row['full_inputs_before'] == row['full_inputs_after']
    for base, name, count, digest in [
        (OLD, 'SHA256SUMS', 347, '3250ea718e5b0f358a8a54ba2365a53732d637a2f9686c017e1767e4cdcc7e51'),
        (FAILED, 'SHA256SUMS', 8, 'deb48a3ed612ad9e292436e2037a879df37a0a5e2204594702f436c73bbe4b04')]:
        assert manifest(base, name, count, digest) == manifest(snap(base), name, count, digest)
    assert j(FAILED / 'COMMAND.json')['exit_code'] == 1
    assert j(FAILED / 'INPUTS_BEFORE.json') == j(FAILED / 'INPUTS_AFTER.json')
    assert len(j(FAILED / 'INPUTS_BEFORE.json')) == 7
    assert (FAILED / 'audit.stdout').read_bytes() == b''
    assert info(FAILED / 'audit.stderr')['sha256'] == '6c070f981a6b6f6ae05363e32f8047efda4f2a0e8c458f22dd9152990ccfb7cf'
    for executed, source in [('executed_auditor_snapshot.py', 'audit_p209.py'),
                             ('executed_recorder_snapshot.py', 'record_audit.py')]:
        assert (FAILED / executed).read_bytes() == (OLD / source).read_bytes()
    wrapper = j(BATCH / 'qa/P209_TERMINAL_ARTIFACT_INITIAL_01.failed.actual.json')
    assert wrapper['completion']['exit_code'] == 1
    assert (FAILED / 'audit.stderr').read_text() in wrapper['completion']['output']
    root_static = j(BATCH / 'qa/P209_ARTIFACT_PREPARATION_ROOT_INSPECTION.actual.json')
    assert root_static['completion']['exit_code'] == 0
    root_result = json.loads(root_static['completion']['output'])
    assert root_result['status'] == 'PASS_ROOT_P209_ARTIFACT_PREPARATION_ORIGINAL_STATIC_CLOSURE_NOT_EXECUTED'
    assert (root_result['preparation_payloads'], root_result['original_copies'],
            root_result['historical_commands'], root_result['all_current_paths_checked_twice']) == (347, 33, 47, 390)
    assert root_result['artifact_lifecycle_math_build_view_executions'] == 0

    edits = j(BASE / 'SOURCE_EDITS.json')['files']
    assert set(edits) == {'audit_p209.py', 'record_audit.py', 'lifecycle_audit.py'}
    changes, diff_records, shared = {}, [], {}
    for name, recipe in edits.items():
        assert recipe['original'] == str(OLD / name)
        oldraw = (OLD / name).read_text(); expected = oldraw
        for row in recipe['edits']:
            assert expected.count(row['old']) == 1
            expected = expected.replace(row['old'], row['new'], 1)
        current = (BASE / name).read_text()
        assert current == expected, name
        oldfs, newfs = functions(oldraw), functions(current)
        allowed = {'audit_p209.py': {'main', 'load_aliases'}, 'record_audit.py': {'main'}, 'lifecycle_audit.py': set()}[name]
        assert set(newfs) - set(oldfs) == ({'revision_originals_and_failure'} if name == 'audit_p209.py' else set())
        assert set(oldfs) <= set(newfs)
        assert {k for k in oldfs if oldfs[k] != newfs[k]} == allowed
        shared[name] = sorted(set(oldfs) - allowed)
        for key in shared[name]:
            assert oldfs[key] == newfs[key]
        oldimports = [ast.dump(n) for n in ast.parse(oldraw).body if isinstance(n, (ast.Import, ast.ImportFrom))]
        newimports = [ast.dump(n) for n in ast.parse(current).body if isinstance(n, (ast.Import, ast.ImportFrom))]
        assert oldimports == newimports
        argv = ['/usr/bin/diff', '-u', '--', str(OLD / name), str(BASE / name)]
        inputs = {str(p): info(p) for p in (OLD / name, BASE / name, Path('/usr/bin/diff'))}
        started = datetime.now(timezone.utc).isoformat()
        child = subprocess.run(argv, cwd=ROOT, env=ENV, capture_output=True, check=False)
        assert child.returncode == 1 and not child.stderr and child.stdout
        after = {p: info(p) for p in inputs}; assert after == inputs
        save(BASE / 'diffs' / (name + '.diff'), child.stdout)
        diff_records.append({'argv': argv, 'cwd': str(ROOT), 'environment': ENV, 'started_utc': started,
            'ended_utc': datetime.now(timezone.utc).isoformat(), 'exit_code': child.returncode,
            'stdout': child.stdout.decode(), 'stderr': child.stderr.decode(),
            'inputs_before': inputs, 'inputs_after': after, 'inputs_unchanged': True})
        changes[name] = {'old': info(OLD / name), 'new': info(BASE / name), 'replace_once_blocks': len(recipe['edits']),
                         'unchanged_functions': len(shared[name]), 'changed_functions': sorted(allowed)}
    dump(BASE / 'DIFF_COMMANDS.json', diff_records)
    save(BASE / 'ADAPTATION.diff', ''.join(r['stdout'] for r in diff_records).encode())
    aud = (BASE / 'audit_p209.py').read_text(); life = (BASE / 'lifecycle_audit.py').read_text()
    assert "PREPARATION = BATCH / 'qa/p209_terminal_artifact_revision_01'" in aud
    assert "PREPARATION = BATCH / 'qa/p209_terminal_artifact_revision_01'" in life
    assert functions(life)['actual_initial_gate'] == functions((OLD / 'lifecycle_audit.py').read_text())['actual_initial_gate']
    assert "pin(PREPARATION / 'audit_p209.py', gate['auditor_sha256'])" in life
    assert "if sys.argv[1:] != ['initial_02']:" in (BASE / 'record_audit.py').read_text()
    assert "Path(__file__).resolve()==PREP/'record_audit.py'" in (BASE / 'record_audit.py').read_text()

    gitkey = str(BATCH / 'GIT_SYNC_RECEIPT.md')
    old_b_roles = j(OLD / 'original_snapshot/B_EXACT_HISTORY_ALIASES.json')
    git_roles = []
    for number, directory, digest, seal in [
        (1, 'central_lifecycle_p209_round1', '2f6998d2986831fa8776e31e9d336497e6ab37b114d1b13ef94879f3e2271c24',
         '2ecf22568096dffbf49213869d82e58f1a43d6506968f0753e6197b451558c22'),
        (2, 'central_lifecycle_p209_terminal_push', 'a67457d5fe6e860040ad5f72a51b839e0220b7b83af22188008c8a74850b1865',
         'e5b02d4594deba8e6bec8a5d31dac9b20dd2f40f8245be57dbf56bc5a39fad80')]:
        holder = BATCH / 'qa' / directory
        assert manifest(holder, 'SHA256SUMS', 5, seal) == manifest(snap(holder), 'SHA256SUMS', 5, seal)
        assert info(holder / 'GIT_SYNC_RECEIPT.before.md')['sha256'] == digest
        meta = j(ROOT / ('papers/209-ordered-fibre-threading/frozen_round%d/ROUND%d_PROVENANCE.json' % (number, number)))
        assert meta['all_source_inputs_before_and_rechecked_after'][gitkey] == digest
        capture = j(holder / 'CAPTURE.actual.json')
        if number == 1:
            rows = [r for r in capture['copies'] if r['original_path'] == gitkey]
            assert len(rows) == 1 and rows[0]['sha256'] == digest
            assert rows[0]['physical_path'] == str(holder / 'GIT_SYNC_RECEIPT.before.md')
            assert rows[0]['actual_cmp']['exit_code'] == 0 and rows[0]['actual_cmp']['output'] == ''
            assert old_b_roles[gitkey + ' @ ' + digest] == str(holder / 'GIT_SYNC_RECEIPT.before.md')
        else:
            rows = [r for r in capture['copies'] if r['source'] == str(Path(gitkey).relative_to(ROOT))]
            assert len(rows) == 1 and rows[0]['copy'] == str((holder / 'GIT_SYNC_RECEIPT.before.md').relative_to(ROOT))
            assert rows[0]['actual_comparison']['exit_code'] == 0 and rows[0]['actual_comparison']['output'] == ''
            assert digest + '  ' + str(Path(gitkey).relative_to(ROOT)) in capture['original_sha256_command']['output'].splitlines()
            assert gitkey + ' @ ' + digest not in old_b_roles
        git_roles.append({'round': number, 'sha256': digest, 'physical': str(holder / 'GIT_SYNC_RECEIPT.before.md'),
                          'present_in_original_B_map': number == 1, 'frozen_value_type': 'string'})

    contract = j(BASE / 'INPUT_CONTRACT.json'); previous_contract = j(OLD / 'INPUT_CONTRACT.json')
    assert contract['status'] == 'PREPARED_ONLY_NOT_EXECUTED_OR_ACCEPTED'
    assert contract['artifact_entry'] == ['record_audit.py', 'initial_02']
    assert contract['future_root_artifact_acceptance'] == previous_contract['future_root_artifact_acceptance']
    assert contract['initial_artifact_result_schema'] == previous_contract['initial_artifact_result_schema']
    assert contract['lifecycle_sequence'] == previous_contract['lifecycle_sequence']
    for path in (BATCH / 'qa/p209_terminal_artifact/initial_02', BATCH / 'qa/p209_terminal_artifact/lifecycle_before',
                 BATCH / 'qa/P209_TERMINAL_ARTIFACT_ROOT_INSPECTION.actual.json'):
        assert not path.exists(), ('future output must not be fabricated', path)
    parsed = []
    for p in sorted(BASE.rglob('*.py')):
        code = p.read_text(); tree = ast.parse(code, filename=str(p))
        compile(tree, str(p), 'exec', optimize=0)
        parsed.append(str(p.relative_to(BASE)))
    assert current_before == {p: info(p) for p in immutable}
    result = {'status': 'PASS_STATIC_REVISION_SOURCE_AND_ORIGINAL_CLOSURE_NOT_EXECUTED',
        'started_utc': began, 'ended_utc': datetime.now(timezone.utc).isoformat(),
        'original_copies_verified': len(originals), 'actual_intake_cmp_commands_verified': len(cmps),
        'immutable_old_preparation_B_LNR_failure_paths_checked_twice': len(immutable),
        'immutable_inputs_before': current_before, 'immutable_inputs_after': {p: info(p) for p in immutable},
        'source_changes': changes, 'unchanged_literal_functions': shared,
        'python_sources_parsed_and_compiled_without_execution': parsed,
        'raw_diff_commands': 3, 'raw_diff_exits': [r['exit_code'] for r in diff_records],
        'failure_child_exit': 1, 'failure_wrapper_exit': 1, 'exact_git_history_roles': git_roles,
        'root_original_static_evidence_parsed': {k: root_result[k] for k in ('status', 'preparation_payloads', 'original_copies', 'historical_commands', 'all_current_paths_checked_twice')},
        'control_changes_since_intake': changed_controls,
        'auditor_lifecycle_guard_science_build_view_executions': 0,
        'future_root_gate_schema_unchanged_and_actual_auditor_hash_required': True,
        'owner': 'OWNER_AMBER', 'external_status': 'HOLD_EXTERNAL'}
    dump(BASE / 'STATIC_RESULT.json', result)
    print(json.dumps({k: v for k, v in result.items() if not k.startswith('immutable_inputs_')}, sort_keys=True, indent=2))


if __name__ == '__main__':
    assert sys.flags.isolated and sys.flags.no_site and sys.dont_write_bytecode and not sys.flags.optimize
    assert dict(os.environ) == ENV and Path.cwd() == ROOT
    main()
