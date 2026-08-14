# Paper31 exact experiment report — Wilson semiring verifier trichotomy

Candidate: **SD-C33**
Strongest GO: **source-derived Wilson prime cycles and analytic formal marked
product**
Strongest STOP: **matched-clone, transient-pruning, and recurrent
entropy-dilution trichotomy**
Overall: **Route A rejected; Route B locked**

## Outcome

Alphabet-sum genuinely adds information absent from Paper30's bare
multiplicative clone. On conjugacy classes of finite full shifts, alphabet-sum
and alphabet-product reconstruct the semiring of nonnegative integers, so
successor order and quotient/remainder are source-derived. The Wilson residue
path then closes exactly one primitive cycle of graph length `p-1` for every
prime `p`, with all temporal repetitions and no supplied prime table.

This earns structural A0 and analytic primitive-orbit A1. It does not earn a
same-object determinant. Three exact controls close the positive route:

1. a matched semiring relabel transports every path, cycle, roof, and marker;
2. a transient verifier prunes to its accepted-support diagonal for Wilson
   and arbitrary total predicates; and
3. the primary recurrent exact-clock adjacency is noncompact, while first
   return becomes trace class only by contracting `p-1` original steps to one.

## Frozen source recurrence

For each `n>=2`, the candidate computes

\[
r_{n,1}=1,
\qquad
r_{n,k+1}\equiv r_{n,k}(k+1)\pmod n,
\qquad 1\le k\le n-2.
\]

The graph closes the terminal edge precisely when
`r_{n,n-1}=n-1`. Candidate code implements only successor-ordered
multiplication and least remainder. Its audited source contains integer
literals `0,1,2` and no prime, factorization, support-table, target-zero,
file, or network identifier.

The independent evaluator is physically separate: it imports neither
`wilson_core` nor the generator. It recomputes every residue path and SHA-256,
implements trial division independently, regenerates operation tables, formal
trace terms, exact marker products, and universal-wrapper products, and then
checks serialized candidate artifacts.

## Exact census at cutoff 4096

| Surface | Exact count | Result |
|---|---:|---|
| Wilson candidates `n=2,...,4096` | 4,095 | every final residue, path hash, and cycle length verified |
| accepted cycles | 564 | exactly the primes; largest `4093` |
| composite controls | 3,531 | all reject |
| base-2 Fermat pseudoprimes | 13 | all reject, including `341,561,1729,2047` |
| bare polynomial-UFD addition pairs | 144 | `0/144` transported-addition matches |
| matched semiring operation pairs | 169 | `169/169` match; all Wilson paths copy |
| named semiring controls | 7 | only baseline and matched clone pass the full source lock |
| random operation controls | 33 | `0/32` random magma pairs pass; matched `Z/11Z` relabel passes |
| entropy-budget rows | 1,692 | 564 cycles times three positive real parts |
| formal marked trace powers | 16 | every contribution list finite; no ordinary trace claimed |
| marker comparisons | 2 | equality at `z=1`, exact difference at `z=1/3` |
| universal support wrappers | 5 | every transient wrapper prunes; every unbounded recurrent wrapper dilutes |
| source-separated evaluation | 26,620 | `26,620/26,620 PASS` |
| exact regression tests | 18 | `18/18 PASS` under direct pytest and the isolated runner |

The authority generator reproduces the seven cutoff-4096 prototype JSON
artifacts byte for byte. The seven CSV artifacts have identical parsed rows
after the only bridge normalization: the prototype writer's CRLF is converted
to authority LF. The original prototype ledger/aggregate is
`100490afb62c6302329db814a856782d20cf986c608a365b9a72fb848fc5a0cd`;
the authority LF-canonical 14-artifact aggregate is
`36792d57cc2d58c1b52df47fdf757c86f6e10ed5eae685423259d0d9739a0dee`.

After adding the source-separated evaluation and bounded analysis, two
isolated authority runs produced the same 16 fresh artifacts byte for byte.
Their aggregate SHA-256 is
`c0be3f65d26d655aba06343766c734f19da3349b29cf4f0d731bba23fc33a449`.
The test module resolves authority `results/` by default, so direct pytest and
the custom fresh-directory runner both execute the same 18 assertions; the
runner retains an explicit results-directory override. The integrity auditor
symmetrically excludes its own output and the SHA ledger from both sides of
the inventory comparison, so it exits successfully on both the pre-audit
inventory and the complete frozen tree. A regression assertion executes this
complete-tree audit under direct pytest. The final code/result freeze contains
31 verified hashes; its ledger SHA-256 is
`62f2c8795f9559504c4f82c8bb7c32cc064e338da8dace1becb88529ce7e8f55`.

## Bare versus matched clone

Paper30's bare clone maps an integer to a prime monomial. Ordinary polynomial
addition cannot extend this map because

\[
x_2=\Phi(2)=\Phi(1+1)=\Phi(1)+\Phi(1)=1+1=2,
\]

which is false in the polynomial ring. The 144 exact grid rows contain no
ordinary-addition match.

This is not a universal clone separation. For labels `y_n`, transported
operations

