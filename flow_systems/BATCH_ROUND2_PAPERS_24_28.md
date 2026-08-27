# Papers 24--28 — Round-2 execution report

Date: **2026-08-27**
Batch: **one round / exactly five paper projects**
ARS state: **Stage 1 RESEARCH in progress for all five**
Proposal state: **Stage 1 Classical Flow Baseline / Route A A0--A1**

## Landed outcome

Round 2 executed one kill-gate artifact for each project, following the
next-artifact list in
[`BATCH_START_PAPERS_24_28.md`](BATCH_START_PAPERS_24_28.md). P28 deliberately
stopped at owner separation before an energy window or trace regime was fixed;
that incomplete field is a result, not silently filled input. All five
artifacts are target-free: no prime table or Riemann-zero table was used to
define a system, choose a parameter, set a cutoff, or score an output. The
batch passed **31/31 tests**, and each artifact passed a deterministic replay
or byte-identity check.

| Paper | Frozen continuous-time subtype | Executed artifact | Landed result | Exact claim boundary |
|---|---|---|---|---|
| [P24](papers/24-bianchi-holonomy-flow/README.md) | cusped hyperbolic Bianchi 3-flow | exact Gaussian-integer reduced-word ball through length 5 plus fixed-length holonomy shuffle | 22,409 reduced words, 11,481 exact matrices, 10,944 primitive-within-sample candidates; 6/6 tests | finite elementary-generator sample only; full `Gamma((3))` generation, conjugacy completeness, primitivity and orbit-to-prime-ideal ownership remain `OPEN` |
| [P25](papers/25-three-disk-scattering-flow/README.md) | open three-disk billiard flow | all primitive oriented symbolic words through length 12 at `d/a=5.8,6.0,6.2`, with actual specular solves and controls | 747 words / 2,241 solved rows; neighboring half-density correlations exceed `0.9999985`; 6/6 tests | the tested instability statistic is `STOP_SCOPED / PROVES_TOO_MUCH`; this is not a formal A0--A4 verdict or an arithmetic-source result |
| [P26](papers/26-level11-newform-time-change/README.md) | positive newform-derived time change of a geodesic flow | exact positive-`LR` necklace ledger through length 9, newform-period variation proxy, generic observable and permutation controls | 125 parent necklaces, 11 level-11-selected representatives; 7/7 tests | finite positive-word ledger, not a complete `Gamma_0(11)` conjugacy ledger; Hecke/Euler interpretation remains `HEURISTIC / NOT_TESTABLE` |
| [P27](papers/27-congruence-inverse-limit-no-go/README.md) | inverse-limit congruence geodesic lamination | two-algorithm projective reduction orders for 3 frozen elements across 8 levels | 24/24 order cross-checks and 21/21 bonding checks; 5/5 tests | the finite-level owner is not the inverse-limit flow; the exact theorem `Per(M_infinity)=empty` remains the Route-relevant result |
| [P28](papers/28-bolza-magnetic-flow/README.md) | Bolza magnetic Hamiltonian flow with a tensor-power operator family | owner-separation lemma and `b=0,+1/2,-1/2`, `N=1,2,4,8` ledger | 12/12 owner rows validated; 7/7 tests | owner bookkeeping only; energy window, trace regime and same-owner primitive magnetic-orbit binding remain `OPEN/NOT_ESTABLISHED` |

## Route-map correspondence

The governing files remain [`skills/route-a-evaluator.md`](skills/route-a-evaluator.md)
and [`skills/route-b-evaluator.md`](skills/route-b-evaluator.md). Round 2 is a
Stage-1 evidence-building pass, not a route-promotion event.

```text
ROUND2_ARTIFACTS_EXECUTED=5/5
ROUND2_TARGET_FREE_ARTIFACTS=5/5
ROUND2_TESTS=31/31_PASS
ROUND2_DETERMINISTIC_REPLAYS=5/5_PASS
DISTINCT_CONTINUOUS_TIME_SUBTYPES=5
DIRECT_FINITE_ORBIT_OR_GEODESIC_LEDGERS=3/5
FINITE_TOWER_ALGEBRAIC_DIAGNOSTICS=1/5
OWNER_ONLY_LEDGERS_WITHOUT_ORBIT_DATA=1/5
PROPOSAL_STAGE=1_CLASSICAL_FLOW_BASELINE
ROUTE_A_SCOPE=A0-A1
FORMAL_ROUTE_A_TUPLES_ASSIGNED=0/5
A2_A4_EVALUATIONS=0/5
P25_LOCAL_CONTROL=STOP_SCOPED_PROVES_TOO_MUCH
P27_LOCAL_THEOREM=PROVED_A1_OBSTRUCTION
ROUTE_B_INVOCATIONS=0
ROUTE_B_INVOCATION_ALLOWED=false
GATES_A_E=NOT_REACHED
MANUSCRIPTS_COMPLETE=0/5
```

The two strongest discriminating outcomes point in different directions. P25
shows that a visually arithmetic half-density envelope survives generic
geometry and label controls too easily, so that statistic is stopped. P27
proves a genuine structural obstruction: the frozen inverse-limit flow has no
periodic points, and finite-level periodic data cannot be transferred to that
owner. P24, P26 and P28 delivered finite ledgers or ownership theorems, but
none yet supplies the complete primitive owner required for A1 promotion.

## Dynamical-system restrictions retained

The batch scopes five genuinely different continuous-time forms: a cusped
three-dimensional geodesic flow, an open billiard scattering flow, a smooth
time change on an arithmetic surface, an inverse-limit lamination flow, and a
magnetic Hamiltonian flow coupled to a changing tensor-power quantum family.
Round 2 directly computed finite orbit/geodesic ledgers for P24--P26, a
finite-tower algebraic diagnostic for P27, and an owner-only ledger with no
orbit or spectral data for P28. For each one, phase space, generator, clock,
primitive/repetition convention, arithmetic owner and negative controls remain
separately named. Finite truncations, proxies and changing-operator families
are never credited as the full target system.

## Paper-facing consequence and next smallest artifacts

The research output is being organized toward papers rather than a loose
experiment archive. At this checkpoint P25 has a clean negative-control paper
spine, and P27 has a theorem-first short-note spine; both still require a
closest-prior-result/novelty audit before drafting. P24, P26 and P28 remain
candidate papers whose next artifact must close a specific owner gap:

- P24: run the frozen matched non-arithmetic Kleinian control and either certify
  a complete group/conjugacy enumeration method or keep the word ball explicitly
  proxy-only.
- P25: perform the independent stability cross-check beyond the current 9 rows,
  then build a theorem/experiment manuscript outline around the stopped
  half-density statistic.
- P26: replace the finite positive-word sample by a certified
  `Gamma_0(11)` primitive-class owner or prove that the proposed Hecke recurrence
  is not testable from this construction.
- P27: complete the novelty audit and convert the no-periodic-orbit theorem plus
  owner-firewall experiment into a short manuscript outline.
- P28: freeze one source-backed energy window and trace regime before computing
  magnetic orbits; otherwise the owner ledger remains the terminal result.

No manuscript, formal Route-A tuple, Route-B entry, public release or submission
is claimed by this report.
