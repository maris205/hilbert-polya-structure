# Batch review: HCS-C339--HCS-C343

## Outcome

This round delivers five independent theorem packages from frozen baseline
`e2d94f886963cbe3d42b83f6ef542413a163d3a4`.  Each package contains a
source-local analytic proof, producer-independent executable evidence, a
strict Route-A evaluation, hostile mutation and parser audits, three retained
manuscript rounds, a deterministic final PDF, and a content-addressed release
manifest.  The five advances use genuinely different state spaces and proof
mechanisms: a nonreversible Finsler geodesic flow, a periodic finite-gap
Hamiltonian, a finite wreath-product Markov chain, a directed reinforced walk
in random environment, and a distributed-memory flow with an exact finite
Markov realization.

## Independent theorem increments

- **C339:** the complete rotational Katok--Zermelo atlas on the round
  two-sphere.  Navigation gives every geodesic; an explicit `SO(3)` return
  equation proves that irrational wind leaves exactly the two oriented
  equators as prime closed geodesics.  Their distinct periods, Jacobi
  monodromies and Poincare determinants are exact, and the rational-wind,
  zero-wind, sign-reversal and strong-convexity boundaries are closed.
- **C340:** the complete real-line spectrum of the degree-one Lame
  Hamiltonian.  Its three exact periodic/antiperiodic edges, commuting
  third-order operator and cubic operator identity prove pure absolute
  continuity, the two spectral bands and the absence of every higher open
  gap.  The fiber domain, Green boundary cancellation, free limit and
  Poschl--Teller soliton limit are explicit.
- **C341:** the complete finite-cycle fair switch--walk--switch lamplighter
  spectrum.  Walsh transformation decomposes the full operator into the
  intact lazy cycle and all killed-path blocks, yielding every eigenvalue and
  multiplicity, an explicit eigenbasis and characteristic polynomial, and
  the sharp all-size gap with every small-cycle convention retained.
- **C342:** the exact law of directed linear edge reinforcement on every
  finite strongly connected labelled multigraph whose vertices have nonempty
  outgoing rows.  Every path law equals the annealed law of independent
  Dirichlet transition rows; the conjugate posterior, prediction rule, exact
  row moments and almost-sure row, vertex and arc occupation limits follow.
  Parallel arcs, deterministic rows, unvisited rows and reducible boundaries
  remain explicit.
- **C343:** the complete linear stability atlas for Erlang-2 distributed
  negative feedback.  The memory equation is exactly realized by a compatible
  three-state chain; Routh--Hurwitz gives the sharp stability wall, exact
  imaginary crossing, transversality and unstable-root count, while the full
  discriminant, Jordan, semigroup, zero-feedback and instantaneous-memory
  boundaries are classified without a nonlinear periodic-orbit claim.

