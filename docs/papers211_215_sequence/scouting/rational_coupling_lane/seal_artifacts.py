#!/usr/bin/env python3
"""Author-side compact nonself sealing; no scientific run or independent review."""
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def main():
    report = HERE / 'ARTIFACT_CHECK.json'
    manifest = HERE / 'MANIFEST.sha256'
    assert not report.exists() and not manifest.exists(), 'Preserve previous seals.'
    historical = []
    pins = (HERE / 'INPUT_PINS.sha256').read_bytes()
    for line in pins.decode().splitlines():
        expected, name = line.split('  ', 1)
        assert sha(ROOT / name) == expected, name
        historical.append({'path': name, 'sha256': expected})
    assert len(historical) == 12
    native = HERE / 'native02'
    receipt = json.loads((native / 'receipt.json').read_text())
    assert receipt['scientific_runs'] == 0 and receipt['command_contract_pass']
    assert len(receipt['commands']) == 10
    assert all(c['returncode'] == 0 for c in receipt['commands'])
    assert receipt['historical_raw_pair_equal']
    for c in receipt['commands']:
        assert (native / c['stdout']).exists()
        assert (native / c['stderr']).read_bytes() == b''
    assert pins == (native / 'historical_before.stdout.raw').read_bytes()
    assert pins == (native / 'historical_after.stdout.raw').read_bytes()
    assert pins == (HERE / 'native/historical_before.stdout.raw').read_bytes()
    assert (native / 'historical_compare.stdout.raw').read_bytes() == b''
    assert sha(HERE / receipt['source']['path']) == receipt['source']['sha256']
    for row in receipt['control_snapshots']:
        assert sha(HERE / row['snapshot']) == row['sha256']
    assert len(receipt['control_snapshots']) == 2
    for row in receipt['source_fetches']:
        assert row['curl_exit'] == row['extraction_exit'] == 0
        assert row['http_observation'].splitlines()[0] == '200'
        pdf = HERE / row['path']
        assert sha(pdf) == row['sha256'] and pdf.stat().st_size == row['bytes']
        assert pdf.read_bytes().startswith(b'%PDF-')
        assert (native / ('extract_' + row['label'] + '.stdout.raw')).stat().st_size > 0
    assert len(receipt['source_fetches']) == 2
    original_raws = sorted((HERE / 'native').glob('*.raw'))
    assert len(original_raws) == 10
    assert not (HERE / 'native/receipt.json').exists()
    for p in original_raws:
        if p.name != 'historical_before.stdout.raw':
            assert p.read_bytes() == b'', p.name
    data = {'status': 'PASS_AUTHOR_ARTIFACT_ONLY',
            'historical_input_count': len(historical), 'historical_inputs': historical,
            'complete_second_capture_command_count': len(receipt['commands']),
            'first_capture_partial_raw_payloads': len(original_raws),
            'first_capture_missing_final_receipt_disclosed': True,
            'historical_raw_list_equality_checked': True,
            'physical_control_snapshots_checked': receipt['control_snapshots'],
            'primary_pdf_fetches_checked': receipt['source_fetches'],
            'scientific_runs': 0, 'literal_attempts': 2, 'retained': 0,
            'limits': 'No independent review, scientific replay, or full loader/runtime capsule.'}
    report.write_text(json.dumps(data, indent=2) + '\n')
    payloads = sorted(p for p in HERE.rglob('*') if p.is_file() and p != manifest)
    assert not any(p.is_symlink() for p in payloads)
    rows = [sha(p) + '  ' + p.relative_to(HERE).as_posix() + '\n' for p in payloads]
    manifest.write_text(''.join(rows))
    for line in manifest.read_text().splitlines():
        expected, name = line.split('  ', 1)
        assert sha(HERE / name) == expected, name
    assert len(rows) == len(set(p.relative_to(HERE).as_posix() for p in payloads))
    print(json.dumps({'status': 'PASS_AUTHOR_ARTIFACT_ONLY',
                      'manifest_payloads': len(rows), 'historical_inputs': len(historical),
                      'bytes': sum(p.stat().st_size for p in payloads),
                      'scientific_runs': 0, 'literal_attempts': 2, 'retained': 0}))

if __name__ == '__main__':
    main()
