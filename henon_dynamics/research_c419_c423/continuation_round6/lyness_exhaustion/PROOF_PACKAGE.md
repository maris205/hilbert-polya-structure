# Proof package: exact six-step identity, no global exhaustion

## Claim and status

The original LY4 claim remains the necessary-and-sufficient classification
of every ordinary periodic sequence of nonzero integers satisfying
$$x_i x_{i+3}=a+x_{i+1}+x_{i+2},\qquad a\in\mathbb Z,$$
up to rotation and with exact native least periods.

**Status: NOT CURRENTLY JUSTIFIED.** The new section hypothesis S in
[FROZEN_ATTEMPT.md](FROZEN_ATTEMPT.md) is also unproved. The identities
and the local noncontraction example below are proved auxiliary facts;
they do not refute S or prove the full classification.

## Assumptions and inherited results

For the new difference work, assume $a\ne1$ and every coordinate avoids
$0,-1$. The already classified $-1$ locus and exceptional parameter
$a=1$ are not reopened. The following accepted results are reused:

- [Fifth-pass integral atlas](../../continuation_round5/lyness_closure/PROOF_PACKAGE.md):
  complete least periods at most six, complete $a=1$ integral locus,
  and exclusion of genuine period eight outside $a=1$.
- [Rational-period proof](../../continuation_round5/lyness_sources/PROOF_PACKAGE.md):
  the ordinary rational no-$0,-1$ bound, with its full singular,
  reducible and component-clock treatment and its independent review.
- The integral alternating invariants
  $$\kappa_i=\frac{(x_i+1)(x_{i+2}+1)}{x_{i+1}},\qquad
  \kappa_{i+2}=\kappa_i\in\mathbb Z\setminus\{0\}$$
  for genuine periods greater than two on this stratum, and the
  six-period sign law for $-x_i-1$.

These accepted proofs and finite checks are not rerun. The new argument
does not assume that a sign period is a coordinate period.

## Strategy, notation and dependency map

Put
$$D_i=x_{i+6}-x_i,\qquad E_i=x_{i+2}-x_i.$$
Hypothesis S would say that $D_i=0$ for all $i$ if the orbit also avoids
the section $\{1,-2\}$. The strategy was to obtain a cyclic descent
from the exact difference equations. Step 1 derives those equations.
Step 2 tests the proposed local contraction against an explicit
ordinary integer segment. Step 3 identifies the remaining global
implication. No external source theorem is needed for the new algebra.

## 1. Exact six-step difference identities

### 1.1 A factorization against the two-step difference

Every ordinary solution, even without integrality or periodicity,
satisfies
$$\boxed{
x_{i+2}x_{i+3}D_i
=(x_{i+1}+x_{i+2}+1)E_{i+2}.}\tag{1}
$$

**Proof.** Write seven successive entries as $(x,y,z,w,v,t,s)$.
The recurrence at positions zero and three gives
$$w(s-x)=v+t-y-z.$$
The recurrence at positions one and two gives
$$zt-yv=v-z,$$
and therefore $z(t-y)=(y+1)(v-z)$. Multiplying the first displayed
identity by $z$ and inserting the second gives
$$zw(s-x)=(y+z+1)(v-z),$$
which is exactly (1). No zero or plus-factor has been canceled.
$\square$

Since $D_i=E_i+E_{i+2}+E_{i+4}$, define
$$c_i=\frac{x_{i+1}+x_{i+2}+1}{x_{i+2}x_{i+3}}.$$
The equivalent exact equations are
$$D_i=c_iE_{i+2},\qquad
E_{i+4}+(1-c_i)E_{i+2}+E_i=0.\tag{2}$$
They compare different difference clocks. They are not an estimate
of $D_i$ by a smaller multiple of another six-step difference.

### 1.2 Midpoint equations do not supply that missing estimate

Let $M_i=(x_i+x_{i+6})/2$. Subtracting the original recurrence at
positions $i+6$ and $i$, and expanding symmetrically, gives
$$M_iD_{i+3}+M_{i+3}D_i=D_{i+1}+D_{i+2}.\tag{3}$$
Subtracting the two invariant equations gives
$$(M_i+1)D_{i+2}+(M_{i+2}+1)D_i
=\kappa_iD_{i+1}.\tag{4}$$
These are exact because in a product difference the two quadratic
terms in the increments cancel under the midpoint expansion.

Section avoidance and the inherited sign law make $x_i$ and $x_{i+6}$
belong to the same integer branch, so their midpoint does not cross
$0$ or $-1$. This observation does not make (3) or (4) a positive
maximum-principle system. For example, the direct triangle estimate
from (4) is only
$$|\kappa_i||D_{i+1}|
\le (|M_i+1|+|M_{i+2}+1|)\max_j|D_j|,$$
whose ratio on the right is not forced below one. The actual allowed
two-period word $(3,8)$, at $a=13$, has alternating invariants $2,27$;
the displayed ratio at an even position is $8/2=4$. Its actual
$D_i$ vanish, so this is not a counterexample to S. It demonstrates
that this particular triangle estimate supplies no uniform strict
contraction even on an allowed periodic input.

