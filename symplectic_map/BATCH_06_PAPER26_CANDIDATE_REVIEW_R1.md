# Paper 26 Candidate Review R1

## Candidate identity and R1 disposition

**Working title.** *Global Selector Rigidity and Quadratic Dynamical Degrees for Two-Mode Hamiltonian Product Shears*.

**Frozen candidate.** Let \(K\) be a field of characteristic zero. Let

\[
\varnothing\ne E\subset \mathbf Z_{\ge 2}^{\,2}
\]

be finite, let every \(c_{xy}\in K^\times\), and put

\[
V(q_1,q_2)=\sum_{(x,y)\in E}c_{xy}q_1^xq_2^y,
\qquad
W(p_1,p_2)=\alpha p_1^{e+1}+\beta p_2^{f+1},
\]

where \(\alpha,\beta\in K^\times\) and \(e,f\ge2\). With the sign convention

\[
S(q,p)=(q,p+\nabla V(q)),\qquad
T(q,p)=(q+\nabla W(p),p),
\]

consider \(F=T\circ S\). Reversing both shear signs makes no difference to the degree assertions.

**R1 verdict.** PASS, conditional on preserving exactly the hypotheses and claim boundaries stated below. Within the frozen local corpus, this is the strongest Paper 26 candidate because it joins four pieces not previously joined locally: arbitrary finite positive two-dimensional Newton support, a global contraction/classification theorem for its selector, exact forward--inverse degree comparison, and a uniform quadratic bound on the dynamical degree. This is a local portfolio judgment, not a global priority opinion.

## Exact theorem statement recommended for Paper 26

For \(u=(u_1,u_2)\in\mathbf R_{>0}^2\), define

\[
H(u)=\max_{(x,y)\in E}(xu_1+yu_2),
\qquad
\mathcal A(u)=\bigl(H(u)-u_1,H(u)-u_2\bigr),
\]

and

\[
B=\operatorname{diag}(e,f),\qquad \kappa=\frac ef.
\]

For an exponent \((x,y)\), also define the chamber matrix

\[
A_{x,y}=\begin{pmatrix}x-1&y\\x&y-1\end{pmatrix},
\qquad
C_{x,y}=BA_{x,y}.
\]

On a chamber on which \((x,y)\) is exposed, \(\mathcal A(u)=A_{x,y}u\). On a wall, the same degree vector is obtained from every exponent in the exposed face, although the leading polynomial is the derivative of the whole face polynomial and must not be replaced by one monomial in the noncancellation proof.

The recommended main theorem is the following conjunction.

### Theorem A: exact degrees, selector rigidity, and spectral cap

Under the frozen hypotheses above:

1. The coordinate-degree vectors of all forward and inverse half-steps are exact. With

   \[
   u_0^+=v_0^-=(1,1)^{\mathsf T},
   \]

   they obey

   \[
   v_{n+1}^+=\mathcal A(u_n^+),
   \qquad
   u_{n+1}^+=Bv_{n+1}^+=B\mathcal A(u_n^+),
   \tag{F}
   \]

   and

   \[
   u_{n+1}^-=Bv_n^-,
   \qquad
   v_{n+1}^-=\mathcal A(u_{n+1}^-)=\mathcal A(Bv_n^-).
   \tag{I}
   \]

   Here \(u_n^+\) is the \(q\)-degree vector after \(F^n\), \(v_{n+1}^+\) is the intervening \(p\)-degree vector after the \(S\)-phase, \(v_n^-\) is the \(p\)-degree vector after \(F^{-n}\), and \(u_{n+1}^-\) is the intervening and final \(q\)-degree vector after the \(T^{-1}\)-phase.

2. If

   \[
   c_0=H(1,1)-1=\max_{(x,y)\in E}(x+y)-1,
   \]

   then the forward and inverse states satisfy the exact bridge

   \[
   \boxed{\ u_{n+1}^+=c_0Bv_n^-\ }
   \qquad(n\ge0).
   \tag{B}
   \]

   Consequently the forward and inverse first dynamical degrees exist and are equal.

