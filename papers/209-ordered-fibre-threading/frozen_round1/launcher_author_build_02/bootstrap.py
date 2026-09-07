#!/usr/bin/env python3
"""P209 invocation/runtime wrapper only; it does not implement mathematics."""
import json
import os
from pathlib import Path
import sys

BASE = Path(__file__).resolve().parent
OUT = BASE.parent
OPENED = set()


def audit(event, args):
    if event == "open" and isinstance(args[0], (str, bytes)):
        path = Path(os.fsdecode(args[0])).absolute()
        if path.is_file() and not str(path).startswith("/proc/"):
            OPENED.add(str(path.resolve()))


sys.addaudithook(audit)


def observe(label):
    modules = {name: {"file": getattr(module, "__file__", None),
                      "origin": getattr(getattr(module, "__spec__", None), "origin", None)}
               for name, module in sorted(sys.modules.items())}
    maps = Path("/proc/self/maps").read_text()
    mapped = sorted({str(Path(line.split(None, 5)[5]).resolve())
                     for line in maps.splitlines()
                     if len(line.split(None, 5)) == 6 and line.split(None, 5)[5].startswith("/")})
    result = {"phase": label, "modules": modules, "maps": maps,
              "mapped_files": mapped, "opened_existing_files": sorted(OPENED),
              "argv": sys.argv, "orig_argv": sys.orig_argv, "cwd": os.getcwd(),
              "env": dict(os.environ), "executable": sys.executable,
              "sys_path": sys.path, "flags": str(sys.flags),
              "optimize": sys.flags.optimize, "isolated": sys.flags.isolated,
              "no_site": sys.flags.no_site, "dont_write_bytecode": sys.dont_write_bytecode,
              "pycache_prefix": sys.pycache_prefix,
              "cache_exists": bool(sys.pycache_prefix and Path(sys.pycache_prefix).exists())}
    with (OUT / ("child." + label + ".json")).open("x") as stream:
        json.dump(result, stream, indent=2, sort_keys=True)
        stream.write("\n")


observe("before")
try:
    expected_env = {"PATH": "/usr/bin:/bin", "LANG": "C.UTF-8",
                    "LC_ALL": "C.UTF-8", "TZ": "UTC"}
    if not (sys.flags.isolated == 1 and sys.flags.no_site == 1 and
            sys.flags.optimize == 0 and sys.dont_write_bytecode and
            sys.pycache_prefix == str(OUT / "never_created_child_cache") and
            not Path(sys.pycache_prefix).exists() and dict(os.environ) == expected_env and
            Path.cwd() == OUT and sorted(p.name for p in BASE.iterdir()) == ["bootstrap.py", "verify.py"]):
        raise RuntimeError("P209_CHILD_SETTINGS_OR_CODE_ONLY_CAPSULE_FAILURE")
    program = BASE / "verify.py"
    exec(compile(program.read_bytes(), str(program), "exec"),
         {"__name__": "__main__", "__file__": str(program)})
finally:
    observe("after")
