"""Author instrumentation, not independent scientific verification or an OS trace."""
import sys
import os

reads, imports = set(), set()


def audit(event, args):
    if event == "import":
        imports.add(str(args[0]))
    if event == "open" and isinstance(args[0], (str, bytes)):
        mode, flags = args[1:3]
        if (isinstance(mode, str) and "r" in mode) or (isinstance(flags, int) and not flags & (os.O_WRONLY | os.O_RDWR)):
            reads.add(os.path.abspath(os.fsdecode(args[0])))


sys.addaudithook(audit)
import json
import runpy

target, destination = sys.argv[1:3]
maps_before = open("/proc/self/maps").read()
settings = dict(executable=sys.executable, version=sys.version, flags=str(sys.flags),
                path=sys.path[:], xoptions=sys._xoptions, environment=dict(os.environ))
try:
    sys.argv = [target] + sys.argv[3:]
    runpy.run_path(target, run_name="__main__")
finally:
    maps_after = open("/proc/self/maps").read()
    modules = {name: getattr(module, "__file__", None) for name, module in sorted(sys.modules.items())}
    observed = sorted(reads)
    record = dict(scope="Bounded post-hook Python audit and before/after maps; NOT OS/startup tracing",
                  settings=settings, read_attempts=observed, imports=sorted(imports), modules=modules,
                  maps_before=maps_before, maps_after=maps_after,
                  existing_reads=[p for p in observed if os.path.isfile(p) and not p.startswith("/proc/")])
    with open(destination, "x") as handle:
        json.dump(record, handle, sort_keys=True, indent=2)
        handle.write("\n")
