# Branch-discriminant ledger and an upper-bound limitation

2026-09-09 UTC. Companion to [REPORT.md](REPORT.md).

## Claim and status

**PROVABLE AS STATED:** equations (1)--(9) below and their
method-specific noncontradiction conclusion.

**NOT CURRENTLY JUSTIFIED:** the proposed incompatible upper bound
(BD-U), namely $d_L<p^h-1+p^{e-1}(p-1)$ for every proper root
field. No counterexample to the exact quadratic's full inertia is
constructed.

## Assumptions and notation

Use the exact accepted small cycle for
$P=P_s=(1+s)z+z^2$ over $K=k((s))$,
$k=\overline{\mathbb F}_p$, $p$ odd. The valuation satisfies
$v(s)=1$. Put

$$
n=p^e,\quad r=(p-1)/p,\quad \alpha_i=P^i(\alpha)
\ (i\in\mathbb Z/n\mathbb Z),\quad v(\alpha_i)=r.
$$

The roots $\alpha_i$ are distinct and form one ordinary native cycle.
Let $L=K(\alpha)$, $q=[L:K]=p^h$, $1\le h\le e$,
and $a=e-h$. The accepted splitting-group statement gives
$\operatorname{Gal}(L/K)=\langle P^{p^a}\rangle$ as
permutations of this cycle. The minimal polynomial $D$ of $\alpha$
has root set $\{\alpha_{b p^a}:0\le b<q\}$.

Write $R=k[[s]]$, let $O_L$ be the integral closure, and let
$v_L=qv$ be its integer valuation. The field is totally ramified.
Define

$$
\begin{aligned}
\delta_j&=v(P^{p^j}(\alpha)-\alpha), &&0\le j<e,\\
T_e&=v(\operatorname{Disc}(M_e)),&
S_D&=v(\operatorname{Disc}(D)),\\
I_D&=\operatorname{length}_R(O_L/R[\alpha]),&
d_L&=\text{different exponent of }L/K.
\end{aligned}
$$

The accepted R2 inequalities are
$\delta_j\ge(p^j+1)r$ and $d_L\ge q-1+n r$.
They are inputs, not rederived here. All polynomial discriminants
below are of separable monic polynomials and are nonzero.

## Strategy and dependency map

1. Count native steps of each $p$-adic order to separate internal
   branch contacts from contacts between different branches.
2. Compare the monogenic order with its normalization by an integral
   scaled-monomial lattice.
3. Insert only the already accepted displacement bounds, and compare
   the resulting upper bound with the accepted lower bound.
4. When $q=p$, distinct valuation residues show that the index
   correction is exact.

## 1. Exact branch and total discriminants

For every integer $j$ with $0\le j<e$, and every integer $b$
prime to $p$ with $1\le b<p^{e-j}$,

$$
v(P^{b p^j}(\alpha)-\alpha)=\delta_j.
$$

Indeed the accepted quadratic difference identity

$$
P(x)-P(y)=(x-y)(1+s+x+y)
$$

shows that each iterated ratio of differences between cycle points
is $1$ modulo positive valuation. Express the $b p^j$-step
displacement as a sum of $b$ successive $p^j$-step
displacements. After division by $P^{p^j}(\alpha)-\alpha$,
the summands all have residue $1$, so their sum has residue
$b\ne0$. This also shows that the values are independent of the
choice of the starting point in the native cycle.

There are $(p-1)p^{e-j-1}$ indices in
$\{1,\ldots,n-1\}$ of $p$-adic order $j$. The product of
differences defining $M_e'(\alpha)$, followed by the product over
its $n$ roots, gives

$$
T_e=n(p-1)\sum_{j=0}^{e-1}p^{e-j-1}\delta_j.              \tag{1}
$$

Inside the root set of $D$, the allowed differences have step
indices divisible by $p^a$. Their order classes are therefore
exactly $a,\ldots,e-1$, with the same counts
$(p-1)p^{e-j-1}$. Thus

