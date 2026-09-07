"""Documentary audit and exact nonself seal; never executes candidate code."""
import ast
from datetime import datetime, timezone
from hashlib import sha256
import json
import os
from pathlib import Path
import subprocess
import sys

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
BASE = ROOT / 'docs/papers204_208_sequence/scouting/LNR_SOURCE_RECHECK'
ENV = {'PATH': '/usr/bin:/bin', 'LANG': 'C.UTF-8', 'LC_ALL': 'C.UTF-8', 'TZ': 'UTC'}
CONTROLS = {'SYMBOLIC_DYNAMICS_STATE.md', 'docs/papers204_208_sequence/PIPELINE_STATE.md'}
CURL_CASES = (
    ('01/publisher_pdf', 0, 403, 832805),
    ('02/author_journals', 28, 0, None),
    ('04/doi_openalex', 0, 200, 8234),
    ('06/dblp_exact', 28, 0, None),
)
WEB_RECORDS = (
    'routes/01/web_publisher_open.json',
    'routes/02/web_author_pages.json',
    'routes/03_05_exact_discovery.json',
    'routes/06_exact_pdf_discovery.json',
    'routes/06/web_dblp_exact_open.json',
)


def now():
    return datetime.now(timezone.utc).isoformat()


def info(path):
    path = Path(path)
    raw = path.read_bytes()
    return {'sha256': sha256(raw).hexdigest(), 'bytes': len(raw),
            'resolved': str(path.resolve()),
            'symlink': os.readlink(path) if path.is_symlink() else None}


def save(path, raw):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('xb') as stream:
        stream.write(raw)


def dump(path, value):
    save(path, (json.dumps(value, sort_keys=True, indent=2) + '\n').encode())


def read_json(path):
    return json.loads(path.read_bytes())


def tree_info():
    result = {}
    for p in sorted(BASE.rglob('*')):
        assert not p.is_symlink(), str(p)
        if p.is_file():
            assert '__pycache__' not in p.parts and p.suffix != '.pyc'
            result[str(p.relative_to(BASE))] = info(p)
    return result


