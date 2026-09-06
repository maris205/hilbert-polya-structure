"""Infrastructure only: fresh source execution and consumed-runtime recording."""
import sys
import os
import json
import hashlib
import time

target, evidence = sys.argv[1:3]
def pin(path):
    return hashlib.sha256(open(path, 'rb').read()).hexdigest()
def maps():
    raw = open('/proc/self/maps').read()
    paths = sorted(set(line.split(None, 5)[5].strip() for line in raw.splitlines()
                       if len(line.split(None, 5)) == 6 and line.split(None, 5)[5].startswith('/')))
    return {'raw': raw, 'files': {p: pin(p) for p in paths}}
def modules():
    result = {}
    for name, mod in sorted(sys.modules.items()):
        spec = getattr(mod, '__spec__', None)
        path = getattr(mod, '__file__', None)
        result[name] = {'origin': getattr(spec, 'origin', None),
                        'file': path, 'loader': type(getattr(spec, 'loader', None)).__name__}
        if path and os.path.isfile(path):
            result[name]['sha256'] = pin(path)
    return result
before = {'modules': modules(), 'maps': maps(), 'target_sha256': pin(target),
          'version': sys.version, 'executable': sys.executable, 'flags': repr(sys.flags),
          'path': sys.path, 'environment': dict(os.environ), 'cwd': os.getcwd(),
          'pycache_prefix': sys.pycache_prefix, 'utc': time.strftime('%Y-%m-%d %H:%M:%S UTC', time.gmtime())}
assert sys.flags.optimize == 0 and sys.flags.isolated and sys.flags.no_site and sys.dont_write_bytecode
assert sys.pycache_prefix and not os.path.exists(sys.pycache_prefix)
events = []
def hook(event, args):
    if event == 'open':
        events.append({'event': event, 'path': str(args[0]), 'mode': str(args[1]), 'flags': args[2]})
    elif event == 'import':
        events.append({'event': event, 'name': str(args[0]), 'filename': str(args[1])})
sys.addaudithook(hook)
exit_status = 0
try:
    source = open(target, 'rb').read()
    exec(compile(source, target, 'exec', optimize=0), {'__name__': '__main__', '__file__': target})
except BaseException:
    exit_status = 1
    raise
finally:
    consumed = {}
    for event in list(events):
        if event['event'] == 'open' and os.path.isfile(event['path']):
            consumed[event['path']] = pin(event['path'])
    report = {'before': before, 'after': {'modules': modules(), 'maps': maps(),
              'target_sha256': pin(target)}, 'events': list(events),
              'consumed_files': consumed, 'exit_status': exit_status,
              'cache_prefix_still_absent': not os.path.exists(sys.pycache_prefix)}
    with open(evidence, 'w') as stream:
        json.dump(report, stream, sort_keys=True, indent=2)
        stream.write('\n')
