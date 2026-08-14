# Fourier-Null Haar Fibers

Paper12 freezes **SD-C14**, an infinite-dimensional positive symbolic fiber
over tensor-prime atom loops.  Its visible spectral measure is allowed to
contain a Haar component whose positive Fourier moments vanish.  The sharp
classification is

```text
integral_T z^r dmu(z) = 1 for every r>=1
    iff
mu = delta_1 + c m_Haar,  c>=0.
```

Normalization or finite support forces `c=0`.  The nonnormalized Haar sector
therefore escapes finite moment rigidity but is invisible to the analytic
trace-log determinant.  Fuglede--Kadison magnitude can see it, while natural
self-adjointization erases its phase and recurrent coupling creates balanced
inverse-word mixed cycles.

The deterministic audit confirms the sharp boundaries: cyclic fibers of
orders `2..64` first leak at their order, all 64 Fourier-density perturbations
first leak at the preregistered mode, and the Fuglede--Kadison identity has
maximum quadrature residual `4.440892098500626e-16`.  Most decisively, the
three 128-atom prime/composite/random inventories at three Haar weights give
exactly zero analytic-determinant difference and phase range in all nine
controls.  This supports `PROVES_TOO_MUCH`, not a target-divisor claim.

The shareable paper is [main.pdf](main.pdf); exact experiment details are in
[EXPERIMENT_REPORT.md](EXPERIMENT_REPORT.md).

```text
(A0_ANALYTIC_ARITHMETIC_ORIGIN,
 A1_PASS_ANALYTIC,
 A2_ANALYTIC_DETERMINANT,
 A3_FAIL,
 A4_FAIL)

ROUTE_A_REJECTED
GO_INFINITE_HAAR_ESCAPE
STOP_DETERMINANT_INVISIBILITY
STOP_SCOPED / PROVES_TOO_MUCH
ROUTE_B_LOCKED
```
