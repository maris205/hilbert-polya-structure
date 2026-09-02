# Batch review: HCS-C289--HCS-C293

## Release basis

This review covers five independent theorem packages frozen from source
commit `7fbe9db30cc460a82883533d7cfb2edd988c5b65`, evaluated with
`flow_systems/skills/route-a-evaluator.md` v0.2.0 at SHA-256
`6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`,
fixed epoch `1788307200`, and literal scope
`NO_BAD_EULER_OR_ROOT_NUMBER`.

The owners, clocks, and proof mechanisms change in every slot: a homogeneous
magnetic flow on a negatively curved surface, a rotating-frame celestial
Hamiltonian, a finite random greedy adsorption process, an irreversible
coalescing particle flow, and a degenerate magnetic quantum operator.  Each
manuscript proves a separate all-parameter or all-size result.  The finite
evidence cells audit formulas, branches, and conventions; they do not replace
the analytic, combinatorial, weak-PDE, or operator proofs.

Every released package has 27 content-addressed payloads plus its
self-excluded manifest, retains three substantively different manuscript
rounds, and makes `paper/main.pdf` byte-identical to Round 2.  Each archived
round is reconstructed twice in isolated directories with two LuaLaTeX passes
and the fixed epoch.  Warning-free settled logs, embedded/subset fonts, page
counts, extracted theorem sentinels, and exact file ledgers are release gates.

## Hostile-review closure

The first evidence versions were not accepted merely because their nominal
checkers passed.  C289's initial template residue was removed and its Lorentz
matrix convention was made explicit as the right-action column-frame equation
`F'=FA`, eliminating an apparent sign reversal.  A later cross-review rejected
the inference from full-frame nonreturn to base-point nonreturn.  The final
proof instead computes `exp(tA)e_0`: at criticality its tangent component is
`kappa*v*t`, while in the circle chamber the two independent components force
`sin(theta)=0` and `cos(theta)=1`.  Thus horocycle nonclosure and primitive
circle return are now base-point statements.  The same review downgraded A4
to a formal hint because no self-adjoint quantum realization is constructed.

C290 began as a copied C288 delta-interaction shell; all old code, prose,
evidence, and PDFs were treated as invalid and rebuilt for the CR3BP theorem.
The hostile review then removed an erroneous phrase suggesting that linear
boundedness failed at resonant mass ratios: the linear flow remains bounded
through the entire open Routh chamber, while only nonlinear resonance and KAM
claims remain outside scope.  Both signs of the triangular mixed Hessian are
checked at the defective boundary, and the historical ownership is separated
between Gascheau's 1843 result and Routh's later treatment.

C291 initially admitted two repaired-hash mutations: a changed high factorial
moment and a changed collision-registry distinction.  The independent checker
now reconstructs every stored factorial-moment cell from the all-order
conditional identity, locks the full collision contract, and rejects both
escapes.  A separate manual census corrected the manuscript's edge-order total
to include the empty permutation of `P_0`.

C292's mathematical certificate passed its first independent exact run, but
text inspection found a missing TeX backslash in the weak-form chain rule and
stale scenario totals in the manuscript.  Both were synchronized with the
canonical evidence and promoted to extracted-text release sentinels.

C293 exposed the most consequential semantic error: one resonant angular
Fourier channel had been conflated with spectral multiplicity one.  The free
line Laplacian actually has absolutely continuous multiplicity two almost
everywhere on positive energy.  The theorem, evidence, checker, manuscript,
and repaired-hash mutation suite now distinguish the single angular channel
from its two momentum branches.  The integer-flux operator retains both this
absolutely continuous sector and embedded oscillator eigenvalues.

A final release-integrity attack appended a second YAML
`route_b_invocation_allowed: true` key.  String-sentinel-only manifests could
miss that semantic override even when the checked-in YAML was benign.  All
five releases therefore parse evaluator YAML with a duplicate-rejecting safe
loader, enforce exact key/type/value contracts, and carry explicit conflicting-
key, unknown-key, tuple, scope, and Route-B mutations.

## Five theorem-scale advances

### HCS-C289 -- constant magnetic flow on the hyperbolic plane

