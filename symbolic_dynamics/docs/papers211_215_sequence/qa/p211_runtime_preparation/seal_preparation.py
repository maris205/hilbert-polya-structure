#!/usr/bin/env python3
"""Seal only this completed preparation; no scientific code is imported."""
from hashlib import sha256
import json
import os
from pathlib import Path
import subprocess
import sys

base = Path(__file__).resolve().parent
manifest = base / 'MANIFEST.sha256'
expected_env = {'PATH': '/usr/bin:/bin', 'LANG': 'C.UTF-8', 'LC_ALL': 'C.UTF-8', 'TZ': 'UTC'}
assert dict(os.environ) == expected_env and sys.flags.isolated == sys.flags.no_site == 1
assert sys.flags.optimize == 0 and sys.dont_write_bytecode
assert not manifest.exists() and not manifest.is_symlink()
assert sys.pycache_prefix == str(base / 'never_created_sealer_cache') and not Path(sys.pycache_prefix).exists()
for p in base.rglob('*'):
    assert not p.is_symlink(), str(p)
files = sorted(p for p in base.rglob('*') if p.is_file())
rows = []
total = 0
for p in files:
    data = p.read_bytes()
    total += len(data)
    rows.append(sha256(data).hexdigest() + '  ' + p.relative_to(base).as_posix() + '\n')
with manifest.open('x', encoding='ascii') as stream:
    stream.write(''.join(rows))
command = ['/usr/bin/sha256sum', '-c', 'MANIFEST.sha256']
result = subprocess.run(command, cwd=base, env=expected_env, stdin=subprocess.DEVNULL,
                        stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=30)
assert result.returncode == 0 and result.stderr == b''
assert len(result.stdout.splitlines()) == len(files) and all(line.endswith(b': OK') for line in result.stdout.splitlines())
print(json.dumps({'status': 'SEALED_AND_NATIVE_CHECKED', 'payloads': len(files), 'payload_bytes': total,
                  'manifest_sha256': sha256(manifest.read_bytes()).hexdigest(),
                  'native_check': {'argv': command, 'cwd': str(base), 'environment': expected_env,
                                   'exit': result.returncode, 'complete_stdout_bytes': len(result.stdout),
                                   'complete_stdout_sha256': sha256(result.stdout).hexdigest(),
                                   'OK_lines': len(result.stdout.splitlines()), 'stderr_bytes': len(result.stderr),
                                   'raw_final_check_streams': 'Consumed completely in memory, summarized in actual tool return; not claimed archived inside their own sealed payload.'},
                  'scientific_executions': 0}, sort_keys=True))
