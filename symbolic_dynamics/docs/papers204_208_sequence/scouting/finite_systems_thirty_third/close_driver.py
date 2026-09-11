#!/usr/bin/env python3
"""Append-only closure driver; no scientific producer invocation."""
import pathlib
import sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from record import ROOT, OWN, run
inputs = sorted(str(p.relative_to(ROOT)) for p in OWN.rglob('*') if p.is_file())
result = run('24_documentary_closure', [sys.executable, '-I', '-B', str((OWN / 'close.py').relative_to(ROOT))], inputs)
raise SystemExit(result.returncode)
