# HCS-C52 code/results summary

Status: `RELEASE_CANDIDATE`.

This release certifies only blocks B0--B2.  It does not contain a
rank-two projector outside the rational graph algebra, a local Frobenius
polynomial, or an incidence correspondence.

## Exact result

For

\[
X:\ \sum_{i=0}^7x_i^3=0,\qquad
\sum_{i=0}^6x_ix_{i+1}+\rho x_7x_0=0
\]

over \(K=\mathbf Q(\rho)\), the visible projective monomial symmetry group is
the order-24 dihedral group \(D_{12}\).  The exact element-order histogram is

```text
1:1, 2:13, 3:2, 4:2, 6:2, 12:4.
```

The Cayley--Jacobian piece \(R_{2,-3}\) has 164 ambient monomials, 82
displayed Jacobian relations of exact \(\mathbf Q(\rho)\)-rank 81, and
quotient dimension 83.  For generators
\(r^{12}=s^2=1\), \(srs=r^{-1}\), its character is

\[
\operatorname{Tr}(r^k)=
(83,-1,-3,-1,-7,-1,3,-1,-7,-1,-3,-1),
\quad
\operatorname{Tr}(sr^k)=3.
\]

The one-dimensional multiplicities are \((4,1,3,3)\), and the
two-dimensional multiplicities are \((7,8,6,8,7)\).  The extreme
\(H^{4,1}\) line is trivial, while the trivial representation occurs four
times in \(H^{3,2}\).

Let

\[
\pi_{2i}=\frac16h^{5-i}\times h^i,\qquad
\pi_5=\Delta_X-\sum_{i=0}^5\pi_{2i},\qquad
e_G=\frac1{24}\sum_{g\in G}[\Gamma_g].
\]

The certified middle projectors are

\[
\pi_{\rm core}=\pi_5e_G,
\qquad
\pi_{\rm lev}=\pi_5-\pi_{\rm core}.
\]

They give the same split in Betti, de Rham, and every \(\ell\)-adic
realization:

| summand | rank | normalized Hodge multiplicities |
|---|---:|---|
| core after one Tate twist | 10 | \((1,4,4,1)\) |
| complement after the C51 twist by two | 158 | \((0,79,79,0)\) |

The raw Reynolds projector is never assigned middle rank 10 before applying
\(\pi_5\).

## Exact scoped obstruction

Every element of \(\mathbf Q[G]\) acts on every trivial copy by its
augmentation.  Hence an idempotent that retains \(H^{4,1}\) also retains all
four trivial \(H^{3,2}\) copies and their conjugates.  The smallest such
rational Hodge rank inside the graph algebra is 10, so a rank-two projector
inside \(\mathbf Q[G]\) is refuted.

This does **not** rule out a rank-two projector in the full Chow
correspondence ring.  Rank-10 Frobenius polynomials and additional incidence
correspondences are explicitly deferred to C53.

## Reproduction

From the project directory:

```bash
./code/run_c52.sh
```

The default runner regenerates the certificate in a temporary directory,
runs the independent checker and all mutation tests, compares the temporary
artifacts byte-for-byte with the frozen results, and verifies the
full-project release manifest.
