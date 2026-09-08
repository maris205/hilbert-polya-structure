#!/usr/bin/env python3
"""Author-side final artifact checks and nonself manifest; no science."""
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def main():
    manifest = HERE / 'MANIFEST.sha256'
    report = HERE / 'ARTIFACT_CHECK.json'
    assert not manifest.exists() and not report.exists(), 'Preserve prior artifacts.'
    checked = []
    for line in (HERE / 'INPUT_PINS.sha256').read_text().splitlines():
        expected, path = line.split('  ', 1)
        actual = sha(ROOT / path)
        assert actual == expected, path
        checked.append({'path': path, 'sha256': actual})
    receipt = json.loads((HERE / 'native/receipt.json').read_text())
    assert receipt['pass'] and receipt['scientific_runs'] == 0
    assert len(receipt['commands']) == 3
    assert all(item['returncode'] == 0 for item in receipt['commands'])
    assert (HERE / 'native/input01.stdout.raw').read_bytes() == (HERE / 'native/input02.stdout.raw').read_bytes()
    assert (HERE / 'INPUT_PINS.sha256').read_bytes() == (HERE / 'native/input01.stdout.raw').read_bytes()
    for item in receipt['commands']:
        assert not (HERE / 'native' / item['stderr']).read_bytes()
    assert not (HERE / 'native/compare.stdout.raw').read_bytes()
    assert sha(HERE / 'capture_native.py') == receipt['source']['sha256']
    data = {'status': 'PASS_ARTIFACT_ONLY', 'author_side': True,
            'input_files_checked': checked, 'raw_output_pair_equal': True,
            'input_pins_equal_raw_output': True, 'native_command_count': 3,
            'scientific_run_count': 0,
            'limits': 'No independent review or complete runtime/loader audit.'}
    report.write_text(json.dumps(data, indent=2) + '\n')
    files = sorted(p for p in HERE.rglob('*') if p.is_file() and p != manifest)
    rows = [f'{sha(p)}  {p.relative_to(HERE).as_posix()}\n' for p in files]
    manifest.write_text(''.join(rows))
    for row in rows:
        expected, name = row.rstrip('\n').split('  ', 1)
        assert sha(HERE / name) == expected, name
    print(json.dumps({'status': 'PASS_ARTIFACT_ONLY', 'inputs': len(checked),
                      'manifest_payloads': len(rows), 'scientific_runs': 0}))

if __name__ == '__main__':
    main()
