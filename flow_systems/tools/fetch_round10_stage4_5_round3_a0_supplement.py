"""Late Round-3 S2 metadata supplement: explicit locked inputs, NDJSON stdout only.

No local writes, cache mutations, official validators, or manuscript edits.
The caller retains stdout with apply_patch. Network errors stop the remaining
S2 batch; exhausted 429 retries do the same. HTTP 5xx skips one reference.
"""
import hashlib
import json
import os
import re
import sys
import time
import unicodedata
import urllib.error
import urllib.parse
import urllib.request
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LOCK = ROOT / 'BATCH_ROUND10_STAGE4_5_ROUND3_INPUT_LOCK.json'
EXPECTED_LOCK_SHA256 = '0c7755b343990af1d37049838f81e0483323584c96eab58cddf6e14bc572e229'
PROTOCOL = Path('/root/autodl-tmp/.codex/plugins/cache/ars-codex/ars-codex/0.1.28/skills/academic-research-suite/ars/deep-research/references/semantic_scholar_api_protocol.md')
EXPECTED_COUNTS = {'P29': 22, 'P30': 28, 'P31': 24, 'P32': 30, 'P33': 22}
BASE = 'https://api.semanticscholar.org/graph/v1'
FIELDS = 'title,authors,year,externalIds,venue,publicationDate'


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


def utc():
    return datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z')


def emit(value):
    print(json.dumps(value, ensure_ascii=False), flush=True)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def bib_entries(raw):
    text = raw.decode('utf-8')
    heads = list(re.finditer(r'(?m)^@([A-Za-z]+)\{([^,\s]+),', text))
    rows = []
    for i, head in enumerate(heads):
        end = heads[i + 1].start() if i + 1 < len(heads) else len(text)
        block = text[head.end():end]
        fields, pos = {}, 0
        while True:
            field = re.search(r'(?m)^\s*([A-Za-z][A-Za-z0-9_]*)\s*=\s*', block[pos:])
            if field is None:
                break
            name = field.group(1).lower()
            start = pos + field.end()
            if block[start] != '{':
                raise ValueError('Unsupported unbraced BibTeX field: ' + head.group(2) + ':' + name)
            depth, cursor = 1, start + 1
            while cursor < len(block) and depth:
                if block[cursor] == '\\':
                    cursor += 2
                    continue
                depth += (block[cursor] == '{') - (block[cursor] == '}')
                cursor += 1
            if depth:
                raise ValueError('Unclosed BibTeX field: ' + head.group(2) + ':' + name)
            if name in fields:
                raise ValueError('Duplicate BibTeX field: ' + head.group(2) + ':' + name)
            fields[name] = block[start + 1:cursor - 1]
            pos = cursor
        if not fields.get('title') or not fields.get('year'):
            raise ValueError('Missing title/year: ' + head.group(2))
        rows.append({'ref_slug': head.group(2), 'entry_type': head.group(1), 'bib_fields_raw': fields,
                     'entry_raw_utf8_span': {'start_byte': len(text[:head.start()].encode()), 'end_byte': len(text[:end].encode())}})
    return rows


def title_projection(title):
    title = re.sub(r'\\(mathrm|mathbb|mathbf|text|emph|textrm)\b', '', title)
    title = re.sub(r'\\([A-Za-z]+)', r'\1', title)
    title = title.translate(str.maketrans('', '', '{}\\$'))
    return ' '.join(title.split())


def normalized_title(title):
    return ' '.join(''.join(c for c in title.casefold() if not unicodedata.category(c).startswith('P')).split())


def similarity(a, b):
    a, b = normalized_title(a), normalized_title(b)
    if not a and not b:
        return 1.0
    prior = list(range(len(b) + 1))
    for i, ac in enumerate(a, 1):
        current = [i]
        for j, bc in enumerate(b, 1):
            current.append(min(current[-1] + 1, prior[j] + 1, prior[j - 1] + (ac != bc)))
        prior = current
    return 1 - prior[-1] / max(len(a), len(b))


