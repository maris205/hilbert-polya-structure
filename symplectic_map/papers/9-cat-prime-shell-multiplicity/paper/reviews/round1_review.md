# Independent Manuscript Review — Round 1

Review date: 2026-08-15 UTC  
Candidate: `cat_prime_shell_multiplicity_obstruction_v1`  
Manuscript: *A Multiplicity Audit for Prime-Torsion Euler Products of the Cat Map*  
Reviewer role: fresh independent mathematical, domain, reproducibility, journal-fit, and devil's-advocate reviewer  
Recommendation: **MINOR REVISION**  
Confidence: **5/5** for the mathematics and local artifact audit; **4/5** for literature completeness because this review was intentionally offline  
Overall score: **83/100 (8.3/10)**

## Executive assessment

The scientific core passes. I found no Critical or Major defect in the
split/inert/binary/ramified orbit classification, the uniform odd-prime
multiplicity bound, the separation of raw returns from external orbit
labels, the fixed-scalar denominator obstruction, the exact zero-weight
boundary, the equal-weight repetition failure, the fractional
Jordan-totient identity, or the stated convergence strips. In particular,
the proof never assumes maximal matrix order, the ramified (p=5) shell
retains both periods (2) and (10), and the polynomial-degree theorem is
kept strictly inside its pure-denominator and (z)-independent scalar scope.

The manuscript also handles its unusually strong prior-art collision
honestly. Gaspari and Baake--Neumärker--Roberts are cited at the orbit
classification, classical zeta and weighted-product sources delimit the
formal machinery, and the five development-seen rows are never promoted to
an all-prime proof. The surviving contribution is therefore what the title
says: a low-novelty semantic and mechanism audit, not a new cat-map orbit
classification or dynamical-zeta theory.

Four bounded publication/integrity fixes remain. The Appendix-B claim IDs
have drifted from the final claim manifest; a numerical internal novelty
score is presented as manuscript prose without a scholarly calibration
method; internal sequence labels “Paper 9/Paper 10” prevent the paper and
Figure 3 from being fully standalone; and Figure 1's actual linear axis does
not match the frozen plan's logarithmic-axis description. None changes a
theorem, requires a candidate or test rerun, or calls for new scientific
scope.

## Review scope and immutable bindings

This was a read-only review of the bound source and PDF, source lock, proof
package, raw result, strict result manifest, official reports, citation
ledger, bibliography, figure package, prior independent reviews, and all
pre-review manifests. Apart from this report, I changed no paper, plan,
figure, source, code, experiment, result, or manifest artifact. I did not
invoke the candidate or test suite, enumerate another prime or composite
shell, compute a centralizer, evaluate a numerical value of (s), (p^{-s}),
or (log p), access a prime table or Riemann-zero datum, or use the network.

The principal live bindings reproduce exactly:

| Role | SHA-256 |
|---|---|
| manuscript source | `67afe346285a1a1f322a437c19f14316164fbd0c9066d30e4012ce7ee0b90965` |
| pre-review PDF | `9b63f190e7c751c27682d1a9cc9246f0153edddfec61d4539c573ab70070d51c` |
| source lock | `662809d40f7e409e439983774a36349b90f265616a488061fda3c5b9064c2d49` |
| proof package | `47216ad4021d3476bfd0850ebec24c9ceafb5af8c0573214182fd2d0da7b2daa` |
| independent source review | `9509278ce55d908dba7d7cb4a809a335cc51d9364e8bfdfd1dc66be594775b8f` |
| raw exact result | `448de06e92bd7ab4e5374e5d1f57413df45859cd3476ff14b2691b63ac364fab` |
| strict result manifest | `8ca12744638a47b6e4fa3239a60a19d79229d2b9596ae4fe4b2f66a399618f92` |
| independent result-integrity review | `aa0c7db555f11920c7305be508f6cfff62375970e112e9f720111831da20b3bd` |
| independent plan/figure/citation review | `f8c22bfba9299230a8e2051c089863bf6603ebcb84e5e42955ecbf36a874ec06` |
| citation-verification ledger | `ae25c56d17703ee00b8168eba33bbec77c688e72c8fb6ac520214e523241b808` |
| bibliography | `37ee7c23398806b9e59e86ec9fbf6fd0dfc0483043cff9459d0837b2bd2457ae` |
| figure manifest | `8ae2709444e6e06286b061635352d2ba0c419c04d313edf1272cb57ab41b2b83` |

I independently reproduced every non-self evidence hash listed in the
strict result manifest and its exact nine-file final `results/` inventory.
The unique claim and terminal record agree on `REGISTERED_RUN_0001`, exactly
one registered exact audit and one registered run, the five locked primes,
zero candidate numerical runs, and terminal state `COMPLETED_CERTIFIED`.
The pre- and post-execution JUnit files report 23/23 tests with zero failure,
error, or skip; they were inspected as frozen evidence and were not rerun.

