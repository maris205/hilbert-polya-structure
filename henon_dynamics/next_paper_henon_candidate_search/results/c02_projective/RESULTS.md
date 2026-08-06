# HCS-C02 projective pilot results

## Decision

**Partial structural pass; no Route-A A2 promotion.**  The object established
here is a **two-disk separated holomorphic projective fibre cocycle over the
real symbolic base**.  The proposed Schottky strictification is not
established: the true coefficient \(q=q(\omega)\) varies with the complete
Hénon itinerary, so the exact cocycle is not a finite list of constant
Möbius generators.

## Exact result

The R058 normalized unstable cone converts to the raw complex slope disk

\[
D_0=\{|m|\le R\},\qquad
R=\frac{41/256}{7/48}\frac12=\frac{123}{224}.
\]

For every real base point in the R058 survivor,

\[
|q|\in[1/3,5/8],\qquad
\phi_q(m)=\frac1{-12q-m}.
\]

Consequently, on \(D_0\),

\[
|-12q-m|\ge 4-R=\frac{773}{224},
\]

\[
|\phi_q(m)|\le\frac{224}{773}<R,
\qquad
|\partial_m\phi_q(m)|
\le\left(\frac{224}{773}\right)^2
=\frac{50176}{597529}<0.084.
\]

This is a pole-free, strict holomorphic fibre contraction.  It is exact
rational arithmetic, not a sampled inequality.

There are also explicit, source-locked separated child disks (not claimed to
be unique or optimal).  Set

\[
C=\frac{23}{120},\qquad
\rho=\frac7{120}+\frac{123}{3092}
=\frac{9101}{92760}.
\]

Then

\[
q<0\Longrightarrow \phi_q(D_0)\subset D(C,\rho),
\qquad
q>0\Longrightarrow \phi_q(D_0)\subset D(-C,\rho).
\]

The two child disks have open gap

\[
2(C-\rho)=\frac{4339}{23190}\approx0.187107,
\]

and their outer edge is

\[
C+\rho=\frac{224}{773}<R.
\]

Thus the six graph edges carry an exact four-state disk bundle: over state
\((s,t)\), the unstable slope lies in the disk centered at \(-tC\); after a
true transition it lands in the disk centered at \(-sC\).  The coefficient is
still the true \(q(\omega)\), never a statewise fitted constant.

## Memory 1--8

The published contraction proof gives, for two itineraries agreeing on
$[-m,m]$,

\[
|q_0(\omega)-q_0(\widetilde\omega)|
\le \frac7{24}\left(\frac2{\sqrt{17}}\right)^m.
\]

This is sharper than the earlier R059 markdown's loose $5/4$ continuity
prefactor: the published proof starts from the exact diameter $7/24$ of a
common-sign window and contracts once for every inward memory step. The
sharper, source-locked estimate yields the following uniform bounds.

| Memory | Central cylinders | $q_0$ diameter bound | Map-family sup bound | Log-derivative distortion bound |
|---:|---:|---:|---:|---:|
| 1 | 6 | 0.141479 | 0.142564 | 0.983948 |
| 2 | 15 | 0.068627 | 0.069154 | 0.477285 |
| 3 | 40 | 0.033289 | 0.033545 | 0.231517 |
| 4 | 104 | 0.016148 | 0.016271 | 0.112302 |
| 5 | 273 | 0.007833 | 0.007893 | 0.054475 |
| 6 | 714 | 0.003799 | 0.003829 | 0.026424 |
| 7 | 1,870 | 0.001843 | 0.001857 | 0.012818 |
| 8 | 4,895 | 0.000894 | 0.000901 | 0.006217 |

All three uncertainty bounds decrease strictly at every refinement. This
supports a Hölder-driven fibre cocycle; it does not turn the continuum of
$q(\omega)$ values into finitely many exact generators.

## Periodic monodromy sanity

All 17 primitive symbolic cycles through period 8 were generated internally.
The exact primitive counts by period are

\[
(1,0,1,2,2,2,4,5).
\]

For their numerically solved R059 periodic points:

- maximum Hénon recurrence residual: \(3.997\times10^{-15}\);
- maximum error in \(B_{n-1}\cdots B_0=J M_\gamma J\): 0 in the
  executed double-precision operation ordering;
- maximum unstable-slope fixed-point residual: \(3.331\times10^{-16}\);
- maximum error in
  \((\Phi_\gamma)'(m_u)=\Lambda_u^{-2}\):
  \(2.033\times10^{-20}\);
- minimum clearance of an unstable slope inside its predicted child disk:
  \(0.04627>0\).

The matrix identity is algebraic for arbitrary (q_i); the floating-point
cycle run is a regression test for order, slope convention, and word
bookkeeping, not its proof.

## What did not pass

R058/R059 do not currently provide a certified complex neighborhood of the
**base Hénon inverse branches**.  The disk result above is holomorphic in the
fibre variable \(m\) while \(q(\omega)\) remains on the real symbolic
survivor. Therefore this pilot does not establish:

- a finite Schottky group or discrete set of Möbius generators;
- a holomorphic Markov map on a complexified Hénon base;
- nuclearity or a Fredholm determinant;
- meromorphic continuation, a functional equation, or a spectral counting
  law;
- any Route-A A2/A3 or Hilbert--Pólya conclusion.

Approximating each cylinder by a constant \(q\) would be a convergent
finite-memory model, but calling its generators exact would violate the BF1
non-grafting rule.

## Gate and next theorem

The C02 **Schottky strictification gate is failed/not established in round
one**.  Retain the exact two-disk fibre lemma as reusable structure, but do
not promote C02 to the next-paper theorem lane yet.

The smallest legitimate follow-up is to test the R059 signed-square-root
operator

\[
(T_\varepsilon q)_i
=\varepsilon_i\sqrt{\frac{1-q_{i-1}-q_{i+1}}6}
\]

on a frozen complex polydomain.  The required result is strict self-mapping,
a common analytic square-root branch, and contraction with an explicit
complex radius.  Only after that base extension is proved should one ask
whether the combined base--fibre transfer operator is nuclear.  The present
fibre disks alone cannot support that inference.

## Artifacts and reproduction

- `pilot_summary.json`: exact constants, checks, and conservative gate;
- `memory_bounds.csv`: all memory \(1,\ldots,8\) bounds;
- `state_disk_bundle.csv`: all six chronological graph edges;
- `periodic_monodromy.csv`: the 17 primitive-cycle checks;
- `independent_check.json`: independent exact-constant and gate audit.

Run from the repository root:

```bash
python next_paper_henon_candidate_search/code/c02_projective_pilot.py
python next_paper_henon_candidate_search/code/c02_projective_check.py
```

Both commands exit successfully; the independent checker reports
`all_checks_pass=true`.
