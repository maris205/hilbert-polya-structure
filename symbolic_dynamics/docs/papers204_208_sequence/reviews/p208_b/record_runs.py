"""Standalone infrastructure recorder, no author/A imports or executions."""
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import sysconfig
import time
import uuid

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
BASE = ROOT / 'docs/papers204_208_sequence/reviews/p208_b'
ENV = {'PATH': '/root/miniconda3/bin:/usr/bin:/bin', 'LANG': 'C', 'LC_ALL': 'C',
       'TZ': 'UTC', 'SOURCE_DATE_EPOCH': '1700000000', 'FORCE_SOURCE_DATE': '1'}
def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def write(p, data):
    Path(p).write_text(json.dumps(data, sort_keys=True, indent=2)+'\n')
def command(out, name, args, cwd=ROOT):
    start = time.time()
    child = subprocess.run(args, cwd=cwd, env=ENV, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    (out/(name+'.stdout')).write_bytes(child.stdout)
    (out/(name+'.stderr')).write_bytes(child.stderr)
    record = {'argv': [str(x) for x in args], 'cwd': str(cwd), 'environment': ENV,
              'exit_code': child.returncode, 'seconds': time.time()-start,
              'stdout_sha256': sha(out/(name+'.stdout')), 'stderr_sha256': sha(out/(name+'.stderr'))}
    write(out/(name+'.command.json'), record)
    return child
def snapshot_paths():
    std = Path(sysconfig.get_path('stdlib'))
    paths = set()
    for path in std.rglob('*'):
        if 'site-packages' not in path.parts and '__pycache__' not in path.parts and path.is_file() and path.suffix in ('.py', '.so'):
            paths.add(str(path))
    paths |= {str(Path(sys.executable)), str(Path(sys.executable).resolve()), '/usr/bin/cmp', '/usr/bin/ldd', '/bin/bash'}
    paths |= {str(p) for base in (ROOT/'papers/208-original-snapshot-triangulation-sweeps/frozen_round1', BASE/'assignment_context')
              for p in base.rglob('*') if p.is_file()}
    paths |= {str(p) for p in BASE.glob('*.py')}
    paths |= {str(p) for p in BASE.glob('*.sha256')}
    paths |= {str(p) for p in BASE.glob('CANONICAL.json')}
    paths |= {str(p) for p in BASE.glob('SOURCE_CONTEXT_PINS.json')}
    for source in ('sources', 'history_context'):
        directory = BASE/source
        if directory.exists():
            paths |= {str(p) for p in directory.rglob('*') if p.is_file()}
    return paths
def configuration():
    paths = ['/etc/ld.so.cache', '/etc/ld.so.conf', '/etc/ld.so.preload',
             '/root/miniconda3/pyvenv.cfg', '/root/miniconda3/bin/pyvenv.cfg',
             '/root/miniconda3/bin/python._pth', '/root/miniconda3/bin/python3._pth',
             '/root/miniconda3/lib/python313.zip', '/root/miniconda3/lib/python312.zip']
    paths += [str(p) for p in Path('/etc/ld.so.conf.d').rglob('*') if p.is_file()]
    return {p: {'exists': Path(p).exists(), 'sha256': sha(p) if Path(p).is_file() else None} for p in paths}
def pinset(paths):
    return {p: sha(p) for p in sorted(paths)}
def consume(report):
    result = dict(report['consumed_files'])
    for endpoint in ('before', 'after'):
        result.update(report[endpoint]['maps']['files'])
        for info in report[endpoint]['modules'].values():
            if 'sha256' in info:
                result[info['file']] = info['sha256']
    return {p: h for p, h in result.items() if p != '/proc/self/maps'}
def run_pair(label, producer, canonical=None, count=2):
    out = BASE/label
    out.mkdir(exist_ok=False)
    paths = snapshot_paths()
    tool_roots = [Path(sys.executable).resolve(), Path('/usr/bin/cmp'), Path('/bin/bash')]
    # Pin all extension dependencies before execution; distinguish raw aliases from resolved files.
    libraries = set()
    ldd_records = []
    for number, path in enumerate(tool_roots + sorted(Path(sysconfig.get_path('stdlib')).glob('lib-dynload/*.so'))):
        child = command(out, f'ldd_{number:03d}', ['/usr/bin/ldd', str(path)])
        assert child.returncode == 0, path
        aliases = []
        for token in child.stdout.decode().split():
            if token.startswith('/') and Path(token).is_file():
                aliases.append(token)
                libraries.add(str(Path(token).resolve()))
                paths.add(token)
        ldd_records.append({'target': str(path), 'aliases': aliases})
    paths |= libraries
    cfg = configuration()
    paths |= {p for p, info in cfg.items() if info['exists'] and Path(p).is_file()}
    before = pinset(paths)
    write(out/'INPUTS_BEFORE.json', before)
    write(out/'CONFIG_BEFORE.json', cfg)
    write(out/'LINK_DEPENDENCIES.json', ldd_records)
    runs = []
    for number in range(1, count+1):
        prefix = out/('unused_pycache_'+uuid.uuid4().hex)
        assert not prefix.exists()
        args = [sys.executable, '-I', '-S', '-B', '-X', 'pycache_prefix='+str(prefix),
                str(BASE/'runtime_probe.py'), str(producer), str(out/f'run_{number}.runtime.json')]
        child = command(out, f'run_{number}', args)
        runs.append({'number': number, 'exit_code': child.returncode, 'pycache_prefix': str(prefix)})
        assert child.returncode == 0, f'preserved failed producer {number}'
        report = json.loads((out/f'run_{number}.runtime.json').read_text())
        consumed = consume(report)
        missing = {p: h for p, h in consumed.items() if p not in before}
        write(out/f'run_{number}.coverage.json', {'consumed': consumed, 'missing': missing})
        assert not missing, missing
        assert all(before[p] == h == sha(p) for p, h in consumed.items())
        assert report['cache_prefix_still_absent']
        # Existing pyc was never read: attempted absent cache paths are retained as events.
        assert not any(p.endswith('.pyc') for p in consumed)
    comparisons = []
    if count == 2:
        comparisons.append(command(out, 'cmp_pair', ['/usr/bin/cmp', '-s', str(out/'run_1.stdout'), str(out/'run_2.stdout')]).returncode)
    if canonical:
        for number in range(1, count+1):
            comparisons.append(command(out, f'cmp_canonical_{number}', ['/usr/bin/cmp', '-s', str(out/f'run_{number}.stdout'), str(canonical)]).returncode)
    after = pinset(paths)
    write(out/'INPUTS_AFTER.json', after)
    write(out/'CONFIG_AFTER.json', configuration())
    assert before == after and cfg == configuration() and all(x == 0 for x in comparisons)
    write(out/'RECEIPT.json', {'producer': str(producer), 'runs': runs, 'input_count': len(before),
         'configuration_count': len(cfg), 'resolved_ldd_files': len(libraries),
         'raw_ldd_aliases': len(set(p for r in ldd_records for p in r['aliases'])),
         'comparisons': comparisons, 'unchanged_complete_input_set': True,
         'source_only': True, 'optimization': 0})
    print(json.dumps({'label': label, 'status': 'PASS', 'input_count': len(before), 'runs': len(runs), 'comparisons': comparisons}))
if __name__ == '__main__':
    run_pair(sys.argv[1], Path(sys.argv[2]).resolve(), Path(sys.argv[3]).resolve() if len(sys.argv)>3 else None,
             count=1 if sys.argv[1] == 'initial_execution' else 2)
