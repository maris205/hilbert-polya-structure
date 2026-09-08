#!/usr/bin/env python3
"""Create the immutable nonself author-handoff seal and native-check it; no overwrites."""
import hashlib
from pathlib import Path
import subprocess

paper = Path(__file__).resolve().parent
manifest = paper / "SHA256SUMS"
files = sorted(path for path in paper.rglob("*") if path.is_file() and path != manifest)
rows = []
for path in files:
    rows.append(hashlib.sha256(path.read_bytes()).hexdigest() + "  " + str(path.relative_to(paper)))
with manifest.open("x") as stream:
    stream.write("\n".join(rows) + "\n")
result = subprocess.run(["/usr/bin/sha256sum", "-c", "SHA256SUMS"], cwd=paper, capture_output=True, check=False)
print(result.stdout.decode(), end="")
print(result.stderr.decode(), end="")
print("payload_count", len(files))
print("manifest_sha256", hashlib.sha256(manifest.read_bytes()).hexdigest())
print("native_exit", result.returncode)
raise SystemExit(result.returncode)
