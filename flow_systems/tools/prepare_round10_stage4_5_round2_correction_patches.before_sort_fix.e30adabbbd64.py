#!/usr/bin/env python3
"""Prepare exact, unapplied integrity patches within the confirmed R10 scope.

Emits source-accounted issue-list adapters and writer handoffs, never a draft,
patch approval, official authorization sidecar, or scientific result.
"""
import datetime
import hashlib
import importlib.util
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
ARS = Path('/root/autodl-tmp/.codex/plugins/cache/ars-codex/ars-codex/0.1.28/skills/academic-research-suite/ars')
REQUEST = ROOT / 'BATCH_ROUND10_STAGE4_5_ROUND2_CORRECTION_AUTHORIZATION_REQUEST.json'
REQUEST_SHA = 'd9be18e2199dd64100a1482018eb9bf77586e2548ba751cc0c2b57e06195f992'
PREFIX = 'BATCH_ROUND10_STAGE4_5_ROUND2_CORRECTION_SCOPE_'


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def desc(path):
    raw = path.read_bytes()
    return {'path': str(path.relative_to(ROOT)), 'sha256': sha(raw), 'bytes': len(raw)}


def encoded(obj):
    return (json.dumps(obj, ensure_ascii=False, indent=2, sort_keys=True) + '\n').encode()


