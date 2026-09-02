# Batch plan: HCS-C309--HCS-C313

## Frozen contract

- Source commit: `b3e2f3f7207b85d7be942ff72b1f49e754615c76`
- Date / epoch: `2026-09-03` / `1788393600`
- Evaluator: `flow_systems/skills/route-a-evaluator.md` v0.2.0,
  SHA-256 `6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`
- Scope: `NO_BAD_EULER_OR_ROOT_NUMBER`
- Batch size: exactly five independent papers, followed by a user checkpoint

## Papers and theorem gates

1. **C309 matrix Riccati flow:** derive the all-dimensional Mobius solution,
   full signed-time pole atlas, forward limit/rate, strict gradient law,
   symmetric-involution Morse--Bott geometry, full Frechet derivative, and
   source block lift.
2. **C310 Dubins synthesis:** close all six analytic path families,
   feasibility and boundary conventions, exact endpoint replay, zero-piece
   degeneracies, all ties, scaling, and reflection in one global optimizer.
3. **C311 Brusselator:** prove positive global existence and the complete
   linear chamber atlas, then derive normalized Hopf tensors, exact complex
   cubic coefficient, negative first Lyapunov coefficient, and leading
   amplitude/frequency data.
4. **C312 Hegselmann--Krause:** prove one-dimensional finite termination with
   an explicit cubic bound, fixed-cluster classification, rational cell
   maps, gap decomposition, and an exact nonconserved-mean counterexample.
5. **C313 round sphere:** integrate every geodesic, classify fixed sets and
   the clean return/orbit quotient, then derive the exact Laplace spectrum,
   heat trace, and completed-square half-wave revival.

## Uniform release gates

### G0 -- collision and ownership

Each paper cites a historical model or theorem owner and records its nearest
workspace collisions.  The five phase spaces, clocks, proof mechanisms, and
headline theorems are independent.  Workspace novelty is never presented as
literature priority.

### G1 -- analytic theorem and boundary closure

Headline statements are proved analytically.  Finite computations test
formula conventions and implementation only.  Repeated eigenvalues and
poles, every Dubins discriminant/tie, all Brusselator linear boundaries, HK
closed-neighborhood/gap faces, and the sphere's maximally clean periodic
family are explicit rather than silently generic.

### G2 -- independent executable evidence

Every package has a canonical sorted-JSON producer with a self-excluding
semantic hash, a checker importing no producer code and independently
reconstructing all audited values, a distinct SymPy lane, two isolated
byte-identical producer replays, and hostile repaired-hash attacks plus a
stale-hash control.

### G3 -- strict serialization and evaluation

JSON loaders reject duplicate keys and nonfinite constants.  Evaluation YAML
loaders reject duplicate or non-string keys, anchors, aliases, merges,
implicit timestamps, unknown/missing fields, type changes, tuple changes,
scope escalation, and Route-B authorization.  Source, date, epoch, evaluator
hash, obstruction IDs HEN-O293--HEN-O297, literal scope, and all false claim
flags are exact typed invariants.

### G4 -- hostile mathematical boundaries

The audits attack omitted/tied Riccati poles and repeated-root Loewner
limits; Dubins reflection, discriminant, zero-piece, and `atan2` faces;
Brusselator eigenvector normalization and Hopf sign conventions; HK strict
versus closed neighborhoods, permanent gaps, termination, and false mean
conservation; and sphere least periods, multiplicities, clean return, and
one- versus two-period revival phases.

### G5 -- manuscripts and two revisions

Every package retains Round 0, Round 1, and Round 2 PDFs from one conditional
LaTeX source.  Both revisions add mathematical content.  Each round is built
twice in fresh directories with two LuaLaTeX passes at the fixed epoch and
must be byte-identical.  Settled logs are warning-free; every font is
embedded/subset; text sentinels and page rasterization pass; `paper/main.pdf`
is exactly Round 2.

### G6 -- exact package and scope closure

Each paper has exactly 27 content-addressed manifest payloads plus one
self-excluded manifest, hence 28 physical files.  Every release script reruns
the evidence, parser, replay, mutation, and PDF gates.  All forbidden claim
flags are exact `false`; matrix spectra, path words, chemical cycles,
confidence graphs, great circles, and spherical harmonics remain source-side
objects.

### G7 -- integration

The final root audit reruns all five release manifests twice, checks 135
manifest payloads and 140 physical package files, updates the global README
and both registries, inspects every final PDF page, runs whitespace and
forbidden-claim audits, stages only the five packages plus six global files,
synchronizes safely with origin, commits, pushes, and stops for user
confirmation before C314.
