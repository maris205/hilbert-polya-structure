# Proof Package: one full-branch ORR representation diagnostic

Author: `/root/thirty_third_finite_scout`, 2026-09-07 UTC.
This package contributes definitions and representation-level deductions,
not an independent review. The old ancestry lemma, inversion monotonicity,
clock bounds and counterexample trajectory retain their original authors.

## Claim

The unchanged target is: for every $n\ge1$ and every initial permutation
$x^{(0)}\in S_n$, activity at epoch $t\ge1$ implies
$$n\ge2t+1. \tag{T}$$
Epoch $t$ means the update from $x^{(t-1)}$ to $x^{(t)}$; an epoch is active
when it contains at least one nontrivial odd increasing-run reversal.
Equivalently, the desired maximum entrance time is
$$H_n\le\left\lfloor\frac{n-1}{2}\right\rfloor.$$
The inherited all-size lower family would then give equality. The empty
permutation has entrance time zero.

The sole diagnostic is to define a globally consistent complete active-run
dependency DAG retaining both activation parents, label histories and
individual inversion creation, and ask whether its overlaps yield (T).

## Status

Original target (T): **NOT CURRENTLY JUSTIFIED**.

The labelled DAG construction, exact epoch-depth statement, disjoint
inversion-pair tags, ancestor-support recurrence and slack identity below
are **PROVABLE AS STATED**. They do not imply a proved linear-depth bound.
No counterexample to (T) is claimed. No new temporal bound replaces it.

This is a closed representation diagnostic, not a third open-ended method
search. The global overlap certificate was not obtained. The complete
graph is defined from an actual orbit; its existence is not a way to know
the orbit's entrance time without that orbit and does not by itself provide
a closed-form clock.

## Assumptions

- The carrier is the whole $S_n$ with distinct labels $[n]=\{1,\ldots,n\}$
  in linear positions. The empty case is treated separately.
- Each old maximal strictly increasing run of odd length is reversed;
  even runs are held. All runs use the same old snapshot. Singletons do
  not count as active events because they do not change the word.
- No position, label set, parity stratum or family of initial states is
  removed. Endpoint-read footprints below are proof metadata, not a guard
  or an extra dynamical rule.
- The original proofs listed in `ORIGINAL_ROLES.json` were read completely.
  The root successor-run lemma and old counterexample are used with their
  precise scope; neither fresh labels nor disjoint ancestor supports is
  assumed. No finite census, program or external theorem is used here.

## Notation

Write $x^{(s)}=T^s(x^{(0)})$. An event $v=(t,I)$ consists of a maximal
increasing interval $I=[a,b]$ in $x^{(t-1)}$ with odd length at least three.
Its time is $t(v)=t$. Let $L(v)$ be its set of labels and $\ell(v)$ the
increasing ordered list of those labels in their old positions.

Its position-read footprint is
$$Q(v)=[\max(1,a-1),\min(n,b+1)]\cap\mathbb Z,$$
and its label-read footprint is
$$R(v)=\{x^{(t-1)}_i:i\in Q(v)\}.$$
Thus $L(v)\subseteq R(v)$; up to two outside labels are retained to
witness maximality. Store their positions and values, and the boundary
descent on each side that exists. Store the original position of every
label as part of the input metadata.

For an event $v$ and a read label $c\in R(v)$, let $h(v,c)$ be the latest
earlier active event whose label set contains $c$, if one exists. This is
the last **participation** event, not necessarily a displacement: a label
in the centre of an odd reversal can stay at the same position. If no such
event exists, the record points to that label's initial position instead.

Let $P_{\mathrm{act}}(v)$ be the immediate active parents in the old root
successor-run lemma. For $t(v)=1$ it is empty. For $t(v)\ge2$ it has
one or two members, all at time $t(v)-1$. Both are retained when there
are two. The old inactive central run and its labels are also recorded.

Define all event predecessors by
$$P(v)=P_{\mathrm{act}}(v)\cup
 \{h(v,c):c\in R(v),\ h(v,c)\text{ exists}\}. \tag{1}$$
An edge $w\to v$ keeps its activation/history type and, for history edges,
every read label responsible for it. Coincident edge endpoints are one
edge with all annotations, not a discarded parent. The resulting event
DAG is denoted $D(x^{(0)})$.

