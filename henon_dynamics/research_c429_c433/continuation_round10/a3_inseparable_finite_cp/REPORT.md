# R10 A3: finite ordinary-cycle product detection for inseparable polynomials

2026-09-09 UTC (actual tool clock). One bounded complete-question proof
scout, not an admission.

## Frozen question and candidate bound, before proof

For every prime $p$, put $k=\overline{\mathbb F}_p$. Let $f\in k[x]$
have degree $d\ge2$ and $f'=0$. Let $g=A/B\in k(x)^\times$, where
$A,B\in k[x]\setminus\{0\}$ are coprime and
$m=\max(\deg A,\deg B)\ge0$. There is no norm-one condition, no
monomial/one-parameter restriction on $f$, and no condition on the
individual multiplicities in $A$ or $B$.

The exact question is whether a coefficient-independent finite return
bound depending only on $d,m$ decides the following condition (CP):
all but finitely many ordinary primitive $f$-cycles avoid the zeros
and poles of $g$ and have native product $\prod_{x\in O}g(x)=1$.
The clock is one application of the original $f$; every native period,
including multiples of $p$, is retained. Affine cycles are used;
including the single fixed point at infinity does not change a
cofinite condition.

Freeze the proposed constants

$$
a=\left\lceil\frac{m}{d-1}\right\rceil,\qquad b=a+1,
\qquad D=2b^2,\qquad N=3D+1=6b^2+1.
$$

For $n\ge1$, put

$$
F_n=f^{\circ n}-x,\qquad
H_n=\prod_{i=0}^{n-1}A(f^{\circ i}(x))-
    \prod_{i=0}^{n-1}B(f^{\circ i}(x)),\qquad
S_* =\prod_{r=1}^{D}F_r.
$$

The candidate full decision rule is

$$
\mathrm{(CP)}\quad\Longleftrightarrow\quad
F_n\mid S_*H_n\ \text{for every }1\le n\le N.
$$

**Initial status: NOT CURRENTLY JUSTIFIED.** The remaining work is to
prove this exact statement, correct a constant with explicit reason,
or identify its exact gap. Finite sample success, formal Noetherianity,
and the unaccepted R10 A1 rank bridge are not substitutes for proof.
The earlier R9 finite-state proof and the complete R10 A1 author
report have been read as mechanism references; the general-polynomial
transfer, fixed-$S$ bound, rank and persistence steps must be proved
at this new scope here.

Only this allocated report may be written. One mechanism and at most
one targeted source batch are allowed. No mathematical program,
census, new agent, external model/API, GPU, Git, old/shared-file,
manuscript or PDF action is allocated. All UL4 and other earlier
artifacts remain frozen. This scout is not an assertion that (CP)
implies a rational transfer, nor is it a fifth-paper admission.

`NO_BAD_EULER_OR_ROOT_NUMBER` remains unconditional.

## 1. Outcome and exact theorem

**Status: PROVABLE AS STATED.** The complete author proof below retains
the frozen question and constants, without adding an assumption.
Independent mathematical review and source/substantiality adjudication
remain separate gates and are not presumed.

**Theorem 1.1.** Under every hypothesis in the frozen question, define

$$
I_g=\{S\in k[x]: F_n\mid S H_n\text{ for every }n\ge1\}.
\tag{1.1}
$$

Then the following are equivalent:

1. The ordinary cofinite native-cycle product condition (CP) holds.
2. $I_g\ne(0)$.
3. $S_*\in I_g$.
4. $F_n\mid S_*H_n$ for every integer $1\le n\le N$.

In particular, (4) is a coefficient-independent finite return
criterion for (CP), with

$$
N=6\left(\left\lceil\frac{m}{d-1}\right\rceil+1\right)^2+1.
\tag{1.2}
$$

There is an additional precise exceptional-period conclusion. If
(CP) holds and a point $x$ is a root of some $F_n$ with $H_n(x)\ne0$,
then its ordinary least period is at most $D$. This does not assert
that the union of all such points has at most $D$ elements, or that
every cycle meeting the numerator/denominator support has period at
most $D$.

The criterion is stated directly for the original map, including
nonmonic maps. It can be evaluated by polynomial composition,
multiplication, and Euclidean remainders in a finite field containing
the finitely many input coefficients. No field-size-independent
running-time claim or practical census size is asserted, and none
of these tests is executed here.

