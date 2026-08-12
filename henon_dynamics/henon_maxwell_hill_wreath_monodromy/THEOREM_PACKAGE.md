# Theorem package

## Locked setting

Let \(P_9\in\mathbb Z[A]\) and \(\beta\in K^\times\), with
\(K=\mathbb Q[A]/(P_9)\), be the exact C33 collision polynomial and
symmetric Maxwell--Hill product. Let \(L\) be the splitting field of
\(P_9\), label its roots \(\alpha_1,\ldots,\alpha_9\), and put
\(\beta_i=\beta(\alpha_i)\). C33 proves

\[
\operatorname{Gal}(L/\mathbb Q)=S_9
\]

and

\[
N:=N_{K/\mathbb Q}(\beta)
=\frac{2^6\,13\,19^5\,41\,59^5\,5653^2}{3^5}.
\]

## Theorem 1: the local pair-parity certificate

There is a discrete valuation \(v\) of \(L\) above \(19\) such that, after
labeling the conjugates suitably,

\[
(v(\beta_1),\ldots,v(\beta_9))\bmod2
=(1,1,0,0,0,0,0,0,0).
\]

### Proof certificate

With \(A=1802+T\), the coefficient valuations of \(P_9\) are
\((5,3,0,\ldots,0)\). The lower Newton edge from \((0,5)\) to \((2,0)\)
has slope \(-5/2\), denominator \(2\), and horizontal length \(2\). It
therefore gives one degree-two local cluster. The shifted numerator of
\(\beta\) has valuations \((3,0,\ldots,0)\), so its unit linear term gives
valuation \(5/2\) at each cluster root. In the integer normalization of
the ramified local field this is \(5\). Finally,

\[
\gcd(P_9,\operatorname{num}\beta)\bmod19=A+3,
\]

so the remaining seven values are units. The denominator of \(\beta\) is
a \(19\)-adic unit.

## Theorem 2: full Kummer rank

The nine classes \([\beta_i]\) are linearly independent in
\(L^\times/L^{\times2}\).

### Proof

Let

\[
R=\left\{r\in\mathbb F_2^9:
\prod_i\beta_i^{r_i}\in L^{\times2}\right\}.
\]

Every \(r\in R\) is orthogonal to the parity vector of Theorem 1. The
\(S_9\)-invariance of \(R\) and the full \(S_9\) Galois action imply

\[
r_i+r_j=0
\]

for every pair \(i\ne j\). Hence \(R\) is contained in the all-ones line.
The all-ones vector would assert that

\[
\prod_i\beta_i=N
\]

is a square in \(L\). But the square-free rational classes are

\[
[N]=3\cdot13\cdot19\cdot41\cdot59,
\qquad
[\operatorname{Disc}P_9]=13\cdot19\cdot41\cdot59.
\]

An \(S_9\)-extension has exactly one quadratic subfield, its sign field
\(\mathbb Q(\sqrt{\operatorname{Disc}P_9})\). Thus \(N\), which is neither
a rational square nor in the sign square class, cannot become a square in
\(L\). Therefore \(R=0\).

## Theorem 3: full wreath monodromy

Let

\[
M=L(\sqrt{\beta_1},\ldots,\sqrt{\beta_9}).
\]

Then

\[
\operatorname{Gal}(M/L)\cong C_2^9
\]

and

\[
\operatorname{Gal}(M/\mathbb Q)
\cong C_2\wr S_9=C_2^9\rtimes S_9.
\]

In particular, its order is

\[
2^9\,9!=185794560.
\]

### Proof

Theorem 2 and Kummer theory give the kernel over \(L\). The normal closure
of the quadratic extension \(K(\sqrt\beta)/K\) embeds into the quadratic
wreath product over the nine embeddings of \(K\). Restriction to \(L\)
has quotient \(S_9\). The embedded group therefore has order
\(2^9\,9!\), equal to the order of the ambient wreath product, and hence is
the full wreath product.

## Corollary: an irreducible degree-eighteen Hénon polynomial

The primitive integral form of

\[
F_{18}(U)=N_{K/\mathbb Q}(U^2-\beta)
\]

is irreducible over \(\mathbb Q\). The certificate independently proves
this by Rabin irreducibility modulo \(7\). Its roots form the natural
signed nine-point set for \(C_2\wr S_9\).

## Route-A decision

The theorem is a positive fixed-period arithmetic result, but it does not
construct a dynamical zeta, a prime correspondence, a critical-line
functional equation, or a self-adjoint operator. Therefore

\[
(A1\_\mathrm{WEAK},A2\_\mathrm{FAIL},A3\_\mathrm{FAIL},
A4\_\mathrm{FORMAL\_HINT})
\]

and the overall decision is `ROUTE_A_REJECTED`. Route B is not authorized.
