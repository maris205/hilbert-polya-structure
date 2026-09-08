# IR1 non-author finite-core certification review

2026-09-07 UTC. Reviewer scope: the finite computational proof, its
coverage logic, and terminal-family matching. This reviewer did not
author IR1's analytic reduction or its enumeration program.

## Verdict and exact claim

**`PASS_FINITE_CORE; ZERO_REMAINING_MUST_FIX_IN_THIS_SCOPE`.**

Proof status: **PROVABLE AS STATED for the following conditional claim**.
If Sections 1–4 of the separately reviewed analytic reduction correctly
reduce every unlisted integral periodic orbit to the displayed bounded
difference/height core, then the full residual core contributes exactly
the two exceptional native cycles

$$
\begin{aligned}
a=-13:&\quad (-4,-2,-3,-3,-2), &&\text{least period }5,\\
a=-2:&\quad (-2,-1,0,0,-1,-2,0,-1,0), &&\text{least period }9,
\end{aligned}
$$

up to cyclic rotation, in addition to the stated F3, F4, F5, F6, F8 and
F12 families. No reverse-orientation quotient is taken.

The independent reconstruction checked **149,732 signed extremal
seeds** and discovered **25,851 oriented cycles**. Every cycle's
parameter, full directed triple-state set, first-return period and family
label agrees with the author's original output. This is a mathematical
reconstruction and full set comparison, not merely a hash check.

The analytic large-difference inequalities and source/substance review
remain separate reviewers' responsibilities. This report alone is not
a verdict on worldwide novelty, an entire manuscript, target arithmetic,
or admission of IR1 into the batch.

## Assumptions, notation and reviewed inputs

The native map and its exact inverse are

$$
T_a(x,y,z)=(y,z,yz+a-x),\qquad
T_a^{-1}(x,y,z)=(xy+a-z,x,y),\qquad a\in\mathbb Z.
$$

For a periodic scalar word write
$d_i=x_{i+2}-x_i$ and $D=\max_i|d_i|$. The finite-core hypothesis is
$1\le D\le100$ and $-3D-1\le x_i\le3D-1$ for every phase.
The parameter-free identity used for normalization is

$$
d_{i-1}+d_{i+1}=(x_{i+1}+1)d_i. \tag{1}
$$

Actually read in full: the frozen IR1 contract, the then-current
`IR1_PROOF.md`, the complete `certify_ir1_core.py`, and the original
summary. All **25,851** original JSONL records were subsequently parsed
and checked by the independent program. The reviewer also read back the
entire independent source after its successful run.

The inspected author inputs are identified in
[INDEPENDENT_SUMMARY.json](INDEPENDENT_SUMMARY.json). In particular:

- Author code SHA256:
  `750b4dbb54cacd1df11cc3929ed436cf8de9877048545f212cecc9bc03b75330`.
- Author cycle JSONL SHA256:
  `352ffd5b5b188e32c347a4083559680e5d1bad12c8e6c6d7cd3dad6324935805`.
- Analytic draft SHA256 at this run:
  `5dcc9c6a84e4219a24fa177399ee1e7292e7217d8b83ab3dda4a90ceebd17e5d`.

The run checked these files were unchanged from its initial read through
completion. Later author revisions require their own relevant diff
review; the original run is not retrospectively relabeled as a new run.

## Strategy and dependency map

1. The analytic reviewer establishes the universal reduction to channels
   plus this finite core. This is the only global exhaustion dependency.
2. The algebra below establishes a complete finite seed parameterization
   directly for both extremal signs.
3. Exact inverse-map iteration partitions every generated seed into a
   certified exit or a closed primitive orbit, without a period bound.
4. Independently generated symbolic family words match the full directed
   state sets. Unmatched words are retained as exceptions.
5. A full independent-to-author comparison checks every terminal orbit,
   not only the two exceptional words or summary counts.

The [review plan](REVIEW_PLAN.md) was written before computation.
The [independent program](independent_ir1_core.py) imports only Python
standard-library modules. It never imports or runs the author's code.

## Proof of finite coverage and termination

### 1. Both signed extremal sections cover the residual core

