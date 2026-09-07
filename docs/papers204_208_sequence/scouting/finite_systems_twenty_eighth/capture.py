#!/usr/bin/env python3
"""Transparent, non-hermetic command and physical-input capture for this lane."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
from datetime import datetime, timezone

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
LANE = ROOT / 'docs/papers204_208_sequence/scouting/finite_systems_twenty_eighth'

def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def pin(p):
    p = Path(p)
    if not p.is_absolute(): p = ROOT / p
    return {'path': str(p), 'exists': p.exists(), **({'sha256': digest(p), 'bytes': p.stat().st_size} if p.is_file() else {})}

def snapshot(name, paths):
    out = LANE / 'history' / name
    out.mkdir(parents=True, exist_ok=False)
    rows = []
    for raw in paths:
        p = Path(raw)
        if not p.is_absolute(): p = ROOT / p
        before = pin(p)
        target = out / (str(p.relative_to(ROOT)) if p.is_relative_to(ROOT) else 'external/' + str(p).lstrip('/'))
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(p, target)
        rows.append({'before': before, 'physical_copy': str(target.relative_to(LANE)), 'copy': pin(target), 'after': pin(p)})
    (out / 'PIN_MANIFEST.json').write_text(json.dumps({'utc': datetime.now(timezone.utc).isoformat(), 'files': rows}, indent=2) + '\n')

def command(name, argv, pins):
    out = LANE / 'commands' / name
    out.mkdir(parents=True, exist_ok=False)
    meta = {'argv': argv, 'cwd': str(ROOT), 'utc_before': datetime.now(timezone.utc).isoformat(), 'pins_before': [pin(p) for p in pins], 'capture_runtime': {'python_executable': sys.executable, 'python_version': sys.version, 'nonhermetic': True}}
    (out / 'invocation.json').write_text(json.dumps(meta, indent=2) + '\n')
    result = subprocess.run(argv, cwd=ROOT, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False)
    (out / 'stdout.txt').write_bytes(result.stdout)
    (out / 'stderr.txt').write_bytes(result.stderr)
    meta.update({'utc_after': datetime.now(timezone.utc).isoformat(), 'exit_code': result.returncode, 'pins_after': [pin(p) for p in pins], 'stdout_sha256': digest(out / 'stdout.txt'), 'stderr_sha256': digest(out / 'stderr.txt')})
    (out / 'result.json').write_text(json.dumps(meta, indent=2) + '\n')
    sys.stdout.buffer.write(result.stdout)
    sys.stderr.buffer.write(result.stderr)
    return result.returncode

if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest='mode', required=True)
    sn = sub.add_parser('snapshot'); sn.add_argument('name'); sn.add_argument('paths', nargs='+')
    cmd = sub.add_parser('command'); cmd.add_argument('name'); cmd.add_argument('--pin', action='append', default=[]); cmd.add_argument('argv', nargs=argparse.REMAINDER)
    args = ap.parse_args()
    if args.mode == 'snapshot': snapshot(args.name, args.paths)
    else: sys.exit(command(args.name, args.argv[1:] if args.argv[0] == '--' else args.argv, args.pin))
