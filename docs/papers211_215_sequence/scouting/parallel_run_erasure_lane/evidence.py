#!/usr/bin/env python3
"""Document capture/seal/audit only; no word-map or scientific enumeration."""
from __future__ import annotations
import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import shutil
import subprocess

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
HERE = ROOT / 'docs/papers211_215_sequence/scouting/parallel_run_erasure_lane'
INPUTS = [
    'docs/papers187_191_sequence/scouting/algebra_lane/replacement/CANDIDATES.md',
    'docs/papers187_191_sequence/scouting/algebra_lane/replacement/pilot.py',
    'docs/papers187_191_sequence/scouting/algebra_lane/replacement/KILL_LEDGER.md',
    'docs/papers187_191_sequence/scouting/algebra_lane/replacement/THEOREM_SPIKES.md',
    'docs/papers204_208_sequence/scouting/finite_systems_thirty_sixth/PROOF_PACKAGE.md',
]
SOURCE_URL = 'https://onlinejudge.org/external/12/1261.pdf'


def sha(data):
    return hashlib.sha256(data).hexdigest()


def write_json(path, value):
    path.write_text(json.dumps(value, sort_keys=True, indent=2) + '\n')


def native(out, stem, argv):
    write_json(out / (stem + '.command.json'), {
        'argv': argv, 'cwd': str(ROOT),
        'started_utc': datetime.now(timezone.utc).isoformat(),
        'scope': 'documentation only; no scientific execution',
    })
    result = subprocess.run(argv, cwd=ROOT, stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE, timeout=55, check=False)
    for stream in ('stdout', 'stderr'):
        (out / (stem + '.' + stream)).write_bytes(getattr(result, stream))
    write_json(out / (stem + '.result.json'), {
        'returncode': result.returncode,
        'stdout_bytes': len(result.stdout), 'stderr_bytes': len(result.stderr),
        'stdout_sha256': sha(result.stdout), 'stderr_sha256': sha(result.stderr),
        'ended_utc': datetime.now(timezone.utc).isoformat(),
    })
    return result.returncode


def capture():
    out = HERE / 'evidence01'
    out.mkdir(exist_ok=False)
    rows = []
    for rel in INPUTS:
        data = (ROOT / rel).read_bytes()
        dest = out / 'originals' / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(data)
        assert data == dest.read_bytes() == (ROOT / rel).read_bytes()
        rows.append({'path': rel, 'bytes': len(data), 'sha256': sha(data),
                     'raw_equal': True})
    write_json(out / 'original_capture.json', rows)
    pins = HERE / 'HISTORICAL_INPUTS.sha256'
    pins.write_text(''.join(row['sha256'] + '  ' + row['path'] + '\n'
                            for row in rows))
    rg, checksum = shutil.which('rg'), shutil.which('sha256sum')
    curl, pdftext = shutil.which('curl'), shutil.which('pdftotext')
    if not all([rg, checksum, curl, pdftext]):
        raise RuntimeError('required documentation executable unavailable')
    codes = [native(out, '01_exact_old_definitions', [rg, '-n', '-A', '5',
        '-B', '2', 'R08/PFR|def parallel_free_reduce|T\\(x\\)_i|'
        'F_n\\(x\\)_i|run segmentation|KILL_DIRECT_FREE_REDUCTION', *INPUTS]),
        native(out, '02_historical_pins', [checksum, '-c', str(pins)]),
        native(out, '03_primary_uva_pdf', [curl, '--fail', '--location',
            '--silent', '--show-error', '--max-time', '45', '--output',
            str(out / '1261.pdf'), SOURCE_URL])]
    source = {'url': SOURCE_URL, 'download_returncode': codes[-1]}
    if codes[-1] == 0:
        pdf = (out / '1261.pdf').read_bytes()
        assert pdf.startswith(b'%PDF-')
        codes.append(native(out, '04_primary_uva_text', [pdftext, '-layout',
            str(out / '1261.pdf'), str(out / '1261.txt')]))
        source.update({'pdf_bytes': len(pdf), 'pdf_sha256': sha(pdf),
                       'extraction_returncode': codes[-1]})
        if codes[-1] == 0:
            body = (out / '1261.txt').read_bytes()
            source.update({'text_bytes': len(body), 'text_sha256': sha(body)})
    for row in rows:
        assert (ROOT / row['path']).read_bytes() == (out / 'originals' / row['path']).read_bytes()
    receipt = {'historical_originals': len(rows),
               'historical_bytes': sum(row['bytes'] for row in rows),
               'historical_raw_pairs': len(rows), 'native_returncodes': codes,
               'scientific_executions': 0, 'pilot_states': 0,
               'literal_attempts': 1, 'reserves': 0,
               'runtime_scope': 'non-hermetic documentation capture only',
               'source': source}
    write_json(out / 'RECEIPT.json', receipt)
    print(json.dumps(receipt, sort_keys=True))
    assert codes == [0, 0, 0, 0]


