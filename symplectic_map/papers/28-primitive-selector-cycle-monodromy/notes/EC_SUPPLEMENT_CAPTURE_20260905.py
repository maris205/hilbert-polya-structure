#!/root/miniconda3/bin/python3.12
"""Capture the single demonstrated missing EC TFM; never compile or retry."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import stat
import sys

PROJECT = Path('/root/autodl-tmp/symplectic_map/papers/28-primitive-selector-cycle-monodromy')
NOTES = PROJECT / 'notes'
OUTPUT = NOTES / 'dependency-ec-supplement-20260905'
TARGET = '/usr/share/texlive/texmf-dist/fonts/tfm/jknappen/ec/ecrm1095.tfm'
CONTROLS = ('EC_SUPPLEMENT_CAPTURE_20260905.py', 'EC_SUPPLEMENT_PLAN_20260905.md')
REVIEW = NOTES / 'EC_SUPPLEMENT_CAPTURE_REVIEW_20260905.json'
BUDGET = 4096
EXPECTED_SIZE = 3584
SOURCE = {
 'main.tex': ('bdc7a1edc06b3f8cfc75c6b47a8c24180883d24eef878c70d857588d19f1762e', 73733, 1605),
 'math_commands.tex': ('16b1e55f52f21b63811a0d34eb64eba955533334f8e5f58005841d6da0a85ce5', 444, 14),
 'references.bib': ('e6a6bdb24a7db3a75b481c8363aa7733cb3dd4c1e8a121d9d9526eb83228882e', 6104, 204),
}
READ = os.O_RDONLY | os.O_NOFOLLOW | os.O_CLOEXEC | os.O_NONBLOCK
DIRECTORY = os.O_RDONLY | os.O_NOFOLLOW | os.O_CLOEXEC | os.O_DIRECTORY


def require(ok, message):
    if not ok:
        raise RuntimeError(message)


def identity(data):
    return {'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()}


def metadata(s):
    return {'dev': s.st_dev, 'ino': s.st_ino, 'size': s.st_size,
            'mode': stat.S_IMODE(s.st_mode), 'uid': s.st_uid, 'gid': s.st_gid,
            'mtime_ns': s.st_mtime_ns, 'ctime_ns': s.st_ctime_ns,
            'nlink': s.st_nlink}


def read_local(path):
    with os.fdopen(os.open(path, READ), 'rb') as stream:
        before = os.fstat(stream.fileno())
        require(stat.S_ISREG(before.st_mode), 'local input not regular')
        data = stream.read()
        require(metadata(before) == metadata(os.fstat(stream.fileno())), 'local input changed')
        return data


def write_new(path, data):
    with os.fdopen(os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL |
                          os.O_NOFOLLOW | os.O_CLOEXEC, 0o600), 'wb') as stream:
        stream.write(data)
        stream.flush()
        os.fsync(stream.fileno())


def json_new(path, value):
    write_new(path, (json.dumps(value, sort_keys=True, indent=2) + '\n').encode())


def sources():
    result = {}
    for name, (sha, size, lf) in SOURCE.items():
        data = read_local(PROJECT / 'paper' / name)
        require((identity(data)['sha256'], len(data), data.count(b'\n')) ==
                (sha, size, lf), 'source binding mismatch: ' + name)
        result[name] = {'sha256': sha, 'bytes': size, 'lf': lf}
    return result


def bindings():
    return {name: identity(read_local(NOTES / name)) for name in CONTROLS}


def budget_check(s):
    require(stat.S_ISREG(s.st_mode), 'target not regular')
    require(s.st_size == EXPECTED_SIZE and 0 < s.st_size <= BUDGET,
            'target size changed or exceeds pre-read budget')
    require(stat.S_IMODE(s.st_mode) == 0o644 and s.st_uid == s.st_gid == 0,
            'target metadata differs from read-only diagnostic')


def open_target():
    """Metadata-only traversal; all physical components reject symlinks."""
    parts = TARGET[1:].split('/')
    parent = os.open('/', DIRECTORY)
    try:
        for part in parts[:-1]:
            child = os.open(part, DIRECTORY, dir_fd=parent)
            os.close(parent)
            parent = child
        before = os.stat(parts[-1], dir_fd=parent, follow_symlinks=False)
        budget_check(before)
        descriptor = os.open(parts[-1], READ, dir_fd=parent)
        try:
            require(metadata(os.fstat(descriptor)) == metadata(before), 'target changed during open')
        except BaseException:
            os.close(descriptor)
            raise
        return descriptor, before
    finally:
        os.close(parent)


def run(review_sha):
    require(sys.flags.isolated and sys.flags.no_site and sys.dont_write_bytecode,
            'run administrative Python with -I -S -B')
    current_bindings, source_before = bindings(), sources()
    review_data = read_local(REVIEW)
    require(identity(review_data)['sha256'] == review_sha, 'review hash mismatch')
    review = json.loads(review_data)
    require(review.get('decision') == 'EC_SUPPLEMENT_CAPTURE_REVIEW_PASS' and
            review.get('bindings') == current_bindings and
            review.get('sources') == source_before and review.get('target') == TARGET and
            review.get('budget_bytes') == BUDGET, 'review does not bind this capture')
    # One new directory, no previous output probe or retry.
    OUTPUT.mkdir(mode=0o700)
    stage = 'intent'
    bytes_read = 0
    try:
        json_new(OUTPUT / 'intent.json', {'target': TARGET, 'budget_bytes': BUDGET,
                 'expected_size': EXPECTED_SIZE, 'bindings': current_bindings,
                 'sources': source_before, 'review_sha256': review_sha,
                 'scope': 'one EC TFM; no subprocess, install, source edit or build'})
        write_new(OUTPUT / 'independent-review.json', review_data)
        stage = 'target-metadata'
        json_new(OUTPUT / 'attempt.json', {'target': TARGET, 'byte_budget_before_open': BUDGET})
        descriptor, before = open_target()
        with os.fdopen(descriptor, 'rb', buffering=0) as stream:
            json_new(OUTPUT / 'metadata-before.json', metadata(before))
            # Exact admitted byte count; never read rejected or speculative bytes.
            stage = 'target-read'
            chunks = []
            while bytes_read < before.st_size:
                part = stream.read(before.st_size - bytes_read)
                require(bool(part), 'short target read')
                chunks.append(part)
                bytes_read += len(part)
            data = b''.join(chunks)
            after = os.fstat(stream.fileno())
            require(metadata(before) == metadata(after), 'target mutated during capture')
        stage = 'snapshot-write'
        write_new(OUTPUT / 'ecrm1095.tfm', data)
        json_new(OUTPUT / 'metadata-after.json', metadata(after))
        require(bindings() == current_bindings and sources() == source_before,
                'source/control changed during capture')
        names = ('intent.json', 'independent-review.json', 'attempt.json',
                 'metadata-before.json', 'metadata-after.json', 'ecrm1095.tfm')
        outputs = {name: identity(read_local(OUTPUT / name)) for name in names}
        json_new(OUTPUT / 'outcome.json', {
            'decision': 'EC_METRIC_CAPTURED_AUDIT_PENDING', 'source_path': TARGET,
            'budget_bytes': BUDGET, 'host_bytes_read': bytes_read,
            'sources': source_before, 'bindings': current_bindings,
            'file': {**identity(data), 'lf': data.count(b'\n'), 'mode': '0o644'},
            'outputs': outputs, 'no_retry': True})
        print(json.dumps({'decision': 'EC_METRIC_CAPTURED_AUDIT_PENDING',
                          'root': str(OUTPUT), 'file': identity(data)}), flush=True)
        return 0
    except BaseException as exc:
        json_new(OUTPUT / 'failure.json', {'decision': 'CAPTURE_FAILED_PRESERVED',
                 'stage': stage, 'type': type(exc).__name__, 'error': str(exc),
                 'target': TARGET, 'host_bytes_read': bytes_read, 'no_retry': True})
        print(json.dumps({'decision': 'CAPTURE_FAILED_PRESERVED', 'stage': stage,
                          'error': str(exc), 'root': str(OUTPUT)}), flush=True)
        return 1


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--review-sha256', required=True)
    args = parser.parse_args()
    require(len(args.review_sha256) == 64 and
            all(c in '0123456789abcdef' for c in args.review_sha256), 'invalid review hash')
    return run(args.review_sha256)


if __name__ == '__main__':
    raise SystemExit(main())
