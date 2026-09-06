# Unadmitted resonance source note

2026-09-07. This note supplies a complete, narrowly quantified source
calculation and two counterexample certificates. It is not a paper admission,
not a complete classification of inseparable lower degrees, and not a formal
Route A evaluation. The coordinator has explicitly requested that the short
two-term extension remain companion material. No old tree is changed.

Continuation status: this remains the original restricted companion and
screening receipt. Its Section 6 records the missing theorem at that initial
checkpoint. [FULL_DEGREE_2P_PROOF.md](FULL_DEGREE_2P_PROOF.md) now supplies an
author proof of the complete degree-$2p$ family for every odd $p$ and
$q=p^e$, $e\ge3$, pending independent review and the separate admission gate.
Neither this note nor its characteristic-three special case is an additional
paper candidate.

## 1. Claim, assumptions and status

**Status: PROVABLE AS STATED for the following restricted family.**

Let $q=p^e$ be a prime power and work over $K=\overline{\mathbb F}_q$.
Choose $a,b,c\in\mathbb F_q^*$ and integers

$$
2\le\ell<m<q,\qquad p\mid m,\qquad p\nmid\ell.
$$

Put $h=m-\ell$, $\rho=p^{v_p(m)}$, and require the two strict gaps

$$
q-m>h,\qquad
q(\rho-h-1)-m(\rho-1)>h. \tag{1}
$$

Every coefficient of $R\in\mathbb F_q[y]$, $\deg R<\ell$, is unrestricted.
Set

$$
g(y)=by^m+cy^\ell+R(y),\quad
H(x,y)=(y,y^q+g(y)-ax),\quad
\Phi(x,y)=(x^q,y^q).
$$

The object is the single morphism $S=H^{-1}\Phi$ on the whole affine plane;
the clock is positive integer iteration. The observable is the number of
geometric points, without multiplicities, of $H^n(P)=\Phi^n(P)$.
For $w=p^{v_p(n)}$, its complete formula is

$$
N_n=q^{2n-w}D_w,\qquad
D_j=\frac{(\ell-1)q^j+q(h+1)-m}{q-1}. \tag{2}
$$

In particular the count depends on the highest non-$p$-divisible exponent
$\ell$, not only the total degree $m$. The assertion includes every positive
period and every coefficient in the stated finite field, not only coefficients
in its prime subfield. It excludes zero $b,c,a$ and does not include equality
in either condition (1).

## 2. Strategy and dependency map

The commuting polynomial pullbacks $T=H^*$, $U=\Phi^*$ are
$\mathbb F_q$-linear. Their difference $\delta=T-U$ is a linear operator,
not a nonlinear point map or a ring endomorphism. The proof uses:

1. The characteristic-$p$ binomial identity for commuting linear operators.
2. A two-leading-term invariant under $\delta$, proved below by degree bounds.
3. The coprime-leading-monomial Gröbner criterion to calculate finite length.
4. The zero-dimensional Jacobian criterion, since $\det DH^n=a^n\ne0$.

