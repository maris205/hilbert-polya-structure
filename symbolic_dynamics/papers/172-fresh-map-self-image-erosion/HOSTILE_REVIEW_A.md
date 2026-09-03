# Hostile Review A — P172

**Manuscript:** *Fresh-Map Self-Image Erosion: Labelled Kernels and a
Forced Jordan Block*  
**Role:** independent hostile reviewer A; not an author of P172  
**Verdict:** `MATHEMATICS_PASS / PASS_WITH_TWO_MINOR_REPAIRS`  
**Counts:** Critical **0** · Major **0** · Minor **2**  
**Lifecycle:** `HOLD_EXTERNAL` (unchanged)  
**Edit boundary:** this review did not edit `main.tex`, either PDF, the author
verifier, or any author report.

## 1. Bottom line

I re-derived the five theorem axes directly from the literal update

```text
A_r = A_(r-1) intersection f_r(A_(r-1)),
```

before inspecting the author verifier.  The endpoint count, every-time
labelled division, algebraic spectrum, forced quotient `J_2`, absorption
claims, and coefficientwise multitime marked transfer are correct as stated
for positive integers `n`.  I found no missing `binom(a,b)` factor, no
orientation error in the Jordan argument, and no failed small or boundary
case.

The mathematical claims therefore need no substantive repair.  Two minor
repairs remain mandatory: make the intended domain `n >= 1` explicit, and
extend the owner subtraction through the successive-elimination/leader-
election vocabulary described in finding `P172-RA-MIN-02`.  A bounded
non-hit after that search still supplies no novelty, priority, or freedom-to-
operate evidence.

No external second-model review endpoint was available in this review
session, so no such corroboration is claimed.  Independence here means a
fresh proof derivation and a separately implemented executable using no
author or scout code.

## 2. Findings and mandatory repairs

### P172-RA-MIN-01 — the positive-integer parameter domain is implicit

**Severity:** Minor.

The first sentence says only “Fix `n`,” while uniform maps on `[n]`, the
factors `n^{-a}`, and the separate `n=1`/`n>=2` conclusions show that the
intended domain is the positive integers.  If `n=0` is admitted, several
displayed expressions require extra `0^0` conventions even though the empty
carrier itself is harmless.  This does not affect any intended theorem, but
the boundary should not be left to convention.

**Mandatory repair:** change the opening definition to “Fix a positive
integer `n`” (or explicitly write `n >= 1`) and use the same domain in the
paper-local narrative/claim ledgers.

**Acceptance criterion:** a repository search of the P172 author package
finds an explicit `n >= 1` scope before the first use of `n^{-a}`.  No proof
or formula change is required.

### P172-RA-MIN-02 — the owner search omits a close alternate vocabulary

**Severity:** Minor under the current `HOLD_EXTERNAL`; it becomes a release
blocker if that hold is ever reconsidered.

The logged queries cover the literal set expression and ordinary random
images, but not the natural equivalent description “each active label votes
for an ambient label; active labels receiving at least one vote survive,” nor
the nearby terms *successive elimination*, *leader election*, *chosen
vertices*, *zero/positive indegree elimination*, and *death-only occupancy*.
That vocabulary leads to the following verified primary neighbor:

