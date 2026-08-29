# Hostile Review B — P112

## Review posture and independence

This is an independent, non-author review of the raw manuscript, its stated
controls, `code/verify.py`, and the stored verifier output.  I did **not** read
`HOSTILE_REVIEW_A.md`.  I did not edit the manuscript or any existing file,
perform final QA, compute release hashes, or use Git.  External dissemination,
novelty, and priority remain **HOLD**.

The review was deliberately adversarial.  I reconstructed the update from the
literal edge orientation, derived the energy and block identities without using
the prose proof, tested both boundary systems, decoded the six-vertex mask by
hand-independent code, searched for cycles and deeper transients, and then ran
the supplied verifier and build in an isolated temporary directory.

## Provisional verdict

**MAJOR REVISION / HOLD.**  I found no counterexample to a theorem and no
mathematical reason to reject the package in its present scope.  The central
dynamics is coherent and the exhaustive controls are unusually strong.  The
blocking issue is owner subtraction: the current four-item bibliography does
not adequately distinguish the residual synchronous iteration from the much
larger tournament arc/cycle-reversal and regular-tournament enumeration
literature.  A visible comma error in the main factorization display must also
be repaired before any release.

The manuscript is strongest when presented as a compact exact analysis of one
specified finite self-map.  It must not be marketed as a sharp transient-depth
result, a new theorem about tournament score sequences generally, or a new
enumeration of regular tournaments.

## Independent reconstruction

### 1. Orientation and update

For each unordered pair `{u,v}`, write `u ->_T v` when `u` wins, and let
`s_T(v)` be the outdegree.  The update has the following literal meaning:

- if `s_T(u)>s_T(v)`, the new edge is `u -> v`;
- if `s_T(u)<s_T(v)`, the new edge is `v -> u`;
- if the scores tie, the old edge is retained.

Thus an arc `x -> y` is reversed exactly when `s_T(x)<s_T(y)`.  This agrees
with the manuscript's definition of the reversed-upset set `R(T)`.  There is no
orientation ambiguity in the mathematical definition.

The coding convention also agrees with the definition: unordered pairs are in
lexicographic order and bit `1` means that the smaller endpoint wins.  For
mask 148 at `n=6`, the least-significant-first bit vector is

```text
(0,0,1,0,1, 0,0,1,0, 0,0,0, 0,0,0).
```

Literal recomputation gives

```text
148, scores (2,2,2,2,3,4)
  4, scores (1,1,2,2,4,5)
  0, scores (0,1,2,3,4,5)
  0, scores (0,1,2,3,4,5).
```

Hence the stated first non-idempotent witness is orientation-correct and shows
`Phi^2 != Phi` at order six.

### 2. Exact energy increment

For every reversed arc `x -> y`, the old score change contributes `-1` to
`delta_x` and `+1` to `delta_y`; simultaneous reversals simply add these
incidence contributions.  Expanding the new squared-score energy gives

```text
E(Phi T)-E(T)
  = 2 sum_v s_T(v) delta_v + sum_v delta_v^2
  = 2 sum_{x->y in R(T)} (s_T(y)-s_T(x)) + sum_v delta_v^2.
```

Every term in the first sum is a positive integer.  If an edge changes then
`R(T)` is nonempty, so the increment is positive.  Conversely, if no edge
changes then every `delta_v` is zero.  The strictness claim is therefore exact,
including the possibility that several reversals cancel at a vertex.  Finiteness
then excludes all temporal cycles of length greater than one.

### 3. Equal-score blocks and positive iterates

Let the old equal-score classes be `C_1,...,C_k`, ordered by strictly decreasing
old score, and put `L_i=sum_{j>i}|C_j|`.  Every interclass edge after one update
points from `C_i` to `C_j` for `i<j`; every intraclass edge is unchanged.
Therefore

```text
Phi(T)=T[C_1] oplus ... oplus T[C_k]
```

and a vertex `v in C_i` has new global score

```text
L_i + s_{T[C_i]}(v).
```

