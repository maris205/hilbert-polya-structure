#!/usr/bin/env python3
"""Verify bounded documentary/source artifacts; never candidate mathematics."""
import json
import pathlib
import re
import sys

OWN = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(OWN))
import record


def read(path):
    return json.loads(path.read_text())


def audit():
    roles = read(OWN / 'ORIGINAL_ROLES.json')
    assert len(roles) == 3
    assert {r['original_path'] for r in roles} == {str(p) for p in record.ORIGINALS}
    for row in roles:
        original, copy = pathlib.Path(row['original_path']), pathlib.Path(row['copy_path'])
        assert copy == OWN / 'inputs' / original.name
        assert record.digest(original) == record.digest(copy) == row['sha256']
        assert not original.is_symlink() and not copy.is_symlink()
    labels = ['01_old_context_copy', '02_old_context_read'] + ['route_' + n for n in ('02', '03', '04', '05')]
    for label in labels:
        directory = OWN / 'commands' / label
        receipt = read(directory / 'receipt.json')
        before, after = read(directory / 'inputs_before.json'), read(directory / 'inputs_after.json')
        assert before == after and receipt['unchanged'] is True
        assert receipt['exit'] == 0 and not receipt['timed_out']
        assert receipt['input_count'] == len(before)
        assert record.digest(directory / 'stdout.raw') == receipt['stdout_sha256']
        assert record.digest(directory / 'stderr.raw') == receipt['stderr_sha256']
        for name, expected in before.items():
            path = pathlib.Path(name)
            assert path.is_relative_to(OWN) or path in record.ORIGINALS
            assert record.digest(path) == expected
    old_read = read(OWN / 'commands/02_old_context_read/receipt.json')
    old_copy = read(OWN / 'commands/01_old_context_copy/receipt.json')
    assert old_copy['started_epoch'] + old_copy['elapsed_seconds'] <= old_read['started_epoch']
    copies = [OWN / 'inputs' / p.name for p in record.ORIGINALS]
    assert all(len(p.read_bytes().splitlines()) <= 4000 for p in copies)
    assert (OWN / 'commands/02_old_context_read/stdout.raw').read_bytes() == b''.join(p.read_bytes() for p in copies)
    routes = sorted(p.name for p in (OWN / 'routes').iterdir() if p.is_dir())
    assert routes == ['01', '02', '03', '04', '05', '06']
    rows = []
    for n in routes:
        route = OWN / 'routes' / n
        if n in ('01', '06'):
            receipt = read(route / 'receipt.json')
            result = read(route / 'tool_return.json')
            assert isinstance(result, str)
            assert receipt['within45'] is True and receipt['elapsed_seconds'] <= 45
            if n == '06':
                assert '(403) Forbidden' in result
            rows.append(dict(route=n, elapsed_seconds=receipt['elapsed_seconds'], kind='serialized_web_tool_return'))
        else:
            receipt = read(OWN / 'commands' / ('route_' + n) / 'receipt.json')
            assert receipt['elapsed_seconds'] <= 45
            fields = (OWN / 'commands' / ('route_' + n) / 'stdout.raw').read_text().splitlines()
            assert len(fields) == 4
            body = route / 'response.body'
            headers = route / 'response.headers'
            assert body.is_file() and headers.is_file()
            assert body.stat().st_size == int(fields[3])
            assert not body.read_bytes().lstrip().startswith(b'%PDF-')
            rows.append(dict(route=n, elapsed_seconds=receipt['elapsed_seconds'], kind='native_http_response',
                             curl_exit=receipt['exit'], http_status=int(fields[0]), content_type=fields[2],
                             body_bytes=body.stat().st_size, body_sha256=record.digest(body), headers_sha256=record.digest(headers)))
    assert '<title>Redirecting</title>' in (OWN / 'routes/02/response.body').read_text()
    alex = read(OWN / 'routes/03/response.body')
    s2 = read(OWN / 'routes/04/response.body')
    assert alex['open_access']['oa_status'] == 'closed' and alex['primary_location']['pdf_url'] is None
    assert s2['openAccessPdf']['status'] == 'BRONZE'
    assert s2['openAccessPdf']['url'].lower() == 'https://doi.org/10.1016/0097-3165(92)90037-u'
    assert next(row['http_status'] for row in rows if row['route'] == '05') == 403
    links = 0
    for link in re.findall(r'\]\(([^)]+)\)', (OWN / 'SOURCE_REPORT.md').read_text()):
        if link.startswith('https://'):
            continue
        assert (OWN / link).is_file() or link == 'DOCUMENTARY_AUDIT.json', link
        links += 1
    outcome = dict(verdict='PASS_DOCUMENTARY_ONLY', source_disposition='HOLD_SOURCE', primary_body_obtained=False,
        primary_theorem_proof_reads=0, original_context_notes=3, original_pins_copies_unchanged=True,
        full_context_read_stdout_byte_equality=True, routes=rows, route_count=6,
        all_routes_within_45_seconds=True, native_commands_checked=6, document_links_checked=links,
        metadata_access_labels_conflict=True, metadata_not_body_completion=True,
        no_pdf_extraction_or_visual_claim=True, scientific_executions=0, theorem_changes=0, admissions=0)
    record.save(OWN / 'DOCUMENTARY_AUDIT.json', outcome)
    print(json.dumps(outcome, sort_keys=True))


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'record':
        inputs = sorted(p for p in OWN.rglob('*') if p.is_file())
        code = record.capture('03_documentary_audit', ['python3', '-I', '-B', str(pathlib.Path(__file__).resolve())], inputs)
        assert code == 0
    else:
        audit()
