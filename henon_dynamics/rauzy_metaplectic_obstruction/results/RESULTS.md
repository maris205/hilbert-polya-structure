# HCS-C24 results

## Material Passport

- Origin Skill: `ars-codex academic-research-suite / experiment-agent`
- Origin Mode: `run`
- Origin Date: `2026-08-09T11:00:00Z`
- Verification Status: `UNVERIFIED`
- Version Label: `exp_result_v1`

Independent verification is recorded separately in
`c24_independent_check.json` and `VALIDATION_REPORT.md`.

## R1: literal source lock passes

The two-row permutation `1234/4321` is retained literally.  Exact BFS gives
seven labeled states and fourteen directed Rauzy edges.  Its crossing matrix
has determinant one and rank four, giving genus two and one order-two zero:

```text
stratum = H(2)
relative lattice = absolute lattice = Z^4
```

Every edge exactly satisfies

\[
B_e\Omega_{\rm src}B_e^T=\Omega_{\rm dst}.
\]

Thus the implementation does not confuse transport between fibers with
fixed-form symplecticity.

## R2: exact primitive labeled ledger

The primitive labeled directed free-cycle counts are:

| elementary length | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| primitive cycles | 4 | 2 | 4 | 4 | 8 | 11 | 22 | 35 | 64 | 110 | 204 | 360 |

The total is 828.  The independent Möbius--trace oracle uses the based closed
walk counts

```text
4, 8, 16, 24, 44, 86, 158, 304, 592, 1148, 2248, 4422.
```

It reproduces all twelve primitive counts exactly.

## R3: phase-invariant eventually-positive labeled cycles

Entrywise positivity changes with cyclic cut, so the release asks whether
every phase matrix has a positive power within the exact four-dimensional
Wielandt bound.  The number of passing primitive labeled cycles is:

| elementary length | 8 | 9 | 10 | 11 | 12 |
|---:|---:|---:|---:|---:|---:|
| eventually positive | 1 | 6 | 14 | 36 | 89 |

All 146 pass through the central state.  Their induced central return periods
are two or three, and the certificate stores every return branch without
discarding the underlying elementary word.

The 146 cycles have only 41 distinct reciprocal characteristic polynomials.
They remain distinct periodic words in the fixed-label Rauzy coding; no
distinctness claim is made after forgetting markings.  Spectral coincidence
is recorded as metadata and is never used as a code quotient.

The unique length-eight class has reciprocal polynomial

\[
x^4-7x^3+13x^2-7x+1
\]

and exact repetition determinants

\[
1,29,361,3509,30976,261725.
\]

Its Perron root lies in the released rational interval near
\(4.3902568845156\), giving \(\ell\approx1.4793877412101\).  The rational
interval, not the decimal, is the certificate.

## R4: the pointwise Weil weight fails on primitive labeled cycles

Among the 146 eventually-positive labeled cycles, exactly 21 have \(\det(I-M)=0\):

| length | 10 | 11 | 12 | total |
|---:|---:|---:|---:|---:|
| singular cycles | 6 | 6 | 9 | 21 |

Their reciprocal polynomial contains \((x-1)^2\), and the exact ledger
confirms

\[
\det(I-M^r)=0,\qquad r=1,\ldots,6.
\]

Algebraically the same holds for every \(r\ge1\).  These are primitive
directed cycles in the labeled Rauzy return coding; the ledger does not claim
146 distinct primitive unmarked Teichmüller geodesics.  Consequently the
regular point formula \(|\det(I-M)|^{-1/2}\) cannot be a finite
primitive-cycle weight on the full selected labeled-cycle set.  This is a
singular-locus result about a distribution
character, not evidence for an infinite ordinary trace.

## R5: two large ordinary-Fredholm realization classes close

Two exact theorems apply.

1. \(\|K\otimes U\|_{\rm ess}=\|K\|\) for an infinite-dimensional unitary
   fiber.  A nonzero exact/modulo-compact branch compression is fatal.
2. An absolutely norm-summable discrete metaplectic atomic sum is noncompact
   unless every central-sign-aware same-projection aggregate vanishes.

The second result uses escaping Weyl coherent states and applies without
cylinder projections.  It covers any selected Hilbert-space analytic
half-plane once its
branch norms are proved summable and a signed aggregate is nonzero.  The first
result covers every bounded Banach-space realization that admits the stated nonzero
exact/modulo-compact branch compression.  Neither application hypothesis has
yet been verified on one particular canonical analytic Zorich space.

## Decision and scope

```text
source lock: PASS
naive pointwise character Euler product: REFUTED
branch-compressible ordinary metaplectic Fredholm: PROVED_SCOPED_OBSTRUCTION
norm-summable discrete atomic realization: PROVED_SCOPED_OBSTRUCTION
canonical analytic Zorich-space application: OPEN
generalized/distributional trace: OPEN AS A NEW OBJECT
Route A: REJECTED
Route B: NOT AUTHORIZED
```

No conclusion is drawn about a canonical flat trace, semifinite determinant,
continuous group smoothing, or another quantum fiber.  No regularizer was
inserted.
