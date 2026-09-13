"""Read-only official E6 finding-set schema and exact artifact binding replay.

No disposition is built; this program cannot create an author choice.
The first official failure returns nonzero and stops the full run.
"""
import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARS = Path('/root/autodl-tmp/.codex/plugins/cache/ars-codex/ars-codex/0.1.28/skills/academic-research-suite/ars')

def main():
    completed = []
    current = None
    try:
        spec = importlib.util.spec_from_file_location('round3_official_e6', ARS/'scripts/claim_strength_drift_disposition.py')
        runtime = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(runtime)
        lock = json.loads((ROOT/'BATCH_ROUND10_STAGE4_5_ROUND3_INPUT_LOCK.json').read_bytes())
        for paper in lock['papers']:
            current = paper['paper_id']
            note = ROOT/'papers'/paper['paper_slug']/'notes'
            finding_path = note/'stage4_5_round3_claim_strength_drift_findings.json'
            finding, raw = runtime.load_json_path(finding_path, 'finding set')
            draft_name = {'P29':'stage4_prime_revision_round5.tex','P30':'stage4_prime_revision_round4.tex','P31':'stage4_prime_revision_round4.tex','P32':'stage4_prime_revision_round4.tex','P33':'stage4_prime_revision_round3.tex'}[current]
            bundle_name = {'P29':'stage4_prime_revision_evidence_bundle_round5.json','P30':'stage4_prime_revision_evidence_bundle_round4.json','P31':'stage4_prime_revision_evidence_bundle_round4.json','P32':'stage4_prime_revision_evidence_bundle_round4.json','P33':'stage4_prime_revision_evidence_bundle_round3.json'}[current]
            runtime._validate_findings(finding)
            runtime._validate_evidence_bindings(finding, (note/draft_name).read_bytes(), (note/bundle_name).read_bytes())
            completed.append({'paper_id':current,'findings':len(finding['findings']),'finding_set_sha256':runtime.bytes_hash(raw),'status':'PASS_SCHEMA_AND_EXACT_BINDINGS'})
        print(json.dumps({'status':'PASS','rows':completed,'author_disposition_created':False,'semantic_truth_or_detection_completeness_proven':False}))
        return 0
    except Exception as exc:
        print(json.dumps({'status':'STOP_FIRST_FAILURE','paper_id':current,'error':str(exc),'completed':completed}))
        return 1

if __name__ == '__main__':
    sys.exit(main())
