# LZK: exact componentwise reduction to binary erasure

Date: 2026-09-05 UTC. Independent Stage-1 gate, not manuscript Review A or B.
Verdict: **KILL_COMPONENTWISE_P100_HF1_ERASURE / HOLD_EXTERNAL**.
The author formulas are correct; their claimed independent mechanism is
already present in the binary erasure and Boolean-deletion archive.

## 1. Literal rule and invariant skeleton

Fix the labelled complete bipartite graph with sides
`L={0,...,r-1}` and `R={r,...,r+s-1}`, where `r,s>=1`, and a palette
`{0,...,q-1}`, `q>=2`. A proper colouring is a state. If colour 0 is absent,
hold. Otherwise interchange 0 and 1 on the connected bichromatic component
containing the least-labelled zero. This is exactly the frozen LZK rule.

Define `U(x)={v:x(v) in {0,1}}` and record all colours at vertices outside
`U`. The pair `sigma=(U,x|_(V\U))` is invariant. Its fibre consists of all
proper extensions of those frozen colours using only 0 and 1 on `U`.
No trajectory enters or leaves a skeleton fibre. Three exhaustive cases
give the **entire** functional graph, without any discarded transient data.

1. `U` is empty: its skeleton fibre is one fixed point.
2. `U` is nonempty and contained in one side: every binary assignment on
   `U` is proper. There are no edges inside `U`, so every Kempe component
   is a singleton. If `U={u_0<...<u_(m-1)}`, put
   `b(x)=sum_j 2^j 1{x(u_j)=0}`. This is a bijection from the skeleton
   fibre onto `{0,...,2^m-1}`, and

   ```text
   b(Fx)=b(x) & (b(x)-1).
   ```

   Thus this whole invariant component is conjugate to P100's binary
   least-valuation erasure `E_(2,m)`. The zero binary state is the colouring
   with all vertices of `U` coloured 1.
3. `U` meets both sides: its induced graph is a connected complete
   bipartite graph. Properness permits precisely two binary assignments,
   the two orientations of 0 and 1 across the sides. The selected component
   is all of `U` and the map exchanges these two states.

Consequently LZK is a disjoint union of binary erasure systems, isolated
fixed points (rank-zero erasure systems), and isolated two-cycles. This is
an exact decomposition, not merely a factor, asymptotic model, or statement
that all finite systems admit functional graphs. The coordinates are
explicit, invariant, and determined before following any orbit.

## 2. All-time inverse atlas transfers exactly

For delete-min on subsets of an ordered `m`-element set, a nonempty target
`Z` has `binom(a,t)` sources at time `t`, where `a` is the number of available
elements strictly below `min Z`. The only possible sources adjoin exactly
`t` such elements; deleting them in order reaches `Z` at exactly epoch `t`.
For the empty target, all sources of size at most `t` are admissible, giving
`sum_(j=0)^min(t,m) binom(m,j)`.

Under the skeleton coordinates, available elements below `min Z` are
exactly the author's `a(y)` earlier one-vertices. For a zero-free target,
`m=|Z_1(y)|`. Every crossing-skeleton target has one parity-determined
source. These are all three author fibre formulas, including exact source
sets rather than just their cardinalities, for every `t>=0`.

The older HF1 scout at
`docs/papers132_136_sequence/replacement_scout/combinatorial/SCOUT.md`,
Section 5.1, already explicitly contains the delete-maximum formulas

```text
p_t(empty)=sum_(j=0)^t binom(n,j),
p_t(B)=binom(n-1-max(B),t),   B nonempty,
```

with out-of-range terms zero. Reversing the order of the ground set gives
the LZK formulas above. HF1's full hypergraph map is a powerset lift; we are
**not** claiming LZK equals that lifted map. Its underlying element map and
entire element fibre atlas are the exact collision. Section 6 of the same
scout already links the HF1/SC1 erasure engine to P100.

