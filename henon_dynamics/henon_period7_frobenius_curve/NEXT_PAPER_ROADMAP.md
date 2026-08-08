# Next paper roadmap: geometry and equivariant Frobenius of the oriented cover

## Successor status (HCS-C20)

HCS-C20 has resolved Stage I completely: the ordered-edge object is the
connected genus-eight \(D_7\) splitting curve, its quotient diagram is
explicit, and chronology induces real cubic multiplication on the scalar
Jacobian.  It also proves good reduction at \(p=5,11,13\) and certifies the
ordinary local-factor identity
\[
L_E=L_B L_C^2.
\]
This triggers the intended collapse branch of Gate 2: after forgetting the
\(\tau\)-labels, the oriented cover supplies only the sign quotient and two
scalar copies.  The fixed-period geometry is retained as HCS-C20, but another
round of scalar or unlabelled period-seven refinement is closed.

The active successor is now cross-period.  It should construct marked
primitive schemes for at least two distinct periods and keep Hénon period
\(n\), Frobenius degree \(r\), and time character \(s\) as three separate
indices.  A determinant is attempted only after an intrinsic repetition law
is proved.

## Central question

Let \(C\) be the normalized genus-three scalar curve and let
\(\widetilde C\) be the ordered-edge correspondence defined generically by

\[
P(\sigma,x)=P(\sigma,y)=0,
\qquad P(\sigma,a-y^2-x)=0.
\]

The next paper should answer one large question:

> What is the connected compactified geometry of \(\widetilde C\), and can
> its genuine two-clock quantities
> \(\#\operatorname{Fix}(\operatorname{Frob}_p^r\tau^s)\) be converted into
> exact equivariant local zeta data at a proved-good prime?

This is deliberately not another scalar point-count sweep.  The Hénon phase
\(s\bmod 7\) must remain visible throughout.

## Stage I: determine the cover, not just its generic fibres

Write the quadratic neighbor polynomial over \(K(C)\) and compute its
discriminant square class and divisor.  Normalize the resulting quadratic
extension and prove one of the two mutually exclusive outcomes:

1. it is connected, in which case its ramification divisor determines
   \(g(\widetilde C)\) by Riemann--Hurwitz; or
2. it splits, in which case the two global orientations and the action of
   reversal must be described explicitly.

Required certificates are exact valuations at every finite discriminant
point, the node branches, and every branch above infinity.  A generic fibre
or averaged transition matrix is insufficient.

**Gate 1:** no further paper is written until connectedness, compactification,
and genus are settled exactly.  If the extension is a dynamically trivial
split double and supplies only two relabelled scalar copies, terminate this
route unless Stage II reveals a nontrivial character sector.

## Stage II: one genuinely good prime and the joint character table

Choose a prime only after clearing all denominators and proving smooth good
reduction for the chosen models of \(C\) and \(\widetilde C\).  Then compute

\[
N_{r,s}=\#\operatorname{Fix}
   (\operatorname{Frob}_p^r\tau^s),
\qquad 0\le s<7,
\]

for enough \(r\) to recover the equivariant cohomological traces.  Use exact
extension-field arithmetic and retain the full \(r\times s\) table.  The
Fourier projectors of the cyclic time action may be formed only after the
Lefschetz \(H^0/H^2\) terms have been accounted for.

Run two independent implementations:

- direct solutions of the normalized correspondence over
  \(\mathbb F_{p^r}\); and
- quotient-ring or resultant fixed-point calculations that do not import the
  producer.

**Gate 2:** require a nontrivial, reproducible separation among the seven
time-character sectors.  If every sector is forced by a scalar numerator and
elementary cyclotomic multiplicities, record the collapse as a negative
result and switch dynamical form.

## Stage III: a fixed-period equivariant zeta, with a hard scope boundary

Once Stages I--II are proved, define the fixed-period equivariant local
determinants from the \(\tau\)-isotypic Frobenius action.  Test reciprocity,
integrality, conductor behavior, reversal pairing \(k\leftrightarrow-k\),
and stability across at least two proved-good primes.

This would be a meaningful paper even if the answer is negative: it would
show precisely whether orientation creates new arithmetic sectors or merely
repackages the scalar genus-three cohomology.  It still cannot pass Route-A2
or A3 globally because only period seven is present.

## Switch criterion

Stop HCS-C19 after the first of the following decisive failures:

- the normalized cover is geometrically trivial and all character factors
  are scalar/cyclotomic copies;
- no selected prime admits a tractable exact good-reduction certificate;
- the joint fixed-point calculation loses \(s\) through an unavoidable
  quotient; or
- the result cannot be extended beyond a single fixed period without fitted
  external arithmetic data.

If a switch is triggered, move to a system whose phase is intrinsic before
quotienting and whose primitive periods vary in one algebraic family, rather
than spending another round on finer scalar counts.
