"""Read-only current Schema-5 handoff accounting and exact binding checks.

This is repository glue for the documented Schema-5 fields, not an invented
replacement for official EVR/coverage/E6/compliance validators. The official
validators are run separately. First failure is retained and stops this run.
"""
import hashlib
import json
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def read(path):
    return json.loads((ROOT / path).read_bytes())

def sha(path):
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()

def require(ok, message):
    if not ok:
        raise ValueError(message)

def binding(row):
    raw = (ROOT / row['path']).read_bytes()
    require(hashlib.sha256(raw).hexdigest() == row['sha256'], 'NEW_BOUND_ARTIFACT_HASH_MISMATCH: ' + row['path'])
    if 'bytes' in row:
        require(len(raw) == row['bytes'], 'NEW_BOUND_ARTIFACT_SIZE_MISMATCH: ' + row['path'])

def main():
    completed = []
    current = None
    try:
        lock = read('BATCH_ROUND10_STAGE4_5_ROUND3_INPUT_LOCK.json')
        for paper in lock['papers']:
            current = paper['paper_id']
            note = 'papers/' + paper['paper_slug'] + '/notes/'
            prefix = 'stage4_5_round3_resume_' + current.lower()
            report_path = note + 'stage4_5_round3_integrity_report' + ('_v2' if current == 'P30' else '') + '.json'
            report = read(report_path)
            for key in ['verdict', 'mode', 'phases', 'overall_issues', 'citation_integrity_score', 'fabrication_risk_score', 'timestamp']:
                require(key in report, 'Schema5 missing ' + key)
            require(report['verdict'] in {'PASS', 'PASS_WITH_CONDITIONS', 'FAIL'}, 'Invalid Schema5 verdict')
            require(report['mode'] == 'final-check', 'Wrong mode')
            for score in ['citation_integrity_score', 'fabrication_risk_score']:
                require(isinstance(report[score], (float, int)) and 0 <= report[score] <= 1, 'Invalid ' + score)
            for descriptor in report['component_bindings'] + report['shared_audit_bindings'] + [report['compliance_report']]:
                binding(descriptor)
            control = report['controlling_inputs']
            for descriptor in control.values():
                binding(descriptor)
            registry = read(control['claim_registry']['path'])
            draft = (ROOT / control['draft']['path']).read_bytes()
            selected = {row['claim_id']: row for row in registry['claims']}
            require(len(selected) == len(registry['claims']), 'Duplicate registered claim id')
            for claim in registry['claims']:
                span = claim['draft_span']
                require(draft[span['start_byte']:span['end_byte']].decode('utf-8') == claim['claim_text'], 'Exact selected claim span mismatch: ' + claim['claim_id'])
            phases = report['phases']
            for key in ['A_references', 'B_citation_context', 'C_data', 'D_originality', 'E_claims']:
                require(key in phases, 'Missing phase ' + key)
            a, b, c, d, e = [phases[k] for k in ['A_references', 'B_citation_context', 'C_data', 'D_originality', 'E_claims']]
            require(a['checked'] == a['passed'] + a['failed'], 'A counts do not reconcile')
            require(0 <= b['verified'] <= b['sampled'], 'B counts invalid')
            require(c['claims_checked'] == len(c['check_groups']), 'C group denominator mismatch')
            require(c['verified'] == sum(r['verdict'] == 'VERIFIED_WITH_SCOPE' for r in c['check_groups']), 'C verified groups mismatch')
            require(d['checked'] and d['coverage']['selected'] / d['coverage']['denominator'] >= 0.5, 'D declared sampling threshold missing')
            cov = e['claim_registry_coverage']
            require(cov['status'] == 'completed' and cov['semantic_extraction_coverage'] == 'not_machine_detectable', 'E1.1 status/limit invalid')
            require(sha(cov['report_path']) == cov['report_sha256'], 'NEW_COVERAGE_ARTIFACT_HASH_MISMATCH')
            cov_raw = read(cov['report_path'])
            require(cov_raw['draft_raw_sha256'] == cov['draft_raw_sha256'] == control['draft']['sha256'], 'Coverage draft mismatch')
            require(cov_raw['registry_raw_sha256'] == cov['registry_raw_sha256'] == sha(control['claim_registry']['path']), 'Coverage registry mismatch')
            require(cov_raw['candidate_unregistered_count'] == cov['candidate_unregistered_count'] == 0, 'Coverage candidate count mismatch')
            evr_path = note + prefix + '_evidence_rows' + ('_v2' if current == 'P30' else '') + '.json'
            require(e['evidence_rows'] == read(evr_path), 'Report embeds different official rows')
            input_path = note + prefix + '_official_evidence_build_input' + ('_v2' if current == 'P30' else '') + '.json'
            expected = read(input_path)['inputs']
            require(len(expected) == len(e['evidence_rows']) == e['selected_tuple_count'], 'Selected tuple count mismatch')
            actual_claims = {}
            claim_rows = {}
            tuple_keys = []
            for exp, row in zip(expected, e['evidence_rows']):
                template = exp['row']
                require(template['claim'] == row['claim'] and template['verdict'] == row['verdict'], 'Selected tuple claim/verdict mismatch')
                require(template['source']['ref_slug'] == row['source']['ref_slug'] and template['anchor']['value_encoded'] == row['anchor']['value_encoded'], 'Selected tuple source/anchor mismatch')
                cid = row['claim']['claim_id']
                require(row['claim']['text'] == selected[cid]['claim_text'], 'Row claim text differs from registry')
                if cid in actual_claims:
                    require(actual_claims[cid] == row['verdict'], 'Per-claim verdict disagreement')
                actual_claims[cid] = row['verdict']
                claim_rows.setdefault(cid, []).append(row)
                tuple_keys.append((cid, row['source']['ref_slug'], row['anchor']['value_encoded']))
            require(len(set(tuple_keys)) == len(tuple_keys), 'Duplicate selected tuple')
            require(set(actual_claims) == set(selected), 'Current registered claim set not fully represented')
            for cid, rows in claim_rows.items():
                refs = {r['source']['ref_slug'] for r in rows if r['source']['ref_slug'] is not None}
                anchors = {r['anchor']['value_decoded'] for r in rows if r['anchor']['kind'] != 'none'}
                require(refs == set(selected[cid]['ref_slugs']), 'Selected reference coverage mismatch: ' + cid)
                require(anchors == set(selected[cid]['writer_anchors']), 'Selected writer-anchor coverage mismatch: ' + cid)
            counts = Counter(actual_claims.values())
            require(e['checked'] == len(actual_claims) and e['verified'] == counts['VERIFIED'], 'E distinct claim summary mismatch')
            require(all(e['verdict_counts'].get(k, 0) == v for k, v in counts.items()), 'E verdict taxonomy count mismatch')
            distorted = {r['claim_id'] for r in e['distortions']}
            require(distorted == {cid for cid, v in actual_claims.items() if v != 'VERIFIED'}, 'E distortion population mismatch')
            counted = Counter(r['severity'] for r in report['correction_list'])
            require(all(report['overall_issues'][k] == counted[k] for k in ['SERIOUS','MEDIUM','MINOR']), 'Ordinary correction severity counts mismatch')
            require(not any(r['id'].startswith('ADV-E6') for r in report['correction_list']), 'E6 accidentally counted as ordinary issue')
            ef = e['claim_strength_drift_findings']
            require(sha(ef['artifact_path']) == ef['artifact_sha256'], 'NEW_E6_HASH_MISMATCH')
            findings = read(ef['artifact_path'])
            require(findings['final_draft_sha256'] == control['draft']['sha256'] and findings['revision_evidence_bundle_sha256'] == control['revision_evidence_bundle']['sha256'], 'E6 current binding mismatch')
            require(report['mandatory_checkpoint']['E6_finding_count'] == len(findings['findings']), 'E6 count mismatch')
            if not findings['findings']:
                require(report['mandatory_checkpoint']['claim_strength_disposition'] == 'NOT_REQUIRED_ZERO_FINDINGS', 'Zero E6 findings cannot require row dispositions')
            require(len(report['seven_failure_modes']) == 7, 'Seven-mode accounting incomplete')
            compliance = read(report['compliance_report']['path'])
            require(compliance['mode'] == 'primary_research' and compliance['overall_decision'] == 'warn', 'Current compliance scope mismatch')
            require(report['verdict'] == 'FAIL' if (counts['UNVERIFIABLE'] or counts['MAJOR_DISTORTION'] or a['failed']) else True, 'Unresolved integrity issue improperly passed')
            completed.append({'paper_id':current, 'report_path':report_path, 'report_sha256':sha(report_path), 'claim_count':e['checked'], 'selected_tuples':len(tuple_keys), 'verdict_counts':dict(counts), 'status':'PASS_HANDOFF_SHAPE_ACCOUNTING_AND_BINDINGS'})
        print(json.dumps({'status':'PASS', 'rows':completed, 'independent_scientific_or_semantic_verification':False}))
        return 0
    except Exception as exc:
        print(json.dumps({'status':'STOP_FIRST_FAILURE', 'paper_id':current, 'error':str(exc), 'completed':completed}))
        return 1

if __name__ == '__main__':
    sys.exit(main())
