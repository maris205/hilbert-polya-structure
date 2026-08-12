# HCS-C34: full Maxwell--Hill wreath monodromy

HCS-C34 takes the exact period-five Hénon Maxwell node proved in C33 and
closes the one large arithmetic gate that C33 deliberately left open. If
\(L/\mathbb Q\) is the \(S_9\) splitting field of the collision polynomial
\(P_9\), and if

\[
\beta_1,\ldots,\beta_9\in L^\times
\]

are the conjugates of the symmetric two-branch Hill product
\(\beta=N_H\), then their square classes are linearly independent in
\(L^\times/L^{\times2}\). Consequently the normal closure

\[
M=L(\sqrt{\beta_1},\ldots,\sqrt{\beta_9})
\]

has the full possible Galois group

\[
\operatorname{Gal}(M/\mathbb Q)
\cong C_2^9\rtimes S_9=C_2\wr S_9,
\qquad |\operatorname{Gal}(M/\mathbb Q)|=185794560.
\]

## The decisive certificate

At \(p=19\), translate the parameter by

\[
A=1802+T=-3+5\cdot19^2+T.
\]

The coefficient valuations of \(P_9(1802+T)\), from low to high degree,
are

\[
(5,3,0,0,0,0,0,0,0,0).
\]

The lower Newton edge joins \((0,5)\) to \((2,0)\), so it isolates a
degree-two root cluster with slope \(-5/2\). The corresponding valuations
of the numerator of \(\beta(1802+T)\) are

\[
(3,0,0,0,0,0,0,0,0).
\]

Thus both cluster roots give odd normalized Hill valuation \(5\); all seven
other conjugates are units because

\[
\gcd(P_9,\operatorname{num}\beta)\bmod19=A+3.
\]

This supplies the parity functional \(e_1+e_2\). Its \(S_9\)-orbit
contains every \(e_i+e_j\), forcing every square relation to be either zero
or the all-ones relation. The latter is impossible: the square-free class
of the rational norm of \(\beta\) is

\[
3\cdot13\cdot19\cdot41\cdot59,
\]

whereas the unique sign quadratic subfield of the \(S_9\) splitting field
has class

\[
13\cdot19\cdot41\cdot59.
\]

## What is and is not new

Kummer theory, the quadratic wreath embedding, and the elementary
\(\mathbb F_2[S_9]\) argument are standard. The new result is the exact
Hénon-specific full-rank theorem: the intrinsic Hill decoration of the
period-five Maxwell collision attains the entire \(C_2^9\) base group.
This is distinct from symbolic monodromy in the complex Hénon horseshoe
locus and from C33's proof of only one nontrivial quadratic class.

This remains a fixed-period arithmetic theorem. It proves no all-period
Euler product, prime law, critical-line statement, or self-adjoint
Hilbert--Pólya operator. The formal evaluation is

\[
(A1\_\mathrm{WEAK},A2\_\mathrm{FAIL},A3\_\mathrm{FAIL},
A4\_\mathrm{FORMAL\_HINT}),
\qquad \texttt{ROUTE\_A\_REJECTED}.
\]

## Reproduction

~~~bash
./code/run_c34.sh
~~~

The runner rebuilds the exact certificate in a temporary directory,
independently checks nine gates, executes adversarial mutation tests, and
verifies the frozen hash manifest without modifying released results.

## Files

- `DERIVATION_PACKAGE.md` gives the complete formula-level argument.
- `THEOREM_PACKAGE.md` separates proved statements from corollaries and
  non-claims.
- `SOURCE_AUDIT.md` records the C33 lock and the literature boundary.
- `code/` contains independent producer/checker implementations and tests.
- `results/` contains the frozen certificate, checker report, and manifest.
- `paper/` contains the compiled research note.
