#!/usr/bin/env python3
"""One original primary-page render to check the printed cover convention."""
import pathlib
import sys
sys.dont_write_bytecode = True
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import record

source = record.OWN / 'sources/poset_whirling/body.raw'
stem = record.OWN / 'sources/poset_whirling/printed_page7'
assert not stem.with_suffix('.png').exists()
run = record.capture('poset_whirling_page7', ['pdftoppm', '-f', '7', '-l', '7', '-r', '130',
    '-png', '-singlefile', str(source), str(stem)], [pathlib.Path(__file__).resolve(), source])
raise SystemExit(run.returncode)
