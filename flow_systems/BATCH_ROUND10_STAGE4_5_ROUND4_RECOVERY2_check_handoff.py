#!/usr/bin/env python3
"""Read-only Round-4 handoff cross-field checker; this is NOT an official validator.

Usage: python -B BATCH_ROUND10_STAGE4_5_ROUND4_RECOVERY2_check_handoff.py MANIFEST.json

The manifest has papers[] objects containing paper_id; report, compliance,
registry, coverage, evidence_rows, source_map, draft, bundle and e6 path strings;
and correction_items[] with correction_id and severity (other fields allowed).
An independent subset of papers is allowed. Manifest-relative paths are resolved
against the manifest directory. A report's notes/... pointers are paper-relative;
its other relative pointers are repository-relative.

This particular manifest contract explicitly selects the ordered Cartesian
product of each selected registry claim's ref_slugs and writer_anchors. Empty
lists expand to [None] and [""]. Registry anchor strings are already writer text:
they are NOT decoded, normalized, substituted with source-provenance locators,
sorted or deduplicated. A saved EVR anchor is decoded exactly once from its own
value_encoded and compared to that literal writer string. This is not a claim
that a generic registry alone defines every possible source/anchor relationship.

The only formal JSON Schema validation performed here is the requested installed
claim-strength-drift-findings/1.0 schema, using Draft202012Validator and local
references only. No official bundle, coverage, evidence-row or compliance tool
is imported or run. Previously saved coverage is compared, NOT replay-validated.
The source map is checked only for literal byte/hash/span consistency, not support.

No files are created or modified, no subprocess is started, no network is used,
and no author disposition or research/stage authorization is inferred. One JSON
object is printed to stdout. Exit 0 means this bounded cross-field check passed;
exit 1 means the first failure/exception stopped it. Neither means a paper PASS,
semantic completeness, scientific correctness, authorship authentication, or
permission to advance. Input selection/authorization and separate official
execution receipts remain the caller's responsibility.
"""

import sys

sys.dont_write_bytecode = True

import hashlib
import json
import math
import re
import stat
from collections import Counter
from datetime import datetime
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parent
ARS = Path('/root/autodl-tmp/.codex/plugins/cache/ars-codex/ars-codex/0.1.28/skills/academic-research-suite/ars')
E6_SCHEMA = ARS / 'shared/contracts/revision/claim_strength_drift_findings.schema.json'
PATH_FIELDS = ('report', 'compliance', 'registry', 'coverage', 'evidence_rows',
               'source_map', 'draft', 'bundle', 'e6')
SEVERITIES = ('SERIOUS', 'MEDIUM', 'MINOR')
PHASE_FIELDS = {
    'A_references': ('checked', 'passed', 'failed', 'issues'),
    'B_citation_context': ('sampled', 'verified', 'issues'),
    'C_data': ('claims_checked', 'verified', 'issues'),
    'D_originality': ('checked', 'issues'),
    'E_claims': ('checked', 'verified', 'distortions', 'claim_registry_coverage',
                 'evidence_rows', 'claim_strength_drift_findings'),
}
ISSUE_FIELDS = {
    'A_references': ('ref_id', 'issue_type', 'severity', 'detail'),
    'B_citation_context': ('ref_id', 'section', 'issue'),
    'C_data': ('claim', 'expected', 'actual', 'severity'),
    'D_originality': ('type', 'severity', 'detail'),
    'E_claims': ('claim', 'source', 'verdict', 'detail'),
}
PRINCIPLES = ('human_oversight', 'transparency', 'reproducibility', 'fit_for_purpose')
CLAIM_VERDICTS = {'VERIFIED', 'MINOR_DISTORTION', 'MAJOR_DISTORTION',
                  'UNVERIFIABLE', 'UNVERIFIABLE_ACCESS'}
TIERS = {'ALL', 'HIGH-IMPACT', 'RANDOM', 'TOP-UP', 'NOT-SELECTED'}
SHA_RE = re.compile(r'^[0-9a-f]{64}$')


class CheckFailure(Exception):
    def __init__(self, code, location, message, **details):
        super().__init__(message)
        self.result = dict(code=code, location=location, message=message, **details)


def integer(value):
    return isinstance(value, int) and not isinstance(value, bool) and value >= 0


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError('Duplicate JSON object key: ' + key)
        result[key] = value
    return result


def reject_constant(value):
    raise ValueError('Non-finite JSON number: ' + value)


def iso_datetime(value):
    if not isinstance(value, str):
        return False
    try:
        return datetime.fromisoformat(value.replace('Z', '+00:00')).tzinfo is not None
    except ValueError:
        return False


def strings_in(value, path=''):
    if isinstance(value, dict):
        for key, child in value.items():
            yield from strings_in(child, path + '/' + key)
    elif isinstance(value, list):
        for index, child in enumerate(value):
            yield from strings_in(child, path + '/' + str(index))
    elif isinstance(value, str):
        yield path, value


def leaves(value, path=''):
    if isinstance(value, dict):
        for key, child in value.items():
            if not isinstance(child, (dict, list)):
                yield path + '/' + key, key, child
            else:
                yield from leaves(child, path + '/' + key)
    elif isinstance(value, list):
        for index, child in enumerate(value):
            yield from leaves(child, path + '/' + str(index))


