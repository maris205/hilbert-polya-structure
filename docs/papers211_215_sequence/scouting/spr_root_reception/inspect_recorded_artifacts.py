"""Read-only SPR recorded-artifact reception; no map or theorem execution."""
from collections import Counter
import gzip
import hashlib
import itertools
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
BASE = HERE.parent / 'arithmetic_lane'


def sha(data):
    return hashlib.sha256(data).hexdigest()


def main():
    receipt = json.loads((BASE / 'sole_pilot/receipt.json').read_bytes())
    assert receipt['exit_code'] == 0 and not receipt['timed_out']
    assert receipt['inputs_before'] == receipt['inputs_after']
    for name, expected in receipt['inputs_before'].items():
        assert sha((BASE / name).read_bytes()) == expected, name
    assert sha(Path(receipt['interpreter_realpath']).read_bytes()) == receipt['interpreter_sha256']
    for name, expected in receipt['outputs'].items():
        raw = (BASE / 'sole_pilot' / name).read_bytes()
        assert sha(raw) == expected['sha256'] and len(raw) == expected['bytes'], name
    transcript = [json.loads(line) for line in (BASE / 'sole_pilot/stdout.raw').read_bytes().splitlines()]
    assert len(transcript) == 37 and transcript[0]['kind'] == 'preregistered_scope'
    last = transcript[-1]
    assert last['kind'] == 'all_checks_pass' and last['boxes'] == 35 and last['states'] == 34636
    runtime = last['runtime_surface']['visible_file_sha256']
    for name, expected in runtime.items():
        assert sha(Path(name).read_bytes()) == expected, name
    packed = (BASE / 'sole_pilot/state_records.jsonl.gz').read_bytes()
    raw = gzip.decompress(packed)
    assert sha(packed) == last['records_gzip_sha256']
    assert sha(raw) == last['records_uncompressed_sha256']
    lines = iter(raw.splitlines(keepends=True))
    total = 0
    box_results = []
    for summary, (n, bound) in zip(transcript[1:-1], itertools.product(range(1, 6), range(7)), strict=True):
        assert summary['kind'] == 'box_pass' and (summary['n'], summary['M']) == (n, bound)
        assert json.loads(next(lines)) == {'box': [n, bound]}
        hh, dd = Counter(), Counter()
        digest = hashlib.sha256()
        count = (bound + 1) ** n
        max_targets = []
        first_max_height = None
        for expected_x in itertools.product(range(bound + 1), repeat=n):
            line = next(lines)
            digest.update(line)
            x, target, height, degree = json.loads(line)
            assert tuple(x) == expected_x and len(target) == n
            assert all(type(v) is int and 0 <= v <= bound for v in target)
            assert type(height) is int and height >= 0
            assert type(degree) is int and 0 <= degree <= count
            hh[str(height)] += 1
            dd[str(degree)] += 1
            if degree == summary['max_fibre']:
                max_targets.append(x)
            if height == summary['max_height'] and first_max_height is None:
                first_max_height = x
        assert summary['states'] == count
        assert digest.hexdigest() == summary['per_state_records_sha256']
        assert dict(hh) == summary['height_histogram'] and dict(dd) == summary['fibre_histogram']
        assert max(map(int, hh)) == summary['max_height'] and max(map(int, dd)) == summary['max_fibre']
        assert max_targets == summary['all_max_fibre_targets']
        assert first_max_height == summary['first_max_height_witness']
        total += count
        box_results.append({'n': n, 'M': bound, 'records': count, 'sha256': digest.hexdigest()})
    assert next(lines, None) is None and total == 34636
    commands = []
    for path in sorted((BASE / 'commands').glob('*/receipt.json')):
        item = json.loads(path.read_bytes())
        for stream in ('stdout', 'stderr'):
            data = (path.parent / (stream + '.raw')).read_bytes()
            assert sha(data) == item[stream + '_sha256']
            assert len(data) == item[stream + '_bytes']
        commands.append({'receipt': str(path.relative_to(BASE)), 'exit_code': item['exit_code']})
    print(json.dumps({'status': 'PASS_RECORDED_ARTIFACTS_ONLY', 'new_scientific_executions': 0,
                      'explicit_inputs': len(receipt['inputs_before']), 'runtime_after_only_files': len(runtime),
                      'state_records': total, 'boxes': box_results, 'documentation_receipts': commands,
                      'limits': 'No transition, orbit, inverse, or inequality was recomputed. Runtime checks do not create a hermetic reuse key.'},
                     indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
