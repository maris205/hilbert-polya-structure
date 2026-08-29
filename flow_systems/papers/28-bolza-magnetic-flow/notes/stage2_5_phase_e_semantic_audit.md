# Paper 28 Stage-2.5 Phase-E semantic audit

Audit target: `paper/manuscript.tex` SHA-256
`864d2f6ce0f76245d4d4237ba2981b3e82fc8e31f7991f1f331817f7c028aec7`.

## Determination

**80/81 selected distinct claims VERIFIED and one MINOR_DISTORTION recorded
within the proof, source, and frozen-artifact scope.** The stable selection comprises 78 HIGH-IMPACT
claims and three RANDOM sentinels from an 85-claim registry. Those claims
expand to 84 `(claim_id, ref_slug-or-null)` evidence tuples; the exact tuple
set is complete.

This semantic determination supersedes the earlier six-claim manual table and
its initial 81/81 verdict. The authorized Phase-A metadata repairs and
scholar-owned experiment declaration/provenance are evaluated by the current
controlling Stage-2.5 report rather than inferred here.

### Non-blocking sequencing distortion — `P28-E1-072`

The manuscript says the verifier first checks source/upstream digests and then
reconstructs the finite state component. In the checked builder,
`finite_traversal()` runs before `build_validation()` checks those locks. The
verify-only wrapper still builds only in fresh temporary directories and
copies nothing to canonical results unless validation succeeds, so this does
not alter the reported counts, hashes, or theorem result. It is nevertheless
an inaccurate ordering description and is recorded as `MINOR_DISTORTION` for
later manuscript correction rather than silently marked verified.

## Audit basis

- All 10 registered numerical/data surface families were traced through the
  exact normal-form proof, finite-component completeness theorem, systole
  proof, certificate, validation JSON, receipt, and fresh deterministic replay.
- The 104 historical tests and 24 Round-8 replay tests passed. Exact counts,
  histogram totals, source locks, and serialized hashes reconcile.
- Every internal selected claim remains within the manuscript's stated
  quantifiers, fixed parameter `u=e^{-1/10}`, cutoff `21/10`, and negative
  Route-A scope. No selected claim promotes the 144 equality states to a
  conjugacy/geodesic count or claims that the unexecuted Bolza/magnetic
  comparison exists.
- All nine citation contexts are semantically supported by the official or
  author-version locators recorded in `stage2_5_independent_audit.md`.

Verdict counts: `VERIFIED=80`, `MINOR_DISTORTION=1`,
`MAJOR_DISTORTION=0`, `UNVERIFIABLE=0`, and
`UNVERIFIABLE_ACCESS=0`.

## Source-bearing selected claims

Six selected claims carry nine reference tuples. The full locator and
short-excerpt table is in `stage2_5_independent_audit.md`, Phase E. It covers:

- `P28-E1-004`: `Nazarenko2013`, `AigonDupuyEtAl2005`;
- `P28-E1-010`: `Nazarenko2013`;
- `P28-E1-020`: `Popescu2024`;
- `P28-E1-021`: `Takeuchi1975`;
- `P28-E1-023`: `Voight2009`, `DespreEtAl2023`;
- `P28-E1-024`: `Nazarenko2013`, `AigonDupuyEtAl2005`.

The content use of all nine tuples is supported. The separate author and
subject metadata defects for `Nazarenko2013` and `AigonDupuyEtAl2005` remain
blocking under Phase A.

## Evidence-carrier limitation

All 84 persisted evidence rows are deliberately `anchorless`. Their schemas,
hash bindings, exact claim objects, tier labels, verdict consistency, and
tuple coverage pass; the rows themselves do not reproduce or independently
authenticate an external excerpt. The semantic verdict instead rests on this
recorded review, the complete Phase-B context audit, the Phase-C proof/artifact
audit, and the frozen replay. Semantic extraction completeness remains
`not_machine_detectable`.