class Audit:
    def __init__(self):
        self.cache = {}
        self.current = None
        self.results = []
        self.checks = 0
        self.sections = []

    def require(self, ok, code, location, message, **details):
        if not ok:
            raise CheckFailure(code, location, message, **details)
        self.checks += 1

    def obj(self, value, location, keys=()):
        self.require(isinstance(value, dict), 'OBJECT_REQUIRED', location, 'Expected an object')
        missing = [key for key in keys if key not in value]
        self.require(not missing, 'MISSING_FIELDS', location, 'Required fields are missing', missing=missing)
        return value

    def array(self, value, location):
        self.require(isinstance(value, list), 'ARRAY_REQUIRED', location, 'Expected an array')
        return value

    def text(self, value, location, nonempty=True):
        self.require(isinstance(value, str) and (not nonempty or bool(value.strip())),
                     'STRING_REQUIRED', location, 'Expected a string' + (' with content' if nonempty else ''))
        return value

    def count(self, value, location):
        self.require(integer(value), 'COUNT_INVALID', location, 'Expected a nonnegative integer, not bool')

    def path(self, value, base):
        self.text(value, 'path')
        p = Path(value)
        self.require('://' not in value, 'LOCAL_PATH_REQUIRED', value, 'URLs are not input paths')
        return (p if p.is_absolute() else base / p).absolute()

    def raw(self, path):
        key = str(path)
        if key not in self.cache:
            info = path.lstat()
            self.require(stat.S_ISREG(info.st_mode) and not path.is_symlink(),
                         'REGULAR_FILE_REQUIRED', key, 'Input must be a regular non-symlink file')
            self.require(info.st_size <= 128 * 1024 * 1024, 'INPUT_TOO_LARGE', key,
                         'This bounded checker accepts files of at most 128 MiB')
            self.cache[key] = path.read_bytes()
        return self.cache[key]

    def read(self, path):
        return json.loads(self.raw(path).decode('utf-8'), object_pairs_hook=unique_object,
                          parse_constant=reject_constant)

    def descriptor(self, path):
        raw = self.raw(path)
        return dict(path=str(path), bytes=len(raw), sha256=digest(raw))

    def pointer(self, value, expected, paper_root, location):
        if isinstance(value, dict):
            self.obj(value, location, ('path',))
            if 'sha256' in value:
                self.require(value['sha256'] == digest(self.raw(expected)), 'POINTER_HASH_MISMATCH',
                             location, 'Declared pointer digest does not match the supplied file')
            if 'bytes' in value:
                self.require(value['bytes'] == len(self.raw(expected)), 'POINTER_SIZE_MISMATCH',
                             location, 'Declared byte count does not match the supplied file')
            value = value['path']
        self.text(value, location)
        base = paper_root if value.startswith('notes/') else ROOT
        actual = self.path(value, base)
        self.require(actual.resolve() == expected.resolve(), 'POINTER_PATH_MISMATCH', location,
                     'Report pointer names a different artifact', expected=str(expected), actual=str(actual))

    def section(self, name):
        self.sections.append(name)


def check_report_shape(a, report):
    a.obj(report, '/report', ('verdict', 'mode', 'phases', 'overall_issues',
                            'citation_integrity_score', 'fabrication_risk_score', 'timestamp'))
    a.require(report['verdict'] in {'PASS', 'PASS_WITH_CONDITIONS', 'FAIL'}, 'VERDICT_INVALID',
              '/report/verdict', 'Unknown Schema-5 verdict')
    a.require(report['mode'] == 'final-check', 'MODE_INVALID', '/report/mode',
              'This Round-4 checker expects final-check')
    a.require(iso_datetime(report['timestamp']), 'TIMESTAMP_INVALID', '/report/timestamp',
              'Expected a timezone-qualified ISO-8601 timestamp')
    for key in ('citation_integrity_score', 'fabrication_risk_score'):
        value = report[key]
        a.require(isinstance(value, (int, float)) and not isinstance(value, bool)
                  and math.isfinite(value) and 0 <= value <= 1,
                  'SCORE_INVALID', '/report/' + key, 'Expected a finite score in [0,1]')
    a.obj(report['overall_issues'], '/report/overall_issues', SEVERITIES)
    for severity in SEVERITIES:
        a.count(report['overall_issues'][severity], '/report/overall_issues/' + severity)
    phases = a.obj(report['phases'], '/report/phases', PHASE_FIELDS)
    for name, keys in PHASE_FIELDS.items():
        phase = a.obj(phases[name], '/report/phases/' + name, keys)
        issue_key = 'distortions' if name == 'E_claims' else 'issues'
        for i, issue in enumerate(a.array(phase[issue_key], name + '/' + issue_key)):
            location = name + '/' + issue_key + '/' + str(i)
            a.obj(issue, location, ISSUE_FIELDS[name])
            for key in ISSUE_FIELDS[name]:
                a.text(issue[key], location + '/' + key, nonempty=False)
            if 'severity' in ISSUE_FIELDS[name]:
                a.require(issue['severity'] in SEVERITIES, 'ISSUE_SEVERITY_INVALID', location,
                          'Unknown ordinary issue severity')
    x, b, c, d, e = (phases[key] for key in PHASE_FIELDS)
    for phase, keys in ((x, ('checked', 'passed', 'failed')), (b, ('sampled', 'verified')),
                        (c, ('claims_checked', 'verified')), (e, ('checked', 'verified'))):
        for key in keys:
            a.count(phase[key], 'phase/' + key)
    a.require(x['checked'] == x['passed'] + x['failed'], 'A_COUNT_MISMATCH', 'A_references',
              'checked must equal passed + failed')
    a.require(b['verified'] <= b['sampled'], 'B_COUNT_MISMATCH', 'B_citation_context',
              'verified exceeds sampled')
    a.require(c['verified'] <= c['claims_checked'], 'C_COUNT_MISMATCH', 'C_data',
              'verified exceeds claims_checked; group semantics are not inferred')
    a.require(isinstance(d['checked'], bool), 'D_CHECKED_INVALID', 'D_originality/checked',
              'checked must be boolean')
    a.require(e['verified'] <= e['checked'], 'E_COUNT_MISMATCH', 'E_claims', 'verified exceeds checked')
    a.array(e['evidence_rows'], 'E_claims/evidence_rows')
    a.section('Schema5_documented_required_fields_and_basic_phase_shape')
    return e


