# Papers 24--28 — Round-7 execution report

Date: **2026-08-28**

Batch: **one round / exactly five paper projects**

ARS state: **Stage 1 RESEARCH in progress for all five**

Proposal state: **Route A, primarily A0--A1; P25 remains an exact A1--A2
negative-control calibrator**

## Outcome

Round 7 gives every paper one explicit, paper-facing advance.  The strongest
positive movement is not a Route transition: P24 obtains a new exact
arithmetic invariant, P26 closes all four previously unresolved finite
survivors, and P28 replaces a `0/6` placeholder by a real `6/6` source-verified
non-arithmetic control.  The strongest negative movement is equally useful:
P24 proves that its new invariant is not an injective owner, P25 proves its
symbolic determinant mechanism for every alphabet size, and P27 proves that
every fixed finite Euler prefix escapes along a residual tower.

```text
PAPERS_WITH_EXPLICIT_ROUND7_ADVANCE=5/5
FORMAL_TYPED_ROUTE_A_RECORDS=5/5
PRIMARY_ARITHMETIC_CANDIDATES_REACHING_A2=0/5
NEGATIVE_CONTROL_WITH_EXACT_A2=1/5
ROUTE_A_EXPLORATORY=3/5
ROUTE_A_REJECTED=2/5
MANDATORY_A0_CONTROL_GATES_COMPLETE=0/2  # P24 and P28 remain explicit blockers
ROUTE_B_INVOCATIONS=0/5
ARS_STAGE2_MANUSCRIPTS_AUTHORIZED=0/5
TARGET_PRIME_OR_ZERO_TABLES_USED=0/5
FULL_HISTORICAL_TESTS=292/292
ROUND7_REPLAY_TESTS=71/71
DETERMINISTIC_ROUND7_REPRODUCERS=5/5
```

The formal tuples remain conservative.  No proxy verdict is transferred to a
full physical flow, and no exact finite theorem is renamed a global dynamical
determinant.

## Five paper-level advances

| Paper | Round-7 result | Formal Route-A state | Paper consequence |
|---|---|---|---|
| P24 Bianchi holonomy | Proved `D9(gamma)=(tr(gamma)^2-4)/9 in Z[i]`, its conjugacy/inversion invariance and exact repetition square-factor law; audited 11,481 matrices and 57,405 power identities | `(A0_WEAK_ARITHMETIC_RELATION,A1_WEAK,A2_FAIL,A3_FAIL,A4_FAIL)`; `ROUTE_A_EXPLORATORY`; full flow `UNASSIGNED` | A genuine source-derived invariant now exists, but an exact same-`D9` pair separated by `((gamma-I)/3) mod 3` up to sign proves that `D9` is not an injective unoriented owner |
| P25 three-disk symbolic calibrator | Extended the exact no-repeat determinant theorem from `q=3` to every integer `q>=2`; replayed `q=2,...,8` through degree 12 with zero mismatches | `(A0_FAIL,A1_PASS_ANALYTIC,A2_ANALYTIC_DETERMINANT,A3_FAIL,A4_FAIL)`; `ROUTE_A_REJECTED`; physical flow `UNASSIGNED` | Exact primitive ownership, Euler product and rational determinant persist throughout a deliberately non-arithmetic family, strengthening the `PROVES_TOO_MUCH` calibration |
| P26 Level-11 time change | Exactly classified all four `p=5` quadratic-moment survivors: two full complex source kernels and two nonzero purely imaginary periods that vanish only after real projection | `(A0_WEAK_ARITHMETIC_RELATION,A1_WEAK,A2_FAIL,A3_FAIL,A4_FAIL)`; `ROUTE_A_EXPLORATORY` | The numerical ambiguity is gone: `2/4` are genuine full kernels, `2/4` are projection artifacts, `0/4` are floating artifacts; no global owner product follows |
| P27 congruence inverse limit | Proved fixed-owner factor/prefix escape: quotient orders and physical periods diverge, so every fixed finite Euler prefix eventually becomes the constant term | `(A0_WEAK_ARITHMETIC_RELATION,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)`; `ROUTE_A_REJECTED` | The same-owner Route-A branch is closed coefficientwise as well as periodically; a collective renormalized limit would be a new owner with a new clock and normalization |
| P28 Bolza magnetic flow | Source-verified one exact non-arithmetic genus-two control at `(a,alpha)=(exp(-1/10),pi/4)`; all six fail-closed requirements pass and four inverse-paired primitive owners are certified | `(A0_WEAK_ARITHMETIC_RELATION,A1_WEAK,A2_FAIL,A3_FAIL,A4_FAIL)` on the bounded proxy; `ROUTE_A_EXPLORATORY`; full candidate `UNASSIGNED` | The missing control geometry is no longer hypothetical.  A common-cutoff census is still forbidden until a control systole/lower bound or finite completeness certificate is proved |

