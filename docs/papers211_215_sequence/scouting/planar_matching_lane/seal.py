#!/usr/bin/env python3
"""Author-only full-payload sealing; no mathematical computation or Git."""
from pathlib import Path
import hashlib
import json
import subprocess

HERE = Path(__file__).resolve().parent
ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
MANIFEST = HERE / 'MANIFEST.sha256'

if MANIFEST.exists():
    raise SystemExit('Refusing to replace an existing seal')
files = sorted(p for p in HERE.rglob('*') if p.is_file())
if any(p.is_symlink() for p in HERE.rglob('*')):
    raise SystemExit('Unexpected symlink')
rows = [(hashlib.sha256(p.read_bytes()).hexdigest(), p.relative_to(HERE).as_posix())
        for p in files]
MANIFEST.write_text(''.join(f'{digest}  {name}\n' for digest, name in rows))
for cwd, pin in [(HERE, MANIFEST), (ROOT, HERE / 'HISTORICAL_INPUT_PINS.sha256')]:
    result = subprocess.run(['/usr/bin/sha256sum', '-c', str(pin)],
                            cwd=cwd, capture_output=True)
    if result.returncode:
        raise SystemExit(result.stdout.decode() + result.stderr.decode())
    if len(result.stdout.splitlines()) != (len(files) if cwd == HERE else 6):
        raise SystemExit('Unexpected check census')
print(json.dumps({'status': 'PASS_AUTHOR_ARTIFACT_ONLY', 'payloads': len(files),
                  'payload_bytes': sum(p.stat().st_size for p in files),
                  'historical_pins': 6, 'science': 0,
                  'manifest_sha256': hashlib.sha256(MANIFEST.read_bytes()).hexdigest()}))
