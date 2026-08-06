# Candidate research proposal (historical N+2 label superseded)

> Priority note (2026-08-05): this proposal now competes in the breadth-first
> Hénon candidate search; it is not a scheduled N+2 project.

Priority status: deferred after the novelty audit uncovered substantial prior
work on quantized Hénon spectra and horseshoe-regime WKB/Stokes geometry. This
proposal is not authorized for implementation until G0 proves that the
certified localized trace/determinant target is materially new.

## Problem anchor

Paper 5 begins with an exact area-preserving Hénon recurrence but extracts a
spectrum from a different object: a formal continuum approximation, an added
quartic confinement, a fitted time schedule, and a phase-unwrapping rule. The
central unresolved question is therefore more basic than zero matching:

> **Which spectral object is actually determined by the exact discrete Hénon
> map, and what periodic-orbit information can it rigorously carry?**

## Precise failure mode

There are three distinct objects in the legacy construction:

1. the exact symplectic map \(H_a\);
2. a quartic Schrödinger Hamiltonian obtained after continuum approximation
   and regularization;
3. a finite FFT Floquet matrix plus a noncanonical phase-to-energy branch
   selection.

Their spectra are not interchangeable. The quartic Hamiltonian has a fixed
polynomial Weyl exponent, the full-plane quantum map has unitary quasienergy
phases rather than an automatically discrete energy sequence, and the finite
FFT matrix depends on compactification/boundary conventions.

## Literature and repository gap

- Exact quantization of Hénon-type maps is known (Fornæss--Weickert), and its
  spectral properties were developed further by Weickert.
- Helleman and Shudo--Ikeda already studied quantum levels, propagators,
  horseshoe-regime WKB paths, and Stokes geometry for quantized Hénon maps.
- Semiclassical trace formulas for hyperbolic quantum maps are known.
- The repository has a certified local \(H_6\) survivor, exact symbolic
  dynamics, orbit coordinates, and instability multipliers.
- The repository does **not** yet connect those certified cycles to the exact
  quantum Hénon kernel with a controlled trace error.
- No existing project has proved the simple but decisive Weyl-law obstruction
  for the specific Paper-5 quartic surrogate.

## Chosen idea

Use an “exclude--replace--connect” architecture:

1. **Exclude:** prove that the quartic surrogate cannot have
   Riemann--von Mangoldt asymptotics.
2. **Replace:** state the already known exact Fourier-integral quantization in
   the Paper-5 coordinate convention and prove its unitarity/canonical
   relation directly.
3. **Connect:** localize it chronologically to the certified four-state
   \(H_6\) survivor and derive a periodic-orbit trace formula whose phase is
   the discrete action and whose amplitude is determined by the instability
   roof.

## Dominant contribution thesis

> The quartic continuum spectrum used in Paper 5 is asymptotically
> incompatible with the Riemann-zero counting law and is not a canonical
> spectrum of the Hénon map; a specified natural localized quantization may
> instead admit a target-free semiclassical trace expansion over the certified Hénon
> periodic orbits, with a controlled classical--quantum error.

If reactivated, the paper has one dominant purpose: identify and validate one
fully specified classical--quantum spectral bridge, while proving its gauge
and cutoff limitations. It does not identify a unique “correct” quantum
spectrum.

## Theorem ladder

### T1. Parameter and symplectic identities

Prove area preservation, reversibility, and the exact conjugacy to the
standard conservative Hénon parameter convention.

### T2. Quartic Weyl no-go

For

\[
V(q)=\lambda q^4+O(q^3),\qquad \lambda>0,
\]

prove

\[
N_H(E)=C_{\lambda,\hbar}E^{3/4}+o(E^{3/4}),
\]

with the explicit beta-function constant, and conclude incompatibility with
\(T\log T\) under every fixed affine energy rescaling. State the exact scope
of the obstruction.

### T3. Exact discrete quantization in current coordinates

For

\[
S_a(q,Q)=qQ-q+\frac a3q^3,
\]

derive \(H_a\), define \(U_{a,\hbar}\), and prove unitarity by factorization
into a Fourier transform and a cubic-phase multiplier. Check the Fourier sign,
reflection, and inverse-map convention against Fornæss--Weickert.

Freeze the action gauge, branch \(\sqrt i=e^{i\pi/4}\), global phase, and
subprincipal convention. State explicitly that adding a generating-function
coboundary gives unitary conjugacy while adding a constant rotates the
quasienergy spectrum.

No claim of an exact Egorov identity for arbitrary observables is permitted.

### T4. Local fixed-time trace formula

For the certified local survivor \(\Lambda_*\), prove for each fixed \(n\)
that a specified localized chronological operator satisfies

\[
\operatorname{tr}\mathcal M_\hbar^n
=\sum_{x\in\operatorname{Fix}(H_6^n)\cap\Lambda_*}
\frac{e^{iS_n(x)/\hbar-i\pi\mu_x/2}}
{\sqrt{|\det(I-DH_6^n(x))|}}
+R_n(\hbar),
\]

