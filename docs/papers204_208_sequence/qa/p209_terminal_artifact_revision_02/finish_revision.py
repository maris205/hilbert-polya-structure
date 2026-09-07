"""Final preparation-only source/documentary recheck and measured nonself seal.

Does not import or execute target auditor/lifecycle/guard code. Only native
read-only diff subprocesses run. Scientific files, old packages and all
root-owned paths are read-only. This script exclusively creates final local
evidence files and the final preparation seal after validation.
"""
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
HERE = Path(__file__).resolve().parent
ENV = {'PATH': '/usr/bin:/bin', 'LANG': 'C.UTF-8', 'LC_ALL': 'C.UTF-8', 'TZ': 'UTC'}


def info(path):
    raw = Path(path).read_bytes()
    return {'sha256': sha256(raw).hexdigest(), 'bytes': len(raw)}


def js(path): return json.loads(Path(path).read_bytes())


def save(name, raw):
    with (HERE / name).open('xb') as stream: stream.write(raw)


def dump(name, data): save(name, (json.dumps(data, indent=2, sort_keys=True) + '\n').encode())


def package(base, count, expected):
    assert info(base / 'SHA256SUMS')['sha256'] == expected
    rows = {}
    for line in (base / 'SHA256SUMS').read_text().splitlines():
        match = re.fullmatch(r'([0-9a-f]{64})  (.+)', line); assert match
        digest, rel = match.groups(); relative = Path(rel)
        assert rel not in rows and not relative.is_absolute() and '..' not in relative.parts
        rows[rel] = digest
    physical = set()
    for path in base.rglob('*'):
        assert not path.is_symlink()
        if path.is_file(): physical.add(path.relative_to(base).as_posix())
    assert len(rows) == count and set(rows) == physical - {'SHA256SUMS'}
    assert all(info(base / name)['sha256'] == value for name, value in rows.items())
    return {'payloads': len(rows), 'complete_nonself': True, 'sha256': expected}


