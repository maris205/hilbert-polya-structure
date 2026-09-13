#!/usr/bin/env python3
"""Validate completed official applies, append bundles, emit scoped sidecars/Bib.

No manuscript rewrite, experiment, canonical promotion, or integrity verdict.
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


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def encoded(obj):
    return (json.dumps(obj, ensure_ascii=False, indent=2, sort_keys=True) + '\n').encode()


def desc(path, raw=None):
    raw = path.read_bytes() if raw is None else raw
    return {'path': str(path.relative_to(ROOT)), 'sha256': sha(raw), 'bytes': len(raw)}


def verify(d):
    assert desc(ROOT / d['path']) == d, d['path']


def prepare():
    sys.path.insert(0, str(ARS / 'scripts'))
    import _block_parser as bp
    import ars_anchorize_draft as anchor
    import revision_roadmap as rr
    authority_path = ROOT / (PREFIX + 'AUTHORIZATION_RECEIPT.json')
    authority = json.loads(authority_path.read_bytes())
    verify(authority['confirmed_request'])
    assert authority['confirmed_request']['sha256'] == '759480e724b818c5068233134712a14a4736df116ca295578495912f3a86a42d'
    verify(authority['raw_author_event'])
    verify(authority['authorization_record'])
    outputs, rows = {}, []
    for p in authority['papers']:
        for key in ('base_draft', 'base_block_manifest', 'patch', 'issue_list', 'author_input', 'integrity_authorization'):
            verify(p[key])
        base = ROOT / p['base_draft']['path']
        successor = ROOT / p['proposed_successor_draft']
        notes = successor.parent
        paper_root = notes.parent
        patch = json.loads((ROOT / p['patch']['path']).read_bytes())
        report_path = Path(str(successor) + '.apply-report.json')
        report = json.loads(report_path.read_bytes())
        assert report['patch_digest'] == p['patch']['sha256']
        assert report['authorization_witness']['status'] == 'pass'
        assert report['base_draft_hash'] == p['base_draft']['sha256'][:12]
        assert report['output_draft_hash'] == sha(successor.read_bytes())[:12]
        a, b = base.read_text(), successor.read_text()
        old, new = bp.parse_document(a).block_by_id(), bp.parse_document(b).block_by_id()
        targets = {op['block_id'] for op in patch['ops']}
        for key, block in old.items():
            if key not in targets:
                other = new[key]
                assert a[block.full_start:block.span[1]].encode() == b[other.full_start:other.span[1]].encode(), key
        for op in patch['ops']:
            assert new[op['block_id']].normalized_text == op['new_text'], op['block_id']
        manifest_path = successor.with_suffix('.block-manifest.json')
        manifest = anchor.build_manifest(successor.read_bytes(), bp.parse_document(b))
        manifest_raw = encoded(manifest)
        rr.validate_block_manifest(manifest, manifest_raw, successor.read_bytes())
        number = patch['revision_round']
        old_bundle_path = notes / f'stage4_prime_revision_evidence_bundle_round{number-1}.json'
        bundle = json.loads(old_bundle_path.read_bytes())
        assert bundle['rounds'][-1]['revision_round'] + 1 == number
        assert bundle['final_draft']['sha256'] == p['base_draft']['sha256']
        artifact = lambda path: {'path': str(path.relative_to(paper_root)), 'sha256': sha(path.read_bytes())}
        bundle['rounds'].append({'kind': 'integrity_correction', 'revision_round': number, 'pre_round_draft': artifact(base), 'pre_round_block_manifest': artifact(ROOT / p['base_block_manifest']['path']), 'issue_list': artifact(ROOT / p['issue_list']['path']), 'integrity_authorization': artifact(ROOT / p['integrity_authorization']['path']), 'revision_patch': artifact(ROOT / p['patch']['path']), 'apply_report': artifact(report_path), 'post_round_draft': artifact(successor)})
        bundle['final_draft'] = artifact(successor)
        rr.validate_bundle(bundle, root=paper_root)
        bundle_path = notes / f'stage4_prime_revision_evidence_bundle_round{number}.json'
        bundle_raw = encoded(bundle)
        outputs[manifest_path], outputs[bundle_path] = manifest_raw, bundle_raw
        rows.append({'paper_id': p['paper_id'], 'base_draft': p['base_draft'], 'approved_patch': p['patch'], 'integrity_authorization': p['integrity_authorization'], 'successor': desc(successor), 'apply_report': desc(report_path), 'block_manifest': desc(manifest_path, manifest_raw), 'predecessor_bundle': desc(old_bundle_path), 'revision_evidence_bundle': desc(bundle_path, bundle_raw), 'official_apply_status': 'PASS', 'official_manifest_validation': 'PASS', 'official_continuous_bundle_replay': 'PASS', 'counters': report['counters'], 'all_replacement_texts_exact': True, 'untouched_marked_blocks_byte_identical': len(old)-len(targets), 'structural_flags': report['structural_flags']})
    verify(authority['bibliography_proposal'])
    proposal = json.loads((ROOT / authority['bibliography_proposal']['path']).read_bytes())
    operation = proposal['operation']
    verify(operation['base_artifact'])
    raw = (ROOT / operation['base_artifact']['path']).read_bytes()
    old, new = proposal['old_entry'].encode(), proposal['new_entry'].encode()
    assert raw.count(old) == 1 and sha(old) == operation['expected_current_entry_sha256']
    field = operation['exact_field_change']
    assert old.count(field['old_companion_doi'].encode()) == 1
    assert old.replace(field['old_companion_doi'].encode(), field['new_companion_doi'].encode()) == new
    bib_raw = raw.replace(old, new, 1)
    assert sha(bib_raw) == proposal['proposed_successor_sha256'] and len(bib_raw) == proposal['proposed_successor_bytes']
    bib_path = ROOT / operation['proposed_successor']
    outputs[bib_path] = bib_raw
    finalizer = runpy.run_path(str(ROOT / 'tools/finalize_round10_stage4_5_round2.py'), run_name='read_only_boundary_helpers')
    protected = finalizer['protected_boundary_replay']()
    receipt = {'schema_version': 'round10-exact-patch-application-receipt/1.0', 'generated_at_utc': datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0).isoformat().replace('+00:00', 'Z'), 'status': 'FIVE_EXACT_PATCHES_APPLIED_AND_CONTINUOUS_BUNDLES_VALIDATED_NOT_INTEGRITY_PASS', 'authority': desc(authority_path), 'producer': desc(Path(__file__).resolve()), 'papers': rows, 'bib_proposal': authority['bibliography_proposal'], 'bib_successor': desc(bib_path, bib_raw), 'bib_single_note_doi_change_only': True, 'aggregate': {'papers_applied': 5, 'replaced_blocks': sum(p['counters']['blocks_touched'] for p in rows), 'untouched_blocks_byte_identical': sum(p['untouched_marked_blocks_byte_identical'] for p in rows), 'bib_entries_corrected': 1, 'scientific_executions': 0, 'canonical_promotions': 0}, 'protected_boundary_replay': protected, 'local_diagnostic_incident': desc(ROOT / (PREFIX + 'LOCAL_DIAGNOSTIC_INCIDENT.md')), 'not_yet_completed': ['scoped derived source matrices and reader manifest', 'isolated preview builds', 'fresh Stage 4.5 Round 3 integrity audit'], 'last_completed_integrity_verdict': 'ROUND2_FAIL_ALL_FIVE', 'stage5_authorized': False, 'readme_status_git_mutated': False}
    outputs[ROOT / (PREFIX + 'APPLICATION_RECEIPT.json')] = encoded(receipt)
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
