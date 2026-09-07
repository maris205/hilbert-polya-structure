#!/usr/bin/env python3
"""Bounded primary acquisition/extraction and exact textual read receipts."""
import pathlib
import sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import record

SELF = pathlib.Path(__file__).resolve()


if __name__ == '__main__':
    mode = sys.argv[1]
    if mode == 'fetch':
        name, url = sys.argv[2:4]
        target = record.OWN / 'sources' / name
        target.mkdir(parents=True, exist_ok=False)
        record.save(target / 'request.json', dict(url=url, timeout_seconds=40, role='ordinary_primary_body_acquisition'))
        result = record.capture(name + '_download', ['curl', '--location', '--max-redirs', '5', '--connect-timeout', '12', '--max-time', '40',
             '--silent', '--show-error', '--fail-with-body', '--dump-header', str(target / 'headers.raw'), '--output', str(target / 'body.raw'),
             '--write-out', '%{http_code}\n%{url_effective}\n%{content_type}\n%{size_download}\n', url], [SELF, target / 'request.json'])
        if result.returncode != 0:
            print('Acquisition failed; exact response retained:', name)
        elif (target / 'body.raw').read_bytes().startswith(b'%PDF-'):
            record.capture(name + '_pdfinfo', ['pdfinfo', str(target / 'body.raw')], [SELF, target / 'body.raw'])
            record.capture(name + '_text', ['pdftotext', '-layout', str(target / 'body.raw'), str(target / 'body.txt')], [SELF, target / 'body.raw'])
        else:
            print('Successful HTTP transfer is not a PDF:', name)
    elif mode == 'read':
        label, selection, relative = sys.argv[2:5]
        path = record.ROOT / relative
        result = record.capture(label, ['sed', '-n', selection, str(path)], [SELF, path])
        assert result.returncode == 0
    elif mode == 'headers':
        name, pattern = sys.argv[2:4]
        path = record.OWN / 'sources' / name / 'body.txt'
        result = record.capture(name + '_headers', ['rg', '-n', pattern, str(path)], [SELF, path])
        assert result.returncode in (0, 1)
    else:
        raise SystemExit('bad mode')
