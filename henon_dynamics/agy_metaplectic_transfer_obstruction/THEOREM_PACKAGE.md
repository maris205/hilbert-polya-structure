# HCS-C25 theorem package: AGY return maps force metaplectic noncompactness

## Material Passport

- **Origin Skill:** `ars-codex:academic-research-suite / experiment-agent`
- **Origin Mode:** `theory / source-lock / validate`
- **Origin Date:** `2026-08-10T00:00:00Z`
- **Verification Status:** `VERIFIED` -- the operator proofs received an
  independent theorem audit, and the explicit project-chosen
  AGY-admissible four-letter section witness,
  chronology, full-rank symplectic action, and decoder received a separate
  implementation replay.
- **Version Label:** `theorem_package_v2`

## Status and exact claim

This package closes two concrete operator realizations of the C24 proposal:

1. the raw AGY transfer operator on a vector-valued bounded-
   \(C^1\) space;
2. the invariant-measure-normalized transfer operator on
   \(L^2(\mu;L^2(\mathbb R^2))\).

On the raw AGY space, the unsmoothed metaplectic operator is noncompact
throughout the source half-plane \(\operatorname{Re}s>-\sigma _0\).  On the
normalized \(L^2\) realization it is bounded and noncompact for
\(\operatorname{Re}s\geq0\); on the imaginary axis it is, more precisely, a
coisometry with essential norm one.  In the smaller half-plane

\[
\operatorname{Re}s\geq d/2,
\]

where \(d\) is the number of interval-exchange labels, the literal branch
operators are also absolutely summable in operator norm, and the C24
discrete-metaplectic-atom theorem applies.  For the four-letter system this
threshold is \(\operatorname{Re}s\geq2\).

These are operator-space-specific negative results.  They do not decide a
holomorphic or anisotropic realization that is not boundedly equivalent to
one of the spaces treated here.

## A. Source-locked AGY hypotheses

