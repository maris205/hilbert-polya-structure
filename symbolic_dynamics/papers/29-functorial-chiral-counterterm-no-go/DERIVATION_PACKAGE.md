# Derivation package — Paper 29 / SD-C31

This file records the algebraic chain used by the manuscript.  No numerical prime label, target zero, or Route-B premise enters any step.

## 1. Incidence idempotents

For the zeta matrix (Z), Möbius inverse (M=Z^{-1}), and coordinate selector (E_x=e_xe_x^{\mathsf T}),

\[
q_x=ZE_xM=(Ze_x)(e_x^{\mathsf T}M).
\]

With

\[
u_x(a)=\mathbf1_{a\le x},
\qquad
v_x(b)=\mu(x,b)\mathbf1_{x\le b},
\]

this becomes
\(q_x=u_xv_x^{\mathsf T}\).  The identities
\(v_x^{\mathsf T}u_y=\delta_{xy}\) and
\(q_xq_y=\delta_{xy}q_x\) follow from
\(MZ=I\).

## 2. Weighted sharp and Gram contraction

For
\(W=\operatorname{diag}(w(a))\),

\[
q_y^\sharp=W^{-1}q_y^{\mathsf T}W
=W^{-1}v_yu_y^{\mathsf T}W.
\]

Therefore

\[
q_xq_y^\sharp
=u_x(v_x^{\mathsf T}W^{-1}v_y)u_y^{\mathsf T}W
\]

and

\[
G_{xy}=\operatorname{Tr}(q_xq_y^\sharp)
=\bigl(u_y^{\mathsf T}Wu_x\bigr)
 \bigl(v_x^{\mathsf T}W^{-1}v_y\bigr).
\]

This derivation is valid on every finite pointed poset.  Transported relabeling conjugates (q_x) and preserves the scalar contraction.

## 3. Divisibility diagonal

Let
\(w(n)=n^{2\eta}\).  For a cover atom (p), common lower elements of (p) with itself are (1,p), so

\[
u_p^{\mathsf T}Wu_p=1+p^{2\eta}.
\]

The upper factor is

\[
v_p^{\mathsf T}W^{-1}v_p
=\sum_{p\mid b}\frac{\mu(p,b)^2}{b^{2\eta}}
=p^{-2\eta}\sum_{k\ge1}\frac{\mu(k)^2}{k^{2\eta}}
=p^{-2\eta}C_\eta.
\]

Multiplication gives

\[
G_{pp}=C_\eta(1+p^{-2\eta}).
\]

## 4. Divisibility mixed coefficient

For distinct cover atoms (p,q), the common lower cone is only the bottom element, hence

\[
u_q^{\mathsf T}Wu_p=1.
\]

Common nonzero upper-tail terms have
\(b=pqk\), with (k) squarefree and coprime to (pq).  The two Möbius factors have product (+1).  Thus

\[
G_{pq}
=(pq)^{-2\eta}
\prod_{r\ne p,q}(1+r^{-2\eta})
=C_\eta
\frac{(pq)^{-2\eta}}
{(1+p^{-2\eta})(1+q^{-2\eta})}.
\]

In particular, every off-diagonal coefficient is positive.

## 5. Chiral square

For finite (F),

\[
\mathcal B_{s,F}^2=
\begin{pmatrix}
T_{s,F}T_{1-s,F}^\sharp&0\\
0&T_{1-s,F}^\sharp T_{s,F}
\end{pmatrix}.
\]

Finite cyclicity makes the two block traces equal.  Expanding
\(T_{s,F}\) yields

\[
Q_F(s)=2\sum_{p,q\in F}
p^{-s}q^{s-1}G_{pq}.
\]

At
\(s=1/2+it\), pair the
\((p,q)\) and
\((q,p)\) terms:

\[
p^{-s}q^{s-1}+q^{-s}p^{s-1}
=\frac{2}{\sqrt{pq}}
\cos\!\left(t\log\frac qp\right).
\]

This gives

\[
Q_F(t)=D_F+M_F(t),
\]

\[
D_F=2\sum_{p\in F}\frac{G_{pp}}p,
\quad
M_F(t)=4\sum_{p<q\in F}
\frac{G_{pq}}{\sqrt{pq}}
\cos\!\left(t\log\frac qp\right).
\]

## 6. Mixed summability and holomorphic strip

The bound

\[
0<G_{pq}\le C_\eta(pq)^{-2\eta}
\]

gives

\[
\sum_{p<q}\frac{4G_{pq}}{\sqrt{pq}}
\le2C_\eta\left(\sum_pp^{-(2\eta+1/2)}\right)^2.
\]

The displayed prime sum would converge for
\(\eta>1/4\), but (C_\eta) itself is finite only for
\(\eta>1/2\).  Thus the mixed argument is valid for every
\(\eta>1/2\); the source theorem keeps the stronger frozen hypothesis
\(\eta>1\).  For the cutoff tail, replace primes by all integers:

