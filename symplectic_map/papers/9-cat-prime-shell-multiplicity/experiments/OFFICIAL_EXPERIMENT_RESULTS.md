# Official Experiment Results

Date: 2026-08-14 UTC  
Candidate: `cat_prime_shell_multiplicity_obstruction_v1`  
Frozen matrix:

\[
A=\begin{pmatrix}2&1\\1&1\end{pmatrix}.
\]

## Executive result

The single registered exact audit passed.  On the five source-locked,
development-seen prime shells \(p\in\{2,3,5,7,11\}\), the independent
finite-field classification engine and direct nonzero-vector permutation
engine agree exactly.  They find respectively

\[
m_p=1,2,4,6,24
\]

primitive cycles.  Thus the binary shell is the only registered shell with
one cycle, while every registered odd-prime shell contains multiple cycles.
The one-time orbit-label product consequently has denominator degree \(m_p\),
not one.  Its formal repeat coefficient is \(m_p/r\) for each locked
\(r=1,2,3\).

The raw point-potential return product is not identified with that label
product: it retains primitive orbit lengths and is visibly mixed at
\(p=5\).  Nonzero scalar factor weights cannot remove denominator degree.
Equal weights \(1/m_p\) repair only the first repeat and give
\(m_p^{1-r}\) thereafter.  Complete-shell fractional exponents do sum
exactly to one, but this is classified as `GLOBAL_NORMALIZED_COUNTING`, not
an ordinary local scalar potential and not a prime-specific mechanism.

The terminal classification is

`PRIME_SHELL_MULTIPLICITY_OBSTRUCTION_CERTIFIED / A0_FAIL_GLOBAL_NORMALIZATION_ONLY / ROUTE_B_NOT_OPENED`.

## Frozen execution scope

| Item | Frozen/observed value |
|---|---|
| Registered exact audits | 1 |
| Registered run count | 1 |
| Prime inputs | \(2,3,5,7,11\), and no others |
| Formal repeats | \(1,2,3\) |
| Nonzero vectors partitioned | 203 |
| Primitive cycles recovered | 37 |
| Exact controls | 12/12 pass |
| Candidate numerical runs | 0 |
| Numerical \(s\) or \(\log p\) evaluations | 0 |
| Composite shells enumerated | 0 |
| External prime tables | not accessed |
| Generated prime target arrays | 0 |
| Riemann-zero data | not accessed |
| Centralizer computations | 0 |
| Parameter, matrix, normalization, or selector searches | 0 |
| Raw result pass | `true` |

This is a deterministic exact reproduction and falsification audit.  There
are no random seeds, samples, fitted parameters, floating tolerances,
confidence intervals, or estimated residuals.  Every registered comparison
is exact, and every row has zero discrete mismatch against the frozen
ledger.

## Exact shell and orbit ledger

The period notation `period: point count` and cycle notation
`length: cycle count` are used below.

| \(p\) | Case | Shell size | Point-period profile | Primitive-cycle profile | \(m_p\) | Stratum check |
|---:|---|---:|---|---|---:|---|
| 2 | binary inert | 3 | \(3:3\) | \(3:1\) | 1 | unique binary cycle |
| 3 | inert | 8 | \(4:8\) | \(4:2\) | 2 | uniform period four |
| 5 | ramified Jordan | 24 | \(2:4,\ 10:20\) | \(2:2,\ 10:2\) | 4 | exact mixed boundary |
| 7 | inert | 48 | \(8:48\) | \(8:6\) | 6 | uniform period eight |
| 11 | split | 120 | \(5:120\) | \(5:24\) | 24 | 4 eigenline and 20 off-eigenline cycles |

For every row, the direct canonical cycles are disjoint, exhaustive, and
closed under the cat-map action.  The analytic engine independently returns
the same shell cardinality, period histogram, cycle histogram, \(m_p\), and
split strata.  Each row is explicitly labeled
`FINITE_FALSIFICATION_CONTROL`; none is labeled all-prime evidence.

The ramified row is the main semantic boundary.  Modulo five, four vectors
form two length-two cycles and twenty vectors form two length-ten cycles.
Replacing this mixed profile by a single period would corrupt the raw
return product even though the one-time label degree remains four.

## Raw-return versus orbit-label products

| \(p\) | Raw-return factor | One-time orbit-label factor | Label coefficients at \(r=1,2,3\) |
|---:|---|---|---|
| 2 | \((1-2^{-3s})^{-1}\) | \((1-2^{-s})^{-1}\) | \(1,\ 1/2,\ 1/3\) |
| 3 | \((1-3^{-4s})^{-2}\) | \((1-3^{-s})^{-2}\) | \(2,\ 1,\ 2/3\) |
| 5 | \((1-5^{-2s})^{-2}(1-5^{-10s})^{-2}\) | \((1-5^{-s})^{-4}\) | \(4,\ 2,\ 4/3\) |
| 7 | \((1-7^{-8s})^{-6}\) | \((1-7^{-s})^{-6}\) | \(6,\ 3,\ 2\) |
| 11 | \((1-11^{-5s})^{-24}\) | \((1-11^{-s})^{-24}\) | \(24,\ 12,\ 8\) |

The raw factors use the actual primitive orbit lengths.  The label factors
attach the same formal shell label \(p^{-s}\) once to every primitive cycle.
The registered result keeps these constructions in distinct schema fields,
and every formal coefficient is an integer or rational string.  No value of
\(s\), \(p^{-s}\), or \(\log p\) was evaluated.

## Mechanism controls

