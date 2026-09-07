"""Run only the committed independent kernel; record actual runtime evidence."""
import json
import os
from pathlib import Path
import sys

opened = set()


def audit(event, args):
    if event == "open" and isinstance(args[0], (str, bytes)):
        path = os.fsdecode(args[0])
        if os.path.isfile(path):
            opened.add(str(Path(path).resolve()))


sys.addaudithook(audit)
base = Path(__file__).resolve().parent
try:
    if not (sys.flags.isolated and sys.flags.no_site and sys.flags.dont_write_bytecode
            and sys.flags.optimize == 0 and sys.pycache_prefix
            and not Path(sys.pycache_prefix).exists()):
        raise RuntimeError("ISOLATION_SETTINGS_FAILURE")
    kernel = base / "kernel_v0.py"
    exec(compile(kernel.read_bytes(), str(kernel), "exec"),
         {"__name__": "__main__", "__file__": str(kernel)})
finally:
    modules = {name: {"file": getattr(module, "__file__", None),
                      "origin": getattr(getattr(module, "__spec__", None), "origin", None)}
               for name, module in sorted(sys.modules.items())}
    maps = Path("/proc/self/maps").read_text()
    mapped = sorted({str(Path(line.split()[-1]).resolve()) for line in maps.splitlines()
                     if "/" in line and Path(line.split()[-1]).is_file()})
    result = {"modules": modules, "mapped_files": mapped, "opened_existing_files": sorted(opened),
              "sys_executable": sys.executable, "sys_path": sys.path,
              "flags": str(sys.flags), "optimization": sys.flags.optimize,
              "isolated": sys.flags.isolated, "no_site": sys.flags.no_site,
              "dont_write_bytecode": sys.flags.dont_write_bytecode,
              "pycache_prefix": sys.pycache_prefix,
              "cache_exists_after": Path(sys.pycache_prefix).exists(), "maps": maps}
    (base.parent / "child.observed.json").write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
