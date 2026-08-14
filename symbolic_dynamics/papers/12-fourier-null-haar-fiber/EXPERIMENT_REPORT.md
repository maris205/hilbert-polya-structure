# SD-C14 deterministic experiment report

## Frozen outcome

The infinite Haar component is the unique positive all-order escape from
finite unitary moment rigidity, but it contributes exactly nothing new to the
analytic trace-log determinant. The stage decision is
`GO_INFINITE_HAAR_ESCAPE / STOP_DETERMINANT_INVISIBILITY / STOP_SCOPED /
PROVES_TOO_MUCH`; Route B remains false.

## Results

- The exact classification is \(\mu=\delta_1+c m_{\rm Haar}\), \(c\geq0\).
  Normalization or finite support forces \(c=0\).
- Cyclic approximants of every order \(N=2,\ldots,64\), audited through
  repetition 128, first leak at exactly \(r=N\). Their determinant is
  \((1-q)(1-q^N)^{c/N}\).
- Haar formulas were checked for \(c\in\{0.25,1,3\}\) and twelve complex
  points. The maximum quadrature residual in the unnormalized
  Fuglede--Kadison formula was `4.440892098500626e-16`.
- Density perturbations for frequencies 1 through 16 and four signed
  amplitudes first leak at their preregistered Fourier frequency in all 64
  cases.
- The self-adjoint control satisfies \(H^2=I\); its first even leak is power
  two. The recurrent formal-word control has nonzero coefficient
  \(2(1+c)xy\) from \(uu^{-1}\).
- Tensor-prime, composite-only, and seeded random-increasing inventories each
  used 128 atoms and \(c\in\{0.25,1,3\}\). All 9 controls have analytic
  determinant difference and phase range exactly zero. This is decisive
  `PROVES_TOO_MUCH` evidence.
- No target zeros, crossings, fitted parameters, or argument-principle census
  were used.

## Reproduction

```bash
PYTHONDONTWRITEBYTECODE=1 pytest -q -p no:cacheprovider code/test_sdc14_haar_fiber_experiment.py
PYTHONDONTWRITEBYTECODE=1 python code/sdc14_haar_fiber_experiment.py
sha256sum -c results/SHA256SUMS.txt
```

The executable writes `summary.json` plus six flat CSV tables. Exact formulas
are tested independently of the generated tables; numerical work uses fixed
binary64 arithmetic and a fixed random seed.

## Route-A interpretation

`A0_ANALYTIC_ARITHMETIC_ORIGIN` and `A1_PASS_ANALYTIC` survive: the
tensor-prime symbolic atoms and positive all-repetition ledger are intrinsic.
`A2_ANALYTIC_DETERMINANT` also survives, but the determinant is identically the
unmodified Euler object and contains no visible Haar mechanism. Therefore A3
and A4 fail and the overall verdict is `ROUTE_A_REJECTED` for SD-C14 as a new
mechanism.
