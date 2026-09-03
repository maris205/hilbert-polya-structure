# Batch review: HCS-C334--HCS-C338

## Outcome

This round delivers five independent theorem packages from baseline
`db2c816b7b6bd450f51f79b91842cb882b0bd773`.  Each package contains a
source-local analytic proof, producer-independent executable evidence, a
strict Route-A evaluation, hostile mutation and parser audits, three retained
manuscript rounds, a deterministic final PDF, and a content-addressed release
manifest.  The five advances use different state spaces and proof mechanisms:
an integrable molecular Hamiltonian, a jump-driven affine Markov process, a
finite-genome mutation--selection flow, a resonant quantum Floquet system, and
an abelian random-stack dynamics.

## Independent theorem increments

- **C334:** the complete classical energy atlas of the Morse Hamiltonian,
  including exact turning points, action, period and action--period identity;
  and, for its natural Friedrichs quantization, every bound energy and
  Laguerre eigenfunction, node count, essential spectrum `[0,infinity)`, and
  the non-`L2` zero-energy threshold.  The full energy/level boundary atlas,
  positive-parameter domain and action normalization are explicit.
- **C335:** the pathwise exponential shot-noise OU flow, its exact transition
  Laplace transform and semigroup law, the unique Gamma invariant measure,
  exact Wasserstein contraction, all stationary moments and cumulants, and
  the stationary covariance.  Every finite polynomial filtration is
  diagonalized with simple eigenvalues `0,-gamma,...,-m gamma`; no complete
  `L2` spectral theorem is claimed.
- **C336:** the exact projectivization of finite Crow--Kimura single-peak
  dynamics and its complete finite-genome spectrum.  Walsh decomposition and
  a symmetric rank-one perturbation retain the mutation levels with the exact
  multiplicities and produce `L+1` simple secular roots with strict
  interlacing; the Perron limit, exact projective gap, and `s=0`, `U=0`,
  double-zero and `L=1` faces are closed.
- **C337:** the whole integer-resonance sheet of the quantum kicked rotor in a
  fixed free-after-kick convention.  Even resonance order gives the exact
  Bessel kernel, characteristic function and ballistic momentum moments;
  odd order gives the half-turn factor and exact period-two antiresonance.
  Operator order, `2*pi`/`4*pi` parity, arbitrary momentum seed and zero-kick
  boundaries are explicit.
- **C338:** deterministic abelian cycle popping whenever one legal terminating
  sequence exists, almost-sure Wilson termination for infinite random stacks,
  the weighted spanning-tree law and matrix-tree normalization, and every
  transfer-current inclusion minor.  The proof and evidence close singleton,
  already-a-tree, parallel-edge, root-change and orientation conventions.

The exact nearest-collision ledgers are C216/C232/C250/C295 for C334,
C229/C233/C265/C328 for C335, C171/C200/C253/C271 for C336,
C110/C143/C148/C178/C224/C318/C323 for C337, and C176/C181 for C338.  In
each case the retained owner changes the mechanism, state space or theorem
contract rather than merely changing parameters of the earlier package.

The strict tuples, in order, are
`(A0_FAIL,A1_PASS_ANALYTIC,A2_FAIL,A3_FAIL,A4_NATURAL_QUANTIZATION)`,
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)`,
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`,
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_NATURAL_QUANTIZATION)`, and
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`.  All five are
`ROUTE_A_REJECTED`; Route B remains false.

## Exact release accounting and hashes

Finite evidence units are package-specific regression receipts.  They test
formulas, normalization and implementation conventions but are not finite
extrapolation proofs of the all-parameter theorems.  Four schemas expose an
`audited_leaf_count`, totalling 137,385 scalar leaves; C336 instead exposes
its complete owned row/cell ledger directly.

| ID | finite evidence | checker assertions | symbolic identities | hostile rejections | evidence bytes | final pages/fonts |
|---|---:|---:|---:|---:|---:|---:|
| C334 | 32 bound-count / 128 bound-level / 11 classical / 8 threshold rows / 408 Laguerre cells / 1,446 leaves | 1,749 | 273 | 61/61 | 46,435 | 3 / 13 |
| C335 | 5 parameter / 65 moment / 65 polynomial / 10 semigroup / 60 transition rows / 455 generator cells / 1,311 leaves | 1,600 | 126 | 60/60 | 49,341 | 3 / 11 |
| C336 | 11 boundary / 7 flow / 30 spectral / 28 Walsh rows / 254 flow-coordinate / 195 retained / 225 secular / 396 full-factor cells | 644 | 681 | 70/70 | 112,694 | 3 / 23 |
| C337 | 435 formal / 882 moment / 7 numeric / 120 operator / 396 parity rows / 22,444 leaves | 47,531 | 13,188 | 133/133 | 543,702 | 3 / 21 |
| C338 | 772 simple graphs / 8,136 graph--tree pairs / 55,895 simple events / 24 weighted cases / 846 weighted trees / 7,032 weighted events / 167 stack graphs / 12,754 stack tables / 112,184 leaves | 224,424 | 85 | 142/142 | 1,844,227 | 3 / 8 |
| **total** | **137,385 audited leaves where exposed, plus the C336 owned ledger** | **275,948** | **14,353** | **466/466** | **2,596,399** | **15 / 76** |

