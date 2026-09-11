#!/usr/bin/env python3
"""Append-only documentary recorder. No mathematical producer is imported."""
import hashlib
import json
import pathlib
import subprocess
import sys
import time

ROOT = pathlib.Path('/root/autodl-tmp/symbolic_dynamics')
OWN = ROOT / 'docs/papers204_208_sequence/scouting/finite_systems_thirty_first'

def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def run(label, argv, inputs=()):
    out = OWN / 'commands' / label
    out.mkdir(parents=True, exist_ok=False)
    paths = [ROOT / p for p in inputs]
    pins = {str(p.relative_to(ROOT)): digest(p) for p in paths}
    (out / 'inputs_before.json').write_text(json.dumps(pins, indent=2) + '\n')
    start = time.time()
    proc = subprocess.run(argv, cwd=ROOT, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    (out / 'stdout.raw').write_bytes(proc.stdout)
    (out / 'stderr.raw').write_bytes(proc.stderr)
    after = {str(p.relative_to(ROOT)): digest(p) for p in paths}
    (out / 'inputs_after.json').write_text(json.dumps(after, indent=2) + '\n')
    record = dict(label=label, argv=argv, cwd=str(ROOT), exit=proc.returncode,
                  started_epoch=start, finished_epoch=time.time(),
                  input_count=len(paths), unchanged=pins == after,
                  recorder_sha256=digest(pathlib.Path(__file__)),
                  stdout_sha256=hashlib.sha256(proc.stdout).hexdigest(),
                  stderr_sha256=hashlib.sha256(proc.stderr).hexdigest())
    (out / 'receipt.json').write_text(json.dumps(record, indent=2) + '\n')
    print(json.dumps(record))
    return proc

def original(p):
    parts = p.casefold().split('/')
    bad = ('p208', 'p209', 'paper208', 'paper209', 'ofs', 'fth')
    if any(any(x in v for x in bad) for v in parts):
        return False
    forbidden = ('review', 'qa', 'freez', 'frozen', 'snapshot', 'runtime',
                 'generated', 'extracted', 'command', 'search', 'history',
                 'historical', 'source', 'cache', 'postcheck', 'execution',
                 'replay', 'terminal', 'controls', 'input', 'archive', 'assets')
    if any(any(x in v for x in forbidden) for v in parts[:-1]):
        return False
    if any(x in parts for x in ('order_geometry_tenth', 'order_geometry_tenth_desk',
                              'finite_systems_tenth', 'finite_systems_nineteenth',
                              'finite_systems_thirty_first')):
        return False
    if p.startswith('docs/papers204_208_sequence/') and not p.startswith('docs/papers204_208_sequence/scouting/'):
        return False
    name = parts[-1]
    if p.startswith('papers/') and name.endswith('.tex'):
        return True
    return name.endswith('.md') and any(x in name for x in ('proof', 'scout_report', 'kill', 'candidate_ledger', 'intake', 'disposition', 'handoff', 'collision', 'theorem', 'dossier')) and not any(x in name for x in ('root_inspection', 'receipt', 'source', 'canonical', 'input', 'search', 'snapshot', 'history'))

def main():
    op = sys.argv[1]
    if op == 'discover':
        argv = ['rg', '--files', 'papers', 'docs', '-g', '*.md', '-g', '*.tex']
        for pattern in ('**/reviews/**', '**/qa/**', '**/*frozen*/**', '**/*freez*/**', '**/*snapshot*/**', '**/*runtime*/**', '**/*generated*/**', '**/*extracted*/**', '**/*commands*/**', '**/*search*/**', '**/*history*/**', '**/*historical*/**', '**/*sources*/**', '**/controls/**', '**/order_geometry_tenth/**', '**/order_geometry_tenth_desk/**', '**/finite_systems_tenth/**', '**/finite_systems_nineteenth/**', '**/finite_systems_thirty_first/**'):
            argv += ['-g', '!' + pattern]
        for pattern in ('*p208*', '*p209*', '*paper208*', '*paper209*', '*ofs*', '*fth*'):
            argv += ['--iglob', '!' + pattern]
        result = run('01_discovery', argv)
        listed = result.stdout.decode().splitlines()
        selected = sorted(p for p in listed if original(p))
        (OWN / 'SELECTED_ORIGINALS.json').write_text(json.dumps(selected, indent=2) + '\n')
        print(json.dumps(dict(discovered=len(listed), selected=len(selected))))
    elif op == 'search':
        label, pattern = sys.argv[2:4]
        selected = json.loads((OWN / 'SELECTED_ORIGINALS.json').read_text())
        run(label, ['rg', '-n', '-i', '--', pattern] + selected, selected)
    elif op == 'read':
        label, path = sys.argv[2:4]
        if not original(path) and not path.startswith(str(OWN.relative_to(ROOT)) + '/'):
            raise SystemExit('Read target outside original-only policy')
        run(label, ['sed', '-n', sys.argv[4] if len(sys.argv)>4 else '1,99999p', path], [path])
    elif op == 'command':
        label = sys.argv[2]
        run(label, sys.argv[3:])
    elif op == 'seal':
        paths = sorted(p for p in OWN.rglob('*') if p.is_file() and p != OWN / 'SHA256SUMS')
        target = OWN / 'SHA256SUMS'
        if target.exists():
            raise SystemExit('Manifest already exists; preserve historical version before any replacement')
        target.write_text(''.join(digest(p) + '  ' + str(p.relative_to(OWN)) + '\n' for p in paths))
        print(json.dumps(dict(payloads=len(paths), sha256=digest(target))))
    else:
        raise SystemExit(op)

if __name__ == '__main__':
    main()
