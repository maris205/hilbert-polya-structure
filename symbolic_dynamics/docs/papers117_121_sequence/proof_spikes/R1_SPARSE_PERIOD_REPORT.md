# R1 sparse-period residual spike

**System.** Strict upper-triangular binary matrices, equivalently labelled
ordered DAGs on `[n]`, under

\[
T(A)=A+A^2\qquad (A\in M_n(\mathbb F_2)).
\]

**Proof status.** `PROVABLE_AS_STATED`, and the stated range strengthens.

**Selection verdict after owner subtraction.** **KILL.**  The residual theorem
is exact, but it reduces completely to the already-subtracted scalar period
formula plus one elementary path-support inequality.  It therefore triggers
the hostile gate's announced kill condition rather than clearing it.

**External status.** `HOLD_EXTERNAL`.  Search absence below is only a bounded
no-hit, never a novelty or priority claim.

## 1. Claim, strengthening, and boundaries

Write

\[
r(A)=\min\{r\geq 1:A^r=0\},\qquad e(A)=\#\{(i,j):A_{ij}=1\}.
\]

For `s >= 1`, put

\[
m=m_s=2^{2^{s-1}}.
\]

### Theorem 1 (exact sparse period stratum)

If `A` has exact period `2^s`, then `e(A) >= m`.  Equality holds if and only
if the ordered DAG of `A` consists of one increasing directed path of length
`m` and isolated vertices.  Consequently the number of exact-period-`2^s`
states with exactly `m` arcs is

\[
\binom{n}{m+1}.
\]

This formula is valid for **every `n > m`**, not merely for the requested
range `m < n <= m^2`.  For `n <= m`, the stratum is empty.  Thus the target
claim is true without correction, but its upper range restriction is
unnecessary.

All conventions are explicit:

- the zero matrix has `r(0)=1` and period one;
- period one is outside Theorem 1 because `s >= 1`;
- a path of length `m` has `m` arcs and `m+1` vertices;
- vertices retain the fixed order `1<...<n`, and every permitted arc points
  upward in that order;
- the binomial coefficient is zero when `n<m+1`, consistently with the empty
  stratum.

## 2. Dependency map

The proof has exactly two inputs.

1. **Scalar/composition input:** the period is determined by `r(A)`.
2. **Ordered-DAG input:** a nonzero matrix power supplies an actual increasing
   path, hence an arc lower bound.

The equality classification and count use only Input 2 after the period
window from Input 1 has been identified.  The arc-budget corollary in Section
5 uses the same two inputs and no new engine.

## 3. Exact period versus nilpotence index

### Lemma 2 (iterate formula)

For every integer `t >= 0`,

\[
T^t(A)=\sum_{j\preceq t} A^{2^j},
\tag{3.1}
\]

where `j preceq t` means that every binary digit of `j` is also a binary digit
of `t`.

#### Proof

Let `f(x)=x+x^2` in the commutative polynomial ring `F_2[x]`, and let `F`
denote Frobenius, `F(g)=g^2`.  Then `f=I+F`, so

\[
f^{\circ t}(x)=(I+F)^t(x)
 =\sum_{j=0}^t \binom tj F^j(x)
 =\sum_{j\preceq t}x^{2^j}.
\]

The last equality is Lucas's parity criterion.  Evaluation at the single
matrix `A` is a ring homomorphism from `F_2[x]` to the commutative algebra
`F_2[A]`, giving (3.1).  This avoids any false appeal to Frobenius additivity
on a general noncommutative matrix algebra.  ∎

### Lemma 3 (exact point period)

If `r=r(A)`, the exact period of `A` is

\[
P(r)=2^{s(r)},\qquad
s(r)=\min\{s\geq0:2^{2^s}\geq r\}.
\tag{3.2}
\]

In particular, for `s>=1`, the period is exactly `2^s` if and only if

\[
m_s<r(A)\leq m_s^2.
\tag{3.3}
\]

#### Proof

The minimal polynomial of a nilpotent matrix of index `r` is `x^r`.
Therefore

\[
I,A,A^2,\ldots,A^{r-1}
\tag{3.4}
\]

are linearly independent.  Let \(t>0\) and \(v=\nu_2(t)\).  In (3.1), the term
indexed by `j=0` is `A` itself.  Among the positive binary submasks of `t`,
the least is `j=2^v`; hence the least remaining matrix power is

\[
A^{2^{2^v}}.
\]

If `2^{2^v}>=r`, that and every larger power vanish, so `T^t(A)=A`.  If
`2^{2^v}<r`, its coefficient is one and no other surviving term has the same
exponent; independence (3.4) prevents cancellation.  Thus

\[
T^t(A)=A\quad\Longleftrightarrow\quad 2^{2^{\nu_2(t)}}\geq r.
\]

