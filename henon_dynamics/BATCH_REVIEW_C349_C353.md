# Batch review: HCS-C349--HCS-C353

## Outcome

This round delivers five independent theorem packages from frozen baseline
`327fc1172cebcdeb17adfd2d8ad12636fbb94f52`.  Each package contains a
source-local analytic proof, producer-independent exact evidence, a strict
Route-A evaluation, hostile mutation and parser audits, three retained
manuscript rounds, a deterministic final PDF, and a content-addressed release
manifest.  The five owners use genuinely different state spaces and proof
engines: a constrained integrable Hamiltonian, a reaction--diffusion PDE, an
infinite-state open queueing network, a whole-line supersymmetric Dirac
operator, and an exchangeable random partition-growth process.

## Independent theorem increments

- **C349:** the complete declared Neumann-sphere integrability atlas.  The
  constrained flow is globally complete; all Uhlenbeck integrals, their two
  affine relations, Dirac--Poisson involution and rational `2 x 2` Lax
  determinant are explicit.  Connected compact regular fibers are Liouville
  two-tori, with closure exactly when the physical frequency vector has a
  common period.  Axial equilibria, coordinate reductions, double-spectrum
  `SO(2)` faces, the isotropic great-circle limit and the natural compact
  quantization for fixed `hbar>0` are closed separately.
- **C350:** the complete linear finite-domain Schnakenberg Turing atlas.  The
  positive equilibrium, kinetic chamber, complexified modal spectrum and
  continuous Turing window are exact.  Strict integer selection gives every
  unstable Neumann mode and length entry/exit wall, including lower and upper
  endpoint ties, double contact, a window missing the lattice, equal
  diffusion, the homogeneous mode and the excluded zero-diffusion face.  No
  nonlinear pattern branch is inferred from linear instability.
- **C351:** the exact open Jackson-network recurrence, product-form and
  visible quasi-reversal theorem.  Componentwise subcritical traffic is
  necessary and sufficient for positive recurrence; the invariant law is the
  unique independent geometric product.  The marked-jump time reversal is
  reconstructed, and forward external-departure histories are jointly
  independent Poisson processes independent of the present state.  Critical,
  overloaded, self-routing, isolated, tandem and zero reverse-input faces are
  explicit, without a false joint-independence claim for internal arcs.
- **C352:** the complete integer-kink Jackiw--Rebbi spectrum and scattering
  atlas.  The self-adjoint Dirac square gives one chiral zero mode and every
  simple pair `+/-sqrt(j(2n-j))`.  A normalized Darboux unitary identifies the
  entire continuous subspace with the free channel, proving purely absolutely
  continuous exterior bands and excluding embedded and singular-continuous
  spectrum.  Both bounded non-`L2` thresholds and the convention-locked
  reflectionless transmission product are exact.
- **C353:** the complete two-scale Ewens--Chinese-restaurant partition atlas.
  The local insertion rule yields exchangeability, the EPPF and every finite
  occupancy-vector probability.  The total block count is an independent
  Bernoulli sum with exact PGF, logarithmic strong law and normalized CLT.
  Mixed factorial moments plus uniform integrability prove joint independent
  Poisson limits for every fixed vector of block sizes, with all fixed-size
  concentration boundaries stated separately.

The strict tuples, in order, are
`(A0_FAIL,A1_WEAK,A2_FAIL,A3_FAIL,A4_NATURAL_QUANTIZATION)`,
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)`,
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)`,
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_NATURAL_QUANTIZATION)`, and
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)`.  All five are
`ROUTE_A_REJECTED`; Route B remains false.

## Exact release accounting and hashes

The finite ledgers are regression and convention receipts.  They do not
replace the analytic proofs of invariant-torus topology, the continuum PDE
criterion, recurrence of an infinite CTMC, whole-line spectral type, or the
probabilistic limit theorems.

