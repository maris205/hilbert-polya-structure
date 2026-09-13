# All iterates: finite-orbit Artin–Schreier classes of a quadratic Hénon map

Date: 2026-09-07. Author proof, not an independent verdict or a manuscript.
This strengthens the scalar classification by controlling every finite orbit,
including periods divisible by the characteristic. It is not derived by
assuming that finite-order matrices are diagonalizable.

## Claim

Let $K$ be algebraically closed of characteristic $p>2$, let $c\in K$,
and put $A=K[x,y]$, $F=(x^2+c-y,x)$, $\sigma=F^*$ and
$Q=A/\{h^p-h:h\in A\}$ as an additive $\mathbb F_p$-vector space.
The finite-orbit subspace
$$
Q_{\mathrm{fin}}=\{v\in Q:\sigma^Nv=v\text{ for some integer }N\ge1\}
$$
is
$$
\boxed{Q_{\mathrm{fin}}=
\begin{cases}
\mathbb F_3\cdot[q^3xy],&p=3,\ c\ne0,\ q^2=-1/c,\\
0,&\text{otherwise}.
\end{cases}}
\tag{M1}
$$
In the nonzero case $\sigma$ acts as $-1$. In particular, simultaneously
for every $N\ge1$ and $\lambda\in\mathbb F_p^*$,
$$
\boxed{
Q^{\sigma^N=\lambda}=
\begin{cases}
\mathbb F_3\cdot[q^3xy],&p=3,\ c\ne0,\ \lambda=(-1)^N,\\
0,&\text{otherwise}.
\end{cases}}
\tag{M2}
$$
Thus the same unique unmarked cyclic degree-$p$ étale cover is the only
one that can admit a lift of any positive iterate of $F$. In the exceptional
case every iterate lifts; its deck action is $(-1)^N$ and is commuting
exactly for even $N$.

## Status and assumptions

`PROVABLE AS STATED / AUTHOR PROOF COMPLETE`, pending new narrow independent
check. All polynomial supports are allowed. No characteristic-two, nonclosed
base-field, higher-degree or general noncyclic-cover conclusion is asserted.
No numerical test, finite enumeration or external operation is used.

## Notation and matrix statement

For a positive integer $r$ and $T\in\mathrm{GL}_r(\mathbb F_p)$, let
$$
L_T=\sigma-T:A^r\longrightarrow A^r,
\quad C_T=A^r/(L_TA^r+K^r).
$$
The action of $\sigma$ is componentwise. For a vector $h$, write
$h^{[p]}$ for componentwise $p$th powers, and let
$\Phi\langle h\rangle=\langle h^{[p]}\rangle$ on $C_T$.
All powers of $T$ below are matrix powers, whereas $[p]$ is componentwise
Frobenius. Set $u=\langle x\rangle$ as a scalar orbit symbol; $tu$ for
$t\in K^r$ means the coinvariant of the vector polynomial $tx$.

The stronger intermediate result is
$$
\boxed{
\ker(\sigma-T:Q^r\to Q^r)=
\begin{cases}
\{a[q^3xy]:a\in\ker(T+I:\mathbb F_3^r\to\mathbb F_3^r)\},
&p=3,\ c\ne0,\\
0,&\text{otherwise}.
\end{cases}}
\tag{M3}
$$

## Proof strategy and dependency map

1. The vector-valued binary-word orbit basis gives one copy of $K^r$ per
   nonempty orbit in $C_T$, with $T$-weighted obstruction coefficients.
2. The scalar AS bridge extends directly to vectors because $T$ has entries
   in $\mathbb F_p$ and is invertible. This step is proved below.
3. The repaired [highest-orbit argument](PAPER30_AS_SHIFT_FORMULA_ERRATUM_20260907.md)
   and [dual-weight proof](PAPER30_AS_ODD_PRIME_EXCEPTION_PROBE_20260907.md)
   remain valid with nonzero vector coefficients: each surviving target
   has exactly one possible contributing word. The precise uses are given
   below, rather than diagonalizing $T$.
4. The single-letter vector formula identifies every remaining fixed
   vector, yielding (M3).
5. A cyclic permutation matrix encodes any finite orbit in $Q$, proving
   (M1), and finite multiplicative order of $\lambda$ proves (M2).
