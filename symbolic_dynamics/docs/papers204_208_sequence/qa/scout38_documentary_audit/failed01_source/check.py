"""Original-byte documentary checking; no imported old code or scientific run.

Author /root/thirty_third_finite_scout/orientation_source_desk authored the
historical child source desk. This is self-familiarity/documentary checking,
not independent mathematical or manuscript review.
"""
import collections
import hashlib
import json
from pathlib import Path
import re
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
LANE = ROOT / 'docs/papers204_208_sequence/scouting/finite_systems_thirty_eighth'
CHILD = LANE / 'orientation_source_desk'
OUTER = '778fe4f92eb351eab1fe97a782e9ab93cb5c53f73f31024465778868eb188e45'
INNER = '88b0c0f4d85e3f2d47e011001858a6782f4c2aa34f757e7574d3d99a5ddd9984'
PKEYS = set('argv cwd started_epoch finished_epoch exit input_count unchanged stdout_sha256 stderr_sha256 role'.split())
IKEYS = set('argv cwd inputs_before executable recorder start_utc_epoch'.split())
CKEYS = IKEYS | set('exit_code end_utc_epoch stdout stderr inputs_after'.split())
PARENTS = '01_control_copy 02_control_relevant 03_filename_inventory 04_scoped_body_search 05_graph_and_allocation_originals 06_source_desk_report 07_sink_original 08_documentary_audit greedy_download greedy_headers greedy_pdfinfo greedy_selected greedy_text orientation_parent_selected'.split()
CHILDREN = 'control_pins_after_reads r1_acm_curl r2_tcs_curl r3_arxiv_curl r3_pdfinfo r3_pdftotext r3_read_1_630 r3_read_280_410 r3_read_references r3_text_locate read_failures read_failures_pinned'.split()


def digest(data):
    return hashlib.sha256(data).hexdigest()


def read(path):
    path = Path(path)
    assert path.is_file() and not path.is_symlink(), str(path)
    return path.read_bytes()


def obj(path):
    def unique(pairs):
        d = {}
        for key, value in pairs:
            assert key not in d, ('duplicate JSON key', str(path), key)
            d[key] = value
        return d
    return json.loads(read(path), object_pairs_hook=unique)


def lines(data):
    """Only LF separates records: preserve CR, FF and a missing final LF."""
    chunks = data.split(b'\n')
    return [s + b'\n' for s in chunks[:-1]] + ([chunks[-1]] if chunks[-1] else [])


def files(base):
    found = sorted(base.rglob('*'))
    assert not any(p.is_symlink() for p in found)
    return {p.relative_to(base).as_posix(): p for p in found if p.is_file()}


def roles():
    r = obj(LANE / 'CONTROL_ROLES.json')
    expected = [
        (ROOT / 'SYMBOLIC_DYNAMICS_STATE.md', 'b259bc776d3597fa7c30e1bed962d91a46fc3c62fe43b542f03e2006256c603f'),
        (ROOT / 'docs/papers204_208_sequence/PIPELINE_STATE.md', 'f381d5929f2bc36aa0eb8ce9b4c7b968d4c3bc79c2e731ceb6efce0534499d31')]
    assert r == [dict(original_path=str(p), copy_path=str(LANE / 'controls' / p.name), sha256=h,
        role='physical_copy_before_packaged_control_read_after_initial_navigation') for p, h in expected]
    return {x['original_path']: x for x in r}


def physical(original, sha):
    alias = roles().get(original)
    if alias:
        assert alias['sha256'] == sha, ('historical role mismatch', original)
        return Path(alias['copy_path'])
    return Path(original)


def all_inputs():
    paths = set(files(LANE).values()) | {HERE / 'check.py', HERE / 'capture.py', Path(sys.executable).resolve()}
    for receipt in (LANE / 'commands').glob('*/receipt.json'):
        for key in ('inputs_before.json', 'inputs_after.json'):
            for original, sha in obj(receipt.parent / key).items():
                paths.add(physical(original, sha))
    for receipt in (CHILD / 'commands').glob('*/receipt.json'):
        r = obj(receipt)
        for pin in r['inputs_before'] + r['inputs_after'] + [r[x] for x in ('executable', 'recorder', 'stdout', 'stderr')]:
            paths.add(physical(pin['path'], pin['sha256']))
    return sorted(paths)


