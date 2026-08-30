# HCS-C246 — Linear-rate AIMD perpetuity and occupation law

We freeze the hybrid process

\[
 \dot X_t=a>0,\qquad \text{jump rate }rho X_t,qquad X_t\mapstobeta X_t,
 \quad 0<beta<1.
\]

For the pre-jump value (Y_n), the integrated hazard gives the exact chain

\[
Y_{n+1}^{2}=beta^{2}Y_n^{2}+\frac{2a}{rho}E_{n+1},
\qquad E_{n+1}\sim\mathrm{Exp}(1).
\]

Thus (Z_n=Y_n^2) is a contractive affine perpetuity with stationary Laplace
product
(prod_{j\ge0}(1+(2a/rho)beta^{2j}s)^{-1}).  The release also records
the exact generator moment recurrence, a stationary Markov-renewal/Palm
occupation formula, the continuous stationary Laplace-generator identity
\(\varphi'(s)-\varphi'(beta s)=(a/rho)s\varphi(s)\), and a rational deterministic hazard skeleton.  For
(beta>0) the embedded chain is Markov and is not iid regenerative; only the
(beta=0) reset face has iid regeneration.  On this face the pre-jump law is
Rayleigh, with (f_Y(y)=(rho/a)y e^{-rho y^2/(2a)}), while continuous time
has the half-normal density (f_X(x)=\sqrt{2rho/(pi a)}e^{-rho x^2/(2a)})
and mean (\sqrt{2a/(pi rho)}).

The producer and independent checker cover (3^3=27) rational parameter
tuples (beta\in\{1/2,2/3,3/4\}), (a\in\{1/2,1,3/2\}),
(rho\in\{1/2,1,2\}), moment orders 0--8, a 12-term q-product prefix,
and six exact reward-skeleton steps.  The strict scope is
`NO_BAD_EULER_OR_ROOT_NUMBER`; the q-product is source-local Laplace data,
never an Euler factor or target determinant.  Route B is disabled and the
tuple is `(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`.

The 28-file release is locked to source/code baseline
`5f357e2d2b78604f6c286bfbd05da922e1d6791f`, evaluator SHA
`6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`, date
`2026-08-30`, and fixed epoch `1788048000`.

Run the audit from this directory:

```text
PYTHONDONTWRITEBYTECODE=1 python3 -B code/c246_tcp_aimd_producer.py
PYTHONDONTWRITEBYTECODE=1 python3 -B code/c246_tcp_aimd_checker.py
PYTHONDONTWRITEBYTECODE=1 python3 -B code/c246_tcp_aimd_sympy_crosscheck.py
PYTHONDONTWRITEBYTECODE=1 python3 -B code/c246_tcp_aimd_replay.py
PYTHONDONTWRITEBYTECODE=1 python3 -B code/c246_tcp_aimd_mutation.py
PYTHONDONTWRITEBYTECODE=1 python3 -B code/c246_release_manifest.py
```
