#!/usr/bin/env python3
"""Download exact primary source bodies into this owned lane only."""
import pathlib
import sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import record
SELF = pathlib.Path(__file__).resolve()
OWN = SELF.parent
directory = OWN / 'sources'
directory.mkdir(exist_ok=False)
rows = [
    ('cpm2017', 'https://drops.dagstuhl.de/storage/00lipics/lipics-vol078-cpm2017/LIPIcs.CPM.2017.23/LIPIcs.CPM.2017.23.pdf'),
    ('ifip2008', 'https://dl.ifip.org/db/conf/ifipTCS/ifipTCS2008/MasseBFLR08.pdf'),
]
for index, (name, url) in enumerate(rows):
    pdf = directory / (name + '.pdf')
    txt = directory / (name + '.txt')
    result = record.capture(str(15+index*2) + '_download_' + name,
        ['curl', '-f', '-L', '--max-time', '45', '-o', str(pdf), url], [SELF])
    assert result.returncode == 0
    result = record.capture(str(16+index*2) + '_extract_' + name,
        ['pdftotext', '-layout', str(pdf), str(txt)], [SELF, pdf])
    assert result.returncode == 0
    record.save(directory / (name + '.json'), dict(role='downloaded_primary_body', url=url,
        pdf_sha256=record.digest(pdf), text_sha256=record.digest(txt)))
