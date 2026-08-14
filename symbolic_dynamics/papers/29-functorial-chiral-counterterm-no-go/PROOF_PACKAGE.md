# Proof package — Paper 29 / SD-C31

## Status ledger

- Exact incidence/Gram formulas: **proved**.
- Mixed absolute summability, holomorphy, and cutoff tails: **proved**.
- Classification of reference-independent natural quadratic kernels: **proved in the frozen active-cutoff category**.
- Finite-scheme ambiguity: **proved**.
- Diagonal and additive pair-local linear-Gram selectivity no-gos: **proved in the stated classes**.
- Universal no-go for arbitrary nonlocal tower invariants: **open**.
- Arithmetic-spectral completion: **rejected**.

## Definitions

Let
\((P,\le,\bot)\) be a finite pointed poset.  Its zeta matrix is (Z), Möbius inverse is (M=Z^{-1}), and

\[
q_x=ZE_xM.
\]

With
\(W=\operatorname{diag}(w(a))>0\), define

\[
X^\sharp=W^{-1}X^*W,
\qquad
G_{xy}=\operatorname{Tr}(q_xq_y^\sharp).
\]

The active predicate is the source cover predicate
\(A(P)=\{x:\bot\prec x\}\).  The positive coefficient mark
\(\nu\) is transported data and never selects atoms.

For finite
\(F\subseteq A(P)\),

\[
T_{s,F}=\sum_{x\in F}\nu(x)^{-s}q_x,
\quad
\mathcal B_{s,F}=
\begin{pmatrix}0&T_{s,F}\\T_{1-s,F}^\sharp&0\end{pmatrix}.
\]

## Proposition 1 — bare-poset coefficient obstruction

The field
\(p\mapsto p^{-s}\) is not natural on the unmarked integer-divisibility poset.

**Proof.** Every permutation of the prime generators extends multiplicatively to a pointed automorphism of
\((\mathbb N_{\ge1},\mid,1)\).  All covers of (1) therefore form one automorphism orbit.  A scalar natural on the bare poset must be constant on that orbit, while
\(p^{-s}\) is not.  Unequal coefficients require the uniformly transported mark
\(\nu(n)=n\).  The atom set must still be obtained from the cover relation. ∎

## Theorem 2 — rank-one Gram contraction

Writing

\[
u_x(a)=\mathbf1_{a\le x},
\qquad
v_x(b)=\mu(x,b)\mathbf1_{x\le b},
\]

one has
\(q_x=u_xv_x^{\mathsf T}\) and

\[
G_{xy}
=\bigl(u_y^{\mathsf T}Wu_x\bigr)
 \bigl(v_x^{\mathsf T}W^{-1}v_y\bigr).
\]

**Proof.** The (x)-th column selector gives
\(ZE_x=(Ze_x)e_x^{\mathsf T}\), so
\(q_x=(Ze_x)(e_x^{\mathsf T}M)=u_xv_x^{\mathsf T}\).  Substitute the rank-one factors into
\(q_y^\sharp=W^{-1}v_yu_y^{\mathsf T}W\) and use
\(\operatorname{Tr}(ab^{\mathsf T})=b^{\mathsf T}a\). ∎

## Theorem 3 — exact divisibility Gram coefficients

Fix
\(\eta>1\),
\(w(n)=n^{2\eta}\), and

\[
C_\eta=\sum_{k\ge1}\frac{\mu(k)^2}{k^{2\eta}}
=\frac{\zeta(2\eta)}{\zeta(4\eta)}.
\]

For cover atoms (p,q),

\[
G_{pp}=C_\eta(1+p^{-2\eta}),
\]

and, if (p\ne q),

\[
G_{pq}=C_\eta
\frac{(pq)^{-2\eta}}
{(1+p^{-2\eta})(1+q^{-2\eta})}>0.
\]

**Proof.** For (p=q), the common lower-cone factor in Theorem 2 is
\(1+p^{2\eta}\).  The upper factor is
\(p^{-2\eta}C_\eta\).  For (p\ne q), the only common lower bound is (1).  A nonzero common upper-tail term is (b=pqk), with (k) squarefree and coprime to (pq); the two Möbius signs have product (+1).  Removing the Euler factors at (p,q) from (C_\eta) yields the displayed expression. ∎

