# C146 proof package

## Claim and status

**Status: PROVABLE AFTER WEAKENING.**  The all-iterate central fixed-circle,
singular-stability, zero-Lefschetz, and transverse toral-count claims are
proved.  The proposed stronger assertion that all horizontal fixed classes
lift to circles is false for the frozen standard lattice automorphism; an
exact counterexample is included.

## Assumptions and notation

Write the real Heisenberg group in upper-triangular coordinates as

```text
(x,y,z)*(X,Y,Z)=(x+X,y+Y,z+Z+xY).
```

Let `Gamma=Z^3`, `N=Gamma\H`,

```text
A=[[2,1],[1,1]],
q(x,y)=x(x-1)+xy+y(y-1)/2,
Phi(x,y,z)=(2x+y,x+y,z+q(x,y)).
```

The central circle is `C={[0,0,z]:z mod 1}`.  Let `L_k` denote the Lucas
sequence `L_0=2,L_1=1,L_(k+1)=L_k+L_(k-1)`.

## Dependency map

1. The lattice map uses the exact polarization of `q`.
2. The clean component uses pointwise central fixation and horizontal
   hyperbolicity.
3. Stability singularity uses the block-triangular derivative.
4. The Lefschetz computation uses explicit Heisenberg cohomology.
5. The toral count uses the finite cokernel of `A^n-I` and `tr(A^n)=L_(2n)`.
6. The rejected lift uses the left-quotient fixed equation at `n=2`.

## Theorem 1: genuine lattice automorphism

The displayed `Phi` is a Lie-group automorphism of `H`, maps `Gamma`
bijectively to itself, and hence descends to `N`.

**Proof.**  For `v=(x,y)` and `w=(X,Y)`, direct expansion gives

```text
q(v+w)-q(v)-q(w)=2xX+xY+Xy+yY.                 (1)
```

The old cocycle is `c(v,w)=xY`.  The new one is

```text
c(Av,Aw)=(2x+y)(X+Y),
```

so `c(Av,Aw)-c(v,w)` is exactly the right side of (1).  Equality of the
central coordinates in `Phi(g*h)=Phi(g)*Phi(h)` follows, while the horizontal
coordinates follow from linearity of `A`.  For integers `m,n`, each of
`m(m-1)`, `mn`, and `n(n-1)/2` is integral, so `Phi(Gamma)` is contained in
`Gamma`.  Since `A^{-1}` is integral and the inverse central correction is
`-q(A^{-1}v)`, the inverse also preserves `Gamma`; the containment is a
bijection.  Therefore the quotient map is well defined. ∎

## Theorem 2: an all-iterate clean fixed component

For every `n>=1`, `C` is a connected component of `Fix(Phi^n)`, and the fixed
set is not discrete.

**Proof.**  Since `q(0,0)=0`, `Phi(0,0,z)=(0,0,z)`, so every point of `C` is
fixed by every iterate.  The horizontal eigenvalues of `A` are
`(3+sqrt(5))/2` and `(3-sqrt(5))/2`; neither has a positive power equal to
one.  Hence `A^n-I` is nonsingular.  The fixed-base classes in the horizontal
torus are therefore finite and discrete, so the fibre over the zero class is
locally isolated in horizontal directions.  Its entire central fibre is
fixed.  More precisely, along `C` the derivative has block form
`[[A^n,0],[ell_n,1]]`.  If `(I-DPhi^n)(delta v,delta z)=0`, its horizontal
equation is `(I-A^n)delta v=0`, hence `delta v=0`; the central variation
`delta z` is free.  Thus `ker(I-DPhi^n)=T C`, proving that `C` is a clean
one-dimensional connected component. ∎

## Theorem 3: singular isolated stability at every iterate

For every point and every `n>=1`, the derivative of `Phi^n` has diagonal
blocks `A^n` and `1`.  Consequently

```text
det(I-DPhi^n)=det(I-A^n)(1-1)=0.               (2)
```

