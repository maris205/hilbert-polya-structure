#!/usr/bin/python3.10
"""Non-scientific, additive closure of the two already accepted root bindings."""
from hashlib import sha256
import json
import os
from pathlib import Path
import re

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
QA = ROOT / 'docs/papers211_215_sequence/qa'
HERE = Path(__file__).resolve().parent
reads = {}
checks = 0


def require(value, label):
    global checks
    checks += 1
    assert value, label


def read(path):
    p = Path(path)
    raw = p.read_bytes()
    row = {'bytes': len(raw), 'sha256': sha256(raw).hexdigest()}
    require(str(p) not in reads or reads[str(p)] == row, ('read drift', str(p)))
    reads[str(p)] = row
    return raw


def put(path, value):
    raw = value if isinstance(value, bytes) else (json.dumps(value, sort_keys=True, indent=2) + '\n').encode()
    with path.open('xb') as stream:
        stream.write(raw)
    return {'bytes': len(raw), 'sha256': sha256(raw).hexdigest()}


def manifest(base, name='SHA256SUMS'):
    rows = {}
    for line in read(base / name).decode().splitlines():
        match = re.fullmatch(r'([0-9a-f]{64})  (.+)', line)
        require(match is not None, ('manifest syntax', base, line))
        digest, rel = match.groups()
        require(rel not in rows and not Path(rel).is_absolute() and '..' not in Path(rel).parts, rel)
        require(rel != name, ('self manifest', rel))
        require(sha256(read(base / rel)).hexdigest() == digest, ('payload', rel))
        rows[rel] = digest
    actual = {str(p.relative_to(base)) for p in base.rglob('*') if p.is_file() and p != base / name}
    require(set(rows) == actual, ('complete manifest', base, set(rows) ^ actual))
    return len(rows)


require(Path.cwd() == ROOT, 'root cwd')
summary = []
for mode, accepted_name in [('initial', 'PRODUCTION_RECORDS_NATIVE02.json'), ('pair', 'PRODUCTION_RECORDS_NATIVE01.json')]:
    base = QA / ('p211_author_' + mode + '_binding')
    require(not (base / 'SHA256SUMS').exists(), ('new seal only', mode))
    inputs = json.loads(read(base / 'INPUTS_AT_BINDING.json'))
    for path, row in inputs.items():
        p = Path(path)
        read(p)
        actual = {**reads[path], 'resolved': str(p.resolve()), 'symlink': os.readlink(p) if p.is_symlink() else None}
        require(actual == row, ('exact rich binding input', path))
    result = json.loads(read(base / 'RESULT.json'))
    native = json.loads(read(base / accepted_name))
    require(native['exit_code'] == 0, ('accepted native', mode))
    reception = json.loads(native['output'])
    require(reception['status'] == 'PASS_ROOT_COMPLETE_AUTHOR_PRODUCTION_RECORDS', ('accepted status', mode))
    require(reception['binding']['sha256'] == sha256(read(base / 'BINDING.json')).hexdigest(), ('binding', mode))
    require(reception['actual_author_invocations_received'] == (1 if mode == 'initial' else 2), ('actual science count', mode))
    require(reception['actual_raw_comparisons_received'] == (0 if mode == 'initial' else 3), ('actual compare count', mode))
    require(manifest(Path(result['attempt'])) == reception['complete_payloads'], ('execution seal count', mode))
    for nested in sorted(base.rglob('SHA256SUMS')):
        manifest(nested.parent)
    before = sorted(p for p in base.rglob('*') if p.is_file())
    require(not any(p.is_symlink() for p in base.rglob('*')), ('no linked archive', mode))
    rows = [(str(p.relative_to(base)), read(p)) for p in before]
    raw = ''.join(sha256(value).hexdigest() + '  ' + rel + '\n' for rel, value in rows).encode()
    pin = put(base / 'SHA256SUMS', raw)
    require(manifest(base) == len(rows), ('new complete seal', mode))
    summary.append({'mode': mode, 'binding_inputs': len(inputs), 'payloads': len(rows), 'manifest': pin,
                    'execution_payloads': reception['complete_payloads'], 'failed_artifacts_preserved': True})
for path, row in list(reads.items()):
    raw = Path(path).read_bytes()
    require({'bytes': len(raw), 'sha256': sha256(raw).hexdigest()} == row, ('final drift', path))
put(HERE / 'INPUTS.json', reads)
result = {'status': 'ACCEPTED_AUTHOR_BINDINGS_ADDITIVELY_SEALED', 'packages': summary,
          'checks': checks, 'read_paths': len(reads), 'scientific_executions': 0,
          'new_builds_or_reviews': 0, 'historical_payloads_changed': 0}
put(HERE / 'RESULT.json', result)
print(json.dumps(result, sort_keys=True))