Finally, give each event its individual pair tags
$$K(v)=\{\{c,d\}:c,d\in L(v),\ c\ne d\}. \tag{2}$$
Each unordered pair is one tag, not two orientations. Its annotation says
that the smaller label preceded the larger before this event and follows
it after this event.

## Proof Strategy

First make the requested representation explicit, without identifying its
existence with a new time theorem. Activation edges retain branching at
each epoch. History edges retain participation through intervals during
which a label is held, including labels read only at a maximality boundary.
Pair tags record every inversion created, without collapsing them to a
scalar potential.

Then define the exact union of all read-label supports in an event's full
ancestry. Test the proposed support-depth implication by an exact slack
identity and the already-preserved seven-label orbit. Stop when the identity
requires a new overlap invariant that is not proved here.

## Dependency Map

1. Finite event set and disjoint pair tags use the literal simultaneous
   increasing-run reversal and permanence of an inverted label pair.
2. Nonempty immediate activation parent sets use the original root lemma;
   both of its cases are retained, not compressed to a chosen chain.
3. DAG acyclicity and exact event depth use strictly increasing times and
   the existence of an activation predecessor at the immediately prior time.
4. Ancestor support and its slack identity use finite set union only.
5. A linear depth conclusion would additionally need the unproved overlap/
   slack inequality in Step 5. Steps 1–4 do not assert that inequality.
6. The old seven-label orbit is used only as an exact diagnostic of this
   representation. No source example, larger box or numerical probe is added.

## Proof

### Step 1. Pair permanence, finite events and exact tags

For distinct labels $c<d$, their pair is inverted when $d$ occurs before
$c$. Consider one epoch. If both lie in one reversed interval, that old
interval is strictly increasing; the pair was not inverted and becomes
inverted. If they are in different old run intervals, those intervals
retain their left-to-right order; the relative order of the two labels
does not change. If they are in the same held run, neither moves. These
cases exhaust the pair's locations.

Therefore no inverted label pair can ever become noninverted. An active
event creates exactly the pairs in (2). Two distinct events at the same
epoch have disjoint label sets, since maximal runs are disjoint. Two
events at different epochs cannot share a pair tag, because its earlier
creation would make the two labels inverted and therefore unable to lie
together in a later increasing interval. Thus all $K(v)$ are disjoint.

Every active event creates at least one previously uncreated pair and
there are finitely many label pairs. Hence the number of events is finite.
If an epoch has no active event, the state is fixed and no later epoch
has one. This proves that the complete finite event set used to define
$D(x^{(0)})$ exists. No new quadratic or other entrance bound is extracted
from the pair count.

A useful representation-level consequence is
$$|L(v)\cap L(w)|\le1\qquad(v\ne w). \tag{3}$$
Indeed, two common labels would give a common pair tag. This is a
statement about the labels in individual event intervals; it is not a
bound on intersection of their accumulated ancestor supports.

### Step 2. Complete activation/history bookkeeping and acyclicity

The original local lemma applies to an event $v$ at time $t\ge2$ because
its run occurs in the successor $x^{(t-1)}$ of $x^{(t-2)}$. It says that
the run contains either one whole old even run plus one old active
endpoint, or one old singleton plus the two facing old active endpoints.
The corresponding old active events occur at epoch $t-1$. Those one or
two events are precisely $P_{\mathrm{act}}(v)$, and the central old
inactive run is unambiguous in the old maximal-run partition.

For completeness about the local lemma's use: an old active interval is
decreasing after reversal, so a new increasing run can meet it from outside
only at an endpoint. A held even/singleton run preserves every internal
ascent, so a maximal new increasing run meeting it must take it whole.
Two old held runs remain separated by a descent unless an active interval
lies between them; a new increasing run cannot cross that whole decreasing
interval. Thus there is at most one held central run. With no central run
there are at most two facing active endpoints, too short to be active.
Oddness then gives exactly the two stated parent cases. This restates
the inherited proof, not a stronger no-reuse conclusion.

For each $c\in R(v)$, earlier participation events containing $c$ have
distinct times, since a label belongs to at most one event at an epoch.
They form a finite set, so the latest one $h(v,c)$ is unique when it
exists. Participation history cannot be silently treated as new history
when $c$ reappears after an interval of held epochs.

