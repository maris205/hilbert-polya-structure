"""One-time complete initial review closure; never rewrite prior artifacts."""
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import sys
import time

BASE = Path(__file__).resolve().parent
ROOT = BASE.parents[3]
ENV = {'PATH': '/usr/bin:/bin', 'LANG': 'C.UTF-8', 'LC_ALL': 'C.UTF-8', 'TZ': 'UTC'}
assert dict(os.environ) == ENV and sys.flags.optimize == 0 and sys.flags.no_site and sys.flags.isolated
assert not (BASE / 'SHA256SUMS').exists()
assert not (BASE / 'INITIAL_ARTIFACTS.sha256').exists()
assert not (BASE / 'INITIAL_REPORT.md').exists()
AUDIT = BASE / 'initial_audit_01'
assert not AUDIT.exists()
AUDIT.mkdir()
def digest(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda: stream.read(1048576), b''):
            h.update(block)
    return h.hexdigest()
def save(name, payload):
    with (AUDIT / name).open('x') as stream:
        stream.write(json.dumps(payload, indent=2, sort_keys=True) + '\n')
save('ATTEMPT.json', {'argv': sys.orig_argv, 'env': dict(os.environ), 'cwd': str(Path.cwd()), 'flags': str(sys.flags), 'started_epoch': time.time(), 'script_sha256': digest(__file__), 'phase': 'INITIAL_ONLY_NO_DELTA'})
shutil.copyfile(BASE / 'REPORT.md', BASE / 'INITIAL_REPORT.md')
manifests = []
for manifest in sorted(BASE.rglob('SHA256SUMS')):
    lines, seen = manifest.read_text().splitlines(), set()
    for line in lines:
        pin, name = line.split('  ', 1)
        p = Path(name)
        assert re.fullmatch('[0-9a-f]{64}', pin) and not p.is_absolute() and '..' not in p.parts and name != 'SHA256SUMS' and name not in seen
        seen.add(name)
        assert digest(manifest.parent / name) == pin, str(manifest.parent / name)
    assert seen == {p.relative_to(manifest.parent).as_posix() for p in manifest.parent.rglob('*') if p.is_file() and p != manifest}
    manifests.append({'path': str(manifest), 'payloads': len(lines), 'sha256': digest(manifest)})
save('INNER_MANIFESTS.json', manifests)
freeze_rows = (BASE / 'INPUT_PINS.sha256').read_text().splitlines()
for line in freeze_rows:
    pin, name = line.split('  ', 1)
    assert digest(ROOT / name) == pin, name
assert len(freeze_rows) == 1990
known = {}
for name in ['review_pair_01/ALL_INPUTS_INCLUDING_CAPSULES_BEFORE.json', 'review_pair_01/ALL_INPUTS_AFTER.json',
             'review_build_01/ALL_INPUTS_INCLUDING_CAPSULES_BEFORE.json', 'review_build_01/ALL_INPUTS_AFTER.json',
             'reconciliation_01/INPUTS_BEFORE.json', 'reconciliation_01/INPUTS_AFTER.json',
             'auxiliary_01/INPUTS_BEFORE.json', 'auxiliary_01/INPUTS_AFTER.json']:
    data = json.loads((BASE / name).read_bytes())
    for path, row in data.items():
        pin = row['sha256']
        assert path not in known or known[path] == pin, path
        known[path] = pin
for path, pin in known.items():
    assert digest(path) == pin, path
save('CURRENT_INPUT_CLOSURE.json', known)
assert digest(BASE / 'verify.py') == '28fad641f3928907c9dca259b3360000f0c9063edee7005148ed9a5fc10779af'
assert digest(BASE / 'CANONICAL.json') == '9dd6229968748e2caf0e3fe74b802603b6dc51f37704bdf098dbdfb969433b36'
findings = json.loads((BASE / 'FINDINGS.json').read_bytes())
assert findings['findings'] == [] and not any(findings['current_open_counts'].values())
assert not (BASE / 'DELTA.md').exists()
for name in ['REPORT.md', 'SOURCE_AND_PROOF.md', 'BUILD_REPORT.md', 'REPLAY_LOG.md', 'verify.py', 'CANONICAL.json', 'INPUT_PINS.sha256', 'FINDINGS.json']:
    assert (BASE / name).is_file() and (BASE / name).stat().st_size
save('RESULT.json', {'status': 'PASS_INITIAL_PACKAGE_CLOSURE', 'freeze_pins': len(freeze_rows), 'inner_manifests': manifests, 'current_input_paths': len(known), 'original_mathematical_commitment_unchanged': True, 'open_findings': 0, 'delta_exists': False, 'scope': 'Actual hashes/manifests/artifact roles; no new mathematical producer, compiler, renderer or visual inspection.'})
payloads = sorted(p for p in BASE.rglob('*') if p.is_file())
assert not any(p.is_symlink() for p in payloads)
with (BASE / 'INITIAL_ARTIFACTS.sha256').open('x') as stream:
    stream.write(''.join(digest(p) + '  ' + p.relative_to(BASE).as_posix() + '\n' for p in payloads))
payloads.append(BASE / 'INITIAL_ARTIFACTS.sha256')
with (BASE / 'SHA256SUMS').open('x') as stream:
    stream.write(''.join(digest(p) + '  ' + p.relative_to(BASE).as_posix() + '\n' for p in sorted(payloads)))
for line in (BASE / 'SHA256SUMS').read_text().splitlines():
    pin, name = line.split('  ', 1)
    assert digest(BASE / name) == pin
print(json.dumps({'status': 'SEALED_INITIAL_REVIEW', 'payloads': len(payloads), 'seal_sha256': digest(BASE / 'SHA256SUMS'), 'initial_explicit_payloads': len(payloads) - 1, 'current_input_paths': len(known), 'input_pins': len(freeze_rows), 'initial_report_sha256': digest(BASE / 'INITIAL_REPORT.md'), 'delta_exists': False}, sort_keys=True))
