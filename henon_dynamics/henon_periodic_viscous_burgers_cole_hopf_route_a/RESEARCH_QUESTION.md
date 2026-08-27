# Research question and frozen source object

## Question

For every viscosity \(\nu>0\), circumference \(L>0\), mean \(m\in\mathbb R\), and
Sobolev exponent \(s>3/2\), can one give a single all-parameter description of the
periodic viscous-Burgers semiflow on

\[
X_m^s=\left\{u\in H^s(\mathbb T_L;\mathbb R):
  L^{-1}\int_{\mathbb T_L}u\,dx=m\right\},
\]

including its global coordinates, recurrence set, sharp leading decay, and full
linearized spectrum, without confusing a finite regression census with proof?

## Frozen answer

Yes. Put

\[
\mathbb P^{s+1}_+=
\{w\in H^{s+1}(\mathbb T_L;\mathbb R):\min w>0\}/\mathbb R_{>0}
\]

and \(\Phi_m([w])=m-2\nu\partial_x\log w\). This is a bijection onto \(X_m^s\).
In fixed physical coordinates it conjugates Burgers to

\[
K_t=\exp\!\left[t(\nu\partial_x^2-m\partial_x)\right]
\]

on the positive projective cone. Under the Galilean variable \(y=x-mt\), this is
the ordinary heat semigroup. The theorem package proves the resulting global phase
portrait and exact Fourier asymptotics for the whole parameter family.

## Clock and normalization lock

- Clock: source physical time \(t\), with no time change.
- Fourier wave number: \(\kappa_k=2\pi k/L\).
- Drift sign: \(K_t w(x)=(e^{\nu t\partial_x^2}w)(x-mt)\).
- Cole--Hopf sign: \(u=m-2\nu\partial_x\log w\).
- Linearized eigenvalue: \(-\nu\kappa_k^2-i m\kappa_k\).

No arithmetic labels, target zero/prime tables, Euler factors, root numbers,
automorphy assertions, or Hilbert--Pólya claims enter the question.
