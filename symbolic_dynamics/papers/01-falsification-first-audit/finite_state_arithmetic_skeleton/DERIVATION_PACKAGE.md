# Derivation Package: Finite-State Determinants

## 1. Problem Setup and Target Quantity

Let \(G=(V,E)\) be a finite directed multigraph.  Each edge \(e\) carries

\[
\tau_e>0,\qquad w_e\in\mathbb C,\qquad U_e\in U(d).
\]

The roof, scalar weight, and cocycle are locally constant.  On
\(\mathbb C^V\otimes\mathbb C^d\), define

\[
M(s)_{uv}=\sum_{e:u\to v}w_e e^{-s\tau_e}U_e,\qquad
D(s)=\det(I-M(s)).
\]

The target quantities are the primitive-orbit Euler ledger and the global
zero-count growth of \(D\).

## 2. Assumptions and Modeling Choices

1. \(V,E\), and \(d\) are finite.
2. Roofs are positive and take only the edge values \(\tau_e\).
3. Weights and cocycles are fixed before target inspection.
4. \(D\not\equiv0\); the identically singular case is not a divisor candidate.
5. The theorem does not cover an infinite-memory Hölder potential merely
   coded over a finite alphabet.

## 3. Notation

For a closed edge path \(\gamma=e_1\cdots e_n\), write

\[
T_\gamma=\sum_j\tau_{e_j},\quad
w_\gamma=\prod_jw_{e_j},\quad
U_\gamma=\prod_jU_{e_j}.
\]

Primitive cyclic paths are denoted by \([\gamma]\).

## 4. Derivation

In a right half-plane where \(\rho(M(s))<1\),

\[
-\log\det(I-M(s))
=\sum_{n\ge1}\frac{\operatorname{Tr}M(s)^n}{n}.
\]

Expanding the trace enumerates based closed paths of length \(n\).  Regrouping
each path as a repetition of a primitive cyclic path gives

\[
\begin{aligned}
Z(s)
&:=D(s)^{-1}\\
&=\exp\left(
  \sum_{[\gamma]\ {\rm primitive}}\sum_{r\ge1}
  \frac{w_\gamma^r e^{-srT_\gamma}
  \operatorname{tr}(U_\gamma^r)}{r}
  \right)\\
&=\prod_{[\gamma]\ {\rm primitive}}
  \det\!\left(I-w_\gamma e^{-sT_\gamma}U_\gamma\right)^{-1}.
\end{aligned}
\]

The determinant expansion of a finite block matrix contains finitely many
products of entries.  Hence

\[
D(s)=\sum_{j=1}^{K}a_j e^{-\lambda_js},
\qquad \lambda_j\ge0,
\]

after collecting equal exponents.  Thus \(D\) is an entire exponential
polynomial.  If every \(\tau_e\in h\mathbb N\), then

\[
D(s)=P(e^{-hs})
\]

for a polynomial \(P\), so every nonzero root of \(P\) lifts to a vertical
arithmetic progression of period \(2\pi i/h\).

For the full \(q\)-shift, \(\#\operatorname{Fix}(\sigma^n)=q^n\), and therefore

\[
\zeta_\sigma(z)
=\exp\left(\sum_{n\ge1}\frac{q^nz^n}{n}\right)
=\frac1{1-qz}.
\]

Putting \(z=q^{-s}\) yields \(D_q(s)=1-q^{1-s}\).  Möbius inversion gives the
primitive necklace count

\[
N_q(n)=\frac1n\sum_{d\mid n}\mu(d)q^{n/d}.
\]

This equals the number of monic irreducible polynomials of degree \(n\) over
\(\mathbb F_q\).  Consequently

\[
\prod_{P\ {\rm monic\ irreducible}}
\left(1-|P|^{-s}\right)^{-1}
=\frac1{1-q^{1-s}},
\qquad |P|=q^{\deg P}.
\]

The equality is exact at the count and repetition-ledger level.  It does not
identify rational primes with individual shift orbits.

## 5. Main Result

**PROVED.** Every nonzero finite-state, finite-memory, finite-dimensional
twisted determinant above has disk zero count \(n_D(R)=O(R)\).  Hence no finite
product or quotient of such determinants can have the completed Riemann
divisor, whose count is \(\Theta(R\log R)\).

## 6. Interpretation

Finite symbolic memory solves the orbit-accounting problem cleanly.  Its
analytic rigidity is also the obstruction: finite-dimensional twists change
coefficients and phases, not the exponential type or divisor-growth order.

## 7. Scope and Limitations

The result does not rule out countable-state systems, infinite-memory
potentials, operator-valued weights, or infinite-dimensional transfer
operators.  Any such escape must be evaluated as a new frozen candidate and
must pass A0 independently.
