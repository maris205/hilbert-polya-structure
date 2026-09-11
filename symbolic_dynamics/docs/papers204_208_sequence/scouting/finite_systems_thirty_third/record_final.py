#!/usr/bin/env python3
"""Final conservative exclusions; earlier recorder and pathsets stay immutable."""
import json
import pathlib
import sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import record_v2 as v2

prior_original = v2.original
def original(p):
    return prior_original(p) and not any('/scouting/' + lane + '/' in p for lane in ('order_geometry_tenth', 'order_geometry_tenth_desk'))

v2.original = original
v2.SELECTED = v2.OWN / 'SELECTED_ORIGINALS_FINAL.json'

if sys.argv[1] == 'verify':
    files = [v2.SELECTED, pathlib.Path(__file__), v2.OWN / 'record_v2.py', v2.OWN / 'record.py']
    inputs = v2.selected() + [str(p.relative_to(v2.ROOT)) for p in files]
    v2.base.run('03_final_actual_paths', [sys.executable, '-I', '-B', str(pathlib.Path(__file__).relative_to(v2.ROOT)), 'verify_paths'], inputs)
else:
    v2.main()
