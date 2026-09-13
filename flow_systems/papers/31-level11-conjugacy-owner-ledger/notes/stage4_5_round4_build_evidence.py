"""One official evidence_rows.build call per selected tuple; no filesystem writes.

stdout is base64(gzip(exact JSON rows)); the orchestration persists these bytes
with apply_patch and then extracts the JSON text without rebuilding rows.
"""
import base64
import gzip
import hashlib
import json
from pathlib import Path
import sys
from urllib.parse import quote

sys.dont_write_bytecode = True
ARS = Path('/root/autodl-tmp/.codex/plugins/cache/ars-codex/ars-codex/0.1.28/skills/academic-research-suite/ars')
sys.path.insert(0, str(ARS / 'scripts'))
import evidence_rows

BASE = Path('papers/31-level11-conjugacy-owner-ledger/notes')
def get(name):
    return json.loads((BASE / ('stage4_5_round4_' + name + '.json')).read_text())
registry = get('claim_registry')
decisions = {r['claim_id']: r for r in get('semantic_claim_review')['claim_decisions']}
sources = get('source_map')
provenance = {r['ref_slug']: r for r in get('source_provenance')['sources']}
raw = (BASE / 'stage4_prime_revision_round6.tex').read_bytes()
assert hashlib.sha256(raw).hexdigest() == registry['draft_raw_sha256']
rows = []
for claim in registry['claims']:
    span = claim['draft_span']
    assert raw[span['start_byte']:span['end_byte']].decode('utf-8') == claim['claim_text']
    for source in claim['ref_slugs'] or [None]:
        decision = decisions[claim['claim_id']]
        prov = provenance.get(source)
        anchor = {'kind': 'section', 'value_encoded': quote(prov['exact_locator'], safe='')} if prov else {'kind':'none','value_encoded':''}
        template = {
            'surface':'phase_e_claim_verification',
            'row_id': 'EVR-P31-R4-' + str(len(rows)+1).zfill(4),
            'claim': {'claim_id':claim['claim_id'],'text':claim['claim_text'], 'paper_locator':decision['block_id']+'; UTF8 '+str(span['start_byte'])+':'+str(span['end_byte']), 'selection_tier':'ALL'},
            'source': {'ref_slug':source,'display_label':source if source else 'Project-local definition, record, direct reasoning, or unresolved author attestation'},
            'anchor':anchor,
            'verdict':decision['verdict'],
            'detail':decision['detail'],
        }
        if prov:
            assert prov['excerpt_literal_match'] and len(prov['excerpt']) <= 1000
            template['source']['source_artifact_sha256'] = prov['carrier']['sha256']
            row = evidence_rows.build(template, sources[source], extracted_text=prov['excerpt'])
        else:
            row = evidence_rows.build(template, None)
        rows.append(row)
assert len(rows) == sum(max(1,len(c['ref_slugs'])) for c in registry['claims'])
payload = (json.dumps(rows, ensure_ascii=False, indent=2)+'\n').encode('utf-8')
print(base64.b64encode(gzip.compress(payload, mtime=0)).decode('ascii'))
