# Proof package

## Status and dependency graph

**Proof status: PROVABLE AS STATED.**

The proof is self-contained apart from the Curtis--Hedlund--Lyndon theorem
for maps between subshifts.  Its dependency graph is

```text
affine divisibility identity
  -> exact skeleton -> essential periods -> Toeplitz/aperiodicity
  -> prime/composite common-period analysis -> constructive iff prime

high-center identity + Curtis--Hedlund--Lyndon
  -> directive letter map
  -> equality on the distinguished orbit
  -> equality on its closure
  -> unique surjective 1-block quotient
  -> conjugacy and admissible-partition classification
  -> graphical Stirling/chromatic corollaries.
```

Finite computations in `evidence/canonical_evidence.json` are falsification
checks only.  In particular, the bounded local-rule search is not used in
the proof of the all-radius factor theorem.

## Assumptions and notation

Use exactly the objects in `THEOREM_CONTRACT.md`.  Thus `p>=3` is an integer,

```text
nu_p(m)=max{e>=0:p^e divides m},       m!=0,
L(k)=(p-1)k+1,
x(k)=u_{nu_p(L(k))},
r_N=(p^N-1)/(p-1).
```

For composite `p`, `nu_p` is only a divisibility exponent.  A statement
`p` does not divide `a` below does not assert that `a` is invertible modulo
`p`.  Invertibility is used only in the explicitly prime lane.

The directive `u` has exact finite support, least period `h>=2`, and
`u_n!=u_{n+1}` for all `n`.  Put `r_0=0`.  Then

```text
L(r_N)=p^N,                 r_{N+1}=r_N+p^N.
```

## Lemma 1: coordinate periodicity

Every coordinate `k` of `x` is periodic.  More precisely, if
`e=nu_p(L(k))`, then `p^(e+1)` is a period of the position `k`.

### Proof

Write `L(k)=p^e a` with `p` not dividing `a`.  For every `t in Z`,

```text
L(k+t p^(e+1))
 = p^e [a+(p-1)t p].
```

The bracket is congruent to `a` modulo `p`, hence is not divisible by `p`.
Its divisibility exponent is therefore zero, so the whole expression has
divisibility exponent `e`.  This congruence argument remains valid for
composite `p`.  ∎

## Lemma 2: exact skeleton and unique hole

For every `N>=1`,

```text
Per_{p^N}(x)=Z \ (r_N+p^N Z).
```

### Proof

Because `p-1` is coprime to `p`, it is invertible modulo `p^N`.  Directly,

```text
p^N divides L(k)  iff  k=r_N (mod p^N).
```

If `k` is outside this residue class, let `e=nu_p(L(k))<N` and write
`L(k)=p^e a`, with `p` not dividing `a`.  For all `t in Z`,

```text
L(k+t p^N)=p^e[a+(p-1)t p^(N-e)].
```

The bracket is congruent to `a` modulo `p`; hence the exponent, and
therefore the letter, is unchanged along the whole `p^N` progression.

Now take any `k` in the alleged hole class.  Both `r_N` and
`r_{N+1}=r_N+p^N` lie in its `p^N` progression.  Their letters are
respectively `u_N` and `u_{N+1}`, which differ.  Consequently no coordinate
in this residue class is `p^N`-periodic.  This proves both inclusions and
also checks the indexing: stage `N` has hole `r_N`, while the next center is
obtained by adding exactly one `p^N`.  ∎

## Proposition 3: essential periods, simple-Toeplitz form, and aperiodicity

The sequence `x` is an aperiodic normal simple Toeplitz sequence, and every
`p^N` is essential.

### Proof

The `p^N`-skeleton has one hole residue modulo `p^N`.  If that skeleton had
a positive period `q<p^N`, translation by `q` would preserve its hole set,
forcing `q=0 (mod p^N)`, a contradiction.  Thus `p^N` is essential.  The
periods divide successively, and Lemma 1 shows that their periodic parts
cover `Z`, so `(p^N)_{N>=1}` is a period structure.

