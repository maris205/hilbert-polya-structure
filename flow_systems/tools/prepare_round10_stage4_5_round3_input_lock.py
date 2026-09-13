#!/usr/bin/env python3
"""Inventory immutable Round-3 inputs; print three append-only JSON patches.

This is deliberately not an ARS validator, an integrity audit, a build, a patch
application, or an independent semantic review. It reads existing local bytes
and the pinned protected-boundary helper only. It never writes its outputs.
The orchestrator must review and apply the complete emitted patch separately.
"""

import datetime
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import runpy
import sys


ROOT = Path(__file__).resolve().parents[1]
PREFIX = 'BATCH_ROUND10_STAGE4_5_ROUND2_'
OLD_LOCK = PREFIX + 'INPUT_LOCK.json'
BATCH_APP = PREFIX + 'EXACT_PATCH_APPLICATION_RECEIPT.json'
BATCH_AUTH = PREFIX + 'EXACT_PATCH_AUTHORIZATION_RECEIPT.json'
BATCH_REQUEST = PREFIX + 'EXACT_PATCH_APPROVAL_REQUEST.json'
OLD_COMPLETION = PREFIX + 'EXACT_PATCH_PREVIEW_COMPLETION_RECEIPT.json'
P29_APP = 'BATCH_ROUND10_P29_B0006_APPLICATION_RECEIPT.json'
P29_AUTH = 'BATCH_ROUND10_P29_B0006_EXACT_AUTHORIZATION_RECEIPT.json'
P29_REQUEST = 'BATCH_ROUND10_P29_B0006_EXACT_PATCH_APPROVAL_REQUEST.json'
RECOVERY_AUTH = PREFIX + 'P32_PREVIEW_RECOVERY_AUTHORIZATION_RECEIPT.json'
RECOVERY_REQUEST = PREFIX + 'P32_PREVIEW_RECOVERY_REQUEST.json'
HELPER = 'tools/finalize_round10_stage4_5_round2.py'
NEW_COMPLETION = 'BATCH_ROUND10_P29_B0006_PREVIEW_COMPLETION_RECEIPT.json'
NEW_LOCK = 'BATCH_ROUND10_STAGE4_5_ROUND3_INPUT_LOCK.json'
NEW_REPLAY = 'BATCH_ROUND10_STAGE4_5_ROUND3_INPUT_BINDING_REPLAY.json'
OUTPUTS = (NEW_COMPLETION, NEW_LOCK, NEW_REPLAY)
PINS = {
    OLD_LOCK: '11875bf33e0318997c385d0d89bde3a7987bb9166b18967994ccb3ca5ac44bb0',
    BATCH_APP: '799c3ee37e73a29d562b350a80c2d26ec60499990c781321f5608be2d3c3204f',
    BATCH_AUTH: '3f4e15e8aa07d9c6aa1e24297c19edaab594695f472d6a70c8e4e8ae9512478d',
    BATCH_REQUEST: '759480e724b818c5068233134712a14a4736df116ca295578495912f3a86a42d',
    OLD_COMPLETION: 'ee274e901481b2dc675023c5e6135af775c2abf2700c7babaea8608eb55bac40',
    P29_APP: '5cc36dfea88efead824fea31003e2a80aaa264544d7720a3cc6d119cdaa1bc9a',
    P29_AUTH: 'b00c26caa6853d894ce3871358d77f1424c7061a6fa8f71fca6def125c23f778',
    P29_REQUEST: '87407696aba59cad12c8c0737c69caad2cb6797cea6c9d024fd313206c639d96',
    RECOVERY_AUTH: '92b9eee054597a88fe4edac24eeb1235c809cefce0bf1c039b5acb4e4df8cde1',
    RECOVERY_REQUEST: '78aeff4125881c496c65352a023b567649ffcff239f2a2610c39e54714258b08',
    HELPER: '7396dad339f2cf25b89de32941e95ebcf31c04d42ec0c2f02a661fd8985f732d',
}
# Current files are explicit; no "latest" glob or old-lock draft substitution.
PAPERS = {
    'P29': ('29-bianchi-ideal-owner-refinement', 5,
            '4f43bdbdfcfc3e1a784e1d1641b39cf3c818faa2ef8f5ac8ce613deab4d1726a',
            'stage4_prime_claim_passage_matrix_round3.json',
            'ac253359ce62df4c4f7d8c1143fde92d71918c157c45a68f8a32717d3bc79b71',
            '3514d897b83d618777c886439d06ae332845b72cf7929dfaf90def8976205791', 16),
    'P30': ('30-three-disk-nonconstant-roof-determinant', 4,
            '9a38c81279303ac81a20914d7a2be70056b6c7b568eef2640ebe3665d54399de',
            'stage4_prime_claim_passage_matrix_round3.json',
            'd62c606e39d2eebbaf3a8b9ae4c8a3d7bce59b7b19a00e2258bd11e1ed153b1d',
            'aec4a1724efef91a4acea32ce98cc781a9307389e0a50f7c3220169333cf9fe4', 18),
    'P31': ('31-level11-conjugacy-owner-ledger', 4,
            'ba7d12ec9bf2766c37fcdb9504f49ba08392ac078c21897587e3ba57fdc85750',
            'stage4_prime_method_passage_matrix_round3.json',
            'afc41796ffd47352355e031ada0f4f8d035f555eb9c2f5cc0705166e36276989',
            'a4f370b9894c8cbd83fe8815510baddcb9d70ff6b1734ed43710faeb83ded500', 16),
    'P32': ('32-homology-cover-renormalization-uniformity', 4,
            'af56c1c68fd514faace8ef546ac38976255b753d662ddfb3e8aad0fbfc1e5073',
            'stage4_prime_claim_passage_matrix_round4.json',
            'f1e03f705df0917071e89f12c8d91d0ea4f769ed6a6fe783e6c4ba5842344208',
            '2b8eb8d3a8fc148fe3886e4aadf1dafc094fe164266c0175928f4bb76aa1b13f', 19),
    'P33': ('33-bolza-control-matched-census', 3,
            'aa3783e6a24f830918ccb88b8dc5ebb28d9c15a94d87ffdb907cf5da9e049d6d',
            'stage4_prime_claim_passage_matrix_round3.json',
            'e3ad458e35bc8989c68f737e1f54fb36b37663f9a4ac16aa46e012a1ec07d65b',
            'ea12c0c4059abd227064335687a0c75a86912bd8c846040be1a1b0d0039c0787', 18),
}
APPLIED_KEYS = ('successor', 'approved_patch', 'apply_report',
                'revision_evidence_bundle', 'block_manifest',
                'integrity_authorization', 'base_draft', 'predecessor_bundle')
