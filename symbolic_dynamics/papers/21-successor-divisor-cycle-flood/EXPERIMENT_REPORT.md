# SD-C23 exact experiment report

## Outcome

The successor-divisor shift passes every internal exactness, same-object, and reproducibility gate, but it fails the desired prime-orbit ledger in the first marked coefficient. Its final Route tuple is

\[
(\mathrm{A0\_STRUCTURAL\_ARITHMETIC\_RELATION},
\mathrm{A1\_WEAK},
\mathrm{A2\_ANALYTIC\_DETERMINANT},
\mathrm{A3\_FAIL},
\mathrm{A4\_FAIL}),
\]

with overall verdict ROUTE_A_REJECTED and Route B locked.

## Exact trace census

Sparse propagation at the certified cutoff $2r-1$ produced every unweighted trace through $r=32$. Möbius inversion reconstructed each trace exactly from primitive counts.

| $r$ | rooted closed walks $T_r$ | primitive rotation classes $P_r$ |
|---:|---:|---:|
| 1 | 0 | 0 |
| 2 | 2 | 1 |
| 3 | 3 | 1 |
| 4 | 10 | 2 |
| 8 | 82 | 9 |
| 16 | 4,002 | 245 |
| 24 | 237,433 | 9,867 |
| 32 | 14,532,674 | 454,021 |

All 128 finite-cutoff flags agree with the exact rule $N\ge2r-1$. The explicit inventory contains 667 primitive directed rotation classes through length 16; reflections were not identified. Canonical cycles were checked for every length through 2048.

## Weighted trace and determinant ledger

For $s=1,2,3$, exact Fraction propagation generated 48 weighted traces through order 16. At $s=1$ the first values are

\[
\operatorname{Tr}L_1=0,\qquad
\operatorname{Tr}L_1^2=\frac1{18},\qquad
\operatorname{Tr}L_1^3=\frac1{1200},\qquad
\operatorname{Tr}L_1^4=\frac{29}{15876}.
\]

Newton recurrence and an independently multiplied primitive-cycle product generated 51 coefficient rows through degree 16 and agreed exactly in every row. Thus the finite ledger validates the whole-operator Fredholm identity on its honest domain; it also exposes the decisive mismatch: the coefficient of $z$ is zero because the graph has no loop.

## Source and adversarial controls

The source audit examined 30,626 edges with source at most 4096. Every edge satisfies $n+1=dq$, all 4,095 successor edges occur, and there are zero loops and zero identity mismatches. No prime table, primality routine, Riemann-zero data, target feedback, or forbidden arithmetic package appears in the authority source.

The $q=\{1,2\}$ spine retains cycles of every tested length $2$ through $32$ with zero margin against the full graph's all-length flood. The $q=1$ successor-only graph is acyclic. The 225 quotient-family rows, 20 graph-control rows, and 64 positive-weight inventory rows show that positive reweighting changes weights but cannot remove the unwanted orbit species.

## Trace-class diagnostics

The analytic proof gives the sharp statement $L_s\in\mathcal S_1$ exactly when $\Re s>1/2$. Finite row-nuclear prefixes through source 4096 are diagnostic only:

| $\sigma$ | prefix at 4096 |
|---:|---:|
| 0.49 | 17.904158278703147 |
| 0.50 | 16.274858200288460 |
| 0.51 | 14.817207256414280 |
| 0.55 | 10.346214472574713 |
| 0.60 | 6.854065051031045 |
| 0.75 | 2.528573354899042 |
| 1.00 | 0.8454788227554695 |
| 1.50 | 0.21046656465316765 |

No convergence threshold was fitted from these decimals.

## Verification and reproducibility

The test suite contains 19 declared tests and all 19 pass. The strict integrity gate checks row counts, exact flags, determinant agreement, Route-A schema, pending two-stage provenance, scope, source policy, LF/JSON determinism, artifact existence, and absence of cache files. Two complete regenerations produce an identical SHA-256 result ledger.

## Claim boundary

The experiments support a strongly connected, mixing symbolic system with an intrinsic arithmetic relation and a genuine analytic Fredholm determinant. They do not support rational-prime selectivity, a marked prime Euler product, meromorphic continuation past the trace-class boundary, a functional equation, a Weil form, or a Hilbert--Pólya operator. The failure is structural rather than numerical: the same minimal quotient spine already produces primitive cycles at every length.
