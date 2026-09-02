# Batch review: HCS-C304--HCS-C308

## Release basis

This review covers five independent theorem packages frozen from source
commit `c0259978b1d7ebae63fe7b39fce1af2655b8529d`, evaluated with
`flow_systems/skills/route-a-evaluator.md` v0.2.0 at SHA-256
`6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`,
fixed epoch `1788393600`, and literal scope
`NO_BAD_EULER_OR_ROOT_NUMBER`.

The dynamical owner changes in every slot: a fourth-order periodic PDE
semigroup, a Euclidean measurable-control problem, a killed determinantal
Markov process, a monotone random-graph growth process, and a finite
non-normal lattice Hamiltonian.  These are five separate papers rather than
five subdivisions of one result.  Every headline quantifier is owned by an
analytic proof; finite evidence is used only for conventions, exact
regression, and hostile-boundary tests.

Every package has 27 content-addressed payloads plus a self-excluded
manifest.  It retains three substantively different manuscript rounds, with
`paper/main.pdf` byte-identical to Round 2.  Each round was reconstructed in
two isolated directories with two LuaLaTeX passes under the fixed epoch.
Warning-free settled logs, embedded/subset fonts, extracted-text sentinels,
page renders, exact evaluator trees, repaired-hash mutations, and closed file
ledgers are release gates.

## Hostile-review closure

C304 was challenged on the step from a finite shell receipt to a
full-dimensional fastest-mode theorem.  The released proof supplies an
analytic exhaustion cutoff and retains every represented-shell tie; the 12
displayed receipt shells are explicitly not the proof.  A post-round audit
also separated the natural `kappa=0` domains: `H^2 intersect L^2_0` for the
nonzero Laplacian generator and all of `L^2_0` for the zero generator.  The
build description now counts three round variants and identifies the final
PDF as a Round-2 alias.

C305's root geometry was attacked in every chamber.  The final theorem uses
the smaller strong-wind root, keeps the whole interval `[T_-,T_+]`, includes
the origin in the closed forward cone, and records the different zero-target
time sets.  The implicit HJB proof is restricted to `c>0`; the only
nonvacuous zero-cap ambient interior, the one-dimensional forward ray, is
proved directly.  Registry inspection also removed false associations with
C248/C249/C283 and replaced them with the actual control/flow neighbors
C222, C270, and C268.  Repaired-hash mutations lock the corrected map.

C306 fixes the killed convention at the generator level: an attempted
boundary exit or collision terminates the process and is never silently
reflected or suppressed.  The exterior-power basis displays coincident mode
sums with their true multiplicities, while the positive ground state is used
separately for the QSD and Doob transform.  The full-occupancy singleton,
where the killing rate is `2L` and no relaxation mode exists, is not forced
through the `k<L` gap formula.  The continuous-time Darroch--Seneta source
and its DOI were independently checked, and a typesetting audit removed the
last malformed spacing token before the deterministic rebuild.

C307 does not infer connectivity from isolated vertices alone.  After the
isolated-vertex factorial moments, its without-replacement proof inserts a
spanning-tree factor for every component of size at least two and sums two
uniform ranges, through `n/log n` and from there to `n/2`.  This closes the
probability of disconnection without isolated vertices as `o(1)`.  A raw
control character and ambiguous falling-factorial notation were removed.
The final scope asserts weak Gumbel convergence only: no finite-`n` equality
with the last-isolated-vertex time and no unbounded-moment convergence.  Its
true C301/C291/C276 workspace neighbors are now part of the typed evidence,
independent checker, and repaired-hash mutation contract.

C308 distinguishes right-amplitude skin concentration from the
`q`-independent pointwise biorthogonal density.  It states the eigenbasis
condition number only in the canonical sine gauge, treats the one-sided open
chain as one nilpotent Jordan block, and keeps the periodic chain as a cyclic
normal matrix.  The standard oriented ring theorem is frozen at `N>=3`; the
coincident-neighbor `N=2` convention is separate.  Registry inspection
replaced tentative false neighbors with the actual C267/C288/C297/C303
structural boundary.

## Five theorem-scale advances

### HCS-C304 -- full-dimensional linear Cahn--Hilliard spinodal atlas

