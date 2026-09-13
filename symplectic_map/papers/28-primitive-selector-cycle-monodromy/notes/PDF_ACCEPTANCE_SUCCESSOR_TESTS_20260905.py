#!/root/miniconda3/bin/python3.12
"""Directed successor-predicate regressions; never run a validator or build.

Python -I -S -B. Default cases are in-memory and read only the two validator
sources. --recorded-fixtures additionally reads five exact preserved PDF/report
files and the reviewed successor source trio. No PDF library is imported, no
PDF is changed, and no directory or report is written: results go to stdout.
"""

import argparse
import ast
import contextlib
import hashlib
import io
import json
from pathlib import Path
import re
import runpy
import sys


PROJECT = Path('/root/autodl-tmp/symplectic_map/papers/28-primitive-selector-cycle-monodromy')
NOTES = PROJECT / 'notes'
SUCCESSOR = NOTES / 'PDF_ACCEPTANCE_SUCCESSOR_20260905.py'
FROZEN = NOTES / 'PDF_ACCEPTANCE_20260905.py'
FIXTURE = PROJECT / 'build-capsule-ec-20260905/r0/work'
SOURCE = PROJECT / 'paper-successor-20260905'


def identity(data):
    return {'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()}


def ensure(condition, message='assertion failed'):
    if not condition:
        raise AssertionError(message)


def must_reject(callback):
    try:
        callback()
    except (ValueError, IndexError):
        return
    raise AssertionError('invalid fixture was accepted')


def fixture_pdf(payload=b'CMap data\n%%EOF\n', length=None, gap=b'',
                trailer_extra=b'', object_extra=None, stream_suffix=b'\nendstream',
                prefix_extra=b'', free_tail=False):
    """Construct a tiny classic-xref PDF solely in memory, at exact offsets."""
    length_token = str(len(payload)).encode() if length is None else length
    objects = [b'<< /Type /Catalog /Pages 2 0 R >>',
               b'<< /Type /Pages /Kids [3 0 R] /Count 1 >>',
               b'<< /Type /Page /Parent 2 0 R /Contents 4 0 R '
               b'/MediaBox [0 0 612 792] >>',
               b'<< /Length ' + length_token + b' >>\nstream\n' + payload + stream_suffix]
    if object_extra is not None:
        objects.append(object_extra)
    data = bytearray(b'%PDF-1.5\n%\xd0\xd4\xc5\xd8\n' + prefix_extra)
    offsets = []
    for number, obj in enumerate(objects, 1):
        offsets.append(len(data))
        data.extend(str(number).encode() + b' 0 obj\n' + obj + b'\nendobj\n')
        if number == 2:
            data.extend(gap)
    xref = len(data)
    size = len(objects) + 1 + int(free_tail)
    data.extend(b'xref\n0 ' + str(size).encode() + b'\n')
    rows = [len(data)]
    next_free = size - 1 if free_tail else 0
    data.extend(('%010d 65535 f \n' % next_free).encode())
    for offset in offsets:
        rows.append(len(data))
        data.extend(('%010d 00000 n \n' % offset).encode())
    if free_tail:
        rows.append(len(data))
        data.extend(b'0000000000 00001 f \n')
    data.extend(b'trailer\n<< /Size ' + str(size).encode() + b' /Root 1 0 R ' +
                trailer_extra + b'>>\nstartxref\n' + str(xref).encode() + b'\n%%EOF\n')
    return bytes(data), {'xref': xref, 'rows': rows, 'offsets': offsets}


def replace_offset(data, position, value):
    return data[:position] + ('%010d' % value).encode() + data[position + 10:]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--recorded-fixtures', action='store_true')
    args = parser.parse_args()
    ensure(sys.flags.isolated and sys.flags.no_site and sys.dont_write_bytecode,
           'use Python -I -S -B')
    old_data, new_data = FROZEN.read_bytes(), SUCCESSOR.read_bytes()
    ensure(identity(old_data)['sha256'] ==
           'e173a8a54d051f8d296b5d1319a44bdea0f30d3ab0be91cc16747027bf9a126c',
           'frozen validator changed')
    v = runpy.run_path(str(SUCCESSOR))
    physical, link_page, startup = (v['pdf_physical_structure'], v['internal_link_page'],
                                     v['catalog_open_action'])
    Name, Ref = v['Name'], v['Ref']
    results = []

    def case(name, callback):
        try:
            callback()
            results.append({'case': name, 'status': 'PASS'})
        except Exception as exc:
            results.append({'case': name, 'status': 'FAIL',
                            'type': type(exc).__name__, 'error': str(exc)})

    def prior_memory_contract():
        with contextlib.redirect_stdout(io.StringIO()):
            ensure(v['self_test']() == 0)
        old, new = ast.parse(old_data), ast.parse(new_data)
        old_functions = {n.name: ast.dump(n, include_attributes=False)
                         for n in old.body if isinstance(n, ast.FunctionDef)}
        new_functions = {n.name: ast.dump(n, include_attributes=False)
                         for n in new.body if isinstance(n, ast.FunctionDef)}
        for name, original in old_functions.items():
            if name not in ('parse_pdf_object', 'audit_object', 'run'):
                ensure(new_functions[name] == original, 'unexpected predicate change: ' + name)
        source = new_data.decode()
        ensure('require(22 <= boundary["content_pages"] <= 30, "content_page_gate_22_30"' in source)
        for name in ('TITLE', 'TERMINAL', 'PROVENANCE', 'UNSAFE_KEYS', 'UNSAFE_ACTIONS'):
            def assignment(tree):
                return next(ast.dump(n, include_attributes=False) for n in tree.body
                            if isinstance(n, ast.Assign) and any(
                                isinstance(t, ast.Name) and t.id == name for t in n.targets))
            ensure(assignment(old) == assignment(new), 'changed locked constant: ' + name)
        ensure('OpenAction' in v['UNSAFE_KEYS'])

    case('unchanged prior memory tests, title/terminal, 8+32 headings and 22-30 gate', prior_memory_contract)
    case('prefix parser does not consume a following EOF comment', lambda: ensure(
        v['parse_pdf_object'](b'<< /A 1 >> %%EOF\n', prefix=True)[1] == len(b'<< /A 1 >>')))

    names = {'target': {'page': 1, 'to': [72.0, 720.0], 'zoom': 0.0}}
    named = {'kind': 4, 'nameddest': 'target', 'page': 1}
    case('NAMED resolves to matching local page', lambda: ensure(link_page(named, names, 3) == 1))
    for label, item, destinations in (
        ('missing nameddest', {'kind': 4, 'page': 1}, names),
        ('undefined named destination', {**named, 'nameddest': 'missing'}, names),
        ('missing names dictionary', named, {}),
        ('invalid names record', named, {'target': None}),
        ('unresolved page', {**named, 'page': -1}, {'target': {'page': -1}}),
        ('out-of-range page', {**named, 'page': 3}, {'target': {'page': 3}}),
        ('mismatched reported and resolved page', {**named, 'page': 0}, names),
        ('bool reported page', {**named, 'page': True}, names),
        ('bool resolved page', named, {'target': {'page': True}}),
        ('float page', {**named, 'page': 1.0}, names),
        ('URI disguised as NAMED', {**named, 'uri': 'https://public.test/'}, names),
        ('file disguised as NAMED', {**named, 'file': 'other.pdf'}, names),
        ('Named action name is not nameddest', {'kind': 4, 'name': 'NextPage', 'page': 1}, names),
    ):
        case('reject ' + label, lambda item=item, destinations=destinations:
             ensure(link_page(item, destinations, 3) is None))
    for kind in (0, 2, 3, 5, 99, True):
        case('do not convert external/unsupported link kind ' + str(kind),
             lambda kind=kind: ensure(link_page({**named, 'kind': kind}, names, 3) is None))
    for page in (0, 2):
        case('direct GOTO valid boundary page ' + str(page),
             lambda page=page: ensure(link_page({'kind': 1, 'page': page}, names, 3) == page))
    for page in (-1, 3, None, True, 1.0):
        case('direct GOTO rejects invalid page ' + repr(page),
             lambda page=page: ensure(link_page({'kind': 1, 'page': page}, names, 3) is None))

    page_refs = [162, 172, 200]
    action = {'S': Name('GoTo'), 'D': [Ref((162, 0)), Name('Fit')]}

    def catalog(value):
        return {'Type': Name('Catalog'), 'OpenAction': value}

    def lookup(xref):
        if xref != 161:
            raise ValueError('unresolved object')
        return action

    case('catalog GoTo Fit through actual-style reference', lambda: ensure(
        startup(catalog(Ref((161, 0))), lookup, page_refs) == {
            'status': 'verified_local_goto', 'page': 0, 'page_xref': 162,
            'view': 'Fit', 'parameters': []}))
    case('catalog without OpenAction', lambda: ensure(
        startup({'Type': Name('Catalog')}, lookup, page_refs) == {'status': 'absent'}))
    for view, params in (('XYZ', [None, 720, 0]), ('FitH', [720]), ('FitV', [None]),
                         ('FitR', [0, 0, 612, 792]), ('FitB', []),
                         ('FitBH', [None]), ('FitBV', [72])):
        local = {'S': Name('GoTo'), 'D': [Ref((172, 0)), Name(view), *params]}
        case('catalog legal local view ' + view, lambda local=local: ensure(
            startup(catalog(local), lookup, page_refs)['page'] == 1))
    for action_name in ('JavaScript', 'Launch', 'URI', 'GoToR', 'GoToE', 'Named'):
        case('reject startup action ' + action_name, lambda action_name=action_name: must_reject(
            lambda: startup(catalog({**action, 'S': Name(action_name)}), lookup, page_refs)))
    bad_actions = {
        'GoTo plus Next chain': {**action, 'Next': Ref((161, 0))},
        'GoTo plus URI key': {**action, 'URI': b'https://public.test/'},
        'GoTo missing destination': {'S': Name('GoTo')},
        'integer local page instead of page object': {**action, 'D': [0, Name('Fit')]},
        'non-page object destination': {**action, 'D': [Ref((161, 0)), Name('Fit')]},
        'missing page object destination': {**action, 'D': [Ref((999, 0)), Name('Fit')]},
        'wrong page generation': {**action, 'D': [Ref((162, 1)), Name('Fit')]},
        'unverified named startup destination': {**action, 'D': b'Doc-Start'},
        'bad view arity': {**action, 'D': [Ref((162, 0)), Name('Fit'), 1]},
        'unknown view': {**action, 'D': [Ref((162, 0)), Name('Execute')]},
        'NaN view coordinate': {**action, 'D': [Ref((162, 0)), Name('FitH'), float('nan')]},
        'bool view coordinate': {**action, 'D': [Ref((162, 0)), Name('FitH'), True]},
        'negative zoom': {**action, 'D': [Ref((162, 0)), Name('XYZ'), 0, 0, -1]},
        'invalid fit rectangle': {**action, 'D': [Ref((162, 0)), Name('FitR'), 2, 0, 1, 5]},
        'null fit rectangle': {**action, 'D': [Ref((162, 0)), Name('FitR'), None, 0, 1, 5]},
    }
    for label, invalid in bad_actions.items():
        case('reject ' + label, lambda invalid=invalid: must_reject(
            lambda: startup(catalog(invalid), lookup, page_refs)))
    case('reject cyclic startup reference', lambda: must_reject(
        lambda: startup(catalog(Ref((161, 0))), lambda _: Ref((161, 0)), page_refs)))

    def object_exception_scope():
        findings = []
        v['audit_object'](catalog(Ref((161, 0))), [], findings, 'xref/701',
                          verified_open_action_location='xref/701')
        ensure(not findings)
        v['audit_object']({'Type': Name('Catalog'), 'OpenAction': Ref((161, 0))}, [], findings,
                          'xref/999', verified_open_action_location='xref/701')
        ensure(any(f['code'] == 'unsafe_pdf_key' for f in findings))
        findings = []
        v['audit_object'](catalog({'S': Name('JavaScript'), 'JS': b'bad'}), [], findings,
                          'xref/999')
        ensure({'unsafe_pdf_key', 'unsafe_action'} <= {f['code'] for f in findings})
        findings = []
        v['audit_object']({'S': Name('URI'), 'URI': b'file:///private'}, [], findings)
        ensure(any(f['code'] == 'unapproved_exact_uri' for f in findings))

    case('OpenAction exception stays catalog-local and danger predicates remain', object_exception_scope)

    valid, layout = fixture_pdf()
    case('classic one-revision PDF with stream EOF', lambda: ensure(
        physical(valid)[0]['opaque_stream_eof_markers'] == 1))
    payload = b'%%EOF\nstartxref\n123\nxref\n0 1\nendstream\nendobj\n%PDF-1.5\n'
    opaque, _ = fixture_pdf(payload=payload)
    case('all marker-looking stream bytes stay opaque', lambda: ensure(
        physical(opaque)[0]['streams'] == 1))
    case('valid nonzero object-zero free-list head', lambda: physical(fixture_pdf(free_tail=True)[0]))
    case('bookmark Prev is not trailer Prev', lambda: physical(fixture_pdf(
        object_extra=b'<< /Title (Bookmark) /Prev 1 0 R >>')[0]))
    for label, suffix in (('garbage', b'garbage'), ('space', b' '), ('extra newline', b'\n'),
                          ('comment', b'% comment\n'), ('extra EOF', b'%%EOF\n'),
                          ('second document', valid)):
        case('reject terminal suffix ' + label, lambda suffix=suffix: must_reject(
            lambda: physical(valid + suffix)))
    appended_table = valid + valid[layout['xref']:].replace(
        b'startxref\n' + str(layout['xref']).encode(), b'startxref\n' + str(len(valid)).encode())
    case('reject appended self-contained xref without Prev', lambda: must_reject(
        lambda: physical(appended_table)))
    for offset in (1, len(valid), layout['offsets'][3] + 1):
        bad = valid.replace(b'startxref\n' + str(layout['xref']).encode(),
                            b'startxref\n' + str(offset).encode())
        case('reject wrong startxref offset ' + str(offset), lambda bad=bad: must_reject(
            lambda: physical(bad)))
    for extra in (b'/Prev 0 ', b'/XRefStm 1 ', b'/Pr#65v 0 ', b'/XRef#53tm 1 '):
        case('reject revision/hybrid trailer ' + extra.decode(), lambda extra=extra: must_reject(
            lambda: physical(fixture_pdf(trailer_extra=extra)[0])))
    case('reject trailer Size mismatch', lambda: must_reject(
        lambda: physical(valid.replace(b'/Size 5', b'/Size 9'))))
    case('reject duplicate live offset', lambda: must_reject(lambda: physical(
        replace_offset(valid, layout['rows'][2], layout['offsets'][0]))))
    case('reject live object generation mismatch', lambda: must_reject(
        lambda: physical(valid.replace(b'4 0 obj', b'4 1 obj'))))
    case('reject live object number mismatch', lambda: must_reject(
        lambda: physical(valid.replace(b'4 0 obj', b'8 0 obj'))))
    for label, gap in (('unindexed object', b'99 0 obj\nnull\nendobj\n'),
                       ('old EOF', b'%%EOF\n'), ('second header', b'%PDF-1.5\n'),
                       ('hidden comment', b'% unindexed data\n')):
        case('reject inter-object ' + label, lambda gap=gap: must_reject(
            lambda: physical(fixture_pdf(gap=gap)[0])))
    case('reject extra header before first indexed object', lambda: must_reject(
        lambda: physical(fixture_pdf(prefix_extra=b'%PDF-1.5\n')[0])))
    for length in (b'17', b'19', b'-1', b'true', b'999999', b'5 0 R'):
        # Check token mutations and generate payload-length +/-1 below too.
        actual_length = len(b'CMap data\n%%EOF\n')
        if length.isdigit() and int(length) == actual_length:
            continue
        case('reject malformed stream Length ' + length.decode(), lambda length=length: must_reject(
            lambda: physical(fixture_pdf(length=length)[0])))
    for delta in (-1, 1):
        token = str(len(b'CMap data\n%%EOF\n') + delta).encode()
        case('reject stream Length delta ' + str(delta), lambda token=token: must_reject(
            lambda: physical(fixture_pdf(length=token)[0])))
    case('reject missing stream terminator', lambda: must_reject(
        lambda: physical(fixture_pdf(stream_suffix=b'\nendstreXm')[0])))

    recorded = None
    if args.recorded_fixtures:
        captured = {}
        for relative in ('main.pdf', 'report/objects.txt', 'report/links.json',
                         'report/destinations.json', 'report/acceptance.json'):
            raw = (FIXTURE / relative).read_bytes()
            captured[relative] = (raw, identity(raw))
        ensure(captured['main.pdf'][1]['sha256'] ==
               'a6778a8ead3004a9b14784d02e1c98c9a59d5a837231ece670da03dff0c8bf63')
        ensure(captured['report/acceptance.json'][1]['sha256'] ==
               'a59a59bb64a355f039d516562742140b21c2a9de7a8ee997e0e425dc6da94517')
        links = json.loads(captured['report/links.json'][0])
        dests = json.loads(captured['report/destinations.json'][0])
        acceptance = json.loads(captured['report/acceptance.json'][0])
        pieces = re.split(r'(?m)^XREF ([0-9]+)\n', captured['report/objects.txt'][0].decode())
        trailer = v['parse_pdf_object'](pieces[0].removeprefix('TRAILER\n').strip())
        trees = {int(pieces[i]): v['parse_pdf_object'](pieces[i + 1].strip())
                 for i in range(1, len(pieces), 2)}
        root = trailer['Root'][0]
        page_xrefs = []

        def visit(ref, seen):
            ensure(isinstance(ref, Ref) and ref not in seen)
            seen = seen | {ref}
            tree = trees[ref[0]]
            if tree.get('Type') == Name('Page'):
                page_xrefs.append(ref[0])
            else:
                ensure(tree.get('Type') == Name('Pages'))
                for child in tree['Kids']:
                    visit(child, seen)

        visit(trees[root]['Pages'], set())
        count = acceptance['total_pages']
        ensure(len(page_xrefs) == count == 22)
        case('recorded 21 CMap EOF markers plus one valid terminal trailer', lambda: ensure(
            physical(captured['main.pdf'][0]) == ({
                'profile': 'single-classic-xref/direct-stream-length', 'xref_offset': 736872,
                'xref_size': 703, 'live_objects': 662, 'streams': 62, 'raw_eof_markers': 22,
                'opaque_stream_eof_markers': 21, 'physical_terminal_verified': True}, trailer)))
        named_links = [link for link in links if link['kind'] == 4]
        case('all 163 recorded NAMED links really resolve and agree', lambda: ensure(
            len(named_links) == 163 and all(link_page(link, dests, count) == link['page']
                                           for link in named_links)))
        case('recorded catalog startup points to first actual page', lambda: ensure(
            startup(trees[root], trees.__getitem__, page_xrefs) == {
                'status': 'verified_local_goto', 'page': 0, 'page_xref': 162,
                'view': 'Fit', 'parameters': []}))
        case('recorded genuine 20-page content failure remains outside 22-30', lambda: ensure(
            acceptance['content_boundary']['content_pages'] == 20 and
            not 22 <= acceptance['content_boundary']['content_pages'] <= 30))

        def actual_object_safety():
            urls = acceptance['bibliography']['exact_uri_allowlist']
            findings = []
            for xref, tree in trees.items():
                v['audit_object'](tree, urls, findings, 'xref/' + str(xref),
                                  verified_open_action_location='xref/' + str(root))
            ensure(findings == [], 'actual object safety findings: ' + repr(findings[:3]))
            ensure(all(link['uri'] in urls for link in links if link['kind'] == 2))

        case('recorded safe catalog exception retains exact URI/object audit', actual_object_safety)

        def actual_sources():
            for name, expected in v['SOURCE_HASHES'].items():
                ensure(identity((SOURCE / name).read_bytes())['sha256'] == expected, name)
            ensure(len(v['source_headings']((SOURCE / 'main.tex').read_text())) == 40)

        case('reviewed successor source trio and forty source headings', actual_sources)
        recorded = {name: binding for name, (_, binding) in captured.items()}
    ensure('pymupdf' not in sys.modules and 'fitz' not in sys.modules)
    failures = [row for row in results if row['status'] != 'PASS']
    print(json.dumps({'schema': 'paper28-successor-predicate-regressions-v1',
                      'status': 'FAIL' if failures else 'PASS', 'cases': len(results),
                      'failures': failures, 'results': results,
                      'validator': identity(new_data), 'test_script': identity(Path(__file__).read_bytes()),
                      'frozen_validator': identity(old_data), 'recorded_fixtures': recorded,
                      'filesystem_writes': 0, 'pdf_library_imported': False,
                      'validator_run_invocations': 0, 'build_invocations': 0,
                      'acceptance_claim': 'NOT_GRANTED'}, indent=2, sort_keys=True))
    return 1 if failures else 0


if __name__ == '__main__':
    raise SystemExit(main())
