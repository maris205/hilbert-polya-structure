#!/usr/bin/env python3
"""One-shot exact pre-index preservation, after final P209 root acceptance.

Only creates the explicitly named new control-snapshot package. Never edits
any source, accepted paper or historical record; exclusive creation only.
"""
from hashlib import sha256
import json
from pathlib import Path
import shutil
import subprocess

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
BATCH = ROOT / 'docs/papers204_208_sequence'
OUT = BATCH / 'qa/central_lifecycle_p209_complete'
ENV = {'PATH': '/usr/bin:/bin', 'LANG': 'C.UTF-8', 'LC_ALL': 'C.UTF-8', 'TZ': 'UTC'}
INPUTS = {
    ROOT / 'SYMBOLIC_DYNAMICS_STATE.md': '736e3f648bc6dda583254dcc58f49fc764043c30ea464ec524fac04f2ec67265',
    BATCH / 'PIPELINE_STATE.md': '70de1375b0b55339408b7399178a17f91f3058b3f068faa7c395ab633e525b47',
    BATCH / 'GIT_SYNC_RECEIPT.md': '303e1ad876f35fc6715d896f2979fd212f64aeb686ebd8ee1e2d649e9628b230',
    BATCH / 'FINAL_THEOREM_CONTRACTS.md': 'cc45f5de4a943b2f2aff4d0d4d2e990cf77bca99d49ea5c497cc93782dbdedd9',
}


def info(path):
    assert path.is_file() and not path.is_symlink(), str(path)
    data = path.read_bytes()
    return {'bytes': len(data), 'sha256': sha256(data).hexdigest()}


def main():
    gate = BATCH / 'qa/P209_LIFECYCLE_ROOT_INSPECTION.actual.json'
    actual = json.loads(gate.read_bytes())
    assert actual['completion']['exit_code'] == 0
    result = json.loads(actual['completion']['output'])
    assert result['status'] == 'PASS_ROOT_P209_FINAL_LIFECYCLE_ORIGINAL_INSPECTION'
    assert result['final_manifest_sha256'] == 'c6d10fac378e6c1dfefa831a16cc3d9deb1e404cf0d3e75120628212af75bd3c'
    before = {str(p): info(p) for p in INPUTS}
    assert all(before[str(p)]['sha256'] == h for p, h in INPUTS.items())
    OUT.mkdir(exist_ok=False)
    records = []
    for origin, expected in INPUTS.items():
        target = OUT / origin.name
        assert not target.exists()
        shutil.copyfile(origin, target)
        argv = ['/usr/bin/cmp', '--', str(origin), str(target)]
        command = subprocess.run(argv, cwd=ROOT, env=ENV, capture_output=True, check=False)
        record = {'original': str(origin), 'copy': str(target), 'expected_sha256': expected,
                  'before': before[str(origin)], 'copy_pin': info(target), 'after': info(origin),
                  'argv': argv, 'cwd': str(ROOT), 'environment': ENV, 'exit_code': command.returncode,
                  'stdout': command.stdout.decode(), 'stderr': command.stderr.decode()}
        records.append(record)
        assert record['before'] == record['copy_pin'] == record['after']
        assert command.returncode == 0 and not command.stdout and not command.stderr
    assert {str(p): info(p) for p in INPUTS} == before
    receipt = {'schema': 'p209-completion-pre-index-controls-v1',
               'status': 'PASS_FOUR_EXACT_PREUPDATE_COPIES', 'root_acceptance': info(gate),
               'source': info(Path(__file__)), 'copies': records,
               'new_scientific_build_or_view_executions': 0, 'external_status': 'HOLD_EXTERNAL'}
    with (OUT / 'PRESERVATION.actual.json').open('x') as file:
        json.dump(receipt, file, indent=2, sort_keys=True)
        file.write('\n')
    print(json.dumps(receipt, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
