# Batch review: HCS-C344--HCS-C348

## Outcome

This round delivers five independent theorem packages from frozen baseline
`1af63b945e19b5f94ac1cb76f93af5ac66d3d562`.  Each package contains a
source-local analytic proof, producer-independent executable evidence, a
strict Route-A evaluation, hostile mutation and parser audits, three retained
manuscript rounds, a deterministic final PDF, and a content-addressed release
manifest.  The five advances use genuinely different state spaces and proof
mechanisms: a complex Hamiltonian resonant triad, an infinite self-adjoint
lattice impurity, a deterministic nonsmooth reflection map, a nonlinear
nonlocal parabolic probability flow, and a random walk in frozen iid spatial
disorder.

## Independent theorem increments

- **C344:** the complete regular and singular invariant-level atlas of the
  canonical Hamiltonian resonant triad.  Two Manley--Rowe integrals and the
  Hamiltonian reduce intensity to a completely classified cubic; a Jacobi
  `sn^2` formula gives its least period.  Two third-kind elliptic increments,
  rather than intensity return alone, give the exact full-state closure test.
  The zero-Hamiltonian transfer orbit, factor-two full period, equal-action
  heteroclinic, maximal-Hamiltonian relative equilibrium, axes and coupling
  boundaries are explicit.
- **C345:** the complete infinite-volume spectrum and one-channel scattering
  law of a side-coupled Fano--Anderson impurity.  Physical-sheet monotonicity
  gives exactly one simple pole on each exterior, while sign filters reject
  extraneous squared-quartic roots.  Parity reduction, local-uniform
  Stone--Stieltjes inversion, exterior pole exhaustion and band-edge atom
  tests prove two-fold absolutely continuous band multiplicity and absence of
  singular continuous spectrum.  Density, residues, unit mass, exact `T/R`,
  the in-band Fano zero and every degenerate face are closed.
- **C346:** the sharp all-input theorem for a two-axis oblique Skorokhod map.
  A running-supremum fixed point proves existence and uniqueness exactly for
  `rho*sigma<1`, with optimal weighted contraction coefficient,
  input-to-regulator/state stability, monotone Picard rate, causality,
  continuity preservation and continuous time-change covariance.  A null
  regulator cone proves critical nonuniqueness, and one simultaneous negative
  jump proves infeasibility at and beyond the wall; normal and triangular
  faces remain explicit.
- **C347:** the complete identical-frequency noisy mean-field Kuramoto
  stationary atlas.  The global classical probability flow obeys an exact
  free-energy dissipation identity.  Zero stationary flux exhausts all
  profiles by uniform and von Mises densities; a self-contained positive
  coefficient proof of strict Bessel-ratio monotonicity gives the exact
  `K=2D` threshold and uniqueness modulo rotation.  The uniform Fourier
  spectrum and two-term critical expansion are exact, without a general
  convergence or Hopf claim.
- **C348:** the complete one-dimensional iid RWRE direction--speed phase
  theorem under strict ellipticity and integrable log bias.  The quenched
  finite-interval scale function yields Solomon's direction trichotomy;
  stationary ergodic crossing times and finite/infinite-mean inversion yield
  the deterministic velocity and both transient zero-speed chambers.  The
  full Beta environment and homogeneous walk faces are explicit, and Fubini
  keeps annealed and quenched-almost-every-environment conclusions distinct.

The strict tuples, in order, are
`(A0_FAIL,A1_WEAK,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`,
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_NATURAL_QUANTIZATION)`,
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)`,
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)`, and
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)`.  All five are
`ROUTE_A_REJECTED`; Route B remains false.

## Exact release accounting and hashes

Finite evidence units are package-specific regression receipts.  They test
formulae, normalization and implementation conventions but are not finite
extrapolation proofs of the all-parameter theorems.

