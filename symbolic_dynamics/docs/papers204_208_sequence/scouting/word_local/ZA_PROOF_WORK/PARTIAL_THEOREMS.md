# ZA partial theorems — exact scope and proof status

Let `X_n={x: x_0=0, 0<=x_i<=n−i for 1<=i<n}`, and set `F(x)_0=0`,
`F(x)_i=LCP(x,x[i:])`. All results below are elementary and provable as
stated. None implies the requested complete recurrence/clock theorem.

## 1. Mask sectors and recurrent lower bound

Closure follows from the maximum suffix length `n−i`. The first compared
letter is `x_0=0`, hence for every `i>=1`,

```text
F(x)_i=0  iff  x_i>0.
```

If `S(x)={i>=1:x_i=0}`, then `S(Fx)=[1,n−1]\S(x)`. Thus for `n>=2` there
are no fixed points and every recurrent period is even. The unions of the
two mask classes `S,S^c` are invariant and form `2^(n−2)` disjoint nonempty
sectors. Each finite nonempty invariant sector contains a cycle. Therefore
there are at least `2^(n−2)` cycles and at least `2^(n−1)` recurrent states.
Equality in either bound is unproved for general `n`.

The class with zero set `S` has exactly

```text
w(S)=product_(i notin S)(n−i)
```

states, because every nonzero coordinate has `n−i` choices. A complementary
sector has `w(S)+w(S^c)` states. This is an invariant-sector census, not a
basin theorem. It becomes a basin size only **conditionally** on exactly one
cycle occupying that sector; this hypothesis is not established here.
For `n=1` the sole state `(0)` is fixed.

## 2. The one-step image is the complete set of realizable Z arrays

The forward inclusion is definitional. Conversely, take any finite word `u`
and distinguish the equality class containing `u_0`. Rename that class 0.
Order all other equality classes by decreasing location of their last
occurrence, and name them `1,2,...`. A class whose last occurrence is `l`
receives label at most `n−l`: there are at most `n−1−l` classes ending later.
Every occurrence at index `i<=l` then has label at most `n−l<=n−i`.
The renamed word belongs to `X_n` and preserves every equality comparison,
so it has the same Z array. This proves surjectivity onto all realizable
arrays, independently of the finite enumeration.

Ordinary restricted-growth words also represent every equality pattern,
although they do not necessarily lie in `X_n`; the right-to-left recoding
just given repairs the carrier issue. This justifies enumerating complete
valid images through restricted-growth realizers. It is not a claim that
arbitrary binary realizers suffice: their output collection has only one
member per zero mask.

## 3. Exact factorial fibre extremum; two maximizing targets

For a prescribed target `t`, `t_i>0` forces `x_i=0`, while `t_i=0` forces
`x_i` into `{1,...,n−i}`. Consequently

```text
|F^(-1)(t)| <= product_(i:t_i=0)(n−i) <= (n−1)!.
```

For `n>=2`, equality requires `t_i=0` at every `1<=i<=n−2`, since omitting
any corresponding factor omits an integer at least two. The final target
coordinate can only be zero or one. Both possibilities attain equality:
choose all source coordinates `1,...,n−2` independently nonzero, then choose
the last source coordinate 1 for target `0^n` or 0 for target `0^(n−1)1`.
All earlier LCP values are immediately zero, and the last is as required.
These are exactly the two maximizers. At `n=1` there is one target and fibre
size one. This proof is a static forced-letter product, identical in type
to P134's extremal argument, and receives no separation credit.

## 4. Every-target equality-constraint formulation (zero-credit apparatus)

For target `t`, impose equalities `x_j=x_(i+j)` for `0<=j<t_i`, and, if
`i+t_i<n`, the inequality `x_(t_i)!=x_(i+t_i)`. These constraints are exactly
the LCP specification. Collapse equality classes. A class containing index
0 has allowed set `{0}`; any other class `C` has the nested allowed interval
`{0,...,n−max C}`. A target with an inequality inside one class has no parent.
Otherwise its parents are exactly proper list colourings of the graph whose
edges are those inequalities, with the displayed allowed sets.

Equivalently, inclusion–exclusion over inequality edges counts the fibre:
for each edge subset, contract its components, multiply the cardinalities
of the intersections of their allowed sets, and use sign `(−1)^(#edges)`.
This is exact for every target but is generic constraint enumeration, not
a new efficient inverse formula. It is not promoted as an independent
paper-scale theorem and was not used as a substitute for convergence.

## 5. A necessary condition on a hypothetical two-cycle

Suppose `y=F(x)` and `x=F(y)` with `n>=2`. At each positive index exactly
one of `x_i,y_i` is positive; call that value `a_i`, and call its location
the colour of `i`. If indices `i,j` have opposite colours and `i+j<n`, then

```text
not (a_i>j and a_j>i).
```

Indeed, assume `x_i=a_i>0` and `y_j=a_j>0`. If `a_i>j`, the prefix match in
`x_i=F(y)_i` forces `y_(i+j)=y_j>0`. If also `a_j>i`, the prefix match in
`y_j=F(x)_j` forces `x_(i+j)=x_i>0`, contradicting complementary zero masks.
This condition does not show that every trajectory enters a two-cycle or
that one pair is uniquely selected by its mask. It is only a possible
constraint for a future non-prefix-based approach.

## Unresolved assertions

No proof is supplied for eventual period at most two, uniqueness per mask,
a useful uniform clock, an exact all-size recurrent decoder, or a genuinely
new full inverse/basin axis beyond static LCP constraints. Failed strict
and weak prefix-contraction lemmas are recorded in the companion report.