def check_registry_and_rows(a, registry, draft, rows, embedded, source_map):
    a.obj(registry, '/registry', ('schema_version', 'draft_raw_sha256', 'claims'))
    a.require(registry['schema_version'] == 'claim-registry/1.0', 'REGISTRY_VERSION', '/registry',
              'Expected claim-registry/1.0')
    a.require(registry['draft_raw_sha256'] == digest(draft), 'REGISTRY_DRAFT_HASH', '/registry',
              'Registry is not bound to the exact supplied draft bytes')
    a.array(rows, '/evidence_rows')
    a.require(embedded == rows, 'SAVED_ROWS_DIFFER', '/report/phases/E_claims/evidence_rows',
              'Full embedded array differs from the saved official array; no truncation/reordering allowed')
    a.obj(source_map, '/source_map')
    for slug, text in source_map.items():
        a.text(slug, '/source_map/key')
        a.text(text, '/source_map/' + slug, nonempty=False)
    expected, selected, ids, spans = [], {}, set(), set()
    for i, claim in enumerate(a.array(registry['claims'], '/registry/claims')):
        p = '/registry/claims/' + str(i)
        a.obj(claim, p, ('claim_id', 'claim_text', 'draft_span', 'claim_kinds', 'ref_slugs',
                         'writer_anchors', 'paper_section', 'selection_tier'))
        cid = a.text(claim['claim_id'], p + '/claim_id')
        a.require(cid not in ids, 'DUPLICATE_CLAIM_ID', p, 'Duplicate registered claim ID', claim_id=cid)
        ids.add(cid)
        a.text(claim['claim_text'], p + '/claim_text')
        span = a.obj(claim['draft_span'], p + '/draft_span', ('start_byte', 'end_byte'))
        lo, hi = span['start_byte'], span['end_byte']
        a.require(integer(lo) and integer(hi) and lo < hi <= len(draft), 'REGISTRY_SPAN_INVALID', p,
                  'Span must be a nonempty in-bounds raw-byte interval')
        a.require((lo, hi) not in spans, 'DUPLICATE_CLAIM_SPAN', p, 'Duplicate registered span')
        spans.add((lo, hi))
        try:
            actual = draft[lo:hi].decode('utf-8', errors='strict')
        except UnicodeDecodeError as exc:
            raise CheckFailure('REGISTRY_UTF8_BOUNDARY', p, str(exc)) from exc
        a.require(actual == claim['claim_text'], 'REGISTRY_SPAN_TEXT_MISMATCH', p,
                  'Exact raw UTF-8 slice does not equal claim_text', claim_id=cid, span=[lo, hi])
        for key in ('ref_slugs', 'writer_anchors'):
            values = a.array(claim[key], p + '/' + key)
            for value in values:
                a.text(value, p + '/' + key)
            a.require(len(values) == len(set(values)), 'REGISTRY_DUPLICATE_MEMBER', p + '/' + key,
                      'Ordered arrays must not contain duplicate members')
        a.require(claim['selection_tier'] in TIERS, 'REGISTRY_SELECTION_INVALID', p,
                  'Unknown selection tier')
        if claim['selection_tier'] == 'NOT-SELECTED':
            continue
        selected[cid] = claim
        for slug in claim['ref_slugs'] or [None]:
            for anchor in claim['writer_anchors'] or ['']:
                expected.append((cid, slug, anchor))
    a.section('Registry_raw_draft_binding_unique_exact_UTF8_spans')
    actual_tuples, unique_rows, claims, bound_slugs = [], set(), {}, set()
    for i, row in enumerate(rows):
        p = '/evidence_rows/' + str(i)
        a.obj(row, p, ('schema_version', 'surface', 'row_id', 'claim', 'source', 'anchor',
                       'verdict', 'excerpt'))
        a.require(row['schema_version'] == 'evidence-row/1.0' and row['surface'] == 'phase_e_claim_verification',
                  'EVR_SURFACE_VERSION', p, 'Unexpected evidence-row surface/version')
        rid = a.text(row['row_id'], p + '/row_id')
        a.require(rid not in unique_rows, 'DUPLICATE_ROW_ID', p, 'Duplicate evidence row ID')
        unique_rows.add(rid)
        claim = a.obj(row['claim'], p + '/claim', ('claim_id', 'text', 'paper_locator', 'selection_tier'))
        cid = claim['claim_id']
        a.require(isinstance(cid, str) and cid in selected, 'UNSELECTED_EVIDENCE_CLAIM', p,
                  'Evidence row does not name a selected registered claim')
        a.require(claim['text'] == selected[cid]['claim_text']
                  and claim['selection_tier'] == selected[cid]['selection_tier'],
                  'ROW_CLAIM_REGISTRY_MISMATCH', p, 'Claim text/tier must equal registry without normalization')
        a.text(claim['paper_locator'], p + '/claim/paper_locator')
        a.require(row['verdict'] in CLAIM_VERDICTS, 'CLAIM_VERDICT_INVALID', p, 'Unknown claim verdict')
        if cid in claims:
            a.require(claims[cid]['claim'] == claim and claims[cid]['verdict'] == row['verdict'],
                      'CLAIM_ROWS_DISAGREE', p, 'Repeated rows disagree on the full claim object or verdict')
        claims[cid] = dict(claim=claim, verdict=row['verdict'])
        source = a.obj(row['source'], p + '/source', ('ref_slug', 'source_content_sha256', 'source_content_utf8_bytes'))
        slug = source['ref_slug']
        a.require(slug is None or isinstance(slug, str), 'ROW_REF_TYPE', p, 'Source slug must be string or null')
        anchor = a.obj(row['anchor'], p + '/anchor', ('kind', 'value_encoded', 'value_decoded'))
        encoded = a.text(anchor['value_encoded'], p + '/anchor/value_encoded', nonempty=False)
        decoded = a.text(anchor['value_decoded'], p + '/anchor/value_decoded', nonempty=False)
        a.require(not re.search(r'%(?![0-9A-Fa-f]{2})', encoded), 'MALFORMED_PERCENT_ESCAPE', p,
                  'Encoded anchor contains an invalid percent escape')
        once = unquote(encoded, encoding='utf-8', errors='strict')
        a.require(once == decoded, 'ANCHOR_ONCE_DECODE_MISMATCH', p,
                  'Decoded anchor is not exactly one strict decode; + is never space')
        a.require(anchor['kind'] in {'none', 'quote', 'page', 'section', 'paragraph'}, 'ANCHOR_KIND_INVALID', p,
                  'Unknown anchor kind')
        a.require((anchor['kind'] == 'none' and encoded == decoded == '')
                  or (anchor['kind'] != 'none' and bool(decoded.strip())), 'ANCHOR_EMPTY_STATE', p,
                  'Empty selection requires explicit none; non-none requires content')
        actual_tuples.append((cid, slug, decoded))
        excerpt = a.obj(row['excerpt'], p + '/excerpt', ('state', 'text', 'excerpt_sha256', 'source_span_utf8'))
        content_sha = source['source_content_sha256']
        if content_sha is not None:
            a.require(slug in source_map and isinstance(content_sha, str), 'SOURCE_MAP_MISSING', p,
                      'A source-bound row needs its explicitly supplied session source')
            data = source_map[slug].encode('utf-8')
            bound_slugs.add(slug)
            a.require(content_sha == digest(data) and source['source_content_utf8_bytes'] == len(data),
                      'SOURCE_MAP_BYTES_MISMATCH', p, 'Source-map bytes do not match the saved row binding')
            if excerpt['text'] is not None:
                a.text(excerpt['text'], p + '/excerpt/text')
                ex = excerpt['text'].encode('utf-8')
                span = a.obj(excerpt['source_span_utf8'], p + '/excerpt/source_span_utf8', ('start', 'end'))
                lo, hi = span['start'], span['end']
                a.require(integer(lo) and integer(hi) and lo < hi <= len(data), 'EXCERPT_SPAN_INVALID', p,
                          'Excerpt byte interval is invalid')
                a.require(data[lo:hi] == ex and excerpt['excerpt_sha256'] == digest(ex),
                          'EXCERPT_BYTES_MISMATCH', p, 'Retained excerpt differs from the declared source-map slice/hash')
        else:
            a.require(source['source_content_utf8_bytes'] is None and excerpt['text'] is None,
                      'UNBOUND_SOURCE_HAS_TEXT', p, 'A row without source-content binding must not carry source bytes')
    a.require(len(expected) == len(actual_tuples), 'SELECTED_TUPLE_COUNT_MISMATCH', '/evidence_rows',
              'Ordered selected Cartesian tuple count differs', expected=len(expected), actual=len(actual_tuples))
    for i, (wanted, actual) in enumerate(zip(expected, actual_tuples)):
        a.require(wanted == actual, 'ORDERED_SELECTED_TUPLE_MISMATCH', '/evidence_rows/' + str(i),
                  'Literal writer-anchor tuple differs; no source-locator substitution or fuzzy match is permitted',
                  expected=list(wanted), actual=list(actual))
    a.require(len(set(actual_tuples)) == len(actual_tuples), 'DUPLICATE_SELECTED_TUPLE', '/evidence_rows',
              'Duplicate claim/source/decoded-anchor tuple')
    a.require(set(claims) == set(selected), 'SELECTED_CLAIM_SET_MISMATCH', '/evidence_rows',
              'Selected registry claims are not exactly represented')
    a.section('Saved_official_rows_exact_array_and_ordered_selected_tuples')
    a.section('Source_map_literal_hash_and_excerpt_byte_consistency_not_support')
    return claims, dict(registry_claims=len(registry['claims']), selected_claims=len(selected),
                        evidence_rows=len(rows), expected_tuples=len(expected),
                        source_map_entries=len(source_map), source_bound_slugs=len(bound_slugs))