6. The cover consequence uses the already explicit lifting criterion in
   [the full odd-characteristic scalar classification](PAPER30_AS_FULL_ODD_CLASSIFICATION_20260907.md).

## Proof

### Step 1. Matrix-weighted orbit obstructions

Use the binary-word basis $M_e=\prod_iX_i^{e_i}$, with finite binary
support, $X_0=x$, $X_{-1}=y$, $X_i^2=X_{i-1}+X_{i+1}-c$, and
$\sigma M_e=M_{\sigma e}$. Its ordinary monic triangularity and infinite
nonempty shift orbits are unchanged by taking $r$ copies of $A$.

On one nonempty orbit write a vector polynomial as $\sum_j c_j\sigma^jM_O$,
where the vectors $c_j\in K^r$ have finite support. Define
$$
\ell_{O,T}(h)=\sum_j T^j c_j\in K^r.
\tag{M4}
$$
The coefficient equation for $L_Tb=h$ is
$b_{j-1}-Tb_j=c_j$. Its obstruction is (M4), and when (M4) vanishes a
finite-support solution is
$$
b_j=-T^{-j-1}\sum_{k\le j}T^k c_k.
$$
The formula vanishes on both sufficiently long tails and satisfies the
coefficient equation by subtraction. A homogeneous finite-support solution
is zero, since $b_{j-1}=Tb_j$ and $T$ is invertible. Consequently each
nonempty orbit contributes exactly $K^r$ to $C_T$, and
$$
L_Ts\in K^r\quad\Longrightarrow\quad s\in K^r.
\tag{M5}
$$
Constants are removed in the definition even if $T$ has eigenvalue $1$.

### Step 2. The vector AS bridge

Componentwise Frobenius commutes with $T$ because its entries belong to
$\mathbb F_p$. Thus $L_T(h^{[p]})=(L_Th)^{[p]}$, $\Phi$ is well-defined,
and $L_T\wp=\wp L_T$ componentwise.
There is an $\mathbb F_p$-linear isomorphism
$$
\ker(\sigma-T:Q^r\to Q^r)\ \simeq\ \operatorname{Fix}(\Phi:C_T\to C_T).
\tag{M6}
$$
For a vector class $[g]$ in the left side, choose $h$ such that
$L_Tg=\wp(h)$ and send $[g]$ to $\langle h\rangle$. Another choice of $h$
differs by $\mathbb F_p^r\subset K^r$, and replacing $g$ by $g+\wp(s)$
replaces $h$ by $h+L_Ts$. The map is well-defined and lands in the fixed space.

For injectivity, if $h=L_Ts+a$ with $a\in K^r$, then
$L_T(g-\wp(s))=\wp(a)\in K^r$. Equation (M5) makes $g-\wp(s)$ constant;
componentwise surjectivity $\wp(K)=K$ then makes $[g]=0$. For surjectivity,
write $\wp(h)=L_Tg+a$ for a fixed coinvariant; choose $b\in K^r$ with
$\wp(b)=-a$. Then $L_Tg=\wp(h+b)$, and its class maps to $\langle h\rangle$.
This proves (M6), without any semisimplicity assumption.

### Step 3. The scalar support bounds apply to nonzero vector coefficients

Define $\delta(v)$ as the largest minimum ordinary degree of an orbit
with nonzero vector obstruction. Choose one minimum-degree source word
per such orbit. If $D=\delta(v)$ has a strong-balanced top source,
its Frobenius-leading exponent pair $(pa,pb)$ has target orbit minimum
$pD$. No lower ordinary term reaches it. The repaired adjacent-minima
argument shows that no distinct selected top source reaches its target
orbit either. Its surviving vector is $T^j t^{[p]}$ for some integer $j$
and nonzero source vector $t$. Frobenius on a field is injective and $T$
is invertible, so this vector is nonzero. Therefore $\delta(\Phi v)=pD$.

Otherwise all top support is on the unique odd-reflection orbit of degree
$D=3n+1$. For $n\ge1$ the dual-weight proof gives exactly the same
target minimum $pD-(p-1)/2$, strictly above both $p(D-1)$ and $D$.
Among target representatives within ordinary degree $pD$ only $W_0,W_1$
exist; the $U=2a+b$ bound excludes $W_1$. These statements concern the
word polynomials alone and are independent of their coefficient vectors.
The only remaining target vector is again $T^j t^{[p]}\ne0$; all lower
sources are excluded by the target minimum. Thus every fixed vector lies
on the single-letter block $K^r u$.

