#!/usr/bin/env python3
"""Static-only checker.  Never imports or executes inspect_five.py."""
import ast
import hashlib
import json
from pathlib import Path

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
HERE = ROOT / 'docs/papers211_215_sequence/qa/five_paper_terminal_exact_preparation01'


def pin(path):
    data = path.read_bytes()
    return {'sha256': hashlib.sha256(data).hexdigest(), 'bytes': len(data)}


source = (HERE / 'inspect_five.py').read_text()
tree = ast.parse(source)
compile(tree, str(HERE / 'inspect_five.py'), 'exec')
binding = json.loads((HERE / 'INPUT_BINDINGS.json').read_bytes())
assert [row['id'] for row in binding['papers']] == ['P211', 'P212', 'P213', 'P214', 'P215']
assert sum(len(row['replay_pairs']) for row in binding['papers']) == 15
assert sum(len(row['terminal_builds']) for row in binding['papers']) == 10
assert all(set(row['freezes']) == {'Round0', 'Round1', 'Round2'} for row in binding['papers'])


def leaves(value):
    if value is None or isinstance(value, str):
        yield value
    elif isinstance(value, list):
        for item in value:
            yield from leaves(item)
    elif isinstance(value, dict):
        for item in value.values():
            yield from leaves(item)


all_leaves = list(leaves(binding['papers']))
pending = sum(value is None for value in all_leaves)
existing = sorted({value for value in all_leaves if isinstance(value, str) and '/' in value})
missing_existing = [name for name in existing if not (ROOT / name).is_file()]
assert pending > 0
assert not missing_existing, missing_existing
result = {
    'schema': 'p211-p215-exact-five-static-source-check-v1',
    'status': 'PASS_STATIC_SOURCE_PENDING_INPUTS_GATE_NOT_EXECUTED',
    'ast_parse': True,
    'compile_without_execution': True,
    'driver_imported': False,
    'driver_executed': False,
    'exact_papers': 5,
    'declared_replay_pairs': 15,
    'declared_terminal_builds': 10,
    'declared_round_manifests': 15,
    'pending_null_bindings': pending,
    'present_bound_paths': len(existing),
    'missing_nonnull_paths': missing_existing,
    'source': pin(HERE / 'inspect_five.py'),
    'binding': pin(HERE / 'INPUT_BINDINGS.json'),
    'five_paper_completion': False,
    'root_acceptance': False,
    'external': 'HOLD_EXTERNAL'
}
print(json.dumps(result, indent=2, sort_keys=True))
