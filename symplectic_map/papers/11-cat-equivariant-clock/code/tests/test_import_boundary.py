import os
import subprocess
import sys
from pathlib import Path


def test_preclaim_import_graph_stays_science_free() -> None:
    root = Path(__file__).parents[2]
    script = r'''
import sys
import tempfile
from pathlib import Path

import equivariant_clock.cli as cli
import equivariant_clock.gates as gates
import equivariant_clock.manifest
import equivariant_clock.review
from equivariant_clock.constants import CODE_REVIEW_PATH, PREEXECUTION_AUDIT_PATH, PREEXECUTION_TEST_PATH
from equivariant_clock.lifecycle import claim_registered_run
from equivariant_clock.protocol import sha256_file

science = {
    "equivariant_clock.candidate",
    "equivariant_clock.invariants",
    "equivariant_clock.finite_module",
    "equivariant_clock.cyclic_cset",
}
assert science.isdisjoint(sys.modules)
gates.collect_safe_preflight(Path(sys.argv[1]))
assert science.isdisjoint(sys.modules)
with tempfile.TemporaryDirectory() as temporary:
    fake = Path(temporary)
    (fake / "results").mkdir()
    for relative in (CODE_REVIEW_PATH, PREEXECUTION_AUDIT_PATH, PREEXECUTION_TEST_PATH):
        path = fake / relative
        path.write_text(relative + "\n", encoding="utf-8")
    claim_registered_run(
        fake,
        reviewed_code_sha256="a" * 64,
        review_file_sha256=sha256_file(fake / CODE_REVIEW_PATH),
        preflight_sha256=sha256_file(fake / PREEXECUTION_AUDIT_PATH),
    )
    assert science.isdisjoint(sys.modules)
    cli.load_postclaim_science(fake, "a" * 64)
    assert science.issubset(sys.modules)
'''
    environment = dict(os.environ)
    environment["PYTHONDONTWRITEBYTECODE"] = "1"
    completed = subprocess.run(
        [sys.executable, "-c", script, str(root)],
        cwd=Path(__file__).parents[1],
        env=environment,
        capture_output=True,
        text=True,
        check=False,
    )
    assert completed.returncode == 0, completed.stdout + completed.stderr
