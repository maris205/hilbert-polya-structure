"""Shared command-line helpers for non-overwriting JSON artifacts."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys
from typing import Mapping


PROJECT_ROOT = Path(__file__).resolve().parents[2]
CODE_ROOT = Path(__file__).resolve().parents[1]
if str(CODE_ROOT) not in sys.path:
    sys.path.insert(0, str(CODE_ROOT))


def output_path(value: str) -> Path:
    path = Path(value)
    if not path.is_absolute():
        path = PROJECT_ROOT / path
    return path


def write_json_new(path: Path, payload: Mapping) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    try:
        with path.open("x", encoding="utf-8") as handle:
            json.dump(payload, handle, indent=2, sort_keys=True)
            handle.write("\n")
    except FileExistsError as exc:
        raise SystemExit(f"Refusing to overwrite existing output: {path}") from exc


def add_output_argument(parser: argparse.ArgumentParser, default: str) -> None:
    parser.add_argument(
        "--output",
        default=default,
        help="New JSON output path, relative to the project root unless absolute",
    )
