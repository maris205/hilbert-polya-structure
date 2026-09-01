# Theorem package

## Frozen owner

Let \(p\) be any fixed rational prime.  Give the compact additive group
\(G=\mathbb Z_p\) Haar mass one.  Its Pontryagin dual is
\(\widehat G=\mathbb Q_p/\mathbb Z_p\).  A nonzero class \(\xi\) has exact
conductor \(n(\xi)=n\ge1\) when its character is trivial on \(p^n\mathbb Z_p\)
but not on \(p^{n-1}\mathbb Z_p\).  There are exactly
\((p-1)p^{n-1}\) such characters.

For \(\alpha>0\), define the explicit conductor-shell Fourier multiplier

\[
D_{p,\alpha}1=0,\qquad
D_{p,\alpha}\chi_\xi=p^{\alpha n(\xi)}\chi_\xi,
\]

on the domain where the weighted squared Fourier coefficients are summable;
it is nonnegative and self-adjoint.
Set \(A_{p,\alpha,\mu}=D_{p,\alpha}+\mu I\), \(\mu\ge0\), and
\(T_t=e^{-tA_{p,\alpha,\mu}}\).  This multiplier definition, rather than any
external Vladimirov normalization, is authoritative.

## Main theorem

For every fixed prime \(p\), \(\alpha>0\), and \(\mu\ge0\):

1. The spectrum of \(D_{p,\alpha}\) is the simple eigenvalue zero and the
   eigenvalues \(p^{\alpha n}\), \(n\ge1\), with multiplicity
   \((p-1)p^{n-1}\).  Thus \(A_{p,\alpha,\mu}\) has the simple eigenvalue
   \(\mu\) and \(\mu+p^{\alpha n}\) with the same multiplicities.  Both
   operators have compact resolvent.
2. \(e^{-tD_{p,\alpha}}\) is a strongly continuous, positive, conservative,
   self-adjoint Markov contraction semigroup.  The killed semigroup \(T_t\) is
   positive sub-Markov and \(\|T_t\|=e^{-\mu t}\).
3. For \(q>0\), let \(\mathcal S_q\) mean that the singular values have
   finite \(q\)-sum; for \(0<q<1\) this is the quasi-Schatten ideal with its
   usual quasi-norm.  For \(t>0\), \(T_t\) belongs to every
   \(\mathcal S_q\), and

   \[
   \operatorname{Tr}T_t=e^{-\mu t}\left[1+
   \sum_{n\ge1}(p-1)p^{n-1}e^{-tp^{\alpha n}}\right].
   \]

