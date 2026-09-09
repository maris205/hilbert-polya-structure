# AM1 analytic proof package and completed-classification pointer

## Claim

For $a\in\mathbb Z$, let
$$F_a(x,y)=\left(y,\frac{y(y+1)}2+a-x\right)\quad\text{on }\mathbb Q^2.$$
The frozen main question is to classify its entire periodic-point locus for
every $a$, with exact least periods, without a height or period cutoff.
The claims proved here are the explicitly numbered analytic reductions below.
The completed computer-assisted classification, exceptional table and exact
one-run receipt are in [CLASSIFICATION.md](CLASSIFICATION.md).

## Status

**Main classification: PROVABLE AS STATED, computer-assisted author proof
in CLASSIFICATION.md; nonauthor review pending.**
**Numbered reductions 1--8 below: PROVABLE AS STATED.**
The original all-$a$ question is preserved. The numbered analytic steps use
no mathematical program; the full classification subsequently used exactly
one proved finite-core certificate, whose dependency is explicitly linked.

## Assumptions and notation

All periodic points are ordinary rational points. If an orbit has period
$n\ge1$, write its cyclic scalar sequence as $(x_i)_{i\in\mathbb Z/n\mathbb Z}$.
It satisfies
$$x_{i-1}+x_{i+1}=\frac{x_i(x_i+1)}2+a.\tag{1}$$
Repeated scalar coordinates are allowed. The least state period is the least
period of the cyclic sequence, since two adjacent coordinates determine both
forward and backward iteration. For a prime $p$, normalize $|p|_p=p^{-1}$.
Write $H_c(u,v)=(v,v^2+c-u)$.

## Proof strategy and dependency map

1. Apply a maximum $p$-adic norm argument to (1), treating the prime two
   separately, to prove integrality.
2. Direct substitution proves the rational affine normal form; exact five-step
   substitution gives a separation witness against the deducted C412 theorem.
3. Sum (1) and use integrality to close only the upper parameter boundary.
4. Real maxima and differences give necessary restrictions, not exhaustion.
5. An elementary Newton-basis identity reduces general integer-valued
   quadratics to C412 or $F_a$. The now-complete full-class application,
   including its finite proof dependency, is in [CLASSIFICATION.md](CLASSIFICATION.md).

The first seven reductions were the initial screen. The coordinator then
requested checking a scaled-symbol argument within the same AM1 contract.
Step 8 gives that complete large-parameter reduction with a checked safe
threshold; it was established before the finite certificate was executed.
The comparison to C412 uses its actual existing classification. Its entire
six-symbol section and local-word proof were read before Step 8 was written.

## Proof

### 1. Every rational periodic point is integral

Fix an odd prime $p$ and put $M=\max_i|x_i|_p$. If $M>1$, choose $j$ with
$|x_j|_p=M$. Since $|1/2|_p=1$, the quadratic term in (1) has norm $M^2$,
the linear term has norm $M$, and $|a|_p\le1$. The unique largest term gives
right-hand norm $M^2$, whereas the left-hand norm is at most $M$, a
contradiction. Thus every $x_i$ is integral at every odd prime.

At $p=2$, if $M>1$ then the three terms $x_j^2/2$, $x_j/2$, $a$ have
norms $2M^2$, $2M$, and at most one. Their unique largest term has norm
$2M^2>M$, again contradicting (1). Hence every coordinate is integral at
two as well. A rational number integral at every prime is an integer.

Conversely, $t(t+1)/2$ is integral for every integer $t$, so both $F_a$ and
its inverse $(x,y)\mapsto(x(x+1)/2+a-y,x)$ preserve $\mathbb Z^2$.
This converse is invariance, not an assertion that every integer point is
periodic.

### 2. Rational normal form and a genuine period-five witness

Put $u_i=x_i/2+1/4$. From (1),
$$u_{i-1}+u_{i+1}
=\frac{x_i^2+x_i}{4}+\frac a2+\frac12
=u_i^2+\frac a2+\frac7{16}.$$
Thus $S(x,y)=(x/2+1/4,y/2+1/4)$ gives
$$S F_a S^{-1}=H_{a/2+7/16}.$$
Its image of the integral coordinate lattice is $1/4+(1/2)\mathbb Z$;
all corresponding numerators with denominator four are odd. The denominator
of $a/2+7/16=(8a+7)/16$ is exactly sixteen for every integer $a$.