$$
S_D=q(p-1)\sum_{j=a}^{e-1}p^{e-j-1}\delta_j
 =\frac qn T_e
  -q(p-1)\sum_{j=0}^{a-1}p^{e-j-1}\delta_j.              \tag{2}
$$

For $a=0$, the last sum is empty and zero. Equation (2) is also
the exact subtraction of inter-branch resultants from the total
discriminant. In particular, simply dividing $T_e$ by the number
of branches would retain positive contacts between different
branches and would not give $S_D$.

## 2. The slope-forced normalization index

For $0\le i<q$, put

$$
f_i=\lfloor i r\rfloor,\qquad \beta_i=s^{-f_i}\alpha^i.
$$

Each $\beta_i$ is integral because
$v(\beta_i)=ir-f_i\ge0$. Since $D$ has degree $q$, these
$q$ elements are a $K$-basis of $L$. Consequently the full
$R$-lattice

$$
\Lambda=\bigoplus_{i=0}^{q-1}R\beta_i
$$

lies in $O_L$ and contains $R[\alpha]$, whose monic basis is
$1,\alpha,\ldots,\alpha^{q-1}$. The diagonal basis change
$\alpha^i=s^{f_i}\beta_i$ gives

$$
I_D\ge\operatorname{length}_R(\Lambda/R[\alpha])
 =\sum_{i=0}^{q-1}\lfloor ir\rfloor
 =\frac{q(p-1)(q-2)}{2p}.                               \tag{3}
$$

For the last equality, write $q=pu$ and $i=cp+b$ with
$0\le c<u$, $0\le b<p$. Then
$\lfloor ir\rfloor=c(p-1)+\lfloor b(p-1)/p\rfloor$.
The latter floor is $0$ at $b=0$ and $b-1$ for
$1\le b<p$. Summing gives

$$
p(p-1)\frac{u(u-1)}2+
u\frac{(p-1)(p-2)}2
=\frac{q(p-1)(q-2)}{2p}.
$$

The trace-form determinant identity is

$$
S_D=d_L+2I_D.                                           \tag{4}
$$

Here is a direct verification of the normalizations. The trace dual
of $O_L$ is $\mathfrak p_L^{-d_L}$ by the definition of the
different. The valuation of the trace Gram determinant of an
integral basis is therefore the $R$-length of
$\mathfrak p_L^{-d_L}/O_L$, which is $d_L$ because the residue
degree is $1$. Replacing an integral basis by the monic basis of
$R[\alpha]$ multiplies this determinant by the square of the
basis-change determinant. The valuation of the latter determinant
is $I_D$, which proves (4). Thus the exponent $d_L$ in (4)
is a field different, not an order discriminant.

Combining (3)--(4) yields

$$
d_L\le S_D-q r(q-2).                                    \tag{5}
$$

## 3. The total-discriminant upper bound and its limitation

Insert the accepted $\delta_j\ge(p^j+1)r$ into the subtracted
prefix of (2). The finite sum is

$$
(p-1)\sum_{j=0}^{a-1}p^{e-j-1}(p^j+1)
=(p-1)a p^{e-1}+n-q.
$$

Equations (2) and (5) give the valid bound

$$
d_L\le
U_{e,h}(T_e):=
\frac qn T_e
-q r\big((p-1)(e-h)p^{e-1}+n-2\big).                    \tag{6}
$$

This is an upper bound on the field different using the total
polynomial discriminant and a proved normalization correction.
There is no assertion that it is sharp.

The same accepted lower bounds in (1), now applied to every
index, imply

$$
T_e\ge n r\big((p-1)e p^{e-1}+n-1\big).
$$

Substitution into (6) proves

$$
U_{e,h}(T_e)\ge
q r\big((p-1)h p^{e-1}+1\big)
>q-1+n r.                                               \tag{7}
$$

To verify strictness without an asymptotic argument, set
$c=q/p\ge1$. The difference between the middle and last
expressions in (7) is

$$
n r\big(c h(p-1)-1\big)-c+1.
$$

