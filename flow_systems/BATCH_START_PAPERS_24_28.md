# Papers 24--28 — Stage-1 batch start

Date: **2026-08-26**  
Batch: **one round / exactly five paper projects**  
ARS state: **Stage 1 RESEARCH in progress for all five**  
Proposal state: **Stage 1 Classical Flow Baseline / Route A A0--A1**

## Authorization and governing constraints

The batch is started under the scholar's exact instruction:

> 1就行，注意结论概要写入readme.md，及时同步git，另外，每个论文要有明确的进展，一轮5个论文，开始下一轮就行，注意路线图的阶段，还有动力学系统的初始限定，大胆假设，变换不同的子类型就行

The governing route files are `skills/route-a-evaluator.md` and
`skills/route-b-evaluator.md`.  The initial dynamical restrictions are those in
`propose-flow-systems.md`:

- the primary object is a genuine continuous-time flow;
- phase space, generator, clock, primitive object, repetition law, arithmetic
  source, analytic object, and data split are frozen before target comparison;
- no prime or Riemann-zero table enters the definition, selection, cutoff, or
  parameter choice;
- no roof length `log p` or von Mangoldt weight is inserted by hand;
- a bold hypothesis is labeled `HEURISTIC` until a source or proof closes it;
- generic-chaos, shuffled-label, neighboring-parameter, simpler-parent, and
  proves-too-much controls are part of the falsification contract;
- Route B is not invoked merely because a natural quantum operator exists.

## Five projects and concrete progress

| Paper | Continuous-time subtype | Concrete Stage-1 progress now recorded | Route-stage position |
|---|---|---|---|
| P24 Bianchi holonomy | finite-volume cusped hyperbolic 3-flow | proved a self-contained level-`(3)` neat/torsion-free lemma; froze complex length, cusp/scattering obligations, and `Q(i)` Dedekind-zeta prime-ideal ownership | Proposal Stage 1 / A0--A1 screen; tuple unassigned; Route-B evaluation not run and invocation disallowed |
| P25 three-disk scattering | open hyperbolic billiard flow | proved the frozen `d=6a` geometry is safely no-eclipse; separated exact multiple-scattering determinant from semiclassical orbit zeta; internally prespecified it as the non-arithmetic control | Proposal Stage 1 / A0 negative control; source absent by construction; half-density test open; tuple unassigned |
| P26 level-11 newform time change | smooth positive time change of a geodesic flow | corrected `rho` to a time-density/slowness factor with speed multiplier `1/rho`; proved the positivity interval and exact first period variation; removed the unsupported “standard modular symbol” label | Proposal Stage 1 / A0--A1 screen; tuple unassigned; Route-B evaluation not run and invocation disallowed |
| P27 congruence inverse-limit no-go | inverse-limit geodesic lamination | proved the residual normal tower's total-space flow has no periodic points, including the compatible-lift, normality, and `PSL_2` intersection steps | Proposal Stage 1 / A0--A1; `PROVED_A1_OBSTRUCTION` is an informal mapping only; tuple and overall verdict unassigned |
| P28 Bolza magnetic | magnetic Hamiltonian/contact flow plus tensor-power quantization | proved degree/flux normalization, replaced the nonexistent global potential by connection holonomy, and froze `H_N=Delta^{L^N}` on `L^2(Sigma_B,L^N)` as `N->infinity`; fixed `Delta^L` remains a separate open candidate | Proposal Stage 1 / A0--A1 plus non-credit semiclassical architecture note; Route B not invoked |

## Subtype diversity

The five objects deliberately vary the mechanism while preserving continuous
time:

1. arithmetic cusped geodesic flow with complex holonomy;
2. non-arithmetic open scattering flow as a negative calibrator;
3. source-derived smooth time change on an arithmetic modular surface;
4. a noncompact inverse-limit lamination yielding a periodic-orbit no-go;
5. a compact magnetic Hamiltonian flow with a changing semiclassical
   tensor-power operator family and a separately tracked fixed candidate.

This is not five cosmetic parameter variants of one codebase.  The subtype
switch changes the owner of time, orbit phase, compactness, analytic surface,
and available falsification theorem.

## Bold hypotheses and kill gates

