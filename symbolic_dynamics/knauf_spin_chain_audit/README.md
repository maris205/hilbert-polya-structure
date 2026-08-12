# SD-C06 — Knauf Spin-Chain Audit

## Frozen construction

Knauf's binary recursion is

\[
h_0=1,\qquad
h_{k+1}(\sigma,0)=h_k(\sigma),\qquad
h_{k+1}(\sigma,1)=h_k(\sigma)+h_k(1-\sigma),
\]

with

\[
Z_k(s)=\sum_{\sigma\in\{0,1\}^k}h_k(\sigma)^{-s}.
\]

In the proved convergence half-plane, the primary source obtains

\[
\lim_{k\to\infty}Z_k(s)
=Z(s)=\frac{\zeta(s-1)}{\zeta(s)}.
\]

## Findings

- **PROVED (primary-source theorem):** a low-description-complexity binary
  arithmetic recursion produces the exact unsigned zeta quotient for
  \(\operatorname{Re}s>2\).
- **NUMERICAL_OBSERVATION:** finite-depth multiplicities and convergence on
  the locked real/complex grid are tested without loading any Riemann zeros.
  Only points with \(\operatorname{Re}s>2\) are compared as evidence in the
  proved convergence domain; the remaining points are boundary/continuation
  diagnostics only.
- **MODELING_CHOICE:** the Liouville factor
  \(\lambda(h_k(\sigma))\) is an additional arithmetic observable.  It is not
  shown to arise as the holonomy of a pre-existing symbolic symmetry.
- **OPEN in the cited work:** the signed convergence needed in the wider
  half-plane is not proved; the paper links the gap to a spectral-radius /
  Ramanujan-graph problem.
- **A1/A2 failure for this program:** the finite partition sum and its limit
  are not a demonstrated primitive-cycle Fredholm determinant for the same
  binary recursion.  Nontrivial zeros appear as poles of the unsigned
  quotient.

This is the strongest direct prior-art collision found.  It remains an audit
benchmark, not a Route-B-ready candidate.

The random-sign protocol intentionally re-keys the field at every depth
\((\text{seed},k)\).  Differences between adjacent depths for that control are
therefore descriptive cross-level differences, not truncation drift of one
fixed random observable.  The post-run semantic audit records this boundary.

## Sources

- A. Knauf, [official preprint](https://www.mis.mpg.de/publications/preprint-repository/article/1997/issue-15)
- A. Knauf, [journal article](https://doi.org/10.1007/s002200050441)
- [erratum](https://doi.org/10.1007/s002200050715)
- A. Knauf, [recurrence normalization used by the implementation](https://arxiv.org/abs/1305.6410)

## Artifacts

- [Derivation package](DERIVATION_PACKAGE.md)
- [Post-run semantic audit](POST_RUN_AUDIT.md)
- exact finite-depth experiment and results under this candidate's `code/` and
  `results/` directories