4. On the mean-zero space, initially for \(\Re s>1/\alpha\),

   \[
   \zeta_{p,\alpha}(s)=\operatorname{Tr}'D_{p,\alpha}^{-s}
   =(1-p^{-1})\frac{p^{1-\alpha s}}{1-p^{1-\alpha s}}.
   \]

   This rational function of \(p^{-\alpha s}\) is its meromorphic continuation.
   Its complete pole set is

   \[
   s_k=\frac1\alpha+\frac{2\pi i k}{\alpha\log p},\quad k\in\mathbb Z,
   \]

   every pole is simple, and every residue is
   \((1-p^{-1})/(\alpha\log p)\).  Moreover
   \(\zeta(0)=-1\), \(\zeta'(0)=-\alpha\log p/(p-1)\), and

   \[
   \det{}'_{\zeta}D_{p,\alpha}=p^{\alpha/(p-1)}.
   \]

5. With \(N(\Lambda)\) counting positive eigenvalues with multiplicity,

   \[
   p^{\alpha m}\le\Lambda<p^{\alpha(m+1)}
   \quad\Longrightarrow\quad N(\Lambda)=p^m-1.
   \]

   Consequently
   \(\limsup_{\Lambda\to\infty}N(\Lambda)/\Lambda^{1/\alpha}=1\) and
   \(\liminf=1/p\).  This is an exact, non-vanishing discrete-scale
   oscillation, not an \(o(1)\) remainder.
6. For \(\sigma,q>0\),

   \[
   (I+D_{p,\alpha})^{-\sigma}\in\mathcal S_q
   \quad\Longleftrightarrow\quad \alpha\sigma q>1.
   \]

   The equality face diverges.

## Second reconstruction and positivity proof

Let \(E_n\) be conditional expectation onto functions constant on cosets of
\(p^n\mathbb Z_p\), with \(E_0=P_0\) the projection onto constants.  Then
\(E_n\uparrow I\) strongly and

\[
W_0=\operatorname{ran}E_0,\qquad
W_n=\operatorname{ran}E_n\ominus\operatorname{ran}E_{n-1},\qquad
\dim W_n=(p-1)p^{n-1}.
\]

Both reconstructions give

\[
D_{p,\alpha}=\sum_{n\ge1}p^{\alpha n}P_{W_n}
=\sum_{n\ge0}a_n(I-E_n),
\]

where \(a_0=p^\alpha\) and
\(a_n=p^{\alpha(n+1)}-p^{\alpha n}\) for \(n\ge1\).  Indeed, on \(W_m\)
the second sum telescopes to \(\sum_{n<m}a_n=p^{\alpha m}\).  Each
\(E_n+e^{-sa_n}(I-E_n)\) is a positive conservative contraction.  Finite
products commute, and their strong limit is \(e^{-sD_{p,\alpha}}\), proving
the Markov claim without an appeal to a named p-adic operator.

## Trace, zeta, counting, and ideals

The shell multiplicities immediately give the heat trace.  Superexponential
decay in the shell number makes it finite for every \(t>0\).  For the zeta,
the same multiplicities produce a geometric series with ratio
\(p^{1-\alpha s}\); its denominator gives all poles, and differentiation at
zero gives the determinant formula.

Summing the first \(m\) positive-shell multiplicities gives
\(\sum_{n=1}^m(p-1)p^{n-1}=p^m-1\), proving the counting staircase and both
envelopes.  More precisely, if \(t=p^{-\alpha m}\tau\), then locally uniformly
for \(\tau>0\),

\[
t^{1/\alpha}\bigl(\operatorname{Tr}e^{-tD_{p,\alpha}}-1\bigr)
\xrightarrow[m\to\infty]{} \Phi_{p,\alpha}(\tau)
=\frac{p-1}{p}\tau^{1/\alpha}
\sum_{j\in\mathbb Z}p^j e^{-\tau p^{\alpha j}},
\]

and \(\Phi_{p,\alpha}(p^\alpha\tau)=\Phi_{p,\alpha}(\tau)\).  Absolute and
locally uniform convergence follows from geometric decay as \(j\to-\infty\)
and superexponential decay as \(j\to+\infty\).  Finally, the \(q\)-sum of the
resolvent singular values is comparable to
\(\sum_n p^{n(1-\alpha\sigma q)}\), proving the exact Schatten condition and
endpoint divergence.

## Direct-owner boundary

Example 5.1 of Chacón-Cortés--Zúñiga-Galindo (`arXiv:1511.02146`) already
gives the same positive shell spectrum, multiplicities, geometric zeta, and
vertical pole lattice in dimension one.  Those formulas receive zero originality credit.
The retained result is the integrated zero-mode/Markov
reconstruction, scale and quasi-Schatten boundary, primed determinant,
degenerate faces, and independent finite-quotient certificate.

## Degenerate faces

- **\(\alpha=0\).** The natural frozen face is
  \(D_{p,0}=I-P_0\).  It is bounded and noncompact, with eigenvalue one of
  infinite multiplicity.  For each \(t>0\), the heat operators converge
  strongly as \(\alpha\downarrow0\), but not in operator norm: on mean-zero
  shells the norm defect is exactly \(e^{-(\mu+1)t}\).  Heat trace,
  finite-\(q\) Schatten membership, and the compact-resolvent zeta theorem fail.
- **\(\mu=0\).** Constants form the zero eigenspace, and the heat semigroup is
  conservative.  Every zeta and determinant in this package is explicitly
  mean-zero/primed, so no zero eigenvalue is silently inverted.
- **\(t=0\).** \(T_0=I\), which is neither compact nor in any finite
  \(\mathcal S_q\).  All trace and smoothing statements require \(t>0\).
- **\(\alpha\to\infty\).** For fixed \(t>0\),
  \(T_t\to e^{-\mu t}P_0\) in operator norm because the mean-zero norm is
  \(e^{-\mu t-tp^\alpha}\).
- **Smallest prime.** No formula uses an odd-prime hypothesis; \(p=2\) is
  included.  The parameter \(p\) is discrete, so there is no omitted
  “\(p\to1\)” boundary.

## Finite-quotient reconstruction

On \(G_N=\mathbb Z/p^N\mathbb Z\), the character indexed by \(k\ne0\) has
conductor \(N-v_p(k)\).  The DFT multiplier and
\(\sum_{n=1}^Np^{\alpha n}(E_n-E_{n-1})\) therefore agree exactly.  The
executable certificate tests quotient orders through 4096 and also verifies
small cases with exact SymPy rational matrices.  These computations audit
normalization and indexing; the proofs above establish the infinite theorem.

## Route-A conclusion

The fixed p-adic owner warrants only `A0_WEAK_ARITHMETIC_RELATION`.  There is
no all-prime carrier, primitive-orbit ledger, target determinant, analytic
bridge, or same-clock quantization.  Composite branching numbers \(4,6,10\)
reproduce the shell algebra, exposing the strongest proves-too-much
obstruction.  Thus the complete tuple is

`(A0_WEAK_ARITHMETIC_RELATION,A1_FAIL,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`,

overall `ROUTE_A_REJECTED`, under `NO_BAD_EULER_OR_ROOT_NUMBER`.
