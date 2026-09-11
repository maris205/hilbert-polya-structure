#!/usr/bin/env python3
"""Read-only documentary package check; does not execute mathematics."""
import hashlib
import json
import pathlib
import re

OWN = pathlib.Path(__file__).resolve().parent

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def main():
    receipts = sorted((OWN / 'commands').glob('*/receipt.json'))
    rows = 0
    child_exits = []
    recorder_hashes = {sha(OWN / p) for p in ('audit.py', 'audit_v1.py', 'audit_v2.py')}
    for path in receipts:
        r = json.loads(path.read_text())
        folder = path.parent
        assert r['argv'] and r['cwd'] == '/root/autodl-tmp/symbolic_dynamics'
        assert sha(folder / 'stdout.raw') == r['stdout_sha256']
        assert sha(folder / 'stderr.raw') == r['stderr_sha256']
        before = json.loads((folder / 'inputs_before.json').read_text())
        after = json.loads((folder / 'inputs_after.json').read_text())
        assert before == after and r['unchanged']
        assert len(before) == r['input_count']
        assert r['recorder_sha256'] in recorder_hashes
        rows += len(before)
        child_exits.append({'label': r['label'], 'exit': r['exit']})
    old = json.loads((OWN / 'SELECTED_ORIGINALS.json').read_text())
    current = json.loads((OWN / 'SELECTED_ORIGINALS_V2.json').read_text())
    protected = [p for p in old if re.match(r'papers/(208|209)-', p)]
    builds = [p for p in old if any('build' in part.casefold() for part in pathlib.PurePosixPath(p).parts[:-1])]
    assert len(old) == 1701 and len(current) == 1335
    assert len(protected) == 22
    for p in current:
        parts = pathlib.PurePosixPath(p).parts
        assert not re.match(r'papers/(208|209)-', p)
        assert not any(any(x in part.casefold() for x in ('p208','p209','paper208','paper209','ofs','fth')) for part in parts)
        assert not any(any(x in part.casefold() for x in ('review','qa','build','compile','frozen','freeze','snapshot','runtime','generated','extracted','commands','history','historical','source','search','archive','controls')) for part in parts[:-1])
        assert 'finite_systems_nineteenth' not in parts
        assert 'order_geometry_tenth' not in parts and 'order_geometry_tenth_desk' not in parts
    expected = {'SYMBOLIC_DYNAMICS_STATE.md':'62eb6631e29d5b47ae5941093707c9bb58fdb916b1fa58d969987dd881e260da',
                'PIPELINE_STATE.md':'29c6884ea88f6c2c5275d132244ad19150f745f896d3419c931fdfdd2cfb9441',
                'GIT_SYNC_RECEIPT.md':'a67457d5fe6e860040ad5f72a51b839e0220b7b83af22188008c8a74850b1865'}
    for name, h in expected.items():
        assert sha(OWN / 'controls' / name) == h
    print(json.dumps({'status':'PASS_DOCUMENTARY_CHECK_ONLY', 'completed_receipts_checked':len(receipts),
        'recorded_before_after_input_rows_checked':rows, 'original_scope_failure_protected_paths':protected,
        'original_scope_failure_build_paths':len(builds), 'corrected_selected_originals':len(current),
        'control_aliases_checked':len(expected), 'child_exits':child_exits,
        'scientific_executions':0, 'pilots':0,
        'limitations':['No rehash of protected original scientific bodies after discovery of the failure.',
                       'Recorded before/after equality is checked, not a claim all original paths remain live unchanged.',
                       'No independent source/value review or strict scientific runtime reuse key.']}, indent=2))

if __name__ == '__main__':
    main()