## Strengths

### S1. The all-prime orbit theorem is elementary, exhaustive, and correct

The split proof uses only diagonalization and the shared order of
(lambda,lambda^{-1}); the inert proof uses multiplication in
(mathbb F_{p^2}); and the binary and ramified cases are closed directly.
The argument establishes exact periods before dividing shell cardinality by
orbit length.

**Evidence Anchor**: `equation: manuscript Theorem 2.1 and equations (4)--(7) — split, inert, p=2, and p=5 cases`

### S2. The two product semantics are not conflated

The fixed-point exponential correctly retains (|gamma|) through its
Birkhoff sum, while the separately defined external label assigns one
(p^{-s}) variable per primitive orbit. The mixed (p=5) factor is used as
an effective stress test.

**Evidence Anchor**: `equation: equations (9)--(14) — raw fixed-point ledger, mixed p=5 factor, and label coefficient m_p/r`

### S3. The obstruction and every escape boundary are scoped sharply

The degree proof covers only fixed nonzero scalar linear denominators; zero
weights, equal weights, fractional outer exponents, selectors, matrices,
numerators, alternating products, Fredholm/transfer determinants, and
centralizer quotients are each treated separately rather than silently
folded into one no-go claim.

**Evidence Anchor**: `equation: Theorem 4.1, equations (17)--(22), and Section 5.1 — obstruction, exact repair, and outside-theorem routes`

### S4. The theorem/computation firewall is unusually strong

The five exact rows are explicitly development-seen controls. Their 203
points, 37 cycles, and twelve locked controls agree across two exact engines,
while the all-prime theorem and global analytic strips remain proof-sourced.

**Evidence Anchor**: `dataset: Table 1 and EXPERIMENT_RESULTS.json — p={2,3,5,7,11}, m_p={1,2,4,6,24}, 203 points, 37 cycles`

### S5. Citation, build, and figure provenance are closed

The manuscript cites exactly the same eleven keys present in the verified
bibliography. The three vector figures preserve the intended semantic
boundaries, and all bound source/result/figure hashes match their pre-review
manifests.

**Evidence Anchor**: `figure: Figures 1--3 and Appendix C — frozen controls, product semantics, mechanism boundary, and artifact bindings`

## Critical findings

**None.** No single defect invalidates a core mathematical claim or makes
the scoped negative conclusion untenable.

## Major findings

**None.** No theorem, computation, citation role, or evidence chain requires
substantial re-analysis, new evidence, or structural reconstruction.

## Minor findings

### M1. Appendix-B claim IDs do not match the final claim manifest

**Problem**: Table 3 uses the older planning decomposition: C1--C2 for orbit
arithmetic, C3--C4 for the two products, C5 for scalar degree, C6 for power
sums, C7 for fractional normalization, C8 for convergence, C9 for selector
cost, and X1--X2 for escapes. The frozen `CLAIM_MANIFEST.json` instead uses
C1 orbit arithmetic, C2 both products, C3 scalar degree, C4 equal weights,
C5 fractional normalization, C6 selector cost, C7 convergence, C8 the
registered audit, and C9 the outside-theorem escapes.

**Evidence Anchor**: `table: Appendix B, Table 3 versus paper/CLAIM_MANIFEST.json claims C1--C9 — identifiers diverge from C2 onward`

**Why it matters**: The scientific prose remains correct, but the table
advertised as the manuscript's claim--evidence firewall cannot be used to
trace the final machine-readable claim package. It also leaves the final C8
audit claim without its correct row and produces the visibly merged
“X1--X2outside the theorem” entry on page 14.

**Suggestion**: Rewrite Table 3 to the final C1--C9 map above, remove X1--X2
unless those IDs are explicitly added to the manifest, and give C8 its
registered-result authority. Rebuild and rebind every manuscript-side
manifest affected by the source/PDF change; do not edit the frozen result or
source lock.

**Severity**: Minor  
**Confidence**: 5/5 — direct source/manifest comparison

### M2. The numerical novelty self-score belongs in the internal audit, not the scholarly argument

**Problem**: The introduction states a precise (2.5)--(3/10) novelty
score, but the manuscript supplies no scholarly calibration scale from
which that number follows. The underlying conclusion—strong prior collision
and deliberately modest novelty—is well supported and should remain.

**Evidence Anchor**: `text: manuscript.tex:118--121 "Its novelty is calibrated at 2.5--3/10"`

**Why it matters**: A private route-selection score is useful in
`NOVELTY_ASSESSMENT.md`, but presenting it as article prose makes an honest
literature boundary look like an ungrounded quantitative research result.

