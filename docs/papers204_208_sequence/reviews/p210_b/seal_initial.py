"""Finish the initial nonself seal only after actual evidence closure; no delta acceptance."""
import gzip
import hashlib
import json
import os
from pathlib import Path
import re
import sys
import time

HERE = Path(__file__).resolve().parent
ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
ENV = {'PATH': '/usr/bin:/bin', 'LANG': 'C.UTF-8', 'LC_ALL': 'C.UTF-8', 'TZ': 'UTC'}
assert dict(os.environ) == ENV
assert sys.flags.isolated and sys.flags.no_site and sys.dont_write_bytecode and sys.flags.optimize == 0
assert sys.pycache_prefix and not Path(sys.pycache_prefix).exists()
assert not (HERE / 'SHA256SUMS').exists() and not (HERE / 'SEAL_AUDIT.actual.json').exists()
started = time.time()
checks = 0


def demand(ok, label):
    global checks
    checks += 1
    assert ok, label


def sha(path):
    h = hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(1 << 20), b''):
            h.update(block)
    return h.hexdigest()


def obj(path):
    return json.loads(path.read_text())


required = ['REPORT.md', 'verify.py', 'verify.committed.py', 'PARAMETERS.json', 'CANONICAL.json',
            'REPLAY_LOG.md', 'REPLAY_KEYS.json', 'SOURCE_AND_PROOF.md', 'INDEPENDENT_PROOF.md',
            'BUILD_REPORT.md', 'VIEW_build02.actual.json', 'INPUT_PINS.sha256', 'FINDINGS.json',
            'DELTA.md', 'ARTIFACT_ROLES.md', 'READ_LIMITS.md', 'INDEPENDENCE_ORDER.md', 'AUDIT.actual.json',
            'native/audit02/RESULT.json', 'history/audit_package.attempt01.py']
for name in required:
    demand((HERE / name).is_file(), 'required physical role: ' + name)
findings = obj(HERE / 'FINDINGS.json')
demand(findings['current_open_counts'] == {'Critical': 0, 'Major': 0, 'Minor': 0}, 'all three severity levels explicitly audited')
demand(findings['reviewer_infrastructure_resolved_counts'] == {'Critical': 0, 'Major': 0, 'Minor': 2}, 'two real resolved B infrastructure Minors')
demand(findings['current_manuscript_findings'] == [] and not findings['accepted_delta'], 'no fabricated findings or premature acceptance')
demand('INITIAL_PENDING_ROOT_RESPONSE' in (HERE / 'DELTA.md').read_text(), 'initial-only delta gate')
for line in (HERE / 'INPUT_PINS.sha256').read_text().splitlines():
    expected, name = line.split('  ', 1)
    demand(sha(ROOT / name) == expected, 'all frozen input pins still exact')
files = sorted(p for p in HERE.rglob('*') if p.is_file())
demand(not any(p.suffix in {'.pyc', '.pyo'} for p in files), 'no package bytecode artifacts')
links = []
for path in HERE.glob('*.md'):
    for label, target in re.findall(r'\[([^\]]+)\]\(([^)]+)\)', path.read_text()):
        if target.startswith(('https://', 'http://', '#')):
            continue
        target = target.split('#', 1)[0]
        resolved = (path.parent / target).resolve()
        demand(resolved.is_file(), 'literal Markdown physical link: ' + str(path) + ' -> ' + target)
        links.append(dict(document=str(path.relative_to(HERE)), href=target, physical=str(resolved), sha256=sha(resolved)))