## 2. Strategy, assumptions, and dependency map

The only assumptions are the frozen ones. In particular, $m=0$,
$p=2$, unequal numerator and denominator degrees, arbitrary common
coefficient fields, and every support multiplicity are included.
The condition $f'=0$ implies $p\mid d$, but the proof neither assumes
that $d$ is a power of $p$ nor replaces $f$ by a Frobenius map.

The single finite-state mechanism has the following dependencies:

1. Actual affine conjugacy reduces the proof to monic $f$ without
   changing $d,m$, ordinary periods, or the stated tests.
2. $F_n'=-1$ makes all return roots simple, identifying $I_g\ne0$
   exactly with (CP), up to the actual finite support cycles.
3. The cyclic degree-$d$ algebra has a digit basis and a
   nondegenerate top-coefficient pairing. A directly proved Laurent
   extractor gives the general-polynomial transfer matrices.
4. Their state inequality gives a closed low range, logarithmic
   contraction of one exceptional $S$-site, and a complete fixed-$S$
   finite-word theorem.
5. For $S=1$, a split tensor has rank at most $D$. Polynomial
   evaluation makes its rank equal to the number of visible return
   points once both halves are long enough.
6. Finite multiplicative orders in $\overline{\mathbb F}_p$ make
   any specified visible cycle persist at arbitrarily long returns.
   Under finite support, its native period is therefore at most $D$.
7. This replaces the unknown annihilator by $S_*$; the fixed-$S$
   theorem then yields exactly the frozen $N$.

No conclusion of the unaccepted R10 A1 theorem is invoked. Its
rank/persistence idea and the accepted R9 construction are mechanism
references; every needed assertion at the present scope is proved
below. The classical word-span cutoff is also proved directly.

## 3. Nonmonic maps: actual conjugacy, not rescaling the dynamics

Let $c_d\ne0$ be the leading coefficient of $f$. Choose $t\in k^\times$
with $c_dt^{d-1}=1$, possible because $k$ is algebraically closed.
For $\phi(y)=ty$, put

$$
\widetilde f=\phi^{-1}\circ f\circ\phi=t^{-1}f(ty),\qquad
\widetilde A(y)=A(ty),\quad \widetilde B(y)=B(ty).
\tag{3.1}
$$

Then $\widetilde f$ is monic, still has derivative zero and degree
$d$, and $\widetilde A,\widetilde B$ are coprime with the same
height $m$. The map $\phi$ bijects ordinary primitive cycles,
preserves their least periods, carries their zero/pole exceptions
bijectively, and preserves the actual products of $g$.

Iteration of the actual conjugacy gives, for the quantities built
from the tilded data,

$$
\widetilde F_n(y)=t^{-1}F_n(ty),\quad
\widetilde H_n(y)=H_n(ty),\quad
\widetilde S_*(y)=t^{-D}S_*(ty).
\tag{3.2}
$$

Consequently each divisibility in Theorem 1.1 is unchanged by this
substitution and nonzero scalar factors. A fixed polynomial $S$
corresponds to $S(ty)$, of the same degree, so fixed-$S$ statements
transfer as well. It suffices to prove the theorem for monic $f$.
The decision rule itself never requires a choice of $t$.

## 4. Simple roots, ordinary products, and the annihilator

For every $n\ge1$, the chain rule gives

$$
(f^{\circ n})'=0,\qquad F_n'=-1.
\tag{4.1}
$$

Thus the monic degree-$d^n$ polynomial $F_n$ has exactly $d^n$
distinct roots in $k$. Put

$$
\mathcal B_n=\{x\in k:F_n(x)=0,\ H_n(x)\ne0\},\qquad
\mathcal B=\bigcup_{n\ge1}\mathcal B_n.
\tag{4.2}
$$

Every root of $F_n$ belongs to an ordinary primitive cycle of least
period dividing $n$. Cyclically permuting the $n$ numerator factors,
and separately the $n$ denominator factors, shows that $H_n$ is
constant along that cycle. Therefore $\mathcal B_n$ is a union of
full native cycles, and $f$ permutes it.

By simple roots, for every polynomial $S$,

$$
F_n\mid SH_n\quad\Longleftrightarrow\quad
S(x)=0\text{ for every }x\in\mathcal B_n.
\tag{4.3}
$$

