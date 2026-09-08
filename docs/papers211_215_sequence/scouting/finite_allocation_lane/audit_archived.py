#!/usr/bin/env python3
"""Read-only consistency audit of archived evidence; never evaluates MCA."""
from pathlib import Path
import hashlib
import json

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
HERE = Path(__file__).resolve().parent
OUT = HERE / 'evidence01'


def sha(data):
    return hashlib.sha256(data).hexdigest()


def main():
    originals = json.loads((OUT / 'original_capture.json').read_text())
    for row in originals:
        current = (ROOT / row['path']).read_bytes()
        frozen = (OUT / 'originals' / row['path']).read_bytes()
        assert current == frozen
        assert len(current) == row['bytes'] and sha(current) == row['sha256']
    inputs = json.loads((OUT / 'PILOT_INPUTS.json').read_text())
    for row in inputs:
        current = (HERE / row['path']).read_bytes()
        frozen = (OUT / 'pilot_inputs' / row['path']).read_bytes()
        assert current == frozen
        assert len(current) == row['bytes'] and sha(current) == row['sha256']
    commands = sorted(OUT.glob('*.command.json'))
    for path in commands:
        stem = path.name.removesuffix('.command.json')
        result = json.loads((OUT / (stem + '.result.json')).read_text())
        assert result['returncode'] == 0
        for key in ['stdout', 'stderr']:
            data = (OUT / (stem + '.' + key)).read_bytes()
            assert len(data) == result[key + '_bytes']
            assert sha(data) == result[key + '_sha256']
    records = [json.loads(line) for line in (OUT / '05_sole_pilot.stdout').read_text().splitlines()]
    summary = json.loads((OUT / 'pilot_summary.json').read_text())
    footer = records[-1]
    assert footer.pop('kind') == 'summary' and footer == summary
    assert len(records) == 5705 and summary['state_count'] == 5704
    assert summary['deductive_assertions'] == 17919
    assert len(summary['boxes']) == 30 and not summary['constant_max_counterexamples']
    assert len({(r['m'], r['N'], tuple(r['state'])) for r in records[:-1]}) == 5704
    assert all(r['kind'] == 'state' for r in records[:-1])
    assert len(commands) == 7 and len(inputs) == 4 and len(originals) == 8
    result = {'audit': 'ARCHIVED_CONSISTENCY_ONLY', 'historical_raw_pairs': len(originals),
              'pilot_input_raw_pairs': len(inputs), 'native_command_bindings': len(commands),
              'archived_state_records': len(records) - 1,
              'new_scientific_executions': 0}
    print(json.dumps(result, sort_keys=True))


if __name__ == '__main__':
    main()
