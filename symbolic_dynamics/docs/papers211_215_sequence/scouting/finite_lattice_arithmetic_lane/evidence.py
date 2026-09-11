#!/usr/bin/env python3
"""Documentation capture/seal/audit only; no FCSR implementation or pilot."""
from __future__ import annotations
import argparse
from datetime import datetime, timezone
import hashlib
from html.parser import HTMLParser
import json
from pathlib import Path
import shutil
import subprocess

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
HERE = ROOT / 'docs/papers211_215_sequence/scouting/finite_lattice_arithmetic_lane'
INPUTS = [
    'docs/papers204_208_sequence/scouting/finite_algebra_ninth/INTAKE.md',
    'docs/papers204_208_sequence/scouting/finite_algebra_ninth/PROOF_AND_ADAPTER_NOTES.md',
    'docs/papers204_208_sequence/scouting/finite_algebra_ninth/SOURCE_AND_COLLISION.md',
]
SOURCE_URL = 'https://www.johndcook.com/blog/2020/06/09/complex-square-root/'


def sha(data):
    return hashlib.sha256(data).hexdigest()


def write_json(path, value):
    path.write_text(json.dumps(value, sort_keys=True, indent=2) + '\n')


class SourceText(HTMLParser):
    def __init__(self):
        super().__init__()
        self.fragments = []

    def handle_data(self, data):
        if data.strip():
            self.fragments.append(data.strip())


def extract(raw):
    parser = SourceText()
    parser.feed(raw.decode('utf-8', errors='replace'))
    return ('\n'.join(parser.fragments) + '\n').encode()


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
    rg, checksum, curl = (shutil.which(name) for name in ('rg', 'sha256sum', 'curl'))
    if not all([rg, checksum, curl]):
        raise RuntimeError('required documentation executable unavailable')
    codes = [native(out, '01_exact_qrm_original', [rg, '-n', '-A', '7',
        '-B', '3', 'QRM|n=2|swaps the coordinates|quantized consensus', *INPUTS]),
        native(out, '02_historical_pins', [checksum, '-c', str(pins)]),
        native(out, '03_primary_root_formula', [curl, '--fail', '--location',
            '--silent', '--show-error', '--max-time', '45', '--output',
            str(out / 'root_formula.html'), SOURCE_URL])]
    source = {'url': SOURCE_URL, 'download_returncode': codes[-1],
              'extraction': 'stdlib HTMLParser in this documentation producer'}
    if codes[-1] == 0:
        raw = (out / 'root_formula.html').read_bytes()
        body = extract(raw)
        (out / 'root_formula.txt').write_bytes(body)
        source.update({'html_bytes': len(raw), 'html_sha256': sha(raw),
                       'text_bytes': len(body), 'text_sha256': sha(body)})
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
    assert codes[:2] == [0, 0]


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
    assert len(commands) == 3
    codes = []
    for path in commands:
        command = json.loads(path.read_text())
        assert command['cwd'] == str(ROOT) and command['argv']
        stem = path.name.removesuffix('.command.json')
        result = json.loads((out / (stem + '.result.json')).read_text())
        codes.append(result['returncode'])
        for stream in ('stdout', 'stderr'):
            data = (out / (stem + '.' + stream)).read_bytes()
            assert len(data) == result[stream + '_bytes']
            assert sha(data) == result[stream + '_sha256']
    receipt = json.loads((out / 'RECEIPT.json').read_text())
    assert receipt['historical_originals'] == 3 and codes[:2] == [0, 0]
    assert receipt['native_returncodes'] == codes
    assert receipt['scientific_executions'] == 0 and receipt['literal_attempts'] == 1
    if receipt['source']['download_returncode'] == 0:
        for ext, prefix in [('html', 'html'), ('txt', 'text')]:
            data = (out / ('root_formula.' + ext)).read_bytes()
            assert len(data) == receipt['source'][prefix + '_bytes']
            assert sha(data) == receipt['source'][prefix + '_sha256']
        assert extract((out / 'root_formula.html').read_bytes()) == (out / 'root_formula.txt').read_bytes()
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
                      'native_returncodes': codes,
                      'payload_files_checked': len(expected),
                      'scientific_executions': 0}, sort_keys=True))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('action', choices=['capture', 'seal', 'audit'])
    args = parser.parse_args()
    {'capture': capture, 'seal': seal, 'audit': audit}[args.action]()
