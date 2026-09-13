# Independent parameter check: exact first cancellation times

Date: 2026-09-05. Bounded independent proof check by
`p29_periodic_lifting`. The input is the scalar parameter subsystem,
not the separate multivariate degree theorem. This report changes
neither the original failed parameter draft nor the periodic-lift report.
No candidate PASS, paper acceptance, or product acceptance is granted.

## Claim

For every integer $m\ge1$, there exists $c\in\mathbb C\setminus\{0\}$
such that, for
$$
R_c(z)=1+\frac{c}{z^4},
$$
the orbit starting at $1$ first hits $0$ after exactly $m$ steps.
Equivalently, $0\mapsto\infty\mapsto1\mapsto\cdots\mapsto0$ is
an exact critical cycle of length $L=m+2$.

The additional proposed formula $\deg A_m=4^{m-1}$ is part of the
input and is checked separately rather than silently assumed.

## Status

**Original exact-degree and original counting formulas: REFUTED.**
Already $\deg A_3=17$, not $16$. This is consistent with the explicit
failure retained in
[the original author draft](PAPER29_CANCELLATION_PARAMETER_PROOF_20260905.md).

**Existence claim: PROVABLE AS STATED over nonzero complex parameters.**
With the corrected degrees, the root-return multiplicities are constant,
the divisor-count identity is valid, and its primitive count is positive.
Neither simple parameter roots nor a transversality theorem is needed.
In fact the parameters obtained are nonzero algebraic integers.

**Corrected exact formulas: PROVED.** For $m\ge0$,
$$
d_m:=\deg A_m=\left\lfloor\frac{4^{m+1}}{15}\right\rfloor
=\begin{cases}
(4^{m+1}-1)/15,&m\text{ odd},\\
(4^{m+1}-4)/15,&m\text{ even}.
\end{cases}                                                    \tag{1}
$$
For $L\ge3$, put $b_L=d_{L-2}$. If $w_L$ is the sum of the
multiplicities in $A_{L-2}$ of parameters with first hit at $L-2$, then
$$
b_L=\sum_{d\mid L,\ d\ge3}w_d,\qquad
w_L=\sum_{d\mid L,\ d\ge3}\mu(L/d)b_d>0.                      \tag{2}
$$

## Assumptions and notation

All factorizations and local expansions are over $\mathbb C$. The
parameter $c=0$ is excluded. Define
$$
A_0=1,\quad A_1=1+c,\quad
A_{m+1}=A_m^4+cA_{m-1}^{16}\quad(m\ge1).
$$
Orders of vanishing are measured in the local coordinate
$t=c-c_*$. A root of order $\nu$ is counted $\nu$ times. The proof
does not infer the number of distinct roots from their total order.

The degree-four map is taken on $\mathbb P^1$, so $R_c(0)=\infty$
and $R_c(\infty)=1$. Near $0$, its reciprocal is
$z^4/(z^4+c)$, and near $\infty$ its difference from $1$ is
$cw^4$, where $w=1/z$. Both points are critical with local degree four.
The parameter assumption $c\ne0$ is used in these local assertions.

## Proof strategy and dependency map

1. Prove coprimality and the exact numerator recurrence before using
   polynomial degrees or interpreting zero parameters.
2. Compute degrees by strict comparisons, so cancellation of leading
   terms cannot enter the induction.
3. Classify all repeated zero times for each root parameter on
   $\mathbb P^1$.
4. Produce a holomorphic full-return germ through $0$, despite the
   intermediate visit to $\infty$; use its order-$16$ remainder to
   prove unchanged parameter-root multiplicity.
5. Partition the total polynomial degree by exact cycle lengths,
   then use a strict bound on contributions from proper divisors.

## Proof

### 1. Reduced fractions and absence of adjacent common roots

Induction in the recursion gives $A_m\in\mathbb Z[c]$ and
$A_m(0)=1$. A common root of $A_{m+1}$ and $A_m$ would have
$c_*\ne0$ and, by the recursion, $A_{m-1}(c_*)=0$. Induction
backward reaches $A_0(c_*)=0$, a contradiction. Thus
$$
\gcd(A_m,A_{m-1})=1\quad(m\ge1).                              \tag{3}
$$
Substituting a reduced fraction into $1+c/z^4$ now proves, as an
identity in $\mathbb C(c)$,
$$
R_c^m(1)=\frac{A_m(c)}{A_{m-1}(c)^4}\quad(m\ge1).             \tag{4}
$$
Its numerator and denominator have no common root by (3).
At any fixed $c_*\ne0$, this fraction also represents the parameter
orbit on $\mathbb P^1$: it never becomes an indeterminate $0/0$.

