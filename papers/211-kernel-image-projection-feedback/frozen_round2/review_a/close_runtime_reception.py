"""Close A's saved-runtime evidence keys only; no scientific or native invocation."""
from hashlib import sha256
import json
import os
from pathlib import Path
import re

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
QA = ROOT/'docs/papers211_215_sequence/qa'
HERE = ROOT/'docs/papers211_215_sequence/reviews/p211_a'
OUT = HERE/'evidence/runtime_closure01'
READS = {}
CHECKS = 0


def need(ok, label):
    global CHECKS
    CHECKS += 1
    if not ok:
        raise AssertionError(label)


def read(path):
    path = Path(path)
    body = path.read_bytes()
    need(str(path) not in READS or READS[str(path)] == body, ('unchanged read', str(path)))
    READS[str(path)] = body
    return body


def identity(body):
    return {'sha256': sha256(body).hexdigest(), 'bytes': len(body)}


def pin(path, expected=None):
    path = Path(path)
    row = {**identity(read(path)), 'resolved': str(path.resolve(strict=True)),
           'symlink': os.readlink(path) if path.is_symlink() else None}
    if expected is not None:
        expected = {'sha256': expected} if isinstance(expected, str) else expected
        need(all(row[key] == value for key, value in expected.items()), ('complete expected pin', str(path)))
    return row


def unique(pairs):
    result = {}
    for key, value in pairs:
        need(key not in result, ('duplicate JSON key', key))
        result[key] = value
    return result


def doc(path):
    return json.loads(read(path), object_pairs_hook=unique)


def check_list(path, base, population):
    rows = {}
    for line in read(path).decode().splitlines():
        match = re.fullmatch(r'([0-9a-f]{64})  (.+)', line)
        need(match is not None, ('pin line syntax', str(path)))
        digest, name = match.groups()
        need(not Path(name).is_absolute() and '..' not in Path(name).parts and name not in rows,
             ('safe unique input name', name))
        pin(base/name, digest)
        rows[name] = digest
    need(len(rows) == population, ('entire input population', str(path)))
    return rows


need(Path.cwd() == ROOT and not os.path.lexists(OUT), 'owned new closure only')
read(__file__)
pin(HERE/'receive_runtime_records.py', '192bd77ab4c29683ca3b181e2602ca633a4507d8768719be16e7181348104308')
pin(HERE/'PREPARATION_SHA256SUMS', '67b61e77cca2195f264902e54fedb5688ca39d1c3b649282f3306c1172519a07')
preparation = check_list(HERE/'PREPARATION_SHA256SUMS', HERE, 20)
frozen = check_list(HERE/'INPUT_PINS.sha256', ROOT, 33)
external = check_list(HERE/'EXTERNAL_READ_PINS.sha256', ROOT, 32)
freeze = ROOT/'papers/211-kernel-image-projection-feedback/frozen_round0'
expected_freeze = check_list(freeze/'SHA256SUMS', freeze, 32)
need({p.relative_to(freeze).as_posix() for p in freeze.rglob('*') if p.is_file()}
     == set(expected_freeze)|{'SHA256SUMS'}, 'complete unchanged physical Round0 membership')
need(not any(p.is_symlink() for p in freeze.rglob('*')), 'physical Round0 remains unlinked')
received = []
for mode in ('initial', 'pair'):
    folder = HERE/'evidence'/('runtime_'+mode+'_reception01')
    result = doc(folder/'RESULT.json')
    native = doc(HERE/'evidence'/('RUNTIME_'+mode.upper()+'_RECEPTION_NATIVE01.json'))
    parts = [native['result']]+[p['result'] for p in native['polls']]
    need(parts[-1]['exit_code'] == 0 and not parts[-1].get('session_id'), 'actual settled own receiver')
    printed = json.loads(''.join(p['output'] for p in parts))
    need(printed['status'] == result['status'] == 'PASS_A_REVIEWER_RUNTIME_ORIGINAL_RECEPTION'
         and printed['mode'] == result['mode'] == mode
         and printed['checks'] == result['checks']
         and printed['actual_read_paths'] == result['actual_read_paths']
         and printed['result_sha256'] == identity(read(folder/'RESULT.json'))['sha256'],
         'complete actual own tool/result correspondence')
    inputs = doc(folder/'READ_INPUTS.json')
    need(len(inputs) == result['actual_read_paths'], 'whole own consumed input key')
    for path, expected in inputs.items():
        need(pin(path, expected) == expected, ('all unchanged rich receipt inputs', path))
    need(result['new_scientific_producer_invocations'] == result['new_builds']
         == result['new_native_commands_from_receiver'] == 0, 'read-only receiver boundary')
    received.append({'mode': mode, 'checks': result['checks'], 'read_paths': len(inputs),
                     'payloads': result['complete_payloads'], 'native_commands': result['native_commands'],
                     'binding_inputs': result['binding_original_inputs']})
