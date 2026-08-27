# Route-A independent cross-subtype batch plan: C204--C208

Status: **complete; five theorem owners released and batch-audited**.

Date: 2026-08-27

Source commit: `d108ef46fea7a8f62490a69071a83fcbda7c113b`.

Scope firewall: `NO_BAD_EULER_OR_ROOT_NUMBER`.

Evaluator authority: `flow_systems/skills/route-a-evaluator.md` version 0.2.0,
SHA-256 `6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`.

## Frozen sequence

1. **C204:** every finite-field linear endomorphism: rational-canonical fixed
   counts, periodic and transient decomposition, all cycles, zeta and the
   full-function Koopman characteristic polynomial.
2. **C205:** the non-sofic Dyck shift: context-free circular code, exact
   algebraic zeta, all fixed and primitive counts, entropy, dominant-pole
   asymptotics and branch-point/nonrational boundaries.
3. **C206:** Couette shear on `T x R`: exact Fourier semigroup, exact sector
   norm, cubic-time enhanced dissipation, inviscid mixing, periodic-state and
   trace-class stopping boundaries.
4. **C207:** one-dimensional Barenblatt profiles for every `m>0`: compact,
   Gaussian and algebraic-tail phases, exact Beta normalization and moments,
   threshold geometry and rescaled stationarity.
5. **C208:** continuous-time linear birth--death branching: exact all-state
   transition law, moments, three long-time regimes and every rate/population
   boundary.

Collision decisions and rejected alternatives are frozen in
`IDEA_REPORT_C204_C208.md`.

## Uniform paper contract

Each candidate releases exactly 28 physical files: 27 content-addressed
payloads plus one self-excluded manifest.  The payload comprises eight
theorem/writing documents, seven executable code/manifest files, one evaluator
YAML, seven paper artifacts including three content-distinct revision PDFs and
the final PDF, and four result/evidence artifacts.

Every package must pass a deterministic producer, a producer-independent
checker with recursive exact-schema closure, separate symbolic
reconstruction, canonical byte replay, repaired-hash semantic mutations,
unknown-key mutations and a stale-hash mutation.  Each paper receives two
substantive content revisions.  Every final PDF must reproduce byte for byte in
two fresh fixed-epoch LuaLaTeX builds from `main.tex`, embed and subset all
fonts, have clean logs and extractable text, and survive visual inspection of
every page.  Internal hostile checking is not external peer review.

## Proof and evidence contract

- C204 must retain repeated roots of `X^n-1` in characteristic `p`, singular
  primary factors, and the distinction between periodic-subspace dimension and
  total-state cycle data.  Finite-field arithmetic is not target local data.
- C205 must freeze edge-type conventions and distinguish finite admissible
  words from cyclic words whose bi-infinite repetition is admissible.  Series
  checks do not replace the circular-code proof or dominant-singularity
  argument.
- C206 must freeze its Fourier sign, retain the exact `1/12`, and keep the
  linear advection--diffusion owner separate from nonlinear Couette stability.
  A contraction semigroup on `T x R` is not automatically trace class.
- C207 must restrict uniqueness to the declared first-kind centered
  zero-flux self-similar class, treat `m=1/3` as a divergent second-moment
  equality boundary, and avoid using finite-second-moment entropy arguments
  where that moment is infinite.
- C208 must retain the survivor-binomial layer for multiple ancestors, keep
  probability generating functions distinct from dynamical zeta functions,
  and state each conditional/scaled limit with its atom and initial-population
  dependence.

## Integrity gates

ARS implementation-integrity and frame-lock audits cover source ownership,
hallucinated results, shortcut reliance, bug-as-insight risk and scope drift.
No paper may introduce target zero or prime tables, arithmetic local data,
Euler factors, root numbers, automorphy, target divisor/counting or functional-
equation claims, a Hilbert--Pólya operator, or Route-B input.  Native finite
zeta functions, PDE semigroups and probability generating functions remain
explicitly source-local.

## Completion condition

The round is complete only after all five executable suites, three-round paper
builds, fresh reproducibility/font/log/text/visual checks, manifests,
cross-package collision review, registries and README pass; the scoped commit
is pushed and verified equal to the remote head.  Exact counts and hashes are
then frozen in `BATCH_REVIEW_C204_C208.md` before the next user checkpoint.

Completion ledger: all five suites, 15 final-paper pages, 135 tracked payloads,
five self-excluded manifests, all fresh-build gates, and the internal theorem
cross-audits are closed in [`BATCH_REVIEW_C204_C208.md`](BATCH_REVIEW_C204_C208.md).
