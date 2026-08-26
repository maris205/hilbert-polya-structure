# HCS-C178: all-angle harmonic strobe and same-clock quantization

This package gives one exact classical--Koopman--quantum ledger for the
unit-frequency planar oscillator

\[
H(q,p)=\frac{q^2+p^2}{2},\qquad T_\theta=\Phi_\theta .
\]

The common parameter is physical real time \(\theta\in\mathbb R\).
Classically, \(T_{\theta+2\pi}=T_\theta\), and the Gaussian Koopman family
has the same \(2\pi\) period.  The quantum family is not descended to that
quotient: \(Q_{\theta+2\pi}=-Q_\theta\) and
\(Q_{\theta+4\pi}=Q_\theta\).

At irrational \(\theta/(2\pi)\), every positive iterate fixes only the
origin and the classical Artin--Mazur zeta is \((1-z)^{-1}\).  At a reduced
rational angle \(2\pi a/b\), every \(b\)-th iterate fixes the whole plane,
so the classical cardinality series is undefined.  The invariant-Gaussian
Koopman unitary has an exact Laguerre--angular basis with eigenvalues
\(e^{im\theta}\) and infinite radial multiplicity.  The same physical clock
also defines the natural quantum oscillator propagator with Hermite phases
\(e^{-i\theta(j+1/2)}\), exact Egorov covariance, and the retained
metaplectic global sign.  Both unitary lifts are
noncompact, outside every finite Schatten class, and lack an ordinary
trace-class Fredholm determinant.

Route-A verdict:

`(A0_FAIL, A1_FAIL, A2_FAIL, A3_FAIL, A4_NATURAL_QUANTIZATION)`;
overall `ROUTE_A_REJECTED`; Route B remains unauthorized.  The natural
quantization does not repair A0--A3.

## Reproduce

```bash
python3 code/c178_harmonic_strobe_producer.py
python3 code/c178_harmonic_strobe_checker.py
python3 code/c178_sympy_crosscheck.py
python3 code/c178_replay.py
python3 code/c178_mutation.py
python3 code/c178_release_manifest.py
```

The paper is `paper/main.pdf`.  The release has 27 content-addressed payload
files plus the self-excluded manifest.  The common scope is
`NO_BAD_EULER_OR_ROOT_NUMBER`.