\[
\sum_{n>X}n^{-(2\eta+1/2)}
=O(X^{1/2-2\eta}).
\]

For complex (s), the two mixed monomials have prime exponents
\(2\eta+\Re s\) and
\(2\eta+1-\Re s\).  Both exceed one precisely inside

\[
1-2\eta<\Re s<2\eta.
\]

Normal convergence on compact subsets gives holomorphy, and swapping (p,q) gives reflection.

## 7. Diagonal germ

Substitute the diagonal Gram coefficient:

\[
D_X
=2C_\eta\sum_{p\le X}p^{-1}
+2C_\eta\sum_{p\le X}p^{-1-2\eta}.
\]

The first series diverges.  The second converges to the prime-zeta value
\(P(1+2\eta)\), with tail bounded by the corresponding integer integral.

Mertens' formula gives

\[
\sum_{p\le X}p^{-1}=\log\log X+\mathfrak B_1+o(1),
\]

so

\[
Q_{F_X}(t)-2C_\eta\log\log X
\to2C_\eta\bigl(\mathfrak B_1+P(1+2\eta)\bigr)+M_\eta(t).
\]

## 8. Full and leading atomwise schemes

Leading-only subtraction gives

\[
Q_F(t)-2C_\eta\sum_{p\in F}p^{-1}
\to2C_\eta P(1+2\eta)+M_\eta(t).
\]

Full-diagonal subtraction gives

\[
Q_F(t)-2\sum_{p\in F}\frac{G_{pp}}p
\to M_\eta(t).
\]

Their exact finite shift is

\[
2C_\eta P(1+2\eta)>0.
\]

At the experiment's
\(\eta=2\), this becomes
\(2C_\eta\sum_pp^{-5}\).

## 9. Sharp versus Abel convention

For the prime-zeta regulator,

\[
P(1+\varepsilon)
-\log(1/\varepsilon)
\to\mathfrak B_1-\gamma.
\]

Dominated convergence applies to the absolutely summable diagonal tail and mixed series.  The sharp constant uses
\(\mathfrak B_1\), while the Abel constant uses
\(\mathfrak B_1-\gamma\).  Thus

\[
\operatorname{FP}_{\rm Abel}
-\operatorname{FP}_{\rm sharp}=-2C_\eta\gamma.
\]

## 10. Quadratic kernel classification

Polarization turns every real bidegree-
\((1,1)\) quadratic form into
\(2a^*K_Fa\) with (K_F) Hermitian.  A pointed isomorphism
\(\phi\) transports coefficient vectors by (U_\phi); scalar invariance for every vector is equivalent to

\[
K_{\phi F}=U_\phi K_FU_\phi^*.
\]

If
\(F\subset F'\) inside one ambient realization, equality for all vectors supported on (F) is equivalent to the principal-block condition

\[
K_F=K_{F'}|_{F\times F}.
\]

For the critical coefficients, the residual diagonal is absolutely summable exactly when

\[
k_{pp}=C_\eta+r_p,
\qquad
\sum_p|r_p|/p<\infty.
\]

Because the native mixed kernel is already weighted-
\(\ell^1\), residual mixed convergence is equivalent to

\[
\sum_{p<q}|k_{pq}|/\sqrt{pq}<\infty.
\]

## 11. Local selectivity contradiction

A diagonal counterterm has no mixed Fourier coefficient, so every mixed difference in (t) is unchanged.  In the pair-local linear-Gram class, a local coefficient
\(\beta\) changes a native pair coefficient (G_{xy}) to
\((1-\beta)G_{xy}\).  Exact preservation forces
\(\beta=0\); exact cancellation forces
\(\beta=1\).  Transported naturality applies the same coefficient to identical local pair data.  No coefficient meets both gates.

## 12. Functional ownership

The ordinary quadratic trace is unavailable because the critical countable operator is not Hilbert--Schmidt.  The honest modified determinant satisfies

\[
\log\det{}_3(I-z\mathcal B_s)
=-\sum_{m\ge3}\frac{z^m}{m}\operatorname{Tr}(\mathcal B_s^m).
\]

Chiral parity kills odd powers, so order four is first visible.  Declaring a finite part defines the new functional

\[
\mathfrak D_{\mathcal R}(s,z)
=\det{}_3(I-z\mathcal B_s)
\exp[-z^2\operatorname{FP}_{\mathcal R}Q(s)/2].
\]

If the scheme changes by (h(s)), the functional is multiplied by
\(\exp[-z^2h(s)/2]\).  This factor is entire and zero-free in (z).  It preserves the auxiliary divisor but does not restore ordinary trace or
\(\det_2\) ownership.
