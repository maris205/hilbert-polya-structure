# C178 exact results

## Claim-bearing results

- Physical time is \(\theta\in\mathbb R\), with
  \(T_\theta^n=R_{n\theta}\) and
  \(T_{\theta+2\pi}=T_\theta\) for every positive iterate.
- Irrational \(\theta/(2\pi)\) gives
  \(\operatorname{Fix}(T_\theta^n)=\{0\}\) and
  \(\zeta_{\rm AM}(z)=(1-z)^{-1}\) for all \(n\ge1\).
- Reduced rational \(\theta/(2\pi)=a/b\) gives the whole plane as the fixed
  set exactly when \(b\mid n\); the classical Artin--Mazur series is then
  undefined.
- The Gaussian Koopman basis is the normalized Laguerre--angular basis, with
  phase \(e^{im\theta}\) and infinite radial multiplicity.
- Irrational angles have a dense pure-point eigenvalue set; rational angles
  have the \(b\)-th roots, all with infinite multiplicity.
- \(S(q,p)=(q,-p)\) reverses the classical and Gaussian Koopman clocks.
- The natural quantum oscillator uses the same \(\theta\), has Hermite phase
  \(e^{-i\theta(j+1/2)}\), exact Egorov rotation, and conjugation reversal.
- The quantum lift is not single-valued on the classical time quotient:
  \(Q_{\theta+2\pi}=-Q_\theta\) and
  \(Q_{\theta+4\pi}=Q_\theta\).  For exact rational real time
  \(\theta/(2\pi)=a/b\), its spectrum is \(e^{-i\pi a/b}\) times the
  \(b\)-th roots; the global sign is never discarded.
- Both unitary lifts are noncompact, in no finite Schatten class, and have no
  ordinary trace-class Fredholm determinant.
- Heat/Wick evolution is a different clock and is not used as a repair.

## Deterministic validation

- Canonical evidence payload SHA-256:
  `91b74dc7381ff6b7ceea0792ae4d03c4d8f58727e0f406660bb9111f027ef4e9`.
- Released evidence-file SHA-256:
  `69087059465060c7c0b8536807d8192ff4db3c914e9ad1791474053ea35b12ba`.
- Producer-independent checker: 26,271 assertions; separate SymPy path:
  10,465 exact checks; hostile mutations: 64 repaired-hash plus one stale-hash
  mutation, all rejected.
- Released two-page PDF SHA-256:
  `936b9aa851d26114e4131a649460ad84e7522e7e6dbfa21907558810113d3fb3`.
- Finite sentinels: 1,656 rational fixed-set rows, 108 irrational rows, 209
  Laguerre rows, 874 Koopman phase rows, and 736 quantum phase rows.
- Byte replay is exact at 931,603 bytes.

## Route decision

`(A0_FAIL, A1_FAIL, A2_FAIL, A3_FAIL, A4_NATURAL_QUANTIZATION)`;
overall `ROUTE_A_REJECTED`; `route_b_invocation_allowed: false`.

The natural quantization is retained as source progress.  It cannot repair
the missing arithmetic origin, primitive target carrier, target determinant,
or global target analytic structure.
