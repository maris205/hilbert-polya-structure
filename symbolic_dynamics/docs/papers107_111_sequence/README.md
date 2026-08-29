# P107–P111 Route-A sequence

Status: **FINAL QA PASS / INTERNAL FREEZE / EXTERNAL HOLD**.

This batch continues the standing five-paper Route-A search for sharply
solvable dynamical systems.  Selection was breadth-first: an exact early
signal had to support a full temporal theorem package, and a candidate was
killed or reserved when its signal failed, its owner boundary was too close,
or its phase/update repeated an occupied repository class.

| paper | phase space and action | concrete theorem advance |
|---:|---|---|
| [P107](../../papers/107-annihilator-power-ideal-dynamics/README.md) | ideals of `Z/NZ`; `I -> Ann(I)^r` | clipped prime-exponent reflection, resonance, parity-sensitive depths/CDF, CRT cycle census and zeta |
| [P108](../../papers/108-capped-fibonacci-dynamics/README.md) | integer square `{0,...,a}^2`; `(x,y) -> (y,min(a,x+y))` | exact capped Fibonacci iterate, full absorption clock/CDF, sharp Fibonacci depth threshold, image and every fibre |
| [P109](../../papers/109-nilpotent-image-subspace-dynamics/README.md) | all subspaces of `F_q^d`; `U -> N(U)` for one regular nilpotent block | exact pointed fibres, joint time/rank kernel, Gaussian absorption layers, periodic/zeta and recovery boundary |
| [P110](../../papers/110-cyclic-shift-join-partition-dynamics/README.md) | partitions of `Z/nZ`; `pi -> pi join rho(pi)` | coset endpoints, Möbius–Bell basins, sharp depth, primitive-chord deepest shell |
| [P111](../../papers/111-positive-heisenberg-word-area-cocycle/README.md) | iid products of `I+E_12` and `I+E_23` | exact word-area law and moments, SLLN/CLT, polynomial norm boundary, `n^2` pressure kink |

## Final internal freeze

| paper | pages | PDF bytes | exact assertions | hostile audit | final gate |
|---:|---:|---:|---:|---|---|
| P107 | 4 | 271,211 | 212,843 | [A](../../papers/107-annihilator-power-ideal-dynamics/HOSTILE_REVIEW_A.md), [B](../../papers/107-annihilator-power-ideal-dynamics/HOSTILE_REVIEW_B.md), [decision](../../papers/107-annihilator-power-ideal-dynamics/HOSTILE_REVIEW.md) | [PASS](../../papers/107-annihilator-power-ideal-dynamics/FINAL_QA.md) |
| P108 | 3 | 269,786 | 67,475,970 | [A](../../papers/108-capped-fibonacci-dynamics/HOSTILE_REVIEW_A.md), [B](../../papers/108-capped-fibonacci-dynamics/HOSTILE_REVIEW_B.md), [decision](../../papers/108-capped-fibonacci-dynamics/HOSTILE_REVIEW.md) | [PASS](../../papers/108-capped-fibonacci-dynamics/FINAL_QA.md) |
| P109 | 5 | 302,089 | 515,379 | [A](../../papers/109-nilpotent-image-subspace-dynamics/HOSTILE_REVIEW_A.md), [B](../../papers/109-nilpotent-image-subspace-dynamics/HOSTILE_REVIEW_B.md), [decision](../../papers/109-nilpotent-image-subspace-dynamics/HOSTILE_REVIEW.md) | [PASS](../../papers/109-nilpotent-image-subspace-dynamics/FINAL_QA.md) |
| P110 | 5 | 321,838 | 1,916,206 | [A](../../papers/110-cyclic-shift-join-partition-dynamics/HOSTILE_REVIEW_A.md), [B](../../papers/110-cyclic-shift-join-partition-dynamics/HOSTILE_REVIEW_B.md), [decision](../../papers/110-cyclic-shift-join-partition-dynamics/HOSTILE_REVIEW.md) | [PASS](../../papers/110-cyclic-shift-join-partition-dynamics/FINAL_QA.md) |
| P111 | 7 | 316,032 | 421,285 | [A](../../papers/111-positive-heisenberg-word-area-cocycle/HOSTILE_REVIEW_A.md), [B](../../papers/111-positive-heisenberg-word-area-cocycle/HOSTILE_REVIEW_B.md), [decision](../../papers/111-positive-heisenberg-word-area-cocycle/HOSTILE_REVIEW.md) | [PASS](../../papers/111-positive-heisenberg-word-area-cocycle/FINAL_QA.md) |
| **total** | **24** | **1,480,956** | **70,541,683** | two nonauthor passes per paper | **5/5 PASS** |

The assertion total is a descriptive sum of heterogeneous exact
falsification checks, not a paper score and not a proof by enumeration.  The
five PDFs contain 86,944 bytes of searchable layout text and 112/112
embedded, subsetted, Unicode-mapped font records.  All 26 paper-local
bibliography entries are cited and resolved.

## Evidence map

