# Independent Manuscript Verification — Round 2

**Paper:** *Exact 2-Adic Valuation of Higher-Period Multipliers for a Frozen
PCF Quadratic*  
**Review date:** 2026-08-14  
**Review mode:** fresh independent verification of the bounded Round-1
revision, followed by a regression audit of the complete scientific and
artifact package  
**Round-1 verdict:** `PASS_WITH_MINORS` (four required minors)  
**Round-2 verdict:** **PASS / MAY_FINALIZE**

## Decision

**Overall score:** 9.2/10  
**Confidence:** 0.99  
**Required Round-1 minors closed:** 4/4  
**Critical findings:** 0  
**Major findings:** 0  
**Residual required minors:** 0  
**Exact blocker:** none

The revised source and frozen revision PDF close all four acceptance gates in
the Round-1 review.  The edits do not weaken, enlarge, or otherwise alter the
mathematical conclusions.  The exact all-period result remains the local
valuation identity; rational equality is proved absent only at periods two
and three, reproduced as absent on the development-seen finite ledger through
period seven, and explicitly open uniformly for every period at least four.
No modulus-only, characteristic-exponent, prime-orbit, zero, quantization, or
route claim has been introduced.

The current revision snapshot may be finalized.  Finalization should be a
mechanical release step only: copy the accepted PDF, record this review and
its digest in the final integrity indexes, and update the pipeline state.  It
must not change the accepted scientific source, frozen evidence, period
cutoff, figures, bibliography, or source lock without reopening review.

## Independence and access boundary

I did not author the manuscript, Round-1 response, proof package, source lock,
code, frozen results, figures, bibliography, or integrity records.  I did not
execute or extend the registered candidate, access a prime table or
Riemann-zero dataset, use approximate matching, or use the network.  My
scientific checks used the already frozen exact artifacts.  The safe unit
suite and manuscript compilation were run only as regressions; compilation
was performed in an isolated temporary copy and did not modify the paper
directory.  This review is the sole project artifact written in Round 2.

## Reviewed bindings

All values below were recomputed from current regular files.

| Artifact | SHA-256 | Status |
|---|---|---|
| Round-1 review | `b4b571cdcaf5aab6825235e2012fedf7e64b3434a14b17064f5d3d5a5b1a31a5` | MATCH |
| Round-1 response | `c5a833c4db2f9e4b6fe0a706149ffe6106110278152e1da4bd6bbd969a0e6ea4` | MATCH |
| pre-review PDF | `36cf7d4f50ef712e3208565d081a57dd5602a828c3eedc5ad50e4386603bf8be` | MATCH; immutable Round-1 input |
| revised manuscript source | `60a9868f92b2d34e9ae140cebc534118225d05fe647530df1341c5ad0cc96974` | MATCH |
| Round-1 revision PDF | `fac4b7a3a5f19f515ebd982a3eef0e3c63e1c025616fbaeb62a94621d19632bf` | MATCH; accepted Round-2 input |
| current `manuscript.pdf` | `fac4b7a3a5f19f515ebd982a3eef0e3c63e1c025616fbaeb62a94621d19632bf` | byte-identical to revision PDF |
| Round-1 revision integrity | `8c98badc4125d8e319d3e2efe26d65c8d91fdde51aad5abaad18246442306335` | MATCH |
| Round-1 pipeline state | `c7699ea0c83442d600a56422f324d6a7660f472ae9944df759237cf1220947ad` | MATCH |
| source lock | `205b6969b3c1b2ce7e448a4d8b43df59706d34e79db3bc70ca271d302fa499a1` | MATCH |
| proof package | `9c4cff04ac7434822c5e0d091509947da554ac612a6f7b4332c5675fc6a355c9` | MATCH |
| official result | `847564ffb9e69aee2018dfa179490fafa81b733ad58231dab9202b82623f3ce6` | MATCH |
| strict result manifest | `6d9407408437954f52b4a1cb7f0caa50ca00bd22be9cf9a348a1bbb60c9a87e8` | MATCH |
| figure manifest | `cd4f4a2e831790657dac7b1a4c9706e8693101cb0f0d8b3830b36691a50940c8` | MATCH |
| bibliography | `dbcb1de7f92643291e688308b472616107a0b376db24a250379f97826d5d53f1` | MATCH |

