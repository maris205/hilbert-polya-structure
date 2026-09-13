# Minimal trace selections on a fixed coefficient neighborhood

Date: 2026-09-06. Author-side bounded proof, V1.
This is a new selection theorem using the retained quadratic Hénon jets.
It is not a revision of the stopped fifth candidate, a formal Paper29,
a long-paper value/page PASS, or a manuscript.

## 1. Claim, assumptions and status

**Author mathematical status: PROVABLE AS STATED.**
Independent checking of the complete statement and its occupation
elimination remains separate. The supplementary finite-frame observation
with $k+3$ fixed-point observations is not used as an accepted proof of
this stronger result.

Fix $k\ge6$ with $6\mid k$, and put $d=k-3$. Phases are indexed by
$\mathbb Z/k\mathbb Z$, with representatives $0,\ldots,k-1$.
Consider
$$
H_c(x,y)=(x^2+c-y,x),\qquad
F_{\epsilon,u}=H_{c_{k-1}}\circ\cdots\circ H_{c_0},\qquad
c_j=\epsilon^{-2}(u_j-1).
\tag{1}
$$
All work is over $\mathbb C$; $\epsilon\ne0$ and is held fixed in
coefficient differentiation. Put
$$
A=\{1,\ldots,d\},\qquad
B_0=A,\quad B_i=\{i\}\ (1\le i\le d),\quad
B_\alpha=\{1,2\},\quad B_\beta=\{2,3\}.
\tag{2}
$$
There are exactly $d+3=k$ different nonempty subsets in (2).
The three phases $0,k-2,k-1$ are positive in every one of these
base patterns. The row labels are ordered $0,1,\ldots,d,\alpha,\beta$.

For any prescribed positive macro periods
$\boldsymbol n=(n_0,n_1,\ldots,n_d,n_\alpha,n_\beta)$, the word
of row $p$ consists of:

- one block with minus set $B_p$ if $n_p=1$;
- $n_p-1$ blocks with minus set $B_p$ and one all-plus block if $n_p\ge2$.

Set
$$
a_p=\begin{cases}1,&n_p=1,\\1-1/n_p,&n_p\ge2,\end{cases}
\qquad w_p=a_p^{-1}\in[1,2].
\tag{3}
$$
Let $\rho_p=\operatorname{tr}DF^{n_p}$ on the corresponding labeled
cycle, and let $K$ have rows
$$
\kappa_p=\frac1{n_p\rho_p}\,d_u\rho_p.
\tag{4}
$$

### Theorem

There exist $\epsilon_0,\eta,c,C>0$, depending only on $k$, such that
for every prescribed period vector the above words define $k$
pairwise-disjoint, simple, exact-period cycles with nonzero traces
throughout the fixed product region
$$
0<|\epsilon|<\epsilon_0,\qquad \|u\|_\infty<\eta.
\tag{5}
$$
Their normalized trace differential satisfies
$$
\sigma(K)\asymp_k
(1,\underbrace{|\epsilon|,\ldots,|\epsilon|}_{k-3},
|\epsilon|^2,|\epsilon|^2)
\tag{6}
$$
in decreasing singular-value order. In particular
$|\det K|\ge c|\epsilon|^{k+1}$ on (5). All constants are independent
of the periods. The rows are differentiated in $u$, not in a coordinate
$v$ with $u=\epsilon v$; no shrinking $u$-region is used.

An exact power-locus coefficient is
$$
\det K(\epsilon,0)
=\Delta_k\left(\prod_p a_p\right)\Gamma(w)\epsilon^{k+1}
 +O_k(\epsilon^{k+2}),
\tag{7}
$$
where the remainder is uniform in the periods,
$$
\Gamma(w)=w_0+w_\alpha+w_\beta
-\sum_{i=1}^d w_i-w_1-2w_2-w_3\le 2-d\le-1,
\tag{8}
$$
and $\Delta_k\ne0$ is the explicit rational matrix determinant in
(20) below. Thus the period coefficient cannot vanish anywhere on
the occupation cube. The order $k+1$ attains the previously proved
universal obstruction for every selection at $u=0$.

