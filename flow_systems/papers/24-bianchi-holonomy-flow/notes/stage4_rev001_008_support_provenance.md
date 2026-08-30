# P24 Stage-4 support and provenance note for REV-001--REV-008

## Material Passport

- Origin Skill: `ars-codex:academic-research-suite` revision protocol plus deterministic experiment validation
- Origin Stage: Stage 4 supporting work only
- Verification Status: `VERIFIED / REPRODUCIBLE`
- Authority: `BATCH_ROUND9_STAGE4_AUTHORIZATION_REQUEST.md` SHA-256 `174cf1b035c55f72cdc06f1df6eb5e39138cbc9982ed1fb97457189a964ecd63`
- Author event: `BATCH_ROUND9_STAGE4_AUTHOR_EVENT_20260830.txt` SHA-256 `5e5ad1b6ff2a62060368877016ad4b14f869f22a3e38f9a703672ea52ecd067f`
- Anchored base: `notes/stage3_revision_base.tex` SHA-256 `b59bc70c51960f6c89167619df21923c035b4311d9df4e40c034a1fe036cf60e`
- Registered surfaces: 10 surfaces in `notes/stage4_claim_surface_manifest.json`, SHA-256 `2af286143812b1fdd1d1242df2868a8a75f375fa5cd9c1f1f0ff1b2472ce5d64`; no claim-strength replacement is authorized
- Scope: this is evidence for a later block-bounded revision. It is not a manuscript patch and makes no author decision beyond the recorded defaults.

## REV-001 bounded adjacent-work check

The supplied seven-entry bibliography was checked against a bounded primary-source search for (i) first quotients of principal-congruence filtrations, (ii) trace congruences in principal congruence subgroups, (iii) trace-set non-specificity for Bianchi groups, and (iv) trace-of-powers recurrences. Three sources materially constrain originality allocation:

