# Batch plan: HCS-C334--HCS-C338

## Frozen contract

- Source commit: `db2c816b7b6bd450f51f79b91842cb882b0bd773`
- Date / epoch: `2026-09-03` / `1788393600`
- Evaluator: `flow_systems/skills/route-a-evaluator.md` v0.2.0,
  SHA-256 `6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`
- Scope: `NO_BAD_EULER_OR_ROOT_NUMBER`
- Batch size: exactly five independent papers, followed by a user checkpoint

## Papers and theorem gates

1. **C334 Morse oscillator:** close every classical bounded orbit of the Morse
   Hamiltonian, its action and period, then derive the complete finite quantum
   bound spectrum and eigenfunctions together with the essential-spectrum,
   dissociation and zero-energy threshold boundaries.
2. **C335 exponential shot-noise OU:** derive the pathwise flow and exact
   transition Laplace transform for Poisson arrivals with exponential marks,
   prove the unique stationary Gamma law, all stationary cumulants and the
   exact covariance, and diagonalize every finite polynomial filtration
   without claiming a full Hilbert-space spectrum.
3. **C336 Crow--Kimura single peak:** identify the nonlinear normalized
   mutation--selection flow with a projectivized linear semigroup, give the
   complete finite-genome spectrum as retained Hamming-layer eigenvalues plus
   a strictly interlacing rank-one secular spectrum, and prove Perron
   convergence with all zero-mutation, zero-selection and one-locus faces.
4. **C337 kicked rotor:** solve the entire integer-resonance sheet of the
   quantum kicked rotor.  Even resonance order gives an exact Bessel kernel
   and ballistic momentum moments; odd order gives exact period-two
   antiresonance.  Floquet order, phase, zero-kick and shifted-momentum
   boundaries are explicit.
5. **C338 Wilson cycle-popping:** prove almost-sure termination and abelian
   pop-order independence of the infinite-stack dynamics, its Wilson
   loop-erased-walk realization, the weighted spanning-tree law and
   matrix-tree normalization, and the complete transfer-current edge
   determinant with root, tree, singleton and multiedge boundaries.

## Uniform release gates

### G0 -- collision and ownership

Every package records its historical source owner and nearest workspace
neighbors.  The five systems are respectively an integrable Hamiltonian with
natural quantization, a compound-Poisson-driven decay process, a nonlinear
finite-genome selection flow, a periodically driven Floquet quantum system,
and an abelian random stack dynamics.  `NEW` means only no existing workspace
owner, never a literature-priority claim.

### G1 -- analytic theorem and boundary closure

Headline statements are proved analytically.  Finite evidence tests formulas,
normalizations and implementation conventions; it is never extrapolated into
an all-parameter proof.  Threshold equality, reducible faces, multiplicity
loss, Floquet parity and transfer-current orientation are frozen explicitly.

### G2 -- independent executable evidence

Every package has a canonical sorted-JSON producer with a self-excluding
semantic hash, a checker importing no producer code and independently
reconstructing the audited quantities, a separate symbolic lane, two isolated
byte-identical producer replays, and hostile repaired-hash attacks plus a
stale-hash control.

### G3 -- strict serialization and evaluation

JSON loaders reject duplicate keys and nonfinite constants.  Evaluation YAML
loaders reject duplicate or non-string keys, anchors, aliases, merges,
implicit timestamps, unknown or missing fields, type changes, tuple changes,
scope escalation and Route-B authorization.  Source baseline, fixed date and
epoch, evaluator digest, literal scope and every false claim flag are typed
invariants.

### G4 -- hostile mathematical boundaries

The audits attack the Morse energy shift, action normalization and threshold
state; the shot-noise decay/rate convention and any false full-spectrum
upgrade; the Crow--Kimura Walsh multiplicities, secular sign, interlacing and
finite-length threshold language; the kicked-rotor operator order, `2*pi`
parity, Bessel phase and kinetic-energy factor; and Wilson stack order,
orientation, Laplacian normalization and determinantal signs.

### G5 -- manuscripts and two revisions

Every package retains Round 0, Round 1 and Round 2 PDFs from one conditional
LaTeX source.  Both revisions add mathematical content.  Each round is built
twice in fresh directories with two LuaLaTeX passes at the fixed epoch and
must be byte-identical.  Settled logs are warning-free; every font is embedded
and subset; text sentinels and page rasterization pass; `paper/main.pdf` is
exactly Round 2.

### G6 -- exact package and scope closure

Each paper must contain exactly 27 content-addressed manifest payloads plus
one self-excluded manifest, hence 28 physical files.  Every release script
reruns evidence, parser, replay, mutation and PDF gates.  All forbidden claim
flags are exact `false`.  Molecular, stochastic, evolutionary, Floquet and
spanning-tree source data remain source-local.

### G7 -- integration

The final root audit reruns all five release manifests twice, checks 135
manifest payloads and 140 physical package files, updates the global README
and both registries, inspects every final PDF page, runs whitespace and scope
audits, stages only this batch, synchronizes safely with origin, commits,
pushes, and stops for user confirmation before C339.