def check_coverage(a, e, coverage, paths, registry, paper_root):
    p = '/report/phases/E_claims/claim_registry_coverage'
    summary = a.obj(e['claim_registry_coverage'], p, ('status', 'registry_schema_version', 'report_path',
        'report_sha256', 'draft_raw_sha256', 'registry_raw_sha256', 'candidate_unregistered_count',
        'semantic_extraction_coverage'))
    a.require(summary['status'] == 'completed', 'COVERAGE_UNRESOLVED', p,
              'Current final handoff requires a completed saved coverage record')
    a.pointer(summary['report_path'], paths['coverage'], paper_root, p + '/report_path')
    a.require(summary['report_sha256'] == digest(a.raw(paths['coverage'])), 'COVERAGE_HASH_MISMATCH', p,
              'Coverage pointer digest differs from supplied saved coverage bytes')
    a.obj(coverage, '/coverage', ('schema_version', 'registry_schema_version', 'draft_raw_sha256',
          'registry_raw_sha256', 'registry_claim_count', 'candidate_unregistered_count',
          'semantic_extraction_coverage', 'candidates'))
    a.require(coverage['schema_version'] == 'claim-registry-coverage/1.0', 'COVERAGE_VERSION', '/coverage',
              'Unexpected saved coverage version')
    expected = {'registry_schema_version': 'claim-registry/1.0',
                'draft_raw_sha256': digest(a.raw(paths['draft'])),
                'registry_raw_sha256': digest(a.raw(paths['registry'])),
                'semantic_extraction_coverage': 'not_machine_detectable'}
    for key, value in expected.items():
        a.require(summary[key] == coverage[key] == value, 'COVERAGE_BINDING_MISMATCH', p + '/' + key,
                  'Report, saved coverage and exact current input disagree')
    a.count(coverage['candidate_unregistered_count'], '/coverage/candidate_unregistered_count')
    a.count(summary['candidate_unregistered_count'], p + '/candidate_unregistered_count')
    a.require(summary['candidate_unregistered_count'] == coverage['candidate_unregistered_count'],
              'COVERAGE_CANDIDATE_COUNT_MISMATCH', p, 'Report and saved non-clean candidate counts disagree')
    # A nonzero lexical candidate count is not automatically a missing semantic
    # claim. E1.1 returns every candidate to semantic inspection; that separate
    # review is not inferred here and the official count must never be padded
    # or rewritten to zero. P32's four inspected candidates remain visible.
    a.require(coverage['registry_claim_count'] == len(registry['claims']), 'COVERAGE_REGISTRY_COUNT', '/coverage',
              'Saved coverage registry count differs from the actual registry')
    a.array(coverage['candidates'], '/coverage/candidates')
    a.section('Saved_coverage_pointer_current_hashes_and_summary_only_no_official_replay')