**Proof.**  The central coordinate of `Phi` is `z+q(x,y)`.  Its Jacobian is
block lower triangular with diagonal blocks `A` and `1`.  Products retain
this form with diagonal blocks `A^n` and `1`, so determinant factorization
gives (2).  Thus the ordinary denominator for an isolated periodic orbit is
singular; C146 does not replace it with a clean-trace regularization. ∎

## Theorem 4: zero Lefschetz number

For all `n>=1`, `L(Phi^n)=0`.

**Proof.**  Put `alpha=dx`, `beta=dy`, and `gamma=dz-x dy`; then
`d gamma=-alpha wedge beta`.  The inclusion of the left-invariant de Rham
complex into the de Rham complex of a compact quotient of a connected,
simply-connected nilpotent Lie group is a cohomology isomorphism (the Nomizu
theorem); `H` and `Gamma\H` satisfy exactly these hypotheses.  Computing the
three-generator invariant complex gives dimensions `(1,2,2,1)`, with bases
`1`, `[alpha],[beta]`, `[alpha wedge gamma],[beta wedge gamma]`, and
`[alpha wedge beta wedge gamma]`: `alpha,beta` are closed, `gamma` is not,
`alpha wedge beta=-d gamma` is exact, the other two degree-two forms are
closed and nonexact in this finite complex, and the volume form spans degree
three.  Pullback acts with trace `tr(A^n)` on both
middle cohomology groups: horizontal correction terms in `Phi^*gamma` only
add multiples of the exact form `alpha wedge beta`.  It acts as the identity
on degrees zero and three because `det A=1` and the center multiplier is one.
The alternating trace is therefore

```text
1-tr(A^n)+tr(A^n)-1=0.                          (3)
```

This agrees with the determinant obstruction but does not count the clean
components. ∎

## Proposition 5: exact toral negative control

The induced map on `T^2` has exactly

```text
|det(A^n-I)|=tr(A^n)-2=L_(2n)-2                (4)
```

isolated fixed points at iterate `n`.

**Proof.**  Fixed classes form the kernel of `A^n-I` on `R^2/Z^2`.  For an
integer matrix with nonzero determinant, that kernel has order equal to the
index of `(A^n-I)Z^2`, namely the determinant's absolute value.  Since
`det(A^n)=1`, `det(A^n-I)=2-tr(A^n)<0`.  Finally `A=Q^2` for
`Q=[[1,1],[1,0]]`, whose power trace is the Lucas number, so
`tr(A^n)=L_(2n)`.  Nonsingularity makes all these toral points isolated. ∎

## Proposition 6: the naive fibre count is false

At `n=2`, the horizontal class `v=(1/5,2/5)` satisfies
`(A^2-I)v=(2,1)`, but no point over it is fixed by `Phi^2` on `Gamma\H`.

**Proof.**  Along the two iterates,
`q(v)+q(Av)=-1/5+1/5=0`.  If a point `g=(v,z)` were fixed in the left
quotient, there would be `gamma=(2,1,k)` in `Gamma` with
`Phi^2(g)=gamma*g`.  Comparing central coordinates requires
`0=k+2(2/5)=k+4/5`, impossible for integer `k`.  Equivalently the frozen
condition value is `-4/5`, not an integer. ∎

## Boundaries and open risks

The theorem proves one clean fixed-circle component at every iterate and the
exact horizontal control count.  It does not enumerate all fixed components
of the nilmanifold.  No clean fixed-set trace formula is constructed.  There
is a limited natural lift hint: Haar measure is preserved, so
`U_Phi f=f composed with Phi` is unitary on all of `L^2(N,Haar)` and retains
the iterate clock.  No identity connects it to the singular clean-family
weights, so this does not exceed `A4_FORMAL_HINT`.  There is no target divisor,
target functional equation, counting law, arithmetic/local interpretation,
Hilbert--Polya claim, or Route-B authorization.  Verdict:
`(A1_FAIL,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`.