| \(p\) | Scalar denominator degree | Equal-weight sums at \(r=1,2,3\) | Fractional shell exponents | Fractional sum | Selector discard cost |
|---:|---:|---|---|---:|---:|
| 2 | 1 | \(1,1,1\) | \(1\) | 1 | 0 |
| 3 | 2 | \(1,1/2,1/4\) | two copies of \(1/2\) | 1 | 1 |
| 5 | 4 | \(1,1/4,1/16\) | \(1/12,1/12,5/12,5/12\) | 1 | 3 |
| 7 | 6 | \(1,1/6,1/36\) | six copies of \(1/6\) | 1 | 5 |
| 11 | 24 | \(1,1/24,1/576\) | twenty-four copies of \(1/24\) | 1 | 23 |

The mechanism comparison has three separate conclusions:

1. With every scalar factor weight nonzero, denominator degree remains
   \(m_p\).  Degree one occurs only at the binary control among the five
   locked rows.
2. Setting every scalar weight to \(1/m_p\) makes the first power sum one,
   but at repeats two and three it gives \(m_p^{-1}\) and \(m_p^{-2}\).
   This is not a repeated-factor repair for any registered odd prime.
3. Weighting each orbit externally by its point mass
   \(|\gamma|/(p^2-1)\) gives total exponent one exactly.  This changes the
   construction to complete-shell normalized counting.  Alternatively,
   retaining one factor requires discarding exactly \(m_p-1\) cycles and
   introduces a noncanonical global selector.

The symbolic composite control records

\[
J_2(q)=q^2\prod_{\ell\mid q,\ \ell\ \mathrm{prime}}(1-\ell^{-2}),
\qquad
\sum_\gamma |\gamma|=J_2(q),
\]

and hence the same fractional identity for symbolic exact-order-\(q\)
shells.  No value of \(q\) was selected and no composite shell was scanned.
This establishes non-prime-specificity of the normalization at the symbolic
contract level.

## Proof-versus-computation boundary

| Statement | Evidence role | Certified content | Explicit nonclaim |
|---|---|---|---|
| Five locked shell ledgers | registered exact computation | dual-engine equality and exact frozen profiles | no new or blind prime evidence |
| Odd-prime multiplicity theorem | `notes/PROOF_PACKAGE.md` | all odd primes satisfy the proved multiplicity lower bound | not inferred from five rows |
| Scalar denominator obstruction | polynomial-degree proof | fixed nonzero scalar factors cannot collapse degree | does not cover matrices, numerators, or alternating determinants |
| Real/absolute convergence strips | proof-only contract | divergence and nonabsolute convergence for \(1<\Re s\le2\); absolute convergence for \(\Re s>3\) | no claim for \(2<\Re s\le3\), no exact abscissa |
| Composite normalized identity | symbolic proof contract | complete-shell fractional mass is non-prime-specific | no composite enumeration or primality test |
| Centralizer and enriched escapes | outside scope | reserved as genuine later possibilities | no Paper-9 centralizer closure |

No analytic continuation, conditional-convergence strip, prime/zero
correspondence, transfer/Fredholm determinant, quantization, or zero
statement is claimed.

## Interpretation and route decision

The strongest finite observation is not merely that multiplicities exceed
one: it is the exact compatibility of three constraints.  The orbit
partition forces \(m_p\) label factors, formal repetition preserves the
coefficient \(m_p/r\), and the only no-discard unit-exponent control changes
the object into global normalized counting.  This closes the direct
unweighted and pure nonzero-scalar normalization attempt at A0.

It does not close every possible dynamical construction.  Centralizer
quotients, matrix-valued weights, numerator or alternating cancellation,
transfer/Fredholm formulations, cohomological superdeterminants, and
enriched selectors remain explicitly outside the theorem and execution.
The centralizer quotient is reserved for Paper 10.  Route B is not opened by
this Paper-9 result.

## Provenance and frozen tracker note

| Artifact | SHA-256 |
|---|---|
| Source lock | `662809d40f7e409e439983774a36349b90f265616a488061fda3c5b9064c2d49` |
| Execution tree | `466fb64928ad5f8b5b4c2643d8875c98568bbbdaabd4abeb6f24cc7ba13ecddb` |
| Deployment review | `dffcd516d349ef864d078764b9e9ccaa2edccd70d52802e77b6965baa70b9b27` |
| Authorized pre-execution audit | `a54ad84f5e889b9e54a4f4407b1e8a9021a001358188419ffa961f11d8f2b75a` |
| Registered claim | `863d9d3c4e77bd2407776244c8e925abd60fd265cff5163698e81d32f144e2d4` |
| Raw experiment result | `448de06e92bd7ab4e5374e5d1f57413df45859cd3476ff14b2691b63ac364fab` |
| Completed terminal | `bc82784449e50ec85c3d268197ab8489c7e2a888bfb35aa4a49915488b66273c` |
| Post-run JUnit, 23/23 pass | `43f03d9be620188422dbb01d8ff016d4811eb505475214845ae17dffb21c6304` |

The source lock binds `experiments/EXPERIMENT_TRACKER.md` at SHA-256
`00fc66f266b7a1ddcccc0b355ff7dbb6ea787f1d60319862dbd7d5da6262d0b9`.
It therefore remains unchanged.  Its zero-run and `TODO_NOT_AUTHORIZED`
entries are historical source-design records, not a mutable completion
dashboard.  The live execution status is carried by the unique claim,
result, terminal, this report, the independent result-integrity report, and
the final strict manifest.