def mode_rows(a, report, paper_root):
    rows = report.get('seven_failure_modes')
    if rows is None:
        pointer = report.get('audit_metadata', {}).get('failure_mode_report')
        a.text(pointer, '/report/audit_metadata/failure_mode_report')
        path = a.path(pointer, paper_root if pointer.startswith('notes/') else ROOT)
        separate = a.read(path)
        a.obj(separate, '/failure_mode_report', ('rows',))
        rows = separate['rows']
    a.array(rows, '/seven_failure_modes')
    a.require(len(rows) == 7, 'MODE_COUNT', '/seven_failure_modes', 'Exactly seven mode records are required')
    numbers, blocking, warning = set(), [], []
    for i, row in enumerate(rows):
        p = '/seven_failure_modes/' + str(i)
        a.obj(row, p, ('mode', 'status'))
        n = row['mode']
        a.require(integer(n) and 1 <= n <= 7 and n not in numbers, 'MODE_ID', p, 'Mode IDs must uniquely cover 1..7')
        numbers.add(n)
        status = row['status']
        a.require(status in {'CLEAR', 'SUSPECTED', 'INSUFFICIENT EVIDENCE'}, 'MODE_STATUS', p,
                  'Unknown mode status; this manifest carries no authenticated override input')
        block = status == 'SUSPECTED' or (status == 'INSUFFICIENT EVIDENCE' and n in {1, 3, 5, 6})
        if block:
            blocking.append(n)
        elif status == 'INSUFFICIENT EVIDENCE':
            warning.append(n)
        if 'blocking' in row:
            a.require(isinstance(row['blocking'], bool) and row['blocking'] == block,
                      'MODE_BLOCK_FLAG', p, 'Declared blocking flag contradicts the exact mode/status rule')
    return ('block' if blocking else 'warn' if warning else 'pass'), blocking, warning


