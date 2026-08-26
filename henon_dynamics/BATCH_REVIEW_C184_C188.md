# Batch review: HCS-C184--HCS-C188

Date: 2026-08-26

Source commit: `908a6818caedb0c46195a591873a2ac9c685b55e`.

Evaluator authority: `flow_systems/skills/route-a-evaluator.md` version 0.2.0, SHA-256 `6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`.

Common scope: `NO_BAD_EULER_OR_ROOT_NUMBER`.

Recommendation: **retain all five independent all-parameter source theorems
and their exact stopping results; keep C184--C188 rejected by Route A because
every paper fails A0; leave Route B unauthorized.**

## Completed paper outputs

### C184 -- Sierpiński-gasket spectral decimation

For the unnormalized Dirichlet graph Laplacian on every finite pre-gasket,
C184 closes the complete 2-, 5-, and 6-series genealogy under

\[
R(t)=t(5-t).
\]

The exceptional continuation is explicit: a 6-series born at the terminal
level stays at 6, while a continued 6-series is forced through `6 -> 3`
before ordinary two-branch inverse decimation resumes.  The birth
multiplicities are

\[
a_j=\frac{3^{j-1}+3}{2},\qquad
b_j=\frac{3^j-3}{2},
\]

and their weighted lineage sum is exactly
\(N_m=(3^{m+1}-3)/2\).  This gives a monic characteristic recurrence and the
closed determinant

\[
\det L_m=
2^{(3^m-1)/2}
3^{(3^{m+1}-6m-3)/4}
5^{(3^m+6m-1)/4}.
\]

