#!/usr/bin/env python3
"""Fresh-path byte replay for HCS-C291 evidence."""
from __future__ import annotations

import hashlib
import os
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PRODUCER = ROOT / "code/c291_dimer_rsa_producer.py"
REFERENCE = ROOT / "results/c291_dimer_rsa_evidence.json"


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def build(path: Path) -> bytes:
    env = dict(os.environ)
    env.update({"PYTHONDONTWRITEBYTECODE": "1", "TZ": "UTC"})
    # The producer owns a package-relative output, so replay a fresh copied
    # package skeleton rather than redirecting to the release evidence path.
    root = path / "package"
    (root / "code").mkdir(parents=True)
    copied = root / "code/c291_dimer_rsa_producer.py"
    copied.write_bytes(PRODUCER.read_bytes())
    subprocess.run([sys.executable, "-B", str(copied)], env=env, check=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    return (root / "results/c291_dimer_rsa_evidence.json").read_bytes()


def main() -> None:
    with tempfile.TemporaryDirectory(prefix="c291-replay-a-") as a, tempfile.TemporaryDirectory(prefix="c291-replay-b-") as b:
        first = build(Path(a))
        second = build(Path(b))
    reference = REFERENCE.read_bytes()
    assert first == second == reference
    print(f"C291 fresh-path byte replay: PASS sha256={digest(reference)} bytes={len(reference)}")


if __name__ == "__main__":
    main()
