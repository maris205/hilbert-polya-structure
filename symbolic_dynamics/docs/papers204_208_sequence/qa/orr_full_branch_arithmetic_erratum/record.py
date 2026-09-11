#!/usr/bin/env python3
"""Hash receipt for a local wording erratum; no mathematical execution."""
import hashlib
import json
import pathlib
import subprocess
import sys
import time

OWN = pathlib.Path(__file__).resolve().parent
ROOT = OWN.parents[3]
OLD = ROOT / 'docs/papers204_208_sequence/scouting/ORR_FULL_BRANCH_DIAGNOSTIC'


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def save(path, value):
    assert not path.exists(), str(path)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + '\n')


if __name__ == '__main__':
    if sys.argv[1] == 'record':
        target = OWN / 'check'
        target.mkdir(exist_ok=False)
        originals = [OLD / 'PROOF_PACKAGE.md', OLD / 'SHA256SUMS']
        paths = originals + [OWN / 'CORRECTION.md', pathlib.Path(__file__).resolve()]
        before = {str(p): digest(p) for p in paths}
        save(target / 'inputs_before.json', before)
        argv = ['sha256sum'] + [str(p) for p in originals]
        started = time.time()
        run = subprocess.run(argv, cwd=ROOT, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        (target / 'stdout.raw').write_bytes(run.stdout)
        (target / 'stderr.raw').write_bytes(run.stderr)
        after = {str(p): digest(p) for p in paths}
        save(target / 'inputs_after.json', after)
        proof_entry = next(line[:64] for line in (OLD / 'SHA256SUMS').read_text().splitlines() if line[66:] == 'PROOF_PACKAGE.md')
        receipt = dict(argv=argv, cwd=str(ROOT), started_epoch=started, finished_epoch=time.time(), exit=run.returncode,
            input_count=len(paths), unchanged=before == after,
            original_proof_matches_seal=digest(originals[0]) == proof_entry,
            expected_original_seal=digest(originals[1]) == 'b0b23a0ba5396035251085a7a007c151623ad17013944fdd4dfe17783bd16024',
            stdout_sha256=digest(target / 'stdout.raw'), stderr_sha256=digest(target / 'stderr.raw'),
            role='documentary_hash_check_only_not_mathematical_execution')
        save(target / 'receipt.json', receipt)
        print(json.dumps(receipt, sort_keys=True))
        assert run.returncode == 0 and before == after
        assert receipt['original_proof_matches_seal'] and receipt['expected_original_seal']
    elif sys.argv[1] == 'seal':
        target = OWN / 'SHA256SUMS'
        assert not target.exists()
        paths = sorted(p for p in OWN.rglob('*') if p.is_file() and p != target)
        target.write_text(''.join(digest(p) + '  ' + str(p.relative_to(OWN)) + '\n' for p in paths))
        print(json.dumps(dict(nonself_payloads=len(paths), sha256=digest(target))))
    else:
        raise SystemExit('bad mode')
