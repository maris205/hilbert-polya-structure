#!/usr/bin/env python3
"""P32 entrypoint for the shared, audit-only Stage-4.5 Round-2 builder."""

from __future__ import annotations

import importlib.util
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
IMPLEMENTATION = (
    ROOT
    / "papers/29-bianchi-ideal-owner-refinement/notes/stage4_5_round2_build_audit.py"
)


def main() -> int:
    spec = importlib.util.spec_from_file_location("round10_p29_p32_stage45_round2", IMPLEMENTATION)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {IMPLEMENTATION}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.main(["--paper", "P32"])


if __name__ == "__main__":
    raise SystemExit(main())
