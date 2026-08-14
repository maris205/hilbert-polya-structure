# NARRATIVE REPORT — SD-C22

## One-sentence result

Making the explicit semiring primality verifier recurrent produces an exact
prime orbit ledger, but the arithmetic clock $\log p$ is diluted over
$\asymp p\log p$ graph steps, forcing the natural whole vertex adjacency to
be noncompact; first return restores the Euler product only by erasing the
computation.

## Why this candidate was tested

SD-C21 showed that a deterministic trial-division graph can compute primality
from full-shift alphabet sum, Cartesian product, and entropy, but its
computation lived in a transient directed acyclic graph.  Its determinant saw
only prime accept loops.  The most direct repair was therefore to make the
verification itself recurrent: close every successful computation back to
its input and let the quotient-search states lie on the prime orbit.

That repair succeeds combinatorially.  Every prime has one primitive cycle,
every composite falls into an acyclic cemetery, and the total cycle clock can
be set to $h(F_p)=\log p$.  Nothing in the primitive-orbit inventory imports a
prime table.

## What breaks

The verifier is long.  Its contracted cycle has

\[
\ell(p)=2+\sum_{d=2}^{\lfloor\sqrt p\rfloor}\left\lceil p/d\right\rceil
\sim\frac12p\log p.
\]

An exact total roof of only $\log p$ cannot keep every edge clock large.  Some
edge has roof at most $\log p/\ell(p)$, so its weight approaches one for every
fixed $\operatorname{Re}s>0$.  Because the prime cycles occupy mutually
orthogonal vertex blocks, these near-isometric edges escape every compact
tail.  The whole adjacency is not compact, lies in no finite Schatten class,
and has the unit circle in its essential approximate spectrum.

This is a sharp incompatibility for the frozen object:

```text
exact arithmetic orbit clock log p
              +
explicit graph-step verification of length ~ (p/2) log p
              |
              v
edge clocks approach zero, edge weights approach one
              |
              v
no ordinary whole-vertex Fredholm determinant
```

## What survives

Each finite prime block still has determinant
$1-z^{\ell(p)}p^{-s}$.  Consequently the raw orbit product

\[
\prod_p(1-z^{\ell(p)}p^{-s})
\]

converges normally for $\operatorname{Re}s>1$ and $|z|\le1$.  At $z=1$ it is
$1/\zeta(s)$.  This identity is useful but must remain a combinatorial orbit
ledger; it is not a Fredholm determinant of the noncompact whole operator.

Inducing on the input states gives the diagonal return operator
$R_s e_p=p^{-s}e_p$.  This is trace class for $\operatorname{Re}s>1$ and has
the desired Euler determinant.  It is also exactly the prime-loop core already
isolated in Paper 04.  The verifier has disappeared between returns.  The
marker exposes the loss: the original graph counts $z^{\ell(p)}$, whereas the
return map counts $z$.

## Why the negative result matters

The obstruction is not peculiar to trial division or to primes.  A total
decider for any infinite support can be padded by an acceptance-independent
uniformly prescribed delay.  Closing accepted computations and assigning
total clock $\log n$ then reproduces the same noncompactness.  Thus a
vertex-disjoint ``algorithm per integer'' can compile essentially arbitrary
decidable Euler supports.  It proves too much to supply intrinsic arithmetic
selectivity.

The experiment reinforces, rather than replaces, the proof.  The exact suite
passes twelve tests, matches all 564 prime cycles through 4096, gives
$\ell(4093)=15293$, and finds the best possible largest edge weight at
$s=2$ already equal to $0.9989128997668932$.  The raw and induced markers
agree at $z=1$ and separate at $z=1/3$.

## Route decision

SD-C22 earns structural arithmetic relation and analytic-consistency credit,
but it fails the same-object determinant gate and all downstream spectral
gates:

```text
(A0_STRUCTURAL_ARITHMETIC_RELATION,
 A1_PASS_ANALYTIC,
 A2_FAIL,
 A3_FAIL,
 A4_FAIL)

ROUTE_A_REJECTED
ROUTE_B_LOCKED
```

The next in-family candidate must not add another disjoint verifier wrapper.
It must begin with an overlapping, genuinely recurrent semiring-local grammar
and prove primitive-cycle separation before selecting a roof or determinant.
