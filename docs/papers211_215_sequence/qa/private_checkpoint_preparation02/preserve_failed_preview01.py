#!/usr/bin/env python3
"""Preserve the first preparation parser failure source before correction."""
from pathlib import Path
import runpy
import sys

HERE = Path(__file__).resolve().parent
source = HERE / 'checkpoint.py'
m = runpy.run_path(str(source), run_name='failed_preview_source_readonly_helpers')
m['need'](sys.flags.isolated and sys.flags.no_site and sys.dont_write_bytecode, 'Require -I -S -B')
directory = HERE / 'failure_preservation01'
directory.mkdir(exist_ok=False)
command = m['Commands'](directory, 'prepare')
before = m['key'](source)
target = HERE / 'preview01/FAILED_EXECUTOR.py'
command.run(['/usr/bin/cp', '--no-clobber', '--preserve=mode', str(source), str(target)])
command.run(['/usr/bin/cmp', str(source), str(target)])
m['need'](m['key'](source) == before == m['key'](target), 'Failed source preservation differs')
discovery = m['read'](HERE / 'readonly_discovery01/INVENTORY_PREVIEW.json')
m['need'](m['protected_roles']() == discovery['protected_roles'], 'Protected roles changed')
seal = m['finish'](directory, {'status': 'FAILED_PREVIEW_SOURCE_PRESERVED_BEFORE_CORRECTION',
    'source': str(source), 'source_key': before, 'physical_copy': str(target),
    'commands': command.count, 'actual_raw_cmp_equal': True,
    'protected_roles_unchanged_from_readonly_discovery': True,
    'git_mutations': 0, 'scientific_runs': 0})
print(seal)