All edges in (1) have $t(w)<t(v)$. No directed cycle can have strictly
increasing integer times along every edge; hence $D(x^{(0)})$ is acyclic.
All active events are included by definition. All activation parents are
included, including both sides of a merge. All run/read labels have their
last participation or initial-label record. The stored ordered run and
existing outside boundary values witness its increasing and maximal status.

This is the precise meaning of completeness here: a complete labelled
event/read-history record of the given orbit. It is **not** a claim that
the unlabelled incidence graph, parent counts, or pair tags alone certify
realizability by a permutation orbit. The ordered interval/maximality
conditions remain part of the record. Starting with the initial word and
the complete chronological event records recovers the orbit by the stated
reversals. Recognizing completeness from arbitrary proposed data would
still require checking those literal conditions; it is not a new clock.

### Step 3. Event depth is exactly epoch

Define $d(v)$ as the maximum number of event vertices on a directed path
ending at $v$, counting $v$ itself. Every edge raises time by at least
one, and the earliest possible event time is one, so
$$d(v)\le t(v).$$

If $t(v)=1$, there is no earlier event, hence $d(v)=1$. If $t(v)>1$,
Step 2 supplies an activation predecessor at time $t(v)-1$. Continue
choosing an activation predecessor at each earlier positive time. This
gives a path containing exactly one event at each time from one to
$t(v)$; therefore $d(v)\ge t(v)$. Consequently
$$d(v)=t(v). \tag{4}$$
The choice of one path proves this equality only. It is not used to count
two fresh labels per path edge; the complete branching graph remains the
object used for support below.

### Step 4. Exact full-ancestor support and slack identity

Let $A(v)$ contain $v$ and all of its event ancestors in $D(x^{(0)})$.
Define its complete read-label support by
$$S(v)=\bigcup_{w\in A(v)}R(w). \tag{5}$$
All these labels belong to $[n]$, so $|S(v)|\le n$. The definition and
incoming-edge decomposition of ancestors give the exact recurrence
$$S(v)=R(v)\cup\bigcup_{w\in P(v)}S(w). \tag{6}$$
No disjointness is asserted in (6). In particular the same old event and
its read footprint can reach $v$ along both branches without being counted
twice. Adding the label-history edges does not remove this overlap.

For an event at time $t$, set
$$\sigma(v)=|S(v)|-(2t+1). \tag{7}$$
This integer is a diagnostic **slack**, not an established nonnegative
invariant. For a root event at time one, $R(v)$ contains its at-least-three
run labels, so $\sigma(v)\ge0$ at the initial layer.

For $t\ge2$, choose any immediate activation parent
$p\in P_{\mathrm{act}}(v)$. It has time $t-1$ and $S(p)\subseteq S(v)$.
Define
$$\Delta(v;p)=|S(v)\setminus S(p)|.$$
Taking cardinalities of the inclusion and substituting (7) gives
$$\sigma(v)=\sigma(p)+\Delta(v;p)-2. \tag{8}$$
This identity uses full supports in the entire DAG, not supports along
the selected single chain.

The missing induction would require
$$\sigma(p)+\Delta(v;p)\ge2 \tag{M}$$
at every event of time at least two. It is not enough to know that both
terms are nonnegative: their sum can then only be bounded below by zero.
Conversely, a proved nonnegative-slack invariant would imply
$|S(v)|\ge2t(v)+1$, and then $n\ge2t(v)+1$. Thus it would prove (T).
Equation (8) identifies exactly the unproved implication; naming
$\sigma$ an invariant without proving (M) would be circular.

### Step 5. The existing orbit diagnoses the overlap issue exactly

Use only the old preserved orbit, with all maximal runs displayed:
$$
(2,5\mid1,4,7\mid3,6)
\longmapsto(2,5,7\mid4\mid1,3,6)
\longmapsto(7\mid5\mid2,4,6\mid3\mid1)
\longmapsto(7\mid5,6\mid4\mid2,3\mid1).
$$
Call its first event $a$, its two second-epoch events $b,c$ in left-to-right
order, and its third-epoch event $e$. These names are vertices of this
existing orbit, not new candidate aliases. Their run and read footprints
from the definitions are

