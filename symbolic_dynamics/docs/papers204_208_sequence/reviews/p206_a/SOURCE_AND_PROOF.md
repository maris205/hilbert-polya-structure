# P206 A — all-target weak-template adapter and proof audit

2026-09-05 UTC. Independent manuscript reviewer: batch197_fosp_gate.
Reviewed immutable Round0, not a proposed revision. Mathematical status:
**PROVABLE AS STATED**. Value recommendation: **KILL_VALUE** under this
batch's materially separate two-axis gate. The adverse adapter below is a
reviewer deduction; it is not attributed verbatim to the older paper.

## 1. Primary source, exact operators, and read ceiling

Amy N. Myers and Herbert S. Wilf, *Left-to-right maxima in words and
multiset permutations*, Israel Journal of Mathematics 166 (2008), 167–183,
DOI 10.1007/s11856-008-1026-x. The [publisher metadata](https://link.springer.com/article/10.1007/s11856-008-1026-x)
was actually read. Mathematical locators below refer to the
[primary preprint](https://arxiv.org/pdf/math/0701078), not an inspected
subscription journal body. Read contexts: definitions, PDF p. 1; marginal
Theorem 3, p. 3; positional-template Theorem 6, p. 4; first-occurrence
encoding, Section 6, pp. 7–8; full template-operator argument, Section 7.2,
pp. 10–12. The 2007 arXiv deposit and served title-page 2018 date are not
substituted for the verified 2008 publication year.

The source's $W$ means weak left-to-right record; $O$ means not a weak
record. For $F_\tau(z)=\sum_k f(k,\tau)z^k$, Theorem 6 equations (10),(13)
give

$$\Omega_W F=\frac F{1-z},\qquad
\Omega_O F=zF'-\frac F{1-z}.$$

Equation (9) gives $\Omega_S F=zF/(1-z)$ for a strong record. These count
every word satisfying a full positional template, not just its number of
records. They do not themselves mention cyclic feedback or $R^2$.

Initialization is explicit here: an empty template has one empty word.
A feasible nonempty $W/O$ template starts with $W$; normalize that first
symbol to $S$, since the first position is vacuously strong. Starting from
the source's $1/(1-z)$ and applying $\Omega_S$ gives the correct one-letter
counts. Subsequent operators apply to nonempty prefixes, with constant
coefficient zero. This avoids an empty-alphabet convention ambiguity from
applying $\Omega_W$ directly to the displayed empty generating function.

## 2. The exact adapter claim and assumptions

Let $n\ge1$, with original labelled positions in $\mathbb Z/n\mathbb Z$.
The carrier is precisely $\{1,2,3\}^n$, records are strict, and all scans
use the same source. For a target $b$, let
$Z(b)=\{i:b_i=1\}$. If this set is nonempty, it partitions the remaining
positions into forward open intervals between consecutive roots. A run
may be empty. Keep the original position labels; choosing a first root
only orders a product and does not quotient rotations.

For a target run $u=(u_1,\ldots,u_m)\in\{2,3\}^m$, define a template
on the reversed interval by

$$\tau(u)_j=\begin{cases}W,&u_{m+1-j}=2,\\O,&u_{m+1-j}=3.\end{cases}$$

Let $\mathcal W_2(\tau)$ be the set of binary words over $\{1,2\}$
whose weak-record positions are exactly the $W$ positions of $\tau$.
The claim is a bijection, for every target, between its maximum-three
sources and $\prod_u\mathcal W_2(\tau(u))$, with every root fixed to
source three and each chosen binary word reversed into its own labelled
interval. Maximum-two and maximum-one sources are separate singleton or
empty branches. If $Z(b)$ is empty, every branch is empty.

This is stronger than matching fibre cardinalities: it reconstructs every
source coordinate, and its inverse reads those same coordinates. It is
not the generic assertion that any inverse can be encoded statically.

## 3. Complete proof of the adapter

### Step 1: output roots and the three disjoint source maxima

A scan has one strict record exactly when its initial letter is a global
maximum. If it starts below the maximum, the scan eventually encounters a
larger value and has at least two records. Consequently any source has
$Z(b)$ equal to its entire set of maximum positions, and $Z(b)$ is nonempty.
In particular a target with no one has no source, independently of the
manuscript's first-image proof.

If the source maximum is one, its only possible word is $1^n$, whose
target is $1^n$. If its maximum is two, a source two gives output one and
a source one gives output two. Therefore this branch consists of the
single word $x_i=3-b_i$ exactly when $b$ is binary and has a one. Its
maximum is then really two. These cases include the target $1^n$.

### Step 2: a local equivalence that retains every cyclic constraint

Suppose the source maximum is three. Its three positions are forced to
be exactly $Z(b)$. In one forward intervening source run
$a=(a_1,\ldots,a_m)\in\{1,2\}^m$, the next root is a three; after
that three, no later source value can become a record. Thus no coordinate
in another run imposes any further restriction on this run's output.

At position $j$, a source two has records two, three, so its output is two.
A source one has three records exactly when some source two occurs among
$a_{j+1},\ldots,a_m$ before that terminating three. Otherwise its records
are one, three and its output is two.

Put $v=(a_m,\ldots,a_1)$. A binary position of $v$ is a weak record if it
is two, or if it is one and no preceding two occurs. The preceding two
condition is exactly the later-two condition in $a$. Therefore

$$R(x)_{\text{position of }a_j}=2
\quad\Longleftrightarrow\quad
m+1-j\text{ is a weak record position of }v.$$

The complementary condition is output three. This proves equivalence of
the entire target run to the full $W/O$ template, not to marginal record
data. It also proves sufficiency: take any matching $v$, reverse it, and
the resulting source realizes every coordinate of $u$.

### Step 3: product bijection and cyclic boundaries

Fix source three at each root. For each labelled interval independently
choose $v\in\mathcal W_2(\tau(u))$ and reverse it into that interval.
Step 2 gives the prescribed output at every nonroot; Step 1 gives output
one at every root. This constructs a maximum-three source. Reading and
reversing its intervals is an inverse to the construction, so there is
neither omission nor duplication. Empty intervals contribute the unique
empty word. Consecutive roots, one root, and the closing cyclic interval
are all included. At $n=1$ the one root has one empty interval.

Combining this product with the two singleton branches is disjoint,
because their source maxima differ. This completes the full source-set
bijection for every target with a one; the rootless case was rejected in
Step 1. No use of the author's run-count formula or $R^2$ theorem is needed.

### Step 4: evaluate the prior operators at alphabet size two

For a nonempty prefix write $(a,b)=(f(1,\tau),f(2,\tau))$. Extracting the
first two coefficients from the displayed operators gives

$$W:(a,b)\longmapsto(a,a+b),\qquad
O:(a,b)\longmapsto(0,b-a).$$

The first feasible symbol initializes $(1,2)$; a first $O$ is impossible.
If the length-$m$ template is all $W$, repeated updates give $(1,m+1)$.
Otherwise suppose its initial $W$ run has length $t$. Just before the
first $O$, the pair is $(1,t+1)$; just after, it is $(0,t)$. Either later
operator fixes $(0,t)$. Its binary-word count is therefore exactly $t$.

For $\tau(u)$, an all-$W$ template means $u=2^m$, while $t$ is precisely
the terminal two-run length of $u$. These are exactly the manuscript's
two $g(u)$ branches. This is coefficient extraction from an existing
full-template theorem, not a new unevaluated counting problem.

### Step 5: every zero/nonzero interface and both corrections

If a target contains a cyclic $31$ edge, the interval ending at that root
ends in three. Its reversed template starts with $O$, so the maximum-three
branch is empty. The target contains three, ruling out maxima one and two
as well. Conversely, if a target has a one and no cyclic $31$, every
nonempty interval ends in two. Its template starts with $W$ and the counts
in Step 4 are positive. Thus the exact nonempty-target set is
$\mathcal D_n$; the first-image support also follows from this adapter.

For $b\in\mathcal D_n$, the product in Step 4 is the maximum-three
count; the maximum-two branch contributes $\mathbf1_{\{3\notin b\}}$;
the maximum-one branch contributes $\mathbf1_{\{b=1^n\}}$. At the
all-one target each of the three branches is a singleton, so the fibre
is three. At $n=2$ the only feasible targets are $11,12,21$, each with
three sources. Rootless and $31$ targets have zero sources as just proved.
This recovers all of Theorem 3.1, including every boundary and the actual
source decoder, from the explicitly proved interface plus prior templates.

## 4. What is prior, what remains task-specific, and the value decision

| Item | Exact status after the adapter |
|---|---|
| Count all binary words with any fixed weak/nonweak positional template | Direct output of prior Theorem 6 at alphabet size two |
| The two evaluated run factors $m+1$ and terminal length $t$ | Immediate two-coefficient calculation above; not a new counting axis |
| Maximum positions are output roots; reverse each binary interval | Task-specific interface lemma, fully proved in Steps 1–3; not claimed stated by Myers–Wilf |
| All labelled source words and the $3/2/1$ branches | Exact product bijection plus two one-line singleton branches; no remaining fibre constraint |
| First-image support | Positive-template criterion and root condition give precisely $\mathcal D_n$ |
| $R(\mathcal D_n)=\mathcal C_n$, reflection, sharp height | Not supplied by the cited template theorem; the manuscript's temporal deduction survives |
| Fibre maximum and all equality targets | Compare the evaluated factors, then apply the already deducted integer-product optimum |

The interface lemma is real and is needed; it must not be erased by saying
the older source literally proves a cyclic-feedback theorem. However,
after that short change of representation there is no new inverse
enumeration left: every source restriction, every count, and all zero
cases have been transferred to an existing full positional-template
calculus. Theorem 3.2 adds a strict factor comparison and labelled transport
of the classical product optimum, already zero-credit arithmetic under
the admitted contract. This does not restore a materially separate axis.

Therefore A recommends **KILL_VALUE** for the admitted two-axis paper,
while retaining **MATH_VALID** for the stated mathematics. This is not a
claim that the older article contains $R^4=R^2$, not an accusation of
plagiarism, and not a universal theorem about all static inverse formulas.
A temporal-only note would be a different admission decision, not a
no-change acceptance of this contract. Larger finite cutoffs cannot repair
the exact all-length adapter.

The manuscript's $123123/123213$ example is correct. It only separates
displayed single-scan conditioning data. The adapter instead uses the full
target's root positions and reversed positional templates on each interval,
so the example supplies no counterexample to Steps 1–5. The source audit
already permits an exact enriched adapter to reopen admission; this is
such an adapter.

## 5. Independent mathematical audit of the surviving statements

Read the full [modular dynamics proof](../../../../papers/206-ternary-cyclic-record-feedback/frozen_round0/sections/02_dynamics.tex),
[inverse/extremal proof](../../../../papers/206-ternary-cyclic-record-feedback/frozen_round0/sections/03_fibres.tex)
and [complete proof package](../../../../papers/206-ternary-cyclic-record-feedback/frozen_round0/PROOF_PACKAGE.md).
No repair lemma was supplied to the author.

For the temporal proof, the first-image scan comparison permits the
terminal appearance of the old initial maximum; it never creates a missing
extra record. The constructed source $4-b$ has upward increments at most
one and maximum three, so each integer record level is forced. For the
second-image comparison, an initial increase contributes exactly one
record, equality contributes none, and the only initial decrease is a
unit drop. In that case the lower start can add at most the one missing
intermediate level before their common higher records. This also covers
the old maximum encountered last. Reflection on the two-sided unit-step
language is onto and involutive, not merely forward invariant. Every
periodic point belongs to the second image, proving exact recurrence.
Constant reflection-fixed points have minimum one. The $n=1,2$ cases and
the closing $13$ edge of $3^{n-2}21$ establish the sharp claimed heights.

The trace count uses cyclic labelled walks, including diagonal loops at
$n=1$. Direct determinants give
$\det(\lambda I-A)=\lambda(\lambda^2-3\lambda+1)$ and
$\det(\lambda I-B)=(\lambda-1)(\lambda^2-2\lambda-1)$.
Words avoiding one contribute $2^n$ in both matrices. The artificial
zeroth recurrence values are never interpreted as $n=0$ carrier counts.

The inverse proof is mathematically correct, as also certified deductively
by Steps 1–5. For maxima, replacing a three-containing target by its
binary version strictly increases at least one positive factor, and also
adds its maximum-two source. For nonconstant binary targets, the factor
product is exactly the product of root-block sizes. Merging ones, splitting
parts at least five, exchanging three twos for two threes, and retaining
the four-versus-two-twos equality gives every optimum, not just one witness.
The all-one target and lengths one/two are separately compared. These are
valid deductions, even though the inverse contribution is transferred.

## 6. Other source and internal collision subtraction

Omer Berkman, Baruch Schieber and Uzi Vishkin, *Optimal Doubly Logarithmic
Parallel Algorithms Based On Finding All Nearest Smaller Values*, Journal
of Algorithms 14(3) (1993), 344–370, DOI 10.1006/jagm.1993.1018. Read the
[institutional primary abstract and metadata](https://cris.technion.ac.il/en/publications/optimal-doubly-logarithmic-parallel-algorithms-based-on-finding-a/),
not its full algorithmic proof. It defines nearest smaller values on each
side of an ordered array. Order reversal yields the ordinary greater-value
primitive; this does not provide the feedback temporal theorem. No source
hit/nonhit is used as a blanket novelty certificate.

The following originals were actually inspected at the stated literal
rule/proof scopes and pinned in [supplementary inputs](SUPPLEMENTARY_INPUTS.sha256).
This is bounded subtraction, not an exhaustive classification of factors.

- [P117](../../../../papers/117-odd-run-reversal-cyclic-words/main.tex):
  odd-run binary reversal and its parity classification. Its absence of
  fixed states at odd length differs from CRC3's unique fixed word; no direct
  autonomous bijection on those carriers gives this CRC3 core.
- [P122](../../../../papers/122-even-record-block-reversal/main.tex):
  record-block permutation reversal and its descending mechanism. The
  inspected recurrent classification has fixed permutations rather than
  CRC3's strict two-cycles; shared record vocabulary is not a literal owner.
- [P139](../../../../papers/139-lyndon-factor-start-feedback/main.tex):
  recomputed Lyndon factor starts, suffix-record/leading-one mechanism
  and all-one terminal behaviour. Its literal statistic and erosion
  theorem do not supply the CRC3 reflection theorem.
- [P176](../../../../papers/176-first-frequency-rotation/main.tex):
  adaptive two-branch rotations, generator-component theorem and complete
  inverse proof in Section 4. Its every-target fibres have at most two
  sources. CRC3 already has three constant-target sources, and seven at
  length five, excluding this direct inverse transfer.
- [P202](../../../../papers/202-ternary-ordered-reset/main.tex):
  ordered neighbour-reset rule and complete one-step decoder. Each
  nonempty fibre is a power of two, unlike CRC3's seven. This excludes
  that direct independent-bit decoder, not arbitrary enriched maps.

None of these limited separations reverses the positive Myers–Wilf adapter.

## 7. Actual finite stress test, distinct from the proof

The new [checker](verify.py) reads no file and imports no author, gate, old
paper, or reviewer implementation. It compares full literal functional
graphs with local-cycle orbit classification, pointer-depth evaluation,
a reverse whole-circle skyline transducer, and the template-definition
source-set construction. Template counts are computed separately by the
old operator specialization, not by the manuscript's terminal-run formula.

The complete [actual output](CANONICAL.json) passed 3,698,764 assertions:
all 265,719 ternary states/targets for $n=1,\ldots,11$, full source sets
in every box, 797,157 maximum-branch comparisons, every binary template
of length zero through twelve, and integer-product DP through one hundred.
It checks every invalid target and every labelled maximum target. These
finite equalities pressure the deduction; Steps 1–5 are the all-length
reason for the adverse adapter. See [replay evidence](REPLAY_LOG.md).