Choose a phase with $d_0=\delta$, where $\delta\in\{-D,D\}$, and
write $(x_0,x_1,x_2)=(u,s,v)$, $v=u+\delta$. Equation (1) implies
$|s+1|\le2$, hence $s\in\{-3,-2,-1,0,1\}$.

The neighboring differences are

$$
p=v-su+s-a,\qquad q=sv+a-u-s,
\qquad p+q=(s+1)\delta.
$$

The independent program chooses $q\in[-D,D]$ first, then sets
$p=(s+1)\delta-q$ and keeps only $|p|\le D$. The two neighboring
instances of (1) require

$$
|(u+1)p|\le2D,\qquad |(u+\delta+1)q|\le2D. \tag{2}
$$

The height conditions place $u$ in the intersection

$$
[-3D-1,3D-1]\ \cap\ [-3D-1-\delta,3D-1-\delta].
$$

If $p\ne0$, intersect this further with the integer interval centered
at $-1$ of radius $\lfloor2D/|p|\rfloor$. If $q\ne0$, intersect
with the integer interval centered at $-1-\delta$ of radius
$\lfloor2D/|q|\rfloor$. Zero differences impose no extra restriction.
These intersections are exactly (2), including all equality cases.

For every integer $u$ in the resulting interval, recover

$$
a=q-s(u+\delta)+u+s. \tag{3}
$$

Thus every residual periodic orbit contributes a seed with its actual
parameter; no parameter interval has been selected empirically. Both
extremal signs are enumerated, so completeness does not rely on a
time-reversal normalization. The program additionally checks that (3)
recovers both displayed neighboring differences for each seed.

### 2. Exit or first return is a complete decision procedure

Starting at each retained seed, the independent program follows
$T_a^{-1}$ with fixed $D$ and fixed $a$. It rejects a seed only upon a
coordinate leaving $[-3D-1,3D-1]$ or a two-step difference exceeding $D$.
Either event is incompatible with the normalized residual cycle.

If no exit occurs, only finitely many integer triples remain available.
A repeated state must occur. Since $T_a$ is bijective, if the inverse
orbit repeats at times $i<j$, applying $T_a^i$ shows that the initial
state returns after $j-i$ steps. Consequently a first repeated state
cannot be a noninitial state. The program explicitly detects any such
contradiction with a visited-state set. It contains **no period cutoff**.

The returned state set is independently traversed in the native forward
direction. The traversal must close at its initial state, visit every
recorded state, and contain no duplicate triple before return. This
certifies the native least period, not just a period dividing a printed
word length.

### 3. The orbit identifier preserves native orientation

For a fixed $a$, different cycles of an injective deterministic map have
disjoint triple-state sets. The pair consisting of $a$ and the least
lexicographic triple therefore identifies a cycle without choosing a
word reversal. Equality checks nevertheless compare the **entire**
triple-state sets, so the identifier is not used as a lossy fingerprint.

The author canonicalizes scalar words by rotations and explicitly adds
their reversed words as additional candidates. This is correct: the
recurrence is reversal invariant, but a reverse need not be a rotation.
The independent code instead discovers both signs directly, then checks
that reversing each terminal word finds its actual counterpart in the
discovered set. It never identifies a pair solely because they reverse.

## Actual single-run result

Executed once from the active repository root:

```text
python -B henon_dynamics/research_c419_c423/continuation_round2/integral_return_review/finite_core/independent_ir1_core.py
```

Python **3.12.3**; exit code **0**; measured runtime **3.37218 seconds**.
The independent search was not rerun after this PASS. Subsequent work
read its output and audited its source.

| Extremal sign | Seeds | First returns | Height exits | Difference exits |
|---|---:|---:|---:|---:|
| Negative | 74,866 | 25,907 | 18,624 | 30,335 |
| Positive | 74,866 | 25,907 | 18,615 | 30,344 |
| Total | 149,732 | 51,814 | 37,239 | 60,679 |

The rows exactly partition the seed set. Opposite directions can exit
through different boundaries; the nine-seed exchange between exit types
is not a mismatch in periodic classification. The author's forward
positive-sign traversal corresponds to the inverse negative-sign
traversal under the reversor, explaining their matching exit totals.

