# HCS-C03 exact finite-field pilot results

Status: **complete; `INCONCLUSIVE_BULK_DIFFERENCE`; no promotion**.

Route-A ceiling: **`LOCAL_FACTORS_ONLY`**.

The full \(p\leq251\) run proves a reproducible exact local ledger, but it
does not provide a canonical global Euler product, analytic continuation,
global divisor, or Hilbert--Pólya operator.  The large differences from an
unrestricted random permutation are almost entirely the already predicted
effect of writing the map as a product of two involutions.

## Frozen experiment

The definitions, two control ensembles, diagnostics, and thresholds were
frozen in `code/c03_PROTOCOL.md` before the full run.  The object was

\[
H_6(q,r)=(1-6q^2-r,q)\quad\text{on all of }\mathbb F_p^2,
\]

with every prime \(p\leq251\), 16 deterministic replicates in each control
ensemble, master seed `20260805`, fixed counts through iterate 64, and direct
iterate checks through 12.  The primes 2 and 3 are bad reductions because the
quadratic coefficient vanishes; they remain in the exact ledger but were
excluded from all aggregates.  The good prime 7 was flagged separately
for its zero fixed-point discriminant.

The frozen empirical thresholds were:

- `NO_BULK_ANOMALY`: every matched-control primary diagnostic has mean
  absolute standardized effect below 1, and at most 20% of good primes lie
  outside the empirical 95% interval;
- `CANDIDATE_NONRANDOM_SIGNAL`: at least one diagnostic has absolute mean
  standardized effect at least 2, a common sign at at least 75% of valid good
  primes, and outside-interval rate at least 50%.

Neither condition was met.  The correct preregistered intermediate label is
therefore `INCONCLUSIVE_BULK_DIFFERENCE`, not a positive anomaly.

## Exact census

The run covered 54 primes, 52 good primes, and 995,777 phase points in 61.171
seconds.  For every prime it stores

\[
Z_p(u)=\prod_{\ell\geq1}(1-u^\ell)^{-c_{\ell,p}},\qquad
\#\operatorname{Fix}(H_6^n)=\sum_{\ell\mid n}\ell c_{\ell,p},
\]

both as sparse cycle factors and as cyclotomic factors.  All denominator
degrees equal \(p^2\).  Every permutation, inverse, repetition, direct fixed
count, and factor-degree check passed.

Across the 52 good primes there are 6,166 cycles.  Exactly 6,076 are
\(R\)-symmetric, while the remaining 90 cycles form 45 reversal pairs.  Of the
52 primes, 27 have no nonsymmetric pair at all.  The paired base factor has
total degree 1,142, so the symmetric sectors cover 993,480 of 995,764 good
phase points, a point-weighted fraction of 0.997706.

This concentration is not an arithmetic anomaly.  For
\(R(q,r)=(r,q)\) and \(I=H_6R\), every symmetric cycle contributes two
fixed-locus incidences, while nonsymmetric cycles contribute none.  Hence