| paper | manuscript | exact control | evidence and build |
|---:|---|---|---|
| P107 | [source](../../papers/107-annihilator-power-ideal-dynamics/main.tex), [PDF](../../papers/107-annihilator-power-ideal-dynamics/main.pdf) | [verifier](../../papers/107-annihilator-power-ideal-dynamics/code/verify_annihilator_power.py), [output](../../papers/107-annihilator-power-ideal-dynamics/code/verification_output.txt) | [claims](../../papers/107-annihilator-power-ideal-dynamics/CLAIMS_EVIDENCE.md), [controls](../../papers/107-annihilator-power-ideal-dynamics/CONTROL_RESULTS.md), [build](../../papers/107-annihilator-power-ideal-dynamics/BUILD.md), [seal](../../papers/107-annihilator-power-ideal-dynamics/SHA256SUMS) |
| P108 | [source](../../papers/108-capped-fibonacci-dynamics/main.tex), [PDF](../../papers/108-capped-fibonacci-dynamics/main.pdf) | [verifier](../../papers/108-capped-fibonacci-dynamics/code/verify_capped_fibonacci.py), [output](../../papers/108-capped-fibonacci-dynamics/code/verification_output.txt) | [claims](../../papers/108-capped-fibonacci-dynamics/CLAIMS_EVIDENCE.md), [controls](../../papers/108-capped-fibonacci-dynamics/CONTROL_RESULTS.md), [build](../../papers/108-capped-fibonacci-dynamics/BUILD.md), [seal](../../papers/108-capped-fibonacci-dynamics/SHA256SUMS) |
| P109 | [source](../../papers/109-nilpotent-image-subspace-dynamics/main.tex), [PDF](../../papers/109-nilpotent-image-subspace-dynamics/main.pdf) | [verifier](../../papers/109-nilpotent-image-subspace-dynamics/code/verify.py), [output](../../papers/109-nilpotent-image-subspace-dynamics/code/verification_output.txt) | [claims](../../papers/109-nilpotent-image-subspace-dynamics/CLAIMS_EVIDENCE.md), [controls](../../papers/109-nilpotent-image-subspace-dynamics/CONTROL_RESULTS.md), [build](../../papers/109-nilpotent-image-subspace-dynamics/BUILD.md), [seal](../../papers/109-nilpotent-image-subspace-dynamics/SHA256SUMS) |
| P110 | [source](../../papers/110-cyclic-shift-join-partition-dynamics/main.tex), [PDF](../../papers/110-cyclic-shift-join-partition-dynamics/main.pdf) | [verifier](../../papers/110-cyclic-shift-join-partition-dynamics/code/verify.py), [output](../../papers/110-cyclic-shift-join-partition-dynamics/CONTROL_OUTPUT.txt) | [claims](../../papers/110-cyclic-shift-join-partition-dynamics/CLAIMS_EVIDENCE.md), [controls](../../papers/110-cyclic-shift-join-partition-dynamics/CONTROL_RESULTS.md), [build](../../papers/110-cyclic-shift-join-partition-dynamics/BUILD.md), [seal](../../papers/110-cyclic-shift-join-partition-dynamics/SHA256SUMS) |
| P111 | [source](../../papers/111-positive-heisenberg-word-area-cocycle/main.tex), [PDF](../../papers/111-positive-heisenberg-word-area-cocycle/main.pdf) | [verifier](../../papers/111-positive-heisenberg-word-area-cocycle/code/verify.py), [output](../../papers/111-positive-heisenberg-word-area-cocycle/code/verify.out) | [claims](../../papers/111-positive-heisenberg-word-area-cocycle/CLAIMS_EVIDENCE.md), [controls](../../papers/111-positive-heisenberg-word-area-cocycle/CONTROL_RESULTS.md), [build](../../papers/111-positive-heisenberg-word-area-cocycle/BUILD.md), [seal](../../papers/111-positive-heisenberg-word-area-cocycle/SHA256SUMS) |

## Search discipline and early kills

The strongest falsified candidate was `U -> U+N(U)`: 36,986 adversarial
checks exposed a coefficient-sensitive `F_2^4` counterexample to the proposed
pivot-gap law.  A meet/join subspace comparator passed 1,442,212 assertions
but was reserved because Gerlach's lattice-sorting framework is a direct
neighbor.  Matrix Möbius and Drazin systems were closed mathematically but
killed by the P103/P106 phase and proof-engine firewall.  Other owner-heavy
signals, including cyclic gcd erosion, degree-parity switching, and a clipped
random path automaton, remain reserves rather than papers.

Batch provenance is recorded in the [Stage-1 report](STAGE1_REPORT.md),
[theorem contracts](phase1/THEOREM_CONTRACTS.md), [kill ledger](phase1/CANDIDATE_POOL_AND_KILL_LEDGER.md),
[collision firewall](phase1/SYSTEM_COLLISION_FIREWALL.md), [source report](phase2/SOURCE_VERIFICATION_REPORT.md),
[Stage-2 report](STAGE2_REPORT.md), [hostile-audit report](STAGE2_5_REPORT.md),
[final QA report](FINAL_QA_REPORT.md), [Material Passport](MATERIAL_PASSPORT.md),
and [canonical PDF manifest](CANONICAL_PDF_MANIFEST.sha256).

Every paper remains an anonymous internal short paper.  DOI checks, bounded
searches, hostile review, successful controls, and mechanical QA do not grant
external owner clearance.  Public release, submission, specialist contact,
venue choice, and novelty or priority language remain **HOLD**.
