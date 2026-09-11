#!/usr/bin/env python3
"""Artifact/source capture only; does not run the old or any new dynamics code."""
from pathlib import Path
import hashlib
import json
import shutil
import subprocess
import sys
from datetime import datetime, timezone

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
OUT = ROOT / 'docs/papers211_215_sequence/scouting/cluster_completion_lane'
RAW = OUT / 'raw'
RAW.mkdir(exist_ok=True)
INPUTS = [
    'docs/papers152_156_sequence/scouting/algebraic_replacement2/SCOUT.md',
    'docs/papers152_156_sequence/scouting/algebraic_replacement2/OWNER_SEARCH_LOG.md',
    'docs/papers152_156_sequence/scouting/algebraic_replacement2/verify_algebraic_replacement2.py',
    'docs/papers152_156_sequence/scouting/algebraic_replacement2/CANONICAL.txt',
    'docs/papers197_201_sequence/scouting/fifth_fresh_20260905/BREADTH_AND_KILL_LEDGER.md',
]
def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

TOOLS = {name: shutil.which(name) for name in ['sha256sum', 'sed', 'rg', 'curl', 'pdftotext', 'cmp']}
assert all(TOOLS.values()), TOOLS
RECEIPT = {
    'kind': 'native artifact and primary-source acquisition; zero scientific runs',
    'author': '/root/round211_rational_scout',
    'cwd': str(ROOT), 'script_sha256': digest(__file__),
    'python': {'path': sys.executable, 'version': sys.version, 'sha256': digest(sys.executable)},
    'tools': {name: {'path': path, 'sha256': digest(path)} for name, path in TOOLS.items()},
    'commands': [],
}
RECEIPT_PATH = OUT / 'NATIVE_RECEIPT.json'
assert not RECEIPT_PATH.exists(), 'Capture receipts are append-only; do not rerun in place.'
def persist():
    RECEIPT_PATH.write_text(json.dumps(RECEIPT, indent=2) + '\n')
def run(name, command, stdout_target=None):
    assert not (RAW / (name + '.stdout')).exists()
    record = {'name': name, 'argv': command, 'cwd': str(ROOT),
              'started_utc': datetime.now(timezone.utc).isoformat()}
    try:
        result = subprocess.run(command, cwd=ROOT, capture_output=True, timeout=35)
        stdout, stderr, code = result.stdout, result.stderr, result.returncode
    except subprocess.TimeoutExpired as exc:
        stdout, stderr, code = exc.stdout or b'', exc.stderr or b'', None
        record['exception'] = repr(exc)
    except OSError as exc:
        stdout, stderr, code = b'', str(exc).encode(), None
        record['exception'] = repr(exc)
    for channel, data in [('stdout', stdout), ('stderr', stderr)]:
        path = RAW / (name + '.' + channel)
        path.write_bytes(data)
        record[channel] = {'path': str(path.relative_to(OUT)), 'bytes': len(data),
                           'sha256': hashlib.sha256(data).hexdigest()}
    if stdout_target:
        (OUT / stdout_target).write_bytes(stdout)
        record['stdout_copy'] = stdout_target
    record['returncode'] = code
    record['finished_utc'] = datetime.now(timezone.utc).isoformat()
    RECEIPT['commands'].append(record)
    persist()
    return code

persist()
run('01_input_before', [TOOLS['sha256sum'], *INPUTS], 'INPUT_PINS.sha256')
run('02_old_scout', [TOOLS['sed'], '-n', '237,266p', INPUTS[0]])
run('03_old_owner', [TOOLS['sed'], '-n', '175,230p', INPUTS[1]])
run('04_old_implementation', [TOOLS['sed'], '-n', '270,306p', INPUTS[2]])
run('05_old_canonical', [TOOLS['rg'], '-n', 'CLU', INPUTS[3]])
run('06_old_repeat_ledger', [TOOLS['sed'], '-n', '1,90p', INPUTS[4]])
pdf = OUT / 'hone2025_original.pdf'
status = run('07_primary_pdf', [TOOLS['curl'], '-L', '--fail', '--silent', '--show-error',
    '--connect-timeout', '8', '--max-time', '20', '-D', str(OUT / 'hone2025_headers.txt'),
    '-o', str(pdf), '-w', 'http_code=%{http_code}\nsize_download=%{size_download}\nurl_effective=%{url_effective}\n',
    'https://kar.kent.ac.uk/id/document/3459160'])
if status == 0 and pdf.exists():
    run('08_primary_text', [TOOLS['pdftotext'], '-layout', str(pdf), '-'])
else:
    RECEIPT['primary_text_skipped_reason'] = 'PDF acquisition did not succeed; failed bytes retained.'
    persist()
run('09_input_after', [TOOLS['sha256sum'], *INPUTS], 'INPUT_AFTER.sha256')
run('10_raw_pin_comparison', [TOOLS['cmp'], str(OUT / 'INPUT_PINS.sha256'), str(OUT / 'INPUT_AFTER.sha256')])
print(json.dumps({'commands': len(RECEIPT['commands']),
                  'returncodes': [x['returncode'] for x in RECEIPT['commands']],
                  'scientific_runs': 0, 'receipt': str(RECEIPT_PATH)}))
