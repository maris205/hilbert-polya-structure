# Eventual-period feedback: sharp triangular thresholds and inverse atlas

Date: 2026-09-05 UTC. **PROVISIONAL THEOREM SPIKE / OWNER_AMBER /
HOLD_EXTERNAL**. No paper number or independent-gate acceptance is implied.

The literal system and initial inverse decomposition were proposed by the
root coordinator. This independently delegated lane supplied the sharp
rank-threshold proof and recursive critical-size census. The root supplied
the strict forest comparison proving the unique maximum fibre. Static
functional-graph and rooted-forest enumeration receive zero contribution
credit throughout.

## Proof status, assumptions, and dependency map

**PROVABLE AS STATED.** This is an author-side proof status, not a selection,
owner, or independent-review verdict. The sole assumptions are an integer
$n\ge1$, the full labelled endofunction carrier, and the simultaneous update
specified below. There are no genericity, acyclicity, or permutation
assumptions on the input. No correction to the stated map is used.

The strategy is disjoint-cycle packing followed by a matching recursive
construction, with independent labelled block decomposition for inversion.

1. The recurrence classification uses the rank-packing inequality in Section 2.
2. The sharp height and all-rank claims use Sections 2 and 3 plus the explicit
   lift in Section 4.
3. The complete critical-size classification examines every equality in that
   same packing chain, then counts label allocations and cyclic orders.
4. The inverse axis uses period-invariant target blocks and the classical
   prescribed-root forest formula; it does not use the height theorem.
5. The maximal fibre uses a strict connected-component comparison and a
   cross-block forest injection, not the rank-packing estimate.

Notation is introduced before its first use in each numbered section.

## 1. Literal map and conventions

Fix `n>=1` and `X_n={f:[0,n-1]->[0,n-1]}`. For a vertex `i`, let
`ell_f(i)` be the length of the unique directed cycle reached by iterating
`f` from `i`, including length-one loops. Define

```
(P_n f)(i)=ell_f(i)-1.
```

All entries are recomputed from the old complete function. This is an
autonomous self-map of `X_n`: every cycle length lies in `[1,n]`. Its
zero state is the constant-zero function, not the identity. Labels are
fixed numerical labels and are not standardized after an epoch.

Write `r(f)=|im f|`, and let `h(f)` be the first time `P_n^t f=0`. The
proof below establishes finiteness; it is not assumed in the definition.

## 2. Rank contraction and complete recurrent classification

Let `L(f)` be the set of distinct cycle lengths occurring anywhere in the
functional graph of `f`. Then

```
r(P_n f)=|L(f)|,
r(f) >= sum_{d in L(f)} d >= r(P_n f)(r(P_n f)+1)/2.       (2.1)
```

Proof. Every cycle has a nonempty basin, so every and only the values
`d-1`, `d in L(f)`, occurs in the period-feedback vector. Select one cycle
of every different length. Its vertices lie in `im f`, selected cycles
are disjoint, and distinct positive integers sum to at least their first
`|L(f)|` possible values. This proves both inequalities.

If `r(P_n f)>=2`, (2.1) makes the rank strictly decrease. If the new rank
is one, the new function is constant, and its next period feedback is
zero because every constant function has a unique one-cycle. It follows
that every orbit reaches zero. The only recurrent and only fixed state is
zero; all eventual periods are one.

The distinction between rank and maximum value matters. The rank inequality
cannot be replaced by an unsupported scalar evolution equality.

## 3. Core-extension lemma

Suppose `g:[0,n-1]->[0,k-1]` and let `u=g|[0,k-1]`, where `1<=k<=n`.
Then for every `t>=0`,

```
(P_n^t g)|[0,k-1] = P_k^t u,
```

and, for `t>=1`,

```
P_n^t g=0  iff  P_k^t u=0.                              (3.1)
```

Consequently `h(g)=h(u)` if `h(u)>=1`; if `u=0`, the height of `g` is
zero or one according as `g=0` or not.

Proof. Every cycle of `g` is contained in the core `[0,k-1]`, and an
outside vertex enters that core in one arrow. All cycle lengths are at
most `k`, so `P_n g` again maps into the core, and its restriction is
`P_k u`. Induct this restriction identity. A period-feedback vector is
zero exactly when all cycles of its input are loops. At each epoch the
cycles of the extension are precisely the cycles of its core restriction.
This proves (3.1), including its stated `t>=1` boundary.

## 4. Sharp all-size and all-rank height theorem

Define the strictly increasing threshold sequence