3. In the forward projective coordinate \(r=u_1/u_2\), write

   \[
   \Phi(r)=H(r,1)=\max_{(x,y)\in E}(xr+y).
   \]

   The induced degree map is

   \[
   \boxed{\ \phi(r)=\kappa\frac{\Phi(r)-r}{\Phi(r)-1}\ }.
   \tag{P}
   \]

   It is globally strictly decreasing on \(\mathbf R_{>0}\), and its logarithmic conjugate

   \[
   \psi(t)=\log\phi(e^t)
   \]

   is a uniform contraction of \(\mathbf R\). Hence there is a unique fixed positive ray and every positive ray converges to it.

4. If the fixed ray is in the interior of one Newton chamber, every selector orbit is eventually stationary. If the fixed ray is on a wall, the exact tie orbit stays on that wall, while every strict orbit is eventually an alternation of the two chambers adjacent to the wall. At a multiple tie, “adjacent” means the two extreme exposed choices immediately to the left and right; the whole tied face is used on the wall itself. Thus every selector tail has period at most two, and no selector cycle of length \(k>2\) occurs.

5. If the fixed ray is interior, the dynamical degree is the Perron root of one positive integral \(2\times2\) chamber matrix \(C_{x,y}\), so

   \[
   [\mathbf Q(\lambda):\mathbf Q]\le2.
   \]

   If the fixed ray lies on a wall, the two adjacent matrices share the same positive fixed ray and the same one-step multiplier \(\mu\); this multiplier is an integer, and \(\lambda=\mu\). Therefore, uniformly in both cases,

   \[
   \boxed{\ [\mathbf Q(\lambda):\mathbf Q]\le2\ }.
   \tag{D}
   \]

6. The ordinary scalar degree sequence is eventually governed by a recurrence of order at most two in the stationary case. In the strict wall case, each stride-two subsequence is governed by an order-at-most-two recurrence, and their full interlacing is governed by an order-at-most-four recurrence. A selector alternation is not a numerical two-cycle: the projective ratios converge strictly to the wall. If the fixed ray is \(r_*=1\), the ordinary seed is already fixed and its degree sequence is geometric.

The theorem should assert upper recurrence orders, not minimal orders. It should assert the first dynamical degree only; no higher dynamical-degree, entropy, compactification, integrability, or conjugacy conclusion follows here.

## Proof audit

### 1. Exposed-face Hessian lemma

For a positive weight \(u\), let

\[
E_u=\{(a,b)\in E:au_1+bu_2=H(u)\}
\]

and let

\[
P_u(X,Y)=\sum_{(a,b)\in E_u}c_{ab}X^aY^b
\]

be the exposed-face polynomial. Choose an endpoint \((a,b)\) of the convex hull of \(E_u\). The monomial

\[
X^{2a-2}Y^{2b-2}
\]

in

\[
\det\operatorname{Hess}P_u=(P_u)_{XX}(P_u)_{YY}-(P_u)_{XY}^2
\]

can only arise from pairing \((a,b)\) with itself. Indeed, any other contributing pair \(\xi,\eta\in E_u\) would satisfy \(\xi+\eta=2(a,b)\), contradicting extremality of \((a,b)\). Its coefficient is

\[
c_{ab}^{\,2}\bigl[a(a-1)b(b-1)-a^2b^2\bigr]
=c_{ab}^{\,2}ab(1-a-b),
\]

which is nonzero because \(a,b\ge2\), \(c_{ab}\ne0\), and \({\rm char}(K)=0\). Thus

\[
\det\operatorname{Hess}P_u\ne0.
\tag{H}
\]

The Jacobian determinant of \(((P_u)_X,(P_u)_Y)\) is exactly (H). By the characteristic-zero Jacobian criterion, the two partial derivatives are algebraically independent over \(K\).

This endpoint-coefficient argument works for a single exposed monomial, a two-point wall, or a face containing three or more collinear support points. It is the indispensable replacement for positivity: no common sign assumption on the coefficients is needed.

### 2. Why the Hessian lemma closes wall and inverse noncancellation