The number $k$ of scalar traces is minimal for a full-rank differential
on this $k$-dimensional coefficient space, simply by dimension. This
does not assert uniqueness of the selection, optimal numerical
constants, global injectivity, or a classification of every selection.

## 2. Dependencies and the actual new issue

The retained [main proof V2](PAPER29_CYCLIC_HENON_JET_PROOF_V2_20260905.md),
SHA256 `f488e8a7cd5a2c71a4975b2f004b21c87d20f4afb29c967318781963fb2955f0`,
provides the following already independently checked inputs:

1. Two uniform contractions for the orbit and the Riccati return line;
   all sign words yield holomorphic periodic branches with nonzero traces.
2. Primitive macro words have exact periods, and words from different
   macro-shift classes give disjoint cycles.
3. The actual normalized trace differential has a coefficient-holomorphic
   second-order expansion with period-independent Taylor remainders.
4. Its first-order phase functions and second-order sign-correlation
   functions are those recalled below. The universal first-jet obstruction
   gives order at least $k+1$ for any selection when $6\mid k$.

These inputs are not re-proved or counted as new here. The new task is
to select only $k$ actual cycles, allow their periods to vary independently,
and cancel the first jet in two output combinations identically in $u$.
Independent occupation fractions prevent using naive equal-weight mixed
differences. Equations (14)--(19) resolve that obstruction by a bounded
output transformation; its nonvanishing certificate uses $w_p\in[1,2]$.

The proof chain is: lawful words and local correlations; binary
polarization of the second jet; bounded occupation elimination; an
explicit complementary Fourier minor; exact coefficient and uniform
analytic perturbation.

## 3. Exact periods, disjointness and macro-boundary correlations

All $B_p$ are nonempty. For $n_p\ge2$, the all-plus block is a unique
marker, so no shorter nontrivial macro repetition is possible. For
$n_p=1$ the period is one. The parent uniqueness of sign-disc solutions
then proves exact macro period $n_p$ in every case.

The union of the negative phases in each row word is exactly $B_p$.
Different rows have different such sets. A macro shift preserves this
set, so two row words cannot belong to the same macro-shift orbit.
This proves actual disjointness, including repeated period values.
It does not identify or separate elementary-factor orbits at $u=0$.
Simplicity and nonzero traces follow on a common parent domain from
the inherited multiplier estimates.

Write $b_j=\mathbf1_{j\in B_p}$ in a fixed row. The phase means are
$1-2a_pb_j$. A pair of adjacent phases or phases at distance two
can contain two active phases only within one macro block: the three
consecutive inactive phases $k-2,k-1,0$ prevent two active entries
from straddling its boundary. If only one phase is active, the other
sign is identically plus, so its product mean is just that phase mean.
If neither is active it is one. Hence in every case the relevant
two-sign average is exactly
$$
1-2a_p(b_i+b_j)+4a_pb_ib_j.
\tag{9}
$$
There is no substitution of $a_p^2$ for $a_p$, and no equality of the
different rows' occupation fractions is assumed.

## 4. Binary form of the inherited second jet

Let $s_j(u)=\sqrt{1-u_j}$ near one. The phase functions are
$$
h_j=\frac{s_j}{2}(s_{j-1}^{-2}+s_{j+1}^{-2}),\qquad
D_j=-\frac{s_{j-1}s_{j+1}}{2s_j^4},
$$
$$
E_j=\frac1{4s_js_{j+1}}
+\frac{s_{j+1}}{4s_js_{j-1}^2}
+\frac{s_j}{4s_{j+1}s_{j+2}^2}.
\tag{10}
$$
Use the following covector notation to avoid confusing $d=k-3$ with
the differential symbol: $\mathrm d$ always denotes coefficient
differentiation. Put $\ell_i(u)=-2\mathrm d h_i(u)$.
Let $m_i(u)$ be the single-negative-phase change in the second-order
covector, relative to the all-plus pattern. It is explicitly determined
by (10) and the constant part of the inherited second jet; only its
linearity under binary polarization is needed below.