There is also a literal one-hole filling description.  Let

```text
H_N={k:p^N divides L(k)}=r_N+p^N Z.
```

At stage `N`, fill `H_N\H_{N+1}` uniformly with `u_N` and retain the one
residue class `H_{N+1}` as holes.  This is the standard simple-Toeplitz
recursion.  Its nested holes contain no ordinary integer: an integer in all
`H_N` would make the fixed nonzero integer `L(k)` divisible by every power
of `p`.  Hence there is no residual unfilled coordinate, which is the normal
case, and the recursion gives exactly `x`.

Finally, suppose that `x` had a nonzero global period `q`.  Translation by
`q` would preserve every exact `p^N`-skeleton and hence its unique hole
residue.  Thus `p^N` would divide `q` for every `N`, which is impossible for
nonzero `q`.  Therefore `x` is aperiodic.  ∎

## Proposition 4: constructiveness holds exactly for prime bases

Let

```text
B_N=x[0,p^N-1],                         N>=1.
```

In the Hosseini--Yassawi definition, the essential period of `B_N` is the
least common period of its positions.  It equals `p^(N+1)` for every `N`
if `p` is prime.  If `p` is composite, it is strictly smaller than
`p^(N+1)` for every `N`.

### Common upper bound

For `0<=k<p^N`, the positive number `L(k)` is strictly less than
`p^(N+1)`.  Hence `e=nu_p(L(k))<=N`.  The calculation in Lemma 1 shows that
`p^(N+1)` is a period of every such position.  Thus it is a common period of
`B_N` for every integer base `p>=3`.

### Prime lower bound

Assume now that `p` is prime, and let `q>0` be any common period of `B_N`.
If `p^(N+1)` does not divide `q`, write

```text
q=p^j d,        0<=j<=N,        p does not divide d.
```

Here primality makes `(p-1)d` invertible modulo `p^2`.  Choose `t in Z`
satisfying

```text
1+(p-1)d t = p                   (mod p^2).
```

The center `r_j` belongs to `[0,p^N-1]`, including `r_0=0`.  Moreover,

```text
L(r_j)=p^j,
L(r_j+tq)=p^j[1+(p-1)d t].
```

The two exponents are `j` and `j+1`, so the corresponding letters are
`u_j` and `u_{j+1}`, which differ.  This contradicts that `q` is a period of
the position `r_j`.  Therefore every common period is divisible by
`p^(N+1)`, and the common upper bound proves that the essential period of
`B_N` is exactly `p^(N+1)`.

### Composite counterperiod, for every translate

Assume that `p` is composite and let `ell` be any prime divisor of `p`.
Set

```text
q=ell p^N < p^(N+1).
```

Fix `0<=k<p^N`, put `e=nu_p(L(k))`, and let `t` be an arbitrary integer.
If `e<N`, write `L(k)=p^e a`, where `p` does not divide `a`.  Then

```text
L(k+tq)=p^e[a+(p-1)t ell p^(N-e)].
```

The second term in the bracket is divisible by `p`; the bracket is therefore
congruent to `a` modulo `p`, and the exponent remains `e` for **every**
`t in Z`.

If `e=N`, the unique-hole congruence and `0<=k<p^N` force `k=r_N`, so

```text
L(k+tq)=p^N[1+(p-1)ell t].
```

The bracket is `1` modulo `ell`.  Since `ell` divides `p`, the bracket cannot
be divisible by `p`; the exponent remains `N` for every `t`.  Hence `q` is a
common period of every position of `B_N`.  It is strictly smaller than the
next power because a prime divisor of a composite `p` satisfies `ell<p`.
This disproves constructiveness at every level and completes the `if and
only if`.  ∎

## Lemma 5: high-center identity

For `c_n=r_n`, every nonzero `j in Z`, and every `n>nu_p(j)`,

```text
nu_p(L(c_n+j))=nu_p(j).
```

### Proof

Let `e=nu_p(j)` and write `j=p^e a`, where `p` does not divide `a`.  Since
`L(c_n)=p^n`,

