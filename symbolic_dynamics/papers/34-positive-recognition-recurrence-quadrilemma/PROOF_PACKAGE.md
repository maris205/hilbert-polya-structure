# Proof package — Paper 34 / SD-C36

## 1. Assumptions

Let `G=(V,E)` be a countable loop-allowed directed graph with no parallel
edges. Let `A` be a countable
atom set with multiplicatively free norms `N(a)>1`. Assume:

1. the primitive closed directed edge words are exactly one `gamma_a` for
   each `a in A`;
2. `T(gamma_a)=log N(a)` for an additive edge roof;
3. a finite alphabet of size `b>=2` separates the cyclic atom labels when the
   coding conclusion is invoked; and
4. `N(a_j)<=j^kappa` eventually in nondecreasing norm order when the
   quantitative conclusion is invoked.

The free variable `z` counts original graph edges. All no-cancellation
arguments are literal and positive.

## 2. Main theorem

### Theorem 2.1 — positive recognition-to-recurrence quadrilemma

Under the assumptions above:

1. every atom orbit is a simple directed cycle, distinct atom cycles are
   vertex-disjoint, and every recurrent SCC is exactly one atom cycle;
2. if the whole adjacency `L_sigma` is trace class, deleting every edge
   outside the atom cycles preserves all power traces and the Fredholm
   determinant;
3. finite visible separation and polynomial atom growth give infinitely many
   atoms with

   ```text
   ell(a)>=log N(a)/(2 kappa log b),
   ```

   and the bounded whole adjacency is noncompact for every real `sigma>0`;
4. first return changes `1-z^{ell(a)}N(a)^(-s)` to
   `1-zN(a)^(-s)`. Equality as a positive free-marker germ forces
   `ell(a)=1` for every atom.

Consequently, within this class, shared recurrence violates the ledger,
terminal recognition prunes, private visible cycles lose whole-operator
compactness, and inducing changes the clock.

## 3. Recurrent rigidity

### Lemma 3.1 — atom cycles are simple and pairwise disjoint

Every `gamma_a` is simple, and two distinct atom cycles have no common
vertex.

**Proof.** Suppose `gamma_a` and `gamma_c` meet at a vertex. Rotate their edge
words to based closed words `x,y`. Write the unique primitive-root
decomposition `xy=w^m`. The literal ledger identifies `w` with a rotation of
one `gamma_d`. Roof additivity gives

```text
log N(a)+log N(c)=m log N(d),
```

so `N(a)N(c)=N(d)^m`, a nonzero integer exponent relation among the free
norms. This is impossible.

If `gamma_a` repeats a vertex before closing, rotate there and split its word
into nonempty closed words `x,y`. Writing `x=u^m`, `y=v^n` with primitive
roots gives

```text
N(a)=N(c)^m N(d)^n,
```

again contradicting multiplicative freeness. Therefore the atom cycles are
simple and pairwise vertex-disjoint. ∎

### Lemma 3.2 — recurrent SCCs are private cycles

Every recurrent SCC is exactly one atom cycle.

**Proof.** Suppose one SCC contains distinct atom cycles `gamma_a` and
`gamma_c`. They are vertex-disjoint by Lemma 3.1. Choose any directed path
`alpha` from the first cycle to the second and any directed path `beta` back.
The closed word

```text
W=gamma_a alpha gamma_c beta
```

has a primitive root `w`. Because `W=w^m`, `w` and `W` have the same edge
support. The ledger identifies `w` with an atom cycle. It meets `gamma_a`, so
Lemma 3.1 forces it to equal `gamma_a`; yet it contains an edge of the
vertex-disjoint `gamma_c`. Contradiction.

Every edge internal to an SCC lies on a closed walk: append a return path from
its target to its source. Thus an extra recurrent edge beside one atom cycle
produces another primitive root and the same contradiction. Every recurrent
SCC contains a cycle, and the ledger lists all primitive cycles. Hence it is
exactly one atom cycle. ∎

**Hypothesis repair.** The proof uses neither shortest connectors nor
connector interiors disjoint from both cycles. The stronger preregistered
normal form is false on finite graphs. Mutual reachability and arbitrary SCC
paths are sufficient.

## 4. Exact pruning

### Lemma 4.1 — off-core edges are trace/determinant invisible

Let `C_sigma` retain only the atom-cycle edges. If `L_sigma` is trace class,
then `C_sigma` is trace class and, for every `r>=1`,

```text
Tr L_sigma^r = Tr C_sigma^r.
```

Moreover,

```text
det(I-zL_sigma)
 = det(I-zC_sigma)
 = product_a (1-z^{ell(a)}N(a)^(-sigma)).
```

