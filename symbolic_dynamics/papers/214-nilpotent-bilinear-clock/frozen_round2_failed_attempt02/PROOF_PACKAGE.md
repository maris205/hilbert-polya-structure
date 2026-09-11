# P214 proof package

## Claim and status

`PROVABLE AS STATED` for all five clauses of the
[frozen theorem contract](../../docs/papers211_215_sequence/qa/fresh55_root_reception01/THEOREM_CONTRACT.md).
This is the paper-local proof role required by the inherited artifact
contract. It restates the accepted Fresh55 deductions without editing those
originals. Manuscript reviews and computational checks remain pending.

## Assumptions and notation

Let $q$ be a prime power, $m\geq2$, $R=\mathbb F_q[t]/(t^m)$ and $I=tR$.
The full carrier is $I^2$, and $F(x,y)=(y,x(t+y))$. The least nonzero
coefficient degree defines $v(z)$ for $z\ne0$, with $v(0)=m$.
The first hitting time of zero is $\tau(x,y)$, with time zero included.

Coefficient multiplication gives
$v(zw)=\min\{m,v(z)+v(w)\}$, since the coefficient at the summed leading
degree is nonzero in the field unless truncation removes that degree.
Counting free coefficients gives $|t^rR|=q^{m-r}$ for $0\leq r\leq m$.
An element with nonzero constant coefficient has an inverse by a finite
geometric series. In particular $v(t+z)=1$ for $z\in t^2R$.

## Strategy and dependency map

1. Represent both state coordinates by one second-order recurrence.
2. Prove that all terms from index two lie in $t^2R$.
3. Separate the two parity chains; distinguish $v(y)\geq2$ from $v(y)=1$.
4. Count ideal rectangles to obtain the temporal census.
5. Solve the one-step multiplication equation by its ideal image/kernel;
   count its ordinary and saturated target strata.
6. Exhibit the two-sided old-multiplication adapter and the linear control;
   use unequal positive fibres for the stated nonconjugacy obstruction.

No external theorem or finite run is required for these deductions. The
source-audit references are context, not hidden proof dependencies.

## 1. Recurrence and exact clock

Set $x_0=x$, $x_1=y$ and $x_{n+2}=x_n(t+x_{n+1})$. Induction gives
$F^n(x,y)=(x_n,x_{n+1})$. Both initial terms are in $I$. Whenever two
consecutive terms lie in $I$, the product defining the next belongs to
$t^2R$. Thus all terms lie in $I$, and $x_n\in t^2R$ for every $n\geq2$.
All multipliers $t+x_n$ with $n\geq2$ consequently have valuation one.

Write $a=v(x)$, $b=v(y)$. We prove

$$\tau(x,y)=\max\{2(m-b),\,2(m-a)-1\}.\tag{T}$$

If $b\geq2$, the initial multiplier also has valuation one, giving

$$v(x_{2k})=\min\{m,a+k\},\qquad
v(x_{2k+1})=\min\{m,b+k\}\quad(k\geq0).$$

When $a<m$, the last nonzero even-indexed term has index $2(m-a-1)$.
When $b<m$, the last nonzero odd-indexed term has index $2(m-b-1)+1$.
The first zero state is one position after the last nonzero term, which
gives (T). If $a=m$, the even chain is absent; its contribution $-1$ in
(T) cannot exceed the nonnegative odd-chain contribution. If $b=m$, the
odd chain is absent and contributes zero. If both equal $m$, (T) gives zero.

If $b=1$, cancellation in $t+y$ may accelerate the even chain. The ideal
inclusions and later multiplier valuations still give

$$v(x_{2k})\geq\min\{m,a+k\}\quad(k\geq1),\qquad
v(x_{2k+1})=\min\{m,1+k\}\quad(k\geq0).$$

For the odd chain, every update uses a neighboring even term from index
two onward, hence an exact valuation-one multiplier. Therefore
$x_{2m-3}\ne0$, whereas $x_{2m-2}=x_{2m-1}=0$. The first zero state is
$2m-2$, including when $m=2$. As $a\geq1$, (T) gives that same value.

Zero is fixed and every state reaches it, so it is uniquely recurrent and
has period one. If $b=1$ the depth is $2m-2$; if $b\geq2$ both terms in
(T) are at most $2m-3$. This proves the exact height and its equality set.

The cancellation example $(t,-t)$ has $x_2=0$ and, for $k\geq1$,

$$F^{2k}(t,-t)=(0,-t^{k+1}),\qquad
F^{2k+1}(t,-t)=(-t^{k+1},0).$$

Its first zero state is still $2m-2$. No step asserts an exact valuation
increment for both chains in the cancellation branch.

## 2. Depth census