ZERO_DIAGNOSTICS = dict.fromkeys(('undefined_citations', 'undefined_references',
                                'missing_glyphs', 'fatal_errors', 'overfull_hboxes'), 0)
FROZEN = {}
TEMP_FROZEN = {}


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def workspace_path(relative, must_exist=True):
    require(isinstance(relative, str) and relative, 'artifact path is not a string')
    parts = relative.split('/')
    require(not PurePosixPath(relative).is_absolute()
            and all(part not in ('', '.', '..') for part in parts),
            'noncanonical workspace path: ' + relative)
    path = ROOT
    for part in parts:
        path /= part
        require(not path.is_symlink(), 'symlink workspace path: ' + relative)
    if must_exist:
        require(path.is_file(), 'missing/nonregular artifact: ' + relative)
    return path


def artifact(relative, expected_sha=None):
    raw = workspace_path(relative).read_bytes()
    row = {'path': relative, 'sha256': digest(raw), 'bytes': len(raw)}
    require(expected_sha is None or row['sha256'] == expected_sha,
            'pinned SHA mismatch: ' + relative)
    require(relative not in FROZEN or FROZEN[relative] == row,
            'input changed during inventory: ' + relative)
    FROZEN[relative] = row
    return dict(row)


def verify(row, paper_root=None):
    require(isinstance(row, dict) and 'path' in row and 'sha256' in row,
            'missing path/SHA artifact descriptor')
    relative = row['path']
    if isinstance(relative, str) and relative.startswith(('notes/', 'paper/')):
        require(paper_root is not None, 'paper-relative descriptor without paper root')
        relative = paper_root + '/' + relative
    require(re.fullmatch('[0-9a-f]{64}', str(row['sha256'])) is not None,
            'invalid full SHA descriptor: ' + str(relative))
    observed = artifact(relative, row['sha256'])
    if 'bytes' in row:
        require(type(row['bytes']) is int and observed['bytes'] == row['bytes'],
                'artifact byte-count mismatch: ' + relative)
    return observed


def load(row, paper_root=None):
    bound = verify(row, paper_root)
    return json.loads(workspace_path(bound['path']).read_bytes())


def descriptors(value, pointer=''):
    """Walk this JSON value only, never recursively open referenced files."""
    if isinstance(value, dict):
        if isinstance(value.get('path'), str) and 'sha256' in value:
            yield pointer, value
        for key, child in value.items():
            token = key.replace('~', '~0').replace('/', '~1')
            yield from descriptors(child, pointer + '/' + token)
    elif isinstance(value, list):
        for index, child in enumerate(value):
            yield from descriptors(child, pointer + '/' + str(index))


def unique(rows):
    return [row for _, row in sorted({row['path']: row for row in rows}.items())]


def absent_outputs():
    for relative in OUTPUTS:
        target = workspace_path(relative, must_exist=False)
        require(not target.exists(), 'refusing output collision: ' + relative)