## P24 — exact trace-discriminant theorem and owner obstruction

For `gamma=I+3A` in `SL_2(Z[i])`, determinant one gives

```text
tr(gamma)-2=-9 det(A),
D9(gamma)=(tr(gamma)^2-4)/9 in Z[i].
```

If `S_0=1`, `S_1=t` and `S_n=tS_(n-1)-S_(n-2)`, then

```text
D9(gamma^r)=D9(gamma) S_(r-1)(tr(gamma))^2.
```

The exact ledger contains 1 identity, 504 parabolics and 10,976 loxodromics.
All 57,405 identities for `r=1,...,5` pass.  Only 145 `D9` values occur among
11,481 matrices, but aggregate matrix collisions alone are not used as an
owner proof.  Instead, the exact pair

```text
gamma_1=[[1,3],[3,10]],
gamma_2=[[1,-3i],[3i,10]],
D9(gamma_1)=D9(gamma_2)=13
```

has distinct `A=(gamma-I)/3 mod 3` residues even up to sign.  This residue is
fixed by `Gamma((3))` conjugacy and negated by inversion, so the two matrices
are distinct unoriented owners.  Thus `D9` is proved non-injective on the
relevant owner quotient.

The mandatory Route-A arithmetic-control gate is recorded honestly as `0/3
INCOMPLETE`.  This blocks promotion but is not a defect in the exact theorem.

```text
primary-output SHA-256 = 62aff0238f86ed9d582724a58b24d5cab31959742a2101fde026a043ab8d8024
material SHA-256       = f5981f85f70da6afb97dcb4b4256f7223894b5c1eda6464e41fca2a637d49c72
```

## P25 — universal `q`-symbol determinant family

For `A_q=J_q-I_q`, integer `q>=2`, unit roof and step phase `u in {+1,-1}`,
Round 7 proves

```text
tr(A_q^n)=(q-1)^n+(q-1)(-1)^n,
P_n(q)=(1/n) sum_(d|n) mu(d) tr(A_q^(n/d)),
det(I-u z A_q)=(1-(q-1)u z)(1+u z)^(q-1),
zeta_(q,-1)(z)=zeta_(q,+1)(-z).
```

The Euler product converges absolutely for `|z|<1/(q-1)` and the rational
formula supplies meromorphic continuation.  The exact finite replay contains
84 trace/count rows and 182 coefficient rows for `q=2,...,8`, degree at most
12, with zero mismatches.  The cumulative primitive counts are formula
values—not enumerated row populations—and reach 1,366,778,692 for `q=8`.

The theorem demonstrates that exact A1--A2 wiring is generic across this
non-arithmetic symbolic family.  It therefore calibrates the method but gives
no credit to the physical three-disk flight-length flow.

```text
core SHA-256 = 9c3daaa1feffa23090cc4edf5c3cdf0398389f814ef4f0f6b14cad254f23d4d9
```

## P26 — exact closure of the four survivors

The four Round-6 numerical `p=5` survivors are now classified in exact
homology/modular-symbol coordinates:

```text
LRRLRRR, LLRLLRLR   -> compact homology class 0
                        -> full complex period 0

LLLRLLRLR, LLLRLRLLR -> nonzero anti-invariant compact classes
                         -> nonzero purely imaginary full periods
                         -> real projection 0 only
```

All degree-one real periods equal the base real period exactly.  Since
`a_5^2=1`, every survivor also satisfies the frozen finite quadratic moment
`Q_1=I_R(M)^2`, `Q_5=0`.  The final split is therefore

```text
full source kernels       = 2/4
real-projection-only      = 2/4
floating artifacts        = 0/4
unresolved                = 0/4
```

This closes the four-row ambiguity without turning a local finite equality
into an Euler product or A2 result.

```text
artifact-tree SHA-256 = bdfa8f5baaeef47f1bfd8482e8b459d2bd0606cdbb9cdcf0c441a8f65829d678
```

## P27 — coefficientwise escape of every fixed owner panel

Let `Gamma_n` be a descending normal finite-index residual tower and `g` a
fixed primitive base owner.  Its quotient order `o_n(g)` divides forward and
tends to infinity.  With `x_g=exp(-s ell(g))`,