def main():
    started = datetime.now(timezone.utc).isoformat()
    assert HERE == BATCH / 'qa/p209_terminal_artifact_revision_02'
    assert dict(os.environ) == ENV and Path.cwd() == ROOT and sys.flags.optimize == 0
    assert sys.flags.isolated == sys.flags.no_site == 1 and sys.dont_write_bytecode
    assert not (HERE / 'SHA256SUMS').exists()
    assert not (BATCH / 'qa/p209_terminal_artifact/initial_03').exists()
    inputs = {}
    def merge(mapping):
        for path, value in mapping.items():
            if Path(path).is_relative_to(HERE): continue
            assert path not in inputs or inputs[path] == value, path
            inputs[path] = value
    merge(js(HERE / 'SCHEMA_INPUTS_BEFORE.json'))
    merge(js(HERE / 'LINK_LAYOUT.json')['original_inputs_before'])
    merge(js(HERE / 'LINK_ADDITIONS_RESULT.json')['inputs_before'])
    added = js(HERE / 'LINK_ADDITION_INTAKE.json')
    merge(added['inputs_before'])
    controls = {
        ROOT / 'SYMBOLIC_DYNAMICS_STATE.md': 'b259bc776d3597fa7c30e1bed962d91a46fc3c62fe43b542f03e2006256c603f',
        BATCH / 'PIPELINE_STATE.md': 'f381d5929f2bc36aa0eb8ce9b4c7b968d4c3bc79c2e731ceb6efce0534499d31',
        BATCH / 'GIT_SYNC_RECEIPT.md': '303e1ad876f35fc6715d896f2979fd212f64aeb686ebd8ee1e2d649e9628b230',
        ROOT / 'papers/209-ordered-fibre-threading/PAPER_MANIFEST.sha256': '84337036dead70c7680aed5678ed770505b1caa0184b5f405d353c4d9a811c77',
        ROOT / 'papers/209-ordered-fibre-threading/ROOT_LIFECYCLE.md': '5d0381c67eb47234f19c962ffd55a1ad00f6617129c64bda62ff5736f24b87e4'}
    for path, digest in controls.items():
        row = info(path); assert row['sha256'] == digest; merge({str(path): row})
    before = {path: info(path) for path in inputs}; assert before == inputs
    schema = js(HERE / 'SCHEMA_PROJECTIONS.json')
    assert schema['all_inputs_unchanged'] and schema['source_data_records'] == 1017
    assert js(HERE / 'SCHEMA_INPUTS_BEFORE.json') == js(HERE / 'SCHEMA_INPUTS_AFTER.json')
    for name, value in schema['observations'].items():
        if isinstance(value, bool): assert value, name
        elif isinstance(value, dict) and 'equal' in value: assert value['equal'], name
        elif isinstance(value, list):
            for row in value:
                for key in ('embedded_equal', 'attempt_shared_fields_equal', 'map_union_equal', 'attempt_fields_equal'):
                    if key in row: assert row[key], (name, key)
    link = js(HERE / 'LINK_ADDITIONS_RESULT.json')
    assert link['old_missing'] == 176 and link['remaining_missing'] == []
    assert link['resolved_by_exact_origin'] == {'A01': 9, 'B01': 10, 'author_workspace': 157}
    assert link['complete_line_scan_local_links_recomputed'] == 1528 and link['all_original_documents_unchanged']
    copies = schema['physical_copies'] + added['copies']
    for row in copies:
        expected = {k: row[k] for k in ('sha256', 'bytes')}
        assert info(row['copy']) == expected
        if not Path(row['original']).is_relative_to(HERE): assert info(row['original']) == expected
    comparisons = schema['actual_cmp_commands'] + added['actual_cmp_commands']
    assert len(comparisons) == 34 and all(r['exit_code'] == 0 and r['stdout'] == r['stderr'] == '' for r in comparisons)
    immutable = {}
    for name, count, digest in [
        ('p209_terminal_artifact_preparation', 347, '3250ea718e5b0f358a8a54ba2365a53732d637a2f9686c017e1767e4cdcc7e51'),
        ('p209_terminal_artifact_revision_01', 418, '855aba017f5a369c09696272579897324bbd906892b353d17f0c9eb6d7fcbcc5'),
        ('p209_terminal_artifact/initial_01', 8, 'deb48a3ed612ad9e292436e2037a879df37a0a5e2204594702f436c73bbe4b04'),
        ('p209_terminal_artifact/initial_02', 8, '89ab791251744f3aa96911f871f108268c2ebb7e5e1da55329eea45eb70bbc96')]:
        immutable[name] = package(BATCH / 'qa' / name, count, digest)
    draft = package(HERE / 'unexecuted_draft_before_link_registration', 7,
                    '501f7f25cd3dc6756926d73ad089a5a297eb3fe75c70c45d709e468c821bda14')
    functions, source_pins = {}, {}
    expected_changes = {'audit_p209.py': {'reviews', 'revision_originals_and_failure', 'pages_and_links'},
                        'record_audit.py': {'main'}, 'lifecycle_audit.py': set()}
    for name, edits in js(HERE / 'SOURCE_EDITS.json').items():
        old = (BATCH / 'qa/p209_terminal_artifact_revision_01' / name).read_text()
        changed = old
        for row in edits:
            assert changed.count(row['old']) == row['required_old_occurrences'] == 1
            changed = changed.replace(row['old'], row['new'], 1)
        actual = (HERE / name).read_text(); assert changed == actual
        segments = []
        for source in (old, actual):
            tree = ast.parse(source)
            segments.append({n.name: ast.get_source_segment(source, n) for n in tree.body if isinstance(n, ast.FunctionDef)})
        assert set(segments[0]) == set(segments[1])
        diff = {k for k in segments[0] if segments[0][k] != segments[1][k]}
        assert diff == expected_changes[name]
        functions[name] = {'changed': sorted(diff), 'unchanged': len(segments[0]) - len(diff)}
        source_pins[name] = info(HERE / name)
    parsed = []
    for path in sorted(HERE.rglob('*.py')):
        compile(ast.parse(path.read_bytes(), filename=str(path)), str(path), 'exec', dont_inherit=True, optimize=0)
        parsed.append(str(path.relative_to(HERE)))
    diffs = []
    for recorded in js(HERE / 'DIFF_COMMANDS.json'):
        run = subprocess.run(recorded['argv'], cwd=ROOT, env=ENV, capture_output=True, check=False)
        assert run.returncode == 1 and run.stdout == (HERE / recorded['stdout_path']).read_bytes() and run.stderr == b''
        name = Path(recorded['argv'][-1]).name
        stdout_name = 'final_diff_' + name + '.stdout'; stderr_name = 'final_diff_' + name + '.stderr'
        save(stdout_name, run.stdout); save(stderr_name, run.stderr)
        diffs.append({'argv': recorded['argv'], 'cwd': str(ROOT), 'env': ENV, 'exit_code': run.returncode,
                      'stdout': {'path': stdout_name, **info(HERE / stdout_name)},
                      'stderr': {'path': stderr_name, **info(HERE / stderr_name)}})
    native02 = BATCH / 'qa/p209_terminal_artifact/initial_02'
    failure = js(native02 / 'COMMAND.json'); wrapper = BATCH / 'qa/P209_TERMINAL_ARTIFACT_INITIAL_02.failed.actual.json'
    assert info(wrapper)['sha256'] == 'cb4872647ea63e9e2e9253dcb7d11d090947f8399c497a358239223241f9e602'
    assert failure['exit_code'] == js(wrapper)['completion']['exit_code'] == 1
    assert failure['inputs_unchanged'] and failure['unused_cache_absent']
    assert len(js(native02 / 'INPUTS_BEFORE.json')) == 10
    assert js(native02 / 'INPUTS_BEFORE.json') == js(native02 / 'INPUTS_AFTER.json')
    assert info(native02 / 'audit.stderr') == {'bytes': 871, 'sha256': '87df565befc65ce9d96c25cf6e28f470521bea9207750c17ee1123ed6384c09b'}
    assert (native02 / 'audit.stdout').read_bytes() == b''
    assert (native02 / 'audit.stderr').read_text() in js(wrapper)['completion']['output']
    assert not (BATCH / 'qa/p209_terminal_artifact/initial_03').exists()
    after = {path: info(path) for path in before}; assert after == before
    result = {'schema': 'p209-terminal-artifact-revision02-static-preparation-v1',
        'status': 'PASS_STATIC_PREPARATION_ONLY_NOT_ARTIFACT_GATE', 'started_utc': started,
        'ended_utc': datetime.now(timezone.utc).isoformat(), 'all_original_inputs_unchanged': True,
        'original_input_paths': len(before), 'original_inputs_before': before, 'original_inputs_after': after,
        'second_complete_original_package_validation': immutable, 'unexecuted_draft_seal': draft,
        'exact_physical_copies_rechecked': len(copies), 'external_physical_copies': sum(not Path(r['original']).is_relative_to(HERE) for r in copies),
        'native_intake_cmp_commands_retained': len(comparisons), 'source_pins': source_pins,
        'literal_function_changes': functions, 'python_files_parsed_compiled_not_executed': parsed,
        'fresh_final_actual_raw_diffs': diffs, 'initial02_child_exit': 1, 'initial02_wrapper_exit': 1,
        'static_link_missing_before': 176, 'static_link_missing_after': 0,
        'new_target_auditor_lifecycle_guard_executions': 0, 'new_science_build_render_views': 0,
        'initial03_created': False, 'central_controls_unchanged': {str(p): d for p, d in controls.items()},
        'scope': 'Preparation and exact original source/schema evidence only; root must independently inspect and actually execute initial_03.',
        'external': 'OWNER_AMBER / HOLD_EXTERNAL'}
    dump('STATIC_RESULT.json', result)
    payloads = sorted(p for p in HERE.rglob('*') if p.is_file())
    assert all(not p.is_symlink() for p in HERE.rglob('*'))
    lines = ''.join(info(p)['sha256'] + '  ' + p.relative_to(HERE).as_posix() + '\n' for p in payloads)
    save('SHA256SUMS', lines.encode())
    sealed = package(HERE, len(payloads), info(HERE / 'SHA256SUMS')['sha256'])
    print(json.dumps({'status': result['status'], 'payloads': sealed['payloads'], 'seal_sha256': sealed['sha256'],
        'original_input_paths_rechecked': len(before), 'external_copies': result['external_physical_copies'],
        'unexecuted_draft_copies': len(copies) - result['external_physical_copies'],
        'source_pins': source_pins, 'function_changes': functions, 'target_executions': 0}, sort_keys=True))


if __name__ == '__main__': main()
