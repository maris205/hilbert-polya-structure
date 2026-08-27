# Source audit

## Primary record

Kenneth S. Brown and Persi Diaconis, “Random Walk and Hyperplane
Arrangements,” *The Annals of Probability* **26**(4), 1813--1854 (1998),
DOI `10.1214/aop/1022855884`.

The title, authors, journal, volume, issue, pages, year, and DOI were checked
against the published record and the author-hosted paper.  This is the sole
owner source for the all-family theorem package.

## Claim-to-locator ledger

| Claim used by C192 | Source locator | Boundary |
|---|---|---|
| diagonalizability, `lambda_W`, `|mu(W,V)|` multiplicity | Theorem 1 | repeated numeric eigenvalues are aggregated, not treated as distinct |
| separating iff unique stationary; without-replacement sampler; hyperplane mixing bound | Theorem 2 | no reversibility or self-adjointness imported |
| stationary-process infinite-product coupling | Theorem 3 | convergence/coupling theorem, not strict-SST independence |
| exact Möbius nonchamber probability and nonseparating component simplex | Section 4B, equations (4.3)--(4.6) and following remarks | no uniform sharpness claim |
| oriented-matroid extension | Section 6 | only the extension explicitly stated there |

The characteristic polynomial, `det(I-zK)`, and trace formulas are immediate
finite-dimensional consequences of Theorem 1.  C192 owns those deductions and
does not rebrand the underlying diagonalization theorem.

## Strong-stationarity terminology audit

The source gives two exact sampling descriptions: weighted sampling without
replacement and with-replacement sampling stopped when the product is a
chamber.  The coupling proof bounds total variation by the probability that the
partial product is not yet a chamber.  It does not assert that the stopped
chamber is independent of the stopping time, which is an additional condition
in the strict definition of a strong stationary time.  Unequal-weight Tsetlin
examples show why this distinction matters.  Every C192 artifact therefore uses
“stationary stopping sampler” or “coupling time,” never an unqualified strict
SST claim.

## Code-evidence boundary

The producer and two independent oracles enumerate only small coordinate and
braid arrangements.  They test sign products, flat lattices, Möbius recursion,
exact rational matrices, stationary equations, and symbolic characteristic
data.  These computations are regression evidence; they neither establish the
all-arrangement theorem nor support a priority claim.
