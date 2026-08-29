# Independent hostile review B

Date: 29 August 2026
Scope: `main.tex`, `references.bib`, the exact verifier and stored output,
and the rebuilt PDF.  This pass was performed independently of the author
derivation.  External circulation remains **HOLD**.

## Verdict

**PASS for the internal short-paper package.**  CRITICAL: 0.  MAJOR: 0.
MINOR: 1 repaired source issue and 2 residual scope risks.  The theorem
statements survive direct rederivation, the verifier passes **141,190 exact
assertions**, and the four-stage LaTeX/BibTeX build is clean.

## Independent mathematical attack

1. **Double-adjugate normal form.**  For an invertible matrix,
   `adj(A)=det(A)A^{-1}` gives
   `adj(adj(A))=det(A)^(d-2)A`.  For rank at most `d-2`, the first
   adjugate is zero; for rank `d-1`, it has rank one and its adjugate is
   zero when `d>=3`.  Thus the asserted one-step singular collapse has no
   omitted rank endpoint.
2. **Iterates and integrality.**  Determinants evolve by
   `delta -> delta^alpha`, with `alpha=(d-1)^2`.  The scalar recurrence is
   `E_(k+1)=E_k+(d-2)alpha^k`, whose solution is
   `E_k=(alpha^k-1)/d`; integrality follows from `alpha=1 mod d`.
3. **Fixed points, cycles, and zeta.**  On each determinant fiber the
   equation is `delta^E_k=1`; every nonzero determinant fiber has size
   `|SL_d(q)|`.  This reproduces
   `1+|SL_d(q)| gcd(E_k,q-1)`.  Möbius inversion then gives exact-period
   counts, and the displayed Euler product is the standard finite-map
   factorization.
4. **Images and sharp depth.**  Each invertible projective scalar line
   contributes `(q-1)/gcd(alpha^k,q-1)` points.  Prime-by-prime valuation
   gives the stable divisor
   `b=prod_(ell|alpha) ell^v_ell(q-1)` and first stabilization time
   `max ceil(v_ell(q-1)/v_ell(alpha))`.  The separate singular depth-one
   basin explains the outer `max{1,t_*}`.  Empty-prime and already-stable
   endpoints were checked.

## Findings and repairs

- **MINOR — owner citation was present in the bibliography but not attached
  to the claim.**  The sentence calling projective adjugation a classical
  Cremona transformation now cites Dolgachev directly.  This does not alter
  the theorem or claim novelty for the underlying identity.
- A pre-existing source typo in the definition of `alpha,E_k`
  (`,qquad`) was corrected before this pass and was confirmed absent in the
  rebuilt PDF.
- No further mathematical or typesetting repair was required.

## Control independence and mechanical QA

The strongest lane computes two adjugates literally from signed minors and
compares them with the claimed one-step identity over all of `M_3(F_2)`,
`M_3(F_3)`, and `M_4(F_2)`.  Separate exhaustive functional-graph lanes
compare fixed and image sequences through six iterates, and arithmetic
signal lanes check twelve terms.  The post-review-A frozen tree also contains
literal scalar-line image lanes with exact stabilization times
`t_*=0,1,2,4,1`; review B independently inspected these lanes and replayed
them after the freeze.  A fresh run reproduced the stored output byte for
byte and reported `assertions: 141190`.

The exact four stages
`pdflatex -> bibtex -> pdflatex -> pdflatex` all exited zero.  Scans of
`main.log` and `main.blg` found no substantive warning, undefined citation
or reference, multiply-defined label, overfull/underfull box, or error.
The rebuilt PDF has 4 A4 pages and 296,320 bytes.  `pdffonts` reports 23
font entries, all embedded, subsetted, and Unicode-mapped;
`pdftotext -layout` recovered 13,815 bytes.  All four rendered pages were
inspected and show no clipping, collision, malformed formula, or orphaned
heading.

## Collision and owner boundary

The direct ingredients remain owned: Jacobi/complementary-minor identities,
projective adjugate as a Cremona map, finite-field matrix counts, and scalar
power-map functional graphs.  The manuscript now cites each boundary and
claims only their displayed full-space temporal conjunction.  No exact
owner for that conjunction was located in the bounded targeted search; this
is evidence of search absence, not a novelty certificate.

Internal overlap is limited but nonzero: P99 is also matrix/algebraic, while
P97 and P100 use finite absorbers and exact depth formulas.  P103 differs in
state space, map, arithmetic invariant, and cycle/image theorem.  The
literal-minor control is over prime fields only and later iterates use the
proved closed map rather than recomputing two adjugates at every time; these
are residual control-scope limitations, not failures of the proof.

## Residual risk

- **Owner risk: medium-low.**  The underlying double-adjugate identity is
  classical and elementary; an exact finite-field functional-graph treatment
  could exist outside the bounded search.
- **Control risk: low.**  Extension-field and larger-dimension literal-minor
  lanes are absent, although the symbolic proof covers prime powers.
- **Release status: HOLD.**  A broader specialist owner search and the final
  independent artifact freeze remain required before circulation.

## Post-review-A current-tree replay

Review A later made the time-zero convention explicit, added the P97/P99
collision firewall, and strengthened the evidence with multi-step image
staircases.  After that source was frozen, review B independently rechecked
the valuation argument and the new verifier code, reproduced all 141,190
assertions byte for byte, rebuilt the four stages, rescanned the logs and
fonts, and rerendered all four pages.  The current metrics are the ones
reported above.  The theorem verdict and external HOLD are unchanged.