def check_compliance(a, report, compliance, paths, paper_root, e6_count):
    a.obj(compliance, '/compliance', ('mode', 'stage', 'generated_at', 'prisma_trAIce', 'raise',
                                    'overall_decision', 'user_action_required'))
    a.require(compliance['mode'] == 'primary_research' and compliance['stage'] == '4.5'
              and compliance['prisma_trAIce'] is None, 'NON_SR_DISPATCH', '/compliance',
              'The supplied Round-10 dispatch is primary_research / Stage4.5 / PRISMA null')
    a.require(iso_datetime(compliance['generated_at']), 'COMPLIANCE_TIMESTAMP', '/compliance/generated_at',
              'Expected a timezone-qualified ISO-8601 timestamp')
    raise_part = a.obj(compliance['raise'], '/compliance/raise',
                       ('mode', 'principles', 'principle_evidence', 'block_decision'))
    a.require(raise_part['mode'] == 'principles_only', 'RAISE_MODE', '/compliance/raise/mode',
              'The current non-SR dispatch is principles_only')
    for name in ('principles', 'principle_evidence'):
        a.obj(raise_part[name], '/compliance/raise/' + name, PRINCIPLES)
        a.require(set(raise_part[name]) == set(PRINCIPLES), 'PRINCIPLE_KEYS', '/compliance/raise/' + name,
                  'Exactly the four named principles are required')
    for principle in PRINCIPLES:
        status = raise_part['principles'][principle]
        a.require(status in {'pass', 'warn', 'fail'}, 'PRINCIPLE_STATUS', principle, 'Unknown principle status')
        evidence = a.array(raise_part['principle_evidence'][principle], principle + '/evidence')
        a.require(bool(evidence), 'PRINCIPLE_EVIDENCE_EMPTY', principle, 'This handoff requires an explicit rationale')
        for item in evidence:
            a.text(item, principle + '/evidence')
        if status == 'pass':
            a.require(not any(tag in text for text in evidence for tag in ('[MATERIAL GAP]', '[WEAK EVIDENCE]')),
                      'PRINCIPLE_PASS_WITH_GAP', principle, 'A declared pass conflicts with its canonical gap tag')
    for path, text in strings_in(compliance):
        for tag in re.findall(r'\[(?:material\s+gap|weak\s+evidence|gap)[^\]]*\]', text, flags=re.I):
            a.require(tag in {'[MATERIAL GAP]', '[WEAK EVIDENCE]'}, 'NONCANONICAL_GAP_TAG', '/compliance' + path,
                      'Use canonical gap tags, with the principle name outside brackets', actual=tag)
    contribution = raise_part['block_decision']
    a.require(contribution in {'pass', 'warn'}, 'NON_SR_CAP', '/compliance/raise/block_decision',
              'Non-SR compliance contribution is capped at warn, not its independent aggregate')
    if any(v != 'pass' for v in raise_part['principles'].values()):
        a.require(contribution == 'warn', 'COMPLIANCE_CONTRIBUTION', '/compliance/raise',
                  'Non-pass principle assessments require the capped warn contribution')
    mode_decision, blocking_modes, warning_modes = mode_rows(a, report, paper_root)
    legacy = {'PASS': 'pass', 'PASS_WITH_CONDITIONS': 'warn', 'FAIL': 'block'}[report['verdict']]
    rank = {'pass': 0, 'warn': 1, 'block': 2}
    expected = max((contribution, legacy, mode_decision), key=rank.__getitem__)
    a.require(compliance['overall_decision'] == expected, 'COMPLIANCE_AGGREGATE', '/compliance/overall_decision',
              'Aggregate must include independent integrity and seven-mode decisions', expected=expected,
              actual=compliance['overall_decision'], contributions={'raise': contribution, 'integrity': legacy,
                                                                   'failure_modes': mode_decision})
    a.require(isinstance(compliance['user_action_required'], bool), 'USER_ACTION_TYPE', '/compliance',
              'user_action_required must be boolean')
    if expected in {'warn', 'block'} or e6_count:
        a.require(compliance['user_action_required'], 'USER_ACTION_REQUIRED', '/compliance',
                  'An unresolved warning/block/checkpoint cannot silently suppress user action')
    a.require('user_override' not in compliance, 'UNSUPPORTED_OVERRIDE_INPUT', '/compliance',
              'This manifest provides no new author override evidence; do not infer an override')
    pointer = report.get('compliance_report', report.get('audit_metadata', {}).get('compliance_report'))
    a.pointer(pointer, paths['compliance'], paper_root, '/report/compliance_report')
    if isinstance(pointer, dict) and 'overall_decision' in pointer:
        a.require(pointer['overall_decision'] == expected, 'EMBEDDED_COMPLIANCE_AGGREGATE', '/report/compliance_report',
                  'Embedded compliance summary contradicts the named candidate')
    for path, key, value in leaves(report):
        if e6_count and key in {'new_e6_disposition_required', 'new_author_disposition_required_before_advance'}:
            a.require(value is True, 'E6_DISPOSITION_SUPPRESSED', path, 'Nonempty new findings still need an author checkpoint')
        if e6_count and key == 'pipeline_action':
            a.require(value != 'authorized_to_continue', 'E6_AUTHORITY_INFERRED', path,
                      'No disposition artifact/event evidence is supplied to authorize continuation')
        if (expected == 'block' or e6_count) and key in {'stage5_eligible', 'stage5_authorized', 'stage6_authorized'}:
            a.require(value is not True, 'ADVANCEMENT_WITH_OPEN_BLOCK', path,
                      'A blocked report cannot claim next-stage authorization')
    a.section('NonSR_principles_canonical_tags_independent_decision_aggregate_no_override')
    return dict(compliance_contribution=contribution, integrity_contribution=legacy,
                failure_mode_contribution=mode_decision, aggregate=expected,
                blocking_modes=blocking_modes, warning_modes=warning_modes)