For $p\ge5$, the boundary word in the scalar proof has coefficient
$\binom{(p-1)/2}{\lfloor(p-1)/4\rfloor}\ne0$ and is the unique minimum
$V=a+2b$ representative of its orbit. Its non-single-letter target vector
is that nonzero scalar times $T^j t^{[p]}$, with no possible partner.
Hence $\Phi(tu)$ has a non-single-letter component whenever $t\ne0$,
and the fixed space is zero. This checks each cancellation argument in
the matrix setting; it never replaces vector coefficients by an eigenbasis.

### Step 4. The characteristic-three single-letter matrix block

Let $p=3$ and $E=\langle X_0X_1\rangle$ be the two-letter orbit symbol.
The relation between its adjacent representatives is now multiplication
by $T^{-1}$ rather than $\lambda^{-1}$. Therefore
$$
\Phi(tu)=(I+T^{-1})t^{[3]}E-ct^{[3]}u.
\tag{M7}
$$
The distinct orbit summands $K^rE$ and $K^ru$ are independent. A vector
$tu$ is fixed precisely when
$$
(T+I)t^{[3]}=0,\qquad -ct^{[3]}=t.
\tag{M8}
$$
For $c=0$ this forces $t=0$. For $c\ne0$, choose $q$ with $q^2=-1/c$.
The second equation of (M8) holds if and only if $t=qa$ for
$a\in\mathbb F_3^r$, component by component. The first then holds if
and only if $(T+I)a=0$.

Write $g_0=q^3xy$. The scalar identity $(\sigma+1)g_0=\wp(qx)$ gives,
for such an $a$,
$$
L_T(ag_0)=a(\sigma+1)g_0=\wp(aqx),
$$
using $Ta=-a$ and $a^{[3]}=a$. Its bridge image is exactly $qau$.
The bridge isomorphism therefore proves (M3), including exhaustiveness.

### Step 5. Finite orbits and arbitrary iterate eigenclasses

If $v\in Q$ satisfies $\sigma^Nv=v$, form
$$
G=(v,\sigma v,\ldots,\sigma^{N-1}v)\in Q^N.
$$
Let $T$ be the cyclic permutation matrix sending a column
$(w_0,\ldots,w_{N-1})$ to $(w_1,\ldots,w_{N-1},w_0)$. Then
$\sigma G=TG$ and (M3) applies. Outside the exceptional characteristic
and parameter, $G=0$. In the exceptional case every component is an
$\mathbb F_3$ multiple of $[g_0]$, so $v$ is in that single line.
Conversely $(\sigma+1)[g_0]=0$, proving that this line is finite-orbit.
This proves (M1), even when $p\mid N$; the matrix proof did not use a
factorization of its characteristic polynomial or divide by $N$.

If $\sigma^Nv=\lambda v$ with $\lambda\in\mathbb F_p^*$, let $d$ be
its finite multiplicative order. Then $\sigma^{Nd}v=v$, so (M1) applies.
The action on the sole possible line is $-1$, which proves (M2).

Finally a cyclic degree-$p$ connected cover admits a lift of $F^N$
exactly when its nonzero defining class satisfies such an eigen-equation.
The unique cover in the exceptional case already has the explicit lift
of $F$ given in the scalar classification, so its $N$th iterate supplies
a lift of $F^N$. Its conjugation on the deck group is $(-1)^N$.
Every lift differs by a deck transformation, which does not change that
conjugation. The commuting criterion follows. $\square$

## Corrections, boundaries and open risks

- The argument handles nonsemisimple $T$, including the cyclic matrix when
  the period is divisible by $p$; merely diagonalizing it would not suffice.
- The coefficient system is constant over $\mathbb F_p$. Replacing $T$
  by an arbitrary matrix over $K$ would break Frobenius commutation.
- The vector extension proves a complete finite-orbit statement, not that
  all of the infinite-dimensional space $Q$ vanishes.
- No conclusion about nonabelian or higher $p$-power covers is claimed.
- The new matrix obstruction, bridge, vector noncancellation, single-letter
  block and finite-orbit reduction all still require narrow independent
  checking before a mathematical acceptance is recorded.
- The scalar proofs and their completed/pending review states remain
  separate; this new author theorem does not change their frozen inputs.
