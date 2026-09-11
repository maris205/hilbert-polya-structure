# Fresh47 independent proof, collision and value check

2026-09-11. Reviewer: `current_round_independent_scout`, separate from
author `current_round_two_seats_scout`. The reviewer read the author's
complete temporal proof before checking it and did not contribute that
proof. Root proposed the rooted-tree collision question; the reviewer
verified it below. This is a bounded candidate review, not a manuscript
review, admission, new number, or cross-model certification.

## Outcome

**GO_NARROW_TO_GATE for the exact-clock theorem as substantive progress;
NOT a clearance of a fresh dynamical system.** Both temporal inequalities
and the resulting all-word clock withstand this independent deductive
check. A bounded independent execution found no temporal counterexample.
The initial inverse formula had a **Major algebra error**, found by the
author while checking PRE and independently verified here; the corrected
formula is accepted deductively, with the failed statement preserved.

The inverse mechanism is completely inherited from PRE. It can still be
the mathematically separate evaluated baseline in a narrow clock-centered
note; the criteria do not require two independently new proof mechanisms.
More importantly, a rooted-tree conjugacy identifies the `q=4` dynamics
with the old PFR system. Thus a **new-system admission remains unresolved**
under the inherited exclusion of conjugates. A gate would have to decide
explicitly whether this substantive theorem on an occupied schedule may
be retained under the user's clear-theorem-progress requirement. This
review neither silently waives that boundary nor calls the new clock old.

## 1. Inputs and independence

Read the full initial `finite_residual_fresh47/DESK.md`, then the corrected
inverse and source sections after the author reported their correction.
The initial full read preceded the author's edit. The author's separately
preserved V1 is expressly a reconstructed draft, not an immutable original
byte capture. No false original-capture claim is made here.

Read the current anchor, complete inherited
`docs/papers197_201_sequence/PROBLEM_ANCHOR.md`, project workflow, complete
PRE `PROOF_AND_DISPOSITION.md` and `SOURCE_AND_COLLISION.md`, C01 at
`docs/papers147_151_sequence/scouting/combinatorial/SCOUT.md:269`, and the
original PFR candidate/kill rows plus `pilot.py:445–481` in
`docs/papers187_191_sequence/scouting/algebra_lane/replacement/`.
Historical scientific programs were not imported or executed.

The research-review skill guided claim/source separation. Its named
external provider is unavailable; this is the project-authorized
current-model independent process, not an external review. No child
reviewer was spawned. Only this new independent directory was written.

## 2. Temporal proof audit

### First inequality

For each maximal run, its walk alternates on one edge. An even run maps
all its vertices to the surviving boundary vertex. An odd run maps its
vertices, except the last, to the initial boundary, and the last to the
final boundary. The displacement is at most one. Crucially, consecutive
run maps agree at their common boundary, including intervening empty
output pieces. Their concatenation is order preserving. Thus a maximizing
ordered input pair maps to an ordered output pair, and each endpoint
distance loses at most one. This proves `M(Rw) >= M(w)-2`; no matching
choices or assumed common deletion tree are used.

### Exposed-peak lemma

A strict output peak toward a root enters and exits on the same edge.
The two surviving letters originate in distinct odd runs of the same
letter. Since input runs are maximal, at least one even run lies between
them, and the first such run has a different letter. It starts at the
peak vertex, crosses an edge other than its unique parent edge, and
returns. Its first edge therefore supplies the required extra unit of
root distance. These witness intervals occur in output-index order.
This is the schedule-specific step; normal-form uniqueness alone would
not establish it.

### Second inequality: distinct indices

For a maximizing output pair `p<r` with strict excess, `p=0` is impossible:
replacing it by `r` would strictly increase the objective. The symmetric
argument excludes `r=k`. Both neighbours of `p` are admissible first
indices, so maximality makes `p` a strict distance-to-start peak. Both
neighbours of `r` are admissible second indices, so `r` is a strict
distance-to-end peak. The two exposed witnesses occur in the correct
order, proving `M(w) >= M(Rw)+2`.

### Second inequality: coincident indices