## Exact verification of the four required minors

### M1 — finite cycle field and additive valuation: CLOSED

Theorem 4.1 now begins with a **finite extension** `L/K` containing the exact
cycle coordinates and explicitly takes `w` to be an **additive
non-Archimedean valuation of L** above the unique valuation of `K` over two.
This makes the completion invoked in the proof well-defined and removes the
old domain-of-notation ambiguity.

The proof meaning is unchanged and correct.  Completing `L` at `w` places the
cycle in a complete residue-characteristic-two field, the constant term
`-u` has norm strictly between zero and one, and the local sharp-boundary
lemma gives `w(z_j)=0`.  The chain rule then yields
`w(Lambda_C)=n*w(2)`.  Rationality plus algebraic integrality still gives the
odd-integer quotient and no equality exclusion beyond the stated one.

**Decision:** exact requested repair present in source and on revised PDF
page 5; no residual issue.

### M2 — the `d | n` Hensel-lift coincidence: CLOSED

The proof of Proposition 5.1 now explicitly introduces the unique lift
`y in O_{K_{u,d}} subset O_{K_{u,n}}` satisfying `g^d(y)=y`.  It then uses
`d | n` to infer `g^n(y)=y` and uniqueness among roots of `g^n-X` reducing to
`alpha` to conclude `y=z_alpha`.  Only after that identification does the
proof use reduction to exclude every smaller positive dynamical period.

This is the missing logical bridge identified in Round 1.  It correctly
separates:

1. existence and uniqueness of the `g^d-X` lift;
2. coincidence with the `g^n-X` lift in the common residue class; and
3. exactness of the least period by the exact Frobenius degree of `alpha`.

The subsequent identity `sigma(z_alpha)=g(z_alpha)` and the unramified norm
formula are unaffected.

**Decision:** exact requested repair present in source and on revised PDF
page 6; no residual issue.

### M3 — quotient ring, cross terms, and coefficient comparison: CLOSED

Section 6 now gives all three pieces required for a self-contained
calculation:

1. from `2=u^3/(u^2-u+1)`, it states `(2)=(u^3)` in the unramified
   extensions and identifies
   `O_{K_{u,n}}/(2) ~= F_{2^n}[ubar]/(ubar^3)`, with basis
   `1,ubar,ubar^2`;
2. it states that every cross term in
   `(alpha+b_1*u+b_2*u^2)^2` carries a factor two and vanishes modulo
   `u^3`, leading to `sigma(b_1)=1` and `sigma(b_2)=b_1^2=1`;
3. with `t=u+u^2`, it records `t^2=u^2 (mod u^3)`, `t^3=0`,
   `e_n=1`, and `e_k in F_2`, then expands
   `product_j(alpha_j+t)` before comparing coefficients in the displayed
   basis.

The resulting congruence

`B_C = 1 + e_{n-1}u + (e_{n-1}+e_{n-2})u^2 (mod 2)`

therefore supports the two-coefficient obstruction without an implicit
local-ring step.  The degree-two and degree-three exclusions and the
degree-four necessary-only witness retain exactly their previous meanings.

**Decision:** exact requested repair present across revised PDF pages 6--7;
no residual issue.

### M4 — certificate independence wording: CLOSED

The revised manuscript consistently describes the gcd and resultant/field
norm checks as **separately implemented but algebraically equivalent exact
certificates**.  I checked every certificate-context occurrence, including:

- the abstract;
- contribution 4;
- the Figure 2 caption;
- the registered-audit narrative;
- the Appendix B introduction to equation (20); and
- the raw-ledger commentary.

No remaining use of `independent` in the manuscript modifies the
gcd/resultant evidence pair.  The remaining occurrences correctly describe
different matters: an independent literature comparison, the independent
result-integrity audit, the independently deployment-reviewed code tree, an
upstream regression, or independence of paper compilation from candidate
execution.  The rendered Figure 2 itself says only that the exact engines
agree; its revised caption supplies the correct algebraic-equivalence class.

The retrospective claim manifest and paper configuration use the same
calibrated wording.  Frozen contemporaneous records retain their historical
engine labels, as they must under the source lock, but the accepted
manuscript nowhere presents the two decisions as logically or statistically
independent evidence.

**Decision:** exact requested global manuscript and figure-caption repair is
present; no residual issue.

## Bounded-revision audit

