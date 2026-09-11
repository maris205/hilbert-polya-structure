# LC proof package: complete author deductions, no promotion

2026-09-07 UTC. Mathematical author: `/root/thirty_third_finite_scout`.
The source-desk child contributed no LC definition, lemma, proof or code.
No independent review and no scientific execution are claimed.

## Claim

Use exactly the carrier and simultaneous least-positive-collector map in
[LC_LITERAL.md](LC_LITERAL.md): $m\geq1$, $N\geq0$,
$X_{m,N}=\{x\in\mathbb Z_{\geq0}^m:\sum_i x_i=N\}$. For nonempty
support $S$, let $k=|S|$ and let $p$ minimize $(x_i,i)$ on $S$. The
collector receives one unit from each other positive bin, so

$$F(x)=x-\mathbf1_S+k e_p.$$

The zero vector is fixed. Every one-bin support is fixed.

We prove the following full-carrier statements, with no sharp global
entry-time assertion:

1. For $N>0$ and initial support size $q$, entry into the recurrent locus
   occurs by

   $$B(q,N)=(q-1)N+\frac{q(q-1)}2.$$

   Every recurrent state with support size $k$ has minimal period exactly
   $k$. For $N=0$ the only state is fixed.
2. Let $r_S(i)\in\{1,\ldots,k\}$ be the rank of label $i$ in increasing
   order within $S$. Set $U_i=kx_i+r_S(i)$ and order the support as
   $\pi_1,\ldots,\pi_k$ by increasing $(x_i,i)$, equivalently by increasing
   $U_i$. A positive-support state is recurrent exactly when

   $$\max_{i\in S}U_i-\min_{i\in S}U_i<k^2,
   \qquad x_{\pi_j}\geq j\quad(1\leq j\leq k).\tag{R}$$

   Consequently, for fixed $m\geq1,N>0$, the possible minimal periods are
   exactly the integers $k$ with $1\leq k\leq m$ and $k(k+1)/2\leq N$.
3. For every target $y\in X_{m,N}$, a nonredundant source decoder and its
   evaluated one-step fibre are given in Step 5 below. This includes all
   zero fibres, all disappearing support coordinates, all selector ties,
   $N=0$, and one-bin supports.

## Status

PROVABLE AS STATED for these mathematical claims, by the proofs below.
`KILL_VALUE_UNIFORM_HUNGER_AND_SELECTOR_ERASURE / NO_PROMOTION` for the
current paper batch. This is an author disposition, not a candidate-gate
or manuscript-review PASS. There is no proof of an all-target fibre maximum,
all-time inverse enumeration, sharp entry time, or global novelty.

## Assumptions and notation

Every parameter and update convention is fixed in `LC_LITERAL.md`.
Support coordinates retain their original labels; there is no relabelling
of the state after a zero appears. The temporary rank $r_S$ is used only
to encode the least-label tie rule numerically in a proof. $e_p$ is the
$p$th coordinate vector and $\mathbf1_S$ is the support indicator.
Lexicographic comparison of pairs first compares numerical load and then
the original integer label. A recurrent state returns to itself after a
positive number of steps; its least such number is its minimal period.

For integers $b\geq0$, use $\binom bh=0$ when $h<0$ or $h>b$.
Only integer binomial arguments occur below.

## Strategy and dependency map

1. Positivity and conservation imply support can only decrease. Thus a
   periodic orbit has one fixed support throughout.
2. Within any interval of constant support, adding elapsed time to all
   loads turns the update into incrementing the least of $k$ priorities by
   $k$. Encoding ties makes this a deterministic equal-step queue.
3. The queue enters a chamber of priority width less than $k^2$ after an
   explicitly bounded number of increments. In that chamber every label
   is selected exactly once in the next $k$ steps. Positivity of this
   round is exactly the second condition in (R).
4. Summing the bounded phases over strictly decreasing support sizes gives
   the full-carrier entry bound, not just a fixed-support claim.
