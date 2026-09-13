"""Restricted P31 repair: build only the 28 affected rows; read-only JSON stdout.

The installed official builder checks excerpt provenance, NOT locator accuracy
or the scientific claim. Six held sources are explicitly extracted historical
publisher-deposited abstracts; S19 is only a retained historical short fragment.
No old file, registry, writer text, coverage record, or unaffected row is changed.
"""
import sys
sys.dont_write_bytecode = True
import copy
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import quote

ARS = Path('/root/autodl-tmp/.codex/plugins/cache/ars-codex/ars-codex/0.1.28/skills/academic-research-suite/ars')
sys.path.insert(0, str(ARS / 'scripts'))
import evidence_rows

BASE = Path('papers/31-level11-conjugacy-owner-ledger/notes')
PREFIX = 'stage4_5_round4_'
def read(name):
    return json.loads((BASE / name).read_text(encoding='utf-8'))
def digest(raw):
    return hashlib.sha256(raw).hexdigest()
def descriptor(path):
    raw = path.read_bytes()
    return dict(path=str(path), bytes=len(raw), sha256=digest(raw))

started = datetime.now(timezone.utc).isoformat()
registry = read(PREFIX + 'recovery1_claim_registry.json')
previous = read(PREFIX + 'recovery1_evidence_rows.json')
sources = read(PREFIX + 'recovery3_source_map.json')
provenance = {r['ref_slug']: r for r in read(PREFIX + 'recovery3_source_provenance.json')['sources']}
finalization_path = BASE / 'stage4_5_round1_source_finalization_proposal.json'
finalization = read(finalization_path.name)
records = {r['source_id']: (i, r) for i, r in enumerate(finalization['rows'])}
draft = (BASE / 'stage4_prime_revision_round6.tex').read_bytes()
assert digest(draft) == registry['draft_raw_sha256']
claims = {c['claim_id']: c for c in registry['claims']}
expected_refs = {'P31-S05', 'P31-S06', 'P31-S08', 'P31-S09', 'P31-S16', 'P31-S17', 'P31-S19'}
assert set(sources) == set(provenance) == expected_refs
assert len(previous) == 403

affected = []
for position, old in enumerate(previous):
    if old['anchor']['kind'] == 'none':
        continue
    slug = old['source']['ref_slug']
    assert slug in expected_refs
    prov = provenance[slug]
    claim = claims[old['claim']['claim_id']]
    span = claim['draft_span']
    assert draft[span['start_byte']:span['end_byte']].decode('utf-8') == claim['claim_text'] == old['claim']['text']
    assert claim['ref_slugs'] == [slug] and len(claim['writer_anchors']) == 1
    anchor = claim['writer_anchors'][0]
    record_index, record = records[slug]
    assert anchor == prov['exact_locator'] == record['exact_passage_locator']
    assert prov['excerpt'] == record['support_excerpt'] and prov['excerpt'] in sources[slug]
    assert prov['excerpt_literal_match'] is True
    assert len(prov['excerpt'].split()) <= 25
    carrier = Path(prov['carrier']['path'])
    assert descriptor(carrier) == {key: prov['carrier'][key] for key in ('path', 'bytes', 'sha256')}
    pointer = str(finalization_path) + '#/rows/' + str(record_index)
    text = claim['claim_text']
    if text.startswith('The bounded source-finalization record'):
        role = 'Historical record claim: the named locator is literally recorded in exact_passage_locator; this verifies what the record says, not an independent locator-authentication claim.'
    elif text.startswith('The retained excerpt'):
        role = 'Bounded-context claim: the retained source fragment supplies the limited context expressly described; the manuscript explicitly excludes proof of the registered role in full.'
    elif text.startswith('Manuscript use is limited'):
        role = 'Project-use claim: registered_role matches this stated manuscript-use restriction. The external fragment alone does not prove the full registered mathematical role.'
    elif text.startswith('Its recorded scope'):
        role = 'Project-boundary claim: hypothesis_or_scope and transfer_boundary_preserved match the stated scope and forbidden transfer; these are local recorded restrictions, not a theorem or implementation result.'
    else:
        raise AssertionError('Unexpected affected claim kind: ' + claim['claim_id'])
    if slug == 'P31-S19':
        source_scope = ('Source level: only the historical carrier support_excerpt (75 UTF-8 bytes) is held. Its carrier digest is the JSON record digest, NOT the old PDF response digest. No full PDF or page-text extraction is replayable here; the old page-1 locator is retained as a recorded locator and is NOT independently page-authenticated. Recovery1 ordinary browser text at printed p.182 separately corroborates wording, not PDF page mapping.')
        label = slug + ' — historical retained original-language fragment only; original PDF page not replayable'
    else:
        source_scope = ('Source level: actual publisher-deposited Crossref abstract retained in the input-locked historical network record, with explicit markup/entity/whitespace extraction into this exact held source string. Source provenance records the transformation; the builder does not normalize or authenticate the locator. Any Recovery1 different-locator evidence remains separately identified corroboration, not the selected tuple.')
        label = slug + ' — historical publisher-deposited abstract; explicit text extraction'
    detail = role + ' Local record: ' + pointer + '. ' + source_scope + ' No full theorem, subgroup completeness, primitive-owner certificate, execution, or new transfer conclusion is inferred.'
    template = {
        'surface': 'phase_e_claim_verification',
        'row_id': 'EVR-P31-R4R3-' + str(position + 1).zfill(4),
        'claim': copy.deepcopy(old['claim']),
        'source': {'ref_slug': slug, 'display_label': label, 'source_artifact_sha256': prov['carrier']['sha256']},
        'anchor': {'kind': old['anchor']['kind'], 'value_encoded': quote(anchor, safe='')},
        'verdict': old['verdict'],
        'detail': detail,
    }
    row = evidence_rows.build(template, sources[slug], extracted_text=prov['excerpt'])
    affected.append(dict(position=position, previous_row_id=old['row_id'], previous_row_sha256=old['row_sha256'], row=row))
assert len(affected) == 28
assert all(sum(x['row']['source']['ref_slug'] == s for x in affected) == 4 for s in expected_refs)
inputs = [BASE / (PREFIX + x) for x in ['recovery1_claim_registry.json', 'recovery1_evidence_rows.json', 'recovery3_source_map.json', 'recovery3_source_provenance.json']]
inputs += [finalization_path, BASE / 'stage4_prime_revision_round6.tex', Path(__file__), ARS / 'scripts/evidence_rows.py']
print(json.dumps(dict(status='BUILT_28_OFFICIAL_ROWS_ONLY', started_at=started,
    completed_at=datetime.now(timezone.utc).isoformat(), inputs=[descriptor(p) for p in inputs],
    official_builder_calls=len(affected), unaffected_rows_to_preserve=375,
    source_locator_authentication_inferred=False, scientific_verdict_change=False,
    files_written=False, network_used=False, affected=affected), ensure_ascii=False))
