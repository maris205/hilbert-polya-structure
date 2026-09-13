#!/usr/bin/env python3
"""Transcribe the actual latest author event; use ARS's exact-patch builder.

Outputs are emitted as apply_patch input. No draft is applied by this helper.
"""
import datetime
import hashlib
import json
from pathlib import Path
import runpy
import sys

ROOT = Path(__file__).resolve().parents[1]
ARS = Path('/root/autodl-tmp/.codex/plugins/cache/ars-codex/ars-codex/0.1.28/skills/academic-research-suite/ars')
PREFIX = 'BATCH_ROUND10_STAGE4_5_ROUND2_EXACT_PATCH_'
REQUEST = ROOT / (PREFIX + 'APPROVAL_REQUEST.json')
REQUEST_SHA = '759480e724b818c5068233134712a14a4736df116ca295578495912f3a86a42d'
EVENT_ID = 'AUTHOR-EVENT-R10-S45R2-EXACT-PATCH-CONFIRM-20260905'


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def encoded(obj):
    return (json.dumps(obj, ensure_ascii=False, indent=2, sort_keys=True) + '\n').encode()


def desc(path, raw=None):
    raw = path.read_bytes() if raw is None else raw
    return {'path': str(path.relative_to(ROOT)), 'sha256': sha(raw), 'bytes': len(raw)}


def verify(row):
    assert desc(ROOT / row['path']) == row, row['path']


def prepare():
    assert sha(REQUEST.read_bytes()) == REQUEST_SHA
    request = json.loads(REQUEST.read_bytes())
    sys.path.insert(0, str(ARS / 'scripts'))
    import revision_roadmap as rr
    stamp = datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0).isoformat().replace('+00:00', 'Z')
    event_path = ROOT / (PREFIX + 'AUTHOR_EVENT_20260905.txt')
    record_path = ROOT / (PREFIX + 'AUTHORIZATION_RECORD.md')
    assert event_path.read_bytes() == '确认\n'.encode()
    assert REQUEST_SHA in record_path.read_text()
    event = {'event_id': EVENT_ID, 'source': 'explicit_session_user_message', 'actor_role': 'author', 'input_sha256': sha(event_path.read_bytes())}
    for key in ('scope_request', 'scope_confirmation', 'preapplication_validation', 'review_diff', 'bibliography_proposal', 'retained_reading_cautions'):
        verify(request[key])
    outputs, rows = {}, []
    for p in request['papers']:
        for key in ('base_draft', 'base_block_manifest', 'issue_list', 'patch', 'revision_log', 'writer_handoff'):
            verify(p[key])
        assert not (ROOT / p['proposed_successor_draft']).exists()
        base_raw = (ROOT / p['base_draft']['path']).read_bytes()
        patch_raw = (ROOT / p['patch']['path']).read_bytes()
        patch = json.loads(patch_raw)
        issue_raw = (ROOT / p['issue_list']['path']).read_bytes()
        issues = json.loads(issue_raw)
        decisions = [{'correction_id': d['correction_id'], 'author_event_id': EVENT_ID, 'decision': d['decision_if_confirmed'], 'authorized_targets': d['authorized_targets_if_confirmed']} for d in p['proposed_author_decisions_not_yet_collected']]
        assert all(d['decision'] == 'authorize' for d in decisions)
        author_input = {'schema_version': 'integrity-correction-authorization-input/1.0', 'revision_patch_sha256': p['patch']['sha256'], 'author_events': [event], 'author_decisions': decisions}
        authorization = rr.build_integrity_authorization(author_input, issue_list=issues, issue_list_raw=issue_raw, patch=patch, patch_raw=patch_raw, base_raw=base_raw)
        input_raw, auth_raw = encoded(author_input), encoded(authorization)
        witness = rr.validate_integrity_patch_authorization(patch, patch_raw=patch_raw, base_raw=base_raw, issue_list=issues, issue_list_raw=issue_raw, integrity_authorization=authorization, integrity_authorization_raw=auth_raw)
        assert witness['status'] == 'pass'
        notes = (ROOT / p['base_draft']['path']).parent
        input_path = notes / 'stage4_5_round2_correction_author_input.json'
        auth_path = notes / 'stage4_5_round2_correction_integrity_authorization.json'
        outputs[input_path], outputs[auth_path] = input_raw, auth_raw
        rows.append({**p, 'author_input': desc(input_path, input_raw), 'integrity_authorization': desc(auth_path, auth_raw), 'official_authorization_witness': witness})
    finalizer = runpy.run_path(str(ROOT / 'tools/finalize_round10_stage4_5_round2.py'), run_name='read_only_boundary_helpers')
    protected = finalizer['protected_boundary_replay']()
    receipt = {'schema_version': 'round10-exact-patch-author-approval-receipt/1.0', 'recorded_at_utc': stamp, 'status': 'AUTHOR_CONFIRMED_EXACT_BYTES_OFFICIAL_AUTHORITY_VALIDATED_NOT_APPLIED', 'confirmed_request': desc(REQUEST), 'raw_author_event': desc(event_path), 'author_event_id': EVENT_ID, 'authorization_record': desc(record_path), 'producer': desc(Path(__file__).resolve()), 'official_builder': {'path': str(ARS / 'scripts/revision_roadmap.py'), 'sha256': sha((ARS / 'scripts/revision_roadmap.py').read_bytes())}, 'papers': rows, 'bibliography_proposal': request['bibliography_proposal'], 'aggregate': request['aggregate'], 'protected_boundary_replay': protected, 'allowed_derived_operations': request['allowed_derived_operations_after_author_approval'], 'explicitly_forbidden': request['explicitly_forbidden'], 'mandatory_stop_conditions': request['mandatory_stop_conditions'], 'scientific_integrity_status': 'LAST_COMPLETED_ROUND2_FAIL_ALL_FIVE_NO_STAGE5_ELIGIBILITY', 'patch_applied': False}
    outputs[ROOT / (PREFIX + 'AUTHORIZATION_RECEIPT.json')] = encoded(receipt)
    for path in outputs:
        assert not path.exists(), f'refusing overwrite {path}'
    return outputs


if __name__ == '__main__':
    outputs = prepare()
    print('*** Begin Patch')
    for path, raw in outputs.items():
        print('*** Add File: ' + str(path))
        for line in raw.decode().splitlines():
            print('+' + line)
    print('*** End Patch')
