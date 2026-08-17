# SD-C42 independent selection and terminal provenance audit — final correction

## Decision rule and chronology

The active rule is the machine-literal rule in the replacement
`SOURCE_LOCK.md`: retain a historical card exactly when it has a proved
nonempty intrinsic primitive/repetition ledger and its historical A2 verdict
is exactly `A2_ANALYTIC_DETERMINANT`; then maximize literal A3 followed by A4,
with low ID only as a final tie break.

This corrective audit was written after provisional Paper-40 outputs,
in-flight corrective smoke-test outputs, and the DA M1--M20 findings were
known. It is not presented as an untouched prospective selection. Its only
timing claim is that the exact corrected input set enumerated in
`CONTROL_LOCK.md` is frozen before the one canonical empty-results replacement
rerun. Dependent proof/Route/literature/report bytes are post-run renderings,
not prospective inputs. The independence claim is
narrower: the rule uses only the six pre-existing Session-4 cards and does not
import a ranking or authorization from Paper 39.

## Mechanical six-card table

| Candidate | Proved nonempty intrinsic primitive/repetition ledger | Historical A2 verdict exactly analytic determinant | Survives | A3 | A4 |
|---|---:|---:|---:|---|---|
| SD-C01 | yes: primitive necklaces | yes | **yes** | `A3_FAIL` | `A4_FAIL` |
| SD-C02 | yes: one period-one zero primitive orbit | yes: `D_AM=1-z` | **yes** | `A3_FAIL` | `A4_FAIL` |
| SD-C03 | yes: primitive renewal necklaces | no: `A2_FAIL` | no | `A3_FAIL` | `A4_FAIL` |
| SD-C04 | yes: historical primitive digit necklaces | yes | **yes** | `A3_PARTIAL_ANALYTIC_STRUCTURE` | `A4_FORMAL_HINT` |
| SD-C05 | no: acyclic and no primitive cycles | no: `A2_FAIL` | no | `A3_FAIL` | `A4_FAIL` |
| SD-C06 | no intrinsic primitive-cycle ledger | no: `A2_FAIL` | no | `A3_PARTIAL_ANALYTIC_STRUCTURE` | `A4_FAIL` |

The survivor set is exactly `{SD-C01, SD-C02, SD-C04}`. `SD-C04` uniquely
wins the A3 comparison; A4 is therefore not needed to break a tie but is still
checked in the declared order. The filter does not remove `SD-C02` for being
trivial. It does not relabel `SD-C03`'s local determinant as an analytic A2
pass.

The corrected reference and independent evaluators must parse all six exact
cards, verify the hashes below, reproduce this table, and reject dedicated
selection mutations. A prose table alone is not selection evidence.

### Frozen per-card evidence-anchor schema

The historical YAML has no uniform `ledger_nonempty` boolean. The parser must
therefore validate the following exact, prospectively fixed YAML anchors; it
may not infer eligibility from candidate IDs or a preset survivor list.

| Card | Exact nonempty-ledger anchor(s) | Exact A2 anchor |
|---|---|---|
| SD-C01 | `a1.evidence_status=PROVED`; `a1.metrics.formula_degree_cutoff=12`; `a1.metrics.all_repetition_checks_pass=true` | `a2.verdict=A2_ANALYTIC_DETERMINANT`; `a2.evidence_status=PROVED` |
| SD-C02 | `a1.evidence_status=PROVED`; `a1.metrics.fixed_points_every_period=1`; `a1.metrics.primitive_orbits="one period-1 zero orbit"` | `a2.verdict=A2_ANALYTIC_DETERMINANT`; `a2.evidence_status=PROVED` |
| SD-C03 | `a1.evidence_status=PROVED`; `a1.verdict=A1_WEAK`; exact `a1.strongest_evidence` contains `primitive-necklace and repetition expansion` | `a2.verdict=A2_FAIL`; `a2.evidence_status=PROVED` |
| SD-C04 | `a1.evidence_status=PROVED`; `a1.metrics.primitive_necklaces_max_cutoff=63319`; `a1.metrics.repetition_matrix_failures=0` | `a2.verdict=A2_ANALYTIC_DETERMINANT`; `a2.evidence_status=PROVED` |
| SD-C05 | `a1.evidence_status=PROVED`; `a1.metrics.directed_cycles=0`; exact `a1.strongest_failure` contains `no primitive cycles or repetitions` | `a2.verdict=A2_FAIL`; `a2.evidence_status=PROVED` |
| SD-C06 | `a1.evidence_status=NOT_TESTABLE`; `a1.metrics.primitive_orbit_count=not_applicable` | `a2.verdict=A2_FAIL`; `a2.evidence_status=NOT_TESTABLE` |

