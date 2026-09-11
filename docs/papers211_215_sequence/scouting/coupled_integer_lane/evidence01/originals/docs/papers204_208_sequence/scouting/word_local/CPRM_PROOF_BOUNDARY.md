# Cyclic least-positive remainders: elementary complete boundary

2026-09-06 UTC. Root author. **NO_PROMOTION / HOLD_EXTERNAL**.
The mathematical statements below are useful closed deductions, not an
admitted theorem contract. The original 30-box cutoff remains unchanged.

## Claim and status

Let $n\ge2$, $m\ge1$, and $X=\{1,\ldots,m\}^n$, with labelled cyclic
coordinates. Define
$$T(x)_i=1+((x_i-1)\bmod x_{i+1}).$$
Let $g(x)=\gcd(x_0,\ldots,x_{n-1})$. Then every orbit terminates at
$g(x)^n$; the only recurrent states are uniform words. Its entrance obeys
$$h(x)\le\sum_i\lfloor\log_2(x_i/g(x))\rfloor
\le n\lfloor\log_2(m/g(x))\rfloor.$$
This is **not** an asserted sharp global clock.

The quotient-word reconstruction below gives every inverse source set.
The unique target of largest fibre is $1^n$. Its size is evaluated by the
finite divisor-chain polynomial in Step 4. These claims are
**PROVABLE AS STATED**; priority, source clearance and substantive
independence of the two proposed axes are not conclusions of this proof.

## Assumptions, notation and dependency map

All remainders are least positive remainders; all entries are positive;
there is no zero completion. Put $q_i=\lfloor(x_i-1)/x_{i+1}\rfloor$.
The cyclic shift $S$ has $(Sx)_i=x_{i+1}$. Nonnegative quotient words
with a zero break the cyclic recurrence into finite directed chains.

1. The quotient matrix is unimodular because some quotient is zero.
2. Every strict scalar remainder drop at least halves its old entry.
3. Inverting the broken nonnegative recurrence gives all predecessors;
   decreasing its positive inhomogeneous terms to one gives an injection.
4. The uniform-one source graph is a reset vertex plus a descending
   divisor DAG; ordinary return-path enumeration evaluates its count.

## Proof

### Step 1. Gcd preservation and the terminal value

The inequalities $1\le T(x)_i\le\min(x_i,x_{i+1})$ prove invariance
and coordinatewise descent. A fixed point satisfies
$x_i\le x_{i+1}$ at every index and is therefore uniform. A nonfixed
state makes a strict decrease in at least one positive integer, so every
orbit eventually reaches a uniform word; no longer cycle is possible.

At a minimum coordinate $i$, $x_i\le x_{i+1}$ and hence $q_i=0$.
Writing $A=I-\operatorname{diag}(q)S$, we have $T(x)=Ax$. The cyclic
determinant is $\det A=1-\prod_iq_i=1$: in its permutation expansion
the only possible terms are the all-diagonal term and the complete
cyclic shift. This also holds for $n=2$ by direct determinant expansion.
Thus $A$ and $A^{-1}$ have integer entries, and each of $x,T(x)$ is an
integer linear combination of the other's entries. Their gcds coincide.
The final uniform value must consequently be $g(x)$.

### Step 2. Logarithmic potential bound, not a sharp clock

For positive integers $a,b$ with $a>b$, set
$r=1+((a-1)\bmod b)$. If $b\le a/2$, then $r\le b\le a/2$.
If $b>a/2$, the positive quotient is one and $r=a-b<a/2$.
Thus every strict update satisfies $r\le a/2$.

Scaling commutes with this positive-remainder rule: $T(gz)=gT(z)$.
Indeed $\lfloor(gz_i-1)/(gz_{i+1})\rfloor
=\lfloor(z_i-1)/z_{i+1}\rfloor$, by writing $z_i$ as a multiple
of $z_{i+1}$ plus its least positive remainder. Work with $z=x/g(x)$.
The nonnegative integer potential
$\sum_i\lfloor\log_2z_i\rfloor$ decreases by at least one at every
nonfixed step, because changed coordinates halve and none increases.
Its final value is zero. This proves exactly the stated bound.
Neither the initial census nor this inequality identifies every extremal
clock source or the sharp $H(n,m)$.

### Step 3. Complete inverse and strict global target comparison

