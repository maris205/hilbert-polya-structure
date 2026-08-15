"""Build the strict post-run result manifest from any working directory."""

import sys

sys.dont_write_bytecode = True

from pathlib import Path


CODE_ROOT = Path(__file__).absolute().parents[1]
sys.path.insert(0, str(CODE_ROOT))

from base2_clock.cli import main


if __name__ == "__main__":
    raise SystemExit(main(["post-manifest", *sys.argv[1:]]))