The maximum observed traversal length was **18**, not an imposed bound.
The author's forward-only maximum was **12**; neither value limits the
search. The observed seed parameters ranged from **-503 to 497**. These
are outputs of (3), not assumed parameter cutoffs.

| Family | Distinct oriented cycles in this finite certificate |
|---|---:|
| F3 | 200 |
| F4 | 25,350 |
| F5 | 99 |
| F6 | 100 |
| F8 | 50 |
| F12 | 50 |
| Exceptions | 2 |
| Total | 25,851 |

These finite counts are **not** counts of all members of the unbounded
symbolic families. In particular, they cannot be inserted as global
fixed-point counts on all of $\mathbb Z^3$.

## Independent terminal-family and least-period checks

The independent program generated the stated terminal words from their
integer parameters and compared complete directed triple-state sets,
instead of copying the author's rotation-pattern classifier. A small
explicit polynomial implementation over $\mathbb Z[X,Y]$ checked all
**40** recurrence identities for F2/F3/F4/F5/F6/F8/F12 before enumeration.
This verifies family existence symbolically for all allowed integer
parameters, not only at finite-core values.

The proper-period conditions in the supplied draft are also consistent:

- F2 alternates $u,v$ with $a=u+v-uv$; it is fixed exactly when $u=v$.
- F3 has period three unless its parameter $t=-2$, when it is fixed.
- F4 has period two exactly when $2t=a+1$, and is fixed only when also
  $t=-1$. Otherwise it has period four.
- F5 has prime length five and contains both $0$ and $-1$, so it cannot
  be constant and always has least period five.
- F6 collapses to a fixed word at $t=0$. For $t\ne0$, periods one or
  two contradict the displayed zero positions, and period three would
  require $t=-t$ over the integers. Its least period is six.
- F8 cannot have period one or two because its even positions include
  both $-1$ and $1$. Period four requires $t=-t-2$, or $t=-1$;
  at that parameter its least period is four, otherwise eight.
- For F12 with $m\ge1$, period four or two would equate the first
  coordinate $1$ with the fifth coordinate $-1$. Period three would
  equate the third coordinate $1$ with the sixth coordinate $-m$.
  Period six would require $m=1-m$, impossible for integral $m$.
  Thus its least period is twelve. Its unforced ownership remains C413.

Both exceptional words pass the recurrence in both directions and have
respectively five and nine distinct triple states; their printed lengths
are therefore their true first returns. They are unmatched by every
applicable generated family.

### Important orientation check: 49 genuinely distinct reverse pairs

Exactly **25,753** terminal cycles are equal to their reversal up to
rotation. The remaining **98**, all in F5, form **49** distinct pairs.
For example, at $a=-1$ these native words are different cycles:

$$
(-50,-1,49,0,0),\qquad (-50,0,0,49,-1).
$$

In the F5 parameterization, reversal replaces $u$ by $-1-u$.
That replacement must not be used as a general rotation equivalence.
The author code already preserves these pairs; this is a verified
requirement for subsequent prose and counting, not an outstanding code
defect. Both exceptional cycles are self-reversing up to rotation.

## Corrections, limitations and handoff

No computational must-fix item remains. The original draft's statements
that the finite output is still pending are chronological placeholders;
the author/coordinator should replace those when assembling the completed
theorem, using the original output and this independent receipt. This
reviewer did not edit the author's files.

The report's all-parameter implication remains conditional on the
separate analytic review of the universal reduction. A source novelty
verdict, level-by-level arithmetic formulas, and any future manuscript
are not certified by this computation. Exact Python arithmetic plus
two independently structured implementations is strong reproducible
computational evidence, not a proof-assistant kernel certificate or
human peer review.

Artifacts: [independent source](independent_ir1_core.py),
[complete native cycles](INDEPENDENT_CYCLES.jsonl),
[summary with per-amplitude partition and input identifiers](INDEPENDENT_SUMMARY.json),
and the [pre-run plan](REVIEW_PLAN.md). Only this reviewer-owned directory
was written. No author output was overwritten, no old certification was
rerun, and no Git, accepted-contract, manuscript or evaluator state was
modified.
