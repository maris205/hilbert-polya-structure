"""Safe development fixtures: imports only, never registered engine dispatch."""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest


sys.dont_write_bytecode = True
PROJECT_ROOT = Path(__file__).absolute().parents[2]
CANDIDATE_ROOT = PROJECT_ROOT / "code/candidate_v1"
sys.path.insert(0, str(CANDIDATE_ROOT))


def _load_science_module(track: str):
    path = CANDIDATE_ROOT / track / "engine.py"
    spec = importlib.util.spec_from_file_location("paper12_" + track + "_safe_test", path)
    if spec is None or spec.loader is None:
        raise RuntimeError("could not create safe engine import specification")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="session")
def q_engine():
    return _load_science_module("track_q")


@pytest.fixture(scope="session")
def r_engine():
    return _load_science_module("track_r")
