# Proof Package — known local rules as subtraction controls

## Claim

A. For the known cyclic binary majority rule, every recurrent state is
fixed or is one of the two alternating words on an even ring. Except for
those alternating words, the exact transient depth is half the longest
initial cyclic run of disagreement edges, rounded down. The sharp global
depth on a ring of length $n\geq1$ is $\lfloor(n-1)/2\rfloor$.

B. Finite-chain three-point median filtering is encoded injectively by
nested binary threshold layers, and evolves each layer by the rule in A.
Its pointwise depth is the maximum of the binary-layer depths and its
sharp global depth has the same formula. Its inverse choices are coupled:
multiplying independent binary-layer fibre counts is not a valid
full-target formula in general.

C. Simultaneous source reversal and simultaneous sink reversal on acyclic
orientations are conjugate by reversing every edge. The exact old
source-to-sink C6 and the already-written opposite-orientation SER inverse
therefore cannot be turned into a new entrance by changing orientation
conventions.

These are deductions about explicitly source-owned controls, not newly
fixed candidate maps, new scientific executions, or a new two-axis proposal.

## Status

PROVABLE AS STATED for A–C. NOT CURRENTLY JUSTIFIED for a new
source-subtracted two-axis contract, a binary-majority full-target fibre
extremum, or an evaluated finite-chain full-target inverse atlas.

## Assumptions

- All rings are labelled. Indices are modulo $n$ and repeated coordinates
  at $n=1,2$ are retained in the three-point rule.
- Median alphabets are the ordered set $\{0,\ldots,q-1\}$ with $q\geq2$.
  Updates are synchronous and use the old state.
- Graphs in C are finite and simple. Reversing sources or sinks is
  unambiguous because their nonisolated members are independent.
- No assertion here identifies cyclic majority with P132's nested-prefix
  rule or P80's cocktail-party graph rule. Those read originals have
  different dependency neighborhoods and serve only as internal boundaries.

## Notation

For a binary word $x\in\{0,1\}^{\mathbb Z/n\mathbb Z}$ write
$$
(Mx)_i=\operatorname{maj}(x_{i-1},x_i,x_{i+1}),\qquad
d_i=x_i\mathbin{\oplus}x_{i+1},
$$
where $\oplus$ is addition modulo two. If $d$ is not the all-one word, let
$L(d)$ be the largest length of a cyclic run of ones, with $L(0^n)=0$.
For even $n$, the all-one disagreement word corresponds exactly to the
two alternating binary words. The depth of a state means the least time
its orbit reaches a periodic state.

For a finite-chain word define
$$
(\mathcal M_qx)_i=\operatorname{med}(x_{i-1},x_i,x_{i+1}),\qquad
\theta_a(x)_i=\mathbf1_{\{x_i\geq a\}}\quad(1\leq a\leq q-1).
$$
For an orientation $O$, let $R(O)$ reverse all edges, and let $F_{\rm src}$
and $F_{\rm snk}$ reverse all edges incident with current sources and
current sinks respectively.

## Proof Strategy

Use disagreement edges for binary time evolution, injective threshold
encoding for median evolution, an explicit small counting obstruction to
independent inverse layers, and edgewise conjugation for orientations.
No general majority-network convergence theorem, statistical experiment,
or unread source theorem is required for these deductions.

## Dependency Map

1. The binary update identity in Step 1 gives zero persistence and
   erosion of disagreement runs.
2. Run erosion and the cyclic parity constraint give every recurrent
   state, exact depth and sharp witnesses.
3. The threshold/median equivalence gives the finite-chain assertions.
4. The three-site example disproves the independent inverse-product claim.
5. Reversal interchanges sources and sinks, giving C.
6. The complete generic ring-preimage proof read in fresh12 is used only
   in the subtraction discussion, not as a new theorem.

## Proof

### Step 1. Binary majority acts by eroding disagreement runs

A bit changes exactly when both neighbors differ from it. Hence
$$
(Mx)_i=x_i\oplus(d_{i-1}d_i).
$$
Subtracting the two neighboring new bits gives
$$
d'_i=d_i\oplus d_{i-1}d_i\oplus d_id_{i+1}
=d_i(1\oplus d_{i-1}\oplus d_{i+1}).
$$
In particular, a zero disagreement edge stays zero. If the word $d$ has
at least one zero, its maximal one-runs remain separated forever.

A run of length one has zeros on both sides, so its sole one survives.
In a run of length at least two, each endpoint sees one neighboring zero
and one neighboring one and disappears; every interior one sees two
neighboring ones and survives. A length-two run disappears completely.
Thus each even run of length $2k$ vanishes after exactly $k$ steps, while
each odd run of length $2k+1$ becomes a singleton after exactly $k$ steps.

### Step 2. Recurrence, exact clock and sharpness

The binary word is fixed exactly when $d_{i-1}d_i=0$ at every site.
For $d\neq1^n$, Step 1 therefore gives
$$
\operatorname{depth}(x)=\lfloor L(d)/2\rfloor.
$$
For strictness, at every earlier time a maximal run still has length at
least two, so some site changes. It cannot already be periodic: the number
of disagreement edges strictly decreases whenever such a run exists.
When no such run remains, the word is fixed.

