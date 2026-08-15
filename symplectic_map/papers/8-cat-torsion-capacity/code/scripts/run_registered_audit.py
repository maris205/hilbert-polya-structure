"""Run the fixed registered audit; independent authority is mandatory."""

import sys

sys.dont_write_bytecode = True

from pathlib import Path


CODE_ROOT = Path(__file__).absolute().parents[1]
sys.path.insert(0, str(CODE_ROOT))

from cat_torsion.cli import main


if __name__ == "__main__":
    raise SystemExit(main(["registered", *sys.argv[1:]]))
