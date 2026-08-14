# HCS-P53 results

## Analytic result

For every primitive orbit \(\gamma\),

\[
\log|N\beta_{\gamma,n}|
=\frac{\varphi(n)}2\mathcal H_\gamma
+O_\gamma(\sqrt n(1+\log n)^2),
\qquad
\mathcal H_\gamma=\log M(f_{\lambda_\gamma}).
\]

For \(\Re s>\sigma_0\),

\[
\tau^2Z(s,\tau)\to
\frac3{\pi^2}\sum_\gamma
e^{-s\widehat\ell_\gamma}\mathcal H_\gamma
\]

locally uniformly.  The certified numerical half-plane is
\(\Re s>3.125206884004728\ldots\).

For real \(\sigma\) there, the joint orbit/index profile converges to the
pressure-height orbit law times \(\Gamma(2,1)\).  The tagged vector has no
norm- or weakly-convergent boundary subnet.

## Exact/high-precision sentinels

| object | source-native H6 | unit-circle conjugates | \(\mathcal H\) | final Abel ratio |
|---|---:|---:|---:|---:|
| period 1 | yes | 0 | 3.0501161905168335 | 0.998235304857352 |
| period 3 | yes | 0 | 8.905609291064076 | 0.9981948211638283 |
| period 4 | yes | 0 | 6.359570875399758 | 0.9981913241856065 |
| abstract Salem stress | no | 2 | 0.5435350724978696 | 1.003612954592687 |

The period-one physical logarithm is only
\(\log\Lambda_1=1.96734662909421\ldots\), so the physical-only mutation is
strictly false.

At the final three-orbit sample scale \(\tau=0.025\), the normalized Abel
ratio is `0.9982278165892107`.  The observed Laplace values at
\(r=0.5,1,2\) are respectively
`0.44348903051181876`, `0.24873019480776581` and
`0.1096556880333355`, approaching the exact Gamma targets
\(4/9,1/4,1/9\).

## Claim status

- all-orbit Abel exchange in safe half-plane: **PROVED**;
- joint pressure-height/Gamma boundary: **PROVED**;
- tagged vector boundary: **REFUTED**;
- pressure-critical continuation: **OPEN**;
- rational-prime trace, determinant and operator: **OPEN**.