def temporary_bytes(path):
    # Only the exact retained /tmp build file named by a pinned receipt is read.
    require(path.is_absolute() and path.parent.parent == Path('/tmp')
            and path.parent.name.startswith('round10-'), 'unexpected temporary build path')
    current = Path('/')
    for part in path.parts[1:]:
        current /= part
        require(not current.is_symlink(), 'symlink in temporary build path')
    require(path.is_file(), 'missing retained temporary build file: ' + str(path))
    raw = path.read_bytes()
    row = {'path': str(path), 'sha256': digest(raw), 'bytes': len(raw)}
    require(str(path) not in TEMP_FROZEN or TEMP_FROZEN[str(path)] == row,
            'temporary build bytes changed during inventory')
    TEMP_FROZEN[str(path)] = row
    return raw


def preview_inputs(paper_id, applied, app_desc, auth_desc, bibliography, recovery):
    cfg = PAPERS[paper_id]
    notes = 'papers/' + cfg[0] + '/notes/'
    job = 'stage4_prime_revision_round' + str(cfg[1])
    if paper_id == 'P32':
        job += '_preview_attempt2'
    receipt_desc = artifact(notes + job + '_build_receipt.json', cfg[5])
    receipt = load(receipt_desc)
    require(receipt.get('paper_id') == paper_id and receipt.get('status') == 'PASS_CLEAN',
            paper_id + ': preview identity/status mismatch')
    require(receipt.get('pages') == cfg[6] and receipt.get('diagnostics') == ZERO_DIAGNOSTICS,
            paper_id + ': preview page/diagnostic mismatch')
    require(receipt.get('protected_snapshot_unchanged') is True
            and receipt.get('protected_locked_bindings') == 119,
            paper_id + ': missing build boundary record')
    expected = {'input_draft': applied['successor'], 'application_receipt': app_desc,
                'authority': auth_desc, 'bibliography': bibliography,
                'revision_evidence_bundle': applied['revision_evidence_bundle']}
    for key, value in expected.items():
        require(receipt.get(key) == value, paper_id + ': build binding mismatch: ' + key)
    for key in ('builder', 'preview', 'final_latex_log', 'transcript', *expected):
        verify(receipt[key])
    require(receipt['preview']['path'] == notes + job + '.pdf', 'wrong preview output path')
    commands = receipt.get('commands', [])
    require(len(commands) == 6 and all(row.get('exit_code') == 0 for row in commands),
            paper_id + ': expected six recorded successful build/readback commands')
    require([Path(row['argv'][0]).name for row in commands] ==
            ['lualatex', 'bibtex', 'lualatex', 'lualatex', 'pdfinfo', 'pdftotext'],
            paper_id + ': build/readback command inventory mismatch')
    log = workspace_path(receipt['final_latex_log']['path']).read_text(encoding='utf-8')
    diagnostics = {
        'undefined_citations': len(re.findall(r"Citation [`'][^\n]+ undefined|There were undefined citations", log, re.I)),
        'undefined_references': len(re.findall(r"Reference [`'][^\n]+ undefined|There were undefined references", log, re.I)),
        'missing_glyphs': log.count('Missing character:'),
        'fatal_errors': len(re.findall(r'Fatal error|Emergency stop', log, re.I)),
        'overfull_hboxes': log.count('Overfull \\hbox'),
    }
    require(log and diagnostics == ZERO_DIAGNOSTICS, paper_id + ': nonclean retained log')
    raw = workspace_path(applied['successor']['path']).read_bytes()
    expected_compile = re.sub(rb'(?m)^<!--block:B[0-9]+-->(?:\r?\n|$)', b'', raw)
    transform_note = 'Whole block-marker lines removed; all other draft bytes unchanged.'
    if paper_id == 'P32':
        transform = recovery['proposed_preview_only_transform']
        old = transform['exact_source_fragment'].encode('utf-8')
        new = transform['proposed_compile_fragment'].encode('utf-8')
        token = transform['inserted_token'].encode('utf-8')
        require(expected_compile.count(old) == 1 and new.count(token) == 115
                and new.replace(token, b'') == old, 'P32 authorized transform mismatch')
        expected_compile = expected_compile.replace(old, new, 1)
        record = receipt['preview_only_recovery']
        require(record.get('exact_fragment_reversal_checked') is True,
                'P32 missing recorded reversal check')
        require(verify(record['authorization']) == artifact(RECOVERY_AUTH)
                and verify(record['confirmed_request']) == artifact(RECOVERY_REQUEST),
                'P32 recovery authorization mismatch')
        verify(record['original_builder_preserved'])
        transform_note += ' P32 exact authorized temporary fragment has 115 reversible inserted tokens.'
    if paper_id == 'P29':
        for key in ('approved_patch', 'official_apply_report', 'confirmed_request',
                    'predecessor_builder', 'protected_boundary_helper'):
            verify(receipt[key])
        require(receipt['approved_patch'] == applied['approved_patch']
                and receipt['official_apply_report'] == applied['apply_report']
                and receipt['confirmed_request'] == artifact(P29_REQUEST),
                'P29 B0006-specific build bindings mismatch')
    directory = Path(receipt['temporary_compile_directory'])
    require(temporary_bytes(directory / 'manuscript.tex') == expected_compile
            and digest(expected_compile) == receipt['compile_source_sha256'],
            paper_id + ': retained compile copy mismatch')
    require(temporary_bytes(directory / 'references.bib') ==
            workspace_path(bibliography['path']).read_bytes(), 'temporary bibliography mismatch')
    require(digest(temporary_bytes(directory / (job + '.pdf'))) == receipt['preview']['sha256'],
            paper_id + ': retained temporary/published PDF mismatch')
    return {
        'paper_id': paper_id, 'build_receipt': receipt_desc,
        'draft': applied['successor'], 'bibliography': bibliography,
        'preview': receipt['preview'], 'final_latex_log': receipt['final_latex_log'],
        'transcript': receipt['transcript'], 'pages': receipt['pages'],
        'status': receipt['status'], 'diagnostics': diagnostics,
        'recorded_commands': commands, 'compile_source_sha256': digest(expected_compile),
        'compile_transform': transform_note,
        'retained_temporary_directory': str(directory),
        'original_build_pdf_readback_text_sha256': receipt['pdf_readback_text_sha256'],
        'pdf_readback_rerun': False, 'build_rerun': False,
        'evidence_scope': 'Rehashed local preview bytes and retained build records, not a semantic or visual PDF review.',
    }