## Theorem 4 — exact critical decomposition and summability

Finite-dimensional cyclicity gives

\[
Q_F(s):=\operatorname{Tr}\mathcal B_{s,F}^2
=2\sum_{p,q\in F}p^{-s}q^{s-1}G_{pq}.
\]

At
\(s=1/2+it\),

\[
Q_F(t)=2\sum_{p\in F}\frac{G_{pp}}p
+4\sum_{p<q\in F}\frac{G_{pq}}{\sqrt{pq}}
\cos\!\left(t\log\frac qp\right).
\]

The mixed series converges absolutely and uniformly for real (t), and its cutoff tail obeys

\[
\sup_t|M_\eta(t)-M_{F_X}(t)|
=O_\eta(X^{1/2-2\eta}).
\]

**Proof.** Since
\(G_{pq}\le C_\eta(pq)^{-2\eta}\), the absolute mixed mass is at most

\[
2C_\eta\left(\sum_p p^{-(2\eta+1/2)}\right)^2<\infty.
\]

The Weierstrass test gives uniform convergence.  Bounding the prime tail by the integer tail gives the stated rate. ∎

The holomorphic mixed series

\[
M_\eta(s)=2\sum_{p<q}G_{pq}
\left(p^{-s}q^{s-1}+q^{-s}p^{s-1}\right)
\]

is normally convergent on compact subsets of
\(1-2\eta<\Re s<2\eta\) and satisfies
\(M_\eta(1-s)=M_\eta(s)\).

## Theorem 5 — diagonal asymptotics

For
\(F_X=\{p:p\le X\}\),

\[
D_X=2C_\eta\sum_{p\le X}\frac1p
+2C_\eta\sum_{p\le X}p^{-1-2\eta}.
\]

Only the first summand diverges; the second has tail
\(O_\eta(X^{-2\eta})\).  Hence

\[
Q_{F_X}(t)=2C_\eta\log\log X
+2C_\eta\bigl(\mathfrak B_1+P(1+2\eta)\bigr)
+M_\eta(t)+o(1),
\]

uniformly in real (t).

## Theorem 6 — natural quadratic kernels

A real counterterm homogeneous of bidegree
\((1,1)\) in the active coefficient vector has the unique form

\[
C_{P,F}(a)=2a^*K_{P,F}a,
\]

with (K_{P,F}) Hermitian.  It is natural under transported pointed isomorphisms and compatible active cutoffs if and only if

