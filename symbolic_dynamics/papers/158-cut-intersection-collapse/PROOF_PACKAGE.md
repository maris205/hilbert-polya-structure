# Proof Package — P158 cut-intersection collapse

## Claim

For repeated independent fair vertex-cut intersections of a labelled `K_n`,
the exact absorption CDF, first-hit law, almost-sure absorption, every-target
fibre, exact image criterion, and labelled image-size EGF are the formulas in
`main.tex` and the frozen Stage‑1 theorem contract.

## Status

**PROVABLE AS REPAIRED.**  The broad scout's shorthand omitted the case
`r=R,z>0`.  The theorem now retains the exact condition and the zero-valued
fibre formula at that boundary.

## Assumptions

- `n>=2`, `t>=1`, and all vertices and epochs are distinguished.
- The `tn` cut bits are mutually independent and fair.
- A nontrivial complete bipartite component has both sides nonempty.
- Isolates are order-one connected components, not degenerate bicliques.
- `A_R(m)` uses `A_0(0)=1`, `A_0(m>0)=0`, and `A_R(0)=1`.
- Enumeration is not a proof premise.

## Notation

- `c_t(v)` is the length-`t` history word at vertex `v`.
- `bar(w)` is its bitwise complement.
- `R=2^(t-1)` is the number of unordered complementary word pairs.
- `r(H)` and `z(H)` count nontrivial complete-bipartite components and
  isolates.
- `(R)_r` is a falling factorial.

## Proof strategy

Replace the sequential intersections by the bijective word representation.
Prove a labelled one-sided occupancy lemma.  Use it at the empty target for
the temporal law.  For an arbitrary target, reserve a distinct oriented pair
for each nontrivial component and count isolates on the unused pairs.

## Dependency map

1. The literal update implies the complement-history representation.
2. One complementary pair has labelled EGF `2e^x-1` under one-sided
   occupancy.
3. The empty target uses the occupancy lemma with no reserved pairs.
4. A fixed target uses uniqueness of connected bipartitions and the no-reuse
   rule for consumed pairs.
5. The image EGF follows from the proved classification, not from finite
   enumeration.

## Proof

### Step 1: complement histories

An edge `uv` survives through epoch `t` exactly when
`b_s(u) != b_s(v)` for all `s<=t`.  Binary coordinatewise inequality is
bitwise complementation, so

```text
uv in G_t  iff  c_t(u)=bar(c_t(v)).
```

The cut bits and the vertex-word assignment are the same `tn` labelled
coordinates, so no histories or probabilities are lost.

### Step 2: one-sided occupancy

For one complementary pair, an admissible inverse image is empty, a nonempty
labelled set using the first word, or a nonempty labelled set using the second
word.  The labelled EGF is

```text
1+2(e^x-1)=2e^x-1.
```

For `R` distinguished pairs, multiplication gives

```text
A_R(m)=m![x^m](2e^x-1)^R
      =sum_(j=0)^R (-1)^(R-j) C(R,j) 2^j j^m.
```

Coefficient extraction also proves all zero-size boundary values.

### Step 3: temporal theorem

The graph is empty at time `t` iff no complementary pair is occupied on both
sides.  There are `A_R(n)` successful assignments among `2^(tn)` equiprobable
histories.  Monotone edge deletion identifies `{T<=t}` with this event, so
the CDF and consecutive-difference first-hit formula follow.

For a fixed edge, the second endpoint has exactly one complementary word
among `2^t`, hence survival probability `2^(-t)`.  The union bound gives

```text
P(T>t) <= C(n,2) 2^(-t).
```

It implies almost-sure absorption.  The positive-integer tail-sum identity
then gives the exact mean series and the displayed geometric upper bound.

### Step 4: image necessity

Within one complementary pair, all edges join the two word classes, so a
two-sided occupied pair forms a connected complete bipartite component and a
one-sided occupied pair contributes only isolates.  Different pairs have no
edges between them.

Two nontrivial components cannot share a pair, since cross edges between
opposite sides would join them.  Thus `r<=R`.  When all `R` pairs are
consumed, an extra isolate has no legal word: either word joins it to the
nonempty opposite component side.  Hence `r=R` forces `z=0`.

### Step 5: sufficiency and every target fibre

A connected bipartite component has a unique bipartition up to side swap.
Assign distinct complementary pairs to the `r` labelled components in
`(R)_r` ways, and orient their two sides in `2^r` ways.  Isolates cannot use a
consumed pair.  Their assignments on the `R-r` unused pairs must be one-sided
and are counted by `A_(R-r)(z)`.

Every constructed assignment yields the prescribed graph.  Conversely, any
history assignment yielding it recovers a unique pair injection, component
orientation, and residual isolate assignment.  Thus

```text
# fibre = (R)_r 2^r A_(R-r)(z).
```

When `r=R,z>0`, this equals zero because `A_0(z)=0`.  The necessity argument
handles all graphs outside the component class.  At `n=5,t=2`, the graph of
two disjoint edges plus an isolate is exactly this zero-fibre boundary.

### Step 6: labelled image EGF

A nontrivial complete bipartite graph on an `s`-element labelled set is a
nonempty proper subset modulo complementation, so there are `2^(s-1)-1` and
the component EGF is

```text
B(x)=(e^x-1)^2/2.
```

An unordered set of `j` such components contributes `B(x)^j/j!`.  For
`j<R`, arbitrary isolates contribute `e^x`; for `j=R`, the isolate set must
be empty.  Summing these disjoint cases and extracting `n![x^n]` proves the
image formula.

## Corrections or missing assumptions

- **Corrected:** `r<=R` alone is not sufficient when isolates are present.
  The exact condition is `r<=R` and (`z=0` or `r<R`).
- No further missing assumption is known in the frozen contract.

## Open risks

- A direct owner may use antipodal-word, cut-space, separating-family, or
  bicluster terminology not retrieved by the bounded screen.
- The proof is elementary after the encoding; ownership is judged only on the
  literal process-and-fibre conjunction.
- Any compression that drops `A_0(z)` or the `n=5,t=2` example reintroduces
  the repaired statement error.
