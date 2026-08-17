# Derivation Package

## Target

Derive the exact relation among the full-`q` shift's primitive factors, its
finite-field norm clock, and the rational-prime marked Euler product, then
identify the first unavoidable failures without changing the source object.

## Status

COHERENT AS STATED

## Invariant Object

The invariant object is the source primitive factor

\[
 \left(1-z^{n(\gamma)}e^{-sT_q(\gamma)}\right)^{-1}
 =\left(1-z^{n(\gamma)}q^{-s n(\gamma)}\right)^{-1}
\]

owned by a primitive necklace `gamma` of the full `q`-shift. Object, clock,
marker, weight, multiplicity, and determinant owner remain attached to this
factor throughout the exact derivation.

## Assumptions

1. `q` is one of the rational primes `2, 3, 5` fixed by `SD-C01`.
2. Primitive words are aperiodic cyclic necklaces; rotations are quotiented
   and reversal is not automatically quotiented.
3. One shift step has clock `log q` and marker `z`.
4. A rational-prime primitive factor has clock `log p`, marker `z`, and
   multiplicity one.
5. Equalities involving the target product are asserted only on `Re(s)>1`
   and small `|z|`, or as formal coefficient identities where stated.

## Notation

- `Prim_q`: primitive cyclic necklaces over `F_q`.
- `n(gamma)`: primitive word length.
- `N_q(n)`: number of elements of `Prim_q` of length `n`.
- `T_q(gamma)=n(gamma) log q`: source clock.
- `P`: positive rational primes.
- `P(s)=sum_p p^(-s)`: prime zeta series on `Re(s)>1`.
- `D_q(s,z)`: source inverse zeta determinant.
- `D_P(s,z)`: separate rational-prime comparison determinant.

## Derivation Strategy

First derive the source periodic and primitive ledgers. Then compare one source
factor with one target factor at the clock and marker levels. Finally compare
the full marked determinants at their first `z` coefficient. Each comparison
is exact and gives an independent failure mode.

## Derivation Map

1. `#Fix(sigma^r)=q^r` gives `D_q(s,z)=1-zq^(1-s)`.
2. Möbius inversion gives `N_q(n)` and the primitive product.
3. Clock equality forces a proposed image prime to be `q^n`.
4. The primitive word `01` has `n=2`, so the forced image is composite.
5. Marker equality forces `n=1`; clock equality then forces `p=q`.
6. `N_q(1)=q`, so multiplicity fails even on the only compatible length.
7. The first marked trace coefficient gives an analytic failure independent
   of an objectwise map.

## Main Derivation

### Step 1 — periodic-point and determinant identity

The full `q`-shift has exactly `q^r` fixed points of `sigma^r`. Give each
original shift step the combined factor `z q^(-s)`. Its marked Artin-Mazur
series is

\[
 \begin{aligned}
 Z_q(s,z)
 &=\exp\left(\sum_{r\ge1}\frac{q^r(zq^{-s})^r}{r}\right)\\
 &=\exp\left(\sum_{r\ge1}\frac{(zq^{1-s})^r}{r}\right)\\
 &=\frac1{1-zq^{1-s}}.
 \end{aligned}
\]

This is an identity in the convergence disk and a formal identity in `z`.
Thus

\[
 D_q(s,z)=Z_q(s,z)^{-1}=1-zq^{1-s}.
\]

### Step 2 — primitive factors

Every period-`r` word is a unique repetition of a primitive necklace whose
length divides `r`. Hence

\[
 q^r=\sum_{d\mid r}dN_q(d).
\]

Möbius inversion gives

\[
 N_q(n)=\frac1n\sum_{d\mid n}\mu(d)q^{n/d}.
\]

Regrouping repetitions produces

\[
 Z_q(s,z)=\prod_{\gamma\in\operatorname{Prim}_q}
 \left(1-z^{n(\gamma)}q^{-s n(\gamma)}\right)^{-1}.
\]

