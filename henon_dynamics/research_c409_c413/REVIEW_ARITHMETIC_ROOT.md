# Independent internal mathematical check: the active-fibre criterion

2026-09-06. Reviewer: root coordinator, not the author of the arithmetic
proof. Reviewed the complete 467-line `arithmetic/PROOF_PACKAGE.md` as it stood
on this date. This is current-team mathematical review, not peer review or a
publication-priority certificate. No C number or formal Route-A grade follows
from this review alone.

## Result and scope

No mathematical blocker found in Theorem 1 or its FAD corollary. The proof
closes the actual phase-collision difficulty rather than assuming that a sum
of natural-boundary series retains a natural boundary. Its conductor-grid
argument is a substantive step beyond the one-prime radial expansion.

I independently checked the compact-group construction, the absolute Fourier
expansion, the noncancellation/density mechanism, the limiting passage, both
analytic alternatives, and the FAD positivity/CRT application. I did not run
a finite census: the issue here is an all-conductor proof, and the exact
identities below provide a more direct check.

## Detailed checks

1. **Correct group and clock.** The closure D is exactly the compatible CRT
   fibre product. For any finite neighbourhood specification the generalized
   CRT supplies an integer, including when W contains primes outside S.
   Thus the diagonal generator is dense. Character evaluation at it is
   injective; this is essential to identify Fourier coefficients with actual
   atomic masses rather than with a presentation containing duplicate points.

2. **Wiener expansion.** For an active nonnegative pair (s,t), the sequence
   `h(k)=p^(-s k-t p^k)` decreases strictly to zero. Its telescoping expansion
   into ball indicators is correct both away from zero and at zero. Each
   indicator has Fourier coefficient norm one. Finite fibre indicators,
   products, restriction to D and collection of repeated characters preserve
   absolute summability. Orthogonality verifies that the resulting collected
   coefficients really are the Haar Fourier coefficients.

3. **Active fibre cannot be locally constant in the p direction.** At a
   witness a, other coordinates can be chosen nonzero even when their residue
   is zero. The remaining prefactor B0 is therefore nonzero. The values at
   `x_p=0` and `x_p=p^K` differ for every K above the modulus exponent. If
   all supported characters were trivial on U_p(K), uniform convergence
   would force invariance under that subgroup, a contradiction. The proof
   correctly obtains unbounded *actual* conductor in one fixed phase class.

4. **Dense grids, not merely infinitely many frequencies.** Multiplication
   of the p coordinate by `v=1+p^kappa t` leaves its finite residue unchanged
   and is an automorphism of D. It also leaves q_C unchanged. Substitution
   in its Fourier integral gives exactly the stated equal-coefficient rule.
   A primitive character of conductor p^k is carried through a full rotated
   grid of p^(k-kappa) distinct generator values. Since k is unbounded, those
   grids meet every open arc. No lower uniform bound on their masses is
   needed; nonzero mass at each selected point is enough.

5. **All phase collisions are removed before taking limits.** Within a
   torsion class, the roots of unity have already been absorbed into the
   finite-coordinate weight b_C. Between different classes, an equality of
   frequencies would make the representative ratio torsion, which is excluded
   by construction. Since the characters used have finite order, there are
   no remaining cross-class collisions. This validates the actual measure
   in equation (10), including complex/signed weights.

6. **Radial limit and meromorphic obstruction.** For `|xi|=|xi0|=1`,
   `(1-r)|r xi/xi0 /(1-r xi/xi0)|<=r`. Dominated convergence against the
   finite total variation measure therefore extracts exactly the mass at
   xi0. A nonzero limit excludes local holomorphic continuation at the inverse
   point. If meromorphic continuation existed through an arc, its poles
   would have to contain a dense subset inside its open domain, impossible
   for a nonzero meromorphic function. This does not assume uniformity of
   the radial residues over the grid.

7. **Necessity / rational branch.** Failure of AF means every active factor
   with nonzero b_C(a) lies on a residue ball whose valuation is fixed below
   v_p(W). All other factors are constant. Hence q_C depends only on its
   finite coordinate, giving equation (12). This includes an empty phase
   sum, empty prime set, vanishing periodic weights and phases which are
   themselves roots of unity. Increasing W does not change the criterion:
   an active zero p-adic residue has a zero-residue lift, while restriction
   maps any witness for a larger W back to one for the original W.

