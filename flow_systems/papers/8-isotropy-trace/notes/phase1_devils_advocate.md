# Paper 8 Phase-1 devil's-advocate mathematical audit

Date: 2026-08-14  
Mode: independent, read-only preregistration stress test; no web search and no
Phase-3 proof credit  
Protocol lock:
`51c85aae8262d6fb8597d49e6c23a1926ebb24ee3c3429d996228565b4d7a547`  
Candidate lock:
`d1d11519bd8661be1a62f5cf7bdc34e14a929a79776c52001b2a0d362082cc8a`

## Verdict

**REVISE — Critical 0 / Major 5 / Minor 3.**

No singleton defect disproves the proposed one-orbit isotropy theorem.  Phase 1
nevertheless cannot close: the present locks do not define one falsifiable
global trace object, one normalization chain, or one completion-level
nonnormality comparison.  Each Major item below requires a dated amendment and
independent exact-byte re-lock before Phase 2.

## Strongest counter-argument

The proposed local calculation is plausible precisely because it is a standard
periodic-action calculation; that does not yet show that the source packet owns
the desired positive-time prime ledger.  The locks move between a single
packet groupoid, an infinite packet union, an individual orbit, a Morita model,
compact-operator fibre images, and a regular von Neumann completion without
freezing the maps and domains that would make their traces one object.  The
displayed fibre trace is two-sided in the repetition index, while the advertised
ledger is one-sided.  The regular coefficient also depends on a chain of four
measure normalizations that is not recorded as a Weil identity.  Most
importantly, a scalar sum of fibre traces can exist even when the corresponding
global kernel is absent from the groupoid algebra or outside the trace's L1
domain.  In that case the project has recovered only a locally finite formal
distribution, not a source-owned groupoid trace.

There is also a stronger source-intrinsic alternative than the design currently
tests.  Exact common isotropy `L_p Z` makes the flow on `Gamma_p` factor through
the compact circle `K_p=R/(L_p Z)` with a free action.  Conditional on the
already required compact-Hausdorff and continuity gate, the intrinsic quotient
`Q_p=Gamma_p/K_p` is compact Hausdorff without any identification with `B_p`.
This does not select a canonical probability, but it changes the packet-level
measure and assembly problem.  A negative conclusion reached without testing
this quotient would be frame-locked toward the product-proxy obstruction.

## Findings

### CRITICAL

| # | Dimension | Finding | Evidence Anchor | Confidence |
|---|---|---|---|---|
| — | — | No singleton rejection-level defect identified at the preregistration stage. | text: protocol line 64 calls the formula a theorem target rather than evidence | 5/5; direct mathematical audit of both locks |

### MAJOR

| # | Dimension | Finding and required amendment | Evidence Anchor | Confidence |
|---|---|---|---|---|
| M1 | Object/domain consistency | The protocol freezes a per-prime object `G_p=Gamma_p rtimes R`, while the candidate lock assigns the same packet-level record the infinite union `X=disjoint_union_p Gamma_p`.  The unindexed global kernel `a_f(x,t)=f(t)` is then not shown to be in `C_c(G)` or in any global trace L1 domain.  Split per-packet and global-union candidate IDs; freeze whether the union has the inherited subspace topology or coproduct topology; use finite-prime-support kernels first; and add an explicit global trace-norm/summability gate.  A convergent scalar return series must not substitute for membership of one global operator in the trace domain. | absence: protocol lines 125–141 and candidate-lock lines 24–99 — expected distinct local/global IDs, topology, algebra, and L1 gate; checked typed records, frozen conventions, P8-3, P8-7, and stop rules | 5/5; groupoid support and semifinite-domain audit |
| M2 | Positive-time ownership | The proved target is the two-sided formula `L sum_(r in Z) f(rL)`, but the assembled record silently becomes `sum_(r>=1)`.  No restriction, projection, orientation convention, or test class performs that passage.  Freeze the operation explicitly—for example, restriction to test functions supported in `(0,infinity)`—and state that the one-sided class is not a star-subalgebra and the resulting positive-time distribution is not itself a C*-trace.  Zero and negative time must remain visible in the parent trace record. | equation: research-protocol lines 223–227 versus candidate-lock lines 89–98 | 5/5; Fourier/trace-domain audit |
| M3 | Haar/measure/Plancherel normalization | The locks mention time Haar `dt`, normalized orbit probability `du/L`, and a dual integral `dtheta/(2pi L)` under the single label “isotropy-Haar average.”  Normalized Haar probability `dtheta/(2pi)` is a different normalization.  Freeze the range- or source-fibre Haar convention and the exact Weil identity linking `dt`, `du/L`, isotropy Haar, and dual Plancherel measure; derive the regular trace coefficient from that chain.  Any scalar mismatch must be a reported result, not repaired by rescaling after comparison. | text: protocol lines 57–65, 163–174, and 233–249; candidate-lock lines 39–45 and 100–119 | 5/5; harmonic-analysis normalization audit |
| M4 | Completion and nonnormality object | The trivial-character functional alternates between a trace on a groupoid C*-algebra, a compact-operator image, and a candidate compared with the regular von Neumann completion.  P8-2 permits isomorphism, stable isomorphism, Morita equivalence, or measurable decomposition without specifying which is sufficient.  Freeze separate objects for `C*(G)`, `C*_r(G)`, `pi_theta(C*(G))`, and `M_reg`; record every quotient/embedding; require proof that the pulled-back fibre trace descends to the same reduced algebra represented in `M_reg`.  “No normal extension” must be stated only along that fixed embedding.  Morita equivalence alone cannot close this comparison. | absence: protocol lines 98–102 and 257–272 plus candidate-lock lines 60–83 and 140–149 — expected fixed algebras, maps, and extension diagram; checked all completion, trace, and P8-2/P8-5/P8-6 clauses | 5/5; operator-algebra ownership audit |
| M5 | Ignored intrinsic quotient path | Because every point of `Gamma_p` has isotropy `L_p Z`, the action factors through the free compact action of `K_p=R/(L_p Z)`.  Conditional on the protocol's own compact-Hausdorff/continuity gate, `Q_p=Gamma_p/K_p` is an intrinsic compact Hausdorff orbit quotient even though `Q_p ≅ B_p` is unproved.  Add `Q_p`, its quotient map, and the induced family of invariant measures from probabilities on `Q_p` as a separate source-derived candidate; P8-1/P8-7 must test it before using product-chart failure to declare packet assembly not testable.  This path does not create a canonical transverse probability or cross-prime mass, so those gates remain open. | absence: protocol lines 87–105, 179–202, and 273–280 — expected the quotient forced by common isotropy; checked in-scope objects, typed records, orbit conventions, and packet assembly target | 5/5; compact-group action and same-object audit |