Fix $b\in X$. Enumerate $q\in\{0,\ldots,m-1\}^n$ with at least
one zero. Solve the equations
$$x_i=b_i+q_ix_{i+1}.$$
There is a unique positive integer solution: start at any zero quotient
with $x_i=b_i$ and recur backwards around the cycle. The resulting
answer is independent of the chosen zero, as each chain ends at a zero
and has a unique backward solution. Retain the word precisely when
$x_i\le m$ and $b_i\le x_{i+1}$ for every $i$. These are necessary
and sufficient for $b_i$ to be the least positive remainder; its quotient
is then exactly $q_i$. Each true source has a unique such $q$, so this
procedure lists every source once, including empty fibres.

For a retained quotient word, replace every $b_i$ in the reconstruction
by 1, obtaining $u_i=1+q_iu_{i+1}$. Backward induction along each
chain gives $1\le u_i\le x_i\le m$. The remaining output condition
$1\le u_{i+1}$ is automatic, so $T(u)=1^n$. Distinct sources of the
fixed target $b$ have distinct quotient words, and these are recovered
from their new sources $u$. This is an injection of the entire fibre
over $b$ into that over $1^n$, not only a comparison of cardinalities.

If $b$ is nonuniform, its zero quotient word would reconstruct $x=b$,
which is not fixed. Thus that quotient is absent from its fibre but
present in the uniform-one fibre. The comparison is strict.
If $b=k^n$ with $k>1$, take the quotient word with one entry $m-1$
and all others zero. Its uniform-one source has that coordinate $m$
and all others 1; for $k^n$ it would instead have coordinate $km>m$.
Again it is a missing quotient. This proves uniqueness of $1^n$ for
$m\ge2$. For $m=1$ it is the sole target and hence the unique maximum.

### Step 4. Evaluated divisor-chain return polynomial

In the uniform-one fibre, an allowed neighboring source pair $(a,b)$
satisfies $b\mid(a-1)$. From vertex $1$ every next value $b\le m$
is allowed; from a vertex $a>1$ every next value is a positive divisor
of $a-1$, and is strictly smaller than $a$. Thus every closed source
walk visits 1; the remainder of the graph is acyclic.

Define integer polynomials recursively by
$$P_1(z)=1,\qquad
P_a(z)=z\sum_{b\mid a-1}P_b(z)\quad(2\le a\le m),\qquad
R_m(z)=z\sum_{a=1}^m P_a(z),\quad D_m(z)=1-R_m(z).$$
Every divisor on the right is less than $a$, so this is an explicit
finite evaluation without an unknown recurrence coefficient. $P_a$
counts paths from $a$ to their first visit to 1 by edge length; $R_m$
counts first-return walks from 1. The maximum fibre is
$$|T^{-1}(1^n)|=[z^n]\left(-\frac{zD_m'(z)}{D_m(z)}\right).$$
For completeness, let $B$ be the adjacency matrix of the edges from
vertices $a>1$ and set its row at 1 to zero. It is strictly lower
triangular, hence nilpotent. The full adjacency is $B+e_1\mathbf1^T$.
The determinant lemma and the finite geometric expansion give
$$\det(I-z(B+e_1\mathbf1^T))
=1-z\mathbf1^T(I-zB)^{-1}e_1=1-R_m(z).$$
The formal log-determinant identity then gives the displayed generating
function for the traces, which count labelled cyclic source words.
No quotient by rotations is taken. For example $D_2=1-z-z^2$ and
$D_3=1-z-2z^2-z^3$; these are evaluations, not extra theorem axes.

## Source/value boundary and disposition

The convergence uses ordinary simultaneous Euclidean reductions,
unimodularity and an integer logarithmic potential; it gives no sharp
all-parameter clock. Gcd-basin counts by Möbius inversion, if appended,
would be standard static gcd enumeration. The inverse is the complete
positive-affine broken-cycle recurrence, and its maximizer follows by
decreasing all inhomogeneous terms to their minimum. The return-polynomial
evaluation is ordinary renewal/DAG enumeration. These exact reductions
expose how little residual has been established beyond the tools.

The bounded searches in the intake and the later formulations
`gcd ring remainder distributed algorithm`, `Euclidean synchronous gcd`,
`positive remainder cyclic algorithm`, and `Euclidean algorithm cellular
integers` supplied no exact primary-body theorem. Search nonhits are not
clearance. P131's different continued-fraction queue does not remove
the Euclidean primitive deduction. A complete newest-literature or
independent source/value review has not occurred.

Root does **not** submit this elementary conjunction as a replacement
paper. Its mathematical boundary is retained as **NO_PROMOTION**; no
reserve, paper ID, sharp clock, accepted review or external clearance is
claimed. A future genuinely stronger result would need a new explicit
proof/value obligation, not more brute-force boxes of the same signal.
