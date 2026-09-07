# Three author-side desk proofs and exact boundaries

Author: `/root/twentieth_algebra_scout`, 2026-09-06 UTC.
Status: **PROVABLE AS STATED** for the explicitly stated lemmas below;
**NOT CURRENTLY JUSTIFIED** for a fresh, unconsumed two-axis paper contract.
These are original author deductions for subtraction/triage, not an
independent review, numerical theorem or global novelty claim.

## Assumptions, notation and dependency map

The three total maps and their full carriers are fixed in INTAKE.md. Height
means first entrance into the periodic core. The order of a nonzero scalar
is its multiplicative order. Empty products and empty least common multiples
are one. No assertion depends on a finite enumeration.

1. D1: diagonal Frobenius plus entrywise commutator equations -> exact
   iterates -> image/core and pointwise period -> independent scalar inverse
   equations and extrema. This same coordinate template consumes the package.
2. D2: solve three word equations -> a square-root source-set bijection ->
   odd-order unique divisibility -> singleton fibres and recurrence only.
3. D3: anisotropic reflection identity, with the declared no-op branch ->
   norm preservation -> an explicit three-column coefficient matrix ->
   Gram factor. A factor is not a temporal classification or inverse solution.

## 1. D1: exact full-time scalar normal form

Let $A\in\operatorname{UT}_n(\mathbb F_q)$, put $a_i=a_{ii}$, and write
$x_{ij}=a_{ij}$ for $i<j$. Its literal update is

$$a_i\longmapsto a_i^p,\qquad
x_{ij}\longmapsto(a_i-a_j)x_{ij}.\tag{1}$$

This follows by multiplying a diagonal matrix on the two sides: the
$ij$ entries are $a_i x_{ij}$ and $x_{ij}a_j$. It also proves carrier
closure. For $t\geq1$, define $N_t=1+p+\cdots+p^{t-1}$.
Induction on $t$ in (1), using Frobenius additivity, gives

$$a_i(t)=a_i^{p^t},\qquad
x_{ij}(t)=x_{ij}(a_i-a_j)^{N_t}.\tag{2}$$

At the induction step the new multiplier is
$a_i^{p^t}-a_j^{p^t}=(a_i-a_j)^{p^t}$, giving $N_{t+1}=N_t+p^t$.
There is no zero-to-zero exponent ambiguity because $N_t\geq1$.

### 1.1 Core and exact height

Let

$$\mathcal R=\{A:x_{ij}=0\text{ whenever }a_i=a_j\}.$$

Equality of two diagonal entries is preserved and reflected by Frobenius.
Equation (1) therefore sends every state into $\mathcal R$. Restricted to
$\mathcal R$, it is a bijection: recover each diagonal by the unique
inverse Frobenius; when two recovered entries differ, divide the target
off-diagonal entry by their nonzero difference; when they agree, both
source and target off-diagonal entries in $\mathcal R$ are zero. Thus
$\mathcal R$ is exactly the periodic core. A state outside it enters in
one step and cannot recur outside it. Consequently

$$\tau(A)=\begin{cases}
1,&\exists i<j:\ a_i=a_j,\ x_{ij}\ne0,\\
0,&\text{otherwise}.
\end{cases}\tag{3}$$

The sharp global height is zero for $n=1$ and one for $n\geq2$, witnessed
by $E_{12}$ in the latter case. This is a one-layer erasure followed by a
permutation, not a new growing clock.

### 1.2 Exact pointwise eventual period

Let $s$ be the least positive integer with $a_i^{p^s}=a_i$ for every $i$.
It exists and divides $r$: it is the orbit length of the diagonal tuple
under a permutation whose $r$th power is identity. For $a_i\ne a_j$ set

$$c_{ij}=(a_i-a_j)^{N_s}.$$

All $a_i$ and their differences belong to $\mathbb F_{p^s}$. Hence
$c_{ij}\ne0$ and
$c_{ij}^{p-1}=(a_i-a_j)^{p^s-1}=1$, so $c_{ij}\in\mathbb F_p^*$.
After each block of $s$ steps the diagonal returns and (2) multiplies
$x_{ij}$ by exactly $c_{ij}$. Any return must use a multiple of $s$;
among such times $s\ell$, each nonzero surviving entry returns exactly
when $c_{ij}^{\ell}=1$. Therefore the eventual period of every source is