| Paper | `HEURISTIC` hypothesis | First kill gate |
|---|---|---|
| P24 | complex-length holonomy plus Gaussian arithmetic may yield an intrinsic prime-ideal local factorization | shuffle holonomy angles at fixed lengths and compare a matched non-arithmetic Kleinian ledger; no canonical orbit/prime map means stop |
| P25 | instability half-density can look arithmetically suggestive for entirely generic reasons | vary `d/a` through 5.8, 6.0, 6.2 and compare shuffled/random/composite labels; persistence certifies `PROVES_TOO_MUCH` rather than success |
| P26 | first variation of the time-changed zeta may expose a Hecke/Euler decomposition | replace the newform one-form by a norm-matched generic bounded observable and permute orbit periods; no exact Hecke recurrence means stop |
| P27 | renormalized finite-level zeta data might survive even though the inverse-limit flow has no closed orbit | distinguish a finite-level projective statistic from a zeta owned by the limit flow; any conflation is rejected immediately |
| P28 | minimal nonzero flux may produce arithmetic-specific phase cancellation in a source-bound tensor-power trace regime | compare `b=0,+1/2,-1/2` at common `N`, bundle degree, energy window, and trace regime, plus a matched non-arithmetic metric; topology/flux-only persistence fails A0 |

## Stage and route receipt

```text
NEXT_ROUND=P24-P28
ARS_STAGE_1_PROJECTS_IN_PROGRESS=5/5
FINAL_INITIALIZATION_AUDIT=PASS
PRIOR_FINDINGS_CLOSED=10/10
STAGE_1_PROJECTS_READY_FOR_NEXT_ARTIFACT=5/5
PROPOSAL_STAGE=1_CLASSICAL_FLOW_BASELINE
ROUTE_A_SCOPE=A0-A1
FORMAL_ROUTE_A_TUPLES_ASSIGNED=0/5
LOCAL_THEOREM_PROGRESS=P27_PROVED_A1_OBSTRUCTION_INFORMAL_MAPPING
P27_FORMAL_ROUTE_A_STATUS=UNASSIGNED
P27_A2_A4=NOT_EVALUATED
NEGATIVE_CONTROL=P25_A0_SOURCE_ABSENT_BY_CONSTRUCTION_HALF_DENSITY_TEST_OPEN
ROUTE_B_INVOCATIONS=0
ROUTE_B_INVOCATION_ALLOWED=false
GATES_A_E=NOT_REACHED
MANUSCRIPTS_COMPLETE=0/5
```

The absence of a formal tuple is intentional: object and falsification
contracts are frozen, but the requested primitive ledgers and controls have not
yet been executed.  P27's no-periodic-orbit theorem supports the local tag
`PROVED_A1_OBSTRUCTION`; because the formal evaluator input has not been
assigned, it is not the formal verdict `A1_FAIL`, and A2--A4 remain unevaluated.

## Next executable artifacts

- P24: exact word-cutoff complex-length/holonomy ledger with cusp-risk column.
- P25: exhaustive primitive cyclic disk-word ledger through topological length
  12 for `d/a=5.8,6.0,6.2`.
- P26: primitive hyperbolic-class ledger with `length`, newform period,
  first-variation coefficient, and generic-observable controls.
- P27: finite-level reduction-order table, kept explicitly separate from the
  theorem that the inverse-limit flow itself has no periodic points.
- P28: tensor-family owner lemma followed by a symmetry-resolved ledger at
  common `N`, bundle degree, energy window, and trace regime for
  `b=0,+1/2,-1/2`; fixed-operator high-energy ownership remains separate and
  open.

Each project received an executed Round-2 artifact on 2026-08-27. The finite
ledger/control portions above landed; P28 stopped correctly at owner separation,
with the energy window and trace regime still unassigned rather than invented.
Numerical counts, claim boundaries, route-map correspondence and the 31/31 test
receipt are recorded in the
[Round-2 execution report](BATCH_ROUND2_PAPERS_24_28.md). This startup document
remains the frozen pre-execution contract.

## Primary-source screen

The 2026-08-26 source screen used original papers, journal records, arXiv, and
LMFDB.  The principal anchors are recorded in each project's Stage-1 research
brief.  The screen does not establish external novelty; it only validates the
frozen mathematical objects and separates established background from the five
new hypotheses.
