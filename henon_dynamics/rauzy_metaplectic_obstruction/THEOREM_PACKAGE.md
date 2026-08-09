# Theorem package: discrete metaplectic atoms cannot be compact

## Theorem 1: tensor essential norm

Let \(H_0,H_1\) be Hilbert spaces, let \(F\) be infinite dimensional, let
\(K:H_0\to H_1\) be bounded, and let \(U:F\to F\) be unitary.  Then

\[
\boxed{\|K\otimes U\|_{\rm ess}=\|K\|.}
\]

In particular, \(K\otimes U\) is compact if and only if \(K=0\).

### Proof

The upper bound follows from the ordinary operator norm.  Fix a unit vector
\(x\in H_0\) and an orthonormal sequence \((e_n)\) in \(F\).  Then
\(x\otimes e_n\rightharpoonup0\).  Every compact \(C:H_0\otimes F\to
H_1\otimes F\) satisfies \(C(x\otimes e_n)\to0\) in norm, whereas

\[
\|(K\otimes U)(x\otimes e_n)\|=\|Kx\|.
\]

Thus \(\|K\otimes U-C\|\ge\|Kx\|\).  Take the supremum over unit \(x\) and
then the infimum over compact \(C\).  \(\square\)

If \(K\) is compact, every nonzero singular value of \(K\) is repeated with
infinite multiplicity in \(K\otimes U\).  Finite oscillator cutoffs merely
display a growing finite part of this exact multiplicity.

## Corollary 2: modulo-compact branch compression

Under the assumptions of Theorem 1, let \(X,Y\) be Banach spaces and let
\(T:X\to Y\) be bounded.  Suppose bounded maps \(J:H_0\otimes F\to X\)
and \(R:Y\to H_1\otimes F\) satisfy

\[
RTJ=aK\otimes U+C,
\]

where \(a\ne0\), \(K\ne0\), and \(C\) is compact.  Then

\[
\boxed{
\|T\|_{\rm ess}\ge
\frac{|a|\|K\|}{\|R\|\|J\|}>0.
}
\]

This follows from the two-sided ideal property of compact operators.  It
applies to exact cylinder isolation and to isolation modulo compact errors.

## Theorem 3: discrete metaplectic atom obstruction

Let \(d\in\mathbb N\) with \(d\ge1\), and let \(H_0,H_1\) be Hilbert spaces.
Let

\[
\mu:\operatorname{Mp}(2d,\mathbb R)\longrightarrow
\mathcal U(L^2(\mathbb R^d))
\]

be the oscillator representation.  Let \(A_h:H_0\to H_1\) be bounded and
assume

\[
\sum_h\|A_h\|<\infty.
\]

The norm-convergent operator

\[
T=\sum_h A_h\otimes\mu(\widetilde g_h)
\]

is indexed by a countable collection in the metaplectic group.  Choose one
lift \(\widetilde g\) over each projected \(g\in\operatorname{Sp}(2d,\mathbb
R)\), and write

\[
\mu(\widetilde g_h)=\varepsilon_h\mu(\widetilde g),
\qquad \varepsilon_h\in\{\pm1\}.
\]

Define the signed aggregate

\[
A_g=\sum_{\pi(\widetilde g_h)=g}\varepsilon_h A_h.
\]

If at least one \(A_g\) is nonzero, then \(T\) is noncompact.  Quantitatively,

\[
\boxed{
\|T\|_{\rm ess}\ge
\sup_{\|x\|=\|y\|=1}
\left(\sum_g|\langle A_gx,y\rangle|^2\right)^{1/2}.
}
\]

The aggregation does not average chronological matrices.  It combines only
identical fiber operators and retains the actual central sign.

### Proof

Fix unit vectors \(x\in H_0\), \(y\in H_1\).  Inclusion on \(x\) and the
output slice on \(y\) compress \(T\) to

\[
V=\sum_g a_g\mu(\widetilde g),
\qquad a_g=\langle A_gx,y\rangle,
\]

with \((a_g)\in\ell^1\).  It suffices to prove
\(\|V\|_{\rm ess}\ge\|(a_g)\|_{\ell^2}\).

Let \(W(z)\) be the Weyl representation and choose a unit Schwartz vector
\(\phi\).  There is a phase-space vector \(z\ne0\) such that

\[
(g-h)z\ne0
\]

for every pair of distinct projected atoms: avoid the countable union of the
proper kernels \(\ker(g-h)\).  Put \(\phi_t=W(tz)\phi\).  Weyl matrix
coefficients vanish at infinity, hence \(\phi_t\rightharpoonup0\).
Metaplectic covariance gives, up to harmless phases,

\[
\mu(\widetilde g)\phi_t
=W(tgz)\mu(\widetilde g)\phi.
\]

For \(g\ne h\), the inner product of the corresponding terms tends to zero
because their centers differ by \(t(g-h)z\).  Diagonal terms have norm one.
Since \((a_g)\in\ell^1\), the double series is dominated by
\(\sum_{g,h}|a_ga_h|<\infty\), so dominated convergence yields

\[
\|V\phi_t\|^2\longrightarrow\sum_g|a_g|^2.
\]

For every compact \(C\), \(C\phi_t\to0\).  Therefore
\(\|V-C\|\ge\|(a_g)\|_2\), proving the scalar estimate.  The two slice maps
have norm one, and taking the supremum over \(x,y\) proves the theorem.
\(\square\)

The vanishing of Weyl matrix coefficients used above is elementary for
Schwartz vectors and extends to all \(L^2\) vectors by density and unitarity.

## C24 application

In a half-plane where a source-faithful Hilbert-space Rauzy/Zorich realization has

\[
\mathcal L_s^{\rm Mp}
=\sum_h e^{-sr_h}K_h\otimes\mu(\widetilde B_h),
\qquad
\sum_h e^{-\operatorname{Re}s\,r_h}\|K_h\|<\infty,
\]

Theorem 3 proves noncompactness whenever one signed aggregate is nonzero.  If
the selected analytic space has no proved absolute norm sum, Corollary 2 gives
the alternative branch-resolved route.

Noncompactness excludes every finite Schatten class, Hilbert/Banach
nuclearity, the ordinary Fredholm determinant, and finite-order regularized
determinants for this operator.  It does **not** say that
\(I-z\mathcal L_s^{\rm Mp}\) can never be Fredholm or invertible.

## Distribution-character firewall

For one infinite-dimensional unitary, \(|U|=I\) and
\(\operatorname{Tr}|U|=\infty\).  Thus \(\operatorname{Tr}U\) is not an
ordinary Hilbert-space trace.  Thomas instead defines the character after
smooth group integration and obtains a distribution.  On the regular set
\(\det(g-I)\ne0\), that distribution has a smooth representative of the form

\[
\text{Weil/Maslov/lift phase}\cdot|\det(g-I)|^{-1/2}.
\]

The 21 certified selected primitive labeled C24 cycles on \(\det(I-M)=0\)
show that this regular formula cannot be assigned orbitwise across the full
selected labeled-cycle set.  No claim is made that the 146 labels are distinct primitive
unmarked Teichmüller geodesics.

## Exact scope

The results close the unsmoothed discrete ordinary-Fredholm form within either
of the two stated realization hypotheses: a nonzero exact/modulo-compact
branch compression, or an absolutely norm-summable atomic expansion with a
nonzero signed aggregate.  Verifying one of those hypotheses on a particular
canonical analytic Zorich space remains an application gate.  The results do
not exclude flat traces, distributional characters, canonical semifinite
determinants, genuinely continuous group smoothing, or a new quantum fiber.
An arbitrary heat factor or oscillator truncation is outside the frozen
candidate.
