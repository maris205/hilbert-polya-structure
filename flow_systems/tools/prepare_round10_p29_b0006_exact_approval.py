#!/usr/bin/env python3
"""Validate one unapplied P29 proposal and emit its exact approval package.

The current confirmation is scope/preparation only. This script does not build
author authority, apply a patch, generate a successor, or run a fresh audit.
"""
import datetime
import difflib
import hashlib
import json
from pathlib import Path
import runpy
import sys

ROOT = Path(__file__).resolve().parents[1]
ARS = Path('/root/autodl-tmp/.codex/plugins/cache/ars-codex/ars-codex/0.1.28/skills/academic-research-suite/ars')
NOTES = ROOT / 'papers/29-bianchi-ideal-owner-refinement/notes'
PREFIX = 'BATCH_ROUND10_P29_B0006_'


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def encode(value):
    return (json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + '\n').encode('utf-8')


def desc(path, raw=None):
    raw = path.read_bytes() if raw is None else raw
    return {'path': str(path.relative_to(ROOT)) if path.is_relative_to(ROOT) else str(path), 'sha256': sha(raw), 'bytes': len(raw)}


def verify(binding):
    assert desc(ROOT / binding['path']) == binding, binding['path']


def main():
    sys.path.insert(0, str(ARS / 'scripts'))
    import _block_parser as bp
    import ars_apply_revision_patch as ap
    import revision_roadmap as rr
    handoff_path = NOTES / 'stage4_5_round3_preflight_b0006_writer_handoff.json'
    handoff = json.loads(handoff_path.read_bytes())
    for key in ('base_draft', 'base_block_manifest', 'issue_list', 'source_finding', 'scope_author_event', 'scope_record', 'prior_bundle'):
        verify(handoff[key])
    assert handoff['source_finding']['sha256'] == '611cd9840ff68bc8becb75b8f0f0dcb36f3a6c072ab892eae18ad8f67327d351'
    assert (ROOT / handoff['scope_author_event']['path']).read_bytes() == '确认\n'.encode()
    base_path = ROOT / handoff['base_draft']['path']
    base_raw = base_path.read_bytes()
    parsed = bp.parse_document(base_raw.decode('utf-8'))
    manifest = json.loads((ROOT / handoff['base_block_manifest']['path']).read_bytes())
    assert [(r['block_id'], r['old_hash']) for r in manifest['blocks']] == [(b.block_id, b.norm_hash) for b in parsed.blocks]
    issue_raw = (ROOT / handoff['issue_list']['path']).read_bytes()
    issue = json.loads(issue_raw)
    rr.validate_integrity_correction_list(issue, issue_list_raw=issue_raw, base_raw=base_raw)
    assert issue['revision_round'] == 5
    assert len(issue['issues']) == 1 and issue['issues'][0]['correction_id'] == 'IL-MEDIUM-1'
    assert issue['issues'][0]['proposed_targets'] == [{'block_id': 'B0006', 'allowed_operations': ['replace_block']}]
    patch_path = ROOT / handoff['patch_output']
    patch = json.loads(patch_path.read_bytes())
    target = handoff['target']
    expected_op = {key: target[key] for key in ('op', 'block_id', 'old_hash', 'roadmap_item_ids', 'claim_strength_changes', 'collateral_authorization_ids')}
    expected_op['new_text'] = target['required_new_text']
    assert patch == {**handoff['patch_header'], 'ops': [expected_op]}
    block = parsed.block_by_id()['B0006']
    assert block.normalized_text == target['old_text'] and block.norm_hash == target['old_hash']
    old, new = target['exact_old_sentence'], target['exact_new_sentence']
    assert base_raw.count(old.encode()) == block.normalized_text.count(old) == 1
    assert new not in base_raw.decode('utf-8')
    assert expected_op['new_text'] == block.normalized_text.replace(old, new, 1)
    assert expected_op['new_text'].replace(new, old, 1) == block.normalized_text
    prospective_raw = base_raw.replace(old.encode(), new.encode(), 1)
    assert prospective_raw.replace(new.encode(), old.encode(), 1) == base_raw
    analysis = ap.validate_patch(patch, base_raw, parsed, touched_ratio_threshold=0.6)
    assert not analysis['structural_flags']['any'], analysis['structural_flags']
    assert not (ROOT / handoff['future_successor_not_authorized_yet']).exists()
    assert not (ROOT / handoff['future_bundle_not_authorized_yet']).exists()
    preview_path = ROOT / 'BATCH_ROUND10_STAGE4_5_ROUND2_EXACT_PATCH_PREVIEW_COMPLETION_RECEIPT.json'
    assert desc(preview_path)['sha256'] == 'ee274e901481b2dc675023c5e6135af775c2abf2700c7babaea8608eb55bac40'
    previews = json.loads(preview_path.read_bytes())
    for paper in previews['papers']:
        for key in ('draft', 'build_receipt', 'preview'):
            verify(paper[key])
    for paper in previews['derived_materials']:
        for binding in [paper['producer_receipt'], *paper['materials']]:
            verify(binding)
    helpers = runpy.run_path(str(ROOT / 'tools/finalize_round10_stage4_5_round2.py'), run_name='read_only_boundary_helpers')
    boundary = helpers['protected_boundary_replay']()
    stamp = datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0).isoformat().replace('+00:00', 'Z')
    diff_path = ROOT / (PREFIX + 'EXACT_PATCH_REVIEW.diff')
    diff_raw = ''.join(difflib.unified_diff([line+'\n' for line in target['old_text'].splitlines()], [line+'\n' for line in expected_op['new_text'].splitlines()], fromfile='P29/B0006/current-round4', tofile='P29/B0006/proposed-round5')).encode()
    reading_path = ROOT / (PREFIX + 'PREAPPLICATION_READING.md')
    assert desc(patch_path)['sha256'] in reading_path.read_text()
    validation_path = ROOT / (PREFIX + 'PREAPPLICATION_VALIDATION.json')
    validation = {
        'schema_version': 'round10-p29-b0006-preapplication-validation/1.0', 'generated_at_utc': stamp,
        'status': 'PROPOSAL_SCHEMA_HASH_SCOPE_PASS_NOT_APPLIED_NOT_INTEGRITY_PASS',
        'tool': desc(Path(__file__).resolve()),
        'official_tools': [desc(ARS / 'scripts' / name) for name in ('_block_parser.py', 'revision_roadmap.py', 'ars_apply_revision_patch.py')],
        'handoff': desc(handoff_path), 'issue_list': handoff['issue_list'], 'patch': desc(patch_path),
        'official_issue_list_validation': 'PASS', 'official_patch_phase1_validation': 'PASS',
        'structural_flags': analysis['structural_flags'], 'base_block_count': len(parsed.blocks),
        'proposed_touched_blocks': ['B0006'], 'exact_single_sentence_replacement': True,
        'old_sentence_bytes': len(old.encode()), 'new_sentence_bytes': len(new.encode()),
        'prospective_in_memory_only_draft_sha256': sha(prospective_raw),
        'prospective_in_memory_only_draft_bytes': len(prospective_raw),
        'reversal_reproduces_base_bytes': True,
        'semantic_cross_reading': desc(reading_path), 'review_diff': desc(diff_path, diff_raw),
        'prior_five_preview_snapshot': desc(preview_path), 'five_previews_and_derived_materials_unchanged': True,
        'protected_boundary': {'locked_file_bindings_replayed': boundary['locked_file_bindings_replayed'], 'changed_protected_files': boundary['changed_protected_files'], 'canonical_file_count': len(boundary['protected_canonical_files']), 'science_tree_count': len(boundary['science_trees']), 'readme_status_file_count': len(boundary['read_only_files'])},
        'official_authorization_build_run': False, 'patch_applied': False, 'preview_built': False, 'fresh_stage4_5_round3_run': False,
        'scope_limit': 'Read-only proposal checks and local semantic reading; neither official author authority nor a scientific/integrity PASS. The local preflight is not a completed third audit.'
    }
    validation_raw = encode(validation)
    request_path = ROOT / (PREFIX + 'EXACT_PATCH_APPROVAL_REQUEST.json')
    request = {
        'schema_version': 'round10-p29-b0006-exact-patch-approval-request/1.0', 'generated_at_utc': stamp,
        'status': 'AWAITING_AUTHOR_CONFIRMATION_OF_EXACT_PATCH_NOT_APPLIED',
        'scope_record': handoff['scope_record'], 'scope_event': handoff['scope_author_event'], 'source_finding': handoff['source_finding'],
        'base_draft': handoff['base_draft'], 'base_block_manifest': handoff['base_block_manifest'], 'prior_bundle': handoff['prior_bundle'],
        'issue_list': handoff['issue_list'], 'patch': desc(patch_path), 'revision_log': desc(ROOT / handoff['revision_log_output']),
        'preapplication_validation': desc(validation_path, validation_raw), 'review_diff': desc(diff_path, diff_raw),
        'exact_old_sentence': old, 'exact_new_sentence': new,
        'proposed_author_decisions_not_yet_collected': [{'correction_id': 'IL-MEDIUM-1', 'decision_if_confirmed': 'authorize', 'authorized_targets_if_confirmed': [{'block_id': 'B0006', 'allowed_operations': ['replace_block']}]}],
        'named_successor': handoff['future_successor_not_authorized_yet'], 'named_successor_bundle': handoff['future_bundle_not_authorized_yet'],
        'allowed_after_exact_approval': ['Record the actual new author event and build official integrity authorization input/sidecar bound to this exact patch.', 'Officially apply only P29 B0006 to the named round5 successor; emit its exact apply report, new block manifest and continuous round5 revision-evidence bundle.', 'Create a versioned P29-only notes preview builder bound to the actual new application receipt, using the existing strict five-zero diagnostic criteria and no-shell-escape; preserve all existing PDFs, receipts and builders. Emit the round5 PDF, build log/transcript and build receipt under notes.', 'After P29 preview and chain verification pass, perform the previously authorized fresh Stage4.5 Round3 for the actual current five manuscripts, then stop at its mandatory checkpoint.'],
        'explicitly_forbidden': ['Edit any other P29 sentence or block, bibliography entry, source matrix, ClaimIntent manifest, or P30--P33 manuscript.', 'Overwrite any existing approved patch, draft, preview, bundle, old audit or failed build history.', 'New scientific code/experiment/result execution or refresh, stronger scientific claims, initial-system or Route changes.', 'Canonical/submission promotion, README/status changes, Git commit/push/sync, Stage5/6.'],
        'mandatory_stop_conditions': ['Any artifact/hash/target mismatch.', 'Any failed official validator, independent replay, or isolated build.', 'Any structural change or need for a further out-of-scope edit.', 'Any scientific-value, initial-system, Route or claim-strengthening change.'],
        'decision_rule': 'The next unqualified author confirmation after this exact request and patch SHA are presented approves only these exact patch bytes and the one listed correction decision/target/operation, plus the explicitly bounded post-approval continuation. Any changed patch requires new approval. This request itself is not author input or an authorization sidecar.',
        'current_batch': 'Round10 P29--P33, five papers; not a new batch',
        'revision_round_vs_audit_round': 'P29 prospective revision round5 is a write-chain index; fresh integrity Stage4.5 Round3 has not begun.'
    }
    request_raw = encode(request)
    md = f'''# P29 B0006：单块精确补丁确认

单块补丁已准备并通过只读格式、基稿/块绑定和精确单句替换检查；尚未应用、未生成 round5 正文或 PDF，未运行 fresh Stage4.5 Round3。

[完整 patch 字节]({request['patch']['path']})，SHA-256 `{request['patch']['sha256']}`，{request['patch']['bytes']} bytes。

[机器确认请求]({request_path.name})，SHA-256 `{sha(request_raw)}`。请求中的唯一决定为 `IL-MEDIUM-1 / authorize / B0006 / replace_block`。

拟句：

> {new}

只替换此前列明的那一句，其余 B0006 和其余 {len(parsed.blocks)-1} 个块不在修改范围内。[完整块差异]({diff_path.name})；[前置检查]({validation_path.name})；[语义阅读]({reading_path.name})。

收到你对这份具体补丁的“确认”后，才构建官方授权并应用到 `stage4_prime_revision_round5.tex`，接续完整 bundle，复验 P29 新预览，再执行原五篇 fresh Stage4.5 Round3 并停在其检查点。保留其他四篇现有稿与预览，不扩大修改范围。

仍是 Round10 五篇和 Route A 原限定；不做科学执行、canonical 晋升、README/status/Git 或 Stage5/6。上一条“确认”只批准准备范围，未被追认为这份新 patch SHA 的批准。ARS 的精确补丁确认规则要求当前这一步作者确认；技术前检 PASS 不是完整性 PASS。
'''
    outputs = {diff_path: diff_raw, validation_path: validation_raw, request_path: request_raw, ROOT / (PREFIX + 'EXACT_PATCH_APPROVAL_REQUEST.md'): md.encode()}
    for path in outputs:
        assert not path.exists(), f'refusing overwrite {path}'
    print('*** Begin Patch')
    for path, raw in outputs.items():
        print('*** Add File: ' + str(path))
        for line in raw.decode('utf-8').splitlines():
            print('+' + line)
    print('*** End Patch')


if __name__ == '__main__':
    main()
