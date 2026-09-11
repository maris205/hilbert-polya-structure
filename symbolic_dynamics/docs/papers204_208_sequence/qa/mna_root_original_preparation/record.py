#!/usr/bin/env python3
"""Future root documentary capture only; exclusive output chosen by root.
No scientific code is imported or executed. Native child is new inspect.py.
Caller must retain this recorder's native invocation/output/exit separately.
"""
import argparse
from hashlib import sha256
import json
import os
from pathlib import Path
import re
import subprocess
import sys
from datetime import datetime, timezone

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
QA = ROOT / 'docs/papers204_208_sequence/qa'
PREP = QA / 'mna_root_original_preparation'
AUDIT = QA / 'mna_gate_documentary_audit'
ENV = {'PATH': '/usr/bin:/bin', 'LANG': 'C.UTF-8', 'LC_ALL': 'C.UTF-8', 'TZ': 'UTC'}
PYTHON = Path('/usr/bin/python3.10')


def need(test, detail):
    if not test:
        raise AssertionError(detail)


def metadata(path):
    data = Path(path).read_bytes()
    return {'sha256': sha256(data).hexdigest(), 'bytes': len(data)}


def now():
    return datetime.now(timezone.utc).isoformat()


def sample():
    modules, mapped = {}, {}
    for name, module in sorted(sys.modules.items()):
        path = getattr(module, '__file__', None)
        if path and Path(path).is_file():
            p = Path(path).resolve(strict=True)
            need(p.suffix not in ('.pyc', '.pyo'), ('no_source_bytecode', name))
            modules[name] = {'path': str(p), **metadata(p)}
    maps = Path('/proc/self/maps').read_bytes()
    for line in maps.decode().splitlines():
        fields = line.split(None, 5)
        if len(fields) == 6 and fields[5].startswith('/'):
            need(not fields[5].endswith(' (deleted)'), ('deleted_mapping', fields[5]))
            p = Path(fields[5]).resolve(strict=True)
            mapped[str(p)] = metadata(p)
    return {'modules': modules, 'mapped_files': mapped, 'volatile_proc_maps': maps.decode(),
        'flags': repr(sys.flags), 'environment': dict(os.environ), 'executable': str(Path(sys.executable).resolve()),
        'sys_path': sys.path, 'pycache_prefix': sys.pycache_prefix,
        'scope': 'Current file-backed sample, not OS/startup/continuous tracing; proc text is an observation, not reused input.'}


