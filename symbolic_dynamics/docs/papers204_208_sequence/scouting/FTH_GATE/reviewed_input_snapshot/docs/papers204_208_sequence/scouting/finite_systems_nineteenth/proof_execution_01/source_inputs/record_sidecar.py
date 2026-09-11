"""Reuse recording infrastructure only; no prior scientific kernel imports."""
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import sysconfig

import record_execution as infrastructure

BASE = Path(__file__).resolve().parent
ROOT = BASE.parents[3]
sha, save, run = infrastructure.sha, infrastructure.save, infrastructure.run


def main():
    destination = BASE / sys.argv[1]
    destination.mkdir(exist_ok=False)
    env = {'PATH': '/usr/bin:/bin', 'LANG': 'C.UTF-8', 'LC_ALL': 'C.UTF-8', 'TZ': 'UTC'}
    save(destination / 'environment.json', env)
    inputs = destination / 'source_inputs'
    inputs.mkdir()
    sources = {'INTAKE.md': 'INTAKE.md', 'SOURCE_AND_HISTORY.md': 'SOURCE_AND_HISTORY.md',
               'FTH_PROOF_PACKAGE.md': 'FTH_PROOF_PACKAGE.md', 'verify_fth.py': 'verify_fth.py',
               'record_sidecar.py': 'record_sidecar.py', 'record_execution.py': 'record_execution.py',
               'execution_01/producer.stdout': 'original_pilot.stdout'}
    for original, copy in sources.items():
        shutil.copyfile(BASE / original, inputs / copy)
    history = infrastructure.HISTORICAL + ['docs/papers204_208_sequence/scouting/FTH_ROOT_LOCAL_OBSERVATIONS.md']
    science_before = {name: sha(BASE / name) for name in sources}
    history_before = {name: sha(ROOT / name) for name in history}
    save(destination / 'source.before.json', science_before)
    save(destination / 'history.before.json', history_before)
    runtime_paths = {Path(sys.executable).resolve(), Path('/usr/bin/cmp').resolve(),
                     Path('/usr/bin/ldd').resolve(), Path('/bin/sh').resolve()}
    with open('/proc/self/maps', encoding='utf8') as source:
        runtime_paths |= {Path(line.split()[-1]).resolve() for line in source
                          if '/' in line and Path(line.split()[-1]).is_file()}
    for folder, directories, files in os.walk(Path(sysconfig.get_path('stdlib'))):
        directories[:] = [d for d in directories if d not in ('site-packages', 'dist-packages', '__pycache__')]
        runtime_paths |= {Path(folder, name).resolve() for name in files if Path(name).suffix in ('.py', '.so')}
    linked = set()
    for path in sorted(runtime_paths):
        if path.suffix == '.so' or path == Path(sys.executable).resolve():
            proc = subprocess.run(['/usr/bin/ldd', str(path)], env=env, capture_output=True, check=False)
            linked |= {Path(token).resolve() for token in proc.stdout.decode('utf8', errors='replace').split()
                       if token.startswith('/') and Path(token).is_file()}
    runtime_paths |= linked
    runtime_before = {str(p): sha(p) for p in sorted(runtime_paths)}
    save(destination / 'runtime.before.json', runtime_before)
    command = [str(Path(sys.executable).resolve()), '-I', '-S', '-B', str(inputs / 'verify_fth.py')]
    code = run(command, destination, 'producer', env)
    science_after = {name: sha(BASE / name) for name in sources}
    history_after = {name: sha(ROOT / name) for name in history}
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
        if record['file'] and Path(record['file']).is_file():
            used.add(str(Path(record['file']).resolve()))
    capsule = {str((inputs / name).resolve()) for name in sources.values()}
    uncovered = sorted(p for p in used if str(Path(p).resolve()) not in runtime_before
                       and str(Path(p).resolve()) not in capsule)
    save(destination / 'runtime.observed.json', dict(paths=sorted(used), uncovered=uncovered, runtime=observed))
    intact = science_before == science_after and history_before == history_after and runtime_before == runtime_after
    save(destination / 'RECEIPT.json', dict(status='PASS' if intact and not uncovered else 'PROVENANCE_FAILED',
        source_inputs=len(sources), historical_inputs=len(history), runtime_superset=len(runtime_before),
        observed_files=len(used), uncovered=uncovered, before_after_equal=intact,
        producer_exit=code, raw_stdout_sha256=sha(destination / 'producer.stdout'),
        output_bytes=(destination / 'producer.stdout').stat().st_size))
    print((destination / 'RECEIPT.json').read_text(), end='')
    if not intact or uncovered:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
