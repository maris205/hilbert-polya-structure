# Consolidated hostile review — P131 Euclidean quotient queues

**Review closure date:** 2026-08-31 UTC.  **Final internal verdict:**
**GO_INTERNAL**.  **External status:** **HOLD_EXTERNAL**.

This document consolidates `HOSTILE_REVIEW_A.md` and `HOSTILE_REVIEW_B.md`
after the round-two boundary repair.  The individual files remain the
immutable round records; this file states the final disposition of every
finding against the final `main.tex`.

## 1. Review history and disposition

Hostile Review A found no counterexample but withheld internal continuation
for three substantive reasons: foundational definitions and equality/core
boundaries were incomplete; the proposed `L/R` route reduced immediately to
run lengths rather than defining a raw string map; and P117/P122/P126 were not
explicitly subtracted in the manuscript.  It also requested an explicit
singleton `eta`, a marked-cut example, synchronized support files, and fresh
exact/build controls.

Round 1 closed those conditions by:

- defining recurrence, depth, both literal equality updates, and the
  transported marked gap before the terminal-core theorem;
- defining the normalized raw-string self-map `Psi`, proving the all-size
  identity `E Phi = Psi E`, and deriving singleton absorption, the raw core,
  and both inverse strings directly on paths;
- comparing complete raw output, core, and inverse strings in the verifier,
  in addition to run-length cross-checks;
- naming P117/P122/P126, admitting the literal composition-carrier collision,
  and limiting value to the map-specific temporal conjunction plus raw path
  engine;
- adding `eta(b)=(1,b-1)` for singleton targets and the `(2,1,3)` marked-gap
  example.

Hostile Review B independently reconstructed every theorem, fresh-ran the
canonical verifier, ran a separate cut-mask control through `N=14`, and
performed an isolated four-stage build and four-page QA.  It returned
`GO_INTERNAL / HOLD_EXTERNAL` with no critical or major finding and one
minor: the comparison with P126 needed the exceptional levels `N=2,3`.

Round 2 closed that minor in `main.tex:122-130`.  The final text now states
that the `N=2,3` finite functional graphs are isomorphic, levelwise
nonconjugacy holds for every `N>=4`, and the resulting separation is only a
graded-family/internal distinction, not priority evidence.

## 2. Final severity ledger

| class | opened | outstanding | final disposition |
|---|---:|---:|---|
| Critical | 0 | 0 | none |
| Major — mathematics/definition | 2 | 0 | closed in round 1 |
| Major — owner/internal scope | 1 | 0 | closed in round 1 |
| Major — control/reproducibility | 0 | 0 | none |
| Minor | 4 | 0 | three closed in round 1; P126 boundary closed in round 2 |

There is no outstanding hostile-review blocker.  Historical severity counts
in the round files describe the manuscript at those review times and are not
the final ledger.

## 3. Final mathematical assessment

The final carrier and update are coherent.  Canonical digit words
`[0;a_1,...,a_k]` with `a_i>=1`, `a_k>=2`, and digit sum `N` form a set of
size `2^(N-2)` and are literally the positive compositions of `N-1` after
`a_k -> a_k-1`.  The update preserves digit sum and terminal canonicality.

The stated subtractive Euclidean convention, including its final equality
step, produces the normalized path
`E(q)=L^{a_1}R^{a_2}L^{a_3}...` of length `N`.  The raw map `Psi` preserves
the normalized path carrier and satisfies `E(Phi(q))=Psi(E(q))` in every
size.

The last digit-one index is the exact entrance time.  Cyclic runs of ones, or
singleton path blocks, contract into their preceding nonsingleton; the marked
gap fixes the ordered terminal core.  Recurrent words have all digits at
least two, `Phi` acts on them by rotation, and the eventual period is the
primitive rotation period of the core.  Maximum depth is `N-2`.

The exact-depth OGFs and coefficient formulas sum to the full carrier count.
The two explicit inverse branches, including singleton `eta`, exhaust every
target fibre; fibres have size `0`, `1`, or `2`.  The image and Garden counts
have the correct `N=2,3` boundaries.  The recurrent Burnside and fixed-point
formulas are correct classical corollaries and remain zero-credit.

## 4. Exact and build evidence

The canonical verifier exhausts every state for `2<=N<=18`.  A final fresh
run produced **6,101,926 assertions**, `STATUS=PASS`, and a 1,868-byte stdout
that byte-matched `code/verification_output.txt`; both have SHA-256
`caa4df1e70fd2bdb86aa5aeb1308c2baa74b5d5e560d73980f1f6886c91bc8c6`.
Finite exhaustion is falsification evidence, not an all-size proof.

The final isolated `pdflatex`, `bibtex`, `pdflatex`, `pdflatex` build used
only `main.tex` and `references.bib`.  Its PDF byte-matched both `main.pdf`
and `main_round2.pdf`: **314,641 bytes**, four A4 pages, SHA-256
`07c7d40c21e42dde6dd416ca1aa11aef60847d6e2e506df3db4a2e4bbfd7b4af`.
Settled logs, all four rasterized pages, 21 font rows, anonymous metadata, and
PDF safety properties passed the final audit documented in `FINAL_QA.md`.

## 5. Owner subtraction and allowed claim ceiling

The composition carrier is explicitly admitted.  P117 receives zero credit
for cyclic run-reduction/recurrent-classification language; P122 receives
zero credit for the sharp-linear-clock plus target-fibre/image/Garden
silhouette; P126 receives zero credit for composition-carrier depth,
pointwise-fibre, and image language.  P126's synchronous balanced refinement
and P131's one-place Euclidean path queue are separated only with the exact
small-level qualification now in the manuscript.

External sources own canonical finite-CF uniqueness, terminal-one
normalization, Euclidean digit-sum cost, Stern--Brocot coding, continuants,
composition and regular-language machinery, cyclic-composition enumeration,
Burnside, and divisor counting.  None is residual contribution mass.

The allowed internal claim is only the conjunction for this literal map:

1. the rational half-level and normalized quotient queue;
2. the last-one clock, sharp depth, and marked-gap terminal core;
3. the raw normalized path map, all-size conjugacy, path absorption, and raw
   predecessor split;
4. all exact-depth layers;
5. all pointwise one-step fibres, image states, and Garden states;
6. recurrent rotation classification and pointwise primitive period.

No novelty, priority, ownership, posting, submission, or external-release
claim is authorized.  A bounded owner non-hit never changes that boundary.

## 6. Final verdict and external re-entry

**GO_INTERNAL.**  The manuscript, exact control, support documents, and final
PDF satisfy the internal hostile-review and reproducibility gates.  There is
no open re-entry condition for internal continuation.

**HOLD_EXTERNAL.**  Any future external-release request requires a specialist
primary-source owner search focused on literal cyclic finite-CF quotient maps
and Euclidean path queues, an explicit claim-to-owner matrix, resolution of
authorship/release authority, and a new independent release decision.  A
search non-hit alone is insufficient.