For $a=0$, direct evaluation gives
$$(0,1)\mapsto(1,1)\mapsto(1,0)\mapsto(0,-1)
\mapsto(-1,0)\mapsto(0,1).$$
The five displayed states are distinct, so the least period is five.
Rational conjugacy preserves rationality and least periods; C412 admits only
least periods $1,2,3,4$. Consequently this particular $F_0$ cannot be rationally
conjugate to any member of C412. No assertion about all individual $a$ follows
from this one witness.

### 3. Exact upper-parameter boundary

Summing (1) around a period gives
$$\sum_i(x_i^2-3x_i+2a)=0,
\qquad
\sum_i\left(x_i-\frac32\right)^2
=n\left(\frac94-2a\right).\tag{2}$$
For $a\ge2$ the right-hand side is negative, impossible even over the reals.
For $a=1$, integrality from Step 1 makes each summand at least $1/4$, and
their average is exactly $1/4$. Thus every $x_i$ is either one or two.
If some $x_i=1$, equation (1) forces both neighbours to equal one;
iteration around the cycle makes every coordinate one. If no coordinate
is one, all are two. Both constant words satisfy (1). These give exactly
the fixed points $(1,1)$ and $(2,2)$.

### 4. A parameter-dependent real height bound

Let $M=\max_i|x_i|\ge0$ and choose a coordinate of that absolute value.
For a real number $t$ with $|t|=M$,
$$\left|\frac{t(t+1)}2\right|\ge\frac{M^2-M}{2}.$$
Its equation (1) gives
$$\frac{M^2-M}{2}-|a|\le2M,$$
and therefore
$$M\le\frac{5+\sqrt{25+8|a|}}2.\tag{3}$$
For each fixed $a$, this bounds the possible integral states and hence gives
a finite partial-permutation procedure without a period cutoff. Because the
bound grows with $|a|$, this is not an all-parameter orbit-family classification.

### 5. Extremal adjacent differences

Define $d_i=x_{i+1}-x_i$. Subtract the equation for $i$ from that for $i+1$:
$$d_{i-1}+d_{i+1}
=\frac{x_i+x_{i+1}+1}{2}\,d_i.\tag{4}$$
If the orbit is nonconstant, $D=\max_i|d_i|>0$. At an index with $|d_i|=D$,
the left-hand side of (4) has absolute value at most $2D$. Dividing by
$D/2$ yields
$$|x_i+x_{i+1}+1|\le4.\tag{5}$$
For a constant orbit the exact equation is instead $x^2-3x+2a=0$.
Equation (5) constrains only a maximal-difference edge; it does not assert
that every edge has bounded sum or that the whole cycle uses a fixed alphabet.
No propagation or exhaustive finite-core theorem is supplied here.

### 6. The scalar polynomial does not descend modulo two

The integers zero and two are congruent modulo two, but their triangular
values are zero and three. Consequently $t(t+1)/2$ does not define a function
on $\mathbb Z/2\mathbb Z$ through reduction of arbitrary integer lifts.
In particular $F_a(0,0)$ and $F_a(0,2)$ have second coordinates incongruent
modulo two although the input states are congruent. Integral-coefficient
finite-quotient permutation arguments cannot be applied without modification.

### 7. Conditional reduction of all integer-valued quadratics

Let $P\in\mathbb Q[t]$ have degree exactly two and take integer values on
every integer. Write $G_P(x,y)=(y,P(y)-x)$ and define
$$r=P(0),\qquad n=P(1)-P(0),\qquad
m=P(2)-2P(1)+P(0).$$
These are integers and $m\ne0$. The degree-two interpolation identity at
zero, one and two gives
$$P(t)=m\frac{t(t-1)}2+nt+r.\tag{6}$$
Conversely every such polynomial is integer-valued.

If $m=2k$ is even, then $k\ne0$ and $P(t)=kt^2+(n-k)t+r$.
The invertible rational scaling $(x,y)\mapsto(kx,ky)$ conjugates
$(y,P(y)-x)$ to the monic integral map
$$(u,v)\mapsto(v,v^2+(n-k)v+kr-u),$$
which belongs to C412.

