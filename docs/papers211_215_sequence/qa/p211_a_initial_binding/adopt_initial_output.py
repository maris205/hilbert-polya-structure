"""Root exclusive A canonical adoption; accepted author adoption mechanics reused."""
from hashlib import sha256
import json
import os
from pathlib import Path
import subprocess
import time

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
OUT = Path(__file__).resolve().parent
ATTEMPT = ROOT/'docs/papers211_215_sequence/qa/root_replays/p211_a_initial_01'
SOURCE = ATTEMPT/'recorder/commands/03_verify_01/stdout.raw'
TARGET = ROOT/'docs/papers211_215_sequence/reviews/p211_a/CANONICAL.json'
ENV = {'PATH': '/usr/bin:/bin', 'LANG': 'C.UTF-8', 'LC_ALL': 'C.UTF-8', 'TZ': 'UTC'}
EXPECTED = {'sha256': 'e637aa186b5d11c3bba1ad5318d42c7dc93ea736fee9ed3013ebcc1beaa9cd43', 'bytes': 1313394}


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


assert OUT == ROOT/'docs/papers211_215_sequence/qa/p211_a_initial_binding'
assert not os.path.lexists(TARGET) and not (OUT/'ADOPTION').exists()
assert sha256((OUT/'BINDING.json').read_bytes()).hexdigest() == '8f019e9cc35ba0c0d3ed02d9b419f844acc09f0df83ae8aeff590811463b5f0f'
assert sha256((ATTEMPT/'SHA256SUMS').read_bytes()).hexdigest() == '91570ff70f06a60f1190ab64c4593505580880b572266941494a61eaf7bc3375'
semantic_native = read(OUT/'OUTPUT_SEMANTICS_NATIVE01.json')
production_native = read(OUT/'PRODUCTION_RECORDS_NATIVE01.json')
assert semantic_native['exit_code'] == production_native['exit_code'] == 0
semantic = json.loads(semantic_native['output'])
production = json.loads(production_native['output'])
assert semantic['status'] == 'PASS_FULL_SAVED_A_OUTPUT_SEMANTICS'
assert production['status'] == 'PASS_ROOT_COMPLETE_A_PRODUCTION_RECORDS' and production['mode'] == 'initial'
assert {key: semantic[key] for key in EXPECTED} == EXPECTED
assert production['raw_stdout'] == [{'path': str(SOURCE), **EXPECTED}]
assert semantic['actual_A_check_total'] == 30951 and production['actual_A_invocations_received'] == 1
data = SOURCE.read_bytes()
assert identity(data) == EXPECTED
directory = OUT/'ADOPTION'
directory.mkdir()
request = {'operation': 'exclusive raw initial A stdout adoption, never overwrite',
    'source': str(SOURCE), 'target': str(TARGET), 'target_lexisted_before': False,
    'approved_source': EXPECTED, 'started_epoch': time.time(),
    'semantic_native_pin': identity((OUT/'OUTPUT_SEMANTICS_NATIVE01.json').read_bytes()),
    'production_native_pin': identity((OUT/'PRODUCTION_RECORDS_NATIVE01.json').read_bytes())}
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
result = {'status': 'ROOT_A_CANONICAL_ADOPTED_FROM_COMPLETE_ACTUAL_INITIAL_STDOUT',
    'source': str(SOURCE), 'target': str(TARGET), **EXPECTED,
    'adoption': 'exclusive xb raw write and actual successful cmp; no normalization or prior-pilot conversion',
    'infrastructure': 'accepted author adoption mechanics adapted to exact A pins and statuses',
    'scientific_producer_invocations': 0, 'strict_pair_completed': False,
    'native_comparisons': 1, 'completed_epoch': time.time()}
write(directory/'RESULT.json', result)
files = sorted(path for path in directory.iterdir() if path.is_file())
write(directory/'SHA256SUMS', ''.join(sha256(path.read_bytes()).hexdigest()+'  '+path.name+'\n' for path in files).encode())
print(json.dumps(result, sort_keys=True))
