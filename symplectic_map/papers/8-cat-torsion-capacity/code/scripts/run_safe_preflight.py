"""Run safe P0--P3 from any working directory without importing candidate code."""

import sys

sys.dont_write_bytecode = True

from pathlib import Path


CODE_ROOT = Path(__file__).absolute().parents[1]
sys.path.insert(0, str(CODE_ROOT))

from cat_torsion.cli import main


if __name__ == "__main__":
    raise SystemExit(main(["safe-preflight", *sys.argv[1:]]))