\[
y_m\oplus y_n=y_{m+n},
\qquad
y_m\otimes y_n=y_{mn}
\]

give an isomorphic semiring presentation. All 169 operation rows and every
Wilson residue path agree exactly. Naturality requires this equality; it is a
firewall against claiming that the construction selects the literal printed
integers.

## Prime-cycle layer

Wilson's theorem identifies terminal closure with primality. A successful
deterministic block gives one primitive cycle `Gamma_p` of length `p-1`.
With total roof `log p`, its `r`-fold temporal repetition has weight
`p^(-rs)`. The formal diagonal sum at graph power `m` is

\[
\operatorname{Tr}_{\mathrm{per}}(L_s^m)
=\sum_{p-1\mid m}(p-1)p^{-sm/(p-1)},
\]

which is finite because `p-1` divides `m` only when `p<=m+1`. The formal
trace-log gives

\[
D_W(s,z)=\prod_p\left(1-z^{p-1}p^{-s}\right).
\]

It converges normally for `|z|<1` on compact subsets of the `s`-plane and at
`z=1`, `Re(s)>1` specializes to the Euler product. This is valid periodic data
and earns `A1_PASS_ANALYTIC`; it is not `det(I-zL_s)`.

## Whole recurrent operator: noncompactness

Let nonnegative edge roofs on `Gamma_p` sum to `log p`. At least one edge has

\[
\tau(e_p)\le \frac{\log p}{p-1},
\qquad
|w_s(e_p)|\ge p^{-\operatorname{Re}(s)/(p-1)}\longrightarrow1.
\]

The selected edges lie in disjoint prime blocks. Their source basis vectors
are orthonormal and have orthogonal images whose norms do not tend to zero.
Thus the primary recurrent adjacency is noncompact for every
`Re(s)>0` and belongs to no finite Schatten class, for every nonnegative
exact-clock allocation.

At the largest finite witness `p=4093`, `Re(s)=2`, the forced lower bound is
`4093^(-2/4092)=0.99594322976540206`. The finite row illustrates the analytic
proof; it is not a numerical proof of noncompactness.

## First return and marker ownership

Inducing on one base per prime cycle gives

\[
R_s e_p=p^{-s}e_p,
\qquad
\det(I-zR_s)=\prod_p(1-zp^{-s}),
\]

an honest trace-class determinant exactly for `Re(s)>1`. But first return
changes one cycle from `p-1` graph steps to one induced step. At cutoff 31 and
`s=2`, the products agree exactly at `z=1` and differ exactly at `z=1/3`:

\[
\prod_{p\le31}(1-z^{p-1}p^{-2})
\ne
\prod_{p\le31}(1-zp^{-2})
\quad(z=1/3).
\]

The induced determinant therefore belongs to a changed time object and cannot
repair A2 for the primary recurrent graph.

## Transient pruning and universal controls

A feed-forward verifier DAG has no closed walk. With a summable regulator its
power traces vanish, and block triangularity leaves only terminal accept
loops. Deleting the verifier computation preserves all periodic data. The
same wrapper was instantiated for:

- Wilson primes;
- squares;
- powers of two;
- Fibonacci numbers; and
- a seeded hash support.

All five produce the same pruning/dilution alternatives. Thus the transient
Euler product records an already-computed support; it is not a Wilson-specific
dynamical cancellation.

## Findings in analysis form

**Observation.** Wilson and independent trial division agree on all 4,095
integers.
**Interpretation.** The source recurrence exactly implements the classical
terminal relation without a prime table.
**Implication.** A0 and primitive A1 pass, but terminal correctness alone does
not yield an operator determinant.
**Next step.** Require arithmetic interaction before accept/reject is known.

**Observation.** The bare clone fails while the matched clone copies every
row.
**Interpretation.** Addition changes the source language but remains invariant
under transported semiring isomorphism.
**Implication.** This is a genuine Paper30 escape, not integer-presentation
selectivity.
**Next step.** Keep matched clones mandatory.

**Observation.** Recurrent exact-clock weights force near-unit edges.
**Interpretation.** Entropy `log p` is diluted across `p-1` disjoint steps.
**Implication.** The primary operator is noncompact and A2 fails.
**Next step.** Seek source-derived overlapping recurrence compatible with the
roof/length compactness criterion.

**Observation.** First return agrees only after setting the free marker to
one.
**Interpretation.** Induction changes graph time.
**Implication.** Its honest determinant cannot be transferred to the original
graph.
**Next step.** Preserve the original graph-step marker in every same-object
claim.

## Route decision and next obligation

The frozen Route-A tuple is

    (A0_STRUCTURAL_ARITHMETIC_RELATION,
     A1_PASS_ANALYTIC,
     A2_FAIL,
     A3_FAIL,
     A4_FAIL).

Overall: Route A rejected; Route B false/locked.

Paper32 must not replace Wilson with another terminal primality verifier. It
must construct a source-derived nonterminal, overlapping recurrent
interaction before acceptance is known; prove compactness or an honest
determinant for the uninduced whole operator; preserve the original marker;
and pass matched-clone plus universal-wrapper controls before any RH claim.

No target-zero datum or RH conclusion is used anywhere in this experiment.
