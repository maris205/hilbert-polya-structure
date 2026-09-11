#!/usr/bin/env python3
"""Capture pure/static and author artifact checks only, never a Git phase."""
from pathlib import Path
import runpy
import sys

HERE = Path(__file__).resolve().parent
m = runpy.run_path(str(HERE / 'checkpoint.py'), run_name='readonly_check_recorder')
m['need'](sys.flags.isolated and sys.flags.no_site and sys.dont_write_bytecode, 'Require -I -S -B')
directory = HERE / 'readonly_checks01'
directory.mkdir(exist_ok=False)
command = m['Commands'](directory, 'prepare')
try:
    sources = {n: m['key'](HERE / n) for n in
               ('checkpoint.py', 'pure_checks.py', 'inspect_preparation.py', 'run_readonly_checks.py')}
    command.run(['/usr/bin/python3', '-I', '-S', '-B', str(HERE / 'pure_checks.py')])
    command.run(['/usr/bin/python3', '-I', '-S', '-B', str(HERE / 'inspect_preparation.py')])
    m['need'](sources == {n: m['key'](HERE / n) for n in sources}, 'Check source changed')
    seal = m['finish'](directory, {'status': 'PASS_RECORDED_READONLY_PREPARATION_CHECKS',
        'sources': sources, 'commands': command.count, 'git_commands': 0,
        'scientific_runs': 0, 'independent_review': False})
    print(seal)
except BaseException:
    m['failure'](directory, 'readonly-preparation-checks')
    raise
