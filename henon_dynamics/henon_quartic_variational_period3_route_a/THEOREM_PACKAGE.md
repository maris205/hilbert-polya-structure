# Exact theorem package — C120

Let

\[
V(q)=\frac{q^4}{4}-q^2,\qquad F(q,p)=(V'(q)-p,q),
\qquad R(q,p)=(p,q).
\]

## Proposition 1 — exact reversible variational structure

The Jacobian

\[
B(q)=\begin{pmatrix}3q^2-2&-1\\1&0\end{pmatrix}
\]

has determinant one. Moreover,

\[
F^{-1}(Q,P)=(P,P^3-2P-Q),\qquad RFR=F^{-1}.
\]

For `S(q,Q)=qQ-V(q)`, the convention `p=-S_q`, `P=S_Q` yields
`Q=V'(q)-p` and `P=q`, hence exactly recovers `F`.

## Proposition 2 — fixed and primitive period-three witnesses

The fixed equation is `q(q-2)(q+2)=0`, giving phase-space fixed points
`(0,0)`, `(2,2)`, and `(-2,-2)`. The distinct states

\[
x_0=(0,-1),\quad x_1=(1,0),\quad x_2=(-1,1)
\]

satisfy `F(x_i)=x_{i+1 mod 3}` and therefore form a primitive three-cycle.

## Proposition 3 — parabolic chronological monodromy

Along the cycle, chronological differentiation gives

\[
M=B(-1)B(1)B(0)=
\begin{pmatrix}-1&0\\-3&-1\end{pmatrix}.
\]

Thus `tr M=-2`, `det M=1`, and

\[
\det(I-zM)=1+2z+z^2=(1+z)^2.
\]

The repeated multiplier `-1` is recorded only as finite tangent data.

## Proposition 4 — action and Morse certificate

For cyclic indices, define

\[
\mathcal A(q_0,q_1,q_2)=\sum_{i=0}^2
  \bigl(q_iq_{i+1}-V(q_i)\bigr).
\]

At `(0,1,-1)`, its gradient vanishes, its value is `1/2`, and

\[
D^2\mathcal A=
\begin{pmatrix}2&1&1\\1&-1&1\\1&1&-1\end{pmatrix}.
\]

The determinant is `4` and the characteristic polynomial is
`(lambda+2)(lambda^2-2lambda-2)`. The eigenvalues are
`-2, 1-sqrt(3), 1+sqrt(3)`, so the critical point is nondegenerate with Morse
index two.

## Controls and boundary

At nearby `alpha=5/2`, the transition from `(1,0)` misses `(-1,1)` by
`(-1/2,0)`. Deleting the cubic term misses it by `(-1,0)`. Replacing the
last state by `(0,1)` also fails the cyclic transition. These controls rule
out parameter- or word-agnostic attribution.

The structural propositions are exact, but the canonical evaluator tuple is
`(A1_WEAK, A2_FAIL, A3_FAIL, A4_FORMAL_HINT)`. There is no target prime
correspondence, source-owned dynamical zeta/Fredholm object, target divisor,
or global analytic structure. The generating and reversing structure is only
a formal liftability hint; no quantum object, Hilbert space, or operator
domain is supplied, and this is not a Route-B result.