The same ledger closes the finite heat trace and finite spectral zeta,
including \(H_m(0)=\zeta_m(0)=N_m\),
\(-H'_m(0)=4N_m\), and
\(\exp[-\zeta'_m(0)]=\det L_m\).  These are exact finite spectral results,
not an infinite-gasket regularized determinant.  A refinement word moves
between different graphs and Hilbert spaces, so it is not physical time on
one frozen autonomous system.

### C185 -- Brockett double-bracket sorting flow

For every real symmetric isospectral orbit with simple spectrum and every
strictly ordered diagonal target \(N\), C185 proves the all-dimension theorem

\[
\dot H=[H,[H,N]],\qquad
\frac{d}{dt}\operatorname{Tr}(HN)=\lVert[H,N]\rVert_F^2.
\]

The flow is globally defined and isospectral.  Its equilibria are exactly the
\(n!\) permutation diagonals.  At a permutation \(\pi\), every pair mode has
rate

\[
\rho_{ij}(\pi)=
(\lambda_{\pi(i)}-\lambda_{\pi(j)})(\nu_j-\nu_i),
\]

so the unstable dimension for the ascent flow, equivalently the Morse index
of \(-\operatorname{Tr}(HN)\), is the inversion number of \(\pi\).  Every
trajectory converges to one equilibrium; outside the finite union of
lower-dimensional stable manifolds it converges to the increasing alignment.
Strict Lyapunov growth excludes every nonconstant recurrent or periodic
trajectory.  Repeated source eigenvalues produce stabilizer directions rather
than false tangent zero modes, while repeated target entries produce genuine
Morse--Bott equilibrium families.

### C186 -- triaxial Euler-top elliptic action--angle atlas

For every \(I_1<I_2<I_3\), every \(G>0\), and the full energy interval, C186
gives two exact Jacobi charts, two components per regular energy, all six
axial equilibria, four intermediate-axis heteroclinic branches, stable
endpoint periods, separatrix divergence, and two KKS cap actions.  With
\(a=I_1^{-1}>b=I_2^{-1}>c=I_3^{-1}\), the regular periods are

\[
T_3(e)=\frac{4K(k)}{G\sqrt{(b-c)(a-e)}}
\quad(c<e<b),
\]

\[
T_1(e)=\frac{4K(k)}{G\sqrt{(a-b)(e-c)}}
\quad(b<e<a),
\]

with the regime-specific moduli recorded in the paper.  A hostile convention
audit froze

\[
\{F,H\}=-M\cdot(\nabla F\times\nabla H),
\qquad \dot F=\{F,H\},
\]

and repaired the action charts to use the canonical cap momenta
\(P_3=G-M_3\) and \(P_1=G-M_1\), each with bracket \(+1\) with its angle.

For a sampled time map, a regular component is fixed pointwise exactly when
\(n\tau=qT(e)\).  The period is continuous and diverges at the separatrix, so
every sampling time has fixed circles at all sufficiently large iterates.
Thus the full-sphere finite isolated-cardinality Artin--Mazur series is not
available.  KKS area still gives a canonical unitary Koopman direct integral;
that positive A4 coordinate does not repair A0--A3.

### C187 -- rectangular tableau-promotion cyclic sieving

For every rectangle \(a\times b\), \(N=ab\), and every iterate, C187 applies
the source-locked unshifted q-hook CSP

\[
F_{a,b}(q)=\frac{[N]_q!}{\prod_{c\in b^a}[h(c)]_q},
\qquad
\#\operatorname{Fix}(j^d)=F_{a,b}(\omega_N^d).
\]

Since \(j^N=1\), every actual period divides \(N\).  Möbius inversion gives

\[
P_\ell=\sum_{d\mid\ell}\mu(\ell/d)
\#\operatorname{Fix}(j^d),
\qquad C_\ell=P_\ell/\ell,
\]

and hence

\[
\zeta_j(z)=\prod_{\ell\mid N}(1-z^\ell)^{-C_\ell},
\qquad
\det(I-zU)=\zeta_j(z)^{-1}.
\]

Every \(N\)-th root receives the exact spectral multiplicity
\(\sum_{\ell\mid N,\,N\mid k\ell}C_\ell\), and evacuation is an involutive
reversor.  One-row and one-column rectangles are identity boundaries, while
the `2 x 2` action has order two rather than four; the paper therefore never
upgrades `order divides N` to a false uniform exact-order claim.

### C188 -- irreducible rational max-plus cyclicity

For every irreducible rational max-plus matrix \(A\), let \(\lambda\) be the
maximum cycle mean, \(B=A-\lambda\), and let \(\gamma\) be the lcm of the
cyclicities of the critical SCCs.  The source-locked cyclicity theorem gives
the exact least ultimate matrix-power period

\[
B^{t+\gamma}=B^t\qquad(t\ge T),
\]

with no smaller positive ultimate matrix period.  One equality propagates by
right multiplication, so the least transient is exactly

\[
T(A)=\min\{t\ge0:B^{t+\gamma}=B^t\}.
\]

The ultimate CSR theorem supplies \(B^t=CS^tR\) after a matrix-dependent
transient.  Every raw or projective vector orbit has ultimate period dividing
\(\gamma\), possibly strictly, and divisor-indexed attraction cones give its
exact period stratum.  The normalized eigencone lies in the period-one cone;
the ultimate column spans form a \(\gamma\)-periodic family.

The primitive boundary is sharp.  For

\[
B_m=\begin{pmatrix}0&-m\\0&-1\end{pmatrix},
\qquad
B_m^t=\begin{pmatrix}0&-m\\0&\max(-t,-m)\end{pmatrix},
\]

the critical cyclicity is one but the least transient is exactly \(m\).
Thus even fixed dimension and fixed support admit no weight-independent
transient bound.  Reducible matrices can have several growth rates and CSR
terms, so the single-growth theorem is not extended across that boundary.

## Strict Route-A record

| paper | A0 | A1 | A2 | A3 | A4 | overall |
|---|---|---|---|---|---|---|
| C184 | `A0_FAIL` | `A1_FAIL` | `A2_FAIL` | `A3_PARTIAL_ANALYTIC_STRUCTURE` | `A4_FORMAL_HINT` | `ROUTE_A_REJECTED` |
| C185 | `A0_FAIL` | `A1_FAIL` | `A2_FAIL` | `A3_FAIL` | `A4_FORMAL_HINT` | `ROUTE_A_REJECTED` |
| C186 | `A0_FAIL` | `A1_WEAK` | `A2_FAIL` | `A3_FAIL` | `A4_NATURAL_QUANTIZATION` | `ROUTE_A_REJECTED` |
| C187 | `A0_FAIL` | `A1_WEAK` | `A2_FAIL` | `A3_FAIL` | `A4_NATURAL_QUANTIZATION` | `ROUTE_A_REJECTED` |
| C188 | `A0_FAIL` | `A1_WEAK` | `A2_FAIL` | `A3_FAIL` | `A4_FAIL` | `ROUTE_A_REJECTED` |

Every `route_b_invocation_allowed` value is false.  No paper borrows another
paper's positive spectral, orbit, or operator coordinate to repair its own
failed A0 gate.

## Uniform release audit

| paper | checker assertions | SymPy checks | hostile rejections | payload closure | PDF pages |
|---|---:|---:|---:|---:|---:|
| C184 | 3,041 | 33,177 | 71/71 | 27/27 | 2 |
| C185 | 183,158 | 253,765 | 68/68 | 27/27 | 2 |
| C186 | 4,268 | 25 | 21/21 | 27/27 | 2 |
| C187 | 230,034 | 3,065 | 108/108 | 27/27 | 2 |
| C188 | 7,924 | 10,615 | 138/138 | 27/27 | 3 |
| **total** | **428,425** | **300,647** | **406/406** | **135/135** | **11** |

The hostile total consists of 401 repaired-hash semantic attacks and five
separate stale-hash attacks.  Canonical replay closes 13,761,492 evidence
bytes.  Every package contains exactly 27 content-addressed payloads and one
self-excluded manifest.  Checkers do not import producer implementations;
separate symbolic paths reconstruct headline identities; finite censuses are
regression oracles and never proofs of all-parameter source theorems.

All five manuscripts preserve three pairwise-distinct drafting rounds with
`main.pdf == main_round2.pdf`.  Fixed-epoch fresh-directory builds reproduce
each final byte for byte, listed fonts are embedded and subsetted, final logs
are clean, and all eleven rendered pages have been inspected.  Classical
citations are source locks, not external reviews or novelty certifications.

## Content-addressed release ledger

| paper | evidence SHA-256 | PDF SHA-256 | manifest SHA-256 |
|---|---|---|---|
| C184 | `9955cf03d3acd4c240569d0138348f78f58c69ebddb517b6b588d3dd74fd7bb9` | `3ae96a32319b2af57b72b73ab3085cfbe38c88b24f5fc0a831107ed44274230d` | `7b6a90cd55fa6a527b8fad02fc2d5396f852d8fe001c2bf384162bcf5531b0eb` |
| C185 | `9a273ac5bb3d55b02e680ebe6ee801ada1390a5404ee8230cd754b90a104ec50` | `94fd82d3077217c35edd8d92f035e91425206af838c8881dca76596bd6f38497` | `76967d6416471578e8d55baecb010dc9e14e944f6302646013e6d28ddadc2ac8` |
| C186 | `5c2c37d589be99b1780ca9cbbcd13f8bed17acbeb3e2e62c2f357229ce9940f2` | `43565cd22e891ca2d89aff7791b536a8acb8adc64b319b3ca290b5daaf140d20` | `041ae47767e36b1df9ccc530a47ffc5ba7d2d110008f2337a2c729704ede0eb7` |
| C187 | `7a56357284d543999d3ea7fab794629873743e0c9076ec044c55548239a8a801` | `eace7ed5e6e5d0233eddeda5653ae389c9d8e5df1708c7242fc72aa971e533cc` | `54c015e5b07df76be01045e090aae00a4043d074f33b116adf610a5a3f797998` |
| C188 | `d7fc6d5211b5c716ef2f507ce6ba07646a40653ee2a1bb5bc2ac792c43d21b4e` | `f84601e5cf3b35d2ba2c2774f07fcd1cb8b380b3e5775a846acd91733e8a99f6` | `713e1feee3457f4c22aaf3bf144f35dffa98fd0a65f7c76cd9c00dff825ac6b3` |

## Internal cross-review and repair ledger

These are evidence-anchored internal theorem, scope, and release audits.  They
are not external peer review and do not claim reviewer or error-process
independence.

- **C184:** independent graph reconstruction confirmed the deleted-boundary
  Laplacian convention, the base spectrum, every exceptional birth and forced
  continuation, dimension closure, characteristic sign, determinant
  exponents, and finite heat/zeta identities.  The source theorem remains
  attributed to Fukushima--Shima, and the refinement/physical-time boundary
  is explicit.
- **C185:** hostile sign review confirmed the strict positive Lyapunov
  identity, inversion-mode instability for ascent, the Morse-index convention
  for the negative energy, and the compact LaSalle/stable-manifold convergence
  argument.  Source- and target-spectrum degeneracies are not conflated, and
  no Lax notation is promoted to a fixed unitary clock.
- **C186:** cross-review caught both a Markdown command typo and a genuine
  Poisson-sign inconsistency in the first action-chart draft.  The package now
  freezes the bracket, uses the correct cap momenta, checks four symbolic sign
  identities, and attacks both convention fields after repaired hashes.  All
  evidence, all three PDFs, reports, and the manifest were regenerated.  An
  excluded `__pycache__` file was also removed so the physical 28-file contract
  is literal rather than merely logical.
- **C187:** two independent reviews confirmed that the standard-tableau CSP
  uses the unshifted q-hook quotient in the frozen promotion convention.  They
  also checked order divisibility rather than equality, direct promotion and
  evacuation on 37,401 tableaux, Möbius periods, determinant, traces, and
  spectral multiplicities.
- **C188:** the candidate survived only after the primary source was checked
  for the exact statement that the matrix-power ultimate period equals
  critical cyclicity rather than merely dividing it.  The checker was then
  strengthened after a repaired-hash dimension mutation exposed an unlocked
  field, and the max-times/max-plus logarithmic isomorphism was locked across
  evidence, checker, evaluator record, source audit, and paper.  Matrix and
  point periods, CSR onset, reducible growth, and the unbounded transient
  family remain separate claims.

## ARS Stage 2.5 failure-mode audit

1. **Implementation bug passing self-review: CLEAR.**  Five producer-independent
   checkers, five separate symbolic paths, canonical byte replays, repaired-hash
   mutations, direct small-system reconstructions, and edge controls agree.
2. **Hallucinated citation: CLEAR.**  Every imported classical theorem has a
   primary-source record with exact ownership and convention translation.
3. **Hallucinated result: CLEAR AT PROOF LAYER.**  All-parameter headlines have
   written proofs or accurately delimited source theorems plus proved package
   consequences.  Finite tables remain sentinels.
4. **Shortcut reliance: CLEAR.**  No cutoff establishes an infinite theorem;
   no finite max-plus scan establishes cyclicity, and no finite gasket or
   tableau enumeration replaces the cited all-parameter inputs.
5. **Bug reframed as insight: CLEAR.**  The C186 Poisson sign and C188 unlocked
   field were repaired across dependent artifacts rather than promoted as
   discoveries.
6. **Methodology fabrication: CLEAR.**  Producer, checker, symbolic, replay,
   mutation, build, font, visual, and manifest procedures are executable and
   content-addressed.
7. **Frame-lock: CLEAR.**  Five different owners and their singular boundaries
   were retained; no failed arithmetic gate is repaired by importing another
   paper's spectral or quantization coordinate.

## ARS Stage 4.5 post-manuscript audit

The seven modes were repeated against final PDFs, evaluator YAMLs, evidence
bytes, manifests, and rendered pages.  The clocks remain distinct: graph
refinement, continuous Lyapunov time, rigid-body Hamiltonian time, one
promotion step, and one max-plus multiplication are never merged.  Every
post-draft correction that changed content triggered evidence, PDF, report,
and manifest regeneration as applicable.  All papers retain limitations,
nonclaims, declarations, source ownership, and the common scope literal.

No target zero or prime census, target divisor, target functional equation or
counting law, arithmetic local datum, Euler factor, root number, automorphy
object, Hilbert--Pólya operator, or Route-B input appears as an affirmative
package claim.

## Batch conclusion

The round makes five separate large advances and does not split one theorem
into five installments.  It closes an all-level fractal spectrum, a complete
sorting-flow phase portrait, an all-energy Hamiltonian atlas, an all-rectangle
finite dynamical spectrum, and an all-irreducible max-plus eventual-dynamics
classification.  The strongest honest roadmap conclusion is nevertheless
negative: none of the five exact structures has an intrinsic rational-prime
carrier or logarithmic arithmetic clock.  All five therefore stop at A0
without forcing arithmetic semantics or authorizing Route B.