def check(output):
    records, sed_records, commands = [], [], []
    originals = set()
    old_occurrences = 0
    def pin(original, sha, size, role, old=False):
        nonlocal old_occurrences
        p = physical(original, sha)
        data = read(p)
        assert digest(data) == sha, (role, original, 'hash')
        assert size is None or len(data) == size, (role, original, 'size')
        records.append(dict(original_path=original, physical_path=str(p), sha256=sha, bytes=len(data), role=role,
            resolution='exact_historical_control_copy' if original != str(p) else 'original_physical_path'))
        if old:
            old_occurrences += 1
            originals.add((original, sha))
        return data
    def seal(base, expected_hash, count, excluded):
        data = read(base / 'SHA256SUMS')
        assert digest(data) == expected_hash
        entries = {}
        for line in lines(data):
            assert line.endswith(b'\n')
            match = re.fullmatch(rb'([0-9a-f]{64})  ([^\n]+)\n', line)
            assert match
            sha, rel = (s.decode() for s in match.groups())
            p = Path(rel)
            assert not p.is_absolute() and '..' not in p.parts and rel not in entries
            entries[rel] = sha
            pin(str(base / rel), sha, None, 'manifest:' + str(base))
        assert len(entries) == count and list(entries) == sorted(entries)
        assert set(files(base)) == set(entries) | excluded
        return entries
    outer = seal(LANE, OUTER, 156, {'SHA256SUMS'})
    inner = seal(CHILD, INNER, 60, {'SHA256SUMS', 'SEAL_CHECK.json', 'SEAL_CHECK.stdout', 'SEAL_CHECK.stderr'})
    assert len(files(CHILD)) == 64
    assert {str((CHILD / rel).relative_to(LANE)) for rel in files(CHILD)} <= set(outer)
    seal_receipt = obj(CHILD / 'SEAL_CHECK.json')
    assert set(seal_receipt) == set('argv cwd exit_code payload_count manifest_sha256 stdout_sha256 stderr_sha256 excluded_nonself_closure scope'.split())
    assert seal_receipt['argv'] == ['sha256sum', '-c', 'SHA256SUMS'] and seal_receipt['cwd'] == str(CHILD)
    assert seal_receipt['exit_code'] == 0 and seal_receipt['payload_count'] == 60 and seal_receipt['manifest_sha256'] == INNER
    assert seal_receipt['excluded_nonself_closure'] == sorted({'SHA256SUMS', 'SEAL_CHECK.json', 'SEAL_CHECK.stdout', 'SEAL_CHECK.stderr'})
    assert read(CHILD / 'SEAL_CHECK.stdout') == ''.join(k + ': OK\n' for k in inner).encode()
    assert read(CHILD / 'SEAL_CHECK.stderr') == b''
    for stream in ('stdout', 'stderr'):
        pin(str(CHILD / ('SEAL_CHECK.' + stream)), seal_receipt[stream + '_sha256'], None, 'historical_inner_native_check')
    assert sorted(p.name for p in (LANE / 'commands').iterdir()) == PARENTS
    assert sorted(p.name for p in (CHILD / 'commands').iterdir()) == CHILDREN
    parents, children = {}, {}
    def reconstruct(r, before, stdout, label, exception=False):
        argv = r['argv']
        if argv[0] != 'sed':
            return False
        assert argv[1] == '-n' and all(re.fullmatch(r'\d+,\d+p', s) for s in argv[2].split(';'))
        ranges = [tuple(map(int, s[:-1].split(','))) for s in argv[2].split(';')]
        source_lines, used = [], []
        for arg in argv[3:]:
            path = str((Path(r['cwd']) / arg).absolute())
            if path in before:
                sha = before[path]
                role = 'explicit_command_input'
            else:
                assert exception, ('sed source lacks pin', label, path)
                rel = str(Path(path).relative_to(CHILD))
                sha = inner[rel]
                role = 'later_child_manifest_only_NOT_historical_preread_pin'
            data = pin(path, sha, None, label + ':sed_source:' + role)
            source_lines.extend(lines(data))
            used.append(dict(path=path, sha256=sha, bytes=len(data), formfeed_bytes=data.count(b'\x0c'), role=role))
        reconstructed = b''.join(line for n, line in enumerate(source_lines, 1) for lo, hi in ranges if lo <= n <= hi)
        assert reconstructed == stdout, ('sed raw bytes', label)
        sed_records.append(dict(command=label, argv=argv, ranges=ranges, inputs=used, bytes=len(stdout),
            sha256=digest(stdout), formfeed_bytes=stdout.count(b'\x0c'), raw_byte_equal=True,
            method='LF-only splitting; cumulative line numbering over files; original byte preservation; no sed rerun'))
        return True
    for label in PARENTS:
        base = LANE / 'commands' / label
        assert set(files(base)) == {'receipt.json', 'inputs_before.json', 'inputs_after.json', 'stdout.raw', 'stderr.raw'}
        r, b, a = obj(base / 'receipt.json'), obj(base / 'inputs_before.json'), obj(base / 'inputs_after.json')
        assert set(r) == PKEYS and b == a and r['unchanged'] is True and r['input_count'] == len(b)
        assert r['cwd'] == str(ROOT) and r['exit'] == 0 and r['started_epoch'] <= r['finished_epoch']
        assert r['role'] == 'native_documentary_not_scientific_execution' and str(LANE / 'record.py') in b
        for stage, pins in [('before', b), ('after', a)]:
            for original, sha in pins.items():
                pin(original, sha, None, label + ':' + stage, old=stage == 'before' and label != '08_documentary_audit')
        streams = {s: pin(str(base / (s + '.raw')), r[s + '_sha256'], None, label + ':' + s) for s in ('stdout', 'stderr')}
        assert streams['stderr'] == b''
        reread = reconstruct(r, b, streams['stdout'], label)
        parents[label] = (r, b)
        commands.append(dict(schema='parent', label=label, receipt=r, before=b, after=a, sed_byte_reconstruction=reread))
    for label in CHILDREN:
        base = CHILD / 'commands' / label
        assert set(files(base)) == {'invocation.json', 'receipt.json', 'stdout.bin', 'stderr.bin'}
        r, invocation = obj(base / 'receipt.json'), obj(base / 'invocation.json')
        assert set(r) == CKEYS and set(invocation) == IKEYS and invocation == {k: r[k] for k in IKEYS}
        assert r['cwd'] == str(CHILD) and r['inputs_before'] == r['inputs_after']
        assert r['exit_code'] == (22 if label in {'r1_acm_curl', 'r2_tcs_curl'} else 0)
        assert r['start_utc_epoch'] <= r['end_utc_epoch']
        assert r['recorder']['path'] == str(CHILD / 'record_command.py')
        b = {p['path']: p['sha256'] for p in r['inputs_before']}
        assert len(b) == len(r['inputs_before'])
        groups = [('before', r['inputs_before']), ('after', r['inputs_after'])] + [(k, [r[k]]) for k in ('executable', 'recorder', 'stdout', 'stderr')]
        for role, pins in groups:
            for p in pins:
                assert set(p) == {'path', 'sha256', 'bytes'}
                pin(p['path'], p['sha256'], p['bytes'], label + ':' + role, old=role != 'after')
        for stream in ('stdout', 'stderr'):
            assert r[stream]['path'] == str(base / (stream + '.bin'))
        reread = reconstruct(r, b, read(base / 'stdout.bin'), label, exception=label == 'read_failures')
        if reread:
            assert read(base / 'stderr.bin') == b''
        children[label] = r
        commands.append(dict(schema='child', label=label, receipt=r, invocation=invocation, sed_byte_reconstruction=reread,
            incomplete_original_input_pins=label == 'read_failures'))
    assert children['read_failures']['inputs_before'] == []
    assert len(children['read_failures_pinned']['inputs_before']) == 4
    assert children['read_failures']['argv'] == children['read_failures_pinned']['argv']
    assert read(CHILD / 'commands/read_failures/stdout.bin') == read(CHILD / 'commands/read_failures_pinned/stdout.bin')
    assert len(sed_records) == 11 and old_occurrences == 207 and len(originals) == 158
    expected_audit = set(p for p in files(LANE).values() if '08_documentary_audit' not in p.parts and p not in {LANE / 'SHA256SUMS', LANE / 'CLOSURE.md'})
    for label, (_, b) in parents.items():
        if label != '08_documentary_audit':
            expected_audit.update(physical(p, h) for p, h in b.items())
    for r in children.values():
        expected_audit.update(physical(p['path'], p['sha256']) for p in r['inputs_before'] + [r['executable'], r['recorder']])
    assert set(parents['08_documentary_audit'][1]) == {str(p) for p in expected_audit} and len(expected_audit) == 265
    old_rows = [dict(schema='parent', command=k, exit=r['exit'], pin_count=len(b), raw_sed_reexecution_byte_exact=r['argv'][0] == 'sed') for k, (r, b) in parents.items() if k != '08_documentary_audit']
    old_rows += [dict(schema='child', command=k, exit=r['exit_code'], explicit_pin_count=len(r['inputs_before']), raw_sed_reexecution_byte_exact=r['argv'][0] == 'sed', incomplete_initial_read_disclosed=k == 'read_failures') for k, r in children.items()]
    old_rows.append(dict(result='PASS_DOCUMENTARY_ONLY', parent_commands=13, child_commands=12, checked_pin_occurrences=207,
        distinct_historical_identities=158, control_copy_aliases=2, raw_sed_reexecutions_byte_exact=11, child_inner_payloads=60,
        child_all_files_to_be_parent_sealed=64, selected_historical_notes=104, historical_match_lines=55, scientific_executions=0, pilots=0))
    assert read(LANE / 'commands/08_documentary_audit/stdout.raw') == ''.join(json.dumps(r, sort_keys=True) + '\n' for r in old_rows).encode()
    discovery = obj(LANE / 'DISCOVERY_SCOPE.json')
    metadata = sorted(set(line.rstrip(b'\n').decode() for line in lines(read(LANE / 'commands/03_filename_inventory/stdout.raw'))))
    assert len(metadata) == discovery['metadata_paths'] == 901
    assert len(discovery['selected_paths']) == 104 and discovery['selected_paths'] == sorted(set(discovery['selected_paths']))
    assert set(discovery['selected_paths']) <= set(metadata)
    assert sum(discovery['denied_counts'].values()) + 104 == 901
    query = parents['04_scoped_body_search'][0]['argv']
    assert query[:5] == ['rg', '-n', '-i', 'solitaire|chip[- ]fir|load[- ]balanc|allocat|pile|redistribut|sink.{0,15}revers|source.{0,15}revers|revers.{0,15}sink|greedy', '--']
    assert query[5:] == discovery['selected_paths']
    assert set(parents['04_scoped_body_search'][1]) == set(query[5:]) | {str(LANE / p) for p in ('record.py', 'discover.py', 'DISCOVERY_SCOPE.json')}
    hits = lines(read(LANE / 'commands/04_scoped_body_search/stdout.raw'))
    assert len(hits) == 55
    hit_records = []
    for hit in hits:
        path, number, content = hit.split(b':', 2)
        path, number = path.decode(), int(number)
        assert path in discovery['selected_paths'] and content == lines(read(path))[number - 1]
        hit_records.append(dict(path=path, line=number, content_sha256=digest(content)))
    # Acquisition outputs are inspected, not fetched or converted again.
    source_checks = []
    for label, header, body, status, size, pages, url in [
        ('r1_acm_curl', CHILD / 'r1_acm.headers', CHILD / 'r1_barbosa_gafni_1989.pdf', 403, None, None, 'https://dl.acm.org/doi/pdf/10.1145/69558.69560'),
        ('r2_tcs_curl', CHILD / 'r2_tcs.headers', CHILD / 'r2_yeh_zhu_2005.pdf', 403, None, None, 'https://www.sciencedirect.com/science/article/pii/S0304397504007923/pdf'),
        ('r3_arxiv_curl', CHILD / 'r3_arxiv.headers', CHILD / 'r3_yeh_2006.pdf', 200, 236143, 23, 'https://arxiv.org/pdf/math/0604226'),
        ('greedy_download', LANE / 'sources/greedy/headers.raw', LANE / 'sources/greedy/body.raw', 200, 1007064, 25, 'https://arxiv.org/pdf/2102.00346')]:
        r = children[label] if label in children else parents[label][0]
        assert r['argv'][-1] == url
        statuses = re.findall(rb'^HTTP/[^ ]+ (\d{3})[^\r\n]*', read(header), re.M)
        assert int(statuses[-1]) == status
        if status == 403:
            assert not body.exists() and b'curl: (22)' in read(CHILD / 'commands' / label / 'stderr.bin')
        else:
            assert read(body).startswith(b'%PDF-') and len(read(body)) == size
            info = read((CHILD / 'commands/r3_pdfinfo/stdout.bin') if label == 'r3_arxiv_curl' else LANE / 'commands/greedy_pdfinfo/stdout.raw')
            assert re.search(rb'^Pages:\s+' + str(pages).encode() + rb'$', info, re.M)
            assert re.search(rb'^File size:\s+' + str(size).encode() + rb' bytes$', info, re.M)
        source_checks.append(dict(command=label, url=url, http_status=status, exit=r.get('exit_code', r.get('exit')), body_bytes=size, recorded_pdf_pages=pages, reacquired=False))
    assert read(LANE / 'commands/greedy_download/stdout.raw') == b'200\nhttps://arxiv.org/pdf/2102.00346\napplication/pdf\n1007064\n'
    for path in [LANE / p for p in ('allocation_search_input.json', 'allocation_search_output.json', 'greedy_search_input.json', 'greedy_search_output.json')] + [CHILD / p for p in ('web_discovery_04.json', 'web_arxiv_metadata.json')]:
        assert isinstance(obj(path), dict)
    control = children['control_pins_after_reads']
    assert control['argv'] == ['sha256sum'] + [p['path'] for p in control['inputs_before']]
    assert read(CHILD / 'commands/control_pins_after_reads/stdout.bin') == ''.join(p['sha256'] + '  ' + p['path'] + '\n' for p in control['inputs_before']).encode()
    summary = dict(result='PASS_DOCUMENTARY_SELF_FAMILIARITY_ONLY', outer_payloads=156, outer_physical_files=157,
        child_inner_payloads=60, child_physical_files=64, historical_inner_check_outputs=3, parent_commands=14,
        child_commands=12, historical_audit_input_paths=265, historical_audit_pin_occurrences=207,
        historical_audit_distinct_identities=158, checked_pin_occurrences=len(records), sed_raw_reconstructions=11,
        metadata_paths=901, selected_paths=104, archived_hits_verified_at_original_line=55,
        original_audits_rerun=0, source_queries_or_acquisitions_rerun=0, scientific_runs=0, independent_review=False,
        prior_child_source_authorship='/root/thirty_third_finite_scout/orientation_source_desk')
    artifacts = dict(pin_occurrences=records, commands=commands, sed_reconstructions=sed_records, source_checks=source_checks,
        discovery=dict(scope=discovery, metadata_paths=metadata, archived_hit_checks=hit_records,
            limitation='Historical filename inventory and archived match lines checked; no rerun or claim of present-day exhaustive repository search.'), summary=summary)
    for name, value in artifacts.items():
        with (output / (name + '.json')).open('x') as f:
            json.dump(value, f, indent=2, sort_keys=True)
            f.write('\n')
    print(json.dumps(summary, sort_keys=True))


if __name__ == '__main__':
    assert len(sys.argv) == 2
    destination = Path(sys.argv[1]).resolve()
    assert destination.parent == HERE and destination.is_dir()
    check(destination)
