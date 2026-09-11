# Fresh36: independent bounded residual desk

Date: 2026-09-11. Author: `current_round_independent_scout`.
Status: **AUTHOR-DESK NEGATIVE; NOT INDEPENDENT REVIEW OR PROMOTION**.

Scope: the current round's two empty seats only. Three explicitly defined
families were taken through mechanism triage, not five padded labels.
No pilot, source execution, import, build, process inspection, child agent,
Git operation, central-index edit, numbering change or external upload occurred.
This desk does not establish literature exhaustion or a quota contribution.

## 1. Littlewood quotient-union on bounded partitions

Fix integers `r >= 2`, `B >= 0`. The state space is all integer partitions
of size at most B. Under the ordered r-core/r-quotient bijection, write
`lambda <-> (kappa; lambda_0,...,lambda_{r-1})`. Define Q(lambda) to be the
partition obtained by merging the multisets of parts of all quotient
components, discarding the core. This is not an abacus bead-moving update.

### Source boundary

Walsh and Warnaar, *Modular Nekrasov–Okounkov formulas*, Proposition 4.1
and equation (4.6), give the Littlewood bijection, its size identity and
the r-core generating function. The actual proposition and formula were
read in the [primary paper PDF](https://www.mat.univie.ac.at/~slc/wpapers/s81walshwar.pdf).
The claims below are author deductions, not claims of that paper about Q.
An author-hosted PDF continuation timed out; an arXiv HTML-v2 attempt
returned 404. The successful PDF was the basis, not those failed accesses.

### Time axis: exact global maximum, elementary proof

Let h(lambda) be the first time Q iterates reach the empty partition.
The size identity gives

`|Q(lambda)| = (|lambda|-|kappa|)/r <= floor(|lambda|/r)`.

Thus empty is the only recurrent state and

`max h = 0` if B=0; otherwise `max h = floor(log_r B)+1`.

For the upper bound, after `floor(log_r B)+1` steps the size is below 1.
For sharpness start with `(1)`, which maps to empty, and repeatedly take
the unique partition with empty core and ordered quotient
`(previous_partition, empty,...,empty)`. The h-step example has size
`r^(h-1)`. It belongs to the state space exactly when that size is at most B.
For B>=1, empty and `(1)` have the same image, so Q is noninjective.

### Inverse axis: evaluated all-target fibre

For target mu let s=|mu| and m_j be the multiplicity of its part j.
Let c_r(k) count r-core partitions of size k and
`C_r(K)=sum_{0<=k<=K} c_r(k)`, with C_r(K)=0 for K<0. Then

`#Q^{-1}(mu) = C_r(B-rs) * product_{j>=1} binom(m_j+r-1,r-1)`.

Indeed, distribute the m_j indistinguishable parts among r labelled
quotient components independently; stars-and-bars gives the product.
Choose any core of size at most B-rs. The Littlewood bijection supplies
exactly one source partition for every such choice, with no overlap.
This also handles the empty target and unattainable targets. If desired,
c_r(k) is evaluated by coefficients of the classical generating function

`sum c_r(k) z^k = product_{j>=1} (1-z^(rj))^r/(1-z^j)`.

### Residual decision

This is the strongest literal candidate in this desk: an all-parameter
sharp clock plus an evaluated inverse formula really were obtained.
Nevertheless both follow immediately from one classical decomposition:
size contraction and independent allocation of quotient parts. No distinct
pointwise/core-layer clock or new fibre extremum mechanism has been shown.
No exact local quotient-union hit was identified during bounded navigation;
that is not an absence certificate. Do not promote merely because the
literal map differs from older abacus dynamics. **No two-axis residual
cleared; no pilot parameters handed off.**

## 2. Nonzero-mod-3 path recomputation on ordered DAGs

For n>=1 take every binary strictly upper-triangular n-by-n adjacency
matrix A. Define

`T(A)_ij = 1{(A+A^2+...+A^(n-1))_ij != 0 mod 3}` for i<j.

This is a total finite autonomous update; n=1 has the unique empty graph.
For n>=3 the two three-vertex chains differing only by edge 13 both map
to the complete triangle, and isolated extra vertices preserve the
collision. The n<=2 boundary is the identity.

### Literal distinction and old mechanism

The local predecessor DP3 uses path count **equal to 1 modulo 3**.
Our predicate is **nonzero modulo 3**: a triangle with two paths from
1 to 3 distinguishes them. This is therefore not a literal-identity claim.
The already-read source of the old mechanism is
`docs/papers204_208_sequence/scouting/finite_structures_eighth/PROOF_BOUNDARIES.md`,
Section 4 (with its intake/source files). Its span-triangular scalar
forcing argument applies unchanged apart from relabelling scalar maps.
The ICALP 2025 primary article
[Fully Dynamic Algorithms for Transitive Reduction](https://doi.org/10.4230/LIPIcs.ICALP.2025.92)
was opened as path-count background; no ownership of this autonomous
modular iteration is attributed to it.

### Time-axis proof and a nonfixed recurrence witness

Write the positive path count at (i,j) as `a_ij+q_ij mod 3`, where q
uses strictly shorter spans. For q=0,1,2, respectively, the scalar
update of a is identity, constant 1, and flip. Adjacent bits are fixed.
Once lower spans are periodic with common period L, composition over a
full forcing period is identity, flip or constant. The next span thus
has period dividing 2L and incurs at most L additional transient steps.
Induction yields, for n>=2, eventual period dividing `2^(n-2)` and
transient at most `2^(n-2)-1`. These are bounds, not sharpness claims.
They are the previous triangular mechanism, not a residual theorem.

It would be false to claim fixed-point-only behavior. For n=5 set all
span-1 and span-2 edges to 1, edges 14 and 25 to 0, and edge 15=t.
Span-2 positive path counts are 2 and span-3 counts are 3. The paths
from 1 to 5 excluding edge 15 are exactly
`135, 1235, 1245, 1345, 12345`, so the full count is t+5.
All other bits stay fixed while t flips. This is an explicit two-cycle,
and extends by isolated vertices to n>=5. It is a hand proof, not a run.

### Inverse axis and decision

Given previously selected shorter-span source edges, compute q. For a
target bit b: q=0 forces a=b; q=1 requires b=1 and leaves a free;
q=2 forces a=1-b. This is only a branching triangular decoder.
Summing its unresolved branches is not an evaluated all-target fibre,
nor is a sharp extremum established. **Old time mechanism plus missing
inverse residual: reject as current paper seat; no pilot.**

## 3. Sardinas–Patterson residual-set update

Fix a finite nonempty codebook C contained in Sigma^+, and let U be the
set of all suffixes of words of C, including full words and epsilon. On the
finite state space P(U), define a total update without any halting rule:

`T_C(S) = C^{-1}S union S^{-1}C`,

where `A^{-1}B={v : uv in B for some u in A}`. Both quotients consist
of suffixes of codewords, so the update stays in P(U).
Noninjectivity is not universal in C; it occurs, for example, for
`C={0,01}`, because U includes 1 and `T_C({1})=T_C(empty)=empty`.

### Source boundary

[Cassaigne and Nicolas, On the decidability of semigroup freeness](https://arxiv.org/html/0808.3112)
was read for historical attribution of the Sardinas–Patterson algorithm
in the free-monoid setting. It is not treated as a source for the exact
total map above. A primary 1967 paper access failed; a code-theory PDF
access redirected to abstract/header material; an OCR search snippet
was not used to justify the formula. There remains an exact-iteration
source-body gap. The elementary identities below stand independently.

### Mechanism proof

Define `R(s)=C^{-1}{s} union {s}^{-1}C`. Quotients distribute over
unions, hence `T_C(S)=union_{s in S}R(s)`. Thus this is precisely the
direct-image map of a finite relation on U; all iterates are powers of
that relation applied to S. It is not a new dynamical mechanism merely
because code residuals supply the relation. The local graph-set scout
`docs/papers162_166_sequence/scouting/graph_set/OWNER_SEARCH_LOG.md`
already identifies powerset relation-image lifts
as the old P97/BQC lane. No sharp code-specific clock is proved here.

For completeness, a generic all-target inverse expression is available.
For y subset U set `E_y={s in U:R(s) subset y}`. Inclusion–exclusion gives

`#T_C^{-1}(y) = sum_{B subset y} (-1)^|B| * 2^{#{s in E_y:R(s) intersect B = empty}}`.

Every valid source is a subset of E_y; the alternating sum enforces
coverage of every member of y. This is generic set-cover counting,
not a new code-specific evaluated simplification or sharp extremum.
**Relation-image reduction and no independent code-specific second
axis: negative desk; no pilot.**

## Handoff boundary

Three finite autonomous families were instantiated; all author proofs
above remain unreviewed. Fresh36 provides no promotion recommendation,
retained-seat claim, completed-paper claim or broader exhaustion claim.
The quotient-union family is the only one with both quantities explicitly
evaluated, but that alone does not establish two independent contributions.
No executable source or pilot parameter box is proposed.
