#!/usr/bin/env python3
"""Six named legacy candidates only, using direct-directory filename globs."""
import pathlib
import sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import record
SELF = pathlib.Path(__file__).resolve()
BASE = record.ROOT / 'docs/papers204_208_sequence/scouting'
rows = [
    ('03_hvd_filenames', 'word_local/HVD_PROOF_WORK', ['/*.md']),
    ('04_ncc_filenames', 'word_local', ['/NCC*.md']),
    ('05_orr_initial_filenames', 'finite_systems_twenty_second', ['/*.md']),
    ('06_orr_second_filenames', 'ORR_SECOND_CLOCK_ATTEMPT', ['/*.md']),
    ('07_ned_filenames', 'finite_systems_twenty_first', ['/*.md']),
    ('08_ctm_filenames', 'finite_systems_twenty_eighth', ['/*.md']),
    ('09_gcf_filenames', 'finite_systems_twenty_seventh', ['/*.md']),
]
for label, directory, globs in rows:
    cwd = BASE / directory
    assert not record.forbidden(cwd)
    argv = ['rg', '--files']
    for pattern in globs:
        argv += ['-g', pattern]
    result = record.capture(label, argv, [SELF], cwd=cwd)
    assert result.returncode in (0, 1)
    for line in result.stdout.decode().splitlines():
        p = cwd / line
        assert p.parent == cwd and not record.forbidden(p), str(p)