It follows that $I_g\ne(0)$ if and only if $\mathcal B$ is finite.
Indeed, an infinite set of distinct points cannot all be roots of a
nonzero polynomial. If $\mathcal B$ is finite, the polynomial
$\prod_{x\in\mathcal B}(X-x)$, interpreted as $1$ for an empty
set, generates exactly the ideal in (1.1).

We now prove that this finiteness is equivalent to (CP), including
the support exceptions. Only finitely many periodic cycles can meet
the finite zero/pole support of $g$: distinct cycles are disjoint,
and each such cycle contains a support point. Their full union is
finite, although its cardinality is not bounded here by the number
of support points.

On any cycle $O$ avoiding this support, of least period $r\mid n$,
put $W_O=\prod_{x\in O}g(x)$. At any $x\in O$,

$$
H_n(x)=\left(\prod_{i=0}^{n-1}B(f^{\circ i}(x))\right)
        (W_O^{n/r}-1),
\tag{4.4}
$$

where the prefactor is nonzero. If (CP) holds, outside its finitely
many exceptional cycles and the support cycles, $W_O=1$, so (4.4)
vanishes at every return. Hence $\mathcal B$ is contained in the
finite union of those cycles. Conversely, if $\mathcal B$ is finite,
every admissible cycle with $W_O\ne1$ contributes all its points to
$\mathcal B_r$ at its own native period $r$. Only finitely many
cycles can do so. Together with the finite support cycles, this is
exactly (CP). We have proved (1) $\Longleftrightarrow$ (2).

There is no derivative-induced blindness in (4.3): the derivative
in (4.1) is a nonzero constant, including in characteristic two.

## 5. The cyclic digit algebra and its exact coefficient extractor

For $n\ge1$, let

$$
\mathcal A_n=k[X_0,\ldots,X_{n-1}]/
\bigl(f(X_i)-X_{i+1}:i\bmod n\bigr).
\tag{5.1}
$$

The relations determine $X_i=f^{\circ i}(X_0)$ and then impose
$F_n(X_0)=0$. Thus they give an isomorphism

$$
\mathcal A_n\simeq k[x]/(F_n),\qquad X_i\longmapsto f^{\circ i}(x).
\tag{5.2}
$$

Writing $X_i^d$ in terms of $X_{i+1}$ and the lower-degree terms
of $f(X_i)$ strictly lowers total degree. Therefore the monomials

$$
X^\epsilon=\prod_{i=0}^{n-1}X_i^{\epsilon_i},\qquad
\epsilon_i\in\{0,\ldots,d-1\},
\tag{5.3}
$$

span. Their images in (5.2) are monic of the distinct degrees
$\sum_i\epsilon_i d^i$, ranging over every integer from $0$ to
$d^n-1$. They are independent and form a basis.

Let $L_n$ select the coefficient of $\prod_i X_i^{d-1}$ in this
basis. Under (5.2), it selects the coefficient of $x^{d^n-1}$ in
the remainder of degree below $d^n$. The pairing $L_n(uv)$ is
nondegenerate: if a nonzero remainder $u$ has degree $q$ and
leading coefficient $u_q\ne0$, multiplying by $x^{d^n-1-q}$
produces that top coefficient without reduction. Since (5.3) is
a basis, this proves, for any $U\in\mathcal A_n$,

$$
U=0\quad\Longleftrightarrow\quad
L_n(X^\epsilon U)=0\text{ for every digit word }\epsilon.
\tag{5.4}
$$

Here is the required extractor for a general monic polynomial $f$.
For a polynomial $J$ in the $X_i$, define

$$
\mathscr R_n(J)=
[X_0^{-1}\cdots X_{n-1}^{-1}]
J\prod_{i=0}^{n-1}
\left(\sum_{q_i\ge0}\frac{X_{i+1}^{q_i}}{f(X_i)^{q_i+1}}\right),
\tag{5.5}
$$

where each inverse power of $f(X_i)$ is expanded at infinity.
This coefficient is a finite algebraic sum. To verify that fact,
take one input monomial $\prod_i X_i^{j_i}$ of total degree $J_0$.
An inverse-power term has exponent $-d(q_i+1)-u_i$ with
$u_i\ge0$. The coefficient condition at each variable is

$$
j_i+q_{i-1}-d(q_i+1)-u_i=-1,
$$

and summing gives

$$
J_0-n(d-1)=(d-1)\sum_iq_i+\sum_i u_i.
\tag{5.6}
$$

