# Claims--Evidence Map

## Input lock

The writer uses three immutable input trees.  Their complete byte-level
inventory is `INPUT_MANIFEST.json` (SHA-256
`3102dac1842590882581563ec3046dcb436e792f16d7fd4b2fcbd6a9d360896d`).
The principal frozen manifests are:

| Input | Manifest / tree anchor | Audit status |
|---|---|---|
| `/tmp/p49_tree_stage2` | `bea7a189ea0b3472cc6b469eb36e6460b60c4bae66265659b19af6e89883f0da` | internally proved and validated; held for audit |
| `/tmp/p49_tree_cross_audit` | `273f18e57b55f4fac76cefc3f9544e8d180508cc2297bdd9e4a3c781edb082d6` | `STAGE2_CLEAN`; 56,710 independent exact assertions |
| `/tmp/p49_tree_independent_audit` | tree record `59b8451bd0356e70d95295209d60b5d128882e51afb5774ae806770dea450765` | `STAGE2_CLEAN`; 127,500 independent composition checks |

The manuscript treats exact computation as verification evidence, never as a
replacement for the universal proofs.

## Core claims

| ID | Manuscript claim | Universal proof evidence | Exact finite evidence | Source/positioning boundary | Status and location |
|---|---|---|---|---|---|
| Q0 | For every equiprobable fixed-phase stratum used in the paper, Hausdorff dimension in the tree metric is the liminf of normalized log cylinder counts. | Stage-2 `PROOF_PACKAGE.md`, Lemma 1; cross-audit `PROOF_REAUDIT.md`, C0, including the closed-ball endpoint and Frostman inequality direction. | Independent prefix/cylinder recurrences in both audits. | The metric and ball scale are owned by Ban--Lai--Wu (BLW); no BLW dimension equality is imported. | Supported; Preliminaries and Appendix A. |
| Q1 | A complete cyclic core with phase sizes `a_j` has dimension `min_j H_j(log a)` with the exact backward-index kernel. | Stage-2 Lemmas 2--3; cross-audit C1 off-by-one derivation. | 13,302 internal prefix identities; 4,734 internal and independent residue checks; 37,440 additional root-audit residue checks. | Presented as the supporting irreducible calculation, not as a priority claim over BLW irreducible theory. | Supported; Section 4. |
| Q2 | The unrestricted one-level strictly transient feeder has dimension equal to a finite max--min over integer phase compositions of its `d` children; explicitly declared finite-composition one-level variants use the same finite-union argument. | Stage-2 Lemma 4 and Theorem 5; independent C2 finite-union proof. Concentrated compositions recover Q1 and show that the feeder maximum dominates every core-root stratum. | 6,219 exhaustive one-level compositions; 12,438 prefix identities; 1,086 recursive feeder counts; 127,500 broader independent compositions. | Restricted to complete cyclic blocks, the stated one-level phase access, and no return edge; no arbitrary transient-feeder inference. | Supported; Section 4. |
| Q3 | The spectral mean `bar(c)` is an upper bound for every allocation, and equality holds exactly when the circular convolution of allocation and phase log-sizes is constant. | Stage-2 Lemma 6 and Theorem 7; cross-audit C3 kernel-invertibility proof. | 6,219 exact convolution identities and saturation equivalences; 127,500 independent equivalences. | No external nonlinear Perron--Frobenius equality is used. | Supported; Section 5. |
| Q4 | `p` dividing `d` is universally sufficient for saturation; necessity holds only when every nonzero Fourier mode of `c` is nonzero. | Stage-2 Theorem 8; cross-audit Fourier proof. | 135 uniform-saturation cases; exact negative witness `p=4,d=2,a=(2,3,2,3),m=(1,1,0,0)` with all shifted products equal to `6`. | The manuscript must never state an unconditional divisibility iff. | Supported with explicit extra hypothesis; Section 5. |
| Q5 | For two phases, both core and optimized feeder dimensions have closed parity-sensitive formulas, including the equal-phase boundary. | Stage-2 Theorem 9; cross-audit C5. | 175 parameter cases, 1,050 fixed-composition formula checks; 80 even saturation and 60 odd deficit cases. | Exact special case, not an empirical fit. | Supported; Section 6. |
| Q6 | For the canonical unrestricted `L`-level forced chain, the exact denominator is `d^L`; the optimized dimensions are monotone, lie below `bar(c)`, and approach it with an explicit `O(d^{-L})` bound. | Stage-2 Theorem 10; cross-audit C6, including the embedding `m -> d m` and balanced integer construction. | 10,212 exact `L`-level compositions and prefix checks; 36/36 independent optimizer matches; 39 exact divisibility hits; 9 additional nested-grid checks. | A restricted-multilevel variant requires an explicit balanced-access assumption; arbitrary finite strictly transient feeder shapes and return edges remain excluded. | Supported; Section 7. |
| Q7 | A four-state reducible example has cyclic-core dimension `log 2/3` but full dimension `log 2/2`, disproving an arbitrary Hausdorff cyclic-essential-SCC maximum formula. | Stage-2 Corollary 11; two independent reproofs. | Direct recursive adjacency control and exact prime-log comparison in both audits. | Ban et al. (2021, 2022) already own the analogous reducible topological-entropy phenomenon; only the Hausdorff calculation is residual here. | Supported; Section 8. |

## Methodological evidence

| Evidence family | Frozen count | Intended manuscript use | Forbidden inference |
|---|---:|---|---|
| Stage-2 exact assertions | 73,517 | Reproducibility ledger and algebra/index regression checks | Universal proof from finite census |
| Cross-audit exact assertions | 56,710 | Independent implementation agreement | Novelty or publication priority |
| Root independent profiles | 1,740 | Broader profile coverage | Exhaustiveness over all parameters |
| Root independent compositions | 127,500 | Constant-convolution and optimizer stress test | General reducible theorem |
| Mutation controls | 6 | Demonstrate why each frozen hypothesis matters | A taxonomy of every possible failure |

## Required nonclaims

The article will state all of the following explicitly.

1. It does not prove a variational formula for arbitrary reducible incidence
   matrices.
2. It does not cover feeder return edges, nontransient reuse, or incomplete
   cyclic blocks.
3. It does not cover arbitrary finite strictly transient feeder shapes.  Its
   multilevel theorem is for the canonical unrestricted forced chain;
   restricted multilevel variants require balanced access.
4. It does not make divisibility necessary without the full Fourier-support
   assumption.
5. It does not import the version-sensitive BLW primitive/equality clauses.
6. It does not claim firstness or exhaustive novelty; the bounded search found
   no exact collision.
7. The exact programs are proof companions and falsification controls, not
   numerical experiments supporting asymptotic truth.

## Figure/table evidence provenance

| Planned item | Evidence source | Reproducibility rule |
|---|---|---|
| Fig. 1 transient-to-cyclic phase schematic | Frozen definitions only | Pure TikZ source; no external raster asset. |
| Fig. 2 two-phase parity profile | Q5 closed formulas | Script computes values directly from the displayed formulas and emits canonical CSV/JSON before plotting. |
| Fig. 3 exact optimizer and balanced-gap curves | `p49_tree_stage2/evidence/level_l.json` plus formulas in Q6 | Derivation script copies only cited rows to canonical JSON and records the source SHA-256. |
| Table 1 owner/scope comparison | Verified primary sources and `SOURCE_LOCK.md` | Every row tied to a DOI/arXiv primary record; no priority column. |
| Table 2 validation ledger | Frozen JSON and both audit receipts | Counts and hashes only; no fabricated performance metric. |
