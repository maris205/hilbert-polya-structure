# Paper 27 Stage-2.5 Claim Registry coverage adjudication

Audit target: `paper/manuscript.tex` SHA-256 `c2809011a722b81732952d889f194549adea58875b605dbafe58ada93de9b4b9`  
Registry: `claim-registry/1.0` SHA-256 `05455f35794381fc5f472baaa56cdd2fedaf3d3cbdb99f58f344364c26893452`

## Result

- Registered population: **77** exact UTF-8-bound rows.
- Risk-stratified selection: **70** distinct claims: `67` HIGH-IMPACT, `3` RANDOM, `0` TOP-UP.
- Persisted evidence tuples: **71/71**; exact `(claim_id, ref_slug-or-null)` set equality PASS.
- Mechanically detectable candidates: **7**; unresolved candidates: **0**.
- Coverage replay state: **COMPLETED / zero bounded gaps**.
- Semantic extraction coverage remains exactly **`not_machine_detectable`**; this report never upgrades bounded lexical coverage into a completeness guarantee.
- All evidence carriers are explicitly `anchorless`; they prove registry/tuple conformance but do not independently prove a source excerpt or a semantic verdict. Semantic adjudication lives in `stage2_5_phase_e_semantic_audit.md` and the Phase A--C proof/source audits.

## Supersession record

The first Round-9 sidecar build underclassified numerical, causal, and methods-critical claims and excluded mechanical-origin rows from the RANDOM denominator. It is superseded. The stable build applies ARS #549 to every registry row, checks 100% of HIGH-IMPACT claims, applies the rounded-up 10% sentinel to the complete non-high-impact remainder, and persists one row per selected source tuple.
