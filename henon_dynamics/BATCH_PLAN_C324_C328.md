# Batch plan: HCS-C324--HCS-C328

## Frozen contract

- Source commit: `1aba1f6fd0cf81baa7c137a2ce7ce3d097ba63fc`
- Date / epoch: `2026-09-03` / `1788393600`
- Evaluator: `flow_systems/skills/route-a-evaluator.md` v0.2.0,
  SHA-256 `6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`
- Scope: `NO_BAD_EULER_OR_ROOT_NUMBER`
- Batch size: exactly five independent papers, followed by a user checkpoint

## Papers and theorem gates

1. **C324 Hunter--Saxton:** prove the exact characteristic Jacobian and
   pulled-back slope for every nonconstant periodic `C2` datum, the maximal
   classical lifespan, exact breaking labels and universal blow-up rate,
   retaining energy, constant-data, multiple-minimum and reverse-time faces.
2. **C325 Moser--Tardos:** prove the proper witness-tree probability and
   branching bounds, eventwise and total expected resampling bounds,
   almost-sure termination and correctness for every legal selection rule in
   the finite variable model.
3. **C326 two-site inclusion:** prove beta-binomial reversibility, the entire
   simple Hahn spectrum, exact semigroup kernel, sharp gap and `L2` decay,
   with the zero-mass, one-particle and zero-attraction boundaries closed.
4. **C327 Kronig--Penney:** derive the self-adjoint Floquet fibres and exact
   discriminant, prove pure absolute continuity and the spectrum criterion,
   close all coupling/energy band chambers, and derive indexed IDS/DOS and
   high-energy gap asymptotics.
5. **C328 harmonic run-and-tumble:** prove the velocity-resolved beta
   stationary law and all joint polynomial moments; derive the complete
   stationary `2 x 2` correlation matrix with its `t>=0`, negative-lag and
   Jordan conventions; and classify every finite polynomial filtration,
   including odd-Jordan/even-semisimple resonance and the zero-speed
   semisimple boundary.

## Uniform release gates

### G0 -- collision and ownership

Each paper cites historical source owners and records its nearest workspace
collisions.  The five systems are a nonlinear PDE, a randomized constraint
algorithm, an attractive interacting-particle chain, a periodic singular
quantum Hamiltonian, and a confined active-matter PDMP.  Workspace novelty is
never presented as literature priority.

### G1 -- analytic theorem and boundary closure

Headline statements are proved analytically; finite evidence tests formulas
and conventions.  The Hunter--Saxton integrated constant and gauge,
resampling-table and dependency conventions, inclusion rate/parameter
normalization, delta-jump and quasi-momentum conventions, and run-and-tumble
transport/switching normalizations are explicit and immutable.

### G2 -- independent executable evidence

Every package has a canonical sorted-JSON producer with a self-excluding
semantic hash, a checker importing no producer code and independently
reconstructing all audited values, a separate SymPy lane, two isolated
byte-identical producer replays, and hostile repaired-hash attacks plus a
stale-hash control.

### G3 -- strict serialization and evaluation

JSON loaders reject duplicate keys and nonfinite constants.  Evaluation YAML
loaders reject duplicate or non-string keys, anchors, aliases, merges,
implicit timestamps, unknown/missing fields, type changes, tuple changes,
scope escalation, and Route-B authorization.  Source baseline, date, epoch,
evaluator hash, literal scope, and every false claim flag are exact typed
invariants.

### G4 -- hostile mathematical boundaries

The audits attack the Hunter--Saxton half factor, energy sign, min/max switch
and weak-continuation overclaim; witness-tree root/order/closed-neighborhood
conventions and rule-uniformity; inclusion upward/downward rates, beta-binomial
normalization, Hahn eigenvalues and singular alpha face; Kronig--Penney delta
jump sign, `1/(2k)` factor, imaginary-wave-number continuation, band indexing
and zero thresholds; and run-and-tumble flip factor two, invariant interval,
beta exponent, critical correlation limit and polynomial/full-spectrum
distinction.

### G5 -- manuscripts and two revisions

Every package retains Round 0, Round 1, and Round 2 PDFs from one conditional
LaTeX source.  Both revisions add mathematical content.  Each round is built
twice in fresh directories with two LuaLaTeX passes at the fixed epoch and
must be byte-identical.  Settled logs are warning-free; every font is
embedded/subset; text sentinels and page rasterization pass; `paper/main.pdf`
is exactly Round 2.

### G6 -- exact package and scope closure

Each paper must have exactly 27 content-addressed manifest payloads plus one
self-excluded manifest, hence 28 physical files.  Every release script reruns
the evidence, parser, replay, mutation, and PDF gates.  All forbidden claim
flags are exact `false`; source eigenvalues, band discriminants, witness trees
and stochastic moments remain source-side objects.

### G7 -- integration

The final root audit reruns all five release manifests twice, checks 135
manifest payloads and 140 physical package files, updates the global README
and both registries, inspects every final PDF page, runs whitespace and
forbidden-claim audits, stages only the five packages plus global batch files,
synchronizes safely with origin, commits, pushes, and stops for user
confirmation before C329.