For every finite `d>=1`, `kappa>0`, and real `alpha`, the mean-zero periodic
generator is self-adjoint, bounded above, and produces an analytic
positive-time trace-class semigroup.  The paper gives the exact lattice-shell
spectrum and multiplicities, free-energy dissipation, complete
stable/critical/spinodal chamber, Morse index and kernel, every fastest shell
and tie, actual-support asymptotics, and the theorem that every recurrent
state is stationary.  The singular zero-capillarity face is closed as heat,
identity, or failure of bounded-semigroup generation.

Route-A verdict:
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`,
`ROUTE_A_REJECTED`.

### HCS-C305 -- constant-wind Zermelo navigation beyond weak wind

For every finite Euclidean dimension, constant wind, nonnegative control
cap, and target, the exact time-`t` reachable set is a translated ball.  One
quadratic contact theorem gives full-space weak-wind reachability, the
critical open half-space, the strong-wind forward cone, exact minimum times,
and every attainable-time set.  It also proves the unique a.e. constant
saturated optimizer, rotation and scaling laws, the HJB equation, the
double-root cone singularity, and all zero-wind, zero-cap, zero-target, and
one-dimensional faces.

Route-A verdict:
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)`,
`ROUTE_A_REJECTED`.

### HCS-C306 -- killed noncolliding walkers and the Q-process

For all `1<=k<=L`, the one-particle Dirichlet sine basis and the
Karlin--McGregor determinant give the complete killed kernel in the ordered
discrete Weyl chamber.  Antisymmetric tensor powers provide every Slater
eigenfunction and all `binom(L,k)` modes.  The positive ground state then
closes the exact survival and absorption laws and moments, leading decay,
spectral gap, unique quasi-stationary distribution, and conservative Doob
transform with invariant law `h^2`, including the one-particle and
full-occupancy boundaries.

Route-A verdict:
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`,
`ROUTE_A_REJECTED`.

### HCS-C307 -- exact connectivity hitting and its Gumbel window

Decomposition by the component containing vertex one yields an exact
all-`n,m` recurrence for connected labelled graphs.  Uniform edge-prefixes
therefore give the complete finite connectivity-hitting CDF, PMF, tails,
moments, and deterministic support.  At
`m=floor((n/2)(log n+c))`, factorial moments give the Poisson isolated-vertex
law and the two-range spanning-tree bound removes every other component,
proving the standard Gumbel limit for the normalized hitting time in the
actual `G(n,m)` process.

Route-A verdict:
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)`,
`ROUTE_A_REJECTED`.

### HCS-C308 -- finite Hatano--Nelson boundary and skin atlas

For positive hoppings, a diagonal similarity sends the open chain to a
symmetric path, yielding its Chebyshev characteristic polynomial, real
simple spectrum, canonical left/right sine basis, biorthogonality,
conditioning, propagator, and resolvent.  Periodic boundary conditions give
the exact Fourier points on the spectral ellipse.  The same theorem closes
the Hermitian face, orientation reversal, both one-sided Jordan-versus-cyclic
faces, the zero matrix, the two-site convention, and the singular
open/periodic boundary limit without importing topology or disorder claims.

