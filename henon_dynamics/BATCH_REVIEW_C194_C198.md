# Batch review: HCS-C194--HCS-C198

Date: 2026-08-27

Source commit: `c3a5b9bbb3b6d0881f395abe4a01accd322f69cb`.

Evaluator authority: `flow_systems/skills/route-a-evaluator.md` version 0.2.0,
SHA-256 `6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`.

Common scope: `NO_BAD_EULER_OR_ROOT_NUMBER`.

Recommendation: **retain all five independent all-parameter dynamical
theorems and their exact negative boundaries; keep C194--C198 rejected by
Route A and leave Route B unauthorized.**  C194 has a weak intrinsic integer-
arithmetic signal, while C196 has a natural quantization, but neither supplies
the missing rational-prime primitive owner, logarithmic clock, target divisor,
or analytic bridge.

## Completed paper outputs

### C194 -- Holte carries at every width and base

For every `n>=1` and integer base `b>=2`, C194 freezes the actual stochastic
carry process for one column of `n` independent digits.  Holte's coefficient
window gives the full transition matrix, and the mixed-radix construction
proves the all-base semigroup

\[
P_aP_b=P_{ab},\qquad P_b^r=P_{b^r}.
\]

The common base-independent diagonalization closes the simple spectrum
`1,b^{-1},...,b^{-(n-1)}`, the Eulerian stationary law, all power traces,
`det(I-zP_b)`, the characteristic polynomial, and the exact spectral-projector
convergence expansion.  The `n=1` boundary and the Diaconis--Fulman total-
variation bound are explicit.  Prime and composite bases obey the same
theorem.  The base-power semigroup is not a rational-prime primitive-orbit
repetition law and supplies neither a `log p` clock nor arithmetic weights.

### C195 -- periodic viscous Burgers as a positive projective heat flow

For every viscosity `nu>0`, circumference `L>0`, mean `m in R`, and Sobolev
index `s>3/2`, C195 closes the fixed-mean periodic viscous Burgers flow through
the positive projective Cole--Hopf coordinate.  In fixed coordinates the
linear owner is the drift--heat semigroup

\[
e^{t(\nu\partial_x^2-m\partial_x)},
\]

while the Galilean coordinate uses `x-mt` and pure heat flow.  The paper proves
global existence, instantaneous smoothing, the unique constant equilibrium
on each mean leaf, absence of nonconstant equilibria and recurrent or periodic
points, the first-active-Fourier-mode asymptotic with its exact remainder gap,
and the complete equilibrium linearization spectrum.  The finite rational
trigonometric census tests signs and semigroup conventions only; it is not the
infinite-dimensional proof.

### C196 -- repulsive rational Calogero--Moser as a free Hermitian pencil

For every `N>=2`, `g>0`, strictly ordered real initial positions and arbitrary
real momenta, C196 represents the physical solution as the ordered spectrum of

\[
X(t)=Q_0+tL_0,\qquad
(L_0)_{jk}=p_j\delta_{jk}+\frac{ig(1-\delta_{jk})}{q_j-q_k}.
\]

The rank-one commutator `[Q_0,L_0]=ig(J-I)` proves that both the pencil and
`L_0` have simple spectrum.  Hermitian perturbation then closes global
collision avoidance, completeness, the Newton equations with the exact
`2g^2` factor, and all trace integrals.  Ordered eigenvalues and spectral-line
intercepts give a global forward/inverse scattering atlas, both time ends,
incoming/outgoing rank reversal, intercept preservation, and linear relative
escape; hence no bounded nonconstant periodic orbit exists.  Moser Sections
3--4 and the Section-4 note added in proof retain classical ownership.  The
finite inverse sentinel reconstructs positions only; the full phase-space
inverse is analytic.

### C197 -- all-relaxation Douglas--Rachford subspace dynamics

For every pair of finite-dimensional real linear subspaces and every real
relaxation `lambda`, C197 decomposes the relaxed Douglas--Rachford map into the
four intersection spaces and every principal two-plane.  A principal angle
`theta` contributes the exact modulus

