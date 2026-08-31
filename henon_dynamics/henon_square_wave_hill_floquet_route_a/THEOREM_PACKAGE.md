# Theorem package

Define the entire functions

\[
C(k,t)=\sum_{m\ge0}{(-k)^m t^{2m}\over(2m)!},\qquad
S(k,t)=\sum_{m\ge0}{(-k)^m t^{2m+1}\over(2m+1)!}.
\]

They satisfy `C_t=-kS`, `S_t=C`, and `C^2+kS^2=1`.  Hence

\[
\Phi(k,t)=\begin{pmatrix}C&S\\-kS&C\end{pmatrix}\in SL(2,\mathbb R)
\]

for every real `k`.  This is simultaneously the cosine/sine, shear, and
cosh/sinh transfer for positive, zero, and negative `k`.

## Complete Floquet--Jordan theorem

Let `M=Phi(k2,tau2) Phi(k1,tau1)`, `T=tau1+tau2>0`, and write `Cj,Sj` for the
two segments.  Then

\[
\Delta=\operatorname{tr}M
=2C_1C_2-(k_1+k_2)S_1S_2,qquad\det M=1.
\]

- `|Delta|<2`: conjugacy is elliptic and every solution is bounded.  The
  Floquet angle per time is `acos(Delta/2)/T`.
- `|Delta|>2`: the real reciprocal multiplier pair is hyperbolic.  Generic
  solutions grow exponentially, one forward eigenline decays, and the
  positive growth rate is `acosh(|Delta|/2)/T`.
- `Delta=+/-2`: if `M=+/-I`, every solution is periodic/antiperiodic over one
  coefficient period.  Otherwise `M` has a nontrivial Jordan block: exactly
  one Floquet eigenline stays bounded and generic solutions grow linearly
  (with alternating sign on the minus face).

Cayley--Hamilton gives, for every `n>=1`,

\[
M^n=U_{n-1}(\Delta/2)M-U_{n-2}(\Delta/2)I.
\]

Here `U_{-1}=0` and `U_0=1`, so the formula includes `n=1` without an
unstated negative-index convention.

The same formulas close `k_j=0`, `k_j<0`, `tau_j=0`, constant-coefficient
collapse, and segment-order swap.  The swapped product can differ, but its
trace and Floquet class agree by cyclicity.

This is not a theorem for arbitrary periodic coefficients or nonlinear
stability.  Continuous parameters provide no arithmetic owner or target
determinant.

```text
(A0_FAIL,A1_WEAK,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)
ROUTE_A_REJECTED; Route B false.
```

Scope: `NO_BAD_EULER_OR_ROOT_NUMBER`.
