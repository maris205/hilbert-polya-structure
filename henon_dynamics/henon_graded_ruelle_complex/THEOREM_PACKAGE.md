# Conditional operator blueprint and exact closed gates

## 1. Audited status

This document separates the exact part of HCS-C22G from the functional-
analytic theorem that remains to be proved.

The following statements are established:

1. the lifted Hénon branches and their three-complex-dimensional cross maps
   are explicit and use the correct BPS mixed-data convention;
2. the stated common disk inclusions, pole exclusions, Jacobian bounds, and
   one-step injectivity statements follow from exact rational estimates;
3. with a fixed product-contour orientation, the block-Jacobian identity
   behind the raw residue sign is an exact algebraic identity;
4. the exterior-algebra cancellation and the resulting parity shift are
   exact finite-dimensional identities.

The following statements are **open gates**, not results of this package:

1. an all-word composition theorem for the three-variable vector kernels,
   including the exact iterated half-inverse numerator and chronological
   matrix cocycle;
2. equality of the nuclear trace with the diagonal contour integral and its
   Grothendieck residue for every closed word;
3. explicit enlarged holomorphy domains, especially in the output expanding
   variable, supporting an order-zero nuclear factorization;
4. a complete metric-approximation-property argument for the particular
   mixed exterior/interior Banach spaces;
5. locally uniform holomorphy in a fixed nuclear ideal strong enough for a
   canonical Fredholm determinant.

Consequently, the Fredholm factors and the joint meromorphic continuation
below are conditional consequences.  They are not presently proved theorems.

## 2. Exact lifted dynamics and cross-map convention

Let

\[
\widehat F_a(x,y,m)
=
\left(
y,\ 1-ay^2-x,\
\frac{\gamma}{-2ay-\beta m}
\right),
\qquad
\gamma=\frac{112}{123},\quad
\beta=\frac{123}{112},
\]

where \(a\in\{59/10,61/10\}\).  Write

\[
X_\sigma=\overline D\!\left(\sigma\frac{23}{48},\frac7{48}\right),
\quad
Y_\sigma=\overline D\!\left(\sigma\frac{121}{256},\frac{41}{256}\right),
\quad
M=\overline D(0,1/2).
\]

The four Markov states are \(i=(\sigma,t)\in\{-,+\}^2\), with edge

\[
(\sigma,t)\longrightarrow(r,\sigma)
\quad\Longleftrightarrow\quad
(t,r)\ne(+,+).
\]

There are six state edges and two parameter letters on each edge.

The contracting input block is

\[
c=(x,m)\in Y_t\times M,
\]

and the expanding input coordinate is \(y\in X_\sigma\).  Fix the
contracting input \(c\) and the expanding **output** \(z\in X_r\).  Define

\[
h_{a,\sigma}(c,z)
=P_{a,\sigma}(x,z)
=\sigma\sqrt{\frac{1-x-z}{a}}
\]

and

\[
K_{a,\sigma}(c,z)
=\left(
P_{a,\sigma}(x,z),
G_{a,P_{a,\sigma}(x,z)}(m)
\right),
\qquad
G_{a,y}(m)=\frac{\gamma}{-2ay-\beta m}.
\]

Direct substitution gives

\[
\widehat F_a(c,h(c,z))=(K(c,z),z).
\]

This is the BPS convention: input contracting data and output expanding data
are fixed, and the input expanding coordinate is solved.  Prescribing an
arbitrary projective output and inverting \(G\) is a different boundary-value
problem; its pole at output slope zero is irrelevant here.

## 3. Exact one-step domain and Jacobian data

The inherited disk proof gives

\[
P_{a,\sigma}(Y_t\times X_r)\Subset X_\sigma
\]

for both parameter letters and all six allowed state edges.  The minimum
coordinate clearance is \(7/5490\).  The normalized image ratios are

\[
\rho_1=\frac{39}{41},\qquad
\rho_2=\frac{250880}{466211},\qquad
\rho_3=\frac{907}{915}.
\]

