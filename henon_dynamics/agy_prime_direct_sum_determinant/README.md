# HCS-C28 — sharp prime-Schatten thresholds

HCS-C28 closes the global finite-Weil assembly gate left by HCS-C27.  The
answer is a sharp positive/negative split.  The undamped sum over all odd
primes is not even compact, but the Dirichlet-damped operator

\[
\mathfrak L_{s,z}
=\bigoplus_{p\ {\rm odd}}p^{-z}\mathcal L_{s,p}
\]

is trace class exactly when \(\operatorname{Re}z>3\).  On that half-plane it
has an ordinary prime-order-independent Fredholm determinant

\[
\det(I-u\mathfrak L_{s,z})
=\prod_{p\ {\rm odd}}D_p(s,u p^{-z}).
\]

## Main theorem

For every Schatten index \(1\le q\le\infty\), the fixed-prime C27 operator
satisfies, locally uniformly in the AGY transfer parameter,

\[
\|\mathcal L_{s,p}\|_{S_q}\asymp p^{2/q}.
\]

Consequently,

\[
\bigoplus_p c_p\mathcal L_{s,p}\in S_q
\quad\Longleftrightarrow\quad
\sum_p p^2|c_p|^q<\infty,
\]

and the direct sum is compact exactly when \(c_p\to0\).  Thus
\(p^{-z}\)-damping gives \(S_q\) exactly on
\(q\operatorname{Re}z>3\).  In particular, the ordinary Fredholm threshold
\(\operatorname{Re}z>3\) is necessary as well as sufficient.

The determinant retains genuine chronology:

\[
\operatorname{Tr}\mathfrak L_{s,z}^{,n}
=\sum_p p^{-nz}\sum_{w\in\Gamma^n}
\Theta_p(g_w)
\frac{\lambda_w^{-(s+1)}}{\chi_w'(\lambda_w)}.
\]

No averaged transition matrix is used, and a repeated primitive word uses
\(\Theta_p(g_w^r)\), never \(\Theta_p(g_w)^r\).

## Why the two more canonical assemblies fail

- The unweighted counting-trace direct sum is noncompact because its block
  norms stay comparable to one.
- Normalized finite-Weil characters converge to the regular character of
  the integral cocycle group.  C25 proves that the positive AGY return
  monoid is free, so every nonempty moment vanishes in this limit and
  \(D_p(s,u)^{1/p^2}\to1\) on a common small \(u\)-disc.
- The ambient C24 full-Rauzy ledger contains one exact rank-two fixed-plane
  control, P073.  It has \(\Theta_p=p\) for every odd prime, so its
  dimension-normalized marked sum is \(\sum_p1/p\) and diverges.  P073 is
  not asserted to be a C26 induced branch.

This is therefore a **prime-graded Dirichlet--Fredholm determinant**, not an
adelic Weil representation.  The factor \(p^{-z}\) introduces an external
\(\log p\) clock; no continuation to \(z=0\), functional equation, common
conductor, Riemann divisor, self-adjoint operator, or RH statement follows.

## Reproduce

```bash
cd henon_dynamics/agy_prime_direct_sum_determinant
python -m pip install -r requirements.txt
bash code/run_c28.sh
```

The release runner regenerates the theorem certificate and independent
replay, executes the regression/mutation suite, and verifies the frozen
artifact manifest.  Refreshing that manifest is a separate explicit release
operation; a normal replay cannot bless changed artifacts.

## Project map

- `RESEARCH_QUESTION.md` and `EXPERIMENT_PLAN.md` — frozen gates;
- `DERIVATION_PACKAGE.md` and `THEOREM_PACKAGE.md` — proof chain;
- `SOURCE_AUDIT.md` — local provenance and the non-adelic terminology gate;
- `paper/main.pdf` — compiled manuscript;
- `code/` — exact producer, independent checker, mutation tests, and runner;
- `results/` — certificates, validation reports, and frozen hashes;
- `route_a_evaluation.yaml` — conservative Route-A evaluation.

## Decision

The Route-A tuple is

```text
(A1_WEAK,
 A2_ANALYTIC_DETERMINANT,
 A3_PARTIAL_ANALYTIC_STRUCTURE,
 A4_FORMAL_HINT)
```

with overall status `ROUTE_A_EXPLORATORY`; Route B is not authorized.  The
next large gate is a two-sided based/path-groupoid trace, where identity
holonomy loops can survive the regular trace, or a genuine local
\(p\)-adic/adelic oscillator architecture.  Further small-prime scans cannot
alter the C28 theorem.