There is a common polynomial in $\epsilon$ with covector coefficients
$g(\epsilon,u)=g_0(u)+\epsilon g_1(u)+\epsilon^2g_2(u)$ such that
$$
\kappa_p=g+a_p\left[
 \epsilon\sum_{i=1}^d b_i\ell_i
 +\epsilon^2\left(\sum_{i=1}^d b_im_i+q_{B_p}\right)\right]
 +\epsilon^3\mathcal R_p(\epsilon,u),
\tag{11}
$$
where $g_0=\mathrm d\sum_j\log(2s_j)$, and
$$
q_B(u)=4\sum_{i=1}^{d-1}b_ib_{i+1}\,\mathrm dE_i(u)
       +4\sum_{i=1}^{d-2}b_ib_{i+2}\,\mathrm dD_{i+1}(u).
\tag{12}
$$
All coefficients and remainders are holomorphic on a fixed parent
domain, with bounds independent of the row periods. To obtain (11),
insert (9) and the phase means into the inherited expansion. Every
constant term goes into $g$, every term linear in a single $b_i$ into
$m_i$, and the product terms have the coefficient four in (12).
The stable-multiplier correction is included in the inherited bounded
remainder; no equality of the different exact trace functions with an
all-plus iterate trace is claimed.

For the selected sets,
$$
q_{B_i}=0\ (1\le i\le d),\qquad
q_{B_\alpha}=f_1:=4\mathrm dE_1,\qquad
q_{B_\beta}=f_2:=4\mathrm dE_2,
$$
$$
q_{B_0}=q_A=4\sum_{i=1}^{d-1}\mathrm dE_i
              +4\sum_{i=1}^{d-2}\mathrm dD_{i+1}.
\tag{13}
$$

## 5. Occupation elimination without an equal-period assumption

Define the weighted observed rows $r_p=w_p\kappa_p$ and
$$
x_0=w_0-\sum_{i=1}^d w_i,\qquad
x_\alpha=w_\alpha-w_1-w_2,\qquad
x_\beta=w_\beta-w_2-w_3.
\tag{14}
$$
Since $1\le w_p\le2$ and $d\ge3$,
$$
x_0\le2-d\le-1,\qquad x_\alpha\le0,\qquad x_\beta\le0,
\qquad \Gamma=x_0+x_\alpha+x_\beta\le2-d.
\tag{15}
$$
All these coefficients have absolute values bounded solely by $k$.
In particular no division by a period-dependent small difference of
occupation fractions occurs.

Form the following $k$ output combinations, in the indicated order:
$$
C=\frac{r_0-\sum_{i=1}^d r_i}{x_0},\qquad
U_i=r_i-w_iC\quad(1\le i\le d),
\tag{16}
$$
$$
V_\alpha=r_\alpha-r_1-r_2-x_\alpha C,\qquad
V_\beta=r_\beta-r_2-r_3-x_\beta C.
\tag{17}
$$
The $r_i$ in (17) are the original weighted rows, not $U_i$.
Equation (11) gives, uniformly on a fixed $u$-polydisc,
$$
C=g+\epsilon^2q_A/x_0+O(\epsilon^3),\qquad
U_i=\epsilon\ell_i+
\epsilon^2(m_i-w_iq_A/x_0)+O(\epsilon^3),
\tag{18}
$$
$$
V_\alpha=\epsilon^2(f_1-x_\alpha q_A/x_0)+O(\epsilon^3),\qquad
V_\beta=\epsilon^2(f_2-x_\beta q_A/x_0)+O(\epsilon^3).
\tag{19}
$$
The zero coefficients in these equations vanish identically in $u$.
In particular the last two rows are genuinely divisible by
$\epsilon^2$ as jointly holomorphic functions, not just at $u=0$.

Let $T(a)$ be the matrix of the transformation from $K$ to
$(C,U_1,\ldots,U_d,V_\alpha,V_\beta)^T$. It is invertible and both
it and its inverse are bounded uniformly on $a\in[1/2,1]^k$.
For an explicit inverse, recover $r_i=U_i+w_iC$, then
$r_0=x_0C+\sum r_i$, and recover $r_\alpha,r_\beta$ from (17);
finally multiply each $r_p$ by $a_p$. Its determinant is
$\det T=1/(x_0\prod_pa_p)$: row weighting contributes
$1/\prod a_p$, the division in (16) contributes $1/x_0$, and the
remaining additions have determinant one. This remains true when the
later rows are expressed using the original $r_i$ in (17).

