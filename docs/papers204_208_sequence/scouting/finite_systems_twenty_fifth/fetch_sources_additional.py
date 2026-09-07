"""Bounded second physical source attempt; no scientific evaluations."""
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import time
from concurrent.futures import ThreadPoolExecutor

BASE = Path(__file__).resolve().parent
ENV = {'PATH': '/usr/bin:/bin', 'LANG': 'C.UTF-8', 'LC_ALL': 'C.UTF-8', 'TZ': 'UTC'}
URLS = [
    ('dmgt_direct', 'https://www.dmgt.uz.zgora.pl/publish/pdf.php?doi=1610'),
    ('schweitzer_slides', 'https://www.ac.tuwien.ac.at/wp/wp-content/uploads/logalg25_schweitzer.pdf'),
]

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def save(path, obj):
    path.write_text(json.dumps(obj, indent=2, sort_keys=True) + '\n')

def run(argv, out, tag):
    save(out / (tag + '.ATTEMPT.json'), dict(argv=argv, cwd=str(BASE), environment=ENV,
        started_utc=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())))
    with (out / (tag + '.stdout')).open('xb') as stdout, (out / (tag + '.stderr')).open('xb') as stderr:
        proc = subprocess.run(argv, cwd=BASE, env=ENV, stdout=stdout, stderr=stderr, check=False)
    save(out / (tag + '.RESULT.json'), dict(exit=proc.returncode,
        stdout_sha256=sha(out / (tag + '.stdout')), stderr_sha256=sha(out / (tag + '.stderr'))))
    return proc.returncode

def main():
    out = BASE / 'public_sources_additional'
    out.mkdir(exist_ok=False)
    curl = str(Path(shutil.which('curl')).resolve())
    pdftext = str(Path(shutil.which('pdftotext')).resolve())
    toolpaths = [Path(__file__).resolve(), Path(curl), Path(pdftext)]
    save(out / 'tools.before.json', {str(p): sha(p) for p in toolpaths})
    def fetch(entry):
        tag, url = entry
        target = out / (tag + '.pdf')
        code = run([curl, '--location', '--fail-with-body', '--max-time', '45',
            '--dump-header', str(out / (tag + '.headers')), '--output', str(target),
            '--write-out', '%{http_code}\n%{url_effective}\n%{size_download}\n', url], out, tag + '.curl')
        row = dict(tag=tag, url=url, curl_exit=code, exists=target.exists())
        if target.exists():
            row.update(bytes=target.stat().st_size, sha256=sha(target))
        if code == 0 and target.read_bytes().startswith(b'%PDF'):
            row['pdftotext_exit'] = run([pdftext, '-layout', str(target), str(out / (tag + '.txt'))], out, tag + '.pdftotext')
        return row
    with ThreadPoolExecutor(max_workers=2) as pool:
        rows = list(pool.map(fetch, URLS))
    save(out / 'tools.after.json', {str(p): sha(p) for p in toolpaths})
    save(out / 'RETRIEVAL.json', rows)
    print(json.dumps(rows, sort_keys=True))

if __name__ == '__main__':
    main()
