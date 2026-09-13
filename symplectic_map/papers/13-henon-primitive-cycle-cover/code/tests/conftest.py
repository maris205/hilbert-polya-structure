from pathlib import Path
import sys

import pytest


CODE_ROOT = Path(__file__).resolve().parents[1]
PAPER_ROOT = Path(__file__).resolve().parents[2]
if CODE_ROOT.as_posix() not in sys.path:
    sys.path.insert(0, CODE_ROOT.as_posix())


@pytest.fixture(scope="session")
def paper_root():
    return PAPER_ROOT


@pytest.fixture(scope="session", autouse=True)
def _bind_junit_to_code_tree(record_testsuite_property):
    from candidate_v1.bootstrap.manifest import code_tree_sha256

    record_testsuite_property("p13_code_tree_sha256", code_tree_sha256(PAPER_ROOT))
