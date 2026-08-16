# Paper 38 exact integration preregistration — SD-C40

Date frozen: 2026-08-15

Route: strict Route A v0.2; Route B locked

Experiment type: deterministic exact audit (CPU only)

## Material passport

- Origin skills: `experiment-bridge`, `analyze-results`, and ARS experiment-agent
- Origin mode: preregistered exact integration
- Verification status at freeze: `UNVERIFIED`
- Version label: `SD-C40-stage1-prereg-v1`
- Data regime: generated integer fixtures; no external dataset or sampling

## Frozen object and ownership boundary

The sole object is the full oriented-edge geodesic shift on the
presentation-canonical Bass--Serre tree of the original ascending HNN
splitting

\[
BS(1,r)=\langle u,v\mid vuv^{-1}=u^r\rangle
\]

over \(\langle u\rangle\cong\mathbb Z\). The only allowed coefficient is the
canonical signed HNN height/modular cocycle. This is a new object and receives
neither inherited same-object credit nor inherited generator-step-marker
credit. Quotients, fundamental domains, arbitrary representations, radial or
basepoint damping, alternative Bass--Serre splittings, von Neumann/groupoid
determinants, and Route-B repairs are outside scope.

## Frozen claims and exact falsifiers

1. **Full-tree emptiness.** A tree has no positive-length reduced closed edge
   path. Falsifier: one exact reduced closed path on the frozen tree object.
2. **No ordinary Fredholm ownership.** The full-tree Hashimoto operator has an
   infinite orthogonal image family of constant nonzero norm, hence is
   noncompact and not trace class. Falsifier: a source-canonical nonzero
   modular weighting that makes this same operator trace class without a
   quotient, basepoint, damping, or arbitrary representation.
3. **Tree-lattice formula inapplicable.** Vertex and edge stabilizers are
   infinite cyclic, so the action is nonproper and fails the finite-stabilizer
   tree-lattice hypotheses. At `r=1` the image in the automorphism group of
   the line is discrete but the kernel is infinite; for `r>=2` the faithful
   image is nondiscrete. Falsifier: exact satisfaction of the required
   properness and finite-stabilizer hypotheses.
4. **Orbital substitute is generic.** For \(r\ge2\), the separately typed
   positive-height conjugacy ledger obeys
   \(Z_{+,r}(z)=(1-z)/(1-rz)\), with the modular \(s=1\) specialization
   \((1-z/r)/(1-z)\). Falsifier: disagreement among direct residue orbits,
   Burnside counts, Möbius primitive counts, repetition, Euler product, and
   the closed forms.
5. **Balanced divergence.** At \(r=1\), the group-conjugacy ledger is infinite
   at every positive height. It must not be encoded as zero.
6. **Marker incompatibility.** Bass--Serre translation length is a new tree-
   edge clock and is many-to-one relative to the old Cayley generator clock.
   Falsifier: an injective length-preserving correspondence on every frozen
   marker witness.

Finite computations audit formulas and implementation only. Infinite-object
conclusions remain theorem-owned by the frozen proof package.

## Frozen controls

- balanced `r=1`;
- primes `r=2,3,5,7`;
- composite baseline `r=4` and composites `r=6,8,9,10,12`;
- eighteen deliberate `BS(p,q)` controls spanning ascending, reversed-
  ascending, balanced, and non-ascending cases;
- 64 seeded cyclically reduced two-generator one-relator controls, seed
  `380038`, with evaluator-side eligibility parsing;
- finite rooted-tree no-cycle certificates;
- orthogonal-column and growing partial Hilbert--Schmidt-mass certificates;
- empty, divergent, marker-collision, and `PROVES_TOO_MUCH` controls;
- fresh source/evaluator-separated runs A and B plus isolated cold-copy run C.

Ineligible random presentations receive
`INELIGIBLE_NO_FROZEN_CYCLIC_HNN_SPLIT`; they are not mechanism failures.

## Frozen analysis and decision rule

All arithmetic is integer or `fractions.Fraction`. Results are exact finite
enumerations, not sample estimates: no p-values, confidence intervals,
effect-size thresholds, or error bars are applicable. Comparisons are exact
equalities against preregistered formulas and exact byte identity across
runs.

`GO` requires, on the full tree itself, a nonempty source-selective primitive
ledger, an honest ordinary Fredholm determinant, and an internally consistent
new tree-edge marker, surviving every listed control. An empty ledger,
non-trace-class operator, inapplicable determinant theorem, generic orbital
substitute, balanced divergence, or marker incompatibility is terminal:

`STOP_BASS_SERRE_TREE_BRANCH` / `CLOSE_ENTIRE_AFFINE_BRANCH`.

No mechanism search follows a terminal result. Paper 39 is restricted to the
already frozen affine-branch closure obstruction DAG.

## Frozen integration and integrity contract

- Source and evaluator occupy disjoint directories and communicate only via
  canonical JSON over subprocess standard streams.
- Runs A/B are fresh processes; C executes from a temporary isolated copy
  removed before freeze.
- Absent, null, empty, and populated transport metadata must leave scientific
  and Route bytes unchanged.
- Simulated root-manifest absent/present metadata must leave the same bytes
  unchanged. Stage 1 must not create `PAPER_MANIFEST.sha256`.
- The fixed Route card is
  `evaluations/route_a/SD-C40/2026-08-15.yaml` and uses the literal pending
  provenance triple `PENDING_FIRST_ARTIFACT_COMMIT`.
- `results/SHA256SUMS.txt` excludes itself, the mutable fixed Route card, and
  the future root manifest.
- Every managed text file is UTF-8 without BOM, LF-only, with exactly one EOF
  newline. Cache and compiled Python residue are forbidden.
- The integrated artifact must run from a clean copy with all `/tmp/paper38_*`
  inputs absent; external prototype availability is provenance-only.