For `p=r`, strict excess means this vertex is off the endpoint geodesic.
It is interior. Maximality with first index `p-1` and second index `p+1`
forces the incoming and outgoing neighbours to be closer to the start
and end, respectively. Off the geodesic, both parent edges coincide.
One exposed witness consequently raises both distances, and the same
input index can be used twice. This covers the case that would be missed
by assuming two distinct peaks.

### Clock conclusion and boundaries

The detection lemma correctly handles both off-geodesic excursions and
backwards travel on the endpoint geodesic. While the output is nonfixed,
the two inequalities force the exact decrement of `M` by two. At the
last nonfixed step, detection and the first inequality force excess one
or two; the ceiling therefore drops from one to zero. Length decrease
guarantees termination. The empty word, fixed words and unary alphabet
all satisfy the stated boundary formulas. Nonbijectivity holds when
`N>=2` since the empty word and `aa` have the same image; the `N<=1`
carriers are correctly degenerate identity maps.

**Assessment:** no outstanding temporal proof finding. This is a deductive
assessment, not an inference from the finite test.

## 3. Major inverse error and accepted correction

V1 claimed the off-diagonal gap numerator `1-(q-2)e`. For one intervening
even run between distinct target letters, there are `q-2` available
colours. But that wrong expression has zero coefficient of `e` after
expansion, immediately contradicting this count when `q>=3`.

At `q=3`, target `ab`, source length four, the seven actual predecessors
are `aaab`, `abbb`, `bbab`, `ccab`, `abaa`, `abcc`, `accb`. The V1
formula gives six. This is an independently checked hand counterexample,
not a claimed failed execution. The author found and disclosed the
algebra error before executing either proposed program.

The correct matrix entry is `1/((1-(q-1)e)(1+e))`. With
`o=z/(1-z^2)` and `e=z^2/(1-z^2)`, multiplying all run and gap weights gives

\[
G_y(z)=\frac{(q-1)^a z^{m+2a}(1-z^2)^{m-a}}
                  {(1-qz^2)^{m+1}}.
\]

Expansion gives exactly the corrected finite binomial sum in Section 3.
The empty target is independently `1/(1-qz^2)`. Unary boundaries also
work: target `a` has series `z/(1-z^2)`; longer unary targets have no
predecessors. **Finding F1: Major, repaired and independently accepted
at proof/formula level.** No author-code execution or independent
inverse-fibre execution is certified by this review.

PRE's exact substitution is not merely an analogy. Its retained weight
`z` becomes `o`; its deleted-run weight `L=z^2/(1-z)` becomes `e`.
The boundary gap, colour matrix `K=J-I`, diagonal/off-diagonal entries,
unique run decomposition and coefficient extraction stay unchanged.
Accordingly the corrected inverse has **zero independent new-mechanism
credit**, while remaining a complete, materially separate mathematical
conclusion from the exposed-peak time proof.

## 4. Stronger PFR collision: tree conjugacy

The author's `aaa` literal comparison does not rule out dynamical
conjugacy. The following is a verified collision, originally raised as a
question by root.

For even `q=2r`, compare the free group on `r` generators with the free
product of `q` copies of `C_2`. Their rooted Cayley graphs are both the
`q`-regular tree (for `q=2`, a two-sided line). Choose a rooted unlabelled
tree isomorphism. Each length-`n` word is uniquely its length-`n` walk
from the root; transport the walk through the isomorphism and read its
labels in the other tree. This gives a length-preserving word bijection,
simultaneously for all cutoffs `N`.

In the PFR walk, adjacent inverse letters are exactly an immediate
traversal and reversal of one edge. Partition the walk into maximal
consecutive segments traversing a single undirected edge. The actual old
left-to-right scan deletes disjoint successive pairs within each such
segment, leaving its parity-length walk. It cannot pair across a segment
boundary because the edges there differ. Fresh47's constant-letter runs
are precisely these same single-edge segments in its self-inverse
labelling. Hence one update commutes with the transported-walk bijection,
and so do all subsequent updates.

The archived rank-two PFR is therefore **exactly conjugate to the `q=4`
Fresh47 member**, not just similar on a few words. The argument relates
other even alphabets to their analogous free-group schedule; it does not
pretend the archive instantiated every rank. No odd-alphabet freshness
claim follows, since the shared tree/schedule mechanism remains occupied.