5. Undo a proposed collector and distinguish surviving support from erased
   old unit bins. This gives all source sets and an explicit binomial sum.
6. The known uniform-kernel hunger-game identity and the elementary
   selector/erased-coordinate counting are deducted before assessing value.

## Proof

### Step 1. Carrier closure and monotone support

Every donating coordinate was a positive integer, so subtracting one never
creates a negative load. The collector retains positive load. The total
increment is $-(k-1)+(k-1)=0$, and initially zero coordinates remain zero.
Hence $F$ is autonomous on $X_{m,N}$ and
$\operatorname{supp}F(x)\subseteq\operatorname{supp}x$.
If a state returns to itself, this inclusion must be equality at every step
of its cycle. A one-bin support is fixed by the literal formula. With at
least two positive bins, at least one donor coordinate decreases, so such
a state cannot be fixed. For $N=0$ no other state besides zero exists.

### Step 2. Exact priority-queue representation on one support phase

Start a phase with support $S$ of size $k$ and positive loads $a_i$.
Let $t$ count steps since the beginning of this phase, and assume no
support loss has occurred through the times being considered. Put

$$z_i(t)=x_i(t)+t,\qquad
W_i(t)=kz_i(t)+r_S(i).$$

Adding the same $t$ to all loads does not change their order or tie rule.
Thus the selected coordinate has the least $W_i$. Its update increases
$z_i$ by $k$ and $W_i$ by $k^2$; all other $z_i$ and $W_i$ remain fixed.
Distinct label ranks make all $W_i$ distinct, so there is no numerical tie
in this encoded queue. This is an exact representation as long as the
support is unchanged, not a claim that one fixed queue describes the
entire trajectory after a support loss.

Queue chamber lemma. For distinct priorities with fixed residues
$r_S(i)$ modulo $k$, if

$$\max_i W_i-\min_i W_i<k^2,\tag{C}$$

then adding $k^2$ to the least priority moves it after every other priority.
The remaining priorities keep their order. The updated maximum is the old
minimum plus $k^2$, whereas the updated minimum is strictly larger than
the old minimum; therefore (C) remains true. Repeating proves that each
label is selected once in the next $k$ queue steps, in its initial priority
order, and that all priorities then increase by $k^2$.

To bound entrance to this chamber, let $A=\max_i a_i$ and

$$D=\sum_{i\in S}\left\lceil\frac{A-a_i}{k}\right\rceil.$$

In the unconstrained queue, while a priority value $z_i<A$ exists, only a
coordinate below $A$ can be selected. Each such selection decreases by one
the number of further increments needed for that coordinate to reach
$A$. Thus after exactly $D$ steps all $z_i$ lie in $[A,A+k-1]$:
coordinates originally at $A$ have not yet been selected, and a crossing
from below $A$ overshoots it by at most $k-1$. Consequently
$\max W_i-\min W_i\leq k(k-1)+(k-1)=k^2-1$, so (C) holds.

For a positive phase with total mass $N$ we have $A\leq N-k+1$. Using
$\lceil d/k\rceil\leq(d+k-1)/k$ for each integer $d\geq0$ gives

$$D\leq A-\frac Nk+k-1\leq N-\frac Nk\leq N-1,$$

because $N\geq k$. The queue comparison proves that an actual support
phase either loses a coordinate before this bound, or reaches (C) by
$D\leq N-1$ steps.

### Step 3. Full recurrent criterion and minimal periods

At a given state with support size $k$, subtracting the common quantity
$kt$ from $W_i(t)$ gives $U_i=kx_i+r_S(i)$, so priority width is exactly
the width in (R).

Suppose (R) holds. By the chamber lemma the first $k$ queue selections are
$\pi_1,\ldots,\pi_k$. Until its selection at step $j$, coordinate
$\pi_j$ has load $x_{\pi_j}-(j-1)$, which is positive by (R).
After its selection and through the end of this round, its load at time
$t\in\{j,\ldots,k\}$ is $x_{\pi_j}+k-t\geq x_{\pi_j}\geq1$.
These inequalities show that the entire round is a valid actual orbit
with no support loss. Every coordinate has donated/collected with net
increment zero after the round, so $F^k(x)=x$.

