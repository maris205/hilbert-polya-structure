#!/usr/bin/env python3
"""One-shot physical preservation before the P210-admission index update."""
from pathlib import Path
from hashlib import sha256
import json
import subprocess

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
BATCH = ROOT / 'docs/papers204_208_sequence'
OUT = BATCH / 'qa/central_admission_p210'
ENV = {'PATH': '/usr/bin:/bin', 'LANG': 'C.UTF-8', 'LC_ALL': 'C.UTF-8', 'TZ': 'UTC'}
INPUTS = {
    ROOT / 'SYMBOLIC_DYNAMICS_STATE.md': '7f6506c6c4ce3f0e418e161f2ce508018bc651c07b42e2c738a0b4945fb8d5ec',
    BATCH / 'PIPELINE_STATE.md': 'fbd241b662b3169847e7ca09407c0037070bf4a32b2fecd93d5a4ecbe245d48a',
    BATCH / 'FINAL_THEOREM_CONTRACTS.md': '887f52a013a56e6ec638e80514a52cc1be290c1791d34fc345eba00d2aaf46e5',
    BATCH / 'GIT_SYNC_RECEIPT.md': '3793a50f6dc74cf5b4d2fc9626e00d5c28e14b739052ba78ecc6fd873377dbdd',
}


def info(path):
    assert path.is_file() and not path.is_symlink(), str(path)
    data = path.read_bytes()
    return {'bytes': len(data), 'sha256': sha256(data).hexdigest()}


def main():
    prerequisites = {}
    for name, status in [('MNA_ROOT_ORIGINAL_FINAL_RECEPTION.actual.json', 'PASS_ROOT_MNA_ORIGINAL_FINAL_RECEPTION'),
                         ('P209_CHECKPOINT_ROOT_COMPLETION.actual.json', 'PASS_ROOT_P209_COMPLETION_PRIVATE_CHECKPOINT_RECEPTION')]:
        path = BATCH / 'qa' / name
        actual = json.loads(path.read_bytes())
        assert actual['completion']['exit_code'] == 0
        assert json.loads(actual['completion']['output'])['status'] == status
        prerequisites[str(path)] = info(path)
    prerequisites[str(BATCH / 'P210_ROOT_ADMISSION.md')] = info(BATCH / 'P210_ROOT_ADMISSION.md')
    before = {str(p): info(p) for p in INPUTS}
    assert all(before[str(p)]['sha256'] == h for p, h in INPUTS.items())
    OUT.mkdir(exist_ok=False)
    records = []
    for source, expected in INPUTS.items():
        target = OUT / source.name
        assert not target.exists()
        commands = []
        for argv in (['/usr/bin/cp', '--', str(source), str(target)], ['/usr/bin/cmp', '--', str(source), str(target)]):
            run = subprocess.run(argv, cwd=ROOT, env=ENV, capture_output=True, check=False)
            commands.append({'argv': argv, 'cwd': str(ROOT), 'environment': ENV, 'exit_code': run.returncode,
                             'stdout': run.stdout.decode(), 'stderr': run.stderr.decode()})
            assert run.returncode == 0 and run.stdout == run.stderr == b''
        row = {'original': str(source), 'copy': str(target), 'before': before[str(source)], 'copy_pin': info(target), 'after': info(source), 'commands': commands}
        assert row['before'] == row['copy_pin'] == row['after']
        records.append(row)
    assert {str(p): info(p) for p in INPUTS} == before
    result = {'status': 'PASS_FOUR_EXACT_PRE_P210_CONTROL_COPIES', 'prerequisites': prerequisites, 'source': info(Path(__file__)),
              'copies': records, 'new_scientific_build_or_view_executions': 0, 'external_status': 'HOLD_EXTERNAL'}
    with (OUT / 'PRESERVATION.actual.json').open('x') as stream:
        json.dump(result, stream, sort_keys=True, indent=2); stream.write('\n')
    print(json.dumps(result, sort_keys=True, indent=2))


if __name__ == '__main__':
    main()
