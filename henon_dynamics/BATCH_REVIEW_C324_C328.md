# Batch review: HCS-C324--HCS-C328

## Outcome

This round delivers five independent theorem packages from baseline
`1aba1f6fd0cf81baa7c137a2ce7ce3d097ba63fc`.  Each package contains its own
research question, analytic theorem and proof, producer-independent evidence,
strict Route-A evaluation, hostile audit, three retained manuscript rounds,
final PDF, and content-addressed release manifest.  These are five different
dynamical systems rather than five installments of one result.

The state spaces and proof engines are deliberately separated: a nonlinear
wave-breaking PDE, a randomized constraint-resampling algorithm, an attractive
finite-particle chain, a periodic singular quantum Hamiltonian, and a confined
active-particle PDMP.

## Independent theorem increments

- **C324:** for every nonconstant periodic `C2` datum in the once-integrated
  Hunter--Saxton formulation, an explicit degree-one characteristic
  diffeomorphism on the complete classical interval; exact forward and backward
  lifespans controlled separately by `min u0_x` and `max u0_x`; the entire
  simultaneous breaking-label sets; conserved slope energy; quadratic
  Jacobian collapse; and the universal future slope coefficient `-2`.  Smooth
  asymmetric two-harmonic receipts distinguish the two extrema and directions.
- **C325:** under the asymmetric finite variable-model local-lemma condition,
  a complete resampling-table proof valid for every legal sequential selection
  rule.  The corrected compatibility argument orders retained vertices by
  non-increasing depth and proves the required table-cell order separately for
  every variable, without the false assumption that those vertices form an
  ancestor chain.  The branching sum gives the eventwise and total expectation
  bounds, almost-sure termination, and a bad-event-free output.
- **C326:** the normalized beta-binomial reversible law of the two-site
  symmetric inclusion process; the full simple Hahn spectrum
  `j(j-1+2*alpha)` with positive finite-sum norms; the complete finite-time
  spectral kernel and sharp `L2` decay; and the entire `alpha=0` boundary,
  including endpoint hitting probabilities, all stationary mixtures
  `c delta_0+(1-c) delta_N`, and the symmetric endpoint limit from positive
  attraction.
- **C327:** a closed-form realization of the periodic delta-comb Hamiltonian,
  its determinant-one transfer matrix and exact Floquet discriminant; pure
  absolute continuity and Bloch multiplicities; every repulsive, free, weakly
  attractive and strongly attractive band/gap chamber, including the exact
  `ga=-4` zero threshold; all nonzero-coupling Bragg gaps; a two-term
  high-energy displacement/energy-width expansion; and indexed IDS/DOS
  formulas with the correct per-length normalization.
- **C328:** the velocity-resolved beta stationary law of the harmonically
  confined run-and-tumble process and all joint polynomial moments; the full
  stationary `2 x 2` correlation matrix for nonnegative lag, its transpose
  rule for negative lag, and the `mu=2*lambda` Jordan limit; and every finite
  polynomial-filter characteristic polynomial.  For positive speed, integral
  `2*lambda/mu` resonances are size-two Jordan blocks exactly at odd integers
  and are semisimple at even integers; zero speed removes all such couplings.

The strict tuples, in order, are
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`,
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)`,
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`,
`(A0_FAIL,A1_WEAK,A2_FAIL,A3_FAIL,A4_NATURAL_QUANTIZATION)`, and
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)`.  All five are
`ROUTE_A_REJECTED` and keep Route B locked.

## Exact release accounting and hashes

Finite evidence units remain package-specific because slope profiles,
assignment kernels, Hahn vectors, Bloch cells and PDMP moment filters are not
interchangeable observables.

| ID | finite evidence | checker assertions | symbolic identities | hostile rejections | evidence bytes | final pages/fonts |
|---|---:|---:|---:|---:|---:|---:|
| C324 | 12 harmonic profiles / 6 asymmetric profiles / 270 samples / 2,354 leaves | 3,857 | 1,508 | 60/60 | 201,305 | 2 / 23 |
| C325 | 3 exact instances / 7 events / 112 transition rows / 955 leaves | 177 | 21 | 48/48 | 46,567 | 2 / 17 |
| C326 | 36 parameter rows / 180 states / 180 Hahn vectors / 9 zero-face rows / 3,045 leaves | 3,499 | 492 | 63/63 | 97,814 | 2 / 20 |
| C327 | 216 Bragg rows / 150 transfer rows / 70 IDS-DOS rows / 5,428 leaves | 5,607 | 295 | 55/55 | 341,458 | 4 / 25 |
| C328 | 12 parameter rows / 108 moment rows / 216 spectral cells / 33 resonances / 1,989 leaves | 2,226 | 61 | 66/66 | 101,456 | 3 / 22 |
| **total** | **13,771 audited leaves** | **15,366** | **2,377** | **292/292** | **788,600** | **13 / 107** |