def revision_chain(paper_id, paper_root, applied):
    bundle = load(applied['revision_evidence_bundle'])
    require(verify(bundle['final_draft'], paper_root) == applied['successor'],
            paper_id + ': revision bundle final draft mismatch')
    rounds = bundle['rounds']
    require([row['revision_round'] for row in rounds] == list(range(1, PAPERS[paper_id][1] + 1)),
            paper_id + ': discontinuous protocol round numbers')
    bindings = [verify(row, paper_root) for _, row in descriptors(bundle)]
    surface_rows, round_rows = [], []
    previous = verify(bundle['chain_start']['draft'], paper_root)
    for row in rounds:
        require(verify(row['pre_round_draft'], paper_root) == previous,
                paper_id + ': adjacent bundle drafts do not join')
        previous = verify(row['post_round_draft'], paper_root)
        patch = load(row['revision_patch'], paper_root)
        require(patch['revision_round'] == row['revision_round'], 'patch protocol round mismatch')
        round_rows.append({'revision_round': row['revision_round'], 'kind': row['kind'],
                           'operation_count': len(patch['ops']),
                           'revision_patch': verify(row['revision_patch'], paper_root)})
        if 'claim_surface_manifest' in row:
            descriptor = verify(row['claim_surface_manifest'], paper_root)
            surface = load(descriptor)
            require(surface.get('surfaces') == [] and surface.get('claim_intent_sources') == [],
                    paper_id + ': expected explicit empty historical surface registry')
            surface_rows.append({'artifact': descriptor, 'revision_round': row['revision_round'],
                                 'base_draft_sha256': surface['base_draft_sha256'],
                                 'surfaces': [], 'claim_intent_sources': [],
                                 'role': 'RETAINED_EMPTY_PROTOCOL_SURFACE_REGISTRY_NOT_NEW_CURRENT_COVERAGE'})
    require(rounds[-1]['kind'] == 'integrity_correction', 'wrong last protocol branch')
    manifest = load(applied['block_manifest'])
    require(manifest.get('base_draft_hash') == applied['successor']['sha256'][:12],
            paper_id + ': current block manifest draft hash mismatch')
    return {'bundle': applied['revision_evidence_bundle'], 'bound_artifacts': unique(bindings),
            'rounds': round_rows, 'operation_count': sum(row['operation_count'] for row in round_rows),
            'historical_claim_surface_registries': surface_rows,
            'official_bundle_validation_run': False, 'semantic_e6_review_run': False,
            'claim_strength_drift_verdict': None,
            'scope': 'Protocol bytes, branch inventory and adjacent draft bindings only; no operation-semantic or claim-strength clearance.'}