The smallest positive `t` satisfying this condition is `2^{s(r)}`, proving
(3.2).  Since `m_s=2^{2^{s-1}}` and `2^{2^s}=m_s^2`, comparison of adjacent
thresholds gives (3.3).  ∎

## 4. Sparse-period theorem

### Lemma 4 (arc support of a nonzero power)

For every ordered-DAG adjacency matrix over `F_2`,

\[
r(A)\leq e(A)+1.
\tag{4.1}
\]

#### Proof

If `r=r(A)`, then `A^{r-1}` is nonzero.  Some entry
`(A^{r-1})_{ij}` is therefore one.  It is the parity of the length-`r-1`
directed walks from `i` to `j`; an odd set is nonempty.  Because every arc is
strictly increasing, such a walk repeats no vertex and is an increasing
directed path containing `r-1` distinct arcs.  Hence the entire graph has at
least `r-1` arcs.  ∎

### Proof of Theorem 1

Suppose that the exact period is `2^s`.  Equation (3.3) gives
`r(A)>=m+1`, and Lemma 4 gives

\[
e(A)\geq r(A)-1\geq m.
\]

If `e(A)=m`, both inequalities are equalities: `r(A)=m+1`.  Since
`A^m != 0`, the proof of Lemma 4 supplies an increasing path with `m` arcs.
Those arcs exhaust the entire edge set.  The graph is therefore exactly that
one path, while every vertex outside it is isolated.

Conversely, a single increasing path of length `m`, with all remaining
vertices isolated, has `A^m != 0` (there is one full path between its
endpoints) and `A^{m+1}=0`; hence `r(A)=m+1`.  Since `m>=2`,

\[
m<m+1\leq m^2,
\]

so Lemma 3 gives exact period `2^s`.

Finally choose the `m+1` path vertices.  Their increasing order forces the
only possible path: consecutive selected vertices must be joined.  Thus each
chosen subset gives one state, and distinct subsets give distinct states,
for a total of `binom(n,m+1)`.  The converse construction works for every
`n>m`, proving the strengthened range.  ∎

### Corollary 5 (support of the period stratum)

For `s>=1`, an exact-period-`2^s` state exists on `n` ordered vertices if and
only if `n>=m_s+1`.  Its minimum arc count is `m_s`, and the minimum layer has
size `binom(n,m_s+1)`.

#### Proof

Necessity follows from Theorem 1.  For sufficiency take an increasing path on
`m_s+1` chosen vertices and isolate all others.  ∎

## 5. Broader exact arc-budget envelope

The sparse theorem extends to a sharp statement for every admissible arc
budget, although only for the **maximum** period at that budget.

### Theorem 6 (fixed-budget nilpotence and period maxima)

For `0<=e<=binom(n,2)`,

\[
\max_{A:e(A)=e}r(A)=\min(e+1,n)
\tag{5.1}
\]

and consequently

\[
\max_{A:e(A)=e}\operatorname{per}_T(A)
=2^{\min\{s\geq0:2^{2^s}\geq\min(e+1,n)\}}.
\tag{5.2}
\]

Both maxima are attained explicitly.

#### Proof

Strict upper triangularity gives `r(A)<=n`, while Lemma 4 gives
`r(A)<=e+1`; this proves the upper bound in (5.1).

If `e<n-1`, take a path of length `e` and isolated vertices.  Its index is
`e+1`.  If `e>=n-1`, start with the full chain

\[
1\longrightarrow2\longrightarrow\cdots\longrightarrow n
\]

and add any `e-(n-1)` other increasing arcs.  A length-`n-1` increasing walk
on `n` vertices must visit all vertices in their fixed order, so the displayed
chain is the unique such walk from `1` to `n`.  Thus
`(A^{n-1})_{1n}=1` even over `F_2`, and `r(A)=n`.  This proves sharpness in
all cases, including `n=1,e=0`.  Formula (5.2) now follows from the monotone
period function (3.2).  ∎

This gives a complete, exact answer to the broader question “how large can
the period be with `e` arcs?”, but it does not enumerate a full period layer.

## 6. Counterexample attacks and discarded strengthenings

### False conjecture: nilpotence index equals longest graph path plus one

This is false for fixed all-one adjacency weights in characteristic two.
On vertices `1<2<3<4`, take the four arcs

\[
1\to2,\quad1\to3,\quad2\to4,\quad3\to4.
\]

The graph has two paths of length two from `1` to `4`, but they cancel modulo
two.  Hence `A^2=0`, `r(A)=2`, and the state is fixed, despite combinatorial
longest-path length two.  The proof above deliberately uses only the valid
one-way statement `A^k != 0 =>` at least one length-`k` path.

### Unnecessary range restriction

