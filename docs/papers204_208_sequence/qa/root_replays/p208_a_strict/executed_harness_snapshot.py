#!/usr/bin/env python3
"""New P208 root mathematical replay pair with explicit source/runtime closure.

The historical recorders and receipts are not edited. This is reproduction,
not another independent review. Mode is author or a; each output is exclusive.
"""
from datetime import datetime, timezone
from hashlib import sha256
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys
import sysconfig
import traceback

ROOT = Path(__file__).resolve().parents[3]
BATCH = ROOT / 'docs/papers204_208_sequence'
PAPER = ROOT / 'papers/208-original-snapshot-triangulation-sweeps'
ARCHIVE = BATCH / 'qa/p208_round0_input_inspection_v2/historical_workspace_origins'
PYTHON = Path(sys.executable).resolve()
STDLIB = Path(sysconfig.get_path('stdlib')).resolve()
ENV = {'PATH': '/usr/bin:/bin', 'LANG': 'C', 'LC_ALL': 'C', 'TZ': 'UTC'}
WRAPPER = r'''
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
'''


def info(path):
    raw = path.read_bytes()
    return {'sha256': sha256(raw).hexdigest(), 'bytes': len(raw)}


def save(path, raw):
    with path.open('xb') as stream:
        stream.write(raw)


def dump(path, value):
    save(path, (json.dumps(value, sort_keys=True, indent=2) + '\n').encode())


def pin_files(paths):
    return {str(p.resolve()): info(p.resolve()) for p in sorted(set(paths))}


def manifest(base, name, complete=False):
    source = base / name
    result = {}
    for line in source.read_text().splitlines():
        expected, rel = line.split('  ', 1)
        local = Path(rel)
        assert not local.is_absolute() and '..' not in local.parts and local.parts
        assert rel not in result and rel != name
        path = base / local
        assert path.is_file() and not path.is_symlink()
        value = info(path)
        assert value['sha256'] == expected, str(path)
        result[rel] = value
    if complete:
        assert set(result) == {p.relative_to(base).as_posix() for p in base.rglob('*')
                               if p.is_file() and p != source}
    result[name] = info(source)
    return {str(base / rel): value for rel, value in result.items()}


def scientific_inputs(mode):
    result = manifest(PAPER, 'AUTHOR_MANIFEST.sha256')
    assert len(result) == 484
    frozen = manifest(PAPER / 'frozen_round0', 'SHA256SUMS', complete=True)
    assert len(frozen) == 488
    result.update(frozen)
    historical = manifest(ARCHIVE, 'SHA256SUMS', complete=True)
    assert len(historical) == 8
    expected_origins = {}
    for line in (PAPER / 'provenance/INPUT_ORIGINS.sha256').read_text().splitlines():
        digest, rel = line.split('  ', 1)
        expected_origins[rel] = digest
        assert historical[str(ARCHIVE / rel)]['sha256'] == digest
    assert len(expected_origins) == 7
    result.update(historical)
    if mode == 'a':
        review = BATCH / 'reviews/p208_a'
        result.update(manifest(review, 'SHA256SUMS', complete=True))
        for pin_name in ['INPUT_PINS.sha256', 'HISTORY_CONTEXT_PINS.sha256']:
            for line in (review / pin_name).read_text().splitlines():
                digest, rel = line.split('  ', 1)
                p = Path(rel)
                assert not p.is_absolute() and '..' not in p.parts
                p = ROOT / p
                value = info(p)
                assert value['sha256'] == digest, str(p)
                result[str(p)] = value
    result[str(Path(__file__).resolve())] = info(Path(__file__).resolve())
    return result


def runtime_inputs():
    paths = [p for p in STDLIB.rglob('*') if p.is_file()
             and 'site-packages' not in p.parts and '__pycache__' not in p.parts]
    paths += [PYTHON, Path('/usr/bin/cmp'), Path('/usr/bin/ldd'), Path('/bin/bash')]
    return pin_files(paths)


