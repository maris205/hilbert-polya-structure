#!/usr/bin/python3.10
"""Receive same-auditor delta originals; no submitted execution/import."""
from hashlib import sha256
import json
from pathlib import Path
import re

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
QA = ROOT / 'docs/papers211_215_sequence/qa'
BASE = QA / 'p211_build_independent_delta01'
OUT = Path(__file__).resolve().parent
reads, checks = {}, 0


def check(value, label):
    global checks
    if not value:
        raise AssertionError(label)
    checks += 1


def pin(raw):
    return {'bytes': len(raw), 'sha256': sha256(raw).hexdigest()}


def read(path):
    path = Path(path)
    raw = path.read_bytes()
    value = pin(raw)
    check(str(path) not in reads or reads[str(path)] == value, ('drift', str(path)))
    reads[str(path)] = value
    return raw


def data(path):
    return json.loads(read(path))


manifest = read(BASE / 'SHA256SUMS')
check(pin(manifest) == {'bytes': 4415, 'sha256': 'd10158393bed3383299e93f079ff939b578912e86c8c564e8ef1c7bd9b3cd24e'}, 'exact independent manifest')
names = set()
for line in manifest.decode().splitlines():
    m = re.fullmatch(r'([a-f0-9]{64})  (.+)', line)
    check(m is not None, 'manifest syntax')
    digest, name = m.groups()
    check(name not in names and name != 'SHA256SUMS' and not Path(name).is_absolute() and '..' not in Path(name).parts, 'nonself unique safe path')
    names.add(name)
    check(pin(read(BASE / name))['sha256'] == digest, 'full payload pin')
check(len(names) == 49 and {p.relative_to(BASE).as_posix() for p in BASE.rglob('*') if p.is_file()} == names | {'SHA256SUMS'}, 'complete 49 payloads')
inputs = data(BASE / 'READ_INPUTS_BEFORE.json')
check(inputs == data(BASE / 'READ_INPUTS_AFTER.json') and len(inputs) == 353, 'complete 353 read key')
for path, value in inputs.items():
    check(pin(read(path)) == value, ('exact original referent', path))
result = data(BASE / 'RESULT.json')
actual = data(BASE / 'TOOL_RETURN.actual.json')['returned']
check(actual['exit_code'] == 0 and json.loads(actual['output']) == result, 'entire actual tool-body binding')
check(result['status'] == 'BLD_I1_RESOLVED_FOR_REVISION01_PENDING_EXACT_ROOT_BINDING' and result['new_concrete_blockers'] == [] and
      result['candidate']['pin'] == pin(read(QA / 'p211_build_revision01/discovery01/DEPENDENCY_LOCK.candidate.json')), 'exact revised verdict scope')
for attempt in sorted((BASE / 'native').glob('*/ATTEMPT.json')):
    a, r = data(attempt), data(attempt.with_name('RECEIPT.json'))
    check(all(r[k] == v for k, v in a.items()) and r['native_exit_code'] in a['expected_exit_codes'], 'real comparison argv and exit')
    for s in ('stdout', 'stderr'):
        check(pin(read(attempt.with_name(s + '.raw'))) == r[s], 'full comparison raw bytes')
    if r['argv'][0] == '/usr/bin/cmp':
        check(read(r['argv'][1]) == read(r['argv'][2]), 'physical full byte-pair equality')
    else:
        name = Path(r['argv'][-1]).name
        saved = QA / 'p211_build_revision01/diagnostic_capture01/commands' / ('diff_' + name.replace('.', '_'))
        check(read(saved / 'stdout.raw') == read(attempt.with_name('stdout.raw')) and
              data(saved / 'RECEIPT.json')['native_exit_code'] == r['native_exit_code'], 'entire saved/fresh native delta equality')
for path, value in reads.items():
    check(pin(Path(path).read_bytes()) == value, 'all independent inputs unchanged')
summary = {'status': 'ROOT_ACCEPTS_SAME_AUDITOR_BLD_I1_REVISION01_DELTA', 'checks': checks,
           'read_paths': len(reads), 'payloads': len(names), 'independent_inputs': len(inputs),
           'scientific_executions': 0, 'builds': 0, 'submitted_code_evaluations': 0,
           'original_report': 'Major/open unchanged for original version', 'root_binding': 'NEXT_SEPARATE_ACTION'}
for name, row in [('INDEPENDENT_DELTA_INPUTS.json', reads), ('INDEPENDENT_DELTA_RESULT.json', summary)]:
    with (OUT / name).open('xb') as f:
        f.write((json.dumps(row, sort_keys=True, indent=2) + '\n').encode())
print(json.dumps(summary, sort_keys=True))
