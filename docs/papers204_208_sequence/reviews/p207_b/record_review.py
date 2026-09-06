#!/usr/bin/env python3
"""Actual isolated B execution recorder, fail closed and retain raw evidence."""
import argparse
from datetime import datetime, timezone
from hashlib import sha256
import json
from pathlib import Path
import shutil
import subprocess
import sys


def utc():
    return datetime.now(timezone.utc).isoformat()


def save(path, data):
    with path.open('x', encoding='utf-8') as stream:
        json.dump(data, stream, indent=2, sort_keys=True)
        stream.write('\n')


def hashfile(path):
    return sha256(path.read_bytes()).hexdigest()


def pinpaths(manifest, root):
    out = []
    for line in manifest.read_text().splitlines():
        digest, name = line.split('  ', 1)
        source = root/name
        if hashfile(source) != digest:
            raise RuntimeError(f'Input manifest mismatch: {name}')
        out.append(source)
    return out


def writepins(path, inputs, root):
    text = ''.join(f'{hashfile(p)}  {p.relative_to(root)}\n' for p in sorted(set(inputs)))
    with path.open('x') as stream:
        stream.write(text)
    return text


def execute(out, label, command, cwd):
    rec = {'command': command, 'cwd': str(cwd), 'started_utc': utc()}
    with (out/f'{label}.stdout').open('xb') as stdout, (out/f'{label}.stderr').open('xb') as stderr:
        run = subprocess.run(command, cwd=cwd, stdout=stdout, stderr=stderr, check=False)
    rec.update(exit_code=run.returncode, ended_utc=utc(),
               stdout_sha256=hashfile(out/f'{label}.stdout'), stderr_sha256=hashfile(out/f'{label}.stderr'))
    return rec


def manifest(out):
    files = sorted(p for p in out.rglob('*') if p.is_file() and p != out/'MANIFEST.sha256')
    with (out/'MANIFEST.sha256').open('x') as stream:
        for p in files:
            stream.write(f'{hashfile(p)}  {p.relative_to(out)}\n')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('label')
    parser.add_argument('--initialize', action='store_true')
    parser.add_argument('--runs', type=int, choices=(1, 2), default=2)
    args = parser.parse_args()
    if not args.label.replace('_', '').isalnum():
        raise SystemExit('Unsafe label')
    base = Path(__file__).resolve().parent
    root = base.parents[3]
    out = base/'executions'/args.label
    out.mkdir(parents=True, exist_ok=False)
    receipt = {'schema': 'p207-b-actual-execution-v1', 'started_utc': utc(), 'initialize': args.initialize,
               'commands': [], 'status': 'RUNNING', 'root': str(root), 'directory': str(out)}
    inputs = []
    error = None
    try:
        inputs = pinpaths(base/'INPUT_PINS.sha256', root)
        inputs += pinpaths(base/'CONTEXT_PINS.sha256', root)
        inputs += [base/'verify.py', base/'record_review.py', base/'INPUT_PINS.sha256', base/'CONTEXT_PINS.sha256']
        canonical = base/'CANONICAL.json'
        if not args.initialize:
            inputs.append(canonical)
            shutil.copyfile(canonical, out/'CANONICAL.input.json')
        elif canonical.exists():
            raise RuntimeError('Initial canonical already exists')
        writepins(out/'INPUTS.before.sha256', inputs, root)
        # Python's absolute executable and runtime flags are explicit evidence.
        python = str(Path(sys.executable).resolve())
        receipt['python_binary_sha256'] = hashfile(Path(python))
        probe = execute(out, 'runtime_probe', [python, '-I', '-B', '-c',
            'import json,sys; assert __debug__ and sys.flags.optimize == 0; assert sys.flags.isolated == 1; assert sys.flags.dont_write_bytecode == 1; print(json.dumps({"version":sys.version,"executable":sys.executable,"optimize":sys.flags.optimize,"isolated":sys.flags.isolated,"dont_write_bytecode":sys.flags.dont_write_bytecode,"debug":__debug__},sort_keys=True))'], out)
        receipt['commands'].append(probe)
        if probe['exit_code']:
            raise RuntimeError('Runtime flag probe failed')
        for k in range(1, args.runs+1):
            run_dir = out/f'run{k}_source'
            run_dir.mkdir()
            shutil.copyfile(base/'verify.py', run_dir/'verify.py')
            if hashfile(run_dir/'verify.py') != hashfile(base/'verify.py'):
                raise RuntimeError('Copied checker changed')
            rec = execute(out, f'run{k}', [python, '-I', '-B', str(run_dir/'verify.py')], run_dir)
            receipt['commands'].append(rec)
            if rec['exit_code']:
                raise RuntimeError(f'Producer {k} failed')
            data = json.loads((out/f'run{k}.stdout').read_bytes())
            if data.get('status') != 'PASS' or data.get('assertions', 0) <= 0:
                raise RuntimeError('Producer schema/status failed')
            rec['assertions'] = data['assertions']
            if args.initialize and k == 1:
                with canonical.open('xb') as stream:
                    stream.write((out/'run1.stdout').read_bytes())
                shutil.copyfile(canonical, out/'CANONICAL.input.json')
            comparison = execute(out, f'run{k}.canonical.cmp', ['cmp', str(out/f'run{k}.stdout'), str(out/'CANONICAL.input.json')], out)
            receipt['commands'].append(comparison)
            if comparison['exit_code']:
                raise RuntimeError('Canonical raw comparison failed')
        if args.runs == 2:
            rec = execute(out, 'pair.cmp', ['cmp', str(out/'run1.stdout'), str(out/'run2.stdout')], out)
            receipt['commands'].append(rec)
            if rec['exit_code']:
                raise RuntimeError('Pair raw comparison failed')
        rec = execute(out, 'canonical_live.cmp', ['cmp', str(canonical), str(out/'CANONICAL.input.json')], out)
        receipt['commands'].append(rec)
        if rec['exit_code']:
            raise RuntimeError('Live canonical changed')
        receipt['canonical_sha256'] = hashfile(canonical)
        receipt['status'] = 'PASS'
    except Exception as exc:
        error = repr(exc)
        receipt['status'] = 'FAIL'
        receipt['failure'] = error
    finally:
        if inputs and (out/'INPUTS.before.sha256').exists():
            try:
                writepins(out/'INPUTS.after.sha256', inputs, root)
                rec = execute(out, 'input_pins.cmp', ['cmp', str(out/'INPUTS.before.sha256'), str(out/'INPUTS.after.sha256')], out)
                receipt['commands'].append(rec)
                if rec['exit_code']:
                    receipt['status'] = 'FAIL'
                    receipt['failure'] = 'Runtime input pin drift'
                    error = receipt['failure']
            except Exception as exc:
                receipt['status'] = 'FAIL'
                receipt['pin_failure'] = repr(exc)
                error = error or repr(exc)
        receipt['ended_utc'] = utc()
        save(out/'RECEIPT.json', receipt)
        manifest(out)
    print(json.dumps({'receipt': str(out/'RECEIPT.json'), 'status': receipt['status'], 'failure': error}, sort_keys=True))
    return int(receipt['status'] != 'PASS')


if __name__ == '__main__':
    raise SystemExit(main())