If $m$ is odd, put $q=n-(m+1)/2\in\mathbb Z$ and define
$$T(x,y)=(mx+q,my+q),\qquad
A=mr+\frac{3q-q^2}{2}.$$
The product $q(3-q)$ is even, so $A\in\mathbb Z$. First scaling by $m$
makes the scalar polynomial $v^2/2+(n-m/2)v+mr$. Translating both coordinates
by $q$, with $n-m/2=q+1/2$, makes its linear coefficient $1/2$ and its
constant coefficient
$$mr+\frac{q^2}{2}-(q+1/2)q+2q
=mr+\frac{3q-q^2}{2}=A.$$
Thus $T\circ G_P\circ T^{-1}=F_A$. This rational affine conjugacy preserves
rational points and least native periods.

Therefore a complete solution of AM1, combined with C412, would provide the
all-rational-periodic classification for every integer-valued quadratic
polynomial Hénon map. Recover original coordinates using $x=(u-q)/m$ in
the odd case or $x=u/k$ in the even case. Those original coordinates need
not be integers; no contrary integrality claim is made.

### 8. Complete large-negative-parameter reduction

**Claim.** For every $a\le-146$, put $N=-2a-2$, choose the unique integer
$k\ge17$ with $k^2\le N\le k^2+2k$, and set
$$r=k+\frac12,\qquad s=N-k(k+1).$$
The entire rational periodic locus consists of cyclic rotations of the
words in the following table, taking precisely the row whose parameter
condition holds. If none holds, the periodic locus is empty.

| $s$ | Parameter $a$ | Original-coordinate words | Least periods |
| --- | --- | --- | --- |
| $-4$ | $1-k(k+1)/2$ | $(1-k)$, $(k+2)$ | $1,1$ |
| $0$ | $-1-k(k+1)/2$ | $(-k-1,-k-1,k,k)$ | $4$ |
| $4$ | $-3-k(k+1)/2$ | $(-k-3,k,k)$, $(k-2,-k-1,-k-1)$ | $3,3$ |
| $12$ | $-7-k(k+1)/2$ | $(-k-3,k-2)$ | $2$ |

The listed formulas are valid for every integer $k\ge0$ as existence
statements, with the same least periods and no within-row coincidences.
Exhaustion in this step is asserted only for $a\le-146$.

**8a. Annulus with an explicit threshold.** Step 1 reduces every rational
cycle to integral coordinates. In this step use the differently scaled
centered variable $v_i=x_i+1/2$ and constant $c=-2a-7/4=N+1/4$.
Equation (1) becomes
$$v_i^2-c=2(v_{i-1}+v_{i+1}).\tag{7}$$
With $R=\max_i|v_i|$, it gives
$$R\le2+\sqrt{c+4},\qquad |v_i^2-c|\le4R.\tag{8}$$
Indeed $R^2-c\le4R$, and the positive root of that quadratic is the
stated bound. The intervals $[k^2,k^2+2k]$ partition nonnegative integers;
$a\le-146$ gives $N\ge290$, hence $k\ge17$. Consequently
$$r\ge\frac{35}{2},\qquad -r+\frac12\le s\le r-\frac12,
\qquad c=r^2+s.$$
The upper bound in (8) is strictly less than $r+3$, because
$c+4\le r^2+r+7/2<(r+1)^2$ for $r>5/2$.
Both $R$ and $r$ are half-integers, so $R\le r+2$.
If $|v_i|\le r-3$ at an index, then
$$c-v_i^2\ge r^2-r+\frac12-(r-3)^2
=5r-\frac{17}{2}>4r+8\ge4R.$$
The strict inequality is valid for $r>33/2$, which the chosen threshold
satisfies. It contradicts (8). Thus
$$r-2\le |v_i|\le r+2.$$
There is a unique representation
$$v_i=\varepsilon_i r+\delta_i,\qquad
\varepsilon_i\in\{-1,1\},\quad\delta_i\in\{-2,-1,0,1,2\}.\tag{9}$$