def check_paper(a, item, manifest_base, e6_validator):
    a.obj(item, '/manifest/papers/item', ('paper_id', *PATH_FIELDS, 'correction_items'))
    a.current = a.text(item['paper_id'], '/manifest/papers/item/paper_id')
    a.sections = []
    start_checks = a.checks
    paths = {name: a.path(item[name], manifest_base) for name in PATH_FIELDS}
    documents = {name: a.read(path) for name, path in paths.items() if name != 'draft'}
    draft = a.raw(paths['draft'])
    draft.decode('utf-8', errors='strict')
    paper_root = paths['draft'].parent.parent
    report, registry = documents['report'], documents['registry']
    e = check_report_shape(a, report)
    claims, metrics = check_registry_and_rows(a, registry, draft, documents['evidence_rows'],
                                              e['evidence_rows'], documents['source_map'])
    counts = Counter(row['verdict'] for row in claims.values())
    a.require(e['checked'] == len(claims) and e['verified'] == counts['VERIFIED'], 'E_DISTINCT_COUNTS',
              '/report/phases/E_claims', 'Claim-level summary differs from distinct evidence claims')
    for key in ('verdict_counts',):
        if key in e:
            a.obj(e[key], '/report/phases/E_claims/' + key)
            a.require({k: v for k, v in e[key].items() if v} == dict(counts), 'E_VERDICT_COUNTS', key,
                      'Declared verdict counts differ from distinct claims')
    if 'selected_tuple_count' in e:
        a.require(e['selected_tuple_count'] == len(documents['evidence_rows']), 'E_TUPLE_SUMMARY', 'E_claims',
                  'selected_tuple_count differs from actual evidence rows')
    expected_distortions = Counter((row['claim']['text'], row['verdict']) for row in claims.values()
                                   if row['verdict'] != 'VERIFIED')
    actual_distortions = Counter((row['claim'], row['verdict']) for row in e['distortions'])
    a.require(expected_distortions == actual_distortions, 'E_DISTORTION_POPULATION', 'E_claims/distortions',
              'Distortion text/verdict multiset differs from non-VERIFIED distinct claims')
    a.section('Distinct_claim_counts_full_claim_object_agreement_and_distortions')
    ordinary, seen = Counter(), set()
    for i, issue in enumerate(a.array(item['correction_items'], '/manifest/correction_items')):
        p = '/manifest/correction_items/' + str(i)
        a.obj(issue, p, ('correction_id', 'severity'))
        cid, severity = issue['correction_id'], issue['severity']
        a.require(isinstance(cid, str) and severity in SEVERITIES
                  and re.fullmatch(r'IL-' + str(severity) + r'-[1-9][0-9]*', cid) is not None,
                  'CORRECTION_ID_FORMAT', p, 'Use a report-local IL-<SEVERITY>-<n> correction ID')
        a.require(cid not in seen, 'DUPLICATE_CORRECTION_ID', p, 'Duplicate report-local correction ID')
        seen.add(cid)
        ordinary[severity] += 1
        a.require(cid == 'IL-' + severity + '-' + str(ordinary[severity]), 'CORRECTION_ID_SEQUENCE', p,
                  'Number each severity bucket freshly from 1 in manifest order; legacy IDs belong in mapping fields')
    a.require(all(report['overall_issues'][s] == ordinary[s] for s in SEVERITIES), 'OVERALL_ISSUE_COUNTS',
              '/report/overall_issues', 'Ordinary severity counts differ from manifest correction_items',
              expected=dict(ordinary), actual=report['overall_issues'])
    must_fail = ordinary['SERIOUS'] or ordinary['MEDIUM'] or counts['MAJOR_DISTORTION'] \
        or counts['UNVERIFIABLE'] or report['phases']['A_references']['failed']
    if must_fail:
        a.require(report['verdict'] == 'FAIL', 'INTEGRITY_VERDICT_UNDERSHOOT', '/report/verdict',
                  'A serious/medium/unverifiable/major-distortion/reference failure requires FAIL')
    elif ordinary['MINOR'] or counts['MINOR_DISTORTION'] or counts['UNVERIFIABLE_ACCESS']:
        a.require(report['verdict'] != 'PASS', 'INTEGRITY_UNQUALIFIED_PASS', '/report/verdict',
                  'Unresolved minor/access conditions cannot be an unqualified PASS')
    a.section('Report_local_correction_ID_buckets_and_issue_severity_verdict_consistency')
    check_coverage(a, e, documents['coverage'], paths, registry, paper_root)
    pointer = a.obj(e['claim_strength_drift_findings'], 'E_claims/claim_strength_drift_findings',
                    ('schema_version', 'artifact_path', 'artifact_sha256'))
    a.require(pointer['schema_version'] == 'claim-strength-drift-findings/1.0', 'E6_POINTER_VERSION', 'E_claims',
              'Unexpected E6 pointer version')
    a.pointer(pointer['artifact_path'], paths['e6'], paper_root, 'E_claims/claim_strength_drift_findings/artifact_path')
    a.require(pointer['artifact_sha256'] == digest(a.raw(paths['e6'])), 'E6_POINTER_HASH', 'E_claims',
              'E6 pointer digest does not match exact named finding-set bytes')
    findings = documents['e6']
    errors = sorted(e6_validator.iter_errors(findings), key=lambda error: '/'.join(map(str, error.absolute_path)))
    a.require(not errors, 'E6_OFFICIAL_SCHEMA_INVALID', '/e6', 'Installed E6 Draft202012 schema rejected the finding set',
              errors=[dict(path='/' + '/'.join(map(str, error.absolute_path)), message=error.message) for error in errors])
    a.require(findings['status'] == 'completed' and findings['final_draft_sha256'] == digest(draft)
              and findings['revision_evidence_bundle_sha256'] == digest(a.raw(paths['bundle'])),
              'E6_CURRENT_BINDING', '/e6', 'A supplied revision bundle requires completed E6 bound to exact draft/bundle')
    ids = [row['finding_id'] for row in findings['findings']]
    a.require(ids == ['ADV-E6-' + str(i + 1) for i in range(len(ids))], 'E6_ID_SEQUENCE', '/e6/findings',
              'Finding IDs must be the exact ordered ADV-E6-1..N sequence')
    a.section('Installed_E6_Draft202012_schema_and_exact_current_artifact_bindings')
    decisions = check_compliance(a, report, documents['compliance'], paths, paper_root, len(ids))
    metrics.update(verdict_counts=dict(counts), ordinary_issue_counts={s: ordinary[s] for s in SEVERITIES},
                   e6_findings=len(ids), coverage_candidates=len(documents['coverage']['candidates']),
                   coverage_candidate_unregistered_count=documents['coverage']['candidate_unregistered_count'])
    result = dict(paper_id=a.current, status='PASS_CUSTOM_CROSSFIELD_ONLY',
                  checks_passed=a.checks - start_checks, completed_sections=list(a.sections),
                  artifacts={name: a.descriptor(path) for name, path in paths.items()},
                  metrics=metrics, decisions=decisions,
                  e6_disposition='NOT_VALIDATED_OR_INFERRED' if ids else 'NOT_REQUIRED_ZERO_FINDINGS',
                  author_disposition_or_stage_authority_certified=False)
    a.results.append(result)