def source_materials(paper_id, paper_root, matrix_desc, matrix):
    notes = paper_root + '/notes/'
    if paper_id in ('P29', 'P32'):
        names = ['stage4_prime_source_finalization_round3.json',
                 'stage4_prime_source_finalization_round3_validation.json',
                 'stage4_5_round1_browser_reference_verification.json',
                 'stage4_5_round1_reference_citation_audit.json',
                 'stage4_5_round2_browser_reference_verification.json',
                 'stage4_5_round2_reference_citation_audit.json']
    elif paper_id in ('P30', 'P31'):
        names = ['stage4_5_round1_source_finalization_proposal.json',
                 'stage4_5_round1_reference_network_audit.json',
                 'stage4_5_round2_reference_network_audit.json',
                 'stage4_5_round2_reference_citation_audit.json']
    else:
        names = ['stage4_prime_round5_source_use_locator_final.json',
                 'stage4_prime_round5_source_identity_replay_receipt.json']
    carrier_desc = artifact(notes + names[0])
    carrier = load(carrier_desc)
    if 'source_finalization' in matrix:
        require(verify(matrix['source_finalization'], paper_root) == carrier_desc,
                paper_id + ': matrix source-finalization mismatch')
    if paper_id == 'P33':
        require(verify(matrix['bindings']['historical_source_use_locator_carrier']) == carrier_desc,
                'P33 source-use carrier mismatch')
    retained = [artifact(notes + name) for name in names]
    retained.extend(artifact(notes + name) for name in (
        'stage1_phase2_source_inventory.tsv', 'stage1_phase2_source_verification.tsv',
        'stage1_phase3_literature_matrix.tsv'))
    excerpt_rows = []
    for index, row in enumerate(carrier.get('rows', [])):
        excerpt, expected = row.get('support_excerpt'), row.get('support_excerpt_sha256')
        if expected is not None:
            require(isinstance(excerpt, str) and digest(excerpt.encode('utf-8')) == expected,
                    paper_id + ': retained excerpt bytes/hash mismatch')
            excerpt_rows.append({'source_id': row['source_id'], 'carrier': carrier_desc,
                                 'json_pointer': '/rows/' + str(index) + '/support_excerpt',
                                 'sha256': expected, 'bytes': len(excerpt.encode('utf-8'))})
    return {'matrix': matrix_desc, 'retained_carriers': unique(retained),
            'inline_excerpt_byte_bindings': excerpt_rows,
            'new_source_retrievals': 0, 'new_original_passage_verifications': 0,
            'historical_nested_descriptor_policy':
                'Carrier bytes and listed source containers are frozen, not all nested old draft/matrix assertions. '
                'P30/P31 Round-1 proposals contain pre-regeneration matrix descriptors; these are historical assertions, '
                'not current file bindings and are not silently rebound or certified. Retrieval hashes without retained '
                'bodies are recorded history, not proof that a full original source body is locally available.',
            'scope': 'Exact retained file/excerpt bytes only. Metadata, abstract excerpts and manuscript contexts are not upgraded into full-text or theorem-applicability evidence.'}


def matrix_inputs(paper_id, paper_root, draft, completion_derived):
    cfg = PAPERS[paper_id]
    matrix_desc = artifact(paper_root + '/notes/' + cfg[3], cfg[4])
    matrix = load(matrix_desc)
    require(matrix.get('paper_id') == paper_id, 'matrix paper identity mismatch')
    # Current matrix bytes may carry explicitly historical substructures. Freeze
    # the carrier but never adopt an old in-place derivation as current authority.
    embedded = [verify(row, paper_root) for pointer, row in descriptors(matrix)
                if not pointer.startswith('/historical_derivation/')]
    producer, reader = None, None
    if paper_id == 'P29':
        require(len(matrix['rows']) == 22, 'P29 matrix population mismatch')
        require(sum(row['passage_status'] == 'EXACT_LOCATOR_FINALIZED' for row in matrix['rows']) == 13,
                'P29 bounded-locator partition mismatch')
        require(sum(row['passage_status'] == 'EXPLICIT_BOUNDED_UNAVAILABILITY_METADATA_ONLY'
                    for row in matrix['rows']) == 9, 'P29 unavailable partition mismatch')
        require(verify(matrix['base_draft']) != draft, 'P29 matrix unexpectedly rebound to current draft')
        context = {'role': 'UNCHANGED_SOURCE_MATRIX_WITH_HISTORICAL_ROUND2_CONTEXT',
                   'historical_base_draft': verify(matrix['base_draft']),
                   'current_draft_context_rebind_claimed': False,
                   'counts': {'rows': 22, 'bounded_locators': 13, 'unavailable_metadata_only': 9}}
    else:
        derived = completion_derived[paper_id]
        require(matrix_desc in derived['materials'], 'current matrix absent from actual producer completion')
        producer = verify(derived['producer_receipt'])
        # Bind the producer receipt itself; its explicitly historical differences
        # (including the P31 replaced-entry-before defect) are not current targets.
        if paper_id in ('P30', 'P31'):
            require(verify(matrix['successor_draft'], paper_root) == draft, 'matrix successor mismatch')
            context = {'role': 'CURRENT_POST_APPLY_CONTEXT_WITH_RETAINED_SOURCE_EVIDENCE',
                       'counts': matrix['result_counts']}
            require(len(matrix['rows']) == (28 if paper_id == 'P30' else 24), 'matrix row count mismatch')
        elif paper_id == 'P32':
            require(verify(matrix['current_draft']) == draft and len(matrix['rows']) == 30,
                    'P32 current context/row mismatch')
            context = {'role': 'CURRENT_POST_APPLY_CONTEXT_WITH_RETAINED_SOURCE_EVIDENCE',
                       'counts': matrix['summary'],
                       'required_joint_reading': 'B0018 qualification, B0132 table and its concluding paragraph; CW01-CW04 remain metadata-only, UNVERIFIABLE and without positive passage support.'}
        else:
            require(verify(matrix['bindings']['current_draft']) == draft
                    and len(matrix['rows']) == 48, 'P33 current context/row mismatch')
            context = {'role': 'CURRENT_CITATION_CONTEXTS_NOT_A_FULL_CLAIM_REGISTRY',
                       'counts': matrix['counts'],
                       'required_joint_reading': 'B0037 with B0127, and B0062 with B0128; current manuscript contexts are not original-source excerpts or independent proof.'}
        if paper_id == 'P31':
            path = paper_root + '/notes/stage4_prime_reader_artifact_manifest_round3.json'
            reader_desc = artifact(path)
            require(reader_desc in derived['materials'], 'P31 current reader missing from producer completion')
            value = load(reader_desc)
            require(len(value['entries']) == value['entry_count'] == 11, 'P31 reader denominator mismatch')
            reader = {'artifact': reader_desc,
                      'entries': [verify(row, paper_root) for row in value['entries']],
                      'historical_predecessor': verify(value['predecessor_manifest']),
                      'scope': 'Local listed bytes only; historical TSV is not the current JSON projection; the old manifest stale matrix entry remains disclosed, not repaired or accepted as a current binding.'}
    return {'artifact': matrix_desc, 'context_scope': context,
            'embedded_descriptor_bindings': unique(embedded),
            'producer_receipt': producer, 'reader_inventory': reader,
            'fresh_passage_or_integrity_verdict': None,
            'retained_source_evidence': source_materials(paper_id, paper_root, matrix_desc, matrix)}


