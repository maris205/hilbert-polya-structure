
import hashlib, json, os, sys
from pathlib import Path
assert sys.flags.optimize == 0 and sys.flags.isolated == 1
assert sys.flags.no_site == 1 and sys.dont_write_bytecode
cache = Path(sys.pycache_prefix)
assert not cache.exists()
source = Path('verify.py')
exec(compile(source.read_bytes(), str(source), 'exec', optimize=0),
     {'__name__': '__main__', '__file__': str(source)})
assert not cache.exists()
modules = {}
for name, module in sorted(sys.modules.items()):
    origin = getattr(module, '__file__', None)
    spec = getattr(module, '__spec__', None)
    if origin and Path(origin).is_file():
        path = Path(origin).resolve()
        assert path.suffix != '.pyc', str(path)
        modules[name] = {'path': str(path), 'sha256': hashlib.sha256(path.read_bytes()).hexdigest()}
    else:
        modules[name] = {'origin': getattr(spec, 'origin', None)}
mapped = {}
for line in Path('/proc/self/maps').read_text().splitlines():
    fields = line.split(None, 5)
    if len(fields) == 6 and fields[5].startswith('/'):
        path = Path(fields[5]).resolve()
        assert path.is_file(), str(path)
        mapped[str(path)] = hashlib.sha256(path.read_bytes()).hexdigest()
result = {'version': sys.version, 'executable': str(Path(sys.executable).resolve()),
          'flags': repr(sys.flags), 'optimize': sys.flags.optimize,
          'isolated': sys.flags.isolated, 'no_site': sys.flags.no_site,
          'dont_write_bytecode': sys.dont_write_bytecode,
          'pycache_prefix': str(cache), 'cache_absent': not cache.exists(),
          'sys_path': sys.path, 'environment': dict(sorted(os.environ.items())),
          'modules': modules, 'mapped_files': mapped}
with Path(sys.argv[1]).open('x') as stream:
    json.dump(result, stream, sort_keys=True, indent=2)
    stream.write('\n')