They control, respectively, the first contracting output in \(Y_\sigma\),
the projective output in \(M\), and the expanding half-inverse in
\(X_\sigma\).  These strict ratios are compactness data.  By themselves they
are not yet a proof of a nuclear factorization.

The projective denominator obeys

\[
\frac{11371}{3360}
\le |-2ay-\beta m|
\le \frac{1831}{224}.
\]

Consequently,

\[
|\det D\widehat F_a|
=\frac1{|-2ay-\beta m|^2}
\ge\frac{50176}{3352561}>0.
\]

For fixed \(z\),

\[
\partial_xP=\partial_zP=-\frac1{2aP},
\]

and

\[
\det D_{(x,m)}K
=-\frac1{2aP(-2aP-\beta m)^2},
\qquad
|\det D_{(x,m)}K|
\ge\frac{401408}{204506221}>0.
\]

For fixed \(c\), the selected square-root branch makes
\(z\mapsto h(c,z)\) injective.  For fixed \(z\), the first component of
\(K\) recovers \(x\), and the Möbius second component recovers \(m\).
Thus the one-step pinning coordinates are holomorphic and injective on the
certified domains.

To pass from this one-step statement to arbitrary words, a block version of
the Rugh/BPS iterated-pinning lemma must still be written down: the
intermediate mixed variables must be solved in the correct order, and the
resulting maps must be shown to retain strict enlarged domains.  Ordinary
composition of the one-step cross maps is not a substitute for this lemma.

## 4. Candidate Banach spaces and frozen fibre basis

For \(i=(\sigma,t)\), the candidate scalar space is

\[
\mathcal A_i
=A_0\!\left(
(\widehat{\mathbb C}\setminus Y_t)
\times(\widehat{\mathbb C}\setminus M)
\times X_\sigma
\right),
\]

with the supremum norm, holomorphy in the interior, and continuous boundary
values.  The subscript zero means vanishing when either exterior coordinate
is infinity.  The degree-\(k\) candidate space is

\[
\mathcal B_{i,k}=\mathcal A_i\otimes\bigwedge^k\mathbb C^3_{\rm phys}.
\]

The scalar function arguments are ordered as

\[
(x,m,u),
\]

but the fibre is **always** expressed in the physical tangent basis

\[
(e_x,e_y,e_m).
\]

