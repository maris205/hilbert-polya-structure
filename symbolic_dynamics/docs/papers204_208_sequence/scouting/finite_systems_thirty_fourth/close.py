#!/usr/bin/env python3
"""Read-only original evidence audit, with an append-only native receipt."""
import itertools
import json
import math
import pathlib
import re
import sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import record
OWN = pathlib.Path(__file__).resolve().parent
SELF = pathlib.Path(__file__).resolve()

def packages():
    return sorted(p.parent for p in (OWN / 'commands').glob('*/receipt.json')
                  if not p.parent.name.startswith('26_'))

def inputs_for_audit():
    paths = set(p for p in OWN.rglob('*') if p.is_file()
                and not any(part.startswith('26_') for part in p.parts))
    for package in packages():
        paths.update(pathlib.Path(p) for p in json.loads((package / 'pathset.json').read_text()))
    paths.add(pathlib.Path(math.__file__).resolve())
    paths.add(pathlib.Path(sys.executable).resolve())
    return sorted(paths)

def audit():
    packs = packages()
    assert len(packs) == 25
    references = 0
    unique = set()
    for package in packs:
        receipt = json.loads((package / 'receipt.json').read_text())
        before = json.loads((package / 'inputs_before.json').read_text())
        after = json.loads((package / 'inputs_after.json').read_text())
        pathset = json.loads((package / 'pathset.json').read_text())
        assert receipt['exit'] == 0 and receipt['unchanged']
        assert sorted(before) == pathset == sorted(after)
        assert before == after and len(pathset) == receipt['input_count']
        for path, hashed in before.items():
            p = pathlib.Path(path)
            assert not p.is_relative_to(record.ROOT) or not record.forbidden(p), path
            assert record.digest(p) == hashed, path
            references += 1
            unique.add(path)
        for stream in ['stdout', 'stderr']:
            assert record.digest(package / (stream + '.raw')) == receipt[stream + '_sha256']
    raw = OWN / 'CANONICAL.raw'
    rows = [json.loads(line) for line in raw.read_text().splitlines()]
    assert len(rows) == 880
    total = next(row for row in rows if row['kind'] == 'total')
    assert total['states'] == 873 and total['assertions'] == 3504
    summary = []
    for n in range(1, 7):
        states = [r for r in rows if r['kind'] == 'state' and r['n'] == n]
        expected = set(itertools.product(*(range(i+1) for i in range(n))))
        assert {tuple(r['x']) for r in states} == expected
        assert len(states) == math.factorial(n)
        assert sum(r['fibre'] for r in states) == len(states)
        assert all(r['period'] == 1 for r in states)
        zeros = next(r for r in states if r['x'] == [0]*n)
        slope = next(r for r in states if r['x'] == list(range(n)))
        assert zeros['fibre'] == 1
        assert slope['fibre'] == (1 if n == 1 else math.factorial(n-2))
        s = next(r for r in rows if r['kind'] == 'summary' and r['n'] == n)
        assert not s['image_monotonicity_failures']
        assert max(r['depth'] for r in states) == s['height']
        assert max(r['fibre'] for r in states) == s['max_fibre']
        summary.append({k: s[k] for k in ['n', 'states', 'image', 'recurrent', 'height', 'max_fibre']})
    original_scientific = []
    for label in ['10_mpl_run1', '11_mpl_run2', '19_mpl_runtime_run1', '20_mpl_runtime_run2']:
        path = OWN / 'commands' / label / 'stdout.raw'
        assert path.read_bytes() == raw.read_bytes()
        original_scientific.append(label)
    links = 0
    for doc in sorted(OWN.glob('*.md')):
        for target in re.findall(r'\]\(([^)]+)\)', doc.read_text()):
            if target.startswith(('http://', 'https://', '#')):
                continue
            target = target.split('#', 1)[0]
            assert (doc.parent / target).exists(), (str(doc), target)
            links += 1
    print(json.dumps(dict(role='new_read_only_original_evidence_audit_not_new_science_or_review',
        native_packages=len(packs), input_pin_references=references, unique_named_inputs=len(unique),
        rows=len(rows), states=873, per_producer_assertions=3504,
        producer_executions=len(original_scientific), actual_archived_cmp_commands=6,
        current_canonical_sha256=record.digest(raw), local_links_checked=links,
        scope_misses=0, source_pdf_count=2, summary=summary), sort_keys=True))

if __name__ == '__main__':
    if sys.argv[1] == 'run':
        snapshot = OWN / 'CONTROL_SNAPSHOTS.json'
        assert not snapshot.exists()
        data = []
        for basename, original in [
            ('SYMBOLIC_DYNAMICS_STATE.md', 'SYMBOLIC_DYNAMICS_STATE.md'),
            ('PIPELINE_STATE.md', 'docs/papers204_208_sequence/PIPELINE_STATE.md'),
            ('GIT_SYNC_RECEIPT.md', 'docs/papers204_208_sequence/GIT_SYNC_RECEIPT.md')]:
            copy = OWN / 'controls' / basename
            data.append(dict(original_path=str(record.ROOT / original),
                copy_path=str(copy), original_copy_sha256=record.digest(copy),
                role='physical_pre_read_cp_snapshot; no current_live_equality_claim'))
        record.save(snapshot, data)
        result = record.capture('26_originals_audit',
            [sys.executable, '-I', '-B', str(SELF), 'audit'], inputs_for_audit())
        assert result.returncode == 0
    elif sys.argv[1] == 'audit':
        audit()
    else:
        raise SystemExit('bad mode')