The primary source is A. Avila, S. Gouëzel, and J.-C. Yoccoz,
*Exponential mixing for the Teichmüller flow*,
[arXiv:math/0511614](https://arxiv.org/abs/math/0511614), especially its
definition of a uniformly expanding Markov map and the construction from a
neat strongly positive Rauzy path.

The theorem below uses exactly the following consequences of that
construction.  They are listed as hypotheses so that no property of a
different acceleration is imported silently.

Let \(\Delta\) be the bounded John domain of the AGY induced map, with finite
induced Lebesgue reference measure \(m\).  In particular \(m\) is nonatomic.
There is a countable collection of pairwise disjoint open sets
\((D_\gamma)_{\gamma\in\Gamma}\) covering a full-measure subset of
\(\Delta\), and

\[
T:D_\gamma\longrightarrow\Delta
\]

is a \(C^1\) diffeomorphism for every \(\gamma\).  Write
\(h_\gamma:\Delta\to D_\gamma\) for its inverse branch and

\[
j_\gamma(x)=\operatorname{Jac}_m h_\gamma(x)>0.
\]

The source gives uniform constants \(0<\kappa<1\), \(C_J,C_r<\infty\)
such that

\[
\|Dh_\gamma\|_\infty\leq\kappa,
\qquad
\|D\log j_\gamma\|_\infty\leq C_J,
\qquad
\|Dr_\gamma\|_\infty\leq C_r,
\tag{A.1}
\]

where

\[
r_\gamma=r\circ h_\gamma>0.
\]

For an interval exchange on \(d\) labels, the two direct AGY formulas are

\[
j_\gamma(x)=\|B_\gamma^*x\|^{-d},
\qquad
r_\gamma(x)=\log\|B_\gamma^*x\|,
\]

and hence the convention-locked identity is

\[
\boxed{j_\gamma=e^{-d r_\gamma}.}
\tag{A.2}
\]

The paths \(\gamma\) begin and end at the selected Rauzy state.  To define
their lifts without identifying the changing crossing forms silently, write
\(J_\pi=\Omega_\pi^{-1}\), use the base-state form
\(J_0=J_{\pi_*}\) as a fixed reference, and choose integral frames
\(S_\pi\) with \(S_\pi^TJ_\pi S_\pi=J_0\).  Such frames exist here
because every \(J_\pi\) is an integral unimodular alternating form.  For an
edge \(e:\pi_{\rm src}\to\pi_{\rm dst}\), set

\[
g_e=S_{\pi_{\rm dst}}^{-1}B_eS_{\pi_{\rm src}}.
\]

The transport identity gives \(g_e^TJ_0g_e=J_0\), and along a path the
frames telescope:

\[
g_\gamma=g_{e_n}\cdots g_{e_1}
=S_{\pi_{\rm end}}^{-1}B_\gamma S_{\pi_{\rm start}}.
\]

In the four-letter \(\mathcal H(2)\) case, the crossing form has full rank
and \(g=2\).  Thus \(g_e\in\operatorname{Sp}(J_0,\mathbb Z)\).  After one
fixed real identification of \((\mathbb R^4,J_0)\) with standard phase
space, fix one lift of each \(g_e\), compose the lifts in
later-on-the-left chronology to obtain \(\widetilde g_\gamma\), and set

\[
U_\gamma=\mu_{\rm osc}(\widetilde g_\gamma)
\quad\hbox{on}\quad
\mathscr F=L^2(\mathbb R^2).
\tag{A.3}
\]

Every \(U_\gamma\) is unitary and the central metaplectic sign is retained.

Finally, \(T\) has a unique absolutely continuous invariant probability
measure

\[
d\mu=\rho\,dm,
\qquad
0<c_\rho\leq\rho\leq C_\rho<\infty,
\qquad
\rho\in C^1_b(\Delta).
\tag{A.4}
\]

Thus \(\mu\) is nonatomic as well.

The AGY exponential-tail theorem supplies the full raw half-plane
\(\operatorname{Re}s>-\sigma _0\).  On \(\operatorname{Re}s\ge0\), the
operator bounds and all Hilbert-space conclusions use only (A.1)--(A.4),
finite diameter in the AGY Finsler metric, and the full-branch partition.

## B. Raw \(C^1_{\mathscr F}\) transfer operator

Let

\[
\mathcal B_{\mathscr F}=C^1_b(\Delta;\mathscr F),
\qquad
\|F\|_{\mathcal B}=\sup_x\|F(x)\|_{\mathscr F}
 +\sup_x\|DF(x)\|.
\]

For \(s\in\mathbb C\), put

\[
w_{s,\gamma}(x)=e^{-s r_\gamma(x)}j_\gamma(x)
\]

and define the raw branch and transfer operators by

\[
(A^{\rm raw}_{s,\gamma}F)(x)
=w_{s,\gamma}(x)U_\gamma F(h_\gamma x),
\qquad
\mathcal L^{\rm raw}_s=\sum_{\gamma\in\Gamma}
A^{\rm raw}_{s,\gamma}.
\tag{B.1}
\]

### Theorem B.1 -- absolute branch boundedness

For every fixed \(s\) with \(\operatorname{Re}s>-\sigma _0\), the series in
(B.1) converges absolutely in
\(\mathcal B(\mathcal B_{\mathscr F})\).  More precisely,

\[
\sum_\gamma\|A^{\rm raw}_{s,\gamma}\|
\leq C_s\sum_\gamma
 \|e^{-\operatorname{Re}(s)r_\gamma}j_\gamma\|_\infty<\infty.
\tag{B.2}
\]

#### Proof

Let \(D_0=C_J\operatorname{diam}(\Delta)\).  Bounded distortion and change
of variables give

\[
\sup_\Delta j_\gamma
\leq e^{D_0}\frac{1}{m(\Delta)}
       \int_\Delta j_\gamma\,dm
=e^{D_0}\frac{m(D_\gamma)}{m(\Delta)}.
\]

Because the \(D_\gamma\) form a partition modulo null sets,

\[
\sum_\gamma\|j_\gamma\|_\infty\leq e^{D_0}<\infty.
\tag{B.3}
\]

For \(a=\operatorname{Re}s>-\sigma _0\), put
\(v_{a,\gamma}=e^{-a r_\gamma}j_\gamma\).  Its logarithmic derivative is
bounded by \(C_J+|a|C_r\), uniformly in \(\gamma\).  The same
bounded-distortion and change-of-variables argument therefore gives

\[
 \sum_\gamma\|v_{a,\gamma}\|_\infty
 \le C_a\int_\Delta e^{-a r(y)}\,dm(y)<\infty,
\]

where the final integral is finite by the AGY exponential-tail theorem.
Moreover,

\[
Dw_{s,\gamma}
=w_{s,\gamma}\bigl(D\log j_\gamma-sDr_\gamma\bigr).
\]

Together with (A.1) and the product rule for
\(w_{s,\gamma}U_\gamma F\circ h_\gamma\), this yields

\[
\|A^{\rm raw}_{s,\gamma}\|_{\mathcal B\to\mathcal B}
\leq C(1+|s|)\|v_{a,\gamma}\|_\infty.
\]

Summing proves the claim.  Formula (B.3) is the simpler special case
\(a\geq0\).  \(\square\)

### Theorem B.2 -- bump/evaluation branch compression

For every \(s\) with \(\operatorname{Re}s>-\sigma _0\),
\(\mathcal L^{\rm raw}_s\) is noncompact on
\(\mathcal B_{\mathscr F}\).

#### Proof

Fix one branch \(\gamma_0\) and a point \(x_0\in\Delta\).  Since
\(y_0=h_{\gamma_0}(x_0)\) lies in the open set \(D_{\gamma_0}\), choose
\(\psi\in C^1_c(D_{\gamma_0})\) with \(\psi(y_0)=1\).  Define bounded maps

\[
J_\psi:\mathscr F\to\mathcal B_{\mathscr F},
\quad (J_\psi v)(y)=\psi(y)v,
\qquad
R_{x_0}:\mathcal B_{\mathscr F}\to\mathscr F,
\quad R_{x_0}F=F(x_0).
\]

For \(\gamma\neq\gamma_0\), \(h_\gamma(x_0)\in D_\gamma\) is outside the
support of \(\psi\).  Consequently

\[
R_{x_0}\mathcal L^{\rm raw}_sJ_\psi
=w_{s,\gamma_0}(x_0)U_{\gamma_0}.
\tag{B.4}
\]

The scalar in (B.4) is nonzero.  Since \(\mathscr F\) is infinite
dimensional, (B.4) is a nonzero infinite-dimensional unitary compression.
The C24 modulo-compact branch theorem therefore gives

\[
\|\mathcal L^{\rm raw}_s\|_{\rm ess}
\geq
\frac{|w_{s,\gamma_0}(x_0)|}
     {\|R_{x_0}\|\,\|J_\psi\|}>0.
\]

Thus the full operator is noncompact.  Notice that no cancellation claim is
being inferred from its formal summands: (B.4) is an exact bounded
compression of the already norm-convergent operator.  \(\square\)

## C. Invariant-measure-normalized \(L^2\) operator

Define the conditional inverse-branch probabilities

\[
p_\gamma(x)
=j_\gamma(x)\frac{\rho(h_\gamma x)}{\rho(x)}.
\tag{C.1}
\]

The invariance equation for \(\rho\) gives

\[
p_\gamma\geq0,
\qquad
\sum_\gamma p_\gamma(x)=1
\quad\hbox{for almost every }x.
\tag{C.2}
\]

Let

\[
\mathcal H=L^2(\Delta,\mu;\mathscr F)
\]

and set

\[
(\mathcal P_sF)(x)
=\sum_\gamma p_\gamma(x)e^{-sr_\gamma(x)}
 U_\gamma F(h_\gamma x).
\tag{C.3}
\]

For \(a=\operatorname{Re}s\geq0\), this countable Bochner sum is absolutely
convergent almost everywhere and unconditionally convergent in
\(\mathcal H\).  Indeed,

\[
\sum_\gamma p_\gamma e^{-ar_\gamma}\|F(h_\gamma x)\|
\leq
\left(\sum_\gamma p_\gamma\right)^{1/2}
\left(\sum_\gamma p_\gamma\|F(h_\gamma x)\|^2\right)^{1/2}.
\]

The square of the second factor integrates, by branch disintegration, to
\(\|F\|_{\mathcal H}^2\).  For any tail \(A\), the squared
\(\mathcal H\)-norm of the corresponding partial sum is at most

\[
\int_{\bigcup_{\gamma\in A}D_\gamma}\|F(y)\|^2\,d\mu(y),
\]

which tends to zero.  Thus (C.3) is independent of the enumeration before
any contraction argument is applied.

If \(\mathcal L^{\rm raw}_{s,m}\) denotes the same raw formula realized on
\(L^2(\Delta,m;\mathscr F)\), the raw and normalized Hilbert operators are
related by the boundedly invertible density conjugacy

\[
\mathcal P_s=M_\rho^{-1}\mathcal L^{\rm raw}_{s,m}M_\rho,
\tag{C.4}
\]

with the natural change between \(L^2(\mu)\) and \(L^2(m)\).  Formula (C.3),
rather than (C.4), is authoritative for the Hilbert-space proofs below.

### Theorem C.1 -- contraction and exact branch obstruction

For every \(s\) with \(\operatorname{Re}s\geq0\), \(\mathcal P_s\) is a
contraction on \(\mathcal H\), but it is not compact.

For a fixed branch, define

\[
(K_{s,\gamma}f)(x)
=p_\gamma(x)e^{-sr_\gamma(x)}f(h_\gamma x),
\quad
K_{s,\gamma}:L^2(D_\gamma,\mu)\to L^2(\Delta,\mu).
\tag{C.5}
\]

Then

\[
\boxed{
\|K_{s,\gamma}\|
=\operatorname*{ess\,sup}_{x\in\Delta}
 \sqrt{p_\gamma(x)}e^{-\operatorname{Re}s\,r_\gamma(x)}>0.
}
\tag{C.6}
\]

Since \(\mu\) is nonatomic,

\[
\boxed{
\|K_{s,\gamma}\|_{\rm ess}=\|K_{s,\gamma}\|.
}
\tag{C.6a}
\]

If \(J_\gamma\) denotes extension by zero from
\(L^2(D_\gamma,\mu;\mathscr F)\) into \(\mathcal H\), then

\[
\mathcal P_sJ_\gamma=K_{s,\gamma}\otimes U_\gamma.
\tag{C.7}
\]

Consequently

\[
\|\mathcal P_s\|_{\rm ess}\geq\|K_{s,\gamma}\|>0.
\tag{C.8}
\]

#### Proof

Convexity of the squared Hilbert norm, (C.2), and
\(|e^{-sr}|\leq1\) give

\[
\|\mathcal P_sF(x)\|^2
\leq\sum_\gamma p_\gamma(x)\|F(h_\gamma x)\|^2.
\]

The inverse-branch disintegration identity

\[
\int_{D_\gamma}q(y)\,d\mu(y)
=\int_\Delta p_\gamma(x)q(h_\gamma x)\,d\mu(x)
\tag{C.9}
\]

then proves \(\|\mathcal P_sF\|\leq\|F\|\).

The same identity gives, for scalar \(f\),

\[
\|K_{s,\gamma}f\|^2
=\int_{D_\gamma}p_\gamma(Ty)e^{-2\operatorname{Re}s\,r(y)}
 |f(y)|^2\,d\mu(y),
\]

which proves (C.6).  It is strictly positive because \(D_\gamma\) has
positive measure, \(p_\gamma(Ty)>0\) almost everywhere on that branch, and
the roof is finite.

Put \(m(y)=\sqrt{p_\gamma(Ty)}
e^{-\operatorname{Re}s\,r(y)}\) and \(M=\operatorname*{ess\,sup}m\).
For every \(\varepsilon>0\), nonatomicity partitions a positive-measure
subset of \(\{m>M-\varepsilon\}\) into disjoint positive-measure sets
\(E_n\).  Their normalized indicators form an orthonormal, hence weakly
null, sequence, while
\(\|K_{s,\gamma}1_{E_n}/\sqrt{\mu(E_n)}\|\ge M-\varepsilon\).
Every compact operator sends this sequence to zero in norm.  Letting
\(\varepsilon\downarrow0\) proves (C.6a).

Disjointness of the branch domains proves the exact isolation (C.7), and
the tensor essential-norm theorem proves (C.8).  With \(U_\gamma=1\), the
same branch compression and (C.6a) show that the scalar normalized transfer
is already noncompact for every \(\operatorname{Re}s\geq0\).  \(\square\)

### Theorem C.2 -- imaginary-axis coisometry

For every \(t\in\mathbb R\), \(\mathcal P_{it}\) is a coisometry and

\[
\boxed{
\mathcal P_{it}\mathcal P_{it}^*=I,
\qquad
\|\mathcal P_{it}\|_{\rm ess}=1.
}
\tag{C.10}
\]

#### Proof

We take Hilbert inner products to be linear in their first argument.  For
\(y\in D_\gamma\), define the twisted Koopman operator

\[
(\mathcal U_tG)(y)
=e^{it r(y)}U_\gamma^*G(Ty).
\tag{C.11}
\]

Invariance of \(\mu\) and unitarity of the multiplier show that
\(\mathcal U_t\) is an isometry.  Equations (C.3) and (C.9) give
\(\mathcal P_{it}=\mathcal U_t^*\).  Hence

\[
\mathcal P_{it}\mathcal P_{it}^*
=\mathcal U_t^*\mathcal U_t=I.
\]

For an orthonormal sequence \((e_n)\) in \(\mathcal H\), the sequence
\((\mathcal U_te_n)\) is orthonormal and

\[
\mathcal P_{it}\mathcal U_te_n=e_n.
\]

Every compact \(C\) sends \(\mathcal U_te_n\) to zero in norm.  Therefore
\(\|\mathcal P_{it}-C\|\geq1\); the reverse bound follows from
\(\|\mathcal P_{it}\|=1\).  This proves (C.10).  \(\square\)

The scalar normalized Perron--Frobenius operator is noncompact throughout
\(\operatorname{Re}s\geq0\) by (C.6a), and on the imaginary axis it is
likewise the adjoint of an isometry.  The normalized \(L^2\) conclusion is
therefore a space-level robustness test, not an oscillator-specific novelty.
The oscillator-specific full-sum obstruction is Theorem B.2 on the raw
\(C_b^1\) realization.

## D. Absolute atomic half-plane

This section verifies, rather than assumes, the two application hypotheses
of the C24 discrete-metaplectic-atom theorem on the normalized \(L^2\)
space.

Extend (C.5) to a base operator \(A_{s,\gamma}\) on all of
\(L^2(\Delta,\mu)\) by first restricting the input to \(D_\gamma\).  Let

\[
q_\gamma=\mu(D_\gamma),
\qquad
R_\gamma=\inf_{x\in\Delta}r_\gamma(x).
\]

### Proposition D.1 -- branch-norm summability

Uniform distortion, (A.2), and (A.4) imply

\[
p_\gamma(x)\asymp e^{-d r_\gamma(x)},
\qquad
q_\gamma\asymp e^{-dR_\gamma},
\tag{D.1}
\]

with constants independent of \(\gamma\).  Hence, for
\(a=\operatorname{Re}s\geq0\),

\[
\|A_{s,\gamma}\|
\leq C q_\gamma^{\,1/2+a/d}.
\tag{D.2}
\]

In particular,

\[
\boxed{
a\geq d/2
\quad\Longrightarrow\quad
\sum_\gamma\|A_{s,\gamma}\|<\infty.
}
\tag{D.3}
\]

#### Proof

The first comparison in (D.1) follows directly from (A.2) and the uniform
upper and lower bounds on \(\rho\).  The oscillation of every
\(r_\gamma\) is uniformly bounded by (A.1) and finite AGY Finsler diameter
of \(\Delta\).  Integrating \(p_\gamma\) therefore gives the second
comparison.
Formula (C.6) now yields (D.2).  If \(a\geq d/2\), then
\(\beta=1/2+a/d\geq1\), so \(q_\gamma^\beta\leq q_\gamma\).  Finally,
\(\sum_\gamma q_\gamma=1\), proving (D.3).  \(\square\)

### Proposition D.2 -- signed aggregates cannot cancel

Let \(\varpi:\operatorname{Mp}(J_0,\mathbb R)\to
\operatorname{Sp}(J_0,\mathbb R)\) denote the covering map.  Choose one
reference lift above every projected symplectic matrix \(g\), and write

\[
U_\gamma=\varepsilon_\gamma U_g,
\qquad
\varepsilon_\gamma\in\{\pm1\},
\]

and form the signed aggregate

\[
A_{s,g}
=\sum_{\varpi(\widetilde g_\gamma)=g}
 \varepsilon_\gamma A_{s,\gamma}.
\tag{D.4}
\]

Every nonempty aggregate in (D.4) is nonzero.

#### Proof

Fix \(\gamma_0\) occurring in the aggregate and choose a nonzero scalar
function \(f\) supported in \(D_{\gamma_0}\).  If
\(\gamma\neq\gamma_0\), then \(h_\gamma(x)\in D_\gamma\) and hence
\(f(h_\gamma x)=0\) almost everywhere.  Thus

\[
A_{s,g}f
=\varepsilon_{\gamma_0}A_{s,\gamma_0}f\neq0.
\]

The argument retains rather than removes the central sign.  \(\square\)

Combining D.1 and D.2 with the C24 atomic theorem proves noncompactness once
again for \(\operatorname{Re}s\geq d/2\).  This proof is redundant with
Theorem C.1, but it closes the previously open absolute-branch and
noncancellation gates on this specific Hilbert realization.

## E. An all-length Rauzy matrix decoder

The support proof in Proposition D.2 already rules out aggregate
cancellation.  The following independent result is stronger on the present
four-letter coding: the full chronological matrix itself retains the entire
fixed-start labeled path.

This is presented as an explicit algorithmic restatement of the standard
simplicial-cylinder coding geometry, not as an unsupported general novelty
claim.  Kerckhoff's refinement cones provide the closest classical
geometric antecedent; the row-dominance/subtraction formulation and the
conventions needed here are proved in full below.

### Theorem E.1 -- fixed-start matrix injectivity

Fix an irreducible labeled Rauzy permutation \(\pi\).  For a finite path
\(\gamma=e_1\cdots e_n\) starting at \(\pi\), use

\[
B_e=I+E_{\ell,w},
\qquad
B_\gamma=B_{e_n}\cdots B_{e_1}.
\]

Then the pair \((\pi,B_\gamma)\) uniquely determines the complete directed
edge word \(e_1\cdots e_n\).  The conclusion uses the full labeled
\(d\)-by-\(d\) Rauzy matrix; it need not survive passage to a relative
quotient, a characteristic polynomial, a spectrum, or a conjugacy class.

#### Proof

Put \(R=B_\gamma^T\).  At the current permutation let \(a\) and \(b\) be
the distinct rightmost top and bottom labels.  The two possible outgoing
arrows interchange winner and loser.  If the true first arrow has winner
\(w\) and loser \(\ell\), then

\[
R=(I+E_{w,\ell})R',
\qquad
R'=B_{e_2\cdots e_n}^T.
\tag{E.1}
\]

Therefore

\[
\operatorname{row}_w(R)
=\operatorname{row}_w(R')+\operatorname{row}_\ell(R'),
\qquad
\operatorname{row}_\ell(R)=\operatorname{row}_\ell(R').
\tag{E.2}
\]

The true candidate is thus characterized by componentwise dominance
\(\operatorname{row}_w(R)\ge\operatorname{row}_\ell(R)\), with at least
one strict coordinate because \(R'\) is nonnegative and invertible.  If the
opposite arrow also passed, the two rows would dominate each other and hence
would be equal, contradicting invertibility of \(R\).  Exactly one first
arrow is admissible.

Subtracting the loser row from the winner row recovers

\[
R'=(I-E_{w,\ell})R.
\tag{E.3}
\]

This subtraction preserves the nonnegative integral path-matrix cone.  The
sum of all entries decreases by the strictly positive sum of the loser row.
After updating the labeled permutation, induction peels every edge and ends
at \(I\).  Hence decoding is unique.  \(\square\)

### Corollary E.2 -- no branch-matrix collision in the four-letter model

Distinct AGY return paths based at the frozen four-letter state have distinct
full matrices.  Since the crossing form is nondegenerate in the present
\(\mathcal H(2)\) realization, no relative-homology quotient intervenes.
After the decoder recovers the edge word, the declared edge lifts recover
the metaplectic central sign as well.  The matrix alone does not encode that
sign, and the corollary does not claim otherwise.

Concatenations of first-return words decode uniquely and split at visits to
the base state.  Thus their matrix monoid is free on the countable set of
first-return generators.  This statement is about full labeled matrices,
not their characteristic polynomials; the C24 spectral collisions are fully
compatible with it.

## F. Chronology audit

No transition matrix is averaged in any theorem above.  In an iterate of
(C.3), an inverse history contributes the ordered operator product obtained
by literal composition.  The unitary belonging to the later forward return
acts on the left of the unitary belonging to the earlier return.  Therefore
the underlying Rauzy matrices have exactly the C24 chronological order, and
the product of the declared metaplectic lifts automatically retains the
central sign.  Roofs add along the same literal history.

Grouping terms in (D.4) is only an algebraic collection of identical final
fiber operators after the chronological products have been formed.  It is
not a replacement by an averaged Rauzy matrix.

## G. Ordinary-determinant conclusion and escape hatches

For every \(s\) with \(\operatorname{Re}s>-\sigma _0\), the raw operator
\(\mathcal L^{\rm raw}_s\) is noncompact on
\(C^1_b(\Delta;\mathscr F)\).  It is therefore not Banach nuclear, and its
ordinary Banach nuclear determinant is unavailable.

For every \(s\) with \(\operatorname{Re}s\geq0\):

- \(\mathcal P_s\) is noncompact on \(L^2(\mu;\mathscr F)\), so it lies in
  no finite Schatten class;
- the ordinary Hilbert Fredholm determinant and every finite-order
  regularized determinant \(\det_p\) are unavailable for \(\mathcal P_s\);
- on \(s=it\), the stronger coisometry statement (C.10) holds.

Noncompactness does **not** imply that \(I-z\mathcal P_s\) is never Fredholm
or invertible.  The result also does not exclude:

- a flat or dynamical determinant not defined by an ordinary operator trace;
- the Weil distribution character, with its singular-locus restrictions;
- a canonically forced semifinite trace;
- genuine continuous group smoothing;
- a holomorphic or anisotropic completion with a separately proved trace
  theorem;
- a different quantum fiber or a different explicitly declared
  acceleration.

The bump/evaluation proof cannot be copied to a holomorphic space: a
nonzero holomorphic function cannot be supported inside one real branch.
Likewise, compactness and nuclearity do not transfer from one completion to
another.  A holomorphic C25 continuation would have to source-lock a common
complex domain, prove uniform complex distortion and branch-norm summability,
and prove a nonzero signed aggregate without using support.  None of those
facts is claimed here.

## H. Validation closure

The released exact certificate selects
\(\gamma_*=t^{64}(tbttbtbb)^8\) at the declared four-letter base state.  An
independent implementation verifies its 128 arrows, eight complete blocks,
neatness, strict matrix positivity, determinant one, and preservation of the
nondegenerate crossing form.  It also replays every step of the decoder and
the projective Jacobian identity \(j=e^{-4r}\).

The metaplectic conclusion does not depend on choosing a numerical central
sign: choose lifts of the declared symplectic edge maps and compose them
chronologically.  Every resulting branch factor is unitary, and both exact
compressions remain nonzero after either central choice.  Thus an explicit
oscillator-matrix discretization would add no application hypothesis and is
not used as a finite surrogate for the infinite-dimensional fibre.