Suppose \(L_1,L_2\) are algebraically independent leading forms. Evaluation \(K[X,Y]\to K[L_1,L_2]\) is injective. Therefore neither exposed-face derivative vanishes after substitution, and

\[
(P_u)_X(L_1,L_2),\qquad(P_u)_Y(L_1,L_2)
\]

remain algebraically independent. Taking positive integer powers preserves algebraic independence. Starting with \(q_1,q_2\), this proves inductively that the leading \(q\)-forms in every forward step are algebraically independent. Starting with \(p_1,p_2\), it proves the analogous fact for every inverse step.

This is stronger than merely observing that formal monomials have distinct exponent vectors. At a wall, several top-weight monomials can contribute, and with arbitrary signs a formal cancellation concern is real. Injectivity after the face-Hessian lemma rules it out. The same induction also rules it out after the phase order is reversed in \(F^{-1}=S^{-1}\circ T^{-1}\).

### 3. Carry domination and exact vector recursions

For every \(u>0\), the support condition \(x,y\ge2\) gives

\[
H(u)\ge2u_1+2u_2.
\]

Hence

\[
H(u)-u_1\ge u_1+2u_2>\max(u_1,u_2),
\]

and

\[
H(u)-u_2\ge2u_1+u_2>\max(u_1,u_2).
\tag{C}
\]

Thus each fresh component of \(\nabla V\) dominates every carried component. Since \(e,f\ge2\), each fresh component of \(\nabla W\) likewise dominates the carried \(q\)-coordinates. The exposed-face argument proves that these nominal top degrees are attained, and (C) prevents cancellation with the carried coordinate. This proves (F).

For the inverse, \(T^{-1}\) first produces degree vector \(Bv_n^-\), dominating the carried \(q\)-coordinates; \(S^{-1}\) then produces \(\mathcal A(Bv_n^-)\), dominating both the new \(q\)-coordinates and the carried \(p\)-coordinates. The same face-Hessian induction proves attainment. This proves (I) with no generic-coefficient qualification.

For \(n\ge1\), the fresh \(q\)-coordinates dominate all \(p\)-coordinates in \(F^n\), while the fresh \(p\)-coordinates dominate all \(q\)-coordinates in \(F^{-n}\). Consequently

\[
\deg(F^n)=\lVert u_n^+\rVert_\infty,
\qquad
\deg(F^{-n})=\lVert v_n^-\rVert_\infty.
\tag{V}
\]

### 4. Exact forward--inverse bridge

Because

\[
\mathcal A(1,1)=c_0(1,1),
\]

the case \(n=0\) of (B) is

\[
u_1^+=B\mathcal A(1,1)=c_0Bv_0^-.
\]

If \(u_{n+1}^+=c_0Bv_n^-\), homogeneity of \(\mathcal A\) gives

\[
\begin{aligned}
u_{n+2}^+
&=B\mathcal A(u_{n+1}^+)\\
&=B\mathcal A(c_0Bv_n^-)\\
&=c_0B\mathcal A(Bv_n^-)\\
&=c_0Bv_{n+1}^-.
\end{aligned}
\]

This proves (B) for all \(n\ge0\). Combining it with (V) yields

\[
c_0\min(e,f)\deg(F^{-n})
\le \deg(F^{n+1})
\le c_0\max(e,f)\deg(F^{-n}),
\]

so the two exponential growth rates are equal.

There is also an exact phase conjugacy. If

\[
G=B\circ\mathcal A,\qquad G^-=\mathcal A\circ B,
\]

then

\[
B\circ G^-=G\circ B.
\]

Since \(B\) is invertible on the positive cone, the forward \(BA\) and inverse \(AB\) projective systems are conjugate by the projective scaling \(r\mapsto\kappa r\). The bridge above is stronger than a bare spectral \(AB/BA\) observation because it compares the literal ordinary-degree states from their ordinary seeds.

### 5. Uniform logarithmic contraction

On a chamber exposed by \((x,y)\),

\[
\Phi(r)=xr+y
\]

and

\[
\phi(r)=\kappa\frac{(x-1)r+y}{xr+y-1}.
\]

Direct differentiation gives