$$P(A)=s\,\operatorname{lcm}_{\substack{i<j\\a_i\ne a_j,\ x_{ij}\ne0}}
\operatorname{ord}(c_{ij}).\tag{4}$$

For a transient source, its first image has the same support on unequal
diagonal pairs and Frobenius-conjugate diagonal differences; each $c_{ij}$
is unchanged because it lies in $\mathbb F_p$. Thus (4) applies to its
eventual cycle as well. In particular $P(A)\mid s(p-1)$. At $p=2$ every
$c_{ij}=1$ and the period is precisely $s$. At $n=1$ or with no surviving
off-diagonal support, the empty lcm is one and the formula gives the
diagonal Frobenius period.

### 1.3 All targets, every positive time, and every maximizing target

Fix $t\geq1$ and an arbitrary upper triangular target $Y=(y_{ij})$.
There is a unique possible input diagonal $a$ satisfying
$a_i^{p^t}=y_{ii}$. Let

$$m(Y)=|\{(i,j):i<j,\ y_{ii}=y_{jj}\}|.$$

Frobenius is bijective, so input diagonal equality is equivalent to the
displayed target equality. Equation (2) now gives

$$|(T^t)^{-1}(Y)|=
\begin{cases}
q^{m(Y)},&y_{ij}=0\text{ whenever }i<j,\ y_{ii}=y_{jj},\\
0,&\text{otherwise}.
\end{cases}\tag{5}$$

Indeed each unequal pair fixes its input by division by a nonzero
coefficient, and each equal pair supplies $q$ freely chosen entries if
its target entry is zero, otherwise none. Distinct entries are independent,
and the diagonal has no further choice. This proves the exact source-set
description as well as its cardinality; it is not a coefficient-extraction
encoding awaiting evaluation.

Since $m(Y)\leq\binom n2$, the maximum is $q^{\binom n2}$.
For $n\geq2$, equality of all pairs forces a constant diagonal, and
reachability forces all upper off-diagonal entries zero. Conversely every
$Y=cI$ realizes that maximum. At $n=1$ every target is scalar and has
one predecessor, so the same equality description still holds. There are
exactly $q$ maximizing targets, at every $t\geq1$.

### 1.4 What the adapter subtracts

Equations (1)--(5) expose the **whole** result as a finite cyclic base
permutation plus independent scalar actions with a zero-multiplier erase
branch. In a return block, the only added coefficient is the elementary
finite-field norm $c_{ij}$; the period is the lcm of scalar orders. The
entire inverse is independent equations $cx=y$ with the coefficient fixed
by a uniquely recovered diagonal. No noncommutative coupling of upper
entries remains in these coordinates. In particular it is less, not more,
than P175's need to sum over possible diagonals/support colourings.

The old NL13 literal $(a,b)\mapsto(a,ab)$ and the full CS gate supply
exact historical scalar-action precedents; P175 supplies the actual
state-diagonal commutator formula. D1 is **not literally equal or claimed
conjugate** to any of them. The consumed template, not a title match, is
the reason for **NO_PROMOTION**. No mathematical impossibility statement
about every imaginable retained-diagonal variant is implied.

## 2. D2: a complete square-root fibre adapter

This lemma is stronger than the stated carrier: let $G$ be any finite
group, with no commutativity assumption. For every target $(A,B,C)$ the
map

$$r\longmapsto
\bigl(rB^{-1},\ B r^{-1}A,\ A^{-1}r\bigr)\tag{6}$$

is a bijection from $\{r\in G:r^2=ACB\}$ onto
$T^{-1}(A,B,C)$.

To prove necessity, suppose $ab=A$, $bc=B$, $ca=C$. Put $r=abc=aB$.
Associativity gives $r^2=abcabc=(ab)(ca)(bc)=ACB$. Solving successively
gives $a=rB^{-1}$, $b=B r^{-1}A$, and $c=A^{-1}r$.
Conversely the triple in (6) has first product $A$ and second product
$B$ by adjacent cancellation. Its third product is
$A^{-1}r^2B^{-1}=A^{-1}ACBB^{-1}=C$. Finally a recovered source gives
back $r=aB$, so no roots or sources are overcounted. Thus

$$|T^{-1}(A,B,C)|=|\{r:r^2=ACB\}|.\tag{7}$$