## 6. The complementary Fourier minor and polarized resonant rows

Let $S$ denote cyclic phase shift and $L_1=I-S-S^{-1}$.
At $u=0$, $g_0=-\mathbf1^T/2$ and $\ell_i=e_i^TL_1$.
Let $R$ be the two-dimensional Fourier subspace of frequencies
$\pm\pi/3$, and let $N$ be the nonconstant nonresonant subspace.
Its dimension is $k-3=d$.

Define the fixed rational determinant
$$
\Delta_k=\det
\begin{pmatrix}
-\mathbf1^T/2\\
e_1^TL_1\\ \vdots\\ e_d^TL_1\\
4\mathrm dE_1(0)\\4\mathrm dE_2(0)
\end{pmatrix}.
\tag{20}
$$
Its entries are explicit: $4\mathrm dE_j(0)$ has weights
$1,1/2,1/2,1$ in positions $j-1,j,j+1,j+2$, respectively.

The first $d+1=k-2$ rows in (20) are independent and vanish on $R$.
To verify independence, use the unitary Fourier columns
$q_\nu(j)=k^{-1/2}\zeta_\nu^j$, with
$\zeta_\nu=e^{2\pi i\nu/k}$. After the constant column is separated,
the $d\times d$ matrix in rows $i=1,\ldots,d$ and columns
$\nu\notin\{0,k/6,5k/6\}$ has entries
$$
(1-2\cos(2\pi\nu/k))\,k^{-1/2}\zeta_\nu^i.
\tag{21}
$$
All displayed eigenvalues are nonzero. Removing those factors and one
$\zeta_\nu$ from each column leaves the Vandermonde matrix with
exponents $0,\ldots,d-1$ at $d$ distinct nonzero nodes. Its
determinant is the nonzero product of the pairwise node differences.
Thus these rows span the annihilator of $R$.

For any $z\in R$, the relation $z_{j-1}+z_{j+1}=z_j$ gives
$$
4\mathrm dE_j(0)z=\tfrac12(z_j+z_{j+1}),\qquad
4\mathrm dD_j(0)z=-3z_j.
\tag{22}
$$
The two rows $f_1,f_2$ restrict independently to $R$. Indeed their
values on $q_+,q_-$ are proportional to
$$
\begin{pmatrix}
(1+e^{i\pi/3})e^{i\pi/3}&(1+e^{-i\pi/3})e^{-i\pi/3}\\
(1+e^{i\pi/3})e^{2i\pi/3}&(1+e^{-i\pi/3})e^{-2i\pi/3}
\end{pmatrix}.
$$
The nonzero column factors leave determinant
$e^{-i\pi/3}-e^{i\pi/3}\ne0$. Equations (21)--(22) prove
$\Delta_k\ne0$ without an unverified numerical determinant.

The remaining identity is
$$
q_A(0)|_R=-f_1(0)|_R-f_2(0)|_R.
\tag{23}
$$
For detail, (13) and (22) give
$q_Az=\frac12(z_1+z_d)-2\sum_{i=2}^{d-1}z_i$.
Every vector in $R$ is six-periodic and sums to zero over six
consecutive positions. Since $d=k-3\equiv3\pmod6$, one has
$z_d=z_3$ and $\sum_{i=1}^d z_i=z_1+z_2+z_3$.
The preceding expression is therefore
$\frac12(z_1+z_3)-2z_2=-3z_2/2$.
On the other hand $f_1z+f_2z=(z_1+2z_2+z_3)/2=3z_2/2$.
This proves (23), including $k=6$.

## 7. Uniform analytic rank and the exact coefficient