The proposed hypothesis `n<=m^2` is not needed for the equality layer.  It is
the upper end of the *nilpotence-index* window (3.3), not an upper bound on
the number of ambient isolated vertices.  For example, at period two
`m=2`; for every `n>=3`, including `n>4=m^2`, the two-arc equality states are
exactly the `binom(n,3)` increasing two-edge paths.

### Extra arcs do not admit the same equality conclusion

The classification is intentionally limited to `e=m`.  Once extra arcs are
allowed, parity cancellation can lower the index, while other extra arcs can
preserve it.  Neither the support nor the count of an arbitrary higher arc
layer follows from this argument.

## 7. Deterministic verification

Verifier:
[`r1_sparse_period_verify.py`](./r1_sparse_period_verify.py)

Run from the repository root:

```text
python3 docs/papers117_121_sequence/proof_spikes/r1_sparse_period_verify.py
```

The standard-library verifier executed **75,026 exact assertions** and
covered:

- all `2^(n choose 2)` ordered DAGs for `1<=n<=6`, checking the exact period
  formula, `r<=min(e+1,n)`, every fixed-budget maximum, and all accessible
  equality layers;
- every two-arc state for `3<=n<=12` and every four-arc state for
  `5<=n<=9`, checking the equality characterization and binomial count;
- all constructed `m=16` equality states for `17<=n<=20`, checking index 17
  and exact period eight;
- an explicit sharp witness for every arc budget at every `1<=n<=12`;
- the four-arc parity-cancellation diamond above.

The canonical summary was:

```text
assertions=75026
period-2 minimum-layer counts n=3..12: 1,4,10,20,35,56,84,120,165,220
period-4 minimum-layer counts n=5..9: 1,6,21,56,126
period-8 constructed counts n=17..20: 1,18,171,1140
exhaustive state counts n=1..6: 1,2,8,64,1024,32768
diamond: arcs=4, longest_path=2, nilpotence_index=2, period=1
```

Two consecutive fresh invocations produced identical one-line JSON output.
The computation is evidence against small counterexamples, not a substitute
for the proofs in Sections 3--5.

## 8. Owner subtraction and final gate

### Direct scalar owner

[Wadsanthat and Panraksa, *Distribution of cycle lengths of a quadratic map
over finite fields of characteristic 2* (2019)](https://murex.mahidol.ac.th/en/publications/distribution-of-cycle-lengths-of-a-quadratic-map-over-finite-fiel/)
directly studies the scalar map `x -> x^2+x`, including its additive
structure, nilpotent points, and cycle lengths.  Lemmas 2 and 3 therefore
receive **zero residual credit**: evaluating the same composition polynomial
in `F_2[A]` does not create a new temporal engine.

### Classical graph/matrix background

[Gansner, *Acyclic Digraphs, Young Tableaux and Nilpotent Matrices*, SIAM J.
Algebraic Discrete Methods 2 (1981), 429--440](https://doi.org/10.1137/0602046)
relates Jordan invariants of generic nilpotent matrices supported by acyclic
digraphs to path families.  It is not a direct owner of the fixed all-one
binary adjacency problem—mod-two cancellation prevents that identification—
but it makes the path/nilpotence bridge classical background rather than a
new engine.

Bounded searches using the formulations `minimum arcs prescribed
nilpotency index upper triangular`, `nilpotent adjacency matrix sparsity
acyclic digraph`, `ordered DAG A+A^2 period`, and `exact period stratum
x+x^2 matrix` found no direct statement of Theorem 1 or Theorem 6.  That is a
bounded no-hit only.

### Does the spike clear the hostile objection?

**No.**  It answers the requested extremal slice exactly, but after deleting
the scalar-owned period/index conversion, all remaining content is:

\[
A^{r-1}\ne0
\Longrightarrow
\text{some increasing path has }r-1\text{ arcs}.
\]

Minimum arcs, equality structure, the binomial count, stratum feasibility,
and the fixed-budget envelope are short consequences of that same witness.
There is no second independent mechanism, no full nonminimal period-stratum
census, and no protection against the reviewer summary “scalar iterate plus
a path witness.”  This is precisely the failure mode stated in the Phase-3
hostile gate.

## 9. Final disposition

| question | decision |
|---|---|
| Is the requested theorem correct? | **Yes; proved, with range strengthened to all `n>m`.** |
| Is the equality characterization exhaustive? | **Yes.** |
| Is the binomial count exact? | **Yes.** |
| Is there a broader exact corollary? | **Yes: the fixed-arc-budget maxima (5.1)--(5.2).** |
| Did bounded verification find a counterexample? | **No; 75,026 assertions passed.** |
| Does it survive scalar-owner subtraction as a paper engine? | **No.** |
| Candidate action | **KILL; do not freeze a paper number.** |

The theorem and verifier may be retained as an internal control result, but
novelty, priority, submission, and all external dissemination remain on
**HOLD**.
