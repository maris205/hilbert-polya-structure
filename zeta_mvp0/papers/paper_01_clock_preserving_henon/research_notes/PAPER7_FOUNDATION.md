# Paper 7 Foundation

> **Scope update (2026-08-05):** This is a planning record, not a
> preregistration. Historical-selection language has been corrected; the
> authoritative theorem and evidence labels are in
> `paper/sections/04_quantum_weyl.tex` and `CLAIM_LEDGER.md`.

## Recommended title

**Clock-Preserving Hénon Warps of an Exponential Schrödinger Operator: Two
Growing Riemann--von Mangoldt Terms and Finite-Window Diagnostics**

The title deliberately avoids “Hilbert--Pólya operator.”  The Hilbert--Pólya
motivation belongs in the abstract and discussion because the arithmetic
prime-trace gate is still open.

## One-sentence thesis

We construct a zero-input family of self-adjoint confining Hénon-warped
Schrödinger operators whose quantum counts retain the two growing
Riemann--von Mangoldt terms, and show numerically that the centered
\(a=1.02\) member has stable sampled dynamics and a finite-window magnetic
symmetry response, while leaving the prime-power and zero gates open.

## Prospective discovery framing and historical boundary

Paper 7 illustrates a prospective breadth-first Hilbert--Pólya search rather
than documenting a preregistered historical tournament.  The protocol was
formalized after parts of this family had already been explored.  It separates
two future modes:

- **Route B** generates structurally different candidates, applies cheap
  Q/W/S/P/Z kill tests, and asks whether any anomalous signal survives frozen
  controls and independent replication;
- **Route A** takes a survivor and writes the shortest conditional bridge to
  the next unopened gate, concentrating proof effort on that bridge alone.

Retrospectively, the present family supports a paper because Q and W became
analytic while sampled dynamics and magnetic spectral diagnostics survived
several numerical failure checks.  This is a paper-scope judgment, not a
reconstruction of a preregistered promotion.  The prospective protocol and
death-log schema are in `RH_DISCOVERY_PROTOCOL.md`.

## Core object

\[
 \boxed{
 \mathcal H_{a,n,B}
 =\frac12(-i\nabla-A_B)^2
 +2\pi\exp\!\left(\pi|\widetilde H_a^n(q)|^2\right),}
\]

where

\[
 \widetilde H_a(x,y)=(-2ar_ax-ax^2-y,x),\qquad
 r_a=\frac1{1+\sqrt{1+a}},\qquad
 A_B=\frac B2(-y,x).
\]

The organizing idea is a pair of independent **clock-preserving
deformations**:

\[
 \text{radial exponential clock}
 \xrightarrow{\text{area-preserving Hénon warp}}
 \text{active geometry and sampled dynamics}
 \xrightarrow{\text{fixed magnetic field}}
 \text{antiunitary-symmetry diagnostics}.
\]

The first deformation preserves configuration sublevel volume; the second
preserves momentum-fiber volume.  Neither uses zero ordinates or a prime list.

## Gates and side-diagnostic status

| Label | Status | Evidence |
|---|---|---|
| Q — self-adjoint discrete quantum object | **Proved** | Friedrichs form, confinement, compact resolvent. |
| W — two growing Riemann--von Mangoldt terms | **Proved** | Exact classical phase volume and independently audited magnetic/nonmagnetic bracketing theorem. |
| S — active Hénon dynamics | **Sampled numerical support** | R000--R001 and R106 FTLE/SALI, step/time convergence, independent DOP853 solver, radial and magnetic controls. |
| R — random-matrix/symmetry diagnostic | **Finite-window descriptive support** | R100--R107A adjacent-ratio CDFs, magnetic response, and independent-order stencil agreement. R is not an HP gate. |
| C — relative-container admissibility | **Proved** | Relative staircase, heat trace, tempered wave distribution, and third-resolvent generalized SSF framework; no cancellation or arithmetic content. |
| P — endogenous prime-power trace | **Open** | No structural \(r\log p\) periods or \((\log p)p^{-r/2}\) amplitudes yet. |
| Z — explicit-formula/zero fluctuation | **Not tested; not authorized before P** | No individual-zero comparison in Paper 7. |
| RH | **No claim** | Earlier gates and side diagnostics cannot substitute for P/Z. |

