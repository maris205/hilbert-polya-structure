#!/usr/bin/env python3
"""Read-only documentary closure; no scientific map or imported recorder."""
import hashlib
import json
import pathlib
import re

ROOT = pathlib.Path('/root/autodl-tmp/symbolic_dynamics')
OWN = pathlib.Path(__file__).resolve().parent
checks = 0

def need(value):
    global checks
    checks += 1
    assert value

def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def original(p):
    if str(OWN.relative_to(ROOT)) in p:
        return False
    if any(re.search(r'review|qa|freez|snapshot|source|runtime|history|historical|command|build|compile|copied|receipt|execution', s, re.I) for s in p.split('/')[:-1]):
        return False
    if re.fullmatch(r'papers/[0-9]+-[^/]+/(main\.tex|sections/[^/]+\.tex|PROOF_PACKAGE\.md)', p):
        return True
    if re.fullmatch(r'docs/papers[0-9]+_[0-9]+_sequence/scouting/[^/]+/[^/]+\.md', p):
        return any(s in p.rsplit('/', 1)[1] for s in ('PROOF', 'SCOUT_REPORT', 'KILL', 'CANDIDATE_LEDGER', 'INTAKE', 'DISPOSITION', 'HANDOFF', 'COLLISION', 'THEOREM', 'DOSSIER'))
    return bool(re.fullmatch(r'docs/papers[0-9]+_[0-9]+_sequence/phase1/(CANDIDATE_POOL_AND_KILL_LEDGER|THEOREM_CONTRACTS|SYSTEM_COLLISION_FIREWALL)\.md', p))

selected = json.loads((OWN / 'SELECTED_ORIGINALS.json').read_text())
need(len(selected) == 1253)
need(selected == sorted(set(selected)))
need(all(original(p) for p in selected))
searches = {'03_broad_structures', '04_graph_inclusion', '06_precise_graph_operators', '12_lonesum_history'}
receipts = sorted((OWN / 'commands').glob('*/receipt.json'))
input_rows = 0
for path in receipts:
    receipt = json.loads(path.read_text())
    directory = path.parent
    if receipt['label'].startswith('22_'):
        continue
    before = json.loads((directory / 'inputs_before.json').read_text())
    after = json.loads((directory / 'inputs_after.json').read_text())
    pathset = json.loads((directory / 'pathset.json').read_text())
    need(pathset == sorted(before))
    need(before == after)
    need(receipt['unchanged'])
    need(receipt['input_count'] == len(pathset))
    need(receipt['recorder_sha256'] == digest(OWN / 'audit.py'))
    need(receipt['stdout_sha256'] == digest(directory / 'stdout.raw'))
    need(receipt['stderr_sha256'] == digest(directory / 'stderr.raw'))
    need(receipt['exit'] == 0)
    for rel, expected in before.items():
        need(digest(ROOT / rel) == expected)
        input_rows += 1
    if receipt['label'] in searches:
        need(pathset == selected)
        need(receipt['argv'][:4] == ['rg', '-n', '-i', '--'])
        need(receipt['argv'][5:] == selected)
    print(json.dumps(dict(label=receipt['label'], input_rows=len(pathset), status='PASS'), sort_keys=True))
need((OWN / 'commands/08_oni_pilot_a/stdout.raw').read_bytes() == (OWN / 'commands/09_oni_pilot_b/stdout.raw').read_bytes())
for name in ('SYMBOLIC_DYNAMICS_STATE', 'PIPELINE_STATE', 'GIT_SYNC_RECEIPT'):
    need((OWN / 'controls' / (name + '.md')).read_bytes() ==
         (ROOT / 'docs/papers204_208_sequence/qa/central_lifecycle_p209_b_initial' / (name + '.before.md')).read_bytes())
print(json.dumps(dict(status='PASS documentary closure only', commands=sum(not p.parent.name.startswith('22_') for p in receipts),
                      recorded_input_rows=input_rows, selected_originals=len(selected), checks=checks), sort_keys=True))
