# Fixed-basis parity lemma for real-square character oldforms

Date: 2026-09-07 UTC. Bounded extension coordinated with the independent
character-block reviewer. This is a proof lemma, not a paper admission.

## Claim and status

**PROVABLE AS STATED.** For a primitive character $\chi$ whose square is
real, the character-paired oldform scattering sector at $N=q^2L$
commutes at all regular parameters precisely when
$$
\chi(p)\in\{1,-1\}\quad\text{for every }p\nmid q
\text{ with }v_p(L)\text{ odd}.
\tag{1}
$$
If $\chi$ itself is real, its single character sector commutes for
every $L$, with no bound on the oldform exponents. If $\chi$ is not
real but $\chi^2$ is real, the pair is $(\chi,\bar\chi)$.

The local algebra, tensor argument and constant-term specialization
needed for this conditional-on-real-square assertion are supplied
below. The necessity of a real square in the full AS2 classification
is not asserted or proved here; the separate character reviewer owns it.

## Assumptions and notation

- Weight zero, trivial nebentypus and fixed width-one cusp coordinates.
- $q$ is the conductor of $\chi$ and $q^2\mid N$; $L=N/q^2$.
- The real-square assumption means $\chi^4=1$ on the unit group.
  Thus $\chi(p)\in\{1,-1,i,-i\}$ for $p\nmid q$.
- For one unramified prime, $p>1$, $e=v_p(L)$,
  $x=p^s$, $y=p^{1-s}$, and $r_a=\max(a,e-a)$.
- $C(X)$ denotes the principal matrix from
  [PROOF_PACKAGE.md](PROOF_PACKAGE.md), at an arbitrary nonzero
  complex argument $X$. Its fixed-basis proof only used $XY=p$,
  so it applies verbatim to $Y=p/X$, not only to positive-real $X$.
- For $c\in\{1,-1,i,-i\}$ define
  $$
  C_c(x)_{j,a}=c^{|j-a|}x^{r_a-|j-a|}.
  $$
  The parameter is never conjugated when replacing $c$ by $\bar c$.

## Strategy and dependencies

Use the principal fixed basis already proved, together with three
constant diagonal matrices. A purely imaginary phase produces a
fixed half-chain sign operator. It is the identity when $e$ is even;
when $e$ is odd it interchanges just the two central channels.
Tensor sign-pattern comparisons rule out cancellation between
different odd-exponent imaginary-phase primes.

The classical input is the incoming character coefficient formula and
the completed character functional equation. Their exact connection
to this algebra is recorded in Step 5, rather than assumed from a
parameter-dependent change of basis.

## Proof

### Step 1. Reduce the paired local matrix by constant similarities

Put
$$
\kappa=c^2\in\{1,-1\},\quad
D=\operatorname{diag}(\kappa^j)_{j=0}^e,\quad
H=\operatorname{diag}(c^{r_a})_{a=0}^e,\quad
F=\operatorname{diag}(\kappa^{r_a+a})_{a=0}^e.
$$
All three matrices are fixed, and $D^2=F^2=I$. Since
$\bar c/c=c^{-2}=\kappa$,
$$
C_{\bar c}(x)=DC_c(x)D.
\tag{2}
$$
Consider the paired local family
$$
\mathcal K_c(s)=
\begin{pmatrix}
0&C_c(x)^{-1}C_{\bar c}(y)\\
C_{\bar c}(x)^{-1}C_c(y)&0
\end{pmatrix}.
\tag{3}
$$
Conjugation by $\operatorname{diag}(I,D)$ changes it into
$\left(\begin{smallmatrix}0&A(s)\\A(s)&0\end{smallmatrix}\right)$,
where
$$
A(s)=C_c(x)^{-1}DC_c(y).
$$
A fixed two-block Walsh matrix then gives $A(s)\oplus(-A(s))$.

To identify $A$, set $X=x/c$ and $V=y/c$. Directly from the entries,
$$
C_c(x)=C(X)H,\qquad C_c(y)=C(V)H.
$$
The parity identity $|j-a|\equiv j+a\pmod2$ gives
$$
DC(V)=C(\kappa V)F.
$$
Since $X(\kappa V)=p$, we obtain
$$
A(s)=H^{-1}P(X)F H,
\qquad P(X)=C(X)^{-1}C(p/X).
\tag{4}
$$
This is the decisive formula: all similarities so far are independent
of $s$. The replacement of an argument by $X=x/c$ is not a change
of coordinates, and does not assume that $C(X)$ diagonalizes anything.

### Step 2. The commuting cases

If $c=\pm1$, then $\kappa=1$ and $F=I$ for every $e$.
Equation (4) and the fixed principal basis prove commutativity.

If $c=\pm i$ and $e$ is even, then $r_a+a$ is even for every $a$:
it equals $e$ on the left half and $2a$ on the right half. Again
$F=I$, and the same fixed-basis conclusion follows. This also covers
$e=0$.

