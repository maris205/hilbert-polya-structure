#!/usr/bin/env python3
"""Records compilation and static scientific producer; no imported science."""
import pathlib
import sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from record import ROOT, OWN, run

P = str(OWN.relative_to(ROOT))
op = sys.argv[1]
inputs = [P + '/INTAKE.md', P + '/pilot.c']
if op == 'compile':
    run('07_compiler_version', ['/usr/bin/gcc', '--version'], ['/usr/bin/gcc'])
    run('08_compile_static', ['/usr/bin/gcc', '-nostdlib', '-static', '-fno-stack-protector', '-fno-builtin', '-fno-pie', '-no-pie', '-O2', '-Wall', '-Wextra', '-Werror', '-Wl,--build-id=none', '-o', P + '/pilot', P + '/pilot.c'], inputs + ['/usr/bin/gcc'])
elif op == 'inspect':
    run('09_static_elf', ['/usr/bin/readelf', '-l', '-d', '-s', P + '/pilot'], inputs + [P + '/pilot', '/usr/bin/readelf'])
elif op == 'run':
    label = sys.argv[2]
    r = run(label, [str(OWN / 'pilot')], inputs + [P + '/pilot'])
    if r.returncode: raise SystemExit(r.returncode)
elif op == 'compare':
    a = P + '/commands/10_pilot_a/stdout.raw'
    b = P + '/commands/11_pilot_b/stdout.raw'
    run('12_raw_canonical_cmp', ['/usr/bin/cmp', a, b], [a, b, '/usr/bin/cmp'])
else:
    raise SystemExit(op)
