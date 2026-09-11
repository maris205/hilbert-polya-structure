"""Additively seal accepted A bindings; explicit accepted author-closure reuse."""
from hashlib import sha256
import json
import os
from pathlib import Path
import re

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
QA = ROOT/'docs/papers211_215_sequence/qa'
HERE = Path(__file__).resolve().parent
reads = {}
checks = 0


def require(value, label):
    global checks
    checks += 1
    assert value, label


def read(path):
    path = Path(path)
    raw = path.read_bytes()
    row = {'bytes': len(raw), 'sha256': sha256(raw).hexdigest()}
    require(str(path) not in reads or reads[str(path)] == row, ('read drift', str(path)))
    reads[str(path)] = row
    return raw


def put(path, value):
    raw = value if isinstance(value, bytes) else (json.dumps(value, sort_keys=True, indent=2)+'\n').encode()
    with path.open('xb') as stream:
        stream.write(raw)
    return {'bytes': len(raw), 'sha256': sha256(raw).hexdigest()}


def manifest(base):
    rows = {}
    for line in read(base/'SHA256SUMS').decode().splitlines():
        match = re.fullmatch(r'([0-9a-f]{64})  (.+)', line)
        require(match is not None, ('manifest syntax', base, line))
        digest, rel = match.groups()
        require(rel not in rows and not Path(rel).is_absolute() and '..' not in Path(rel).parts and rel != 'SHA256SUMS', rel)
        require(sha256(read(base/rel)).hexdigest() == digest, ('payload', rel))
        rows[rel] = digest
    actual = {str(path.relative_to(base)) for path in base.rglob('*') if path.is_file() and path != base/'SHA256SUMS'}
    require(set(rows) == actual, ('complete manifest', base, set(rows)^actual))
    return len(rows)


require(Path.cwd() == ROOT, 'root cwd')
read(__file__)
read(QA/'p211_author_binding_closure/close.py')
summary = []
for mode in ('initial', 'pair'):
    base = QA/('p211_a_'+mode+'_binding')
    require(not (base/'SHA256SUMS').exists(), ('new seal only', mode))
    inputs = json.loads(read(base/'INPUTS_AT_BINDING.json'))
    for path, row in inputs.items():
        path_obj = Path(path)
        read(path)
        actual = {**reads[path], 'resolved': str(path_obj.resolve()), 'symlink': os.readlink(path_obj) if path_obj.is_symlink() else None}
        require(actual == row, ('every exact rich binding input', path))
    result = json.loads(read(base/'RESULT.json'))
    native = json.loads(read(base/'PRODUCTION_RECORDS_NATIVE01.json'))
    require(native['exit_code'] == 0, ('accepted native', mode))
    reception = json.loads(native['output'])
    require(reception['status'] == 'PASS_ROOT_COMPLETE_A_PRODUCTION_RECORDS', ('accepted A status', mode))
    require(reception['binding']['sha256'] == sha256(read(base/'BINDING.json')).hexdigest(), ('binding', mode))
    require(reception['actual_A_invocations_received'] == (1 if mode == 'initial' else 2), ('actual science count', mode))
    require(reception['actual_raw_comparisons_received'] == (0 if mode == 'initial' else 3), ('actual compare count', mode))
    require(manifest(Path(result['attempt'])) == reception['complete_payloads'], ('execution seal count', mode))
    for nested in sorted(base.rglob('SHA256SUMS')):
        manifest(nested.parent)
    before = sorted(path for path in base.rglob('*') if path.is_file())
    require(not any(path.is_symlink() for path in base.rglob('*')), ('no linked archive', mode))
    rows = [(str(path.relative_to(base)), read(path)) for path in before]
    require(len(rows) == (17 if mode == 'initial' else 10), 'exact current payload population')
    raw = ''.join(sha256(value).hexdigest()+'  '+rel+'\n' for rel, value in rows).encode()
    pin = put(base/'SHA256SUMS', raw)
    require(manifest(base) == len(rows), ('new complete seal', mode))
    summary.append({'mode': mode, 'binding_inputs': len(inputs), 'payloads': len(rows), 'manifest': pin,
                    'execution_payloads': reception['complete_payloads'], 'all_original_bytes_unchanged': True})
for path, row in list(reads.items()):
    raw = Path(path).read_bytes()
    require({'bytes': len(raw), 'sha256': sha256(raw).hexdigest()} == row, ('full final read-set drift', path))
put(HERE/'INPUTS.json', reads)
result = {'status': 'ACCEPTED_A_BINDINGS_ADDITIVELY_SEALED', 'packages': summary,
          'checks': checks, 'read_paths': len(reads), 'scientific_executions': 0,
          'new_builds_or_reviews': 0, 'historical_payloads_changed': 0,
          'reuse': 'Accepted author closure structure, explicit A roles/statuses and 17/10 population; no changed old auditor.'}
put(HERE/'RESULT.json', result)
print(json.dumps(result, sort_keys=True))