For the equation `D_t dot(gamma)=b J dot(gamma)` on curvature `-kappa^2`, the
paper derives a constant Lorentz-frame generator and classifies every orbit.
Strong field `|b|>kappa v` gives hyperbolic circles with primitive period
`2*pi/sqrt(b^2-kappa^2 v^2)`; equality gives nonclosed horocycles and a
nonzero index-three nilpotent generator; weak nonzero field gives hypercycles;
and zero field gives geodesics.  A separate Frenet radius--circumference proof
checks the clock, while zero speed, sign reversal, and the Euclidean limit are
kept distinct.  The closed circles form clean positive-dimensional families,
not isolated arithmetic primitive owners.

Route-A verdict:
`(A0_FAIL,A1_WEAK,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`,
`ROUTE_A_REJECTED`.

### HCS-C290 -- five Lagrange points and the exact stability threshold

For `0<mu<=1/2`, strict monotonicity on the three singular x-axis intervals
proves that the planar circular restricted three-body problem has exactly
three collinear equilibria, while direct substitution gives the two
triangular points.  The collinear Hessian has `S>1`, forcing one real and one
imaginary eigenvalue pair at every point.  At the triangular points the
characteristic polynomial is
`lambda^4+lambda^2+(27/4)mu(1-mu)`.  This yields the exact Routh--Gascheau
threshold `(9-sqrt(69))/18`; equality is defective, with linear growth, and
is not mislabeled stable.  The statement is linear only.

Route-A verdict:
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`,
`ROUTE_A_REJECTED`.

### HCS-C291 -- finite dimer RSA on every path and cycle

Conditioning on the first accepted edge gives an exact PGF convolution for
all paths and a Riccati ordinary generating function.  Arbitrary
differentiation yields a triangular hierarchy for every factorial moment;
the first two closed solutions give exact finite means and
`Var(M_n)=exp(-4)n+2exp(-4)+o(1)`.  Binary gap words prove that every integer
between the sharp lower and upper support bounds is attained.  For cycles,
`G_n(z)=zF_{n-2}(z)` gives the complete distribution, the boundary mean
correction tending to `exp(-2)`, and the same linear variance coefficient.
The terminal matching is maximal, not necessarily maximum.

Route-A verdict:
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)`,
`ROUTE_A_REJECTED`.

### HCS-C292 -- arbitrary finite all-event sticky-particle flow

After canonical premerging of initially coincident positive masses, one
adjacent-event construction handles binary, multi-cluster, and spatially
disjoint simultaneous collisions.  The same flow is the mass-weighted
isotonic projection of the free configuration and the slope process of a
cumulative-mass lower convex hull.  These representations prove global
forward uniqueness, no splitting, and the `N-1` merger bound.  Each event
satisfies an exact pairwise-variance energy-loss identity, and the associated
atomic density and momentum solve pressureless Euler distributionally with
the kinetic-energy entropy defect concentrated at collisions.