\[
\phi'(r)=\kappa\frac{1-x-y}{(xr+y-1)^2}<0.
\tag{M}
\]

More importantly, the derivative in logarithmic coordinates satisfies the explicit strict inequality

\[
\left|\frac{d\log\phi}{d\log r}\right|
=\frac{r(x+y-1)}{((x-1)r+y)(xr+y-1)}<1.
\tag{L}
\]

Indeed, the denominator minus the numerator in (L) is

\[
\begin{aligned}
&((x-1)r+y)(xr+y-1)-r(x+y-1)\\
&\qquad=x(x-1)r^2+2(x-1)(y-1)r+y(y-1)>0.
\end{aligned}
\tag{G}
\]

For each of the finitely many \((x,y)\in E\), the ratio in (L) extends continuously to \(r=0\) and \(r=\infty\), with value zero at both ends. Its supremum is therefore strictly below one. Taking the maximum over finite \(E\) gives a common \(q<1\). The function \(\Phi\), and hence \(\phi\), is continuous at every Newton wall. Integrating the one-sided logarithmic derivative across the finitely many walls shows

\[
|\psi(t)-\psi(s)|\le q|t-s|
\qquad(s,t\in\mathbf R).
\]

Thus \(\psi\) is a contraction of the complete metric space \(\mathbf R\). Banach's theorem gives a unique fixed \(t_*\), and every logarithmic ratio converges to it. Equation (M), together with continuity at walls, also makes \(\phi\) globally strictly decreasing.

### 6. Complete selector-tail classification

Let \(r_*=e^{t_*}\).

If \(r_*\) lies strictly inside a Newton chamber, convergence eventually places every orbit in that chamber; the selector is therefore stationary from some finite time onward.

If \(r_*\) is a Newton wall, strict decrease and \(\phi(r_*)=r_*\) imply

\[
r<r_*\Longrightarrow\phi(r)>r_*,
\qquad
r>r_*\Longrightarrow\phi(r)<r_*.
\tag{S}
\]

Because \(\phi\) is injective, no off-wall point can land on \(r_*\). Convergence eventually confines every strict orbit to the two chambers adjacent to the wall, and (S) then forces their alternation. A point on the wall remains there by homogeneity. At a multiple tie, the two side chambers are governed by the two extreme exposed exponents, while the tie step uses the full face polynomial already handled by the Hessian lemma.

Uniform contraction excludes every nonfixed numerical periodic orbit, including a numerical two-cycle. The only period two in the conclusion is the eventual **selector word** on opposite sides of a limiting wall. Therefore no selector tail of period \(k>2\) exists.

### 7. Spectral degree: why the sharp bound is two, not four

In an interior chamber the tail matrix is

\[
C=C_{x,y}
=\begin{pmatrix}
e(x-1)&ey\\
fx&f(y-1)
\end{pmatrix},
\]

a strictly positive integral \(2\times2\) matrix. Its fixed positive ray is its Perron ray, so

\[
\lambda=\rho(C)
\]

and the characteristic polynomial of \(C\) proves \([\mathbf Q(\lambda):\mathbf Q]\le2\).

Now suppose the fixed ray lies on a wall. A genuine wall has rational slope, so choose a primitive \(w\in\mathbf Z_{>0}^2\) on it. Let \(C_-\) and \(C_+\) be the matrices of the adjacent left and right chambers. Every exponent on the tied face has the same dot product with \(w\), hence

\[
C_-w=C_+w=B\mathcal A(w)=\mu w
\tag{W}
\]

for one common \(\mu>0\). The vector on the left of (W) is integral. Since \(w\) is primitive, Bézout applied to its two coordinates shows \(\mu\in\mathbf Z\); equivalently, \(\mu\) is a rational eigenvalue of an integral matrix and hence a rational algebraic integer.

Both \(C_-\) and \(C_+\) are positive, so their common positive eigenvector is their Perron eigenvector. Moreover

\[
M=C_+C_-,\qquad Mw=\mu^2w,
\]

and positivity gives \(\rho(M)=\mu^2\). The one-step dynamical degree of the alternating tail is therefore

