# Internal hostile review — P92

Audit date: 2026-08-28 UTC  
Disposition: **internal GO / external HOLD**

The initial manuscript was written by the algebraic candidate scout. Round 1
was performed independently by the stochastic scout; Round 2 was an
independent integrating rederivation by the primary agent after the repairs.
This is internal adversarial review, not external peer review.

## Round 1 — attack of the initial draft

The reviewer rederived the Fourier action over prime and nonprime finite
fields, the weighted Singer-cycle determinant, all trace and Möbius formulas,
the mixing argument, the binary affine boundary, and first-anomaly recovery.
The theorem package was mathematically retained, but five repairs were made:

1. Two fixed-count formulas rendered the indicator macro as the ordinary
   letters `one`. Both occurrences now use the defined `\one` macro, so the
   displayed formulas are mathematically well formed in the PDF.
2. The manuscript now proves that a nontrivial additive character gives a
   nondegenerate pairing even over nonprime fields. This closes the basis
   assertion used by the finite Fourier transform.
3. The maximal-entropy statement now says precisely that recurrence errors
   are iid uniform on `F_q^×` and independent of the uniform time-zero state,
   rather than recording only their one-step marginal.
4. The control claim was narrowed from direct verification of the Fourier
   character action to what the program actually checks independently: the
   Singer orbit, hyperplane weights, full integer characteristic polynomial,
   traces, and recovery. The internal field tag `quartic` was corrected to
   `gf4` because `F_4/F_2` is quadratic.
5. Informal ownership language was replaced by bounded-search and cited-
   background language. No absolute novelty inference is drawn from search
   absence.

After repair, the registered program again passed **258 exact assertions** in
the five lanes `(2,2)`, `(3,2)`, `(3,3)`, `(4,2)`, and `(5,2)`, and the PDF
rebuilt successfully.

## Round 1 independent derivation ledger

- For every dual vector `xi`, substitution gives
  `A chi_xi = w(xi_r) chi_(C^T xi)`, with weight `q-1` on the coordinate
  hyperplane and `-1` off it.
- The nonzero dual vectors form one orbit of length `L=q^r-1`. Exactly
  `H=q^(r-1)-1` members have last coordinate zero, while the complement has
  even size. Hence the cyclic weight is `D=(q-1)^H` with no missing sign.
- The spectrum therefore has factors `(t-(q-1))(t^L-D)`. Power sums give
  `F_n=(q-1)^n + 1_{L|n} L(q-1)^(Hn/L)` and summation gives the two zeta
  factors with the recorded signs.
- For `q>=3`, the secondary spectral radius is strictly below `q-1`.
  Double regularity plus simplicity forces irreducibility, and the unique
  peripheral eigenvalue forces period one.
- For `q=2`, translation by the unique affine fixed point conjugates the
  state permutation to the Singer cycle: one fixed orbit and one `L`-cycle.
- Since `L>1`, the first positive difference from `F_1^n` occurs exactly at
  `L`, recovering `q=F_1+1` and `r=log_q(L+1)`.

## Round 2 — reattack after repair

The integrating pass repeated the determinant sign calculation, the
nonprime-field character argument, the regular-digraph mixing proof, the
binary endpoint, and all divisibility endpoints in the least-period formula.
It reran the exact control and rebuilt the manuscript through
`pdflatex -> bibtex -> pdflatex -> pdflatex`. No theorem change was required.

The second pass also checked that the text does not imply that the binary
system has only two maximal-entropy measures: the two periodic measures are
the ergodic endpoints and all maximal-entropy measures are their convex
combinations.

## Bounded literature and scope audit

The bibliography positively assigns primitive-polynomial and Singer-cycle
background, deterministic LFSR cycle structure, the finite-type zeta
determinant, and the Parry measure to their cited sources. A bounded search
did not identify a direct source for the combined nonzero-discrepancy SFT,
weighted Singer block, and delayed-anomaly recovery theorem. This is not a
priority certification; noisy LFSR, affine finite-field walk, and Schreier-
graph terminology remain plausible routes to an unlocated source.

## Residual risks and verdict

- **Mathematics:** low after two independent derivations and exact full-matrix
  controls in all frozen lanes.
- **Scope:** low inside the primitive-companion/nonzero-error family.
- **Literature/priority:** medium because the source search was bounded.
- **Verdict:** GO for internal Stage 2 use; HOLD for posting, submission,
  author contact, or priority language.
