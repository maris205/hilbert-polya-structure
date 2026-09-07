#!/usr/bin/env python3
"""Public primary acquisition/read infrastructure, not mathematical code."""
import pathlib
import sys
sys.dont_write_bytecode = True
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import record

SELF = pathlib.Path(__file__).resolve()

if __name__ == '__main__':
    if sys.argv[1] == 'fetch':
        name, url = sys.argv[2:4]
        destination = record.OWN / 'sources' / name
        destination.mkdir(parents=True, exist_ok=False)
        record.save(destination / 'request.json', dict(url=url, max_time_seconds=40,
            role='ordinary_public_primary_acquisition'))
        run = record.capture(name + '_download', ['curl', '--location', '--max-redirs', '5',
            '--connect-timeout', '12', '--max-time', '40', '--silent', '--show-error', '--fail-with-body',
            '--dump-header', str(destination / 'headers.raw'), '--output', str(destination / 'body.raw'),
            '--write-out', '%{http_code}\n%{url_effective}\n%{content_type}\n%{size_download}\n', url],
            [SELF, destination / 'request.json'])
        if run.returncode == 0 and (destination / 'body.raw').read_bytes().startswith(b'%PDF-'):
            record.capture(name + '_pdfinfo', ['pdfinfo', str(destination / 'body.raw')], [SELF, destination / 'body.raw'])
            record.capture(name + '_text', ['pdftotext', '-layout', str(destination / 'body.raw'), str(destination / 'body.txt')],
                [SELF, destination / 'body.raw'])
        else:
            print('No successful PDF body acquisition:', name)
    elif sys.argv[1] == 'read':
        label, selection, relative = sys.argv[2:5]
        path = record.ROOT / relative
        run = record.capture(label, ['sed', '-n', selection, str(path)], [SELF, path])
        assert run.returncode == 0
    elif sys.argv[1] == 'locate':
        name, pattern = sys.argv[2:4]
        path = record.OWN / 'sources' / name / 'body.txt'
        run = record.capture(name + '_locate', ['rg', '-n', pattern, str(path)], [SELF, path])
        assert run.returncode in (0, 1)
    else:
        raise SystemExit('bad mode')

