# WCR: whole-constant-run relabelling — author deduction and negative disposition

2026-09-07 UTC. New proof authorship: `/root/thirty_third_finite_scout`.
This is a source-first scout proof, not independent review or admission.
No scientific program, sampled orbit, exhaustive pilot or canonical numerical
output was produced in this lane.

## Claim

For each integer $n\geq1$, let $X_n=\{1,\ldots,n\}^n$. For a word
$x\in X_n$, let $I_x(i)$ be the maximal constant interval containing its
position $i$. Define the literal autonomous map

$$F_n(x)_i=|I_x(i)|\qquad(1\leq i\leq n).$$

All positions are updated simultaneously from the old word. The entire
run length is used, not the suffix length, not length minus one, and not
a variable-length run-length encoding. The carrier includes every word;
there is no alphabet or endpoint repair. Run lengths lie in $[n]$, so the
map is closed on the stated finite carrier.

Let $\tau_F(x)=\min\{t\geq0:F_n^{t+1}(x)=F_n^t(x)\}$. We prove:

1. Every recurrent state is fixed. Fixed words are in bijection with
   positive compositions of $n$ having unequal adjacent parts.
2. For $n\geq2$, $\max_{x\in X_n}\tau_F(x)=1+\lfloor\log_2 n\rfloor$;
   for $n=1$, the maximum is zero.
3. For any target $y\in X_n$, write its maximal constant runs as
   $a_1^{L_1}\cdots a_s^{L_s}$, with $a_j\ne a_{j+1}$. Its one-step fibre
   is empty unless $a_j\mid L_j$ for every $j$. When all divisibilities
   hold, put $K(y)=\sum_j L_j/a_j$. Then

   $$|F_n^{-1}(y)|=n(n-1)^{K(y)-1}.$$

   For $n=1$ the expression uses $0^0=1$. The image has $2^{n-1}$ words.
   For $n\geq3$ the unique maximum-fibre target is $1^n$, with fibre
   $n(n-1)^{n-1}$. At $n=2$, the two image targets $11$ and $22$ both
   have fibre two; at $n=1$, the only fibre has size one.

## Status

PROVABLE AS STATED for the three displayed mathematical claims.
`KILL_VALUE_NO_SEPARATE_SECOND_RESIDUAL / NO_PROMOTION` for this batch.
The proof status is the author's deductive assessment, not a review PASS.

## Assumptions and notation

Only the integer restriction $n\geq1$ and the literal definition above are
assumed. A positive composition is an ordered sequence of positive integers
with prescribed sum; let $\mathcal C_n$ denote all such compositions of $n$.
For $\alpha=(b_1,\ldots,b_k)\in\mathcal C_n$, define

$$\Psi(\alpha)=b_1^{b_1}\cdots b_k^{b_k}\in X_n.$$

Equal adjacent parts are allowed in $\alpha$ and yield consecutive equal
letters in this expanded word. Let $R(x)$ be the sequence of maximal
constant-run lengths of $x$. Define $M$ on $\mathcal C_n$ by simultaneously
replacing each maximal group of $r$ consecutive equal parts $a$ by the single
part $ra$. A group with $r=1$ is unchanged. $M$ is an auxiliary factor map,
not a second scouted literal counted toward the lane's ceiling.

## Proof strategy and dependency map

First factor the word update through compositions. The merger process has
positive masses and preserves their left-to-right order. A merger at epoch
$t$ has a child created at epoch $t-1$; following these children produces a
causal chain whose mass at least doubles at every epoch. This gives the
logarithmic upper bound. Geometric compositions, with an explicit residual
placement case, give sharpness at every $n$.

The inverse has a different formal construction but no material residual:
target values force all old run lengths and boundaries, after which the
only freedom is a proper colouring of a path.

Dependencies:

1. Factor identities and injectivity of $\Psi$ imply the recurrent
   classification and translate merger time to word time.
2. Ordered positive-mass intervals imply the immediate-parent lemma.
3. That lemma implies doubling and the time upper bound; the geometric
   composition gives the matching lower bound, including its residual case.
4. Unique target segmentation gives the complete inverse and its extremum.
5. Fixed enumeration is the existing Carlitz-composition theorem; it is
   deducted, not imported as a new contribution. No source theorem is
   needed to justify claims 1–3 themselves.

## Proof

### Step 1. Exact factor and injective expansion

For every word $x$, the definition gives $F_n(x)=\Psi(R(x))$.
For every composition $\alpha$, each maximal group of $r$ equal parts $a$
in its expansion is one constant run of length $ra$. Groups of different
part values meet at unequal letters. Consequently

$$R\Psi=M,\qquad F_n\Psi=\Psi M.$$

