# Batch review: HCS-C299--HCS-C303

## Release basis

This review covers five independent theorem packages frozen from source
commit `83c058259c02707d004fca2d6b1a4ebaf5036094`, evaluated with
`flow_systems/skills/route-a-evaluator.md` v0.2.0 at SHA-256
`6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`,
fixed epoch `1788307200`, and literal scope
`NO_BAD_EULER_OR_ROOT_NUMBER`.

The owner and proof mechanism change in every slot: similarity reduction and
Biot--Savart reconstruction for a viscous vortex; monotone wave curves for a
hyperbolic conservation law; lattice refinement and occupancy for an
absorbing Markov chain; recursive distributional contraction for Quicksort;
and Choi/PPT analysis for a quantum dynamical semigroup.  These are five
separate papers, not fragments of one result.  Finite evidence audits exact
formulas and parameter boundaries; every headline statement is proved
analytically.

Every released package has 27 content-addressed payloads plus a self-excluded
manifest.  It retains three substantively different manuscript rounds, with
`paper/main.pdf` byte-identical to Round 2.  Each round is reconstructed twice
in isolated directories with two LuaLaTeX passes under the fixed epoch.
Warning-free settled logs, embedded/subset fonts, extracted-text sentinels,
page renders, exact evaluator trees, repaired-hash hostile mutations and
closed file ledgers are release gates.

## Hostile-review closure

C299's theorem was kept inside the regular finite-circulation radial forward
self-similar class.  The first integral exposes the otherwise hidden
constant, which regularity at the origin forces to zero.  A review then fixed
the historical journal spelling, declared the Lagrangian angle to be a
continuous real lift rather than only an element modulo `2*pi`, and hardened
the checker from shape-only tests to exact nonclaim, boundary, reference,
row-key and canonical-rational trees.  New repaired-hash mutations lock those
changes.

C300 was attacked at the mathematical and serialization levels.  Three naked
typesetting tokens in displayed formulas were removed.  More importantly,
the manuscript now computes the shock entropy production explicitly as

`a^3 rho_0 sqrt(r)[log(r)-(r-r^(-1))/2] < 0`, `r>1`,

rather than inferring its sign by slogan from the Lax inequalities.  A second
red team forged the model, theorem, nonclaims, boundary prose, source roles,
case IDs, numeric types and Route-A YAML while repairing the evidence hash.
The released checker therefore locks complete typed trees, ordered unique
case IDs, canonical numeric strings and the full evaluation object.

C301 does not infer diagonalizability merely from triangularity.  Its rank
filtration supplies a squarefree annihilating polynomial, and the distinct
diagonal values then give diagonalizability over the rationals.  The contract
was also tightened to `n>=1`, so no hidden `0^0` convention enters the kernel
or absorption formula.  The critical limit is stated in terms of convergence
of `n^2/2^t`; dyadic rounding is retained instead of being averaged away.

C302 originally moved too quickly from a fixed-transform contraction to the
varying finite-subproblem recursion and then cubed a law known only to lie in
`L^2`.  The final proof builds the finite and limiting variables on one
i.i.d.-uniform binary tree.  An exact weighted recurrence and a limsup cutoff
close recursive `L^2` convergence with coefficient-square limit `2/3`.
Separately, a summable tree-level moment bound proves `L^3` integrability
before the third-moment identity is used.  Type-and-length mutations then
closed Boolean-as-integer and zip-truncation escapes in finite PGF and
centered-pivot rows.

C303 separates all singular parameter faces.  The zero generator has a
four-dimensional Liouvillian kernel, whereas the other nonzero
population-preserving faces have a two-dimensional kernel.  The faithful
two-sided thermal chamber has one finite entanglement-breaking threshold;
one-sided damping and pure dephasing reach the entanglement-breaking boundary
only at infinite time.  The Choi/PPT inequality, coherence convention,
upward/downward polarity and exact trace contraction were independently
recomputed after this correction.

## Five theorem-scale advances

### HCS-C299 -- Lamb--Oseen radial self-similar vortex

