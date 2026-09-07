"""Full author execution capsule; infrastructure pattern reused from lanes 19/21."""
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
ENV = {'PATH': '/usr/bin:/bin', 'LANG': 'C.UTF-8', 'LC_ALL': 'C.UTF-8', 'TZ': 'UTC'}
SOURCE = ['INTAKE.md', 'PRECODE_PROOFS.md', 'SOURCE_AND_HISTORY.md', 'pilot.py', 'record_execution.py']
HISTORICAL = [
    'docs/research_state/WORKFLOW.md',
    'docs/research_state/HISTORY_AND_CAVEATS.md',
    'docs/papers204_208_sequence/PROBLEM_ANCHOR.md',
    'docs/papers204_208_sequence/scouting/ROOT_PREINTAKE_EXCLUSIONS_20260906.md',
    'docs/papers204_208_sequence/scouting/word_local/SCOUT_REPORT.md',
    'docs/papers204_208_sequence/scouting/algebra/PROOF_NOTES.md',
    'docs/papers204_208_sequence/scouting/algebra/CS_GATE/CANDIDATE_GATE.md',
    'docs/papers204_208_sequence/scouting/finite_systems_sixteenth/INTAKE.md',
    'docs/papers204_208_sequence/scouting/finite_systems_seventeenth/INTAKE.md',
    'docs/papers204_208_sequence/scouting/finite_systems_eighteenth/INTAKE.md',
    'docs/papers204_208_sequence/scouting/finite_systems_twentieth/INTAKE.md',
    'docs/papers204_208_sequence/scouting/finite_systems_twenty_first/SCOUT_REPORT.md',
    'docs/papers167_171_sequence/scouting/p170_replacement_lane/SCOUT.md',
    'docs/papers122_126_sequence/scouting/combinatorial/SCOUT.md',
    'papers/117-odd-run-reversal-cyclic-words/main.tex',
    'docs/papers204_208_sequence/scouting/finite_systems_twenty_first/record_execution.py',
]


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def save(path, obj):
    with Path(path).open('x', encoding='utf8') as target:
        target.write(json.dumps(obj, sort_keys=True, indent=2) + '\n')


def run(command, destination, tag, env=ENV):
    before = time.time()
    with (destination / (tag + '.stdout')).open('xb') as out, (destination / (tag + '.stderr')).open('xb') as err:
        result = subprocess.run(command, cwd=destination, env=env, stdout=out, stderr=err, check=False)
    save(destination / (tag + '.command.json'), dict(command=command, cwd=str(destination),
        exit=result.returncode, started_epoch=before, finished_epoch=time.time(), environment=env,
        stdout=tag + '.stdout', stderr=tag + '.stderr'))
    return result.returncode


def config_state():
    paths = [Path('/etc/ld.so.cache'), Path('/etc/ld.so.conf'), Path('/etc/ld.so.preload')]
    paths += sorted(Path('/etc/ld.so.conf.d').glob('*.conf'))
    return {str(p): dict(exists=p.exists(), resolved=str(p.resolve()), sha256=sha(p) if p.is_file() else None)
            for p in paths}


