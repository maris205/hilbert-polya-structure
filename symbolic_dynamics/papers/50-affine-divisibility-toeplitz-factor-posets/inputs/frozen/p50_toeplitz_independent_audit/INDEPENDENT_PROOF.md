# Independent proof reconstruction

## Status

**PROVABLE AS STATED.**  The only imported theorem is the standard
Curtis--Hedlund--Lyndon representation of a continuous shift-commuting map
by a finite local rule.  All divisibility and finite-graph arguments below
are reconstructed from the contract rather than from either candidate
implementation.

## 1. Nonzero affine arguments and coordinate periodicity

The equality `(p-1)k+1=0` has no integral solution because `p-1>=2` cannot
divide `1`.  Thus `nu_p` is never evaluated at zero.

Let `e=nu_p(L(k))` and write `L(k)=p^e a` with `p` not dividing `a`.  For
every integer `t`,

```text
L(k+t p^(e+1)) = p^e [a+(p-1)tp].
```

The bracket is congruent to `a` modulo `p`, so its `p`-divisibility exponent
is zero.  Hence position `k` is periodic with period `p^(e+1)`.  This uses no
field property and is valid when `p` is composite.

## 2. Exact skeleton, essential periods, and simple-Toeplitz form

Since `gcd(p-1,p)=1`,

```text
p^N divides L(k)  iff  k=r_N (mod p^N),
L(r_N)=p^N,       r_(N+1)=r_N+p^N.
```

If `k` is outside that residue, put `e=nu_p(L(k))<N` and
`L(k)=p^e a`.  Then

```text
L(k+t p^N)=p^e[a+(p-1)t p^(N-e)],
```

whose bracket remains nonzero modulo `p`.  The letter is constant on the
whole `p^N` progression.  Conversely, the progression through any member of
`r_N+p^N Z` contains both `r_N` and `r_(N+1)`.  Their letters are `u_N` and
`u_(N+1)`, which differ by cyclic-neighbor distinctness.  Therefore

```text
Per_{p^N}(x)=Z \ (r_N+p^N Z).
```

The complement of the skeleton is a single residue class.  A translation
period of this skeleton must preserve that class, hence must be divisible by
`p^N`; the skeleton consequently has least positive period `p^N`.  Thus
every `p^N` is essential.

Let `H_N=r_N+p^N Z`, with `H_0=Z`.  The layer `H_N\H_(N+1)` is filled
uniformly by `u_N`, leaving exactly the next single hole class.  No ordinary
integer lies in all `H_N`, since that would make its fixed, nonzero affine
value divisible by every power of `p`.  Coordinate periodicity shows that
these layers cover `Z`, so this is a normal one-hole simple-Toeplitz filling.
If `x` had a nonzero global period `q`, that period would preserve every
unique hole class and force `p^N|q` for every `N`, an impossibility.  Hence
`x` is aperiodic.

## 3. Constructiveness: the prime/composite split

For a position, a period means invariance on its full arithmetic
progression.  Let `B_N=x[0,p^N-1]`, and take the common period of all its
positions.

For `0<=k<p^N`,

```text
0 < L(k) < p^(N+1),
```

so `nu_p(L(k))<=N`.  Section 1 then gives `p^(N+1)` as a period of every
position in `B_N`.  This is the universal upper bound.

Now suppose `p` is prime and a positive common period `q` is not divisible
by `p^(N+1)`.  Write `q=p^j d`, where `0<=j<=N` and `p` does not divide `d`.
The coefficient `(p-1)d` is invertible modulo `p^2`, so an integer `t`
exists with

```text
1+(p-1)dt = p (mod p^2).
```

The coordinate `r_j` lies in `B_N`, including `r_0=0`, and

```text
L(r_j)=p^j,
L(r_j+tq)=p^j[1+(p-1)dt].
```

The two exponents are exactly `j` and `j+1`; the corresponding directive
letters differ.  This contradicts that `q` is a common period.  Thus the
least common period is exactly `p^(N+1)`.

There is a harmless indexing defect in the displayed finite-word definition
in the inspected Hosseini--Yassawi v3 source: it writes `i=1,...,ell` after
displaying a word starting at `x_0`.  The frozen contract explicitly uses
all positions.  Even under a literal convention omitting coordinate zero,
the prime lower bound is unchanged.  Only the case `j=0` above used zero;
replace it by `k=1`, for which `L(1)=p`, choose `s` with
`1+(p-1)q s = p (mod p^2)`, and take translation multiplier `t=ps`.
Indeed, `L(1+tq)=p[1+(p-1)qs]`, so the exponents at `1` and `1+tq` are
`1` and `2`.  Thus the
source indexing defect does not change the prime/composite conclusion.

Finally suppose `p` is composite, and let `ell` be a prime divisor of `p`.
Put `q=ell*p^N`, which is strictly below `p^(N+1)`.  For a coordinate
`0<=k<p^N`, write `e=nu_p(L(k))`.  If `e<N`, then for every integer `t`,

