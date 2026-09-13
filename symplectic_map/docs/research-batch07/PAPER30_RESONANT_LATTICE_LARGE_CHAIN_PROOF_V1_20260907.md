# Resonant kicked chains: a uniform large-chain author proof

Date: 2026-09-07. Status: `AUTHOR_PROOF_PENDING_INDEPENDENT_CHECK`.
Proof-writer feasibility status: `PROVABLE AS STATED` (author assessment).
This is a proof-first research record, not a candidate PASS or manuscript.
Route applicability: `NOT_APPLICABLE`.

## Claim and precise boundary

Let $L_N$ be the graph Laplacian of the path with vertices $1,\ldots,N$,
$N\ge2$. Consider the exact symplectic polynomial map
$$
p'=p-f_\eta(q)-\epsilon L_Nq,\qquad q'=q+p',
\tag{1}
$$
where $f$ acts coordinatewise and
$$
f_\eta(x)=x+\frac{5x^2+155x^3-5x^4-83x^5}{24}
             +\eta x^2(x^2-1)^2.
\tag{2}
$$
The parameter $\eta$ is fixed before varying $\epsilon$. Define
$$
\theta(\eta)=-\frac{46331}{648}+\frac{250}{27}\eta,
\qquad \theta_\pm=-4\pm\sqrt{50/3},
\qquad r_0=\sqrt{24/25}.
\tag{3}
$$

**Theorem (author claim).** For every compact set $E\subset\mathbb R$,
the uncoupled two-cycle with $(q_1,p_1)=(1,2)\leftrightarrow(-1,-2)$
and all other sites zero has a locally unique real-analytic continuation
for $\eta\in E$ and $|\epsilon|<\epsilon_E$, with $\epsilon_E>0$
independent of $N$. The branch is selected near its specified phase.

Let $K$ be a compact subset of either $(\theta_-,\theta_+)$ or
$(-\infty,\theta_-)\cup(\theta_+,\infty)$, and restrict $\eta$ by
$\theta(\eta)\in K$. There exist $N_K,\epsilon_K,C_K>0$, independent of
$N\ge N_K$, with the following properties for $0<\epsilon<\epsilon_K$.

1. If $K\subset(\theta_-,\theta_+)$, the actual two-step monodromy
   has exactly one simple reciprocal-conjugate quartet off the unit
   circle. Every other multiplier is on the unit circle and semisimple.
   Its largest log-modulus obeys the joint estimate
   $$
   \left|\frac{\log\rho(\mathcal M_{N,\eta,\epsilon})}{\epsilon}
    -\frac{\sqrt{50/3-(\theta+4)^2}}{50\sqrt3}\right|
     \le C_K\bigl(\epsilon+r_0^{2(N-1)}\bigr).
   \tag{4}
   $$
2. If $K\subset(-\infty,\theta_-)\cup(\theta_+,\infty)$, all
   multipliers are on the unit circle and semisimple. Thus each of
   these finite-chain linearized periodic motions is linearly bounded
   for all integer iterates. No nonlinear orbital stability is claimed.

This determines the two open small-coupling phases uniformly for long
finite chains. It does not classify $\theta=\theta_\pm$, parameters
approaching those endpoints with $\epsilon$ or $N$, or every short
finite chain. It does not construct a nonlinear infinite-chain orbit,
claim optimal constants, or assert a bound uniform in time and $N$ for
the norms of all monodromy powers. All such additions require separate
proofs. Negative coupling is not part of the phase assertion.

The two uncoupled local maps have the same first-order data for every
$\eta$ in (2). Their higher jets are not fixed: in particular $f''$
changes. The theorem concerns this one specified family, not arbitrary
couplings or a universality classification.

## Prior deductions and dependency map