The expansion $\Psi$ is injective. Indeed, from a constant run $a^L$ in an
expanded word, recover precisely $L/a$ consecutive parts equal to $a$.
Those parts are uniquely determined because each such part contributes
exactly $a$ letters and an unequal part would create an unequal letter.
This also supplies the divisibility condition used below.

Every composition occurs as $R(x)$: for $n\geq2$ colour its consecutive
parts alternately $1,2$ and repeat each colour by the relevant part length.
These are exactly the maximal runs. For $n=1$ the only composition is
realized by the word $1$. Therefore the image of $F_n$ is exactly
$\Psi(\mathcal C_n)$. Positive compositions correspond bijectively to
subsets of the $n-1$ internal cuts in a row of $n$ units, so there are
$2^{n-1}$ image words.

### Step 2. Fixed and recurrent states

Each nonfixed $M$ step strictly decreases the number of parts; a fixed
composition has no equal adjacent parts. Hence every composition eventually
becomes fixed, and the two factor identities show that every word eventually
becomes fixed. A recurrent word in a finite functional graph with this
property must itself be fixed, since a nontrivial cycle could not subsequently
reach a fixed word.

If $F_n(x)=x$, set $\alpha=R(x)$. Then $x=\Psi(\alpha)$ and
$\Psi(M\alpha)=\Psi(\alpha)$; injectivity gives $M\alpha=\alpha$.
Conversely, $M\alpha=\alpha$ implies $F_n\Psi(\alpha)=\Psi(\alpha)$.
Thus fixed words correspond exactly to compositions with unequal adjacent
parts, with no additional colour choices.

This is the classical Carlitz class. For example, its ordinary generating
function, including the empty composition in degree zero, is already

$$C(z)=\left(1-\sum_{a\geq1}\frac{z^a}{1+z^a}\right)^{-1}.$$

The body-read source is Heubach–Mansour, Theorem 4.1 and Example 4.2;
its proof and multivariate refinement 4.3 are inspected in this lane.
We claim no new fixed-count or weighted fixed-count theorem.

### Step 3. Causal merger doubling

View each initial part as an interval of consecutive unit positions of its
specified length. Later parts are unions of consecutive earlier intervals.
No interval vanishes or crosses another: each has positive mass and all
updates only unite adjacent intervals. Call a group of at least two parts
united by the transition $M^{t-1}\alpha\to M^t\alpha$ a merger at epoch
$t\geq1$. A part is created at its merger epoch; initial parts have creation
epoch zero, and parts in singleton groups retain their earlier creation epoch.

Immediate-parent lemma: every merger at epoch $t\geq2$ contains, among its
input parts, at least one part created at epoch $t-1$.

To prove the lemma, suppose all input parts were already present at epoch
$t-2$. They have not changed their intervals or masses by epoch $t-1$.
Two of them that are adjacent at epoch $t-1$ must also have been adjacent
at epoch $t-2$: an intervening positive interval could not disappear, and
could not be absorbed across either unchanged endpoint interval. All input
parts of the merger have the same mass, so these parts already formed an
adjacent equal-mass group at epoch $t-2$. The transition to epoch $t-1$
would have merged them, contradicting their unchanged presence. This proves
the lemma.

Every part created at epoch one has mass at least two. Inductively, a part
created at epoch $t\geq2$ has an input part created at epoch $t-1$, of mass
at least $2^{t-1}$. The merger has at least two equal-mass inputs, so its
output has mass at least $2^t$. Because total mass remains $n$, every merger
epoch satisfies $2^t\leq n$.

Let $T=\min\{t\geq0:M^{t+1}\alpha=M^t\alpha\}$. If a transition has no
mergers, its input is fixed and all subsequent transitions have no mergers.
Thus the nonfixed transitions are exactly epochs $1,\ldots,T$, and

$$T\leq\lfloor\log_2 n\rfloor.$$

For $t\geq1$ the factorization gives
$F_n^t(x)=\Psi(M^{t-1}R(x))$. It follows that

$$\tau_F(x)=
\begin{cases}
0,&F_n(x)=x,\\
1+\tau_M(R(x)),&F_n(x)\ne x.
\end{cases}$$

For the second case, if $T=0$ the first image is fixed but $x$ is not. If
$T\geq1$, each of $M^0R(x),\ldots,M^{T-1}R(x)$ is nonfixed, and injectivity
of $\Psi$ ensures each corresponding word image is nonfixed. The first
fixed image is exactly the $(T+1)$st. This proves the word upper bound.

### Step 4. All-size sharpness, including the residual placement

Fix $n\geq2$, let $k=\lfloor\log_2 n\rfloor\geq1$, and write
$n=2^k+r$ with $0\leq r<2^k$. The geometric composition

