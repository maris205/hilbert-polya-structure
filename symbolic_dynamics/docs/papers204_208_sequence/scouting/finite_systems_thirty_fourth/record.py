#!/usr/bin/env python3
"""Scoped documentary command recorder; output is never a proof or review."""
import hashlib
import json
import pathlib
import subprocess
import sys
import time

ROOT = pathlib.Path('/root/autodl-tmp/symbolic_dynamics')
OWN = pathlib.Path(__file__).resolve().parent

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def save(path, value):
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + '\n')

def forbidden(path):
    rel = str(path.relative_to(ROOT)).lower()
    parts = pathlib.PurePosixPath(rel).parts
    if path.is_relative_to(OWN):
        return False
    return (any(p in {'qa', 'reviews', 'review', 'freeze', 'freezes', 'build', 'builds',
                     'order_geometry_tenth_desk', 'order_geometry_tenth',
                     'finite_systems_nineteenth', 'finite_systems_twentieth'} for p in parts)
            or any('gate' in p or 'fth' in p or 'ofs' in p for p in parts)
            or any(p.startswith(('208', '209', 'p208', 'p209')) for p in parts)
            or any(p.startswith(('round0', 'round1', 'round2', 'terminal')) for p in parts))

def capture(label, argv, inputs=(), cwd=ROOT):
    out = OWN / 'commands' / label
    out.mkdir(parents=True, exist_ok=False)
    paths = sorted(set([pathlib.Path(__file__).resolve()] + [pathlib.Path(p).resolve() for p in inputs]))
    for path in paths:
        assert not path.is_relative_to(ROOT) or not forbidden(path), str(path)
        assert path.is_file(), str(path)
    save(out / 'pathset.json', [str(p) for p in paths])
    before = {str(p): digest(p) for p in paths}
    save(out / 'inputs_before.json', before)
    started = time.time()
    result = subprocess.run(argv, cwd=cwd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    (out / 'stdout.raw').write_bytes(result.stdout)
    (out / 'stderr.raw').write_bytes(result.stderr)
    after = {str(p): digest(p) for p in paths}
    save(out / 'inputs_after.json', after)
    receipt = dict(role='new_native_command', label=label, argv=argv, cwd=str(cwd),
                   started_epoch=started, finished_epoch=time.time(), exit=result.returncode,
                   input_count=len(paths), unchanged=before == after,
                   stdout_sha256=digest(out / 'stdout.raw'), stderr_sha256=digest(out / 'stderr.raw'))
    save(out / 'receipt.json', receipt)
    print(json.dumps(receipt, sort_keys=True))
    assert before == after
    return result

def discovered(label):
    paths = []
    for line in (OWN / 'commands' / label / 'stdout.raw').read_text().splitlines():
        p = ROOT / line
        assert not forbidden(p), line
        paths.append(p)
    return paths

if __name__ == '__main__':
    mode = sys.argv[1]
    if mode == 'discover_words':
        argv = ['rg', '--files', 'papers', '-g', '**/*word*/main.tex', '-g', '**/*prefix*/main.tex',
                '-g', '**/*border*/main.tex', '-g', '**/*palindrom*/main.tex', '-g', '**/*radius*/main.tex',
                '-g', '**/*run*/main.tex', '-g', '**/*period*/main.tex', '-g', '**/*string*/main.tex']
        argv += ['-g', '!**/208*/**', '-g', '!**/209*/**', '-g', '!**/round*/**',
                 '-g', '!**/freeze*/**', '-g', '!**/build*/**', '-g', '!**/reviews/**', '-g', '!**/qa/**']
        capture('01_word_filenames', argv)
        discovered('01_word_filenames')
    elif mode == 'word_search':
        paths = discovered('01_word_filenames')
        argv = ['rg', '-n', '-i', 'palindrom|suffix|border|prefix|literal|\\\\title|\\\\begin\\{abstract', '--'] + [str(p) for p in paths]
        capture('02_word_body_search', argv, paths)
    elif mode == 'read':
        label = sys.argv[2]
        paths = [ROOT / p for p in sys.argv[3:]]
        capture(label, ['sed', '-n', '1,2000p'] + [str(p) for p in paths], paths)
    elif mode == 'seal':
        target = OWN / 'SHA256SUMS'
        assert not target.exists()
        paths = sorted(p for p in OWN.rglob('*') if p.is_file() and p != target)
        target.write_text(''.join(digest(p) + '  ' + str(p.relative_to(OWN)) + '\n' for p in paths))
        print(json.dumps(dict(nonself_payloads=len(paths), sha256=digest(target))))
    else:
        raise SystemExit('unknown mode')