| ID | evidence SHA-256 | round 0 PDF SHA-256 | round 1 PDF SHA-256 | round 2 / final PDF SHA-256 | manifest SHA-256 |
|---|---|---|---|---|---|
| C334 | `5bf33042e906ad5a66fe02bcf57a6d68f8448b5b58784b5818799b7c0f1f4ffc` | `8f6b3e8485f3b97d0cd84b3f620546c06312377389c9af18a9fe634c047683fa` | `e7d7de5b27b29fc3ebc56b31e0b65acc2a3aa25c78826b6885734184329c6c7b` | `2a671d242db3ab2beabbc13deecb66cf3229625ccc64f543c29a8a8bbb97654d` | `4e509b5cf1a66031d96cfe6a462dfd3d17d7151d305fab1bd13c525b4c87ea8b` |
| C335 | `2e70a4a4d7ddb0943b8362a2b7396f0e1a64fabb43981e83786a7d9fe432df92` | `65b4a5c6966feda3221e505098cb140c325435907af56669a1647db1407e5781` | `132ff9b25045e43d26fdd10d8c57071f89c539a04ef1cf1cef2e90b5de0711d8` | `326f73bece2f5e4688a96b35e99a78e4617961bf15e4afcbf8f0e6fab7ae74ec` | `a19a37efc11bae5745aa68942043b5dc22db5eca7e69628e76507d3862cda289` |
| C336 | `b4102f835b4fc68165c6fa94f657166d56977b10c86ea9959361d2aa67025f8a` | `a055046d2fb2bbb5940fa3f3b9ecff8423ff09508947f123cc7800b448501a02` | `f5ca1f243db737a0b4b2f86b4fd8dbbd074d5b734e0d3f2b0f27f4324f97e3bc` | `cdde6ab95da987d1c21c816edc734c77d0d81a47ed9011076e75cd92cefd6d1a` | `75c2ba2856c6d308196e70083956a471162bd2754d01c37f532a00e8f0b4af64` |
| C337 | `7395dd85f963d8085027133380044839ddc80c2423603fd49dd1df8154e3ecc8` | `3c95dc08a70b5204b3cca04d7f39a084dc78daed3bce2721db3f97b790d4f47a` | `6ff9954a5b6ae3f8c6178c1e579748f64e27ddc7570c3aeacf65a19225ef87fe` | `c8190d9295bd62c41af9f666bcfe341ee26006e0854631a2639cca4a64663a3d` | `d22d1e338bc12fe08c431e96c0ae43a9089b59370e36e5ef61083a8a54ad1cfe` |
| C338 | `6fe802d7b5a5cbaae6426001309931949ccae872b94ed23825607a9fa7c7f282` | `4da9f036410ec30fd3080ca0907479f540c35e11c60b9721401dbeb334f36867` | `144202417e9c69fbe6d3f80e16c42190aa4aab0357a3d3a8d74cbb29aabc3e13` | `a13711c9f3ccfe29b9e65ae5d4807c805328bdd177c098b839ba633d5946ea69` | `b3d2fe5e9b6b3a12fb7b8e8c473a14fac95fe67ed49e3f0869673ee2fe3c1929` |

Every row has three distinct revision hashes and a final PDF identical to
Round 2.  The five manifests cover 135 payloads and 140 physical package
files.  All 15 final pages were visually inspected; all 76 final font rows
are embedded and subset.  Settled builds contain no layout, citation,
reference, destination, rerun, missing-character or missing-glyph warning.
The five final release programs pass in write mode and in two consecutive
no-write runs with stable hashes.

## Adversarial proof corrections and integrity

Review changed theorem-critical details rather than only prose.  C334 locked
the action normalization and non-`L2` dissociation threshold, then repaired
tab-consumed `\tfrac` and `\quad` source tokens and added a full-directory
control-character gate before rebuilding every PDF.  C336's author-swapped
review independently rechecked retained multiplicities, the rank-one secular
sign and strict interlacing, the location of the top two roots, the exact
projective gap, the double-zero corner and the one-locus formula.  It also
reconciled the final font receipt with the executable `pdffonts` count.  C337
fixed silent comma-in-exponent transcription artifacts in the evolution and
period-two formulas, extended the source gate to reject their recurrence,
and rebuilt all three manuscripts.  C338's independent review checked the
local diamond/strip proof behind abelianity, almost-sure termination, weighted
tree normalization, transfer-current orientation and invariance of principal
minors.  C335's transition transform, Gamma limit, Wasserstein equality and
finite-filtration-only spectral boundary were independently reconstructed.

Every checker imports no producer code.  JSON parsing rejects duplicate keys
and nonfinite constants.  Evaluation parsing locks exact schemas and rejects
aliases, anchors, merges, non-string keys, implicit timestamps, unknown
fields, type changes, authority drift and tuple drift.  Hostile suites repair
evidence hashes before semantic attacks, every Python entry point rejects
optimized execution, and isolated producer runs replay byte for byte.

## Citation and scope integrity

The source audits assign the classical Morse potential to Morse and its exact
quantum solution to the established Morse-oscillator literature; exponential
shot noise to the source stochastic-process literature; the mutation--
selection owner to Crow and Kimura; integer quantum resonance to the kicked-
rotor literature; and cycle popping, weighted spanning trees and transfer
currents to Wilson, Kirchhoff and Burton--Pemantle.  Workspace reconstruction,
packaging and collision screening are not presented as literature priority.

All five evaluations set `route_b_invocation_allowed: false` under literal
scope `NO_BAD_EULER_OR_ROOT_NUMBER`.  No target arithmetic local datum, Euler
factor, bad-prime datum, root number, automorphy object, target
divisor/counting law or functional equation, target zero match,
Hilbert--Polya operator, or Route-B input is asserted.  The molecular levels,
Gamma law, finite-genome secular polynomial, Floquet/Bessel formulas and graph
determinants retain only their explicitly evaluated source-side meanings.