| ID | finite evidence | independent/symbolic checks | hostile rejections | evidence bytes | final pages/fonts |
|---|---|---:|---:|---:|---:|
| C344 | 72 regular, 12 zero-Hamiltonian and 24 relative-equilibrium rows | 6,776 / 546 | 141/141 | 133,830 | 3 / 13 |
| C345 | 126 spectral, 315 scattering/density, 63 Fano and 21 moment rows | 13,734 / 1,467 | 154/154 | 203,209 | 4 / 21 |
| C346 | 6 matrices, 36 events, 72 pause expansions, 27 Picard rows and 6 wall witnesses | 886 / 5,125 | 70/70 | 29,363 | 3 / 23 |
| C347 | 17 positive coefficients, 9 quotient coefficients, 7 tail bounds, 4 root brackets and 162 Fourier rows | 199 exact rows / 60 | 71/71 | 38,356 | 3 / 18 |
| C348 | 400 Beta cells, 280 two-atom laws, 780 words, 2,930 hitting coordinates and 5 constant faces | exhaustive / 122 | 72/72 | 953,582 | 3 / 20 |
| **total** | **five independent finite ledgers** | **21,396 named assertions plus 199 exact rows and one exhaustive reconstruction / 7,320** | **508/508** | **1,358,340** | **16 / 95** |

| ID | evidence SHA-256 | round 0 PDF SHA-256 | round 1 PDF SHA-256 | round 2 / final PDF SHA-256 | manifest SHA-256 |
|---|---|---|---|---|---|
| C344 | `03fe83cbfc95f6c227b4318de90c35a7f91a9716a0c61a7ab90ad326ebaa675d` | `37c8032ed49567157bd882a3cb5145c89958c45c37f8ccdaa14c03ebc4db225e` | `18512e3cdb2e0441448de19380bdaffc8d7a06c0b12aa9984d1d920f9c20172c` | `9872da46013d60d25a0ccbcb94d993fd1241d123620440240f4b7c55bbea2432` | `c41dd17e56af60bd4b2e52838e0f9c543cb13ccea9ea7d448ff355577fba9755` |
| C345 | `809e130153863cb1327be31599c854a001f140576363753b590bf8049c4226b5` | `a447f74f8ab96466a94c1d83bac8460d65f6bde153c31134fee837c8dde78b01` | `06e2c5bfbc6ef3211523e8e9f7108b507a2b168509b3d300156d140ede39f5a3` | `4c1c2e075f60d1a5bd8273d6a89575db86355dd713ad033226c182f52c037962` | `5cb4dded6d73d299833eea713268088128aadbdd6a9d659ba8615eb7a7e9c400` |
| C346 | `933f2e85fa500c96ebf5cd23fcabf93e460fe1708d42d5ca10e38541505b27a8` | `dac0b3f8e5ed7b395b30a8a1fe42bf8f383707b9cf64520208e863730d1e8001` | `1267731c062b25c628c832a721ceaf508a65907a7003218739897c189afaf860` | `eecd570218803814ae0042512ef5d72196e8b00a9e93c497c3492cebdbe4881c` | `28167501d8704694602989b40ca846b7a50ba0cc08fcf2f3e0d2f4576d952810` |
| C347 | `c349f90c35c572651dd91ed13c3204e88a54a1c376689c33e8cba8145e308fcb` | `f8a65c7f1616d2e4196b2053482acb1e55d3ede086ccffb6fdf800b501a11921` | `0158395607b4d9fe43c28cc06d8dfc5a8ed377abd895c45bd6525fe40c1ee517` | `28d82beba070c42b33b211e2a2699c272397fa877c66bac0a26c8a2210947dd1` | `153a3992cb6fe92740cec6fdc5deecb95aa02e2eb752d4cedb954798e250117b` |
| C348 | `4107c56cb70c3211aac2a8db44472f3c4e0668846fae3abba4d61a23aea4ce26` | `4ec713f566d02d689d192dd785f3989bbecc6f54362b3636545678eff4531fe5` | `79566d244d7ec0d732fc4c104c2d55f90e66783c922e0945bc8376ac969e2ae9` | `4a3640e6f4ecaed268346c9844d00b2f2032dd0237591ab13fe3762b2095ac5a` | `eea84450b5f180f1df7743f8a23574c00a65e0a18f07d8ccfa69d4f894049146` |

