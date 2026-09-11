"""Same complete scout29 audit, bounded-output v2; no mathematical producer."""
from contextlib import redirect_stdout
from hashlib import sha256
import io
import json
import os
from pathlib import Path
import re
import runpy
import subprocess
import sys

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
BASE = ROOT / 'docs/papers204_208_sequence/scouting/finite_systems_twenty_ninth'
SEAL = 'f8cf3a7c8aae24a3313e1f6ab76dbabd7a6144b6d769e1fbf805c2925e123cf0'
ENV = {'PATH': '/usr/bin:/bin', 'LANG': 'C.UTF-8', 'LC_ALL': 'C.UTF-8', 'TZ': 'UTC'}
READS = {}

def pin(path):
    path = Path(path).absolute()
    assert path.is_file(), str(path)
    if path.is_relative_to(ROOT):
        assert not path.is_symlink(), str(path)
    row = {'sha256': sha256(path.read_bytes()).hexdigest(),
           'bytes': path.stat().st_size, 'resolved': str(path.resolve()),
           'symlink': os.readlink(path) if path.is_symlink() else None}
    if str(path) in READS:
        assert READS[str(path)] == row, ('drift', str(path))
    READS[str(path)] = row
    return row

def manifest():
    path = BASE / 'SHA256SUMS'
    assert pin(path)['sha256'] == SEAL
    rows = {}
    for line in path.read_text().splitlines():
        value, name = line.split('  ', 1)
        p = Path(name)
        assert re.fullmatch('[0-9a-f]{64}', value)
        assert not p.is_absolute() and '..' not in p.parts
        assert name == p.as_posix() and name not in rows and name != 'SHA256SUMS'
        assert pin(BASE / p)['sha256'] == value
        rows[name] = value
    files = list(BASE.rglob('*'))
    assert not any(p.is_symlink() for p in files)
    assert set(rows) == {p.relative_to(BASE).as_posix() for p in files
                         if p.is_file() and p != path}
    assert len(rows) == 168
    return rows

pin(__file__)
outer = manifest()
audit = BASE / 'audit.py'
pin(audit)
prior_argv = sys.argv
sys.argv = [str(audit), '--manifest']
captured = io.StringIO()
try:
    with redirect_stdout(captured):
        result = runpy.run_path(str(audit), run_name='__main__')
finally:
    sys.argv = prior_argv
audit_stdout = captured.getvalue()
summary = json.loads(audit_stdout)
assert summary['status'] == 'PASS_AUTHOR_READ_ONLY_ARTIFACT_AUDIT'
assert summary['counts'] == {'manifest_payloads': 168, 'pin_rows': 37873,
                            'snapshots': 25, 'command_receipts': 25,
                            'full_scope_searches': 3, 'raw_pairs': 3}
assert summary['unique_read_paths_rechecked'] == 5511
for path, value in result['reads'].items():
    assert pin(path)['sha256'] == value
aliases = []
for (name, value), physical in sorted(result['aliases'].items()):
    assert pin(physical)['sha256'] == value
    aliases.append({'original_path': str(ROOT / name), 'original_sha256': value,
                    'physical_path': str(physical)})
# Inspect complete archived command streams and explicit named-tool identities.
command_rows = []
for path in sorted((BASE / 'evidence').glob('*/receipt.json')):
    receipt = json.loads(path.read_bytes())
    for stream in ('stdout', 'stderr'):
        assert pin(path.parent / (stream + '.bin'))['sha256'] == receipt[stream + '_sha256']
    command_rows.append({'label': path.parent.name, 'command_record': str(path),
                         'command_record_sha256': pin(path)['sha256'],
                         'argv_sha256': sha256(json.dumps(receipt['argv'], separators=(',', ':')).encode()).hexdigest(),
                         'exit': receipt['exit'], 'input_count': receipt['input_count'],
                         'stdout_sha256': receipt['stdout_sha256'],
                         'stderr_sha256': receipt['stderr_sha256']})
for row in json.loads((BASE / 'evidence/named_tools.json').read_bytes()):
    got = pin(row['path'])
    assert got['sha256'] == row['sha256'] and got['resolved'] == row['resolved']
comparisons = []
for old, new in [('history_focused', 'history_focused_v2'),
                 ('local_pdf_candidates', 'local_pdf_candidates_v2'),
                 ('local_pdf_relevance', 'local_pdf_relevance_v2')]:
    argv = ['/usr/bin/cmp', '--', str(BASE / 'evidence' / old / 'stdout.bin'),
            str(BASE / 'evidence' / new / 'stdout.bin')]
    pin(argv[0])
    process = subprocess.run(argv, cwd=ROOT, env=ENV, capture_output=True)
    comparisons.append({'argv': argv, 'cwd': str(ROOT), 'env': ENV,
                         'exit': process.returncode,
                         'stdout': process.stdout.decode(), 'stderr': process.stderr.decode()})
    assert process.returncode == 0
for path in list(READS):
    pin(path)
assert manifest() == outer
print(json.dumps({'status': 'PASS_ROOT_SCOUT29_COMPLETE_NEGATIVE_CLOSURE',
    'seal_sha256': SEAL, 'payloads_checked_twice': len(outer),
    'actual_original_auditor_stdout': audit_stdout,
    'historical_aliases': aliases, 'complete_archived_commands': command_rows,
    'actual_root_raw_comparisons': comparisons,
    'all_current_read_paths_and_resolved_identities_checked_twice': len(READS),
    'scope': 'Complete negative-desk archive/current-pin inspection and three new documentary raw comparisons. No mathematical producer, pilot, build, PDF view, independent review, admission or hermetic-reuse claim.'},
    indent=2, sort_keys=True))