\[
\lambda=\sqrt{\rho(M)}=\mu\in\mathbf Z.
\]

A generic monodromy argument would only say that \(\lambda\) satisfies an equation of degree at most four. That bound is valid but nonsharp here. The uniform contraction identifies the limiting wall, and the common-ray identity (W) sharpens it to degree one in the wall case. The uniform conclusion is degree at most two.

### 8. Scalar recurrences

In the stationary case, each coordinate of the tail state satisfies Cayley--Hamilton for \(C\):

\[
z_{n+2}-\operatorname{tr}(C)z_{n+1}+\det(C)z_n=0.
\tag{R2}
\]

If \(r_*\ne1\), convergence makes one \(q\)-coordinate the permanent visible maximum, so the ordinary total degree itself eventually satisfies (R2). If \(r_*=1\), the ordinary seed \((1,1)\) is already on the unique fixed ray, and the actual degree sequence is geometric. The inverse sequence has the same order bound through the conjugate \(AB\) phase system and its own eventual visible coordinate.

In the strict wall case, the even and odd state subsequences are iterates of \(C_+C_-\) and \(C_-C_+\), respectively. These products have the same trace and determinant. Once the visible coordinate has stabilized on each parity, both scalar parities satisfy the same stride-two recurrence, which can be written on the full sequence as

\[
d_{n+4}-\operatorname{tr}(M)d_{n+2}+\det(M)d_n=0
\tag{R4}
\]

for all sufficiently large \(n\). Thus each stride-two subsequence has order at most two and the full interleaving has order at most four. If the ordinary seed lies on the wall, it is fixed projectively and the sequence is geometric instead. No claim of minimal order should be made.

## Hand-checkable examples

### Example 1: one face and a stationary fixed ray

Take

\[
E=\{(2,2)\},\qquad e=f=2,
\]

with arbitrary nonzero \(c_{22},\alpha,\beta\). Then

\[
A=\begin{pmatrix}1&2\\2&1\end{pmatrix},
\qquad
B=2I,
\qquad
C=\begin{pmatrix}2&4\\4&2\end{pmatrix}.
\]

The ordinary seed is the fixed ray \((1,1)\), \(c_0=3\), and

\[
C(1,1)^{\mathsf T}=6(1,1)^{\mathsf T}.
\]

Thus \(\lambda=6\), the selector is stationary from the start, and the scalar degree sequence is geometric. This example checks the one-face endpoint-Hessian argument and the exact seed bridge without any case split.

### Example 2: a three-support transient followed by wall alternation

Take

\[
E=\{(2,12),(3,10),(5,4)\},
\qquad
(e,f)=(27,8),
\qquad
\kappa=\frac{27}{8},
\]

again with arbitrary nonzero coefficients. The upper envelope has the three chambers

\[
(2,12)\quad(r<2),\qquad
(3,10)\quad(2<r<3),\qquad
(5,4)\quad(r>3).
\]

The wall \(r_*=3\) is fixed because its height is \(\Phi(3)=19\) and

\[
\frac{27}{8}\frac{19-3}{19-1}=3.
\]

Starting from the ordinary ratio \(r_0=1\), the first three images are

\[
r_1=\frac{27}{8}>3,
\]

\[
r_2=\frac{27}{8}\frac{5r_1+4-r_1}{5r_1+4-1}
=\frac{315}{106},
\qquad 2<r_2<3,
\]

and

\[
r_3=\frac{27}{8}\frac{3r_2+10-r_2}{3r_2+10-1}
=\frac{2535}{844}
=3+\frac{3}{844}>3.
\]

The selector word begins

\[
(2,12),\ (5,4),\ (3,10),\ (5,4),\ldots
\]

and thereafter alternates between the two faces adjacent to \(r=3\), while the ratios contract to \(3\).

For the primitive wall vector \(w=(3,1)\), both adjacent exponents give

\[
\mathcal A(w)=(16,18),
\]

so

\[
B\mathcal A(w)=(432,144)=144(3,1).
\]

Thus the wall multiplier and dynamical degree are the integer

