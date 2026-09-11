#!/usr/bin/env python3
"""Independent, read-only Scout41 documentary check; no target imports/science."""
import collections
import hashlib
import json
import pathlib
import re
import shutil
import subprocess
import sys
import time

sys.dont_write_bytecode = True
OWN = pathlib.Path(__file__).resolve().parent
ROOT = OWN.parents[3]
TARGET = ROOT / 'docs/papers204_208_sequence/scouting/finite_systems_forty_first'
EXPECTED_SEAL = '3d71f6f995f6b1b6f8cdd56c5e385613743c0b6be9bb752f0c1a454e9bd5053d'
DETAIL = {'scope': 'DOCUMENTARY_ONLY; NO_PROMOTION unchanged', 'native_commands': []}


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_json(path):
    return json.loads(path.read_text())


def save(path, value):
    assert not path.exists(), str(path)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + '\n')


def native(label, argv, cwd=ROOT):
    begin = time.time()
    run = subprocess.run(argv, cwd=cwd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    streams = {}
    for name in ('stdout', 'stderr'):
        path = OWN / (label + '.' + name + '.raw')
        assert not path.exists(), str(path)
        path.write_bytes(getattr(run, name))
        streams[name] = {'path': str(path), 'bytes': path.stat().st_size, 'sha256': digest(path)}
    obj = {'label': label, 'argv': argv, 'cwd': str(cwd), 'exit': run.returncode,
           'started_epoch': begin, 'finished_epoch': time.time(), 'streams': streams}
    DETAIL['native_commands'].append(obj)
    print(json.dumps({'fresh_native': obj}, sort_keys=True), flush=True)
    assert run.returncode == 0, obj
    return OWN / (label + '.stdout.raw'), OWN / (label + '.stderr.raw')


def actual_cmp(label, left, right):
    native(label, ['cmp', '--', str(left), str(right)])


def roles():
    values = read_json(TARGET / 'CONTROL_ROLES.json')
    expected = {
        str(ROOT / 'SYMBOLIC_DYNAMICS_STATE.md'): ('SYMBOLIC_DYNAMICS_STATE.md', '736e3f648bc6dda583254dcc58f49fc764043c30ea464ec524fac04f2ec67265'),
        str(ROOT / 'docs/papers204_208_sequence/PIPELINE_STATE.md'): ('PIPELINE_STATE.md', '70de1375b0b55339408b7399178a17f91f3058b3f068faa7c395ab633e525b47'),
    }
    assert len(values) == 2 and {r['original_path'] for r in values} == set(expected)
    for r in values:
        name, pinned = expected[r['original_path']]
        assert r['copy_path'] == str(TARGET / 'controls' / name)
        assert r['sha256'] == pinned == digest(pathlib.Path(r['copy_path']))
        assert r['role'] == 'physical_copy_before_packaged_control_read_after_initial_navigation'
    return {r['original_path']: r for r in values}


def resolved(original, pinned, aliases):
    if original in aliases:
        assert pinned == aliases[original]['sha256']
        return pathlib.Path(aliases[original]['copy_path'])
    return pathlib.Path(original)


def input_paths():
    aliases = roles()
    found = {p for p in TARGET.rglob('*') if p.is_file()}
    for receipt in (TARGET / 'commands').glob('*/receipt.json'):
        for key in ('inputs_before.json', 'inputs_after.json'):
            for original, pinned in read_json(receipt.parent / key).items():
                found.add(resolved(original, pinned, aliases))
    found.update([OWN / 'check.py', OWN / 'capture.py', ROOT / 'AGENTS.md',
                  ROOT / 'SYMBOLIC_DYNAMICS_STATE.md', ROOT / 'docs/papers204_208_sequence/PIPELINE_STATE.md',
                  ROOT / '.agents/skills/symbolic-dynamics-research/SKILL.md',
                  ROOT / 'docs/research_state/WORKFLOW.md',
                  ROOT / 'docs/papers204_208_sequence/PROBLEM_ANCHOR.md',
                  ROOT / 'docs/papers204_208_sequence/ARTIFACT_CONTRACT.md'])
    for executable in ('sed', 'rg', 'cmp', 'pdfinfo', 'pdftotext', 'sha256sum', sys.executable):
        located = shutil.which(executable)
        assert located, executable
        found.add(pathlib.Path(located).resolve())
    return sorted(found)


def forbidden(path):
    if path.is_relative_to(TARGET) or not path.is_relative_to(ROOT):
        return False
    for component in path.relative_to(ROOT).parts:
        v = component.lower()
        if v in {'qa', 'review', 'reviews', 'freeze', 'freezes', 'build', 'builds', 'history', 'snapshots', 'capsules', 'capsule', 'runtime'}:
            return True
        if 'gate' in v or v.startswith(('p208', 'p209', '208-', '209-', 'ofs', 'fth', 'round0', 'round1', 'round2', 'terminal')):
            return True
        if re.search(r'(^|[^a-z0-9])(ofs|fth|p208|p209)([^a-z0-9]|$)', v):
            return True
        if any(s in v for s in ('order_geometry_tenth', 'finite_systems_tenth', 'finite_systems_nineteenth', 'finite_systems_twentieth')):
            return True
    return False


def exclude(path):
    if path.is_relative_to(TARGET):
        return 'own_lane'
    if forbidden(path):
        return 'protected_or_mixed'
    parts = path.relative_to(ROOT).parts
    if any(p.lower() in {'inputs', 'controls', 'sources', 'commands', 'public_sources', 'discovery'}
           or p.lower().startswith(('evidence_capture', 'replay', 'source_only', 'strict_', 'input_', 'history_')) for p in parts):
        return 'nested_artifact'
    if any(p.startswith(('ORR_', 'LNR_', 'NED_', 'CTM_', 'HVD_', 'NCC_', 'GCF_', 'LAST_SEAT_'))
           or p in {'finite_systems_thirty_third', 'finite_systems_thirty_fourth', 'finite_systems_thirty_sixth',
                    'finite_systems_thirty_eighth', 'finite_systems_thirty_ninth', 'finite_systems_fortieth'} for p in parts):
        return 'old_hold_prior_own_or_other_active_lane'
    if path.name not in {'SCOUT.md', 'SCOUT_REPORT.md', 'SCOUT_AND_KILL_LEDGER.md', 'KILL_LEDGER.md',
                         'INTAKE.md', 'PROOF_AND_DISPOSITION.md', 'PROOF_AND_ADAPTERS.md', 'PROOF_PACKAGE.md'}:
        return 'unselected_basename'
    bases = [ROOT / 'docs' / name / 'scouting' for name in ('papers204_208_sequence', 'papers197_201_sequence',
             'papers192_196_sequence', 'papers187_191_sequence', 'papers172_176_sequence', 'papers157_161_sequence')]
    if not any(path.is_relative_to(base) and len(path.relative_to(base).parts) <= 3 for base in bases):
        return 'outside_note_depth'
    return None


def main():
    assert digest(TARGET / 'SHA256SUMS') == EXPECTED_SEAL
    entries = {}
    for line in (TARGET / 'SHA256SUMS').read_text().splitlines():
        match = re.fullmatch(r'([0-9a-f]{64})  (.+)', line)
        assert match, line
        pinned, name = match.groups()
        rel = pathlib.PurePosixPath(name)
        assert not rel.is_absolute() and '..' not in rel.parts and name != 'SHA256SUMS' and name not in entries
        path = TARGET / name
        assert path.is_file() and not path.is_symlink() and digest(path) == pinned
        entries[name] = pinned
    physical = {str(p.relative_to(TARGET)) for p in TARGET.rglob('*') if p.is_file() and p.name != 'SHA256SUMS'}
    assert len(entries) == 196 and physical == set(entries)
    assert not any(p.is_symlink() for p in TARGET.rglob('*'))
    native('target_sha256sum_check', ['sha256sum', '-c', 'SHA256SUMS'], TARGET)
    DETAIL['target_manifest'] = {'path': str(TARGET / 'SHA256SUMS'), 'sha256': EXPECTED_SEAL,
                                 'nonself_payloads': len(entries), 'complete_entries': entries}

    aliases = roles()
    DETAIL['historical_control_aliases'] = list(aliases.values())
    receipt_paths = sorted((TARGET / 'commands').glob('*/receipt.json'))
    prior = [p for p in receipt_paths if p.parent.name != '08_documentary_audit']
    assert len(receipt_paths) == 31 and len(prior) == 30
    census, occurrences, identities, all_identities, categories = [], 0, set(), set(), collections.Counter()
    for receipt_path in receipt_paths:
        base = receipt_path.parent
        receipt = read_json(receipt_path)
        before, after = [read_json(base / name) for name in ('inputs_before.json', 'inputs_after.json')]
        assert set(p.name for p in base.iterdir()) == {'receipt.json', 'inputs_before.json', 'inputs_after.json', 'stdout.raw', 'stderr.raw'}
        assert before == after and receipt['unchanged'] is True and receipt['input_count'] == len(before)
        assert receipt['cwd'] == str(ROOT) and receipt['role'] == 'native_documentary_not_scientific_execution'
        assert receipt['started_epoch'] <= receipt['finished_epoch']
        expected_exit = 35 if base.name == 'synchronism_download' else 0
        assert receipt['exit'] == expected_exit
        pin_details = []
        for original, pinned in before.items():
            path = resolved(original, pinned, aliases)
            assert path.is_absolute() and path.is_file() and not path.is_symlink()
            assert digest(path) == pinned and not forbidden(path)
            pin_details.append({'historical_path': original, 'sha256': pinned, 'resolved_path': str(path)})
            all_identities.add((original, pinned))
            if receipt_path in prior:
                occurrences += 1
                identities.add((original, pinned))
        stream_details = {}
        for stream in ('stdout', 'stderr'):
            path = base / (stream + '.raw')
            assert digest(path) == receipt[stream + '_sha256']
            stream_details[stream] = {'path': str(path), 'bytes': path.stat().st_size, 'sha256': digest(path)}
        item = {'command': base.name, 'receipt_path': str(receipt_path), 'receipt': receipt,
                'pins': pin_details, 'streams': stream_details}
        census.append(item)
        if receipt_path in prior:
            categories[receipt['argv'][0]] += 1
        print(json.dumps({'historical_command': base.name, 'argv': receipt['argv'], 'exit': receipt['exit'],
                          'checked_pins': len(before), 'streams': stream_details}, sort_keys=True), flush=True)
    assert occurrences == 199 and len(identities) == 134
    assert categories == {'cp': 1, 'sed': 10, 'rg': 6, 'curl': 5, 'pdfinfo': 4, 'pdftotext': 4}
    DETAIL['historical_commands'] = census
    DETAIL['prior_pin_identities'] = [{'path': p, 'sha256': d} for p, d in sorted(identities)]

    outer = read_json(TARGET / 'commands/08_documentary_audit/inputs_before.json')
    expected_outer = {TARGET / name for name in entries if not name.startswith('commands/08_documentary_audit/') and name != 'CLOSURE.md'}
    for item in census:
        if item['command'] != '08_documentary_audit':
            expected_outer.update(pathlib.Path(p['resolved_path']) for p in item['pins'])
    assert len(outer) == len(expected_outer) == 303 and set(outer) == {str(p) for p in expected_outer}
    DETAIL['outer_303_path_reconstruction'] = sorted(str(p) for p in expected_outer)
    archived = [json.loads(line) for line in (TARGET / 'commands/08_documentary_audit/stdout.raw').read_text().splitlines()]
    assert len(archived) == 35
    assert [r['command'] for r in archived[:30]] == [p.parent.name for p in prior]
    for old, path in zip(archived[:30], prior):
        receipt = read_json(path)
        assert old == {'command': path.parent.name, 'exit': receipt['exit'], 'pins': receipt['input_count'],
                       'raw_sed_reexecution_byte_exact': receipt['argv'][0] == 'sed'}

    sed_count = 0
    for path in prior:
        receipt = read_json(path)
        if receipt['argv'][0] != 'sed':
            continue
        label = 'sed_' + path.parent.name
        fresh_out, fresh_err = native(label, receipt['argv'])
        actual_cmp(label + '_cmp_stdout', fresh_out, path.parent / 'stdout.raw')
        actual_cmp(label + '_cmp_stderr', fresh_err, path.parent / 'stderr.raw')
        sed_count += 1
    assert sed_count == 10

    scope = read_json(TARGET / 'DISCOVERY_SCOPE.json')
    inventory = sorted(set(pathlib.Path(line) for line in (TARGET / 'commands/03_filename_inventory/stdout.raw').read_text().splitlines()))
    selected, denied = [], collections.Counter()
    for path in inventory:
        reason = exclude(path)
        if reason:
            denied[reason] += 1
        else:
            selected.append(str(path))
    assert len(inventory) == scope['metadata_paths'] == 939
    assert selected == scope['selected_paths'] and len(selected) == 111 and dict(denied) == scope['denied_counts']
    body_receipt = read_json(TARGET / 'commands/04_scoped_body_search/receipt.json')
    assert body_receipt['argv'][body_receipt['argv'].index('--') + 1:] == selected
    body_lines = (TARGET / 'commands/04_scoped_body_search/stdout.raw').read_text().splitlines()
    assert len(body_lines) == 34
    for line in body_lines:
        path, number, text = line.split(':', 2)
        assert path in selected and pathlib.Path(path).read_text().splitlines()[int(number) - 1] == text
    DETAIL['discovery_reconstruction'] = {'inventory_paths': 939, 'selected_paths': selected, 'denied_counts': dict(denied),
                                          'matching_lines_verified_against_pinned_files': body_lines,
                                          'fresh_inventory_or_rg_body_search': False}

    pdf_records = []
    for name, pages, size in [('schuele', 21, 983421), ('synchronism_arxiv', 137, 2879210),
                              ('fuks_sequences', 15, 200359), ('powley', 31, 278199)]:
        base = TARGET / 'sources' / name
        pdf, layout = base / 'body.raw', base / 'body.txt'
        request = read_json(base / 'request.json')
        dl_receipt = read_json(TARGET / 'commands' / (name + '_download') / 'receipt.json')
        dl_stdout = (TARGET / 'commands' / (name + '_download') / 'stdout.raw').read_text().splitlines()
        headers = (base / 'headers.raw').read_bytes()
        assert pdf.read_bytes().startswith(b'%PDF-') and pdf.stat().st_size == size
        assert dl_stdout[0] == '200' and int(dl_stdout[-1]) == size and 'pdf' in dl_stdout[-2].lower()
        assert dl_receipt['argv'][-1] == request['url'] and request['max_time_seconds'] == 40
        assert b'200' in headers and b'content-type:' in headers.lower()
        info = (TARGET / 'commands' / (name + '_pdfinfo') / 'stdout.raw').read_text()
        assert int(re.search(r'^Pages:\s+(\d+)$', info, re.M).group(1)) == pages
        out, err = native('pdf_layout_' + name, ['pdftotext', '-layout', str(pdf), '-'])
        actual_cmp('pdf_layout_' + name + '_cmp_stdout', out, layout)
        actual_cmp('pdf_layout_' + name + '_cmp_stderr', err, TARGET / 'commands' / (name + '_text') / 'stderr.raw')
        assert err.read_bytes() == b''
        pdf_records.append({'name': name, 'url': request['url'], 'sha256': digest(pdf), 'bytes': size,
                            'archived_pdfinfo_pages': pages, 'layout_sha256': digest(layout),
                            'fresh_layout_cmp': True, 'fresh_pdfinfo_or_page_view': False})
    DETAIL['primary_pdfs'] = pdf_records
    for index, obj in enumerate(archived[30:34]):
        expected = pdf_records[index]
        assert obj == {'actual_primary_pdf_bytes': expected['bytes'], 'actual_primary_pdf_pages': expected['archived_pdfinfo_pages'],
                       'byte_exact_to_recorded_layout_text': True, 'exit': 0,
                       'documentary_extraction_argv': ['pdftotext', '-layout', str(TARGET / 'sources' / expected['name'] / 'body.raw'), '-']}

    failed = TARGET / 'sources/synchronism'
    failed_receipt = read_json(TARGET / 'commands/synchronism_download/receipt.json')
    assert not (failed / 'body.raw').exists()
    assert (TARGET / 'commands/synchronism_download/stderr.raw').read_bytes() == b'curl: (35) Recv failure: Connection reset by peer\n'
    assert failed_receipt['argv'][-1] == read_json(failed / 'request.json')['url']
    assert set(p.name for p in failed.iterdir()) == {'headers.raw', 'request.json'}
    DETAIL['preserved_failure'] = {'receipt': str(TARGET / 'commands/synchronism_download/receipt.json'), 'exit': 35,
                                  'body_absent': True, 'no_fresh_retry': True,
                                  'stderr_sha256': failed_receipt['stderr_sha256'],
                                  'headers_sha256': digest(failed / 'headers.raw')}
    queries = []
    for batch in range(1, 8):
        if batch < 4:
            request_path, result_path = [TARGET / f'search{batch:02d}_{part}.json' for part in ('input', 'output')]
            request, result = read_json(request_path), read_json(result_path)
            kind, count = 'search_query', 4
        else:
            request_path = result_path = TARGET / f'source_query_{batch:02d}.json'
            obj = read_json(request_path)
            request, result = obj['request'], obj['result']
            kind, count = {4: ('search_query', 2), 5: ('search_query', 2), 6: ('open', 1), 7: ('click', 1)}[batch]
        assert len(request[kind]) == count and result
        queries.append({'batch': batch, 'request_path': str(request_path), 'result_path': str(result_path),
                        'request': request, 'result_type': type(result).__name__,
                        'request_sha256': digest(request_path), 'result_sha256': digest(result_path)})
    DETAIL['archived_browser_batches'] = queries
    summary = {'result': 'PASS_DOCUMENTARY_ONLY', 'manifest_payloads': 196, 'outer_native_paths': len(outer),
               'prior_commands': 30, 'prior_pin_occurrences': occurrences, 'prior_pin_identities': len(identities),
               'all_31_pin_occurrences': sum(len(r['pins']) for r in census), 'all_31_pin_identities': len(all_identities),
               'native_command_categories': dict(categories), 'fresh_sed_executions': sed_count,
               'fresh_pdf_layout_executions': len(pdf_records), 'fresh_raw_cmp_executions': 28,
               'fresh_scientific_producers': 0, 'fresh_builds_renders_page_views': 0,
               'new_mathematical_review_or_admission': False, 'disposition': 'NO_PROMOTION / HOLD_EXTERNAL'}
    old = archived[-1]
    for key, expected in {'result': 'PASS_DOCUMENTARY_ONLY', 'prior_commands': 30, 'checked_historical_pin_occurrences': 199,
                          'distinct_historical_identities': 134, 'control_copy_aliases': 2,
                          'raw_sed_reexecutions_byte_exact': 10, 'primary_layout_reextractions_byte_exact': 4,
                          'inventory_paths': 939, 'selected_original_notes': 111, 'query_matches': 34, 'actual_web_batches': 7,
                          'successful_primary_PDF_routes': 4, 'preserved_failed_primary_routes': [{'command': 'synchronism_download', 'exit': 35}],
                          'known_exact_comparison_literals': 1, 'new_literal_rules': 0, 'scientific_executions': 0,
                          'pilots': 0, 'independent_mathematical_reviews': 0}.items():
        assert old[key] == expected, key
    DETAIL['summary'] = summary
    save(OWN / 'DETAIL.actual.json', DETAIL)
    print(json.dumps(summary, sort_keys=True), flush=True)


if __name__ == '__main__':
    try:
        main()
    except BaseException:
        save(OWN / 'DETAIL.failed.actual.json', DETAIL)
        raise