8. **FAD passage.** The normalized dominant determinant term is the positive
   product of `|1-eta^n|²` from unit-circle conjugate pairs. Realizability and
   a nonzero count exclude root-of-unity eigenvalues; otherwise a zero count
   at every multiple of the root order contradicts any existing periodic
   point. The exponent period for the selected prime is coprime to that
   prime, so CRT selects an active exponent residue whose p component is
   zero. If every grouped phase weight vanished there, the positive leading
   sequence would vanish on that progression. Thus AF is forced. The
   subdominant term is analytic beyond the rescaled boundary because all
   radial and periodic factors are bounded.

9. **Zeta is not confused with its logarithmic derivative.** The exponential
   defining zeta is nonzero in its convergence disk. A meromorphic extension
   has discrete zeros and poles; an arc avoiding them would extend
   `z zeta'/zeta=Z_f` holomorphically. This contradicts the established dense
   radial singularities. The conclusion for zeta is therefore justified.

## Exact adversarial control

The author's masked example has coefficients
`(1-(-1)^n)|n|_2`. At odd n these equal 2 and at even n they equal zero,
so its generating function is exactly `2z/(1-z²)`. The only residue with
unbounded 2-valuation has grouped phase coefficient zero. AF correctly
fails. Removing the phase mask makes b_C nonzero at the zero residue and
restores the full conductor grids. These are exact deductions, not a
numerically extrapolated classification.

## Primary dependency comparison actually checked

Independently accessed the public
[BCH v2 text](https://arxiv.org/pdf/2209.00085v2), dated 19 April 2024:
Definition 7.1.1–7.1.2 has the asserted positivity and own-prime-coprime gcd
periods; Lemma 10.3.10 includes strict positivity of the normalized dominant
term. Theorem 11.3.8 assumes a unique dominant root and integral wild
exponents. Remark 11.3.10 identifies cancellation between equal-radius
component series as the difficulty in removing hyperbolicity. Problem
14.1.2 asks for that removal. These checked statements match the proposed
increment. This paragraph deliberately does not claim that the final EMS
book or subsequent research has been checked; the author's current source
audit must address that separately.

## Before admission / writing

- Finish the bounded recent-owner and final-version audit; distinguish an
  answer to a question in the checked public version from worldwide priority.
- A verified genuinely nonhyperbolic realizable example would help readers
  see the scope. It must not become another paper or require a new unproved
  realization assumption.
- Preserve the finite-prime restriction, all phase aggregation and the exact
  distinction between this analytic criterion and C407's Cantor-topology
  theorem. The two statements and the hard steps are different.
- Preserve all target arithmetic limitations. This source-system theorem
  alone provides no target Euler factors, root number or zero correspondence.

## Follow-up: newer-owner deduction and realized example

The coordinator subsequently read the complete `SOURCE_AUDIT.md`,
`POSTCLASSICAL_DELTA.md` and `REALIZED_EXAMPLE.md`. In addition to the
earlier independent BCH check, the original
[BHN v1 text](https://arxiv.org/pdf/2307.07910v1) was independently opened
and Definition 2.11(P1)–(P3), Theorem 2.14, Remark 2.15 and the neighboring
stability statements actually read. The sublinear-height requirement is
explicit, not an inferred limitation of the proof.

The no-wild deduction in `POSTCLASSICAL_DELTA.md` is sound: periodic
rational factors and logarithmic valuations give an almost
quasi-constant, while the determinant recurrence is stable. This entire
branch must be deducted from new contribution. The proposed genuinely
wild factor has height `n log p` on n=p^a, so it is not an application
of that theorem. Absence of this sufficient hypothesis alone would not
establish novelty; the separate full conductor-grid proof is what closes
the stated remaining mathematical problem.

The Salem example was independently verified. Its companion polynomial
is irreducible modulo two; the substitution Y=X+X^(-1) gives one real
reciprocal pair and one non-torsion unit-circle pair. Hence its normalized
dominant toral count has the three distinct non-torsion-ratio phase
classes stated in the supplement. The additive factor's ordinary root
count follows by its least Frobenius exponent. Their product is a
genuine self-map with finite positive fixed sets and nonhyperbolic wild
FAD data. The same formulas are classical input, not an extra new result.
The failed all-embeddings unit-disc criterion was also checked directly
by sending lambda to lambda^(-1).

**Substance judgment after deduction:** the surviving wild multi-phase
classification is a defensible independent theorem contract. It proves
that the *actual aggregated* measure has dense nonzero atoms, including
all finite primes and phase cancellation masks, and answers the retained
nonhyperbolic wild question in the inspected BCH version. It is not a
relabeling of C407's topology theorem or a one-prime corollary. This
judgment does not certify publication priority, the unavailable EMS final
book, or equality between BHN's preprint and final publisher text.

This is one research-ready candidate, not a numbered completed paper.
The batch still needs five independently defensible contracts before its
frozen writing plan, and any resulting manuscript needs full review.
