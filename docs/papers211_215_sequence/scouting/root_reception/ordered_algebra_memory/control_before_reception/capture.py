"""Preserve exact two live navigation controls before a documentary refresh."""
from hashlib import sha256
import json
import os
from pathlib import Path
import subprocess
import time

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
OUT = Path(__file__).resolve().parent
ENV = {'PATH': '/usr/bin:/bin', 'LANG': 'C.UTF-8', 'LC_ALL': 'C.UTF-8', 'TZ': 'UTC'}


def pin(data):
    return {'bytes': len(data), 'sha256': sha256(data).hexdigest()}


def put(path, value):
    body = value if isinstance(value, bytes) else (json.dumps(value, sort_keys=True, indent=2)+'\n').encode()
    with path.open('xb') as stream:
        stream.write(body)


assert OUT == ROOT/'docs/papers211_215_sequence/scouting/root_reception/ordered_algebra_memory/control_before_reception'
originals = OUT/'originals'
assert not os.path.lexists(originals)
originals.mkdir()
records, mapping = [], []
for source in (ROOT/'SYMBOLIC_DYNAMICS_STATE.md', ROOT/'docs/papers211_215_sequence/PIPELINE_STATE.md'):
    data = source.read_bytes()
    target = originals/source.name
    assert not os.path.lexists(target)
    for label, argv in (('copy_'+source.name, ['/usr/bin/cp', '--', str(source), str(target)]),
                        ('cmp_'+source.name, ['/usr/bin/cmp', '--', str(source), str(target)])):
        request = {'label': label, 'argv': argv, 'cwd': str(ROOT), 'environment': ENV,
                   'stdin': 'DEVNULL', 'timeout_seconds': 30, 'started_epoch': time.time()}
        put(OUT/(label+'.ATTEMPT.json'), request)
        result = subprocess.run(argv, cwd=ROOT, env=ENV, stdin=subprocess.DEVNULL,
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=30)
        put(OUT/(label+'.stdout.raw'), result.stdout)
        put(OUT/(label+'.stderr.raw'), result.stderr)
        receipt = {**request, 'ended_epoch': time.time(), 'exit_code': result.returncode,
                   'stdout': pin(result.stdout), 'stderr': pin(result.stderr)}
        put(OUT/(label+'.RECEIPT.json'), receipt)
        records.append(receipt)
        assert result.returncode == 0 and result.stdout == result.stderr == b''
    assert source.read_bytes() == target.read_bytes() == data
    mapping.append({'logical_path': str(source), 'physical_original': str(target), 'pin': pin(data)})
put(OUT/'MAPPING.json', mapping)
result = {'status': 'EXACT_TWO_PRE_41_CLOSED_CONTROLS_PHYSICALLY_PRESERVED',
          'actual_native_commands': records, 'mapping': mapping, 'scientific_executions': 0}
put(OUT/'RESULT.json', result)
print(json.dumps(result, sort_keys=True))