def json_bytes(value):
    return (json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + '\n').encode('utf-8')


def pending(relative, raw):
    return {'path': relative, 'sha256': digest(raw), 'bytes': len(raw)}


def main():
    absent_outputs()
    roots = {path: artifact(path, pin) for path, pin in PINS.items()}
    generator = artifact(Path(__file__).resolve().relative_to(ROOT).as_posix())
    old_lock, old_completion = load(roots[OLD_LOCK]), load(roots[OLD_COMPLETION])
    batch_app, p29_app = load(roots[BATCH_APP]), load(roots[P29_APP])
    require(batch_app['authority'] == roots[BATCH_AUTH] and p29_app['authority'] == roots[P29_AUTH],
            'root application/authority mismatch')
    for authority, request in ((BATCH_AUTH, BATCH_REQUEST), (P29_AUTH, P29_REQUEST)):
        require(load(roots[authority])['confirmed_request'] == roots[request],
                'root authority/exact-request mismatch')
    require(old_completion['application_receipt'] == roots[BATCH_APP], 'old completion/app mismatch')
    recovery = load(roots[RECOVERY_REQUEST])
    for key in ('base_builder', 'trigger', 'already_completed_application', 'prior_exact_authority',
                'approved_draft_to_keep_byte_identical', 'approved_patch_to_keep_byte_identical'):
        verify(recovery[key])
    prior_failure = load(recovery['trigger'])
    require(prior_failure['status'] == 'FAIL' and prior_failure['diagnostics']['overfull_hboxes'] == 1,
            'P32 failed attempt history mismatch')
    preserved_failure = {key: verify(old_completion[key]) for key in (
        'prior_p32_failure_preserved', 'prior_p32_failed_log_preserved', 'prior_p32_failed_transcript_preserved')}
    require(preserved_failure['prior_p32_failure_preserved'] == verify(recovery['trigger'])
            and preserved_failure['prior_p32_failed_log_preserved'] == verify(prior_failure['final_latex_log'])
            and preserved_failure['prior_p32_failed_transcript_preserved'] == verify(prior_failure['transcript']),
            'P32 failure receipt/log provenance mismatch')
    helper = runpy.run_path(str(workspace_path(HELPER)), run_name='round3_input_lock_read_only_boundary')
    boundary = helper['protected_boundary_replay']()
    require(boundary == old_completion['protected_boundary']
            and boundary == p29_app['protected_boundary_replay'],
            'protected canonical/science/read-only snapshot drift')
    for _, row in descriptors(old_lock):
        if 'bytes' in row:
            verify(row)
    for row in boundary['read_only_files']:
        verify(row)
    old_papers = {row['paper_id']: row for row in old_lock['papers']}
    applications = {row['paper_id']: row for row in batch_app['papers']}
    derived = {row['paper_id']: row for row in old_completion['derived_materials']}
    require(set(old_papers) == set(applications) == set(PAPERS)
            and set(derived) == set(PAPERS) - {'P29'}, 'five-paper population mismatch')
    require(p29_app['paper_id'] == p29_app['paper']['paper_id'] == 'P29', 'P29 override identity mismatch')
    applications['P29'] = p29_app['paper']
    papers, previews = [], []
    for paper_id, cfg in PAPERS.items():
        paper_root = 'papers/' + cfg[0]
        old, applied = old_papers[paper_id], applications[paper_id]
        current = {key: verify(applied[key]) for key in APPLIED_KEYS}
        require(current['successor']['path'] == paper_root + '/notes/stage4_prime_revision_round' + str(cfg[1]) + '.tex'
                and current['successor']['sha256'] == cfg[2], paper_id + ': wrong current successor')
        # The bibliography is selected from actual current build/application
        # bindings, not an inherited old-lock current-input default.
        if paper_id == 'P29':
            bib = verify(p29_app['bibliography'])
        elif paper_id == 'P30':
            bib = verify(batch_app['bib_successor'])
        else:
            job = 'stage4_prime_revision_round' + str(cfg[1])
            if paper_id == 'P32':
                job += '_preview_attempt2'
            build = load(artifact(paper_root + '/notes/' + job + '_build_receipt.json', cfg[5]))
            bib = verify(build['bibliography'])
        expected_bib = (paper_root + '/paper/references.bib' if paper_id == 'P33' else
                        paper_root + '/notes/stage4_prime_references_round' + ('3' if paper_id == 'P30' else '2') + '.bib')
        require(bib['path'] == expected_bib, 'wrong current bibliography path')
        current['bibliography'] = bib
        app_desc = roots[P29_APP] if paper_id == 'P29' else roots[BATCH_APP]
        auth_desc = roots[P29_AUTH] if paper_id == 'P29' else roots[BATCH_AUTH]
        current['application_receipt'], current['exact_patch_authority'] = app_desc, auth_desc
        preview = preview_inputs(paper_id, applied, app_desc, auth_desc, bib, recovery)
        previews.append(preview)
        chain = revision_chain(paper_id, paper_root, applied)
        matrix = matrix_inputs(paper_id, paper_root, current['successor'], derived)
        passport_desc = artifact(paper_root + '/notes/stage4_5_round2_material_passport.json')
        passport = load(passport_desc)
        require(passport['content_hash'] == old['audit_draft']['sha256']
                and passport['content_hash'] != current['successor']['sha256'],
                paper_id + ': latest Round-2 passport is not the expected historical seed')
        require(passport.get('claim_intent_manifests') == [], 'unexpected passport ClaimIntent registry')
        claim_intents = []
        for name in ('stage1_phase3_claim_intent_manifest.json', 'stage1_phase4_claim_intent_manifest.json',
                     'stage1_phase6_claim_intent_manifest.json', 'stage2_claim_intent_manifest.json'):
            descriptor = artifact(paper_root + '/notes/' + name)
            value = load(descriptor)
            claim_intents.append({'artifact': descriptor, 'manifest_id': value.get('manifest_id'),
                                  'declared_claim_count': len(value['claims']),
                                  'role': 'HISTORICAL_DECLARED_INTENT_NOT_AN_INVENTED_CURRENT_SURFACE_REGISTRY'})
        papers.append({'paper_id': paper_id, 'paper_slug': cfg[0], 'protocol_revision_round': cfg[1],
                       'current_inputs': current, 'current_preview': preview,
                       'source_matrix_inventory': matrix, 'continuous_revision_evidence': chain,
                       'claim_intent_source_inventory': claim_intents,
                       'explicit_passport_claim_intent_registry': [],
                       'latest_passport_seed': {'artifact': passport_desc,
                           'role': 'LATEST_PASSPORT_SEED_HISTORICAL_NOT_CURRENT_INTEGRITY',
                           'bound_historical_draft': old['audit_draft'],
                           'experiment_intake_declaration': passport['experiment_intake_declaration'],
                           'experiment_provenance_count': len(passport['experiment_provenance']),
                           'existing_history_retained_in_seed': True, 'fresh_verdict_inherited': False},
                       'historical_round2_input_inventory': old['audit_inputs'],
                       'historical_prior_integrity_evidence': old['prior_integrity_evidence'],
                       'frozen_initial_system': old['frozen_initial_system'],
                       'frozen_route_state': old['frozen_route_state'],
                       'protected_canonical_files': old['protected_canonical_files'],
                       'protected_science_trees': old['science_trees'],
                       'fresh_audit_verdict': None})
    stamp = datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0).isoformat().replace('+00:00', 'Z')
    common = {'generated_at_utc': stamp, 'generator': generator,
              'stage4_5_round3_completed': False, 'stage5_or_stage6_run': False,
              'scientific_execution_performed': False, 'official_validator_executed': False,
              'manuscript_or_bibliography_mutation': False, 'canonical_promotion': False}
    p29_completion = {**common, 'schema_version': 'round10-p29-b0006-preview-completion/1.0',
                      'status': 'P29_ROUND5_PREVIEW_PASS_CLEAN_NOT_INTEGRITY_PASS',
                      'application_receipt': roots[P29_APP], 'authority': roots[P29_AUTH],
                      'confirmed_request': roots[P29_REQUEST], 'preview': previews[0],
                      'superseded_preview_role_only': old_completion['papers'][0],
                      'prior_preview_completion_retained': roots[OLD_COMPLETION],
                      'protected_boundary': boundary,
                      'scope': 'P29 actual retained preview binding completion only. The older P29 Round-4 preview remains history; no old receipt was rewritten.'}
    completion_raw = json_bytes(p29_completion)
    input_lock = {**common, 'schema_version': 'round10-stage4.5-round3-input-lock/1.0',
                  'status': 'IMMUTABLE_INPUT_INVENTORY_FRESH_INTEGRITY_AUDIT_NOT_RUN',
                  'batch': 'Round10', 'audit_round': 3, 'paper_ids': list(PAPERS),
                  'papers': papers, 'current_preview_pages_total': sum(row['pages'] for row in previews),
                  'p29_preview_completion': pending(NEW_COMPLETION, completion_raw),
                  'root_authority_and_application_bindings': {key: roots[key] for key in (
                      BATCH_AUTH, BATCH_REQUEST, BATCH_APP, P29_AUTH, P29_REQUEST, P29_APP,
                      RECOVERY_AUTH, RECOVERY_REQUEST)},
                  'root_authority_scope': 'Exact correction and preview-recovery authority only; this inventory does not manufacture additional writing, scientific or audit authority.',
                  'historical_round2_lock': roots[OLD_LOCK],
                  'historical_preview_completion': roots[OLD_COMPLETION],
                  'preserved_p32_failed_attempt': preserved_failure,
                  'protected_boundary': boundary,
                  'current_vs_historical_rule': 'Only current_inputs/current_preview and explicitly current matrix contexts select the audit target. All old verdicts, passports, old draft contexts and pre-apply statuses are retained history; no historical PASS, FAIL, count, claim span or source verdict is a fresh Round-3 finding.',
                  'claim_surface_rule': 'Explicit empty protocol surface and passport ClaimIntent registries remain empty. Historical intent manifests are inventory only; fresh claims, UTF-8 spans, coverage, EVR and E6 semantic findings must be generated and adjudicated separately.',
                  'fresh_current_claim_registry': None, 'fresh_current_integrity_verdict': None,
                  'observed_workspace_bindings': [FROZEN[key] for key in sorted(FROZEN)],
                  'retained_temporary_preview_bindings': [TEMP_FROZEN[key] for key in sorted(TEMP_FROZEN)]}
    lock_raw = json_bytes(input_lock)
    replay = {**common, 'schema_version': 'round10-stage4.5-round3-input-binding-replay/1.0',
              'status': 'LOCAL_BYTE_BINDING_REPLAY_ONLY_NOT_INDEPENDENT_INTEGRITY_REVIEW',
              'input_lock': pending(NEW_LOCK, lock_raw),
              'p29_preview_completion': pending(NEW_COMPLETION, completion_raw),
              'workspace_binding_count': len(FROZEN), 'temporary_binding_count': len(TEMP_FROZEN),
              'paper_count': len(papers), 'current_preview_count': len(previews),
              'current_preview_pages_total': sum(row['pages'] for row in previews),
              'protected_boundary': boundary,
              'authorship_and_independence': {
                  'preparer_role': 'same-model-family auxiliary input-inventory agent',
                  'p29_preview_builder_author_overlap': True,
                  'independent_author_claimed': False, 'cross_model_verification_claimed': False,
                  'independent_error_process_claimed': False,
                  'formal_independent_semantic_review_performed': False},
              'scope': 'Existing local hashes, byte lengths, recorded build results, exact temporary compile transforms, adjacent bundle bindings and explicit inventory boundaries only. This is not A-E, coverage, EVR, E6 semantic, originality, compliance or scientific-result validation.',
              'payload_persistence': 'Three new JSON files are emitted together; the generator itself performs no file writes. Lock and completion hashes describe the exact pending UTF-8 payload bytes.'}
    # Recheck all reads and protected trees before emitting any payload bytes.
    for row in list(FROZEN.values()):
        verify(row)
    for name in list(TEMP_FROZEN):
        temporary_bytes(Path(name))
    require(helper['protected_boundary_replay']() == boundary, 'protected boundary changed during inventory')
    absent_outputs()
    payload = [(NEW_COMPLETION, completion_raw), (NEW_LOCK, lock_raw), (NEW_REPLAY, json_bytes(replay))]
    lines = ['*** Begin Patch']
    for relative, raw in payload:
        lines.append('*** Add File: ' + str(ROOT / relative))
        lines.extend('+' + line for line in raw.decode('utf-8').splitlines())
    lines.append('*** End Patch')
    print('\n'.join(lines))
    print('Prepared 3 append-only payloads; no files written, builds run, or integrity verdicts issued.', file=sys.stderr)


if __name__ == '__main__':
    try:
        main()
    except Exception as exc:
        print('STOP: ' + type(exc).__name__ + ': ' + str(exc), file=sys.stderr)
        sys.exit(1)