**Proof.** Let `V_c` be the atom-cycle vertices. Let `U` send every such
vertex to its successor and fix all other vertices. The diagonal conditional
expectation is contractive on trace class. Because no off-core vertex has a
self-loop,

```text
D_sigma=E_diag(U^*L_sigma)
```

is diagonal with exactly the cycle-edge weights, and `C_sigma=UD_sigma`.
Thus `||C_sigma||_1<=||L_sigma||_1`.

The diagonal coefficient of `L_sigma^r` is the nonnegative sum of length-`r`
closed walks based at that vertex. Every edge in a closed walk is recurrent,
so Lemma 3.2 confines the walk to one atom cycle. The corresponding diagonal
coefficients of `L_sigma^r` and `C_sigma^r` coincide. Summing them proves the
power-trace identity. The trace logarithm proves determinant equality near
zero, and entireness extends it to all `z`. A simple weighted `ell(a)`-cycle
has determinant `1-z^{ell(a)}N(a)^(-sigma)`, which gives the product. ∎

## 5. Finite visible coding

### Lemma 5.1 — logarithmic cycle-length subsequence

If the finite visible code separates atoms and `N(a_j)<=j^kappa` eventually,
then infinitely many atoms satisfy

```text
ell(a)>=log N(a)/(2 kappa log b).
```

**Proof.** Let `M_J=max_{j<=J}ell(a_j)`. Fewer than

```text
sum_{r=1}^{M_J} b^r < b^{M_J+1}/(b-1)
```

nonempty visible words have length at most `M_J`; cyclic words are no more
numerous. Separation therefore gives `J< b^{M_J+1}/(b-1)`, and eventually
`M_J>=log J/(2 log b)`. At every record index `J`, the new atom has length
`M_J`. Record atoms form an infinite subsequence. Combining the record bound
with `log N(a_J)<=kappa log J` proves the claim. ∎

For primes, the elementary eventual estimate `p_J<=J^2` yields
`ell(p)>=log p/(4 log b)` on an infinite subsequence.

### Lemma 5.2 — whole-operator noncompactness

For each real `sigma>0`, the whole adjacency is either unbounded or bounded
and noncompact.

**Proof.** On every cycle in the subsequence of Lemma 5.1, choose an edge of
minimum roof. Its roof is at most the average:

```text
tau(e_a)<=log N(a)/ell(a)<=2 kappa log b.
```

Its coefficient is therefore at least `b^{-2 kappa sigma}`. The source
vertices lie on pairwise disjoint cycles, so their standard basis vectors are
orthonormal and weakly null. Positivity gives

```text
||L_sigma delta_{o(e_a)}||_2 >= b^{-2 kappa sigma}.
```

A compact operator sends a bounded weakly-null sequence to a norm-null
sequence. This contradiction proves noncompactness whenever the operator is
bounded. Every finite Schatten-class operator is compact. ∎

## 6. Marker ownership

### Lemma 6.1 — first return changes time

Inducing on one basepoint per atom cycle gives

```text
R_s e_a=N(a)^(-s)e_a.
```

When the weights are summable, this diagonal is trace class and

```text
det(I-zR_s)=product_a(1-zN(a)^(-s)).
```

The raw factor is `1-z^{ell(a)}N(a)^(-s)`. The raw and induced factors agree
at `z=1`, but agree as free-marker germs only if `ell(a)=1`.

**Proof.** One return traverses the full cycle and multiplies its weights to
`exp(-sT(gamma_a))=N(a)^(-s)`. This proves the induced formula. One induced
step equals `ell(a)` original steps, which proves the two factors.

For the converse, compare the coefficient of `z` in an absolutely convergent
positive trace logarithm. The raw coefficient is

```text
sum_{a:ell(a)=1} N(a)^(-sigma),
```

while the atom target coefficient sums over all atoms. Positivity forces all
lengths to equal one. A finite alphabet has only `b` one-letter cyclic words,
so finite visible separation then fails for an infinite atom set. ∎

## 7. Assumption audit

- A one-way connector is not recurrent and is correctly pruned.
- A supplied private-cycle inventory satisfies the ledger but violates the
  source-visible recognition requirement.
- An infinite alphabet avoids the word-counting lemma.
- Signed, complex, matrix, exterior, or supertrace weights may cancel mixed
  trace coefficients; the literal primitive words still exist.
- Boolean existential or idempotent path semantics require a different trace.
- First return is a valid induced object, but it is not the original marker.

No claim outside these explicit assumptions is part of Theorem 2.1.

## 8. Proof verdict

The theorem is proved as stated for the frozen positive compiler class. The
unscoped statement “arithmetic recognition can never become recurrence” is
false. The contribution is the complete scoped quadrilemma, not any single
Kraft, pruning, coding, or trace-ideal lemma.
