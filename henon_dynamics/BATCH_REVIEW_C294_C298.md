# Batch review: HCS-C294--HCS-C298

## Release basis

This review covers five independent theorem packages frozen from source
commit `f8d3ad9a8940b54e82854b2924be353575ed8fcb`, evaluated with
`flow_systems/skills/route-a-evaluator.md` v0.2.0 at SHA-256
`6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`,
fixed epoch `1788307200`, and literal scope
`NO_BAD_EULER_OR_ROOT_NUMBER`.

The owner and proof mechanism change in every slot: convex coding for an open
dispersing billiard, action--angle analysis for an integrable central force,
an event-driven many-body quotient, exact projective propagation for a
non-Hermitian dimer, and exterior-power/flag analysis for a compact
Grassmann gradient flow.  These are five separate papers, not fragments of
one result.  Finite evidence audits formulas and boundary conventions; the
headline statements are proved analytically.

Every released package has 27 content-addressed payloads plus a self-excluded
manifest.  It retains three substantively different manuscript rounds, with
`paper/main.pdf` byte-identical to Round 2.  Each round is reconstructed twice
in isolated directories with two LuaLaTeX passes under the fixed epoch.
Warning-free settled logs, embedded/subset fonts, extracted-text sentinels,
page renders, exact evaluator trees, and closed file ledgers are release
gates.

## Hostile-review closure

C294 initially identified every reduced cyclic word class directly with an
oriented geometric ray.  That was not injective: `[01]` and `[0101]` have the
same geometric support, traversed once and twice.  The final theorem defines
a periodic-ray iterate as a primitive oriented geometric ray paired with a
positive traversal multiplicity.  All cyclic classes correspond to such
iterates; primitive classes correspond exactly to primitive rays.  The
shift-by-primitive-length symmetry of the convex minimizer proves that word
powers give repeated traversals.  The evidence contract, checker, hostile
mutations, all manuscript rounds and hashes were regenerated after this
repair.

C295 was audited against five recurrent central-force mistakes.  The final
domain begins at the exact circular energy, uses `ell=|L|`, applies the
rational apsidal criterion only to noncircular `ell>0` motions, distinguishes
the radial period from the full Cartesian period `2T_r` of a nonstationary
center-crossing orbit, and keeps the simultaneous Kepler/collision corner
singular.  Independent recomputation found no residual formula or boundary
error.

C296 began with a false full physical-space free-point quotient.  For one
translating rod that claim predicts the available-length period
`(ell-a)/|v|`, not the physical period `ell/|v|`; changing the cyclic cut also
adds a common translation.  The released theorem is therefore explicitly
the quotient by common rotation.  On that shape space the compressed free
flow, simultaneous events, finite event bound and velocity-stabilizer return
criterion are exact, while reconstruction of the missing rotation is
recorded as a cocycle obstruction.

C297's symbolic review caught and separated two discriminants: the Riccati
fixed-ray quadratic has discriminant `-4 delta`, whereas the matrix
characteristic polynomial has discriminant `+4 delta`.  The final proof uses
`H^2=delta I`, retains the defective nilpotent exceptional point, and does not
transport the positive metric across its loss-of-positivity boundary.  A
later release audit also required obstruction `HEN-O281` to be locked in the
evaluator, evidence, checker, mutation and manifest contracts rather than
merely described in global prose.

C298 was designed around two nongeneric hazards.  Distinct eigenvalues do not
make all subset sums distinct, so the limit and rate use the actual nonzero
Plücker support; matroid greedy exchange gives the unique supported leading
basis.  When eigenvalues repeat, selecting one coordinate from a tied block
is wrong.  The final statement instead takes the eigenflag associated graded
and proves the complete product-Grassmann Morse--Bott atlas.  The strict
Lyapunov identity independently excludes nonconstant recurrence.

The global release contract itself found one further issue: obstruction IDs
must be exact machine-readable fields in every package.  C296 and C297 were
rebuilt after `HEN-O280` and `HEN-O281` were threaded through their strict
evaluation/evidence contracts.  Thus a prose-only registry entry cannot pass
the final release gate.

A final type-and-polarity red team then exploited Python's `True == 1` and
`False == 0`, initially escaping through selected finite-row and Route-B
fields.  It also forged bibliographic metadata, boundary prose, and even
replaced a canonical nonclaim by an affirmative target Euler/root-number
claim while retaining false scope flags.  The released checkers use recursive
exact-type/value trees for these contracts; named repaired-hash mutations
prove that every observed escape is rejected.  C294's independent word lane
was also extended through the full tenth row rather than trusting the final
producer entry.

