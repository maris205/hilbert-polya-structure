#!/usr/bin/env python3
"""Re-run the C115 producer in isolation and demand byte identity."""
from __future__ import annotations

from hashlib import sha256
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

PROJECT = Path(__file__).resolve().parents[1]
PRODUCER = PROJECT / "code/c115_mcmillan_producer.py"
EVIDENCE = PROJECT / "results/c115_mcmillan_evidence.json"


def main() -> None:
    expected = EVIDENCE.read_bytes()
    with tempfile.TemporaryDirectory(prefix="c115-replay-") as temporary:
        root = Path(temporary) / "package"
        (root / "code").mkdir(parents=True)
        (root / "results").mkdir()
        copy = root / "code/c115_mcmillan_producer.py"
        shutil.copy2(PRODUCER, copy)
        process = subprocess.run([sys.executable, str(copy)], text=True, capture_output=True)
        if process.returncode != 0:
            raise RuntimeError(process.stderr)
        actual = (root / "results/c115_mcmillan_evidence.json").read_bytes()
    if actual != expected:
        raise AssertionError("isolated producer replay is not byte-identical")
    print("C115_REPLAY_PASS", sha256(expected).hexdigest())


if __name__ == "__main__":
    main()