I extracted both 11-page PDFs and compared their complete text.  The
scientific differences are confined to the four requested classes:

- the M4 certificate wording in the abstract, contribution list, Figure 2
  caption, registered-audit section, and Appendix B;
- the finite-extension/additive-valuation statement in Theorem 4.1;
- the explicit `d | n` Hensel uniqueness bridge in Proposition 5.1; and
- the expanded quotient-ring and coefficient calculation in Section 6.

Pagination and line wrapping change where the added exposition reflows the
document, but no theorem conclusion, result scalar, citation, figure,
bibliography entry, source-lock claim, period range, or route status changes.
The pre-review PDF remains at its bound digest.  The accepted revised source,
revision PDF, and current working PDF match their Round-1 revision records.

## Mathematical regression audit

### Local and frozen valuation theorems — PASS

The escape argument outside the unit disk, forward invariance of the open
unit disk, strict cyclic distance contraction for a nontrivial cycle, and the
chain-rule multiplier computation remain correct.  The exclusion of fixed
points from the local lemma is retained.  The 2-Eisenstein argument gives the
unique cubic completion and the identity `v_u(2)=3`.  Rational integrality is
proved inside the manuscript; no unpublished predecessor is required as a
logical premise.

### Frobenius--Hensel and residue obstruction — PASS

Modulo `u`, `g^n-X` reduces to `X^(2^n)-X` with derivative `-1`, so the
residue lifts are unique and exhaustive.  The repaired divisibility bridge
correctly identifies exact dynamical period with exact Frobenius degree.
Uniqueness in the residue class gives `sigma(z_alpha)=g(z_alpha)`, and the
orbit product is the unramified norm.  The modulo-two expansion is now
fully explicit.  The irreducible degree-two, degree-three, and degree-four
polynomial statements are correct; the quartic remains a witness to
insufficiency, not an equality cycle.

### Cycle polynomial and repetition — PASS

The identity
`P_C(g(X))=(-1)^n P_C(X)P_C(-X)` and the special-value consequences have the
correct signs.  Cancellation at the fixed point `-a` is legitimate for an
exact cycle of length at least two.  The manuscript retains the caveat that a
single-cycle polynomial need not lie in `K[X]`.

The root-of-unity argument in the totally ramified cubic completion is
correct.  A rational repeated return of ordinary absolute value `2^(nr)`
forces `B_C^r=+/-1`, hence `B_C=+/-1`; it neither promotes the least period
to `nr` nor makes a modulus-only inference.

### Open and nonclaim boundaries — PASS

The following distinctions remain explicit in the abstract, main text,
figures, appendices, claim manifest, and pipeline indexes:

- all-period exact 2-adic valuation: proved;
- rational quotient oddness: proved under rationality;
- rational equality at periods two and three: excluded by proof;
- rational equality on periods two through seven: absent only in a
  development-seen finite reproduction;
- uniform rational equality exclusion for all `n>=4`: `OPEN_FOR_N_GE_4`;
- complex-modulus equality without rationality: not decided;
- characteristic-exponent equality: not decided;
- Route A: not advanced; Route B: not opened.

No finite ledger is used to prove a degree-independent statement.

## Frozen result and lifecycle regression

Read-only parsing of `EXPERIMENT_RESULTS.json` reproduced every scalar in the
manuscript ledger:

| `n` | exact-set degree | cycles | gcd degrees | exact norm pair | wall time (ns) |
|---:|---:|---:|---|---|---:|
| 2 | 2 | 1 | 0, 0 | `2^2`, `2^2` | 63,931,487 |
| 3 | 6 | 2 | 0, 0 | `2^9`, `2^9` | 174,504,404 |
| 4 | 12 | 3 | 0, 0 | `2^20`, `2^24` | 411,053,181 |
| 5 | 30 | 6 | 0, 0 | `2^50*16807`, `2^60*161051` | 1,637,080,691 |
| 6 | 54 | 9 | 0, 0 | `2^102*117649`, `2^120*387420489` | 4,033,271,287 |
| 7 | 126 | 18 | 0, 0 | `2^294`, `2^266*868028736113769706358509` | 16,919,324,815 |

