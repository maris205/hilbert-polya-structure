# Paper 28 Stage-2.5 Claim Registry coverage adjudication

Audit target: `paper/manuscript.tex` SHA-256 `864d2f6ce0f76245d4d4237ba2981b3e82fc8e31f7991f1f331817f7c028aec7`  
Registry: `claim-registry/1.0` SHA-256 `031e04aae854667ba03e4b39d8df28fa61391264ab7f8c1fee55d6d6a3514f07`

## Result

- Registered population: **85** exact UTF-8-bound rows.
- Risk-stratified selection: **81** distinct claims: `78` HIGH-IMPACT, `3` RANDOM, `0` TOP-UP.
- Persisted evidence tuples: **84/84**; exact `(claim_id, ref_slug-or-null)` set equality PASS.
- Mechanically detectable candidates: **5**; unresolved candidates: **0**.
- Coverage replay state: **COMPLETED / zero bounded gaps**.
- Semantic extraction coverage remains exactly **`not_machine_detectable`**; this report never upgrades bounded lexical coverage into a completeness guarantee.
- All evidence carriers are explicitly `anchorless`; they prove registry/tuple conformance but do not independently prove a source excerpt or a semantic verdict. Semantic adjudication lives in `stage2_5_phase_e_semantic_audit.md` and the Phase A--C proof/source audits.

## Supersession record

The first Round-9 sidecar build underclassified numerical, causal, and methods-critical claims and excluded mechanical-origin rows from the RANDOM denominator. It is superseded. The stable build applies ARS #549 to every registry row, checks 100% of HIGH-IMPACT claims, applies the rounded-up 10% sentinel to the complete non-high-impact remainder, and persists one row per selected source tuple.