\[
\sqrt{1-\lambda(2-\lambda)\sin^2\theta},
\]

with the mismatch factor `|1-lambda|` retained.  The package therefore gives
the exact fixed space, convergence precisely for `0<lambda<2`, the sharp
operator-norm rate, the unique uniform optimum `lambda=1`, the shadow limit,
trace and determinant factors, the `lambda=2` orthogonal-rotation endpoint,
its finite-order rational-angle criterion, and instability outside the closed
window.  This is complete projection geometry, not an arithmetic orbit law.

### C198 -- all-positive-parameter closed SIR phase portrait

For every `beta,gamma>0` and nonnegative closed-population initial state, C198
uses physical scaling to obtain

\[
x'=-xy,\qquad y'=y(x-1),\qquad y+x-\log x=\text{constant}.
\]

The invariant closes positivity, global existence, the threshold and peak,
forward convergence, exact time quadrature, final-size sensitivity, stability
along the infection-free equilibrium line, and absence of nonconstant
recurrence.  For `y_0>0` the physical final state is the lower Lambert branch
`-W_0(-x_0e^{-x_0-y_0})`; the upper branch is the other invariant-curve
intersection.  The infection-free boundary is kept separate: it remains at
its initial equilibrium and may lie on the upper branch.  The paper is a
data-free mathematical theorem, not clinical modeling or medical advice.

## Strict Route-A record

| paper | A0 | A1 | A2 | A3 | A4 | overall |
|---|---|---|---|---|---|---|
| C194 | `A0_WEAK_ARITHMETIC_RELATION` | `A1_FAIL` | `A2_FAIL` | `A3_FAIL` | `A4_FORMAL_HINT` | `ROUTE_A_REJECTED` |
| C195 | `A0_FAIL` | `A1_FAIL` | `A2_FAIL` | `A3_FAIL` | `A4_FORMAL_HINT` | `ROUTE_A_REJECTED` |
| C196 | `A0_FAIL` | `A1_FAIL` | `A2_FAIL` | `A3_FAIL` | `A4_NATURAL_QUANTIZATION` | `ROUTE_A_REJECTED` |
| C197 | `A0_FAIL` | `A1_FAIL` | `A2_FAIL` | `A3_FAIL` | `A4_FORMAL_HINT` | `ROUTE_A_REJECTED` |
| C198 | `A0_FAIL` | `A1_FAIL` | `A2_FAIL` | `A3_FAIL` | `A4_FAIL` | `ROUTE_A_REJECTED` |

Every `route_b_invocation_allowed` value is false.  C194's weak A0 signal is
local to positional integer addition; C196's A4 signal is local to the
positive inverse-square Schrödinger form.  Neither coordinate is transferred
to another paper, and the two signals are not combined into a synthetic pass.

## Uniform executable and release audit

| paper | checker assertions | SymPy checks | hostile rejections | evidence bytes | payload closure | PDF pages |
|---|---:|---:|---:|---:|---:|---:|
| C194 | 24,602 | 14,248 | 160/160 | 537,471 | 27/27 | 2 |
| C195 | 1,490 | 129 | 23/23 | 199,419 | 27/27 | 2 |
| C196 | 2,210 | 1,200 | 136/136 | 123,388 | 27/27 | 3 |
| C197 | 870 | 552 | 13/13 | 47,660 | 27/27 | 2 |
| C198 | 419 | 127 | 13/13 | 31,004 | 27/27 | 2 |
| **total** | **29,591** | **16,256** | **345/345** | **938,942** | **135/135** | **11** |

The hostile total consists of 340 repaired-hash semantic attacks and five
stale-hash attacks.  C196's repaired set includes unknown-key injections at
the top, finite-regression, case, pencil-row, and scattering levels; exact key
sets now reject the schema extension that the first checker version accepted.
All five checkers are producer-independent, all five symbolic programs
reconstruct headline identities separately, and all five evidence files replay
byte for byte.