The resulting scores of block `i` lie in
`[L_i,L_i+|C_i|-1]`.  The maximum of the immediately lower block interval is
`L_i-1`; hence the intervals are disjoint and preserve block order.  Later
updates cannot change interblock edges or merge old blocks, and score
comparisons inside a block are exactly internal-score comparisons.  Induction
then yields, for every `t>=1`,

```text
Phi^t(T)=oplus_i Phi_{C_i}^{t-1}(T[C_i]).
```

This validates the substantive factorization.  The PDF, however, visibly
prints a stray comma in each exponent on the right-hand side; see MINOR below.

### 4. Exact pointwise depth and the only proved global bound

Define a leaf when the current subtournament is fixed; otherwise split it into
its equal-score classes and recurse.  A nonfixed tournament cannot have just
one score class, because a total score tie makes the update retain every edge.
Thus every child of a nonleaf on `n` vertices has at most `n-1` vertices and the
tree is well-founded.

The factorization gives the exact recurrence

```text
tau(T)=0                                      if T is fixed,
tau(T)=1+max_i tau(T[C_i])                    otherwise.
```

Consequently `tau(T)` equals the refinement-tree height.  Induction only gives
the stated universal estimate `tau(T)<=n-1` for `n>=1`.  Exhaustion through
order six finds maximum depths

```text
n:          0  1  2  3  4  5  6
max depth:  0  0  0  0  1  1  2.
```

Those data do **not** show that `n-1` is sharp, asymptotically attainable, or
even close to the true maximum.  The manuscript currently respects this
boundary.  It must continue to do so in the title, abstract, metadata, and any
future cover letter.

### 5. Fixed tournaments, recurrence, and EGF

If `T` is fixed, every edge between distinct score classes already points from
the higher class to the lower class.  Vertices in the same class receive the
same external wins and have the same global score, so their internal scores are
equal.  Each induced block is therefore a regular tournament.

Conversely, in an ordinal sum of regular blocks of sizes `m_i`, every vertex in
block `i` has score

```text
a_i=sum_{j>i}m_j+(m_i-1)/2.
```

For adjacent blocks, `a_i-a_{i+1}=(m_i+m_{i+1})/2>0`.  Thus the blocks are
exactly the score classes and the update fixes the tournament.  This also proves
uniqueness.  The empty tournament is correctly treated as the empty sum.

Let `r_j` count regular tournaments on a fixed labelled `j`-set, with `r_0=0`,
and let `f_n` count fixed tournaments.  Choosing the label set and orientation
of the unique top block gives, for `n>=1`,

```text
f_n=sum_{j=1}^n binom(n,j) r_j f_{n-j},       f_0=1.
```

With exponential generating functions `R` and `F`, this is
`F=1+RF`, hence `F=1/(1-R)`.  Using
`(r_1,r_2,...,r_6)=(1,0,2,0,24,0)` gives

```text
(f_0,...,f_6)=(1,1,2,8,40,264,2048),
```

as claimed.  The recurrence is a standard labelled ordered-sequence
construction once the fixed-point decomposition has been established; it
should not receive novelty credit in isolation.

### 6. Zeta and boundary systems

Strict energy implies `Fix(Phi_n^m)=Fix(Phi_n)` for all `m>=1`.  Substitution
into the finite Artin--Mazur definition gives

```text
zeta_{Phi_n}(z)=exp(sum_{m>=1} f_n z^m/m)=(1-z)^(-f_n).
```

At `n=0` and `n=1`, the phase space is a singleton, the map is the identity,
`tau=0`, `f_n=1`, and the zeta function is `(1-z)^(-1)`.  No empty-product or
zero-vertex exception is missing.

## Counterexample campaign

I actively tried the following failure modes:

- reverse the stated arrow convention and compare the literal update;
- allow simultaneous incidence cancellations in the energy computation;
- seek overlap or adjacency contact between successive score intervals;
- seek a nonfixed one-class node that would break the depth induction;
- seek a fixed tournament whose score class is not internally regular;
- seek two adjacent regular blocks with the same global score;
- seek a positive-period orbit not fixed by the map;
- test idempotence below order six and decode the reported mask at order six;
- test `n=0` and `n=1` separately rather than letting a recurrence silently
  swallow them.

