# Hénon candidate foundry: idea report

Generation round: HCS-2026-08-05

Status at generation freeze: **twelve ideas generated; no pilot had yet run**.
Post-round update: C02/C02B is retained as analytic infrastructure; C03 and
C05 are stopped as obstructions; no formal Route-A pass was obtained.  See
`refine-logs/EXPERIMENT_RESULTS.md` for the completed tournament.

## 1. Landscape conclusion

The repository already has a strong local \(H_6\) laboratory, but its present
scalar instability-roof determinant does not supply an arithmetic primitive
mechanism, a global analytic completion, or a Hilbert--Pólya operator. The
next search should therefore vary the **kind of structure**, not merely the
cutoff or scalar potential.

The twelve ideas below span four nearly orthogonal axes:

1. arithmetic: finite fields and periodic-point number fields;
2. analytic geometry: projective cocycles, representation-valued transfer
   operators, and complex compactification;
3. symplectic/semiclassical structure: action, Maslov phase, reversibility,
   contact suspension, and scattering;
4. dynamical regimes: chronological parameter cocycles, pruning fronts, and
   parabolic inducing.

The certified pressure/dimension project is not counted as a new idea. It is
registry entry HCS-C00, serving as infrastructure, control, and fallback.

## 2. Ranked promotion queue

This is an information-gain ranking, not a truth or novelty score.

| Rank | ID | Candidate | Why it is high | Main reason it may die |
|---:|---|---|---|---|
| 1 | HCS-C03 | finite-field local zeta/global Euler product | exact, intrinsic arithmetic, cheap | full-space local zeta may be only a trivial finite permutation factor |
| 2 | HCS-C02 | derivative-projective Schottky/holomorphic cocycle | possible A2/A3 analytic bridge derived from Hénon itself | no canonical disjoint complex domains or only post-hoc Möbius generators |
| 3 | HCS-C05 | action--instability--Maslov determinant | closest faithful continuation of Paper 5; catalogue already contains inputs | prior art and phase convention; may reduce to an ordinary weighted zeta |
| 4 | HCS-C01 | chronological two-letter Hénon cocycle | tests genuinely ordered dynamics and reuses neighboring parameters | generic noncommutativity is not arithmetic structure; base may be grafted |
| 5 | HCS-C04 | derivative-representation zeta ladder | exact \(SL_2\)-type identities may expose intrinsic duality | may algebraically collapse to shifted scalar factors |
| 6 | HCS-C07 | parabolic induced zeta at \(a=3\) | exact boundary regime may create nonstandard analytic structure | no controllable inducing scheme or only elliptic-island numerics |

Only three computational pilots are available in round one. The provisional
seats are C03, C02, and C05. C01 is the first replacement if the C02
intrinsicness gate or the C05 novelty gate fails during source lock.

## 3. Desktop Route-A triage

These are **obligations and ceilings**, not formal evaluator verdicts. The
required source locks, determinant conventions, and pilot artifacts do not yet
exist, so all twelve ideas remain pre-evaluation.

