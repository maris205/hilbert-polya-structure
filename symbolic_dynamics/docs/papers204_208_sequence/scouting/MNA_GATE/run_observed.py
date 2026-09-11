#!/usr/bin/env python3
"""Instrumentation only: records Python audit opens and actual mapped objects."""
import hashlib
import json
import os
from pathlib import Path
import sys

source = Path(sys.argv[1]).resolve()
runtime_output = Path(sys.argv[2]).resolve()
opened = set()

def observe(event, args):
    if event == 'open' and isinstance(args[0], (str, bytes)):
        opened.add(os.fsdecode(args[0]))

sys.addaudithook(observe)
try:
    code = compile(source.read_bytes(), str(source), 'exec')
    exec(code, {'__name__':'__main__','__file__':str(source)})
finally:
    mapped = set()
    maps = Path('/proc/self/maps').read_text()
    for line in maps.splitlines():
        fields = line.split()
        if len(fields) >= 6 and fields[-1].startswith('/'):
            mapped.add(fields[-1])
    modules = sorted({str(Path(module.__file__).resolve()) for module in sys.modules.values()
                      if getattr(module,'__file__',None) and Path(module.__file__).is_file()})
    observed = sorted(opened)
    present = sorted({str(Path(p).resolve()) for p in observed + modules + list(mapped)
                      if Path(p).is_file()})
    record = {'role':'Python_audit_open_events_plus_modules_and_proc_maps_not_OS_syscall_trace',
              'executable':str(Path(sys.executable).resolve()),'version':sys.version,
              'flags':str(sys.flags),'sys_path':sys.path,'pycache_prefix':sys.pycache_prefix,
              'environment':dict(sorted(os.environ.items())),
              'audit_open_paths':observed,'module_files':modules,'mapped_paths':sorted(mapped),
              'files':{p:{'sha256':hashlib.sha256(Path(p).read_bytes()).hexdigest(),
                          'bytes':Path(p).stat().st_size} for p in present},
              'proc_maps':maps}
    runtime_output.write_text(json.dumps(record,sort_keys=True,indent=2)+'\n')
