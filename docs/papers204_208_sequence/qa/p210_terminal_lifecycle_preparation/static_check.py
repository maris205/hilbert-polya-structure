#!/usr/bin/env python3
"""Data/AST-only preparation check; never import or call the lifecycle reader."""
import ast
import hashlib
import json
from pathlib import Path
import re
import shlex

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
QA = ROOT / 'docs/papers204_208_sequence/qa'
HERE = QA / 'p210_terminal_lifecycle_preparation'
PAPER = ROOT / 'papers/210-weakly-increasing-run-aggregation'
HISTORY = QA / 'p210_precompletion_controls_01'
INITIAL = QA / 'p210_terminal_artifact_03'
ENV = {'PATH': '/usr/bin:/bin', 'LANG': 'C.UTF-8', 'LC_ALL': 'C.UTF-8', 'TZ': 'UTC'}

def pin(path):
    data = Path(path).read_bytes()
    return {'sha256': hashlib.sha256(data).hexdigest(), 'bytes': len(data)}

def obj(path):
    return json.loads(Path(path).read_bytes())

def manifest(path):
    rows = {}
    for line in Path(path).read_text().splitlines():
        m = re.fullmatch(r'([0-9a-f]{64})  (.+)', line)
        assert m and m[2] not in rows and not Path(m[2]).is_absolute() and '..' not in Path(m[2]).parts
        rows[m[2]] = m[1]
    return rows