| ID | finite evidence | independent / symbolic checks | hostile rejections | evidence bytes | final pages / fonts |
|---|---|---:|---:|---:|---:|
| C349 | 60 tangent states, 120 Lax probes, 30 axial, 30 coordinate, 6 repeated-spectrum and 5 isotropic rows | 9,540 / 767 | 152/152 | 139,424 | 3 / 12 |
| C350 | 9 parameter cases, 63 modal rows and 20 length walls | 150 / 14 | 60/60 | 24,459 | 3 / 6 |
| C351 | 12 networks, 1,020 balance rows and 84 visible reverse rows | 1,215 / 9 | 80/80 | 356,885 | 3 / 13 |
| C352 | 25 spectrum, 24 factorization and 150 scattering rows | 199 / 171 | 58/58 | 124,335 | 3 / 18 |
| C353 | 914 occupancy, 528 Stirling, 2,640 block-count, 320 innovation, 740 factorial-moment, 80 normalization and 16 boundary rows | 5,238 / 219 | 69/69 | 960,868 | 3 / 19 |
| **total** | **five independent exact ledgers** | **16,342 / 1,180** | **419/419** | **1,605,971** | **15 / 68** |

| ID | evidence SHA-256 | round 0 PDF SHA-256 | round 1 PDF SHA-256 | round 2 / final PDF SHA-256 | manifest SHA-256 |
|---|---|---|---|---|---|
| C349 | `3143cfd331de6cfc48f63bda13475bb4d62e7707d944c8d607f09dfead4f1f6c` | `8eb527baea8e37e40a70df7f3c58f0a162b2e44e4c7914fd382357516868a18a` | `344a9764b65290cc34ce805999b486c44d08330f5e0982cd91fe3eb391929ca9` | `f7d5568fb30b19a5b072f128b2998d884085b677e3529ffdca3b47f94e2f384b` | `da1b1fcdf7a31cecc4a91753cd287f32e1cef6f4c620249ae0204b345250f609` |
| C350 | `df020d6e943cc03e0185a8f7109b103adb4ed959452fde49d492426b94469429` | `495ef248da1dca9c1e2af49c0b247ed6a4b3de0ed7b0e36147e8ceeeb5445c9c` | `f21b7e603b719efc4148e4276963e1f0ccd643d48a0af430e9e1000c9742dd70` | `a7350723ba41d6e58b5d91c26f81a455a10a93d18ef67c1d3f758a7284a0c8a6` | `a12059b188140f8515d4f08d60fa3d42a62b1d527fadc50e496afc6f2f5d8f28` |
| C351 | `6918d5f06a0a57f9746111ef6dbfdf9293a467c49b64edd3dbdcaa85a981ffcd` | `7fcc245e500f2db0f8afbe1f25a694b7b3fe32b40ced666ac19db599af673f45` | `a633bb175929cf9e1fd9407c40876cb6f21d50f89be81502f7075cac440fee88` | `229823ee78f2831d573820db647f0199a9b0b11631195ce2b31c414fab9d9dcc` | `9e8f0a80e1f6fb37b242b3fd516da907322f99fcef307be3601ad581382bc914` |
| C352 | `c06aa780bd080bf3b86c845bcea8ded1cb3dd813a307c0fa5764f35b87942f4d` | `dea6caf29d13b75effd2caed8a62d73cb30fc5b0877cbeaeb9ffadc79bf4a582` | `e47dcca6d65014aeaca742854ef32b28f439c6a28aeea60a7dab08c6d93890a2` | `fc60a7ad8bc10257f9d9e99502cfa2ec9dabaca4981281c55e5af6e12bee9f85` | `77b981cf2ca261fbba1f64587dc2b5faa4990d3be55c6dd54bb22341d6207d26` |
| C353 | `62a8a6b81425cb4e78b7ebd3c8fede2f9fcec247f12f0beb5a14bc9e4cf4e866` | `41c16a138ff09d0f21c95420569e087d1b491ad3747f5f230da8e3d0946a96b1` | `73e6df231c336ac74512d362157936f732e055e375464c2b8f83a2fe223b46ca` | `4a036ef295873af816d9bf73a9719cae20aafc38c7d7f06df7a0604cbda6a0e1` | `b23fda9a0dc72bf79305b5064d7ca66aade755db94be2df9515b8e34ec5f3835` |

