# Exclusion proofs and failed carrier, not a new theorem contract

2026-09-07 UTC. Author: `/root/thirty_third_finite_scout`.
All deductions here are author work. There was no independent mathematical
review, scientific code, pilot or canonical. No source proof is rewritten.

## Claim

Three bounded exclusions are checked:

1. Next-equal-letter distance feedback on its natural suffix-bounded word
   carrier is conjugate by position reversal to old PD on inversion words.
2. A cyclic-next-feasible-coordinate sweep is exactly known whirling. On
   bounded order-reversing poset labels, its fiberwise threshold-ideal
   adapter is the already published/preprinted rowmotion mechanism, not
   a separate new dynamics or substantial inverse theorem.
3. The proposed Jacobi version of cyclic-next-feasible updating on weakly
   increasing tuples is **not** a self-map of that carrier.

The third item is the sole new-rule proposal considered explicitly in this
lane. It fails before there is a valid finite autonomous candidate. Existing
PD, Foata/BWT/RSK and whirling are exclusion controls, not fresh literals.

## Status

`PROVABLE AS STATED` for the negative claims 1–3 below.
The attempted assertion that the Jacobi proposal defines an autonomous
endomorphism is false, so a full-carrier recurrent/inverse contract for it
is `NOT CURRENTLY JUSTIFIED`. No repair or weakened carrier is commissioned.
Overall disposition: `NO_FRESH_SLATE / NO_PROMOTION / ZERO_PILOTS`.

## Assumptions and notation

Words in the first item have positions numbered from zero. For $n\geq1$,
set

$$E_n=\{x\in\mathbb Z_{\geq0}^n:0\leq x_i\leq i\},\qquad
D_n=\{x\in\mathbb Z_{\geq0}^n:0\leq x_i\leq n-1-i\}.$$

On a word, $P(x)_i$ is the distance to its nearest equal letter strictly
to the left, or zero if no such letter exists. Define $Q(x)_i$ using the
nearest equal letter strictly to the right, with the same zero convention.
These are precise old-rule comparison formulas, not claims of new systems.
The word reversal $R$ is $(Rx)_i=x_{n-1-i}$.

For item 2, $\mathcal F\subseteq\{0,\ldots,q\}^n$ is any nonempty
finite word family and $q\geq0$. A local whirl $w_i$ fixes every coordinate
except $i$, cycles the $i$th coordinate through residues modulo $q+1$
at least once forward, and stops at the first resulting word in
$\mathcal F$. The starting word is eligible after one complete cycle, so
this terminates. A sweep is a fixed-order sequential composition.

For the poset comparison, $P$ is a finite poset, $q\geq1$, and
$\mathcal F_q(P)$ consists of functions $f:P\to\{0,\ldots,q\}$ with
$x\leq_P y\Longrightarrow f(x)\geq f(y)$. Write $x\lessdot y$ when
$y$ covers $x$. The product poset has coordinatewise order. All products
of maps use ordinary composition, with the rightmost map applied first.

The failed proposal uses

$$C_{n,q}=\{x\in\{0,\ldots,q\}^n:x_1\leq\cdots\leq x_n\},
\qquad n\geq1,\ q\geq1.$$

For each $i$, evaluate $w_i(x)$ against the **old** other coordinates and
put $J(x)_i=(w_i(x))_i$ simultaneously. The proposed codomain was
$C_{n,q}$, not the entire unconstrained cube.

## Proof strategy and dependency map

1. Reflect equal-letter positions to obtain an exact conjugacy, including
   the no-occurrence convention and the carrier endpoints.
2. On every fixed outside-coordinate fiber, a local whirl is the cyclic
   successor permutation of the feasible values. Then use the exact
   threshold ideal to inspect the poset specialization with the correct
   order-reversing bounds. This is a deduction of the known adapter for
   exclusion, not a new paper contribution.
3. Substitute one two-coordinate valid input into the simultaneous proposal.
   No search or finite census is needed to refute a universally quantified
   carrier-closure statement.

## Proof

### 1. The next-gap proposal is the old previous-gap rule reflected

For $x\in E_n$, every positive output $P(x)_i$ is at most $i$, so $P$
maps $E_n$ into itself. The corresponding distance bound proves $Q(D_n)
is contained in $D_n$. Reversal is a bijection $R:D_n\to E_n$.

Fix $x\in D_n$ and $i$. An equal letter at $j>i$ corresponds under $R$
to the equal letter at $n-1-j<n-1-i$. The nearest such $j$ becomes the
nearest previous equal letter, and the distance is unchanged:

$$j-i=(n-1-i)-(n-1-j).$$

If there is no such $j$, both maps return zero. Therefore
$RQ=PR$, including $n=1$. This is the exact old PD conjugacy.
It neither solves PD's unresolved global recurrent classification nor
supplies new proof credit.

If one first proposes $Q$ on all length-$n$ words over
$\{0,\ldots,n-1\}$, its first image is merely **contained** in $D_n$;
it is not claimed equal to $D_n$. All subsequent dynamics are the same
restricted rule above. No whole-carrier bijection between that larger
alphabet cube and $E_n$ is asserted. The extra first step cannot by itself
fill the missing temporal theorem or establish a material new mechanism.