## Five theorem-scale advances

### HCS-C294 -- equilateral three-disk no-eclipse billiard

For three equal disks with `r>0` and `d>4r/sqrt(3)`, compact convex
minimization produces the unique polygon for every reduced cyclic code.
No-eclipse forces boundary contact; strict convexity gives uniqueness; the
first variation gives non-grazing specular reflection; positive
determinant-one optical blocks give hyperbolicity.  Primitive code classes
are therefore in bijection with primitive oriented geometric rays, and word
powers record traversal multiplicity.  The paper also proves the exact
fixed/primitive/reversal ledger, uniform length bounds and the source-local
collision zeta `1/((1-2z)(1+z)^2)` at every period.

Route-A verdict:
`(A0_FAIL,A1_PASS_ANALYTIC,A2_FAIL,A3_FAIL,A4_NATURAL_QUANTIZATION)`,
`ROUTE_A_REJECTED`.

### HCS-C295 -- Hénon isochrone action and closure atlas

For `V(r)=-mu/(b+sqrt(b^2+r^2))`, the bound chamber is exactly
`E_c(ell)<=E<0`, and
`J_r=mu/sqrt(-2E)-(ell+sqrt(ell^2+4mu*b))/2`.  The paper derives the
action Hamiltonian, energy-only radial period, exact apsidal ratio and the
if-and-only-if rational closure/least-return law for noncircular motions.
Circular orbits, signed angular momentum, smooth center crossings, escape and
the noncommuting Kepler/collision boundary are treated separately.

Route-A verdict:
`(A0_FAIL,A1_WEAK,A2_FAIL,A3_FAIL,A4_NATURAL_QUANTIZATION)`,
`ROUTE_A_REJECTED`.

### HCS-C296 -- rotation-reduced equal hard rods on a circle

After quotienting labels and common rotation, equal elastic rods are exactly
conjugate to free points on the available circle of length `L=ell-Na`, modulo
permutations and common translation.  This yields a global shape flow through
binary and simultaneous events, conservation and no-Zeno closure, and the
exact return condition
`y_i+T v_i=y_(sigma(i))+c (mod L), v_i=v_(sigma(i))`, including the complete
velocity-stabilizer congruence.  The omitted global rotation is deliberately
not reconstructed without its cocycle.

Route-A verdict:
`(A0_FAIL,A1_WEAK,A2_FAIL,A3_FAIL,A4_NATURAL_QUANTIZATION)`,
`ROUTE_A_REJECTED`.

### HCS-C297 -- PT-symmetric balanced-gain/loss dimer

For `H=[[i gamma,kappa],[kappa,-i gamma]]`, the identity
`H^2=(kappa^2-gamma^2)I` gives the exact unbroken, exceptional and broken
propagators.  The paper closes generic vector and projective least periods,
the rank-one nilpotent exceptional growth, broken attracting/repelling rays,
the global Riccati field, the conserved indefinite form and an explicit
pseudo-Hermitian metric with its sharp signature boundary.

Route-A verdict:
`(A0_FAIL,A1_WEAK,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`,
`ROUTE_A_REJECTED`.

### HCS-C298 -- exact Schubert and Morse--Bott Grassmann flow

For `dot(P)=[P,[P,A]]` with real symmetric `A`, the global solution is the
orthogonal projector onto `exp(tA)Ran(P_0)`.  Exterior powers give exact
Plücker scaling.  With simple spectrum, every Schubert cell has an exact
coordinate-plane limit and actual-support rate, and every exchange mode is
classified.  Repeated eigenvalues yield all product-Grassmann critical
components, associated-graded limits and exact stable/unstable/center
dimensions.  Finally `d Tr(AP)/dt=||[P,A]||_F^2` excludes every nonconstant
recurrent orbit.