\[
\mu=\lambda=144.
\]

Here \(c_0=\max_E(x+y)-1=13\); it is the seed-bridge constant and must not be confused with the wall multiplier \(144\). All displayed calculations are exact rational arithmetic.

## Assumptions, counterexamples, and STOP boundaries

| Boundary | What fails outside it | Counterexample or mandatory STOP |
|---|---|---|
| \(E\subset\mathbf Z_{\ge2}^2\) | Face derivatives can vanish, carry domination can fail, and the logarithmic gap (G) need not be positive. | For \(V=q_1^m\), \(\partial V/\partial q_2=0\) and \(\det\operatorname{Hess}V=0\). Axis support is not an extension of this theorem. |
| \(W\) is separated pure power and \(\alpha\beta\ne0\) | \(B\) ceases to be diagonal, so formula (P), global order reversal, and the \(BA/AB\) scalar conjugacy used here disappear. | For \(W=p_1^2p_2^2\), the momentum gradient has degree matrix \(\begin{psmallmatrix}1&2\\2&1\end{psmallmatrix}\), not a diagonal \(B\); the displayed fractional map need not be decreasing. Mixed \(W\) is STOP, not a corollary. |
| \({\rm char}(K)=0\) | Derivative and Hessian coefficients can vanish, destroying algebraic independence and exact noncancellation. | In characteristic \(p\), \(V=q_1^p q_2^2\) has \(\partial V/\partial q_1=0\). Positive characteristic is excluded. |
| Dimension exactly two | The positive projective cone is no longer an ordered line, so a decreasing interval contraction cannot classify selectors. The quadratic spectral cap is false dimension-free. | Papers 21, 23, and 25 locally exhibit cubic, quartic, and arbitrary algebraic Perron degrees in higher-dimensional stationary Hamiltonian support systems. Dimension \(\ge3\) is STOP for this theorem. |
| \(E\) finite and equal to the actual nonzero support | A finite piecewise-linear envelope and a uniform maximum of branch contraction constants are used. | A coefficient declared zero must be removed from \(E\); no “ghost” support point may be used in a chamber claim. |
| Ordinary seed and fixed phase \(F=T\circ S\) | The exact bridge constant and indexing depend on these choices. | Other seeds are allowed for the contraction theorem, but the displayed bridge and the special \(r_*=1\) geometric statement must be reindexed or restated. |

The exponents \(e,f\ge2\) and \(x,y\ge2\) are proof hypotheses, not claims of optimality. Paper 26 should not advertise them as necessary in every conceivable variant.

## Local collision matrix: Papers 20--25

| Local paper | Scientific claim or mechanism already occupied | Collision with the frozen candidate | Surviving Paper 26 delta |
|---|---|---|---|
| Paper 20 | A fixed two-mode stationary selector, a positive \(2\times2\) matrix, and a quadratic Perron formula. | Direct collision with “stationary matrix implies quadratic \(\lambda\).” | Do not claim that mechanism alone. Paper 26 classifies every finite positive two-dimensional support, includes walls, arbitrary nonzero coefficient signs, and inverse exactness. |
| Paper 21 | A fixed three-mode stationary selector with an exact cubic visible recurrence. | Direct collision with matrix visibility and Cayley--Hamilton recurrence as techniques. | Paper 26's new statement is a dimension-two universal upper/classification theorem, not another constructed algebraic degree. |
| Paper 22 | Arbitrary-mode endpoint spikes, a stationary selector cone, a common unit sector, and a cubic quotient/annihilator. | Collision with support-selected matrices and kernel/spectral factor reasoning. | No arbitrary Newton-envelope selector classification, wall theorem, or inverse-degree bridge appears there. |
| Paper 23 | A fixed four-mode stationary four-spike construction and irreducible quartic subfamilies. | Collision with exact positive matrix recurrences and higher Perron degree constructions. | Paper 26 moves in the opposite direction: it proves a sharp two-dimensional obstruction \([\mathbf Q(\lambda):\mathbf Q]\le2\) for an arbitrary finite positive support class. |
| Paper 24 | A two-mode crossed-binomial family with forced strict selector alternation, a wall-fixing calculation, exact two-step monodromy/parity laws, a bounded wall-fixing iff lemma, and a conditional period-\(k\) technical lemma. | This is the closest collision. One-branch fractional maps, decreasing behavior, a designed period-two selector word, and order-four parity recurrences are occupied. | Paper 24 does not prove arbitrary-support uniform log contraction, a unique global fixed ray, the interior/wall/tie trichotomy, exclusion of all \(k>2\), wall noncancellation with arbitrary face coefficients, inverse exactness, or the universal quadratic cap. |
| Paper 25 | A stationary support-row-rank factor bound and sharp positive all-\(d\) families with unbounded Perron degree and minimal scalar recurrence order. | Collision with the general selected-matrix viewpoint, exact ordinary visibility, and matrix-to-scalar recurrences. | Paper 25 explicitly excludes inverse growth, periodic selectors, arbitrary supports, and selector classification. Its higher-dimensional examples supply a STOP boundary rather than the present theorem. |