def main():
    destination = BASE / sys.argv[1]
    destination.mkdir(exist_ok=False)
    save(destination / 'environment.json', ENV)
    inputs = destination / 'source_inputs'
    inputs.mkdir()
    for name in SOURCE:
        shutil.copyfile(BASE / name, inputs / name)
    history_dir = destination / 'historical_inputs'
    for name in HISTORICAL:
        target = history_dir / name
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(ROOT / name, target)
    science_before = {name: sha(BASE / name) for name in SOURCE}
    history_before = {name: sha(ROOT / name) for name in HISTORICAL}
    save(destination / 'source.before.json', science_before)
    save(destination / 'history.before.json', history_before)
    config_before = config_state()
    save(destination / 'configuration.before.json', config_before)
    runtime = {Path(sys.executable).resolve(), Path('/usr/bin/ldd').resolve(), Path('/bin/sh').resolve(),
               Path('/bin/bash').resolve(), Path('/usr/bin/cmp').resolve(), Path('/usr/bin/sha256sum').resolve()}
    with open('/proc/self/maps', encoding='utf8') as source:
        runtime |= {Path(line.split()[-1]).resolve() for line in source if '/' in line and Path(line.split()[-1]).is_file()}
    stdlib = Path(sysconfig.get_path('stdlib'))
    for folder, directories, files in os.walk(stdlib):
        directories[:] = [d for d in directories if d not in ('site-packages', 'dist-packages', '__pycache__')]
        for filename in files:
            path = Path(folder) / filename
            if path.suffix in ('.py', '.so'):
                runtime.add(path.resolve())
    for p, record in config_before.items():
        if record['sha256']:
            runtime.add(Path(p).resolve())
    links = destination / 'dynamic_links'
    links.mkdir()
    link_records = []
    for path in sorted(runtime):
        with path.open('rb') as source:
            is_elf = source.read(4) == b'\x7fELF'
        if not is_elf:
            continue
        tag = 'ldd_' + str(len(link_records)).zfill(3)
        pin_before = sha(path)
        code = run(['/usr/bin/ldd', str(path)], links, tag)
        output = (links / (tag + '.stdout')).read_text()
        dependencies = sorted({str(Path(s).resolve()) for s in output.split() if s.startswith('/') and Path(s).is_file()})
        runtime.update(Path(p) for p in dependencies)
        link_records.append(dict(target=str(path), target_before=pin_before, target_after=sha(path),
                                 tag=tag, exit=code, dependencies=dependencies))
    save(destination / 'dynamic_links.json', link_records)
    runtime_before = {str(p): sha(p) for p in sorted(runtime)}
    save(destination / 'runtime.before.json', runtime_before)
    cache = destination / 'never_written_cache'
    save(destination / 'execution_choices.json', dict(isolated=True, no_site=True, no_bytecode=True,
        optimization=0, pycache_prefix=str(cache), cache_exists_before=cache.exists(),
        old_cache_dirs_excluded=True, ambient_environment_not_inherited=True,
        recorder_version=sys.version, recorder_flags=repr(sys.flags), recorder_executable=sys.executable))
    code = run([str(Path(sys.executable).resolve()), '-I', '-S', '-B', '-X',
                'pycache_prefix=' + str(cache), str(inputs / 'pilot.py')], destination, 'producer')
    science_after = {name: sha(BASE / name) for name in SOURCE}
    history_after = {name: sha(ROOT / name) for name in HISTORICAL}
    runtime_after = {name: sha(name) for name in runtime_before}
    config_after = config_state()
    save(destination / 'source.after.json', science_after)
    save(destination / 'history.after.json', history_after)
    save(destination / 'runtime.after.json', runtime_after)
    save(destination / 'configuration.after.json', config_after)
    if code:
        save(destination / 'RECEIPT.json', dict(status='PRODUCER_FAILED_PRESERVED', producer_exit=code))
        raise SystemExit(code)
    observed = json.loads((destination / 'producer.stderr').read_text())
    used = set(observed['mapped_files'])
    used |= {str(Path(r['file']).resolve()) for r in observed['modules'].values()
             if r['file'] and Path(r['file']).is_file()}
    capsules = {str((inputs / name).resolve()): sha(inputs / name) for name in SOURCE}
    uncovered = sorted(p for p in used if str(Path(p).resolve()) not in runtime_before and str(Path(p).resolve()) not in capsules)
    save(destination / 'runtime.observed.json', dict(paths=sorted(used), uncovered=uncovered, runtime=observed))
    copies_equal = all(sha(inputs / n) == v for n, v in science_before.items()) and all(
        sha(history_dir / n) == v for n, v in history_before.items())
    intact = science_before == science_after and history_before == history_after and runtime_before == runtime_after and config_before == config_after
    clean = not cache.exists() and observed['xoptions'].get('pycache_prefix') == str(cache)
    passed = intact and copies_equal and clean and not uncovered and all(r['target_before'] == r['target_after'] and r['exit'] == 0 for r in link_records)
    save(destination / 'RECEIPT.json', dict(status='PASS' if passed else 'PROVENANCE_FAILED', source_inputs=len(SOURCE),
        historical_inputs=len(HISTORICAL), runtime_superset=len(runtime_before), observed_files=len(used),
        ldd_commands=len(link_records), configuration_entries=len(config_before), copies_equal=copies_equal,
        before_after_equal=intact, no_written_cache=clean, uncovered=uncovered, producer_exit=code,
        raw_stdout_sha256=sha(destination / 'producer.stdout'), output_bytes=(destination / 'producer.stdout').stat().st_size))
    print((destination / 'RECEIPT.json').read_text(), end='')
    if not passed:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