Route-A verdict:
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`,
`ROUTE_A_REJECTED`.

## Exact release accounting and hashes

The exact totals below were populated only after every repaired hostile gate,
the five closed-world manifests, independent cross-audits, and final
root-level replay passed on the same files.

| ID | audited cells | checker assertions | symbolic checks | hostile rejections | evidence bytes | final pages/fonts |
|---|---:|---:|---:|---:|---:|---:|
| C294 | 226 | 92,280 | 417 | 58/58 | 67,180 | 4 / 21 |
| C295 | 116 | 11,254 | 1,099 | 87/87 | 146,516 | 4 / 22 |
| C296 | 149 | 2,685 | 159,064 | 96/96 | 38,783 | 4 / 18 |
| C297 | 176 | 6,475 | 516 | 52/52 | 85,343 | 3 / 22 |
| C298 | 189 | 2,717 | 534 | 116/116 | 74,655 | 4 / 23 |
| **total** | **856** | **115,411** | **161,630** | **409/409** | **412,477** | **19 / 106** |

| ID | evidence SHA-256 | round 0 PDF SHA-256 | round 1 PDF SHA-256 | round 2 / final PDF SHA-256 | manifest SHA-256 |
|---|---|---|---|---|---|
| C294 | `85e1fa131ba318099c20b1edc97b577f6f1356a882065a874b95034cb032f1f9` | `b3ca978ef07c70e038fac52d960970b9e1e728038295082a963b9c0cd4490965` | `e94f2d1c50fb73ec9292e33dbcaaf7ffaa88f9a9dba04db89850965cb4430921` | `a8d7f4c1a0aa4b2bca95435348e6305c942cf226f3201157d8a2e0f8105606d8` | `1845d786f41f26ff1410deab42662bd2207acc57dc3c017b6f9cbccda1678b68` |
| C295 | `3eafe6ca64829ce4389efe8d11b89f556f018e67bdd59595e2330e28c702f472` | `959003cf32111953109f9a64875503805f120bf7bdd1310c62269db34a3fcd79` | `d81c873e253e1505f316844fc27ad0cb6cd972e60736fe926d0de4f4c2cb691f` | `e89f5fa8ba9d9b2148f7d15d2b1d48d6767681278ff6c123fd61f2e673b87f3b` | `9e1518ca4326e8f0f8535ddebcab66cd4e1b44a6441d13432ef043bc06d541a5` |
| C296 | `7d12ae96f3e146b25586caa99d4f594be6243ecea2684683dbe8aee5368dc06b` | `8ea2fd6618e41272a03c396a295957f1e02acbbc2a1e7cb3e56fbed96555d15b` | `9cac72b380bdbc9794037a113f1dd1b05629b9e6c9b00e1e8ac16308de56270f` | `dc8890acabb563e3de21572381e479c8ac7ea2a23e6e4077aab4f8bffa6589f9` | `9e7c6cacd3f040d088820babfc8a6227ab4893c542c2ea1f136b30828671f47d` |
| C297 | `5d3bba21dd63e89f0183427a111b663f20ef6da5fb65e2ffdf186c137e42273a` | `e10307506e636527f3296fda541e627b6c17b704c059eb3c2845054beb87ccb2` | `3208737429a4d28a18f399d038271a4b74ea2b7b9851887c627033dade1c337d` | `a6122768fabaa99cfa3ab62ef28384a5360103c029ce4393fe94f16d4537fc82` | `5c2a8fa7078f55fa326a2912249aaa92f42a80aa2df29e8af90c884656a07331` |
| C298 | `0519b0fd34b0ae5c41e2e92be6970d677229c1571c05552faba8fdf0667d3134` | `0d8d6e35da94f740b9246155b3adaf44b2769700dd352c89f8bc8f6b32b388db` | `b33a6ebe333284632d72bd20ccaec7f065f32d4c7a40dfa164d632147449dde7` | `37c2512b70f1042b18b3fc89282fa58f82d65897e9e4c6aab6f8199957477295` | `33fd0f55de487d301700c96ab4aa2b714161fd497c2e5e4bc8dbccae95d937a3` |

Every row has three distinct retained revision hashes and a final PDF equal
to Round 2.  The five manifests cover 135 content-addressed payloads and 140
physical package files.  Every settled build log is free of layout,
citation, reference, destination, missing-character and rerun warnings; all
106 final font rows are embedded and subset, and all 19 final pages were
visually inspected.

## Citation, proof, and scope integrity

The papers assign the classical dispersing-billiard, isochrone,
equal-hard-rod, PT-symmetric and Grassmann/double-bracket neighborhoods to
named literature owners.  Repository packaging is never used as evidence of
literature priority.  Every headline theorem is proved analytically; finite
tables are regression and convention evidence only.

All five evaluations set `route_b_invocation_allowed: false`.  No target
arithmetic local datum, Euler factor, bad-prime datum, root number, automorphy
object, target divisor/counting law or functional equation, target zero
match, Hilbert--Pólya operator, or Route-B input is asserted.