This table is the paper's most important honesty device.  Q/W/S/R/C cannot be
used to infer P or Z.

## Formal theorem package

### T1. Clock invariance under area-preserving configuration warps

For every proper determinant-one diffeomorphism \(\Psi:\mathbb R^2\to
\mathbb R^2\),

\[
 \mathcal N_{\rm cl,\Psi}(E)
 =\frac{E}{2\pi}\log\frac{E}{2\pi}
  -\frac{E}{2\pi}+1.
\]

The invariant is

\[
 A_\Phi(t)=|\{q:\pi|\Psi(q)|^2<t\}|=t.
\]

### T2. Quantum two-term law for every fixed Hénon iterate

For fixed \(a>-1\), \(a\ne0\), fixed \(n\ge1\), and \(D=2^n\),

\[
 N_{a,n}(E)
 =\frac{E}{2\pi}\log\frac{E}{2\pi}
  -\frac{E}{2\pi}
  +O_{a,n}\!\left(E^{3/4}(\log E)^{1+D/2}\right).
\]

The error is \(o(E)\), so both growing terms survive quantization.  It is far
too large to determine the zeta constant term or explicit-formula
fluctuations.

### T3. Fixed magnetic fields preserve T1--T2

For each fixed \(B\), the same formula holds with an
\(O_{a,n,B}\) constant.  The exact classical identity follows from
momentum-fiber translation.  The quantum proof uses a local gauge on each
\(E^{-1/4}\) square; the residual vector potential is uniformly \(O_B(\ell)\)
and does not worsen the safe error envelope.

### T4. The warp is not removed by a unitary coordinate change

Moving the potential to radial coordinates turns the Euclidean kinetic term
into a determinant-one variable kinetic metric.  The Hénon geometry changes
representation but does not disappear.

### T5. Standard geometric time reversal is absent in the centered magnetic core

At \(B=0\), complex conjugation gives \(T^2=+1\).  At fixed \(B\ne0\), it
maps the \(B\) member to \(-B\).  For centered \(a\ne0,n=1,2\), no
orientation-reversing Euclidean isometry preserves the potential, so the
standard reflected-conjugation repair is unavailable.  This does not exclude
every abstract nonlocal antiunitary.

### T6. A rigorous signed relative-spectrum container

For the radial/Hénon pair, each first resolvent belongs to
\(\mathcal S_p\) exactly for \(p>1\), while every integer resolvent power
\(m\ge2\) is trace class.  Hence the third resolvent-power difference admits
a generalized spectral-shift framework.  In the discrete setting the
canonical normalization

\[
 \xi(E)=N_0(E)-N_1(E)
\]

satisfies the compactly supported trace formula

\[
 \operatorname{Tr}(f(H_1)-f(H_0))
 =\int f'(E)\xi(E)\,dE.
\]

The relative heat trace is an ordinary trace for \(t>0\), and the relative
wave trace is a tempered distribution.  First-resolvent trace class is not
proved and is disfavored by a divergent phase-space trace-norm diagnostic.
None of these facts supplies prime-power times or amplitudes.

## Frozen numerical propositions

### E1. Classical activity at the legacy \(a=1.02\)

At \(E=1000\), the radial control's median dimensionless FTLE decays from
0.1777 at 20 natural units to 0.0355 at 160, while SALI remains 0.768.  For
\((a,n)=(1.02,1)\), the corresponding FTLE remains 0.75 and SALI reaches
\(3.5\times10^{-16}\); \((1.02,2)\) remains near 1.23.  All R001 records pass
the energy-drift gate.

This is stable deterministic evidence at sampled points, not a theorem of
positive-measure chaos or ergodicity.

### E2. Scalar quantum level repulsion

For \(a=1.02,n=1,B=0\), the fourth-grid and \(h^2\)-extrapolated mean adjacent
ratios are 0.53225 and 0.52983, near the GOE reference 0.53590.  The ratio
array correlation from the previous to fourth grid is 0.982.  Descriptive CDF
distance is 0.045 to GOE and 0.153 to GUE.  R107A's fourth-order covariant
stencil gives 0.53477; its pointwise ratio array correlates 0.997 with the
archived second-order extrapolation.

