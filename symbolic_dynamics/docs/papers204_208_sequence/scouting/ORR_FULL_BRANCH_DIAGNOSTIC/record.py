#!/usr/bin/env python3
"""Small read/pin recorder for one non-computational ORR diagnostic."""
import hashlib
import json
import pathlib
import subprocess
import sys
import time

OWN = pathlib.Path(__file__).resolve().parent
ROOT = OWN.parents[3]
BASE = ROOT / 'docs/papers204_208_sequence/scouting'
ORIGINALS = [
    BASE / 'finite_systems_twenty_second/INTAKE.md',
    BASE / 'finite_systems_twenty_second/PRECODE_PROOFS.md',
    BASE / 'finite_systems_twenty_second/ORR_FIBRE_PROOF.md',
    BASE / 'ORR_ROOT_CLOCK_BOUNDARY.md',
    BASE / 'ORR_SECOND_CLOCK_ATTEMPT/PROOF_PACKAGE.md',
    BASE / 'ORR_SECOND_CLOCK_ATTEMPT/ATTEMPT_REPORT.md',
    BASE / 'ORR_SECOND_CLOCK_ATTEMPT/SOURCE_READS.md',
]


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def save(path, value):
    assert not path.exists(), str(path)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + '\n')


def capture(label, argv, inputs, cwd=ROOT):
    directory = OWN / 'commands' / label
    directory.mkdir(parents=True, exist_ok=False)
    paths = sorted(set([pathlib.Path(__file__).resolve()] + list(inputs)))
    before = {str(p): digest(p) for p in paths}
    save(directory / 'pathset.json', [str(p) for p in paths])
    save(directory / 'inputs_before.json', before)
    start = time.time()
    run = subprocess.run(argv, cwd=cwd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    (directory / 'stdout.raw').write_bytes(run.stdout)
    (directory / 'stderr.raw').write_bytes(run.stderr)
    after = {str(p): digest(p) for p in paths}
    save(directory / 'inputs_after.json', after)
    result = dict(role='documentary_execution_not_scientific_run', argv=argv,
                  cwd=str(cwd), started_epoch=start, finished_epoch=time.time(),
                  exit=run.returncode, inputs=len(paths), unchanged=before == after,
                  stdout_sha256=digest(directory / 'stdout.raw'),
                  stderr_sha256=digest(directory / 'stderr.raw'))
    save(directory / 'receipt.json', result)
    print(json.dumps(result, sort_keys=True))
    assert before == after
    assert run.returncode == 0


if __name__ == '__main__':
    mode = sys.argv[1]
    if mode == 'copy':
        destination = OWN / 'inputs'
        destination.mkdir(exist_ok=False)
        relative = [str(p.relative_to(ROOT)) for p in ORIGINALS]
        capture('01_original_copy', ['cp', '--parents', '-p'] + relative + [str(destination)], ORIGINALS)
        rows = []
        for original in ORIGINALS:
            copy = destination / original.relative_to(ROOT)
            assert digest(original) == digest(copy)
            rows.append(dict(original_path=str(original), copy_path=str(copy),
                             sha256=digest(copy), role='exact_copy_before_new_body_read'))
        save(OWN / 'ORIGINAL_ROLES.json', rows)
    elif mode == 'read':
        which = int(sys.argv[2])
        selected = ORIGINALS[:4] if which == 1 else ORIGINALS[4:]
        copies = [OWN / 'inputs' / p.relative_to(ROOT) for p in selected]
        capture('02_original_read' if which == 1 else '03_second_attempt_read',
                ['sed', '-n', '1,4000p'] + [str(p) for p in copies], copies)
    elif mode == 'seal':
        target = OWN / 'SHA256SUMS'
        assert not target.exists()
        paths = sorted(p for p in OWN.rglob('*') if p.is_file() and p != target)
        target.write_text(''.join(digest(p) + '  ' + str(p.relative_to(OWN)) + '\n' for p in paths))
        print(json.dumps(dict(nonself_payloads=len(paths), sha256=digest(target))))
    else:
        raise SystemExit('bad mode')
