# Bounded proof check — ANG-20260914-RWS01

**Date:** 2026-09-14.  
**Reviewer context:** separate AI subagent /root/review_cycle_three.  
**Reviewed material:** the [version-1 card](../candidate-card.md),
[paper](../paper.md), [claim ledger](../claim-ledger.md) and
[evidence index](README.md).  
**Outcome:** no blocking mathematical defect found in the claims reviewed.

This is a scoped model-assisted mathematical check, not human peer review,
a calibrated reviewer assessment, a literature novelty judgment, or a
formal Route evaluation. The reviewer received the requested risk areas and
was not blinded to the intended stop decision. Separate invocation does not
establish independent error processes. No manuscript or candidate definition
was edited.

## 1. Full carrier and uniform-source result

Proposition 1 gives a valid two-sided inverse. Each output coordinate uses
only finitely many input coordinates, including the reflected boundary, so
the map and its inverse are continuous on the entire product carrier.
The uniform-state calculations are exact: both L(0) and L(1) vanish,
G(0)=1, and the elementary small-divisor test gives G(1)=pi. Therefore
R squared of the zero pair is indeed (1,pi), without a supplied prime word.
This is a genuine arithmetic readout of the same action, not an inherited
claim from 131.

## 2. Theorem 2: no hidden restriction to special initial states

The spatial recursion is well founded. Equation (2) determines the complete
time row at coordinate 3 from an arbitrary two-sided boundary row a at
coordinate 2. In equation (3), every divisor input to G_n has index strictly
below n. Hence the formula defining row n+1 uses only rows already defined.
There is no unspoken upper-boundary constraint and no limit equation waiting
to be solved after all finite rows have been constructed.

The resulting spacetime satisfies the frozen recurrence at every coordinate
and every integer time. Its states at times -1 and 0 therefore determine
the same complete R-orbit, since R is invertible. Translation of the time
index establishes R C = C S with the shift direction stated in the paper.

Surjectivity and injectivity can be checked separately:

- Given any pair (x,y) in the full carrier, its unique complete R-orbit
  provides a boundary word a. Successive use of equations (2) and (3)
  recovers every row of that orbit, so C(a)=(x,y). Thus no arbitrary
  two-register initial states are omitted.
- Given any boundary word a, the constructed orbit has boundary row exactly
  a by definition. Extracting the boundary of its state C(a) recovers a.
  Consequently two distinct boundary words cannot give the same initial
  state.

The claimed finite window also checks. For row n, radius n-2 is sufficient.
The time-shifted row-n terms expand the radius to n-1 for row n+1; row n-1
and every lower divisor row lie within that window. Every coordinate of C
is therefore continuous. Conversely the t-th boundary bit is coordinate 2
of the second register of R to the power t, a continuous function for every
positive or negative integer t. This proves a homeomorphism, not merely a
set-theoretic coding.

## 3. Complete packets, roof and scalar zeta

The conjugacy transports the full fixed-point set, so exactly 2 to the power
m states are fixed by R to the power m. Decomposing that set by least periods
gives the stated divisor recurrence for b_m. Dividing least-period-m points
by m accounts for cyclic phase once and only once. The paper does not add an
orientation-reversal quotient or select a preferred symbolic subfamily.

The unit-roof suspension is complete. Height modulo one forces every return
time to be an integer, and the base period then gives primitive length m
and repeated length r m. The same roof is used in the packet product.

The logarithmic convergence argument can be bounded explicitly. With
rho=abs(q)<1/2, b_m is at most 2 to the power m divided by m, and

    sum_m b_m sum_r rho^(m r)/r
        <= [1/(1-rho)] sum_m (2 rho)^m/m < infinity.

Thus exchanging the absolutely convergent sums is justified, and the fixed
point divisor identity gives log Z = sum_k (2q)^k/k. Exponentiation yields
Z=1/(1-2 exp(-s)) on Re(s)>log(2). Its displayed meromorphic continuation
belongs to that same function. This proves a scalar ordinary-orbit-zeta
claim only; no transfer operator, function space, nuclearity, trace formula
or formal Route-A target/divisor result follows automatically.

## 4. Controls, arithmetic observables and stop scope

The pure-wave and spatially constant-source rules permit the same successive
row reconstruction, so their identical unweighted packet spectra are
established on their own carriers. They are comparison objects, not a
substitution for R's roof or analytic owner.

The reconstruction and inverse boundary extraction depend on G. Accordingly
the integer-labelled register observables remain G-dependent after transport
to the full shift. Equality of unweighted period spectra does not negate
the prime source output. The record correctly retains T1 as PARTIAL,
while preserving the full positive T0, T2, and ordinary-product T3 results.

The particular boundary word belonging to the zero pair is not classified
here. Full-shift conjugacy alone determines neither its periodicity nor its
nonperiodicity. Keeping the zero-seed return question OPEN is warranted;
the source nonreturn theorem for the different map in 131 is not imported.

The documented stop/fork decision is therefore supported by the planned
control-equivalence test for unweighted packet data. It is not a theorem
excluding every arithmetic-sensitive observable, alternative coupling, or
analytic construction. No classical symplectic carrier or Route coordinate
has been supplied, and Route B remains NOT INVOKED.

## Reviewed input identity

SHA-256 values from sha256sum on the two explicit files:

| Input | SHA-256 |
| --- | --- |
| candidate-card.md | d6bbda99c70986f5ba51caec386bec781a9442421a3fdfcad5e27592fb7132eb |
| paper.md | f38b88fc62891ea29a0c02100f1e8c69188d47f8d8b20b873fb28b60d4721bb7 |

All checks above concern elementary proofs in those local records. No
numerical experiment, finite-box extrapolation, external theorem, external
upload, or new candidate was introduced by this review.