**Suggestion**: Replace the number in the manuscript with a qualitative
statement such as “the contribution is deliberately modest and primarily
diagnostic.” Retain the exact (2.5)--(3/10) assessment and bounded-search
cutoff in the internal novelty record. Do not weaken the direct Gaspari and
Baake--Neumärker--Roberts collision statements.

**Severity**: Minor  
**Confidence**: 5/5 — scholarly-register and claim-strength review

### M3. Internal paper numbering prevents a standalone submission

**Problem**: The text calls itself “Paper 9,” reserves work for “Paper 10,”
and Figure 3 repeats “Paper 10” in the centralizer card. These labels make
sense in the research pipeline but have no defined referent for a journal
reader.

**Evidence Anchor**: `text: manuscript.tex:622--625 "Paper 9 neither constructs nor rules out a quotient."`

**Why it matters**: The paper otherwise reads as an anonymous standalone
technical note. Undefined internal sequencing weakens journal fit and makes
the figure dependent on repository context.

**Suggestion**: Use “the present paper” and “future work” in prose, replace
the Figure-3 card's “Paper 10” label with “future work” or “companion audit,”
then regenerate only the affected figure through the frozen deterministic
figure workflow and refresh its figure/package manifests. No centralizer
calculation should be added in this revision.

**Severity**: Minor  
**Confidence**: 5/5 — direct manuscript and figure inspection

### M4. Figure 1 and the frozen plan disagree on the multiplicity-axis scale

**Problem**: The frozen plan specifies a “compact logarithmic axis” for
Figure 1B, whereas the rendered panel uses a linear (0,5,ldots,25) scale.
The linear rendering is mathematically correct, legible, and arguably
clearer for these five values; the defect is the unacknowledged contract
drift, not the plot itself.

**Evidence Anchor**: `figure: Figure 1B — linear m_p ticks 0,5,10,15,20,25 versus PAPER_PLAN.md logarithmic-axis specification`

**Why it matters**: The pre-review package claims the plan and figure
package are mutually consistent. A reviewer should not have to guess
whether the scale changed deliberately or accidentally.

**Suggestion**: Prefer the existing linear plot and update the revision-era
plan/figure contract to say “compact linear axis,” recording the changed
plan hash in the revised package. If the logarithmic scale was actually
intended, regenerate Figure 1 instead. Do not change the plotted exact
values.

**Severity**: Minor  
**Confidence**: 5/5 — direct plan-to-render comparison

## Claim-by-claim verdict

| Claim surface | Verdict | Review note |
|---|---|---|
| Split/inert common-period formulas | PASS | Both diagonal entries have order τ_p; inert multiplication by λ makes every nonzero vector have the same exact period. |
| Binary and ramified boundaries | PASS | Cayley--Hamilton gives the unique binary 3-cycle; the rank-one nilpotent calculation gives 4 period-2 and 20 period-10 points at p=5. |
| Uniform odd-prime bound and uniqueness of p=2 | PASS | Split gives m_p≥p+1, inert gives m_p≥p−1, and p=5 gives equality p−1=4. |
| Raw-return versus orbit-label products | PASS | The primitive return keeps orbit length; the external label keeps multiplicity. |
| Fixed nonzero scalar obstruction and zero boundary | PASS | Polynomial degree closes the exact stated family; zeros force {1,0,…,0}. |
| Equal weights and fractional normalization | PASS | Power sums are m_p^(1−r); fractional orbit masses sum to one and extend via J_2(q) without selecting q. |
| Global convergence strips | PASS | The first repeat and m_p≥p−1 force failure through σ=2; m_p≤p²−1 gives absolute convergence for σ>3. |
| Matrix/centralizer/Fredholm escapes | PASS AS NONCLAIMS | They remain explicitly outside the theorem and were not computed. |
| One-shot five-row evidence | PASS | Live hashes, inventory, frozen JUnit evidence, reports, and strict manifest agree; the rows remain controls only. |
| Claim-evidence appendix | PASS WITH M1 | Semantic contents are correct, but the claim IDs are stale. |

## Citation, originality, anonymity, and venue positioning

Mechanical citation extraction gives eleven unique cited keys and exactly
the same eleven BibTeX entries, with eleven generated `bibitem` records and
zero BibTeX warning. The two strongest collisions are cited directly at the
classification and conclusion, not hidden in a generic related-work list.
This review did not repeat live URL resolution; metadata confidence is bound
to the independently reviewed 2026-08-14 ledger.

A fresh conservative local screen, using a slightly different TeX
normalizer from the frozen originality manifest, again found zero common
contiguous 12-token shingles between the substantive Paper-9 body and each
of Papers 1--8 or `propose-symplectic-map.md`. This supports only a local
reuse check, not an external plagiarism certificate. PDF metadata and source
inspection found `Anonymous Authors`, no affiliation, email, ORCID,
acknowledgment, grant, repository link, or local filesystem path.

