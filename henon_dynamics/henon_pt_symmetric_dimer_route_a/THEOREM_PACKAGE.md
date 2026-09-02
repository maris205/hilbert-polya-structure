# Exact theorem and proof package — C297

Frozen obstruction identifier: `HEN-O281`.

Let `kappa>0`, `gamma` be real, and

\[
 H=\begin{pmatrix}i\gamma&\kappa\\ \kappa&-i\gamma\end{pmatrix},
 \qquad i\dot\psi=H\psi,
 \qquad \delta=\kappa^2-\gamma^2.
\]

## Theorem 1 — exact three-chamber flow

One has `H^2=delta I`.  Hence

\[
e^{-itH}=\begin{cases}
\cos(\omega t)I-i\dfrac{\sin(\omega t)}{\omega}H,
 &\delta>0,\quad\omega=\sqrt\delta,\\[5pt]
I-itH,&\delta=0,\\[5pt]
\cosh(\nu t)I-i\dfrac{\sinh(\nu t)}{\nu}H,
 &\delta<0,\quad\nu=\sqrt{-\delta}.
\end{cases}
\]

For `delta>0`, `H` has the distinct real eigenvalues `+omega,-omega`.
Every ray with nonzero components in both eigenlines has least projective
period `pi/omega`; the corresponding vector has least period `2pi/omega`.
The two eigenrays are stationary.

For `delta=0`, `H` is nonzero, rank one, and nilpotent.  Its kernel is its
unique eigenline.  If `H psi_0` is nonzero, then
`psi(t)=psi_0-itH psi_0` has linear leading growth.

For `delta<0`, the eigenvalues are `+i nu,-i nu`.  Under `e^{-itH}` their
eigenmodes scale as `e^{nu t}` and `e^{-nu t}`.  The growing eigenray attracts
every forward ray having a nonzero growing component; the other eigenray is
repelling.

### Proof

Direct multiplication gives `H^2=delta I`.  Separating even and odd terms in
the exponential series gives all three displayed formulae, including the
nilpotent case without a singular limit.  The spectral statements then
follow from the roots of `lambda^2-delta`.  In the unbroken eigenbasis, a
generic projective ratio is multiplied by `exp(2 i omega t)`, which gives the
stated least ray period; equality of both vector phases first occurs after a
full `2pi` turn.  In the broken eigenbasis the same ratio is multiplied by
`exp(-2 nu t)`, proving the attracting/repelling assertions.

## Theorem 2 — projective Riccati atlas

On the chart `psi_1` nonzero, set `z=psi_2/psi_1`.  Then

\[
 \dot z=i\kappa(z^2-1)-2\gamma z.
\]

Its complex quadratic discriminant is `-4 delta`.  It has two distinct fixed
rays off the exceptional sheets and one double fixed ray on them.  The chart
at infinity supplies the same global field on `CP^1`; no physical ray is
lost when `psi_1=0`.

### Proof

The vector equation gives
`dot psi_1=gamma psi_1-i kappa psi_2` and
`dot psi_2=-i kappa psi_1-gamma psi_2`.  The quotient rule yields the Riccati
equation.  Its fixed points are exactly eigenvectors with first coordinate
nonzero; the reciprocal chart covers the remaining point.  The discriminant
and Theorem 1 give the multiplicity and stability classification.

## Theorem 3 — conserved metrics and the sharp positivity boundary

With the Pauli matrices `sigma_x,sigma_y`, define

\[
 Q=\sigma_x,
 \qquad \eta=I+\frac{\gamma}{\kappa}\sigma_y.
\]

Both obey `H^dagger Q=QH` and `H^dagger eta=eta H`; consequently
`psi^dagger Q psi` and `psi^dagger eta psi` are conserved.  The eigenvalues
of `eta` are `1+|gamma|/kappa` and `1-|gamma|/kappa`.  Therefore `eta` is
positive definite exactly for `|gamma|<kappa`, positive semidefinite and
singular at equality, and indefinite in the broken chamber.  The standard
norm instead satisfies

\[
 \frac{d}{dt}\|\psi\|^2=2\gamma\,\psi^\dagger\sigma_z\psi,
\]

so it is not generally conserved.

### Proof

All identities follow by two-by-two matrix multiplication.  Conservation is
the derivative identity
`d_t(psi^dagger M psi)=i psi^dagger(H^dagger M-MH)psi`.  The two eigenvalues
of `eta` give the exact signature boundary.

## Boundary and claim status

At `gamma=0` the system is Hermitian.  The limit `kappa→0` with nonzero
`gamma` is an uncoupled gain/loss pair and has no positive `eta` of the
displayed normalized form.  At `(kappa,gamma)=(0,0)`, outside the frozen
domain, `H=0` and every state is fixed; it is not an exceptional point.  The
zero vector is a vector solution but not a projective state.

The theorem is **PROVABLE AS STATED**.  Its strict Route-A tuple is

```text
(A0_FAIL,A1_WEAK,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)
overall = ROUTE_A_REJECTED
```

The finite-dimensional pseudo-Hermitian metric is not a Hilbert--Pólya
operator.  No target arithmetic data, Euler factor, root number, automorphy,
target zero match, or Route-B input occurs.
