#!/usr/bin/env python3
"""Pin the exact primary-body excerpts actually selected for reading."""
import pathlib
import sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import record
SELF = pathlib.Path(__file__).resolve()
OWN = SELF.parent
for label, name, extent in [('24_cpm2017_body_excerpt', 'cpm2017', '1,220p'),
                            ('25_ifip2008_body_excerpt', 'ifip2008', '1,160p')]:
    txt = OWN / 'sources' / (name + '.txt')
    pdf = OWN / 'sources' / (name + '.pdf')
    record.capture(label, ['sed', '-n', extent, str(txt)], [SELF, txt, pdf])