Items 1, 3 and 4, and the overall conversion of $\delta^j y$ to all-period
counts, already occur in
[C404's proof](../../continuation_c404_c408_round2/henon_resonance/PROOF_PACKAGE.md).
The additional source lemma is the stable two-term block in Step 2. The
analytic natural-boundary consequence uses C404's same argument and is not
another independent result or another paper.

## 3. Proof

### Step 1. The finite-degree binomial bound

Write $u=g(y)-ax$. If $D$ is a positive integer and
$r_D=p^{v_p(D)}$, then the first nonzero nonconstant binomial coefficient
in $(Y+Z)^D-Y^D$ occurs at $Z^{r_D}$: write $D=r_D d$ with $p\nmid d$
and use $((Y+Z)^{r_D})^d=(Y^{r_D}+Z^{r_D})^d$.
Consequently

$$
\deg\bigl((y^q+u)^D-y^{qD}\bigr)
\le q(D-r_D)+mr_D. \tag{3}
$$

The term with binomial index $r_D$ has that degree, and terms at larger
indices have strictly smaller degree because $m<q$. We shall use only the
upper bound when the leading contribution is to be suppressed.
For every bivariate polynomial $P$,

$$
\deg\delta P\le q\deg P, \tag{4}
$$

since both substitutions have coordinate degrees at most $q$.

### Step 2. A stable two-leading-term block

For every $j\ge1$, define

$$
A_1=0,\qquad A_{j+1}=q(A_j+\ell-1),\qquad
C_j=(c\bar\ell)^{j-1}\ne0,
$$

where $\bar\ell\in\mathbb F_p^*$ is the residue of $\ell$. We claim

$$
\delta^j y=C_jy^{A_j}(by^m+cy^\ell)+R_j,
\qquad \deg R_j<A_j+\ell. \tag{5}
$$

For $j=1$, $\delta y=g(y)-ax$, so (5) holds because $\ell\ge2$.
Assume it at $j$. Put $D=A_j+m$ and $E=A_j+\ell$. The integer $A_j$
is zero or divisible by $q$. Since $m<q$, it follows that
$v_p(D)=v_p(m)$ and $E\equiv\ell\pmod p$.

Consider first $C_jc\delta(y^E)$. Its binomial index one term is

$$
C_jc\bar\ell\,y^{q(E-1)}(g(y)-ax).
$$

This has the specified two terms at degrees
$d=q(E-1)+m$ and $d-h=q(E-1)+\ell$, with common block multiplier
$C_{j+1}$. All remaining terms in this binomial-index-one contribution
have smaller degree than $d-h$. A term of binomial index $i\ge2$ has
degree at most

$$
q(E-i)+mi=d-(i-1)(q-m)<d-h,
$$

using the first strict inequality in (1).

For $C_jb\delta(y^D)$, equation (3) gives degree at most
$q(D-\rho)+m\rho$. Its deficit from $d$ is exactly

$$
d-[q(D-\rho)+m\rho]
=q(\rho-h-1)-m(\rho-1)>h.
$$

Thus it cannot alter either retained term. Finally (4) gives
$\deg\delta R_j\le q(E-1)=d-m<d-h$. This proves (5) at $j+1$,
including the absence of any untracked term between its two displayed
degrees. There is no inference from a finite numerical prefix.

The unique top degree is $D_j=A_j+m$. Its recurrence is

$$
D_1=m,\qquad D_{j+1}=q(D_j-h-1)+m.
$$

Solving it gives (2). It is a positive integer; also $D_j<q^j$, either
from this recurrence and $m<q$, or directly from $A_j$.

### Step 3. Every positive period

The coefficient field makes $T$ and $U$ commute and $U(P)=P^q$ for
$P\in\mathbb F_q[x,y]$. Write $n=ws$, where $w=p^{v_p(n)}$ and
$p\nmid s$. In their algebra of linear operators,

$$
T^w-U^w=\delta^w,
\qquad
T^n-U^n=\sum_{i=0}^{s-1}T^{wi}U^{w(s-1-i)}\delta^w. \tag{6}
$$

Any polynomial with a unique top term $d_0y^D$ retains a unique top term
$d_0y^{qD}$ under either $T$ or $U$. This follows from the degree bound
on its other monomials and the monic $y^q$ term in $H_2$.
Applying (6) to $y$ therefore gives the unique top term

$$
s\,b(c\bar\ell)^{w-1}
y^{q^{n-w}D_w},
$$

whose coefficient is nonzero. The other fixed polynomial
$T^n x-x^{q^n}$ has unique top term $-x^{q^n}$ because
$\deg T^n x=q^{n-1}<q^n$.

### Step 4. Ordinary points, not only intersection length

The leading monomials $x^{q^n}$ and $y^{q^{n-w}D_w}$ are relatively
prime in any graded order. The standard monomials of the quotient are
therefore exactly their rectangular complement, of size $q^{2n-w}D_w$.
This also proves zero-dimensionality with no point at infinity after
homogenization to the actual two degrees.

The $q^n$ powers have zero derivatives and $\det DH=a$, so the Jacobian
determinant of the two fixed equations is $a^n\ne0$. The finite scheme
is reduced over $K$. Its length is the number of its geometric points,
which proves (2). Finally, $H$ commutes with $\Phi$, so this is the fixed
scheme of $(H^{-1}\Phi)^n$, with the stated single-map clock. $\square$

## 4. Exact same-degree counterexample to coefficient blindness

Take $p=3$, $q=27$, $a=1$ and compare
$g_0=y^6$ with $g_1=y^6+y^5$. Both have the same total degree and leading
coefficient. At $n=3$, their ordinary point counts differ:

$$
N_3(g_0)=19683\cdot2484=48\,892\,572,
\qquad
N_3(g_1)=19683\cdot3030=59\,639\,490. \tag{7}
$$

For $g_1$, the theorem applies with $h=1$, $\rho=3$:
$q-m=21>1$ and $q(\rho-h-1)-m(\rho-1)=15>1$.
It gives $D_3=(4\cdot27^3+48)/26=3030$.

Here is a short separate certificate for $g_0$. Its operator difference
satisfies

$$
\delta^2y
=2y^{99}+y^{36}+y^{81}x^3+y^{18}x^3+x^6-y+x^{27}.
$$

For the first term, (3) is attained at binomial index $9$, giving top
degree $27(99-9)+6\cdot9=2484$ and coefficient one in $\mathbb F_3$.
All other terms in the displayed polynomial have total degree at most
$84$, so (4) bounds their images by $2268<2484$. Thus $\delta^3y$
has unique top term $y^{2484}$. Since $3$ is the characteristic,
$\delta^3y=H_2^3-y^{27^3}$. The other equation has top term
$-x^{19683}$; the same coprime-monomial and Jacobian argument proves
the first value in (7). This is a finite counterexample to a proposed
coefficient-blind extension, not a classification theorem for all $g$.

## 5. A forward-return obstruction for the wild cubic

For $f=x^3+x^2$ in characteristic three, direct exact squarefree
factorization at the fifth forward iterate gives

$$
f^5(x)-x=U(x)V(x)^2,\qquad
V=x^5-x^4-x^3-x+1,
$$

where $\deg U=233$ and $U,V$ are squarefree and coprime. Thus the
ordinary geometric fixed-point count is $233+5=238$, not the
scheme length $243$. The executable receipt in
[bounded_probe.py](bounded_probe.py) reconstructs the iterate and
its squarefree factors and checks that
$\gcd(V,f-x)=1$. As $5$ is prime, the roots of $V$ form an exact
five-cycle; its return multiplier is one because those roots are
multiple roots of $f^5-x$.

This certificate is bounded exact algebra, not an all-cycle ramification
theorem. The generic inverse-image group from C410 does not prove a
forward degree count or control the diagonal specialization $t=x$.

## 6. Corrections, missing theorem and substance boundary

The original full-support wish is **NOT CURRENTLY JUSTIFIED**. The proved
two-term theorem does not cover arbitrary lower support, ties in (1),
vanishing $c$, or all possible transitions of dominant Hasse terms.

A concrete next full-family question is: for fixed characteristic three,
every $q=3^e$ with $e\ge3$, every $a,b\in\mathbb F_q^*$ and every
degree-six polynomial $g$ with leading coefficient $b$, classify
$\deg\delta^j y$ and its leading monomials for all $j\ge1$, including
all coefficient strata. The nonzero $y^5$ stratum is settled above.
The stratum with no $y^5$ but a nonzero $y^4$ term is not proved by this
note, and cannot be brought under the two-term theorem by relabeling its
top degree. No result for that stratum follows from the small tests.

The missing step is a finite Hasse-support state description that remains
closed under $\delta$ through all heights and resolves coefficient
cancellations in ties. Tracking only degree and $p$-valuation of the
highest exponent is insufficient: lower terms can overtake it, as (7)
demonstrates. An arbitrary finite polynomial-expansion algorithm is not
the promised finite-state, all-height theorem.

There is also a clean perfection reduction for the separate face
$g=G^{\rho}$, $\rho=p^t$, $2\le\deg G<q/\rho$ and
$p\nmid\deg G$. It suggests, and can prove by the same separated-top
lemma after taking $\rho$th roots, the degree expression
$[(m-\rho)q^j+(q-m)\rho^j]/(q-\rho)$. We do **not** use that
unwritten general-face proof to close the missing mixed-support stratum,
and do not offer it as another paper. Formula (7) has its independent
finite certificate above.

The mathematics here is source-local. It supplies no target Euler
factor, root number, automorphy, zero/divisor correspondence or
Hilbert–Pólya operator. AI-assisted derivation and exact computation are
disclosed; author checking is not independent internal review or human
peer review. No worldwide novelty or publication-readiness claim is made.