def prepare():
    assert sha(REQUEST.read_bytes()) == REQUEST_SHA
    request = json.loads(REQUEST.read_bytes())
    sys.path.insert(0, str(ARS / 'scripts'))
    import revision_roadmap as rr
    import _block_parser as bp
    stamp = datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0).isoformat().replace('+00:00', 'Z')
    event = ROOT / (PREFIX + 'AUTHOR_EVENT_20260905.txt')
    assert event.read_bytes() == '确认\n'.encode()
    record = ROOT / (PREFIX + 'AUTHORIZATION_RECORD.md')
    outputs = {}
    receipt_path = ROOT / (PREFIX + 'AUTHORIZATION_RECEIPT.json')
    receipt = {
        'schema_version': 'round10-integrity-correction-scope-confirmation/1.0',
        'recorded_at_utc': stamp,
        'status': 'AUTHOR_CONFIRMED_EXACT_SCOPE_PATCH_BYTES_NOT_YET_APPROVED',
        'author_event': desc(event), 'authorization_record': desc(record),
        'confirmed_request': desc(REQUEST), 'confirmed_scope': request['aggregate'],
        'allowed_derived_operations': request['allowed_derived_operations'],
        'explicitly_forbidden': request['explicitly_forbidden'],
        'exact_patch_sha256_approval_present': False,
        'formal_integrity_apply_authorization_emitted': False,
        'scope_effect': 'Prepare exact patches within the confirmed targets; present concrete patch digests together before official integrity apply. Do not fabricate approval of future bytes.'
    }
    receipt_raw = encoded(receipt)
    outputs[receipt_path] = receipt_raw
    receipt_desc = {'path': str(receipt_path.relative_to(ROOT)), 'sha256': sha(receipt_raw), 'bytes': len(receipt_raw)}
    for p in request['papers']:
        for key in ('base_draft', 'base_block_manifest', 'stage4_5_blocker_source'):
            assert desc(ROOT / p[key]['path']) == p[key], key
        base = ROOT / p['base_draft']['path']
        assert not (ROOT / p['proposed_successor_draft']).exists()
        text = base.read_text()
        parsed = bp.parse_document(text)
        by_id = parsed.block_by_id()
        manifest = json.loads((ROOT / p['base_block_manifest']['path']).read_bytes())
        assert manifest['base_draft_hash'] == p['base_draft']['sha256'][:12]
        old_hashes = {b['block_id']: b['old_hash'] for b in manifest['blocks']}
        findings = sorted({i for t in p['targets'] for i in t['finding_ids']})
        assert len(findings) == p['issue_count']
        mapping = {fid: fid if re.fullmatch(r'IL-(SERIOUS|MEDIUM|MINOR)-[1-9][0-9]*', fid)
                   else f'EA-{i+1:03d}' for i, fid in enumerate(findings)}
        revision_round = int(re.search(r'round(\d+)\.tex$', p['proposed_successor_draft']).group(1))
        issues = {'schema_version': 'integrity-correction-list/1.0',
                  'revision_round': revision_round, 'base_draft_sha256': p['base_draft']['sha256'],
                  'issues': [{'correction_id': mapping[fid],
                              'description': f"Frozen Stage-4.5-Round-2 finding {fid}. Confirmed conservative branch: {p['strategy']}",
                              'proposed_targets': [{'block_id': t['block_id'], 'allowed_operations': t['allowed_operations']}
                                                   for t in p['targets'] if fid in t['finding_ids']]}
                             for fid in findings]}
        rr.validate_integrity_correction_list(issues, issue_list_raw=encoded(issues), base_raw=base.read_bytes())
        notes = base.parent
        issue_path = notes / 'stage4_5_round2_correction_patch_issue_list.json'
        issue_raw = encoded(issues)
        issue_desc = {'path': str(issue_path.relative_to(ROOT)), 'sha256': sha(issue_raw), 'bytes': len(issue_raw)}
        rows = []
        for target in p['targets']:
            block = by_id[target['block_id']]
            normalized = block.normalized_text.encode()
            assert sha(normalized) == target['expected_current_normalized_content_sha256']
            assert len(normalized) == target['expected_current_normalized_content_bytes']
            assert old_hashes[block.block_id] == target['manifest_old_hash_prefix_12'] == block.norm_hash
            span = target['content_utf8_span_end_exclusive']
            raw = base.read_bytes()[span['start']:span['end']]
            assert sha(raw) == target['expected_current_raw_content_sha256']
            rows.append({**target, 'correction_ids': [mapping[fid] for fid in target['finding_ids']],
                         'old_text': block.normalized_text})
        source_paths = [notes / name for name in (
            'stage4_5_round2_local_claim_dependency_catalog.json',
            'stage4_5_round2_local_claim_semantic_re_adjudication.json',
            'stage4_5_round2_local_semantic_adjudication.json',
            'stage4_5_round2_reference_citation_audit.json',
            'stage4_5_round2_evidence_rows.json', 'stage4_5_round2_reference_network_audit.json',
            'stage4_5_round2_final_integrity_report.md') if (notes / name).is_file()]
        handoff = {'schema_version': 'round10-integrity-correction-writer-handoff/1.0',
                   'generated_at_utc': stamp, 'paper_id': p['paper_id'],
                   'scope_confirmation': receipt_desc, 'confirmed_request': desc(REQUEST),
                   'status': 'WRITE_PATCH_ONLY_AWAIT_EXACT_PATCH_APPROVAL_BEFORE_APPLY',
                   'base_draft': p['base_draft'], 'base_block_manifest': p['base_block_manifest'],
                   'issue_list': issue_desc, 'finding_to_correction_id': mapping,
                   'source_finding_artifact': p['stage4_5_blocker_source'],
                   'source_materials': [desc(path) for path in source_paths],
                   'strategy': p['strategy'], 'targets': rows,
                   'patch_header': {'patch_format_version': '1.1', 'authorization_context': 'integrity_correction',
                                    'revision_round': revision_round, 'base_draft_hash': manifest['base_draft_hash'],
                                    'issue_list_sha256': sha(issue_raw), 'emitted_by': 'draft_writer_agent'},
                   'patch_output': str((notes / 'stage4_5_round2_correction_patch.json').relative_to(ROOT)),
                   'log_output': str((notes / 'stage4_5_round2_correction_revision_log.md').relative_to(ROOT)),
                   'writer_rules': ['Emit only one replace_block per listed target; copy old_hash and correction_ids from this handoff.',
                                    'Preserve every supported component, scientific value, frozen initial system and Route boundary.',
                                    'Do not invent source text or author metadata, strengthen claims, introduce new citations, or write outside scope.',
                                    'Use empty claim_strength_changes and collateral_authorization_ids arrays.',
                                    'No manuscript successor, author-approval sidecar, apply, matrix or audit output; those are orchestrator work.',
                                    'Replacement text must not contain block markers. Keep existing citation convention and honest source-locator boundaries.']}
        outputs[issue_path] = issue_raw
        outputs[notes / 'stage4_5_round2_correction_writer_handoff.json'] = encoded(handoff)
    for path in outputs:
        assert not path.exists(), f'refusing overwrite {path}'
    return outputs


if __name__ == '__main__':
    outputs = prepare()
    # Emit an apply_patch payload; the caller uses its file-editing tool.
    print('*** Begin Patch')
    for path, raw in outputs.items():
        print('*** Add File: ' + str(path))
        for line in raw.decode().splitlines():
            print('+' + line)
    print('*** End Patch')
