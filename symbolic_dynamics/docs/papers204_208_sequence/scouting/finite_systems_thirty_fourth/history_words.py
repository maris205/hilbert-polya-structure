#!/usr/bin/env python3
"""Word-mechanism history lookup over a narrowly selected body grammar."""
import pathlib
import sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import record

SELF = pathlib.Path(__file__).resolve()
if sys.argv[1] == 'discover':
    argv = ['rg', '--files', 'docs/papers204_208_sequence/scouting',
            '-g', '**/*SCOUT*REPORT*.md', '-g', '**/PROOF_PACKAGE.md',
            '-g', '**/SLATE.md', '-g', '**/SOURCE_AND_COLLISION.md',
            '-g', '**/DERIVATION_PACKAGE.md', '-g', '**/word_local/*.md',
            '-g', '**/*PROOF_PACKAGE.md']
    for pattern in ['**/qa/**', '**/reviews/**', '**/review/**', '**/*GATE*/**',
                    '**/*gate*/**', '**/*FTH*/**', '**/*fth*/**', '**/*OFS*/**', '**/*ofs*/**',
                    '**/208*/**', '**/209*/**', '**/p208*/**', '**/p209*/**',
                    '**/P208*/**', '**/P209*/**', '**/*freeze*/**', '**/*FREEZE*/**',
                    '**/round*/**', '**/Round*/**', '**/*build*/**', '**/*BUILD*/**',
                    '**/order_geometry_tenth_desk/**', '**/order_geometry_tenth/**',
                    '**/finite_systems_nineteenth/**', '**/finite_systems_twentieth/**',
                    '**/finite_systems_thirty_fourth/**']:
        argv += ['-g', '!' + pattern]
    record.capture('03_history_filenames', argv, [SELF])
    record.discovered('03_history_filenames')
elif sys.argv[1] == 'search':
    paths = record.discovered('03_history_filenames')
    argv = ['rg', '-n', '-i', 'palindrom|longest.{0,30}suffix|suffix.{0,30}length|PSL|LPS|palindrome.{0,30}array', '--']
    argv += [str(p) for p in paths]
    record.capture('04_history_palindrome_search', argv, [SELF] + paths)
else:
    raise SystemExit('bad mode')
