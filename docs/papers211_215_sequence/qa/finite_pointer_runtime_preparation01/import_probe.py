#!/usr/bin/env python3
"""Frozen import-only pointer runtime discovery. No scientific source access.

Only the six producer import statements below occur. The startup-provided
posix module is inspected, not imported, for actual cwd/environment/cache
settings. No Counter/Fraction/product/factorial operation is evaluated.
"""
import sys

startup_modules = sorted(sys.modules)
events = []
def audit(event, args):
    if event == 'open':
        path, mode, flags = args
        if isinstance(path, (str, bytes)):
            events.append({'event': event, 'path': path.decode() if isinstance(path, bytes) else path,
                           'mode': mode, 'flags': flags})
            if isinstance(flags, int) and flags & (1 | 2 | 64 | 512 | 1024):
                raise RuntimeError('import-only probe forbids ordinary writes')
    elif event == 'import':
        events.append({'event': event, 'module': args[0], 'filename': args[1]})
    elif event in ('subprocess.Popen', 'os.fork', 'os.forkpty', 'os.posix_spawn',
                   'os.exec', 'os.system', 'os.kill', 'os.killpg'):
        raise RuntimeError('import-only probe forbids process and signal actions')

sys.addaudithook(audit)
import json
from collections import Counter
from fractions import Fraction
from itertools import product
from math import factorial

posix_runtime = sys.modules['posix']
assert len(sys.argv) == 3
assert sys.executable == '/usr/bin/python3.10'
assert sys.flags.isolated == sys.flags.no_site == 1
assert sys.flags.optimize == 0 and sys.dont_write_bytecode
assert sys.pycache_prefix == sys.argv[1]
assert posix_runtime.getcwd() == sys.argv[2]
assert sys.path == ['/usr/lib/python310.zip', '/usr/lib/python3.10', '/usr/lib/python3.10/lib-dynload']
try:
    posix_runtime.lstat(sys.pycache_prefix)
except FileNotFoundError:
    cache_absent = True
else:
    raise AssertionError('probe cache must remain nonexistent')
environment = {key.decode(): val.decode() for key, val in posix_runtime.environ.items()}
assert environment == {'PATH': '/usr/bin:/bin', 'LANG': 'C.UTF-8', 'LC_ALL': 'C.UTF-8', 'TZ': 'UTC'}
with open('/proc/self/maps', 'r', encoding='ascii') as stream:
    maps = stream.read()
modules = {}
for name, module in sorted(sys.modules.items()):
    spec = getattr(module, '__spec__', None)
    path = getattr(module, '__file__', None)
    assert path is None or not path.endswith(('.pyc', '.pyo'))
    modules[name] = {'file': path, 'origin': getattr(spec, 'origin', None)}
row = {'status': 'IMPORT_ONLY_NO_SCIENCE',
       'declared_imports': ['sys', 'json', 'collections.Counter', 'fractions.Fraction',
                            'itertools.product', 'math.factorial'],
       'argv': sys.argv, 'orig_argv': sys.orig_argv, 'cwd': posix_runtime.getcwd(),
       'environment': environment, 'executable': sys.executable, 'version': sys.version,
       'flags': repr(sys.flags), 'sys_path': sys.path, 'cache': sys.pycache_prefix,
       'cache_absent': cache_absent, 'startup_modules': startup_modules,
       'modules': modules, 'proc_maps': maps, 'audit_events': events,
       'encodings': {'filesystem': sys.getfilesystemencoding(),
                     'filesystem_errors': sys.getfilesystemencodeerrors(),
                     'default': sys.getdefaultencoding(), 'stdin': sys.stdin.encoding,
                     'stdout': sys.stdout.encoding, 'stderr': sys.stderr.encoding},
       'science_source_reads': [], 'scientific_executions': 0,
       'limits': 'Post-hook Python imports/opens and one file-backed map sample; no OS/startup/native-open tracing.'}
print(json.dumps(row, sort_keys=True, separators=(',', ':'), allow_nan=False))
