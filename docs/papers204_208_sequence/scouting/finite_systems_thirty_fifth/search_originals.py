#!/usr/bin/env python3
"""Exact-depth original-only search; stdout is documentary JSON, no writes."""
from hashlib import sha256
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import time

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
BATCH = ROOT / 'docs/papers204_208_sequence'
FORBIDDEN_NAMES = {'FTH_GATE', 'OFS_GATE', 'finite_systems_thirty_third',
                   'finite_systems_thirty_fourth', 'finite_systems_thirty_fifth'}


def pin(path):
    assert path.is_file() and not path.is_symlink() and path.resolve() == path, str(path)
    raw = path.read_bytes()
    return {'sha256': sha256(raw).hexdigest(), 'bytes': len(raw)}


def main():
    assert len(sys.argv) == 2 and sys.flags.optimize == 0 and sys.flags.isolated and sys.flags.no_site and sys.dont_write_bytecode
    assert Path.cwd() == ROOT
    selection = []
    for directory in sorted((ROOT / 'papers').iterdir()):
        match = re.match(r'^(\d+)-', directory.name)
        if not directory.is_dir() or not match or not 57 <= int(match.group(1)) <= 207:
            continue
        selection.extend(directory / n for n in ('README.md', 'main.tex', 'PROOF_PACKAGE.md') if (directory / n).is_file())
    for directory in sorted((BATCH / 'scouting').iterdir()):
        if not directory.is_dir() or directory.name in FORBIDDEN_NAMES:
            continue
        selection.extend(p for p in sorted(directory.iterdir()) if p.is_file() and p.suffix == '.md'
                         and not any(t in p.name.upper() for t in ('FTH', 'OFS', 'P208', 'P209')))
    for directory in sorted((ROOT / 'docs').iterdir()):
        if directory.is_dir() and re.fullmatch(r'papers\d+_\d+_sequence', directory.name):
            selection.extend(directory / n for n in ('BREADTH_LEDGER.md', 'TITLE_COLLISION_INVENTORY.md', 'KILL_LEDGER.md')
                             if (directory / n).is_file())
    selection = sorted(set(selection))
    assert selection and all(not set(p.relative_to(ROOT).parts) & {'qa', 'frozen_round0', 'frozen_round1', 'frozen_round2', 'reviews', 'runtime'} for p in selection)
    before = {str(p): pin(p) for p in selection}
    command = ['/usr/bin/rg', '-n', '-i', '--no-heading', '--', sys.argv[1], *map(str, selection)]
    child = subprocess.run(command, cwd=ROOT, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False)
    after = {str(p): pin(p) for p in selection}
    assert child.returncode in (0, 1) and not child.stderr and before == after
    print(json.dumps({'schema': 'scout35-exact-depth-original-history-search-v1',
          'scope': 'Only explicit top-level original files. No descendant QA/freeze/build/runtime traversal or mathematical execution.',
          'finished_epoch': time.time(), 'selection_count': len(selection), 'selection_depth_rule': {
              'papers': 'papers/<57..207-slug>/{README.md,main.tex,PROOF_PACKAGE.md} only',
              'scouting': 'current-batch/scouting/<nonexcluded-lane>/*.md immediate files only',
              'ledgers': 'docs/papersN_M_sequence/{BREADTH_LEDGER.md,TITLE_COLLISION_INVENTORY.md,KILL_LEDGER.md} only'},
          'argv': command, 'cwd': str(ROOT), 'environment': dict(os.environ), 'exit': child.returncode,
          'stdout': child.stdout.decode(), 'stderr': child.stderr.decode(),
          'inputs_before': before, 'inputs_after': after, 'inputs_unchanged': True,
          'tool': {'path': '/usr/bin/rg', **pin(Path('/usr/bin/rg'))},
          'searcher': {'path': str(Path(__file__).resolve()), **pin(Path(__file__).resolve())}}, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
