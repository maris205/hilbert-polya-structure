# P102--P106 Route-A sequence

Status: **FINAL QA PASS / INTERNAL FREEZE / EXTERNAL HOLD**.

This batch continues the standing five-paper Route-A search for sharply
solvable dynamical systems.  The five phase spaces, actions, and headline
invariants are deliberately different:

| paper | phase space | action | headline invariant |
|---|---|---|---|
| [P102](../../papers/102-cyclic-group-algebra-involution-norm-dynamics/README.md) | a split cyclic group algebra | involutive norm `a -> a a*` | Fourier-orbit fixed sequence and sharp transient depth |
| [P103](../../papers/103-double-adjugate-matrix-dynamics/README.md) | all matrices over a finite field | double adjugation | singular collapse and projective image staircase |
| [P104](../../papers/104-monomial-toggle-contraction-cocycles/README.md) | random products of two monomial matrices | iid left multiplication | folded singular-value CLT and exact annealed pressure |
| [P105](../../papers/105-cycle-minimum-pruning-dynamics/README.md) | the symmetric group | simultaneous cycle-minimum pruning | longest-cycle transient and exact reverse fibres |
| [P106](../../papers/106-synchronous-mis-polarity-dynamics/README.md) | Boolean configurations on a graph | synchronous MIS update | polarity collapse and bipartite zeta square law |

## Final internal freeze

The canonical controls and PDFs give the following frozen Stage-2 packet.
P103 gained 850 exact scalar-line staircase assertions during cross-hostile
strengthening, so the author-freeze total of 24,679,662 is superseded by the
current review total of **24,680,512**.

| paper | PDF pages | exact assertions | independent audit | final gate |
|---:|---:|---:|---|---|
| P102 | 6 | 116,278 | [A](../../papers/102-cyclic-group-algebra-involution-norm-dynamics/HOSTILE_REVIEW_A.md), [B](../../papers/102-cyclic-group-algebra-involution-norm-dynamics/HOSTILE_REVIEW_B.md), [gate](../../papers/102-cyclic-group-algebra-involution-norm-dynamics/HOSTILE_REVIEW.md) | [PASS](../../papers/102-cyclic-group-algebra-involution-norm-dynamics/FINAL_QA.md) |
| P103 | 4 | 141,190 | [A](../../papers/103-double-adjugate-matrix-dynamics/HOSTILE_REVIEW_A.md), [B](../../papers/103-double-adjugate-matrix-dynamics/HOSTILE_REVIEW_B.md), [gate](../../papers/103-double-adjugate-matrix-dynamics/HOSTILE_REVIEW.md) | [PASS](../../papers/103-double-adjugate-matrix-dynamics/FINAL_QA.md) |
| P104 | 5 | 741,486 | [A](../../papers/104-monomial-toggle-contraction-cocycles/HOSTILE_REVIEW_A.md), [B](../../papers/104-monomial-toggle-contraction-cocycles/HOSTILE_REVIEW_B.md), [gate](../../papers/104-monomial-toggle-contraction-cocycles/HOSTILE_REVIEW.md) | [PASS](../../papers/104-monomial-toggle-contraction-cocycles/FINAL_QA.md) |
| P105 | 5 | 17,219,241 | [A](../../papers/105-cycle-minimum-pruning-dynamics/HOSTILE_REVIEW_A.md), [B](../../papers/105-cycle-minimum-pruning-dynamics/HOSTILE_REVIEW_B.md), [gate](../../papers/105-cycle-minimum-pruning-dynamics/HOSTILE_REVIEW.md) | [PASS](../../papers/105-cycle-minimum-pruning-dynamics/FINAL_QA.md) |
| P106 | 4 | 6,462,317 | [A](../../papers/106-synchronous-mis-polarity-dynamics/HOSTILE_REVIEW_A.md), [B](../../papers/106-synchronous-mis-polarity-dynamics/HOSTILE_REVIEW_B.md), [gate](../../papers/106-synchronous-mis-polarity-dynamics/HOSTILE_REVIEW.md) | [PASS](../../papers/106-synchronous-mis-polarity-dynamics/FINAL_QA.md) |
| **total** | **24** | **24,680,512** | two nonauthor passes per paper | **5/5 PASS** |

The five PDFs total **1,562,518 bytes**.  Their canonical SHA-256 values are
sealed in [the PDF manifest](CANONICAL_PDF_MANIFEST.sha256), and every
paper-local `SHA256SUMS` verification passes.

## Evidence map

