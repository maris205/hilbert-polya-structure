#!/usr/bin/env python3
"""Disclosed token-aware path adapter; original recorder remains immutable."""
import pathlib
import re
import sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import record
SELF = pathlib.Path(__file__).resolve()

def forbidden(path):
    if path.is_relative_to(record.OWN):
        return False
    parts = path.relative_to(record.ROOT).parts
    for part in parts:
        p = part.lower()
        if p in {'qa', 'reviews', 'review', 'freeze', 'freezes', 'build', 'builds'}:
            return True
        if 'gate' in p or p.startswith(('fth', 'ofs', '208', '209', 'p208', 'p209', 'round0', 'round1', 'round2', 'terminal')):
            return True
        if re.search(r'(^|[^a-z0-9])(fth|ofs)([^a-z0-9]|$)', p):
            return True
    return False

record.forbidden = forbidden

if __name__ == '__main__':
    base = record.ROOT / 'docs/papers204_208_sequence/scouting'
    mode = sys.argv[1]
    if mode == 'discover_rest':
        rows = [('06_orr_second_filenames', 'ORR_SECOND_CLOCK_ATTEMPT'),
                ('07_ned_filenames', 'finite_systems_twenty_first'),
                ('08_ctm_filenames', 'finite_systems_twenty_eighth'),
                ('09_gcf_filenames', 'finite_systems_twenty_seventh')]
        for label, directory in rows:
            cwd = base / directory
            result = record.capture(label, ['rg', '--files', '-g', '/*.md'], [SELF], cwd=cwd)
            assert result.returncode in (0, 1)
            for line in result.stdout.decode().splitlines():
                p = cwd / line
                assert p.parent == cwd and not forbidden(p), str(p)
    elif mode == 'read':
        label = sys.argv[2]
        paths = [record.ROOT / p for p in sys.argv[3:]]
        result = record.capture(label, ['sed', '-n', '1,4000p'] + [str(p) for p in paths], [SELF] + paths)
        assert result.returncode == 0
    elif mode == 'test':
        for suffix in ['qa/x.md', 'reviews/x.md', 'FTH_SOURCE.md', 'OFS_PROOF.md',
                       'FTH_GATE/x.md', 'OFS_GATE/x.md', 'P208_SOURCE.md', 'P209_SOURCE.md',
                       'freeze/x.md', 'build/x.md', 'round0/x.md']:
            assert forbidden(base / suffix), suffix
        assert not forbidden(base / 'finite_systems_twenty_second/PRECODE_PROOFS.md')
        print('11 protected representative names denied; PRECODE_PROOFS.md allowed; no body read')
    else:
        raise SystemExit('bad mode')
