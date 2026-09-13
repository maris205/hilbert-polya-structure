# Round 1 Refinement: Relative Normalization and Two Primitive Cycle Coordinates

## Problem Anchor

> For the normalized two-parameter Hénon family
> \(H_{a,c}(x,y)=(ay+x^d+c,x)\), with fixed integers \(d,n\ge2\), construct
> the generic cover of actual exact-period-\(n\) cycles without confusing the
> full fixed scheme, formal-period points, or special fibers; determine its
> cycle monodromy; and decide whether the cycle observables
> \(\tau=\sum_i z_i\) and
> \(\rho=\operatorname{tr}(DH_{a,c}^{n})\) each generate the generic
> primitive-cycle field.

## Anchor Check

- **Original bottleneck:** the periodic-point equations are explicit, but the
  actual primitive-cycle cover, its special line, its monodromy, and its
  intrinsic cycle coordinates must be separated scheme-theoretically.
- **Why the repair still addresses it:** the repair changes the construction,
  not the target.  It starts with the generic actual-period factor and returns
  to the parameter plane by relative normalization.
- **Drifting suggestions rejected:** arbitrary polynomial automorphisms,
  projective compactification, every-fiber smoothness, arithmetic-height
  statements, and numerical cycle surveys.

## Simplicity Check

- **Dominant contribution:** PC1, the normalized primitive-period cover with
  its exact scalar special fiber and full symmetric cycle monodromy.
- **Supporting contribution:** PC2, the two natural cycle observables
  \(\tau\) and \(\rho\) separately generate the same generic cycle field.
- **Components removed:** the embedded formal-period subscheme, an everywhere
  torsor assertion, and any third observable.
- **Why this is smallest adequate:** PC1 supplies the geometric field on which
  PC2 makes sense; PC2 needs no additional cover or parameter.

## Changes Made

### 1. Full fixed algebra separated from exact-period normalization

- **Reviewer said:** formal and actual periods collide on branch fibers.
- **Action:** retain \(B_n\) only as the full cyclic algebra.  Define \(E_n\)
  as the actual-exact-\(n\) idempotent block of \(B_n\otimes_AK\), then set
  \(S\) to the integral closure of \(A\) in \(E_n\).
- **Impact:** the theorem no longer depends on a nonexistent everywhere
  embedded actual-period subscheme.

### 2. Special fiber made into a theorem rather than an identification by notation

- **Reviewer said:** normalization and base change do not commute formally.
- **Action:** use the scalar dynatomic field on \(a=0\), Henselian idempotent
  lifting, finite normalization, Cohen--Macaulay/miracle-flatness, a same-rank
  normal-overring comparison, and flat nilpotent exclusion.
- **Impact:** \(S/aS\) is proved to be the affine dynatomic algebra, while no
  claim is made that every fiber is reduced, smooth, or a free cyclic torsor.

### 3. Monodromy comparison direction fixed

- **Reviewer said:** the special-to-global restriction direction was unsafe.
- **Action:** the good part of the scalar special line contributes a subgroup
  of global monodromy.  Its full wreath action, together with the universal
  time-shift centralizer bound, fixes the point action and yields full
  \(S_r\) on cycles.
- **Impact:** the monodromy theorem now has both a lower and an upper bound.

### 4. \(\tau\) and \(\rho\) separated

- **Reviewer said:** non-base, primitive, derivative trace, and field trace had
  been conflated.
- **Action:** prove cyclic invariance, then separate non-base lemmas at the
  scalar line for \(\tau\) and for pointwise derivative trace \(\rho\).  Only
  after full \(S_r\) is established is the maximal-stabilizer argument used.
- **Impact:** each norm polynomial is irreducible of degree \(r\) for its own
  reason; neither conclusion is borrowed from the other observable.

### 5. Degree-one boundary isolated

- **Reviewer said:** \((2,2)\) has only one primitive cycle.
- **Action:** record \(\tau=a-1\) and
  \(\rho=4a^2-6a+4+4c\) explicitly and describe their primitivity as a linear
  boundary case only.
- **Impact:** no nontrivial monodromy inference is drawn from \(r=1\).

## Revised Proposal

Fix \(d,n\ge2\).  Let

\[
A=\mathbb Q[a,c],\qquad K=\mathbb Q(a,c),\qquad
\nu(d,n)=\sum_{e\mid n}\mu(n/e)d^e,\qquad r=\nu(d,n)/n.
\]

For cyclic coordinates indexed modulo \(n\), define

\[
B_n=A[z_0,\ldots,z_{n-1}]/
 (z_i^d+a z_{i-1}+c-z_{i+1})_i.
\]

With a graded term order the leading monomials are the pairwise coprime
\(z_i^d\).  Hence the defining equations form a monic Gröbner basis and the
standard monomials \(\prod_i z_i^{e_i}\), \(0\le e_i<d\), give an
\(A\)-basis of rank \(d^n\).

