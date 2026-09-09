# AS2-B: exact signed quadratic recurrence and the all-input exhaustion gap

2026-09-08 UTC. The complete all-odd-prime, all-embedded-quadratic
question remains [the frozen AS2-B](FROZEN_QUESTIONS.md). None of the
subfamilies below replaces its domain. All absolute values without a
$p$ subscript in height statements are Archimedean.

## B1. Exact integral-state recurrence for every input

Let $Ax^2+Bx+C=0$ be a primitive integral irreducible quadratic
polynomial of the input, with $A\ne0$. Set

$$
D=B^2-4AC,\quad \delta=2Ax+B\in\mathbb Q_p,
\quad P_0=-B,\quad Q_0=2A.
$$

Then $D$ is a nonsquare integer, $\delta^2=D$,
$x=(P_0+\delta)/Q_0$, and $Q_0\mid D-P_0^2$.
The same chosen $\delta$ is kept at every tick. With the actual signed
Browkin quotient $a_n=s_p(x_n)$, define

$$
P_{n+1}=a_nQ_n-P_n,\qquad
Q_{n+1}=\frac{D-P_{n+1}^2}{Q_n},\qquad
x_{n+1}=\frac{P_{n+1}+\delta}{Q_{n+1}}.
\tag{B1.1}
$$

These formulas give the actual orbit $x_{n+1}=T_p(x_n)$; every
$P_n,Q_n$ is integral, $Q_n\ne0$, and $Q_n\mid D-P_n^2$.

**Proof, including the denominator issue.** Suppose the claims hold
at $n$. As $\delta$ is a $p$-adic square root of an integer,
$v_p(\delta)\geq0$. Thus $v_p(x_n)\geq-v_p(Q_n)$.
The floor $a_n$ belongs to $\mathbb Z[1/p]$; it is zero if
$v_p(x_n)>0$, and otherwise has the same valuation as $x_n$.
Consequently $a_nQ_n\in\mathbb Z$, so $P_{n+1}\in\mathbb Z$.

For every prime $r\ne p$, $a_n$ is $r$-integral. Expansion of
$D-(a_nQ_n-P_n)^2$, together with $Q_n\mid D-P_n^2$, gives
$v_r(Q_{n+1})\geq0$. At $p$, write
$x_n^c=(P_n-\delta)/Q_n$. The exact factorization is

$$
Q_{n+1}=-Q_n(x_n-a_n)(x_n^c-a_n).
$$

The floor definition gives $v_p(x_n-a_n)\geq1$, while the numerator
of $x_n^c-a_n=(P_n-\delta-a_nQ_n)/Q_n$ is $p$-integral.
Therefore $v_p(Q_{n+1})\geq1$. The quadratic irrationality prevents
either factor from vanishing. This proves integrality and nonvanishing.
The divisibility at the next step follows from
$D-P_{n+1}^2=Q_nQ_{n+1}$, and rationalizing $1/(x_n-a_n)$ proves
(B1.1). Induction completes the proof. QED.

