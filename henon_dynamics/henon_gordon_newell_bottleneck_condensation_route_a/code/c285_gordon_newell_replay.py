#!/usr/bin/env python3
"""Two fresh-path byte replays for HCS-C285."""
import hashlib
import os
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CANONICAL = ROOT / "results/c285_gordon_newell_evidence.json"
payloads = []
with tempfile.TemporaryDirectory(prefix="c285-gordon-newell-replay-") as temp:
    for index in range(2):
        fresh = Path(temp) / f"independent-path-{index}" / "receipt.json"
        env = dict(os.environ)
        env["C285_EVIDENCE_OUT"] = str(fresh)
        env["PYTHONDONTWRITEBYTECODE"] = "1"
        subprocess.run([sys.executable, "-B", str(ROOT / "code/c285_gordon_newell_producer.py")],
                       env=env, check=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        env.pop("C285_EVIDENCE_OUT")
        env["C285_EVIDENCE"] = str(fresh)
        checked = subprocess.run([sys.executable, "-B", str(ROOT / "code/c285_gordon_newell_checker.py")],
                                 env=env, check=True, stdout=subprocess.PIPE,
                                 stderr=subprocess.STDOUT, text=True)
        assert "C285 independent checker: PASS" in checked.stdout
        payloads.append(fresh.read_bytes())
canonical = CANONICAL.read_bytes()
assert payloads[0] == payloads[1] == canonical
print(f"C285 double fresh-path byte replay: PASS ({len(canonical)} bytes; sha256={hashlib.sha256(canonical).hexdigest()})")