\[
s_p=\frac{\#\operatorname{Fix}(R)+\#\operatorname{Fix}(I)}2.
\]

For every odd prime both fixed loci contain \(p\) points, so \(s_p=p\)
identically.  Consequently

\[
Z_p=Z_{p,\mathrm{sym}}Z_{p,\mathrm{pair}}^2,qquad
K_p=p+2t_p.
\]

The same identity holds in the matched random-involution ensemble.  It is a
forced reversible-map factorization, not a license to delete the square
factor and not evidence for an RH divisor.

## Fixed-point arithmetic head

The exact first-iterate count also passed its independent algebraic check:

\[
\#\operatorname{Fix}(H_6/\mathbb F_p)
=1+\left(\frac{28}{p}\right)
=1+\left(\frac7p\right)
\quad(p\ne2,3).
\]

Among good primes, 28 have no fixed point, 23 have two, and \(p=7\) has the
single double-root fixed point.  This is the forced Dirichlet-character
structure of the \(n=1\) fixed-point scheme.  It was predicted before the
full run and is not a discovered cross-prime anomaly.  It only matches the
first logarithmic coefficient of a possible
\(\zeta(s)L(s,\chi_{28})\)-type head at the good primes; it
does not identify full Euler factors.

## Control ruling

Against unrestricted random permutations, the good-prime aggregate effects
are enormous: mean standardized effects are \(+38.802\) for cycle count,
\(-2.884\) for largest-cycle fraction, and \(+44.624\) for short-cycle point
mass.  These comparisons reject the wrong null model.

Against the fixed-locus-matched involution-product control, none of the
prespecified diagnostics reaches the frozen candidate threshold:

| diagnostic | Hénon mean | matched-control mean | mean z | mean absolute z | outside 95% |
|---|---:|---:|---:|---:|---:|
| cycle count | 118.577 | 120.512 | -0.768 | 1.073 | 13.5% |
| fixed points | 0.904 | 1.978 | -0.683 | 0.737 | 9.6% |
| largest-cycle fraction | 0.07502 | 0.07955 | -0.089 | 1.078 | 23.1% |
| short-cycle point fraction | 0.28244 | 0.28049 | -0.127 | 0.940 | 19.2% |
| symmetric-degree fraction | 0.99591 | 0.99122 | +0.212 | 0.915 | 15.4% |

The symmetric-cycle count agrees exactly with the matched control, as the
fixed-locus identity requires.  No diagnostic reaches the frozen candidate
threshold.  Cycle count and largest-cycle dispersion narrowly exceed the
strict `NO_BULK_ANOMALY` thresholds, so the computer-generated ruling remains
`INCONCLUSIVE_BULK_DIFFERENCE`; with only 16 controls per prime, promoting
either small residual would be unjustified.  This is consistent with the
random-involution null results of Roberts and Vivaldi
(https://arxiv.org/abs/0905.4135).

## Hard-kill decision and Route A

The naive claim

> raw finite-field Hénon permutation factors already define a distinguished
> RH-relevant global Euler product

is killed at this stage.  Exact local factors pass, but their conspicuous bulk
structure is forced by reversibility and matched by the correct null model.
No additional computation over more primes is warranted without a prior
theorem that defines the global object.

There is a sharper conceptual obstruction.  Substituting \(u=p^{-s}\) binds
the dynamical iterate \(n\) to the Euler power \(p^{-ns}\).  The census gives
no cohomological, sheaf-theoretic, or trace-formula reason for this diagonal
identification.  It also differs from the standard extension-degree role of
Frobenius in a Hasse--Weil local zeta.  Numerical convergence of a truncated
product would not repair that missing arrow.

The recorded Route-A verdict is therefore:

- A1: `A1_WEAK`;
- A2: `A2_FAIL`;
- A3: `A3_FAIL`;
- A4: `A4_FAIL`;
- overall: `ROUTE_A_REJECTED`.

C03 can be retained as a local arithmetic/reversibility control or revived
only after a target-blind global construction is supplied theoretically.  It
does not advance to the next-paper theorem lane from this pilot.

## Reproduction and artifacts

Commands, from repository root:

```bash
python next_paper_henon_candidate_search/code/c03_test_finite_field.py
python next_paper_henon_candidate_search/code/c03_finite_field.py
python next_paper_henon_candidate_search/code/c03_independent_check.py
```

The ten unit tests passed.  The independent checker imports none of the
primary implementation and recomputed all 54 raw cycle ledgers with tuple
states; all passed in 0.497 seconds.

- `c03_census.json`: complete configuration, local factors, fixed counts,
  controls, checks, aggregates, firewall, and Route-A ruling;
- `c03_prime_summary.csv`: one row per prime;
- `c03_cycle_counts.csv`: sparse raw/symmetric/paired cycle factors;
- `c03_fix_counts.csv`: fixed counts through iterate 64;
- `c03_random_controls.csv`: all 1,728 frozen control realizations;
- `c03_independent_check.json`: independent raw-ledger replication.

Primary implementation SHA-256:
`fe48b62cde643ff93d5f019154e6d517b66e016597111a5f93dbbe0c7c618029`.
Frozen protocol SHA-256:
`360bcf842cc52191b87cfce77f1ee5b7b6ff55205ae4f15c9b6b3b87c75c5da7`.

## Limitations

- The census ends at \(p=251\); the empirical control quantiles use only 16
  replicates per prime.
- The matched control preserves reversibility and both involution fixed-set
  sizes, but not polynomial degree or algebraic geometry.
- The computation uses \(\mathbb F_p^2\), not points over all extension fields.
- Local cyclotomic rationality is automatic for a finite permutation and is
  not formal Route-A A2.
- No normalization beyond the exact symmetric/paired factorization was
  allowed; no target data were used.
