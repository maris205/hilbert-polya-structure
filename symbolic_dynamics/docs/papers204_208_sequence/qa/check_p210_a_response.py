#!/usr/bin/python3.10
"""Read-only exact no-change check before submitting P210's initial A response."""
from pathlib import Path
import hashlib
import json
import subprocess
import sys

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
PAPER = ROOT / 'papers/210-weakly-increasing-run-aggregation'
REVIEW = ROOT / 'docs/papers204_208_sequence/reviews/p210_a'
FROZEN = PAPER / 'frozen_round0'
SEALS = {'review': 'e60d352a6520dd5f56b01035912ce753bb1a669c7368ce0a999ff56a72ff966d',
         'round0': 'e8446cd17b1a283c74f9a6b4ced413b9e30810396c3d30f936ac2986ce790e26',
         'author': 'b0c72e401acaf50acb611dc27f2ff1c45e3ad6e1b547218b48d13be8c82a0f6c',
         'whole': '9c092df8a673debea2697f6213e92002b8fb575b336a8821f5c18fdb0a79e727'}
CURRENT = {}
CHECKS = 0

def require(ok, message):
    global CHECKS
    CHECKS += 1
    if not ok:
        raise AssertionError(message)

def read(path):
    path = Path(path)
    data = path.read_bytes()
    key = {'resolved': str(path.resolve()), 'symlink': path.is_symlink(),
           'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()}
    if str(path) in CURRENT:
        require(CURRENT[str(path)] == key, 'input changed: ' + str(path))
    CURRENT[str(path)] = key
    return data

def manifest(directory, name, expected, count, physical):
    seal = directory / name
    data = read(seal)
    require(hashlib.sha256(data).hexdigest() == expected, 'exact seal ' + str(seal))
    rows = {}
    for line in data.decode().splitlines():
        digest, rel = line.split('  ', 1)
        require(len(digest) == 64 and not Path(rel).is_absolute() and '..' not in Path(rel).parts and rel not in rows,
                'strict unique relative manifest path')
        require(hashlib.sha256(read(directory / rel)).hexdigest() == digest, 'manifest payload ' + rel)
        rows[rel] = digest
    require(len(rows) == count, 'complete declared manifest count')
    if physical:
        require(set(rows) == {str(p.relative_to(directory)) for p in directory.rglob('*') if p.is_file() and p != seal},
                'exact full physical manifest membership')
    return rows

def main():
    require(sys.flags.isolated and sys.flags.no_site and sys.flags.dont_write_bytecode and not sys.flags.optimize,
            'isolated no-site unoptimized read-only interpreter')
    review = manifest(REVIEW, 'SHA256SUMS', SEALS['review'], 484, True)
    frozen = manifest(FROZEN, 'SHA256SUMS', SEALS['round0'], 493, True)
    author = manifest(PAPER, 'AUTHOR_MANIFEST.sha256', SEALS['author'], 489, False)
    manifest(PAPER, 'PAPER_MANIFEST.sha256', SEALS['whole'], 987, True)
    require(read(PAPER / 'SHA256SUMS') == read(PAPER / 'AUTHOR_MANIFEST.sha256') == read(FROZEN / 'AUTHOR_MANIFEST.sha256'),
            'exact original author-scope aliases')
    for rel, digest in author.items():
        require(frozen[rel] == digest and read(PAPER / rel) == read(FROZEN / rel), 'every489 original live/frozen byte unchanged')
    pins = read(REVIEW / 'INPUT_PINS.sha256').decode().splitlines()
    require(len(pins) == 494, 'all494 reviewed freeze inputs')
    for line in pins:
        digest, rel = line.split('  ', 1)
        require(hashlib.sha256(read(ROOT / rel)).hexdigest() == digest, 'all reviewed inputs unchanged')
    native = []
    for rel in ('verify.py', 'CANONICAL.json', 'main.pdf', 'AUTHOR_MANIFEST.sha256'):
        argv = ['/usr/bin/cmp', str(PAPER / rel), str(FROZEN / rel)]
        result = subprocess.run(argv, cwd=ROOT, env={'PATH': '/usr/bin:/bin', 'LANG': 'C', 'LC_ALL': 'C', 'TZ': 'UTC'},
                                capture_output=True, timeout=60, check=False)
        native.append({'argv': argv, 'cwd': str(ROOT), 'environment': {'PATH': '/usr/bin:/bin', 'LANG': 'C', 'LC_ALL': 'C', 'TZ': 'UTC'},
                       'exit_code': result.returncode, 'stdout': result.stdout.decode(), 'stderr': result.stderr.decode()})
        require(result.returncode == 0 and not result.stdout and not result.stderr, 'actual full raw cmp ' + rel)
    keys = sorted(CURRENT)
    for key in keys:
        read(key)
    print(json.dumps({'status': 'PASS_EXACT_NO_SCIENTIFIC_OR_PAPER_CHANGE_BEFORE_A_RESPONSE', 'checks': CHECKS,
                      'current_paths_reread': len(keys), 'complete_key_digest': hashlib.sha256(json.dumps(CURRENT, sort_keys=True).encode()).hexdigest(),
                      'seals': SEALS, 'author_payloads': len(author), 'round0_payloads': len(frozen), 'initial_a_payloads': len(review),
                      'actual_native_raw_comparisons': native, 'science_executions': 0, 'tex_builds': 0, 'new_views': 0,
                      'reviewer_delta_accepted': False, 'paper_complete': False}, sort_keys=True))

if __name__ == '__main__':
    main()
