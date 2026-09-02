# Batch review: HCS-C314--HCS-C318

## Outcome

This round delivers five independent theorem packages from baseline
`1938bae19e5a92f9ce2411aafdc68323bd641bd0`.  Each paper has its own
research question, analytic theorem/proof package, executable evidence,
strict Route-A evaluation, hostile audit, three retained manuscript rounds,
final PDF, and content-addressed release manifest.  None is an installment
of another paper.

The dynamical subtypes are deliberately different: an ancient geometric
PDE, a velocity-coupled integrable root flow, a complete-memory stochastic
process, a nonlinear matrix inverse algorithm, and a Hermitian chiral
quantum lattice.

## Independent theorem increments

- **C314:** direct curve-shortening verification for the central Angenent
  oval; exact curvature range, width, height, area and elliptic perimeter;
  punctured-strip arrival-time foliation and PDE; circular extinction; and
  both translated Grim-Reaper ends.  The central-component restriction and
  the disjoint `2*pi` translates of the unrestricted equation are explicit.
- **C315:** global hyperbolicity of the strictly positive real goldfish
  pencil; signed-time interlacing, positive velocities, exact group law and
  center drift; and a two-sided scattering atlas through the first inverse-
  time coefficient, with the ballistic carrier transferred across rank.
- **C316:** exact finite transition and first-two-moment laws for the
  elephant random walk; regular and singular martingale charts; the
  diffusive, critical and superdiffusive regimes; first four moments of the
  superdiffusive limit; and separate `p=0`, `p=3/4`, `p=1` and initial-bias
  endpoints.
- **C317:** the spectral-radius necessary-and-sufficient Newton--Schulz
  basin, sharp Jordan polynomial/double-exponential rates and all unit-circle
  faces; the support-compatible Moore--Penrose necessary-and-sufficient
  basin for arbitrary rank; and every canonical `alpha A*` and rank-zero
  boundary.
- **C318:** the exact finite SSH continuant and a unique hyperbolic edge
  pair iff `w/v>(M+1)/M`, with exact energy, vectors, taper and splitting;
  strict separation from the bulk winding threshold; exact continuum and
  finite-sampled gaps (including the odd-ring residual gap), periodic parity
  and all hopping faces; an entire matrix-sinc propagator; and a quench
  theorem that distinguishes continuum zeros from finite momentum-grid hits.