def audit():
    initial = tree_info()
    copied = read_json(BASE / 'ORIGINAL_INPUTS.json')
    assert len(copied) == 21
    live = {}
    control_changes = {}
    for source, pin in copied.items():
        dest = BASE / pin['relative_copy']
        assert str(dest) == pin['physical']
        actual = info(dest)
        assert actual['sha256'] == pin['sha256'] and actual['bytes'] == pin['bytes']
        assert actual['symlink'] is None
        current = info(source)
        live[source] = current
        rel = str(Path(source).relative_to(ROOT)) if Path(source).is_relative_to(ROOT) else None
        if current['sha256'] != pin['sha256'] or current['bytes'] != pin['bytes']:
            assert rel in CONTROLS, (source, 'non-control original changed')
            control_changes[source] = {'at_assignment': pin, 'at_audit': current,
                'interpretation': 'Permitted separate root central-control update, not repinning this original.'}
    cmp_dirs = sorted((BASE / 'commands').glob('intake_cmp_*'))
    assert len(cmp_dirs) == 21
    for folder in cmp_dirs:
        receipt = read_json(folder / 'RECEIPT.json')
        assert receipt['argv'][0:2] == ['/usr/bin/cmp', '--']
        assert receipt['exit_code'] == 0 and receipt['inputs_unchanged'] is True
        assert receipt['environment'] == ENV and receipt['cwd'] == str(ROOT)
        assert not (folder / 'stdout').read_bytes() and not (folder / 'stderr').read_bytes()
        assert receipt['stdout'] == info(folder / 'stdout')
        assert receipt['stderr'] == info(folder / 'stderr')
        assert read_json(folder / 'INPUTS_BEFORE.json') == read_json(folder / 'INPUTS_AFTER.json')
    http_results = []
    assert len(list((BASE / 'routes').glob('*/*/HTTP_RESULT.json'))) == 4
    for name, code, http_code, body_bytes in CURL_CASES:
        folder = BASE / 'routes' / name
        receipt = read_json(folder / 'RECEIPT.json')
        attempt = read_json(folder / 'ATTEMPT.json')
        record = read_json(folder / 'HTTP_RESULT.json')
        parsed = read_json(folder / 'stdout')
        assert receipt['exit_code'] == code == record['actual_curl_exit']
        assert receipt['inputs_unchanged'] is True and receipt['status'] == 'COMPLETED'
        assert receipt['environment'] == ENV and receipt['cwd'] == str(ROOT)
        assert receipt['argv'] == attempt['argv']
        assert receipt['argv'][0] == '/usr/bin/curl'
        assert receipt['argv'][-1] == record['request_url']
        assert '--location' in receipt['argv'] and '--fail' not in receipt['argv']
        assert record['transport_result'] == parsed and parsed['http_code'] == http_code
        assert receipt['stdout'] == info(folder / 'stdout')
        assert receipt['stderr'] == info(folder / 'stderr')
        assert read_json(folder / 'INPUTS_BEFORE.json') == read_json(folder / 'INPUTS_AFTER.json')
        for key, pin in record['retained_responses'].items():
            assert pin == info(folder / key)
        assert record['no_authentication_or_paywall_bypass'] is True
        if body_bytes is None:
            assert not (folder / 'response.body').exists()
            assert (folder / 'response.headers').stat().st_size == 0
            assert b'Connection timeout after 15000 ms' in (folder / 'stderr').read_bytes()
        else:
            raw = (folder / 'response.body').read_bytes()
            assert len(raw) == body_bytes
            assert not raw.startswith(b'%PDF-')
            if http_code == 403:
                assert b'<html' in raw[:400].lower()
            else:
                oa = json.loads(raw)
                assert oa['doi'] == 'https://doi.org/10.1016/j.patrec.2011.02.005'
                assert oa['best_oa_location'] is None
                assert oa['open_access']['oa_url'] is None
                assert len(oa['locations']) == 1 and oa['locations'][0]['pdf_url'] is None
                assert oa['has_content']['pdf'] is False
        http_results.append({'case': name, 'curl_exit': code, 'http_code': http_code,
                             'body_bytes': body_bytes, 'receipt': str(folder.relative_to(BASE) / 'RECEIPT.json')})
    for name in WEB_RECORDS:
        data = read_json(BASE / name)
        assert data['request']
        assert isinstance(data.get('result', data.get('response_full_text')), str)
        assert data.get('result', data.get('response_full_text'))
    ledger = read_json(BASE / 'ROUTE_LEDGER.json')
    findings = read_json(BASE / 'FINDINGS.json')
    assert ledger['routes_limit'] == ledger['routes_attempted'] == 6
    assert [r['route'] for r in ledger['routes']] == ['01', '02', '03', '04', '05', '06']
    assert ledger['actual_web_tool_calls'] == 5 and ledger['actual_curl_commands'] == 4
    assert ledger['primary_body_obtained'] is False
    assert findings['primary_body_obtained'] is False
    assert findings['candidate_status'] == 'HOLD_SOURCE'
    assert findings['admission_status'] == 'NO_ADMISSION'
    assert findings['findings'][0]['id'] == 'LNR-S1' and findings['findings'][0]['state'] == 'OPEN'
    assert findings['new_scientific_executions'] == findings['source_findings_closed'] == 0
    json_count = 0
    for name in initial:
        if name.endswith('.json'):
            read_json(BASE / name)
            json_count += 1
    for name in ('record_work.py', 'finish_source_recheck.py'):
        ast.parse((BASE / name).read_text(), filename=name)
    assert initial == tree_info()
    result = {'status': 'PASS_DOCUMENTARY_INTEGRITY_NOT_SOURCE_CLEARANCE',
              'utc': now(), 'original_copies_verified': 21, 'actual_intake_cmp_receipts_verified': 21,
              'routes': 6, 'actual_curl_results': http_results, 'web_records_verified': 5,
              'json_records_parsed': json_count, 'source_body_obtained': False,
              'candidate_status': 'HOLD_SOURCE', 'admission_status': 'NO_ADMISSION',
              'scientific_executions': 0, 'source_findings_closed': 0,
              'audit_scope': 'Byte/receipt/schema/syntax integrity only; no author/scientific code executed.',
              'live_inputs_observed': live, 'live_control_changes_since_intake': control_changes,
              'full_pre_audit_inputs_before': initial, 'full_pre_audit_inputs_after': tree_info()}
    dump(BASE / 'AUDIT_RESULT.json', result)
    print(json.dumps({k: v for k, v in result.items() if not k.startswith('full_') and k != 'live_inputs_observed'},
                     sort_keys=True, indent=2))