## Claim-by-claim subtraction from the two closest papers

### Subtraction from Paper 24

1. **Branch formula and monotonicity are not a standalone novelty claim.** Paper 24 already uses a special two-branch tropical/projective map to force alternation. Paper 26 may claim only the finite-envelope uniform inequality (L)--(G) and the global classification derived from it.

2. **A constructed period-two selector is occupied.** The new claim is that every strict wall-limit orbit for arbitrary finite positive support eventually alternates between the adjacent faces, while the numerical ratio converges and has no nontrivial cycle.

3. **Two-step monodromy and parity order four are occupied as mechanisms.** The new spectral statement is the common-wall-ray sharpening: both adjacent matrices have the same multiplier, forcing wall \(\lambda\in\mathbf Z\), and hence the universal degree cap two.

4. **Paper 24's bounded wall-fixing iff lemma remains credited.** Paper 26 replaces its bounded two-binomial parameter question by a global fixed-ray theorem for an arbitrary finite Newton envelope; it must not rebrand the earlier special wall calculation.

5. **Paper 24's conditional period-\(k\) lemma is not a classification theorem.** Paper 26's no-\(k>2\) result comes from the new uniform log contraction. The manuscript must distinguish these logical levels explicitly.

6. **Wall and inverse noncancellation are new obligations.** Paper 24's strict chambers avoid the arbitrary tied-face cancellation problem and it does not compare \(F\) with \(F^{-1}\). Paper 26 earns these claims only through the exposed-face Hessian lemma and the exact bridge (B).

### Subtraction from Paper 25

1. **Selected degree matrices and Perron--Frobenius are inherited infrastructure.** The stationary \(2\times2\) Perron description is not new by itself.

2. **Matrix recurrences visible in ordinary degree are occupied.** Paper 26 should claim the universal stationary/wall order bounds for this arbitrary-support class, not novelty for Cayley--Hamilton or visibility induction.

3. **Algebraic-degree statements must be dimension-qualified.** Paper 25 constructs degree \(d\) in \(d\) modes. Paper 26's value is precisely the sharp obstruction in the ordered two-dimensional projective setting; it must never sound dimension-free.

4. **Paper 25 is stationary and existential, not an arbitrary-support classification.** Its support-row-rank theorem does not imply the global selector contraction here, and its scope expressly excludes inverse growth and periodic selectors.

5. **Minimal recurrence order is not transferred.** Paper 25 proves minimality using cyclicity and observation. Paper 26 proves only eventual upper bounds, which can drop in symmetric or wall-fixed examples.

## Frozen local-literature collision audit

The closest dangerous collision in the material actually reviewed is internal Paper 24, not a public source: its crossed-binomial wall-fixing lemma and parity monodromy already occupy the most visually similar special case. The proof and title must therefore lead with arbitrary Newton support, global log contraction, face-Hessian exactness, and forward--inverse equality.

The public records already frozen in the local Papers 24--25 notes provide context but no checked collision with the full conjunction:

