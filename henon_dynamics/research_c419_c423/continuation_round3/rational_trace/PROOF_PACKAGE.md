# RT3: exact denominator lemma and unresolved rational classification

2026-09-07 UTC. No numerical or symbolic program was required.

## Claim and status

The [unchanged contract](FROZEN_CONTRACT.md) asks for all ordinary
periodic points of $T_a$ on $\mathbb Q^3$, for every $a\in\mathbb Z$
and every rational level. **Status: NOT CURRENTLY JUSTIFIED.**

The denominator lemma below is proved. Its integral-level corollary
is a short consequence of the accepted IR1 theorem and does not count
as a fourth independent contract. The all-rational-level claim is not
silently replaced by that corollary.

## Assumptions and notation

Let $(x_i)_{i\in\mathbb Z/n\mathbb Z}$ be a rational periodic scalar
sequence for the original clock, satisfying

$$x_i+x_{i+3}=x_{i+1}x_{i+2}+a,\qquad a\in\mathbb Z.$$

Its invariant is
$k=x_i^2+x_{i+1}^2+x_{i+2}^2-x_ix_{i+1}x_{i+2}
-a(x_i+x_{i+1}+x_{i+2})$.
Let $q$ be the least common multiple of the positive reduced
denominators of all scalar coordinates in this finite orbit. For each
prime $p$, normalize $|p|_p=p^{-1}$ and put $H_p=\max_i|x_i|_p$.

## Strategy and dependency map

1. Two recurrence identities bound the neighbors of a p-adic maximum.
2. At that phase, one term of the invariant strictly dominates all
   other terms if $H_p>1$.
3. Applying the valuation conclusion at every prime gives the exact
   level denominator and the integral-level corollary.
4. An explicit period-two family shows why no uniform $q$ bound follows.
5. The integer finite-core argument does not cover all unbounded $q$.

## 1. Denominator theorem

**Lemma.** The reduced denominator of $k$ is exactly $q^2$. In
particular, if $k\in\mathbb Z$, every rational periodic point is integral.

**Proof.** Fix $p$. If $H_p\le1$, all coordinates and $a$ are p-adic
integers, so $|k|_p\le1$. Suppose $H_p>1$ and choose $j$ with
$|x_j|_p=H_p$. The recurrences at $j-2$ and $j-1$ give

$$x_{j-1}x_j=x_{j-2}+x_{j+1}-a,\qquad
x_jx_{j+1}=x_{j-1}+x_{j+2}-a.$$

The ultrametric inequality and $|a|_p\le1<H_p$ bound both right
sides by $H_p$. Division by $|x_j|_p$ gives
$|x_{j-1}|_p,|x_{j+1}|_p\le1$.
Evaluate the invariant at $(x_{j-1},x_j,x_{j+1})$. The square $x_j^2$
has norm $H_p^2$. The other two squares have norm at most $1$, the
triple product at most $H_p$, and each linear term at most $H_p$.
Thus the square is the unique term of largest norm. The strict
ultrametric equality gives $|k|_p=H_p^2$.

Write $p^e$ for the exact p-part of $q$. If $e>0$, then $H_p=p^e$
and $v_p(k)=-2e$. If $e=0$, the preceding integral case gives
$v_p(k)\ge0$. These statements at every prime say precisely that
the reduced denominator of $k$ is $q^2$. They also include $k=0$,
whose reduced denominator is one: in that case no $H_p>1$ is possible.
The argument does not assume a nonsingular invariant surface or a
lower bound on the period. $\square$

Consequently, at integral $a,k$, the ordinary rational periodic locus
equals the ordinary integer locus already classified by
[IR1](../../continuation_round2/integral_return/IR1_CLASSIFICATION.md),
with exactly the same native least periods and counts. This is an
application of IR1, not a second independent classification result.

## 2. Unbounded denominators are real, not a technical nuisance

At $a=0$, for every integer $q\ge2$, put

$$u=1+q^{-1},\qquad v=1+q.$$

Then $uv=u+v$, so $T_0(u,v,u)=(v,u,v)$ and
$T_0(v,u,v)=(u,v,u)$. Since $u\ne v$, this is an ordinary least-two
cycle, not a fixed point. Its common denominator is exactly $q$ and
its invariant is

$$k=uv(uv-3)=\frac{(q+1)^2(q^2-q+1)}{q^2}.$$

The numerator is coprime to $q$, verifying the denominator conclusion
directly in an unbounded family. This is the inherited period-two
algebra over rational parameters, not a newly discovered orbit family.

For an arbitrary rational level whose denominator is not a square,
the lemma excludes rational periodic points altogether. When it is a
square, the lemma is necessary, not sufficient and not a full atlas.

## 3. Why the current proof does not close the full question

The accepted integer proof uses

$$d_i=x_{i+2}-x_i,\qquad
d_{i+1}+d_{i-1}=(x_{i+1}+1)d_i.$$

At a real maximum $D=\max|d_i|>0$, one gets
$|x_{i+1}+1|\le2$. Over integers this produces the five centers
$-3,-2,-1,0,1$. Over $q^{-1}\mathbb Z$, it produces $4q+1$ possible
centers. Neither the five-center case analysis nor its fixed universal
core therefore applies to every $q$. The lower bound for a nonzero
difference also drops from one to $1/q$.

The denominator theorem gives a bound for a *specified* level, but
the contract quantifies over all rational levels, including the
unbounded $q$ above. No denominator-uniform classification of the
new centered cases, no all-period exclusion outside known rational
curves, and no complete parameter atlas has been proved here.
Running a larger rational-height box would not fix that gap.

## Disposition and open risks

**Do not admit RT3.** The integral-level corollary and square-denominator
obstruction are useful short companions to IR1. The unrestricted
rational classification remains open in this bounded screen, not
proved false. No arithmetic census, fresh IR1 verification, manuscript,
formal evaluation or new C-number was produced. Source comparisons
are recorded separately; none is claimed to prove global priority.
