# HCS-C46 — Fractional Divisor Obstruction for the Normalized Hénon Root

HCS-C45 constructs a canonical normalized Galois-norm Euler germ on
\(\operatorname{Re}s>1/2\).  This project asks whether its local factors are
ordinary rational determinant ratios.

The first split prime decides the question.  At \(p=7\), with
\(d_7=[\mathbf Q(\zeta_7)^+:\mathbf Q]=3\), the exact norm is

\[
N_7(z)=\frac{P_{18}(z)^2}{49P_{12}(z)^2},
\]

where \(P_{18}\) and \(P_{12}\) are squarefree and coprime over \(\mathbf Q\).
Every zero and pole therefore has order \(\pm2\), not divisible by three.
Consequently \(N_7\) is not a cube and

\[
G_7(z)=N_7(z)^{1/3}
\]

has local branch orders \(\pm2/3\).

## Decision

`STOP_ORDINARY_DETERMINANT_PROMOTION` is a theorem.  The C45 half-plane germ
remains valid, but it cannot be realized by an ordinary finite-dimensional
rational local determinant and cannot cross the certified unit-circle local
divisor as a single-valued meromorphic scalar function.

This does not rule out a normalized-trace or von Neumann algebra determinant.
HCS-C47 tests that operator category directly.

## Route A

\[
(\mathrm{A1\_WEAK},
 \mathrm{A2\_ANALYTIC\_DETERMINANT},
 \mathrm{A3\_FAIL},
 \mathrm{A4\_NATURAL\_QUANTIZATION}).
\]

The A2 label refers to the surviving C45 analytic germ; A3 fails for its
ordinary single-valued determinant promotion.  Route B is not authorized.