If $d=1^n$, cyclic parity
$$
\bigoplus_{i=0}^{n-1}d_i=0
$$
forces $n$ even. The two possible binary words alternate and each site
changes at every step, giving exact period two. There is no other
nonfixed recurrent state by the preceding strict-decrease argument.

For every nonalternating word, $L(d)\leq n-1$, giving the global bound.
For $n=2k+1\geq3$, choose $d=1^{2k}0$; for $n=2k+2\geq4$, choose
$d=1^{2k}00$. Each has an even number of ones and hence lifts to a
cyclic binary word: choose $x_0=0$ and recursively set
$x_{i+1}=x_i\oplus d_i$, with cyclic closure supplied by that parity.
Its depth is $k=\lfloor(n-1)/2\rfloor$.

At $n=1$, the three entries of the local rule are the same bit and all
states are fixed. At $n=2$, the two neighbor entries are the other bit,
so $M(x_0,x_1)=(x_1,x_0)$; all states are periodic and have depth zero.
These agree with the stated formula.

### Step 3. Ordered median layers are a coupled lift

For any three ordered values and every threshold $a$, their median is at
least $a$ if and only if at least two of those values are at least $a$.
Consequently
$$
\theta_a(\mathcal M_qx)=M(\theta_a(x)).
$$
The entire threshold tuple is injective, since
$$
x_i=\sum_{a=1}^{q-1}\theta_a(x)_i.
$$
Its layers are nested:
$\theta_{a+1}(x)_i\leq\theta_a(x)_i$ for every $a,i$.

If a finite-chain state is periodic, every threshold layer is periodic.
Conversely, if every layer is periodic, Step 2 says all its layer periods
divide two, so injectivity gives $\mathcal M_q^2x=x$.
Applying this statement along the orbit proves
$$
\operatorname{depth}(x)=
\max_{1\leq a\leq q-1}\operatorname{depth}(\theta_a(x)).
$$
The binary result supplies the upper bound. Embedding a sharp binary word
using the two values $0$ and $q-1$ supplies equality, including $n=1,2$.
This is threshold transport of the binary clock, not a new mechanism
created by enlarging the alphabet.

### Step 4. Independent inverse layers overcount

Take $n=q=3$ and the finite-chain target $y=(1,1,1)$.
Each three-point neighborhood is the entire three-site ring.
Its threshold targets are $111$ and $000$. Under binary majority, each
has four predecessors, which would give $16$ independent layer pairs.

The actual finite-chain fibre has size $13$. Among all $27$ ternary
words, the output median is zero exactly when at least two entries are
zero, giving $1+3\cdot2=7$ words. Median two gives another disjoint
seven. The remaining $27-7-7=13$ have median one.

An explicit inadmissible layer pair is
$\theta_1=110$, $\theta_2=001$: it has the required binary outputs but
violates $\theta_2\leq\theta_1$ at the last coordinate. Thus the
independent product is not a valid full-target inverse formula.
These counts follow by finite case partition on paper; no pilot executed.

### Step 5. Source/sink convention changes do not create a new map

Reversal $R$ is an involution on the finite set of acyclic orientations.
The sources of $R(O)$ are exactly the sinks of $O$.
Reversal of all edges commutes with reversal of any specified edge set.
Therefore, edge by edge,
$$
F_{\rm src}=R\circ F_{\rm snk}\circ R.
$$
This includes isolates, whose incident edge sets are empty.
The acyclic carrier is preserved: after a source is flipped it is a sink,
so a new directed cycle cannot contain any flipped source, and the
remaining edges agree with the old acyclic orientation. The sink argument
follows by $R$.

The old C6 already fixes $F_{\rm src}$ literally. On the connected
$n\geq2$ carrier of the full SER inverse in
finite_orientation_residual_scout01/PROOF_PACKAGE.md, that inverse is
therefore transported by this exact conjugacy, not re-earned here.
This proves C and completes the stated controls. $\square$

## Corrections or Missing Assumptions

The cyclic boundary in A and B is essential. The Fitch–Coyle–Gallagher
median-filter source uses replicated endpoint values, not a ring; its
claims cannot silently be substituted for the cyclic assertions above.

The generic four-state pair-overlap trace formula in fresh12 gives the
binary-majority one-step count for each labelled cyclic target, including
the repeated-coordinate cases $n=1,2$. That proof is already available
for every local rule and supplies no separate residual mechanism here.
It neither proves a maximal target classification nor justifies multiplying
threshold-layer counts for ordered medians.

No binary-majority extremum, complete finite-chain inverse atlas, new
tree-specific source-reversal clock, or new CCA/GHM/FCA temporal theorem
is asserted in this packet.

## Open Risks

All current deductions are by this scout's author; they have no independent
review. Majority/median, source reversal and the excitable/inhibitory rules
are known source controls. A source access failure is not a novelty
certificate, and a direct source need not print this exact proof to consume
its primitive. No new literal or candidate entrance is counted.
HOLD_EXTERNAL.
