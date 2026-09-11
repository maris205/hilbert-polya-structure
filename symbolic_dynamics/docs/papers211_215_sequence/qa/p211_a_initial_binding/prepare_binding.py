"""Root A-only initial binding. Author binding mechanics reused, no science run."""
import ast
from hashlib import sha256
import json
import math
import os
from pathlib import Path

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
QA = ROOT/'docs/papers211_215_sequence/qa'
REVIEW = ROOT/'docs/papers211_215_sequence/reviews/p211_a'
OUT = Path(__file__).resolve().parent
PREP = QA/'p211_runtime_preparation'
RECEPTION = QA/'p211_a_root_reception'
ATTEMPT = QA/'root_replays/p211_a_initial_01'
READS = {}


def raw(path):
    path = Path(path)
    data = path.read_bytes()
    if str(path) in READS:
        assert READS[str(path)] == data
    READS[str(path)] = data
    return data


def pin(path, expected=None):
    path = Path(path)
    data = raw(path)
    row = {'sha256': sha256(data).hexdigest(), 'bytes': len(data),
           'resolved': str(path.resolve(strict=True)),
           'symlink': os.readlink(path) if path.is_symlink() else None}
    if expected is not None:
        expected = {'sha256': expected} if isinstance(expected, str) else expected
        assert all(row[k] == expected[k] for k in row if k in expected), str(path)
    return row


def doc(path):
    return json.loads(raw(path))


def write(name, value):
    with (OUT/name).open('xb') as stream:
        stream.write((json.dumps(value, sort_keys=True, indent=2, allow_nan=False)+'\n').encode())


assert OUT == QA/'p211_a_initial_binding'
assert not (OUT/'BINDING.json').exists() and not os.path.lexists(ATTEMPT)
assert not os.path.lexists(REVIEW/'CANONICAL.json')
assert ATTEMPT.parent.resolve(strict=True) == ATTEMPT.parent
source = pin(REVIEW/'verify.py', '35140051d98c1adcc14ca0041407f1a07a0488bb40a9962fa586ac517c0a389a')
params_pin = pin(REVIEW/'parameters.json', 'a12bcbda054a0a6a8cfc6ebd774e70ff8df4318dd7d902e0724a6d84212e78cc')
parameters = doc(REVIEW/'parameters.json')
tree = ast.parse(raw(REVIEW/'verify.py'))
assert [n.names[0].name for n in tree.body if isinstance(n, ast.Import)] == ['itertools', 'json', 'math', 'sys']
assert not any(isinstance(n, ast.ImportFrom) for n in ast.walk(tree))
assert parameters['n_values'] == list(range(1, 8)) and parameters['expected_total_vertices'] == 2353
for node in tree.body:
    if isinstance(node, ast.Assign) and isinstance(node.targets[0], ast.Name) and node.targets[0].id == 'EXPECTED_PARAMETERS':
        assert ast.literal_eval(node.value) == parameters
        break
else:
    raise AssertionError('missing exact source parameter contract')
lock_path = PREP/'discovery02/RUNTIME_LOCK.json'
lock_pin = pin(lock_path, '1499a93909e39b49c16408985053936b7eb7efcf664e91fd75fa77de607be2ab')
lock = doc(lock_path)
assert len(lock['files']) == 122
for path, row in lock['files'].items():
    pin(path, row)
adapter = {str(PREP/name): pin(PREP/name, expected) for name, expected in (
    ('runtime_core.py', '2fd41cfac779f8d5f4e23089fcc9f2b6b041cbebe19e7003b2db6b4815909934'),
    ('p211_runtime.py', 'bff2dcf25ee846b04eac0bbd46eb7b3e58c728c6d7e8e9ce591c9cef1ae4e421'))}
native = doc(RECEPTION/'PREPARATION_NATIVE01.json')
assert native['result']['exit_code'] == 0
received = doc(RECEPTION/'PREPARATION_RESULT.json')
assert json.loads(native['result']['output']) == received
assert received['status'] == 'PASS_ROOT_A_PREPARATION_ORIGINALS' and received['payloads'] == 20
assert doc(RECEPTION/'BUILD_REUSE_NATIVE01.json')['result']['exit_code'] == 0
pin(REVIEW/'PREPARATION_SHA256SUMS', '67b61e77cca2195f264902e54fedb5688ca39d1c3b649282f3306c1172519a07')
provenance_paths = set()
for path, expected in doc(RECEPTION/'PREPARATION_READ_INPUTS.json').items():
    pin(path, expected)
    provenance_paths.add(path)
for name in ('inspect_production.py', 'inspect_saved_output.py', 'REUSE_SCOPE.md',
             'ADAPTER_DIFF_NATIVE.json', 'ADAPTER_COPY_NATIVE.json', 'BUILD_REUSE_NATIVE01.json',
             'PREPARATION_RESULT.json', 'PREPARATION_READ_INPUTS.json', 'PREPARATION_NATIVE01.json',
             'PREPARATION_RECEPTION.md', 'NAVIGATION_LIMITS.md'):
    provenance_paths.add(str(RECEPTION/name))