- Alan J. Hoffman, Kate Jenkins, and Tim Roughgarden, “On a Game in Directed
  Graphs,” *Information Processing Letters* **83**(1) (2002), 13–16,
  DOI [10.1016/S0020-0190(01)00309-X](https://doi.org/10.1016/S0020-0190(01)00309-X);
  an [author-hosted manuscript](https://timroughgarden.org/papers/lethal.pdf)
  gives the operative rule.

This is **not** a literal collision on the material inspected.  In one round
of Hoffman–Jenkins–Roughgarden, every eligible current vertex chooses an
outgoing arc, the chosen heads are eliminated, and the retained “survivors”
are the vertices that are heads of no chosen arc.  P172 instead retains the
current labels that are heads of at least one draw.  Moreover, their next
round runs on the graph induced by the retained vertices, whereas P172 draws
an endomap into the fixed ambient set `[n]`, so draws may leave the current
set.  Thus the retained side (zero indegree versus positive indegree) and the
sampling space (current induced graph versus fixed ambient set) both differ.
No conjugacy or transfer of P172's labelled kernel, top Jordan coupling, or
marked product follows from that paper.  The general successive-elimination
paradigm and terminology nevertheless receive zero contribution credit.

**Mandatory repair:** extend `SOURCE_VERIFICATION.md` and the scouting owner
log with this comparison, and run/log the alternate query family above.  A
direct source for the positive-indegree, fixed-ambient literal—or a proof
transfer supplying its theorem package—is a kill switch.  A further non-hit
must remain labeled only as a bounded non-hit.

The following record is suitable for `references.bib` if the neighbor is
cited in the manuscript's owner-boundary paragraph:

```bibtex
@article{HoffmanJenkinsRoughgarden2002,
  author  = {Hoffman, Alan J. and Jenkins, Kate and Roughgarden, Tim},
  title   = {On a Game in Directed Graphs},
  journal = {Information Processing Letters},
  volume  = {83},
  number  = {1},
  pages   = {13--16},
  year    = {2002},
  doi     = {10.1016/S0020-0190(01)00309-X}
}
```

Suggested zero-credit language for `SOURCE_VERIFICATION.md` is:

> Hoffman–Jenkins–Roughgarden own a neighboring successive-elimination
> language in which selected heads are removed and zero-indegree vertices
> survive on the current induced graph. P172 keeps positive-indegree current
> labels after fixed-ambient draws. The general paradigm is zero credit, but
> the source is not a literal owner and does not transfer the P172 kernel,
> Jordan, or marked-fibre package.

**Acceptance criterion:** the primary metadata, both rule differences, the
zero-credit boundary, and the direct-owner kill switch are present in the
source/owner records.  If `main.tex` continues to call the conjunction
“owner-thin,” its owner-boundary paragraph should cite or explicitly account
for this neighbor.  External status remains `HOLD_EXTERNAL` regardless of a
query non-hit.

## 3. Independent theorem re-derivation

### 3.1 Fixed endpoint and image-size count

Fix `B subseteq A`, with sizes `b` and `a`, and put `D=f(A)`.  The simultaneous
conditions

```text
A intersection D = B,    |D| = k
```

are equivalent to `D=B disjoint-union R`, where `R` is a `(k-b)`-subset of
`[n] setminus A`.  There are `binom(n-a,k-b)` choices for `R`.  For fixed
`D`, the restriction `f|A` must be onto `D`, giving
`k! S(a,k)` choices.  This proves

```text
H_n(a,b;k) = binom(n-a,k-b) k! S(a,k)
```

for a *fixed* labelled target.  Hence no factor `binom(a,b)` belongs in
`P(A,B)`; that factor appears exactly once only when all size-`b` targets are
summed to form `Q_ab`.

Boundary controls also pass: at `a=0`, the sole restriction has `b=k=0` and
is counted by `0! S(0,0)=1`; impossible values are killed by the binomial or
surjection factor.  A target not contained in `A` is impossible because the
chain is nested.

**Disposition:** no mathematical change.

### 3.2 Every-time labelled division, including `t=0` and marks

Every trajectory remains inside its initial set `A`.  The stabilizer of `A`
in the symmetric group acts transitively on its `b`-subsets and preserves
both the law of every fresh map and every image-size mark.  Conditional on
final size `b`, all `binom(a,b)` possible endpoints therefore have the same
probability.  Summing them gives `(Q^t)_ab`, so each fixed endpoint has mass

```text
(Q^t)_ab / binom(a,b).
```

At `t=0`, the identity matrix makes this one for `B=A` and zero otherwise.
The same group action preserves an entire mark history
`(|f_1(A_0)|,...,|f_t(A_(t-1))|)`, so the division is valid coefficient by
coefficient in the multivariate generating polynomial, not merely after
setting all marks to one.

**Disposition:** no missing labelling factor and no change.

### 3.3 Algebraic spectrum and the forced quotient `J_2`

Order subsets by nondecreasing cardinality.  A transition from `A` can reach
only subsets of `A`; if the target has the same size as `A`, it must equal
`A`.  Thus `P` is triangular.  The equality
`A intersection f(A)=A` holds precisely when `f|A` is a permutation of `A`,
so the diagonal entry on every `a`-set is `a!/n^a`.  Reading the triangular
diagonal proves the claimed algebraic multiset with multiplicities
`binom(n,a)`.

For `lambda_a=a!/n^a`,

```text
lambda_(a+1) / lambda_a = (a+1)/n.
```

This ratio is strictly below one for `a<n-1`, and the sole quotient
collision for `n>=2` is `lambda_(n-1)=lambda_n`.  In the lower-triangular
quotient, solve `(Q-lambda I)x=0` from row zero upward.  The distinct first
`n-1` diagonal entries force `x_0=...=x_(n-2)=0`.  Row `n-1` initially leaves
`x_(n-1)` free, while row `n` contains

```text
Q_(n,n-1) = n (n-1)! S(n,n-1) / n^n > 0
```

and therefore forces `x_(n-1)=0`; only `x_n` is free.  Algebraic
multiplicity two and geometric multiplicity one give exactly one
`J_2(lambda)` in `Q`.  Cardinality-constant functions form a `P`-invariant
subspace represented by `Q`; a restriction of a diagonalizable operator has
square-free minimal polynomial.  Since `Q` does not, neither does `P`.

This proves only the asserted quotient block and full non-diagonalizability,
not a full Jordan inventory; the manuscript respects that boundary.

**Disposition:** forced-`J_2` logic passes unchanged.

### 3.4 Recurrence, absorption, and small boxes

For `n>=2`, any nonempty proper `A` can jump to the empty set by mapping all
of `A` to one point outside `A`.  The full set can jump to a proper set, for
example under a constant map.  Since the chain is finite and nested, every
nonempty state has a positive-probability path to zero and no nonempty closed
class exists.  Zero is the unique recurrent state and absorption is almost
sure.  The CDF is the size-zero entry `(Q^t)_(a,0)`; first-step conditioning
and isolation of the self-loop gives the displayed mean recursion.

For `n=1`, both subsets are indeed fixed.  For `n=2`, direct enumeration gives

```text
Q = [[1,   0,   0],
     [1/2, 1/2, 0],
     [0,   1/2, 1/2]],
```

and the recursion gives `E_1=2`, `E_2=4`.

**Disposition:** recurrence and boundary claims pass; only the scope wording
in `P172-RA-MIN-01` remains.

### 3.5 Multitime marked transfer

The one-step polynomial kernel is the fixed-endpoint count summed over the
`binom(a,b)` labelled targets.  Conditional on an intermediate size, fresh
map sampling makes the next marked transition depend on that size alone.
Ordinary matrix multiplication therefore sums over all intermediate sizes
and multiplies the corresponding monomials, producing the joint mark
polynomial.  Final-layer relabelling symmetry gives the fixed-target division
coefficientwise.  Nothing in this argument makes the epoch marks independent,
and the manuscript explicitly avoids that overclaim.

**Disposition:** no change.

## 4. Independent executable audit

Review A's verifier is located at
`docs/papers172_176_sequence/reviews/p172_review_a/verify_review_a.py`.  It
imports only Python's standard library and imports no author, scout,
manuscript, or earlier-paper module.  It was built from the literal rule with
a materially separate representation and proof attack:

- `frozenset` carriers rather than the author's integer-mask matrix;
- direct enumeration of restrictions and inclusion--exclusion onto counts,
  independently cross-checked against `k! S(a,k)`;
- sparse trajectory propagation for every labelled initial/final state;
- coefficientwise multitime mark-history propagation;
- denominator clearing and fraction-free integer rank calculations;
- direct construction of the full `2^n` operator in addition to quotient
  tests.

The canonical run records **86,630 exact assertions** and covers:

- one-step every-labelled-target/image-size counts for all subsets through
  `n=6`;
- every labelled endpoint through epochs `t=0,...,6` for `n=1,...,6`;
- coefficientwise mark histories through `t=3` for `n=1,...,4`;
- full-operator triangularity, algebraic multiplicity, and
  non-semisimplicity for `n=2,...,5`;
- quotient Jordan nullities `1,2` and exact absorption recurrences for
  `n=2,...,14`;
- the `n=1` and `n=2` boundary sentinels.

Fresh-process replay with `PYTHONHASHSEED=0` is byte-identical to
`CANONICAL.txt`.  Pinned SHA-256 values are:

```text
714d52d4a64a1bbd7ad0835c67ffce36b64c89cd16548ecd33e8cbbb40e0d8d3  verify_review_a.py
14b88091521e2527d880f2c334968cbfa72c89be619a0b8b07c360846fcf66c7  CANONICAL.txt
```

The author verifier is structurally standalone: it has no local imports and
does enumerate literal restrictions before comparing the formula.  Its
marked checks are one-step, while Review A adds a coefficientwise multitime
test.  Because the implementations use different carriers, propagation
styles, onto formulas, and rank routines, no verifier-independence repair is
required.  As always, finite execution attacks arithmetic and boundary
errors; it is not the all-parameter proof.

## 5. Source and owner subtraction audit

The two cited records were checked against their primary/publisher pages:

- Zubkov–Serov, [Math-Net record](https://www.mathnet.ru/eng/dm1403), DOI
  [10.4213/dm1403](https://doi.org/10.4213/dm1403), owns the ordinary repeated
  random-image process and its image-size asymptotics, not the inspected
  self-image-intersection theorem package.
- Flajolet–Odlyzko,
  [DOI 10.1007/3-540-46885-4_34](https://doi.org/10.1007/3-540-46885-4_34),
  owns classical random-mapping statistics.  The 1990 proceedings metadata
  in `references.bib` is consistent with the publisher record.

The manuscript correctly assigns ordinary occupancy/surjection counts,
triangular spectra, Jordan algebra, and hitting-time recursions zero credit.
The internal comparison against P158, P162, P170, and P171 identifies
different update literals/proof engines; repository search found no earlier
P1–P171 instance of the exact P172 conjunction.  These checks support only
the absence of an observed internal collision.  They do not establish
external ownership.

Finding `P172-RA-MIN-02` is the sole source-audit repair.  It is deliberately
not upgraded to a direct-owner finding: the inspected primary source uses the
complementary retained side and a different sampling space.  Conversely, it
cannot be omitted merely because it is not a kill, since it is the closest
located alternate vocabulary for the update.

## 6. Review decision and closure criteria

The theorem package is mathematically accepted by Review A without formula
or proof changes.  The round closes when both minor acceptance criteria are
met and the independent verifier still reproduces all **86,630** assertions.
Until then the precise verdict is

```text
MATHEMATICS_PASS / PASS_WITH_TWO_MINOR_REPAIRS / HOLD_EXTERNAL
```

Neither completion of those repairs nor another bounded owner-search non-hit
authorizes a novelty claim or external circulation.