```text
L(k+tq)=p^e[a+(p-1)t ell p^(N-e)],
```

and the bracket is congruent to `a` modulo `p`, so the exponent stays `e`.
If `e=N`, the unique-hole congruence forces `k=r_N`, and

```text
L(k+tq)=p^N[1+(p-1)ell t].
```

The bracket is `1` modulo `ell`, hence cannot be divisible by `p`.  The
exponent again remains fixed.  Therefore `ell*p^N` is a full progression
period of every position of `B_N`, proving nonconstructiveness at every
level for every composite base.  Together with the prime argument this is
an if-and-only-if.

## 4. High centers

Let `c_n=r_n`, take `j!=0`, and write `j=p^e a` with `p` not dividing `a`.
For `n>e`,

```text
L(c_n+j)=p^n+(p-1)j
          =p^e[p^(n-e)+(p-1)a].
```

The bracket is congruent to `-a` modulo `p`, so it is not divisible by `p`.
Consequently

```text
nu_p(L(c_n+j))=nu_p(j).
```

This includes negative offsets and composite bases and uses no inverse.

## 5. Arbitrary-radius pointed factor collapse

Let `F:T_{p,u}->T_{p,v}` be continuous, onto, shift commuting, same-base,
and pointed.  By Curtis--Hedlund--Lyndon, after padding if necessary there
is a symmetric radius `R>=0` and a local rule `phi` on `[-R,R]`.  If `R>0`,
let

```text
M=max{nu_p(j):0<|j|<=R};
```

for `R=0`, take `M=-1`.  At every center `c_n` with `n>M`, Section 4 gives

```text
x(c_n)=u_n,
x(c_n+j)=u_{nu_p(j)}  for 0<|j|<=R.
```

Thus all off-center entries are independent of `n`; the window depends on
`n` only through its center letter.  Exact support and periodicity make each
source letter occur at arbitrarily high indices.  Define `lambda(a)` to be
`phi` applied to the resulting high window with center `a`.

Pointedness and `L(c_n)=p^n` give

```text
v_n = F(x)(c_n) = lambda(u_n)          (n>M).
```

Let `H` be the least common multiple of the two directive periods.  Adding
a sufficiently large multiple of `H` extends this equality to every
integer directive index.  Therefore, for every coordinate `k`,

```text
x_{p,v}(k)=v_{nu_p(L(k))}
          =lambda(u_{nu_p(L(k))})
          =lambda(x_{p,u}(k)).
```

The original map and the coordinate letter map agree on the distinguished
point, hence by shift commutation on its orbit and by continuity on its
closure.  Exact target support makes `lambda` surjective, and occurrence of
every source letter in the directive makes it unique.

Conversely, a surjective letter map with `v=lambda(u)` sends the
distinguished point to the target point.  Its compact image contains the
target orbit and is exactly the closure of that orbit, so it is onto the
target subshift.  This proves the all-finite-radius equivalence.  Applying
the same statement to an inverse shows that pointed conjugacies are exactly
bijections of directive letters.  The proof fails exactly where the
contract says it should: a wrong base destroys the shared high centers, and
a nonpointed map does not provide the displayed equality at them.

## 6. Partition classification and counts

For a source alphabet `A`, form the simple graph `G_u` with an edge between
letters that are cyclic neighbors in the directive.  The kernel of a
surjective letter map is a partition `P` of `A`.  Its quotient directive has
unequal cyclic neighbors exactly when no edge has both endpoints in one
block, namely when every block is independent in `G_u`.  Exact support is
preserved, and unequal cyclic neighbors exclude period one; reduction to
the least directive period stays in the frozen family.  Conversely, mapping
letters to the blocks of any such partition constructs the pointed factor.

Two quotient targets are pointedly conjugate exactly when their kernels are
equal: a pointed conjugacy is a bijective relabeling, which preserves the
kernel, and equal kernels differ only by such a relabeling.  A map from the
target of `P` to the target of `Q` exists exactly when the `Q`-block of a
letter depends only on its `P`-block, equivalently when `P` refines `Q`.
Exact support makes the induced map unique.  This gives a refinement poset,
not a lattice assertion.

Partitions into `k` independent blocks are precisely unlabeled proper
`k`-color-class decompositions.  Labeling their blocks injectively into
`q` colors gives `(q)_k` choices, so

```text
P_G(q)=sum_k S_G(k)(q)_k.
```

The least available `k` is `chi(G)`.  Since cyclic-neighbor distinctness
ensures that `G` has an edge, a two-letter target exists exactly when `G` is
bipartite.  These count pointed-conjugacy classes, not labeled maps.

## Boundary audit

The arguments explicitly cover `p=3`, `h=2`, radius zero, negative offsets,
composite divisibility exponents, all translates in the common-period
definition, exact support, cyclic adjacency, and the absence of a residual
integer hole.  They do not use bounded computation as a proof and do not
extend to wrong-base or nonpointed maps.