The derived nonempty field is true for C01--C04 and false for C05--C06.
Survival is `derived_nonempty AND (a2.verdict ==
A2_ANALYTIC_DETERMINANT)`, which yields C01/C02/C04. An evaluator must reject
any card whose anchor set does not match the frozen schema instead of falling
back to prose heuristics.

## Immutable six-card inputs

All paths are relative to the authority repository and were read only.

| Candidate | Route-card path | SHA-256 |
|---|---|---|
| SD-C01 | `symbolic_dynamics/papers/01-falsification-first-audit/evaluations/route_a/SD-C01/20260812T090631Z.yaml` | `ee47a9c90c6bfbc54ba6b09b21f416dcece58b0d0ba9a391ca196d1b41d365a2` |
| SD-C02 | `symbolic_dynamics/papers/01-falsification-first-audit/evaluations/route_a/SD-C02/20260812T090631Z.yaml` | `5b5e9a2fe33a0ba8d281cf59c8f5346b95033c655d258554c0f76f8cfa0a434f` |
| SD-C03 | `symbolic_dynamics/papers/01-falsification-first-audit/evaluations/route_a/SD-C03/20260812T090631Z.yaml` | `2263b1c7bac4336628f444ded88e4e2ad98117f430113faf1ea5a91c16380328` |
| SD-C04 | `symbolic_dynamics/papers/01-falsification-first-audit/evaluations/route_a/SD-C04/20260812T090631Z.yaml` | `0609076081ccd69e9ffa3e0f708d426a33f7d41e2884f90bb2792bbc90209a92` |
| SD-C05 | `symbolic_dynamics/papers/01-falsification-first-audit/evaluations/route_a/SD-C05/20260812T090631Z.yaml` | `4a18295b1e20245c7196f21be4e4afc52857bf981efb461556720ab9e8ab5ed1` |
| SD-C06 | `symbolic_dynamics/papers/01-falsification-first-audit/evaluations/route_a/SD-C06/20260812T090631Z.yaml` | `d93683662a0cbee8e07d79329477d8b60bb273fb72e4bd64c05847e09a576c1b` |

Additional frozen inputs:

| Role | Relative authority path | SHA-256 |
|---|---|---|
| Route criteria | `symbolic_dynamics/skills/route-a-evaluator.md` | `29bd6275aa0c80ecce9cca898f06687208475c0a9a40cf3b9592fde45951458a` |
| Session-4 global lock | `symbolic_dynamics/papers/01-falsification-first-audit/SESSION4_PREREGISTRATION.md` | `681757d86d882384eb5bdbdddba11e04aeb69228bae98707b404535b753e3d25` |
| Global registry | `symbolic_dynamics/papers/01-falsification-first-audit/docs/candidate_registry.md` | `0e29fcfd37c3f048573ff3d705961de65ceb57a7421d5272ccaa586367a5d86c` |
| SD-C04 derivation | `symbolic_dynamics/papers/01-falsification-first-audit/farey_gauss_transfer/DERIVATION_PACKAGE.md` | `c5a246e213695160be76d616e69864d73dae42cf072c944ec6986a10c637b586` |
| Session-4 literature audit | `symbolic_dynamics/papers/01-falsification-first-audit/docs/LITERATURE_AUDIT.md` | `f57b0318ca54e83420d7ad6e4935b35c7b7c0faa6c28204ba9cfc114a130b28a` |

## Paper-39 terminal-clean promotion provenance

