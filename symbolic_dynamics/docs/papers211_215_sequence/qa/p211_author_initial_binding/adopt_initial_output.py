"""Exclusive root canonical adoption after full actual initial reception."""
from hashlib import sha256
import json
import os
from pathlib import Path
import subprocess
import time

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
OUT = Path(__file__).resolve().parent
ATTEMPT = ROOT/'docs/papers211_215_sequence/qa/root_replays/p211_author_initial_01'
SOURCE = ATTEMPT/'recorder/commands/03_verify_01/stdout.raw'
TARGET = ROOT/'papers/211-kernel-image-projection-feedback/CANONICAL.json'
ENV = {'PATH': '/usr/bin:/bin', 'LANG': 'C.UTF-8', 'LC_ALL': 'C.UTF-8', 'TZ': 'UTC'}
EXPECTED = {'sha256': '2a9d1311a491805644efa7cd4884ae50ed9f9ffa48e347b822a7ff68e12ee6b4', 'bytes': 1327062}


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


assert not os.path.lexists(TARGET) and not (OUT/'ADOPTION').exists()
assert sha256((OUT/'BINDING.json').read_bytes()).hexdigest() == '8173883c5e4f2c7681e01aa4d8bda37b34e001eb7d9aef816c9ed819a9e5f987'
assert sha256((ATTEMPT/'SHA256SUMS').read_bytes()).hexdigest() == 'b350c2bdee301da6b4f34a812a23916d0b5aba9804db3deb781b42a36e10882c'
semantic_native = read(OUT/'OUTPUT_SEMANTICS_NATIVE01.json')
production_native = read(OUT/'PRODUCTION_RECORDS_NATIVE02.json')
assert semantic_native['exit_code'] == production_native['exit_code'] == 0
semantic = json.loads(semantic_native['output'])
production = json.loads(production_native['output'])
assert semantic['status'] == 'PASS_FULL_SAVED_AUTHOR_OUTPUT_SEMANTICS'
assert production['status'] == 'PASS_ROOT_COMPLETE_AUTHOR_PRODUCTION_RECORDS' and production['mode'] == 'initial'
assert {k: semantic[k] for k in EXPECTED} == EXPECTED
assert production['raw_stdout'] == [{'path': str(SOURCE), **EXPECTED}]
data = SOURCE.read_bytes()
assert identity(data) == EXPECTED
directory = OUT/'ADOPTION'
directory.mkdir()
request = {'operation': 'exclusive raw initial stdout adoption, never overwrite',
    'source': str(SOURCE), 'target': str(TARGET), 'target_lexisted_before': False,
    'approved_source': EXPECTED, 'started_epoch': time.time(),
    'semantic_native_pin': identity((OUT/'OUTPUT_SEMANTICS_NATIVE01.json').read_bytes()),
    'production_native_pin': identity((OUT/'PRODUCTION_RECORDS_NATIVE02.json').read_bytes())}
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
result = {'status': 'ROOT_CANONICAL_ADOPTED_FROM_COMPLETE_ACTUAL_INITIAL_STDOUT',
    'source': str(SOURCE), 'target': str(TARGET), **EXPECTED,
    'adoption': 'exclusive xb raw write and actual successful cmp; no normalization or prior-pilot conversion',
    'scientific_producer_invocations': 0, 'strict_pair_completed': False,
    'native_comparisons': 1, 'completed_epoch': time.time()}
write(directory/'RESULT.json', result)
files = sorted(p for p in directory.iterdir() if p.is_file())
write(directory/'SHA256SUMS', ''.join(sha256(p.read_bytes()).hexdigest()+'  '+p.name+'\n' for p in files).encode())
print(json.dumps(result, sort_keys=True))
