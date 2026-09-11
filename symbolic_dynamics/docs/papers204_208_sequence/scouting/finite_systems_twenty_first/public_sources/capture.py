"""Record actual public-source requests; access failures are not body reads."""
import hashlib
import json
from pathlib import Path
import subprocess
import time

BASE = Path(__file__).resolve().parent
ENV = {'PATH': '/usr/bin:/bin', 'LANG': 'C.UTF-8', 'LC_ALL': 'C.UTF-8', 'TZ': 'UTC'}


def run(tag, command):
    before = time.time()
    with (BASE / (tag + '.stdout')).open('xb') as out, (BASE / (tag + '.stderr')).open('xb') as err:
        result = subprocess.run(command, cwd=BASE, env=ENV, stdout=out, stderr=err, check=False)
    (BASE / (tag + '.command.json')).write_text(json.dumps(dict(command=command, cwd=str(BASE),
        exit=result.returncode, started_epoch=before, finished_epoch=time.time(), environment=ENV),
        indent=2, sort_keys=True) + '\n')
    return result.returncode


def main():
    results = []
    requests = [
        ('crossref', 'https://api.crossref.org/works/10.1016%2F0097-3165(92)90037-U', 'crossref.json'),
        ('primary_api', 'https://api.elsevier.com/content/article/PII:009731659290037U?httpAccept=text/plain', 'primary_api.body'),
        ('primary_pdf', 'https://www.sciencedirect.com/science/article/pii/009731659290037U/pdf', 'primary_pdf.body'),
        ('survey', 'https://www.math.bas.bg/smb/2015_PK/tom_2015/pdf/079-091.pdf', 'drensky_survey.pdf'),
    ]
    for tag, url, output in requests:
        command = ['/usr/bin/curl', '--location', '--max-time', '30', '--fail-with-body',
            '--dump-header', tag + '.headers', '--output', output,
            '--write-out', '%{http_code}\n%{url_effective}\n%{size_download}\n', url]
        code = run(tag, command)
        path = BASE / output
        results.append(dict(tag=tag, exit=code, output=output, bytes=path.stat().st_size if path.exists() else 0,
            sha256=hashlib.sha256(path.read_bytes()).hexdigest() if path.exists() else None))
    if next(r for r in results if r['tag'] == 'survey')['exit'] == 0:
        code = run('survey_pdftotext', ['/usr/bin/pdftotext', '-layout', 'drensky_survey.pdf', 'drensky_survey.txt'])
        results.append(dict(tag='survey_pdftotext', exit=code))
    (BASE / 'RETRIEVAL.json').write_text(json.dumps(results, indent=2, sort_keys=True) + '\n')
    print(json.dumps(results, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
