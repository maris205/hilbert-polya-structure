# Batch plan: HCS-C339--HCS-C343

## Frozen contract

- Source commit: `e2d94f886963cbe3d42b83f6ef542413a163d3a4`
- Date / epoch: `2026-09-03` / `1788393600`
- Evaluator: `flow_systems/skills/route-a-evaluator.md` v0.2.0,
  SHA-256 `6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`
- Scope: `NO_BAD_EULER_OR_ROOT_NUMBER`
- Batch size: exactly five independent papers, followed by a user checkpoint

## Papers and theorem gates

1. **C339 Katok--Zermelo Randers sphere:** construct the nonreversible
   constant-flag-curvature metric on the round two-sphere from an equatorial
   Killing wind, prove the navigation description of every geodesic, and for
   irrational wind classify the two and only two oriented prime closed
   geodesics, their distinct periods, Jacobi monodromy, Poincare determinant
   and every rational, zero-wind, sign and convexity boundary.
2. **C340 one-gap Lame operator:** determine the complete real-line spectrum
   of `-d^2/dx^2+2 k^2 sn^2(x,k)` for `0<k<1`, including its three exact
   band edges, periodic/antiperiodic labels, pure absolute continuity and the
   fact that precisely one finite gap is open.  The analytic proof must use
   the explicit Bloch/finite-gap structure rather than extrapolate finite
   Floquet computations, and it must close the free and soliton limits.
3. **C341 switch--walk--switch lamplighter:** Walsh-diagonalize the complete
   finite Markov operator on lamps and walker over the cycle, identify every
   block with a killed lazy path or the intact cycle, give the full spectrum,
   multiplicities, characteristic polynomial, sharp gap and slow-mode
   multiplicity, and retain all small-cycle and randomization-convention
   boundaries.
4. **C342 directed edge reinforcement:** derive every finite path probability
   on a finite strongly connected directed multigraph having at least one
   outgoing labelled arc at every vertex, prove equality with
   the annealed law of an independent row-Dirichlet environment, close the
   conjugate posterior and prediction law, and prove the almost-sure edge and
   vertex occupation limits with their exact row moments.  Parallel arcs,
   outdegree-one rows and non-strongly-connected boundaries remain explicit.
5. **C343 Erlang-2 distributed delay:** convert the normalized gamma-memory
   equation exactly to a compatible three-dimensional linear chain, give the
   necessary and sufficient Routh stability region, exact Hopf factorization,
   frequency and transversal root crossing, count unstable roots beyond the
   wall, and classify repeated roots and every Jordan/zero/instantaneous
   limit without asserting nonlinear periodic-orbit birth.

## Uniform release gates

### G0 -- collision and ownership

Every package records primary source owners and nearest workspace neighbors.
The five systems are respectively a nonreversible Finsler geodesic flow, a
periodic finite-gap Schrodinger operator, a finite wreath-product Markov
chain, a reinforced path process in random environment, and a distributed
memory flow with an exact Markov realization.  `NEW` means only no existing
workspace owner, never literature priority.

### G1 -- analytic theorem and boundary closure

Headline completeness statements are proved analytically.  Finite evidence
tests formulas, normalization and implementation conventions; it is never
extrapolated to irrational-wind orbit exhaustion, an infinite-line spectral
theorem, all cycle sizes, almost-sure limits or an all-parameter root theorem.
Degenerate closed-orbit families, closed Lame gaps, small cycles, unvisited
Dirichlet rows and repeated delay roots are kept as theorem boundaries.

### G2 -- independent executable evidence

Every package has a canonical sorted-JSON producer with a self-excluding
semantic hash, a checker importing no producer code and independently
reconstructing the audited quantities, a separate symbolic lane, two isolated
byte-identical producer replays, and repaired-hash hostile mutations plus a
stale-hash control.

### G3 -- strict serialization and evaluation

JSON loaders reject duplicate keys and nonfinite constants.  Evaluation YAML
loaders reject duplicate or non-string keys, anchors, aliases, merges,
implicit timestamps, unknown or missing fields, type changes, tuple changes,
scope escalation and Route-B authorization.  Source baseline, fixed date and
epoch, evaluator digest, literal scope and every false claim flag are typed
invariants.  Python optimization modes are rejected wherever assertions form
part of an audit boundary.

### G4 -- hostile mathematical boundaries

The audits attack Randers orientation, wind sign, period denominators and the
strong-convexity wall; Lame modulus, edge ordering, Bloch parity and the claim
of only one open gap; lamplighter update order, fair resampling, killed-path
length and small-cycle convention; directed arc labels, rising factorials,
row denominators and annealed/quenched semantics; and Erlang kernel
normalization, feedback sign, Hopf threshold, strict inequalities and Jordan
sizes.

### G5 -- manuscripts and two revisions

Every package retains Round 0, Round 1 and Round 2 PDFs from one conditional
LaTeX source.  Both revisions add mathematical content.  Each round is built
twice in fresh directories with two LuaLaTeX passes at the fixed epoch and
must be byte-identical.  Settled logs are warning-free; every font is embedded
and subset; text sentinels and page rasterization pass; `paper/main.pdf` is
exactly Round 2.

### G6 -- exact package and scope closure

Each paper contains exactly 27 content-addressed manifest payloads plus one
self-excluded manifest, hence 28 physical files.  Every release script reruns
evidence, parser, replay, mutation and PDF gates.  All forbidden claim flags
are exact `false`.  Geodesic, Hill, Markov, reinforced-walk and delay data
remain source-local.

### G7 -- integration

The final root audit reruns all five release manifests twice, checks 135
manifest payloads and 140 physical package files, updates the global README
and both registries, inspects every final PDF page, runs whitespace and scope
audits, stages only this batch, synchronizes safely with origin, commits,
pushes, and stops for user confirmation before C344.
