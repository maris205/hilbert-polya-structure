# HCS-C20 adversarial review log

**Date:** 2026-08-08

## Round 1: rejected as a local-factor proof

The first exact computation established the characteristic-zero dihedral
geometry and reproduced the three branch-corrected point-count rows.  It did
not yet justify calling those rows Hasse--Weil local factors.  The adversarial
review rejected that promotion for a substantive reason: abstract good
reduction of a quotient curve does not by itself prove that normalization of
the singular plane model commutes with reduction.

The review isolated six missing bridges:

1. a smooth proper two-chart model for the genus-two sign quotient;
2. a precise tame vertical-inertia argument for the cyclic degree-seven
   cover;
3. all hypotheses needed for purity of the branch locus;
4. geometric connectedness of the special fibre;
5. extension of the reflection and smoothness of its relative quotient; and
6. a finite birational comparison between the quotient model and the
   reduced plane septic.

This was a genuine rejection, not a request for cosmetic additions.

## Round 2: proof repaired

The final proof in `SELECTED_PRIME_GOOD_REDUCTION.md` closes all six bridges.
In particular:

- nontrivial vertical inertia would have (e=7,f=1) and produce a tame
  character (C_7\hookrightarrow k^\times), where
  (k=\mathbb F_p(B_{\mathbb F_p})); geometric integrality reduces its
  algebraic constants to (\mathbb F_p), contradicting
  (p\not\equiv1\pmod7);
- regularity, excellence, finite normalization, generic etaleness, and
  codimension-one unramifiedness are recorded before invoking purity;
- geometric connectedness is transported from generic to special fibre in
  the proper smooth family;
- the tame involution is checked in completed relative local rings;
- monicity gives total-space normalization on affine and infinity charts;
  and
- exact irreducible specializations give degree seven on the integral plane
  special fibre, while the quotient special fibre also has degree seven, so
  the comparison is finite birational.

The remaining branch ledger is exact: one affine ordinary node with Hessian
discriminant (-7), and seven rational normalization branches at infinity.
This proves the correction (7+\epsilon_{p,r}) rather than assuming it.

## Computational independence audit

An intermediate checker reproduced the data but used the same finite-field
package as the producer.  That was rejected as insufficiently independent.
The released checker is non-importing and implements its own polynomial
quotient fields, irreducibility tests, operation tables, point enumeration,
Newton reconstruction, norm calculation, and SHA-256 certificate binding.
The regression suite includes deliberate certificate mutations that must
fail.

The final machine-readable audit also renamed the irreducible-specialization
record from the potentially misleading `geometric_integrality_witness` to
`plane_integrality_witness`.  The witness proves that the plane special fibre
is integral; geometric integrality of the smooth cover comes separately from
proper-smooth connectedness.  Producer, checker, tests, and both JSON
artifacts were regenerated after this schema correction.

## Final sign-off

The mathematical adversary and the Route-A adversary independently accepted
the repaired theorem.  Both specifically confirmed the vertical-inertia,
purity, connectedness, tame quotient, simultaneous-normalization, node, and
infinity arguments; neither found a remaining scientific release blocker.
The Route-A tuple was left unchanged.

## Final claim boundary

Accepted as exact:

- the connected (D_7) splitting curve and quotient genera;
- the Jacobian isogeny and the chronology-induced real cubic multiplication;
- good reduction and genuine local factors at (p=5,11,13); and
- ordinary spectral collapse
  (H^1(E)=H^1(B)\oplus H^1(C)^{\oplus2}) up to the isogeny realization.

Not claimed:

- good reduction at any untested prime;
- equality of the full endomorphism algebra or absolute simplicity;
- a polarized product decomposition;
- a cross-period dynamical determinant, Riemann divisor, or
  Hilbert--Polya operator; or
- novelty of the general dihedral/Prym/real-multiplication mechanism.
