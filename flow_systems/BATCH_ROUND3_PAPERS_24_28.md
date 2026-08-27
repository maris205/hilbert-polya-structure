# Papers 24--28 — Round-3 execution report

Date: **2026-08-27**

Batch: **one round / exactly five paper projects**

ARS state: **Stage 1 RESEARCH in progress for all five**

Proposal state: **Stage 1 Classical Flow Baseline / Route A A0--A1**

## Outcome

Round 3 produced one distinct paper-facing advance for every project.  It did
not assign a formal Route-A tuple, invoke Route B, authorize Stage 2 manuscript
drafting, or compare against a Riemann-zero target.

| Paper | Round-3 result | Evidence boundary |
|---|---|---|
| P24 Bianchi holonomy | Constructed an explicit rank-4 classical Schottky/Kleinian control.  Eight paired round disks satisfy all 28 exact separation inequalities and all eight generator/inverse conjugacy identities.  The marked cutoff contains 4,148 oriented cyclic classes, of which 4,092 are primitive and 56 are observed repetitions. | The control is a proved free, discrete, torsion-free, convex-cocompact, purely loxodromic **infinite-volume non-lattice**.  It is not a finite-volume, cusp-, covolume-, or length-matched Bianchi control; containment in a larger arithmetic ambient group is open.  The score comparison is only numerical. |
| P25 three-disk scattering | Replaced the nine-row Round-2 binary64 cross-check by a 100-digit direct physical ray-intersection/reflection return map with three finite-difference scales.  All **2,241/2,241** frozen rows are now `NUMERICALLY_CERTIFIED`; 2,232 previously open rows were closed. | The parity convention `tr(M_direct)=(-1)^word_length tr(M_paraxial)` explains 804 old failures; conditioning explains the other 1,428.  The generic half-density conclusion remains `NUMERICAL_OBSERVATION` and the control verdict remains `STOP_SCOPED / PROVES_TOO_MUCH`, not an arithmetic result. |
| P26 level-11 newform time change | Proved the oriented-owner law for `omega_f=2*pi*i*f(z)dz`: invariance under `Gamma_0(11)` conjugacy, sign reversal under inverse orientation, and linearity under repetition.  A finite exact regression checked 99 conjugacy rows and 44 translation-covariance rows. | This closes conjugacy/repetition ownership for the frozen one-form period.  It is not complete primitive-class enumeration and does not prove the proposed Hecke/Euler recurrence. |
| P27 congruence inverse-limit no-go | Completed a primary-source closest-prior audit.  Direct structural prior exists, so the project is narrowed from a broad novelty claim to the explicit `Gamma(3 n!)` factorial tower, its sign-sensitive residual proof, the 3-by-8 finite quotient ledger, and the finite-owner firewall. | `Per(M_infinity)=empty` remains a proved local A1 obstruction.  The paper must be presented as an explicit specialization/methods case study, not as the first general aperiodic hyperbolic laminated geodesic flow.  Failure to find the exact factorial chain in the frozen search is not a novelty proof. |
| P28 Bolza magnetic flow | Bound a source-compatible square-root connection on the even subsequence `N=2m` to the Kordyukov--Taimanov trace theorem.  The exact phase-space scaling `q=2p` preserves trace time and primitive/repetition owners.  Signed-field even-subsequence trace ownership is proved at the frozen shell; the positive/negative action signs are checked at fixed repetition index. | The theorem applies only to the frozen even-subsequence subtype.  Odd `N`, arbitrary flat twists, the zero-field theorem, a fixed `Delta^L`, and the full all-`N` family remain `OPEN/NOT_ESTABLISHED`.  The executable contract verifies scaling identities; it records, but does not machine-prove, the source theorem's hypotheses. |

## Reproducibility receipt

| Paper | Tests | Deterministic artifact | Final core/tree SHA-256 |
|---|---:|---|---|
| P24 | 9/9 | two builds plus `--verify-existing` | `3fa2c5df0093a89da7fe92234c7cbfe900e641caf72ced8019e5240073f81d8a` |
| P25 | 7/7 | full second 100-digit replay, byte-identical | `78bb657056717711c49f67fe89fe13616421ea9e145ff12c3b0e63fba25f1534` |
| P26 | 5/5 | two byte-identical builds | `a3e71f86124ec8ae58f3971002fd3e0f11a0f06ccf3851e1f4ed4fad25d03841` |
| P27 | 5/5 | carry-forward owner ledger rebuilt twice | ledger `811c53a24e34def2b7fbb9353ccd568dd638a9c57706443626091bc4c23e09de` |
| P28 | 8/8 | two byte-identical contract builds | `a28bf68d0da5c34350224031428f18f325af0d11619df95f2509741475275f3d` |

The final project receipts therefore record **34/34 tests passed** and a
deterministic validation path for all five projects.  P25's full numerical
replay is the expensive member of the batch; the other four rebuild quickly.

## P28 adversarial-review closure

