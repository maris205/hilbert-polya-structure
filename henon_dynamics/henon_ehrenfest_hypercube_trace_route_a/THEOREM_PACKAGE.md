# C171 proof package

## Definition

Let \(X_d=\{-1,+1\}^d\), let \(x^{(i)}\) be obtained from \(x\) by flipping
coordinate \(i\), and define on \(L^2(X_d,2^{-d}\#)\)
\[
 (P_df)(x)=\frac1d\sum_{i=1}^d f(x^{(i)}),\qquad d\geq1.
\]
For \(S\subseteq\{1,\ldots,d\}\), put
\(\chi_S(x)=\prod_{i\in S}x_i\).

## Theorem (all-dimensional Ehrenfest certificate)

For every integer \(d\geq1\):

1. The \(2^d\) Walsh characters are an orthonormal eigenbasis and
   \[
   P_d\chi_S=\left(1-\frac{2|S|}{d}\right)\chi_S.
   \]
   Thus \(\lambda_j=1-2j/d\) has multiplicity \(\binom dj\).
2. For every \(n\geq0\),
   \[
   \operatorname{Tr}P_d^n=\sum_{j=0}^d\binom dj\lambda_j^n,
   \quad
   \det(I-zP_d)=\prod_{j=0}^d(1-z\lambda_j)^{\binom dj}.
   \]
   For \(|z|<1\),
   \(-\log\det(I-zP_d)=\sum_{n\geq1}\operatorname{Tr}(P_d^n)z^n/n\).
3. Every vertex has the same return probability,
   \[
   P_d^n(x,x)=2^{-d}\operatorname{Tr}P_d^n,
   \]
   and this probability is zero for odd \(n\).
4. Hamming weight \(k\) is a Markov lumping with
   \[
   Q(k,k+1)=\frac{d-k}{d},\qquad Q(k,k-1)=\frac{k}{d}.
   \]
   It is reversible for \(\pi_k=2^{-d}\binom dk\).  Its symmetric similarity
   has off-diagonal entry \(\sqrt{(k+1)(d-k)}/d\), and its simple spectrum is
   \(\lambda_0,\ldots,\lambda_d\), with Krawtchouk eigenvectors.
5. \(P_d\) is a natural finite self-adjoint contraction.  This fact alone does
   not supply a same-clock Hamiltonian lift: \(e^{-itP_d}\) replaces the
   discrete Markov clock and its path weights.

## Proof

Flipping coordinate \(i\) multiplies \(\chi_S\) by \(-1\) exactly when
\(i\in S\).  Averaging the \(|S|\) negative and \(d-|S|\) positive terms gives
the eigenvalue in part 1.  Walsh orthogonality and the count
\(\#\{S:|S|=j\}=\binom dj\) prove completeness and multiplicity.  Parts 2
then follow from the finite-dimensional spectral theorem; the trace-log
identity follows by applying \(-\log(1-w)=\sum_{n\geq1}w^n/n\) to every
eigenvalue.

Coordinate translations act transitively on \(X_d\) and commute with \(P_d\),
so all diagonal entries of \(P_d^n\) agree; their sum is the trace.  The cube
is bipartite by parity of Hamming weight, and one flip changes parity, proving
the odd-time assertion.

At weight \(k\), precisely \(d-k\) flips increase and \(k\) decrease weight,
which gives \(Q\).  The binomial identity
\[
 \binom dk(d-k)=\binom d{k+1}(k+1)
\]
is detailed balance.  Therefore
\(D_\pi^{1/2}QD_\pi^{-1/2}\) is symmetric with the stated off-diagonal.
Define
\[
 K_j(k)=\sum_r(-1)^r\binom kr\binom{d-k}{j-r},\qquad
 \sum_jK_j(k)t^j=(1-t)^k(1+t)^{d-k}.
\]
Applying \(Q\) to the generating function and differentiating in \(t\) gives
\[
 QK_j=(1-2j/d)K_j.
\]
The \(d+1\) eigenvalues are distinct, hence these vectors form a basis and
the lumped spectrum is simple.  Finally each coordinate flip is a self-adjoint
permutation and their average is self-adjoint; exponentiating that average is
a different continuous-time unitary evolution, not the frozen Markov system.
This proves all claims. \(\square\)

## Dependency and edge-case audit

- \(d=1\): eigenvalues \(1,-1\); the lumped chain is the original two-cycle.
- Even \(d\): zero is an eigenvalue with multiplicity \(\binom d{d/2}\); its
  determinant factor equals one and is not silently assigned positive degree.
- \(n=0\): the trace and return identities give \(2^d\) and one.
- The trace-log radius is stated as \(|z|<1\), since \(1\) is always spectral.
- For every \(d>1\), weighted Markov closed walks are not fixed points of a
  deterministic map.  At \(d=1\) the operator is the deterministic two-cycle,
  but this isolated boundary supplies no uniform all-\(d\) primitive-orbit or
  arithmetic structure; no family-level Artin--Mazur claim follows.