Route-A verdict:
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`,
`ROUTE_A_REJECTED`.

## Exact release accounting and hashes

The package-specific evidence units are preserved because a PDE shell, a
navigation probe, a chamber state, a graph mask, and a matrix boundary row
are not interchangeable observables.

| ID | finite evidence | checker assertions | symbolic identities/cells | hostile rejections | evidence bytes | final pages/fonts |
|---|---:|---:|---:|---:|---:|---:|
| C304 | 18 cases / 216 shells / 1,653 leaves | 1,930 | 36 | 72/72 | 77,985 | 3 / 26 |
| C305 | 29 cases / 12 HJB probes / 744 leaves | 734 | 27 | 85/85 | 38,897 | 3 / 21 |
| C306 | 36 cases / 502 states / 273 probes | 5,803 | 221 | 68/68 | 135,733 | 3 / 26 |
| C307 | 298 count cells / 33,867 masks / 60 diagnostics | 5,606 | 338 | 82/82 | 99,360 | 3 / 26 |
| C308 | 123 audited rows | 1,070 | 259 | 43/43 | 45,425 | 3 / 17 |
| **total** | **five distinct ledgers** | **15,143** | **881** | **350/350** | **397,400** | **15 / 116** |

C306's symbolic total comprises 15 characteristic cases, 72 coefficient
identities, 114 phase-type moment cells, and 20 full-occupancy identities.
C307's total comprises 129 connected-coefficient checks, eight polynomial
identities, 48 tail-moment identities, and 153 isolated-factorial cells.

| ID | evidence SHA-256 | round 0 PDF SHA-256 | round 1 PDF SHA-256 | round 2 / final PDF SHA-256 | manifest SHA-256 |
|---|---|---|---|---|---|
| C304 | `a1f026d7cb41c12c2cbe798eba28ee75e07f4e0aa909434a0c92da9d78a488bc` | `5bd10d6e78d18bbdeeffe967329a80bb7e896ab13bba9d2ebec60149505752b1` | `6b5ed469f5a8bda8113fd3ea7a8444fdfb2f7f6597331ed8fb0ae25afa6370fe` | `9d9525ab50369f110dbfd0a98ff3f153b7c6c146b3c0facfe0f1f2ac9f2b3c47` | `cddc7e298cdc2d4ba82c37c48c8edce3e2d1e00a9437219af16168f0345aa7f5` |
| C305 | `dd971dc65ced312ae4d09f15fb2625ea230dc913d7acbd6313037ff5159f9f58` | `e4cb469251a2626bb8d0bdcda23cd9e00765092de4e9c88b26deb63b87cc4af1` | `321e68a9f67939550ed259b70c26242fc3ed011db08ebd210d0a3d1825fdb06a` | `26b69034b7cef082f01028a5c2c8b74c45d313aa1324ccdacfe434eae9bf6eea` | `a578250f24c1a67536a3b19b52bd4c1904bee17e3b0b722c082f1e7044d95ca7` |
| C306 | `9f9cd4bc19881165321750845302541ead2b9ac13399da52807335148ab54560` | `984778f5571b5a401afcb488795909331f4a8f39e73b91b5951c05be1811e913` | `0fff12a0f675220b14807eabda627ae227e7638d1bbaa93f96570812e2d1e151` | `d951d8019029fbba3145a406461cd534451374e28ae786488678acf2ba77e92a` | `ad24d99436e0ad353cd0748cd1b5f6d6db435a2ec17edaa8e88eea39783cd279` |
| C307 | `6c886e10f6aa405d0c34fc134ebe42c185e801e1aae20039dc0829016cc92cfd` | `48422f1fd9f9a03a777f2ff7487d3e2a6d0c75f9b173b882ce52749bb4e0abf7` | `57adea30caf75026d6672365fc0eaae5bb4805be6dfb562d3cad408e5dd35953` | `2d0b722327df4079b63dbe72cb1c757c176e59ff01cb1b953a8045ca63412916` | `fb8c3275559fd4c966dafaa5e2dd6b05dc08ee4641187681638d4afba3fbb98e` |
| C308 | `01ab53a54c00ec80c3dc6ccefbd827b35c001ebbd38a4cf1ce6ccefad9eb261c` | `c6b969ca113ae80684098f450f846ddfa556c06cbee32e05d3389e5ee9d215dc` | `386d2743aad8a079071662d39bebb17f92045e31e1d7dd3e3cc9bd5c615e6b93` | `0ddd3fad510c184a999ad785ab7ac1af170b66169f15b54bda92b9fcb5e1e8bd` | `85c21be74076c1c9c51b44c4f32b028c1e738e35bbbdf2aa0afd69f12c89bfb4` |

Every row has three distinct retained revision hashes and a final PDF equal
to Round 2.  The five manifests cover 135 payloads and 140 physical package
files.  All 15 final pages were visually inspected; all 116 final font rows
are embedded and subset.  Settled build logs are free of layout, citation,
reference, destination, rerun, and missing-character warnings.

## Citation, proof, and scope integrity

The papers assign the Cahn--Hilliard/spinodal, Zermelo navigation,
Karlin--McGregor/Darroch--Seneta, Erdos--Renyi, and Hatano--Nelson
neighborhoods to their historical literature owners.  Repository packaging
is never used as evidence of literature priority.  The collision map was
checked against the C1--C303 registry after drafting, including the corrected
C261/C277 and C276 distinctions in the batch idea report.

All five evaluations set `route_b_invocation_allowed: false`.  No target
arithmetic local datum, Euler factor, bad-prime datum, root number, automorphy
object, target divisor/counting law or functional equation, target zero
match, Hilbert--Polya operator, or Route-B input is asserted.
