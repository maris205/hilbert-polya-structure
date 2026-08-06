# Narrative report

## One-sentence contribution

The proposed dihedral quotient of parameter-varying Hénon exact-period covers
does not supply a new Route-A mechanism: its orbit marker and reversor
decomposition are direct prior work, the quotient retains only the trivial
dihedral sector, and every period-six component has genus zero.

## Research question

Does retaining the Hénon parameter and quotienting an exact-period cover by
time translation and reversal create a positive-dimensional arithmetic object
whose Frobenius cohomology preserves enough dynamics to be a credible Route-A
or Hilbert--Pólya precursor?

## Evidence

1. The scaling \(x=Aq\) identifies the exact Paper-5 recurrence with the
   Hamiltonian Hénon family used by Endler and Gallas.
2. Their orbital polynomial \(S_n(\sigma)\), its
   \(C_n(\sigma)^2D_n(\sigma)N_n(\sigma)\) factorization, and Gallas's
   arbitrary-period Möbius formulas already construct the cyclic/dihedral
   orbit marker proposed in C12C.
3. For a finite étale exact-period cover with \(D_n\)-action, functions on the
   coarse quotient are the invariant sector.  The generator \(H\in D_n\) acts
   identically there, and the Frobenius trace is the average of the joint
   traces over \(D_n\).  This is compatible with an unmarked scalar orbit
   zeta, but it cannot support claims about non-trivial isotypic joint action.
4. At period six, the squarefree marker is \(C_6D_6N_6\).  The first two
   components are manifestly rational.  The discriminant of \(N_6\) as a
   quadratic in \(A\) is
   \[
   16(\sigma-6)(\sigma+2)(3\sigma^2-8\sigma-12)^2,
   \]
   so its normalization is birational to
   \(Y^2=(\sigma-6)(\sigma+2)\), also rational.
5. Exact code reproduces the period-one through period-35 class counts and
   detects a period-14 arithmetic typo in the published display without
   changing the prior-art conclusion.

## Scope

The result rejects the registered **coarse quotient as a new global Route-A
mechanism**.  It does not kill scalar zeta functions of unmarked autonomous
cycles, the full equivariant exact-period cover, its non-trivial
\(D_n\)-isotypic local systems, or a future theorem establishing compatible
monodromy across periods.  Those objects currently lack a cross-period tower,
a prime-like clock, and a target divisor, so they are not promoted here.

## Decision

```text
STOP C12C as a new direct Route-A object; do not compute another low-period
quotient curve without a cross-period determinant theorem.
PIVOT to a different dynamical form with a canonical self-adjoint operator.
```