The strict tuples, in order, are
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)`,
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`,
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)`,
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)`, and
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_NATURAL_QUANTIZATION)`.
All five are `ROUTE_A_REJECTED`.

## Exact release accounting and hashes

The finite evidence units stay package-specific because curve samples,
polynomial roots, random-walk laws, matrix residuals, and lattice modes are
not interchangeable observables.

| ID | finite evidence | checker assertions | symbolic identities/groups | hostile rejections | evidence bytes | final pages/fonts |
|---|---:|---:|---:|---:|---:|---:|
| C314 | 20 parameter rows / 220 curve points / 2,639 leaves | 2,632 | 9 | 44/44 | 242,355 | 3 / 22 |
| C315 | 14 pencils / 413 root-time cells / 1,892 leaves | 2,047 | 7 | 45/45 | 161,455 | 3 / 17 |
| C316 | 35 parameter pairs / 490 time slices / 14,914 leaves | 10,315 | 105 | 39/39 | 638,965 | 2 / 20 |
| C317 | 45 matrix/boundary cases / 7,720 leaves | 8,490 | 483 | 40/40 | 227,630 | 2 / 22 |
| C318 | 55 continuants / 595 momentum cells / 7,161 leaves | 10,948 | 9,181 | 53/53 | 353,392 | 4 / 19 |
| **total** | **34,326 audited leaves** | **34,432** | **9,785** | **221/221** | **1,623,797** | **14 / 100** |

C314 also audits eight extinction scales and 35 translated-tip samples.
C315 retains 45 fixed anchors and 28 asymptotic rows.  C316 contains all
positive-mass cells through time 14 plus direct history enumeration and
four-moment ledgers.  C317 separates square Jordan, compatible rectangular,
incompatible-support and canonical-scale witnesses.  C318's symbolic count
expands exact continuant, edge, propagator and quench identities cell by
cell.

| ID | evidence SHA-256 | round 0 PDF SHA-256 | round 1 PDF SHA-256 | round 2 / final PDF SHA-256 | manifest SHA-256 |
|---|---|---|---|---|---|
| C314 | `40300f48e0c8eff674398d6139b751af41fd7ea00fe65cd5a2adae44b5976b73` | `1e1b0cbd88e5f5a1fe87876a48e828aa7a7cebdb068188cbe8b887d9a3392cae` | `b810d07f3448fc5bdb8317f47ae52e56fd5934765e07720cea7672eaf1c20cc6` | `04ce2bfe3e2f5be15587e64f3f827ce8768fcda399594de853344346867f0319` | `a871e0461fb8da78f1a2d8069434e81e6d16cc1b8087e6da90a4f219abecb69d` |
| C315 | `4db6923b8f134c72d1c53a20daf4f45f46e75ee87356f6b94a3ad6c6324dcbaf` | `59575a577b341150cdf8155d60cdba6ea9b1272ab08f18363e4240b4608cba4f` | `e4f3d07460e46a8dfa7f7bf0c3a958345c6448ecd211757514b883a8795e6028` | `065266ca46d66e7edc274b6883045bb284a229f6c067a1f0904207266bee9569` | `295f53cc84c5bbb3d9d20661298c1b3c3737a6b6d3f5d249a6cfca8df5f11538` |
| C316 | `3b0004c830c2579e234a5263a3a76c7a65272e5b45f7de74165af94538dccd64` | `7ab9406d010d459896fad4779d2b71e94a719c5486ae78e5d13f9251f96bb4ec` | `402a42396f8206b087c765fad057e66be1735dc18e2a3e33aa34de692cb1ffac` | `7d8b230b29f9bc92a871857e71765f29ddfd7c6eac7d37fcb1d01d7a5f4fc5e2` | `dade613eaac7064388a2a94f8836307290039656531f31d8b9c2c15d97934dde` |
| C317 | `51943f98667f9b121c386d4b92584ea1cdbafa88937430891f17078aff0a125a` | `d8a3b399b4b525c284fb2423a99b504ca24255b5dbe7279009a03d5a6d1ed80b` | `875b240f0339d9eb483c74a5351e9344c889889a8daf841879033752aea60ebe` | `95277b6e99a57586b89c6cfe756014d2403f71b73a18ae2157877e9c55595c9c` | `808088234e657269c375d069a6a01ba85c441c95d58de23fdced459e14fb796b` |
| C318 | `21a6c427ee64b8bc835d455d931546000dbf92f591a580c9bfdd819d94eb323e` | `43a73c91aafbc66fb41f6c2b254323644938901b3f5d9015f9222ef0dcfa61fb` | `92acf84d635a082d8f7834ba9030de0e8bd7cbcdc8302c312a16f41263a2f7f4` | `b079037a4a7ba33a2db35076cb2b75114643016c6388fb65647c13e06a934947` | `ac78dbc564e50e7e20c8a3b6a7e11b02892861616ef92a739ff78e969c7d2505` |

Every row has three distinct revision hashes and a final PDF equal to Round
2.  The five manifests cover 135 payloads and 140 physical package files.
All 14 final pages were visually inspected; all 100 final font rows are
embedded and subset.  Settled build logs are free of layout, citation,
reference, destination, rerun, and missing-character warnings.

## Citation, proof, and scope integrity

The source audits assign the explicit ancient oval to Angenent's 1992
paper, the goldfish dynamics to Calogero, the elephant walk and its
martingale phase theorem to Schuetz--Trimper and Bercu, reciprocal/generalized
matrix iteration to Schulz--Hotelling--Ben-Israel, and the chiral chain to
Su--Schrieffer--Heeger with standard bulk--boundary context.  Repository
packaging is never used as evidence of literature priority.  The collision
map was checked against the C1--C313 registry after drafting.

The C314 unrestricted periodic equation is never called one compact curve.
C316 finite enumeration is never used as a central-limit proof, and its
deterministic endpoints are not called nondegenerate.  C317 is an exact-
arithmetic theorem, not a floating-point stability claim.  C318 keeps its
finite edge threshold separate from bulk topology, and its continuum gap
separate from the parity-sensitive finite-sampled gap and finite-grid quench
zeros.

All five evaluations set `route_b_invocation_allowed: false`.  No target
arithmetic local datum, Euler factor, bad-prime datum, root number, automorphy
object, target divisor/counting law or functional equation, target zero
match, Hilbert--Polya operator, or Route-B input is asserted.  C315's
polynomial pencil is only a source-side formal hint; C318's
`A4_NATURAL_QUANTIZATION` belongs solely to its finite Hermitian lattice.