with \(|R_n(\hbar)|\le C_n\hbar\), or a comparably explicit certified
remainder. The cutoff must equal one microlocally on the stationary points and
must preserve the ordered Markov itinerary.

The block adjacency is \(\mathbf1_{\{A_{w,w'}=1\}}\) for input/source \(w\)
and output/target \(w'\). Prove trace class of the localized operator, exclude
extra stationary points in its support, and verify
\(\det D^2\Phi_n=(-1)^{n-1}\det(I-DH_6^n)\) with separate \(n=1,2\) handling.

### T5. Instability-amplitude identity

For every primitive hyperbolic cycle and its repetitions, express the trace
amplitude exactly in terms of the already proved instability time
\(T_p=\log|\Lambda_{u,p}|\). This explains the mathematical role of the prior
project's roof without reinterpreting it as a quantum level.

### Stretch T6. Log-time or determinant control

Either:

- extend the trace error uniformly to \(n\le c|\log\hbar|\); or
- certify a truncated determinant on a fixed contour by an explicit tail
  bound/Rouché argument.

T6 is not required for the minimal paper, but without it the novelty claim
must emphasize the certified geometry and explicit error bounds rather than a
global spectral determinant.

## Minimal validation program

The computational half uses no primes, zero ordinates, completed zeta
functions, or arithmetic lookup tables.

1. Reproduce the legacy low-\(a\) tangency algorithm only to show what it does
   and does not test.
2. Numerically verify the quartic \(E^{3/4}\) law across domain/grid choices as
   a sanity check for T2.
3. Assemble the localized quantum kernel by high-order quadrature, not a
   periodic FFT box.
4. Compute quantum traces independently from matrix powers and classical
   traces independently from certified orbit data.
5. Freeze \(a=6\), the four rectangles, cutoff family, Fourier convention,
   Maslov convention, \(\hbar\)-grid, quadrature tolerance, and period range
   before comparing the two traces.
6. Run cutoff, quadrature, neighboring-parameter, scrambled-action, and
   incorrect-amplitude controls.

Detailed metrics and gates are in `EXPERIMENT_PLAN.md`.

## Scope and non-claims

In scope:

- exact discrete action;
- natural unitary quantization;
- localized/open quantum map;
- fixed-time trace formula;
- local semiclassical determinant only if certified;
- precise Route-A evaluation.

Out of scope:

- fitting Riemann zeros;
- claiming a self-adjoint Hilbert--Pólya Hamiltonian;
- phase unwrapping into a chosen energy sequence;
- full-repeller or full-binary-horseshoe completeness;
- global first homoclinic tangency certification;
- GUE agreement as a main result;
- non-autonomous schedules or averaged transition matrices;
- Gamma factor, functional equation, or completed-\(\xi\) identity.

## Weaknesses that must remain visible

1. Exact quantization is prior work; the novelty is the certified local trace
   bridge and Paper-5 obstruction.
2. The full \(L^2(\mathbb R)\) unitary is not trace class and need not have a
   discrete point spectrum; localization changes the spectral question to an
   open-map/resonance question.
3. Open resonances may depend on cutoffs even when fixed-time local trace
   coefficients are microlocally stable.
4. A fixed-time stationary-phase theorem may be judged too standard unless the
   paper supplies explicit certified constants, a useful period range, or
   determinant control.
5. The certified survivor is local. Its cycle determinant is
   \(1-z-z^3-z^4\), not \(1-2z\).
6. No arithmetic mechanism currently turns the orbit phases or amplitudes into
   von Mangoldt weights.
7. A classical canonical relation does not uniquely fix global or subprincipal
   quantum phases. The selected convention must be justified and every
   spectral conclusion restricted to that specified operator.

## Route selection record

| Candidate | Strength | Reason not selected as the dominant paper |
|---|---|---|
| Refit more Riemann zeros | Visually direct | Target leakage and noncanonical spectral object; no evidentiary gain |
| Re-estimate tangency near \(1.0056\) | Repairs a legacy claim | The old algorithm is invalid, and the relevant conservative homoclinic structure has substantial prior literature; weak spectral progress |
| Certify the global horseshoe-closing tangency near \(5.69931\) | Strong computer-assisted dynamics result | Valuable separate paper, but requires a new full-repeller proof and is less directly tied to the spectral question |
| Finish the classical Ruelle-operator limit | Strong rigorous continuation | Retained as C00 foundation/control/fallback |
| Exact quantization alone | Natural operator | Already done by Fornæss--Weickert; insufficient novelty |
| Weyl no-go + certified localized trace bridge | Directly corrects Paper 5's spectral step | HCS-C09 candidate pending G0 and a stronger-than-standard theorem |

## Go/no-go decision

This route remains deferred. Proceed to a manuscript only if G0 first shows
material novelty, T2--T5 then survive independent checking, and the
quantum--orbit trace error decreases under at least three successive
semiclassical refinements for the frozen low-period set.

If T4 is already present in the literature in essentially the same
Hénon-localized form, or if localization/cutoff errors dominate without a
provable invariant, keep this route deferred. The classical Ruelle-operator
convergence paper is already the selected N+1 route.
