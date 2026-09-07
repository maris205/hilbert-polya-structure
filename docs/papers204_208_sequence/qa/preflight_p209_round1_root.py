"""Read-only preflight of the fully reviewed one-time Round1 adapter."""
from pathlib import Path
import ast
import hashlib
import json
import runpy
import subprocess

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
PREP = ROOT / 'docs/papers204_208_sequence/qa/p209_round1_preparation_v2'
source = PREP / 'freeze_p209_round1.py'
assert hashlib.sha256(source.read_bytes()).hexdigest() == '19cf0898e201f25dc5724233ff1cdef59d8a0001d6239fe5d15aeb9212f63c44'
assert hashlib.sha256((PREP / 'SHA256SUMS').read_bytes()).hexdigest() == 'baf747d531a06c76dfcff7a086819df0fc4668549f70c20894b9783750a9e0f7'
ast.parse(source.read_text())
functions = runpy.run_path(str(source), run_name='root_readonly_preflight_not_main')
assert not functions['TARGET'].exists() and not functions['TARGET'].is_symlink()
complete = functions['complete_manifest']
assert len(complete(PREP)) == 9
assert len(complete(PREP.parent / 'p209_round1_preparation')) == 10
core, author, live, whole = functions['core_inputs']()
accepted, external, counts = functions['accepted_a'](core)
history, core_links, anchor_links = functions['link_mapping'](core, accepted)
assert len(core) == 1989 and len(author) == 1985 and len(whole) == 3978
assert len(core_links) == 243 and len(functions['ANCHORS']) == 11
assert sum(bool(row['copy_relative']) for row in history.values()) == 1
assert accepted['current_open_findings'] == 0
archive = json.loads((PREP / 'PREPARATION_CHECKS.json').read_text())
def walk(value):
    if isinstance(value, dict):
        if 'argv' in value and 'stdout' in value and value['argv'][:2] == ['/usr/bin/diff', '-u']:
            output = 'V1_TO_V2.diff' if 'freeze_p209_round1_v1.py' in value['argv'][-2] else 'ADAPTATION.diff'
            assert value['exit'] == 1 and value['stderr'] == ''
            assert value['stdout'].encode() == (PREP / output).read_bytes()
        for item in value.values():
            walk(item)
    elif isinstance(value, list):
        for item in value:
            walk(item)
    elif isinstance(value, str) and value.startswith('{'):
        try:
            walk(json.loads(value))
        except json.JSONDecodeError:
            pass
walk(archive)
comparisons = []
for a, b in ((PREP / 'original_snapshot/freeze_p209_round0.py', PREP.parent / 'freeze_p209_round0.py'),
             (PREP / 'original_snapshot/freeze_p209_round0.py', functions['ROUND0'] / 'FREEZE_ADAPTER.py'),
             (PREP / 'original_snapshot/freeze_p209_round1_v1.py', PREP.parent / 'p209_round1_preparation/freeze_p209_round1.py')):
    argv = ['/usr/bin/cmp', '--', str(a), str(b)]
    p = subprocess.run(argv, cwd=ROOT, env=functions['ENV'], capture_output=True)
    comparisons.append({'argv': argv, 'exit': p.returncode, 'stdout': p.stdout.decode(), 'stderr': p.stderr.decode()})
    assert p.returncode == 0
pins = dict(functions['READ_PINS'])
for name, value in pins.items():
    assert functions['digest'](Path(name)) == value
assert not functions['TARGET'].exists()
print(json.dumps({'status': 'PASS_ROOT_READONLY_P209_ROUND1_PREFLIGHT',
    'script_sha256': functions['digest'](source), 'preparation_payloads': 9,
    'preserved_v1_payloads': 10, 'core_payloads': len(core), 'author_payloads': len(author),
    'prior_whole_payloads': len(whole), 'acceptance_anchors': 11, 'planned_round1_payloads': 2003,
    'accepted_evidence_counts': counts, 'core_links': len(core_links),
    'anchor_links': len(anchor_links), 'old_external_pins': len(history),
    'actual_current_input_paths_rechecked_twice': len(pins), 'raw_comparisons': comparisons,
    'round1_absent': True, 'no_freezer_main_or_mathematical_producer_called': True}, indent=2, sort_keys=True))