All indices are nonnegative and hence bounded. Each individual
inverse-power coefficient is finite as well. This justifies the
coefficient rearrangements, without analytic convergence or division
by any integer in characteristic $p$.

Multiplication by $f(X_j)-X_{j+1}$ cancels its geometric series
in (5.5). In the remaining factors there is no negative power of
$X_j$, so their coefficient with $X_j^{-1}$ is zero, even after
multiplication by a polynomial. This proves that $\mathscr R_n$
annihilates the defining ideal. The cancellation is an identity of
the same locally finite coefficient expansions: successive geometric
terms telescope, with the unbounded remainder having no contribution
to any fixed coefficient. It is also valid for $n=1$, when cancellation
leaves a polynomial.

For the top digit monomial, (5.6) forces every $q_i,u_i$ to be zero,
and monicity gives coefficient one. Every other digit monomial
has total degree below $n(d-1)$, so (5.6) forbids a contribution.
Thus $\mathscr R_n$ descends to the quotient and equals $L_n$.

## 6. General-polynomial transfer matrices and the fixed-$S$ theorem

For $h\in k[X]$ and nonnegative integers $r,s$, define

$$
T_h(r,s)=[X^{-1}]\frac{X^r h(X)}{f(X)^{s+1}}.
\tag{6.1}
$$

The same Laurent expansion as above is intended. A nonzero entry
must satisfy

$$
ds\le r+\deg h-d+1.
\tag{6.2}
$$

This follows because the largest exponent of the fraction is
$r+\deg h-d(s+1)$; if it is below $-1$, there is no $X^{-1}$
coefficient. A zero $h$ gives the zero matrix and needs no degree
convention. Factoring the input of (5.5) gives the exact cyclic sum

$$
L_n\left(\prod_i h_i(X_i)\right)=
\sum_{r_0,\ldots,r_{n-1}\ge0}
\prod_iT_{h_i}(r_{i-1},r_i),\qquad r_{-1}=r_{n-1}.
\tag{6.3}
$$

Indeed $r_i$ is the outgoing power $q_i$ of $X_{i+1}$ in (5.5),
so (6.1) extracts exactly the corresponding incoming and outgoing
powers at $X_i$. Finiteness was proved in (5.6).

Fix now $0\ne S\in k[X]$, set $\ell=\deg S$, and put

$$
k_S=\begin{cases}
0,&\ell=0,\\
\lfloor\log_d\ell\rfloor+1,&\ell\ge1.
\end{cases}
\tag{6.4}
$$

For all the digit tests in (5.4), the ordinary factors
$X^\epsilon A$ or $X^\epsilon B$ have degree at most $m+d-1$.
The distinguished factor containing $S$ has degree at most
$m+\ell+d-1$. Therefore (6.2) gives

$$
ds\le r+m\quad\text{at a bulk site},\qquad
ds\le r+m+\ell\quad\text{at the distinguished site}.
\tag{6.5}
$$

At a maximal index of a nonzero cyclic contribution, its incoming
index is no larger. Thus every index is at most
$\lfloor(m+\ell)/(d-1)\rfloor$, and in particular at most

$$R=a+\ell.$$

This last bound holds because $(d-1)a\ge m$ and $d-1\ge1$.
All the matrices below may consequently be restricted to rows and
columns $0,\ldots,R$ without losing any cyclic contribution.
For $\epsilon\in\{0,\ldots,d-1\}$ let

$$
\mathsf M_\epsilon=
\operatorname{diag}(T_{X^\epsilon A},T_{X^\epsilon B}),\qquad
\mathsf B_\epsilon=
\operatorname{diag}(T_{SX^\epsilon A},-T_{SX^\epsilon B}).
\tag{6.6}
$$

Applying (6.3) to the two whole products gives

$$
L_n\left(S(X_0)X^\epsilon H_n\right)=
\operatorname{tr}\left(
\mathsf B_{\epsilon_0}\mathsf M_{\epsilon_1}\cdots
\mathsf M_{\epsilon_{n-1}}\right).
\tag{6.7}
$$

Here $H_n$ is understood through (5.2). For $n=1$ the product
after $\mathsf B$ is the identity. All scalar factors of $g$ are
already in $A$ and appear at each site; no period-dependent phase
has been dropped. The minus sign occurs once, including its usual
interpretation in characteristic two.

