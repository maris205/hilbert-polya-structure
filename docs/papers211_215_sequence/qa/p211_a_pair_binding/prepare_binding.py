"""Root A strict-pair approval after exact initial adoption; no science run."""
from hashlib import sha256
import json
import os
from pathlib import Path

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
QA = ROOT/'docs/papers211_215_sequence/qa'
OUT = Path(__file__).resolve().parent
INITIAL = QA/'p211_a_initial_binding'
ATTEMPT = QA/'root_replays/p211_a_pair_01'
READS = {}


def raw(path):
    path = Path(path)
    data = path.read_bytes()
    if str(path) in READS:
        assert READS[str(path)] == data
    READS[str(path)] = data
    return data


def identity(data):
    return {'sha256': sha256(data).hexdigest(), 'bytes': len(data)}


def pin(path, expected=None):
    path = Path(path)
    result = {**identity(raw(path)), 'resolved': str(path.resolve(strict=True)),
              'symlink': os.readlink(path) if path.is_symlink() else None}
    if expected is not None:
        assert all(result[key] == expected[key] for key in result if key in expected), str(path)
    return result


def doc(path):
    return json.loads(raw(path))


def write(name, value):
    with (OUT/name).open('xb') as stream:
        stream.write((json.dumps(value, sort_keys=True, indent=2, allow_nan=False)+'\n').encode())


assert OUT == QA/'p211_a_pair_binding' and not (OUT/'BINDING.json').exists()
assert not os.path.lexists(ATTEMPT) and ATTEMPT.parent.resolve(strict=True) == ATTEMPT.parent
old_bytes = raw(INITIAL/'BINDING.json')
assert sha256(old_bytes).hexdigest() == '8f019e9cc35ba0c0d3ed02d9b419f844acc09f0df83ae8aeff590811463b5f0f'
old = json.loads(old_bytes)
binding = json.loads(old_bytes)
assert old['approved'] is True and old['role'] == 'A' and old['mode'] == 'initial'
for row in doc(INITIAL/'INPUTS_AT_BINDING.json').items():
    pin(*row)
for name, status in [('PRODUCTION_RECORDS_NATIVE01.json', 'PASS_ROOT_COMPLETE_A_PRODUCTION_RECORDS'),
                     ('OUTPUT_SEMANTICS_NATIVE01.json', 'PASS_FULL_SAVED_A_OUTPUT_SEMANTICS'),
                     ('ADOPTION_NATIVE01.json', 'ROOT_A_CANONICAL_ADOPTED_FROM_COMPLETE_ACTUAL_INITIAL_STDOUT')]:
    native = doc(INITIAL/name)
    assert native['exit_code'] == 0 and json.loads(native['output'])['status'] == status
adoption = doc(INITIAL/'ADOPTION/RESULT.json')
canonical = Path(old['canonical']['path'])
canonical_pin = pin(canonical, adoption)
assert canonical_pin['sha256'] == 'e637aa186b5d11c3bba1ad5318d42c7dc93ea736fee9ed3013ebcc1beaa9cd43'
assert canonical_pin['bytes'] == 1313394 and raw(canonical) == raw(adoption['source'])
adoption_files = []
for line in raw(INITIAL/'ADOPTION/SHA256SUMS').decode().splitlines():
    digest, name = line.split('  ', 1)
    assert name != 'SHA256SUMS' and not Path(name).is_absolute() and '..' not in Path(name).parts
    pin(INITIAL/'ADOPTION'/name, {'sha256': digest})
    adoption_files.append(name)
assert len(adoption_files) == 6 and sorted(adoption_files+['SHA256SUMS']) == sorted(path.name for path in (INITIAL/'ADOPTION').iterdir())
comparison = doc(INITIAL/'ADOPTION/CMP_RECEIPT.json')
assert comparison['argv'] == ['/usr/bin/cmp', '--', adoption['source'], str(canonical)]
assert comparison['exit_code'] == 0 and comparison['cwd'] == str(ROOT)
assert comparison['environment'] == {'PATH': '/usr/bin:/bin', 'LANG': 'C.UTF-8', 'LC_ALL': 'C.UTF-8', 'TZ': 'UTC'}
assert doc(INITIAL/'ADOPTION/CMP_ATTEMPT.json') == {key: comparison[key] for key in doc(INITIAL/'ADOPTION/CMP_ATTEMPT.json')}
for name in ('stdout', 'stderr'):
    body = raw(INITIAL/'ADOPTION'/('cmp.'+name+'.raw'))
    assert body == b'' and identity(body) == comparison[name]
transcript = doc(canonical)
binding['mode'], binding['attempt'] = 'pair', str(ATTEMPT)
binding['canonical'] = {'path': str(canonical), **canonical_pin}
binding['schema']['equalities'].append({'path': ['check_total'], 'value': 30951})
for index, carrier in enumerate(transcript['carriers']):
    binding['schema']['equalities'].extend([
        {'path': ['carriers', index, 'check_counts'], 'value': carrier['check_counts']},
        {'path': ['carriers', index, 'check_total'], 'value': carrier['check_total']}])
additions = [INITIAL/name for name in ('BINDING.json', 'INPUTS_AT_BINDING.json',
            'PRODUCTION_RECORDS_NATIVE01.json', 'OUTPUT_SEMANTICS_NATIVE01.json',
            'PRODUCTION_TOOL_INVOCATION.json', 'ADOPTION_NATIVE01.json', 'adopt_initial_output.py')]
additions += list((INITIAL/'ADOPTION').iterdir())
additions += [Path(__file__).resolve(), QA/'p211_author_pair_binding/prepare_binding.py']
for path in sorted(additions):
    binding['provenance_inputs'].append({'path': str(path), **pin(path)})
binding['root_canonical_policy'] = 'Existing accepted A canonical is immutable; compare each full stdout to it and the two stdout files to each other; never publish or replace.'
assert all(type(value) is int and 0 < value <= 900 for value in binding['timeouts'].values())
changed = {key: {'before': old[key], 'after': binding[key]} for key in old if old[key] != binding[key]}
assert set(changed) == {'mode', 'attempt', 'canonical', 'schema', 'provenance_inputs', 'root_canonical_policy'}
for path, data in READS.items():
    assert Path(path).read_bytes() == data
write('INPUTS_AT_BINDING.json', {path: pin(path) for path in list(READS)})
write('BINDING.json', binding)
write('EXACT_INITIAL_TO_PAIR_DELTA.json', changed)
result = {'status': 'ROOT_A_STRICT_PAIR_BINDING_APPROVED_NOT_EXECUTED',
    'binding': {'path': str(OUT/'BINDING.json'), **pin(OUT/'BINDING.json')},
    'attempt': str(ATTEMPT), 'canonical': {'path': str(canonical), **canonical_pin},
    'changed_top_keys': sorted(changed), 'input_keys_checked': len(READS),
    'new_scientific_invocations': 0, 'required_scientific_invocations': 2,
    'required_native_canonical_pair_comparisons': 3,
    'infrastructure_reuse': 'accepted author strict-pair binding mechanics adapted to exact A schema and pins; all initial source/environment/schema contracts retained'}
write('RESULT.json', result)
print(json.dumps(result, sort_keys=True))
