# Fixed-dividend remainder: exact negative-control boundary

Author: /root/round211_finite_matching_scout, 2026-09-09 UTC.
SOURCE/PROOF ONLY. One classical-literal desk control; no fresh nomination.
OWNER_AMBER / HOLD_EXTERNAL.

## Claim

Fix an integer $N\geq1$. On the fixed finite carrier
$X_N=\{0,1,\ldots,N\}$ define

$$
P_N(a)=
\begin{cases}
0,&a=0,\\
N-a\lfloor N/a\rfloor,&1\leq a\leq N.
\end{cases}
$$

Then:

1. Every state reaches the unique fixed point $0$, and its entrance time
   $h_N(a)$ is at most $a$. No nontrivial recurrent cycle exists.
2. The exact one-step image is
   $$P_N(X_N)=\{0,1,\ldots,\lceil N/2\rceil-1\}.$$
3. The complete one-step predecessor sets are
   $$P_N^{-1}(0)=\{0\}\cup\{a\geq1:a\mid N\},$$
   $$P_N^{-1}(r)=\{a\geq1:a\mid(N-r),\ a>r\}
     \quad(1\leq r<N),$$
   and $P_N^{-1}(N)=\varnothing$.
4. The depths are unbounded across the family: for every integer $m\geq3$,
   with $N=m!-1$, the source $m\in X_N$ has $h_N(m)=m$.

These are elementary boundaries for the classical Pierce remainder map.
They are not a sharp formula for the global clock or a new inverse theorem.

## Status

PROVABLE AS STATED for claims 1–4.
A sharp all-$N$ maximum-clock formula, all time layers, and an independently
evaluated global fibre-extremum law are NOT CURRENTLY JUSTIFIED by this desk.
Research disposition: NO_PROMOTION / NO_RESERVE.

## Assumptions and notation

$N$ is fixed throughout an orbit. The old scalar value $a$ is the next
divisor; the dividend is never replaced by $a$.
Remainders are ordinary nonnegative remainders, not least-positive ones.
The absorbing value at zero completes the published terminating algorithm
to a total finite map; it introduces no reset to a positive state.
There are no registers, hidden phases, mutable preference/endpoint data,
cyclic coordinate shifts, carries, sorting, gcd normalization or clipping.

Let $D(t)$ be the number of positive divisors of a positive integer $t$.
Let $[E]$ denote $1$ when statement $E$ is true and $0$ otherwise.
The entrance time $h_N(a)$ counts updates until the first occurrence of zero;
$h_N(0)=0$.

## Strategy and dependency map

1. Euclidean division gives $0\leq P_N(a)<a$ and therefore termination.
2. Combining a remainder inequality with its division equation bounds the
   whole image; the quotient-one branch realizes every target in that bound.
3. The same division equation supplies a bijection between predecessors
   and sufficiently large divisors of $N-r$.
4. A factorial congruence constructs an exact long chain.

All mathematical steps below are elementary author deductions, not a
scientific execution or an independent review. Published sources are
used for literal and proof-mechanism subtraction, not as substitutes for
missing deductions.

## Proof

### Step 1. Finite closure, recurrence and normalization to Pierce

For every positive $a\leq N$, Euclidean division gives a unique integer
$q=\lfloor N/a\rfloor\geq1$ and a unique remainder
$r=N-qa$ with $0\leq r<a$. Thus $P_N$ maps $X_N$ to itself, and
every positive state strictly decreases. An orbit beginning at $a$ can
contain at most $a$ positive states before reaching zero, proving
$h_N(a)\leq a$. A positive state cannot be fixed or lie on any directed
cycle because values strictly decrease along positive steps. Zero is
fixed, so it is the whole recurrent set.

For completeness, let
$G_N=\{a/N:a\in X_N\}$ and $\phi_N(a)=a/N$.
Define the Pierce transformation on this grid by
$F(0)=0$ and $F(x)=1-x\lfloor1/x\rfloor$ for $x>0$.
Then for each positive $a$,

$$
F(\phi_N(a))
=1-\frac aN\left\lfloor\frac Na\right\rfloor
=\frac{P_N(a)}N
=\phi_N(P_N(a)).
$$

The identity also holds at zero. Since $\phi_N$ is a bijection onto $G_N$,
this is a time-preserving conjugacy of the full finite maps.
It is not the two-register Euclidean update with a changing dividend.
The published fixed-dividend Pierce algorithm is already the literal under
study; the normalization earns no new mechanism credit.

### Step 2. Complete image

Suppose $r=P_N(a)$ with $a>0$. We have $N=qa+r$,
$q\geq1$, and $a\geq r+1$. Therefore

$$
N\geq a+r\geq2r+1,
$$