None produced a theorem-level counterexample.  The exact exhaustive verifier
independently covers every labelled tournament through order six, 33,868 states
in total, and searches periods through eight positive iterates.

## Fresh computational and build audit

The following was performed in a newly created `/tmp` directory.  No generated
file was copied back into the paper directory.

| Check | Fresh result |
|---|---:|
| verifier exit | PASS |
| assertions | 1,677,508 |
| states enumerated | 33,868 |
| fresh stdout vs stored stdout | byte-identical |
| first non-idempotent state | `n=6`, mask `148` |
| maximum observed depth through `n=6` | 2 |
| fresh PDF pages | 6 |
| fresh PDF bytes | 308,689 |
| final-pass LaTeX overfull/underfull/undefined warnings | 0 |
| PDF fonts | 22/22 embedded, 22/22 subset |

The sole textual match for `Warning` in the final log was the package metadata
line identifying `rerunfilecheck`; it is not a warning message.  I rendered and
visually inspected all six pages.  There were no clipped equations, missing
glyphs, broken hyperlinks, table overflows, or blank pages.  The stray commas in
display (5) are visible and must be fixed.

## Owner and collision audit

This was a bounded search, not a novelty certificate.  Search absence must not
be converted into novelty or priority language.

### What is already owned

1. Landau's theorem and the general theory of tournament score sequences are
   classical.  The manuscript already subtracts Landau and Moon.
