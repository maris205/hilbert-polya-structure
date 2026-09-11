#!/usr/bin/env python3
"""Fresh Round-0 verifier/build capture. Never overwrites a frozen snapshot."""
from hashlib import sha256
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys

paper = Path(__file__).resolve().parents[1]
attempt = sys.argv[1] if len(sys.argv) > 1 else "attempt1"
if not attempt.isalnum():
    raise SystemExit("attempt name must be alphanumeric")
base = paper / "qa_round0" / attempt
base.mkdir(parents=True, exist_ok=False)
env = os.environ.copy()
env.update(SOURCE_DATE_EPOCH="1704067200", TZ="UTC", PYTHONDONTWRITEBYTECODE="1")


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


canonical = (paper / "code/CANONICAL.txt").read_bytes()
for run in (1, 2):
    result = subprocess.run([sys.executable, "code/verify.py"], cwd=paper,
                            env=env, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    (base / f"verifier{run}.stdout").write_bytes(result.stdout)
    (base / f"verifier{run}.stderr").write_bytes(result.stderr)
    if result.returncode or result.stderr or result.stdout != canonical:
        raise SystemExit(f"verifier{run} failed or differs from canonical")
    print(f"VERIFIER{run}=BYTE_IDENTICAL", flush=True)

pdfs = []
for run in (1, 2):
    build = base / f"build{run}"
    build.mkdir()
    for filename in ("main.tex", "references.bib"):
        shutil.copy2(paper / filename, build / filename)
    commands = [
        ["pdflatex", "-interaction=nonstopmode", "-halt-on-error", "main.tex"],
        ["bibtex", "main"],
        ["pdflatex", "-interaction=nonstopmode", "-halt-on-error", "main.tex"],
        ["pdflatex", "-interaction=nonstopmode", "-halt-on-error", "main.tex"],
    ]
    for index, command in enumerate(commands, 1):
        result = subprocess.run(command, cwd=build, env=env,
                                stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        (build / f"pass{index}.stdout").write_bytes(result.stdout)
        if result.returncode:
            print(result.stdout.decode(errors="replace")[-5000:])
            raise SystemExit(f"build{run} pass{index} failed")
    log = (build / "main.log").read_text(errors="replace")
    for forbidden in ("There were undefined references", "Citation `", "Reference `", "! LaTeX Error"):
        if forbidden in log:
            raise SystemExit(f"unresolved build warning: {forbidden}")
    pdfs.append(build / "main.pdf")
    print(f"BUILD{run}={digest(pdfs[-1])}", flush=True)
if pdfs[0].read_bytes() != pdfs[1].read_bytes():
    raise SystemExit("cold PDFs differ")

frozen = paper / "round0_frozen"
frozen.mkdir(exist_ok=False)
(frozen / "code").mkdir()
for filename in ("main.tex", "references.bib", "code/verify.py", "code/CANONICAL.txt", "code/build_round0.py"):
    shutil.copy2(paper / filename, frozen / filename)
shutil.copy2(pdfs[0], frozen / "main.pdf")
for filename in ("main.pdf", "main_round0_original.pdf"):
    if (paper / filename).exists():
        raise SystemExit(f"refusing to replace {filename}")
    shutil.copy2(pdfs[0], paper / filename)
pins = {str(p.relative_to(frozen)): digest(p)
        for p in sorted(frozen.rglob("*")) if p.is_file()}
(frozen / "SHA256SUMS").write_text("".join(f"{value}  {key}\n" for key, value in pins.items()))
receipt = {"status": "ROUND0_AUTHOR_REPLAY_AND_BUILD_PASS",
           "review_A": "NOT_RUN", "review_B": "NOT_RUN",
           "external": "HOLD_EXTERNAL", "pdf_sha256": digest(pdfs[0]),
           "canonical_sha256": sha256(canonical).hexdigest(), "frozen_inputs": pins}
(base / "RECEIPT.json").write_text(json.dumps(receipt, indent=2) + "\n")
print("ROUND0_FROZEN / AWAITING_DUAL_REVIEW / HOLD_EXTERNAL")