### 2. Correct degree induction, including strict leading-term tests

The first degrees are
$$
d_0=0,\quad d_1=1,\quad d_2=4,\quad d_3=17,\quad d_4=68.
$$
In particular, the original exponential formula fails at $m=3$:
$A_2^4$ has degree $16$, whereas $cA_1^{16}$ has degree $17$.

Assume (1) holds through index $m$. When $m$ is odd, direct substitution
in the two candidate degrees gives
$$
4d_m-(1+16d_{m-1})=3.
$$
The first summand is therefore strictly larger, and
$d_{m+1}=4d_m=(4^{m+2}-4)/15$. When $m$ is even,
$$
(1+16d_{m-1})-4d_m=1.
$$
The second summand is strictly larger, and
$d_{m+1}=1+16d_{m-1}=(4^{m+2}-1)/15$.
These formulas start from $d_0=0,d_1=1$, prove the induction, and
show there is no tie at any step. The unique dominant summand has
leading coefficient $1$ inductively, so every $A_m$ is monic.

The floor form of (1) follows because $4^{m+1}$ has remainder $1$
modulo $15$ for odd $m$ and remainder $4$ for even $m$.

### 3. Exact cycle length and all subsequent root occurrences

Let $c_*$ be a root of some $A_m$, and choose its first root index
$m_0\ge1$. All earlier orbit values starting from $1$ are finite
and nonzero. A visit to $\infty$ would have required an earlier visit
to $0$, since $0$ is the only pole of $R_{c_*}$.

The first zero is followed by $\infty$ and then by $1$. Thus the
orbit returns to its starting point after $L_0=m_0+2$ steps. This
period is exact. Indeed, a smaller period would return the zero at
an index strictly below $m_0$: reduce $m_0$ modulo that smaller
period; remainder zero would contradict that the initial value is
$1$, and a positive remainder would contradict minimality of $m_0$.
Equivalently, a repeated state before the first zero would trap the
forward orbit in the earlier repeated segment, preventing that first zero.

It follows that the zero times starting from $1$ are exactly
$m_0+kL_0$ for integers $k\ge0$. In terms of numerator roots,
$$
A_m(c_*)=0
\quad\Longleftrightarrow\quad
L_0\mid m+2.                                                  \tag{5}
$$
The equivalence concerns $m\ge1$. Its implication from divisibility
is valid because $m+2$ is then a positive multiple of $L_0$, so the
zero time is at least $L_0-2=m_0$.

### 4. Legitimate local return germ through the pole

Fix such a parameter $c_*$ and its first index $m_0=L_0-2$. Put
$$
\psi(c,z)=R_c^{m_0}(z),\qquad a(c)=\psi(c,1).
$$
The rational function $\psi$ is holomorphic in a product neighborhood
of $(c_*,1)$. To verify this, follow the first $m_0$ iterates: every
input before the terminal zero is finite and nonzero. Continuity
preserves this condition in sufficiently small neighborhoods at
each of the finitely many composition stages. The terminal output
may be zero; it does not occur as an input to another map in $\psi$.

Direct calculation gives
$$
R_c^2(z)=1+\frac{cz^{16}}{(z^4+c)^4}.                          \tag{6}
$$
This expression is holomorphic near $(c_*,0)$, since $c_*\ne0$.
Combining (6) with the preceding neighborhood for $\psi$ gives a
holomorphic full-return map
$$
\Phi(c,z):=R_c^{L_0}(z)
=\psi\left(c,1+\frac{cz^{16}}{(z^4+c)^4}\right)
=a(c)+z^{16}b(c,z),                                          \tag{7}
$$
where $b$ is holomorphic near $(c_*,0)$. The last equality is the
Taylor expansion of $\psi$ about its second argument $1$; its
constant term is $a(c)$, and every remaining term is divisible by
$z^{16}$. Thus the intermediate pole does not invalidate (7).

For completeness, the remainder really has order sixteen in $z$
at $c_*$: every factor of the derivative of $\psi(c_*,z)$ at $z=1$
is of the form $-4c_*/z_j^5\ne0$, since the input values are finite
and nonzero. Consequently
$b(c_*,0)=c_*^{-3}\partial_z\psi(c_*,1)\ne0$. This extra unit
property is not required for the parameter-multiplicity argument.

### 5. Constant parameter-root multiplicity at every return

