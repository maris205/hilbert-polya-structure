"""Author execution recorder; no mathematical kernels imported."""
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import sysconfig
import time

BASE = Path(__file__).resolve().parent
ROOT = BASE.parents[3]
HISTORICAL = [
    'docs/papers172_176_sequence/scouting/fresh_geometry_automata/SCOUT_AND_KILL_LEDGER.md',
    'docs/papers177_181_sequence/scouting/combinatorial_lane/SCOUT_AND_KILL_LEDGER.md',
    'docs/papers204_208_sequence/scouting/combinatorial_second/PROOF_NOTES.md',
    'docs/papers204_208_sequence/scouting/combinatorial_second/SCOUT_REPORT.md',
    'docs/papers162_166_sequence/scouting/replacement_matchings_incidence/SCOUT.md',
    'docs/papers204_208_sequence/scouting/finite_systems_thirteenth/PROOF_AND_DISPOSITION.md',
    'docs/papers132_136_sequence/replacement_scout/stochastic/SCOUT.md',
    'docs/papers132_136_sequence/replacement_scout/nondivisor_algebra/SCOUT.md',
    'docs/papers204_208_sequence/scouting/finite_systems_fourteenth/INTAKE.md',
    'docs/papers204_208_sequence/scouting/finite_systems_sixteenth/INTAKE.md',
    'docs/papers204_208_sequence/scouting/finite_systems_seventeenth/INTAKE.md',
    'docs/papers204_208_sequence/scouting/finite_systems_eighteenth/INTAKE.md',
    'docs/research_state/WORKFLOW.md', 'docs/research_state/HISTORY_AND_CAVEATS.md',
]


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def save(path, obj):
    path.write_text(json.dumps(obj, indent=2, sort_keys=True) + '\n', encoding='utf8')


def run(command, destination, tag, env):
    started = time.time()
    with (destination / (tag + '.stdout')).open('xb') as out, (destination / (tag + '.stderr')).open('xb') as err:
        result = subprocess.run(command, cwd=destination, env=env, stdout=out, stderr=err, check=False)
    receipt = dict(command=command, cwd=str(destination), exit=result.returncode,
                   started_epoch=started, finished_epoch=time.time(),
                   stdout=tag + '.stdout', stderr=tag + '.stderr')
    save(destination / (tag + '.command.json'), receipt)
    return result.returncode


def main():
    destination = BASE / sys.argv[1]
    destination.mkdir(exist_ok=False)
    env = {'PATH': '/usr/bin:/bin', 'LANG': 'C.UTF-8', 'LC_ALL': 'C.UTF-8', 'TZ': 'UTC'}
    save(destination / 'environment.json', env)
    inputs = destination / 'source_inputs'
    inputs.mkdir()
    source_names = ['INTAKE.md', 'SOURCE_AND_HISTORY.md', 'pilot.py', 'record_execution.py']
    for name in source_names:
        shutil.copyfile(BASE / name, inputs / name)
    science_before = {name: sha(BASE / name) for name in source_names}
    history_before = {name: sha(ROOT / name) for name in HISTORICAL}
    save(destination / 'source.before.json', science_before)
    save(destination / 'history.before.json', history_before)
    runtime_paths = {Path(sys.executable).resolve(), Path('/usr/bin/cmp').resolve(),
                     Path('/usr/bin/ldd').resolve(), Path('/bin/sh').resolve()}
    with open('/proc/self/maps', encoding='utf8') as mapped_source:
        runtime_paths |= {Path(line.split()[-1]).resolve() for line in mapped_source
                          if '/' in line and Path(line.split()[-1]).is_file()}
    stdlib = Path(sysconfig.get_path('stdlib'))
    for folder, directories, files in os.walk(stdlib):
        directories[:] = [d for d in directories if d not in ('site-packages', 'dist-packages', '__pycache__')]
        for file in files:
            path = Path(folder) / file
            if path.suffix in ('.py', '.so'):
                runtime_paths.add(path.resolve())
    # Pin startup and extension libraries before the producer, including dormant
    # stdlib extension libraries. This is a conservative provenance superset.
    linked = set()
    for path in sorted(runtime_paths):
        if path.suffix == '.so' or path == Path(sys.executable).resolve():
            proc = subprocess.run(['/usr/bin/ldd', str(path)], env=env, capture_output=True, check=False)
            for token in proc.stdout.decode('utf8', errors='replace').split():
                if token.startswith('/') and Path(token).is_file():
                    linked.add(Path(token).resolve())
    runtime_paths |= linked
    runtime_before = {str(p): sha(p) for p in sorted(runtime_paths)}
    save(destination / 'runtime.before.json', runtime_before)
    command = [str(Path(sys.executable).resolve()), '-I', '-S', '-B', '-X',
               'pycache_prefix=' + str(destination / 'never_written_cache'), str(inputs / 'pilot.py')]
    code = run(command, destination, 'producer', env)
    science_after = {name: sha(BASE / name) for name in source_names}
    history_after = {name: sha(ROOT / name) for name in HISTORICAL}
    runtime_after = {name: sha(name) for name in runtime_before}
    save(destination / 'source.after.json', science_after)
    save(destination / 'history.after.json', history_after)
    save(destination / 'runtime.after.json', runtime_after)
    if code:
        save(destination / 'RECEIPT.json', dict(status='PRODUCER_FAILED_PRESERVED', exit=code))
        raise SystemExit(code)
    observed = json.loads((destination / 'producer.stderr').read_text())
    used = set(observed['mapped_files'])
    for record in observed['modules'].values():
        path = record['file']
        if path and Path(path).is_file():
            used.add(str(Path(path).resolve()))
    capsule = {str((inputs / name).resolve()): sha(inputs / name) for name in source_names}
    uncovered = sorted(p for p in used if str(Path(p).resolve()) not in runtime_before and str(Path(p).resolve()) not in capsule)
    save(destination / 'runtime.observed.json', dict(paths=sorted(used), uncovered=uncovered, runtime=observed))
    intact = science_before == science_after and history_before == history_after and runtime_before == runtime_after
    save(destination / 'RECEIPT.json', dict(status='PASS' if intact and not uncovered else 'PROVENANCE_FAILED',
        source_inputs=len(science_before), historical_inputs=len(history_before), runtime_superset=len(runtime_before),
        observed_files=len(used), uncovered=uncovered, before_after_equal=intact,
        producer_exit=code, raw_stdout_sha256=sha(destination / 'producer.stdout'),
        output_bytes=(destination / 'producer.stdout').stat().st_size))
    print((destination / 'RECEIPT.json').read_text(), end='')
    if not intact or uncovered:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