What the actual old source checked was the length budget and eventual
normal form. It did not supply the ordered two-endpoint maximum or
exposed-peak decrement. Thus the system/schedule collision is real, and
the new exact-clock theorem remains real progress on that schedule.
Neither fact cancels the other.

## 5. Bounded external owner check

Read Kari et al., [On parallel deletions applied to a word](https://www.numdam.org/item/ITA_1995__29_2_129_0.pdf),
definition on printed page 130 and unary discussion on 135–136. Its
set-valued operation permits different maximal deletion choices. For
`aaaa`, a central-pair deletion can leave `aa`, whereas Fresh47 empties
the run. This primary source is not an exact clock owner merely because
it says parallel deletion.

Three additional queries concerned parallel tree-word cancellation,
free-group reduction depth and simultaneous equal-pair rounds. A relevant
terminological hit led to Ascari's [Stallings-folding paper](https://arxiv.org/pdf/2207.04759),
Section 4.2 and Lemma 4.9: its parallel cancellation selects nested pairs
in an equation-path reduction diagram and collapses intervals. It is not
the maximal-single-edge parity pass. The HTML fetch timed out; the PDF
and its relevant text were successfully read. Neither primary passage
establishes the claimed clock. This is a bounded owner check, not an
exhaustive search, global novelty certificate, or external-release clearance.

## 6. Actual independent pressure test

Source review before execution is in `SOURCE_REVIEW.md`; full executed
source is `pressure.py`. It uses an independent `groupby` literal step
and tree distances by common prefixes, not the author's suffix reduction
implementation. The exact command there was actually executed once,
exited **0**, and returned no session. Full stdout is `stdout.txt`;
`stderr.txt` is actually zero bytes. No rerun or inverse run occurred.

| q | Maximum length | Source words | Counted checks | Nonvacuous second-inequality checks | Worst observed clock |
|---|---:|---:|---:|---:|---:|
| 1 | 8 | 9 | 66 | 0 | 1 |
| 2 | 8 | 511 | 4749 | 178 | 4 |
| 3 | 7 | 3280 | 27710 | 654 | 3 |

Total: 3800 words, 32525 counted checks, 832 nonvacuous checks of the
second implication, zero reported findings. The `checks` field excludes
the additional strict-length guards inside the orbit loop; it is not a
claim to count every executed predicate. Every orbit was run to its
fixed word. Ordinary trusted Python execution is disclosed; there is no
claim of installed-dependency closure, cross-language verification, or
source-only interpreter build. Finite agreement cannot prove any
all-parameter statement.

Observed SHA-256 keys:

```text
pressure.py 3484039c423e7b84d422669f82c7b9deb0dcf34f8f6fc5dcbeb4975ab7e0fda8
stdout.txt a2d93e8344454dc2735cfd6eb03bec0d881893dd06711bfdba5f051eecbe8848
stderr.txt e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
corrected author DESK at review 5871bf36d2f1743707fedbfade02734c45ec5a7608dda09fcdeb3ffab567e918
```

## 7. Value and remaining gate obligation

The inherited promotion list asks for a rigid deductive temporal theorem
and a separate inverse/enumeration conclusion, not two globally new
techniques. The corrected package supplies those mathematical components.
PRE's negative disposition expressly lacked a pointwise temporal result;
the present matching inequalities close a genuine difficulty, including
why greedy cancellation nesting is not the correct schedule clock.
The exact decrement is therefore more than relabelling its old generic
budget. A narrow note may honestly center that contribution and present
the inverse as a fully attributed baseline.

At the same time, the same criteria exclude conjugates as fresh systems.
The gate must therefore address the concrete PFR conjugacy above. It
must not pass merely on an `aaa` label comparison, nor describe this as
two newly discovered mechanisms. The justified recommendation is
**GO_NARROW_TO_GATE on theorem value, with occupied-system eligibility
explicitly unresolved; no admission or seat claim here**. If the batch
requires a previously unoccupied map without allowance for substantive
new theorems on it, this collision is the precise remaining obstacle.
It is not an invented rule that both axes must be novel.

The corrected inverse implementation remains an unexecuted author
proposal; normal paper-local verification, frozen evidence, manuscript
reviews and all later gates remain due if root elects to proceed. No
central file, author file, manuscript number or count was changed. No Git,
external upload or contact occurred. `HOLD_EXTERNAL` remains in force.
