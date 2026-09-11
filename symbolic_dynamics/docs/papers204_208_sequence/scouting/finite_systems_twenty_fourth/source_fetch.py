"""Capture public primary-source retrieval; never execute a science map."""
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import time

BASE = Path(__file__).resolve().parent
ENV = {'PATH': '/usr/bin:/bin', 'LANG': 'C.UTF-8', 'LC_ALL': 'C.UTF-8', 'TZ': 'UTC'}
URLS = [
    ('klop', 'https://www.cs.tau.ac.il/~nachum/papers/klop.pdf'),
    ('bender_knuth', 'https://www.cambridge.org/core/services/aop-cambridge-core/content/view/C9E0C21EE951054EBC573222C166C9A3/S2050509424001592a.pdf/benderknuth_billiards_in_coxeter_groups.pdf'),
]

def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

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
    out = BASE / 'public_sources'
    out.mkdir(exist_ok=False)
    curl = str(Path(shutil.which('curl')).resolve())
    pdftext = str(Path(shutil.which('pdftotext')).resolve())
    recorder = Path(__file__).resolve()
    before = {str(p): sha(p) for p in (recorder, Path(curl), Path(pdftext))}
    save(out / 'tools.before.json', before)
    rows = []
    for tag, url in URLS:
        payload = out / (tag + '.pdf')
        code = run([curl, '--fail-with-body', '-L', '--max-time', '45', '-D',
            str(out / (tag + '.headers')), '-o', str(payload), url], out, tag + '.curl')
        row = dict(tag=tag, url=url, curl_exit=code,
            payload_bytes=payload.stat().st_size if payload.exists() else None,
            payload_sha256=sha(payload) if payload.exists() else None)
        if code == 0 and payload.read_bytes().startswith(b'%PDF-'):
            row['pdftotext_exit'] = run([pdftext, '-layout', str(payload),
                str(out / (tag + '.txt'))], out, tag + '.pdftotext')
        rows.append(row)
    after = {str(p): sha(p) for p in (recorder, Path(curl), Path(pdftext))}
    save(out / 'tools.after.json', after)
    save(out / 'RETRIEVAL.json', dict(rows=rows, before_after_equal=before == after,
        scope='Retrieval success is not a full-text-read or proof-verification claim.'))
    print(json.dumps(dict(rows=rows, before_after_equal=before == after), sort_keys=True))

if __name__ == '__main__':
    main()
