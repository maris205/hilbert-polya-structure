# Fresh42 — second-missing graph response

2026-09-11 UTC. Author `/root/current_round_independent_scout`.
**ONE_LITERAL / NO_RESIDUAL / NO_PILOT_HANDOFF / HOLD_EXTERNAL.**
Author deductions only; no independent gate, admission or counter change.
The circular recency-rank transform assigned elsewhere was not investigated.

## Claim and status

One literal was fixed after bounded navigation: synchronous second-missing
colour on a finite undirected graph. Its first image is conjugate to the
already archived ordinary synchronous mex map. For matchings plus isolates,
the complete recurrence and every-target fibres are evaluated below, but
both reduce to independent scalar choices and two-coordinate exchange.

**PROVABLE AS STATED** for the reduction and matching formulas below.
**NOT CURRENTLY JUSTIFIED** for a source-subtracted two-axis contribution,
a sharp arbitrary-graph entrance clock, or an arbitrary-graph evaluated
fibre extremum. A second literal was not manufactured to fill the cap.

## Assumptions and notation

Let G=(V,E) be finite, simple and undirected, n=|V|, maximum degree Delta
(zero for the empty graph). Let q>=max(4,Delta+2). Colours are
{0,...,q-1}. For a finite set A of nonnegative integers, s2(A) is the
second smallest nonnegative integer absent from A. Define

$$T(c)(v)=s_2(\{c(u):u\in N(v)\}).$$

All updates use the old colouring. This is autonomous and total:
$1\le s_2(A)\le |A|+1\le\Delta+1<q$.
For n>0 it is noninjective: the distinct constant inputs zero and one
both produce two at every nonisolated vertex and one at every isolate.
The empty graph with no vertices has the unique empty state.

Write F for ordinary synchronous mex on palette {0,...,q-2}, and
J(d)=d+1 coordinatewise. For matching results, G is the disjoint union
of m labelled edges and s isolates, so n=2m+s. Depth means least time
to reach a periodic state.

## Strategy and dependencies

1. The first image contains only positive colours; subtract one there.
2. Use the actual archived GM proof only for its ordinary-mex period/deadline.
3. On degree-one components evaluate the scalar rule, then count independent
   sources; handle isolated and empty components separately.
4. Subtract the exact invariant-core adapter and scalar product mechanisms.

## Proof

### 1. Exact first-image adapter

For A contained in {1,...,q-1}, zero is its first missing nonnegative
integer. Its second missing integer is its least missing positive integer.
Consequently

$$s_2(A)=1+\operatorname{mex}(\{a-1:a\in A\}),\qquad TJ=JF.$$

Since T maps every input into J's range, with d=J^{-1}T(c),

$$T^{t+1}(c)=JF^t(d)\quad(t\ge0).$$

Every periodic T-state lies in J's range, because it is an image of its
preceding periodic state. The identity TJ=JF therefore gives a bijection
between periodic T-states and periodic F-states, preserving exact period.

The complete original GM_PROOF_PACKAGE.md was directly read (976254),
including its symmetric-edge exclusion and backwards decreasing-colour
witness. Under q-1>=max(3,Delta+1), its conclusion applies: F-periods
divide two and its entrance deadline is max(1,Delta). Thus T-periods
divide two and its entrance time is at most 1+max(1,Delta).
This last bound is not claimed sharp. It is entirely transported from GM.

### 2. Matching recurrence is completely evaluated

For a singleton neighbour colour a, put f(a)=s2({a}). Directly,

$$f(0)=f(1)=2,\qquad f(a)=1\quad(2\le a<q).$$

On an edge with endpoint colours (a,b), T sends it to (f(b),f(a)).
Its image is exactly {1,2}^2. On that image f exchanges one and two,
so T squares to the identity. Its fixed edge states are exactly (1,2)
and (2,1); its other two states form one two-cycle. An isolate always
maps to one. Independence of connected components now proves:

- the recurrent set has 4^m states, with isolates necessarily one;
- there are 2^m fixed states and (4^m-2^m)/2 two-cycles;
- depth is zero exactly when every nonisolated colour is in {1,2}
  and every isolated colour is one; every other state has depth one.

For n=0 there is one fixed state and depth zero. For n>0 there are
nonrecurrent states because q>=4, giving sharp maximum depth one.

### 3. Matching inverse and all equality cases

Let y be any labelled target. If an isolated target is not one or any
nonisolated target is outside {1,2}, its fibre is empty. Otherwise let
k count the nonisolated coordinates where y=2. Each target-one endpoint
allows q-2 source colours at its opposite endpoint, and each target-two
endpoint allows two source colours. Edge exchange is a permutation of
these independent source roles. Isolated sources are unrestricted. Hence

$$|T^{-1}(y)|=q^s2^k(q-2)^{2m-k}.$$

The maximum is $q^s\max(2,q-2)^{2m}$. At q=4 every target in the
recurrent set maximizes. At q>4 the unique maximizing target is all one
(including isolates). For m=0 both statements agree because that
recurrent set has one element. The empty product gives one when n=0.
This proves every matching statement, without enumeration. These formulas
are scalar-product counting, not a separate graph-specific inverse engine.

## Primary and archive subtraction

Geremias Polanco, *Decomposition of Beatty and Complementary Sequences*,
INTEGERS25 (2025), A104,
[publisher PDF](https://math.colgate.edu/~integers/z104/z104.pdf), was
directly read through Definition3 on printed p.4 and the following example.
Definition3 uses the (k+1)st missing **positive** integer; our definition
uses nonnegative integers. Shifting the whole set and output by one
identifies these scalar conventions. The source owns the skipped-mex
primitive, not this graph dynamics or the displayed matching formulas.
No Beatty-sequence theorem is imported. Actual PDF metadata gives publication
November25,2025; search-engine relative dates were not used.

The original `word_local/GM_GATE/CANDIDATE_GATE.md` was read completely
(1334b8). Its verdict is MATH_VALID / KILL_VALUE_FOR_THIS_BATCH: the exact
GM clock survived, while its inverse is a generic incidence-mex palette
envelope. This desk does not newly review that gate, run its verifier, or
claim that its ordinary-mex inverse is automatically the second-mex inverse
on the full initial palette. Only the invariant positive-colour restriction
has the proved conjugacy. General T-parent counting still requires presence
of all but one lower colour, so it is not evaluated here.

The narrow second-mex phrase search (e1fb6f) returned no local scouting
Markdown match under its stated excluded subdirectories. This is not an
exhaustive literal/primary novelty search. The exact adapter already closes
the temporal residual, so no larger search or pilot is warranted here.

## Navigation and boundaries

Odd-common-neighbour replacement was rejected before nomination: original
P132–P136 root SCOUT.md lines1–37 were read (6ea7ea), with that exact rule
in X09, separately from X10's toggle. It was not counted as a fresh literal.
Fresh29's complete GHM/rule172 negative desk (2c9ce8) and Fresh16's complete
majority/median proof (252afd) were read as exclusions, without reopening
their source-owned controls. Box-ball/cyclic-automaton filename navigation
produced no new nominated rule. Broad searches 561340 and 370aa2 were
truncated; their returned contexts are not an archive-exhaustion claim.

Project research skill enforced early subtraction; research-lit supplied
primary-body checking, and proof-writer separated proved restrictions from
unproved broad claims. Only this DESK.md was written. No pilot, science
kernel, import, verifier, host-runtime probe, build, child agent, Git action,
central edit, paper number, upload or external contact occurred.

**Handoff: one defined second-mex family, no surviving two-axis residual,
zero pilot requests.** No admission or closed-desk-count change is requested.