The strongest venue objection is not hidden: most finite-field arithmetic
is classical and the remaining denominator obstruction is elementary.
Accordingly, external publication fit is limited to a specialized technical
note, negative-result venue, or a companion/appendix role. This limits
significance and originality; it does not create a mathematical blocker,
and this review does not ask for a new mechanism or broader claim merely to
inflate novelty.

## Build, typography, figures, and visual QA

I copied the complete paper tree into two separate temporary directories and
ran the frozen build script independently in both. The two builds produced
the same 15-page PDF at
`9b63f190e7c751c27682d1a9cc9246f0153edddfec61d4539c573ab70070d51c`,
byte-identical to each other, to `paper/manuscript.pdf`, and to
`paper/paper_pre_review.pdf`. Their terminal LaTeX logs and BibTeX logs were
also pairwise byte-identical.

The final PDF has 34/34 fonts embedded and subset, zero raster image objects,
no unresolved citation or cross-reference, and no LaTeX, package, BibTeX,
overfull, or underfull warning. All 15 pages were rendered and inspected at
original tool resolution. Equations, theorem endings, all three figures,
Tables 1--3, long hashes, and all eleven references are legible and
uncropped; no corrupt glyph or missing asset appears. The only visual issue
requiring action is the Table-3 label collision already covered by M1.

All nine frozen figure output hashes reproduce the figure package. Each PDF
master is a one-page vector file with embedded fonts and zero image object;
the SVGs contain no raster-image node. The scientific semantics of Figures
1--3 pass: development controls are separated from proof claims, raw return
from external labeling, and the proved scalar obstruction from live escape
mechanisms.

## Dimension scores

These uncalibrated scores are ordinal quality judgments, not venue
acceptance probabilities. The weighted score follows the ARS rubric; the
concrete unresolved findings control the recommendation.

| Dimension | Score | Descriptor | Basis |
|---|---:|---|---|
| Originality (20%) | 35 | Insufficient for a broad venue | Dominant classification collisions and elementary product algebra; exact limited delta is honestly stated. |
| Methodological rigor (25%) | 97 | Exceptional | Complete exact proof, edge cases, strict semantic scopes, and reproducible one-shot control. |
| Evidence sufficiency (25%) | 97 | Exceptional | Proof/result firewall, dual engines, hash-bound reports, strict manifest, deterministic figures and builds. |
| Argument coherence (15%) | 94 | Exceptional | Orbit arithmetic → product semantics → scalar boundary → safe global bounds is clean and non-overclaiming. |
| Writing quality (15%) | 88 | Strong | Precise and polished, with the claim-map and internal-register fixes M1--M4 outstanding. |
| Literature integration | 94 | Exceptional | Classical, direct, and frontier collisions are cited at their allowed roles; live re-resolution was outside this review. |
| Significance and impact | 52 | Weak/modest | Useful route-closing negative audit, but not a broad new arithmetic-dynamics result. |
| **Weighted average** | **83** | **Minor Revision pending bounded fixes** | No Critical/Major issue; originality remains an inherent venue constraint. |

## Required revision checklist

1. Reconcile Appendix Table 3 with the final C1--C9 claim manifest and fix
   the page-14 row collision.
2. Replace the manuscript's numerical novelty self-score with qualitative,
   evidence-backed positioning; retain the number only in the internal
   novelty audit.
3. Replace “Paper 9/Paper 10” with standalone wording in the text and Figure
   3, regenerate the affected figure deterministically, and refresh the
   figure/package bindings.
4. Reconcile Figure 1B's actual linear axis with the plan's logarithmic-axis
   description, preferably by updating the plan rather than changing the
   correct plotted data.
5. Rebuild twice, close the revised citation/figure/claim hashes, preserve
   the immutable pre-review PDF, and submit the bounded revision to a fresh
   hash-bound Round-2 review. Do not create `paper_final.pdf` on the strength
   of this Round-1 report.

## Devil's-advocate conclusion

The strongest counter-argument is that the paper wraps classical
prime-lattice orbit structure and an elementary polynomial-degree
observation around an externally imposed orbit label that is not itself a
native dynamical zeta construction. That objection is valid as a limit on
novelty and venue reach. It is not a hidden refutation: the manuscript names
the label as external, cites the direct collisions, admits the exact global
fractional repair, and leaves richer determinants and centralizer quotients
open. I found no unresolved Devil's-Advocate Critical issue.

## Final verdict

**MINOR REVISION — scientific core and frozen evidence chain pass.** The four
required fixes are local publication/integrity repairs. They require no
candidate rerun, new experiment, new prime/composite input, centralizer
calculation, numerical analytic evaluation, or Route-A/Route-B scope
expansion. A fresh Round-2 reviewer should verify the revised claim map,
standalone wording, plan/figure bindings, deterministic build, and updated
hash chain before finalization.
