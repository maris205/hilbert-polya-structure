#!/usr/bin/env python3
"""Documentary source acquisition only; no candidate scientific computation."""
import hashlib
import json
import pathlib
import subprocess
import sys
import time

OWN = pathlib.Path(__file__).resolve().parent
ROOT = OWN.parents[3]
OLD = ROOT / 'docs/papers204_208_sequence/scouting/finite_systems_twenty_first'
ORIGINALS = [OLD / name for name in ('INTAKE.md', 'SOURCE_AND_HISTORY.md', 'SOURCE_SUPPLEMENT.md')]


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def save(path, value):
    assert not path.exists(), str(path)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + '\n')


def capture(label, argv, inputs, timeout=None):
    directory = OWN / 'commands' / label
    directory.mkdir(parents=True, exist_ok=False)
    paths = sorted(set([pathlib.Path(__file__).resolve()] + list(inputs)))
    before = {str(p): digest(p) for p in paths}
    save(directory / 'inputs_before.json', before)
    start = time.time()
    timed_out = False
    try:
        result = subprocess.run(argv, cwd=ROOT, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=timeout)
        stdout, stderr, exit_code = result.stdout, result.stderr, result.returncode
    except subprocess.TimeoutExpired as failure:
        stdout, stderr, exit_code = failure.stdout or b'', failure.stderr or b'', 124
        timed_out = True
    (directory / 'stdout.raw').write_bytes(stdout)
    (directory / 'stderr.raw').write_bytes(stderr)
    elapsed = time.time() - start
    after = {str(p): digest(p) for p in paths}
    save(directory / 'inputs_after.json', after)
    receipt = dict(argv=argv, cwd=str(ROOT), started_epoch=start, elapsed_seconds=elapsed,
                   exit=exit_code, timed_out=timed_out, input_count=len(paths), unchanged=before == after,
                   role='documentary_source_command_not_scientific_execution',
                   stdout_sha256=digest(directory / 'stdout.raw'), stderr_sha256=digest(directory / 'stderr.raw'))
    save(directory / 'receipt.json', receipt)
    print(json.dumps(receipt, sort_keys=True))
    assert before == after
    return exit_code


if __name__ == '__main__':
    mode = sys.argv[1]
    if mode == 'copy':
        target = OWN / 'inputs'
        target.mkdir(exist_ok=False)
        assert capture('01_old_context_copy', ['cp', '-p'] + [str(p) for p in ORIGINALS] + [str(target)], ORIGINALS) == 0
        roles = []
        for original in ORIGINALS:
            copy = target / original.name
            assert digest(original) == digest(copy)
            roles.append(dict(original_path=str(original), copy_path=str(copy), sha256=digest(copy), role='copy_before_new_body_read'))
        save(OWN / 'ORIGINAL_ROLES.json', roles)
    elif mode == 'read':
        copies = [OWN / 'inputs' / p.name for p in ORIGINALS]
        assert capture('02_old_context_read', ['sed', '-n', '1,4000p'] + [str(p) for p in copies], copies) == 0
    elif mode == 'route':
        route_id, url = sys.argv[2:4]
        assert route_id in {'02', '03', '04', '05', '06'}
        route = OWN / 'routes' / route_id
        route.mkdir(parents=True, exist_ok=False)
        save(route / 'request.json', dict(url=url, max_seconds=40, process_timeout=43, route=route_id,
                                        role='legally_accessible_direct_request_no_credentials_or_bypass'))
        argv = ['curl', '--location', '--max-redirs', '5', '--connect-timeout', '12', '--max-time', '40',
                '--silent', '--show-error', '--dump-header', str(route / 'response.headers'),
                '--output', str(route / 'response.body'), '--write-out', '%{http_code}\n%{url_effective}\n%{content_type}\n%{size_download}\n', url]
        capture('route_' + route_id, argv, [route / 'request.json'], timeout=43)
    elif mode == 'seal':
        target = OWN / 'SHA256SUMS'
        assert not target.exists()
        paths = sorted(p for p in OWN.rglob('*') if p.is_file() and p != target)
        target.write_text(''.join(digest(p) + '  ' + str(p.relative_to(OWN)) + '\n' for p in paths))
        print(json.dumps(dict(nonself_payloads=len(paths), sha256=digest(target))))
    else:
        raise SystemExit('bad mode')