### MINOR

| # | Dimension | Finding and required clarification | Evidence Anchor | Confidence |
|---|---|---|---|---|
| m1 | Provenance language | Call the transformation groupoid a canonical new construction from the source-defined flow, not an object defined in Deninger's source.  Record its evidence class as a new definition; source ownership of packets and clocks does not by itself award groupoid/trace credit. | text: protocol lines 9–17 and 40–45; candidate-lock lines 7–9 and 138–145 | 5/5; source/derivation boundary audit |
| m2 | Target contamination | “Target contamination is impossible” is too strong for a design motivated by the known return/Euler ledger.  The defensible claim is that no target zero, Euler equality, or fitted phase/mass/normalization is admitted as evidence after the freeze.  Keep the all-character family and arbitrary/composite-clock controls, and state that algebraic distinguishability of `chi_0` does not by itself make its trace source-selected. | text: protocol lines 31–38, 60–74, 303–337, and 425–426 | 4/5; preregistration and confirmation-bias audit |
| m3 | Route scope wording | The headers say “A0–A3 only,” while the operative rules deny every record A3 credit.  Distinguish “A3 is audited and expected to fail/not be reached” from “A3 credit is in scope,” so an exact return formula cannot be presented as partial A3 progress. | text: protocol lines 5–7 and 368–381; candidate-lock lines 3–5 and 152–155 | 5/5; Route namespace audit |

## Observations that are not defects

- The displayed Poisson sign is algebraically consistent with the displayed
  Fourier transform and shifted-frequency target; the induced-representation
  sign still correctly remains a proof obligation.
- Haar systems, invariant unit measures, normal FNS traces, and lower-
  semicontinuous C*-traces are intentionally distinguished in prose.
- The locks do not equate Morita equivalence with isomorphism and explicitly
  withhold determinant, A4, and Route-B credit.
- Zero data and fitted spectral statistics are excluded, and the arbitrary-
  clock and composite-clock controls correctly test arithmetic blindness.

## Mandatory Phase-1 amendment checklist

1. Split the per-prime and global-union groupoids and freeze their topologies,
   algebras, kernels, masses, and L1/trace-norm domains.
2. Define the two-sided-to-positive-time restriction and type its output as a
   distribution rather than a full trace.
3. Add the full Weil/Haar/Plancherel normalization identity.
4. Add a full/reduced/image/Morita/regular-von-Neumann comparison diagram and a
   fixed extension statement for P8-6.
5. Add the intrinsic free compact quotient `Q_p` path and require its
   adjudication before a packet-level negative verdict.

After these amendments are exact-byte re-locked, the one-orbit
Floquet/cancellation hypothesis is suitable for Phase-2 source verification.