The bulk range $0,\ldots,a$ is closed. In fact, from (6.5),

$$s-a\le\frac{r-a}{d}.$$

Starting anywhere in $0,\ldots,R$, after $j$ bulk transitions
every possible index is at most $a+\ell/d^j$. Hence after $k_S$
bulk transitions every index is at most $a$, by the strict inequality
$d^{k_S}>\ell$ when $\ell>0$. When $\ell=0$ it is already in
that range. These are path bounds, not assumptions that nonzero
terms cannot cancel.

Let $\mathsf M^0_\epsilon$ denote the restrictions to the two
closed ranges. They have size $v\times v$, where $v=2b$.
For $n\ge k_S+1$, the input index at the distinguished site of a
cyclic contribution is low, since the preceding $n-1$ bulk sites
include at least $k_S$ transitions. After that site and the first
$k_S$ bulk transitions the output is low again. Define
$\mathsf E_{\epsilon_0\ldots\epsilon_{k_S}}$ to be the low-row,
low-column block of

$$
\mathsf B_{\epsilon_0}\mathsf M_{\epsilon_1}\cdots
\mathsf M_{\epsilon_{k_S}}.
$$

The high intermediate states in this prefix are still summed over.
Every remaining bulk path stays low, so (6.7) becomes

$$
\operatorname{tr}\left(
\mathsf E_{\epsilon_0\ldots\epsilon_{k_S}}
\mathsf M^0_{\epsilon_{k_S+1}}\cdots
\mathsf M^0_{\epsilon_{n-1}}\right).
\tag{6.8}
$$

For completeness, let $W_j$ be the span of all products of the
$d$ matrices $\mathsf M^0_\epsilon$ with length at most $j$,
including the empty product. Then

$$W_{j+1}=W_j+\sum_{\epsilon=0}^{d-1}W_j\mathsf M^0_\epsilon.$$

Equality at one step makes the space stable under all letters and
therefore includes all words. Otherwise its dimension increases
strictly. It starts with dimension one and is contained in a matrix
space of dimension $v^2=4b^2$. Thus words of length at most
$4b^2-1$ span every word product. For each fixed prefix in (6.8),
its trace functional vanishes on all tail words exactly when it
vanishes on those lengths. Including the short cases $n\le k_S$
and using (5.4) proves the full fixed-$S$ theorem:

$$
\left[\forall n\ge1:\ F_n\mid SH_n\right]
\quad\Longleftrightarrow\quad
\left[1\le n\le k_S+4b^2:\ F_n\mid SH_n\right].
\tag{6.9}
$$

The right bracket means every integer in that range. No assumption
about the degree of an unknown exceptional $S$ has entered (6.9).

## 7. Split coefficient rank bounds the visible native periods

Take $S=1$, so the closed range $0,\ldots,a$ suffices throughout.
Use the two-block matrices $M_\epsilon$ from (6.6) on this range,
and put $E=\operatorname{diag}(I_b,-I_b)$. Define

$$
\mathcal T_n(\epsilon)=L_n(H_nX^\epsilon)
=\operatorname{tr}(E M_{\epsilon_0}\cdots M_{\epsilon_{n-1}}).
\tag{7.1}
$$

All products lie in the algebra

$$\mathcal D=\operatorname{Mat}_b(k)\oplus\operatorname{Mat}_b(k),
\qquad\dim_k\mathcal D=2b^2=D.$$

For a cut $1\le h<n$, index a matrix $\mathcal F_{n,h}$ by
digit words $u$ of length $h$ and $v$ of length $n-h$, with entry
$\mathcal T_n(uv)$. The expression $\operatorname{tr}(E M_uM_v)$
is one bilinear pairing on the two elements of $\mathcal D$.
Factoring it through any vector-space basis of $\mathcal D$ gives

$$\operatorname{rank}\mathcal F_{n,h}\le D.
\tag{7.2}
$$

No nondegeneracy of the trace pairing is assumed.

We next compute the same rank from actual ordinary points. For a
monic squarefree polynomial $F_n$ of degree $d^n$, Lagrange
interpolation gives, for every polynomial $R$,

