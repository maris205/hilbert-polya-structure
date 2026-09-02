# Batch plan: HCS-C289--HCS-C293

## Frozen contract

- Source commit: `7fbe9db30cc460a82883533d7cfb2edd988c5b65`
- Date / epoch: `2026-09-02` / `1788307200`
- Evaluator: `flow_systems/skills/route-a-evaluator.md` v0.2.0,
  SHA-256 `6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`
- Scope: `NO_BAD_EULER_OR_ROOT_NUMBER`
- Batch size: exactly five independent papers, followed by a user checkpoint

## Papers and theorem gates

1. **C289 hyperbolic magnetic flow:** all-initial-data
   circle/horocycle/hypercycle/geodesic classification, exact strong-field
   period, and matching Frenet/Lorentz-generator proofs.
2. **C290 planar CR3BP:** exactly five Lagrange points, global collinear
   saddle--center proof, triangular Routh threshold, and the defective
   equality case with linear growth.
3. **C291 dimer RSA:** all-`n` path/cycle terminal PGFs, Riccati OGF,
   factorial-moment hierarchy, support, mean/variance asymptotics, and exact
   boundary correction.
4. **C292 sticky particles:** arbitrary finite and simultaneous all-event
   dynamics, weighted isotonic/convex-hull representation, conservation,
   exact dissipation, and pressureless-Euler weak closure.
5. **C293 magnetic Grushin cylinder:** Friedrichs operator, all flux channels,
   compact/continuous transition, nonresonant heat trace/multiplicities,
   source-local spectral series, and Weyl law.

## Uniform release gates

### G0 -- collision and ownership

Every paper identifies its classical literature owner and the nearest
workspace package.  Workspace novelty is not literature priority, and no
paper claims that a classical theorem is newly discovered.

### G1 -- proof classification

The frozen headline must be classified as `PROVABLE AS STATED`,
`PROVABLE AFTER WEAKENING / EXTRA ASSUMPTION`, or
`NOT CURRENTLY JUSTIFIED`.  Only the first class, or a visibly repaired and
fully proved second class, may ship.  Finite evidence never replaces an
all-parameter, all-size, event, geometric, asymptotic, or operator proof.

### G2 -- independent executable evidence

Each package has a canonical sorted-JSON producer with a self-excluding
payload hash, a checker importing no producer code and reconstructing the
result through a genuinely different route, a separate symbolic check, two
isolated fresh-path byte replays, and hostile mutations with repaired hashes
plus a stale-hash control.

### G3 -- boundary atlas

Threshold, equality, zero, singular, small-size, simultaneous-event,
integer/noninteger flux, orientation, and excluded faces are explicit.  No
undefined quotient, hidden tie convention, unproved self-adjointness, or
unstated time normalization may pass.

### G4 -- manuscripts and revision rounds

Each package retains Round 0, Round 1, and Round 2 PDFs from one conditional
LaTeX source.  Both revisions add mathematical content.  The final paper is a
complete theoretical manuscript, not an abstract sheet, and includes proof,
limitations, source ownership, data/code availability, ethics, conflicts,
funding, contributor roles, and AI-use disclosure.

Every round is rebuilt twice in fresh directories under the fixed epoch and
must be byte-identical.  All fonts are embedded/subset; overfull boxes above
10pt, undefined references/citations, missing glyphs, or settled rerun
warnings are release failures.  `paper/main.pdf` must be byte-identical to
Round 2 and all three round hashes must be distinct.

### G5 -- exact package closure

Each package has 28 physical files and 27 manifest payload files: eight root
documents, seven code files, one Route-A YAML, seven paper files, four result
files, and one self-excluded release manifest.  The release script reruns
every evidence command and every PDF build before auditing the exact ledger.

### G6 -- integrity and scope

References are verified against DOI, publisher, official repository, or
authoritative bibliographic pages.  Every theorem claim is either proved in
the manuscript or explicitly bounded.  All prohibited claim flags remain
false.  In particular, C293's source-local Dirichlet series and divisor
multiplicity may not be interpreted as target Euler factors, a target divisor
law, a functional equation, a zero correspondence, or an operator for the
target problem.

### G7 -- integration

The final batch audit runs every manifest, inspects extracted/rendered PDFs,
checks exact hashes and ledgers, runs `git diff --check`, updates the README
and both registries, stages only C289--C293 and their batch/index files,
synchronizes safely with origin, commits, pushes, and stops for user
confirmation.
