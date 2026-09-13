#!/usr/bin/env python3
"""P32 entrypoint for the shared audit-only Stage-4.5 failure finalizer."""

from __future__ import annotations

import importlib.util
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
MASTER = (
    ROOT
    / "papers"
    / "29-bianchi-ideal-owner-refinement"
    / "notes"
    / "stage4_5_round2_finalize_translation_status_failure.py"
)


def load_master():
    spec = importlib.util.spec_from_file_location("stage4_5_round2_failure_master", MASTER)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {MASTER}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


if __name__ == "__main__":
    module = load_master()
    raise SystemExit(module.main())
