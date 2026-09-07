#!/usr/bin/env python3
"""Scoped command list for sources, raw canonical comparisons and runtime."""
import pathlib
import sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from record import ROOT, OWN, run
P = str(OWN.relative_to(ROOT))
op = sys.argv[1]
if op == 'canonical':
    a = P + '/commands/10_pilot_a/stdout.raw'
    b = P + '/commands/11_pilot_b/stdout.raw'
    c = P + '/CANONICAL.raw'
    assert not (ROOT / c).exists()
    run('14_preserve_raw_canonical', ['/usr/bin/cp', '-p', a, c], [a, '/usr/bin/cp'])
    run('15_run_a_raw_canonical_cmp', ['/usr/bin/cmp', a, c], [a, c, '/usr/bin/cmp'])
    run('16_run_b_raw_canonical_cmp', ['/usr/bin/cmp', b, c], [b, c, '/usr/bin/cmp'])
elif op == 'runtime':
    run('17_disassembly', ['/usr/bin/objdump', '-d', P + '/pilot'], [P + '/pilot', P + '/pilot.c', '/usr/bin/objdump'])
    run('18_runtime_platform', ['/usr/bin/uname', '-srvm'], ['/usr/bin/uname'])
elif op == 'sources':
    (OWN / 'sources').mkdir(exist_ok=False)
    items = [
        ('kutz_2004', 'https://people.mpi-inf.mpg.de/alumni/d1/2009/mkutz/diss/kutzdiss.pdf'),
        ('deschutter_1997', 'https://www.dcsc.tudelft.nl/~bdeschutter/pub/rep/97_67.pdf')]
    for index, (name, url) in enumerate(items, start=19):
        target = P + '/sources/' + name + '.pdf'
        run(str(index) + '_fetch_' + name, ['/usr/bin/curl', '-L', '--fail', '--max-time', '45', '-D', P + '/sources/' + name + '.headers', '-o', target, url], ['/usr/bin/curl'])
        run(str(index) + 'b_extract_' + name, ['/usr/bin/pdftotext', '-layout', target, P + '/sources/' + name + '.txt'], [target, '/usr/bin/pdftotext'])
else:
    raise SystemExit(op)
