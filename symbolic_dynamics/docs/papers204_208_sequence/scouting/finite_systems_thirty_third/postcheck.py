#!/usr/bin/env python3
"""Append-only exact-cwd manifest checks, preserving original seal."""
import hashlib
import json
import pathlib
import subprocess
import sys
import time
ROOT = pathlib.Path('/root/autodl-tmp/symbolic_dynamics')
OWN = pathlib.Path(__file__).resolve().parent

def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()
def save(p, obj):
    p.write_text(json.dumps(obj, indent=2, sort_keys=True) + '\n')

if sys.argv[1] == 'check':
    initial = []
    for line in (OWN / 'SHA256SUMS').read_text().splitlines():
        hashed, rel = line.split('  ', 1)
        assert digest(OWN / rel) == hashed, rel
        initial.append(OWN / rel)
    assert len(initial) == 192
    inputs = initial + [OWN / 'SHA256SUMS', pathlib.Path(__file__), OWN / 'POSTCHECK_FAILURE_TRANSCRIPTION.md', pathlib.Path('/usr/bin/sha256sum')]
    names = sorted(set(map(str, inputs)))
    wrong = ['sha256sum', '-c', 'docs/papers204_208_sequence/scouting/finite_systems_thirty_third/SHA256SUMS']
    correct = ['sha256sum', '-c', 'SHA256SUMS']
    for label, cwd, argv, expected in [('01_wrong_cwd_reproduction', ROOT, wrong, 1), ('02_correct_cwd', OWN, correct, 0)]:
        out = OWN / 'postcheck' / label
        out.mkdir(parents=True, exist_ok=False)
        save(out / 'pathset.json', names)
        before = {p: digest(pathlib.Path(p)) for p in names}
        save(out / 'inputs_before.json', before)
        started = time.time()
        r = subprocess.run(argv, cwd=cwd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        (out / 'stdout.raw').write_bytes(r.stdout)
        (out / 'stderr.raw').write_bytes(r.stderr)
        after = {p: digest(pathlib.Path(p)) for p in names}
        save(out / 'inputs_after.json', after)
        receipt = dict(role='new_documentary_execution_not_original_tool_transcription', label=label, cwd=str(cwd), argv=argv,
            exit=r.returncode, expected_exit=expected, input_count=len(names), unchanged=before==after,
            started_epoch=started, finished_epoch=time.time(), recorder_sha256=digest(pathlib.Path(__file__)),
            stdout_sha256=hashlib.sha256(r.stdout).hexdigest(), stderr_sha256=hashlib.sha256(r.stderr).hexdigest())
        save(out / 'receipt.json', receipt)
        print(json.dumps(receipt, sort_keys=True))
        assert before == after
        assert r.returncode == expected
elif sys.argv[1] == 'seal':
    target = OWN / 'FINAL_SHA256SUMS'
    assert not target.exists()
    files = sorted(p for p in OWN.rglob('*') if p.is_file() and p != target)
    target.write_text(''.join(digest(p) + '  ' + str(p.relative_to(OWN)) + '\n' for p in files))
    print(json.dumps(dict(nonself_payloads=len(files), sha256=digest(target))))
else:
    raise SystemExit(sys.argv[1])