The first independent P28 review found no critical issue but identified two
major source-to-project ownership gaps and four minor presentation/validation
gaps.  The second pass confirmed both major findings closed, then isolated
three final minor inconsistencies.  Round 3 closes them as follows:

1. the time-reversal pairing is `(h,k) -> (h^(-1),k)`, so `h^k` is paired with
   `h^(-k)` without a double reversal;
2. the generated provenance boundary is
   `SOURCE_THEOREM_HYPOTHESES_NOT_MACHINE_VERIFIED` with a separately recorded
   primary-source check; and
3. the project README now states that the observable *is covered by* the source
   theorem after the exact reindexing `m=N/2`.

The eighth unit test locks the fixed-`k` positive/negative action-sign pairing.

## Route-map correspondence

The governing files remain `skills/route-a-evaluator.md` and
`skills/route-b-evaluator.md`.  Round 3 strengthens prerequisites and evidence
inside A0--A1; it does not silently convert local results into formal evaluator
verdicts.

| Route item | Batch status after Round 3 |
|---|---|
| A0 — arithmetic provenance / naturality screen | Sharpened separately for all five: arithmetic Bianchi source with a non-lattice control (P24), source-absent negative control (P25), intrinsic level-11 form (P26), congruence tower (P27), and source-compatible magnetic subtype (P28). |
| A1 — primitive object, repetition, clock, and owner | Strengthened by the Schottky cyclic ledger, direct billiard stability certificate, newform conjugacy theorem, inverse-limit no-period theorem plus owner firewall, and source-bound even-subsequence magnetic trace owner.  Each result retains its stated finite/subtype boundary. |
| Formal `(A0,A1,A2,A3,A4)` tuples | **0/5 assigned**.  Local proofs and controls are not formal tuple entries until a complete evaluator input is frozen. |
| A2--A4 | **Not evaluated for all five**.  No global rational-prime trace identity, analytic continuation credit, or completed target match is claimed. |
| Route B | **0/5 evaluations run; 0/5 invocations**.  The existence of a natural operator in P28 does not trigger Route B. |
| Gates A--E / ARS Stage 2 | **Not reached / not authorized**.  All five remain research projects with paper spines, not completed manuscripts. |

Thus the batch is still in **Route A, Proposal Stage 1, chiefly A0--A1**.  The
gain is depth: each dynamical subtype now has a more defensible theorem,
negative result, source boundary, or reproducible ledger.  It is not a stage
promotion.

## Scientific interpretation

The strongest negative-control result is P25: a fully direct stability replay
shows that the half-density statistic persists in a deliberately non-arithmetic
open billiard and therefore cannot by itself earn arithmetic credit.  P27 also
improves by contraction rather than inflation: the source audit removes a broad
novelty claim before manuscript drafting.

The strongest new positive theorem shapes are P26 and P28.  P26 now owns its
time-change coefficient on oriented `Gamma_0(11)` conjugacy classes and their
repetitions.  P28 now has a legitimate source-to-project trace owner on one
precisely frozen even-subsequence subtype.  Neither theorem yet supplies a
rational-prime dictionary.

P24 supplies the batch's explicit hyperbolic non-lattice calibration, but the
control is not yet geometry-matched to the finite-volume cusped Bianchi host.
That mismatch is now explicit rather than hidden.

## Primary-source narrowing recorded in Round 3

P27's scope is constrained by the direct structural precedents of
Martínez--Matsumoto--Verjovsky
(https://arxiv.org/abs/0711.2307), Penner--Šarić
(https://arxiv.org/abs/math/0508476), and the finite-area regular-cover
inverse-limit setting of Alcalde Cuesta, Carballido Costas, Martínez and
Verjovsky (https://arxiv.org/abs/2411.18418).  These sources support the
narrowed case-study framing; they do not establish that the exact factorial
chain has appeared before.

P28's subtype contract is bound to Kordyukov and Taimanov,
*Trace formula for the magnetic Laplacian on a compact hyperbolic surface*,
arXiv:2202.06055v3 (https://arxiv.org/abs/2202.06055).  The source binding is
part of Stage-1 research integrity, not Route-B credit.

## Smallest next artifacts

- **P24:** instantiate a genuinely finite-volume/cusp-aware non-arithmetic
  Kleinian comparison or formally show why the proposed matching variables
  cannot all be held fixed.
- **P25:** turn the completed 2,241-row direct-map result into the paper's
  negative-control theorem/limitations spine and freeze any next cutoff before
  computing it.
- **P26:** test an exact Hecke-recurrence consequence on owned conjugacy data
  against a norm-matched generic closed one-form control; failure is a valid
  kill result.
- **P27:** write the explicit factorial-tower proposition and owner-firewall
  proof in comparison with the identified prior, without reviving the rejected
  broad novelty claim.
- **P28:** enumerate a primitive Bolza magnetic-orbit ledger with the frozen
  trace/physical clocks, then instantiate the metric-matched non-arithmetic
  control before seeking any arithmetic-specific effect.

No public release, submission, external contact, formal Route promotion, or
Stage-2 manuscript start is authorized by this report.