def record():
    assert not (BASE / 'audit_run').exists()
    folder = BASE / 'audit_run'
    folder.mkdir()
    before = tree_info()
    dump(folder / 'INPUTS_BEFORE.json', before)
    argv = ['/usr/bin/python3.10', '-I', '-S', '-B', str(Path(__file__)), 'audit']
    attempt = {'argv': argv, 'cwd': str(ROOT), 'environment': ENV,
               'started_utc': now(), 'status': 'ATTEMPTED', 'exit_code': None}
    dump(folder / 'ATTEMPT.json', attempt)
    child = subprocess.run(argv, cwd=ROOT, env=ENV, capture_output=True, check=False)
    save(folder / 'stdout', child.stdout)
    save(folder / 'stderr', child.stderr)
    after = {name: info(BASE / name) for name in before}
    dump(folder / 'INPUTS_AFTER.json', after)
    receipt = {**attempt, 'status': 'COMPLETED', 'ended_utc': now(), 'exit_code': child.returncode,
               'inputs_unchanged': before == after,
               'stdout': info(folder / 'stdout'), 'stderr': info(folder / 'stderr'),
               'result': info(BASE / 'AUDIT_RESULT.json') if (BASE / 'AUDIT_RESULT.json').exists() else None}
    dump(folder / 'RECEIPT.json', receipt)
    print(child.stdout.decode(), end='')
    print(json.dumps({'actual_audit_child_exit': child.returncode,
                      'stderr_bytes': len(child.stderr), 'inputs_unchanged': before == after}))
    assert child.returncode == 0 and not child.stderr and before == after


def seal():
    receipt = read_json(BASE / 'audit_run/RECEIPT.json')
    assert receipt['exit_code'] == 0 and receipt['inputs_unchanged'] is True
    result = read_json(BASE / 'AUDIT_RESULT.json')
    assert result['status'] == 'PASS_DOCUMENTARY_INTEGRITY_NOT_SOURCE_CLEARANCE'
    files = tree_info()
    assert 'MANIFEST.sha256' not in files
    lines = ''.join(pin['sha256'] + '  ' + name + '\n' for name, pin in files.items())
    save(BASE / 'MANIFEST.sha256', lines.encode())
    after = tree_info()
    assert set(after) == set(files) | {'MANIFEST.sha256'}
    assert files == {name: after[name] for name in files}
    print(json.dumps({'status': 'SEALED_NONSELF_DOCUMENTARY_PACKAGE',
                      'nonself_entries': len(files), 'total_files': len(after),
                      'manifest': info(BASE / 'MANIFEST.sha256'),
                      'source_status': 'LNR-S1 OPEN / HOLD_SOURCE / NO_ADMISSION'}, sort_keys=True, indent=2))


if __name__ == '__main__':
    assert sys.flags.isolated and sys.flags.no_site and sys.dont_write_bytecode and not sys.flags.optimize
    assert dict(os.environ) == ENV and Path.cwd() == ROOT
    if sys.argv[1:] == ['audit']:
        audit()
    elif sys.argv[1:] == ['record']:
        record()
    elif sys.argv[1:] == ['seal']:
        seal()
    else:
        raise RuntimeError('Require audit, record or seal')