For the two-dimensional Navier--Stokes vorticity equation at `nu>0`, every
regular finite-circulation radial forward-self-similar solution is the signed
Gaussian Lamb--Oseen vortex.  The paper derives the profile from the
similarity ODE, reconstructs the exact Biot--Savart velocity, integrates the
continuous-lift particle angle through an exponential-integral primitive,
and closes all radial moments, `L^p` norms, enstrophy/palinstrophy dissipation,
core behavior, zero circulation, singular age and inviscid measure limits.

Route-A verdict:
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)`, `ROUTE_A_REJECTED`.

### HCS-C300 -- positive-density isothermal Euler Riemann solver

For arbitrary positive left/right densities, finite velocities and sound
speed `a>0`, the two isothermal wave curves meet at the unique positive root
of one strictly increasing scalar equation.  This yields the unique
self-similar Lax solver, all four nondegenerate shock/rarefaction patterns,
all zero-wave faces, exact fan profiles and shock speeds, strict Lax and
mechanical-entropy inequalities, density-scaling symmetry and the theorem
that no finite datum in this chamber creates vacuum.  Exact separating and
compressive families expose why the pressureless limit is singular.

Route-A verdict:
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)`, `ROUTE_A_REJECTED`.

### HCS-C301 -- parallel binary partition fragmentation

For fair independent bit refinement of every block of a labelled set
partition, the paper determines the complete one-step and `t`-step kernels on
the partition lattice.  From one block it gives the exact law of every target
partition, the full spectrum `2^(k-n)` with Stirling multiplicities, rational
diagonalizability, and the absorption CDF `(2^t)_n/2^(tn)`.  The collision
representation by uniform `t`-bit words yields the sharp birthday window
`exp(-lambda/2)` and its unavoidable dyadic phase.

Route-A verdict:
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)`, `ROUTE_A_REJECTED`.

### HCS-C302 -- randomized Quicksort comparison costs

For classical single-pivot Quicksort on uniform distinct permutations, the
paper closes every finite comparison-cost law through an exact PGF recurrence
and derives the all-`n` mean and variance.  With the exact `n+1`
normalization, a single recursive coupling proves `L^2` convergence to the
unique centered contraction fixed point.  A separate tree-series moment
argument licenses the exact identities
`E[Y^2]=7-2*pi^2/3` and `E[Y^3]=16*zeta(3)-19>0`; the latter proves that the
limit is non-Gaussian.

Route-A verdict:
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)`, `ROUTE_A_REJECTED`.

### HCS-C303 -- thermal-qubit Lindblad entanglement-breaking atlas

For downward and upward amplitude damping, pure dephasing and a diagonal
Hamiltonian, the paper exponentiates the qubit GKSL generator exactly.  It
gives the affine Bloch flow, stationary state, complete Liouvillian spectrum,
semigroup law and sharp trace-distance contraction.  The normalized Choi
matrix and two-qubit PPT criterion yield the exact entanglement-breaking
inequality, the unique faithful-thermal threshold, its no-extra-dephasing
radical, and every one-sided, pure-dephasing, unitary and identity boundary.