### Step 3. The noncommuting local case and its exact location

Let $c=\pm i$ and $e=2m+1$. Then $F$ equals $-I$ on indices
$0,\ldots,m$ and $+I$ on indices $m+1,\ldots,2m+1$.
The principal left/right difference eigenvectors from the companion
proof therefore remain eigenvectors of $P(X)F$, with their original
scalar eigenvalue multiplied by $-1$ or $+1$.

On the central subspace, use the fixed vectors
$$
u_L=\sum_{a=0}^m\varphi(p^a)\mathbf e_a,\qquad
u_R=Ju_L,\qquad v_+=u_L+u_R,\quad v_-=u_L-u_R.
$$
They satisfy $Fv_+=-v_-$ and $Fv_-=-v_+$.
Writing $Y=p/X$ and $R=Y/X$, the two principal eigenvalues are
$$
\lambda_\pm(X)=R^m\frac{Y\pm1}{X\pm1}.
$$
Thus the matrix of $P(X)F$ on this fixed two-dimensional subspace is
$$
\begin{pmatrix}0&-\lambda_+(X)\\-\lambda_-(X)&0\end{pmatrix}.
\tag{5}
$$
Its off-diagonal ratio is
$$
\rho_p(X)=\frac{\lambda_+(X)}{\lambda_-(X)}
=\frac{(p+X)(X-1)}{(p-X)(X+1)}.
\tag{6}
$$
This rational function is not constant for $p>1$. If it were the
constant $k$, comparison of the quadratic coefficients would force
$k=-1$, whereas comparison of the linear coefficients would force
$p-1=-(p-1)$, a contradiction. Since $X=p^s/c$ ranges through a
nonempty open set as $s$ varies, the composed meromorphic ratio is
also nonconstant.

For a two-by-two off-diagonal family with nonzero meromorphic entries
$a(s),b(s)$, the commutator vanishes identically exactly when
$a(s)b(t)-a(t)b(s)=0$, equivalently when $a/b$ is constant.
Equation (6) proves that (5), and hence (3), is not a pairwise
commuting family. This proves the local parity dichotomy for all $e$.

### Step 4. No cancellation between several bad local factors

Call an unramified factor bad if $c_p=\pm i$ and $e_p$ is odd.
The same fixed transformations as in Step 1, applied as tensor
products, convert the global paired matrix, up to a common scalar,
into two copies with opposite signs of
$$
\mathcal A(s)=\bigotimes_p A_p(s).
$$
Ramified diagonal factors may be included. If there are no bad
factors, each $A_p(s)$ has a fixed diagonalizing basis, so does
$\mathcal A(s)$, and the paired family commutes.

Suppose there are $b\geq1$ bad factors. In every other factor choose
one fixed eigenline whose eigenvalue is not identically zero. Such
lines exist because all local matrices are generically invertible.
In every bad factor restrict to its central two-dimensional space.
These choices give a fixed invariant subspace. Index its tensor basis
by signs $\varepsilon=(\varepsilon_1,\ldots,\varepsilon_b)$.
Equation (5) sends a sign vector to its simultaneous negative, so
the subspace decomposes into fixed two-dimensional blocks indexed
by $\{\varepsilon,-\varepsilon\}$. Up to choosing the orientation
of such a block, its off-diagonal ratio is
$$
\rho_\varepsilon(s)=\prod_{j=1}^b\rho_{p_j}(p_j^s/c_{p_j})^{\varepsilon_j}.
\tag{7}
$$
The scalar eigenvalues from all other factors cancel in this ratio.
If $b=1$, Step 3 already proves noncommutativity. If $b\geq2$ and
every block were commuting, take the all-plus sign vector and the
vector obtained by changing just its first sign. They represent
different two-dimensional blocks. Both ratios would be constant,
so their quotient would make
$\rho_{p_1}(p_1^s/c_{p_1})^2$ constant. A nonzero meromorphic
function on a connected domain whose square is constant is itself
constant, contradicting Step 3. Therefore one block is noncommuting.

This argument does not assume independence of the logarithms of
different primes and does not overlook a possible product cancellation.

### Step 5. Classical normalization and the real-character case

Here is a direct specialization connecting the local matrices to the
fixed cusp Fourier coordinates. Use a cusp numerator $u$, denominator
$qf$ with $f\mid L$, and oldform label $B\mid L$. In the
Booker--Lee--Strömbergsson coefficient formula from the companion proof,
put $m=qB$ and $g=\gcd(B,f)$. After the common factor $2$ is removed
to match Young's normalized series, its character weight is
$$
\chi(-u)\chi(f/g)\chi(B/g).
$$
At $p\nmid q$ this gives $\chi(p)^{|j-a|}$, where
$j=v_p(B)$ and $a=v_p(f)$. At $p\mid q$, it is zero unless $j=a$.
The magnitude exponent is
$$
v_p(q)+e_p-\min(2a,e_p)+2\min(a,j)-j.
$$
Thus, in fixed Fourier sums with weights $\chi(-u)$, the incoming
matrix is the tensor product of the following local matrices:
$$
\begin{cases}
C_{\chi(p)}(p^s),&p\nmid q,\\
\operatorname{diag}\bigl(p^{s(v_p(q)+\max(a,e_p-a))}\bigr)_{a=0}^{e_p},
   &p\mid q.
