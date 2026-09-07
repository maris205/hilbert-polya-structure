#!/usr/bin/env python3
"""One-shot physical preservation before the P210-Round0 index update."""
from pathlib import Path
from hashlib import sha256
import json
import subprocess

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
BATCH = ROOT / 'docs/papers204_208_sequence'
OUT = BATCH / 'qa/central_round0_p210'
ENV = {'PATH': '/usr/bin:/bin', 'LANG': 'C.UTF-8', 'LC_ALL': 'C.UTF-8', 'TZ': 'UTC'}
INPUTS = {
    ROOT / 'SYMBOLIC_DYNAMICS_STATE.md': '60e44803ceb8e5bb5502d887b586d0392fa68ee07cbf06745aa16f7c040c09eb',
    BATCH / 'PIPELINE_STATE.md': 'bb6d2f51f797bc648d06588b6ab0b8f79c26a61701f224a2685967a609eac057',
    BATCH / 'FINAL_THEOREM_CONTRACTS.md': '7872c4ca18824938881bda31ed5e9a2e7576c829242d529f4f9df19d7255c958',
    BATCH / 'GIT_SYNC_RECEIPT.md': 'afbe3112eda4dfccfed691f05c51f8c923139eb49072f07a5fa21df0f5ae2dea',
}


def info(path):
    assert path.is_file() and not path.is_symlink(), str(path)
    data = path.read_bytes()
    return {'bytes': len(data), 'sha256': sha256(data).hexdigest()}


def main():
    prerequisites = {}
    for name, status in [('P210_ROUND0_ROOT_CLOSURE_COMPLETION.actual.json', 'PASS_ROOT_PHYSICAL_P210_ROUND0_CLOSURE'),
                         ('P210_AUTHOR_STRICT_ROOT_COMPLETION.actual.json', 'PASS_ROOT_P210_AUTHOR_STRICT_PAIR_ORIGINAL_RECEPTION')]:
        path = BATCH / 'qa' / name
        actual = json.loads(path.read_bytes())
        assert actual['exit_code'] == 0
        assert json.loads(actual['output'])['status'] == status
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
    result = {'status': 'PASS_FOUR_EXACT_PRE_P210_ROUND0_CONTROL_COPIES', 'prerequisites': prerequisites, 'source': info(Path(__file__)),
              'copies': records, 'new_scientific_build_or_view_executions': 0, 'external_status': 'HOLD_EXTERNAL'}
    with (OUT / 'PRESERVATION.actual.json').open('x') as stream:
        json.dump(result, stream, sort_keys=True, indent=2); stream.write('\n')
    print(json.dumps(result, sort_keys=True, indent=2))


if __name__ == '__main__':
    main()
