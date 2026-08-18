# Exact Witness Ledger — Paper 47

## Edge and nonedge controls

| Pair | Sum | Product | Quotient | Result |
|---|---:|---:|---:|---|
| \((2,2)\) | 4 | 4 | 1 | loop |
| \((3,6)\) | 9 | 18 | 2 | edge |
| \((4,4)\) | 8 | 16 | 2 | loop |
| \((4,12)\) | 16 | 48 | 3 | edge |
| \((15,30)\) | 45 | 450 | 10 | edge |
| \((30,60)\) | 90 | 1800 | 20 | edge |
| \((60,15)\) | 75 | 900 | 12 | edge |
| \((2,3)\) | 5 | 6 | noninteger | nonedge |

## Coordinate controls

- \((3,6)\) has \((t,a,b)=(1,1,2)\).
- \((15,30)\) has \((t,a,b)=(5,1,2)\).
- \((60,15)\) has \((t,a,b)=(3,4,1)\).
- every loop is \((2t,2t)\), corresponding to \((t,1,1)\).

For row \(m=6\), the divisors \(d\mid36\) with \(d<6\) are
\(1,2,3,4\), producing the neighbors \(30,12,6,3\). This agrees exactly
with the direct divisibility predicate.

## Endpoint controls

- At \(\sigma=0\), a squarefree \(m\) with \(r\) prime factors has degree
  \((3^r-1)/2\).
- At \(\sigma=1/2\), the loop square-sum contains a harmonic series.
- At \(\sigma=1\), the absolute diagonal contains
  \(\sum_{t\ge1}(2t)^{-1}\).
- At \(\sigma>1\), the entrywise upper bound is
  \(2^{-\sigma}\zeta(\sigma)^3\).

## Mixed-cycle control

The triangle \(15\to30\to60\to15\) has three different harmonic quotients
\(10,20,12\). It is a genuine length-three closed walk, not a single
coprime-scale fiber or repeated loop.

## Sign control

On vertices \(3,6\), for real \(s>1\), the principal matrix is

$$
\begin{pmatrix}
0 & 18^{-s/2}\\
18^{-s/2} & 6^{-s}
\end{pmatrix},
$$

whose determinant is \(-18^{-s}<0\). Symmetry does not imply positivity.

## Status

EXACT_PREAUTHORITY_WITNESSES / RESULTS_NOT_RUN