Route-A verdict:
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)`,
`ROUTE_A_REJECTED`.

### HCS-C293 -- magnetic Baouendi--Grushin cylinder

The closed nonnegative quadratic form on standard Lebesgue
`L^2(R times S^1)` defines a Friedrichs operator whose angular Fourier blocks
are shifted harmonic oscillators.  Nonintegral flux has compact resolvent and
pure point spectrum `(2n+1)|k+alpha|`.  Integral flux opens exactly one free
angular channel, whose line-Laplacian absolutely continuous spectrum has
multiplicity two almost everywhere, while all nonresonant channels retain
embedded positive-integer eigenvalues.  Their multiplicity is
`2d_odd(N)`, heat trace is `2 sum d_odd(N)e^{-tN}`, and source-local spectral
series is `2(1-2^{-s})zeta(s)^2`.  The series is not a target Euler product,
divisor law, functional equation, zero bridge, or Hilbert--Polya operator.

Route-A verdict:
`(A0_WEAK_ARITHMETIC_RELATION,A1_FAIL,A2_FAIL,`\
`A3_PARTIAL_ANALYTIC_STRUCTURE,A4_NATURAL_QUANTIZATION)`,
`ROUTE_A_REJECTED`.

## Exact release accounting and hashes

The exact totals below were populated only after every repaired hostile gate,
the five closed-world manifests, the independent cross-audits, and a final
root-level replay all passed on the same files.

| ID | checker assertions | symbolic checks | hostile rejections | evidence bytes | final pages/fonts |
|---|---:|---:|---:|---:|---:|
| C289 | 4,613 | 371 | 43/43 | 46,547 | 4 / 24 |
| C290 | 781 | 46 | 65/65 | 23,510 | 4 / 25 |
| C291 | 19,371 | 132 | 105/105 | 23,778 | 5 / 24 |
| C292 | 1,538 | 255 | 66/66 | 35,704 | 4 / 19 |
| C293 | 2,053 | 750 | 75/75 | 37,777 | 4 / 26 |
| **total** | **28,356** | **1,554** | **354/354** | **167,316** | **21 / 118** |

| ID | evidence SHA-256 | round 0 PDF SHA-256 | round 1 PDF SHA-256 | round 2 / final PDF SHA-256 | manifest SHA-256 |
|---|---|---|---|---|---|
| C289 | `83a0f4b44909a88931ba20bff50019d6a6824b77aefc8a9e30406ab97d06eac0` | `989ee3a527d893e2ba2e8f0a7d17ab82629a3225b5c4fec1cb6ecadd1a1b64b4` | `f63494f71de5b93efa02aed2b4a53785b47abba082adc25eb2bd26ef857a9f35` | `c3361619fe4d967223415894bd712a772989827a0ebc2de5b0fd98872b328cd1` | `3beb6eff7b5f20017c90c66bb234d77a43f0adc74db0924f6019b42c78cecc50` |
| C290 | `e282dd2df3ea8aa0cbec179dff3c9ee39f83cd181f23f026b28598cc9a4a3fe2` | `7c3d1df6a841187f8a0e65ad73f5d4d850d1d3a0b4921beb21590960ea2ba4d6` | `42927de3b7740dd44e340c0b43c5796bf952efc0477dc052987378b2aefeef88` | `88ce6ad9ad23e0cebea986cf9305bc6b258c5816170120e656c334b0b38aed9e` | `5d1bdc120d29e4588f5597260340487b00249035f5e12b8b9f990fdab0fdb211` |
| C291 | `65fdb2333d3fbb6c3177eaa7da5d303ab0b42f2ff99b8d55ecd97e1863008a0f` | `0a0d27c5341ea1eb04e31763c6eaf878f9281b95b5bce6137c34067c08123043` | `c797bca28272288017a5156ab16a15dbab7040a90e611aecaf1db2a78a2d594f` | `b410ec70209302f891992712b4a6be16663e04d2a79cd6f7e4f1e762fef64a22` | `1b3c08ce97a5cb39516443d55a7864ee76f6f98a75a716b6a8bf124b52263bf6` |
| C292 | `dace90669ac08c25b18427dee176b0f09b6754d0fc9d597b8986575363f84809` | `b361f9926d5ff4cf166f3f8d450b9002935cf983c12b0b0a6db4c5299508f884` | `f3cec9741098acaa31816b43af464544b4025a96d63936b8b3f9222b979c3f16` | `b91f101d7947d4a5e5feeaf3a2dd2d405a3308ed1e0ec8bf984be2cdf262f6d8` | `03b995059d4ec0dbc45c0ac922e58fccad26e285ec3c3959dca82c1683f6a13d` |
| C293 | `b84946889a6036c3b8a7bc11023a8e055a69c905e34535bc30a977c9ac727edd` | `3e7b203f3348837f846133f2079e58622737c83e6364ff20a874fd6f02d30638` | `a5563a310c68a4c150fcbe891b40bb48093aa39e28cbc9124291877cbab7df3a` | `3295011b255e5e70761bd1119af1b8b72453b0724cfbb21663614321a763935d` | `fdf57650492e8bee03fa6ac627005c774112c2b4f33e18004c07bd155e00deeb` |

Every row has three distinct retained revision hashes and a final PDF equal
to Round 2.  The five manifests cover 135 content-addressed payloads and 140
physical files.  Every settled build log is free of layout, citation,
reference, destination, missing-character, and rerun warnings; every font row
is embedded and subset, and all 21 final pages were visually inspected.

## Citation, proof, and scope integrity

The papers assign the classical orbit, equilibrium, adsorption, sticky-flow,
and Grushin spectral mechanisms to named literature owners.  Repository
packaging is never used as evidence of novelty.  Exact formulas reconstructed
in the packages are presented as source-local mathematical results.

All five evaluations set `route_b_invocation_allowed: false`.  No target
arithmetic local datum, Euler factor, bad-prime datum, root number, automorphy
object, target divisor/counting law or functional equation, target zero match,
Hilbert--Pólya operator, or Route-B input is asserted.