def request_for(ref):
    fields = ref['bib_fields_raw']
    title = title_projection(fields['title'])
    doi = fields.get('doi', '').strip()
    if doi:
        url = BASE + '/paper/DOI:' + urllib.parse.quote(doi, safe='/') + '?' + urllib.parse.urlencode({'fields': FIELDS + ',citationCount'})
        method = 's2_doi_lookup'
    else:
        url = BASE + '/paper/search?' + urllib.parse.urlencode({'query': title, 'limit': 5, 'fields': FIELDS})
        method = 's2_title_search'
    return {'method': 'GET', 'url': url, 'verification_method': method,
            'query_title': title, 'query_doi': doi or None}


def main():
    start = utc()
    raw_lock = LOCK.read_bytes()
    if sha(raw_lock) != EXPECTED_LOCK_SHA256:
        emit({'event': 'PROTECTED_STOP', 'kind': 'NEW_LOCK_HASH_MISMATCH', 'path': str(LOCK), 'observed_sha256': sha(raw_lock), 'observed_at_utc': utc()})
        return 2
    lock = json.loads(raw_lock)
    refs, bindings, counts = [], [], {}
    for paper in lock['papers']:
        pid = paper['paper_id']
        if pid not in EXPECTED_COUNTS:
            continue
        binding = paper['current_preview']['bibliography']
        raw = (ROOT / binding['path']).read_bytes()
        actual = {'path': binding['path'], 'bytes': len(raw), 'sha256': sha(raw)}
        if actual != binding:
            emit({'event': 'PROTECTED_STOP', 'kind': 'NEW_LOCKED_BIBLIOGRAPHY_BINDING_MISMATCH', 'paper_id': pid, 'expected': binding, 'observed': actual, 'observed_at_utc': utc()})
            return 2
        parsed = bib_entries(raw)
        if len(parsed) != EXPECTED_COUNTS[pid]:
            emit({'event': 'PROTECTED_STOP', 'kind': 'NEW_REFERENCE_POPULATION_TARGET_MISMATCH', 'paper_id': pid, 'expected_count': EXPECTED_COUNTS[pid], 'observed_count': len(parsed), 'observed_at_utc': utc()})
            return 2
        counts[pid] = len(parsed)
        bindings.append({'paper_id': pid, **actual, 'binding_status': 'MATCH'})
        for item in parsed:
            item.update({'paper_id': pid, 'bibliography_path': binding['path'], 'bibliography_sha256': sha(raw)})
            item['planned_request'] = request_for(item)
            refs.append(item)
    if counts != EXPECTED_COUNTS or len({r['ref_slug'] for r in refs}) != 126:
        emit({'event': 'PROTECTED_STOP', 'kind': 'NEW_BATCH_POPULATION_TARGET_MISMATCH', 'counts': counts, 'observed_at_utc': utc()})
        return 2
    emit({'event': 'inventory', 'started_at_utc': start, 'input_lock': {'path': LOCK.relative_to(ROOT).as_posix(), 'sha256': sha(raw_lock)},
          'protocol': {'path': str(PROTOCOL), 'sha256': sha(PROTOCOL.read_bytes())}, 'helper': {'path': Path(__file__).relative_to(ROOT).as_posix(), 'sha256': sha(Path(__file__).read_bytes())},
          'timing_status': 'LATE_SUPPLEMENT_AFTER_COMPLETED_CURRENT_ROUND_A1_WEBSEARCH', 'requested_reference_counts': EXPECTED_COUNTS,
          'bibliography_bindings': bindings, 'reference_count': len(refs), 'references': refs,
          'transport_policy': {'maximum_requests_per_second': 1, 'timeout_seconds': 20, 'http_429_backoff_seconds': 2, 'maximum_429_retries': 3,
                               'network_error': 'stop_remaining_S2_batch_API_UNAVAILABLE', 'http_5xx': 'skip_reference_to_existing_A1',
                               'exhausted_429': 'stop_remaining_S2_batch_API_UNAVAILABLE', 'permission_failure': 'stop_S2_no_bypass'},
          'title_projection': 'Remove BibTeX grouping/backslash/dollar delimiters and formatting commands; collapse whitespace. Raw fields are preserved separately. Match normalization is case-insensitive with Unicode punctuation removed.'})
    api_key = os.environ.get('S2_API_KEY')
    opener = urllib.request.build_opener(NoRedirect())
    last_start, stop_reason = None, None
    outcomes, attempts_total, matched_ids = Counter(), 0, defaultdict(list)
    for ref in refs:
        request = ref['planned_request']
        result = {'event': 'reference_result', 'paper_id': ref['paper_id'], 'ref_slug': ref['ref_slug'], 'request': request, 'attempts': [],
                  'verification_scope': 'S2 metadata only; never passage support, mathematical validity, human-read state or scientific validation.'}
        if stop_reason:
            result.update({'status': 'API_UNAVAILABLE', 'attempted': False, 'reason': stop_reason, 'fallback': 'Existing completed current-round A1 primary-source work; no new A1 search performed.'})
        else:
            result['attempted'] = True
            for retry in range(4):
                if retry:
                    time.sleep(2)
                if last_start is not None:
                    time.sleep(max(0, 1.0 - (time.monotonic() - last_start)))
                headers = {'User-Agent': 'flow-systems-stage4.5-round3-a0-supplement/1.0', 'Accept': 'application/json'}
                if api_key:
                    headers['x-api-key'] = api_key
                call = urllib.request.Request(request['url'], headers=headers)
                attempt = {'attempt_number': retry + 1, 'started_at_utc': utc(), 'request_method': 'GET', 'request_url': request['url'],
                           'authentication': 'configured_S2_API_KEY' if api_key else 'unauthenticated'}
                status, body, failure = None, None, None
                last_start = time.monotonic()
                try:
                    with opener.open(call, timeout=20) as response:
                        status, body = response.status, response.read()
                        attempt['response_headers'] = {k: v for k, v in response.headers.items() if k.lower() in ('content-type', 'date', 'retry-after')}
                except urllib.error.HTTPError as exc:
                    status, body = exc.code, exc.read()
                    attempt['response_headers'] = {k: v for k, v in exc.headers.items() if k.lower() in ('content-type', 'date', 'retry-after')}
                except (urllib.error.URLError, TimeoutError, OSError) as exc:
                    failure = {'type': type(exc).__name__, 'message': str(exc)}
                attempt.update({'ended_at_utc': utc(), 'http_status': status, 'network_error': failure,
                                'response_body_utf8': body.decode('utf-8', errors='replace') if body is not None else None,
                                'response_body_raw_sha256': sha(body) if body is not None else None, 'response_body_raw_bytes': len(body) if body is not None else None})
                result['attempts'].append(attempt)
                attempts_total += 1
                if failure:
                    stop_reason = '[S2-API-UNAVAILABLE] Network error at ' + ref['ref_slug'] + '; no further S2 calls attempted.'
                    result.update({'status': 'API_UNAVAILABLE', 'reason': stop_reason})
                    break
                if status == 429:
                    if retry < 3:
                        continue
                    stop_reason = '[S2-API-UNAVAILABLE] Four 429 responses (initial plus three bounded retries) at ' + ref['ref_slug'] + '; remaining S2 batch not attempted.'
                    result.update({'status': 'API_UNAVAILABLE', 'reason': stop_reason})
                    break
                if status in (401, 403):
                    stop_reason = '[S2-API-UNAVAILABLE] Permission response HTTP ' + str(status) + ' at ' + ref['ref_slug'] + '; no credential extraction or alternate transport attempted.'
                    result.update({'status': 'API_UNAVAILABLE', 'reason': stop_reason, 'permission_stop': True})
                    break
                if status is not None and status >= 500:
                    result.update({'status': 'API_UNAVAILABLE', 'reason': 'HTTP 5xx; skip this reference per protocol.'})
                    break
                if status == 404:
                    result.update({'status': 'S2_NOT_FOUND', 'reason': 'DOI/title endpoint returned 404; absence from S2 is not fabrication.'})
                    break
                if status != 200:
                    result.update({'status': 'API_UNAVAILABLE', 'reason': 'Unexpected HTTP status; no replacement query or endpoint guessing.'})
                    break
                try:
                    parsed = json.loads(body)
                    candidates = parsed.get('data', []) if request['verification_method'] == 's2_title_search' else [parsed]
                    scored = [{'metadata': item, 'title_similarity': similarity(request['query_title'], item.get('title') or ''),
                               'year_matches': str(item.get('year')) == ref['bib_fields_raw']['year']} for item in candidates]
                except (ValueError, TypeError, AttributeError) as exc:
                    result.update({'status': 'API_UNAVAILABLE', 'reason': 'Response parsing unavailable: ' + type(exc).__name__})
                    break
                result['candidate_comparisons'] = scored
                qualifying = [item for item in scored if item['title_similarity'] >= 0.70]
                qualifying.sort(key=lambda item: (item['year_matches'], item['title_similarity']), reverse=True)
                if not qualifying:
                    result.update({'status': 'DOI_MISMATCH' if request['query_doi'] and candidates else 'S2_NOT_FOUND',
                                   'reason': 'No returned title reaches the protocol 0.70 threshold. Metadata discrepancy requires semantic review; not an artifact-binding mismatch.'})
                    break
                chosen = qualifying[0]
                meta = chosen['metadata']
                observations = []
                if not chosen['year_matches']:
                    observations.append({'kind': 'YEAR_DIFFERENCE', 'bib_year': ref['bib_fields_raw']['year'], 's2_year': meta.get('year'), 'interpretation': 'Unadjudicated metadata difference; print/online/preprint dates may differ.'})
                returned_doi = (meta.get('externalIds') or {}).get('DOI')
                if request['query_doi'] and returned_doi and returned_doi.casefold() != request['query_doi'].casefold():
                    observations.append({'kind': 'RETURNED_DOI_DIFFERENCE', 'query_doi': request['query_doi'], 'returned_doi': returned_doi})
                result.update({'status': 'S2_METADATA_MATCH', 'semantic_scholar_id': meta.get('paperId'), 's2_title': meta.get('title'),
                               's2_authors': meta.get('authors'), 's2_year': meta.get('year'), 's2_venue': meta.get('venue'), 's2_citation_count': meta.get('citationCount'),
                               'match_score': chosen['title_similarity'], 'metadata_observations': observations,
                               'doi_exact_string_match': returned_doi == request['query_doi'] if request['query_doi'] else None,
                               'metadata_boundary': 'Title/identifier match is not complete author/venue/date correctness; retained primary-source A1 evidence controls semantic adjudication.'})
                if meta.get('paperId'):
                    matched_ids[meta['paperId']].append(ref['ref_slug'])
                break
            result['fallback'] = 'Existing completed current-round A1 primary-source work remains authoritative; no new A1 search performed.'
        outcomes[result['status']] += 1
        emit(result)
    emit({'event': 'summary', 'completed_at_utc': utc(), 'reference_count': len(refs), 'status_counts': dict(outcomes), 'actual_http_call_count': attempts_total,
          'remaining_batch_stop_reason': stop_reason, 'same_s2_id_groups': [{'semantic_scholar_id': sid, 'ref_slugs': slugs, 'boundary': 'Candidate duplicate/work-family association; cross-paper reuse is not an erroneous bibliography duplicate.'} for sid, slugs in matched_ids.items() if len(slugs) > 1],
          'official_validator_or_replay_run': False, 'scientific_execution': False, 'files_written_by_helper': [], 'cached_metadata_mutated': False})
    return 0


if __name__ == '__main__':
    try:
        raise SystemExit(main())
    except Exception as exc:
        emit({'event': 'PREPARATORY_STOP', 'kind': type(exc).__name__, 'message': str(exc), 'observed_at_utc': utc(), 'no_official_validator_invoked': True})
        raise SystemExit(3)