For one step the rank-`m` erasure block has maximum fibre `m+1`, uniquely at
its empty-subset target. Nonempty targets have at most `m-1` predecessors.
The crossing blocks have fibre 1. Therefore the global maximum is
`max(r,s)+1`, with exactly the author's largest-side-all-ones equality class.
No new inverse engine remains after this transfer.

## 3. Exact assembly coefficients explain the census

Let `chi_(a,b)(k)` count proper `k`-colourings of `K_(a,b)`, now allowing
empty sides. Use `chi_(0,b)(k)=k^b`, including `0^0=1`. For `k=q-2`, the
number `B_m` of rank-`m` erasure blocks is

```text
B_0 = chi_(r,s)(k),
B_m = binom(r,m) chi_(r-m,s)(k)
    + binom(s,m) chi_(r,s-m)(k),                  m>=1,
```

where a summand is zero when its chosen side is smaller than `m`. Choose
the `m` active vertices on one side, then colour the remaining bipartite
graph using colours at least 2. The rank-zero case is written separately
to avoid double counting the empty active set.

The number `C` of strict two-cycles is

```text
C = sum_(a=1)^r sum_(b=1)^s
      binom(r,a) binom(s,b) chi_(r-a,s-b)(k).
```

This chooses the active vertices on each side, colours the complement,
and assigns one two-cycle to the two extensions. Thus the full depth
polynomial, including recurrent points at degree zero, is

```text
H(z) = 2C + sum_(m>=0) B_m (1+z)^m.
```

In particular `fixed=sum B_m`, `recurrent=2C+sum B_m`, and
`image=2C+B_0+sum_(m>=1) B_m 2^(m-1)`. Expanding the standard chromatic
counts by exact colour supports yields the author's onto/multinomial
formulas. This is independent confirmation of their correctness and also
shows why the census adds no separate dynamical mechanism: it counts copies
of the already identified components.

For `q>=3`, a largest side can be active and the other side can use colour
2, proving sharp tail `max(r,s)`. For `q=2`, only the crossing skeleton
`U=V` exists, so the system consists of precisely one two-cycle and has
tail zero. Both equal-size and unequal-size maximum-fibre equality counts
follow by assigning arbitrary colours in `{2,...,q-1}` on the opposite side.

## 4. Collision decision

The author's memo subtracts generic least-label scheduling but omits this
stronger exact P100/HF1 decomposition. P118's synchronous multipartite mex
map is not the literal owner, nor is the randomized KCI/WSK chain. Those
comparisons do not cure the missing binary-erasure subtraction.

P100's `main.tex`, Sections 1--3, gives the binary identity and the complete
digit-sum clock/profile. It explicitly credits binary erasure to Wegner.
HF1 supplies the same inverse atlas under order reversal. The remaining
assembly uses the chromatic/onto bookkeeping that the candidate contract
itself declares zero credit, together with isolated two-cycles. Under the
current problem anchor's exclusion of conjugates, occupied mechanisms, and
axes that collapse to one formula, this candidate does not merit a paper
slot. Correct equations are retained as a negative-control lemma bank.

This is a componentwise mechanism kill; it is not a claim that the complete
LZK carrier is globally conjugate to a single P100 system, or that the KMJ
paper previously stated the literal LZK scheduler. It is also not an
external novelty or priority determination.

## 5. Independent bounded check

`verify_lzk_gate.py` uses edge-based union-find for the literal Kempe
component, disjoint palette enumeration, exact invariant-skeleton grouping,
binary coordinates, direct functional-graph walks, and direct inverse sets.
It imports no author or historical implementation. Onto counts use a
recurrence rather than the author's inclusion--exclusion implementation.

All 20 boxes in `CANONICAL.txt` pass 459,463 assertions. They include
`q=2`, singleton sides, both label orientations, equal side sizes,
`(r,s,q)=(5,5,3)` and `(4,4,5)`. Every-time fibres are tested through
`t=max(r,s)+2`, beyond the maximum transient depth; the all-parameter proof
above supplies arbitrary times. The two fresh-process replay receipt and
input pins are separate files. The author's previous 1,526,365 total lane
assertions are not added to this independent LZK-only count.