```text
(1-x_g^o_n(g))^(-1) = 1 mod x_g^(N+1)
```

for every fixed `N` and all sufficiently large `n`.  The statement remains
true for a fixed finite owner panel and for finite lift multiplicities or
scalar weights, because no term can occur below `o_n(g)`.  In physical time,
all corresponding periods leave every bounded window.

The finite replay unifies 24 exact cusped quotient-order rows, 24 cocompact
homology lower-bound rows and 54 owner/degree diagnostic rows.  Cusped base
conjugacy primitivity remains `NOT_ESTABLISHED`, so those factors are explicitly
loop-order diagnostics rather than primitive zeta factors.  The theorem does
not exclude an as-yet undefined collectively renormalized object; that object
would require a new source lock.

```text
core SHA-256 = 551e92315c46dcbb4d01bd84688bb77eca8fcd4a6c2eaec202fe04f621275845
```

## P28 — source-verified non-arithmetic genus-two control

The selected project-local control is

```text
surface_id = NAZARENKO-EXP-OCTAGON-G2
(a,alpha)  = (exp(-1/10),pi/4)
curvature  = -1
genus      = 2
```

The source-only preflight passes all six requirements before any geometry is
loaded.  The final package then instantiates four exact analytic `SU(1,1)`
side pairings, replays determinant, structure and the published relator at 140
decimal digits, and obtains:

```text
named closed genus-two surface                    PASS
explicit torsion-free cocompact Fuchsian matrices PASS
presentation and checked relator                  PASS
primary / peer-reviewed locator                   PASS
independent non-arithmeticity certificate         PASS
per-owner primitivity certificate                 PASS
```

For `x=exp(-1/5)`, exact trace algebra gives

```text
tr(g0)^2=4x/((1-x)(2x-1)).
```

If this were algebraic, the transcendental `x` would solve a nonzero
quadratic over the algebraic numbers.  Hence `tr(g0^2)` is transcendental.
The square subgroup has finite index in the finitely generated surface group;
arithmeticity is stable under commensurability; after Cayley conjugation,
Takeuchi's criterion applied to that subgroup requires an algebraic trace
field.  This proves non-arithmeticity.  The `Z^4` abelianization both excludes
proper powers and separates the four generator classes up to sign, giving four
distinct inverse-paired primitive owners.

No systole, common cutoff, census, magnetic comparison, determinant or A2
result is claimed.  The Route-A mandatory-control gate remains `0/3
INCOMPLETE` until those comparisons can actually be run.

```text
core SHA-256    = f1fbcc162907622e8f521dc08d56032afec7553810a9bbbcf3ba752728540386
artifact tree   = a11917f6e9eab3bc48f1920b9727b0ec96a9c43c1f7ac13ab69984c005cfccef
receipt SHA-256 = 6a6143adfd14b17a167af9a07c983cf22c50f06596d99ab37e64322d4fb05b13
```

## Route-map correspondence

The governing contracts remain `skills/route-a-evaluator.md` and
`skills/route-b-evaluator.md`.

| Paper | A0 position | A1 position | A2 boundary / next gate |
|---|---|---|---|
| P24 | exact Gaussian level-`(3)` relation, but mandatory controls `0/3` and no prime-ideal dictionary | finite exact matrix/invariant ledger; `D9` owner non-injectivity proved | no determinant; execute genuine controls and refine the owner beyond `D9` |
| P25 | fails by non-arithmetic design | exact oriented primitive symbolic owners for every `q>=2` | exact rational determinant belongs only to the unit-roof symbolic family |
| P26 | newform/Hecke provenance remains indirect | finite owner, inverse and repetition fields are exact | four survivors closed, but all 138 cycle owners and a global product theorem remain open |
| P27 | congruence provenance is non-specific under compact control | fails for the inverse-limit owner; periodic set empty | every fixed finite coefficient prefix also escapes; a renormalized limit must be a new candidate |
| P28 | arithmetic Bolza host plus exact non-arithmetic control source, but controls `0/3` under a common cutoff | 36 bounded Bolza owners and four distinct primitive control seeds | no common census or determinant; first prove a control systole/lower bound or finite completeness certificate |

The program is still in **Route A / ARS Stage 1**.  A1 and the negative A2
calibrator are useful foundations, but the positive arithmetic program remains
at the A0--A1 owner/control bottleneck.  Route B is not opened.

