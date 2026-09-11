"""Root initial binding creation only. Does not invoke scientific code."""
import ast
from hashlib import sha256
import json
import math
import os
from pathlib import Path

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
QA = ROOT/'docs/papers211_215_sequence/qa'
PAPER = ROOT/'papers/211-kernel-image-projection-feedback'
OUT = Path(__file__).resolve().parent
PREP = QA/'p211_runtime_preparation'
RECEPTION = QA/'p211_runtime_root_reception'
ATTEMPT = QA/'root_replays/p211_author_initial_01'
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


assert OUT == QA/'p211_author_initial_binding'
assert not (OUT/'BINDING.json').exists() and not os.path.lexists(ATTEMPT)
assert not os.path.lexists(PAPER/'CANONICAL.json')
if not ATTEMPT.parent.exists():
    ATTEMPT.parent.mkdir()
assert ATTEMPT.parent.resolve(strict=True) == ATTEMPT.parent
source = pin(PAPER/'verify.py', '595fbf7c81f52a86192e82b663526ecb9f5abf222f6854859bfee108ff1355f8')
params_pin = pin(PAPER/'parameters.json', '8c56e641351410fb210e0462301a3321c5e2c8a036aa1a4ef8301de6419d9149')
parameters = doc(PAPER/'parameters.json')
tree = ast.parse(raw(PAPER/'verify.py'))
assert [n.names[0].name for n in tree.body if isinstance(n, ast.Import)] == ['itertools', 'json', 'math', 'sys']
assert not any(isinstance(n, ast.ImportFrom) for n in ast.walk(tree))
assert parameters['n_values'] == list(range(1, 8)) and parameters['total_states'] == 2353
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
assert doc(RECEPTION/'NATIVE02.json')['exit_code'] == 0
assert json.loads(doc(RECEPTION/'NATIVE02.json')['output'])['status'] == 'PASS_ROOT_RUNTIME_PREPARATION_RECEPTION'
assert doc(RECEPTION/'INDEPENDENT_NATIVE01.json')['exit_code'] == 0
provenance = []
source_originals = QA/'p211_author_source_reception/source_preparation_original'
selected = [source_originals/name for name in (
    'PROOF_PACKAGE.md', 'CANONICAL_SCHEMA.md', 'PARAMETER_SPECIFICATION.md', 'PREPARATION_PLAN.md',
    'SOURCE_AUDIT.md', 'CLAIMS_EVIDENCE.md', 'SOURCE_PREPARATION_MANIFEST.json')]
selected += [QA/'p211_author_source_reception/RECEPTION.md',
    PREP/'MANIFEST.sha256', PREP/'PLAN.md',
    QA/'p211_runtime_independent_audit/MANIFEST.sha256',
    RECEPTION/'RECEPTION.md', RECEPTION/'NATIVE02.json',
    RECEPTION/'INDEPENDENT_NATIVE01.json', RECEPTION/'inspect_author_output.py',
    Path(__file__).resolve()]
for path in selected:
    provenance.append({'path': str(path), **pin(path)})
predicates = parameters['predicates']
equalities = [
    {'path': ['schema'], 'value': 'p211-author-kip-v1'},
    {'path': ['parameters'], 'value': parameters},
    {'path': ['box_count'], 'value': 7}, {'path': ['total_states'], 'value': 2353}]
lengths = [{'path': ['boxes'], 'value': 7}, {'path': ['assertions'], 'value': 7}]
for index, (n, size) in enumerate(zip(parameters['n_values'], parameters['carrier_sizes'])):
    assert size == math.comb(2*n-1, n)
    for name, val in [('n', n), ('carrier_size', size), ('fixed_count', 2**(n-1)),
                      ('recurrent_count', 2**(n-1)), ('theorem_height', 0 if n == 1 else (n+1)//2)]:
        equalities.append({'path': ['boxes', index, name], 'value': val})
    for key, count in zip(predicates[:6], [size+1, size+1, size+1, size, size, size+1]):
        equalities.append({'path': ['boxes', index, 'assertions', key], 'value': count})
    lengths += [{'path': ['boxes', index, 'state_records'], 'value': size},
                {'path': ['boxes', index, 'assertions'], 'value': 7}]
deadlines = {'science': 300, 'native': 60, 'envelope': 900}
assert all(type(v) is int and 0 < v <= 900 for v in deadlines.values())
binding = {'format': 'p211-runtime-binding-v1', 'approved': True,
    'purpose': 'P211_MANUSCRIPT', 'role': 'author', 'mode': 'initial', 'attempt': str(ATTEMPT),
    'reviewed_static_source_import_closure': True, 'reviewed_schema_and_parameters': True,
    'declared_imports': ['itertools', 'json', 'math', 'sys'], 'local_helper_imports': [],
    'adapter_sources': adapter, 'runtime_lock': {'path': str(lock_path), **lock_pin},
    'entry': 'verify.py', 'parameters': 'parameters.json',
    'capsule_files': [{'name': 'verify.py', 'path': str(PAPER/'verify.py'), **source},
                      {'name': 'parameters.json', 'path': str(PAPER/'parameters.json'), **params_pin}],
    'argv_template': ['$ENTRY', '--parameters', '$PARAMETERS'], 'parameter_locator': 'explicit_absolute_argv',
    'canonical': {'path': str(PAPER/'CANONICAL.json'), 'sha256': None, 'bytes': None},
    'schema': {'top_keys': ['schema', 'parameters', 'box_count', 'total_states', 'assertions', 'checks', 'boxes'],
               'equalities': equalities, 'lengths': lengths},
    'success_stderr': 'empty', 'timeouts': deadlines, 'provenance_inputs': provenance,
    'root_execution_interface': 'pinned compile/exec within fresh adapter child, explicit main/file/argv/capsule cwd, not direct python verify.py',
    'root_canonical_policy': 'No adoption before full recorded-output and closed-attempt reception; then exclusive raw copy and native comparison.',
    'root_math_boundary': 'Same admitted two axes and original seven boxes; no old pilot conversion or claim extension.'}
for p, data in READS.items():
    assert Path(p).read_bytes() == data
write('INPUTS_AT_BINDING.json', {p: pin(p) for p in list(READS)})
write('BINDING.json', binding)
result = {'status': 'ROOT_AUTHOR_INITIAL_BINDING_READY_NOT_EXECUTED',
    'binding': {'path': str(OUT/'BINDING.json'), **pin(OUT/'BINDING.json')},
    'attempt': str(ATTEMPT), 'input_file_keys': len(READS), 'runtime_keys_checked': 122,
    'schema_equalities': len(equalities), 'schema_lengths': len(lengths),
    'scientific_source_invocations': 0, 'canonical_absent': not os.path.lexists(PAPER/'CANONICAL.json')}
write('RESULT.json', result)
print(json.dumps(result, sort_keys=True))