def configuration():
    # Include absence as well as bytes; discovery is repeated after the pair.
    paths = {Path('/etc/ld.so.cache'), Path('/etc/ld.so.conf'), Path('/etc/ld.so.preload'),
             Path('/lib/ld-linux.so.2'), Path('/lib64/ld-linux-x86-64.so.2'),
             Path('/libx32/ld-linux-x32.so.2'),
             STDLIB.parent / ('python%d%d.zip' % sys.version_info[:2])}
    paths.update(Path('/etc/ld.so.conf.d').glob('*'))
    return {str(p): {'exists': p.exists(), 'resolved': str(p.resolve()),
                    **(info(p) if p.is_file() else {})} for p in sorted(paths)}


def main():
    assert len(sys.argv) == 2 and sys.argv[1] in {'author', 'a'}
    assert sys.flags.optimize == 0 and sys.flags.isolated == 1
    assert sys.flags.no_site == 1 and sys.dont_write_bytecode
    mode = sys.argv[1]
    producer = PAPER if mode == 'author' else BATCH / 'reviews/p208_a'
    expected_assertions = 62101 if mode == 'author' else 130961
    out = BATCH / ('qa/root_replays/p208_' + mode + '_strict')
    out.mkdir(parents=True, exist_ok=False)
    save(out / 'executed_harness_snapshot.py', Path(__file__).read_bytes())
    save(out / 'executed_wrapper_snapshot.py', WRAPPER.encode())
    started = datetime.now(timezone.utc).isoformat()
    commands, runs, failures = [], [], []
    before, after, runtime_before, runtime_after = {}, {}, {}, {}
    config_before, config_after, libs_before, libs_after = {}, {}, {}, {}

    def execute(label, argv, cwd):
        began = datetime.now(timezone.utc).isoformat()
        child = subprocess.run(argv, cwd=cwd, env=ENV, capture_output=True, check=False)
        for name, raw in [('stdout', child.stdout), ('stderr', child.stderr)]:
            save(out / (label + '.' + name), raw)
        record = {'label': label, 'argv': argv, 'cwd': str(cwd), 'environment': ENV,
                  'started_utc': began, 'ended_utc': datetime.now(timezone.utc).isoformat(),
                  'exit_code': child.returncode,
                  'stdout': {'path': label + '.stdout', **info(out / (label + '.stdout'))},
                  'stderr': {'path': label + '.stderr', **info(out / (label + '.stderr'))}}
        commands.append(record)
        dump(out / (label + '.command.json'), record)
        assert child.returncode == 0, (label, child.returncode)
        return child

    def library_capture(label):
        objects = [str(PYTHON), '/usr/bin/cmp', '/bin/bash']
        objects += sorted(p for p in runtime_before if p.endswith('.so'))
        raw = execute(label, ['/usr/bin/ldd', *objects], out).stdout.decode()
        assert 'not found' not in raw
        paths = [Path(p).resolve() for p in re.findall(r'/[^\s():]+', raw) if Path(p).is_file()]
        assert paths, 'empty dynamic-library closure'
        return pin_files(paths)

    def failed(phase, error):
        failures.append({'phase': phase, 'type': type(error).__name__, 'message': str(error)})
        save(out / (phase + '_exception.txt'), traceback.format_exc().encode())

    try:
        before = scientific_inputs(mode)
        dump(out / 'INPUTS_BEFORE.json', before)
        runtime_before = runtime_inputs()
        dump(out / 'RUNTIME_INVENTORY_BEFORE.json', runtime_before)
        config_before = configuration()
        dump(out / 'CONFIGURATION_BEFORE.json', config_before)
        libs_before = library_capture('ldd_before')
        dump(out / 'LIBRARIES_BEFORE.json', libs_before)
        for label in ['run1', 'run2']:
            folder = out / label
            folder.mkdir()
            shutil.copyfile(producer / 'verify.py', folder / 'verify.py')
            initial = {p.name: info(p) for p in folder.iterdir()}
            assert initial == {'verify.py': info(producer / 'verify.py')}
            dump(out / (label + '_SOURCE_ONLY_INITIAL.json'), initial)
            cache = out / (label + '_unused_pycache')
            assert not cache.exists()
            runtime_path = out / (label + '_CONSUMED_RUNTIME.json')
            child = execute(label, [str(PYTHON), '-I', '-S', '-B', '-X',
                'pycache_prefix=' + str(cache), '-c', WRAPPER, str(runtime_path)], folder)
            assert child.stderr == b''
            data = json.loads(child.stdout)
            assert data['assertions'] == expected_assertions
            if mode == 'author':
                assert data['total_states'] == data['total_decoded_predecessors'] == 2055
                assert [r['n'] for r in data['rows']] == list(range(3, 11))
                assert sum(len(r['complete_graph_and_sources']) for r in data['rows']) == 2055
            runtime = json.loads(runtime_path.read_bytes())
            assert runtime['cache_absent'] and not cache.exists()
            assert runtime['optimize'] == 0 and runtime['isolated'] == runtime['no_site'] == 1
            assert runtime['dont_write_bytecode'] and runtime['environment'] == ENV
            assert set(runtime['sys_path']) <= {str(STDLIB), str(STDLIB / 'lib-dynload'),
                str(STDLIB.parent / ('python%d%d.zip' % sys.version_info[:2]))}
            for module in runtime['modules'].values():
                if 'path' in module:
                    assert runtime_before[module['path']]['sha256'] == module['sha256']
                    assert info(Path(module['path']))['sha256'] == module['sha256']
            all_runtime = {**runtime_before, **libs_before}
            for p, digest in runtime['mapped_files'].items():
                assert all_runtime[p]['sha256'] == digest, p
                assert info(Path(p))['sha256'] == digest, p
            final = {p.name: info(p) for p in folder.iterdir()}
            assert final == initial
            execute(label + '_canonical_cmp', ['/usr/bin/cmp', str(producer / 'CANONICAL.json'),
                                              str(out / (label + '.stdout'))], out)
            runs.append({'label': label, 'assertions': data['assertions'],
                         'initial_files': initial, 'final_files': final,
                         'consumed_module_files': sum('path' in m for m in runtime['modules'].values()),
                         'mapped_files': len(runtime['mapped_files']), 'unused_cache_absent': True})
        execute('pair_cmp', ['/usr/bin/cmp', str(out / 'run1.stdout'), str(out / 'run2.stdout')], out)
    except BaseException as error:
        failed('producer_phase', error)
    try:
        after = scientific_inputs(mode)
        dump(out / 'INPUTS_AFTER.json', after)
        runtime_after = runtime_inputs()
        dump(out / 'RUNTIME_INVENTORY_AFTER.json', runtime_after)
        config_after = configuration()
        dump(out / 'CONFIGURATION_AFTER.json', config_after)
        libs_after = library_capture('ldd_after')
        dump(out / 'LIBRARIES_AFTER.json', libs_after)
        assert before == after and before
        assert runtime_before == runtime_after and runtime_before
        assert config_before == config_after and config_before
        assert libs_before == libs_after and libs_before
    except BaseException as error:
        failed('closure_phase', error)
    passed = not failures and len(runs) == 2 and len(commands) == 7 and all(c['exit_code'] == 0 for c in commands)
    receipt = {'status': 'PASS_ROOT_P208_STRICT_PAIR' if passed else 'FAIL', 'mode': mode,
        'kind': 'ROOT_REPRODUCTION_NOT_AN_INDEPENDENT_REVIEW',
        'started_utc': started, 'ended_utc': datetime.now(timezone.utc).isoformat(),
        'inputs': len(before), 'runtime_inventory': len(runtime_before),
        'configuration_entries': len(config_before), 'library_files': len(libs_before),
        'commands': commands, 'runs': runs, 'failures': failures,
        'historical_origins': 'Exact seven archived admission bytes, not mutable present-day central ledgers.',
        'limits': 'Concrete Python source/extensions, loaded file mappings, tools, resolved libraries and loader configuration. Not a hermetic historical OS/kernel image; old receipts retain their original limitations.',
        'external': 'HOLD_EXTERNAL'}
    dump(out / 'RECEIPT.json', receipt)
    rows = [(info(p)['sha256'], p.relative_to(out).as_posix()) for p in sorted(out.rglob('*')) if p.is_file()]
    save(out / 'SHA256SUMS', ''.join(f'{h}  {p}\n' for h, p in rows).encode())
    assert len(manifest(out, 'SHA256SUMS', complete=True)) == len(rows) + 1
    print(json.dumps({k: receipt[k] for k in ['status', 'mode', 'inputs', 'runtime_inventory',
                                             'configuration_entries', 'library_files', 'runs', 'failures']}, indent=2))
    raise SystemExit(0 if passed else 1)


if __name__ == '__main__':
    main()