For an integer $0\leq h\leq2m-2$, (T) is equivalent to

$$v(x)\geq m-\lceil h/2\rceil,\qquad
v(y)\geq m-\lfloor h/2\rfloor.$$

The thresholds lie between $1$ and $m$. Counting the two ideals gives
$q^{\lceil h/2\rceil}q^{\lfloor h/2\rfloor}=q^h$ states of depth at
most $h$. There is one state at depth zero. Subtracting consecutive
cumulative counts gives $(q-1)q^{h-1}$ states at each positive depth.

## 3. Every target fibre

Fix $(u,w)\in I^2$ and put $d=\min\{v(t+u),m-1\}$. An inverse must have
$y=u$ and solve $(t+u)x=w$ with $x\in I$.

For $d\leq m-2$, write $t+u=t^d e$ with $e$ a unit. Multiplication by
$e$ preserves each ideal. Multiplication by $t+u$ therefore has image
$t^{d+1}R$ and kernel $t^{m-d}R$ on $I$. If $w=t^{d+1}w_0$, a solution
is $x_0=te^{-1}w_0$. Two solutions differ by a kernel element, and adding
any such element preserves the equation. Thus the full predecessor set is

$$F^{-1}(\{(u,w)\})=
\{(x_0+k,u):k\in t^{m-d}R\}$$

when $w\in t^{d+1}R$, and is empty otherwise. The nonempty fibre has
$q^d$ elements. The choice of lift $w_0$ does not change the coset.

For $d=m-1$, one has $(t+u)I=0$, even when $t+u$ is nonzero. Hence
$w=0$ is necessary and sufficient, and every $x\in I$ is a solution.
The same formulas apply because $t^{d+1}R=0$ and $t^{m-d}R=I$. In
particular $t+u=0$ has kernel $I$, not the larger additive group of $R$.

## 4. Fibre distribution and extremum

Translation $u\mapsto t+u$ permutes $I$. For each $1\leq d\leq m-2$,
there are $(q-1)q^{m-d-1}$ choices of $u$ with valuation $d$, each
admitting $q^{m-d-1}$ choices of $w$. Consequently

$$\#\{\text{targets with fibre size }q^d\}
=(q-1)q^{2(m-d-1)}.$$

The saturated condition $t+u\in t^{m-1}R$ gives exactly the $q$ targets
$(-t+c t^{m-1},0)$, $c\in\mathbb F_q$, each with fibre size $q^{m-1}$.
These are precisely the maximizers. Summing all nonempty-target counts gives

$$|\operatorname{im}F|=q+(q-1)\sum_{j=1}^{m-2}q^{2j}.$$

Every remaining target has empty fibre. At $m=2$ the sum and ordinary
range are empty, leaving $q$ nonempty fibres of size $q$.

## 5. Ownership and linear comparison

On the same $I^2$, let $M(a,b)=(b,ab)$, $P(x,y)=(x,y+t)$ and
$Q(u,w)=(u-t,w)$. The translations are bijections and substitution gives
$F=Q\circ M\circ P$. This is a complete one-step multiplication adapter;
it deducts all new inverse-mechanism credit. Because $Q\ne P^{-1}$, the
displayed identity is not a conjugacy and does not transport iterates.

For $L(x,y)=(y,tx)$, direct iteration gives

$$L^{2k}(x,y)=(t^kx,t^ky),\qquad
L^{2k+1}(x,y)=(t^ky,t^{k+1}x).$$

It has the clock (T) and the same depth census. When $m=2$, all products
of two elements of $I$ vanish, so the actual maps satisfy $F=L$.

When $m\geq3$, positive fibres of sizes $q$ and $q^{m-1}$ both occur.
For a finite-group endomorphism $\phi$, any nonempty fibre is a coset of
$\ker\phi$, since $\phi(z)=\phi(g)$ is equivalent to
$\phi(g^{-1}z)=1$. All its positive fibres have equal size. Bijective
dynamical conjugacies preserve fibre cardinalities; thus $F$ is not
conjugate to any finite-group endomorphism when $m\geq3$.

## Corrections, authorship and open risks

The admitted theorem survives unchanged. The root's cancellation challenge
was resolved on the original carrier, not by excluding $v(y)=1$. Root is
therefore a proof contributor, along with the main scout and the explicit
P/Q adapter contributor. Author-verifier helpers are also disclosed in
README and receive no independent manuscript-review credit.

The contribution is the stated nonlinear cancellation-safe clock, not a
new clock shape, general contraction method or inverse mechanism. No
arbitrary nonlinear-factor absence, general chain-ring extension, all-time
inverse formula or graph-isomorphism classification has been proved.
Later source, execution, manuscript A/B and artifact gates remain open;
this proof document alone is not paper completion.