$$G_k=(1,1,2,4,\ldots,2^{k-1})$$

has total mass $2^k$. For $k=1$, this notation means $(1,1)$.
At epoch $j\in\{1,\ldots,k\}$ its growing initial part has mass $2^j$:
the two initial unit parts merge first, after which it successively meets
the next part of the same mass. Therefore its last merger is at epoch $k$.

If $r=0$, use $\alpha=G_k$. If $r>0$ and $r\ne2^{k-1}$, append the
single part $r$ to $G_k$. Initially it differs from its left neighbour,
which remains the part $2^{k-1}$ through epoch $k-1$. None of the
intermediate earlier geometric parts can meet $r$ across this positive
last part. At epoch $k$ the growing prefix merges with $2^{k-1}$ to
produce $2^k$, which differs from $r$. Thus the same last epoch $k$
survives.

If $r=2^{k-1}$, prepend $r$ to $G_k$. For $k=1$ the resulting composition
is $(1,1,1)$ and its last merger is at epoch one. For $k\geq2$, the prepended
part differs from the unit part at its right, and remains separated from
the later geometric parts by the growing prefix. The usual prefix merger
occurs at each epoch $1,\ldots,k-1$. At epoch $k-1$ the ordered composition
is precisely $(2^{k-1},2^{k-1},2^{k-1})$; all three parts merge at epoch
$k$. Thus again $\tau_M(\alpha)=k$.

Realize any selected $\alpha$ as run lengths of a word with alternating
run colours $1,2$. Since $M\alpha\ne\alpha$, this word is not fixed.
Step 3 yields $\tau_F(x)=k+1$. This matches the upper bound for every
$n\geq2$. At $n=1$, $X_1=\{1\}$ and the only word is fixed.

### Step 5. Unique inverse decoder and evaluated fibres

Consider a target run $a_j^{L_j}$. Every old maximal run contributing
letters to it must have length $a_j$, because $F_n$ places the old run
length in every one of its positions. Old runs contributing to this target
run occupy consecutive disjoint intervals and exhaust it. Therefore
$L_j$ must be divisible by $a_j$, and the source-run boundaries within
that target run are forced to lie every $a_j$ positions from its start.
A source run cannot cross a boundary between different target values,
because its entire image would be constant. Hence this segmentation is
necessary and unique on the full target.

When all divisibilities hold, it produces $K(y)$ prescribed source blocks.
Assign any colour in $[n]$ to the first block and any colour different
from the preceding block's colour to each later block. The prescribed
blocks then are exactly the source's maximal constant runs, so their
lengths produce $y$ under $F_n$. Conversely, every source must make these
choices, since equal adjacent colours would erase a required source-run
boundary. This is a bijection with proper $n$-colourings of a path on
$K(y)$ vertices, proving the fibre formula.

Always $K(y)=\sum_j L_j/a_j\leq\sum_j L_j=n$. Equality holds precisely
when every target value is one, namely $y=1^n$. For $n\geq3$ the factor
$n-1$ is greater than one, so the fibre expression is strictly increasing
in $K$, proving the unique extremum. At $n=2$ every nonempty fibre is two;
the unique compositions $(1,1)$ and $(2)$ expand to $11$ and $22$. The
case $n=1$ has already been checked. This completes claims 1–3. ∎

## Subtraction and disposition

The word carrier is erased after one step in favor of a positive ordered
mass-merger system. The temporal proof supplies a genuine all-size
logarithmic bound and all-size sharpness, but its mechanism is the
immediate-parent mass-doubling argument. The proposed static/inverse axis
is fully evaluated and reduces without residue to unique run segmentation
and elementary proper colouring of a path; the image is the ordinary
composition set and fixed enumeration is the existing Carlitz class.
This is not a claim that the exact temporal literal has been found in a
primary source. It is a value rejection because no materially independent
second theorem remains after these deductions.

The old ER word rule has a different carrier and uses suffix-run length
minus one; it is not falsely declared identical or conjugate to WCR. Its
original negative record nevertheless documents the occupied run/equality
plus elementary colouring/counting boundary. Equal-size partition merging
is also already an excluded motif; no ordered/unordered conjugacy is
asserted. Those historical facts are context, not proofs of WCR's claims.

## Corrections, missing assumptions and open risks

No theorem weakening or failed scientific assertion occurred: all claims
above were fixed at their first written proof stage, before any pilot.
The $r=2^{k-1}$ witness needs prepending, not the unqualified append rule;
the explicit case split prevents a premature merger. Source non-hits do
not establish novelty, and omitted proofs in the separate Horton extended
abstract are not treated as inspected complete proofs. No independent
author-free review was commissioned for this negatively disposed scout.
There is no reserve, paper number or authorization to open another lane.