Let $\nu$ be the multiplicity of $c_*$ in $A_{m_0}$. By (3), the
denominator in (4) at $m_0$ is a unit, so
$\operatorname{ord}_{c_*}a=\nu\ge1$. For $k\ge1$, set
$$
u_k(c)=R_c^{kL_0-2}(1).
$$
As rational functions, $u_1=a$ and $u_{k+1}=\Phi(c,u_k)$.
These compositions may also be interpreted successively as
holomorphic germs, since $u_k(c_*)=0$ by (5). Equation (7) gives
$$
u_{k+1}=a+u_k^{16}b(c,u_k).                                  \tag{8}
$$
There is an entirely formal version: use $t=c-c_*$, regard
$a\in t^\nu\mathbb C[[t]]$ and $b\in\mathbb C[[t,z]]$, and
compose only series with zero constant term. If $u_k$ has order
$\nu$, then the second term in (8) has order at least $16\nu$,
strictly larger than $\nu$. It cannot cancel the leading term of
$a$, so $u_{k+1}$ also has order exactly $\nu$. Induction yields
$$
\operatorname{ord}_{c_*}u_k=\nu\quad(k\ge1).                 \tag{9}
$$
At each index $kL_0-2$, the adjacent denominator in (4) is nonzero
by (3). Thus (9) is exactly the statement that the multiplicity of
$c_*$ in every $A_{kL_0-2}$ equals its original multiplicity in
$A_{L_0-2}$. Analytic and formal arguments agree; neither assumes
that $\nu=1$.

### 6. Degree partition and positivity of the primitive count

Define $E_L$ as the parameters with first zero time $L-2$, and
let $w_L$ count their multiplicities in $A_{L-2}$. This is a finite
nonnegative integer, because $E_L$ is a subset of a polynomial's
roots. Every root of $A_{L-2}$ belongs to a unique $E_d$ with
$d\mid L$ and $d\ge3$, by (5). Section 5 shows that its
multiplicity is its original multiplicity. Factoring over
$\mathbb C$ therefore gives the first identity in (2).

Möbius inversion gives the second equality in (2); one can define
$b_1=b_2=w_1=w_2=0$ to use the usual divisor-sum notation.
In particular $0\le w_d\le b_d$. The initial values are
$$
w_3=1,\qquad w_4=4,\qquad w_5=17,\qquad
w_6=67,\qquad w_7=273,\qquad w_8=1088.
$$
For the general positivity proof, the degree recursion implies
$d_m\ge4d_{m-1}$ for $m\ge2$, hence
$$
b_L=d_{L-2}\ge4^{L-3}\quad(L\ge3).
$$
Formula (1) also gives $b_d\le4^{d-2}$ for $d\ge3$.
If $L\ge6$, every proper positive divisor of $L$ is at most
$N=\lfloor L/2\rfloor$. Therefore
$$
\sum_{d\mid L,\ 3\le d<L}w_d
\le\sum_{d=3}^{N}b_d
\le\sum_{d=3}^{N}4^{d-2}
=\frac{4^{N-1}-4}{3}
<4^{L-3}\le b_L.                                             \tag{10}
$$
The strict inequality uses $N-1\le L-3$. Subtracting in (2)
shows $w_L>0$. For $L=3,4,5$ there is no proper divisor at least
three, so $w_L=b_L>0$ directly. Thus $E_L$ is nonempty for every
$L\ge3$.

Finally, every parameter in $E_L$ is a root of the monic integer
polynomial $A_{L-2}$ and is nonzero because $A_{L-2}(0)=1$.
It is therefore a nonzero algebraic integer. This proves the
existence claim, its exact first-hit indexing, and the corrected
multiplicity-weighted formulas. $\square$

## Corrections or missing assumptions

- Replace $4^{m-1}$ by (1), and replace $4^{L-3}$ in the exact
  divisor and Möbius identities by $b_L=\lfloor4^{L-1}/15\rfloor$.
  The old exponential is still a valid lower bound, which is why
  the existence argument survives its failure as an equality.
- Preserve the original failed proof as failed. This check does
  not retroactively make its displayed exact formulas true.
- The domain is nonzero complex parameters, with algebraic examples
  proved. No existence theorem for real parameters of every period
  is asserted here.
- Root simplicity is unnecessary. The proof counts multiplicities
  and establishes that each root's multiplicity stays unchanged
  at repeated returns.

## Open risks and scope boundary

There is no remaining gap in the scalar existence proof under its
stated complex-parameter assumptions. This check does not establish
the separate multivariate polynomial map's leading coefficient
recursion, the exact time at which its total degree drops, its
post-cancellation degree behavior, literature novelty, or long-paper
value. Those require their own actual evidence and cannot be inferred
from the scalar parameter theorem.