Route-A verdict:
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`,
`ROUTE_A_REJECTED`.

## Exact release accounting and hashes

The tables in this section are populated only after every repaired hostile
gate, the five closed-world manifests, independent cross-audits and final
root-level replay pass on the same bytes.

| ID | finite evidence | checker assertions | symbolic checks | hostile rejections | evidence bytes | final pages/fonts |
|---|---:|---:|---:|---:|---:|---:|
| C299 | 213 audited cells | 1,195 | 31 | 84/84 | 82,785 | 4 / 24 |
| C300 | 437 audited cells | 1,219 | 30 | 110/110 | 71,893 | 3 / 18 |
| C301 | 44,168 transition cells | 3,570 | 17,910 | 57/57 | 354,369 | 3 / 27 |
| C302 | 173 PGF + 527 pivot cells | 8,377 | 2,424 | 72/72 | 170,183 | 3 / 23 |
| C303 | 124 audited rows | 709 | 129 | 35/35 | 42,956 | 3 / 24 |
| **total** | **five distinct ledgers** | **15,070** | **20,524** | **358/358** | **722,186** | **16 / 116** |

C301 additionally archives 81 all-time rows, 405 block-count coefficients,
104 absorption-mass rows and five critical-window diagnostics.  C302's
finite ledger also records 13 complete PGFs and six variance-limit rows.  The
table deliberately preserves these package-specific units instead of
pretending that a PDE residual, a Markov-matrix cell and a Choi row are the
same observable.

| ID | evidence SHA-256 | round 0 PDF SHA-256 | round 1 PDF SHA-256 | round 2 / final PDF SHA-256 | manifest SHA-256 |
|---|---|---|---|---|---|
| C299 | `518343c593f63402eabbcb602761d54c56003d27c3e9f3774ee405b5115c74c2` | `1c127bc83686c042835e589ccbfbbe84609b5ac90e336f973557f03c4a4fedc9` | `8e2ba5c010ae21cf61edffcfa77f69df2f49c0293c3e2a94bc2ae915ffd19de7` | `5b1a4d4dd9480e55ff970b5ae01dac8435c5c9ac4a62ee3c1f740288cd342b61` | `eb3b36cfe6b3ed8e46a8f34f0320bd41477908760d89bcd75aa6ffe9c75337dd` |
| C300 | `e4a054b3485659ac58021f94b6f36c11a331b92efee04dd1930f910b5a2d994e` | `d494467b8163758a36e942a588982ab358a18d263be3236eeef0aa86755a9a69` | `32020b4388648121ae19fd60ece4ca076476c023190d8265566335017d79936a` | `051da17fe465f1314e40a00329bf06d677b598080f8609cd05f6b9af4790e90a` | `b3dbc2da7e5bd0717da8406fc6b280ad41088ab1b769bb2b541daa24f7aef18b` |
| C301 | `011f146e1fecfb88a6cc4a692d95a8267b9549cfefa43628083ab1aa21b06a03` | `a11bf5746fc2a2056754139143d5abde3ee4f56b56c287c923ce6768a3d0669f` | `8cd42fe5a6b46792c7a57b9e372a398a0806dd6a6931ec887a28ca99f84055c2` | `f09a3fc6ee5f1a2c0954d7d4d7db11d98f01cfc7741e9c82a0a8fb98f92ce872` | `2404dee52364f38a4a3b4ba8d9686f01c10aad4a2f4127773751a5dddb7fac00` |
| C302 | `0ceba774a464fa86ffa9cb20c44b4b7c57aafb3c6d5aec5a63f1417f92e788fc` | `a623329732dd0ca43dd54c1f1798b58b3ee4820d019f981759dff25c1f96f397` | `a8f95799b46c71ea7c67f3bd66e5f011a95a13ac577b810186d6b457003c7a46` | `e28a494e10ffa2f67f724b7458264bab62d30db6868a2c0ee38e50b46d5921bc` | `91050b3740fe8fbbb940535590d43812d45be1c380d6a24ddcb2e9414b936bd0` |
| C303 | `f3ceeec5f667b97f09ea2963b204dd35e64d5fc2f263a3a71c084fae9764f483` | `a76618c30507dbae459d920e98d60e796278de712cea42dc6113e3dee209948a` | `e2a467c3f76a6b77e0eacaa243a664ff0b74b2378e21df7bf8f9f1b1a422576b` | `16c82784cff2f4cbe661938e425c5065dd77ee4de220f9caaa3ff1d7c6a9c544` | `e6a1d7afe743bdbd25382a1fb5cd7271a3b5bcff9f4462da534505cba32fc1a8` |

Every row has three distinct retained revision hashes and a final PDF equal
to Round 2.  The five manifests cover 135 content-addressed payloads and 140
physical package files.  Every settled build log is free of layout,
citation, reference, destination, missing-character and rerun warnings; all
116 final font rows are embedded and subset, and all 16 final pages were
visually inspected.

## Citation, proof, and scope integrity

The papers assign the classical Lamb--Oseen, Lax Riemann-solver,
partition-refinement, Quicksort-limit and GKSL/Choi/PPT neighborhoods to named
literature owners.  Repository packaging is never used as evidence of
literature priority.  Every headline theorem is analytic; finite tables are
regression and convention evidence only.

All five evaluations set `route_b_invocation_allowed: false`.  No target
arithmetic local datum, Euler factor, bad-prime datum, root number, automorphy
object, target divisor/counting law or functional equation, target zero
match, Hilbert--Polya operator, or Route-B input is asserted.