2. Arc and cycle reversals are a substantial established tournament technique.
   Thomassen's *Arc reversals in tournaments*, Discrete Mathematics 71 (1988),
   73--86, DOI
   [10.1016/0012-365X(88)90031-3](https://doi.org/10.1016/0012-365X(88)90031-3),
   is a direct owner that the current bibliography omits.  Ryser's
   score-preserving triangle-reversal result, conventionally routed through
   Moon or a primary source, also needs explicit discussion.  These operations
   are not the same as the manuscript's synchronous score-changing map, but
   keyword-level subtraction is insufficient.
3. Regular-tournament enumeration is independently developed.  McKay's
   *The asymptotic numbers of regular tournaments, Eulerian digraphs and
   Eulerian oriented graphs*, Combinatorica 10 (1990), 367--377, appears on the
   author's [publication list](https://users.cecs.anu.edu.au/~bdm/publications)
   with the [primary manuscript](https://users.cecs.anu.edu.au/~bdm/papers/rt.pdf).
   The values `r_j` and their broader enumeration context cannot be presented as
   residual contributions.
4. A recent close-vocabulary source is Ghosh--Kuchlous--Mehra--Mukhopadhyay,
   *The Power of the Score Sequence of a Tournament*, ESA 2026, DOI
   [10.4230/LIPIcs.ESA.2026.156](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ESA.2026.156).
   It studies which tournament properties are determined by score sequences via
   cycle reversals.  It is not an owner of this iteration, but a contemporary
   score/cycle-reversal discussion must not omit it merely because the draft's
   bibliography predates its appearance.
5. The recurrence and reciprocal EGF are standard labelled sequence
   bookkeeping once the regular-block decomposition is known; Artin--Mazur owns
   the zeta convention.  The manuscript mostly says this correctly.

### Residual scope supported by this audit

The bounded search did not locate the exact deterministic self-map that, in one
synchronous step, directs every unequal-current-score edge from the higher
outdegree endpoint to the lower and leaves ties unchanged.  Nor did it locate
the precise conjunction of strict quadratic increment, persistent score-block
factorization, recursive pointwise depth, and fixed regular-block decomposition.
That is the defensible residual package **if** a fuller owner search remains
negative.  This statement records search outcome only; it is neither novelty
nor priority evidence.

### Internal collision firewall

A repository-wide bounded text search of P1--P111 titles, abstracts/main files,
READMEs, and plans found no earlier tournament, Copeland, regular-tournament, or
score-upset-reversal system.  The manuscript's explicit comparison with P106 is
structurally convincing: P106 evolves vertex subsets under a neighborhood
polarity; P112 evolves complete-graph orientations by score comparisons.  The
shared words “fixed point,” “synchronous,” and “zeta” do not constitute a model
collision.

## Findings by severity

### CRITICAL

**None found.**  I found no false main theorem, orientation inversion,
unhandled boundary state, nontermination counterexample, or corrupt executable
control.

### MAJOR (mathematics)

**None at theorem level.**  The energy, factorization, depth recursion, fixed
decomposition, recurrence, EGF, and zeta formula survive independent
reconstruction.

One scope condition is mandatory: preserve the manuscript's current statement
that `n-1` is merely a universal bound.  Any claim that it is sharp, any
extrapolation from the observed depths through six, or any phrase such as
“the maximum depth is `n-1`” would create a new unsupported MAJOR claim.

### MAJOR (owner scope)

**M-O1 — the owner audit is too narrow for circulation.**  Landau, Moon, and
Monsuur do not by themselves subtract tournament arc/cycle-reversal dynamics,
and Moon is not enough as an enumeration owner for the displayed regular counts.

Actionable repair:

1. add and discuss Thomassen 1988 and the Ryser triangle-reversal lineage;
2. add McKay 1990 as a direct regular-tournament enumeration owner;
3. check and discuss the 2026 score-sequence/cycle-reversal paper;
4. run a documented search over “score correction,” “Copeland dynamics,”
   “degree-based tournament update,” “arc reversal,” “self-consistent
   tournament,” and synchronous/parallel variants;
5. state in the contribution paragraph that the residual object is the exact
   synchronous map and theorem conjunction, not score sequences, reversals,
   regular tournaments, their counts, generic Lyapunov arguments, EGFs, or
   zeta bookkeeping;
6. keep novelty, priority, and external dissemination on HOLD after the repair
   unless a separate independent owner review clears them.

### MINOR

**m1 — visible malformed exponent in the central formula.**  Source display
(5) uses `\Phi_{C_i}^{,t-1}` in both the first and last factors.  The comma is
visible in the PDF and makes the formula look like a distinct notation.

Actionable repair: replace both with `\Phi_{C_i}^{t-1}`, rebuild, and inspect
page 3.

**m2 — make label-set naturality explicit.**  The global map is introduced on
`[n]`, while `Phi_{C_i}` acts on an arbitrary labelled subset.  The prose says
“the same rule,” which is mathematically enough, but one sentence stating that
the definition is natural on any finite labelled vertex set would remove a
needless formal wrinkle.

**m3 — retain the exact mask convention next to the witness.**  The manuscript
does this in the controls section.  Do not move the mask to the abstract or
README without also retaining pair order, least-significant-bit direction, and
the meaning of bit one.

**m4 — distinguish evidence from proof whenever quoting the verifier.**  The
33,868-state exhaustion proves all claims only for orders through six and
falsifies idempotence globally via one witness; it is not the proof of the
infinite-order convergence, depth bound, or fixed decomposition.

## Required repair checklist

- [ ] Repair the two comma exponents in display (5).
- [ ] Add direct arc/cycle-reversal owners and explain the model difference.
- [ ] Add a direct regular-tournament enumeration owner.
- [ ] Audit the recent ESA 2026 score-sequence paper.
- [ ] Document a broader score-correction/Copeland/parallel-update search.
- [ ] Preserve `tau<=n-1` as a non-sharp universal bound only.
- [ ] Preserve explicit `n=0,1` and mask-orientation conventions.
- [ ] Re-run the verifier, byte comparison, fresh build, font check, and page-3
      visual inspection after repairs.
- [ ] Keep external dissemination, novelty, and priority on HOLD pending
      independent owner clearance.

## Final recommendation

The mathematical core is compact, exact, and currently credible.  I recommend
**MAJOR REVISION**, driven by owner-scope repair rather than a failed theorem.
After the bibliography and subtraction paragraph are strengthened and the
display typo is repaired, the paper should receive a fresh independent owner
check.  It should not advance to external circulation on the evidence of this
review alone.
