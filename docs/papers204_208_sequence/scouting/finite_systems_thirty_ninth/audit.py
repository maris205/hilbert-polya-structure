#!/usr/bin/env python3
"""Documentary original-pin/schema/raw-read audit; no mathematical kernel."""
import json
import pathlib
import subprocess
import sys
sys.dont_write_bytecode = True
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import record
import discover

OWN = record.OWN
SELF = pathlib.Path(__file__).resolve()
LABEL = '09_documentary_audit'
ROLES = json.loads((OWN / 'CONTROL_ROLES.json').read_text())
ALIASES = {r['original_path']: r for r in ROLES}


def historical_path(path, digest):
    if path in ALIASES:
        role = ALIASES[path]
        assert digest == role['sha256'], ('control identity', path)
        return pathlib.Path(role['copy_path'])
    return pathlib.Path(path)


def receipts():
    return sorted(p for p in (OWN / 'commands').glob('*/receipt.json') if p.parent.name != LABEL)


def inputs():
    files = {p for p in OWN.rglob('*') if p.is_file() and LABEL not in p.parts}
    for path in receipts():
        for original, digest in json.loads((path.parent / 'inputs_before.json').read_text()).items():
            files.add(historical_path(original, digest))
    return sorted(files)


def main():
    occurrences, rereads = 0, 0
    identities = set()
    for role in ROLES:
        assert record.sha(pathlib.Path(role['copy_path'])) == role['sha256']
    for path in receipts():
        base = path.parent
        obj = json.loads(path.read_text())
        before = json.loads((base / 'inputs_before.json').read_text())
        after = json.loads((base / 'inputs_after.json').read_text())
        assert before == after and obj['unchanged'], str(path)
        assert len(before) == obj['input_count'] and obj['exit'] == 0, str(path)
        for original, digest in before.items():
            assert record.sha(historical_path(original, digest)) == digest, ('old pin', original)
            identities.add((original, digest))
            occurrences += 1
        for stream in ('stdout', 'stderr'):
            assert record.sha(base / (stream + '.raw')) == obj[stream + '_sha256'], str(path)
        fresh_read = False
        if obj['argv'][0] == 'sed':
            result = subprocess.run(obj['argv'], cwd=obj['cwd'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            assert result.returncode == obj['exit']
            assert result.stdout == (base / 'stdout.raw').read_bytes()
            assert result.stderr == (base / 'stderr.raw').read_bytes()
            rereads += 1
            fresh_read = True
        print(json.dumps(dict(command=base.name, exit=obj['exit'], pins=len(before),
            raw_sed_reexecution_byte_exact=fresh_read), sort_keys=True))

    scope = json.loads((OWN / 'DISCOVERY_SCOPE.json').read_text())
    inventory = sorted(set(pathlib.Path(s) for s in
        (OWN / 'commands/03_filename_inventory/stdout.raw').read_text().splitlines()))
    selected, denied = [], {}
    for path in inventory:
        reason = discover.exclude(path)
        if reason:
            denied[reason] = denied.get(reason, 0) + 1
        else:
            selected.append(str(path))
    assert len(inventory) == scope['metadata_paths'] == 922
    assert selected == scope['selected_paths'] and len(selected) == 111
    assert denied == scope['denied_counts']
    for label, count in [('04_scoped_body_search', 346), ('08_whirling_history', 1)]:
        obj = json.loads((OWN / 'commands' / label / 'receipt.json').read_text())
        assert obj['argv'][obj['argv'].index('--') + 1:] == selected
        assert len((OWN / 'commands' / label / 'stdout.raw').read_bytes().splitlines()) == count

    extractions = 0
    for name, pages, size in [('whirling', 21, 428547), ('poset_whirling', 26, 578124)]:
        base = OWN / 'sources' / name
        pdf = base / 'body.raw'
        assert pdf.read_bytes().startswith(b'%PDF-') and pdf.stat().st_size == size
        download = (OWN / 'commands' / (name + '_download') / 'stdout.raw').read_text().splitlines()
        assert download[0] == '200' and int(download[-1]) == size
        info = (OWN / 'commands' / (name + '_pdfinfo') / 'stdout.raw').read_text().splitlines()
        assert int(next(line.split(':', 1)[1] for line in info if line.startswith('Pages:'))) == pages
        argv = ['pdftotext', '-layout', str(pdf), '-']
        result = subprocess.run(argv, cwd=record.ROOT, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        assert result.returncode == 0 and result.stderr == b''
        assert result.stdout == (base / 'body.txt').read_bytes()
        extractions += 1
        print(json.dumps(dict(documentary_extraction_argv=argv, exit=result.returncode,
            byte_exact_to_recorded_layout_text=True, actual_primary_pdf_pages=pages,
            actual_primary_pdf_bytes=size), sort_keys=True))

    print(json.dumps(dict(result='PASS_DOCUMENTARY_ONLY', prior_commands=len(receipts()),
        checked_historical_pin_occurrences=occurrences, distinct_historical_identities=len(identities),
        control_copy_aliases=len(ROLES), raw_sed_reexecutions_byte_exact=rereads,
        primary_layout_reextractions_byte_exact=extractions, inventory_paths=922,
        selected_original_notes=111, first_query_matches=346, second_query_matches=1,
        new_valid_autonomous_maps=0, failed_scheduler_proposals=1, scientific_executions=0,
        pilots=0, independent_mathematical_reviews=0), sort_keys=True))


if __name__ == '__main__':
    if sys.argv[1:] == ['check']:
        main()
    elif sys.argv[1:] == ['capture']:
        result = record.capture(LABEL, [sys.executable, '-B', str(SELF), 'check'], inputs())
        print(result.stdout.decode(), end='')
        print(result.stderr.decode(), end='', file=sys.stderr)
        raise SystemExit(result.returncode)
    else:
        raise SystemExit('use capture or check')