The times sum to exactly `23,239,165,865 ns`.  All six records are `PASS`,
monic/squarefree exact-set objects with period-divisible degree, invariant
normalized product, agreement of the two exact decisions, run IDs
`R042`--`R047`, role `DEVELOPMENT_SEEN_REPRODUCTION`, and optional diagnostic
`NOT_REQUESTED`.  Frozen, executed, and development-seen period lists are all
`[2,3,4,5,6,7]`; `new_blind_periods=[]`.

The result directory contains one immutable claim, one official candidate
result, and one terminal ledger, with no target-hit artifact.  The run is
`REGISTERED_RUN_0001`, registered-run count one, claim state `STARTED`, and
terminal state `COMPLETED_NO_HIT`; every frozen period was started and
completed, with no stopped period or failure code.  No second execution or
post-null extension was observed.

## Tests, manifests, citations, and figures

- A fresh safe invocation completed **38/38 tests** in 3.06 seconds with no
  failure, error, or skip.  It used no cache provider and wrote no bytecode.
- The frozen JUnit file contains 38 distinct test cases and no failure,
  error, or skipped node; its digest is
  `4e38e3197ec588edceac43c8292630a61f018f4f03f36bb3c8606723bbd0f237`.
- All 12 strict-result-manifest hashes recompute correctly.  The live result
  directory is exactly the nine recorded pre-manifest regular files plus the
  manifest; there is no nested, symlinked, target-hit, or extra evidence
  artifact.
- All 32 figure-manifest input/artifact byte counts and hashes recompute
  correctly.  The determinism record binds two identical generations of all
  nine PDF/SVG/PNG outputs.
- The manuscript cites 12 unique keys; the bibliography contains the same 12
  unique keys, with no missing or unused entry.  Every use remains within the
  frozen primary-source verification ledger.  Wang (2026) remains genealogy
  only, and no prime or zero datum is imported.
- Figures 1--3 agree with their frozen sources and preserve the theorem/open,
  development-seen, and necessary-only boundaries.  Figure 3's internal type
  remains relatively small at ordinary print scale, as Round 1 noted, but it
  is sharp, readable under modest zoom, and not a release blocker.

## Build, fonts, and complete PDF inspection

The revised source was compiled twice consecutively in an isolated directory
using the fixed epoch and the same deterministic `pdflatex -> bibtex ->
pdflatex` sequence.  Both builds produced

`fac4b7a3a5f19f515ebd982a3eef0e3c63e1c025616fbaeb62a94621d19632bf`,

which is byte-identical to both `paper_round1_revision.pdf` and the current
`manuscript.pdf`.  The final log contains no LaTeX/package warning, undefined
citation/reference, duplicate-label warning, overfull/underfull box, or
error.  The PDF is an unencrypted 11-page letter-size document with no
JavaScript.  All 33 fonts are embedded and subset.

I rendered and visually inspected every page of both the immutable pre-review
PDF and the revised Round-1 PDF: **22/22 pages passed**.  There is no clipping,
overlap, missing figure, corrupt glyph, blank required content, broken
reference, or illegible ledger.  The four repairs are visibly present in the
revised pages, and all three figures render with their correct captions and
semantic labels.

## Final Round-2 disposition

All five acceptance conditions stated at the end of Round 1 pass:

1. finite cycle field and valuation domain — PASS;
2. explicit `d | n` Hensel-lift identification — PASS;
3. self-contained modulo-two coefficient calculation — PASS;
4. calibrated algebraic-equivalence wording — PASS;
5. refreshed hashes, clean deterministic build, and green safe suite — PASS.

There is no residual scientific, evidentiary, citation, figure, build, or PDF
blocker.  The package is authorized to proceed to mechanical finalization at
the accepted source/PDF hashes above.

`BASE2_CLOCK_MANUSCRIPT_REVIEW_ROUND2 {"critical_findings":0,"major_findings":0,"required_minors_closed":4,"residual_required_minors":0,"reviewed_manuscript_sha256":"60a9868f92b2d34e9ae140cebc534118225d05fe647530df1341c5ad0cc96974","reviewed_pdf_sha256":"fac4b7a3a5f19f515ebd982a3eef0e3c63e1c025616fbaeb62a94621d19632bf","reviewer_independent":true,"source_lock_sha256":"205b6969b3c1b2ce7e448a4d8b43df59706d34e79db3bc70ca271d302fa499a1","verdict":"PASS_MAY_FINALIZE"}`