During a constant-support step, every coordinate changes by $-1$ modulo
$k$, including the selected coordinate because its increment is $k-1$.
Any return time is therefore divisible by $k$. Since $k$ is itself a
return time, the minimal period is exactly $k$. This includes $k=1$.

Conversely suppose $x$ is recurrent. Its support is constant along the
whole future orbit by Step 1. Step 2 shows that the queue enters (C), and
the chamber lemma shows that (C) is preserved afterwards. Returning to
$x$ at a sufficiently late multiple of its period implies (C) already
holds at $x$. The queue then selects $\pi_j$ at step $j$ in the next round.
Its actual load at that selection is positive, so
$x_{\pi_j}-(j-1)\geq1$. Thus $x_{\pi_j}\geq j$ for every $j$, proving
the necessity of both conditions in (R).

The period list follows without an experiment. Necessity comes from
$N=\sum_j x_{\pi_j}\geq\sum_{j=1}^k j=k(k+1)/2$ and $k\leq m$.
For sufficiency, take any $k\leq m$ with this mass bound and write

$$N=\frac{k(k+1)}2+kc+r,\qquad c\geq0,\quad0\leq r<k.$$

Use the first $k$ labels as support, with
$x_i=i+c+\mathbf1_{i\leq r}$, and set the others to zero. These loads
are nondecreasing in label order and satisfy $x_i\geq i$. Their range is
at most $k-1$, so their encoded priority width is at most $k^2-1$.
Criterion (R) therefore applies and the minimal period is $k$.
For $N=0$, the zero state has minimal period one separately.

### Step 4. Full-carrier entry bound across losses

Consider a phase of support size $k\geq2$. If there is no loss during its
first $D\leq N-1$ steps, it reaches (C). The unconstrained next $k$ queue
steps select every coordinate once. Either an actual support loss occurs
during those steps, or all are valid and the state at phase time $D$
returns to itself. Thus after at most $N+k-1$ steps from any phase start,
the orbit has either strictly smaller support or has reached recurrence.

The support sizes encountered before recurrence form a strictly decreasing
subsequence of $q,q-1,\ldots,2$; support one is already fixed. Summing the
nonnegative bounds for every possible such size gives

$$\tau(x)\leq\sum_{k=2}^{q}(N+k-1)
=(q-1)N+\frac{q(q-1)}2=B(q,N).$$

For $q=1$ the empty sum is zero. The case $N=0$ was handled in Step 1.
No extremal witness or sharpness of this bound is asserted.

### Step 5. Nonredundant every-target inverse and evaluated count

When $N=0$, zero has exactly one source. Now fix $N>0$ and target $y$.
Let $T=\{i:y_i>0\}$, let $\ell=|T|\geq1$, and for $p\in T$ put

$$b_p=|\{j\notin T:j>p\}|.$$

Define $C_p(y)\in\{0,1\}$ to be one exactly when

$$y_p\geq\ell\quad\hbox{and}\quad
(y_p-\ell,p)<_{\rm lex}(y_i,i)\quad\hbox{for every }i\in T\setminus\{p\}.$$

Then the complete fibre formula is

$$|F^{-1}(y)|=
\sum_{p\in T}\left[
C_p(y)+\mathbf1_{y_p\geq\ell+1}\binom{b_p}{y_p-\ell}
\right].\tag{I}$$

Here is a bijective decoder proving (I), including its zero cases.
A source collector must be some $p\in T$, because the collector never
vanishes. Any old support has the form $S=T\cup Z$, with
$Z\subseteq[m]\setminus T$. Once $p,Z$ are chosen, the only possible
source is

$$x_p=y_p-(\ell+|Z|)+1,\qquad
x_i=y_i+1\quad(i\in T\setminus\{p\}),\qquad
x_j=1\quad(j\in Z),$$