Over \(K\), isolate the reduced étale idempotent block indexed over an
algebraic closure by actual exact-period-\(n\) points; call it \(E_n\).  It has
dimension \(\nu\).  On the divisor \(a=0\), the recurrence becomes iteration
of \(z\mapsto z^d+c\).  The scalar dynatomic irreducibility theorem and
Henselian idempotent lifting force \(E_n\) to be a single field.

Let \(S\) be the integral closure of \(A\) in \(E_n\).  Finiteness follows
from excellence.  Since a normal finite surface over the regular surface
\(\operatorname{Spec}A\) is Cohen--Macaulay, miracle flatness makes \(S\)
locally free of rank \(\nu\), and a constants argument proves geometric
integrality.  The unique height-one prime over \((a)\), ramification index
\(e=1\), a finite birational comparison, and flat exclusion of nilpotents
prove the exact special fiber

\[
 S/aS\cong D_n:=\mathbb Q[c,z]/(\Phi_{d,n}(z,c)).
\]

This is an affine special fiber statement, not a projective compactification
and not a claim that every fiber is smooth or reduced.

Time shift \(\sigma(z_i)=z_{i+1}\) acts faithfully with order \(n\) on the
generic exact-period field.  Set

\[
 S_0=S^{\langle\sigma\rangle},\qquad
 F=\operatorname{Frac}(S_0)=E_n^{\langle\sigma\rangle}.
\]

Reynolds averaging in characteristic zero gives base change for invariants,
so \(S_0\) is locally free of rank \(r\) and

\[
 S_0/aS_0\cong D_n^{C_n}.
\]

The special object is therefore the affine cycle curve
\(X_0^{\mathrm{aff}}(n)=\operatorname{Spec}(D_n^{C_n})\).  On the good scalar
line, the known dynatomic point monodromy is \(C_n\wr S_r\).  Its image is a
subgroup of the global image, while global monodromy must commute with time
shift and hence lies in the same wreath centralizer.  Thus the point action is
the full wreath action and the induced geometric monodromy on the \(r\)
cycles is \(S_r\) (trivial when \(r=1\)).

Inside \(F\), define

\[
 \tau=\sum_{i=0}^{n-1}z_i,
 \qquad
 \rho=\operatorname{tr}
 \left(DH_{a,c}(z_{n-1},z_{n-2})\cdots
 DH_{a,c}(z_0,z_{n-1})\right).
\]

Both are integral and invariant under cyclic relabeling, hence lie in
\(S_0\).  For \(r>1\), distinct primitive
Puiseux words at infinity on \(a=0\) give different leading values separately
for \(\tau\) and \(\rho\): for \(d\ge3\), compare the primitive words with
one terminal symbol \(\zeta\) and \(\zeta^2\); for \(d=2,n\ge3\), compare a
word with one \(-1\) to one with two adjacent \(-1\).  Hence neither
observable is in \(K\).

In the Galois closure, a marked cycle has stabilizer \(S_{r-1}\).  This is a
maximal subgroup of \(S_r\).  Because each observable is already fixed by
\(S_{r-1}\) but is not fixed by all of \(S_r\), its stabilizer is exactly
\(S_{r-1}\).  Consequently

\[
 K(\tau)=F=K(\rho),
\]

and the two basis-free multiplication characteristic polynomials

\[
 \chi_s(T)=\det(T\operatorname{id}_{S_0}-m_s)\in A[T],
 \qquad s\in\{\tau,\rho\},
\]

defined on \(\bigwedge_A^rS_0\), are separately irreducible of degree \(r\)
over \(K\) and equal there to \(N_{F/K}(T-s)\).  Their nonzero difference
products record separability.  For \((d,n)=(2,2)\), \(r=1\) and the explicit
linear formulas replace the non-base argument.

## Claim-Driven Validation Sketch

### PC1: normalized primitive-cycle cover and monodromy

- Audit the monic basis, actual-period idempotent block, field property,
  normalization, special fiber, invariants, and subgroup direction.
- Use scalar formal-period, nonreduced-fiber, and cusp-normalization examples
  as mandatory falsifiers of the discarded construction.
- Machine algebra, if later authorized, checks only bounded identities and
  counterexamples; source proof plus independent source review remains the
  theorem authority.

### PC2: separate primitive coordinates \(\tau\) and \(\rho\)

- Audit cyclic invariance, the two non-base infinity comparisons, the
  \(S_{r-1}\) stabilizer step, norm-polynomial irreducibility, and discriminant
  nonvanishing.
- Lock the \((2,2)\) formulas as the sole positive finite boundary fixture.
- Reject any substitution of field trace, determinant, or one observable's
  proof for the other.

## Planning Gate

- Final method thesis: PC1 plus PC2 above.
- Dominant contribution: PC1.
- Supporting contribution: PC2 only.
- Explicitly rejected complexity: additional families, observables, periods,
  compactifications, and computational scans.
- Frontier primitive: absent; none is appropriate for an exact algebraic
  proof problem.
