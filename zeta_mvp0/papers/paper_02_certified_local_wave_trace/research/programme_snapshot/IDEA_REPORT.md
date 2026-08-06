# Breadth-First Hilbert--Pólya Candidate Portfolio

> **HISTORICAL / SUPERSEDED TAXONOMY.**  The five-gate scores and the uses of
> \`Z\` in the historical portfolio below predate the current claim ledger.
> They must not be read as evidence that any candidate has passed an
> arithmetic or zero-level test.  The authoritative taxonomy is now
> \`Q/W/S/P/Z\`, with finite-window random-matrix evidence recorded separately
> as side diagnostic \`R\` and relative-container admissibility as side
> diagnostic \`C\`.  For the present Hénon-warped family, \(P\) is open and
> \(Z\) is untested.  The old table is retained only as a provenance record of
> the pre-pilot stress test.

## Research mode

This portfolio implements the requested distinction between two styles of AI
mathematics:

- **RH / Route B:** generate structurally different objects, test cheap
  invariants, and kill most candidates early;
- **bridge closure / Route A:** write a conditional end-to-end channel, expose
  its minimum missing bridges, and attack those bridges rather than adding
  unrelated lemmas.

No candidate below is called a Hilbert--Pólya operator.  The purpose of the
portfolio is to locate objects that satisfy several necessary requirements
without fitting zeta ordinates.

## Historical five-gate scoring rubric (superseded)

| Gate | Question | Pass standard |
|---|---|---|
| Q | Is there a genuine quantum object? | A specified self-adjoint operator with real discrete spectrum, or an explicitly labelled deformation such as a spectral-shift pair. |
| W | Does the mean count have the right scale? | Both growing terms \(\frac{E}{2\pi}\log(E/2\pi)-\frac{E}{2\pi}\) arise analytically and survive quantization. |
| S | Is the Hénon/dynamical content active? | It changes invariant dynamics or spectral data and cannot be removed as a harmless representation choice. |
| P | Is arithmetic endogenous? | Prime powers and von Mangoldt-type amplitudes arise structurally, not by inserting a prime table or fitting zeros. |
| Z | Is there a credible fluctuation mechanism? | A trace, spectral-shift, or periodic-orbit mechanism can in principle carry the signed oscillatory term and the relevant symmetry class. |

The following historical scores ran from 0 (absent or incompatible) to 5 (rigorous or structurally
endogenous).  A high total never compensates for a zero at a necessary gate.
The scores below are from an independent skeptical stress test performed
before the first numerical pilot.

## Ranked portfolio

| Rank | Candidate | Route | Q | W | S | P | Z | Present role |
|---:|---|:---:|---:|---:|---:|---:|---:|---|
| 1 | Hénon-warped exponential Schrödinger operator | B | 5 | 4 | 3 | 0 | 1 | Strongest rigorous Q/W backbone |
| 2 | Self-adjoint spectral-shift pair | A | 5 | 5 | 2 | 2 | 3 | Best home for a signed explicit-formula fluctuation |
| 3 | Energy-dependent compensated Hénon suspension | A | 2 | 3 | 5 | 0 | 2 | Strongest route to genuinely active Hénon dynamics |
| 4 | Clock-normalized anisotropic exponential soft billiard | B | 5 | 4 | 1 | 0 | 2 | Same-clock search over chaotic shapes |
| 5 | Arithmetic roof suspension over Hénon symbols | A | 2 | 2 | 3 | 3 | 2 | Conditional prime-orbit channel |
| 6 | Finite-field/adelic Hénon graph operator | B | 4 | 1 | 4 | 4 | 0 | Arithmetic module, not yet an HP candidate |
| 7 | Quantum graph from a Hénon Markov partition | A/B | 3 | 1 | 4 | 2 | 3 | Exact trace language but wrong naive Weyl scale |
| 8 | Magnetic or spin Hénon deformation | B | 5 | 3 | 3 | 0 | 1 | Symmetry-class laboratory |
| 9 | Hénon FIO/direct-sum block operator | B | 3 | 2 | 5 | 0 | 2 | Engineering-control candidate |
| 10 | Hénon Ruelle/dynamical zeta | B | 0 | 1 | 5 | 2 | 3 | Periodic-orbit module, not self-adjoint HP |
| 11 | Growing-iterate Hénon warp | B | 2 | 2 | 5 | 0 | 2 | High-risk multiscale search |
| 12 | Floquet/log-cooling cocycle | B | 2 | 1 | 5 | 0 | 2 | Dynamical signal with an unbounded-count mismatch |

After the proof repair and independent mathematical audit, candidate 1 has a
project-internal Q/W theorem.  The table retains the pre-pilot independent
score of W=4 to avoid silently upgrading a stress-test score after the fact.

## Candidate cards and hard death criteria

### B1. Hénon-warped exponential Schrödinger family

\[
 \mathcal H_{a,n}=-\frac12\Delta
 +2\pi\exp\!\left(\pi|H_a^n(q)|^2\right).
\]

Area preservation gives the exact classical Riemann mean clock, while fixed
polynomial distortion permits an \(o(E)\) quantum remainder.  Its decisive
question is whether the warp produces a positive-measure chaotic component
at high energy.  Kill the S/Z branch if converged high-energy Lyapunov and
Poincaré diagnostics approach the radial control, or if converged spectra for
different \(a,n\) are indistinguishable.  It may remain valuable as a Q/W
  backbone even after that kill.  In the current taxonomy this is an \(S/R\)
  branch, not a \(Z\) test.

### A1. Spectral-shift pair

Let \(H_0\) supply the exact mean clock and let \(H_1\) contain an active
Hénon-derived deformation.  If a suitable resolvent difference is trace
class, the Krein spectral-shift function satisfies a relative trace formula

\[
 \operatorname{Tr}\bigl(f(H_1)-f(H_0)\bigr)
 =\int f'(E)\,\xi(E)\,dE.
\]

This is a deformation of Hilbert--Pólya, not a claim that one operator's
eigenvalues are the zeros.  It is attractive because \(\xi\) is signed,
unlike a counting function.  Kill it if every admissible Hénon perturbation
has a spectral-shift transform too smooth to support \(\log p\) singular
times, or if the primes must be entered term by term.

### A2. Energy-dependent compensated Hénon suspension

An implicit autonomous suspension can realize an energy-dependent local
Hénon scattering map exactly.  This keeps S active on a positive-density
family of flow boxes.  The stronger same-physical-section compensation with
half-order amplitude and uniform adapted \(C^1\) control is obstructed; it is
not an active conjecture.  Kill the remaining quantum branch if no uniform
canonical atlas and two-parameter quantization can be built without changing
the two growing Weyl coefficients.

### B2. Clock-normalized anisotropic soft billiards

For a proper shape function \(\Phi\) with

\[
 |\{q:\Phi(q)<t\}|=t+O(1),
\]

the potential \(2\pi e^{\Phi(q)}\) has the same two growing clock terms.  A
nonelliptic star-shaped gauge can be smoothed on a fixed compact core, which
changes only the \(O(1)\) part of the count.  This gives a cheap search over
soft-billiard shapes before forcing Hénon algebra into the operator.  Kill a
shape family if its high-energy chaotic fraction tends to zero, or if the
deformation needed for chaos changes either growing clock coefficient.

### A3. Arithmetic roof suspension

Use a certified Hénon symbolic subsystem and seek a roof whose periods and
stability weights generate prime-power trace data.  A database roof
\(r(p)=\log p\) is not a mechanism.  Kill the route if the von Mangoldt sign
and amplitude cannot be derived from an invariant cocycle or transfer
operator, or if the resulting flow has no relevant discrete self-adjoint
spectrum.

### B3. Finite-field/adelic Hénon operator

The reductions of \(H_a\) provide genuine arithmetic orbit data.  However a
permutation matrix has only roots of unity, and \(P+P^*\) only produces
\(2\cos(2\pi k/\ell)\).  Kill the naive construction unless a natural
Hecke-like coupling is found; also kill any infinite direct sum whose Riemann
clock comes only from hand-chosen block rescalings.

### A/B4. Quantum graph or Markov-partition hybrid

This route has an exact trace formula and active symbolic dynamics.  A finite
metric graph nevertheless has an \(O(E)\), not \(E\log E\), Weyl scale.
Kill it if repairing the scale requires prime-coded edge lengths, destroys
compact resolvent, or replaces derivation by dimension bookkeeping.

### B4. Magnetic/spin symmetry deformation

This is useful for GOE/GUE/GSE crossover experiments, especially for other
L-function families.  For the Riemann zeta target, exact \(T^2=-1\) produces
Kramers doublets and points toward GSE rather than the expected unitary class.
Kill it as a zeta mechanism if it supplies only symmetry statistics and no
prime trace.

### B5. Hénon FIO/direct-sum blocks

These objects can quantize the exact canonical map and are valuable negative
controls.  Kill them as HP candidates if the Riemann clock comes from chosen
block dimensions/offsets or if an arbitrary logarithm of unitary phases is
needed to manufacture an unbounded self-adjoint spectrum.

### B6. Ruelle zeta and resonances

Ruelle objects naturally encode Hénon periodic orbits but are generally
non-self-adjoint and have complex resonances, often with a fractal Weyl law.
They can feed the P/Z modules; they fail Q as direct HP operators.  Kill any
attempt to rename complex resonances as a self-adjoint spectrum.

### B7. Growing iterate and non-autonomous cocycles

Letting \(n=n(E)\) can amplify geometric complexity, but an
eigenvalue-dependent operator is not a linear operator.  A spatial-shell
replacement is admissible only if it is fixed in advance.  Kill the route if
derivative distortion becomes \(E^\delta\), shell interfaces cannot be
smoothed uniformly, or Floquet quasienergies modulo \(2\pi\) are used as an
unbounded Riemann count.

## Three frozen sub-two-hour pilots

1. **R000 warped-Hénon chaos pilot.**  Compare \(a=0,1.02,6\), fixed
   \(n=1,2,3\), and \(E=10^2,10^3\) using variational FTLE, energy drift,
   multiple deterministic microcanonical seeds, step/tolerance refinement,
   and a radial integrable control.  No zeta zeros are loaded.
2. **R010 chart-to-chart return pilot.**  Compute
   \(S_{E,j}=P_{E,j}^{-1}\widetilde H_a\) only after freezing entrance/exit
   Darboux charts.  Audit symplectic defect, derivatives through order three,
   compensation one-forms, and energy scaling.  The already proved A9
   obstruction prevents interpreting an expected displacement blow-up as a
   coding bug.
3. **R020 normalized soft-billiard pilot.**  Compare circular, elliptic, and
   smooth nonelliptic star-shaped boundaries with equal sublevel-area slope.
   Measure FTLE/SALI and chaotic phase fraction before any spectral fit.

## Early aspirational selection rule and current status

Paper 7 should proceed with

\[
 \boxed{\text{strict Q+W backbone}
 +\text{Route B chaos screening}
 +\text{Route A spectral-shift/return bridges}.}
\]

The next promotion threshold is not a visually interesting orbit.  The early
proposal required B1 or B2 to show a converged positive-measure chaotic
component, while A1 had to pass a trace-class and nontriviality audit.  The
positive-measure requirement has **not** been met, and this document was not a
preregistered tournament that historically selected Paper 7.  The manuscript
proceeds instead on its Q/W theorem with explicitly sampled S support; R is a
finite-window side diagnostic, C is an admissibility statement, and P/Z remain
the central Hilbert--Pólya gaps.