def seal():
    target = HERE / 'SHA256SUMS'
    if target.exists():
        raise RuntimeError('refusing seal overwrite')
    files = sorted(path for path in HERE.rglob('*') if path.is_file())
    target.write_text(''.join(sha(path.read_bytes()) + '  ' +
                             path.relative_to(HERE).as_posix() + '\n'
                             for path in files))
    print(json.dumps({'payload_files': len(files),
                      'payload_bytes': sum(path.stat().st_size for path in files),
                      'manifest_sha256': sha(target.read_bytes())}, sort_keys=True))


def audit():
    out = HERE / 'evidence01'
    rows = json.loads((out / 'original_capture.json').read_text())
    assert [row['path'] for row in rows] == INPUTS
    for row in rows:
        data = (ROOT / row['path']).read_bytes()
        assert data == (out / 'originals' / row['path']).read_bytes()
        assert sha(data) == row['sha256'] and len(data) == row['bytes']
    commands = sorted(out.glob('*.command.json'))
    assert len(commands) == 4
    for path in commands:
        command = json.loads(path.read_text())
        assert command['cwd'] == str(ROOT) and command['argv']
        stem = path.name.removesuffix('.command.json')
        result = json.loads((out / (stem + '.result.json')).read_text())
        assert result['returncode'] == 0
        for stream in ('stdout', 'stderr'):
            data = (out / (stem + '.' + stream)).read_bytes()
            assert len(data) == result[stream + '_bytes']
            assert sha(data) == result[stream + '_sha256']
    receipt = json.loads((out / 'RECEIPT.json').read_text())
    assert receipt['historical_originals'] == 5
    assert receipt['native_returncodes'] == [0, 0, 0, 0]
    assert receipt['scientific_executions'] == 0 and receipt['literal_attempts'] == 1
    for ext, prefix in [('pdf', 'pdf'), ('txt', 'text')]:
        data = (out / ('1261.' + ext)).read_bytes()
        assert len(data) == receipt['source'][prefix + '_bytes']
        assert sha(data) == receipt['source'][prefix + '_sha256']
    expected = {}
    for line in (HERE / 'SHA256SUMS').read_text().splitlines():
        digest, rel = line.split('  ', 1)
        assert rel not in expected and rel != 'SHA256SUMS'
        expected[rel] = digest
    actual = {path.relative_to(HERE).as_posix() for path in HERE.rglob('*')
              if path.is_file() and path.name != 'SHA256SUMS'}
    assert actual == set(expected)
    for rel, digest in expected.items():
        assert sha((HERE / rel).read_bytes()) == digest
    print(json.dumps({'audit': 'PASS_DOCUMENTATION_ONLY',
                      'raw_historical_pairs_checked': len(rows),
                      'native_bindings_checked': len(commands),
                      'payload_files_checked': len(expected),
                      'scientific_executions': 0}, sort_keys=True))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('action', choices=['capture', 'seal', 'audit'])
    args = parser.parse_args()
    {'capture': capture, 'seal': seal, 'audit': audit}[args.action]()