Finite coverage remains regression: C194 has 72 `(n,b)` cases, 1,836
transition cells and 392 base-semigroup tuples; C195 has 24 positive rational
trigonometric lifts; C196 has 18 systems and 126 pencil rows; C197 has 28
generic principal blocks and 21 composite spaces; C198 has 24 phase cases, 48
Lambert branch values and four physical scalings.  None of those finite counts
is used to discharge an all-parameter quantifier.

Every package contains exactly 27 content-addressed payload files and one
self-excluded manifest, hence exactly 28 physical files.  Across the round
there are 135 payloads, five manifests and 140 physical files.  The three
revision PDFs in each package have pairwise distinct hashes,
`main.pdf == main_round2.pdf`, and two fresh fixed-epoch builds from
`main.tex` alone reproduce every final PDF byte for byte.  All fonts are
embedded and subsetted; final and fresh logs contain no warning, bad box,
undefined reference or missing glyph; text extraction is nonempty and retains
the exact tuple and scope literal.  All 11 final pages were visually inspected.

## Content-addressed release ledger

| paper | semantic payload SHA-256 | evidence SHA-256 | PDF SHA-256 | manifest SHA-256 |
|---|---|---|---|---|
| C194 | `15c02c5b83f6314fef0e3c786f7bdad09feeb1d7a557b7df7bd88db30eb3106f` | `b165dd9ae0b60009db7c9489d969a6910500bb5aec72fea1ec226cf147e43b18` | `9351c9ed695028aa34aa1abc2302c00bfa8c687e03f015c58c6309517b028cc7` | `9ed50fccd25835a85f7a1290ee4001759d94023a19c06ba755f761384021b735` |
| C195 | `aa28a3030ea2332bd6a23e8c0b1585807c0222cbc02a3862ea44a0edf7bbb9f6` | `042f0e30d987c9889dc5a74ed14a27c73531af914e96931108905794e67f9354` | `db9c96e3613114c03e7a91eb0abaa70c8873a53aa99918acc45711638aa15feb` | `0b3264db04aae09b899ecb4a532ae6e8db4bb1df42e750bb5cdadd0fb4dff128` |
| C196 | `6269e5194aa8c5b69bb2d8786efc2ca70935261b10e8e78def7c006ae53e2545` | `58efbb32c8788e901d6e94e6cff27c0f60026a3dc8a4147b04d7613742b617c5` | `efa8b97487763be814a0e3c5b65fe56616a377e3e2aacc7d97e26e611061b008` | `ce324e434f98eb217f08fa29ae00dfbf7e558f5cada500b88fa88cdd642f7006` |
| C197 | `562a3b72ea23f28b760659d011370de28b4acef13255f358f2fba68669e342fe` | `d26e80678baf92fbcb7f4c65951773e1cfe3e5ca528dbdbc34707d31b8ea8d59` | `44977c38ebb09c96a7f796810d20228d55d25a4726d5f069f1283fecc15f897d` | `8f86957a7f8ba5b746de24c887a00aaa6289fa1ca682ee3b3d6e8043d5f4acf3` |
| C198 | `5b6114734a77816d288c4b7b9c7c523d7e280d9324f207bbbc20f1f0ee82e95d` | `9d426881cbf9bb9bc28a5c651dd99ba0d1395130f80b8b87e1e41f8a513a0115` | `6cfd1f076b390cc933801f1259942989676ec9b8eae6a0b47aac7ef0d721a426` | `d572cda90e490449f973fed486c1beb6a8608f301426c2340d9174b1f08db390` |

## Internal cross-review and repair ledger

These are artifact-bound theorem, scope and release audits.  They are not
external peer review, independent error processes, or novelty certificates.

- **C194:** independent inclusion--exclusion and linear algebra confirmed the
  coefficient window, row-action semigroup order, Holte diagonalization,
  Eulerian law and sourced total-variation bound.  Review corrected the
  overbroad phrase “no prime-power repetition” to distinguish the proved
  base-power semigroup from a missing rational-prime primitive-orbit
  repetition law, then rebuilt the evidence and PDF.