root_closure = QA/'p211_a_binding_closure'
root_inputs = doc(root_closure/'INPUTS.json')
need(len(root_inputs) == 441, 'complete original root closure key')
for path, expected in root_inputs.items():
    pin(path, expected)
root_result = doc(root_closure/'RESULT.json')
need(root_result['status'] == 'ACCEPTED_A_BINDINGS_ADDITIVELY_SEALED'
     and root_result['read_paths'] == 441 and root_result['checks'] == 2305
     and root_result['historical_payloads_changed'] == root_result['scientific_executions'] == 0,
     'actual accepted original root closure scope')
root_native = doc(root_closure/'NATIVE01.json')
need(root_native['exit_code'] == 0 and json.loads(root_native['output']) == root_result,
     'entire root closure native result')
read(root_closure/'close.py')
read(QA/'P211_A_RUNTIME_RECEPTION.md')
read(HERE/'RUNTIME_RECEPTION_SCOPE.md')
canonical = HERE/'CANONICAL.json'
canonical_pin = pin(canonical, {'sha256': 'e637aa186b5d11c3bba1ad5318d42c7dc93ea736fee9ed3013ebcc1beaa9cd43',
                               'bytes': 1313394})
raw_pairs = []
for mode, count in (('initial', 1), ('pair', 2)):
    for index in range(1, count+1):
        path = QA/('root_replays/p211_a_'+mode+'_01')/'recorder/commands'/('03_verify_'+str(index).zfill(2))/'stdout.raw'
        need(read(path) == read(canonical), 'new whole raw saved-output/canonical equality')
        raw_pairs.append({'source': str(path), 'target': str(canonical), 'comparison': 'whole bytes in this receiver, not a new native cmp'})
key = {path: {**identity(body), 'resolved': str(Path(path).resolve(strict=True)),
              'symlink': os.readlink(path) if Path(path).is_symlink() else None}
       for path, body in sorted(READS.items())}
for path, expected in key.items():
    need(pin(path) == expected, ('complete closure key unchanged', path))
result = {'status': 'PASS_A_REVIEWER_COMPLETE_RUNTIME_KEY_CLOSURE', 'checks': CHECKS,
          'read_paths': len(key), 'preparation_payloads_unchanged': len(preparation),
          'frozen_inputs_unchanged': len(frozen), 'external_inputs_unchanged': len(external),
          'own_received_packages': received, 'root_original_closure_inputs': len(root_inputs),
          'canonical': canonical_pin, 'whole_raw_equalities': raw_pairs,
          'new_scientific_producers': 0, 'new_builds': 0, 'new_page_views': 0,
          'scope': 'Complete original runtime/binding/received-output key recheck and immutable preparation; no science, build, semantic recomputation or delta acceptance.'}
OUT.mkdir()
for name, value in (('READ_INPUTS.json', key), ('RESULT.json', result)):
    with (OUT/name).open('xb') as stream:
        stream.write((json.dumps(value, sort_keys=True, indent=2, allow_nan=False)+'\n').encode())
print(json.dumps({'status': result['status'], 'checks': result['checks'], 'read_paths': len(key),
                  'result_sha256': sha256((OUT/'RESULT.json').read_bytes()).hexdigest()}, sort_keys=True))
