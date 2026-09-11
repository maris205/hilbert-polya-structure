"""Produce and actually check a documentary nonself payload manifest."""
import hashlib
import json
from pathlib import Path
import subprocess

root = Path(__file__).resolve().parent
excluded = {"SHA256SUMS", "SEAL_CHECK.stdout", "SEAL_CHECK.stderr", "SEAL_CHECK.json"}
files = sorted(p for p in root.rglob("*") if p.is_file() and p.relative_to(root).as_posix() not in excluded)
rows = [hashlib.sha256(p.read_bytes()).hexdigest() + "  " + p.relative_to(root).as_posix() for p in files]
manifest = root / "SHA256SUMS"
manifest.write_text("\n".join(rows) + "\n")
argv = ["sha256sum", "-c", "SHA256SUMS"]
run = subprocess.run(argv, cwd=root, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False)
(root / "SEAL_CHECK.stdout").write_bytes(run.stdout)
(root / "SEAL_CHECK.stderr").write_bytes(run.stderr)
receipt = {"argv": argv, "cwd": str(root), "exit_code": run.returncode,
           "payload_count": len(files), "manifest_sha256": hashlib.sha256(manifest.read_bytes()).hexdigest(),
           "stdout_sha256": hashlib.sha256(run.stdout).hexdigest(),
           "stderr_sha256": hashlib.sha256(run.stderr).hexdigest(),
           "excluded_nonself_closure": sorted(excluded),
           "scope": "documentary payload bytes only; not independent mathematical review"}
(root / "SEAL_CHECK.json").write_text(json.dumps(receipt, indent=2) + "\n")
print(json.dumps(receipt))
raise SystemExit(run.returncode)
