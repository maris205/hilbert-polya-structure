# R3-PC-L: prime levels isolate the unclosed global obstruction

2026-09-08 UTC. This is a hand-proof continuation of the
[unchanged original question](FROZEN_CONTRACTS.md), not an admitted
contract. No mathematical program was run.

## Claim and status

For every odd prime $p$, every $c\in k=\overline{\mathbb F}_p$ and every
$h\in k[x]$, the original question is still whether all ordinary
primitive $f_c=x^2+c$ orbit sums vanish exactly for polynomial
coboundaries, or whether the entire defect space has a uniform
classification.

**The original full question remains UNCLOSED.** This package proves a
more specific necessary condition for a hypothetical defect: at every
sufficiently large prime level there must be an exponentially high
contact on a genuinely new prime-period cycle. Repetition of finitely
many old cycles, including wild iteration at them, cannot by itself
account for the obstruction.

This is an auxiliary localization of the missing argument, not a
full global upper bound and not a second paper question. The optional
second question is unused.

## Deducted input and notation

Write $\Delta_cQ=Q\circ f_c-Q$ and use the unique normal form
$h=\Delta_cQ+v$ with $v\in V=k\oplus xk[x^2]$. These normal forms are
old inputs. A nonzero constant cannot represent a defect because $f_c$
has a fixed point. A hypothetical nonzero defect therefore has positive
odd normal degree $D$.

Set $F_n=f_c^{\circ n}-x$, and let $M_n$ be its maximum root
multiplicity over $k$. The full scheme-level trace argument and
Frobenius necessity are already proved in the
[R2 package, Steps 1--4](../../continuation_round2/positive_characteristic/PROOF_PACKAGE.md):

$$
v\in K_c\setminus\{0\},\quad \deg v=D
\quad\Longrightarrow\quad
M_n>\frac{2^{\lceil n/2\rceil}}{pD}
\quad\text{for every }n\geq1.\tag{1}
$$

They are not claimed again as this round's new contribution. The
local lemmas below are current-team author reasoning, independent of an
external multiplicity theorem.

## Lemma 1: prime-to-characteristic repetition of a tangent germ

Let $g(t)=t+b t^e+O(t^{e+1})$ with $b\ne0$ and $e\geq2$ over a field
of characteristic $p$. For every positive integer $m$,

$$
g^{\circ m}(t)=t+m b t^e+O(t^{e+1}).\tag{2}
$$

In particular, if $p\nmid m$, the multiplicity of $0$ as a root of
$g^{\circ m}(t)-t$ is exactly $e$.

Proof. If two tangent-to-identity series have first displayed
coefficients $b_1,b_2$ in degree $e$, their composition has coefficient
$b_1+b_2$ there. Indeed, substituting $t+O(t^e)$ into $t^e$ changes it
only in degrees at least $2e-1\geq e+1$. Induction proves (2). When
$p\nmid m$, $mb$ is nonzero. No assertion of an upper bound for
$g^{\circ p}$ is made. $\square$

## Lemma 2: fixed points contribute exactly length two at almost all prime levels

For a fixed pair $(p,c)$, let $E_c$ consist of $p$ and any prime which
is the multiplicative order of a nonzero fixed-point multiplier
$\lambda=2a\ne1$ of $f_c$. There are at most two fixed points, so
$E_c$ is finite. The orders exist because every nonzero element of
$\overline{\mathbb F}_p$ lies in a finite multiplicative group.

For every prime $\ell\notin E_c$, the sum of the multiplicities in
$F_\ell$ of all fixed points of $f_c$ is exactly $2$.

Proof. The fixed-point equation is $a^2-a+c=0$.

If $c\ne1/4$, it has two distinct roots and neither multiplier is $1$.
A zero multiplier stays zero on iteration. For a nonzero multiplier,
$\lambda^\ell=1$ would imply that its order divides the prime $\ell$;
since that order is not $1$, it would equal $\ell$, which has been
excluded. Thus $F_\ell'(a)=\lambda^\ell-1\ne0$ at both fixed points.
Each has multiplicity $1$.

If $c=1/4$, there is one fixed point $a=1/2$. In its coordinate $t=x-a$,

$$
f_c(a+t)-a=t+t^2.
$$

Since $\ell\ne p$, Lemma 1 shows that its multiplicity in $F_\ell$ is
exactly $2$. This includes the parameter for which no $F_n$ is ever
squarefree. In either case the total is $2$. $\square$

This is a prime-level reduction inside a proof attempt for the original
question. It does not change the original observable to prime periods
or omit its ordinary cycles with length divisible by $p$.

## Lemma 3: multiplicity is constant along a noncritical cycle