This is the source's standard quadratic recurrence, with its integral
normalization and valuations made explicit; it is not a new algorithm.
It matches equation (7) of
[Capuano–Murru–Terracini, §4](https://arxiv.org/html/2010.07364v1#S4).
In particular, dropping $Q_n$ or fixing its $p$-adic exponent is invalid.

## B2. What the known boundedness criterion does and does not decide

For this exact normalization, eventual periodicity is equivalent to
the existence of infinitely many $n$ for which $|P_n|\leq H$ for some
finite $H$. It is also equivalent to boundedness of the whole $P_n$
sequence. This is the content of the source's Proposition 4.1 and
Corollary 4.6, not a new criterion.

**Direct verification.** If $P_n$ is restricted to a finite set at
infinitely many indices $n\geq1$, then

$$
Q_{n-1}Q_n=D-P_n^2
$$

restricts $Q_n$ to finitely many signed integer divisors of finitely
many nonzero integers. Two states $(P_n,Q_n)$ must agree. The map is
deterministic, so the actual orbit repeats thereafter. Conversely,
because $\delta$ is irrational, equality of two expressions
$(P+\delta)/Q$ forces equality of both $P$ and $Q$. Thus an eventually
periodic orbit has an eventually periodic state sequence; its finite
initial segment does not affect boundedness. QED.

One may equivalently say that a nonperiodic orbit must satisfy
$|P_n|\to\infty$. This remains an infinite-time condition, not a
terminating test. The source's negative-norm subsequence condition is
a sufficient way to obtain boundedness when $D>0$, since
$N(x_n)=(P_n^2-D)/Q_n^2<0$ implies $|P_n|<\sqrt D$.
There is no proof here that every input reaches it.

If a first repeated exact state occurs at indices $i<j$, with $j$
the first repeated-state index, determinism shows that $i$ is the
least preperiod and $j-i$ the least period. Exact algebraic equality is
decidable for these states. Iterating until that event is only a
**semidecision procedure**: no stopping certificate for every negative
instance has been supplied. Large unrepeated prefixes are not negative
certificates. See
[Capuano–Murru–Terracini, Proposition 4.1 and Corollary 4.6](https://arxiv.org/html/2010.07364v1#S4).

## B3. Imaginary quadratic inputs cannot be removed by real descent

For every odd $p$, let $D=1-4p^2<0$ and choose the root
$\delta\in\mathbb Q_p$ of $D$ satisfying $\delta\equiv1\pmod p$.
It exists by Hensel's lemma. Put $x=(1+\delta)/(2p)$.
Since $(\delta-1)(\delta+1)=-4p^2$ and $\delta+1$ is a unit,

$$
v_p(x-1/p)=1,\qquad s_p(x)=1/p.
$$

The equality for the floor uses that $1/p$ is an allowed balanced
finite digit string and the difference lies in $p\mathbb Z_p$.
Moreover $x^2-x/p+1=0$, so

$$
T_p(x)=-x,\qquad T_p(-x)=x,
$$

using $s_p(-x)=-s_p(x)$. This is an exact least period two: $x\ne0$
and $x\ne-x$. Its field is imaginary quadratic and $N(x)=1>0$.
Thus negativity of a real norm is not a necessary periodicity condition
for the frozen full family. This explicit case is contained in the
source-owned signed two-period construction, Example 4.4, and is not
offered as a new paper or new nonperiodicity result.

## B4. The all-input counting trace is already infinite at one tick

Fix any odd $p$. For each $k\geq1$ choose
$\delta_k^2=1+4p^{2k}$ with $\delta_k\equiv1\pmod p$, and put
$x_k=(1+\delta_k)/(2p^k)$. The positive integer $1+4p^{2k}$ lies
strictly between $(2p^k)^2$ and $(2p^k+1)^2$, so every $x_k$ is
quadratic irrational. Also

$$
v_p(\delta_k-1)=2k,\qquad
s_p(x_k)=p^{-k},\qquad
x_k^2-p^{-k}x_k-1=0.
$$

It follows that $T_p(x_k)=x_k$. These are distinct because
$v_p(x_k)=-k$. Hence $\#\operatorname{Fix}(T_p)=\infty$ already for
each one fixed prime. The ordinary all-input Artin–Mazur counting
series has no finite first coefficient. A height-weighted, valuation-
weighted or induced clock would be a different observable and has not
been substituted. This elementary control is not an independent paper.

## B5. Source subtraction and the precise unresolved obligation

Romeo's 2025 Proposition 1 proves necessary simultaneous real
convergence for periodic inputs whose quadratic field has a real
embedding. Its converse remains conjectural in that paper; the paper
does not exhibit a proved nonperiodic Browkin quadratic. Its
probabilistic discussion explicitly assumes digit-distribution
properties. Haar-almost-every statements cannot by themselves establish
anything on the countable set of algebraic quadratic inputs, which has
Haar measure zero. We neither transplant the real hypothesis to B3
nor call a numerical prefix a nonperiodicity proof.
[Romeo, §3 and abstract](https://link.springer.com/article/10.1007/s11139-025-01264-7).

The 2026 paper on varieties of periodic fractions studies prescribed
formal continued fractions and their convergence. In particular,
Remark 4.21 explicitly distinguishes certain constructed expansions
from Browkin/Ruban floor algorithms. Such a periodic representation
does not prove the frozen orbit follows those partial quotients.
[Capuano–Mula–Terracini–Veneziano, Remark 4.21](https://link.springer.com/article/10.1007/s40993-026-00770-x).

The missing full result is a **terminating classification** on all
$(p,x)$ in the frozen family, including a justified stopping rule for
every nonperiodic case and exact least preperiod/period for every
periodic case. Neither an input-dependent effective trapping bound with
proved entry, nor an exhaustive finite negative certificate, nor a
uniform alternative classification has been established here.
The infinite condition in B2 is not such a rule. No mathematical census
was run because it would not fill this gap.

The bounded search does not license a worldwide novelty claim or a
claim that a particular named later theorem cannot exist. It does
establish that the inspected primary statements and the arguments above
do not close the frozen question.

**Disposition:** `FULL_ALL_INPUT_DECISION_GAP`;
`STANDARD_RECURRENCE_AND_PERIODIC_CONTROLS_AUXILIARY`;
`NO_PAPER_CONTRACT_ADMISSION`.
`NO_BAD_EULER_OR_ROOT_NUMBER`.