```text
L(c_n+j)=p^n+(p-1)j
          =p^e[p^(n-e)+(p-1)a].
```

Because `n-e>=1`, the bracket is congruent to `(p-1)a`, and hence to `-a`,
modulo `p`.  It is not divisible by `p`.  Therefore the exponent is exactly
`e`.  Notice that the proof did not invert `a` and is valid for composite
`p`.  ∎

## Theorem 6: every same-base pointed factor is the unique 1-block quotient

Let `F:T_{p,u}->T_{p,v}` be a pointed factor map within the frozen family.
There is a unique surjective letter map `lambda` satisfying
`v_n=lambda(u_n)` for every `n`, and `F=lambda^Z` on all of `X_{p,u}`.
Conversely, every such letter map defines the pointed factor.

### Proof

By Curtis--Hedlund--Lyndon, there are `R>=0` and a local rule `phi` such that

```text
F(z)(k)=phi(z[k-R,k+R]).
```

If `R>0`, let

```text
M=max{nu_p(j):0<|j|<=R};
```

if `R=0`, put `M=-1`.  For every `n>M`, Lemma 5 gives the complete window
around the high center `c_n`:

```text
x(c_n)=u_n,
x(c_n+j)=u_{nu_p(j)}                (0<|j|<=R).
```

All off-center entries are independent of `n`; the whole window depends on
`n` only through its center letter `u_n`.  Since every source letter occurs
infinitely often in the periodic exact-support directive, define

```text
lambda(a)=phi(W_a),
```

where `W_a` is this fixed window with center `a`.  Pointedness gives

```text
v_n=x_{p,v}(c_n)=F(x_{p,u})(c_n)=lambda(u_n)       (n>M).
```

Let `h_u,h_v` be the directive periods and `H=lcm(h_u,h_v)`.  For arbitrary
`n`, choose a sufficiently large multiple `sH` with `n+sH>M`.  Periodicity
then yields

```text
v_n=v_{n+sH}=lambda(u_{n+sH})=lambda(u_n).
```

Thus the relation holds for every directive index.  It follows at every
coordinate `k` of the distinguished point that

```text
x_{p,v}(k)
 =v_{nu_p(L(k))}
 =lambda(u_{nu_p(L(k))})
 =lambda(x_{p,u}(k)).
```

So `F` and the coordinate map `lambda^Z` agree on `x_{p,u}`.  Shift
commutation makes them agree on its entire orbit, and continuity makes them
agree on the orbit closure `X_{p,u}`.  This is the required all-radius
collapse; no finite enumeration is used.

Every target letter appears as some `v_n` because the target directive has
exact support, so `v_n=lambda(u_n)` makes `lambda` surjective.  The same
relation also determines `lambda(a)` from any index with `u_n=a`, proving
uniqueness.

Conversely, if a surjective `lambda` satisfies `v=lambda(u)`, its coordinate
map is continuous and shift commuting, sends the distinguished point to the
target point, and has image

```text
lambda^Z(X_{p,u})
 =closure(orbit(lambda^Z(x_{p,u})))
 =closure(orbit(x_{p,v}))
 =X_{p,v}.
```

It is therefore the pointed factor map.  ∎

## Corollary 7: pointed conjugacy

A pointed factor in Theorem 6 is a conjugacy exactly when `lambda` is
bijective.

### Proof

A bijective letter map has the inverse coordinate map.  Conversely, a
pointed conjugacy has a pointed inverse at the same base.  Applying Theorem
6 to both directions gives letter maps whose coordinatewise compositions
are the identity, so both maps are bijections.  ∎

## Theorem 8: admissible partitions and the refinement poset

Fix a source directive `u` with alphabet `A`, and form the cyclic adjacency
graph `G_u`.  Kernels of same-base pointed factors are exactly the partitions
of `A` whose blocks are independent in `G_u`.

### Proof

The kernel of a surjective letter map `lambda:A->B` is a set partition `P`.
Its image directive has unequal cyclic neighbors exactly when