for path in (QA/'p211_author_initial_binding/prepare_binding.py',
             QA/'p211_runtime_root_reception/RECEPTION.md', PREP/'MANIFEST.sha256',
             QA/'p211_runtime_independent_audit/MANIFEST.sha256',
             ROOT/'docs/papers211_215_sequence/P211_REVIEW_CONTRACT.md', Path(__file__).resolve()):
    provenance_paths.add(str(path))
provenance = [{'path': path, **pin(path)} for path in sorted(provenance_paths)]
equalities = [
    {'path': ['schema'], 'value': 'p211-a-complete-graph-v1'},
    {'path': ['role'], 'value': 'P211_REVIEW_A'},
    {'path': ['parameters'], 'value': parameters},
    {'path': ['total_vertices'], 'value': 2353}, {'path': ['total_targets'], 'value': 2353},
    {'path': ['total_edges'], 'value': 2353},
    {'path': ['verdict'], 'value': 'FINITE_GRAPH_CHECKS_PASS'},
    {'path': ['scope'], 'value': 'n=1..7 finite counterexample pressure only; not an all-n proof or manuscript acceptance'}]
lengths = [{'path': ['carriers'], 'value': 7}]
for index, n in enumerate(parameters['n_values']):
    size = math.comb(2*n-1, n)
    for key, value in (('n', n), ('vertex_count', size), ('height', 0 if n == 1 else (n+1)//2),
                       ('height_prediction', 0 if n == 1 else (n+1)//2)):
        equalities.append({'path': ['carriers', index, key], 'value': value})
    lengths.extend([{'path': ['carriers', index, 'rows'], 'value': size},
                    {'path': ['carriers', index, 'cycles'], 'value': 2**(n-1)},
                    {'path': ['carriers', index, 'reverse_breadth_first_order'], 'value': size}])
deadlines = {'science': 300, 'native': 60, 'envelope': 900}
assert all(type(v) is int and 0 < v <= 900 for v in deadlines.values())
binding = {'format': 'p211-runtime-binding-v1', 'approved': True,
    'purpose': 'P211_MANUSCRIPT', 'role': 'A', 'mode': 'initial', 'attempt': str(ATTEMPT),
    'reviewed_static_source_import_closure': True, 'reviewed_schema_and_parameters': True,
    'declared_imports': ['itertools', 'json', 'math', 'sys'], 'local_helper_imports': [],
    'adapter_sources': adapter, 'runtime_lock': {'path': str(lock_path), **lock_pin},
    'entry': 'verify.py', 'parameters': 'parameters.json',
    'capsule_files': [{'name': 'verify.py', 'path': str(REVIEW/'verify.py'), **source},
                      {'name': 'parameters.json', 'path': str(REVIEW/'parameters.json'), **params_pin}],
    'argv_template': ['$ENTRY', '--parameters', '$PARAMETERS'], 'parameter_locator': 'explicit_absolute_argv',
    'canonical': {'path': str(REVIEW/'CANONICAL.json'), 'sha256': None, 'bytes': None},
    'schema': {'top_keys': ['schema', 'role', 'parameters', 'carriers', 'total_vertices', 'total_targets',
                           'total_edges', 'check_total', 'verdict', 'scope'],
               'equalities': equalities, 'lengths': lengths},
    'success_stderr': 'empty', 'timeouts': deadlines, 'provenance_inputs': provenance,
    'root_execution_interface': 'pinned compile/exec within fresh adapter child, explicit main/file/argv/capsule cwd, not direct python verify.py',
    'root_canonical_policy': 'No adoption before full recorded-output and closed-attempt reception; then exclusive raw copy and native comparison.',
    'root_math_boundary': 'Independent A whole literal graph and target atlas, same admitted two axes and original seven carriers; no source import during preparation.',
    'root_infrastructure_reuse': 'Accepted unchanged runtime supports role A; binding mechanics and record inspector disclosed author-infrastructure adaptations, not independent scientific code.'}
for path, data in READS.items():
    assert Path(path).read_bytes() == data
write('INPUTS_AT_BINDING.json', {path: pin(path) for path in list(READS)})
write('BINDING.json', binding)
result = {'status': 'ROOT_A_INITIAL_BINDING_READY_NOT_EXECUTED',
    'binding': {'path': str(OUT/'BINDING.json'), **pin(OUT/'BINDING.json')},
    'attempt': str(ATTEMPT), 'input_file_keys': len(READS), 'runtime_keys_checked': 122,
    'schema_equalities': len(equalities), 'schema_lengths': len(lengths),
    'scientific_source_invocations': 0, 'canonical_absent': not os.path.lexists(REVIEW/'CANONICAL.json')}
write('RESULT.json', result)
print(json.dumps(result, sort_keys=True))