1. Jonathan Lopez, “Lie algebras and cohomology of congruence subgroups for \(\mathrm{SL}_n(R)\),” *Journal of Pure and Applied Algebra* 218 (2014), 256--268, [doi:10.1016/j.jpaa.2013.05.011](https://doi.org/10.1016/j.jpaa.2013.05.011), [arXiv:1001.2071](https://arxiv.org/abs/1001.2071). Theorem 3.2 and Theorem 4.7 identify the successive \(p\)-congruence quotients with traceless matrix data; the proof sends \(I+p^rA\) to the residue of \(A\). Its stated coefficient class includes \(R=\mathbb Z[i]\), and its results include \(n=2\). This is a direct antecedent for the structural first-jet quotient and trace-zero residue, although not for the manuscript's signed unoriented convention, its exact finite collision certificate, or its negative-specificity package.
2. Grant S. Lakeland, “Equivalent trace sets for arithmetic Fuchsian groups,” *Proceedings of the American Mathematical Society* 145 (2017), 445--459, [doi:10.1090/proc/13194](https://doi.org/10.1090/proc/13194), [arXiv:1312.7771](https://arxiv.org/abs/1312.7771). The proof of Corollary 3.6 derives the classical principal-congruence trace form \(\operatorname{tr}\Gamma(n)=\{An^2\mathbin{\pm}2\}\); Theorem 1.3 shows that a Bianchi group has proper finite-index subgroups with the same complex trace set. These are adjacent antecedents for level-squared trace divisibility and for the warning that trace data alone need not identify the group or owner. They do not state the manuscript's arbitrary-commutative-ring formula in terms of \(\det(A)\), nor the frozen Gaussian loxodromic profile.
3. Primo Brandi and Paolo Emilio Ricci, “Composition Identities of Chebyshev Polynomials, via \(2\times2\) Matrix Powers,” *Symmetry* 12 (2020), 746, [doi:10.3390/sym12050746](https://doi.org/10.3390/sym12050746). Theorem 2 gives traces of powers of a nonsingular \(2\times2\) matrix through Chebyshev polynomials. It confirms that the Cayley--Hamilton trace-power recurrence belongs to established matrix theory rather than being an independent novelty center.

No independently published source for the exact combined statement
\[
  D_{m^2}(I+mA)=m^2\det(A)^2-4\det(A)
\]
over every commutative ring with cancellable \(m\), together with the signed-jet laws and the exact negative finite certificate, was located in this bounded check. That absence is not a novelty proof. The safe allocation is therefore:

- do not claim novelty for determinant expansion, the first congruence quotient, trace-zero first-order data, or Cayley--Hamilton recurrences separately;
- present the value as the explicit all-ring synthesis, the separation of universality from source specificity, the frozen exact certificate, and the conservative owner/Route firewall;
- describe the level-three candidate as the project's tested historical candidate unless an independent antecedent is later supplied.

## Exact derivative profile for REV-003

The Stage-4 profile is a strict derivative of already frozen bytes. It reads the Round-7 ledger (SHA-256 `ac15fe34c25d7d570af48672c17989795c92ce4865ad74f2297fcb3c194bd632`), selects the 10,976 rows whose frozen `matrix_class` is `LOXODROMIC`, and retains the corresponding rows of the Round-8 D9/jet profile (SHA-256 `a8dfb74e1c0faf977f47859028a338e131806175cb642b52b27e6f74e0dab326`). The selection introduces no new classifier.

The exact partition is:

| Quantity | Pooled panel | Loxodromic only | Pooled minus loxodromic |
|---|---:|---:|---:|
| Matrix rows | 11,481 | 10,976 | 505 |
| Distinct \(D_9\) values | 145 | 144 | 1 |
| \(D_9\) collision rows beyond first | 11,336 | 10,832 | 504 |
| Distinct joint descriptors | 517 | 508 | 9 |
| Joint collision rows beyond first | 10,964 | 10,468 | 496 |
| Rows separated by the first jet | 372 | 364 | 8 |
| Maximum \(D_9\) bucket | 505 | 208 | 297 |
| Maximum joint bucket | 84 | 84 | 0 |
| Singleton joint buckets | 0 | 0 | 0 |

All 505 excluded rows (1 identity and 504 parabolics) have \(D_9=(0,0)\), and no selected loxodromic row has \(D_9=(0,0)\). On the loxodromic population, the jet raises descriptor count from 144 to 508 (factor \(127/36\), approximately 3.52778), reduces the maximum bucket from 208 to 84 (factor \(52/21\), approximately 2.47619), and separates 364 of 10,832 scalar-collision rows. The remaining 10,468 joint collision rows are \(2617/2708\), approximately 96.6396%, of the scalar-collision rows. Every joint bucket still contains at least two matrix rows.

These are matrix-row counts only. No row is certified primitive, no pair of colliding joint descriptors is certified to represent distinct primitive loxodromic owners, and no finite rate is promoted to the full Bianchi flow.

New bindings:

- `experiments/stage4_loxodromic_profile_manifest.json`: `1860b1a566e2c4a9a3b9362af4947aa2333d2df4728893780341dd79accaae07`
- `code/stage4_loxodromic_profile.py`: `b02c8ee41f6cd5f2b59a1ad4e37a17ca12ad45effa1fefa7b719761c6d9496ea`
- `code/test_stage4_loxodromic_profile.py`: `ff398a2399b37359268f82534ec47e21c47c6bc4e04d0278f7ccee51ebb2fd9d`
- `experiments/reproduce_stage4_loxodromic_profile.sh`: `2d9469e009affd0359b33aff3408f62f88e467ceaf231359994cade4bd8b2450`
- `results/stage4_loxodromic_d9_jet_collision_profile.csv`: `b345988db7f9a5076983d4c3c2fb88e952b9215b9ea46a9605bae3ed6d73a256`
- `results/stage4_loxodromic_d9_jet_metrics.json`: `8e7c2e32b3638b73caa674518f2c19a629e1f708d219a10500cb830792babdcf`
- `experiments/stage4_loxodromic_profile_receipt.json`: `5c0e0bd39812a2714bd05bf429ff3b6e70cf36c3e841ad553026f4082ff3f6fa`

## Remaining roadmap support decisions

| Item | Evidence-bound implementation branch |
|---|---|
| REV-002 | Distinguish the ring-general algebraic theorem from the finite marked-word panel in title and abstract. Preserve the full flow as unassigned and retain all non-title metadata in `B0004` byte-for-byte. |
| REV-004 | No independently timestamped commit or external registry receipt is present in the reviewed Round-7/Round-8 package. Their JSON dates and `FROZEN_BEFORE_*` labels are self-reported historical records. Use “historical freeze record” consistently; do not claim independently established pre-result chronology. |
| REV-005 | The trace-polynomial identity is unconditional for \(\gamma\in\mathrm{SL}_2(R)\). The normalized \(D_{m^2}\) consequence additionally requires \(\gamma=I+mA\) and cancellability of \(m\); those hypotheses should be repeated at the consequence. |
| REV-006 | The dependency order is: sampled descriptor \(\to\) unbuilt complete primitive-owner ledger \(\to\) unbuilt geometric coding/cross-section with the geometric clock \(\to\) unbuilt orbit weights and transfer object \(\to\) unproved convergence/regularization and determinant/Euler/spectral consequences. Every downstream node remains unconstructed. |
| REV-007 | The operative proved equivalence is conjugacy by the level subgroup \(\Gamma(3)\), with inversion handled by the sign quotient. Ambient Bianchi conjugacy acts through the reduced adjoint action and is not an invariant quotient established here. |
| REV-008 | The missing third canonical control is an **unexecuted matched-distribution noncongruence matrix ensemble**. Before execution, declare the matching variables and the prediction: after removing principal level-(3) membership, universal \(D_9\)-integrality should not persist (nonintegral witnesses must occur), while the principal-congruence theorem itself is unaffected. The first jet is not defined on rows lacking exact division by 3. Coverage remains two of three until this control is separately frozen and run. |

## Route and claim firewall

The only preserved tuple is

```text
(A0_WEAK_ARITHMETIC_RELATION, A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL)
overall = ROUTE_A_EXPLORATORY
FULL_BIANCHI_FLOW_ROUTE_A_TUPLE=UNASSIGNED
ROUTE_B_INVOCATION_ALLOWED=false
```

Nothing in this support work supplies a matched primitive-owner census, a Gaussian-prime label, positive A2, a dynamical determinant, A3, A4, or Route B. Registered ClaimIntent surfaces must remain byte-exact inside any later authorized replacement block.

## Validation record

The following commands completed with exit status 0 on 30 August 2026:

```text
python3 code/test_stage4_loxodromic_profile.py -v
bash experiments/reproduce_stage4_loxodromic_profile.sh
bash experiments/reproduce_round7.sh
bash experiments/reproduce_round8.sh
```

The new suite passed 10 of 10 direct tests. The historical Round-7 and Round-8 suites passed 12 of 12 and 14 of 14 tests, respectively; their two-build byte comparisons and verify-only checks also passed. A pre/post SHA-256 audit checked 124 pre-existing non-bytecode files with no mismatch. The anchored base, manuscript, canonical Round-7 ledger/metrics, canonical Round-8 profile/metrics, and both canonical receipts retain their pre-work hashes.
