# P25 Stage 3 — Phase 0 Field Analysis and Proposed Review Panel

Date: **2026-08-29**

Mode: **ARS `reviewer_full`**

Status: **AWAITING SCHOLAR CONFIRMATION**

## Immutable review target

- Manuscript: `paper/manuscript.tex`
- Manuscript SHA-256: `283695c485a2a48abfab1ef0fe3d479f597f68f3082e20f4a5a1894ca37baefb`
- Rendered PDF: `paper/paper.pdf`
- Rendered PDF SHA-256: `2bff30f417741922bb2b28e3208dd08993f0a83a9511421283143ace22177c9e`
- Stage 2.5 status: `PASS AT MANDATORY CHECKPOINT`
- Review is read-only: reviewer outputs must not modify the manuscript.

No author-confirmed venue, track, article type, or ReviewTargetContext is
available. Every seat therefore uses `criteria_binding_unavailable`; this is
a field-general scientific review and makes no named-venue fit or
submission-readiness claim.

## Paper basic information

| Dimension | Result |
|---|---|
| Exact title | *Why a Unit-Roof Symbolic Determinant Does Not Transfer to the Physical Three-Disk Flow* |
| English abstract | 209 visible words by the current manuscript audit |
| English body | 4,055 words by the current manuscript audit |
| Rendered length | 12 pages |
| Bibliography | 8 entries; 8 cited; 0 orphaned |
| Primary discipline | Hyperbolic dynamical systems and open billiards, specifically three-disk scattering |
| Secondary disciplines | Symbolic dynamics and thermodynamic formalism; mathematical physics and quantum-chaotic scattering; numerical periodic-orbit computation |
| Research paradigm | Theoretical analysis with exact geometry and a high-precision computational certificate |
| Methodology type | Symbolic determinant theorem; periodic-orbit/cohomological obstruction; exact symmetric-orbit geometry; finite numerical orbit and return-map replay; typed negative-control analysis |
| Paper maturity | Pre-submission manuscript with complete proofs, object typing, computation, declarations, provenance package, clean build, and Stage 2.5 PASS; substantive Stage 3 review remains unexecuted |
| Criteria binding | `criteria_binding_unavailable` |

## Route boundary that every reviewer must preserve

- Typed unit-roof symbolic control remains
  `(A0_FAIL,A1_PASS_ANALYTIC,A2_ANALYTIC_DETERMINANT,A3_FAIL,A4_FAIL)` with
  overall status `ROUTE_A_REJECTED`.
- The physical three-disk flow tuple remains **unassigned** because scalar
  clock transfer is disproved.
- Symbolic A1/A2 credit cannot transfer to the physical flow.
- Route B is not invoked; no self-adjoint operator or spectral realization is
  supplied.

## Reviewer Configuration Cards

### Reviewer Configuration Card #1 — Journal-Fit Reviewer (`EIC`)

**Display role**: Journal-Fit Reviewer — field-general and venue-unbound

**Criteria binding**: `criteria_binding_unavailable`

**Identity description**: A senior handling editor familiar with rigorous
dynamical systems, mathematical physics, and computational negative-result
papers, assessing general contribution and readership without assuming a
venue.

**Review focus**:

1. Whether the nonconstant-roof and scalar-nontransfer theorems constitute a
   clear result with significance beyond correcting terminology.
2. Whether the positive symbolic determinant and half-density theorems remain
   correctly typed and separate from the physical-flow conclusion.
3. Whether readers from dynamics, scattering, and numerical mathematics can
   follow the exact, semiclassical, symbolic, and physical distinctions
   without overstatement.

**Will particularly care about**: Whether the two-witness obstruction has
sufficient conceptual and practical importance while avoiding a claim that
all symbolic modeling of the physical flow is impossible.

**Possible blind spots**: Will not independently inspect every solver
tolerance or adjudicate the sharpest formulation of roof cohomology.

### Reviewer Configuration Card #2 — Methodology / Certificate (`R1`)