| Event | Time | $L$ | $R$ |
|---|---:|---|---|
| $a$ | $1$ | $\{1,4,7\}$ | $\{1,3,4,5,7\}$ |
| $b$ | $2$ | $\{2,5,7\}$ | $\{2,4,5,7\}$ |
| $c$ | $2$ | $\{1,3,6\}$ | $\{1,3,4,6\}$ |
| $e$ | $3$ | $\{2,4,6\}$ | $\{2,3,4,5,6\}$ |

For example the read footprint of $a$ includes the adjacent outside
labels $5$ and $3$, while the event $b$ touches the left endpoint of the
whole word and has only the right outside label $4$. These facts follow
from the displayed words and are not produced by a program.

The activation edges are $a\to b$, $a\to c$, $b\to e$, and $c\to e$.
The history edges add $a\to e$ because the read label $4$ last
participated in $a$; the other relevant history edges coincide with
activation edges. Recurrence (6) gives
$$S(a)=\{1,3,4,5,7\},$$
$$S(b)=\{1,2,3,4,5,7\},\qquad
S(c)=\{1,3,4,5,6,7\},$$
$$S(e)=\{1,2,3,4,5,6,7\}.$$
Although $L(b)$ and $L(c)$ are disjoint, their full supports intersect in
the five-element set $S(a)$. Consequently
$$|S(a)|,|S(b)|,|S(e)|=5,6,7,$$
and the respective slacks are $2,1,0$. In particular the full-support
increments along $a\to b\to e$ are each one, not two. The accumulated
slack pays for them in this orbit, and (M) holds with equality at both
steps. This verifies neither (M) at arbitrary sizes nor a global
nonnegative-slack theorem.

The example is consistent with the desired $H_7=3$. It refutes only a
strict two-new-label interpretation of the **new full read-history
support**, not (T). The old single-chain no-reuse failure is preserved;
it is not used again as a proposed proof.

### Step 6. Exact stopping point

The full representation removes the bookkeeping ambiguity about omitted
parents, labels that return after held epochs, and individual inversions.
It does not establish (M). Pair tags do not repeat, but that fact controls
the reuse of label **pairs in individual active intervals**. It gives no
proved comparison here between $\Delta(v;p)$ and the accumulated overlap
of the full read-supports in (6). Statement (3) likewise does not bound
$S(b)\cap S(c)$, as Step 5 demonstrates.

To turn this particular representation into the proposed certificate, one
would have to derive (M), or another genuinely informative rank inequality
implying nonnegative slack, from the ordered run/maximality constraints
and the labelled history. No such derivation is available in this bounded
diagnostic. Writing an injection of $2t+1$ abstract slots into $S(v)$
without constructing it would only restate the missing support bound.

There is therefore no proved depth certificate and no sharp-clock
improvement. Stop here: no second representation, new auxiliary dynamics,
larger pilot, extra source search or another quadratic-potential bound is
started. This completes the requested one diagnostic as a blockage report.

## Corrections or Missing Assumptions

No additional restriction on the full carrier is imposed. Neither
nonnegative slack, disjoint ancestor supports nor a fresh-label charge is
an assumption of the literal system. They cannot be silently inserted to
declare (T) proved. The support claim $|S(v)|\ge2t(v)+1$ is a sufficient
certificate for (T), not a proved fact and not asserted equivalent to (T)
for this particular support: the ambient carrier may contain labels not
in $S(v)$.

The ordered event/read record contains more than its unlabelled DAG or
linear event hypergraph. Discarding the literal order constraints and then
proving a property for arbitrary abstract incidence data would change the
problem; no such replacement is made.

## Open Risks

- The original sharp upper bound is still unproved, and no counterexample
  to it is established.
- The support/slack diagnostic is precisely defined but lacks the required
  global monotonicity/overlap lemma. Definability is not a certificate.
- Pairwise intersection of event label sets is not intersection control
  for all ancestor/read supports.
- The representation may retain much of an orbit's information. It is not
  a compact normal form or a new independently valuable temporal axis.
- No fresh source/value clearance or nonauthor review has occurred. The
  source/value gates would remain necessary even after a successful clock
  proof. The current package closes **NO_PROMOTION**.