### 2. Feasible-coordinate cycling has a generic singleton inverse

Fix all coordinates except $i$. List the values of coordinate $i$ for
which the completed word lies in $\mathcal F$ in their cyclic order. The
definition of $w_i$ advances to the next element of exactly this list.
Thus $w_i$ is a permutation of each such fiber and hence of
$\mathcal F$. Its inverse cycles backward to the previous feasible value.
For a sweep, invert the individual whirls in reverse sweep order.

Consequently every target has exactly one predecessor, every state is
recurrent, and there is no transient. These generic facts give neither
the exact period spectrum nor a substantial target-resolved second axis.
Joseph–Propp–Roby's Definitions 2.3 and 2.6 and Remark 2.8 are exactly
this operation and inverse (with residues represented as $1,\ldots,q+1$).
Renumbering the residue alphabet does not create a new map family.

For the poset specialization, define

$$\Phi(f)=\{(x,j):x\in P,\ 1\leq j\leq f(x)\}\subseteq P\times[q].$$

If $(y,j)$ belongs to this set and $(x,h)\leq(y,j)$, then
$h\leq j\leq f(y)\leq f(x)$, so $(x,h)$ belongs too. Thus $\Phi(f)$
is an order ideal. Conversely each fiber of an order ideal is an initial
segment; its height defines an order-reversing function. These constructions
are inverse bijections.

For one fixed $x\in P$, its feasible interval is

$$L_x=\max\bigl(\{f(y):x\lessdot y\}\cup\{0\}\bigr),\qquad
U_x=\min\bigl(\{f(y):y\lessdot x\}\cup\{q\}\bigr).$$

The cover inequalities and transitivity give exactly
$L_x\leq f(x)\leq U_x$. Since this interval consists of consecutive
integers, the local whirl increases $f(x)$ by one if $f(x)<U_x$ and
returns it to $L_x$ if $f(x)=U_x$.

Inspect the order-ideal toggles down the fiber at $x$, from level $q$
to level $1$. If $d=f(x)<U_x$, no level above $d+1$ can be added because
its immediate lower level is absent, whereas level $d+1$ can be added:
all lower-poset fibers have height at least $d+1$. The existing levels
below it are then not maximal and cannot be deleted. The new height is
$d+1$. If $d=U_x$, no higher level can be added. The toggles delete the
top levels successively until height $L_x$ is reached; deletion below
$L_x$ is forbidden by an upper-poset fiber. The new height is $L_x$.
This proves the exact local identity

$$\Phi w_x=\tau_{(x,1)}\tau_{(x,2)}\cdots\tau_{(x,q)}\Phi.$$

Given a linear extension $x_1,\ldots,x_p$ of $P$, the increasing-fiber
list $(x_1,1),\ldots,(x_1,q),(x_2,1),\ldots,(x_p,q)$ is a linear
extension of $P\times[q]$. The local identities therefore turn the
top-to-bottom whirl sweep into the corresponding top-to-bottom toggle
product. Plante–Roby's Theorem 2.12 identifies this as rowmotion via the
classical toggle characterization stated there as Proposition 1.5.
The present direct check proves the local adapter with coherent bounds;
it is not a new proof of every cited rowmotion theorem or a full source
dependency review. For an empty poset both sets contain one element and
the maps hold; for $q=0$ the same singleton statement holds separately.

### 3. Simultaneous cycling fails before any dynamics contract

Take $n=2$, $q=1$ and $x=(0,1)\in C_{2,1}$. Holding the second coordinate
at one, the next admissible first coordinate is one. Holding the first
coordinate at zero, the next admissible second coordinate modulo two is
zero. Thus

$$J(0,1)=(1,0)\notin C_{2,1}.$$

Each individual local update was admissible, but their simultaneous
combination is not. This refutes the proposed full-parameter self-map
claim by a single exact substitution. It is not a numerical experiment,
and no repaired scheduler, reordered output or enlarged carrier is adopted.

## Corrections or missing assumptions

Plante–Roby's acquired arXiv:2405.07984v2, printed page 7 in the proof of
Lemma 2.11, defines its lower bound from lower covers and upper bound from
upper covers while also asserting the order-reversing inequalities.
Under Definition 2.5 this reverses the roles needed for those bounds.
The exact PDF page was rendered and actually viewed; this is not merely
a text-extraction claim. For example, with $a<b$, $f(a)=1$, $f(b)=0$,
the printed lower-bound expression at $b$ gives one, contradicting
its displayed inequality that this bound is at most $f(b)$.

Step 2 explicitly uses upper covers for $L_x$ and lower covers for $U_x$,
and checks the resulting local correspondence directly. The acquired source
bytes remain unchanged. This notation defect is not asserted to refute
the source's theorem, and repairing a local convention for an exclusion
check earns no fresh owner credit or manuscript-review PASS.

## Open risks and stop

The exact full period structure of general whirling was not proved here;
the source's homomesy and its conjectures are not such a classification.
The whole source manuscripts and original historical scientific code were
not exhaustively reviewed. All local read boundaries are in the source
report. No attempt to rescue an old proof hold or thin bijection was made.
The sole fresh scheduler proposal failed its carrier before a pilot.
Stop without admission or an automatic fortieth lane.
