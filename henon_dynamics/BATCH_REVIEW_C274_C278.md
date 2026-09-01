# Batch review: HCS-C274--HCS-C278

## Release basis

This review is extracted from the five final release manifests, their bound
physical artifacts, and the final proof and integrity audits, not from the
earlier idea report.  Every package is `RELEASE_COMPLETE`, is bound to source
commit `418bcec5afb1f9e5905cc6e2ba7f9e099fef2e02`, evaluator v0.2.0 SHA-256
`6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`,
fixed epoch `1788220800` (2026-09-01 00:00:00 UTC), and literal scope
`NO_BAD_EULER_OR_ROOT_NUMBER`.  Each package closes 27 manifest payloads plus
its self-excluded manifest, retains three substantively different PDF rounds,
uses two fresh two-pass builds per round, and makes the final PDF
byte-identical to round 2.

Across the batch, the producer-independent checkers close 10,444 assertions,
the independent symbolic reconstructions close 1,322 checks, and repaired-hash
hostile testing rejects 129/129 semantic changes.  The five canonical evidence
files contain 719,457 bytes.  The final papers total 15 pages and 103
embedded/subset font records.  These are release-accounting totals: the
heterogeneous matrix cells, caustic samples, complete finite maps, spectral
multipliers, and peakon rows are not collapsed into a scientifically
meaningless common observation count.

A read-only audit reran all thirty producer, checker, symbolic, replay,
mutation, and manifest commands in temporary complete copies.  Every copy
remained byte-identical to its release tree after the gates.  The audit also
reconstructed the C274 Hamiltonian flow and resonance faces, all 873,612 C276
maps through `n=7`, the C277 smoothing quantifier, and both C278 chambers and
collision scalings independently.  It found and repaired a C275 classical/
quantum clock mismatch, a C278 fail-open nested-schema checker, and a C274
citation-context gap before the manifests were frozen.  Fresh deterministic
PDF builds, ledger closure, checker independence, source/evaluator/epoch
locks, and the claim firewall then passed without modifying the release trees.

## Five theorem-scale advances

### HCS-C274 -- ideal Penning-trap symplectic atlas

For the frozen canonical six-dimensional Penning Hamiltonian, the paper gives
the exact symplectic flow and the complete radial trichotomy for
`Delta=c^2-2*zeta^2`: bounded oscillation for `Delta>0`, a critical Jordan
face for `Delta=0`, and exponential splitting for `Delta<0`.  In the stable
chamber it derives both radial frequencies, signed mode actions and Krein
signs, and then closes the active-mode rational-resonance criterion, least
period, and every stroboscopic fixed-space dimension, including zero-field,
zero-axial, free, and magnetic-sign boundaries.

Evidence scale: 48 full `6 x 6` flow matrices, 24 mode/action rows, 13 strobe
rows, 7 period rows, 9 boundary rows, and 2,743 explicitly recounted numeric
cells.  The evidence is 180,061 bytes.  The checker closes 3,664 assertions,
SymPy closes 96 identities, and hostile testing rejects 26/26 attacks.  The
final paper has 4 pages and 17 embedded/subset fonts.

The independent audit separately reconstructed the Hamiltonian sign
convention, exact matrix flow, symplectic and energy identities, stability and
Jordan faces, signed actions, and all thirteen strobe dimensions.  The final
manuscript also locates the two Brown--Gabrielse records precisely at the ideal
Hamiltonian normalization and mode terminology; no proof step is outsourced
to them.

Route-A verdict: `ROUTE_A_REJECTED`, Route B disabled,
`(A0_FAIL, A1_WEAK, A2_FAIL, A3_FAIL, A4_NATURAL_QUANTIZATION)`.

### HCS-C275 -- confocal elliptic-billiard Poncelet rigidity

For every `0<f<e<1` in the positive-orientation elliptic-caustic sector, the
paper constructs an explicit Jacobi covering and conjugates the billiard map
to rotation by

`rho(e,f)=F(asin(sqrt((e^2-f^2)/(e^2(1-f^2)))),e)/(2K(e))`.

It proves strict increase in `e`, strict decrease in `f`, all four boundary
paths and their two endpoint values, and the inverse formula
`f=e*cd(2K(e)rho,e)`.  Every reduced rational `rho=p/q` gives an entire
Poncelet circle of common minimal period `q`; the restricted `q`-return is the
identity with tangent derivative one.  Thus the paper closes a full
parameter theorem and simultaneously proves why an ordinary isolated-orbit
product is unavailable on this clean family.

Evidence scale: 32 rotation-formula cells, 192 covering/tangent-chord cells,
117 monotonicity values, 96 endpoint values, 24 inverse-porism cases, 128
polygon vertices, and 24 return-derivative cells, for 613 executable cells.
The evidence is 277,726 bytes.  The checker closes 4,251 assertions, SymPy
closes 208 identities, and hostile testing rejects 24/24 attacks.  The final
paper has 3 pages and 19 embedded/subset fonts.