If $G$ has odd order, its exponent $m$ is odd, since every element order
divides $|G|$. Choose an integer $k$ with $2k\equiv1\pmod m$.
For every $g\in G$, $(g^k)^2=g$; for any square root $r$ of $g$,
$r=(r^2)^k=g^k$. This uses powers of one element only, not a false
commutativity assumption on different elements. Every target in (7)
therefore has exactly one predecessor. Since $|H_p|=p^3$ is odd, D2 is
a permutation and all its states are recurrent.

Neither a sharp family-wide period formula nor a global cycle census is
provided. More importantly, the requested inverse axis is exactly
singleton inversion in this carrier. For even groups (7) remains valid,
but merely transfers the inverse question to the classical square-root
count; it does not create an evaluated all-group temporal theorem.

The old S04 rectangular-band and NL09 truncated-word updates have this
same three-product word pattern on different semigroups. They are not
equal maps on $H_p^3$ and no conjugacy to them is used. The decisive
rejection here is the new explicit square-root adapter and absent
independent axis, **not** a borrowed historical cycle table.

## 3. D3: norm preservation and a Gram factor, no completed contract

For the fixed nondegenerate symmetric form $B$ over odd $q$, take one
coordinate with $s=s_i$ and $u=u_i$. When $Q(s)\ne0$ set
$a=-2B(u,s)/Q(s)$. Bilinearity gives

$$Q(u+as)=Q(u)+2aB(u,s)+a^2Q(s)=Q(u).\tag{8}$$

When $Q(s)=0$, the defined output is $u$ and the same norm equality
holds. Thus each labelled $Q(u_i)$ is invariant, and the all-triple
carrier is closed. This argument includes $s=0$, nonzero isotropic
directions, zero input vectors and dependent triples. It proves neither
simultaneous involutivity nor bijectivity: changing the other vectors
changes the next reflecting directions.

Let $U$ be the $d\times3$ matrix with columns $u_i$, in a fixed basis
of $V$, and let $H=(B(u_i,u_j))$ be its Gram matrix. For
$\{i,j,k\}=\{1,2,3\}$ define

$$a_i(H)=\begin{cases}
-2(H_{ij}+H_{ik})/(H_{jj}+2H_{jk}+H_{kk}),
 &H_{jj}+2H_{jk}+H_{kk}\ne0,\\
0,&H_{jj}+2H_{jk}+H_{kk}=0.
\end{cases}$$

Define $C(H)$ by column $i=e_i+a_i(H)(e_j+e_k)$, where $e_1,e_2,e_3$
are the standard coordinate vectors in $\mathbb F_q^3$. The literal
update is exactly

$$U'=U C(H),\qquad H'=C(H)^{\mathsf T}H C(H).\tag{9}$$

The first equation is just the three simultaneous reflection formulas;
the second follows by evaluating $B$ on their linear combinations.
Consequently the span of the three vectors never increases, and the
Gram projection is a factor to a rationally specified, total map on
the realized symmetric $3\times3$ Gram matrices. There are at most
$q^6$ such matrices; the three diagonal entries are constant by (8).

Equation (9) does not say that $C(H)$ is always invertible, nor that the
Gram factor is a conjugacy. The information lost by a Gram matrix can
matter for lifted periods and predecessor multiplicities. Even a complete
finite quotient calculation for one $q$ would not prove an all-$q$
classification. Generic finite-linear/Fitting analysis of a return product
of the $C(H)$ matrices, if eventually used, would have to be subtracted.

The old REF map is $(u,v)\mapsto(v,2B(u,v)v-u)$ on a unit conic for
$p\equiv3\pmod4$. D3 has three vectors, independently recomputed sum
directions and explicit isotropic no-op branches. There is no established
literal equality, conjugacy or transferred conic-period formula. The
classical reflection identity is fully spent, and norm preservation plus
this unevaluated factor does not supply a temporal theorem or a full-target
inverse/extremum. D3 closes **HOLD_PROOF / NO_PROMOTION**, with external
literal ownership unresolved. No pilot was used to pretend otherwise.

## Final proof boundary

D1's complete results are consumed by its exposed scalar/Frobenius
template. D2's full inverse is exactly a square-root problem and singleton
on the proposed carrier. D3 has only local identities and a factor, with
both requested global obligations open. The conjunction needed for fresh
admission is therefore **NOT CURRENTLY JUSTIFIED** for each of the three.
There is no reserve or claimed new theorem paper.
