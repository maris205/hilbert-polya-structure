#!/usr/bin/env python3
"""Record two real post-delta P207 source-only builds, without overwrites.

This is a new scoped execution recorder, not a change to cold_build.sh.
It does not inspect images or confer manuscript/batch acceptance.
"""
from datetime import datetime, timezone
from hashlib import sha256
import json
from pathlib import Path
import subprocess
import sys
import traceback


ROOT = Path(__file__).resolve().parents[3]
BATCH = ROOT/'docs/papers204_208_sequence'
PAPER = ROOT/'papers/207-upper-neighbor-rank-dynamics'
FREEZE = PAPER/'frozen_round2'
OUT = PAPER/'qa_final'


def info(path):
    raw = path.read_bytes()
    return {'sha256': sha256(raw).hexdigest(), 'bytes': len(raw)}


def utc():
    return datetime.now(timezone.utc).isoformat()


def main():
    if len(sys.argv) != 1:
        raise SystemExit('No arguments: exact P207 final-build scope only')
    for letter in ('a', 'b'):
        review = BATCH/f'reviews/p207_{letter}'
        finding = json.loads((review/'FINDINGS.json').read_bytes())
        if (finding['accepted_delta'] is not True or
                any(finding['census']['open'].values()) or not (review/'DELTA.md').is_file()):
            raise SystemExit('Accepted actual A/B delta and zero current findings required')
    if not (FREEZE/'SHA256SUMS').is_file():
        raise SystemExit('Physical Round2 required')
    OUT.mkdir(exist_ok=False)
    commands = []
    inputs = [p for p in FREEZE.rglob('*') if p.is_file()]
    inputs += [BATCH/'qa/cold_build.sh', Path(__file__).resolve()]
    for letter in ('a', 'b'):
        inputs += [BATCH/f'reviews/p207_{letter}'/name
                   for name in ('FINDINGS.json', 'DELTA.md', 'SHA256SUMS')]
    before = {str(p.relative_to(ROOT)): info(p) for p in sorted(inputs)}
    failure = None
    built = []

    def execute(label, command, cwd):
        row = {'label': label, 'command': command, 'cwd': str(cwd), 'started_utc': utc()}
        child = subprocess.run(command, cwd=cwd, capture_output=True)
        for kind, raw in (('stdout', child.stdout), ('stderr', child.stderr)):
            path = OUT/f'{label}.{kind}'
            with path.open('xb') as stream:
                stream.write(raw)
            row[kind] = {'path': path.name, **info(path)}
        row.update(exit_code=child.returncode, ended_utc=utc())
        commands.append(row)
        if child.returncode:
            raise RuntimeError(f'{label}: exit {child.returncode}')
        return child

    try:
        execute('round2_pins_before', ['sha256sum', '-c', str(FREEZE/'SHA256SUMS')], FREEZE)
        for k in (1, 2):
            target = OUT/f'cold_build_{k}'
            execute(f'cold_build_{k}', ['bash', str(BATCH/'qa/cold_build.sh'),
                    str(FREEZE), str(target), str(FREEZE/'main.pdf')], ROOT)
            source_names = []
            for line in (target/'SOURCE_INPUTS.sha256').read_text().splitlines():
                digest, name = line.split('  ', 1)
                if info(target/name)['sha256'] != digest or (target/name).read_bytes() != (FREEZE/name).read_bytes():
                    raise RuntimeError('Source-only input changed: '+name)
                source_names.append(name)
            diagnostic = [line for line in (target/'main.log').read_text().splitlines()
                          if any(word in line for word in ('Underfull', 'Overfull', 'Warning', 'undefined'))]
            host_paths = sorted({line[6:] for line in (target/'main.fls').read_text().splitlines()
                                 if line.startswith('INPUT ') and Path(line[6:]).is_absolute()})
            # These are contemporaneous post-build pins, explicitly not a
            # hermetic historical environment or pre-first-build snapshot.
            host_files = {name: info(Path(name)) for name in host_paths if Path(name).is_file()}
            if len(host_files) != len(host_paths):
                raise RuntimeError('An actual external TeX input cannot be pinned after build')
            built.append({'number': k, 'directory': str(target.relative_to(PAPER)),
                          'source_inputs': source_names, 'source_only_inputs_count': len(source_names),
                          'pdf': info(target/'main.pdf'), 'actual_diagnostics': diagnostic,
                          'external_TeX_inputs_pinned_after_build': host_files})
        execute('pair_pdf_cmp', ['cmp', str(OUT/'cold_build_1/main.pdf'),
                                str(OUT/'cold_build_2/main.pdf')], ROOT)
        execute('round2_pins_after', ['sha256sum', '-c', str(FREEZE/'SHA256SUMS')], FREEZE)
        for build in built:
            for name, wanted in build['external_TeX_inputs_pinned_after_build'].items():
                if info(Path(name)) != wanted:
                    raise RuntimeError('External TeX input changed after build: '+name)
    except BaseException as error:
        failure = {'type': type(error).__name__, 'message': str(error)}
        with (OUT/'BUILD_EXCEPTION.txt').open('x') as stream:
            stream.write(traceback.format_exc())
    after = {str(p.relative_to(ROOT)): info(p) for p in sorted(inputs)}
    passed = failure is None and before == after and len(built) == 2 and all(r['exit_code'] == 0 for r in commands)
    record = {'kind': 'ACTUAL_TWO_POST_DELTA_SOURCE_ONLY_TERMINAL_BUILDS_NOT_VISUAL_REVIEW',
              'status': 'BUILD_PAIR_PASS' if passed else 'BUILD_PAIR_FAIL', 'utc': utc(),
              'failure': failure, 'before_inputs': before, 'after_inputs': after,
              'input_bytes_unchanged': before == after, 'commands': commands, 'builds': built,
              'actual_page_view_status': 'PENDING_NOT_INFERRED_FROM_PDF_OR_PNG_HASH',
              'environment_boundary': 'Each helper records engine/version/settings; host TeX files are pinned after its build, not a hermetic or pre-build historical snapshot.',
              'external_status': 'HOLD_EXTERNAL'}
    with (OUT/'BUILD_EXECUTION.json').open('x') as stream:
        json.dump(record, stream, indent=2, sort_keys=True)
        stream.write('\n')
    print(json.dumps({'status': record['status'], 'commands': len(commands),
                      'builds': [{k: b[k] for k in ('number', 'source_only_inputs_count', 'pdf', 'actual_diagnostics')} for b in built],
                      'receipt': str(OUT/'BUILD_EXECUTION.json'), 'failure': failure}, indent=2))
    raise SystemExit(0 if passed else 1)


if __name__ == '__main__':
    main()