Thus \(D\widehat F_a\) below is the derivative from
\((x,y,m)\) to \((x',y',m')\) in that physical basis, even though the
scalar target arguments are ordered

\[
(\zeta_1,\zeta_2,z)=(x',m',y').
\]

If cross-ordered fibre coordinates \((e_x,e_m,e_y)\) are used instead, the
matrix must be replaced by

\[
S\,D\widehat F_a\,S^{-1},
\qquad
S=
\begin{pmatrix}
1&0&0\\
0&0&1\\
0&1&0
\end{pmatrix}.
\]

No mixture of these two conventions is allowed.

## 5. Candidate vector branch kernel

For an edge \(i=(\sigma,t)\to j=(r,\sigma)\), set

\[
j_{a,\sigma}(u,m)=-\sigma(-2au-\beta m),
\qquad
g_{a,\sigma,s}(u,m)
=\exp\!\bigl(-s\operatorname{Log}j_{a,\sigma}(u,m)\bigr),
\]

and define the physical-basis cocycle

\[
W_{a,\sigma,s,k}(x,m,u)
=g_{a,\sigma,s}(u,m)\,
\wedge^kD\widehat F_a(x,u,m).
\]

The candidate branch operator is

\[
\begin{aligned}
(\mathcal K^{a,i\to j}_{s,k}\psi)(\zeta_1,\zeta_2,z)
=
\int_{\partial Y_t\times\partial M\times\partial X_\sigma}
&\frac{\partial_zP_{a,\sigma}(x,z)}
{(\zeta_1-P_{a,\sigma}(x,z))
(\zeta_2-G_{a,P_{a,\sigma}(x,z)}(m))}
\\[-1mm]
&\times
\frac{
W_{a,\sigma,s,k}(x,m,u)\psi(x,m,u)
}{u-P_{a,\sigma}(x,z)}
\frac{dx}{2\pi i}\frac{dm}{2\pi i}\frac{du}{2\pi i}.
\end{aligned}
\]

The product contour is ordered as \((x,m,u)\), with product orientation

\[
dx\wedge dm\wedge du.
\]

This order is part of the definition and is required for the residue sign
below.  Writing \(du\wedge dm\wedge dx\) would reverse that sign.

Because the weight and matrix are holomorphic in \(u\), the one-step Cauchy
residue shows that this formula is equivalent to pulling them outside the
\(u\)-integral and evaluating them at
\(u=P_{a,\sigma}(x,z)\).  Keeping them at the integration variable makes the
source-point convention explicit and is preferred for the word-composition
proof.

The graph blocks are the sums

\[
(\mathcal L_{s,k})_{j,i}
=\sum_{a\in\{59/10,61/10\}}
\mathcal K^{a,i\to j}_{s,k}
\]

on allowed edges, and zero otherwise.  This is a chronological sum, never
an average.

The exact disk clearances make the one-step contour integral well-defined
and bounded on the displayed original domains.  They do not yet establish
the order-zero nuclear claim.

## 6. Exact raw-residue algebra

Let an iterated pinning pair, once constructed, have derivatives

\[
A=\partial_cK,\qquad B=\partial_zK,
\qquad C=\partial_ch,\qquad D=\partial_zh.
\]

Differentiating

\[
F(c,h(c,z))=(K(c,z),z)
\]

gives

\[
DF
=
\begin{pmatrix}A&B\\0&I\end{pmatrix}
\begin{pmatrix}I&0\\C&D\end{pmatrix}^{-1}.
\]

At a diagonal trace, order the residual and variables as

\[
R(x,m,u)
=\bigl(x-K_1(c,u),\ m-K_2(c,u),\ u-h(c,u)\bigr)
\]

and \((x,m,u)\).  Then

\[
DR=
\begin{pmatrix}I-A&-B\\-C&I-D\end{pmatrix},
\qquad
\boxed{\det DR=-D\det(I-DF)}.
\]

With the frozen product orientation \(dx\wedge dm\wedge du\), a simple
Grothendieck residue with numerator \(D\) is therefore

\[
-\frac1{\det(I-DF)}.
\]

This is an exact algebraic identity.  It does not by itself prove that the
nuclear trace of every word operator is represented by this residue.

For every \(3\times3\) matrix \(M\),

\[
\sum_{k=0}^3(-1)^k\operatorname{tr}(\wedge^kM)
=\det(I-M).
\]

Hence, if the desired word trace formula is established, the single
expanding coordinate forces total parity \(k+1\), not \(k\).

## 7. Open all-word composition and trace gate

The following lemma is required before any all-period trace statement may be
promoted.

> **Required word-kernel lemma.**  For every admissible joint word, the
> product of the one-step kernels equals a single iterated cross kernel.  Its
> scalar numerator is \(\partial_z h_w\); its fibre numerator is the ordered
> product
> \[
> g_s^{(n)}(x_0)\,
> \wedge^kD
> (\widehat F_{a_{n-1}}\circ\cdots\circ\widehat F_{a_0})(x_0),
> \]
> with later matrices acting on the left.  All intermediate contour
> deformations and Cauchy residues are legitimate and add no extra sign.

After that lemma, one must still prove:

1. the word operator is nuclear in a fixed ideal and its canonical nuclear
   trace equals its diagonal contour integral;
2. the iterated cross residual has only the declared simple zero in the
   branch domain;
3. closed graph paths and fixed points have the required one-to-one coding,
   including repetitions and periods one and two;
4. the contour order used in the trace agrees with the order in the block
   determinant identity.

The existing symbolic program checks the finite-dimensional block identity
and sample matrix chronology.  It does not prove this lemma or these four
analytic statements.

## 8. Open order-zero nuclear and approximation-property gate

The inequalities \(\rho_i<1\) suggest the classical Ruelle--Rugh
factorization, but the following data are still required:

1. explicit intermediate spaces \(\mathcal B'_{j,k}\), with the direction of
   each restriction map stated;
2. an enlarged output expanding disk on which
   \(P_{a,\sigma}(x,z)\) remains in a compact subset of \(X_\sigma\);
3. preservation on all enlarged domains of the square-root branch,
   projective pole exclusion, and the common logarithm sector;
4. a bounded factor
   \(T_{a,i\to j,s,k}:\mathcal B_{i,k}\to\mathcal B'_{j,k}\);
5. a restriction
   \(R_j:\mathcal B'_{j,k}\to\mathcal B_{j,k}\) with an explicit rank-one
   expansion and locally uniform \(p\)-nuclear bounds, for a fixed
   \(p\le2/3\) (or, preferably, for every \(p>0\));
6. a proof that the reciprocal-coordinate ideal corresponding to vanishing
   on either infinity hyperplane has the metric approximation property.

The last item cannot be replaced by the general assertion that closed ideals
inherit the approximation property.  For these particular disk spaces one
may instead identify the ideal explicitly with

\[
w_1w_2A(\overline{\mathbb D}^{,3})
\]

and prove the metric approximation property using tensor Fejér projections.

The previously listed \(\rho_i\) are image ratios.  In particular,
\(\rho_3\) controls the image of the half-inverse; it is not automatically a
restriction ratio for an enlarged output-\(z\) disk.  That enlarged disk or
an alternative full monomial decomposition must be supplied explicitly.

Only after these points are proved may one conclude that the branch and
graph operators are nuclear of order zero.  To obtain parameter holomorphy,
the factorization must also be locally uniform on compact \(s\)-sets in one
fixed \(p\)-nuclear quasi-norm.  Boundedness of \(\operatorname{Log}j\) on
the original domains is necessary but not, without the enlarged-domain
factorization, sufficient.

## 9. Conditional analytic consequence

Assume the iterated-pinning, word-kernel, nuclear-trace, enlarged-domain,
order-zero, approximation-property, and locally uniform \(s\)-holomorphy
gates above are all proved.  Then one obtains

\[
\operatorname{tr}\mathcal L_{s,k}^n
=-
\sum_{x\in\operatorname{Fix}\widetilde{\mathcal F}^n}
\frac{
g_s^{(n)}(x)\,
\operatorname{tr}(\wedge^kD\widetilde{\mathcal F}^n_x)
}{
\det(I-D\widetilde{\mathcal F}^n_x)
},
\]

and therefore

\[
\sum_{k=0}^3(-1)^{k+1}
\operatorname{tr}\mathcal L_{s,k}^n=B_n(s).
\]

For

\[
D_k(z,s)=\operatorname{Det}(I-z\mathcal L_{s,k}),
\]

the same hypotheses would make each \(D_k\) jointly entire on
\(\mathbb C^2\) and would give, initially in the normal-convergence domain,

\[
D_{\rm inst}(z,s)
=\prod_{k=0}^3D_k(z,s)^{(-1)^{k+1}}
=\frac{D_1(z,s)D_3(z,s)}{D_0(z,s)D_2(z,s)}.
\]

The quotient would then define an element of the several-complex-variable
meromorphic sheaf \(\mathcal M(\mathbb C^2)\).  At common numerator and
denominator zeros it is understood as a meromorphic germ, not as an
everywhere pointwise quotient.  Its polar divisor would be contained in the
zero divisor of \(D_0D_2\), with cancellations possible.

None of these determinant-continuation conclusions is currently asserted
unconditionally.

## 10. Research status

The package now has the status **conditional analytic blueprint / closure
note**.  It records a corrected, reproducible candidate with exact Hénon
domains, constants, cross-map convention, fibre convention, and residue
algebra.  It does not certify a completed nuclear Ruelle complex or a joint
meromorphic continuation.

Even if the open gates are later closed, the mechanism remains classical
Ruelle--Rugh/Grothendieck--Lefschetz infrastructure.  No arithmetic primitive
law, Riemann divisor, functional equation, or self-adjoint Hilbert--Pólya
operator is obtained here.