def runtime_scope():
    files = {str(PYTHON), '/usr/bin/cmp', '/usr/bin/env', '/bin/bash', '/bin/sh'}
    for directory, folders, names in os.walk('/usr/lib/python3.10'):
        folders[:] = [n for n in folders if n not in {'site-packages', 'dist-packages', '__pycache__'}]
        files.update(str(Path(directory) / n) for n in names if not n.endswith(('.pyc', '.pyo')))
    for root in map(Path, ('/usr/lib/x86_64-linux-gnu', '/usr/lib64', '/usr/local/lib')):
        if root.is_dir():
            candidates = root.glob('*') if root == Path('/usr/local/lib') else root.rglob('*')
            files.update(str(p) for p in candidates if p.is_file() and (p.name.endswith('.so') or '.so.' in p.name))
    for root in map(Path, ('/usr/lib/locale/C.utf8', '/usr/lib/x86_64-linux-gnu/gconv', '/usr/lib/gconv', '/etc/ld.so.conf.d')):
        if root.is_dir():
            files.update(str(p) for p in root.rglob('*') if p.is_file())
    optional = ('/etc/ld.so.cache', '/etc/ld.so.conf', '/etc/ld.so.preload', '/etc/localtime', '/etc/locale.conf', '/etc/default/locale',
        '/etc/ssl/openssl.cnf', '/usr/lib/ssl/openssl.cnf', '/usr/lib/python310.zip', '/usr/bin/pyvenv.cfg', '/usr/pyvenv.cfg',
        '/usr/bin/python._pth', '/usr/bin/python3.10._pth', '/usr/lib/python._pth', '/usr/lib/python3.10._pth')
    config = {name: {'lexists': os.path.lexists(name), 'exists': Path(name).exists(), 'file': Path(name).is_file(),
        'resolved': str(Path(name).resolve()), 'symlink': os.readlink(name) if Path(name).is_symlink() else None} for name in optional}
    need(all(not row['lexists'] for name, row in config.items() if name.endswith(('ld.so.preload', 'python310.zip', 'pyvenv.cfg', '._pth'))), 'no_loader_or_import_injection')
    files.update(name for name, row in config.items() if row['file'])
    files.update(str(Path(name).resolve(strict=True)) for name in list(files))
    return {'files': sorted(files), 'configuration': config}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', required=True)
    parser.add_argument('--expected-preparation-sha256', required=True)
    args = parser.parse_args()
    out = Path(args.output)
    need(out.is_absolute() and out.parent == QA and re.fullmatch(r'mna_root_original_[0-9]{2}', out.name) and not os.path.lexists(out), 'explicit_fresh_scoped_output_required')
    need(QA.resolve(strict=True) == QA and Path(__file__).resolve() == PREP / 'record.py', 'physical_scope_and_exact_source')
    need(Path.cwd() == ROOT and Path(sys.executable).resolve() == PYTHON and dict(os.environ) == ENV and
         sys.flags.isolated and sys.flags.no_site and sys.flags.optimize == 0 and sys.dont_write_bytecode and
         sys.pycache_prefix == str(out / 'unused_recorder_cache') and not os.path.lexists(sys.pycache_prefix), 'exact_source_only_recorder_entry')
    need(sys.path == ['/usr/lib/python310.zip', '/usr/lib/python3.10', '/usr/lib/python3.10/lib-dynload'] and not os.path.lexists('/usr/lib/python310.zip'), 'source_only_system_import_paths')
    need(metadata(PREP / 'SHA256SUMS')['sha256'] == args.expected_preparation_sha256, 'actual_preparation_seal_pin')
    out.mkdir()
    def save(name, data):
        path = out / name
        need(path.parent.resolve(strict=True) == path.parent, 'physical_output_parent')
        with path.open('xb') as stream:
            stream.write(data if isinstance(data, bytes) else (json.dumps(data, sort_keys=True, indent=2) + '\n').encode())
    save('RUN_ENTERED.json', {'status': 'ENTERED_NOT_OWN_PRESPAWN', 'argv': sys.orig_argv, 'cwd': str(ROOT), 'environment': ENV, 'utc': now()})
    errors, before, scope, receipt = [], None, None, None
    try:
        fixed = json.loads((PREP / 'INPUT_PINS.json').read_bytes())['inputs']
        for name, expected in fixed.items():
            need(metadata(name) == expected, ('fixed_original_input', name))
        old = json.loads((AUDIT / 'attempt_01/stdout.raw').read_bytes())
        need(old['physical_inputs_before'] == old['physical_inputs_after'] and len(old['physical_inputs_before']) == 1294, 'original_1294_map_schema')
        for name, expected in old['physical_inputs_before'].items():
            need(metadata(name) == expected, ('exact_original_1294_input', name))
        scope = runtime_scope()
        names = set(old['physical_inputs_before']) | set(scope['files'])
        names.update(str(p) for base in (AUDIT, PREP) for p in base.rglob('*') if p.is_file())
        for name in ('inspect.py', 'record.py'):
            save('executed_' + name, (PREP / name).read_bytes())
            names.add(str(out / ('executed_' + name)))
        names.update(str(Path(name).resolve(strict=True)) for name in list(names))
        before = {name: metadata(name) for name in sorted(names)}
        save('INPUTS_BEFORE.json', before)
        save('RUNTIME_SCOPE_BEFORE.json', scope)
        parent_before = sample()
        for path, expected in list(parent_before['mapped_files'].items()) + [(v['path'], {k: v[k] for k in ('sha256', 'bytes')}) for v in parent_before['modules'].values()]:
            need(before.get(path) == expected, ('parent_runtime_before_coverage', path))
        save('PARENT_BEFORE.json', parent_before)
        argv = [str(PYTHON), '-I', '-S', '-B', '-X', 'pycache_prefix=' + str(out / 'unused_checker_cache'), str(PREP / 'inspect.py'),
                '--expected-preparation-sha256', args.expected_preparation_sha256, '--runtime-inputs', str(out / 'INPUTS_BEFORE.json')]
        attempt = {'argv': argv, 'cwd': str(ROOT), 'environment': ENV, 'started_utc': now(), 'status': 'ATTEMPTED', 'exit_code': None,
                   'timeout_seconds': 60, 'before_capsule': metadata(out / 'INPUTS_BEFORE.json'), 'source_before': {name: metadata(PREP / name) for name in ('inspect.py', 'record.py')}}
        save('ATTEMPT.json', attempt)
        failure, timed_out, complete, spawned = None, False, True, True
        try:
            child = subprocess.run(argv, cwd=ROOT, env=ENV, capture_output=True, timeout=60, check=False)
            code, wrapper_code, stdout, stderr = child.returncode, child.returncode, child.stdout, child.stderr
        except subprocess.TimeoutExpired as exc:
            code, wrapper_code, stdout, stderr, timed_out, complete, failure = None, 124, exc.stdout or b'', exc.stderr or b'', True, False, repr(exc)
        except OSError as exc:
            code, wrapper_code, stdout, stderr, spawned, complete, failure = None, 127, b'', b'', False, False, repr(exc)
        save('stdout.raw', stdout); save('stderr.raw', stderr)
        receipt = {**attempt, 'status': 'COMPLETED' if failure is None else 'TIMED_OUT' if timed_out else 'SPAWN_FAILED',
            'ended_utc': now(), 'exit_code': code, 'wrapper_exit_code': wrapper_code, 'timed_out': timed_out, 'spawned': spawned,
            'streams_complete': complete, 'failure': failure, 'stdout': metadata(out / 'stdout.raw'), 'stderr': metadata(out / 'stderr.raw'),
            'source_after': {name: metadata(PREP / name) for name in ('inspect.py', 'record.py')}}
        save('RECEIPT.json', receipt)
        need(code == 0 and stderr == b'' and receipt['source_before'] == receipt['source_after'], 'actual_complete_child_pass')
        result = json.loads(stdout)
        need(result['status'] == 'PASS_ROOT_MNA_ORIGINAL_DOCUMENTARY_CLOSURE' and result['root_reference_closure_unchanged'] is True and result['original_physical_paths_checked_twice'] == 1294, 'actual_child_original_closure')
    except Exception as exc:
        errors.append({'stage': 'capture', 'error': repr(exc)})
    finally:
        if before is not None:
            try:
                after = {name: metadata(name) for name in before}
                save('INPUTS_AFTER.json', after)
                after_scope = runtime_scope(); save('RUNTIME_SCOPE_AFTER.json', after_scope)
                need(after == before and after_scope == scope, 'entire_recorder_input_and_resource_scope_unchanged')
                parent_after = sample(); save('PARENT_AFTER.json', parent_after)
                for path, expected in list(parent_after['mapped_files'].items()) + [(v['path'], {k: v[k] for k in ('sha256', 'bytes')}) for v in parent_after['modules'].values()]:
                    need(before.get(path) == expected, ('parent_runtime_after_coverage', path))
                need(all(not os.path.lexists(out / n) for n in ('unused_recorder_cache', 'unused_checker_cache')), 'all_unused_caches_absent_after')
                for name in ('inspect.py', 'record.py'):
                    need((out / ('executed_' + name)).read_bytes() == (PREP / name).read_bytes(), ('unchanged_exact_source_copy', name))
                if receipt:
                    need(metadata(out / 'stdout.raw') == receipt['stdout'] and metadata(out / 'stderr.raw') == receipt['stderr'] and metadata(out / 'INPUTS_BEFORE.json') == receipt['before_capsule'], 'native_streams_and_before_capsule_unchanged')
            except Exception as exc:
                errors.append({'stage': 'after', 'error': repr(exc)})
    status = 'FAIL_ROOT_MNA_DOCUMENTARY_CAPTURE' if errors else 'PASS_ROOT_MNA_DOCUMENTARY_CAPTURE'
    save('CAPTURE_RESULT.json', {'status': status, 'errors': errors, 'input_count': len(before) if before else None,
        'native_child_exit': receipt['exit_code'] if receipt else None, 'scope': 'Original documentary checking only, not science/admission/review.',
        'completion_boundary': 'This result precedes sealing. Require successful native recorder return plus complete verified seal.', 'owner': 'OWNER_AMBER', 'external_status': 'HOLD_EXTERNAL'})
    files = sorted(p for p in out.rglob('*') if p.is_file())
    need(not any(p.is_symlink() for p in out.rglob('*')), 'output_no_symlinks')
    save('SHA256SUMS', ''.join(metadata(p)['sha256'] + '  ' + p.relative_to(out).as_posix() + '\n' for p in files).encode())
    print(json.dumps({'status': status, 'errors': errors, 'output': str(out), 'payloads': len(files), 'manifest': metadata(out / 'SHA256SUMS'),
        'native_child_exit': receipt['exit_code'] if receipt else None, 'known_inputs': len(before) if before else None,
        'boundary': 'No theorem, third review or admission claim. Root must inspect original source semantics separately.'}, sort_keys=True, indent=2))
    return 1 if errors else 0


if __name__ == '__main__':
    raise SystemExit(main())
