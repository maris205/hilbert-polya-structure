#!/usr/bin/env python3
"""Bounded author artifact/source capture. Contains no scientific execution."""
import datetime
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import time

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
HISTORICAL = [
    'papers/150-zero-totalized-lyness-finite-fields/main.tex',
    'papers/157-newton-hensel-finite-atlas/main.tex',
    'papers/168-quartic-inverse-span-dynamics/main.tex',
    'papers/174-minimum-pivot-mobius-feedback/main.tex',
    'papers/175-diagonal-feedback-commutator/main.tex',
    'papers/180-bilinear-radial-scaling/main.tex',
    'docs/papers172_176_sequence/scouting/fresh_nonlinear_algebra/SCOUT_AND_KILL_LEDGER.md',
    'docs/papers197_201_sequence/scouting/algebra_lane/BREADTH_AND_KILL_LEDGER.md',
    'docs/papers204_208_sequence/scouting/algebra/PROOF_NOTES.md',
    'docs/papers204_208_sequence/scouting/finite_algebra_ninth/PROOF_AND_ADAPTER_NOTES.md',
    'docs/papers211_215_sequence/scouting/nonlinear_lane/PROOF_AND_SUBTRACTION.md',
    'docs/papers211_215_sequence/scouting/algebra_lane/PROOF_PACKAGE.md',
]
CONTROLS = [
    'SYMBOLIC_DYNAMICS_STATE.md',
    'docs/papers211_215_sequence/PIPELINE_STATE.md',
]
SOURCES = [
    ('bedford_frigge', 'https://drna.padovauniversitypress.it/system/files/papers/Bedford_DRNA2018.pdf'),
    ('fulman_guralnick', 'https://par.nsf.gov/servlets/purl/10415826'),
]

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def main():
    started = datetime.datetime.now(datetime.timezone.utc).isoformat()
    native = HERE / 'native02'
    native.mkdir(exist_ok=False)
    (HERE / 'sources').mkdir(exist_ok=True)
    (HERE / 'control_snapshots').mkdir(exist_ok=True)
    records = []

    def run(label, argv, cwd=ROOT, accepted=(0,), timeout=25):
        clock = time.monotonic()
        result = subprocess.run(argv, cwd=cwd, capture_output=True,
                                check=False, timeout=timeout)
        for stream in ('stdout', 'stderr'):
            (native / (label + '.' + stream + '.raw')).write_bytes(getattr(result, stream))
        records.append({'label': label, 'argv': argv, 'cwd': str(cwd),
                        'returncode': result.returncode,
                        'elapsed_seconds': time.monotonic() - clock,
                        'accepted_codes': list(accepted),
                        'stdout': label + '.stdout.raw',
                        'stderr': label + '.stderr.raw'})
        return result

    before = run('historical_before', ['/usr/bin/sha256sum', *HISTORICAL])
    snapshots = []
    for i, original in enumerate(CONTROLS, 1):
        dest = HERE / 'control_snapshots' / Path(original).name
        assert dest.exists(), 'Keep the original successful control snapshots.'
        run('control_compare_' + str(i), ['/usr/bin/cmp', '--', original, str(dest)])
        snapshots.append({'original': original, 'snapshot': str(dest.relative_to(HERE)),
                          'sha256': sha(dest)})
    run('narrow_history', ['/usr/lib/node_modules/@openai/codex/node_modules/@openai/codex-linux-x64/vendor/x86_64-unknown-linux-musl/codex-path/rg', '-n', '-i',
        'secant|arithmetic.harmonic|harmonic.mean|anticommutator|PXE|commutator-sum|AB.?BA',
        *HISTORICAL], accepted=(0, 1))
    fetches = []
    for label, url in SOURCES:
        dest = HERE / 'sources' / (label + '.pdf')
        fetched = run('fetch_' + label,
            ['/root/miniconda3/bin/curl', '-L', '--max-time', '20', '--silent', '--show-error',
             '--output', str(dest), '--write-out', '%{http_code}\n%{url_effective}\n', url],
            accepted=(0, 28))
        row = {'label': label, 'url': url, 'curl_exit': fetched.returncode,
               'http_observation': fetched.stdout.decode(errors='replace')}
        if dest.exists():
            row.update({'path': str(dest.relative_to(HERE)), 'sha256': sha(dest),
                        'bytes': dest.stat().st_size})
            is_pdf = dest.read_bytes()[:5] == b'%PDF-'
            row['pdf_magic'] = is_pdf
            if fetched.returncode == 0 and is_pdf:
                extracted = run('extract_' + label,
                    ['/usr/bin/pdftotext', '-layout', str(dest), '-'])
                row['extraction_exit'] = extracted.returncode
        fetches.append(row)
    after = run('historical_after', ['/usr/bin/sha256sum', *HISTORICAL])
    comparison = run('historical_compare', ['/usr/bin/cmp',
        'historical_before.stdout.raw', 'historical_after.stdout.raw'], cwd=native)
    if before.returncode == after.returncode == comparison.returncode == 0:
        (HERE / 'INPUT_PINS.sha256').write_bytes(before.stdout)
    receipt = {
        'scope': 'artifact_and_source_capture_only_no_science',
        'started_utc': started,
        'completed_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'source': {'path': 'capture_native02.py', 'sha256': sha(HERE / 'capture_native02.py')},
        'interpreter': {'path': sys.executable, 'version': sys.version,
                        'sha256': sha(Path(sys.executable).resolve())},
        'tool_pins': {p: sha(Path(p)) for p in
                     ['/usr/bin/sha256sum', '/usr/bin/cmp', '/usr/bin/cp',
                      '/usr/lib/node_modules/@openai/codex/node_modules/@openai/codex-linux-x64/vendor/x86_64-unknown-linux-musl/codex-path/rg', '/root/miniconda3/bin/curl', '/usr/bin/pdftotext']},
        'provenance_limit': 'Not a hermetic loader, transport, parser, or scientific runtime key.',
        'commands': records, 'source_fetches': fetches,
        'control_snapshots': snapshots, 'historical_input_count': len(HISTORICAL),
        'scientific_runs': 0,
        'command_contract_pass': all(r['returncode'] in r['accepted_codes'] for r in records),
        'historical_raw_pair_equal': before.stdout == after.stdout,
    }
    (native / 'receipt.json').write_text(json.dumps(receipt, indent=2) + '\n')
    print(json.dumps({'commands': len(records), 'history_inputs': len(HISTORICAL),
                      'source_fetches': fetches, 'scientific_runs': 0,
                      'command_contract_pass': receipt['command_contract_pass']}))

if __name__ == '__main__':
    main()
