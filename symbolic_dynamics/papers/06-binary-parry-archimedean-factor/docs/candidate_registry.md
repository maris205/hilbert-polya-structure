# Candidate Registry

## SD-C08 — minimal-binary Parry/Hellinger extension

- Family: **Symbolic Dynamics**, exclusively.
- Base: SD-C07 tensor-prime atom-loop shift with entropy roof.
- New internal datum: the unique least-entropy tensor atom (F_2), its
  maximal-entropy Parry kernel (K_2=J_2/2), and the multiplicity-free
  decomposition of its symbol representation into trivial and sign lines.
- Tilted trace (cyclic representative):

  \[
  H_{\rm cyc}(u)=K_2\operatorname{diag}(e^{-iu},e^{iu}),\qquad
  \operatorname{tr}H_{\rm cyc}(u)^N=\cos(u)^N.
  \]
- Manuscript representative:
  \(H_{\rm sym}(z)=e^{zQ/2}K_2e^{zQ/2}\). With \(z=iu\), up to sign
  convention, it is the cyclic/similar representative with identical power
  traces and characteristic determinants.
- Stage status:
  **GO_A3_ARCHIMEDEAN_FACTOR / STOP_GLOBAL_COMPLETION**.
- Route B: locked; `route_b_invocation_allowed: false`.

### Route-A tuple

```text
(A0_ANALYTIC_ARITHMETIC_ORIGIN,
 A1_PASS_ANALYTIC,
 A2_ANALYTIC_DETERMINANT,
 A3_PARTIAL_ANALYTIC_STRUCTURE,
 A4_FORMAL_HINT)
```

Overall: `ROUTE_A_ANALYTIC_CANDIDATE`.

### Exact stationary channel

On
\(\ell^2(\operatorname{At})\otimes\mathbb C^2\), let

\[
\mathcal A_s=\bigoplus_{F_p}p^{-s}K_2.
\]

Since \(K_2^r=K_2\) and \(\operatorname{tr}K_2=1\),

\[
\operatorname{Tr}\mathcal A_s^r=\sum_p p^{-rs},\qquad
\det(I-\mathcal A_s)=\prod_p(1-p^{-s})=\zeta(s)^{-1}
\]

for \(\Re s>1\). This preserves the full SD-C07 repetition ledger.

### Archimedean sign channel

For the canonical sign observable of the same \(F_2\) fiber and odd \(N\),

\[
Y_N=\frac{S_N}{\sqrt{2\pi N}},\qquad
\mathbb E|Y_N|^{s-1}\longrightarrow
\pi^{-s/2}\Gamma(s/2),\quad \Re s>0.
\]

The finite characteristic function is a cyclic trace of the same tilted
family that gives the stationary ledger at \(u=0\). The Fredholm and Mellin
outputs are nevertheless different transforms; their product is recorded
as a same-source Mellin--Fredholm factorization, not one determinant.

### Specificity and controls

Uniform \(K_3,K_4\) retain the stationary rank-one ledger, but their
canonical radial standard sectors have dimensions \(2,3\) and converge to

\[
M_d(s)=(\pi d)^{-(s-1)/2}
\frac{\Gamma((d+s-1)/2)}{\Gamma(d/2)},
\]

not the binary factor. Biased binary and arbitrary scalar one-dimensional
CLT observables remain proves-too-much controls. A reversible kernel with
nonzero eigenvalue \(\lambda\) fails the ledger through
\(\operatorname{tr}K^r=1+\lambda^r\).

### Active boundary

The frozen Hellinger chiral block has active eigenvalues
\(\pm p^{-1/2}\). More generally, every bounded one-sided ansatz
\(A_t=G^{1/2+it}K=G^{it}A_0\) has all critical-axis \(t\)-dependence in the
unitary gauge \(\operatorname{diag}(G^{it},I)\), even when \([G,K]\ne0\).
No single determinant, meromorphic continuation, functional equation, pole
removal, trivial-zero mechanism, moving zero divisor, Riemann--von Mangoldt
law, or same-object Weil compression is proved.

Canonical evaluation:
`evaluations/route_a/SD-C08/20260813T235000Z.yaml`.
