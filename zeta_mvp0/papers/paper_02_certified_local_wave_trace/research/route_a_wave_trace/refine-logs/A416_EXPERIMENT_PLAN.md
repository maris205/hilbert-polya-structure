# A4.16 phase-anchor experiment plan

Date: 2026-08-09 (UTC)  
Protocol state: `R401-VAL-L3-S0-DRAFT` / non-licensing

## Claim--experiment matrix

| ID | Claim | Required evidence | Promotion if passed |
|---|---|---|---|
| A4.16a-outer | every constrained local-tube shell point lies in the finite angle-tree box | outward slow/momentum bounds plus the exact singular-value inequality giving `abs(Q_plus)<0.18` | implementation prerequisite only |
| A4.16a-angle | on `K=1`, `r_minus<=0.06`, the fast plane avoids the origin and `0 < theta_dot < 18` | directed state-space tree with exact dyadic replay | phase-anchor lemma on tested slabs |
| A4.16a-land | every positive fast turning point in the tube has `0.12 < Q_plus < 0.17` and positive section slope | constrained section-energy tree and independent replay | landing in the A4.15 root box |
| A4.16b-tube | the accepted fast branch stays in `r_minus<0.04` for its whole period | CAPD multiprecision `SolutionCurve` cover of every normalized phase cell | branch membership in the A4.16 candidate class |
| A4.16-quot | the tube-contained periodic candidate quotient has one element | analytic winding/flow-box reduction plus A4.15 | local orbit uniqueness modulo time shift, conditional on whole-orbit tube residence |

## Primary hypothesis

For each \(\epsilon\in[0,0.101]\), any \(K_\epsilon=1\) periodic orbit with
period in \([0.64,0.69]\) that remains in \(r_-<0.06\) for its complete
period is the accepted fast branch modulo time translation.  The fast branch
itself remains in \(r_-<0.04\).

## Anti-claim

A4.16 does not assert that all energy-shell periodic candidates remain in the
local tube.  That routing statement belongs to the future global exclusion
cover.  A result that proves only the accepted branch stays in the tube is
not enough to establish phase completeness for arbitrary candidates.

## Evidence already available

- A4.12: one accepted fast branch over all 51 slabs.
- A4.15: exactly one reduced return root in the fixed local section box.
- Nonrigorous \(2^{20}\)-point scouting: fast angular rates approximately
  9.30--9.66 on sampled constrained states, versus the planned ceiling 18.
- Nonrigorous branch-center integration: maximum sampled slow radius about
  0.01025, versus the planned rigorous ceiling 0.04.
- A provisional 128-bit Arb state-space tree closed 80,959 nodes with no
  unresolved leaf.  Because it was inline, unfrozen, and independently
  unchecked, it is not a proof artifact.
- The existing pure-Arb whole-box Taylor flow wraps to slow-radius enclosures
  near 0.4 and is unsuitable for A4.16b.  CAPD `SolutionCurve` is the selected
  validated alternative.

## Run sequence

### R000 — deterministic local engineering replay

1. Archive the static outer, angle, and landing algorithms in scripts rather
   than inline commands.
2. Run a single 128-bit full-parameter diagnostic directory.
3. Require zero unresolved leaves and record exact minima/maxima only as
   outward interval endpoints.
4. Run an independent checker that does not import the producer.

R000 remains `DRAFT_NON_LICENSING`; it is used only to expose schema,
wrapping, and budget failures.

### R001 — representative S0 smoke

Run the exact matrix

\[
 \{S000,S025,S050\}\times\{128,256\}.
\]

Each composite cell must contain:

- outer-domain proof;
- fast-angle tree;
- positive-section landing tree;
- continuous CAPD branch-tube cover;
- canonical hashes and raw transcripts.

The no-production-import checker for each component must pass every matrix
cell. The static component reports `PASS_STATIC_COMPONENT_SMOKE` with
`component_scope=STATIC_ONLY` and `composite_s0_passed=false`; the CAPD branch
component reports `PASS_NON_LICENSING_BRANCH_TUBE_SMOKE`. Only a separate
checker that binds both component archives over the identical six-cell matrix
may report `PASS_IMPLEMENTATION_SMOKE` with
`component_scope=COMPOSITE_S0`, `composite_s0_passed=true`, and
`final_status=null`.

### R002 — independent pre-freeze review

Before any all-slab execution, an independent reviewer must audit:

- the angle identity and winding argument;
- exact constrained-domain coverage and boundary conventions;
- the L1 box binding and continuous trajectory quantifier;
- producer/checker schema independence;
- crash/resume, write-once, symlink, duplicate-JSON, and type-strict behavior;
- exact 51-slab by two-precision production matrix and resource limits;
- all non-promotion language.

Only an explicit acceptance permits a new `R401-VAL-L3-A1` freeze.

### R003 — prospective all-slab production

After freeze, run 51 slabs independently at 128 and 256 bits.  No threshold,
split rule, input hash, CAPD binary, or checker code may change after first
dispatch.  Production may promote only to a local phase-tube status such as
`PASS_LOCAL_PHASE_TUBE`, never to a global or Hilbert--Polya programme status.

## Metrics and mandatory outputs

For each static proof tree:

- root-domain exact endpoints;
- total/internal/terminal counts and maximum depth;
- counts by classification;
- for each `ANGLE` tree, the weakest positive lower endpoint of \(D_+\),
  \(N_+\), and \(\omega_+N_+\), plus the largest upper endpoint of
  \(\dot\vartheta_+\);
- exact tree root and manifest hash;
- unresolved count, which must be zero.

For each branch cover:

- exact L1 slab/root-box hashes;
- number and exact union of phase cells;
- largest independently recomputed rigorous upper endpoint of \(r_-^2\) and
  its margin below \(0.04^2\);
- CAPD commit, flags, source and binary hashes;
- raw stdout/stderr and return code;
- unresolved phase cells, which must be zero.

For the aggregate checker:

- exact matrix identity;
- per-record and aggregate hash roots;
- replay count and explicit failure list;
- cross-precision domain agreement;
- local milestone value and null final programme value.

## Falsifiers and kill conditions

The route is stopped or reframed if any of the following occurs:

1. the constrained energy shell reaches the fast-plane origin;
2. \(N_+\) can be nonpositive or the rate ceiling cannot be placed below
   \(4\pi/0.69\);
3. a positive turning point can fall outside the A4.15 chart;
4. the known branch cannot be enclosed in \(r_-<0.04\);
5. a proof needs midpoint sampling, tolerance-based boundary repair, or an
   unbound raw transcript;
6. 128/256 results disagree on a domain verdict;
7. the claimed conclusion drops the full-period tube assumption.

## Resource plan

The static pilot is expected to use far less than 1 GiB and seconds to
minutes per matrix cell.  CAPD branch covers are expected to dominate but
have a large geometric margin.  Use at most 24 workers on the 32-vCPU host,
pause above 48 GiB cgroup memory, and pause below 150 GiB free disk.  Resource
exhaustion is an inconclusive outcome, not scientific evidence.

## Decision rule

- **Component pass:** preserve the static and CAPD results under their
  component-only non-licensing values; neither one is a composite result.
- **Smoke pass:** all six cells pass in both independently checked component
  archives and the composite checker binds them; publish only
  `PASS_IMPLEMENTATION_SMOKE` with a null final programme value.
- **Smoke inconclusive:** any unresolved/budget/tool failure; revise only in a
  new attempt directory and re-review before production freeze.
- **Mathematical falsification:** a rigorously surviving state violates an
  angle, landing, or branch-tube inequality; narrow or abandon the proposed
  A4.16 theorem rather than tuning around it.
