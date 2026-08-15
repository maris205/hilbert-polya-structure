from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).absolute().parents[1]))

from centralizer_q.cli import main

raise SystemExit(main(["safe-preflight"]))