\[
K_{P',\phi F}=U_\phi K_{P,F}U_\phi^*,
\qquad
K_{P,F}=K_{P,F'}|_{F\times F}
\quad(F\subset F').
\]

**Proof.** Polarization gives the unique Hermitian kernel.  Substitution of the transported coefficient vector makes scalar invariance equivalent to conjugation by the permutation matrix.  Equality on every old coefficient vector under an active inclusion, followed by polarization, is equivalent to equality of the old principal block. ∎

Thus naturality classifies counterterms as compatible equivariant pair kernels; it does not choose such a kernel.

## Theorem 7 — exhaustion-independent schemes

On the divisibility tower, write the reflection-symmetric kernel as (k_{pq}=k_{qp}\in\mathbb R).  The residual
\(Q_F-C_F\) converges absolutely and independently of the order of finite exhaustion if and only if

\[
k_{pp}=C_\eta+r_p,
\qquad
\sum_p\frac{|r_p|}{p}<\infty,
\]

and

\[
\sum_{p<q}\frac{|k_{pq}|}{\sqrt{pq}}<\infty,
\]

in addition to Theorem 6's equivariance.

**Proof.** Absolute convergence of the residual diagonal is

\[
\sum_p\frac{|G_{pp}-k_{pp}|}{p}<\infty.
\]

Since
\(G_{pp}-C_\eta=C_\eta p^{-2\eta}\) is already summable with weight (p^{-1}), this is equivalent to the first condition.  The native mixed kernel is in the required weighted
\(\ell^1\) space by Theorem 4, so absolute convergence of the residual is equivalent to the second condition. ∎

## Corollary 8 — explicit finite-scheme ambiguity

The leading-only scheme

\[
C_F^{\rm lead}=2C_\eta\sum_{p\in F}\frac1p
\]

has finite part

\[
R_\eta^{\rm lead}(t)
=2C_\eta P(1+2\eta)+M_\eta(t).
\]

The full-diagonal scheme

\[
C_F^{\rm full}=2\sum_{p\in F}\frac{G_{pp}}p
\]

has finite part
\(R_\eta^{\rm full}(t)=M_\eta(t)\).  Their difference is

\[
R_\eta^{\rm lead}-R_\eta^{\rm full}
=2C_\eta P(1+2\eta)>0.
\]

Both are equivariant and active-cutoff compatible.  Therefore naturality plus convergence does not select a finite part. ∎

For the sharp
\(\log\log X\) convention and compatible Abel convention,

\[
\operatorname{FP}_{\rm Abel}
-\operatorname{FP}_{\rm sharp}=-2C_\eta\gamma.
\]

## Theorem 9 — diagonal selectivity no-go

For every diagonal quadratic counterterm,

\[
(Q_F-C_F^{\rm diag})(t_1)
-(Q_F-C_F^{\rm diag})(t_2)
=M_F(t_1)-M_F(t_2).
\]

**Proof.** A diagonal term contains no unordered-pair phase.  It cancels from the difference. ∎

Thus any control with a nonconstant mixed ledger survives every diagonal subtraction.

## Theorem 10 — pair-local linear-Gram no-go

Assume a counterterm is quadratic, additive over atoms and unordered pairs, local to the pointed induced one-/two-atom datum, linear in the native pair Gram contraction, invariant under transported relabeling, and forbidden to branch on printed numeric names.  No such rule can preserve the divisibility mixed mechanism while cancelling every matched mutated/composite/generic control mechanism.

**Proof.** On a nonzero local pair, write the counterterm coefficient as
\(\beta G_{xy}\).  The residual multiplier is (1-\beta).  Preserving the native baseline pair exactly forces
\(\beta=0\).  Cancelling a matched nonzero control pair forces
\(\beta=1\).  Naturality makes the coefficient the same on transported identical local data.  The requirements are inconsistent. ∎

The exact suite independently enumerates 49 preregistered coefficient pairs and finds no selective solution.

## Proposition 11 — ownership and divisor invariance

On the honest Schatten strip, define for a declared reflection-symmetric scheme
\(\mathcal R\)

\[
\mathfrak D_{\mathcal R}(s,z)
=\det{}_3(I-z\mathcal B_s)
\exp\!\left[-\frac{z^2}{2}
\operatorname{FP}_{\mathcal R}\operatorname{Tr}(\mathcal B_s^2)
\right].
\]

This is a new scheme-dependent functional.  If two schemes differ by a holomorphic (h(s)), then

\[
\frac{\mathfrak D_{\mathcal R_2}(s,z)}
{\mathfrak D_{\mathcal R_1}(s,z)}
=\exp[-z^2h(s)/2].
\]

The right-hand side is entire and zero-free in (z), so the two functionals have the same auxiliary-
\(z\) divisor.  Reflection holds exactly when the finite part is reflection symmetric.  None of this creates an ordinary trace or
\(\det_2\). ∎

## Main theorem

Fix the marked integer-divisibility incidence realization with
\(\eta>1\), ambient compilation followed by finite active cutoffs, and reference-independent natural quadratic kernels.  Then the divergent germ, mixed summability, weighted-
\(\ell^1\) classification, and finite-scheme ambiguity above hold.  No diagonal scheme is arithmetic-selective.  Under the additional additive pair-local linear-Gram hypotheses, no counterterm preserves the arithmetic mixed mechanism while cancelling all exact controls.

The theorem makes no claim about arbitrary nonlinear or nonlocal invariants of the entire filtered tower.