**8b. Exact coefficient separation.** Substitution into (7) gives
$$2r(\varepsilon_{i-1}+\varepsilon_{i+1}-\varepsilon_i\delta_i)
=\delta_i^2-2\delta_{i-1}-2\delta_{i+1}-s.\tag{10}$$
The right-hand side has absolute value at most $12+|s|\le r+23/2<2r$.
The coefficient in parentheses on the left is an integer. It must vanish,
and the right-hand side must vanish too. Since the sum of the two neighbouring
signs is even, every $\delta_i$ is even. Put $\delta_i=2d_i$, with
$d_i\in\{-1,0,1\}$. The remaining equation makes $s$ divisible by four.
Writing $t=s/4$, we obtain exactly
$$\varepsilon_{i-1}+\varepsilon_{i+1}=2\varepsilon_i d_i,
\qquad d_{i-1}+d_{i+1}=d_i^2-t.\tag{11}$$
These are the same local equations already classified in
[C412's complete local-word proof](../../continuation_c409_c413_round2/papers/C412_integer_henon/sections/4_local_classification.tex).
That reduction and word classification are fully deducted ownership.

**8c. Exhaustion of the local words.** For completeness, the finite logical
classification of (11) is reproduced here without a period bound. At $d_i=1$
both neighbouring signs equal $\varepsilon_i$; at $d_i=-1$ both are opposite;
at $d_i=0$ the neighbouring signs are opposite to each other. Hence adjacent
offsets $1,-1$ are forbidden. The offset equation implies
$t\in\{-2,-1,0,1,2,3\}$.

- If $t=-2$, the neighbour sum $d_i^2+2\le2$ forces every $d_i=0$,
  which then gives the contradiction $0=2$.
- If $t=-1$, an offset $-1$ would have two neighbours $1$, forbidden.
  A zero must neighbour $1$, but that neighbour would need two neighbours
  $1$, contradicting the zero. Thus every offset is $1$ and all signs agree.
- If $t=0$, an offset $-1$ would neighbour $1$, forbidden. A zero has
  two zero neighbours; an offset $1$ requires a neighbouring zero, which
  cannot neighbour $1$. All offsets vanish and signs repeat
  $(-1,-1,1,1)$, up to cyclic rotation.
- If $t=1$, an offset $1$ needs two zero neighbours, but each such zero
  would require its other neighbour to be $-2$. The remaining offsets
  repeat $(-1,0,0)$: each $-1$ has two zero neighbours, and each zero has
  one zero neighbour and one $-1$ neighbour. Their signs repeat
  $(\varepsilon,-\varepsilon,-\varepsilon)$.
- If $t=2$, offset $1$ would neighbour $-1$, forbidden. A zero would
  have two $-1$ neighbours, whose sign rules make their signs equal,
  contradicting the sign rule at zero. All offsets $-1$ would then
  give $-2=-1$, impossible.
- If $t=3$, zero would need neighbours summing to $-3$, impossible.
  Each nonzero offset needs two $-1$ neighbours, so $1$ is forbidden.
  All offsets are $-1$ and signs alternate.

This gives $t=-1,0,1,3$ and precisely the table, after recovering
$x_i=\varepsilon_i r+2d_i-1/2$. In the four-period row the two values
are distinct and the pattern is not of period two. In each three-period
row the two values are distinct; the repeated value of the first row
is nonnegative and that of the second is negative when $k\ge0$, so the
two cycles never coincide. The two-period row has distinct entries with
difference $2k+1$. The two fixed coordinates differ by $2k+1$ as well.

**8d. Existence outside the large-parameter range.** The symbol patterns
in 8c satisfy (11) algebraically for arbitrary $r$, and substituting
$\delta_i=2d_i$, $s=4t$ into (10) makes both sides zero. Thus they
satisfy (7), and then (1), for every $r=k+1/2$, $k\ge0$, with
$$a=-\frac{k(k+1)}2-2t-1.$$
The distinctness checks just given prove their claimed least periods
for all $k\ge0$. This establishes existence uniformly, but does not
exclude additional small-parameter cycles.

## Corrections, missing assumptions and open risks

- Steps 1--7 are elementary reductions; Step 8 now closes every $a\le-146$
  by a scaled version of the old six-symbol mechanism. The initial concern
  that all negative parameters were unbounded is therefore resolved at this
  analytic gate. No independent-paper novelty follows from that resolution.
- The finite set $-145\le a\le0$ was the remaining gap at the analytic
  gate. After freezing the finite-core contract, one exact run exhausted
  that set plus the $a=1$ control; CLASSIFICATION.md records the closure.
- Any later finite certificate must follow a proved finite residual reduction;
  it cannot infer that reduction from samples.
- The old maximum/summation/symbol strategies, general height finiteness,
  rational affine normalization and integer-valued basis representation must
  remain deducted in contribution review. A complete new classification would
  still need a substantive-increment and nonauthor proof review.
