"""Record two public primary source downloads and text extraction, no science."""
import hashlib
import json
from pathlib import Path
import subprocess
import time

BASE = Path(__file__).resolve().parent
ENV = {'PATH': '/usr/bin:/bin', 'LANG': 'C.UTF-8', 'LC_ALL': 'C.UTF-8', 'TZ': 'UTC'}
SOURCES = [
    ('higham_kim2001', 'https://eprints.maths.manchester.ac.uk/319/1/35097.pdf'),
    ('barmak_minian2009', 'https://arxiv.org/pdf/0907.2954'),
]

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def save(path, obj):
    path.write_text(json.dumps(obj, indent=2, sort_keys=True) + '\n')

def run(argv, tag):
    save(BASE / (tag + '.ATTEMPT.json'), dict(argv=argv, environment=ENV,
        cwd=str(BASE), start_utc=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())))
    with (BASE / (tag + '.stdout')).open('xb') as out, (BASE / (tag + '.stderr')).open('xb') as err:
        proc = subprocess.run(argv, cwd=BASE, env=ENV, stdout=out, stderr=err, check=False)
    save(BASE / (tag + '.RESULT.json'), dict(exit=proc.returncode,
        stdout_sha256=sha(BASE / (tag + '.stdout')), stderr_sha256=sha(BASE / (tag + '.stderr'))))
    return proc.returncode

rows = []
for tag, url in SOURCES:
    path = BASE / (tag + '.pdf')
    if path.exists():
        raise FileExistsError(path)
    code = run(['/usr/bin/curl', '--location', '--fail-with-body', '--max-time', '45',
        '--dump-header', str(BASE / (tag + '.headers')), '--output', str(path), url], tag + '.curl')
    valid = path.is_file() and path.read_bytes().startswith(b'%PDF-')
    conversion = None
    if code == 0 and valid:
        conversion = run(['/usr/bin/pdftotext', '-layout', str(path), str(BASE / (tag + '.txt'))], tag + '.pdftotext')
    rows.append(dict(name=tag, url=url, curl_exit=code, pdf_magic=valid,
        bytes=path.stat().st_size if path.exists() else None,
        sha256=sha(path) if path.exists() else None, pdftotext_exit=conversion))
save(BASE / 'RETRIEVAL.json', rows)
print(json.dumps(rows, sort_keys=True))
