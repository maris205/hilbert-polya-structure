#!/usr/bin/python3.10
"""Read-only exact paper-input check before root submits P210 B no-change delta.

Adapted from the existing A response checker, without executing native commands.
Full Python byte equality is explicitly not a new native cmp or science run.
"""
from pathlib import Path
from hashlib import sha256
import json
import os
import re
import sys

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
QA = ROOT / 'docs/papers204_208_sequence/qa'
PAPER = ROOT / 'papers/210-weakly-increasing-run-aggregation'
REVIEW = ROOT / 'docs/papers204_208_sequence/reviews/p210_b'
FROZEN = PAPER / 'frozen_round1'
ENV = {'PATH': '/usr/bin:/bin', 'LANG': 'C.UTF-8', 'LC_ALL': 'C.UTF-8', 'TZ': 'UTC'}
SEALS = {
    'review': '81b5f97a6b25d6f9e82db87001da1a54668c01268038694d4b8a3b61006b02c3',
    'round1': 'be54b79806d90f22037cee877f92074e744b2ef27bcc0b6b2e4f8dfa658446e0',
    'round0': 'e8446cd17b1a283c74f9a6b4ced413b9e30810396c3d30f936ac2986ce790e26',
    'author': 'b0c72e401acaf50acb611dc27f2ff1c45e3ad6e1b547218b48d13be8c82a0f6c',
    'whole': 'a1abc5b290ed6a74cb6f8b1fb959f479d84926886ff9ce0b8d8179b806e6c94f',
}
CURRENT, TREES = {}, {}
CHECKS = RAW_COMPARISONS = 0


def need(ok, message):
    global CHECKS
    CHECKS += 1
    if not ok:
        raise AssertionError(message)


def read(path):
    path = Path(path)
    need(path.is_file() and path.resolve() == path and not path.is_symlink(), ('physical_file', str(path)))
    data = path.read_bytes()
    key = {'resolved': str(path.resolve()), 'symlink': None, 'bytes': len(data), 'sha256': sha256(data).hexdigest()}
    need(str(path) not in CURRENT or CURRENT[str(path)] == key, ('unchanged_read_key', str(path)))
    CURRENT[str(path)] = key
    return data


def physical(directory):
    entries = list(directory.rglob('*'))
    need(directory.resolve() == directory and all(not p.is_symlink() for p in entries), ('physical_tree', str(directory)))
    names = {p.relative_to(directory).as_posix() for p in entries if p.is_file()}
    need(str(directory) not in TREES or TREES[str(directory)] == names, ('stable_membership', str(directory)))
    TREES[str(directory)] = names
    return names


def rows(directory, filename, expected, count, complete):
    seal = directory / filename
    data = read(seal)
    need(sha256(data).hexdigest() == expected and data.endswith(b'\n'), ('exact_seal', str(seal)))
    result = {}
    for line in data.decode().splitlines():
        m = re.fullmatch(r'([0-9a-f]{64})  (.+)', line)
        need(m is not None, ('strict_manifest_syntax', str(seal)))
        digest, name = m.groups()
        p = Path(name)
        need(p.parts and not p.is_absolute() and '..' not in p.parts and p.as_posix() == name and name != filename and name not in result,
             ('unique_safe_nonself_member', name))
        need(sha256(read(directory / name)).hexdigest() == digest, ('payload_digest', name))
        result[name] = digest
    need(len(result) == count, ('exact_manifest_count', str(seal), len(result), count))
    if complete:
        need(set(result) == physical(directory) - {filename}, ('full_nonself_inventory', str(directory)))
    return result


def equal(a, b):
    global RAW_COMPARISONS
    need(read(a) == read(b), ('full_python_raw_byte_equality', str(a), str(b)))
    RAW_COMPARISONS += 1


def main():
    need(Path(__file__) == QA / 'check_p210_b_response.py' and Path.cwd() == ROOT and
         Path(sys.executable).resolve() == Path('/usr/bin/python3.10') and dict(os.environ) == ENV and
         sys.flags.isolated == sys.flags.no_site == 1 and sys.flags.dont_write_bytecode and not sys.flags.optimize,
         'exact_readonly_root_source_interpreter_environment_cwd')
    cache = QA / 'p210_b_nochange_unused_cache'
    need(sys.pycache_prefix == str(cache) and not os.path.lexists(cache), 'explicit_absent_cache')
    read(Path(__file__))
    review = rows(REVIEW, 'SHA256SUMS', SEALS['review'], 407, True)
    frozen = rows(FROZEN, 'SHA256SUMS', SEALS['round1'], 508, True)
    old = rows(PAPER / 'frozen_round0', 'SHA256SUMS', SEALS['round0'], 493, True)
    author = rows(PAPER, 'AUTHOR_MANIFEST.sha256', SEALS['author'], 489, False)
    whole = rows(PAPER, 'PAPER_MANIFEST.sha256', SEALS['whole'], 1496, True)
    need(sha256(read(PAPER / 'ROOT_LIFECYCLE.md')).hexdigest() ==
         'd1548b317d0575c4ab8c95912f9154786df79763aeebcbe63daa832de0430a7d', 'exact_pre_B_response_lifecycle')
    equal(PAPER / 'SHA256SUMS', PAPER / 'AUTHOR_MANIFEST.sha256')
    equal(PAPER / 'AUTHOR_MANIFEST.sha256', FROZEN / 'AUTHOR_MANIFEST.sha256')
    for name, digest in author.items():
        need(frozen[name] == old[name] == digest, ('unchanged_author_role', name))
        equal(PAPER / name, FROZEN / name)
    for name, digest in old.items():
        need(frozen[name] == digest, ('unchanged_Round0_core_role', name))
        equal(PAPER / 'frozen_round0' / name, FROZEN / name)
    pins = rows(ROOT, 'docs/papers204_208_sequence/reviews/p210_b/INPUT_PINS.sha256',
                'c166030721b74b211c79e529db610c2e1c48221b355f4cc79f7aa71c62950b21', 509, False)
    expected = {str((FROZEN / name).relative_to(ROOT)): digest for name, digest in frozen.items()}
    expected[str((FROZEN / 'SHA256SUMS').relative_to(ROOT))] = SEALS['round1']
    need(pins == expected, 'all_and_only_509_physical_reviewed_Round1_inputs')
    for directory in list(TREES):
        physical(Path(directory))
    keys = sorted(CURRENT)
    for name in keys:
        read(name)
    need(not os.path.lexists(cache), 'cache_still_absent')
    print(json.dumps({'status': 'PASS_EXACT_NO_SCIENTIFIC_OR_PAPER_CHANGE_BEFORE_B_RESPONSE',
          'checks': CHECKS, 'current_paths_reread': len(keys),
          'complete_key_digest': sha256(json.dumps(CURRENT, sort_keys=True, separators=(',', ':')).encode()).hexdigest(),
          'seals': SEALS, 'author_payloads': len(author), 'round0_core_payloads': len(old),
          'round1_payloads': len(frozen), 'whole_paper_payloads': len(whole), 'initial_b_payloads': len(review),
          'full_python_raw_comparisons': RAW_COMPARISONS, 'new_native_child_commands': 0,
          'science_executions': 0, 'tex_builds': 0, 'new_views': 0, 'reviewer_delta_accepted': False,
          'paper_complete': False, 'owner': 'OWNER_AMBER', 'external': 'HOLD_EXTERNAL'}, sort_keys=True))


if __name__ == '__main__':
    main()
