#!/usr/bin/env python3
"""Additional exact-string history search; reuses the immutable recorder."""
import pathlib
import sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import record
SELF = pathlib.Path(__file__).resolve()
if sys.argv[1] == 'search':
    paths = record.discovered('03_history_filenames')
    # Duplicated historical copies are unnecessary in this second lookup.
    paths = [p for p in paths if not any(part in {'snapshots', 'history', 'historical_inputs', 'source_inputs'}
                                        or part.startswith('execution_') for part in p.parts)]
    record.capture('06_partition_history_search',
        ['rg', '-n', '-i', 'Kreweras|noncrossing|non.crossing|cyclic.{0,30}partition|genus|cycle.{0,30}standard|canonical.{0,20}cycle', '--']
        + [str(p) for p in paths], [SELF] + paths)
elif sys.argv[1] == 'discover':
    record.capture('07_partition_filenames', ['rg', '--files', 'papers', '-g', '**/*partition*/main.tex',
        '-g', '**/*kreweras*/main.tex', '-g', '**/*noncross*/main.tex', '-g', '**/*stack*/main.tex',
        '-g', '**/*genus*/main.tex', '-g', '**/*cycle*/main.tex',
        '-g', '!**/208*/**', '-g', '!**/209*/**', '-g', '!**/round*/**',
        '-g', '!**/freeze*/**', '-g', '!**/build*/**', '-g', '!**/reviews/**', '-g', '!**/qa/**'], [SELF])
    record.discovered('07_partition_filenames')
else:
    raise SystemExit('bad mode')
