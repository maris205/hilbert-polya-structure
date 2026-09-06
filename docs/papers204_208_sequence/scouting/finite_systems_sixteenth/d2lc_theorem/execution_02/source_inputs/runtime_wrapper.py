"""Preload the exact standard-library closure and pin it around one producer."""
import collections
import hashlib
import itertools
import json
import os
import pathlib
import sys


def digest(path):
    return hashlib.sha256(pathlib.Path(path).read_bytes()).hexdigest()


def pins():
    paths = {str(pathlib.Path(sys.executable).resolve())}
    modules = {}
    for name, module in sorted(sys.modules.items()):
        found = []
        for attr in ('__file__', '__cached__'):
            value = getattr(module, attr, None)
            if value and pathlib.Path(value).is_file():
                absolute = str(pathlib.Path(value).resolve())
                found.append(absolute)
                paths.add(absolute)
        modules[name] = sorted(set(found))
    for line in pathlib.Path('/proc/self/maps').read_text().splitlines():
        parts = line.split()
        if parts and parts[-1].startswith('/') and pathlib.Path(parts[-1]).is_file():
            paths.add(str(pathlib.Path(parts[-1]).resolve()))
    return {'files': {p: digest(p) for p in sorted(paths)}, 'modules': modules,
            'version': sys.version, 'flags': repr(sys.flags), 'path': sys.path,
            'executable': sys.executable, 'environment': dict(sorted(os.environ.items())),
            'byteorder': sys.byteorder}


producer = pathlib.Path(sys.argv[1]).resolve()
record_dir = pathlib.Path(sys.argv[2]).resolve()
source = producer.read_bytes()
code = compile(source, str(producer), 'exec', dont_inherit=True, optimize=0)
before = pins()
(record_dir / 'RUNTIME_BEFORE.json').write_text(json.dumps(before, sort_keys=True, indent=2) + '\n')
try:
    exec(code, {'__name__': '__main__', '__file__': str(producer)})
finally:
    after = pins()
    (record_dir / 'RUNTIME_AFTER.json').write_text(json.dumps(after, sort_keys=True, indent=2) + '\n')
    assert before == after, 'runtime dependencies changed during producer'