- **C195:** independent Laurent, Fourier and symbolic paths retained the
  Galilean sign, projective gauge and physical-clock boundary.  Review repaired
  escaped Markdown backticks and required the exact five-axis tokens and scope
  literal inside the paper, followed by fresh deterministic builds.
- **C196:** mathematical review verified the commutator sign, energy factor,
  Newton force, two scattering ends and global atlas.  It localized Moser's
  zero-shift statement, narrowed the finite inverse claim to position
  reconstruction, removed accidentally embedded patch text, and exposed an
  unknown-key checker vulnerability.  Exact nested schemas and five new
  repaired-hash injections closed the defect; all dependent counts, PDF and
  hashes were regenerated.
- **C197:** independent projector/reflection reconstruction confirmed every
  principal block and mismatch factor.  Review corrected the documented
  engine from XeLaTeX to LuaLaTeX and added the evaluator authority and scope
  literal directly to the evaluation YAML.
- **C198:** a Lambert-free 100-decimal bisection checker recovered both roots
  and preserved the infection-free upper-branch boundary.  Review added the
  evaluator authority and scope literal to the YAML and removed one
  whitespace-only line before re-closing the manifest.

Generated `.pyc`, `.aux`, `.log`, and `.out` sidecars created during the root
reruns were moved out of the packages before manifest closure.  No release
payload or user-authored source was deleted.

## ARS integrity and post-manuscript audit

1. **Implementation bug passing self-review: CLEAR.**  Five independent
   checkers, five symbolic reconstructions, replay, repaired/stale mutations,
   fresh builds and cross-package reruns agree.  The one schema blind spot was
   found, reproduced, repaired and attacked explicitly.
2. **Hallucinated citation: CLEAR.**  Holte/Diaconis--Fulman, Hopf/Cole,
   Calogero/Moser, Douglas--Rachford/Bauschke et al., and
   Kermack--McKendrick/Pakes retain classical ownership with verified source
   locators.  No literature-priority claim is made.
3. **Hallucinated result: CLEAR AT PROOF LAYER.**  Every infinite quantifier is
   supported by a written proof or a delimited classical theorem plus proved
   consequences.  Finite oracles remain convention checks.
4. **Shortcut reliance: CLEAR.**  Small bases, Fourier supports, particle
   counts, principal blocks and SIR sentinels are never promoted to proofs of
   the complete families.
5. **Bug reframed as insight: CLEAR.**  Patch-text contamination, Markdown
   escaping, engine metadata, schema injection, branch wording and arithmetic
   qualification defects were repaired rather than interpreted as results.
6. **Methodology fabrication: CLEAR.**  Producer, checker, symbolic, replay,
   mutation, PDF and manifest procedures are executable and content-addressed.
7. **Frame lock: CLEAR.**  The five phase spaces and clocks remain column
   addition, physical PDE time, Hamiltonian time, one splitting iteration and
   physical epidemic time.  No candidate borrows another's successful axis.

The final PDFs and evaluator records were re-audited after every repair.  No
target zero or prime table, arithmetic local datum, Euler factor, root number,
automorphy object, target divisor/counting law/functional equation,
Hilbert--Pólya operator, or Route-B input appears as an affirmative claim.

## Batch conclusion

This round takes five separate large steps: an all-base stochastic semigroup
with complete spectrum, an all-parameter nonlinear parabolic conjugacy, an
all-particle collision-free scattering atlas, an all-relaxation operator-
splitting classification, and an all-positive-parameter branch-complete phase
portrait.  It does not divide one theorem into five manuscripts.

The roadmap conclusion remains honest and negative.  C194 advances A0 only to
a weak positional-integer relation; C196 advances A4 to a natural
quantization; the missing A0--A3 chain is not repaired in either case.  All
five papers are therefore retained as complete dynamical progress while all
five remain `ROUTE_A_REJECTED`, scope-locked, and Route B false.
