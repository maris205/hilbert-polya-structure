# Proof package

## Main theorem

Let

```text
Gamma = <a,b,c | [a,b]=c, [a,c]=[b,c]=1>
```

and use coordinates with

```text
(x,y,z)(u,v,w)=(x+u,y+v,z+w+xv).
```

For an odd prime `ell`, let `N_ell` be the kernel of coordinate reduction
onto `Q_ell=Heis(F_ell)`.  Let `p != ell` be prime and let
`alpha,beta,gamma` be nonzero elements of `F_p`.  Define

```text
X = {x in F_p^Gamma :
     alpha*x_g+beta*x_(ga)+gamma*x_(gb)=0 for every g in Gamma}.
```

Then

```text
dim_Fp Fix_(N_ell)(X)
 = D_(p,ell)(alpha,beta,gamma)
   + ell(ell-1) 1_[alpha^ell+beta^ell+gamma^ell=0],
```

where

```text
D_(p,ell)(alpha,beta,gamma)
 = deg gcd_Fp(t^ell-1,(alpha+beta*t)^ell+gamma^ell).
```

For unit coefficients the nonlinear term is present exactly when `p=3`.

## Status

**PROVABLE AS STATED**, subject to the frozen assumptions `ell` odd,
`p != ell`, and `alpha*beta*gamma != 0`.

## Proof

### 1. Finite quotient reduction

Use the left shift `(h.x)_g=x_(h^{-1}g)`.  An `N_ell`-fixed point is constant
on left cosets.  Since `N_ell` is normal, the coset space is the group
`Q_ell`, and right multiplication by the images of `a` and `b` is well
defined.  Consequently the fixed space is the kernel, on `F_p^{Q_ell}`, of

```text
(Tf)(q)=alpha*f(q)+beta*f(qa)+gamma*f(qb).
```

Tensoring this finite-dimensional kernel calculation with an algebraic
closure `k` of `F_p` preserves rank and nullity.

### 2. Irreducible decomposition

Because `p` does not divide `|Q_ell|=ell^3`, Maschke's theorem applies over
`k`.  The group has `ell^2` one-dimensional representations, obtained by
sending `a` and `b` independently to `ell`th roots of unity and sending the
center to one.  For every nontrivial central character `zeta`, define the
degree-`ell` clock--shift module over `k`.  The clock has distinct eigenlines,
and the shift permutes them cyclically, so every nonzero invariant subspace is
the whole module.  Distinct central characters distinguish these modules.
The squared-degree check

```text
ell^2 + (ell-1)ell^2 = ell^3
```

then proves completeness of the list in the split semisimple group algebra.

In the regular representation an irreducible of degree `d` occurs with
multiplicity `d`.  Therefore every singular character contributes one to the
nullity and every singular nonlinear block contributes `ell`.

### 3. Character blocks

Let `u^ell=v^ell=1`.  The character block is the scalar

```text
alpha+beta*u+gamma*v.
```

Since `gamma` is nonzero, a choice of `u` determines at most one `v`, namely
`v=-(alpha+beta*u)/gamma`.  Because `ell` is odd,

```text
v^ell=1
  iff (alpha+beta*u)^ell+gamma^ell=0.
```

The polynomial `t^ell-1` is separable because `p != ell`.  Its common roots
with `(alpha+beta*t)^ell+gamma^ell` therefore count the singular character
blocks without multiplicity.  This count is exactly the displayed gcd degree
`D_(p,ell)`.

### 4. Nonlinear blocks

Fix a nontrivial central character and a primitive `ell`th root `zeta` in
`k`.  After possibly replacing `zeta` by another primitive root, choose the
clock--shift model

```text
U=diag(1,zeta,...,zeta^(ell-1)),
V e_j=e_(j+1 mod ell).
```

The relevant block is

```text
A=alpha I+beta U+gamma V.
```

Write `d_j=alpha+beta*zeta^j`.  In the determinant of
`diag(d_0,...,d_(ell-1))+gamma V`, a nonzero permutation term must choose
either every diagonal entry or every entry of the single `ell`-cycle.
Since `ell` is odd, the cycle has sign `(-1)^(ell-1)=1`.  Hence

```text
det A = product_(j=0)^(ell-1)(alpha+beta*zeta^j)+gamma^ell
      = alpha^ell+beta^ell+gamma^ell.
```

The last identity follows by evaluating the factorization of `X^ell-Y^ell`
at `X=alpha` and `Y=-beta`.

It remains to control corank.  In coordinates, `Ax=0` is a cyclic first-order
recurrence of the form

```text
d_j x_j + gamma*x_(j-1)=0.
```

Because `gamma` is nonzero, any one coordinate determines all the others.
Thus the kernel has dimension at most one.  It is nonzero precisely when the
determinant vanishes, and in that case its dimension is exactly one.  The
determinant does not depend on the chosen nontrivial central character, so
all `ell-1` nonlinear representation types become singular simultaneously.

### 5. Restore multiplicities and descend

The character contribution is `D_(p,ell)`.  A singular nonlinear type has
block nullity one and regular multiplicity `ell`; with `ell-1` types, its
total contribution is `ell(ell-1)`.  Summing the contributions gives the
formula over `k`, and scalar-extension invariance gives the same dimension
over `F_p`.

For `alpha=beta=gamma=1`, the nonlinear determinant is `3`.  It vanishes in
`F_p` exactly for `p=3`, completing the specialization.

## Left/right convention audit

The shift and local equation above give right translation.  On the matrix
coefficient `phi_(lambda,v)(q)=lambda(pi(q)v)`, one has
`R_h phi_(lambda,v)=phi_(lambda,pi(h)v)`.  Thus the chosen operator has the
block `alpha I+beta pi(a)+gamma pi(b)` with no hidden inverse or transpose.
A formulation by the dual convention replaces each representation by its
contragredient.  On
the character sector this inverts and permutes the `ell`th roots.  On the
nonlinear sector it inverts and permutes the nontrivial central characters.
Since the theorem sums nullities over all such blocks and the determinant is
independent of the chosen central character, the formula is convention
invariant even though the individual matrices are not literally identical.

## Control role

The standalone script first checks four direct clock--shift blocks, including
both determinant strata, and then forms the full `ell^3`-square right-
translation matrix for ten parameter tuples.  The direct blocks verify the
determinant and zero/one-nullity lemmas on those samples.  The full quotient
matrices verify the implementation of the displayed group law, the selected
finite operator, and the final nullity formula; they can expose many
transcription or implementation mistakes, including an omitted regular
multiplicity.  A comparison of total nullities alone does not distinguish the
right-translation convention from the dual left convention, because the
preceding audit proves that the total nullity is invariant under that change.
The controls supply no asymptotic or all-parameter proof.
