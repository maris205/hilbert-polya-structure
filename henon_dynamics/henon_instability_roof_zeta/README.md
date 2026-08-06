# Hénon instability-roof zeta

This project asks whether the certified local survivor of the area-preserving
Hénon map

\[
H_6(x,y)=(1-6x^2-y,x)
\]

has a natural non-lattice clock suitable for a dynamical-zeta investigation.
The answer is mathematically positive at the clock level and negative at the
current Hilbert--Pólya level, conditional on the hash-locked companion
certificate for the local survivor.

## Main outcome

The periodic instability length

\[
T_p=\log|\Lambda_{u,p}|
\]

has a positive Hölder roof representative on the certified survivor, with
\(J^u\ge773/224>1\). The pointwise representative is intrinsic up to a Hölder
coboundary; the periodic lengths are invariant. Two exact primitive
multipliers have incommensurable logarithms, so the roof is non-lattice.
Hölder regularity follows from the standard invariant-bundle regularity
theorem for the compact uniformly hyperbolic survivor.

This removes the exact lattice-periodicity obstruction of unit map time. It
does not produce a limiting determinant, functional equation,
Riemann--von Mangoldt law, prime correspondence, or self-adjoint operator.

## Clock triage

| Clock | Exact result | Consequence |
|---|---|---|
| integer map time | determinant \(1-e^{-s}-e^{-3s}-e^{-4s}\), periodic under \(s\mapsto s+2\pi i\) | only \(O(T)\) zeros in a bounded real strip |
| stored generating-function action | an explicit primitive period-four orbit has action zero | not a strictly positive suspension roof |
| instability time | positive, additive under repetition, and non-lattice | escapes the unit-clock periodicity obstruction |

The non-lattice proof uses the negative fixed-orbit multiplier

\[
X^4-4X^3-22X^2-4X+1=0
\]

and the exact period-four multiplier \(289+24\sqrt{145}\), which satisfies
\(X^2-578X+1=0\). Every positive power of the first multiplier has degree four;
every power of the second has degree at most two.

## Frozen experiment

The computed cycle section is

\[
D_{\kappa,N}(s)=
\left[
\prod_p(1-\sigma_p^\kappa e^{-sT_p}z^{n_p})
\right]_{\deg z\le N}\bigg|_{z=1},
\qquad \kappa\in\{0,1\}.
\]

The object, clock, section convention, root rectangle, precision, matching
tolerance, random seeds, and forbidden data were frozen before periods 13--20
were opened. Prime tables, Riemann-zero tables, zeta/xi evaluations, target
fitting, and post-validation unfolding were forbidden.

The complete symbolic catalogue contains 2,170 primitive cycles through period
20. In the rectangle \(-0.25\le\Re s\le0.30\), \(|\Im s|\le20\):

- the untwisted sections contain 43 located zeros at every tested cutoff
  \(N=7,8,10,12,14,16,18,20\);
- all 39 preregistered untwisted zeros survive validation and sealed testing,
  with sealed median drift \(1.759\times10^{-6}\);
- the cutoff-20 positive real zero is
  \(0.2779829816761890234883231168318\ldots\);
- the twisted family retains 43 tracked zeros, one of which is the exact
  symbolic root \(s=0\);
- primitive multiplication and trace recursion agree below
  \(7.5\times10^{-75}\) at the reported roots.

These are finite-section numerical observations. The sampled winding audits
are highly consistent but are not interval-certified argument-principle
counts.

## Controls

At the common Hénon probe, valid random weight, random phase, and same-density
length controls have degree-9--16 coefficient tails between
\(2.86\times10^4\) and \(3.20\times10^5\) times larger than Hénon and retain
few cutoff-8 roots. This establishes structured cancellation relative to those
orbit-level controls; it does not isolate shadowing as the mechanism.

The exact constant-roof parent is even more stable, so stability is not an
arithmetic signature. Numerical continuations at \(a=5.9\) and \(a=6.1\) are
also internally stable, so \(a=6\) is not numerically isolated by this test.
Global period/length shuffles defeat the frozen contour sampler; their sampled
root counts are retained as NOT_TESTABLE rather than guessed.

## Route-A result

The strict evaluation is

    (A1_WEAK, A2_FROZEN_VALIDATION_PASS, A3_FAIL, A4_FORMAL_HINT)
    overall: ROUTE_A_EXPLORATORY
    Route B authorized: false

A1 remains weak because no prime-like correspondence exists. A2 records
internal frozen finite-section stability, not a Riemann-zero match. A3 fails
for lack of a limiting analytic divisor and global counting law. A4 is only a
formal suspension hint without an operator.

## Reproduction

Fast independent verification:

    python henon_instability_roof_zeta/code/check_results.py
    pytest -q henon_instability_roof_zeta/code/tests

Complete regeneration:

    bash henon_instability_roof_zeta/code/run_all.sh

Generated timestamps and PDF metadata are tied to the frozen protocol epoch,
so an identical full rerun is byte-stable rather than acquiring wall-clock
changes.

The independent checker reconstructs the orbit, determinant, winding, root,
precision, control-source, and neighbor gates without importing the producer
module. The recorded result is 38/38 checks and 7/7 unit tests.

## Project map

- PAPER_PLAN.md and NARRATIVE_REPORT.md: claim/evidence and research narrative
- refine-logs/: frozen protocol, experiment plan, and run tracker
- refine-logs/INHERITED_DEPENDENCIES.json: full hashes for the two inherited
  proof premises and period-12 comparison catalogue
- code/: producer, controls, independent checker, tests, figures, and manifest
- results/: raw JSON/CSV, analysis, checker report, and handoff manifest
- evaluations/route_a/: strict Route-A YAML
- paper/main.pdf: compiled mathematical research note

The enclosing workspace has no Git metadata. Provenance is therefore bound by
the frozen protocol and SHA-256 artifact manifest, not by an invented commit
identifier.