Release-integrity repair: the initial A4 score treated the standard Dirichlet
Laplacian as sufficient natural quantization.  The final package instead
records its Hilbert space `L^2(Omega_f)`, domain
`H^2(Omega_f) cap H_0^1(Omega_f)`, self-adjoint compact resolvent, and
antiunitary complex-conjugation reversal, but also the decisive mismatch:
its unitary group uses continuous physical time whereas the frozen classical
owner advances by one reflection.  No same-clock quantum return or theorem
retaining fixed-caustic phases and weights was constructed, so A4 is
conservatively `FORMAL_HINT`.

Route-A verdict: `ROUTE_A_REJECTED`, Route B disabled,
`(A0_FAIL, A1_PASS_ANALYTIC, A2_FAIL, A3_FAIL, A4_FORMAL_HINT)`.

### HCS-C276 -- uniform random-mapping functional graphs

For a uniform random function `f:[n]->[n]`, the paper proves the exact joint
count of cyclic vertices and components,
`binom(n,k)c(k,r) k n^(n-k-1)`, including the empty-forest face.  It derives
the cyclic-point law and expected cycle counts, the complete marked
tail/cycle law, and the finite identity in distribution between cyclic
vertices and the first-collision length.  It then proves the Rayleigh limits
and the joint limiting density `exp(-(x+y)^2/2)` for the scaled tail and cycle
lengths.

Evidence scale: complete enumeration of all 873,612 maps for `1<=n<=7`, 84
cycle--component cells, 84 marked cells, 28 cycle-length aggregates, 528
cyclic masses, 560 collision tails, 528 cycle expectations, and 28
high-precision scaling samples.  The evidence is 118,171 bytes.  The checker
closes 821 assertions, SymPy closes 918 identities, and hostile testing
rejects 24/24 attacks.  The final paper has 2 pages and 25 embedded/subset
fonts.

The independent audit re-enumerated all maps with a separate indegree-peeling
and union--find implementation, then reconstructed every finite formula and
asymptotic boundary.  The enumeration is a regression witness; the arbitrary
`n` theorem is supplied by the forest/permutation and collision proofs.

Route-A verdict: `ROUTE_A_REJECTED`, Route B disabled,
`(A0_FAIL, A1_FAIL, A2_FAIL, A3_FAIL, A4_FAIL)`.

### HCS-C277 -- Caputo fractional Dirichlet heat flow

On `L^2(0,pi)`, the paper diagonalizes the Caputo solution family as
`E_beta(-n^2 t^beta)`, proves inverse-stable subordination, positivity, and
contraction, and separates it sharply from a semigroup for `0<beta<1`.
Within the declared nonnegative smoothing domain, for every fixed `t>0`, it
proves `A^theta S_beta(t)` bounded if and only if `theta<=1`; negative powers
remain bounded because `A>=I` but are explicitly outside that domain.  It
also proves the exact Schatten condition `p>1/2`, the operator-norm long-time
resolvent limit, and the singular `beta=1` heat face with all-order smoothing
and exponential decay.

Evidence scale: 192 spectral rows, 96 long-time rows, and 90 smoothing rows,
for 378 declared numeric cells.  The evidence is 108,517 bytes.  The checker
closes 1,157 assertions, SymPy closes 90 identities, and hostile testing
rejects 14/14 attacks.  The final paper has 3 pages and 22 embedded/subset
fonts.

Proof-integrity repair: an earlier formulation left the quantifier on
`theta` broad enough to conflict with bounded negative powers.  The final
theorem freezes `theta>=0` in the sharp iff statement and separately explains
the negative-power face.  The evidence, checker, paper, evaluation, and
manifest all lock this exact contract.

Route-A verdict: `ROUTE_A_REJECTED`, Route B disabled,
`(A0_FAIL, A1_FAIL, A2_FAIL, A3_FAIL, A4_FORMAL_HINT)`.

### HCS-C278 -- signed Camassa--Holm two-peakon atlas

On the ordered two-peakon manifold, the paper derives the distributional ODE,
the conserved momentum and energy, and the scalar reduction
`y_dot^2=D^2(y-1)(y-P^2/D^2)`.  For `p1*p2!=0` it proves exactly two strict
chambers: global same-sign cosh/tanh scattering and an opposite-sign
sinh/coth branch with finite collision, quadratic gap collapse, and
reciprocal amplitude blow-up.  It proves the scattering centre and amplitude
exchange, a uniform single-peak collision profile, the concentrated-energy
ledger, all one-peak/zero/coincident boundaries, and the complete declared
`alpha` continuation from conservative reflection to sticky coalescence.