so $r\leq\lfloor(N-1)/2\rfloor=\lceil N/2\rceil-1$.
The source zero also maps into this range.

Conversely, take any integer $0\leq r\leq\lfloor(N-1)/2\rfloor$.
Put $a=N-r$. Then $1\leq a\leq N$ and $r<a$.
The equation $N=1\cdot a+r$ is its valid Euclidean division,
so $P_N(a)=r$. This proves the exact image and its size
$|P_N(X_N)|=\lceil N/2\rceil$.

### Step 3. Full predecessor bijection and explicit count

For target zero, every positive predecessor is exactly a positive divisor
of $N$. Such divisors are automatically at most $N$.
The absorbing source zero is an additional predecessor, giving
$|P_N^{-1}(0)|=1+D(N)$.

Now let $1\leq r<N$. If $P_N(a)=r$, then $a>r$ and
$N-r=qa$, so $a$ divides $N-r$.
Conversely, let $a$ be a positive divisor of $N-r$ with $a>r$.
Since $N-r>0$, one has $a\leq N-r\leq N$.
The positive integer $q=(N-r)/a$ gives
$N=qa+r$ with $0<r<a$. Thus this is the Euclidean division by $a$,
and $P_N(a)=r$. Every divisor specifies exactly one source.

Consequently the fibre counts are

$$
|P_N^{-1}(r)|=
\begin{cases}
1+D(N),&r=0,\\
D(N-r)-\displaystyle\sum_{a=1}^{r}[a\mid N-r],&1\leq r<N,\\
0,&r=N.
\end{cases}
$$

The middle expression is a finite explicit arithmetic count, with no
unknown dynamical coefficient. Empty fibres beyond the image are included:
if $2r\geq N$, every positive divisor of $N-r$ is at most $r$.

The quotient-one predecessor is $a=N-r$ when $2r<N$.
All other predecessors have quotient at least two and are proper divisors
of $N-r$. This is precisely the elementary proper-divisor mechanism
already made explicit in the published source noted below.
No independent inverse-extremum theorem follows from merely writing this
count.

### Step 4. An elementary exact long-chain family

Let $m\geq3$ and $N=m!-1$. Then $N\geq m$, so $m$ belongs to
the specified carrier. For every integer $2\leq j\leq m$,
$j$ divides $m!$ and hence $N\equiv-1\pmod j$.
Its nonnegative remainder modulo $j$ is exactly $j-1$.
Also $P_N(1)=0$. Therefore the exact orbit is

$$
m\longmapsto m-1\longmapsto\cdots\longmapsto1\longmapsto0,
$$

which has entrance time $m$. This proves unbounded depth as $N$ grows.
It is a congruence construction, not a sharp estimate for the maximum over
a fixed carrier. It is not asserted new in the Pierce literature.
Claims 1–4 follow. $\square$

## Boundary checks and a warning about the largest fibre

For $N=1$, $X_1=\{0,1\}$ and both states map to zero.
The image has size one, its sole fibre has size two, and
$h_1(0)=0,\ h_1(1)=1$, agreeing with all applicable formulas.
The factorial family explicitly starts at $m=3$ to ensure its source lies
inside the chosen carrier.

Zero is not always a target of largest fibre. At $N=13$,

$$
P_{13}^{-1}(0)=\{0,1,13\},\qquad
P_{13}^{-1}(1)=\{2,3,4,6,12\}.
$$

The first equality uses the positive divisors of $13$; the second uses the
divisors of $12$ exceeding one. Thus the fibre sizes are three and five.
These are hand deductions from the proven formula, not software evaluations
or a recorded failed scientific assertion.

## Source subtraction

Chase–Pandey's actual original body defines the same fixed-dividend map
and its maximum-length problem. Baraskar–Vukusic's published 2026 version
explicitly separates the quotient-one image branch and proves the
proper-divisor criterion in Lemma 4. Its hypotheses restrict the source
divisor to at most $\lfloor N/2\rfloor$; adding the displayed quotient-one
branch explains our full-carrier formula.
See [SOURCES_AND_LIMITS.md](SOURCES_AND_LIMITS.md) for exact versions,
reading boundaries and the distinction from the 2025 preprint numbering.

## Missing obligations and disposition

The upper bound $h_N(a)\leq a$, one terminal basin and the factorial family
do not classify all entrance times or improve a published Pierce clock
theorem. No all-$N$ closed fibre maximum or maximizing-target classification
was proved. The explicit one-step divisor count is an owned arithmetic
primitive, not a second residual axis.

This one known-literal control therefore closes NO_PROMOTION / NO_RESERVE.
No parameter enlargement, special-denominator rescue, additional literal,
experiment, manuscript number or independent review is authorized by this
negative proof.