Breather continuation and symplectic signature methods are established
tools. The non-symmetric one-negative-square Jacobi model used below
is exactly a specialization of Derevyagin--Perotti--Wojtylak,
*Truncations of a class of pseudo-Hermitian operators*, equations
(I.1), (II.3)--(II.4), and the semicircle example III.5:
[author text](https://arxiv.org/html/1503.04314v1).
After replacing $J$ by $(J+4I)/2$, their parameters are
$a_0=(\theta+4)/2$, $b_0^2=1/24$, $a_j=0$, $b_j=1$ for $j\ge1$.
The closed roots and thresholds in the Jacobi problem are therefore
not a new spectral mechanism. The finite terminal diagonal here is
$-2$ rather than the infinite background's $-4$; its effect is
explicitly retained, not erased by applying a truncation label.

The possible new statement is the uniform actual-map conclusion for
(1)--(2), after all these deductions. Scientific value and natural
capacity remain unassessed. This record uses `proof-writer` to keep
the actual map, the limit matrix, and their quantifiers separate.

The proof proceeds through: uniform local continuation; exact two-step
reduction; uniform matrix remainder; a scalar finite-chain resolvent;
uniform persistence of a nonreal pair or a negative-type real line;
and recovery of the complete symplectic multiplier spectrum.

## 1. Uniform continuation and the moving orbit

Write $a=q^0$, $b=q^1$. A two-cycle is equivalent to
$$
f_\eta(a)+\epsilon L_Na-2a+2b=0,
\qquad
f_\eta(b)+\epsilon L_Nb+2a-2b=0.
\tag{5}
$$
Its momenta are $p^0=a-b$, $p^1=b-a$. At zero coupling take
$a=e_1$, $b=-e_1$. Equation (2) gives
$$
f(0)=0,\quad f'(0)=1,\quad f(1)=4,\quad f(-1)=-4,
\quad f'(1)=8/3,\quad f'(-1)=7/2.
\tag{6}
$$
The derivative of (5) in $(a,b)$ is block diagonal by site, with blocks
$$
D_0=\begin{pmatrix}-1&2\\2&-1\end{pmatrix},\qquad
D_*=\begin{pmatrix}2/3&2\\2&3/2\end{pmatrix}.
\tag{7}
$$
Both have determinant $-3$. In the maximum norm their inverses have
norm at most $7/6$. Also $\|L_N\|_{\infty\to\infty}\le4$ for every $N$.
On a fixed small complex neighborhood of $0,1,-1$, the derivatives of
the polynomial (2) are uniformly bounded for $\eta$ in a compact set.

For completeness, put $u=(a-e_1,b+e_1)$ and write (5) as
$D u+\epsilon v+\epsilon\mathcal L u+R_\eta(u)=0$.
Here $\|v\|_\infty\le1$, $\|\mathcal L\|\le4$, and
$\|R_\eta(u)-R_\eta(w)\|_\infty\le C r\|u-w\|_\infty$
when $\|u\|_\infty,\|w\|_\infty\le r$, with $C$ independent of $N$.
Choose $r$ so $(7/6)Cr<1/4$, and then $|\epsilon|$ so
$(7/6)4|\epsilon|<1/4$ and $(7/6)|\epsilon|<r/2$.
The resulting fixed-point map is a contraction of this ball, uniformly
in $N$. Its iterates are holomorphic in $\epsilon$ and converge uniformly
on a smaller disk. This proves the asserted analytic local branch and
its uniqueness. Reality follows from conjugation and uniqueness.
Taking $r<1/2$ keeps $a_1$ and $b_1$ distinct, so the branch has exact
period two. Compact $\eta$-sets share all constants above.

Differentiating (5), only sites 1 and 2 have nonzero forcing.
Using the inverses of (7) gives
$$
\dot a_1=7/6,\quad\dot b_1=-8/9,\qquad
\dot a_2=-1/3,\quad\dot b_2=1/3,
\tag{8}
$$
and zero at all other sites. A dot means derivative at $\epsilon=0$.
Cauchy estimates on the common analytic disk give the first-order
Taylor remainder $O(\epsilon^2)$ in the maximum norm, uniformly in $N$
and compact $\eta$-sets. This bound also controls the diagonal
multiplication operators obtained from $f'_\eta(a),f'_\eta(b)$ in
the Euclidean operator norm.

## 2. Exact monodromy reduction and its uniform first derivative

Define the real symmetric stiffness matrices and their complements
$$
K_a=\operatorname{diag}f'_\eta(a)+\epsilon L_N,\quad
K_b=\operatorname{diag}f'_\eta(b)+\epsilon L_N,
\qquad C_a=2I-K_a,\quad C_b=2I-K_b.
\tag{9}
$$
The variational recurrence is $u_{j+1}+u_{j-1}=C_j u_j$ with $C_j$
alternating between $C_a,C_b$. Its even subsequence satisfies exactly
$$
u_{2k+4}=W u_{2k+2}-u_{2k},\qquad W=C_bC_a-2I.
\tag{10}
$$
Indeed, eliminate $u_{2k+1}$ in two successive recurrence equations.
The change from $(u_0,u_{-1})$ to $(u_2,u_0)$ is invertible because
$C_b$ is uniformly close to $\operatorname{diag}(-3/2,1,\ldots,1)$.
Consequently the actual two-step monodromy is similar to
$$
\begin{pmatrix}W&-I\\I&0\end{pmatrix}.
\tag{11}
$$
For each eigenvalue $w$ of $W$, its corresponding multipliers, with
algebraic multiplicities, satisfy $\lambda+\lambda^{-1}=w$.
Near $w=-1$ these two roots are distinct. Semisimplicity of a real $w$
therefore gives semisimplicity of both associated multipliers.

At zero coupling $C_a^0=\operatorname{diag}(-2/3,1,\ldots,1)$,
$C_b^0=(C_a^0)^{-1}$ and $W(0)=-I$. Put
$$
R_{N,\eta}(\epsilon)=\frac{W(\epsilon)+I}{\epsilon},
\tag{12}
$$
with its removable value at zero. Equations (8)--(9) imply
$$
R_{N,\eta}(\epsilon)=J_N(\theta)+O(\epsilon)
\tag{13}
$$
in Euclidean operator norm, uniformly in $N$ and compact $\eta$-sets.
Before a fixed diagonal normalization, $J_N$ has first diagonal $\theta$,
background diagonal $-2\deg(i)$, background neighbor entries 2,
entry $(1,2)=-1/2$, and entry $(2,1)=1/3$.
For example, each off-diagonal entry in $W'$ is
$(C_a^0)_{jj}+(C_b^0)_{ii}$ on an edge. At site 2 the two orbit shifts
in (8) cancel the two contributions involving $f''(0)$.
At site 1 the diagonal is
$$
\frac32\left(1+\frac76\alpha\right)
+\frac23\left(1-\frac89\beta\right)
=\frac{13}{6}+\frac74\alpha-\frac{16}{27}\beta,
\tag{14}
$$
where $\alpha=-65/2+8\eta$, $\beta=85/3+8\eta$. This is (3).

Conjugating by $S=\operatorname{diag}(\sqrt{3/2},1,\ldots,1)$, that is
replacing $J_N$ by $S^{-1}J_NS$, gives
$$
J_N(\theta)=\begin{pmatrix}\theta&-g e_1^T\\g e_1&T_n\end{pmatrix},
\quad n=N-1,\quad g=1/\sqrt6,
\quad T_n=-2L_n-2e_1e_1^T.
\tag{15}
$$
We use these normalized coordinates henceforth. In them the exact
matrix $R(\epsilon)$ is selfadjoint for the symmetric form
$G(\epsilon)=S^T C_a(\epsilon)S$:
$$
R(\epsilon)^T G(\epsilon)=G(\epsilon)R(\epsilon),
\qquad G(0)=\operatorname{diag}(-1,I_n).
\tag{16}
$$
This follows directly from $W^T C_a=C_aW$. Uniform closeness to $G(0)$
shows that $G(\epsilon)$ has exactly one negative square, for a common
small $|\epsilon|$. No finite-frequency truncation has been used.

## 3. Finite-chain resolvent and the limiting roots

The matrix $T_n$ has spectrum in $[-8,0]$: its quadratic form is
$-2\sum_{j=1}^{n-1}|v_{j+1}-v_j|^2-2|v_1|^2$, and the absolute
row sums are at most 8. For $z\notin[-8,0]$ put
$$
m_n(z)=e_1^T(zI-T_n)^{-1}e_1,\qquad
\Phi_n(z)=z-\theta+\frac16m_n(z).
\tag{17}
$$
The Schur complement gives
$\det(zI-J_N)=\det(zI-T_n)\Phi_n(z)$. Thus off the background
interval, zeros of $\Phi_n$ are exactly the eigenvalues of $J_N$,
including multiplicity. The block inverse formula also shows that
$(zI-J_N)^{-1}$ is uniformly bounded whenever
$\operatorname{dist}(z,[-8,0])$ and $|\Phi_n(z)|$ have positive
lower bounds, with bounded $z$ and $\theta$.

Let $U_j$ be the Chebyshev polynomial of the second kind, with
$U_{-1}=0,U_0=1$. Expansion of the tridiagonal determinant, including
its final diagonal $-2$, yields for $n\ge1$
$$
\det(zI-T_n)=2^n\{U_n(x)-U_{n-1}(x)\},\quad
m_n(z)=\frac{U_{n-1}(x)-U_{n-2}(x)}
                 {2\{U_n(x)-U_{n-1}(x)\}},\quad x=(z+4)/4.
\tag{18}
$$
For $n=1$, the numerator is interpreted as $U_0-U_{-1}=1$;
the formula gives $m_1=1/(z+2)$. For larger $n$, the cofactor at
$(1,1)$ has the same terminal diagonal and size $n-1$, proving
the quotient in (18) as well as the determinant recurrence.

There is a unique solution $r=r(z)$ of
$z+4=2(r+r^{-1})$ with $|r|<1$ off $[-8,0]$:
$$
r(z)=\frac{z+4-\sqrt{(z+4)^2-16}}4.
\tag{19}
$$
The square root is chosen to behave as $z+4$ at infinity. Substitution
of $U_j((r+r^{-1})/2)=(r^{-j-1}-r^{j+1})/(r^{-1}-r)$ into (18)
gives the useful exact identities
$$
m_n(z)=\frac r2\frac{1+r^{2n-1}}{1+r^{2n+1}},\qquad
m_n(z)-m_\infty(z)=\frac{r^{2n}(1-r^2)}{2(1+r^{2n+1})},
\quad m_\infty(z)=r(z)/2.
\tag{20}
$$
These identities imply uniform convergence, with all derivatives,
on each compact subset of the slit plane. Derivative convergence
follows from the same uniform bound on a slightly larger compact
neighborhood and Cauchy's integral formula.

Write $a=\theta+4$ and $\Phi_\infty=z-\theta+m_\infty/6$.
A physical zero obeys $25r^2-12ar+24=0$. Eliminating $r$ gives
$$
150z^2+(24-294\theta)z+1-24\theta+144\theta^2=0.
\tag{21}
$$
In the open interval $|a|<\sqrt{50/3}$ both roots are physical:
$$
z_\pm=\frac{49\theta-4\pm iY}{50},\quad
Y=\sqrt{50/3-a^2},\qquad
r(z_\pm)=\frac6{25}(a\mp iY),\quad |r(z_\pm)|=r_0<1.
\tag{22}
$$
They lie off the real axis. In the exterior $|a|>\sqrt{50/3}$,
we only need the root
$$
z_{\rm neg}=\frac{49\theta-4+\operatorname{sgn}(a)
                         \sqrt{a^2-50/3}}{50},\qquad
r(z_{\rm neg})=\frac6{25}\{a-\operatorname{sgn}(a)
                         \sqrt{a^2-50/3}\}.
\tag{23}
$$
It is real with $|r|<r_0<1$, hence lies outside $[-8,0]$.
The other root of (21) need not be on the physical sheet and is
not used to assert an additional eigenvalue.

At each selected root,
$$
\Phi_\infty'(z)=1-\frac{r^2}{24(1-r^2)}
                  =\frac{24-25r^2}{24(1-r^2)}.
\tag{24}
$$
In (22) it is nonzero: equality would require $r=\pm r_0$ real,
which would force an excluded endpoint. In (23) it is positive.
These facts, their strict margins, and positive distance from the
background interval are uniform on each compact $K$ in the claim.

## 4. Uniform finite-chain and actual-matrix persistence

For the selected root functions in (22) or (23), compactness and (24)
give circles of a common sufficiently small radius centered at the
roots, on which $|\Phi_\infty|$ has a uniform positive lower bound.
Their closed disks avoid $[-8,0]$ and contain precisely one simple
limit zero each; in the nonreal case the two disks stay disjoint and
away from the real axis. These statements follow by choosing the
radius so the variation of $\Phi_\infty'$ in a disk is less than
half the minimum of its absolute value at the centers, and then
decreasing it to respect the indicated distances.

Uniform convergence from (20) and Rouché's theorem show that each
disk contains precisely one eigenvalue $z_N$ of $J_N$, of algebraic
multiplicity one, for all $N\ge N_K$. Its Riesz projection has rank
one. The resolvent bound following (17) is uniform on the circles.
Moreover,
$$
|z_N-z_*|\le C_K r_0^{2n},\qquad n=N-1,
\tag{25}
$$
where $z_*$ denotes the chosen root. To obtain the stated rate rather
than a rate on the contour, evaluate (20) at $z_*$, where $|r|\le r_0$.
The denominator is at least $1-r_0^{2n+1}$. Consequently
$|\Phi_n(z_*)|\le C_Kr_0^{2n}$. After the disks are made small,
derivative convergence and (24) ensure
$$
\left|\int_0^1\Phi_n'\bigl(z_*+t(z_N-z_*)\bigr)\,dt\right|
\ge c_K>0.
$$
Indeed the integrand stays within half the modulus of the fixed
complex number $\Phi_\infty'(z_*)$. Apply the integral identity for
$\Phi_n(z_N)-\Phi_n(z_*)$ to prove (25). The exterior root is real
because the disk and real-coefficient characteristic polynomial
are conjugation invariant and the root is unique.

By (13), $\|R(\epsilon)-J_N\|\le C_K|\epsilon|$. The preceding
uniform resolvent bound and the Neumann series give invertibility
on all these circles for a common $|\epsilon|<\epsilon_K$, as well
as an $O_K(|\epsilon|)$ difference of their resolvents and Riesz
projections. Continuity through $t\epsilon$, $0\le t\le1$, preserves
the rank-one projections. The resulting actual eigenvalues satisfy
$$
|z_{N,\epsilon}-z_N|\le C_K|\epsilon|.
\tag{26}
$$
One dimension-independent justification is the contour formula for
the rank-one spectral first moment. Both
$R(\epsilon)\Pi_\epsilon-J_N\Pi_0$ and the difference of the two
projections have rank at most two. The resolvent identity bounds
their operator norms by $C_K|\epsilon|$; the absolute trace is at
most rank times operator norm. The traces of the first moments are
the respective simple eigenvalues, proving (26).

In the exterior case we must also preserve a sign, not just reality.
An eigenvector of $J_N$ for the real root is
$$
v_N=\binom{1}{g(z_NI-T_n)^{-1}e_1}.
$$
Using $m_n'(z)=-\|(zI-T_n)^{-1}e_1\|^2$ for real $z$ gives
$$
v_N^T G(0)v_N=-1+g^2\|(z_NI-T_n)^{-1}e_1\|^2
                    =-\Phi_n'(z_N)\le-c_K<0.
\tag{27}
$$
The vectors have uniformly bounded Euclidean norm. Put
$v_{N,\epsilon}=\Pi_\epsilon v_N$. The projection estimate, (16),
and (27) preserve a uniform strictly negative value of
$v_{N,\epsilon}^TG(\epsilon)v_{N,\epsilon}$. This vector is real
for real $\epsilon$, by the conjugation-invariant contour projection.
The unique eigenvalue in the real-centered disk is real as well.

## 5. Exhaustion of possible nonreal eigenvalues

We give the finite-dimensional signature argument to avoid requiring
uniform separation of the increasingly dense background eigenvalues.
If a real matrix $A$ satisfies $A^TG=GA$ and the real symmetric
invertible form $G$ has one negative square, a strictly negative
invariant line has a $G$-orthogonal invariant complement on which
$G$ is positive definite. The restriction of $A$ to that complement
is selfadjoint for a positive definite inner product, and hence
has only real semisimple eigenvalues. The direct sum is all of the
space since the line is nondegenerate. Applying this to (27) proves
the same conclusion for every eigenvalue of $R(\epsilon)$ in the
exterior phase, including the isolated real one.

For the interior phase, the two persisting roots are a simple
nonreal conjugate pair. Its real invariant plane has signature
$(1,1)$. Here is an explicit reason. Over the complexification use
the Hermitian form $[v,w]=v^*Gw$. If $Av=zv$ and $\Im z\ne0$,
selfadjointness gives $[v,v]=0$. The vector $\bar v$ is a simple
eigenvector for $\bar z$. The pairing $[v,\bar v]$ is nonzero:
$v^*G$ is a nonzero left eigenvector for $\bar z$, and for an
algebraically simple eigenvalue the left and right eigenvectors
cannot have zero pairing. Otherwise the right eigenvector belongs
to the range of $A-\bar z I$, producing a generalized eigenvector
and contradicting algebraic simplicity. Thus the Gram matrix on
$\operatorname{span}_{\mathbb C}\{v,\bar v\}$ is
$$
\begin{pmatrix}0&c\\\bar c&0\end{pmatrix},\qquad c\ne0,
$$
with one positive and one negative eigenvalue. The same inertia
holds on its real invariant plane. Its $G$-orthogonal complement
is invariant and positive definite, as the unique negative square
has been exhausted. All eigenvalues on that complement are real
and semisimple. Apply this to $A=R(\epsilon)$ and $G=G(\epsilon)$.
There is exactly one nonreal conjugate pair and no further nonreal
eigenvalues or real Jordan blocks.

## 6. Return to the symplectic multipliers

Uniform operator norm bounds in (13) show that every eigenvalue $z$
of $R(\epsilon)$ is bounded independently of $N$ on the compact
parameter set. Its corresponding eigenvalue of $W$ is
$w=-1+\epsilon z$. For all sufficiently small positive $\epsilon$,
each real $w$ therefore lies strictly between $-2$ and 2. The roots
of $\lambda+\lambda^{-1}=w$ are distinct and on the unit circle.
The exact companion reduction (11) and the semisimplicity just
proved give semisimple multipliers for every such real $w$.
For example, on each eigenspace of $W$ the companion matrix is a
direct sum of the scalar $2\times2$ companion, whose two roots
are distinct. In the exterior phase this accounts for the full
$2N$-dimensional monodromy; diagonalizability with unit-modulus
eigenvalues implies bounded powers for each fixed finite matrix.

In the interior phase the one nonreal conjugate pair of $w$ gives
exactly four distinct multipliers $\lambda,\bar\lambda,
\lambda^{-1},\bar\lambda^{-1}$ off the unit circle. Each is simple.
For the analytic root near $\lambda_0=e^{2\pi i/3}$,
$$
\log\lambda(-1+\epsilon z)=\log\lambda_0
                   +\frac{\epsilon z}{i\sqrt3}+O_K(\epsilon^2).
\tag{28}
$$
This follows by differentiating
$\lambda+\lambda^{-1}=w$, since
$\lambda_0-\lambda_0^{-1}=i\sqrt3$; the remainder is uniform for
bounded $z$. For the upper-half-plane root in (22), (25)--(26)
give
$$
\Im z_{N,\epsilon}=\frac{Y}{50}
                  +O_K\bigl(\epsilon+r_0^{2(N-1)}\bigr).
$$
Taking the real part in (28) proves (4); all other multipliers have
modulus one or are the remaining members of the same quartet.
This completes the author proof of the stated theorem. $\square$

## Corrections, exclusions, and remaining review risks

No theorem-level weakening is used between the claim and the proof.
The fixed parameter family (2), the compact-set restrictions, and
the separation from the two limiting thresholds are essential to
the statement proved here. A fixed-size perturbation theorem alone
would not give the common $\epsilon_K$; (17), (20), and the signature
decomposition supply the required dimension-independent control.

The closed Jacobi roots and the general one-negative-square
mechanism are prior deductions, not credited as new. The actual-map
uniform theorem has not yet undergone independent proof checking or
a completed novelty/value assessment. In particular, the relation
to the full statements in MacKay--Sepulchre (1998), beyond an accessed
abstract, remains a literature-access uncertainty, not a claim of
absence. This document makes no publication-capacity or candidate
selection assertion, and no numerical experiment substitutes for
the proof above.
