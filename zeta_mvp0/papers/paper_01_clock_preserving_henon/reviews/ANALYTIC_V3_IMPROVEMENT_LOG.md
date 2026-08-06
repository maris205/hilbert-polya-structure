# Paper 7 analytic-v3 improvement log

## Version lineage

| Version | Role | Pages | SHA-256 |
|---|---|---:|---|
| `../paper/paper7_round2_final.pdf` | Immutable pre-analytic baseline | 35 | `8ad75ae285244bef380d6474b7e1a4ecb943b6fe96d03fa99c9efd44192a3339` |
| `paper7_analytic_v3_round0.pdf` | Analytic-v3 before independent review | 45 | `a990f044865b40de491a9b39d6f41b910f08e9942e3ecb2134ef383a41a7eae0` |
| `paper7_analytic_v3_round1.pdf` | After Round-1 mathematical/editorial revision | 45 | `78a7f3bcaa36f91b944d7c2cf1d1a64e35bd17a346d199814d9206d7fdf76c5b` |
| `paper7_analytic_v3_round2_final.pdf` | Accepted final analytic-v3 | 45 | `e961e1b65963b2b769d7454e27913bbfa57c60d9e46849b4c8f5834a900ab0ff` |

The baseline was never overwritten.

## Scientific upgrade

The earlier manuscript proved the clock construction and Weyl-scale results
but supported spectral activity mainly through geometry and finite-window
diagnostics.  Analytic-v3 adds two exact, independent nonisospectrality
certificates for the centered one-step nonmagnetic scalar pair:

1. strict ground-state activation,
   \[
   \lambda_1(\mathsf H_{a,\hbar})>
   \lambda_1(\mathsf H_{0,\hbar});
   \]
2. the explicit uniform relative heat asymptotic,
   \[
   \Theta_{a,\hbar}(t)-\Theta_{0,\hbar}(t)
   =-\frac{a^2}{24\pi}
   \left[L^2+\bigl(2(1-\gamma)+4\pi r_a^2\bigr)L+\kappa_a\right]
   +O_{a,\hbar}(tL^4).
   \]

The proof appendix contains the complete rearrangement equality-case audit
and the noncompact Brownian good/bad-event remainder argument.

## Structural and presentation upgrade

- Retitled the paper around the two proved analytic contributions.
- Scoped every nonisospectrality statement to the centered one-step
  nonmagnetic subfamily.
- Split \(S_{\mathrm{op}}\) (proved) from \(S_{\mathrm{dyn}}\) (sampled) in
  the hero figure and Hilbert--P\'olya ledger.
- Removed duplicate relative-container/prime-gate prose by making Section 8
  the sole authoritative location.
- Added a cancellation-free analytic Figure 3 and made clear it evaluates
  exact carrier integrals rather than estimated heat traces.
- Expanded the bibliography to 77 audited entries, with 67 printed.
- Added the verified corresponding-author email and corrected the Morrey
  BibTeX name parsing.
- Separated the published low-dimensional-chaos context from the exact
  H\'enon-specific provenance of \(a=1.02\).

## Review-driven mathematical safeguards

- Closed the rearranged form domain explicitly.
- Stated positivity improvement, simplicity, and analytic elliptic
  regularity precisely.
- Separated the two nonnegative rearrangement deficits.
- Verified the exact Brothers--Ziemer exceptional set.
- Deleted an unnecessary, insufficiently sourced all-time heat-trace
  ordering.
- Defined all constants and standardized \(\mathsf H_{a,\hbar}\).
- Preserved the \(\hbar=1\) scope of the displayed two-growing-term Weyl law.

## Integrity corrections found by Round 2

- Inserted a float barrier so Table 5 no longer interrupts Proposition 8.1.
- Rejected an initially proposed Zenodo DOI after file-level review showed it
  referred to a different 21-page expansion.  The final citation points to
  the exact 17-page PDF at an immutable Git commit and records both hashes.

## Final evidence boundary

Analytic-v3 is a stronger Hilbert--P\'olya-motivated candidate audit, not a
Hilbert--P\'olya solution.  Q, W, and the centered scalar
\(S_{\mathrm{op}}\) gate are proved; \(S_{\mathrm{dyn}}\) remains sampled,
R remains finite-window, C is an admissibility result, P is open, Z is
untested, and RH is not claimed.