| ID | evidence SHA-256 | round 0 PDF SHA-256 | round 1 PDF SHA-256 | round 2 / final PDF SHA-256 | manifest SHA-256 |
|---|---|---|---|---|---|
| C324 | `d3d623bc71ed7a73111c7f48d42f97819fa0ec416c711c2d3b441121b8a3df2a` | `d333a5bbe99d836bb9349e85164fc1a7f6fd05d6e4636ae5ac52266e0099b011` | `238e999a7d172e8692f24874e8a59c7dea4c8d46377acb652222918dfa0d73e7` | `32884c754fbeba820b40d153ccb59014d4495954ea3ae995b9362005607f5f51` | `a8e674e506195938e26d59305cc340aff5fb552f6bdb55f2a416b81b34907256` |
| C325 | `38b414d572f6e7de49c8f537df7b26a37a34882f4db74f3f541f55bcf667c732` | `3618ae4bf497fbc9984b6e3944ceb2cff917ac6814d97f9a967b0d6e51cc095a` | `175b241f2ed9ed99ccc03b4d5f9705da65dd9b2c1120245d68a25c7af73b7c63` | `06bd73e5829c47efb94e27d9b3ab631395d2a14d6f446cc0bda920d36800b177` | `0376ebd8439320fd078864ce20a5e707913df8aceae179955011aebd74aeda94` |
| C326 | `0604c2955defd2c0dfa91d3cc18ca03ae8823792a635e72ee4266af807e1b5b0` | `e45d015713df0f6c5c2434fc29ffd4f08b5cf2ca9929b9f382b2163bc48662e3` | `e7b33dd6224cf2584e29538fe62a034556a8e08f431c48a1ce72fbce6f7a632c` | `11ff0fec1005f60c858defcec38a8b306073609f710918eeeb0bada2f811aa04` | `64478510ee5eb06b2a3cabc788a0b610d94aef3f7cfd3ac3265e3a689a740c51` |
| C327 | `f784ba21ff52c4cabd438e1321cce892a77fe6d506567128b88f74c85db2878b` | `a403ce74dbf518c00d78b28ae15842ed394c50e89b559c0869310035c9af9d81` | `975a2fadf2038b156ab19ebd3d4e6a05508a6dd2ee00f2c1b307202b05524cde` | `d721bb570785d9af6cf96cede73ed55fb97316ce5a39b77ca57b10ac791a5208` | `616cb8ca4672d89d4bb9591ca2f618bf2b62c8271728bd7183d0231448c68d60` |
| C328 | `5ffc00eeec98bc39d3d98ed28c25e3305088602ab26fed6fa43543ba469c1d71` | `86ead8d2919f01a95daede6a533b2ba925a214a0af5464b1667b32965d7c51a9` | `3f5f9739d63d908759ae1dbd6b03cd59a10e7d2a42a5345d40c5cad2414356c6` | `5cc9b8d33e2813c05d0e812fbef08988b779a27caa8ab29e78d892566c42edfb` | `e9e2cf7172c4e8bc2db81b19e72cf6869c4e8edaea416272202a8151c5af8318` |

Every row has three distinct revision hashes and a final PDF identical to
Round 2.  The five manifests cover 135 payloads and 140 physical package
files.  All 13 final pages were visually inspected; all 107 final font rows are
embedded and subset.  Settled builds contain no layout, citation, reference,
destination, rerun or missing-character warning.  The final five no-write
release programs all pass from the same workspace state.

## Adversarial proof corrections and integrity

Cross-review materially changed four packages before release.  C324 gained an
explicit construction of the characteristic map and corrected source metadata,
and its evidence gained asymmetric profiles that detect a future/past extremum
swap.  C325 replaced an invalid ancestor-chain shortcut by the max-depth
per-variable table-order proof.  C326 normalized its evaluator schema, routed
the Hahn references through DLMF Sections 18.19, 18.20.5 and 18.22(ii), and
closed the full zero-attraction stationary simplex.  C328 restricted its
semigroup correlation formula to nonnegative lag, added every missing mixed
moment, and separated the zero-speed semisimple face.  C327's attractive first
gap, asymptotic coefficients and IDS scaling were independently recomputed; its
hostile parser matrix and extracted-text gates were then strengthened.

Every checker imports no producer code.  JSON parsing rejects duplicate keys
and nonfinite constants.  Evaluation parsing rejects aliases, anchors, merges,
non-string keys, implicit timestamps, unknown fields and type changes, while
field-level semantic checks lock the authority, tuple, evidence statuses,
theorem status, source owners, scope flags and Route-B prohibition.  The hostile
suites repair payload hashes when attacking semantic fields, and every Python
entry point rejects optimized execution.  Two isolated producer runs replay
byte for byte in each package.

## Citation and scope integrity

The source audits assign the wave equation and periodic characteristic
lineage to Hunter--Saxton, Lenells and Yin; constructive resampling to
Moser--Tardos; the inclusion owner and Hahn conventions to the interacting
particle literature and NIST DLMF; the periodic point-interaction framework to
Kronig--Penney, Albeverio et al. and periodic singular-potential Floquet theory;
and the confined active-particle law to the run-and-tumble literature.  No
workspace packaging claim is used as evidence of literature priority.

All five evaluations set `route_b_invocation_allowed: false` under literal
scope `NO_BAD_EULER_OR_ROOT_NUMBER`.  No target arithmetic local datum, Euler
factor, bad-prime datum, root number, automorphy object, target divisor/counting
law or functional equation, target zero match, Hilbert--Polya operator, or
Route-B input is asserted.  C324 and C326 retain only formal source-side
spectral/geometric hints; C327's natural quantization belongs solely to its
declared delta-comb Hamiltonian.