Evidence scale: 15 same-sign rows, 12 collision rows, 15 `alpha` ledgers, and
4 boundary records, for 42 numeric rows.  The evidence is 34,982 bytes.  The
checker closes 551 assertions, SymPy closes 10 identities, and hostile testing
rejects 41/41 attacks.  The final paper has 3 pages and 20 embedded/subset
fonts.

Proof- and release-integrity repair: the final theorem restricts the two
strict chambers to `p1*p2!=0` and handles equality as a degenerate one-peak
boundary.  Its collision profile now follows from a convergent centre, the
one-Lipschitz kernel estimate, `h=O(s^2)`, and `p=O(s^-1)`.  A later audit
showed that the first checker still accepted repaired-hash changes to the
distributional factor two, scope-key set, proof contract, nested row schemas,
and citation metadata.  The final fail-closed checker locks all of them and
the expanded mutation suite rejects every demonstrated bypass.  The final
bibliography audit also replaced the CH1993 first-page shorthand by the
complete `1661--1664` range and added a repaired-hash venue mutation.

Route-A verdict: `ROUTE_A_REJECTED`, Route B disabled,
`(A0_FAIL, A1_FAIL, A2_FAIL, A3_FAIL, A4_FORMAL_HINT)`.

## Exact release hashes

| ID | evidence SHA-256 | round 0 PDF SHA-256 | round 1 PDF SHA-256 | round 2 / final PDF SHA-256 | manifest SHA-256 |
|---|---|---|---|---|---|
| C274 | `d926343f30716cf64888052c2034055ad352e50e59616dddb9a599d3e5c1ddca` | `ff97af92b8e5eb9c75ac232176f733bddeaf2e3c45c9b5861d970fda67c440c2` | `4624322756d44a9db0a26ef23b2a7c55f797dd62c1dce2deb4a1d979b226fada` | `960afb3c5ec99cbd320a033c72affbc3cde357b0fe4b4cee6c741de773df9d42` | `0bc9f42a3118b398930828b31354fc28b0db9ee954c09794626c5f8292d4a17a` |
| C275 | `b7755f2f7850dbde643baa4e258508b001856415df6681ec8f0c5856087b8f2a` | `67f59b377c1cd7a59e2c803a1db4811a7528e65381601eb7221df9a31c1173af` | `32d6033c240aebdd779d4b49963b48b60084aa732419532bd36324a21eb4e566` | `77b15baa296c7107990f36208099118e7186632a2fc075a3087d74989ec948a1` | `5acb4d07123a62dfd926dd7694ab9b373bd9734118e31f3ebb8f25b6e04ab70b` |
| C276 | `a8bee56f7d757078da0c71836f65097e4cc4ef156b69e59668259213dbbf2ec5` | `4116fb67e5f08c209884164f3e81750fc8bf9b968c7aab508db692d1c846c47d` | `b26f021b96a12a822b637782e1ede34a3f7a3cc776eaa6daaa309fe40a35adcc` | `ff5bee778af4d778c73ffdc1e38b457d64e1babe5050bb16588b72023d035972` | `8302fde14889629ca0b8716eb46da69a0b67da2734b3949df2385bbe40b21477` |
| C277 | `9f8e4df18df866120fb9ebad76a577c80d926dd89cc4a1c9a7a7a80750765643` | `cf3a8fb6ba9fd650836e85f2085f54670fe82c9178cd9a084d7cfe4b8be50b0a` | `b06650e2bff0c629c93c5e020120148279b3ab7038e7852e0a4b5ab20e116180` | `c3efe7030d157fbbe1a7b0a45b2bda73973a8bc5070af9968facef32297fc169` | `4c087c1a8375df3f20a8a877ea9b3dc941a77cb46d5b318af812fb5e5d98013d` |
| C278 | `76685e39ef30234310d1a3f20a9a8dd3dbfcd5e9ac314ed8fda363919f6dbbf9` | `386fe10aff86527b4566678451d87cc4ae92541433408414f8f16870ebc6c62a` | `18ea8214dc9f821093ac5cb156d3c3e32d8704ac0f8a26c36ec031b1cb1f63b4` | `3aef1600dc97bb94cb50922ba7d135950ee9db37295a40268467a474b36faa67` | `591e1a9aafe74043fb50c56daad3ecd755ab47424a89355247f9f0973e7ac6db` |

For every row, the three retained revision hashes are distinct and the final
PDF hash equals the round-2 hash.  The five manifests and their hash-bound
compile reports record deterministic fresh builds, embedded/subset fonts,
settled logs, extractable text, visual inspection, byte replay, semantic
mutation rejection, and manifest closure as `PASS`.  The target-operator/
Route-B gate is explicitly `NOT_CLAIMED`.

