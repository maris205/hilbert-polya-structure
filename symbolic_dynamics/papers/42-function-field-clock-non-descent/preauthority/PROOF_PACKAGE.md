# Proof Package

## Claim

Fix `q` in `{2,3,5}` and let `Prim_q` be the primitive cyclic necklaces of the
full `q`-shift. For `gamma` of length `n`, set

\[
 T_q(\gamma)=n\log q.
\]

Then:

1. there is no total map `pi:Prim_q -> P` to rational primes satisfying
   `log pi(gamma)=T_q(gamma)` for every `gamma`;
2. there is no factorwise identification of all source primitive factors
   `(1-z^n q^(-ns))^(-1)` with rational-prime factors
   `(1-z p^(-s))^(-1)` that preserves marker, weight, and multiplicity;
3. the source marked determinant `1-zq^(1-s)` differs from the rational-prime
   comparison determinant already in the first coefficient of its logarithm.

## Status

PROVABLE AS STATED

## Assumptions

- `q` is exactly one of the frozen rational primes `2,3,5`.
- `Prim_q` uses cyclic rotation and ordinary word primitivity.
- `z` is a free marker for one original source-symbol step.
- target rational-prime factors use one `z` for one primitive prime-loop
  traversal.
- analytic product comparisons occur on `Re(s)>1` and small `|z|`.

## Notation

- `[w]`: cyclic class of a nonempty word `w`.
- `n([w])=|w|` for a primitive word.
- `N_q(n)`: number of primitive necklaces of length `n`.
- `P`: set of positive rational primes.
- `P(s)=sum_(p in P) p^(-s)`.
- `D_q` and `D_P`: source and target-comparison determinants.

## Proof Strategy

Use three independent exact arguments: a length-two clock witness, a
length-one multiplicity count, and a first marked coefficient comparison.
None relies on target zeros or numerical approximation.

## Dependency Map

1. The clock theorem uses only primitivity of `01` and elementary
   exponentiation.
2. The factor theorem uses marker exponents, clock equality, and
   `N_q(1)=q`.
3. The determinant theorem uses fixed-point counts and the rational-prime
   Euler product in its absolute-convergence half-plane.
4. The positive control uses the classical necklace/irreducible-polynomial
   count equality but is not needed to derive the negative clock witness.

## Proof

### Lemma 0 — source determinant and primitive counts

**Statement.** The full `q`-shift satisfies

\[
 D_q(s,z)=1-zq^{1-s}
\]

and

\[
 N_q(n)=\frac1n\sum_{d\mid n}\mu(d)q^{n/d}.
\]

**Proof.** There are exactly `q^r` words fixed by the `r`th shift power.
Therefore

\[
 Z_q(s,z)=\exp\left(\sum_{r\ge1}
 \frac{q^r(zq^{-s})^r}{r}\right)
 =\frac1{1-zq^{1-s}}.
\]

Taking the inverse gives the determinant. Every fixed word has a unique least
period `d` dividing `r`, and each primitive cyclic class of length `d`
contributes `d` based words. Hence `q^r=sum_(d|r)dN_q(d)`. Möbius inversion
gives the displayed formula. QED.

**Novelty boundary.** Lemma 0 is classical and already owned by Paper 1.

### Theorem 1 — exact clock does not descend to rational-prime support

**Statement.** No total map `pi:Prim_q -> P` satisfies

\[
 \log\pi(\gamma)=n(\gamma)\log q
\]

for every primitive source necklace.

**Proof.** The word `01` belongs to every frozen alphabet and is primitive:
if it were a proper power, its length two would force it to be the square of a
length-one word, whose two symbols would be equal. Let `gamma=[01]`. Its
length is two. If the claimed map existed, then

\[
 \log\pi(\gamma)=2\log q=\log(q^2).
\]

The real logarithm is injective on positive numbers, so
`pi(gamma)=q^2`. Because `q>1`, `q^2` is composite, contradicting
`pi(gamma) in P`. QED.

**Quantifier note.** The theorem rules out total maps preserving this exact
clock. It does not rule out partial maps, relabelings with a different clock,
or a new induced object.

### Theorem 2 — marker, weight, and multiplicity cannot all descend

**Statement.** No factorwise identification of every source primitive factor

\[
 (1-z^n q^{-ns})^{-1}
\]

with a rational-prime factor `(1-zp^(-s))^(-1)` preserves marker, weight,
and multiplicity.

**Proof.** Equality of the formal `z` monomials requires `n=1`. Equality of
the analytic weights for all `s` then requires `p=q`. By Lemma 0,

\[
 N_q(1)=q.
\]

Thus `q` distinct source factors have the only compatible monomial
`zq^(-s)`, while the rational-prime Euler product has one factor indexed by
`p=q`. A multiplicity-preserving factorwise identification is impossible.
QED.

**Quantifier note.** Deleting factors, merging them, or changing the marker is
a projection/changed object and is outside the factorwise-identification
claim.

### Theorem 3 — first marked coefficient mismatch

**Statement.** On their common absolute-convergence domain, `D_q(s,z)` and
`D_P(s,z)` cannot be equal as analytic functions of `(s,z)`.

**Proof.** From Lemma 0,

\[
 [z]\{-\log D_q(s,z)\}=q^{1-s}.
\]

For the trace-class diagonal rational-prime comparator,

\[
 [z]\{-\log D_{\mathbb P}(s,z)\}=P(s)=\sum_p p^{-s}.
\]

Take real `s=sigma` and let `sigma` tend to infinity. If `q=2`, then
`2^sigma q^(1-sigma)=2`, whereas

\[
 2^\sigma P(\sigma)=1+\sum_{p\ge3}(2/p)^\sigma\longrightarrow1.
\]

If `q` is `3` or `5`, then

\[
 2^\sigma q^{1-\sigma}=q(2/q)^\sigma\longrightarrow0,
\]

while the same target expression tends to one. For the target limit, dominate
the tail for `sigma>=2` by `sum_(n>=3)(2/n)^2`, a convergent series, and apply
dominated convergence. In every frozen case the first coefficients differ,
so the analytic determinants differ. QED.

### Corollary 4 — bounded repair classification

**Statement.** Within the declared repairs in
`OBJECT_MARKER_OPERATOR_CONTRACT.md`, every repair gives up at least one of
rational-prime support, exact source clock, original marker, full
multiplicity, or source determinant ownership.

**Proof.** The norm projection fails support by Theorem 1. The degree-one
projection fails multiplicity by Theorem 2. Choosing one degree-one orbit is
not total. An arbitrary prime enumeration gives up exact clock. Inducing each
primitive to one return changes `z^n` to `z` and changes the operator/object.
The finite-field prime-polynomial dictionary retains the source ledger but
has a different primitive type from rational primes. These are exactly the
declared rows. QED.

**Quantifier note.** The corollary is exhaustive only over the listed repairs,
not over all symbolic factors or extensions.

## Corrections or Missing Assumptions

No correction to the stated claim is required. The phrase “rational-prime
projection” must always retain the totality and exact-clock qualifiers. The
source function-field ledger must never be described as failing.

## Open Risks

- The exact theorem may be too elementary for standalone novelty.
- A different target marker can evade Theorem 2 but not Theorem 1.
- An enlarged or induced system may encode rational primes, but it requires a
  new source lock and cannot repair `SD-C01` in place.
