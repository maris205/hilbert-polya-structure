# Arithmetic spectral scout: a logarithmic Dirichlet–Gram candidate

2026-09-06. Research stage only: no C number, admission, formal Route-A
evaluation, manuscript or PDF. This file records screening and the precise
candidate now being proved. It is not a claim of exhaustive novelty.

## Screened mechanisms

| Candidate | Object / observable | Decisive ownership or feasibility test | Current decision |
|---|---|---|---|
| Slowly compact Helson matrix | Entries `1/(sqrt(mn) log(mn) (log log(mn))^alpha)`, positive eigenvalue asymptotics | Miheisi–Pushnitski already prove the full leading power law with its constant, for every positive alpha. | Reject classical reconstruction. |
| Finite multiplicative Hilbert sections | `1/(sqrt(mn) log(mn))`, `2 <= m,n <= N`, norm and edge spectrum | The infinite spectrum is owned by Brevig et al. and Perfekt–Pushnitski. Charif–Abdallah–Benyamine already study finite sections; the proposed elementary edge question has no identified independent increment. | Do not admit. Only abstract/metadata of the finite-section source accessed, not its full proof. |
| Log-periodic Helson kernels | A periodic function of `log log(mn)` in the numerator; band spectrum after Mellin transformation | Pushnitski–Sobolev's continuous Hankel band theory is already available. Passing essential spectrum through an existing compact-error equivalence is a short consequence, not a new paper-level contract. | Reject this formulation. |
| Prime-factor hopping over a logarithmic diagonal | Formal prime-orbit decomposition of a source operator | No native dynamical construction or substantive unresolved theorem was identified; the exact decomposition would merely insert the primes as input. | Abandon before construction. |
| Arithmetic sparse compression | Multiplicative Hilbert matrix restricted to primes, including fixed reduced residue classes | Positive trace-class Gram representation is elementary; the substantial question is the *sharp logarithmic eigenvalue law*, with a comparison estimate strong enough on the square-root exponential scale. | Full proof candidate with independent internal checking; not yet admitted. |

The local collision search includes the two Hénon registries and the earlier
Gram/GCD, delta-chain and exponential-wall mechanisms. This candidate does not
reuse their operator or proof. An initial command used nonexistent root-level
registry names and failed; the actual registries are in `henon_dynamics/docs/`.
Absence of an exact keyword match does not establish novelty.

## Active object and contract

Let `a_j > 1` be a locally finite sequence with a positive lower bound away
from 1, and let `w_j > 0`. Suppose the nonnegative Dirichlet series

`D(s) = sum_j w_j a_j^(-s)`

converges for real `s > rho` and, for some `c > 0`, has the local form

`D(rho + u) = -c log u + A(u)`

on the right part of a disk about zero, with `A` holomorphic throughout that
disk. The intended operator is the native positive Gram matrix

`G_ij = sqrt(w_i w_j) (a_i a_j)^(-rho/2) / log(a_i a_j)`

on the indicated sequence space, with eigenvalues in decreasing order and
multiplicity. The desired single theorem is

`log(lambda_n(G)) / sqrt(n) -> -pi sqrt(2)`.

Its natural corollaries concern the Fredholm determinant and the inverse
logarithmic counting function, not Riemann zeros. For primes in any nonempty
fixed collection of reduced classes modulo a fixed q, the local logarithmic
coefficient should be `c = number_of_classes / phi(q)`; the leading logarithmic
spectral coefficient above does not retain this density.

The earlier heuristic for *arbitrary* sets with counting density
`C x / (log x)^beta` was broader: it suggested `-pi sqrt(2 beta)`.
That general density-only statement is **not included** in this contract and
has not been proved. A counting asymptotic is not silently replaced by a
holomorphic logarithmic germ.

## Key difficulty and proposed resolution

Factor G into exponentials to obtain the integral Hankel kernel
`D(rho+t+s)`. Compare it with the exponential integral
`c E1(t+s)`, where `E1(u)=integral_1^infinity exp(-u x) dx/x`.
Their difference has a removable logarithmic singularity at zero.
An explicit dyadic Taylor construction is intended to prove

`N_s(exp(-L); error) = O(L log L) = o(L^2)`.

This is stronger than membership in every Schatten class. The latter, used
in the Miheisi–Pushnitski power-law argument, would not justify the present
exponential-scale conclusion. The comparison with `E1` then reduces, through
Laguerre functions and positive moment weights, to Widom's classical Hankel
matrix with entries `(j+k+1)^(-2)`. That classical spectral law is an input,
not a new theorem here. The full proposed argument is in `PROOF_DRAFT.md`.

Fail the contract if the holomorphic remainder estimate cannot be proved,
if the actual leading coefficient differs, or if primary literature already
contains this same Dirichlet–Gram/logarithmic-germ transfer theorem. Elementary
trace-class positivity alone is not enough to admit a paper.

## Sources actually accessed