Because $p\ge3$ and $h\ge1$, the coefficient in parentheses
is at least $1$. Also $n\ge q=pc$, so $nr\ge c(p-1)$.
The difference is therefore at least
$c(p-2)+1>0$.

The conclusion is stronger than a limitation caused only by
unknown inter-branch contacts. Even if $S_D$ is known exactly,
its tail formula (2) and the accepted displacement bounds give

$$
S_D-q r(q-2)
\ge q r\big((p-1)h p^{e-1}+1\big)
>q-1+n r.
$$

Thus neither upper bound (5) nor (6) can contradict the accepted
different lower bound. An additional estimate on the normalization
index or additional information constraining the actual contacts
is required. This proves a limitation of those two explicit bounds,
not a universal obstruction to a branch-theoretic proof.

## 4. Exactness of the index correction in degree p

Suppose $h=1$, so $q=p$. The integer valuations of the elements
$\beta_i$ from Section 2 are

$$
v_L(\beta_i)=i(p-1)-p\lfloor i(p-1)/p\rfloor,
\qquad 0\le i<p.
$$

They are precisely the distinct residues $0,\ldots,p-1$ in
some order. Every $x\in L$ has a unique expression
$x=\sum_i a_i\beta_i$, $a_i\in K$. The nonzero summands
have pairwise distinct valuations modulo $p$, so their minimum
valuation is attained once. Hence $x$ is integral if and only if
each $a_i\beta_i$ is integral. Since
$0\le v_L(\beta_i)<p$ and $v_L(a_i)\in p\mathbb Z$, the
latter condition is equivalent to every $a_i\in R$.
It follows that $\Lambda=O_L$ and

$$
I_D=\frac{(p-1)(p-2)}2,\qquad
d_L=(p-1)\big(p\delta_{e-1}-p+2\big).                    \tag{8}
$$

The accepted lower estimate for $\delta_{e-1}$ yields

$$
d_L\ge(p-1)(n r+1).                                    \tag{9}
$$

This is exactly consistent with the R2 degree-$p$ identity
$b_L=p\delta_{e-1}-(p-1)$ and
$d_L=(p-1)(b_L+1)$. The order-index calculation supplies no
new restriction that would cap that break.

For a concrete consistency check using an already available scalar,
take the certified discriminant input $p=3,e=2,T_2=144$,
but do not assume the certified full Galois group. Equation (1),
with $\delta_0=4/3$, gives $\delta_1=4$.
A hypothetical degree-$3$ branch would then have
$S_D=3\cdot2\cdot4=24$, $I_D=1$, and $d_L=22$.
Both $q-1+nr=8$ and the sharper value
$(p-1)(nr+1)=14$ in (9) are below $22$.
These conditional numbers demonstrate the precise failure of this
branch-only inequality. They do not assert existence of that
hypothetical field as a root field of the actual polynomial.

## Missing lemma, source ownership, and open risks

The uniform target (BD-U) remains unproved. For $h>1$, a
stronger lower estimate on $I_D$ could potentially reduce (5).
Such an estimate must use more than the scaled monomial lattice;
its valuation residues are no longer all distinct. For $h=1$,
the index is already exact, so one needs a restriction on actual
contacts, Artin--Schreier data, or interactions with another
native periodic field.

The accepted R2 lower bound is not contradicted, weakened, or
reproved. The branch permutation setup is imported from A3.
Discriminant products, trace-form determinants, and valuation
lattices are elementary mechanisms; no novelty in the general
theory is asserted. The fixed-degree high-conductor control from
[Elder--Keating Section 2](https://arxiv.org/html/2503.16830v1)
applies over this perfect residue field but constructs no
periodic points of $P_s$.

The separate interlevel argument being developed by A3 uses contact
with the actual period-$p$ field and quotient ramification. It
contains an extra arithmetic input absent from (1)--(9) and is
therefore outside this method-specific limitation.

No mathematical program was executed. All equalities and
inequalities above were checked algebraically, including $h=1$,
empty prefix $a=0$, valuation normalization, and inequality
directions. The original full-inertia question remains unresolved
in this package.
