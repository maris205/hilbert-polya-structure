"""Root separately approves a canonical-pinned pair after initial reception."""
from hashlib import sha256
import json
import os
from pathlib import Path

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
QA = ROOT/'docs/papers211_215_sequence/qa'
OUT = Path(__file__).resolve().parent
INITIAL = QA/'p211_author_initial_binding'
ATTEMPT = QA/'root_replays/p211_author_pair_01'
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
        assert all(result[k] == expected[k] for k in result if k in expected), str(path)
    return result


def doc(path):
    return json.loads(raw(path))


def write(name, value):
    with (OUT/name).open('xb') as stream:
        stream.write((json.dumps(value, sort_keys=True, indent=2, allow_nan=False)+'\n').encode())


assert OUT == QA/'p211_author_pair_binding' and not (OUT/'BINDING.json').exists()
assert not os.path.lexists(ATTEMPT) and ATTEMPT.parent.resolve(strict=True) == ATTEMPT.parent
old_bytes = raw(INITIAL/'BINDING.json')
assert sha256(old_bytes).hexdigest() == '8173883c5e4f2c7681e01aa4d8bda37b34e001eb7d9aef816c9ed819a9e5f987'
old = json.loads(old_bytes)
binding = json.loads(old_bytes)
assert old['approved'] is True and old['role'] == 'author' and old['mode'] == 'initial'
for row in doc(INITIAL/'INPUTS_AT_BINDING.json').items():
    pin(*row)
for name, status in [('PRODUCTION_RECORDS_NATIVE02.json', 'PASS_ROOT_COMPLETE_AUTHOR_PRODUCTION_RECORDS'),
                     ('OUTPUT_SEMANTICS_NATIVE01.json', 'PASS_FULL_SAVED_AUTHOR_OUTPUT_SEMANTICS'),
                     ('ADOPTION_NATIVE01.json', 'ROOT_CANONICAL_ADOPTED_FROM_COMPLETE_ACTUAL_INITIAL_STDOUT')]:
    native = doc(INITIAL/name)
    assert native['exit_code'] == 0 and json.loads(native['output'])['status'] == status
adoption = doc(INITIAL/'ADOPTION/RESULT.json')
canonical = Path(old['canonical']['path'])
canonical_pin = pin(canonical, adoption)
assert canonical_pin['sha256'] == '2a9d1311a491805644efa7cd4884ae50ed9f9ffa48e347b822a7ff68e12ee6b4'
assert canonical_pin['bytes'] == 1327062 and raw(canonical) == raw(adoption['source'])
semantics = json.loads(doc(INITIAL/'OUTPUT_SEMANTICS_NATIVE01.json')['output'])
binding['mode'], binding['attempt'] = 'pair', str(ATTEMPT)
binding['canonical'] = {'path': str(canonical), **canonical_pin}
binding['schema']['equalities'] += [
    {'path': ['assertions'], 'value': semantics['author_assertions']},
    {'path': ['checks'], 'value': semantics['author_checks']}]
for path in [INITIAL/name for name in ('BINDING.json', 'PRODUCTION_RECORDS_NATIVE02.json',
            'OUTPUT_SEMANTICS_NATIVE01.json', 'ADOPTION_NATIVE01.json', 'ADOPTION/RESULT.json')]+[Path(__file__).resolve()]:
    binding['provenance_inputs'].append({'path': str(path), **pin(path)})
binding['root_canonical_policy'] = 'Existing accepted canonical is immutable; compare each full stdout to it and the two stdout files to each other; never publish or replace.'
assert all(type(v) is int and 0 < v <= 900 for v in binding['timeouts'].values())
changed = {key: {'before': old[key], 'after': binding[key]} for key in old if old[key] != binding[key]}
assert set(changed) == {'mode', 'attempt', 'canonical', 'schema', 'provenance_inputs', 'root_canonical_policy'}
for path, data in READS.items():
    assert Path(path).read_bytes() == data
write('INPUTS_AT_BINDING.json', {p: pin(p) for p in list(READS)})
write('BINDING.json', binding)
write('EXACT_INITIAL_TO_PAIR_DELTA.json', changed)
result = {'status': 'ROOT_AUTHOR_STRICT_PAIR_BINDING_APPROVED_NOT_EXECUTED',
    'binding': {'path': str(OUT/'BINDING.json'), **pin(OUT/'BINDING.json')},
    'attempt': str(ATTEMPT), 'canonical': {'path': str(canonical), **canonical_pin},
    'changed_top_keys': sorted(changed), 'input_keys_checked': len(READS),
    'new_scientific_invocations': 0, 'required_scientific_invocations': 2,
    'required_native_canonical_pair_comparisons': 3}
write('RESULT.json', result)
print(json.dumps(result, sort_keys=True))
