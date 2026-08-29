# Paper 25 Stage-2.5 Claim Registry coverage adjudication

Audit target: `paper/manuscript.tex` SHA-256 `283695c485a2a48abfab1ef0fe3d479f597f68f3082e20f4a5a1894ca37baefb`  
Registry: `claim-registry/1.0` SHA-256 `57063b60063a873d909506e6fcf8c3bd938c4fed57de06cb58beee0daca76956`

## Result

- Registered population: **72** exact UTF-8-bound rows.
- Risk-stratified selection: **48** distinct claims: `45` HIGH-IMPACT, `3` RANDOM, `0` TOP-UP.
- Persisted evidence tuples: **49/49**; exact `(claim_id, ref_slug-or-null)` set equality PASS.
- Mechanically detectable candidates: **1**; unresolved candidates: **0**.
- Coverage replay state: **COMPLETED / zero bounded gaps**.
- Semantic extraction coverage remains exactly **`not_machine_detectable`**; this report never upgrades bounded lexical coverage into a completeness guarantee.
- All evidence carriers are explicitly `anchorless`; they prove registry/tuple conformance but do not independently prove a source excerpt or a semantic verdict. Semantic adjudication lives in `stage2_5_phase_e_semantic_audit.md` and the Phase A--C proof/source audits.

## Supersession record

The first Round-9 sidecar build underclassified numerical, causal, and methods-critical claims and excluded mechanical-origin rows from the RANDOM denominator. It is superseded. The stable build applies ARS #549 to every registry row, checks 100% of HIGH-IMPACT claims, applies the rounded-up 10% sentinel to the complete non-high-impact remainder, and persists one row per selected source tuple.