def main():
    source = HERE / 'inspect_p210_lifecycle.py'
    text = source.read_text()
    parsed = ast.parse(text)
    old_path = QA / 'p210_terminal_artifact_revision_03/inspect_p210_artifact.py'
    old_text = old_path.read_text()
    old = ast.parse(old_text)
    now_nodes = {n.name: n for n in parsed.body if isinstance(n, ast.FunctionDef)}
    old_nodes = {n.name: n for n in old.body if isinstance(n, ast.FunctionDef)}
    helpers = ('file_key', 'pin', 'raw', 'obj', 'physical', 'stripped_links')
    inherited = {}
    for name in helpers:
        now = ast.get_source_segment(text, now_nodes[name])
        prior = ast.get_source_segment(old_text, old_nodes[name])
        assert now == prior
        inherited[name] = hashlib.sha256(now.encode()).hexdigest()
    assert len(now_nodes) == len([n for n in parsed.body if isinstance(n, ast.FunctionDef)])
    imports = set()
    for node in ast.walk(parsed):
        if isinstance(node, ast.Import):
            imports.update(a.name for a in node.names)
        elif isinstance(node, ast.ImportFrom):
            assert node.level == 0
            imports.add(node.module)
        if isinstance(node, ast.Call):
            if isinstance(node.func, ast.Name):
                assert node.func.id not in {'exec', 'eval', 'compile', '__import__'}
            if isinstance(node.func, ast.Attribute):
                assert node.func.attr not in {'write_bytes', 'write_text', 'mkdir', 'unlink', 'rmdir', 'rename',
                    'replace', 'rmtree', 'remove', 'Popen', 'run', 'system', 'kill', 'killpg', 'walk'}
                if node.func.attr == 'rglob':
                    assert now_nodes['physical'].lineno <= node.lineno <= now_nodes['physical'].end_lineno
    assert imports == {'collections', 'hashlib', 'gzip', 'json', 'os', 'pathlib', 're', 'shlex', 'sys',
                       'traceback', 'urllib.parse'}
    main_text = ast.get_source_segment(text, now_nodes['main'])
    assert main_text.index('all_actual_native_closures(binding)') < main_text.index('initial_capture(binding)') < main_text.index("binding['named_current_input_pins']")
    assert main_text.index('force=True') < main_text.index('for name, expected in PACKAGES.items()')
    binding = obj(HERE / 'ACTUAL_BINDING.json')
    assert binding['schema'] == 'p210-document-only-lifecycle-actual-binding-v1' and binding['root_acceptance'] is False
    inputs = {}
    for path, expected in binding['named_current_input_pins'].items():
        assert Path(path).is_absolute()
        inputs[path] = pin(path)
        assert inputs[path] == expected
    initial = binding['initial_artifact']
    doc = binding['documentary_transition']
    assert len(inputs) == 62 and doc['refresh_native_session'] == 67304
    normal = {}
    for prefix, source_name, session, extra in (
        ('P210_ARTIFACT03_ROOT', 'record_p210_artifact_03.py', 16560,
            ['--expected-artifact-preparation-sha256', initial['preparation_seal']['sha256']]),
        ('P210_ARTIFACT_ROOT_READ', 'receive_p210_initial_artifact.py', 53600, []),
        ('P210_COMPLETION_LIFECYCLE_REFRESH_ROOT', 'refresh_p210_completion_whole_manifest.py', 67304, [])):
        launch = obj(QA / (prefix + '_LAUNCH.actual.json'))
        completed = obj(QA / (prefix + '_COMPLETION.actual.json'))
        assert launch['result']['session_id'] == completed['session_id'] == session
        assert launch['result']['output'] == '' and 'exit_code' not in launch['result']
        assert completed['result']['exit_code'] == 0 and 'session_id' not in completed['result']
        assert completed['launch_record'] == prefix + '_LAUNCH.actual.json'
        assert shlex.split(launch['command']) == ['/usr/bin/python3.10', '-I', '-S', '-B', str(QA / source_name), *extra]
        assert launch['cwd'] == str(ROOT)
        normal[prefix] = {'session': session, 'completion_chunk': completed['result']['chunk_id'],
                         'stdout': {'bytes': len(completed['result']['output'].encode()),
                                    'sha256': hashlib.sha256(completed['result']['output'].encode()).hexdigest()}}
    accepted = obj(QA / 'P210_ARTIFACT_ROOT_ACCEPTANCE.actual.json')
    assert accepted == initial['root_acceptance_complete_value']
    root_completed = obj(QA / 'P210_ARTIFACT_ROOT_READ_COMPLETION.actual.json')
    assert root_completed['result']['output'] == json.dumps(initial['root_original_reception_complete_value'], sort_keys=True) + '\n'
    raw = obj(INITIAL / 'ARTIFACT_REPORT.json')
    result = obj(INITIAL / 'RESULT.json')
    expected_summary = dict(status='PASS_ACTUAL_P210_ARTIFACT_INITIAL_CAPTURE', output=str(INITIAL),
        original_wait_exit_code=0, stdout=pin(INITIAL / 'ARTIFACT_REPORT.json'), stderr=pin(INITIAL / 'stderr'),
        result=pin(INITIAL / 'RESULT.json'), seal=pin(INITIAL / 'SHA256SUMS'), checks=raw['checks'],
        current_path_keys=raw['complete_current_key_reconstruction']['complete_keys'], artifact_acceptance=False)
    assert obj(QA / 'P210_ARTIFACT03_ROOT_COMPLETION.actual.json')['result']['output'] == json.dumps(expected_summary, sort_keys=True) + '\n'
    assert raw['checks'] == accepted['initial_gate_checks'] == 5838453
    assert raw['complete_current_key_reconstruction']['canonical_map'] == accepted['complete_current_map']
    before, after = (manifest(p) for p in (HISTORY / 'PAPER_MANIFEST.sha256', PAPER / 'PAPER_MANIFEST.sha256'))
    assert len(before) == len(after) == 2244 and set(before) == set(after)
    assert {n for n in before if before[n] != after[n]} == {'ROOT_LIFECYCLE.md'}
    assert after['ROOT_LIFECYCLE.md'] == doc['current_lifecycle']['sha256']
    assert pin(HISTORY / 'ROOT_LIFECYCLE.md') == raw['pending_lifecycle_and_whole']['lifecycle']
    assert pin(HISTORY / 'PAPER_MANIFEST.sha256') == raw['pending_lifecycle_and_whole']['whole_manifest']
    assert (PAPER / 'PAPER_MANIFEST.sha256').read_bytes() == ''.join(v + '  ' + n + '\n' for n,v in sorted(after.items())).encode()
    life = (PAPER / 'ROOT_LIFECYCLE.md').read_text()
    assert life.split('\n\n', 2)[1] == doc['exact_current_status_paragraph']
    assert all(t in life for t in doc['required_current_lifecycle_tokens'])
    preserve = obj(HISTORY / 'PRESERVATION.actual.json')
    old_inputs = obj(HISTORY / 'INPUTS_BEFORE.json')
    assert old_inputs == obj(HISTORY / 'INPUTS_AFTER.json') == preserve['complete_input_pins']
    assert len(old_inputs) == 5 and len(preserve['copies']) == 2
    commands = []
    for name in ('ROOT_LIFECYCLE.md', 'PAPER_MANIFEST.sha256'):
        origin, copy = PAPER / name, HISTORY / name
        assert preserve['copies'][str(origin)] == dict(physical=str(copy), **pin(copy))
        for argv in (['/usr/bin/cp', '--no-clobber', '--', str(origin), str(copy)],
                     ['/usr/bin/cmp', '--', str(origin), str(copy)]):
            commands.append(dict(argv=argv, cwd=str(ROOT), environment=ENV, exit_code=0, stdout='', stderr=''))
    assert preserve['commands'] == commands
    direct = obj(QA / 'P210_PRECOMPLETION_CONTROLS_ROOT.actual.json')
    assert direct['result']['exit_code'] == 0 and direct['cwd'] == str(ROOT)
    assert shlex.split(direct['command']) == ['/usr/bin/python3.10', '-I', '-S', '-B', str(QA / 'preserve_p210_precompletion_controls.py')]
    assert direct['result']['output'] == json.dumps(dict(status=preserve['status'], copies=preserve['copies'],
        native_commands=commands, payloads=7, seal=doc['preserved_controls_seal']), sort_keys=True) + '\n'
    refresh = obj(QA / 'P210_COMPLETION_LIFECYCLE_REFRESH.actual.json')
    assert refresh['native'] == dict(argv=['/usr/bin/sha256sum', '--check', 'PAPER_MANIFEST.sha256'], cwd=str(PAPER),
        environment=ENV, exit=0, stdout=''.join(n + ': OK\n' for n in sorted(after)), stderr='')
    assert refresh['new_lifecycle_sha256'] == doc['current_lifecycle']['sha256']
    assert refresh['new_whole_sha256'] == doc['current_whole_manifest']['sha256']
    assert obj(QA / 'P210_COMPLETION_LIFECYCLE_REFRESH_ROOT_COMPLETION.actual.json')['result']['output'] == json.dumps(
        {k:v for k,v in refresh.items() if k != 'native'}, sort_keys=True, indent=2) + '\n'
    print(json.dumps(dict(status='PASS_SOURCE_AST_AND_NAMED_DOCUMENTARY_DATA_ONLY_NOT_LIFECYCLE_GATE',
        source=pin(source), source_lines=len(text.splitlines()), exact_six_helper_sources=inherited,
        complete_named_current_input_pins=inputs, actual_normal_native_records=normal,
        preservation_normal_native_chunk=direct['result']['chunk_id'], preservation_actual_commands=4,
        complete_old_and_new_manifest_rows=2244, only_changed_manifest_row='ROOT_LIFECYCLE.md',
        full_actual_refresh_stdout_bytes=len(refresh['native']['stdout'].encode()),
        reader_imported_or_executed=False, reader_functions_called=0, old_programs_imported_or_executed=0,
        host_tree_scans=0, paper_payload_dependency_rehashes=0, new_science_build_view_or_review=0,
        root_acceptance=False, paper_completion=False, five_paper_completion=False), sort_keys=True))

if __name__ == '__main__':
    main()