\end{cases}
\tag{8}
$$
The conductor factors at unramified primes are $1$; hence all powers
of $q^s$ are already contained in the second line of (8).
Numerator representatives of the cusps can be chosen coprime to $N$;
the Fourier sums are independent of their choices modulo
$\gcd(qf,N/(qf))$. They form fixed coordinates, not an
$s$-dependent basis of oldform coefficients.
With that choice, the Booker--Lee--Strömbergsson cusp $u/(qf)$
and Young's cusp $1/(u qf)$ are $\Gamma_0(N)$-equivalent, so the
two conventions are related by a fixed cusp reindexing, not a
spectral-parameter-dependent transformation.

The equality of normalizations follows directly from Young's
definition (3.3): his $E_{\chi,\chi}(Bz,s)$ is half the
Booker--Lee--Strömbergsson $E_\chi^\chi(qBz,s)$.
Young's completion and Proposition 4.2 give
$$
A_\chi(s)E_{\chi,\chi}(Bz,s)
=A_{\bar\chi}(1-s)E_{\bar\chi,\bar\chi}(Bz,1-s),
\quad
A_\chi(s)=\frac{(q/\pi)^s\Gamma(s)L(2s,\chi^2)}{\tau(\chi)}.
\tag{9}
$$
These definitions and formulas were directly checked in
[Young, arXiv:1710.03624v2, Sections 3.2 and 4.1--4.2](https://arxiv.org/html/1710.03624v2#S4.SS2),
version dated 3 November 2017. Equation (7.3) and the adjacent
Fourier-basis discussion were also inspected.

When $\chi^2$ is real, the two scalar factors in the paired
functional equation have one common meromorphic factor and the
constant reciprocal factors $\tau(\chi)/\tau(\bar\chi)$ and its
inverse. A fixed diagonal similarity removes these constants.
The remaining paired matrix is precisely the tensor construction
in Steps 1--4, with the ramified diagonal factors from (8).
Multiplication by a common meromorphic scalar not identically zero
preserves whether the commutator identity holds identically.

When $\chi=\bar\chi$, there is only one character sector, not a
duplicated artificial pair. Its matrix from (9) is a scalar multiple
of $C_\chi(s)^{-1}C_\chi(1-s)$. In (8), every unramified phase is
$\pm1$, so its local matrix is a fixed sign-conjugate of the
principal commuting family. Every ramified factor is diagonal.
Their tensor product therefore has a fixed diagonalizing basis for
every $L$ and every collection of exponents. This completes the
real-character sufficiency requested by the coordinator.

Combining (8)--(9) with Steps 1--4 proves (1) for every character
with real square. Since $p\nmid q$ implies $v_p(L)=v_p(N)$, its
odd-exponent condition may equivalently use $v_p(N)$.
All identities are meromorphic; statements at removable singularities
follow by continuity, with no evaluation of a gamma pole and an
$L$-function zero as separate numerical factors. $\square$

## Concrete consequence for the first proposed repair

The entire scattering family at $N=100$ is commuting. Indeed a
primitive conductor whose square divides $100$ can only be $1$ or
$5$: the apparent moduli $2$ and $10$ contribute no additional
primitive characters because their unit-group characters are induced
from modulus $1$ and $5$, respectively. The conductor-$1$ sector
commutes by the principal proof. The real conductor-$5$ sector
commutes by Step 5. In the quartic pair, the only unramified
oldform prime is $2$, with exponent $2$; Step 2 applies even though
$\chi(2)=\pm i$. The fixed cusp Fourier decomposition contains
exactly these sectors, so all its blocks commute.

Thus the first repair requiring a real $\chi(p)$ at *every*
unramified divisor prime was too strong. Its failure at $N=100$
is deduced here without a new parameter-grid computation.

## Corrections, open risks and scientific boundary

The parity qualification in (1) is essential. This document does not
prove the remaining full-classification implication that a nonreal
square always forces noncommutativity. It also does not itself
provide the elementary level description of the final condition.
Those tasks are independently owned by the other reviewer and
coordinator. The original frozen conjecture and first repair are not
silently rewritten by this file.

All source formulas are classical and all new work here is their
explicit finite-dimensional algebraic deduction. No new autonomous
clock, Euler factor, root number or spectral realization follows.
No mathematical computation, new or repeated, was executed for
this lemma.