```
N_2=2,
N_(h+1)=N_h(N_h+1)/2  (h>=2).
```

Thus

```
N_2,N_3,N_4,N_5,N_6,N_7 = 2,3,6,21,231,26796.
```

This numerical sequence and its triangular recurrence are established
combinatorial background, explicitly appearing in Stephan Wagner's
[*Enumeration of highly balanced trees*](https://math.sun.ac.za/swagner/balanced.pdf),
Section 4. No claim is made to discovering the sequence. The theorem here is
its exact interpretation as the minimum rank needed for a specified height
of this particular labelled period-feedback map.

For every `h>=2`,

```
h(f)>=h  implies  r(f)>=N_h.                            (4.1)
```

Every such threshold is attained by a permutation on `N_h` labels.
Therefore the sharp maximum height is

```
H(1)=0,
H(n)=max{h>=2:N_h<=n}  (n>=2).                          (4.2)
```

More generally, for every `2<=r<=n`, the largest height among rank-`r`
functions on `n` labels is `max{h>=2:N_h<=r}`. At rank one, the only
heights are zero and one, with the latter available iff `n>=2`.

Proof of the lower rank bound. Rank-one functions are constant, so have
height at most one. This proves (4.1) at `h=2`. If `h(f)>=h+1`, then
`h(P_n f)>=h`. By induction `r(P_n f)>=N_h`, and (2.1) gives
`r(f)>=N_h(N_h+1)/2=N_(h+1)`.

Sharp construction. Start with the transposition `f_2=(1,0)` on two
labels; its successive period vectors are `(1,1)` and `(0,0)`, so its
height is two. Suppose a height-`h` permutation `f_h` on `k=N_h` labels
has been constructed. For each `j=0,...,k-1`, form a block `B_j` containing
the unique old label `i` with `f_h(i)=j`, together with exactly `j` fresh
labels. The blocks partition `N_(h+1)=k(k+1)/2` labels. Choose a cyclic
permutation of each `B_j` and let their disjoint union be `f_(h+1)`.
Then `P f_(h+1)` maps every `B_j` to `j`, so it is a core extension of
`f_h` on the old labels. By Section 3 its height is `h`; hence the new
permutation has height `h+1`.

For arbitrary `r` between thresholds, extend the construction on `N_h`
labels to a permutation on `r` labels by fixing all added labels. Its
first period-feedback vector restricts to `P f_h` on the first `N_h`
labels and is zero outside, hence has height `h-1` by the same lemma.
The enlarged permutation has height `h`. Extend it to `n>=r` by mapping
all additional vertices to zero. This preserves its height and gives rank
exactly `r`. Equation (4.2) and the all-rank refinement follow.

## 5. Complete critical-size extremizers and exact census

At `n=N_h`, `h>=2`, every height-`h` function is a permutation. For
`h>=3`, put `k=N_(h-1)`. The complete equality criterion is:

1. `f` has exactly one cycle of each length `1,2,...,k`, with no other
   cycles; and
2. `u=(P f)|[0,k-1]` is a height-`(h-1)` permutation of `[0,k-1]`.

The construction in Section 4 generates exactly these extremizers. Let
`D_h` be their number. Then

```
D_2=1,
D_h=D_(h-1) (N_h-N_(h-1))!  (h>=3).                    (5.1)
```

In particular `D_3=1`, `D_4=6`, and `D_5=6*15!`.

Proof. At the critical size, (4.1) forces full rank, hence a permutation.
Every inequality in

```
N_h = r(f) >= sum_{d in L(f)}d
    >= T(r(P f)) >= T(N_(h-1)) = N_h
```

is an equality. Thus the distinct cycle lengths are precisely `1,...,k`,
each occurs once, and `im(P f)=[0,k-1]`. By the core-extension lemma, its
restriction `u` has height `h-1`. The rank bound on its `k`-point carrier
forces it to be a permutation. These arguments also give sufficiency.

For a fixed eligible `u`, block `B_j` contains its prescribed old label
`u^{-1}(j)` and `j` new labels. Allocate the new labels in
`(N_h-k)!/prod_{j=0}^{k-1}j!` ways. The cyclic order on `B_j` has `j!`
choices. The factors cancel, leaving `(N_h-k)!` choices per `u`, proving
(5.1). This classifies the equality case, rather than merely constructing
some deepest states.

## 6. Every target fibre and first image

For `d>=1`, let `a_d(k)` count functions on a prescribed `k`-element set
all of whose cycles have length exactly `d`. Put `a_d(0)=1`. For `k>0`,

```
a_d(k) = sum_{c=1}^{floor(k/d)}
   [ k! / ((k-dc)! d^c c!) ] R(k,dc),

R(k,m)=1                    if m=k,
R(k,m)=m k^(k-m-1)          if 1<=m<k.
```

Here `R(k,m)` is the classical labelled-forest count with a prescribed
root set. Equivalently, for the labelled rooted-tree EGF `T(z)`,

```
sum_{k>=0}a_d(k) z^k/k! = exp(T(z)^d/d).
```

For a target `g`, put `B_j=g^{-1}(j)` and `k_j=|B_j|`. Then

```
|P_n^{-1}(g)| = product_{j=0}^{n-1} a_(j+1)(k_j).        (6.1)
```

Thus `g` is in the first image iff every nonempty `B_j` has size at
least `j+1`. Its image count is explicitly

```
|im P_n| = sum_{sum k_j=n; each k_j=0 or k_j>=j+1}
                         n! / product_j k_j!.
```

Proof. If `P f=g`, an arrow of `f` connects vertices of the same eventual
period. Thus each `B_j` is `f`-invariant and all cycles in that block have
length `j+1`. Conversely these conditions force `P f=g`. The labelled
restrictions are independent, proving (6.1). To count `a_d(k)`, choose the
`dc` cyclic vertices, put a permutation with `c` disjoint `d`-cycles on
them, and attach a forest rooted at those vertices. The feasibility and
image count follow. This is classical decomposition applied targetwise.

## 7. Unique maximal fibre

For every `n>=1`, the maximum fibre is

```
(n+1)^(n-1),
```

and its unique target is the all-zero function.

Proof. Let `c_d(k)` count connected functions on `k` labels with their
single cycle of length `d`. For `k>=d`, the standard cycle-and-tree
decomposition gives

```
c_d(k) = (k)_d k^(k-d-1),
c_1(k) = k^(k-1),
```

where the first expression at `k=d` means `(d-1)!`. Their ratio is
`(k)_d/k^d<=1`, strictly less than one for `d>=2`. Therefore the connected
EGF for `d`-cycles is coefficientwise bounded by `T(z)`, and its SET
exponential is bounded by `exp(T(z))`. The inequality in coefficient
`z^k` is strict whenever `k>=d>=2`, because the connected coefficient is
already strict. Hence

```
a_d(k)<=a_1(k)=(k+1)^(k-1),
```

strict for nonempty admissible blocks with `d>=2`. A product of rooted-
forest counts on two or more prescribed nonempty blocks is strictly less
than the count of all rooted forests on their union: disjoint union embeds
it, while a forest containing an edge between blocks is outside the image.
Apply these two strict comparisons to (6.1). The sole equality target has
one block and `d=1`, namely `g=0`. Its fibre is the standard rooted-forest
class, counted by adjoining a super-root and applying Cayley's formula.

## 8. Residual claim boundary

No credit is assigned to cycle finding, the functional-graph decomposition,
the rooted-forest formula, the SET/CYC EGF, or the zero-target count alone.
The primary temporal residual is the iterated triangular minimum-rank
hierarchy and its attained all-size maximum. The critical-size recursive
equality classification and factorial census are a second, sharper temporal
enumeration. The labelled block-product inverse, precise image condition,
and strict unique maximum complete the atlas.

The update writes a familiar statistic back as a function, which requires
an explicit hostile gate. It is not a mere histogram iteration: the image
states `(0,1,1)` and `(1,0,1)` have identical value multiplicities, but
their next outputs are respectively `(0,0,0)` and `(1,1,1)`. Their heights
are one and two. Label placement affects the next cycle decomposition.
This example only disproves histogram-factorization. It does **not** defeat
or authorize an exception to the separate `word_poset_lane` intake rule
against canonical statistics written back as states. That original rule is
preserved unchanged. Its lane scope, the central problem-anchor threshold,
and the remaining generic-statistic concern are recorded explicitly in
`SOURCE_OWNER_AND_COLLISION.md` for an independent selection decision.

No count or bounded search non-hit establishes novelty or priority. See that
source memo for the classical-input subtraction and verified-source scope.

## Open risks

The complete deductive claims above survived the author checks, including
all functions through seven labels and critical witnesses through 26796
labels. These bounded computations are not proofs. Independent review may
reject the candidate as owner-thin or as below the central two-axis threshold
even if every theorem remains correct. The known triangular sequence,
functional-graph decomposition, rooted-forest counts, and SET/CYC machinery
must stay attributed background. External status remains `HOLD_EXTERNAL`.