### E3. Magnetic unitary crossover

For \(B=1\), the fourth-grid and extrapolated ratios are 0.58762 and 0.58727;
descriptive CDF distance is 0.061 to GUE and 0.114 to GOE.  The fixed scan

\[
 B=(0,0.25,0.5,1,2,4)
\]

gives mean ratios

\[
 (0.529,0.544,0.577,0.587,0.623,0.598).
\]

Every nonzero field is above the scalar baseline, and every new scan point
passes its coarse/fine grid check.  No field is selected as an arithmetic
optimum.  The independent-order fourth stencil gives 0.59089 at \(B=1\), a
magnetic-minus-scalar shift of 0.05612, and a 0.995 ratio-array correlation
with the second-order extrapolation.

### E4. Numerical integrity

R105 verifies symmetric/Landau gauge equivalence, \(B\leftrightarrow-B\)
isospectrality, deterministic reruns, relative eigen-residuals, orthogonality,
Wilson plaquette flux, source hashes, and absence of zero/prime inputs.

### E5. Independent adaptive magnetic-dynamics check

R106 reimplements the potential derivatives and physical-velocity magnetic
flow locally and advances the state and variational equations with adaptive
DOP853.  At \(E=1000\) and 80 natural units, the radial control has 0/4 joint
FTLE--SALI flags at both \(B=0\) and \(B=1\).  The centered \(a=1.02,n=1\)
model has 4/4 flags at both fields, with median FTLE/SALI

\[
 (0.7513,2.11\times10^{-15})\quad(B=0),\qquad
 (0.6132,6.15\times10^{-15})\quad(B=1).
\]

The nonmagnetic DOP853/Verlet median-FTLE ratio is 0.994, and the maximum
relative energy drift among all sixteen records is \(1.97\times10^{-9}\).
Thus the sampled chaos signal survives both an independent integrator and the
magnetic control, without becoming a positive-measure chaos theorem.  This
check covers the core \(B=1\) branch through 80 natural units; it does not yet
provide magnetic time convergence or cover every field in the quantum scan.

### E6. Independent-order quantum-stencil check

R107 initially passed every cross-stencil physics gate but failed the maximum
Ritz-residual gate.  The frozen R107A remediation requested twenty guard modes
and retained the lowest 180 without changing any physical or statistical
choice.  It then passed all original gates.  At \(B=0,1\), respectively:

- fourth-order coarse/fine median level changes are 0.0407% and 0.0403%;
- fourth-order vs second-order-extrapolated median level differences are
  0.0194% and 0.0189%;
- mean-ratio differences are 0.00494 and 0.00362;
- ratio-array correlations are 0.997 and 0.995;
- maximum retained Ritz residuals are \(4.65\times10^{-10}\) and
  \(6.86\times10^{-11}\).

This is an independent-order finite-difference check, not a wholly independent
discretization family: the Cartesian grid, Peierls links, rectangular wall,
point-sampled potential, and eigensolver remain shared.

## Why \(a=1.02\), and why \(a=6\) is not the core

The two-term theorem holds for every fixed \(a\); it does not select 1.02.
The value 1.02 is a hypothesis fixed by the earlier Hénon study before this
operator family was invented.  That programme was RH-motivated and
zero-exposed.  The value is prior-frozen for the present zero-input runs but
is not claimed to have a statistically blinded lineage or to be an arithmetic
constant derived here.

The \(a=6\) member remains valuable as a certified hyperbolic/high-distortion
control inherited from Papers 3--5.  Its physical allowed domain becomes very
elongated, and R101 local spacing ratios fail the fine/extrapolated stability
check.  It must not be assigned an RMT class in Paper 7.

Centering at the positive fixed point has three roles:

1. it is an affine area-preserving conjugacy, so it retains the discrete
   Hénon dynamics and the exact clock;
2. it makes \(a=0\) an exact radial integrable control for every iterate;
3. it removes the accidental reflection symmetry of the uncentered
   one-iterate potential, enabling a genuine standard-TR-breaking magnetic
   branch.

## Relation to earlier papers

