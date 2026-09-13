#!/usr/bin/env python3
"""Read-only preview/derived binding checks; emit an append-only receipt patch.

This is not an integrity validator or a scientific-result replay. No build,
manuscript mutation, source retrieval, or prior receipt update is performed.
"""
import datetime
import hashlib
import json
from pathlib import Path
import re
import runpy

ROOT = Path(__file__).resolve().parents[1]
PREFIX = 'BATCH_ROUND10_STAGE4_5_ROUND2_'


def desc(path):
    path = ROOT / path
    raw = path.read_bytes()
    return {'path': str(path.relative_to(ROOT)), 'sha256': hashlib.sha256(raw).hexdigest(), 'bytes': len(raw)}


def read(path):
    return json.loads((ROOT / path).read_bytes())


def verify(binding):
    assert desc(binding['path']) == binding, binding['path']


def main():
    application = read(PREFIX + 'EXACT_PATCH_APPLICATION_RECEIPT.json')
    verify(application['authority'])
    request_path = PREFIX + 'P32_PREVIEW_RECOVERY_REQUEST.json'
    request = read(request_path)
    assert desc(request_path)['sha256'] == '78aeff4125881c496c65352a023b567649ffcff239f2a2610c39e54714258b08'
    for key in ('base_builder', 'trigger', 'already_completed_application', 'prior_exact_authority', 'approved_draft_to_keep_byte_identical', 'approved_patch_to_keep_byte_identical'):
        verify(request[key])
    prior_failure = read(request['trigger']['path'])
    assert prior_failure['status'] == 'FAIL'
    for key in ('final_latex_log', 'transcript'):
        verify(prior_failure[key])
    assert prior_failure['diagnostics']['overfull_hboxes'] == 1
    lock = read(PREFIX + 'INPUT_LOCK.json')
    papers = []
    for paper in application['papers']:
        for key in ('successor', 'approved_patch', 'apply_report', 'revision_evidence_bundle', 'block_manifest', 'integrity_authorization'):
            verify(paper[key])
        source = Path(paper['successor']['path'])
        job = source.stem + ('_preview_attempt2' if paper['paper_id'] == 'P32' else '')
        receipt_path = source.parent / (job + '_build_receipt.json')
        receipt = read(receipt_path)
        assert receipt['status'] == 'PASS_CLEAN'
        assert receipt['input_draft'] == paper['successor']
        assert receipt['revision_evidence_bundle'] == paper['revision_evidence_bundle']
        assert receipt['application_receipt'] == desc(PREFIX + 'EXACT_PATCH_APPLICATION_RECEIPT.json')
        assert receipt['protected_snapshot_unchanged'] is True
        assert receipt['protected_locked_bindings'] == 119
        assert receipt['pages'] > 0
        assert not any(receipt['diagnostics'].values())
        assert all(command['exit_code'] == 0 for command in receipt['commands'])
        for key in ('authority', 'application_receipt', 'builder', 'input_draft', 'bibliography', 'revision_evidence_bundle', 'preview', 'final_latex_log', 'transcript'):
            verify(receipt[key])
        bib = application['bib_successor'] if paper['paper_id'] == 'P30' else next(row for row in lock['papers'] if row['paper_id'] == paper['paper_id'])['audit_bibliography']
        assert receipt['bibliography'] == bib
        working_raw = (ROOT / source).read_bytes()
        expected = re.sub(r'(?m)^<!--block:B\d+-->\r?\n?', '', working_raw.decode('utf-8'))
        if paper['paper_id'] == 'P32':
            transform = request['proposed_preview_only_transform']
            old, new = transform['exact_source_fragment'], transform['proposed_compile_fragment']
            assert expected.count(old) == 1
            assert new.count(transform['inserted_token']) == 115
            assert new.replace(transform['inserted_token'], '') == old
            expected = expected.replace(old, new, 1)
            assert receipt['preview_only_recovery']['exact_fragment_reversal_checked'] is True
            for key in ('authorization', 'confirmed_request', 'original_builder_preserved'):
                verify(receipt['preview_only_recovery'][key])
        compile_source = Path(receipt['temporary_compile_directory']) / 'manuscript.tex'
        assert compile_source.read_bytes() == expected.encode('utf-8')
        assert hashlib.sha256(compile_source.read_bytes()).hexdigest() == receipt['compile_source_sha256']
        papers.append({'paper_id': paper['paper_id'], 'draft': paper['successor'], 'build_receipt': desc(receipt_path), 'preview': receipt['preview'], 'pages': receipt['pages'], 'diagnostics': receipt['diagnostics'], 'status': receipt['status']})
    derived = []
    names = {'P30': ['stage4_prime_claim_passage_matrix_round3.json'], 'P31': ['stage4_prime_method_passage_matrix_round3.json', 'stage4_prime_reader_artifact_manifest_round3.json'], 'P32': ['stage4_prime_claim_passage_matrix_round4.json'], 'P33': ['stage4_prime_claim_passage_matrix_round3.json']}
    for paper in application['papers']:
        if paper['paper_id'] not in names:
            continue
        notes = Path(paper['successor']['path']).parent
        derived.append({'paper_id': paper['paper_id'], 'materials': [desc(notes / name) for name in names[paper['paper_id']]], 'producer_receipt': desc(notes / 'stage4_5_round2_derived_materials_receipt.json')})
    helper = runpy.run_path(str(ROOT / 'tools/finalize_round10_stage4_5_round2.py'), run_name='read_only_boundary_helpers')
    boundary = helper['protected_boundary_replay']()
    result = {
        'schema_version': 'round10-exact-patch-preview-completion/1.0',
        'generated_at_utc': datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0).isoformat().replace('+00:00', 'Z'),
        'status': 'FIVE_NOTES_PREVIEWS_PASS_CLEAN_NOT_INTEGRITY_PASS',
        'generator': desc(Path(__file__).resolve()),
        'application_receipt': desc(PREFIX + 'EXACT_PATCH_APPLICATION_RECEIPT.json'),
        'recovery_authorization': desc(PREFIX + 'P32_PREVIEW_RECOVERY_AUTHORIZATION_RECEIPT.json'),
        'recovery_request': desc(request_path),
        'prior_p32_failure_preserved': request['trigger'],
        'prior_p32_failed_log_preserved': prior_failure['final_latex_log'],
        'prior_p32_failed_transcript_preserved': prior_failure['transcript'],
        'papers': papers,
        'total_pages': sum(row['pages'] for row in papers),
        'derived_materials': derived,
        'protected_boundary': boundary,
        'scope': 'Actual preview and byte-binding verification only. Derived semantic cross-reading is separately reported; no A--E integrity verdict is produced here.',
        'stage4_5_round3_completed': False,
        'stage5_or_stage6_run': False,
        'canonical_science_route_readme_status_git_mutations': False,
        'same_model_family_cross_reading_is_not_error_independence': True,
    }
    path = ROOT / (PREFIX + 'EXACT_PATCH_PREVIEW_COMPLETION_RECEIPT.json')
    assert not path.exists(), path
    print('*** Begin Patch\n*** Add File: ' + str(path))
    for line in (json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + '\n').splitlines():
        print('+' + line)
    print('*** End Patch')


if __name__ == '__main__':
    main()
