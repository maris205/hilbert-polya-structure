# HCS-C02C finite-window results

Status: **PASS**  
Run ID: `HCS_C02C_FINITE_WINDOW_V1`

## Outcome

The analytic finite-window pinning, chronological gluing, matching/Hill
determinant, and complex-base projective certificates are consistent with all
frozen adversarial checks.  The result is an effective specialization of
known pinning theory, not a new general pinning or Fredholm theorem.

## Frozen object

\[
H_6(q,p)=(1-6q^2-p,q),\qquad
D_\sigma=\overline D(\sigma\,23/48,7/48).
\]

Open ledgers: 432 complete sign cases through
\(N=8\).  Cyclic ledgers: 120
complete sign words through \(N=8\).  Short-window
complex boundary probes executed: 120;
their count and extrema are persisted in `certificate.json` rather than as
individual CSV rows.

## Strongest exact additions

- one-sided endpoint bounds
  \(|Q_{i,u}|\le\beta\kappa^{i-1}\) and
  \(|Q_{i,v}|\le\beta\kappa^{N-i}\), with
  \(\kappa=2/\sqrt{17}\),
  \(\beta=1/(\sqrt{17}-2)\);
- exact two-coordinate gluing, with scalar averaging rejected by the frozen
  expected-fail control;
- matching/Hill identity
  \[
  \det DF_N=-\frac{\det(I-DH_6^N)}{\det L_N}
  =\frac{\det C_N}{\det L_N};
  \]
- exact complex-base projective child disks
  \[
  D\left(-\varepsilon\frac{288512}{1393719},
  \frac{115360}{1393719}\right),
  \]
  separated by \(448/1803\), with fibre contraction
  \((224/773)^2\).

The base derivative bound is
\(12(224/773)^2=1.007669921>1\); no unscaled joint
base--fibre contraction is claimed.

## Worst regression metrics

- open recurrence residual: 1.827e-13;
- center-case crossed identity residual (100 digit): 5.286e-80;
- boundary-probe crossed residual: 4.951e-12;
- raw binary64 forward crossed discrepancy (conditioning diagnostic):
  6.435e-08;
- center-endpoint envelope ratio: 0.481178;
- boundary-probe envelope ratio: 0.541329;
- matching determinant error: 1.076e-96;
- Hill determinant error: 3.095e-90;
- raw binary64 Hill subtraction error (conditioning diagnostic):
  5.644e-05;
- direct/glued discrepancy: 9.398e-15;
- scalar-average expected-fail residual: 1.411e+00;
- reversed-order expected-fail discrepancy: 5.631e+03.

## Scope decision

`RETAIN_EFFECTIVE_SPECIALIZATION; MANUSCRIPT_HOLD;
NOVELTY_DELTA_UNCONFIRMED`.

Sterling--Dullin--Meiss Theorem 3 already covers the linearly conjugate real
signed-root SFT and real uniqueness.  Rugh and
Baladi--Pujals--Sambarino provide the qualitative complex pinning,
composition, periodic closure, and the orientation-twisted
absolute-denominator Cauchy/Fredholm mechanism.  The present result supplies
explicit complex \(H_6\) domains, constants and signed finite-dimensional
bookkeeping, but its publishable novelty is unconfirmed.  A paper claim still
needs a genuinely new signed, aggregate trace-compatible operator
approximation theorem.  Nuclearity, an infinite Fredholm determinant, Route-A
A2, and Hilbert--Pólya remain unestablished.

The 100-digit recheck is an implementation conditioning correction, not a
change of the frozen map, domains, chronology, cases, or pass threshold.  The
larger raw binary64 discrepancies remain in the certificate and CSV ledgers.