Paper 39 is used only to establish terminal-clean provenance and the existence
of the pre-existing registry. It contributes no Paper-40 selection score.

- P39 source-lock SHA-256:
  `70456aff0b3afff0fe78336da3af7f2fc47724eb59674bf50bb7de4f1857770b`.
- Root research evaluation
  `papers/39-affine-obstruction-dag-closure-certificate/ROUTE_A_EVALUATION.yaml`
  remains the immutable pending-triple artifact, SHA-256
  `7bdb90811575a96518c2f67510ef9deb4335e2051c965643f7e3572e806ff6cd`.
- Final sealed canonical card
  `papers/39-affine-obstruction-dag-closure-certificate/evaluations/route_a/SD-C41/2026-08-16.yaml`
  has SHA-256
  `3a5da787a2d20439f345610b7523a565bf1eb55a618b977933ef1046eab0dbb8`
  and resolves the terminal triple without mutating the research artifact.
- Stage-1 artifact Git commit:
  `0f194edbfd05af853153043a568ffafd6c2f8afb`.
- Stage-2 metadata Git commit and observed authority `HEAD`:
  `18530b90317f6efc43ec2e4601ed8cef57daaddc`, a direct child of Stage 1.
- `PAPER_MANIFEST.sha256` SHA-256:
  `9fe17f0e746fa57a3dbbec7c96d4578b480b6cebcd04c7cb1be03209692516bd`
  (91 entries).

Thus the former “P39 dirty/gated” prose is superseded. The promotion gate is
satisfied by independent terminal auditing, while the explicit P39
no-ranking/no-proposal boundary remains in force.

## Coordinate isolation

- `SD-C04` supplies the one-digit Gauss phase space, branches $\phi_a$,
  digit matrices, derivative potential, Mayer operator $\mathcal L_s$,
  function space, and analytic determinant $\det(I-\mathcal L_s^2)$. Its
  historical primitive type is `SigmaPrimitiveDigit`.
- Paper 40 newly freezes the even iterate as the re-indexed pair object
  $X_2$ with its one-pair shift $\rho$, conjugate to digit-space $\sigma^2$
  by the grouping map $\iota$, with type `RhoPrimitivePair`. Pair symbols,
  rotation/reversal metadata, the odd/even splitting census, raw-index
  reversal in $K_s^k$, pair completeness, and A1 credit must be established by
  the corrected Paper-40 proof and evaluators; none is inherited from the
  historical C04 A1 verdict.
- `SD-C01` and `SD-C02` are losing survivors, not coordinate donors.
- `SD-C05` supplies no prime generator; `SD-C06` supplies no zeta quotient or
  arithmetic observable.
- Papers 34--39 supply scope and terminal provenance only. No affine object,
  marker, operator, determinant, or score transfers.
- The three Paper-40 projections are exact functions of the same `SD-C04`
  monodromy; they are not candidate-coordinate imports.

## Internal priority and corrected claim boundary

Paper 1 owns the qualitative projection mismatch, the 7,018-group finite
collision census, and the next-test request. Paper 40 claims only scoped exact
closure with exactly three projections, explicit witnesses, all-order trace
repetition, clock and marker preservation, and absence of a declared scalar
selector in the untwisted schema. It claims neither discovery nor witness
minimality.

The correction itself carries no novelty credit. Its active chronology is:
v1 provisional results and in-flight corrective smoke tests were inspected;
DA found M1--M20; one exact corrected input set is then frozen before the
canonical empty-results replacement execution. Later package renderings have
no prospective status.

## Replacement promotion checklist

- [x] Paper 39 is independently terminal-clean at the ancestry above.
- [x] Root governance accepted SD-C42 as the scoped authority candidate.
- [x] The six-card rule includes `SD-C02` without a post-hoc filter.
- [ ] Both corrected parsers reproduce all six cards, three survivors, and the
      unique winner and reject all selection mutations.
- [ ] The replacement literature audit binds to the exact final source hash.
- [ ] The final canonical controls and prototype are run only after
      `CONTROL_LOCK.md` is hashed; in-flight smoke tests are not results.