| ID | A1 primitive layer | A2 determinant layer | A3 global analytic layer | A4 natural lift |
|---|---|---|---|---|
| C01 | extended primitive cycles need a common hyperbolic theorem | ordered cocycle determinant open | random/non-autonomous continuation is a known danger | autonomous skew product is natural; operator lift open |
| C02 | inherits real orbit ledger if projective products are exact | possible holomorphic/nuclear determinant | strongest continuation opportunity, conditional on canonical domains | hyperbolic-surface/scattering lift is not automatic |
| C03 | exact finite-field cycles, but prime-like mechanism not shown | each local rational factor exact; global object missing | normalization, continuation and functional structure missing | no natural HP operator identified |
| C04 | inherited cycles with exact monodromy characters | bundle determinant theorem missing | symplectic duality may be only algebraic | bundle/operator lift is natural but unspecified |
| C05 | strongest inherited orbit readiness | only a frozen finite phase-bearing determinant is planned | no functional equation or counting mechanism yet | exact generating-function quantization gives a natural hint |
| C06 | global primitive completeness is the central gap | chamberwise determinant only after completeness | pruning may create singularities; theorem absent | symplectic map remains natural |
| C07 | induced primitive coding absent | countable-state determinant absent | possible branch structure is only a hypothesis | formal symplectic hint only |
| C08 | reuses inherited periodic sums | determinant unchanged unless realization adds a theorem | no arithmetic/global divisor mechanism | main purpose is to test A4 |
| C09 | inherited classical cycles | canonical resonance/scattering determinant missing | cutoff-independent continuation/counting missing | natural quantization exists; self-adjoint HP path does not |
| C10 | exact complex fixed-point counts possible | Lefschetz factor likely rational/known | useful mainly as an A3 obstruction | no Route-B path |
| C11 | closed graph paths are easy but presentation-dependent | finite graph determinants are exact | canonical inverse-limit analytic structure missing | self-adjoint finite graphs do not imply a canonical limit |
| C12 | intrinsic algebraic periodic points possible | Artin-like repetition law missing | global Euler product and continuation missing | no natural quantum lift |

For the certified baseline C00, the RH-relevant ceiling before any new
determinant theorem is approximately

\[
(\mathrm{A1\_WEAK},\mathrm{A2\_FAIL},\mathrm{A3\_FAIL},
\mathrm{A4\_FORMAL\_HINT}).
\]

This does not measure its quality as a dynamical-systems paper. It records that
a certified non-arithmetic pressure/dimension root is not itself a Riemann
dynamical determinant.

## 4. Candidate cards

### HCS-C01 -- genuinely chronological two-letter Hénon cocycle

Define the autonomous skew product

\[
F(\omega,z)=\bigl(\sigma\omega,H_{a_{\omega_0}}z\bigr),
\qquad a_-=5.9,\quad a_+=6.1,
\]

on a frozen mixing symbolic base. A period-\(n\) base word uses the ordered
fibre return

\[
H_{a_{\omega_{n-1}}}\circ\cdots\circ H_{a_{\omega_0}},
\]

never a frequency-weighted average of \(H_{a_-}\) and \(H_{a_+}\), nor an
averaged transfer matrix.

- Distinctness: extended base--fibre primitive cycles are not scalar roof
  weights on \(H_6\) and are not Paper 5's fitted schedule.
- Cheapest test: certify common covering/cone conditions for all
  \(a\in[5.9,6.1]\); then enumerate base words through length 8 and compare
  non-cyclic words with the same symbol counts.
- Kill condition: no common hyperbolic domain; incomplete primitive ledger; or
  all proposed anomalies disappear against chronology-destroying and random
  cocycle controls. Merely observing noncommutativity is not enough.
- Route-A path: BF2 needs the extended primitive-orbit theorem; A2 needs an
  ordered cocycle determinant; A3 needs more than random-cocycle asymptotics.

### HCS-C02 -- Hénon derivative-projective Schottky strictification

For a tangent slope \(m=\delta p/\delta q\), the \(H_6\) derivative acts as

\[
m\longmapsto\frac{1}{-12q-m}.
\]

Ask whether the certified inverse branches induce a holomorphic projective
cocycle on canonical disjoint complex disks, with distortion decreasing under
cylinder refinement. This is not permission to replace the four-state graph
by an arbitrary Schottky group.

- Distinctness: the Möbius action is derived from the full Hénon derivative
  along true branches and must recover true periodic monodromy.
- Cheapest test: interval/complex-disk images for memory 1--8; strict
  containment, contraction, separation, and distortion-versus-memory bounds.
- Kill condition: domains overlap at every admissible scale; distortion does
  not improve; generators must be fitted after the fact; or closed-word
  products fail to recover monodromy with a proved error.