- The prior `5-An Area-Preserving Henon-Map Model.pdf` motivates the frozen
  \(a=1.02\), but its finite-window zero fits are not reused as evidence.
- Paper 3 supplies the rigorous \(a=6\) symbolic/hyperbolic control.
- Paper 5 supplies finite-field arithmetic orbit data, but those data are not
  inserted into this operator.
- Paper 6 supplies the radial exponential Riemann--Weyl backbone.  Paper 7
  makes the Hénon deformation active in a static potential and adds an
  analytically admissible magnetic symmetry control.

This operator is a **Hénon-warped potential**, not a direct quantization of the
discrete Hénon Poincaré map.

## Recommended paper outline

1. **Introduction: an HP-motivated mean-count/symmetry testbed.**
   Q/W/S/R/C/P/Z labels, zero-input audit, and the prospective Route A/Route B
   framework with its non-preregistered historical boundary,
   theorem and experiment summary.
2. **Centered Hénon-warped operators.**  Model, fixed-point centering, roles of
   1.02, 6, and the radial control.
3. **Exact clock invariance.**  General sublevel-volume theorem and classical
   Riemann mean clock.
4. **Quantum two-term Weyl theorem.**  Self-adjointness, compactness,
   polynomial distortion, bracketing; technical details in appendices.
5. **Magnetic robustness and symmetry.**  Local gauge proof and centered
   reflection audit.
6. **Zero-input sampled classical dynamics.**  R000--R001 and independent
   magnetic R106.
7. **Quantum spectra and crossover.**  Failure-first R100 history, R101--R105
   refinement, R107/R107A independent-order stencil check, degeneracy and
   finite-window boundaries.
8. **The missing arithmetic bridge.**  Higher-resolvent spectral-shift
   container, first-resolvent obstruction, R200, and the prime-time mismatch.
9. **Conclusion.**  An HP-motivated mean-count/symmetry testbed, not a
   Hilbert--Pólya solution.

Appendices should contain the first-exit bootstrap, magnetic local count,
centered symmetry lemma, numerical protocols, and reproducibility manifest.

## Strongest reviewer objections and required responses

1. **The mean clock is designed.**  Agree; the contribution is to decouple
   and control the mean clock while independently activating geometry and
   symmetry.
2. **There is no prime trace.**  Agree; P is the central open gate and the
   reason the object is a testbed rather than a solution.
3. **The theorem does not choose 1.02.**  State it as a prior-fixed dynamical
   instance only.
4. **The remainder is much larger than zeta fluctuations.**  State that it
   preserves only the two growing terms.
5. **Classical chaos is not a theorem.**  R106 now supplies the independent
   integrator and magnetic control; still use “stable numerical evidence at
   sampled energies” because only four frozen trajectories at one main energy
   were checked adaptively.
6. **Only 140 interior levels and one underlying grid family.**  R107A now
   changes the leading truncation error and reproduces the result extremely
   closely, but it still shares the Cartesian/Peierls framework.  Enlarge the
   window and add a finite-element or sine-Galerkin calculation before a
   universality claim.
7. **The radial control is not Poisson.**  Call it a degeneracy control; use
   symmetry sectors or a nondegenerate integrable control in the next round.
8. **Magnetic \(B\) is not arithmetic.**  It is a symmetry knob, not a fitted
   number-theoretic constant.

## Next research frontier

The paper can now be drafted without any zero fit.  The relative spectral
route has established its first admissibility statement:

\[
 \operatorname{Tr}(f(H_1)-f(H_0))
 =\int f'(E)\xi(E)\,dE,
\]

with \(\xi=N_0-N_1\), a trace-class third resolvent-power difference, an
ordinary relative heat trace, and a tempered relative wave trace.  The
ordinary first-resolvent Krein condition is disfavored, not proved, because
its principal-symbol absolute integral diverges.

R200 now asks whether a localized relative wave trace has converged nonzero
physical-time peaks that match independently computed Hénon-warped periodic
orbits.  Even a positive R200 would pass only the periodic-orbit interface:
the arithmetic P gate still requires the system itself to derive
\(r\log p\) times and \((\log p)p^{-r/2}\) amplitudes before any comparison
with primes or individual zeta ordinates is authorized.
