"""One-shot artifact recorder. Refuses to overwrite any prior execution."""
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import time

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
BASE = Path(__file__).resolve().parent
HISTORY = [
    'papers/178-state-selected-finite-differences/main.tex',
    'papers/200-lex-first-alternating-switch/main.tex',
    'docs/papers177_181_sequence/scouting/root_crossdomain/SCOUT_AND_KILL_LEDGER.md',
    'docs/papers162_166_sequence/scouting/word_combinatorial/SCOUT.md',
    'docs/papers117_121_sequence/scouting/COMBINATORIAL_SCOUT.md',
    'docs/papers172_176_sequence/scouting/fresh_geometry_automata/SCOUT_AND_KILL_LEDGER.md',
    'docs/papers204_208_sequence/scouting/combinatorial/PROOF_NOTES.md',
    'docs/papers204_208_sequence/scouting/combinatorial/SOURCE_AND_COLLISION_NOTES.md',
    'docs/papers152_156_sequence/scouting/combinatorial_replacement2/SCOUT.md',
    'docs/papers204_208_sequence/scouting/ROOT_PREINTAKE_EXCLUSIONS_20260906.md',
    'docs/research_state/HISTORY_AND_CAVEATS.md',
]


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_json(path, value):
    assert not path.exists(), path
    path.write_text(json.dumps(value, sort_keys=True, indent=2) + '\n')


def manifest(path, mapping):
    assert not path.exists(), path
    path.write_text(''.join(f'{value}  {key}\n' for key, value in sorted(mapping.items())))


def main():
    assert sys.flags.optimize == 0
    for name in ('execution_01', 'execution_02', 'PAIR_RECEIPT.json', 'CANONICAL.json',
                 'HISTORICAL_INPUT_SHA256SUMS', 'PAIR_INPUTS_BEFORE.json', 'PAIR_INPUTS_AFTER.json'):
        assert not (BASE / name).exists(), name
    static = sorted(p for p in BASE.iterdir() if p.is_file())
    before = {str(p.relative_to(ROOT)): sha(p) for p in static}
    before.update({p: sha(ROOT / p) for p in HISTORY})
    write_json(BASE / 'PAIR_INPUTS_BEFORE.json', before)
    manifest(BASE / 'HISTORICAL_INPUT_SHA256SUMS', {p: before[p] for p in HISTORY})
    env = {'PATH': '/usr/local/bin:/usr/bin:/bin', 'LC_ALL': 'C', 'TZ': 'UTC'}
    runs = []
    all_ok = True
    for number in (1, 2):
        directory = BASE / f'execution_{number:02d}'
        directory.mkdir()
        inputs = directory / 'source_inputs'
        inputs.mkdir()
        for p in static:
            shutil.copy2(p, inputs / p.name)
        history_dir = directory / 'historical_inputs'
        for p in HISTORY:
            target = history_dir / p
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(ROOT / p, target)
        copied = sorted(p for root in (inputs, history_dir) for p in root.rglob('*') if p.is_file())
        input_before = {str(p.relative_to(directory)): sha(p) for p in copied}
        manifest(directory / 'INPUTS_BEFORE_SHA256SUMS', input_before)
        command = [sys.executable, '-I', '-B', str(inputs / 'runtime_wrapper.py'),
                   str(inputs / 'pilot.py'), str(directory)]
        started = time.time()
        with (directory / 'stdout.json').open('wb') as stdout, (directory / 'stderr.txt').open('wb') as stderr:
            process = subprocess.run(command, cwd=directory, env=env, stdout=stdout, stderr=stderr)
        elapsed = time.time() - started
        input_after = {str(p.relative_to(directory)): sha(p) for p in copied}
        manifest(directory / 'INPUTS_AFTER_SHA256SUMS', input_after)
        receipt = {'command': command, 'cwd': str(directory), 'environment': env,
                   'exit_code': process.returncode, 'elapsed_seconds': elapsed,
                   'stdout': 'stdout.json', 'stdout_sha256': sha(directory / 'stdout.json'),
                   'stderr': 'stderr.txt', 'stderr_sha256': sha(directory / 'stderr.txt'),
                   'input_files': len(input_before), 'unchanged_inputs': input_before == input_after,
                   'runtime_before': 'RUNTIME_BEFORE.json', 'runtime_after': 'RUNTIME_AFTER.json'}
        write_json(directory / 'COMMAND_RECEIPT.json', receipt)
        runs.append(receipt)
        all_ok = all_ok and process.returncode == 0 and input_before == input_after
    cmp_command = ['/usr/bin/cmp', str(BASE/'execution_01/stdout.json'), str(BASE/'execution_02/stdout.json')]
    compared = subprocess.run(cmp_command, cwd=BASE, env=env, capture_output=True)
    (BASE/'cmp.stdout').write_bytes(compared.stdout)
    (BASE/'cmp.stderr').write_bytes(compared.stderr)
    after = {p: sha(ROOT / p) for p in before}
    write_json(BASE/'PAIR_INPUTS_AFTER.json', after)
    receipt = {'role': 'AUTHOR_PAIR_NOT_INDEPENDENT_REVIEW', 'runs': runs,
               'compare': {'command': cmp_command, 'exit_code': compared.returncode,
                           'stdout': 'cmp.stdout', 'stderr': 'cmp.stderr'},
               'all_live_inputs_unchanged': before == after, 'live_input_count': len(before),
               'success': all_ok and compared.returncode == 0 and before == after}
    write_json(BASE/'PAIR_RECEIPT.json', receipt)
    if not receipt['success']:
        print(json.dumps(receipt, sort_keys=True, indent=2))
        raise SystemExit(1)
    shutil.copyfile(BASE/'execution_01/stdout.json', BASE/'CANONICAL.json')
    canonical_cmp = subprocess.run(['/usr/bin/cmp', str(BASE/'CANONICAL.json'), str(BASE/'execution_01/stdout.json')],
                                   cwd=BASE, env=env, capture_output=True)
    write_json(BASE/'CANONICAL_COPY_RECEIPT.json', {
        'command': ['/usr/bin/cmp', str(BASE/'CANONICAL.json'), str(BASE/'execution_01/stdout.json')],
        'exit_code': canonical_cmp.returncode,
        'stdout': canonical_cmp.stdout.decode(), 'stderr': canonical_cmp.stderr.decode(),
        'canonical_sha256': sha(BASE/'CANONICAL.json')})
    assert canonical_cmp.returncode == 0
    result = json.loads((BASE/'CANONICAL.json').read_text())
    print(json.dumps({k: result[k] for k in ('role','literal_maps_executed','complete_boxes','state_map_pairs','assertions')}, sort_keys=True))


if __name__ == '__main__':
    main()