Every row has three distinct revision hashes and a final PDF identical to
Round 2.  The five manifests cover 135 payloads and 140 physical package
files.  All 16 final pages were visually inspected; all 95 final font rows
are embedded and subset.  Settled builds contain no layout, citation,
reference, destination, rerun, missing-character or missing-glyph warning.
The five final release programs pass in write mode and consecutive no-write
runs with stable hashes.

## Author-swapped corrections and integrity

C344 passed a nonauthor reconstruction of its Poisson signs, first-integral
rank, root order, `sn^2` scaling, both phase increments, zero-Hamiltonian chart
and double-root frequency closure without a theorem-critical correction.

C345's first cross-review found two connected spectral-measure blockers.  In
the standard upper-half-plane convention, `G_dd=<d,(z-H)^(-1)d>` is
anti-Herglotz and `-G_dd` is Herglotz.  More importantly, an algebraic boundary
formula alone did not yet exclude singular continuous mass.  The repaired
proof now uses locally uniform boundary limits and Stone test-function
inversion on every compact subinterval of the open band, real analyticity and
the two simple poles on the exteriors, and the edge formula
`mu({E0})=lim_(eta down to 0) i*eta*G_dd(E0+i*eta)=0`.  A second nonauthor
review independently verified that this exhausts the cyclic even measure and
therefore the full parity-reduced spectrum.

C346's first cross-review found two literal `qquad` strings rendered in the
PDF and an omitted initial-value line in the Banach fixed-point converse.  The
source now uses the intended TeX spacing, the text gate rejects any recurrence,
and the fixed equations plus `x(0)>=0` explicitly imply
`y1(0)<=rho*y2(0)`, `y2(0)<=sigma*y1(0)`, hence `y(0)=0` when
`rho*sigma<1`.  A second nonauthor review exercised the new sentinel in memory,
reran the release and rechecked every sharp-threshold and stability clause.

C347 passed a nonauthor rederivation of the parabolic continuation estimate,
zero-flux argument, positive-series Bessel quotient lemma and equivalent
Turán inequality, factor-two critical threshold, every Fourier eigenvalue and
the critical series through cubic order.  Its final three pages and all
content-addressed release gates passed without a theorem-critical correction.

C348's review found that a cited arXiv identifier had been assigned to the
wrong author; the whole package now locks the correct Zeitouni Saint-Flour
chapter DOI.  It also replaced a terse mixing argument with a quenched strong
Markov construction: conditional one-crossing segments are represented by
iid auxiliary rows, the crossing array is a factor of the simultaneous
Bernoulli shift, and Fubini explicitly transfers each annealed probability-one
event only to almost every quenched environment.  The finite/infinite-mean
inversion and both reflected speed chambers were then independently rederived.

Every checker imports no producer code.  JSON parsing rejects duplicate keys
and nonfinite constants.  Evaluation parsing locks exact schemas and rejects
aliases, anchors, merges, non-string keys, implicit timestamps, unknown
fields, type changes, authority drift and tuple drift.  Hostile suites repair
evidence hashes before semantic attacks, every Python entry point rejects
optimized execution, and isolated producer runs replay byte for byte.

## Citation and scope integrity

The source audits assign the Manley--Rowe relations and three-wave amplitude
equations to their primary wave-interaction literature; the discrete--continuum
and interference lineage to Friedrichs and Fano; orthant reflection and
Lipschitz mapping context to Harrison--Reiman and Dupuis--Ishii; the noisy
coupled-oscillator and reversible mean-field-rotator setting to Sakaguchi and
Bertini--Giacomin--Pakdaman; and the iid direction--speed theorem to Solomon,
with Zeitouni's Saint-Flour chapter as a later formulation.  Workspace
reconstruction, packaging and collision screening are not presented as
literature priority.

All five evaluations use evaluator v0.2.0, SHA-256
`6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`,
and set `route_b_invocation_allowed: false` under literal scope
`NO_BAD_EULER_OR_ROOT_NUMBER`.  No target arithmetic local datum, Euler
factor, bad-prime datum, root number, automorphy object, target
divisor/counting law or functional equation, target zero match,
Hilbert--Polya operator, or Route-B input is asserted.  Elliptic phase returns,
impurity poles, regulator contacts, Kuramoto harmonics and random-environment
products retain only their explicitly evaluated source-side meanings.