If $a$ belongs to a cycle of length $r$ and its return multiplier is
nonzero, the multiplicity of every point in that cycle as a root of
$F_r$ is the same.

Proof. Every one-step derivative on the cycle is nonzero. The germ of
$f_c$ from the completed local coordinate at $a$ to that at $f_c(a)$
therefore has an invertible linear term and a formal inverse. Commutation
$f_c\circ f_c^{\circ r}=f_c^{\circ r}\circ f_c$ conjugates the two return
germs. If $u$ is an invertible formal coordinate and $g$ fixes $0$, then
$u(g(t))-u(t)$ equals $(g(t)-t)$ times a power series with nonzero
constant term $u'(0)$. Substitution by $u^{-1}$ also preserves order.
Thus conjugacy preserves the order of $g(t)-t$. Repeating around the
cycle proves the claim. $\square$

## Proposition: a defect requires large contacts on new prime cycles

Suppose $v\in K_c\setminus\{0\}$ is a normal representative of degree
$D$. For every sufficiently large prime $\ell\notin E_c$, there is an
ordinary primitive orbit $O_\ell$ of exact length $\ell$ such that its
return multiplier is $1$ and its common root multiplicity $e_\ell$ in
$F_\ell$ satisfies

$$
\frac{2^{(\ell+1)/2}}{pD}<e_\ell
\leq\frac{2^\ell-2}{\ell}.\tag{3}
$$

Proof. Take $\ell$ large enough that it is odd and
$2^{(\ell+1)/2}/(pD)\geq2$. By (1), some root of $F_\ell$ has
multiplicity $e_\ell=M_\ell>2$. Lemma 2 rules out all fixed points,
whose individual multiplicities are at most $2$.

The exact period of a root of $F_\ell$ divides $\ell$, hence is either
$1$ or $\ell$. It is therefore $\ell$. Multiplicity greater than one
means $(f_c^{\circ\ell})'(a)=1$. In particular the return multiplier is
nonzero, so Lemma 3 gives the same multiplicity at every one of its
$\ell$ distinct orbit points. The polynomial $F_\ell$ has degree
$2^\ell$, and the fixed points consume total multiplicity $2$ by
Lemma 2. Thus $\ell e_\ell\leq2^\ell-2$. Inequality (1) gives the
strict lower bound. $\square$

The orbits in (3) for different primes are necessarily different.
Consequently an explanation involving only a fixed finite list of old
periodic germs cannot meet this necessary condition. In particular,
growth obtained only by iterating a tangent germ $p^j$ times does not
settle what happens at these new prime periods.

## Exact global step still missing

Let $E_\ell^{\rm new}$ be the largest multiplicity among exact
$\ell$-period points, with value $0$ if there are none. One sufficient
completion would be

$$
\liminf_{\substack{\ell\to\infty\\\ell\text{ prime},\ \ell\notin E_c}}
\frac{E_\ell^{\rm new}}{2^{\ell/2}}=0
\quad\text{for every allowed }(p,c).\tag{4}
$$

Indeed, a hypothetical defect would force the ratio in (4) to be
strictly greater than $\sqrt2/(pD)$ at every sufficiently large prime.
Lemma 2 ensures that fixed points cannot spoil a prime subsequence
bound. No proof of (4), or a weaker sufficient all-parameter statement,
was obtained here.

The upper bound in (3) is too large: after division by $2^{\ell/2}$
it has order $2^{\ell/2}/\ell$, not a quantity tending to zero. Thus
the elementary orbit-length count is not a contradiction and is not
described as a closure.

The finite postcritical orbit, PCF lifting to characteristic zero,
and multiplier-spectrum rigidity were examined as possible global
routes. The source/hypothesis boundaries are recorded separately in
[SOURCE_AUDIT.md](SOURCE_AUDIT.md); none supplies (4) in the inspected
portions. Preserving postcritical combinatorics does not itself establish
a comparison of periodic-root multiplicities under specialization.

The skew-product interpretation also gives no extra conclusion by
itself: an ordinary cycle with nonzero additive return has fibre period
multiplied by $p$, while a zero return leaves that period unchanged.
This is the original observable and its known elementary interpretation,
not a construction of a rational transfer. The earlier rational-pole
lemma remains conditional on the existence of a rational transfer.

## Handoff

One original question continued; zero second questions; zero mathematical
executions; zero complete contracts. This package neither disproves the
original equality nor proves that (4) is false. It identifies the new
prime-period high-contact issue that must be settled by a real global
argument or bypassed by a full algebraic regularity proof. No manuscript,
PDF, old experiment, formal evaluation, release state or Git integration
was changed. No Euler-factor or root-number claim is involved.
