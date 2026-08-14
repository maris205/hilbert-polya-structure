# DERIVATION PACKAGE — SD-C21

## 1. From full shifts to arithmetic instructions

For (F_n=A_n^{\mathbb Z}), alphabet cardinality gives

\[
|A_m\times A_n|=mn,\qquad |A_m\sqcup A_n|=m+n.
\]

Hence the operations (\boxtimes) and (\boxplus) reproduce multiplication
and addition on the chosen conjugacy classes.  Entropy supplies the norm:

\[
h(F_m\boxtimes F_n)=h(F_m)+h(F_n)=\log(mn).
\]

The additive order is not numerical data added from outside.  It is
expressed by existence of an alphabet-sum complement.  In the executable
graph, successor states expose the needed witnesses.

## 2. Why the quotient states matter

The tempting macro

\[
T_{n,d}\to R_{n,1}\quad\Longleftrightarrow\quad d\mid n
\]

hides the full factor predicate in one edge.  The frozen graph instead
constructs

\[
F_d\boxtimes F_2, F_d\boxtimes F_3,ldots
\]

and compares each object with (F_n) under alphabet-sum order.  The first
equality proves a cofactor; the first strict overshoot proves that this (d)
does not divide (n).  Thus the computation is local and terminating, even
though its accepted support is extensionally the prime set.

## 3. Rank-one nuclear decomposition

For each edge (e:u\to v), define

\[
E_e(s)=e^{-s\tau(e)}|\delta_v\rangle\langle\delta_u|.
\]

Then

\[
L_s=\sum_{e\in E(G)}E_e(s),\qquad
\|E_e(s)\|_1=e^{-\sigma\tau(e)}.
\]

The complete edge sum is dominated by

\[
\begin{aligned}
&\sum_p p^{-\sigma}
+\sum_{n\ge2}(2n)^{-\sigma}\\
&\quad+C\sum_{n\ge2}n^{-\sigma}\sum_{d\ge2}d^{-\sigma}
+\sum_{n\ge2}n^{-\sigma}
   \sum_{d\ge2}d^{-\sigma}\sum_{q\ge2}q^{-\sigma}\\
&\quad+\sum_{n\ge2}n^{-\sigma}\sum_{j\ge2}j^{-\sigma},
\end{aligned}
\]

which is finite exactly on the frozen half-plane (\sigma>1).  This is a
sufficient (\mathcal S_1) estimate, not a sharp asymptotic for the number of
verifier states.

## 4. Closed walks and traces

For a trace-class weighted adjacency,

\[
\operatorname{Tr}L_s^r
=\sum_{v\in V(G)}\langle L_s^r\delta_v,\delta_v\rangle.
\]

Each diagonal coefficient is a sum over length-(r) closed walks rooted at
(v).  The graph census leaves only (A_p\to A_p).  Therefore

\[
\operatorname{Tr}L_s^r=\sum_p(p^{-s})^r.
\]

The temporal exponent (r) is automatic.  It is neither an external
prime-power table nor a post-hoc coordinate assignment.

## 5. Fredholm determinant

For small (z),

\[
\det(I-zL_s)
=\exp\left(-\sum_{r\ge1}\frac{z^r}{r}
\operatorname{Tr}L_s^r\right).
\]

Substituting the trace ledger and using absolute convergence yields

\[
\begin{aligned}
\det(I-zL_s)
&=\exp\left(-\sum_p\sum_{r\ge1}
\frac{(zp^{-s})^r}{r}\right)\\
&=\exp\left(\sum_p\log(1-zp^{-s})\right)
=\prod_p(1-zp^{-s}).
\end{aligned}
\]

Normal convergence and Fredholm entireness extend this equality to all
(z\in\mathbb C) for each fixed (\operatorname{Re}s>1).

## 6. The pruning calculation

With accepted states first,

\[
L_s=\begin{pmatrix}D_s&B_s\\0&Q_s\end{pmatrix}.
\]

No path in (Q_s) closes, so (\operatorname{Tr}Q_s^r=0).  Therefore

\[
\det(I-zQ_s)
=\exp\left(-\sum_{r\ge1}\frac{z^r}{r}
\operatorname{Tr}Q_s^r\right)=1
\]

near zero, hence everywhere.  This proves both facts that must be kept
together:

1. the whole graph supports one legitimate trace-class determinant;
2. that determinant is unchanged when the entire verifier is deleted.

## 7. Graph-step versus first-return markers

An (\ell)-edge cycle with total edge weight (w) contributes

\[
1-z^\ell w.
\]

First-return contraction to a single loop of weight (w) gives (1-zw),
which is not the same marked determinant.  At (z=1), both give (1-w).
For a full (z)-comparison, the contracted loop must carry the composite
marker (z^\ell).  In SD-C21 all accepted cycles already have (\ell=1),
so no ambiguity affects the main identity.

## 8. Universal runtime damping

For a total decider with runtime (T(n)), configuration chains can be
arbitrarily long.  The time factor avoids any complexity assumption:

\[
\sum_{t=0}^{T(n)}[n(t+2)]^{-\sigma}
\le n^{-\sigma}\sum_{j\ge2}j^{-\sigma}.
\]

Summing over (n) gives a product of two convergent Dirichlet series.  Thus
even a very slow total decider compiles its support.  This derivation is the
strongest reason the Euler determinant alone cannot certify arithmetic
selectivity.

## 9. Polynomial UFD check

Let (I_q(d)) count monic irreducibles of degree (d).  Unique
factorization gives the formal identity

\[
\prod_{d\ge1}(1-u^d)^{-I_q(d)}
=\sum_{r\ge0}q^ru^r=\frac1{1-qu}.
\]

At (u=q^{-s}), the compiled determinant is (1-q^{1-s}).  The exact
(q=2) audit found

\[
I_2(1),\ldots,I_2(8)=(2,1,2,3,6,9,18,30)
\]

and reconstructed coefficients (1,2,4,\ldots,256).  This is a clean
factorial-monoid collision with the same compiler logic.

## 10. What the formulas do not derive

The identity is proved only for (\operatorname{Re}s>1).  Replacing the
right-hand side by the known analytic continuation of (1/\zeta(s)) does
not continue (L_s), construct a completed determinant, or produce a
functional equation.  No self-adjoint, unitary, scattering, or Hamiltonian
operator is derived.  Those omissions determine A3 and A4.
