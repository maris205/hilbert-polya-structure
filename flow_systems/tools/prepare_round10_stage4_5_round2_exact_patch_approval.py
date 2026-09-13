#!/usr/bin/env python3
"""Read-only patch checks; emit a review/approval package, never apply a patch.

The CLI prints an apply_patch payload. No author decision is fabricated, and
neither a manuscript successor nor an official apply sidecar is generated.
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
SCOPE = ROOT / 'BATCH_ROUND10_STAGE4_5_ROUND2_CORRECTION_AUTHORIZATION_REQUEST.json'
SCOPE_SHA = 'd9be18e2199dd64100a1482018eb9bf77586e2548ba751cc0c2b57e06195f992'
PREFIX = 'BATCH_ROUND10_STAGE4_5_ROUND2_'


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def encoded(obj):
    return (json.dumps(obj, ensure_ascii=False, indent=2, sort_keys=True) + '\n').encode()


def desc(path, raw=None):
    if raw is None:
        raw = path.read_bytes()
    return {'path': str(path.relative_to(ROOT)), 'sha256': sha(raw), 'bytes': len(raw)}


def verify(row):
    assert desc(ROOT / row['path']) == row, row['path']


def prepare():
    assert sha(SCOPE.read_bytes()) == SCOPE_SHA
    scope = json.loads(SCOPE.read_bytes())
    sys.path.insert(0, str(ARS / 'scripts'))
    import _block_parser as bp
    import ars_apply_revision_patch as ap
    import revision_roadmap as rr
    finalizer = runpy.run_path(str(ROOT / 'tools/finalize_round10_stage4_5_round2.py'), run_name='read_only_boundary_helpers')
    protected = finalizer['protected_boundary_replay']()
    stamp = datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0).isoformat().replace('+00:00', 'Z')
    papers, checks, diffs = [], [], []
    for p in scope['papers']:
        for key in ('base_draft', 'base_block_manifest', 'stage4_5_blocker_source'):
            verify(p[key])
        base = ROOT / p['base_draft']['path']
        notes = base.parent
        handoff_path = notes / 'stage4_5_round2_correction_writer_handoff.json'
        h = json.loads(handoff_path.read_bytes())
        verify(h['scope_confirmation'])
        verify(h['issue_list'])
        for row in h['source_materials']:
            verify(row)
        patch_path = ROOT / h['patch_output']
        log_path = ROOT / h['log_output']
        patch = json.loads(patch_path.read_bytes())
        issue_raw = (ROOT / h['issue_list']['path']).read_bytes()
        issues = json.loads(issue_raw)
        rr.validate_integrity_correction_list(issues, issue_list_raw=issue_raw, base_raw=base.read_bytes())
        assert {k: patch[k] for k in h['patch_header']} == h['patch_header']
        targets = {t['block_id']: t for t in h['targets']}
        assert len(patch['ops']) == len(targets) == p['target_count']
        assert {o['block_id'] for o in patch['ops']} == set(targets)
        assert [dict((k, t[k]) for k in original) for t, original in zip(h['targets'], p['targets'])] == p['targets']
        for op in patch['ops']:
            target = targets[op['block_id']]
            assert op['op'] == 'replace_block' and op['op'] in target['allowed_operations']
            assert op['old_hash'] == target['manifest_old_hash_prefix_12']
            assert op['roadmap_item_ids'] == target['correction_ids']
            assert op['claim_strength_changes'] == [] and op['collateral_authorization_ids'] == []
            assert op['new_text'] != target['old_text']
            diffs.extend(difflib.unified_diff([line+'\n' for line in target['old_text'].splitlines()], [line+'\n' for line in op['new_text'].splitlines()], fromfile=p['paper_id']+'/'+op['block_id']+'/frozen', tofile=p['paper_id']+'/'+op['block_id']+'/proposed'))
            diffs.append('\n')
        analysis = ap.validate_patch(patch, base.read_bytes(), bp.parse_document(base.read_text()), touched_ratio_threshold=0.6)
        assert not analysis['structural_flags']['any'], analysis['structural_flags']
        assert not (ROOT / p['proposed_successor_draft']).exists()
        papers.append({'paper_id': p['paper_id'], 'base_draft': p['base_draft'], 'base_block_manifest': p['base_block_manifest'], 'issue_list': h['issue_list'], 'patch': desc(patch_path), 'revision_log': desc(log_path), 'writer_handoff': desc(handoff_path), 'proposed_successor_draft': p['proposed_successor_draft'], 'proposed_author_decisions_not_yet_collected': [{'correction_id': issue['correction_id'], 'decision_if_confirmed': 'authorize', 'authorized_targets_if_confirmed': issue['proposed_targets']} for issue in issues['issues']], 'target_count': len(patch['ops']), 'issue_count': len(issues['issues'])})
        checks.append({'paper_id': p['paper_id'], 'official_issue_list_validation': 'PASS', 'official_patch_phase1_validation': 'PASS', 'exact_target_and_operation_binding': 'PASS', 'source_descriptor_binding': 'PASS', 'counters': analysis['counters_base'], 'structural_flags': analysis['structural_flags'], 'official_authority_validation_run': False, 'patch_applied': False})
    assert sum(p['target_count'] for p in papers) == 66
    assert sum(p['issue_count'] for p in papers) == 17
    bib_path = ROOT / 'papers/30-three-disk-nonconstant-roof-determinant/notes/stage4_5_round2_correction_bib_proposal.json'
    bib = json.loads(bib_path.read_bytes())
    assert bib['operation'] == scope['bibliography_operation']
    operation = bib['operation']
    verify(operation['base_artifact'])
    raw = (ROOT / operation['base_artifact']['path']).read_bytes()
    old = finalizer['extract_bib_entry'](raw, operation['entry_key'])
    assert old.decode() == bib['old_entry'] and sha(old) == operation['expected_current_entry_sha256']
    field = operation['exact_field_change']
    assert old.count(field['old_companion_doi'].encode()) == 1
    new = old.replace(field['old_companion_doi'].encode(), field['new_companion_doi'].encode())
    assert new.decode() == bib['new_entry'] and sha(new) == bib['new_entry_sha256']
    proposed_bib = raw.replace(old, new, 1)
    assert sha(proposed_bib) == bib['proposed_successor_sha256'] and len(proposed_bib) == bib['proposed_successor_bytes']
    for key in ('P30-C01', 'P30-C02', 'P30-S01', 'P30-S03'):
        assert finalizer['extract_bib_entry'](raw, key) == finalizer['extract_bib_entry'](proposed_bib, key)
    assert not (ROOT / operation['proposed_successor']).exists()
    diffs.extend(difflib.unified_diff([line+'\n' for line in old.decode().splitlines()], [line+'\n' for line in new.decode().splitlines()], fromfile='P30-S02/frozen-bib-entry', tofile='P30-S02/proposed-bib-entry'))
    diff_path = ROOT / (PREFIX + 'EXACT_PATCH_REVIEW.diff')
    diff_raw = ''.join(diffs).encode()
    receipt_path = ROOT / (PREFIX + 'PATCH_PREAPPLICATION_VALIDATION.json')
    receipt = {'schema_version': 'round10-patch-preapplication-validation/1.0', 'generated_at_utc': stamp, 'status': 'PREAPPLICATION_SCHEMA_HASH_SCOPE_CHECKS_PASS_NOT_INTEGRITY_PASS', 'tool': desc(Path(__file__).resolve()), 'official_tools': [desc_external(ARS / 'scripts' / name) for name in ('ars_apply_revision_patch.py', 'revision_roadmap.py', '_block_parser.py')], 'scope': desc(SCOPE), 'papers': checks, 'bibliography_proposal': desc(bib_path), 'bib_single_substitution_and_other_bytes_unchanged': True, 'protected_boundary_replay': protected, 'review_diff': desc(diff_path, diff_raw), 'not_performed': ['author approval of actual patch bytes', 'official integrity authorization build/apply', 'successor manuscript or bibliography emission', 'isolated preview build', 'Stage 4.5 Round 3 integrity audit', 'new scientific execution', 'canonical/README/status/Git mutation'], 'semantic_limit': 'These deterministic checks do not establish scientific validity, source support, claim correctness, or final integrity eligibility. All five last completed Round-2 integrity dispositions remain FAIL.'}
    reading_path = ROOT / (PREFIX + 'PATCH_PREAPPLICATION_READING_NOTES.md')
    reading_text = reading_path.read_text()
    assert all(p['patch']['sha256'] in reading_text for p in papers)
    receipt['role_separated_reading_notes_not_integrity_verdict'] = desc(reading_path)
    receipt_raw = encoded(receipt)
    request_path = ROOT / (PREFIX + 'EXACT_PATCH_APPROVAL_REQUEST.json')
    request = {'schema_version': 'round10-exact-patch-approval-request/1.0', 'generated_at_utc': stamp, 'status': 'AWAITING_AUTHOR_APPROVAL_OF_EXACT_PATCH_BYTES_NOT_APPLIED', 'scope_request': desc(SCOPE), 'scope_confirmation': desc(ROOT / (PREFIX + 'CORRECTION_SCOPE_AUTHORIZATION_RECEIPT.json')), 'preapplication_validation': desc(receipt_path, receipt_raw), 'review_diff': desc(diff_path, diff_raw), 'papers': papers, 'bibliography_proposal': desc(bib_path), 'aggregate': scope['aggregate'], 'allowed_derived_operations_after_author_approval': scope['allowed_derived_operations'], 'explicitly_forbidden': scope['explicitly_forbidden'], 'mandatory_stop_conditions': scope['mandatory_stop_conditions'], 'decision_rule': 'The next unqualified author confirmation after this exact request SHA is presented approves exactly the five linked patch byte streams (by their full SHA-256), each listed correction decision and target/operation subset, and the exact linked successor-Bib proposal. This request is a proposal, not an author-input or authorization sidecar. A changed patch requires a new approval.', 'next_execution': 'Only after the author confirmation: record that actual event, build schema-valid per-paper integrity authorization inputs and sidecars, officially apply the approved patches to the named successors, emit only already scoped derived artifacts and isolated previews, then perform the authorized fresh Stage 4.5 Round 3 audit and stop at its checkpoint. No Stage 5 or 6, canonical promotion or Git synchronization.'}
    request['retained_reading_cautions'] = desc(reading_path)
    request_raw = encoded(request)
    md = ['# Round 10：五篇精确补丁统一确认包', '', '状态：补丁已准备并通过只读格式、哈希和范围检查，**尚未应用，尚未进行新一轮完整性审计**。仍为 P29–P33 这五篇，不开启新批次。', '', f'机器请求：[{request_path.name}]({request_path.name})', '', f'SHA-256：`{sha(request_raw)}`；{len(request_raw)} bytes。', '', '回复一次“确认”，将批准下列五份具体补丁字节及各问题的列明目标/操作，以及一处精确 Bib 更正；不需要手工抄写哈希或长授权文本。', '', '| 论文 | 正文替换块 | 精确补丁 SHA-256 |', '| --- | ---: | --- |']
    for p in papers:
        md.append(f"| [{p['paper_id']}]({p['patch']['path']}) | {p['target_count']} | `{p['patch']['sha256']}` |")
    md += ['', f"P30 的 [Bib 更正提案]({bib['operation']['base_artifact']['path'].rsplit('/', 1)[0]}/stage4_5_round2_correction_bib_proposal.json)：仅将 P30-S02 的 note 字段纠正 DOI 从 `10.1063/1.457669` 改为 `10.1063/1.457672`；P30-C01→S01 与 P30-C02→S03 不变。提案 SHA-256 `{sha(bib_path.read_bytes())}`。", '', f'[逐块原文/拟文差异]({diff_path.name})；[只读前置验证回执]({receipt_path.name})。五份 patch 文件包含待批准的完整 new_text；未生成后继稿或 PDF，不将提案当成已落地论文。', '', '主要修订内容：', '', '- P29：纠正翻译状态，保留有支持的设计内容，撤回锁内缺少原始载体的完成性表述。', '- P30：更正引用关系和五席评审描述，区分已完成旧审计与未验证的新修订，收窄未支撑的理论归属和 AI 历史表述。', '- P31：撤回未核验的方法迁移与过宽的文献否定，明确旧 reader manifest 的绑定失效。', '- P32：纠正翻译状态；将原文未绑定的 closest-work 对照限定为候选比较假设。B0018 与未改 B0132 表须连读。', '- P33：将无原文支持的引用收窄为阅读候选；同源合成测试的 14/14 仅保留为运行诊断，不充当正确性或独立验证证据。B0037 与未改 B0127 比较段须连读。', '', '确认后只在原有授权边界内执行官方 apply、列明的衍生矩阵/reader manifest、隔离预览和 Stage 4.5 Round 3，再停在其检查点。当前 Route A、五个初始动力学系统、canonical 稿件、科学代码与结果、README/status 均保持冻结；不执行 Git 同步，不进入 Stage 5/6。', '', '依 ARS academic-research-suite 的 revision_patch_protocol，范围确认不能替代具体 patch SHA 的作者确认；本包不包含伪造的作者输入或授权 PASS。五篇上一轮完整性结果仍是 FAIL，前置机械检查通过不是论文通过。', '']
    md += [f'[提交前阅读注意]({reading_path.name}) 保留了尚需复验的语境问题：P29 繁中摘要的非状态句按精确授权保持原文，其范围仍有跨语言歧义；B0109 仍是历史 Round-1 状态说明。当前请求明确披露最新 Round-2 FAIL，不把这些问题记成已解决，也不据此暗增改写权限。', '']
    outputs = {diff_path: diff_raw, receipt_path: receipt_raw, request_path: request_raw, ROOT / (PREFIX + 'EXACT_PATCH_APPROVAL_REQUEST.md'): '\n'.join(md).encode()}
    for path in outputs:
        assert not path.exists(), f'refusing overwrite {path}'
    return outputs


def desc_external(path):
    raw = path.read_bytes()
    return {'path': str(path), 'sha256': sha(raw), 'bytes': len(raw)}


if __name__ == '__main__':
    outputs = prepare()
    print('*** Begin Patch')
    for path, raw in outputs.items():
        print('*** Add File: ' + str(path))
        for line in raw.decode().splitlines():
            print('+' + line)
    print('*** End Patch')