## 2. A stronger local obstruction with integer invariants

For every integer $m\ge1$, put $a=20m+1$. The eight-entry forward
segment
$$\begin{aligned}
(&12m+2,\ 4m+1,\ 2,\ 2,\ 5,\\
 &10m+4,\ 15m+5,\ 9m+2)
\end{aligned}\tag{5}$$
is an ordinary integer orbit segment, every entry is at least two,
and all defined alternating invariants are the integers $9$ and
$6m+3$.

To check every claimed recurrence equation, the five product-minus-sum
expressions in this segment are
$$\begin{aligned}
2(12m+2)-(4m+1)-2&=20m+1,\\
5(4m+1)-2-2&=20m+1,\\
2(10m+4)-2-5&=20m+1,\\
2(15m+5)-5-(10m+4)&=20m+1,\\
5(9m+2)-(10m+4)-(15m+5)&=20m+1.
\end{aligned}$$
The first two invariant values are
$$\frac{(12m+3)\cdot3}{4m+1}=9,
\qquad \frac{(4m+2)\cdot3}{2}=6m+3.$$
The parameter-free invariant identity propagates these values at
every position for which the required entries occur in (5).

At its first index, (2) has
$$E_2=5-2=3,\quad
D_0=(15m+5)-(12m+2)=3m+3,\quad c_0=m+1.$$
Thus $c_0$ is arbitrarily large, despite section avoidance, eight
ordinary integer entries, positive signs, and integer alternating
invariants. These local hypotheses cannot imply $|c_i|<1$ or a
uniform bound on $|c_i|$.

**This is not a periodic counterexample.** Its next coordinate would be
$$x_8=\frac{44m+8}{10m+4}
=4+\frac{2m-4}{5m+2}.$$
For positive integer $m$, this is integral only at $m=2$: at $m=1$
the correction is $-2/7$, and for $m>2$ it is strictly between zero
and one. At $m=2$, the following coordinate is
$x_9=(41+20+4)/35=13/7$, not an integer. Hence no member of (5)
extends to an ordinary all-integer forward orbit. This explicit
failure is why the segment refutes only the proposed local estimate,
not the global periodic hypothesis S or exhaustion E.

## 3. Exact remaining implication

The proposed global statement is still
$$\begin{gathered}
a\in\mathbb Z\setminus\{1\},\quad
(x_i)\text{ periodic},\quad x_i\in\mathbb Z\setminus\{0,-1,1,-2\},\\
x_i x_{i+3}=a+x_{i+1}+x_{i+2}
\quad\Longrightarrow\quad
c_iE_{i+2}=0\quad\text{for every }i.
\end{gathered}\tag{6}$$
By (1), the conclusion is equivalent to $D_i=0$ for every $i$.
Equations (2)–(4) have not yielded a cyclic sign, divisibility, or
energy argument proving (6). The local family (5) shows that a
pointwise contraction based only on the exhibited local conditions
cannot fill this gap. It does not rule out a genuinely global
arithmetic descent using all of periodicity.

Even proving (6) would leave the full classification of periodic
returns through $\{1,-2\}$. The section contains unbounded adjacent
integer data. No constant-height residual core, return atlas, or
necessary-and-sufficient higher-channel classification has been
established here. The accepted unbounded six-family must remain
removed in its entirety, not only through a bounded sample.

For precision, the accepted rational proof also leaves a finite clock
list, stronger than just the numerical bound 48. Its singular case has
$m\le4$; its genus-zero case has $m=r_0s$ with
$r_0\in\{1,2,3,4\}$ and $s\in\{1,2,3,4,6\}$; its genus-one case has
$m\in\{1,2,3,4,5,6,7,8,9,10,12\}$. Together with
$m=N/\gcd(N,2)$, the remaining native candidates outside the accepted
low-period and eight-period strata are contained in
$$\{7,9,10,12,14,16,18,20,24,32,36,48\}.\tag{7}$$
This is a direct unpacking of the already proved case bounds, not a
new torsion theorem or computation. It neither asserts existence at
these periods nor eliminates their integral points. A finite clock
list does not make the unsolved coefficient and height quantifiers
finite.

## Source access, execution and stopping boundary

No new external source query or retrieval was made in this attempt.
The local inherited proofs and their existing reviews supply the
classical/integrality/torsion dependencies. The identities, segment and
its failed extension above were derived by hand. No mathematical
program, census, old height-eight run, IR1 rerun or GPU/API job was
written, imported or executed. All author writes used `apply_patch`
inside the assigned directory.

The bounded attempt stops because the displayed global implication
and subsequent section-return classification remain unproved. This
is not a proof that no closing argument exists. Under the proof-writer
instruction, the status stays **NOT CURRENTLY JUSTIFIED** rather than
relabeling the local identities as a completed theorem contract.

No new admission, paper, C-number, formal evaluation, target Euler
factor, root number, automorphy, target-zero correspondence or
Hilbert–Pólya conclusion follows. `NO_BAD_EULER_OR_ROOT_NUMBER` remains
in force.