- Route-A path: a canonical holomorphic IFS could yield a nuclear determinant
  and controlled continuation. A hyperbolic-surface or Laplacian claim needs
  an additional non-grafting theorem and is not automatic.

### HCS-C03 -- finite-field Hénon local zeta and global Euler product

Because \(H_6\) has integer coefficients, it permutes
\(\mathbb F_p^2\). Define exactly

\[
Z_p(u)=\exp\!\left(\sum_{n\ge1}
  \frac{\#\operatorname{Fix}(H_6^n/\mathbb F_p)}{n}u^n\right)
=\prod_{\ell\ge1}(1-u^\ell)^{-c_{\ell,p}},
\]

where \(c_{\ell,p}\) is the number of primitive permutation cycles of length
\(\ell\). The real question is whether a **canonical**, target-blind removal
of forced ambient factors leaves local pieces admitting a controlled global
Euler product.

- Distinctness: primes are intrinsic residue characteristics, not a table
  used to fit Hénon orbit lengths.
- Cheapest test: complete cycle decompositions for \(p\le251\), exact local
  rational functions, random-permutation controls, and predeclared candidate
  normalizations.
- Kill condition: no canonical bulk factor; post-hoc normalization; only the
  universal statistics of a finite permutation; or no common convergence
  half-plane/global object.
- Route-A path: local exactness is not formal A2 for \(\xi\). Promotion needs a
  cross-prime cohomological/trace mechanism and a global analytic object.

### HCS-C04 -- derivative-representation zeta ladder

For natural representations \(\rho=\wedge^j\) or
\(\operatorname{Sym}^k\), study bundle transfer operators

\[
(\mathcal L_{s,\rho}f)(x)
=\sum_{\sigma y=x}e^{-s\tau(y)}
  \rho(DH_{\pi(y)})f(y).
\]

The periodic weights use characters of the complete monodromy, not only
\(|\Lambda_u|\).

- Cheapest test: use the 2,170-cycle catalogue for \(k\le4\) and cutoffs
  \(N\le20\); verify all exterior-power identities exactly before looking for
  nontrivial factorization.
- Kill condition: every factor is a forced shift/product of the existing
  scalar determinant, or growth precludes a natural operator space.
- Route-A path: prove the bundle trace formula first; only an intrinsic
  factorization, duality, nuclearity, or continuation upgrades A2/A3.

### HCS-C05 -- action--instability--Maslov two-variable determinant

Use the exact generating function

\[
S_a(q,Q)=qQ-q+\frac a3q^3
\]

to define the orbit action \(A_\gamma\), while keeping the positive
instability length \(\ell_\gamma=\log|\Lambda_{u,\gamma}|\) as the real clock.
A candidate trace/determinant family is

\[
D(z,s,\vartheta)=\exp\!\left[-\sum_{r\ge1}\sum_\gamma
\frac{z^{r n_\gamma}}r
\frac{\chi_{\gamma,r}
e^{-sr\ell_\gamma+i\vartheta rA_\gamma}}
{|\det(I-M_\gamma^r)|^{1/2}}\right],
\]

where \(\chi_{\gamma,r}\) is derived from a frozen reversor/orientation/Maslov
rule. Absolute values may not erase a signed or complex trace.

- Distinctness: this is a two-variable phase-bearing determinant, not the
  existing scalar instability roof and not a cutoff quantum matrix.
- Cheapest test: exact repetition and reversal identities plus cutoff 8--20
  stability using the existing catalogue; random-phase, shuffled-action,
  constant-roof, and neighboring-parameter controls.
- Kill condition: phase is not canonical; repetition fails; apparent symmetry
  is forced by multiplying conjugate factors; or all effects match random
  phase controls. The known zero-action period-four orbit forbids using action
  itself as a positive roof.
- Route-A path: strongest current A1 readiness and a natural A4 hint, but A3
  is absent until a genuine analytic determinant/functional structure is
  derived. The \(a\simeq1.02\) Paper-5 window is not used until orbit
  completeness and the claimed tangency scale are independently re-audited.

### HCS-C06 -- global pruning-front and tangency-window zeta

Leave the certified local \(H_6\) survivor and determine how the complete real
bounded symbolic language changes across the area-preserving Hénon pruning
front. Paper 5's low-parameter claims and the classical full-horseshoe
threshold are independent hypotheses to audit, not interchangeable anchors.

- Cheapest test: frozen parameter grid around a rigorously motivated pruning
  window; enumerate periods through 10 and seal periods 11--12; extract the
  first forbidden words with interval escape/boundedness checks.
- Kill condition: no completeness certificate, unstable language under cutoff,
  or only reproduction of known horseshoe thresholds.
- Route-A path: a certified chamber atlas can support chamberwise zeta
  comparisons; without completeness it remains exploratory numerics.

### HCS-C07 -- parabolic induced zeta at the exact parameter \(a=3\)

At \(a=3\), the fixed point \((1/3,1/3)\) has derivative trace \(-2\), so
\(H_3^2\) has a parabolic direction. Build a first-return system around this
point and ask whether its return-time tail produces a controlled countable
Markov zeta with nonstandard analytic behavior.

- Cheapest test: several frozen neighborhoods, high-precision return tails,
  and continuation from \(a=3\pm10^{-k}\) for low periods.
- Kill condition: tail exponents are section artifacts; no unique/summable
  inducing scheme; or elliptic islands prevent a controlled return model.
- Route-A path: only a certified inducing scheme gives A1/A2; a theorem on
  branch singularities or continuation would be the A3 contribution.

### HCS-C08 -- contact/Reeb realization of the instability suspension

Ask whether the non-lattice instability suspension of the local Hénon basic
set admits a smooth contact/Reeb realization whose Poincaré return is locally
the exact Hénon map and whose return-time periodic sums are unchanged.

- Cheapest test: solve the exact-symplectic mapping-torus/contact gluing
  equations using the frozen generating function and roof cohomology class.
- Kill condition: contact gluing changes periodic lengths; only an abstract
  Hölder suspension exists; or a free contact form is chosen after seeing a
  spectrum.
- Route-A path: a true realization could strengthen A4. It does not repair
  weak A1--A3 and does not authorize Route B by itself.

### HCS-C09 -- open quantum Hénon dilation/scattering determinant

Starting from a localized contraction \(M_{\hbar,\chi}=\chi U_{6,\hbar}\chi\),
ask whether its defect operators select a canonical minimal unitary dilation
and scattering determinant whose localized fixed-time traces reproduce the
certified periodic-orbit phases.

- Cheapest test: three resolutions and three admissible cutoffs equal to one
  near the survivor; compare resonances, scattering phase, and traces.
- Kill condition: spectral drift exceeds local spacing; dilations for
  admissible cutoffs are inequivalent; or the output only repeats the existing
  localized-trace plan.
- Route-A path: cutoff independence and a specified scattering Hilbert space
  are mandatory. Direct Hénon quantization is prior art and is not the claim.

### HCS-C10 -- complex compactification/Lefschetz-zeta obstruction

Resolve the polynomial Hénon map on a rational surface, separate affine fixed
points from the contribution at infinity, and compare the exact cohomological
Lefschetz zeta with the real local weighted determinant.

- Cheapest test: exact degree growth and complex fixed-point counts through
  period 10, including the infinity ledger.
- Kill condition: the result is only a direct substitution into known
  algebraic-stability theorems with no new obstruction theorem.
- Route-A value: primarily negative--it can prove which rational/cohomological
  factors cannot supply the required analytic divisor.

### HCS-C11 -- cylinder inverse-limit metric quantum graph

At memory \(m\), use admissible \((m-1)\)-words as vertices and \(m\)-words as
directed metric edges with certified roof-envelope lengths. Study whether the
self-adjoint graph Laplacians or Dirac operators have a canonical
\(m\to\infty\) resolvent limit preserving the same periodic clock.

- Cheapest test: \(m=4,\ldots,10\), with Kirchhoff and symmetry-compatible
  boundary conditions as controls; compare low spectrum and trace lengths.
- Kill condition: \(O(1)\) spectral drift; boundary-condition dominance; no
  projective/resolvent consistency; or a graph chosen to fit target zeros.
- Route-A/B path: finite graphs are only a formal A4 hint. B1--B3 require a
  canonical infinite operator, domain, self-adjointness, and spectral type.

### HCS-C12 -- periodic-orbit number fields and Galois-twisted zeta

For each primitive symbolic word \(w\), eliminate its periodic-point equations
to obtain an integer polynomial \(P_w\). Study the resulting number field,
discriminant, and Galois action; define an Artin-like twist only if a character
is canonical under dynamical conjugacy and repetition.

- Cheapest test: exact elimination through period 6; factor degrees,
  discriminants, small Galois groups, and random-polynomial controls.
- Kill condition: generic unstructured full symmetric groups; dependence on
  embedding choices; nonmultiplicative repetition; or immediate computational
  blow-up without a theoretical compression.
- Route-A path: an intrinsic Galois cocycle could supply arithmetic A1 and an
  Euler product. No such cocycle is currently known, and Route B is closed.

## 5. Ideas eliminated or merged before pilots

- Plain scalar instability-roof zeta at \(H_6\): already implemented; retained
  as parent/control.
- Pure pressure or Hausdorff dimension: rigorous fallback C00, not an RH
  structure candidate.
- Unit-roof SFT determinant: lattice/vertical-periodicity obstruction.
- Action as the suspension roof: killed by an exact zero-action primitive
  orbit; action survives only as a phase.
- Arbitrary Schottky realization of the four-state graph: post-hoc graft.
- Plain \(H_6\bmod p\) histograms: prior art/trivial finite-permutation risk;
  only a canonical local-to-global object remains in C03.
- Averaged non-autonomous transition matrices: chronology violation.
- Raw Ulam/open finite-volume eigenvalues: repository duplication.
- Direct \(\chi U\chi\) eigenvalues or “quantize Hénon”: prior art and cutoff
  dependence; only the scattering-completion question remains in C09.
- GOE/GUE or COE/CUE statistics alone: a common diagnostic, not a candidate.
- Prime/zero-fitted schedules, weights, scales, phases, or boundary conditions:
  target leakage.

## 6. First-round pilots

### Pilot P1 -- C03 exact arithmetic census

Deliver exact local factors for \(p\le251\), a random-permutation control, and
a written ruling on whether any normalization is canonical **before** a global
product is computed.

### Pilot P2 -- C02 intrinsic projective-domain gate

Deliver interval/complex disk images through memory 8 and either a canonical
contracting domain with a distortion theorem target or the smallest certified
overlap/counterexample. Do not fit a Schottky group.

### Pilot P3 -- C05 phase-bearing orbit determinant

Freeze the Maslov/reversor rule from geometry, verify repetition identities,
and compare three orbit cutoffs with all phase/action controls. Do not inspect
Riemann zeros.

If P2 fails the non-grafting gate or P3 collides with existing trace-formula
literature, replace it with the C01 common-hyperbolicity/chronology pilot.

## 7. Paper-selection rule

No “Paper 6” route is fixed yet. After the pilots:

- a canonical arithmetic local-to-global structure promotes C03;
- a canonical holomorphic projective determinant promotes C02;
- a robust intrinsic phase/duality identity promotes C05;
- a shared failure may instead yield an obstruction paper;
- no surviving RH structure returns the project to C00 as an honestly scoped
  dynamical-systems paper.

This preserves the explorer/search-engine role during discovery and invokes
the theorem-engineering workflow only after one bridge is worth building.
