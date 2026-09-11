"""Read-only runtime discovery; no candidate or scientific code is imported."""
import hashlib
import itertools
import json
import math
import os
import pathlib
import subprocess
import sys
import time


def pin(path):
    path = os.path.realpath(path)
    with open(path, "rb") as stream:
        raw = stream.read()
    return {"path": path, "bytes": len(raw), "sha256": hashlib.sha256(raw).hexdigest()}


paths = {os.path.realpath(sys.executable)}
modules = []
for name, module in sorted(sys.modules.items()):
    path = getattr(module, "__file__", None)
    if path and os.path.isfile(path):
        resolved = os.path.realpath(path)
        modules.append({"module": name, "path": resolved})
        paths.add(resolved)
mapped = set()
with open("/proc/self/maps", encoding="utf-8") as stream:
    for line in stream:
        fields = line.rstrip("\n").split(None, 5)
        if len(fields) == 6 and fields[5].startswith("/") and os.path.isfile(fields[5]):
            mapped.add(os.path.realpath(fields[5]))
paths.update(mapped)
print(json.dumps({"kind": "readonly_runtime_probe_not_science", "argv": sys.argv,
                  "cwd": os.getcwd(), "python_version": sys.version,
                  "environment": dict(sorted(os.environ.items())),
                  "modules": modules, "mapped_runtime_paths": sorted(mapped),
                  "file_pins": [pin(path) for path in sorted(paths)]},
                 sort_keys=True, separators=(",", ":")))
