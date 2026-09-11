#!/usr/bin/env python3
"""One-shot physical preservation before the P210-Round1 index update."""
from pathlib import Path
from hashlib import sha256
import json
import subprocess

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
BATCH = ROOT / 'docs/papers204_208_sequence'
OUT = BATCH / 'qa/central_round1_p210'
ENV = {'PATH': '/usr/bin:/bin', 'LANG': 'C.UTF-8', 'LC_ALL': 'C.UTF-8', 'TZ': 'UTC'}
INPUTS = {
    ROOT / 'SYMBOLIC_DYNAMICS_STATE.md': '7a553b11a5fb5f02930847354534ebdbbdc470215c0f5f4941d7dd3964a9433a',
    BATCH / 'PIPELINE_STATE.md': '59df821cc8a7ee78ec8b2b5ae6c18e40f01c5636b05fc70e5da9170697449b0c',
    BATCH / 'FINAL_THEOREM_CONTRACTS.md': '7628735d02763d914c55843857e607274d9de2286cf7933bf20a1c877a89c99e',
    BATCH / 'GIT_SYNC_RECEIPT.md': 'ff0cd36ec6617a7355e85e29644c8432e37e45355b5e089bee468a86b626146e',
}


def info(path):
    assert path.is_file() and not path.is_symlink(), str(path)
    data = path.read_bytes()
    return {'bytes': len(data), 'sha256': sha256(data).hexdigest()}


def main():
    closure = BATCH / 'qa/P210_A_ROOT_DELTA_INSPECTION.actual.json'
    assert info(closure)['sha256'] == '38e5ca5009a583f5b126a29b60a98d9a936e28cf62d4c800310b98fec49d1650'
    accepted = json.loads(closure.read_bytes())
    assert accepted['status'] == 'ROOT_ACCEPTED_A_DELTA_ORIGINAL_CLOSURE_PASS'
    assert accepted['current_open_findings'] == 0 and accepted['resolved_major_findings'] == 1
    prerequisites = {str(closure): info(closure)}
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
    result = {'status': 'PASS_FOUR_EXACT_PRE_P210_ROUND1_CONTROL_COPIES', 'prerequisites': prerequisites, 'source': info(Path(__file__)),
              'copies': records, 'new_scientific_build_or_view_executions': 0, 'external_status': 'HOLD_EXTERNAL'}
    with (OUT / 'PRESERVATION.actual.json').open('x') as stream:
        json.dump(result, stream, sort_keys=True, indent=2); stream.write('\n')
    print(json.dumps(result, sort_keys=True, indent=2))


if __name__ == '__main__':
    main()