| paper | manuscript | exact control | claims/control/build evidence | review evidence |
|---:|---|---|---|---|
| P102 | [source](../../papers/102-cyclic-group-algebra-involution-norm-dynamics/main.tex), [PDF](../../papers/102-cyclic-group-algebra-involution-norm-dynamics/main.pdf) | [verifier](../../papers/102-cyclic-group-algebra-involution-norm-dynamics/code/verify_involution_norm.py), [stored output](../../papers/102-cyclic-group-algebra-involution-norm-dynamics/code/verification_output.txt) | [claims](../../papers/102-cyclic-group-algebra-involution-norm-dynamics/CLAIMS_EVIDENCE.md), [controls](../../papers/102-cyclic-group-algebra-involution-norm-dynamics/CONTROL_RESULTS.md), [build](../../papers/102-cyclic-group-algebra-involution-norm-dynamics/BUILD.md) | [hostile A](../../papers/102-cyclic-group-algebra-involution-norm-dynamics/HOSTILE_REVIEW_A.md), [hostile B](../../papers/102-cyclic-group-algebra-involution-norm-dynamics/HOSTILE_REVIEW_B.md) |
| P103 | [source](../../papers/103-double-adjugate-matrix-dynamics/main.tex), [PDF](../../papers/103-double-adjugate-matrix-dynamics/main.pdf) | [verifier](../../papers/103-double-adjugate-matrix-dynamics/code/verify_double_adjugate.py), [stored output](../../papers/103-double-adjugate-matrix-dynamics/code/verification_output.txt) | [claims](../../papers/103-double-adjugate-matrix-dynamics/CLAIMS_EVIDENCE.md), [controls](../../papers/103-double-adjugate-matrix-dynamics/CONTROL_RESULTS.md), [build](../../papers/103-double-adjugate-matrix-dynamics/BUILD.md) | [hostile A](../../papers/103-double-adjugate-matrix-dynamics/HOSTILE_REVIEW_A.md), [hostile B](../../papers/103-double-adjugate-matrix-dynamics/HOSTILE_REVIEW_B.md) |
| P104 | [source](../../papers/104-monomial-toggle-contraction-cocycles/main.tex), [PDF](../../papers/104-monomial-toggle-contraction-cocycles/main.pdf) | [verifier](../../papers/104-monomial-toggle-contraction-cocycles/code/verify_monomial_toggle.py), [stored output](../../papers/104-monomial-toggle-contraction-cocycles/code/verify_monomial_toggle.out) | [claims](../../papers/104-monomial-toggle-contraction-cocycles/CLAIMS_EVIDENCE.md), [controls](../../papers/104-monomial-toggle-contraction-cocycles/CONTROL_RESULTS.md), [build](../../papers/104-monomial-toggle-contraction-cocycles/BUILD.md) | [hostile A](../../papers/104-monomial-toggle-contraction-cocycles/HOSTILE_REVIEW_A.md), [hostile B](../../papers/104-monomial-toggle-contraction-cocycles/HOSTILE_REVIEW_B.md) |
| P105 | [source](../../papers/105-cycle-minimum-pruning-dynamics/main.tex), [PDF](../../papers/105-cycle-minimum-pruning-dynamics/main.pdf) | [verifier](../../papers/105-cycle-minimum-pruning-dynamics/code/verify_cycle_minimum_pruning.py), [stored output](../../papers/105-cycle-minimum-pruning-dynamics/CONTROL_OUTPUT.txt) | [claims](../../papers/105-cycle-minimum-pruning-dynamics/CLAIMS_EVIDENCE.md), [controls](../../papers/105-cycle-minimum-pruning-dynamics/CONTROL_RESULTS.md), [build](../../papers/105-cycle-minimum-pruning-dynamics/BUILD.md) | [hostile A](../../papers/105-cycle-minimum-pruning-dynamics/HOSTILE_REVIEW_A.md), [hostile B](../../papers/105-cycle-minimum-pruning-dynamics/HOSTILE_REVIEW_B.md) |
| P106 | [source](../../papers/106-synchronous-mis-polarity-dynamics/main.tex), [PDF](../../papers/106-synchronous-mis-polarity-dynamics/main.pdf) | [verifier](../../papers/106-synchronous-mis-polarity-dynamics/code/verify_mis_polarity.py), [stored output](../../papers/106-synchronous-mis-polarity-dynamics/code/verification_output.txt) | [claims](../../papers/106-synchronous-mis-polarity-dynamics/CLAIMS_EVIDENCE.md), [controls](../../papers/106-synchronous-mis-polarity-dynamics/CONTROL_RESULTS.md), [build](../../papers/106-synchronous-mis-polarity-dynamics/BUILD.md) | [hostile A](../../papers/106-synchronous-mis-polarity-dynamics/HOSTILE_REVIEW_A.md), [hostile B](../../papers/106-synchronous-mis-polarity-dynamics/HOSTILE_REVIEW_B.md) |

Batch-level provenance and status are recorded in the
[Material Passport](MATERIAL_PASSPORT.md), [Stage-2 report](STAGE2_REPORT.md),
[Stage-2.5 audit](STAGE2_5_REPORT.md), and [final QA report](FINAL_QA_REPORT.md).
The scientific contract and audit boundaries are linked below:

- [problem anchor](PROBLEM_ANCHOR.md)
- [Stage-1 selection report](STAGE1_REPORT.md)
- [candidate/kill ledger](phase1/CANDIDATE_POOL_AND_KILL_LEDGER.md)
- [frozen theorem contracts](phase1/THEOREM_CONTRACTS.md)
- [system-collision firewall](phase1/SYSTEM_COLLISION_FIREWALL.md)
- [proof-spike ledger](proof_spikes/README.md)
- [source-verification report](phase2/SOURCE_VERIFICATION_REPORT.md)
- [canonical PDF manifest](CANONICAL_PDF_MANIFEST.sha256)
- [pipeline state](PIPELINE_STATE.yaml)
- [standing authorization and release boundary](STANDING_WORKFLOW_AUTHORIZATION.md)

Every manuscript remains an internal short paper.  Literature searches are
bounded collision audits, not global novelty certificates.  External
submission, public release, author contact, and priority language remain
**HOLD**.  Internal final QA and hashing do not close the external owner gate,
especially P106's high-risk direct-system collision.