The strict tuples, in order, are
`(A0_FAIL,A1_PASS_ANALYTIC,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`,
`(A0_FAIL,A1_WEAK,A2_FAIL,A3_FAIL,A4_NATURAL_QUANTIZATION)`,
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`,
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)`, and
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)`.  All five are
`ROUTE_A_REJECTED`; Route B remains false.

## Exact release accounting and hashes

Finite evidence units are package-specific regression receipts.  They test
formulae, normalization and implementation conventions but are not finite
extrapolation proofs of the all-parameter theorems.

| ID | finite evidence | independent/symbolic checks | hostile rejections | evidence bytes | final pages/fonts |
|---|---|---:|---:|---:|---:|
| C339 | 158 rational-wind rows and 3 quadratic-irrational fixtures | 3,916 / 639 | 54/54 | 73,089 | 3 / 12 |
| C340 | 199 rational-modulus rows | 9,068 / 618 | 55/55 | 175,409 | 3 / 11 |
| C341 | 2,046 Walsh blocks, 20,480 coefficient cells and 6 full kernels | exhaustive / 46 | 59/59 | 773,961 | 2 / 21 |
| C342 | 12,018 paths, 27 summaries, 24 moment rows and 3 environments | exhaustive / 37 | 79/79 | 4,813,459 | 2 / 19 |
| C343 | all parameter, wall, discriminant and semigroup fixture families | 4,542 / 409 | 137/137 | 58,867 | 3 / 20 |
| **total** | **five independent finite ledgers** | **17,526 named assertions plus two exhaustive reconstructions / 1,749** | **384/384** | **5,894,785** | **13 / 83** |

| ID | evidence SHA-256 | round 0 PDF SHA-256 | round 1 PDF SHA-256 | round 2 / final PDF SHA-256 | manifest SHA-256 |
|---|---|---|---|---|---|
| C339 | `54bdfd2d2b57aba2c9259872d0edd0009c5f28fbd03eb7d0f333643d6c1c65e8` | `df9ac03abf38b99b294ddf4ab29e8847a176a219028343534aae3a934354e6cb` | `1d5bc3208c06c194385f9bf18cc283dfa7385d7759f034d15af40f633f7dbdc1` | `7cd9174cfd2ec0294e043e28e244b86edbddfd96cc92984922d11593cb184979` | `fa34fbeff6ca1a1930e7878f6b6326e2a8b121bee1523a83208bcd8aaf118b46` |
| C340 | `369f1e9d1bb4855ed75188388546caa2c1e4066d2e5afb6ddc7b0cc40fa23767` | `80b2f27455d8123fe14b069dcf9db86ab2584b5b0ca6bdcb9ddd24249de19c06` | `8d7ab2a1e83c2ddf1638fef6be9642b82d64255b147efb9e75d3aa66234312aa` | `64f9670e95d464398cc88b15abe1a14a905627cd83b17d22400dc07797dcf414` | `a5e6c82e2a968e3e3e22116f4f87422d196f48f2e6b836d93c7802e0d4024f2a` |
| C341 | `85010a51faad773faf2057b991e50ced62650c2457f3a2c10cbfd37e9f7db69b` | `97ba22907b30ed8be4e2addd35b93fd948329f3c8236cc4f77fdc7cee7a2ff95` | `492bda718671e78f029054487dd8bc51c17cb2f489b9def0d72f37254530180f` | `73435d91fbbdd8b8d6b9abe61b60cab01dba7bd9c457d0089d04638d9f5abec1` | `e3ae8b362f88c936ecc6c835f70260bad02abfa76a22df544c5cc15b479e8724` |
| C342 | `f86842205ac7037034042539684e44e5d824fcc30e382eb4678349f5a8b02b8f` | `6d0463b15add449886d6f5d8b2cb7d016cd7ba07595b2c43ebc020303d2b93e5` | `d3f2389851734d15a5a1c227a48d52d58601f8ef6df2abb4a95b91ca103a5a67` | `575f20edd4d553485669b34397c0f7407e1dad243acc73deea1c5118bc8cf3ff` | `653fc436a245c616a645948b8e276d3c20b69b9d3365326596c3cfbd566d31f7` |
| C343 | `37ac0acba709f9b1e865f5245454cd0336afe239f5b03e9e1b8ffde80db3ef5b` | `60b895f99347cee0210c587d84620cd8ff22760391b25701fa58e3fcbc8c3d8a` | `15a3a957f7ce1bacdb77a72fce4d1ae16f337e964aceda6c082e39d431bab8d2` | `337274ebdc30ed4ef1a06977b235b258eb0979117284c8f375c0fd65e9c6fe79` | `54b017df05c28dc7e4699bfc0875773b0fac3a8a1ddd909f72a733551e9d88a5` |

Every row has three distinct revision hashes and a final PDF identical to
Round 2.  The five manifests cover 135 payloads and 140 physical package
files.  All 13 final pages were visually inspected; all 83 final font rows
are embedded and subset.  Settled builds contain no layout, citation,
reference, destination, rerun, missing-character or missing-glyph warning.
The five final release programs pass in write mode and consecutive no-write
runs with stable hashes.

## Author-swapped corrections and integrity

Independent author-swapped review changed substantive proof boundaries.  In
C339 it required the explicit return equation
`R_z(epsilon T) g R_z(T)=g`, equivalently
`R_z(epsilon T)=g R_z(-T) g^{-1}`.  This exposes the two axes `e_3` and
`g e_3`, isolates the equatorial exception `g e_3=+-e_3`, and closes the
half-turn case instead of relying on an implicit rotation argument.  The
equatorial maximum wording was also corrected before all evidence and PDFs
were rebuilt.

C340 now fixes the fiber domain as `H^3_theta([0,2K])`, states the common
quasiperiodic conditions on the function and its first two derivatives, and
shows cancellation of every Green boundary term.  The adjoint recovers the
same conditions, so the commuting third-order fiber operator is genuinely
skew-adjoint.  A direct periodic-operator source was added for the
Floquet/direct-integral and pure absolutely continuous spectral theorem.

C342's review found the only theorem-critical blocker: the literal class had
allowed a single vertex with no arcs, for which strong connectivity can be
vacuous but the transition row is undefined.  The theorem now requires a
nonempty outgoing labelled row at every vertex, including at least one loop
in the one-vertex case.  This assumption was synchronized through theorem,
paper, evidence, checker, global summaries and a repaired-hash mutation that
attacks its deletion or rewrite.  C341 and C343 passed their independent
proof reviews without a theorem-critical correction.

Every checker imports no producer code.  JSON parsing rejects duplicate keys
and nonfinite constants.  Evaluation parsing locks exact schemas and rejects
aliases, anchors, merges, non-string keys, implicit timestamps, unknown
fields, type changes, authority drift and tuple drift.  Hostile suites repair
evidence hashes before semantic attacks, every Python entry point rejects
optimized execution, and isolated producer runs replay byte for byte.

## Citation and scope integrity

The source audits assign the Katok examples and navigation construction to
their source Finsler-geometric literature; the Lame identities and general
periodic spectral theorem to their elliptic-function and Floquet sources;
finite lamplighter harmonic analysis to Lehner--Neuhauser--Woess; the directed
reinforcement/Dirichlet-environment correspondence to Enriquez--Sabot, with
Diaconis--Freedman as lineage and Sabot--Tournier as overview; and gamma-delay
stability and the linear-chain construction to Boese and
Hurtado--Kirosingh.  Workspace reconstruction, packaging and collision
screening are not presented as literature priority.

All five evaluations use evaluator v0.2.0, SHA-256
`6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`,
and set `route_b_invocation_allowed: false` under literal scope
`NO_BAD_EULER_OR_ROOT_NUMBER`.  No target arithmetic local datum, Euler
factor, bad-prime datum, root number, automorphy object, target
divisor/counting law or functional equation, target zero match,
Hilbert--Polya operator, or Route-B input is asserted.  Geodesic periods,
finite-gap curves, finite-chain spectra, Dirichlet transition rows and delay
roots retain only their explicitly evaluated source-side meanings.
