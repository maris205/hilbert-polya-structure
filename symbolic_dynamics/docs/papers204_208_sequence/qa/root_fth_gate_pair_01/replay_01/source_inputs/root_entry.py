"""Invocation-only wrapper; sealed bootstrap executes the sealed kernel."""
import json
import os
from pathlib import Path
import sys
base = Path(__file__).resolve().parent
def record(label):
    value = {"argv": sys.argv, "orig_argv": sys.orig_argv,
             "cwd": os.getcwd(), "env": dict(os.environ),
             "executable": sys.executable, "flags": str(sys.flags),
             "optimize": sys.flags.optimize, "isolated": sys.flags.isolated,
             "no_site": sys.flags.no_site,
             "dont_write_bytecode": sys.flags.dont_write_bytecode,
             "pycache_prefix": sys.pycache_prefix,
             "cache_exists": bool(sys.pycache_prefix and Path(sys.pycache_prefix).exists())}
    with (base.parent / ("child.invocation." + label + ".json")).open("x") as output:
        json.dump(value, output, indent=2, sort_keys=True)
        output.write("\n")
record("before")
try:
    bootstrap = base / "bootstrap.py"
    exec(compile(bootstrap.read_bytes(), str(bootstrap), "exec"),
         {"__name__": "__main__", "__file__": str(bootstrap)})
finally:
    record("after")