```text
lambda(u_i)!=lambda(u_{i+1})        for every i,
```

which is equivalent to no edge of `G_u` having both endpoints in one block.
Thus every block is independent.  Exact source support makes every block
appear in the quotient directive.  Cyclic-neighbor inequality rules out
period one, and reduction to the least period keeps the quotient inside the
frozen family.

Conversely, sending each source letter to its block for any independent-set
partition produces a surjective letter map and a valid quotient directive,
so Theorem 6 supplies the factor.

Two such quotient targets are pointedly conjugate only if their partitions
are equal.  Indeed, Corollary 7 gives a bijection between their block
alphabets, and equality of the two directive images at every index implies
that two source letters share a block in the first partition exactly when
they share one in the second.  Hence admissible partitions parametrize the
pointed-conjugacy classes injectively as well as surjectively.

For admissible partitions `P,Q`, a factor from the `P` quotient to the `Q`
quotient exists exactly when the `Q` block of a source letter is determined
by its `P` block, which is exactly `P` refining `Q`.  Exact support makes
that induced block map unique.  Actual relabeled quotient objects therefore
form a thin category and hence a preorder; quotienting by pointed conjugacy
gives precisely the refinement poset.  ∎

## Corollary 9: graphical Stirling and chromatic consequences

Let `S_{G_u}(k)` count partitions of `V(G_u)` into `k` nonempty independent
sets.  It counts the `k`-letter pointed factor targets modulo pointed
conjugacy by Theorem 8.  The smallest `k` with positive count is exactly the
chromatic number.  Since the directive has adjacent unequal letters,
`G_u` has an edge and `chi(G_u)>=2`; hence a binary target exists exactly
when `G_u` is bipartite.

Finally, a proper coloring by `q` labeled colors first chooses its partition
into `k` nonempty color classes and then injectively assigns `k` labels to
those classes.  There are `(q)_k` assignments, proving

```text
P_{G_u}(q)=sum_k S_{G_u}(k)(q)_k.
```

All counts are for one fixed source and targets modulo pointed conjugacy;
they do not count different label names or nonpointed maps.  ∎

## Sanity checks and edge cases

1. **Off-by-one:** `r_0=0`, `r_1=1`, and
   `r_{N+1}=r_N+p^N`.  The two witnesses in the stage-`N` hole have
   exponents exactly `N` and `N+1`.
2. **Composite base:** for `p=4`, `2*4^N` is a common period of `B_N`, while
   the exact essential skeleton still has period `4^N`.  This separates two
   notions that must not be conflated.
3. **Radius zero:** the high-center proof takes `M=-1` and remains valid.
4. **Negative offsets:** Lemma 5 uses integer divisibility and works without
   a sign restriction on `j`.
5. **Repeated directive phases:** for `u=(0,1,0,2)`, merging `1` and `2` is
   admissible; the quotient word `(0,1,0,1)` is reduced to least period two.
   This is why quotient directives are normalized after taking the image.
6. **Adjacent merge:** merging `0` and `1` in `(0,1,2)` creates equal cyclic
   neighbors and leaves the frozen target class.
7. **No all-`p` constructiveness claim:** all `p>=3` share the skeleton and
   rigidity proof; only prime `p` use modular inverses in Proposition 4.

## Alternative owner-level route and why it is not the proof used here

Downarowicz--Kwiatkowski--Lacroix give an over-zero factor criterion via a
map between aligned level symbols.  One could combine that theorem with the
one-hole geometry and then prove that its level-symbol map is induced by a
letter map.  The direct high-center/CHL proof above is shorter, exposes every
quantifier, covers arbitrary finite block radius at once, and does not rely
on translating notation between period structures.  The earlier theorem
remains the closest general owner and is credited in `SOURCE_LOCK.md`.

## Remaining obligations

There is no deferred lemma in this package.  Remaining work is an
independent audit of the written proof, source boundary, and deterministic
evidence.  Cross-base and nonpointed questions are intentionally unresolved
because they are outside the theorem contract.
