"""Root exclusive B canonical adoption; accepted author adoption mechanics reused."""
from hashlib import sha256
import json
import os
from pathlib import Path
import subprocess
import time

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
OUT = Path(__file__).resolve().parent
ATTEMPT = ROOT/'docs/papers211_215_sequence/qa/root_replays/p211_b_initial_01'
SOURCE = ATTEMPT/'recorder/commands/03_verify_01/stdout.raw'
TARGET = ROOT/'docs/papers211_215_sequence/reviews/p211_b/CANONICAL.json'
ENV = {'PATH': '/usr/bin:/bin', 'LANG': 'C.UTF-8', 'LC_ALL': 'C.UTF-8', 'TZ': 'UTC'}
EXPECTED = {'sha256': '10daa982cc755162b09c4e1e4783343f4ea25ca4c464e2123693e2156b810658', 'bytes': 3053387}


def identity(data):
    return {'sha256': sha256(data).hexdigest(), 'bytes': len(data)}


def read(path):
    return json.loads(Path(path).read_bytes())


def write(path, value):
    data = value if isinstance(value, bytes) else (json.dumps(value, sort_keys=True, indent=2)+'\n').encode()
    with Path(path).open('xb') as stream:
        stream.write(data)
        stream.flush()
        os.fsync(stream.fileno())


assert OUT == ROOT/'docs/papers211_215_sequence/qa/p211_b_initial_binding'
assert not os.path.lexists(TARGET) and not (OUT/'ADOPTION').exists()
assert sha256((OUT/'BINDING.json').read_bytes()).hexdigest() == 'ba7f9fb4b13b236d189be61da87860f802e478d9d91e17dd6e2368812c9099ed'
assert sha256((ATTEMPT/'SHA256SUMS').read_bytes()).hexdigest() == 'eac19aad71c6c9385e110670954d48f055939bf1d8d6efe6108da81375d1f0ff'
RECEPTION = ROOT/'docs/papers211_215_sequence/qa/p211_b_root_reception'
semantic_native = read(RECEPTION/'INITIAL_SEMANTIC_NATIVE01.json')
production_native = read(RECEPTION/'INITIAL_RUNTIME_NATIVE01.json')
def received(record):
    parts = [record['result']] + [r['result'] for r in record.get('polls', [])]
    assert parts[-1]['exit_code'] == 0 and not parts[-1].get('session_id')
    return json.loads(''.join(r['output'] for r in parts))
semantic, production = received(semantic_native), received(production_native)
assert semantic['status'] == 'PASS_FULL_SAVED_B_OUTPUT_SEMANTICS'
assert production['status'] == 'PASS_ROOT_COMPLETE_B_PRODUCTION_RECORDS' and production['mode'] == 'initial'
assert {key: semantic['saved_stdout'][key] for key in EXPECTED} == EXPECTED
assert production['raw_stdout'] == [{'path': str(SOURCE), **EXPECTED}]
assert semantic['saved_B_check_total'] == 32766 and production['actual_B_invocations_received'] == 1
data = SOURCE.read_bytes()
assert identity(data) == EXPECTED
directory = OUT/'ADOPTION'
directory.mkdir()
request = {'operation': 'exclusive raw initial B stdout adoption, never overwrite',
    'source': str(SOURCE), 'target': str(TARGET), 'target_lexisted_before': False,
    'approved_source': EXPECTED, 'started_epoch': time.time(),
    'semantic_native_pin': identity((RECEPTION/'INITIAL_SEMANTIC_NATIVE01.json').read_bytes()),
    'production_native_pin': identity((RECEPTION/'INITIAL_RUNTIME_NATIVE01.json').read_bytes())}
write(directory/'ADOPTION_ATTEMPT.json', request)
write(TARGET, data)
assert TARGET.read_bytes() == SOURCE.read_bytes() == data
command = {'argv': ['/usr/bin/cmp', '--', str(SOURCE), str(TARGET)],
    'cwd': str(ROOT), 'environment': ENV, 'stdin': 'DEVNULL', 'timeout_seconds': 30,
    'started_epoch': time.time(), 'operation': 'actual complete raw byte comparison'}
write(directory/'CMP_ATTEMPT.json', command)
native = subprocess.run(command['argv'], cwd=ROOT, env=ENV, stdin=subprocess.DEVNULL,
                        stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=30)
write(directory/'cmp.stdout.raw', native.stdout)
write(directory/'cmp.stderr.raw', native.stderr)
receipt = {**command, 'ended_epoch': time.time(), 'exit_code': native.returncode,
           'stdout': identity(native.stdout), 'stderr': identity(native.stderr)}
write(directory/'CMP_RECEIPT.json', receipt)
assert native.returncode == 0 and native.stdout == native.stderr == b''
assert identity(TARGET.read_bytes()) == EXPECTED and SOURCE.read_bytes() == data
result = {'status': 'ROOT_B_CANONICAL_ADOPTED_FROM_COMPLETE_ACTUAL_INITIAL_STDOUT',
    'source': str(SOURCE), 'target': str(TARGET), **EXPECTED,
    'adoption': 'exclusive xb raw write and actual successful cmp; no normalization or prior-pilot conversion',
    'infrastructure': 'accepted author adoption mechanics adapted to exact B pins and statuses',
    'scientific_producer_invocations': 0, 'strict_pair_completed': False,
    'native_comparisons': 1, 'completed_epoch': time.time()}
write(directory/'RESULT.json', result)
files = sorted(path for path in directory.iterdir() if path.is_file())
write(directory/'SHA256SUMS', ''.join(sha256(path.read_bytes()).hexdigest()+'  '+path.name+'\n' for path in files).encode())
print(json.dumps(result, sort_keys=True))
