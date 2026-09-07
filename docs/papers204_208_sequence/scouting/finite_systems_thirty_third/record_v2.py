#!/usr/bin/env python3
"""Tighter path-selection adapter; preserves initial discovery and recorder."""
import json
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import record as base

ROOT, OWN = base.ROOT, base.OWN
SELECTED = OWN / 'SELECTED_ORIGINALS_V2.json'

def original(p):
    if not base.original(p):
        return False
    # Gate material may be a reviewer derivation; avoid that entire ambiguity.
    if any('gate' in s.lower() for s in p.split('/')[2:-1]):
        return False
    if 'TITLE' in p.rsplit('/', 1)[1]:
        return False
    # This lane interleaves FTH scientific bodies with other negative scouts.
    if '/scouting/finite_systems_nineteenth/' in p:
        return False
    return True

def selected():
    ps = json.loads(SELECTED.read_text())
    assert ps == sorted(set(ps))
    assert all(original(p) and (ROOT / p).is_file() and not (ROOT / p).is_symlink() for p in ps)
    return ps

def main():
    op = sys.argv[1]
    if op == 'select':
        assert not SELECTED.exists()
        source = OWN / 'commands/01_path_discovery/stdout.raw'
        paths = sorted(p for p in source.read_text().splitlines() if original(p))
        base.save(SELECTED, paths)
        print(json.dumps(dict(selected=len(paths), initial_body_searches=0)))
    elif op == 'verify_paths':
        for p in selected():
            print(p)
        print(json.dumps(dict(actual_paths=len(selected()), all_valid=True)))
    elif op == 'verify':
        inputs = selected() + [str(p.relative_to(ROOT)) for p in (SELECTED, pathlib.Path(__file__), OWN / 'record.py')]
        base.run('02_actual_selected_paths', [sys.executable, '-I', '-B', str(pathlib.Path(__file__).relative_to(ROOT)), 'verify_paths'], inputs)
    elif op == 'search':
        label, pattern = sys.argv[2:4]
        ps = selected()
        base.run(label, ['rg', '-n', '-i', '--', pattern] + ps, ps)
    elif op == 'read':
        label, path = sys.argv[2:4]
        assert original(path) or path.startswith(str(OWN.relative_to(ROOT)) + '/')
        base.run(label, ['sed', '-n', sys.argv[4] if len(sys.argv)>4 else '1,99999p', path], [path])
    else:
        raise SystemExit(op)

if __name__ == '__main__':
    main()