## Dynamical-system coverage and initial limitations

The five primary continuous-time subtypes are unchanged:

1. finite-volume cusped hyperbolic three-manifold geodesic flow;
2. open three-disk billiard/scattering flow;
3. smooth real-one-form time changes of an arithmetic surface geodesic flow;
4. residual-tower/inverse-limit geodesic lamination flow; and
5. magnetic Hamiltonian/geodesic flow on a closed hyperbolic surface.

Counting source-locked geometric or physical parameter instances gives **12**:
the 11 reported in Round 6 plus the newly instantiated non-arithmetic genus-two
control geometry.  That new control has not yet undergone a magnetic census.
Separately, P25 now supplies **7** exact unit-roof symbolic suspension controls
for `q=2,...,8`.  Thus the repository contains **19 frozen model instances**
if geometric/physical systems and symbolic analytic calibrators are counted
together; this is not a claim of 19 independent samples.

Round 7 deliberately applies five different subtype transformations while
retaining explicit initial limits:

| Paper | Transformation | Frozen limitation |
|---|---|---|
| P24 | holonomy statistic -> exact level trace-discriminant invariant | elementary-generator word ball `L<=5`, not full `Gamma((3))` |
| P25 | three-symbol calibrator -> universal alphabet-size family | theorem all `q>=2`; executable replay only `q<=8`, degree `<=12` |
| P26 | numerical real-period survivors -> exact compact homology and complex-period classes | four survivors only; next expansion is all 138 cycle-owner instances |
| P27 | period escape -> coefficientwise fixed-Euler-prefix escape | fixed finite owner panels and degrees through 256 in replay; no collective renormalization |
| P28 | arithmetic host -> exact non-arithmetic metric control | four seed owners only; no systole, common cutoff or census |

These are bold but typed hypotheses and transformations: each has an explicit
owner, clock/normalization boundary and falsification condition.

## Reproducibility and review receipt

| Paper | Full historical suite | Round-7 tests | Deterministic result |
|---|---:|---:|---|
| P24 | 57/57 | 12/12 | two isolated builds byte-identical; canonical verify passed |
| P25 | 53/53 | 12/12 | two isolated builds byte-identical; canonical verify passed |
| P26 | 56/56 | 13/13 | two isolated builds byte-identical; canonical verify passed |
| P27 | 46/46 | 12/12 | two isolated builds byte-identical; canonical verify passed |
| P28 | 80/80 | 22/22 | two isolated builds byte-identical; canonical verify passed |
| **Total** | **292/292** | **71/71** | **5/5 reproducible** |

All five Round-7 YAML files parse, use only the Route-A evidence-label closed
set, point to existing artifacts, and retain
`route_b_invocation_allowed: false`.  JSON parsing, shell syntax, receipt
bindings and embedded artifact hashes were checked mechanically.

Independent read-only reviews challenged theorem ownership, owner quotient
semantics, evidence-label vocabulary, mandatory controls, source transcription,
Takeuchi's square-subgroup bridge, abelianized owner distinctness, hash
bindings and route boundaries.  The release candidate incorporates all local
minors; no blocker or major mathematical defect was found.  Human confirmation
of P27's nine external locators remains a separate pre-submission gate.

## Next smallest lawful artifacts

1. **P24:** execute three genuine `D9` arithmetic controls and seek a
   source-derived refinement that separates the proved owner collision.  Do
   not return to the stopped marking-sensitive phase statistic.
2. **P25:** preserve the universal theorem as the methods/negative-control
   paper.  A physical billiard determinant must start under a new owner, roof
   and source lock rather than extending the symbolic credit.
3. **P26:** run the exact classifier over all 138 cycle-owner instances / 55
   grouped cases and state the resulting kernel taxonomy as a theorem.  Do not
   call it A2 without a complete owner product.
4. **P27:** either complete the short comparative ownership paper after human
   source confirmation, or freeze a genuinely new collectively renormalized
   candidate with its own clock and normalization.  Same-owner rescue is
   closed.
5. **P28:** prove a rigorous control systole/lower bound or finite
   word-to-length completeness certificate; only then predeclare a common
   geometric cutoff and run the target-blind Bolza/control magnetic census.

## Disclosure

The round used AI-assisted theorem organization, exact-code construction,
source-matrix preparation, adversarial review and documentation integration.
All mathematical claims are bounded by checked local artifacts and cited
sources; numerical replays are not presented as substitutes for analytic
proofs, and no target prime/zero table was used to define or tune a candidate.