Set
$$
\Lambda_\epsilon=\operatorname{diag}
(1,\underbrace{\epsilon,\ldots,\epsilon}_{d},
\epsilon^2,\epsilon^2),\qquad
M(\epsilon,u)=\Lambda_\epsilon^{-1}T(a)K(\epsilon,u).
\tag{24}
$$
Equations (18)--(19) show that $M$ extends jointly holomorphically
to $\epsilon=0$ on a fixed parent $u$-domain. Its bounds and the
needed coefficient-derivative bounds are uniform in all periods.
At $(0,0)$, its first $k-2$ rows are the first rows of (20).
By (23), the last two rows, restricted to $R$, are obtained from
$(f_1,f_2)$ by the matrix
$$
I_2+\begin{pmatrix}x_\alpha/x_0\\x_\beta/x_0\end{pmatrix}
\begin{pmatrix}1&1\end{pmatrix},
\qquad
\det=1+(x_\alpha+x_\beta)/x_0=\Gamma/x_0\ne0.
\tag{25}
$$
Components of these rows in the annihilator of $R$ can be eliminated
using the first $k-2$ rows, so
$$
\det M(0,0)=\Delta_k\Gamma/x_0.
\tag{26}
$$
This also gives a uniform nonzero lower bound. More explicitly,
$\Gamma/x_0\ge1$ by (15); all entries of the limiting matrix are
bounded on the compact occupation cube. The cofactor formula bounds
its inverse uniformly there. The limiting matrix depends on the
periods only through $a$, while its analytic remainders and coefficient
derivatives are uniformly bounded for every period vector.

Consequently one can choose $\eta,\epsilon_0$ depending only on $k$
so that $M(\epsilon,u)$ remains within a common inverse-norm
perturbation radius of $M(0,0)$ for all period vectors and all points
of (5). Both $M$ and its inverse are uniformly bounded. This is a
product domain, not the intersection of unrelated period-dependent
local neighborhoods.

Since $T$ and $T^{-1}$ are uniformly bounded,
$K=T^{-1}\Lambda_\epsilon M$. The singular values are therefore
uniformly comparable to those of $\Lambda_\epsilon$, proving (6).
Furthermore $\det\Lambda_\epsilon=\epsilon^{d+4}=\epsilon^{k+1}$
and $\det T=1/(x_0\prod a_p)$. Equation (26) yields (7).
Holomorphic uniform bounds on the rescaled matrix give the stated
one-higher-order remainder directly. No entrywise estimate of an
unrescaled degenerate determinant is substituted for this step.

The inherited universal first-order obstruction proves that no tuple
can have a smaller finite order at $u=0$ in this normalization.
Dimension proves that fewer than $k$ scalar traces cannot have rank
$k$. These are two separate minimality statements.

## 8. Meaning, boundaries and proof-volume caution

For nonresonant $k$, the retained single-negative-phase selection
already supplies arbitrary-period optimal coordinates on a fixed
$u$-neighborhood. The present theorem fills that fixed-domain property
for every resonant $k$ by changing the selection, not the parameter
normalization and not the number of traces.

The old all-single-negative selection still has its proved critical
curves. At its critical parameters sufficiently close to $u=0$, the
new selection is full rank on (5). Thus its criticality is selection-
dependent, not a common kernel of the whole marked periodic spectrum
on this domain. No claim is made about full-spectrum rank elsewhere,
global conjugacy classes or unmarked quotient singularities.

Only bounded, period-dependent linear combinations of normalized
logarithmic output differentials were used. They do not change the
parameter coordinates or the fact that exactly $k$ raw traces are
observed. The divisions by $\epsilon,\epsilon^2$ are analytic proof
devices at fixed $\epsilon$ and amplify measurement errors; (6) is
the stated conditioning of the unprocessed normalized matrix.

For the original coefficient differential $K_c=\epsilon^2K_u$,
the determinant gains $2k$ powers of $\epsilon$. Unnormalizing rows
also introduces the factors $n_p\rho_p$. Neither variant inherits
the displayed coefficient in (7) without those changes.

The new substance is the support selection, macro-boundary-safe
polarization, uniform elimination of independent occupation fractions,
and the nonvanishing certificate (15), (23), (25). The analytic jet,
Fourier machinery and finite-dimensional perturbation are inherited
tools. The full-spectrum consequence and observation-count lower bound
are short consequences, not separate paper-sized results. Whether
this genuinely stronger fixed-domain theorem plus the necessary
underlying results has sufficient independent long-paper value and
volume has not been assessed. No page count or candidate PASS is
inferred from this proof's length.