## Citation, proof, and reproducibility integrity

The eleven registered references are used only for model or theorem lineage:
the two Brown--Gabrielse Penning-trap papers; Lomelí--Meiss, Kołodziej, and
Chang--Friedberg for confocal Poncelet maps; Harris and Flajolet--Odlyzko for
random mappings; Pollard and Sakamoto--Yamamoto for Mittag--Leffler and
fractional diffusion lineage; and Camassa--Holm plus Grunert--Holden for
peakons and signed continuation context.  Author, title, venue, year, pages,
and DOI were checked against publisher or authoritative records, and every
item is cited at its declared use.  No displayed theorem is outsourced to a
reference.  Workspace ownership is not a literature-priority claim.

For a separate originality control, Pandoc 2.9.2.1 expanded each final-round
conditional in memory and counted the abstract plus recursive `Para`/`Plain`
blocks before the bibliography.  Headers, tables, pure displays, bibliography
material, and blocks with fewer than five visible English prose words were
excluded; `Math`, `Code`, and `RawInline` nodes did not contribute words.
This rule found 78 substantive paragraphs: 22/14/12/16/14 in C274--C278.
The audit sampled 12/8/7/8/9 distinct paragraphs respectively, 44/78 or
56.41 percent overall, with every paper above 50 percent.  Fifty-three quoted
searches of distinctive phrases returned no complete external string match.
This is a public-Web heuristic collision screen, not a plagiarism detector,
an iThenticate/Turnitin certificate, or a literature-priority proof;
unindexed and paywalled text, poor OCR, translations, formulas, and
paraphrases can escape exact-phrase search.

The final integrity audit explicitly considered the seven recurrent
AI-research failure modes:

1. **Implementation bug -- clear.**  Every evidence producer has a
   producer-independent semantic checker, symbolic reconstruction, fresh-path
   byte replay, and repaired-hash mutation tests.  The C278 fail-open cases
   were demonstrated and repaired before release.
2. **Citation hallucination -- clear.**  All eleven records passed existence,
   metadata, context, and ghost-citation checks; the C274 context locator was
   added before final closure.
3. **Hallucinated result -- clear.**  Every finite count and hash is bound into
   canonical evidence and a 27-payload manifest; arbitrary-parameter,
   arbitrary-`n`, and operator theorems are supported by written proofs rather
   than extrapolated grids.
4. **Shortcut or hidden singularity -- clear.**  Jordan and zero-frequency
   trap faces, all four billiard endpoints, empty forests and marked-orbit
   boundaries, negative smoothing powers and `beta=1`, and the
   `p1*p2=0`/collision faces are explicit.
5. **Bug reframed as insight -- clear.**  The C275 A4 downgrade, C277 quantifier
   repair, and C278 chamber/profile/checker repairs were completed before the
   narrative, evaluations, and manifests were frozen.
6. **Methodology fabrication -- clear.**  Assertion, symbolic, mutation,
   evidence-byte, page, font, file, and hash totals agree with executable
   receipts and physical artifacts.
7. **Frame lock -- clear.**  Collision screening rejected near-duplicate
   shuffle, rowmotion, Bernoulli--Laplace, OU, and overbroad billiard/PDE
   proposals and retained five different state spaces, clocks, and proof
   technologies.

Automated search and finite regression cannot certify semantic completeness
by themselves.  They are adversarial controls around the independent
mathematical proof audit, not replacements for it.

## Claim firewall and batch verdict

The firewall is common and literal: `NO_BAD_EULER_OR_ROOT_NUMBER`.  No package
claims a target arithmetic local datum, bad Euler factor, root number,
automorphy statement, target divisor/counting law, target functional equation,
target zero match, or Hilbert--Pólya identification.  In particular:

- C274's resonant tori are clean continuous families, and its natural magnetic
  quantization is candidate-local.
- C275's rational caustic is a full fixed circle; the ambient Dirichlet
  quantum flow has not been connected to the one-reflection owner clock.
- C276's counts and generating functions are random-map ensemble data, not a
  deterministic rational-prime orbit product.
- C277's fractional multipliers, Schatten classes, and resolvent limit are
  source operator facts, not a target divisor or determinant.
- C278's amplitudes, scattering, collision, and declared `alpha` rule form a
  continuous source family, not an isolated rational-prime ledger.

All five candidates are therefore `ROUTE_A_REJECTED`, and Route B remains
disabled.  The round nevertheless advances five independent source theorems:
one complete symplectic chamber/resonance atlas, one full elliptic-caustic
Poncelet rigidity theorem, one finite/asymptotic random-mapping theorem, one
sharp fractional-memory regularity theorem, and one signed peakon
scattering/collision theorem.