**Criteria binding**: `criteria_binding_unavailable`

**Identity description**: A computational dynamical-systems specialist
experienced in periodic billiard orbit solvers, high-precision return maps,
conditioning audits, canonical symbolic enumeration, and reproducible
numerical certificates.

**Review focus**:

1. Completeness of the declared 747-owner symbolic census through length
   twelve, including orientation, cyclic canonicalization, primitivity, and
   replication across three geometries.
2. Two-solver agreement, visibility and reflection tests, direct return-map
   calculation, precision policy, and deterministic handling of the 39
   fallback rows.
3. The locked scalar-clock replay, exact-versus-numerical separation, 3/744
   per-geometry count, artifact hashes, tests, provenance, and verify-only
   behavior.

**Will particularly care about**: Whether `numerically certified` could be
mistaken for interval certification and whether fallbacks or tolerances bias
any conclusion assigned to the finite replay.

**Possible blind spots**: Will not assess the originality of the symbolic
determinant theorem or the exact quantum multiple-scattering determinant.

### Reviewer Configuration Card #3 — Domain / Theorem (`R2`)

**Criteria binding**: `criteria_binding_unavailable`

**Identity description**: A senior hyperbolic-dynamics researcher
specializing in dispersing billiards, subshifts of finite type, suspension
roofs, periodic-orbit cohomology, and thermodynamic formalism.

**Review focus**:

1. The no-eclipse hypothesis and exact construction of the symmetric
   period-two and period-three physical owners and their mean flight lengths.
2. The scope and logical sufficiency of the periodic-sum obstruction,
   no-owner-preserving-scalar-transfer theorem, and two-witness minimax bound.
3. The primitive-count and unit-roof determinant theorem together with use of
   Bowen--Lanford, Ruelle, and Livšic background.

**Will particularly care about**: The theorem excludes
constant-cohomologous roofs and a single scalar substitution; it must not be
read as excluding a genuine nonconstant-roof transfer operator.

**Possible blind spots**: Will not audit solver internals or the exact
quantum determinant in depth.

### Reviewer Configuration Card #4 — Quantum-Scattering / Operator Perspective (`R3`)

**Criteria binding**: `criteria_binding_unavailable`

**Identity description**: A mathematical physicist specializing in open
quantum chaos, hard-disk multiple scattering, semiclassical cycle expansions,
resonance determinants, and operator-versus-symbolic model distinctions.

**Review focus**:

1. The boundary among the finite adjacency determinant, a classical
   nonconstant-roof flow zeta, a semiclassical cycle-expanded object, and the
   exact multiple-scattering determinant.
2. Whether the hyperbolic half-density factorization remains a local
   stability identity and is never promoted to global determinant or
   arithmetic evidence.
3. The function-space, convergence, analytic-continuation, and approximation
   obligations of a legitimate physical-flow successor without Route-B or
   spectral-realization claims.

**Will particularly care about**: Shared collision words or resonance
language must not imply equality of weights, determinant spaces, clocks, or
spectra.

**Possible blind spots**: Will not scrutinize the finite owner enumerator,
Newton conditioning, or every roof-cohomology detail.

### Fixed fifth seat — Devil's Advocate (`DA`)

This fixed ARS seat receives no dynamic configuration card and also uses
`criteria_binding_unavailable`. It will ask whether the two-orbit obstruction
and `q`-symbol determinant family are sufficiently novel, challenge what the
2,241-row replay adds after the exact proof, and search for language that
silently broadens `no constant scalar transfer` into `no physical transfer
operator` or turns a local half-density identity into global evidence.

## Panel separation and next action

After scholar confirmation, the five seats will precommit categorical review
rules before seeing the manuscript. Manuscript-visible reports will run in
role-separated, peer-output-blind contexts with typed provenance. The shared
primary model-family correlation will be disclosed and will not be called
human or statistical independence. Phase 0 creates no manuscript mutation,
Route-A promotion, Route-B invocation, or named-venue claim.