- Miheisi–Pushnitski, *A Helson matrix with explicit eigenvalue asymptotics*,
  [arXiv:1709.06326](https://arxiv.org/abs/1709.06326), JFA DOI
  [10.1016/j.jfa.2017.11.002](https://doi.org/10.1016/j.jfa.2017.11.002).
  Read the public PDF introduction and reduction statements through Theorem 2.1
  and Lemma 2.2; not a full-paper proof audit.
- Pushnitski–Yafaev, *Asymptotic behaviour of eigenvalues of Hankel operators*,
  [arXiv:1412.2633](https://arxiv.org/abs/1412.2633), IMRN DOI
  [10.1093/imrn/rnv048](https://doi.org/10.1093/imrn/rnv048).
  Read the public introduction and Mellin/moment equivalence statements.
  **Caution:** its public v1 introduction prints a Widom exponent involving
  `sqrt(2 gamma n)`, inconsistent with the `gamma-1` form below. Do not copy
  that coefficient uncritically.
- Tantalakis, *Eigenvalue asymptotics for a class of multi-variable Hankel
  matrices*, [arXiv:2206.12695v2](https://arxiv.org/abs/2206.12695v2),
  [10.1515/conop-2022-0137](https://doi.org/10.1515/conop-2022-0137).
  Read its introduction, main statements and proof outline. It explicitly
  reports Widom's example after Theorem 3.3 as
  `exp(-pi sqrt(2(alpha-1)n)+o(sqrt(n)))`.
- Widom, *Hankel matrices*, Trans. AMS 121 (1966), 1–35,
  [10.1090/S0002-9947-1966-0187099-X](https://doi.org/10.1090/S0002-9947-1966-0187099-X).
  Bibliography and JSTOR issue record verified. Attempts to obtain the AMS
  original returned access errors, and JSTOR did not yield readable full text.
  **Original theorem text not yet accessed.** The presently available precise
  statement is Tantalakis's report; do not describe it as an original-text audit.
- Brevig–Perfekt–Seip–Siskakis–Vukotić, *The multiplicative Hilbert matrix*,
  [10.1016/j.aim.2016.07.019](https://doi.org/10.1016/j.aim.2016.07.019).
  Publisher abstract and introduction excerpts actually accessed.
- Charif–Abdallah–Benyamine, *On finite sections of the multiplicative Hilbert
  inequalities*, [publisher record](https://www.cambridge.org/core/journals/canadian-mathematical-bulletin/article/abs/on-finite-sections-of-the-multiplicative-hilbert-inequalities/337B14B5FC144940D1BFB495D5C09356).
  Abstract/metadata only; do not claim to have checked every finite-section result.
- Pushnitski–Sobolev, *Hankel operators with band spectra and elliptic functions*,
  [arXiv:2307.09242](https://arxiv.org/abs/2307.09242), Duke Math. J. 174(4)
  (2025), 685–746, DOI [10.1215/00127094-2024-0043](https://doi.org/10.1215/00127094-2024-0043).
  Institutional abstract and indexed theorem excerpts accessed, not the full proof.

Exact phrase searches for prime-indexed Helson/multiplicative-Hilbert operators
and prime-zeta Hankel kernels did not return an exact primary owner. This is a
limited search outcome, not a novelty certificate. Broader operator-theory
collision checking is still required before admission.

The local Dirichlet L-function inputs for the residue-class application were
subsequently checked against [NIST DLMF §25.15](https://dlmf.nist.gov/25.15):
the paragraph following (25.15.1) gives the principal simple pole and
nonprincipal analyticity, (25.15.2) gives the Euler product, and (25.15.9)
states nonvanishing at 1 for nonprincipal characters. These are classical
inputs, not consequences of the proposed Gram theorem.

## Subsequent independent checks and model-source resolution

The independent mathematical report
`../nonlinear_geometry/REVIEW_SPECTRAL_TRANSFER.md` found no blocker in
the transfer proof conditional on the classical model law. The separate
`../nonlinear_geometry/SPECTRAL_OWNERSHIP_CHECK.md` records four close
primary method owners, including Webb's June 2026 revision. It found no
direct exact owner in its bounded read scopes, but warns that the assembled
statement's standalone substance still requires judgment. None of the
Gram method, analytic low-rank approximation, spectral perturbation,
prime/AP corollaries or determinant corollary is a separate novelty claim.

`MODEL_MOMENT_PROOF.md` now supplies a complete alternate proof of the
classical coefficient by the ALT inequality and coherent states, followed
by a fully written elementary Tauberian step. It avoids using either
conflicting report of Widom's coefficient. The original Widom source
remains unaccessed; Araki's official abstract and Lafleche's full
Hilbert-space ALT statement/proof were actually read, with the access
limits and exact exponent substitution recorded in that supplement.

## Route boundary

This is an arithmetic input operator, not an orbit construction. In particular,
its inverse-log spectral counting scale is quadratic, not the target `T log T`.
There is no proved target Euler factor, root number, automorphy, zero/divisor
correspondence or Hilbert–Pólya realization. No formal grade has been assigned.
