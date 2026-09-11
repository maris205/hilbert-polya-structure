# Route A — final batch QA receipt for P192–P196

terminal_status=PASS
papers=5
review_packages=10
author_assertions=15387752
review_a_assertions=9347475
review_b_assertions=31782429
grand_evidence_assertions=56517656
pages=20
bibliography_records=25
cold_builds=10
visual_pages=20
pdf_manifest_rows=20
open_findings=critical:0,major:0,minor:0
historical_review_findings=critical:0,major:4,minor:4,all_resolved:true
external_status=OWNER_RED_AMBER_P192;OWNER_AMBER_P193_P196;HOLD_EXTERNAL

This batch QA receipt binds the final cold-build, visual, replay, and manifest
surface for the five-paper Route-A batch. The authoritative mechanical audit
stdout is stored in `qa/CANONICAL.txt` and replayed from `qa/audit_batch.py`.

The preflight audit detected one terminal-artifact wording defect: P194
Review B's replay receipt said that two fresh processes passed but did not
carry the literal `Replay 1` and `Replay 2` labels required by the batch
auditor. Those labels were added without changing the verifier, canonical
transcript, pinned inputs, paper, or mathematical finding census; the review
package and aggregate manifest were then resealed before the successful full
audit. This QA finding is not a manuscript or theorem finding.