with all other coordinates zero. These formulas invert exactly the
collector increment and donor decrements; they also preserve total mass.

If $Z=\varnothing$, positivity of $x_p$ is $y_p\geq\ell$, and the
condition that $p$ is the least lexicographic source load is precisely
the displayed condition for $C_p(y)$, after subtracting one from both
compared loads. Thus this case contributes exactly $C_p(y)$ sources.
It includes a one-bin hold source when $\ell=1$.

If $Z\ne\varnothing$, an old donor has load one, so the selected positive
minimum must satisfy $x_p=1$. This forces $|Z|=y_p-\ell\geq1$.
Every surviving donor has source load at least two. Thus the only remaining
selector condition is that $p$ precedes every label in $Z$. Any subset
of the $b_p$ available zero labels greater than $p$, of exactly that forced
size, gives a valid source; and no other subset does. This yields the
binomial term in (I), including zero when too few labels are available.

Different choices cannot duplicate sources. The source itself determines
its unique selected collector by the literal tie rule and determines
$Z$ from the difference between its support and $T$. Conversely, all
admissible choices give the required target by substitution. This proves
the whole decoder and count; no source enumeration or finite census is used.
In particular a target is in the image exactly when the explicit
nonnegative sum (I) is positive. No global maximum of this sum is claimed.

## Exact known-mechanism subtraction

The source actually inspected is Li–Propp, *A Greedy Chip-firing Game*,
arXiv:2102.00346v4 (2022 author version; published RSA 62(3), 2023,
645–666). In its Section 2, a hunger vector chooses its greatest coordinate,
with the least-index tie rule, and adds the selected row of $P-I$.

On a fixed support of size $k$, take $P_{ij}=1/k$ and set

$$h_i=\frac{N/k-x_i}{k}.$$

This is an affine bijection from the mass-$N$ hyperplane on that support
to the zero-sum hunger hyperplane. It reverses load order while preserving
the least-label tie rule. The LC increment transforms exactly to

$$h'=h+\frac1k\mathbf1-e_p=h+(P-I)_p.$$

This is a literal uniform-kernel hunger-game identity for each fixed-support
phase. Positive support and subsequent coordinate loss restrict and splice
such phases; there is no asserted one-step conjugacy of the entire changing-
support carrier to one fixed Markov chain. The phase period argument above
is a direct proof of this elementary uniform case, not an invocation of
the source's general Conjecture 7.4. The paper proves boundedness/rational
eventual periodicity and the period of the zero hunger vector, but explicitly
leaves equality of all periods for a general kernel as a conjecture.

The proposed LC residual consists of a decreasing support, the positivity
test for one round of the equal-step queue, and the inverse selector with
erased old unit coordinates. Formula (I) is fully evaluated but requires
only choosing subsets of those coordinates and checking the deterministic
collector. It does not provide an additional nontransferring enumerative
engine. The two formally separate proofs therefore do not meet this batch's
material two-axis value requirement after the fixed-support primitive and
generic erasure/selector steps are deducted. Stop negatively before a pilot.

## Corrections or missing assumptions

No additional assumption or theorem weakening is needed for the claims
actually stated. The support-phase qualification is essential to the hunger
identity; deleting it would be a false full-carrier conjugacy claim. The
priority tie correction and the positivity inequalities in (R) are both
essential. Priority width alone would incorrectly call $(2,2,2)$ recurrent
when $m=3,N=6$: its literal first two steps are
$(2,2,2)\mapsto(4,1,1)\mapsto(3,3,0)$, so support decreases.
This is a symbolic substitution, not a pilot or a counterexample found by code.

## Open risks and stop

The literature search is bounded, and no claim that this exact absorbing-
support variant is globally new is made. A primary hungry-game adapter is
already sufficient for the stated value deduction. No all-target maximum,
all-time fibre law or sharper clock is silently inferred. All displayed
mathematics is author work and would require nonauthor verification before
admission; the negative disposition does not commission that gate. No
third literal, larger support experiment or automatic next lane is opened.