- Bellon--Viallet, Hasselblatt--Propp, and Dang--Favre provide degree-growth, tropical, or spectral context; they do not replace the exact face/carry proof here.
- Fordy--Hone and Ishibashi--Kano are neighboring sources for piecewise-linear or sign/selector dynamics; they should be cited as context rather than used to imply this contraction classification.
- Janeczko--Jelonek, Berger--Turaev (BT), and Koch--Lomelí (KL) provide symplectic/Hamiltonian shear context, not the claimed Newton-support degree theorem.
- Blanc--van Santen (BvS) and Shao--Sun (SS) are the nearest frozen affine-triangular dynamical-degree records; the map class and exact Hamiltonian support theorem remain distinct in the checked local summaries.
- Déserti (Des) and Abboud--Xie (AX) are broader degree-growth/algebraicity neighbors. Heyman--Shparlinski (HS) is arithmetic infrastructure used by Paper 25 and is not needed for Paper 26's proof.

This is a bounded local audit only. No network search was performed for R1, and absence of a collision in this corpus does not establish firstness, uniqueness, exhaustiveness, or global priority. The words “first,” “only,” “unprecedented,” and equivalent priority language are not authorized.

## Risk register and mandatory manuscript STOP conditions

| Risk | Required control | STOP condition |
|---|---|---|
| Arbitrary-sign wall cancellation | Put the extreme-term Hessian lemma before the degree recursions, then explicitly induct algebraic independence of leading forms. | STOP if the proof falls back to generic coefficients, positivity, or “different monomials cannot cancel.” |
| Inverse exactness | Prove the inverse half-step recursion separately and then prove bridge (B) by induction. | STOP if inverse equality is inferred only from \(\rho(AB)=\rho(BA)\). |
| Selector terminology | State that ratios converge to one fixed ray; only the chamber labels alternate at a wall. | STOP if the paper calls the limiting behavior a numerical two-cycle. |
| Wall algebraic degree | Use the common positive ray and common \(\mu\), then prove \(\mu\in\mathbf Z\). | STOP if the headline remains the nonsharp degree-at-most-four monodromy bound. |
| Scalar recurrence | Separate stationary order at most two from wall stride-two order at most two/full order at most four. | STOP if selector alternation is used to assert a ratio two-cycle, or if recurrence minimality is claimed. |
| Multiple ties | Use the full face polynomial on the wall and adjacent extreme faces on the two sides. | STOP if a multi-term tied face is silently replaced by one monomial. |
| Scope expansion | Keep separated \(W\), positive two-dimensional support, characteristic zero, and dimension two. | STOP if axis supports, mixed \(W\), characteristic \(p\), or dimension \(\ge3\) is stated as covered without a new proof. |
| Novelty wording | Frame scores and noncollision only within the frozen local corpus. | STOP if the manuscript makes a global priority claim without a later authorized literature search. |

## Scores and gate decision

The applicable local gate is novelty/portfolio differentiation at least \(7.5\), standalone value at least \(7.5\), and proof readiness at least \(9.0\).

| Axis | R1 score | Reason |
|---|---:|---|
| Novelty / local portfolio differentiation | **8.3 / 10** | The special period-two mechanism collides strongly with Paper 24, but arbitrary finite positive Newton support, uniform log contraction, exact wall/inverse noncancellation, and the global quadratic cap survive the subtraction as one new local theorem package. This score is not an external novelty score. |
| Standalone mathematical value | **8.7 / 10** | The theorem classifies the entire selector tail and first dynamical degree for a natural infinite two-mode family, explains exactly why walls do not create higher algebraic degree, and includes inverse growth in the same proof architecture. |
| Proof readiness | **9.3 / 10** | Every headline implication has a short exact mechanism: one Hessian coefficient, an algebraic-independence induction, strict carry inequalities, an exact bridge, a uniform logarithmic derivative gap, and Perron/common-ray arguments. No experiment, CAS certificate, or genericity escape is required. |

All three scores clear the gate. The recommended Paper 26 theorem should be developed from this candidate, subject to the STOP controls above and to a later separately authorized source review before any public novelty wording.

PAPER26_CANDIDATE_GATE_PASS_R1
