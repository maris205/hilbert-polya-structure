"""Preserve actual primary-source request and text extraction; no science."""
import hashlib
import json
from pathlib import Path
import subprocess
import time

BASE = Path(__file__).resolve().parent
ENV = {'PATH': '/usr/bin:/bin', 'LANG': 'C.UTF-8', 'LC_ALL': 'C.UTF-8', 'TZ': 'UTC'}


def run(tag, command):
    started = time.time()
    with (BASE / (tag + '.stdout')).open('xb') as out, (BASE / (tag + '.stderr')).open('xb') as err:
        proc = subprocess.run(command, cwd=BASE, env=ENV, stdout=out, stderr=err, check=False)
    (BASE / (tag + '.command.json')).write_text(json.dumps(dict(command=command, cwd=str(BASE),
        environment=ENV, exit=proc.returncode, started_epoch=started, finished_epoch=time.time()), indent=2, sort_keys=True) + '\n')
    return proc.returncode


def main():
    code = run('flip_sort_curl', ['/usr/bin/curl', '--location', '--fail-with-body', '--max-time', '30',
        '--dump-header', 'flip_sort.headers', '--output', 'flip_sort.pdf', '--write-out', '%{http_code}\n%{url_effective}\n%{size_download}\n',
        'https://dmtcs.episciences.org/7411/pdf'])
    result = dict(curl_exit=code)
    if code == 0:
        result['pdftotext_exit'] = run('flip_sort_pdftotext', ['/usr/bin/pdftotext', '-layout', 'flip_sort.pdf', 'flip_sort.txt'])
    file = BASE / 'flip_sort.pdf'
    result['download_bytes'] = file.stat().st_size if file.exists() else 0
    result['download_sha256'] = hashlib.sha256(file.read_bytes()).hexdigest() if file.exists() else None
    (BASE / 'RETRIEVAL.json').write_text(json.dumps(result, sort_keys=True, indent=2) + '\n')
    print(json.dumps(result, sort_keys=True, indent=2))


if __name__ == '__main__':
    main()