$$
L_n(R)=\sum_{F_n(x)=0}\frac{R(x)}{F_n'(x)}
      =-\sum_{F_n(x)=0}R(x).
\tag{7.3}
$$

To verify the coefficient used here, the interpolation basis
$F_n(X)/((X-x)F_n'(x))$ has top coefficient $1/F_n'(x)$.
The identity first holds for the remainder of $R$ and then for
$R$ itself, since values at roots are unchanged. Equation (4.1)
gives the last equality.

Set $t_n=|\mathcal B_n|$ and $\gamma_n(x)=-H_n(x)\ne0$ on
$\mathcal B_n$. It follows that

$$
\mathcal F_{n,h}=V\operatorname{diag}
(\gamma_n(x):x\in\mathcal B_n)W^{\mathsf T},
\tag{7.4}
$$

where

$$
V_{u,x}=\prod_{i=0}^{h-1}f^{\circ i}(x)^{u_i},\qquad
W_{v,x}=\prod_{i=0}^{n-h-1}f^{\circ i}(f^{\circ h}(x))^{v_i}.
$$

If $d^h\ge t_n$, the left digit polynomials are a monic
triangular basis in every degree below $d^h$, by the same degree
argument as in Section 5. Evaluation at $t_n$ distinct points has
full rank $t_n$: Lagrange polynomials of degree below $t_n$ realize
every value vector. Thus $V$ has full column rank. If
$d^{n-h}\ge t_n$, the same explicit degree argument applies to
$W$, since $f^{\circ h}$ permutes $\mathcal B_n$.

The diagonal matrix in (7.4) is invertible. A left inverse for $V$
and a right inverse for $W^{\mathsf T}$ show that (7.4) has rank
at least $t_n$, and its displayed factorization gives rank at most
$t_n$. Hence

$$
t_n=\operatorname{rank}\mathcal F_{n,h}\le D
\quad\text{if }d^h\ge t_n\text{ and }d^{n-h}\ge t_n.
\tag{7.5}
$$

For $t_n=0$ the assertion holds with rank zero. This uses only
ordinary matrix inverses on full-rank evaluation maps, not a Gram
matrix or characteristic-zero positivity.

To apply (7.5), suppose $I_g\ne(0)$, so $\mathcal B$ is finite.
Fix $x\in\mathcal B_{n_0}$ and let $r$ be its ordinary least
period. Put

$$
\alpha=\prod_{i=0}^{n_0-1}A(f^{\circ i}(x)),\qquad
\beta=\prod_{i=0}^{n_0-1}B(f^{\circ i}(x)).
$$

Here $\alpha-\beta=H_{n_0}(x)\ne0$. Because $x$ returns after
$n_0$ steps, for every positive integer $q$ one has

$$H_{qn_0}(x)=\alpha^q-\beta^q.
\tag{7.6}
$$

Every nonzero element of $k$ has finite multiplicative order: it
belongs to the multiplicative group of some finite subfield. Choose
a positive integer $M$ divisible by the orders of every nonzero
element among $\alpha,\beta$. For arbitrarily large $q=1+jM$,
both nonzero values are fixed by the $q$th power; a zero value
remains zero. Therefore (7.6) equals $\alpha-\beta\ne0$.
This includes a one-sided zero product. Both products cannot be
zero at a point of $\mathcal B_{n_0}$.

Thus $x\in\mathcal B_{qn_0}$ for arbitrarily large returns,
and each such set contains its full $r$-cycle. Write
$t=|\mathcal B|$. If $\mathcal B$ is nonempty, choose one of
these returns $n$ so large that, with $h=\lfloor n/2\rfloor$,

$$h\ge1,\qquad d^h\ge t,\qquad d^{n-h}\ge t.$$

Then $t_n\le t$, and (7.5) gives

$$r\le|\mathcal B_n|\le D.
\tag{7.7}
$$

This argument is applied separately to each already visible cycle.
It does not require all of $\mathcal B$ to be simultaneously visible
at one return, nor a coefficient-independent multiplicative order.
If $\mathcal B$ is empty, the claimed period conclusion is vacuous.

## 8. Elimination of the unknown exceptions and the frozen bound

By (7.7), every point of $\mathcal B$ is a root of some $F_r$
with $1\le r\le D$. Hence $S_*$ vanishes on $\mathcal B$, and
(4.3) gives

$$I_g\ne(0)\quad\Longrightarrow\quad S_*\in I_g.
\tag{8.1}
$$

The reverse implication holds because $S_*$ is nonzero. Its degree
is

$$
\ell_* =\sum_{r=1}^{D}d^r
=\frac{d^{D+1}-d}{d-1}<d^{D+1},
$$

so its integer in (6.4) satisfies $k_{S_*}\le D+1$. The fixed-$S$
horizon from (6.9) is therefore at most

$$k_{S_*}+4b^2\le D+1+2D=3D+1=N.
\tag{8.2}
$$

If all the tests in (4) of Theorem 1.1 pass, (6.9) and (8.2)
give $S_*\in I_g$. Conversely, that membership gives every finite
test. Together with Section 4 and (8.1), this proves all four
equivalences and Theorem 1.1. $\square$

The argument supplies a finite decision, not merely a necessary
test: failure of any prescribed remainder proves that (CP) fails,
and passing them all proves (CP). The finite tests include every
return integer from $1$ through $N$. They are not restricted to
prime periods, prime-to-$p$ periods, or an auxiliary Frobenius clock.

## 9. Boundaries, classical subtraction, and verification record

The rational numerator and denominator are kept as whole products.
No individual factor is required to satisfy (CP), and none of its
multiplicities is replaced by a residue modulo $p$. If a support
cycle contains a numerator zero and a denominator zero, both whole
products vanish at its returns. Such a cycle is outside every
$\mathcal B_n$ and is a legitimate finite support exception. The
theorem does not bound its period. A one-sided support cycle is
visible and is explicitly covered by (7.6)--(7.7) when (CP) holds.
This distinction is not omitted in replacing exceptions by $S_*$.

All formulas cover $m=0$, where $a=0$, $b=1$, $D=2$, and $N=7$.
The low range is then the single state $0$. They also cover $p=2$,
where $-1=1$ remains nonzero. Neither branch requires a separate
classification of constant observables or a separable-map argument.

The complete accepted R9 A1 report was read at SHA256
`6c7a21d2ceaecf585f7c37f8c57dcce79ce1243d2ec9926059f826adc9e15d40`:
[R9 fixed-$S$ mechanism](../../continuation_round9/a1_general_quadratic_normone/REPORT.md).
The complete R10 A1 author report was read at SHA256
`3e53c02f8315cfd957be1c235609b3f2fd3292103b7bd8b31aa98b81f69b835e`:
[R10 rank/persistence mechanism](../a1_annihilator_ideal/REPORT.md).
Their earlier parameter scopes and acceptance states were retained.
This proof imports their ideas, not an unproved extension of their
theorems; Sections 3--8 establish the present scope in full.

Before this proof, the coordinator supplied the high-level general-
polynomial two-block/carry/rank/persistence adaptation and proposed
constants. This report supplies the fully checked argument at the
frozen scope, not an independent origination claim for that shared sketch.

The arbitrary-field finite-word span principle is classical.
The one permitted targeted source batch opened the actual author
PDF of Kiefer--Murawski--Ouaknine--Wachter--Worrell, *On the complexity
of equivalence and minimisation for Q-weighted automata*, LMCS 9(1:08)
(2013). Its Section 3 setup and Proposition 3.1 explicitly allow any
field and give a finite word cutoff for a finite-dimensional weighted
representation: [primary PDF, Proposition 3.1](https://archive.model.in.tum.de/um/bibdb/kiefer/13KMOWW-LMCS.pdf).
That classical principle is subtracted and proved directly above.
No rational-field Gram argument, positivity, trace-character
reconstruction, or external automata complexity theorem is imported.

The result established here is the actual general-polynomial
coefficient/carry construction together with elimination of an
unknown finite exceptional set and the ordinary (CP) equivalence
under $f'=0$. Its novelty and independent paper-level substantiality
are not decided by this author proof; the coordinator's separate
source/substantiality process remains necessary.

No claim is made that (CP) yields a rational function $h$ with
$g=h\circ f/h$, with or without a fixed $p$-power. No general
separable-map product theorem, MS6 existence theorem, all-level
ramification result, target Euler factor, root number, or new paper
admission follows from this report.

Mathematical executions: **zero**. Source batches: **one**, consisting
of the direct primary-PDF check described above. No program, census,
new agent, external-model/API call, GPU job, Git, old/shared-file,
manuscript or PDF edit occurred. Only this allocated report was written.

**Final author disposition:** the frozen complete finite-effectivity
question and bound are proved, with no mathematical gap identified
in self-review; independent review remains pending. This bounded
attempt stops at that exact question, with no parameter ladder or
additional mechanism.