def main():
    audit = Audit()
    output = dict(checker='round10-round4-custom-crossfield-handoff/1.0',
                  official_Schema5_validator=False, official_coverage_or_EVR_replay=False,
                  official_compliance_schema_validation=False, network_used=False, files_written=False,
                  semantic_or_scientific_verification=False, author_disposition_or_stage_authority_certified=False)
    try:
        audit.require(len(sys.argv) == 2, 'CLI_ARGUMENTS', 'argv', 'Provide exactly one local JSON manifest path')
        manifest_path = audit.path(sys.argv[1], Path.cwd())
        manifest = audit.read(manifest_path)
        audit.obj(manifest, '/manifest', ('papers',))
        papers = audit.array(manifest['papers'], '/manifest/papers')
        audit.require(bool(papers), 'EMPTY_MANIFEST', '/manifest/papers', 'At least one independently selected paper is required')
        ids = [row.get('paper_id') if isinstance(row, dict) else None for row in papers]
        audit.require(all(isinstance(x, str) and x for x in ids) and len(set(ids)) == len(ids),
                      'MANIFEST_PAPER_IDS', '/manifest/papers', 'Paper IDs must be nonempty and unique')
        schema = audit.read(E6_SCHEMA)
        for location, value in strings_in(schema):
            if location.endswith('/$ref'):
                audit.require(value.startswith('#/'), 'EXTERNAL_SCHEMA_REFERENCE', location,
                              'This checker refuses any external schema resolution')
        from jsonschema import Draft202012Validator
        Draft202012Validator.check_schema(schema)
        validator = Draft202012Validator(schema)
        output['manifest'] = audit.descriptor(manifest_path)
        output['e6_schema'] = audit.descriptor(E6_SCHEMA)
        for paper in papers:
            check_paper(audit, paper, manifest_path.parent, validator)
        output.update(status='PASS_CUSTOM_CROSSFIELD_ONLY', papers=audit.results,
                      checks_passed=audit.checks, pipeline_or_paper_PASS_inferred=False)
        code = 0
    except CheckFailure as exc:
        output.update(status='FAIL_CUSTOM_CROSSFIELD_ONLY', failed_paper=audit.current,
                      failure=exc.result, completed_papers=audit.results,
                      current_completed_sections=audit.sections, checks_passed=audit.checks)
        code = 1
    except (Exception, KeyboardInterrupt) as exc:
        output.update(status='FAIL_CUSTOM_CROSSFIELD_ONLY', failed_paper=audit.current,
                      failure=dict(code='EXCEPTION_STOP', exception_type=type(exc).__name__, message=str(exc)),
                      completed_papers=audit.results, current_completed_sections=audit.sections,
                      checks_passed=audit.checks)
        code = 1
    print(json.dumps(output, ensure_ascii=False, indent=2, allow_nan=False))
    return code


if __name__ == '__main__':
    raise SystemExit(main())
