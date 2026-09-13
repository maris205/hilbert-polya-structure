# Initial Proposal: An Embedded Formal-Period Cover for Normalized Hénon Maps

**Historical status:** superseded and non-normative.  This file records the
broader starting claim so that the later repair is auditable; it is not a
theorem statement and must not be used as source authority.

## Problem Anchor

> For the normalized two-parameter Hénon family
> \(H_{a,c}(x,y)=(ay+x^d+c,x)\), with fixed integers \(d,n\ge2\), construct
> the generic cover of actual exact-period-\(n\) cycles without confusing the
> full fixed scheme, formal-period points, or special fibers; determine its
> cycle monodromy; and decide whether the cycle observables
> \(\tau=\sum_i z_i\) and
> \(\rho=\operatorname{tr}(DH_{a,c}^{n})\) each generate the generic
> primitive-cycle field.

## Broader Starting Claim

Put \(A=\mathbb Q[a,c]\), \(K=\mathbb Q(a,c)\), and introduce cyclic
coordinates \(z_i\), indexed modulo \(n\), with

\[
 z_{i+1}=z_i^d+a z_{i-1}+c.
\]

The initial proposal correctly observed that the full cyclic algebra

\[
B_n=A[z_0,\ldots,z_{n-1}]/
 (z_i^d+a z_{i-1}+c-z_{i+1})_{i\in\mathbb Z/n}
\]

should be finite free of rank \(d^n\).  It then proposed, too quickly, to
perform Möbius subtraction inside \(\operatorname{Spec}B_n\), call the
result an embedded formal primitive-period subscheme over all of
\(\operatorname{Spec}A\), and assert that this object was already the normal,
finite-flat cover of actual exact-period points.  The same proposal identified
its \(a=0\) fiber directly with a smooth dynatomic cover, treated the cyclic
quotient as an everywhere free torsor, and inferred that both \(\tau\) and
\(\rho\) were primitive cycle coordinates.

## Why the Starting Claim Was Attractive

- The equations are monic and expose the rank \(d^n\) of the full fixed-point
  family.
- On \(a=0\), they collapse to the scalar iteration
  \(z\mapsto z^d+c\), where dynatomic monodromy is available.
- Time shift acts cyclically on exact-period points, so passing from points to
  cycles is natural.
- Both \(\tau\) and the derivative trace \(\rho\) are invariant under cyclic
  relabeling.

## Defects That Required Repair

1. A formal dynatomic root at a branch parameter need not have actual exact
   period \(n\).  Formal Möbius subtraction cannot simply be promoted to an
   everywhere embedded actual-period subscheme.
2. The full algebra \(B_n\) and its generic actual-exact-\(n\) factor are
   different objects.  Rank \(d^n\) belongs to the former, while
   \(\nu(d,n)=\sum_{e\mid n}\mu(n/e)d^e\) belongs to the latter.
3. An embedded coordinate algebra need not be normal.  Equality of fraction
   fields does not identify it with the relative normalization.
4. A generically étale cover can acquire a nonreduced special fiber; smoothness
   and freeness do not follow from generic monodromy.
5. Normalization does not commute with base change without an argument.  The
   exact \(a=0\) fiber therefore needed its own same-rank and nilpotent-exclusion
   proof.
6. Special-line monodromy constrains global monodromy only in the
   specialization-to-generic subgroup direction and only away from the branch
   locus.
7. A cycle observable being nonconstant is not, by itself, enough to make it a
   primitive field generator.  The stabilizer argument also needs full
   \(S_r\) cycle monodromy.
8. \(\rho\) is the pointwise trace of a derivative return matrix.  It is not
   the field trace \(\operatorname{Tr}_{F/K}\), and it is not the determinant
   \((-a)^n\).

## Required Refinement

Replace the embedded-formal construction by the following smallest adequate
package:

- retain \(B_n\) only as the full finite-free cyclic algebra;
- form the actual-exact-\(n\) étale idempotent block over \(K\), prove it is a
  single field, and take the relative normalization over \(A\);
- prove, rather than assume, the exact \(a=0\) special fiber;
- take cyclic invariants to obtain the normalized cycle cover and prove its
  full \(S_r\) monodromy;
- prove \(\tau\) and \(\rho\) separately non-base for \(r>1\), then use the
  \(S_r\)-stabilizer theorem to obtain primitivity;
- isolate \((d,n)=(2,2)\), where \(r=1\), as a degree-one boundary rather than
  monodromy evidence.

No arbitrary-Hénon, all-fiber smoothness, projective-compactification, height,
prime, modulus, or parameter-scan claim belongs to this paper.