native = []
for path in files:
    if path.name != 'RESULT.json' or not (path.parent / 'ATTEMPT.json').is_file():
        continue
    start, end = obj(path.parent / 'ATTEMPT.json'), obj(path)
    expected = 1 if path.parent in {HERE / 'native/build01', HERE / 'native/audit01'} else 0
    demand(type(end['native_returncode']) is int and end['native_returncode'] == expected, 'actual numeric native return')
    demand(start['environment'] == ENV, 'safe explicit environment')
    demand(end.get('end_ns', end.get('ended_epoch')) >= start.get('start_ns', start.get('started_epoch')), 'actual time order')
    for key in ['stdout', 'stderr']:
        expected_sha = end[key]['sha256'] if key in end else end[key + '_sha256']
        demand(sha(path.parent / key) == expected_sha, 'completed raw native stream binding')
        if key in end:
            demand((path.parent / key).stat().st_size == end[key]['bytes'], 'raw native stream size')
    settlement = end.get('settlement', end.get('process_group_settlement'))
    demand(settlement['quiescent'] and not any(row['state'] != 'Z' for row in settlement['remaining_members']), 'owned native settlement')
    if 'launcher_source' in start:
        launcher = HERE / ('launch_build_v2.py' if path.parent.name == 'build02' else
                          'launch.py' if path.parent.name in {'produce01', 'pair01', 'build01'} else 'launch_command.py')
        demand(sha(launcher) == start['launcher_source']['sha256'], 'actual transport start source remains exact')
    if 'engine_source' in start:
        engine = HERE / 'instrumentation' / ('evidence_build_v2.py' if path.parent.name == 'build02' else 'evidence.py')
        demand(sha(engine) == start['engine_source']['sha256'], 'actual evidence engine start source remains exact')
    native.append(dict(directory=str(path.parent.relative_to(HERE)), native_returncode=expected))
audit = obj(HERE / 'AUDIT.actual.json')
demand(audit['status'] == 'PASS_INITIAL_EVIDENCE_AUDIT' and audit['checks'] == 259277, 'actual prior complete audit')
with gzip.open(HERE / 'AUDIT_INPUTS.actual.json.gz', 'rt') as stream:
    inputs = json.load(stream)
demand(len(inputs) == 120840, 'actual full byte-read key count')
# The seal does not repeat the 120k-file resource audit; it binds its exact ledger bytes.
demand(obj(HERE / 'native/audit02/RESULT.json')['native_returncode'] == 0, 'completed audit02 parent native 0')
result = dict(status='PASS_INITIAL_SEAL_GATE_NOT_ACCEPTED_DELTA', checks=checks,
              started_epoch=started, ended_epoch=time.time(), native_receipts_checked=len(native),
              native_receipts=native, links=links, source_sha256=sha(Path(__file__)),
              prior_full_audit= {'path': 'AUDIT.actual.json', 'sha256': sha(HERE / 'AUDIT.actual.json')},
              initial_phase='INITIAL_PENDING_ROOT_RESPONSE', payload_files_including_this_gate=len(files)+1,
              boundary='All files physically sealed; evidence audit not reexecuted; own ordinary native tool return is outside nonself package.')
with (HERE / 'SEAL_AUDIT.actual.json').open('x') as stream:
    json.dump(result, stream, sort_keys=True, indent=2)
    stream.write('\n')
payloads = sorted(p for p in HERE.rglob('*') if p.is_file())
with (HERE / 'SHA256SUMS').open('x') as stream:
    for path in payloads:
        stream.write(sha(path) + '  ' + str(path.relative_to(HERE)) + '\n')
actual = {str(p.relative_to(HERE)) for p in HERE.rglob('*') if p.is_file() and p.name != 'SHA256SUMS'}
listed = {}
for line in (HERE / 'SHA256SUMS').read_text().splitlines():
    expected, name = line.split('  ', 1)
    demand(name not in listed and sha(HERE / name) == expected, 'final nonself manifest payload verification')
    listed[name] = expected
demand(set(listed) == actual and len(listed) == len(files)+1, 'exact final physical payload coverage')
print(json.dumps(dict(status='SEALED_INITIAL_PENDING_ROOT_RESPONSE', payloads=len(listed), physical_files=len(listed)+1,
                     manifest_sha256=sha(HERE / 'SHA256SUMS'), checks_including_manifest=checks,
                     complete_native_receipts_checked=len(native), manuscript_open=findings['current_open_counts']), sort_keys=True))