Every row has three distinct revision hashes and a final PDF identical to
Round 2.  The manifests cover 135 payloads and 140 physical package files.
All 15 final pages were visually inspected; all 68 final font rows are
embedded and subset.  Settled builds contain no layout, citation, reference,
destination, rerun, missing-character or missing-glyph warning.  The five
release programs pass in write mode and consecutive no-write runs with stable
hashes.

## Author-swapped corrections and integrity

C349's first cross-review found no blocker or major issue and three useful
minor corrections.  The Uhlenbeck conservation proof now uses the correct
identity
`sum_(j!=i) L_ij x_j = x_i(x dot p)-p_i|x|^2=-p_i`; the compact quantum
operator explicitly fixes `hbar>0`; and the repeated face now proves
`{J_12,F_3}_D=0`, `2H=a+J_12^2+(a_3-a)F_3`, and rank-two independence on a
nonempty regular open set through an exact differential-wedge witness.  The
producer, independent checker, symbolic lane and repaired-hash mutations all
lock the repaired contract.  Focused nonauthor review found no remaining
issue.

C350's audit made the real-to-complex modal passage explicit, added an exact
upper-endpoint neutral witness, and required a separately reconstructed
strict count-formula value in every open-window evidence case.  The checker
uses exact sign tests rather than floating approximations, and the hostile
suite owns all new fields.  Re-review found no blocker or major issue.

C351's audit clarified three process-level boundaries.  The reversed network
uses the natural class allowing zero exogenous rates; detailed reversal is a
law for visible marked jumps, with phantom self-routes reinsertable as
state-preserving marks; and the standard irreducible conservative
countable-state CTMC invariant-probability lemma is stated before recurrence
and uniqueness are invoked.  The external-output past/state orientation and
the nonclaim for internal-arc joint independence were independently checked.

C352's first audit found a genuine completeness gap: Darboux intertwiners had
constructed continuum waves but had not yet excluded singular continuous
spectrum.  The repaired proof defines the normalized transform
`U_m=D_m Q_m^(-1/2)`, proves it unitary onto the continuous subspace, identifies
its orthogonal complement with exactly the constructed bound-state span, and
thereby closes pure absolute continuity, no embedded spectrum and no singular
continuous spectrum.  It also fixes threshold endpoint constants, Jost/time
conventions, and repaired-hash ownership of date and epoch.  Focused re-review
approved the whole spectrum theorem.

C353's audit required direct evidence ownership of date and epoch, duplicate
row attacks for all seven ledgers, and a missing uniform-integrability step in
the multivariate Poisson-limit argument.  The proof now expands the square of
each factorial monomial into finitely many factorial monomials of order at
most twice the original order and applies the uniform moment bound before
passing moments to weak subsequential limits.  Factorial-moment determinacy
then closes the joint limit; focused re-review found no blocker or major.

Every checker imports no producer code.  JSON parsing rejects duplicate keys
and nonfinite constants.  Evaluation parsing locks exact schemas and rejects
aliases, anchors, merges, non-string keys, implicit timestamps, unknown
fields, type changes, authority drift and tuple drift.  Hostile suites repair
evidence hashes before semantic attacks, every Python entry point rejects
optimized execution, and isolated producer runs replay byte for byte.

## Citation and scope integrity

The source audits assign C349 to the Neumann--Moser integrable-system lineage,
C350 to Turing's morphogenesis criterion and Schnakenberg kinetics, C351 to
Jackson networks and Kelly's reversibility framework, C352 to Jackiw--Rebbi
kink fermions and exact one-dimensional kink spectral work, and C353 to Ewens
sampling and Hoppe's urn.  All source-local proofs are reconstructed here;
workspace collision screening and packaging are not presented as literature
priority.

All five evaluations use evaluator v0.2.0, SHA-256
`6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`,
and set `route_b_invocation_allowed: false` under literal scope
`NO_BAD_EULER_OR_ROOT_NUMBER`.  No target arithmetic local datum, Euler
factor, bad-prime datum, root number, automorphy object, target
divisor/counting law or functional equation, target-zero match,
Hilbert--Polya operator, or Route-B input is asserted.  Uhlenbeck residues,
Turing modes, queue departures, kink scattering levels and Ewens blocks retain
only their explicitly evaluated source-side meanings.
