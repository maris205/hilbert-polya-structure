# Redundant fixed-point trace frame: bounded author preflight

Date: 2026-09-06.

## Claim and status

**Mathematical status: PROVABLE AS STATED, with the normalization below
made explicit.**

**Author long-paper preflight: STOP.** This is a short consequence of
the already proved second-order sign-correlation formula, naturally
about 2--4 substantive English pages after citing that formula.
It does not justify a new long-paper project or enlargement for a
22-page target.

Only this new preflight file is created. All previous candidate,
proof, boundary, review and index files remain frozen. The result
below concerns $k+3$ observations and only macro-fixed points.
It makes no minimal-redundancy claim.

## Assumptions and precise statement

Fix $k\ge6$ with $6\mid k$, and retain the family
$$
F_{\epsilon,u}=H_{c_{k-1}}\circ\cdots\circ H_{c_0},\qquad
H_c(x,y)=(x^2+c-y,x),\qquad
c_j=\epsilon^{-2}(u_j-1).
$$
Phase indices are modulo $k$. For a subset $A$ of phases, let
$\rho_A$ be the trace of the macro-fixed-point branch whose minus
signs occur exactly in $A$, and put
$$
\kappa_A=\rho_A^{-1}d_u\rho_A.
$$
The derivative holds $\epsilon$ fixed. Select the sets
$$
\varnothing,\quad \{0\},\ldots,\{k-1\},\quad
P_0=\{k-1,1\},\quad P_1=\{0,2\}.
$$
There are exactly $k+3$ different words in this list.

Let $\mathcal T$ be the vector of these original trace observations,
and let $\mathscr K$ be the $(k+3)\times k$ matrix with rows
$\kappa_A$. Thus
$$
\mathscr K=\operatorname{diag}(\rho_A^{-1})D_u\mathcal T.
$$
There are $\epsilon_0,\eta,c,C>0$, depending on $k$ but not on
$\epsilon,u$, such that throughout the fixed product region
$$
0<|\epsilon|<\epsilon_0,\qquad \|u\|_\infty<\eta,
$$
all selected fixed points are distinct and simple, their traces
are nonzero, and
$$
\|\mathscr K\|\le C,\qquad
\sigma_{\min}(\mathscr K)\ge c|\epsilon|^2.
$$
In particular $D_u\mathcal T$ has full column rank there.
The displayed singular-value estimate is for the normalized
differential $\mathscr K$, not the unnormalized trace Jacobian.

## Dependencies and strategy

The accepted main proof supplies the actual fixed-point branches,
nonzero traces, and a coefficient-holomorphic second-order expansion.
The new work consists only of sign inclusion-exclusion, two Fourier
evaluations, and finite-dimensional analytic perturbation.

Write $s_j=\sqrt{1-u_j}$ near $1$. In the existing expansion the
distance-two sign product centered at $j$ has coefficient
$$
D_j(u)=-\frac{s_{j-1}s_{j+1}}{2s_j^4}.
$$
The first-order coefficient is linear in the phase signs on the
whole fixed coefficient polydisc, not only at $u=0$.

## Proof

### 1. Distinctness of the observations

The empty word, the singleton words and the two doubleton words
are different. The doubletons themselves differ for every $k\ge6$.
The parent sign-disc construction produces an actual fixed point
for each word. Equality of two phase-space points would determine
the same entire elementary orbit and hence the same sign sequence,
which is impossible. All have exact macro period one.

This argument does not require their elementary Hénon orbits to be
different at the power locus. Simplicity and nonzero traces hold on
one common parent domain for the finite list.

### 2. Mixed output differences

Use $\kappa_+=\kappa_\varnothing$ and
$\kappa_i=\kappa_{\{i\}}$. For $j=0,1$, define the output-row difference
$$
\beta_j=\kappa_{\{j-1,j+1\}}-\kappa_{j-1}
        -\kappa_{j+1}+\kappa_+.
$$
The zeroth and first Taylor coefficients vanish identically as
functions of $u$. The zeroth coefficient is common to all words;
the first is linear in their individual signs.

For any quadratic sign product, the displayed inclusion-exclusion
is zero unless its two positions are exactly $\{j-1,j+1\}$.
In that case the sign calculation is
$$
(+1)-(-1)-(-1)+(+1)=4.
$$
For $k\ge6$ this distance-two pair is not adjacent and has a unique
distance-two center. A second center would require $k$ to divide
four. Thus no adjacent coefficient $E_i$ or other $D_i$ contributes.
The wraparound pair $\{k-1,1\}$ obeys the same calculation.
Consequently, on a fixed $u$-polydisc,
$$
\boxed{\beta_j=4\epsilon^2d_uD_j(u)+O(\epsilon^3).}
$$
The remainder is holomorphic and bounded after division by
$\epsilon^3$. The sign of the leading term is positive $4dD_j$.

At zero,
$$
4dD_j(0)=e_{j-1}^T-4e_j^T+e_{j+1}^T.
$$
On the resonant subspace, where $w_{j-1}+w_{j+1}=w_j$, this row
acts as $-3w_j$.

### 3. Two independent missing directions

Let $q_\nu(i)=k^{-1/2}e^{2\pi i\nu i/k}$ and put
$$
\mathcal N=\{1,\ldots,k-1\}\setminus\{k/6,5k/6\}.
$$
There are $k-3$ indices in $\mathcal N$. Let $S$ denote cyclic phase
shift. The first-order matrix is
$C_1=(S+S^{-1}-I)/2$, with
$\ell_\nu=1-2\cos(2\pi\nu/k)\ne0$ on $\mathcal N$.

