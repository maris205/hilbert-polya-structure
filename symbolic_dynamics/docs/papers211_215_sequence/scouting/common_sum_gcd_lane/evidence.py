#!/usr/bin/env python3
"""Documentation capture and archive audit only; no gcd-map implementation."""
from __future__ import annotations
import argparse
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import hashlib
from html.parser import HTMLParser
import json
from pathlib import Path
import shutil
import subprocess

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
HERE = ROOT / 'docs/papers211_215_sequence/scouting/common_sum_gcd_lane'
INPUTS = [
    'docs/papers162_166_sequence/scouting/open_fresh_p166_round6/IDEA_LEDGER.md',
    'docs/papers107_111_sequence/scouting/COMBINATORIAL_SCOUT.md',
    'docs/papers204_208_sequence/scouting/algebra/SCOUT_REPORT.md',
    'docs/papers147_151_sequence/scouting/algebraic/SCOUT.md',
    'papers/47-harmonic-egyptian-mordell-tornheim/sections/03_graph_coordinates.tex',
]
SOURCES = [
    ('02_harris_louwsma', 'https://arxiv.org/html/1909.02022v3'),
    ('03_corrales_valencia', 'https://arxiv.org/html/1604.02502'),
]


def sha(data):
    return hashlib.sha256(data).hexdigest()


def write_json(path, value):
    path.write_text(json.dumps(value, sort_keys=True, indent=2) + '\n')


def command(out, stem, argv):
    if (out / (stem + '.command.json')).exists():
        raise RuntimeError('refusing command overwrite')
    write_json(out / (stem + '.command.json'), {
        'argv': argv, 'cwd': str(ROOT),
        'started_utc': datetime.now(timezone.utc).isoformat(),
        'scope': 'documentation only; no scientific evaluation',
    })
    result = subprocess.run(argv, cwd=ROOT, stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE, timeout=55, check=False)
    (out / (stem + '.stdout')).write_bytes(result.stdout)
    (out / (stem + '.stderr')).write_bytes(result.stderr)
    write_json(out / (stem + '.result.json'), {
        'returncode': result.returncode,
        'stdout_bytes': len(result.stdout), 'stderr_bytes': len(result.stderr),
        'stdout_sha256': sha(result.stdout), 'stderr_sha256': sha(result.stderr),
        'ended_utc': datetime.now(timezone.utc).isoformat(),
    })
    return result.returncode


class ExtractText(HTMLParser):
    def __init__(self):
        super().__init__()
        self.fragments = []

    def handle_data(self, data):
        if data.strip():
            self.fragments.append(data.strip())


def capture():
    out = HERE / 'evidence01'
    out.mkdir(exist_ok=False)
    originals = []
    for rel in INPUTS:
        data = (ROOT / rel).read_bytes()
        copy = out / 'originals' / rel
        copy.parent.mkdir(parents=True, exist_ok=True)
        copy.write_bytes(data)
        assert data == (ROOT / rel).read_bytes() == copy.read_bytes()
        originals.append({'path': rel, 'bytes': len(data), 'sha256': sha(data), 'raw_equal': True})
    write_json(out / 'original_capture.json', originals)
    (HERE / 'HISTORICAL_INPUTS.sha256').write_text(''.join(
        row['sha256'] + '  ' + row['path'] + '\n' for row in originals))
    curl, rg = shutil.which('curl'), shutil.which('rg')
    if not curl or not rg:
        raise RuntimeError('documentation executable unavailable')
    codes = [command(out, '01_old_source_mechanisms', [rg, '-n', '-i',
        'GGT|C2.1|C2.2|GH|DS|LBG|gcd|coprime', *INPUTS])]

    def fetch(source):
        stem, url = source
        destination = out / (stem + '.html')
        code = command(out, stem, [curl, '--fail', '--location', '--silent',
            '--show-error', '--max-time', '45', '--output', str(destination), url])
        info = {'url': url, 'returncode': code, 'present': destination.exists()}
        if code == 0:
            raw = destination.read_bytes()
            parser = ExtractText()
            parser.feed(raw.decode('utf-8', errors='replace'))
            text = '\n'.join(parser.fragments) + '\n'
            (out / (stem + '.txt')).write_text(text)
            info.update({'bytes': len(raw), 'sha256': sha(raw),
                         'text_bytes': len(text.encode()),
                         'contains_expected_subject': 'arithmetical' in text.lower(),
                         'extraction': 'stdlib HTMLParser inside evidence producer; not a separate native command'})
        return info

    with ThreadPoolExecutor(max_workers=2) as executor:
        sources = list(executor.map(fetch, SOURCES))
    codes.extend(row['returncode'] for row in sources)
    for row in originals:
        assert sha((ROOT / row['path']).read_bytes()) == row['sha256']
    receipt = {'historical_originals': len(originals),
               'historical_bytes': sum(row['bytes'] for row in originals),
               'historical_raw_pairs': len(originals),
               'native_returncodes': codes, 'sources': sources,
               'scientific_executions': 0, 'pilot_states': 0,
               'runtime_scope': 'non-hermetic documentation capture only',
               'external_upload_or_contact': False}
    write_json(out / 'RECEIPT.json', receipt)
    print(json.dumps(receipt, sort_keys=True))


def audit():
    out = HERE / 'evidence01'
    rows = json.loads((out / 'original_capture.json').read_text())
    for row in rows:
        data = (ROOT / row['path']).read_bytes()
        assert data == (out / 'originals' / row['path']).read_bytes()
        assert sha(data) == row['sha256'] and len(data) == row['bytes']
    commands = sorted(out.glob('*.command.json'))
    codes = []
    for path in commands:
        stem = path.name.removesuffix('.command.json')
        result = json.loads((out / (stem + '.result.json')).read_text())
        codes.append(result['returncode'])
        for stream in ['stdout', 'stderr']:
            data = (out / (stem + '.' + stream)).read_bytes()
            assert sha(data) == result[stream + '_sha256']
            assert len(data) == result[stream + '_bytes']
    receipt = json.loads((out / 'RECEIPT.json').read_text())
    for source in receipt['sources']:
        if source['returncode'] == 0:
            stem = next(stem for stem, url in SOURCES if url == source['url'])
            raw = (out / (stem + '.html')).read_bytes()
            assert sha(raw) == source['sha256'] and len(raw) == source['bytes']
    assert len(rows) == 5 and len(commands) == 3
    assert codes == receipt['native_returncodes']
    print(json.dumps({'audit': 'ARCHIVED_DOCUMENTATION_ONLY', 'historical_raw_pairs': len(rows),
                      'native_bindings': len(commands), 'native_returncodes': codes,
                      'new_scientific_executions': 0}, sort_keys=True))


def seal():
    path = HERE / 'SHA256SUMS'
    if path.exists():
        raise RuntimeError('sealed package is immutable')
    files = sorted(p for p in HERE.rglob('*') if p.is_file())
    path.write_text(''.join(sha(p.read_bytes()) + '  ' + str(p.relative_to(HERE)) + '\n'
                            for p in files))
    print(json.dumps({'payloads': len(files), 'payload_bytes': sum(p.stat().st_size for p in files)}))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('mode', choices=['capture', 'audit', 'seal'])
    args = parser.parse_args()
    if Path(__file__).resolve() != HERE / 'evidence.py':
        raise RuntimeError('unexpected producer path')
    {'capture': capture, 'audit': audit, 'seal': seal}[args.mode]()