This is also the closed-point Euler ledger of the affine line over `F_q`
after identifying degree-`n` source counts with monic irreducible-polynomial
counts. That is a positive control, not a rational-prime identification.

### Step 3 — clock support obstruction

Suppose a total map `pi:Prim_q -> P` preserves the exact clock. For a
length-`n` primitive necklace,

\[
 \log\pi(\gamma)=n\log q,
\]

so positivity and injectivity of the real logarithm imply

\[
 \pi(\gamma)=q^n.
\]

The cyclic word `01` is primitive for every frozen alphabet because it is not
a square of a length-one word. Its length is two, so its forced image is
`q^2`, which is composite. Therefore no such total rational-prime map exists.

### Step 4 — marker and multiplicity obstruction

Factorwise equality with a target factor requires

\[
 z^n q^{-ns}=z p^{-s}
\]

as a monomial identity. Equality of `z` exponents forces `n=1`; equality of
weights then forces `p=q`. But

\[
 N_q(1)=q.
\]

There are `q` distinct length-one primitive source factors and only one target
factor indexed by the rational prime `q`. Thus the compatible monomial type
still has source-to-target multiplicity `q:1`.

### Step 5 — first marked coefficient obstruction

The source logarithm is

\[
 -\log D_q(s,z)=\sum_{r\ge1}\frac{z^r}{r}q^{r(1-s)},
\]

so its `z` coefficient is `q^(1-s)`. The rational-prime comparison is

\[
 -\log D_{\mathbb P}(s,z)
 =\sum_{r\ge1}\frac{z^r}{r}P(rs),
\]

whose `z` coefficient is `P(s)`.

These functions are unequal. For real `sigma -> +infinity`:

- if `q=2`, multiplying by `2^sigma` gives source value `2`, while
  `2^sigma P(sigma) -> 1`;
- if `q` is `3` or `5`, multiplying by `2^sigma` gives source value
  `q(2/q)^sigma -> 0`, while `2^sigma P(sigma) -> 1`.

The target limit follows because the prime `2` contributes one and the
remaining absolutely convergent terms tend to zero by dominated convergence.
Therefore the two marked determinants disagree before any global divisor
question.

### Step 6 — repetition typing

Source repetition of a length-`n` primitive factor gives

\[
 z^{nr}q^{-nrs}.
\]

Target repetition gives

\[
 z^r p^{-rs}.
\]

The weight part would agree under `p=q^n`, but the marker part agrees only
when `n=1`. Because the primitive comparison already fails support or
multiplicity, repetition cannot repair it.

## Remarks and Interpretation

- The clock is perfectly cyclic and temporally additive on the source. This
  differs from the rooted-clock failure of Paper 41.
- The finite-field norm `q^n` is the correct source arithmetic norm. The
  obstruction is precisely that it is a prime power/cardinality, not a
  rational prime for `n>=2`.
- The determinant mismatch is not inferred from zeros. It occurs in the
  first marked trace coefficient.
- An arbitrary enumeration of source primitives by rational primes can alter
  labels, but it cannot preserve the exact clock and source marker.

## Boundaries and Non-Claims

- No canonical-bijection theorem between necklaces and irreducible
  polynomials is claimed; only count equality is used.
- No universal naturality theorem over all functors or projections is claimed.
- No claim is made about infinite-memory, countable, induced, or re-marked
  systems after a new source lock.
- The inherited `O(R)` divisor-growth theorem remains Paper 1's result and is
  not re-proved as Paper-42 novelty.

## Open Risks

- A primary source may already state this exact clock/marker comparison in
  different language; independent citation chaining is required.
- A reviewer may reject the target primitive marker `z` as the only useful
  convention. The clock-support theorem remains valid independently of that
  marker choice.
- The result is mathematically elementary; standalone significance depends on
  its role as a rigorously typed closure in the larger program.