For each $\nu\in\mathcal N$, form the fixed output combination
$$
\alpha_\nu=\sum_i\overline{q_\nu(i)}(\kappa_i-\kappa_+).
$$
Its zeroth coefficient vanishes throughout the $u$-domain.
At $(\epsilon,u)=(0,0)$, after division by $\epsilon$, its limit is
$\ell_\nu q_\nu^*$.
The unscaled row $\kappa_+$ has limit $-\mathbf1^T/2$.

The two remaining scaled rows have resonant-column matrix
$$
\left(4dD_j(0)q_\pm\right)_{j=0,1}
=-\frac3{\sqrt k}
\begin{pmatrix}
1&1\\ e^{i\pi/3}&e^{-i\pi/3}
\end{pmatrix},
$$
whose determinant is $-9i\sqrt3/k\ne0$.
Thus the centers $0,1$ work. Merely saying “two distinct centers”
would not suffice: centers separated by three have dependent
resonant evaluations.

### 4. Fixed coefficient neighborhood and frame bound

Let $L$ be the constant $k\times(k+3)$ output-combination matrix
whose rows produce $\kappa_+$, the $k-3$ rows $\alpha_\nu$, and
$\beta_0,\beta_1$. Put
$$
\Delta_\epsilon=\operatorname{diag}
(1,\underbrace{\epsilon,\ldots,\epsilon}_{k-3},
\epsilon^2,\epsilon^2),\qquad
M(\epsilon,u)=\Delta_\epsilon^{-1}L\mathscr K(\epsilon,u).
$$
The exact coefficient cancellations above make $M$ jointly
holomorphic across $\epsilon=0$ on a fixed $u$-domain.
There is no division of an $O(\epsilon u)$ error by $\epsilon^2$:
the first-order mixed coefficient is identically zero in $u$.

At $(0,0)$, the first $k-2$ rows span the constant and nonresonant
Fourier covectors; the last two have the invertible resonant
projection just computed. Hence $M(0,0)$ is invertible.
Analytic continuity gives one product polydisc on which $M$ and
$M^{-1}$ are bounded. In particular $\sigma_{\min}(M)\ge c_0>0$.

For $|\epsilon|<1$ and every parameter vector $x$,
$$
\|L\|\,\|\mathscr Kx\|
\ge\|L\mathscr Kx\|
=\|\Delta_\epsilon Mx\|
\ge|\epsilon|^2c_0\|x\|.
$$
This proves the claimed lower bound; boundedness of the normalized
rows gives the upper bound. At $u=0$ the universal first jet still
annihilates resonant parameter vectors, so the order-two lower
scale is consistent with an order-two upper scale there.

### 5. These are output operations, not parameter coordinates

The matrix $L$ is constant and acts on observed spectral rows.
It is not the parameter-column matrix $Q(u)$ used in the earlier
boundary argument. More explicitly,
$$
\kappa_i-\kappa_+
=d_u\log\frac{\rho_i}{\rho_+},\qquad
\beta_j=d_u\log
\frac{\rho_{\{j-1,j+1\}}\rho_+}
     {\rho_{j-1}\rho_{j+1}}.
$$
Thus the mixed operation is a difference of logarithmic spectral
data, not the logarithmic differential of a linear difference of
raw traces. Local logarithm branches suffice. One can also use
$\operatorname{Log}(-\rho_i/\rho_+)$ near $1$; its differential is
the same. The double ratio is near $1$.

The row divisions are output rescalings at fixed $\epsilon$.
They yield a uniformly invertible processed differential, but
amplify relative data errors by factors as large as
$|\epsilon|^{-2}$. No $\epsilon$-independent conditioning of the
unprocessed relative observations is claimed.

Therefore the stated $k+3$ normalized spectral observations form
the asserted frame. This completes the bounded claim.

## Consequence and limits

At the previously constructed critical points of the old
single-minus $k$-tuple, this enlarged observation map is still
full rank once $\epsilon$ is sufficiently small. The old minor
continues to vanish: its frozen boundary theorem is not changed.
The extra observations remove rank loss of the enlarged map,
not zeros of that old determinant.

No minimality of $k+3$, global injectivity, intrinsic full-spectrum
rigidity, or extension to arbitrary periods is proved.
There is no missing lemma for the stated sufficiency result.
Questions about the smallest observation set or intrinsic spectral
information are separate questions, not additional pages supplied
by this calculation.

## Standard-tool deduction and author preflight decision

The new calculation is a finite mixed difference of an already
known second jet. It uses sign inclusion-exclusion, a two-by-two
Fourier determinant, and continuity of matrix invertibility.
The fixed-point construction and period-independent spectral
expansion are inherited, not new methods.

A concise proof occupies about 2--4 substantive English pages
with the existing second-order formula cited, often near the
lower end if the result is integrated as a corollary. Repeating
the root and Riccati constructions, the old boundary proof, or
the general Fourier machinery would not add scientific content.

**STOP the author long-paper preflight for this result.**
Retain it as a correct short structural observation; do not turn
its correctness into value/PASS, manufacture a long manuscript,
or initiate a period extension merely to meet a page threshold.
