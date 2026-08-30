# Narrative Report — P119

External status: **HOLD**. This is an internal theorem narrative, not a
novelty or priority statement.

## The system

Let `N=sum E_(i,i+1)`, fix the regular element `J=I+N` in `U_n(F_q)`, and
iterate

```text
E(X)=X^(-1) J^(-1) X J.
```

The filtration `gamma_k` consists of matrices whose first `k-1`
superdiagonals vanish. It runs from `gamma_1=U_n(F_q)` to
`gamma_n={I}`.

## Owned image theorem and exact residual

Bier 2013 proves over arbitrary fields, for the same fixed regular `J` and
commutator convention,

```text
E(gamma_k)=gamma_(k+1),
```

and the corresponding fixed-`J` iterated Engel images.  These image and
existence statements receive zero contribution credit.  The residual begins
with the finite-field refinement that every target in `gamma_(k+1)` has a
left-coset fibre of exact size `q^(n-k)`.

Composition of those exact counts gives, for `0<=t<=n-k`,

```text
E^t(gamma_k)=gamma_(k+t),
#((E^t|gamma_k)^(-1)(Y)) = q^S(k,t)
```

for `Y` in the displayed image, where
`S(k,t)=sum_(j=k)^(k+t-1)(n-j)`. Therefore

```text
L(k,0)=1,
L(k,t)=(q^(n-k-t+1)-1) q^(sum_(j=k)^(k+t-2)(n-j)).
```

On the full phase the height is exactly `n-1`, the deepest shell has
`(q-1)q^(binom(n,2)-1)` states, the identity is the unique recurrent point,
and the zeta function is `(1-z)^(-1)`. Nested source levels also give exact
filtration-stratum indegrees, so the result records more than the global
depth histogram.

## Why the two proofs differ

The first proof is group-theoretic. With `phi(X)=J^(-1)XJ`, equality of two
values of `X^(-1)phi(X)` says that `X_2 X_1^(-1)` is fixed by `phi`.
Fibres are therefore left cosets. The regular matrix centralizer is exactly

```text
I + a_k N^k + ... + a_(n-1) N^(n-1),
```

which gives `q^(n-k)` elements. Cardinality then upgrades the automatic
image inclusion to equality.

The second counting proof never counts a centralizer or invokes
orbit–stabilizer.
Writing `X=I+A`, `Y=I+B`, the equation becomes

```text
AN-NA = B+NB+AB+NAB.
```

At source superdiagonal `r`, its left side is the onto difference
`(x_1,...,x_m) -> (x_1-x_2,...,x_(m-1)-x_m)`. The right side uses only the
target and source diagonals below `r`; hence the system is triangular.
There is one free field constant at each of the `n-k` stages.

## Strongest scope guard

In `U_4(F_q)`, take `J'=I+E12+E34`. A matrix commutes with `J'` exactly
when `a_23=0` and `a_24=a_13`, leaving four free coordinates. Thus its
centralizer has `q^4` elements and the commutator image has `q^2` elements,
strictly fewer than the `q^3` elements of `gamma_2`. This kills any wording
that replaces the fixed regular shift by an arbitrary unipotent element. It
does not say that every nonregular choice fails.

## Owner subtraction

- Bier owns the same fixed-`J` restricted surjectivity and iterated Engel
  images over arbitrary fields.  Those are reproduced only to make the
  finite dynamics self-contained.
- Lang and Steinberg own the twisted-coboundary setting and terminology.
  Their global Lang-surjectivity hypotheses do not prove the restricted
  inner-automorphism surjections used here.
- Acciarri–Shumyatsky and Khukhro–Shumyatsky explicitly own the
  fixed-second-variable left Engel sequence and sink language.
- Regular Jordan centralizers, lower-central filtrations of unitriangular
  groups, and broad unipotent conjugacy theory are classical.
- Artin–Mazur conversion from fixed counts to zeta is standard.

The residual is only the finite-field left-coset fibre sizes and their exact
fixed-regular `(q,n,k,t)` depth and filtration-typed predecessor census,
together with the explicit `U_4` guard. Search absence remains a bounded
no-hit.

## Internal firewall

P109 evolves subspaces by the image of a regular nilpotent linear operator;
its fibre engine is Grassmannian intersection counting. P119 evolves group
elements by a fixed nonlinear commutator and uses centralizer cosets or
triangular group coordinates. P111 is a random positive word product in an
integer Heisenberg group with area and limit observables. Neither internal
system shares P119's update.

## Evidence package

The canonical verifier uses six literal finite fields and exhausts 55,808
regular phase states plus 20,514 near-regular counterexample states. It
executes 1,491,877 assertions. The 43-row TSV artifact gives exact cumulative
and point layers for all valid `(k,t)` at `(q,n)=(2,6),(3,5),(4,4)`.
Computation is falsification evidence only.
