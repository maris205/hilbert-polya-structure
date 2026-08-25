# Batch review: HCS-C139--HCS-C143

Date: 2026-08-25

System family: five separate Route-A dynamical subtypes under
`NO_BAD_EULER_OR_ROOT_NUMBER`.

Recommendation: **retain all five as explicit source-structural progress;
continue Route A; keep Route B unauthorized**.

## Completed paper outputs

1. **C139** refines the directed-edge suspension by one cyclic `0011`
   marker.  Its eight-state presentation has an exact determinant and
   all-period primitive product.  The period-six words `001011/001101`, which
   have equal cyclic block populations through width three, are separated by
   exactly `sqrt(5)`.  The primitive period-seven pair
   `0101111/0110111` retains the full clock vector `(0,2,2,3,0)`, so the
   new clock is still not orbit-injective.
2. **C140** changes the base from a full shift to the strictly sofic
   mod-three gap shift.  Three intrinsic residual follower languages force
   its minimal right Fischer cover.  The all-zero label point has one
   intrinsic phase but a three-phase cover orbit, giving the exact correction

   ```text
   Z_140(u,v)=(1+v+v^2)/(1-u-v^3).
   ```

   The cover determinant and intrinsic inverse zeta remain explicitly
   distinct.
3. **C141** moves to a nonlinear complex polynomial.  The two inverse
   branches of `F(z)=z^2-6` on `D_4` define trace-class operators on
   `H^2(D_4)` and exhaust every periodic point.  The exact ladder has
   `det(I-uL_0)=1-2u`, `det(I-uL_1)=1`, and a nontrivial entire `m=2`
   Fredholm determinant.  Its raw primitive product starts at stability index
   two and is asserted only in the proved disk `|u|<4`.
4. **C142** supplies a genuinely infinite-rank countable owner.  The frozen
   renewal operator is trace class and has

   ```text
   det_F(I-zT)=1-sum_(m>=1)2^(-m(m+1)/2)z^m,
   ```

   an entire function of order zero with a primitive excursion product.  A
   constant-advance control keeps a simple rational renewal expression while
   its shift has singular value `1/2` with infinite multiplicity, preventing
   ordinary Fredholm ownership.
5. **C143** changes to a finite source-derived quantum walk.  Each frozen
   five-cycle arrangement gives a real ten-dimensional unitary with
   `Theta_w=C_w K`, exact reversal, and a signed primitive path product.
   Equal-population arrangements `00011` and `00101` have different secular
   polynomials; their population-average coin has defect
   `-(24/1625)I` and is not unitary.

## Uniform release audit

All five deterministic producers, producer-independent checkers, separate
symbolic reconstructions, canonical byte replays, and hostile mutation suites
pass.  Their receipts are:

- C139: 16,467 checker assertions, 35 symbolic checks, 8,190 rooted words,
  and 747 primitive cycles through period 12;
- C140: 2,028 checker assertions, 53 symbolic checks, 969 intrinsic rooted
  points, and 74 primitive label cycles through period 15;
- C141: 82 full-exact checker assertions, 38 SymPy/resultant checks, 126
  rooted periodic points, and 23 primitive orbits through period six;
- C142: 110 checker assertions, 56 symbolic checks, 16 determinant
  coefficients, 12 traces, and all 225 primitive necklaces through clock ten;
- C143: 62 checker assertions, 39 symbolic checks, 12 traces per arrangement,
  and every signed path through clock ten (1,270 rooted paths and 125
  primitive cycles at clock ten for each frozen support).

The mutation totals are respectively 49/49, 54/54, 37/37, 25/25, and
30/30.  Their repaired/stale splits are `48+1`, `53+1`, `36+1`, `24+1`,
and `29+1`, for 195/195 rejections overall.

Every release manifest has an exact 27/27 payload ledger with no missing,
extra, size-mismatched, or hash-mismatched file.  Each package has 28 physical
release files including its self-excluded manifest.  No Python cache, bytecode,
or LaTeX auxiliary/log/recorder artifact remains.

Fresh isolated fixed-epoch double builds reproduce all five checked-in PDFs
byte for byte.  The 12 rendered pages use embedded/subset fonts and show no
clipping, collision, truncation, malformed formula, broken table, blank
content, or unreadably small text.  Final logs contain no warning,
overfull/underfull box, undefined reference or citation, or multiply-defined
label.

## Content-addressed release ledger

| paper | evidence SHA-256 | PDF SHA-256 | manifest SHA-256 |
|---|---|---|---|
| C139 | `9d62ca433eac91693e58a6f443e780bed6e2aa6e267898586b8a5b86c5fe7bda` | `abd5a3ca4d98b181eb8bfe6c1fd30cc9728ca98510e4a021177a57b26dd493d5` | `0c2f9b2c9be6ad2ee4560e164a3bf1f3e1961fb2f535cf0090885b30baef3284` |
| C140 | `169cc4fcb795e28b4308037f50f7cccbb51bbbde255ae647aba9390232266aac` | `1e41191864c8a54e672116e181d8be2dc40c27a82db2fefc542ecfe7552ed513` | `11f121d1fd94b5f075720bc93770e1799dca59bd288435afa428cb57eb4363ec` |
| C141 | `50fc0cd938850df871f054e865a8dbbaec732bd715caa21acd064a764c657665` | `d23d87e351622821834fdd6fac6fe6117b0ba602167939e0251442ad0fbfe948` | `03079b962e7be48a174901f2737945537cd446a4ea104657b8cdc9596aec0c9f` |
| C142 | `2206007b8c0008c8529ce5e421ad34c6c8a92498e95300b7a10f594c63fae5a2` | `43473a72f7cf7ae375bae14471c3ee1e1c2a745e0c7a781d9e8722848f7d7382` | `5288ecf2a88a060a92045e81fd87c4de3e31fca702a86484f6a6bab4914906e3` |
| C143 | `07873e5ad9a1939177833946d5c6d611b494bb3258d8e67857afa3948d84d65b` | `8099e81a1bb9e11f9da3e5521bb6bf15bc7bf28eaf7cc06890a813e03c1e79e6` | `7ba772104a3545b38d46cfb03f5df3be17237dec5da0b4814dc22d299a8a3ac5` |

## Internal cross-review repairs

The reviews were evidence-anchored internal theorem/scope audits, not
external peer review.  No acceptance, novelty, or reviewer-independence score
is claimed.  They produced five release-relevant repairs:

- C139 replaced an incorrect verbal path description of its correct
  determinant cofactor by an explicit `7 x 7` to `5 x 5` Laplace reduction;
  it also made word primitivity and the fixed-nonzero-specialization boundary
  self-contained.
- C140 strengthened cover minimality from an internal no-merge observation to
  a genuine three-residual lower bound using synchronizing pasts `1,10,100`;
  it made `F_n` explicit, printed the entropy derivative, scoped imaginary
  periodicity, and removed a round-zero overfull box.
- C141 corrected raw-product terminology from the impossible sum of absolute
  factor values to the compact-uniform sum of factor deviations, and aligned
  the text-extraction command with its recorded digest.
- C142 added an executable Gram-matrix witness that the constant shift has
  singular value `1/2` with arbitrary finite multiplicity, rather than
  checking only a verbal noncompactness lock.
- C143 added an exact computation of the maximum absolute column sum `7/5`
  for both arrangements, directly covering the stated `|z|<5/7` raw-product
  disk.

The following boundaries remain deliberate:

- C139's memory-four result is relative to its frozen forward coding and
  does not give orbit injectivity or a cohomology-invariant minimum.
- C140's intrinsic rational correction has no separately constructed natural
  Fredholm owner on label space.
- C141's Fredholm determinant is entire, but its raw primitive product is not
  claimed outside `|u|<4`; the `m=1` owner cancels identically.
- C142's scalar renewal control is formal and noncompact; it cannot be used to
  infer ordinary determinant ownership.
- C143 is fixed at dimension ten and supplies no growing-level or
  self-adjoint spectral bridge.

## Route-A assessment

The strict tuples are:

```text
C139 (A1_WEAK,A2_FAIL,A3_FAIL,A4_FAIL)
C140 (A1_WEAK,A2_FAIL,A3_FAIL,A4_FAIL)
C141 (A1_WEAK,A2_FAIL,A3_FAIL,A4_FAIL)
C142 (A1_WEAK,A2_FAIL,A3_FAIL,A4_FAIL)
C143 (A1_WEAK,A2_FAIL,A3_FAIL,A4_UNITARY_OR_SCATTERING_CANDIDATE)
```

C143's A4 subgate belongs only to its source-derived coined walk; it is not
combined with any coordinate of C139--C142.  No package has a frozen target
divisor, zero census, functional equation, counting-law comparison,
arithmetic local factor, Euler factor, root number, automorphy object, or
Hilbert--Polya operator.  Every overall verdict is `ROUTE_A_EXPLORATORY` and
`route_b_invocation_allowed=false`.

## Next gate

The next Route-A round should again diversify the source mechanism while
building directly on one exact boundary per paper: a coding-invariant roof
test beyond C139, an intrinsic operator owner for a corrected sofic zeta, a
larger or parameter-uniform nonlinear Ruelle family, a broader trace-class
countable graph, and a growing-size or controlled-limit unitary walk.  A
target-facing comparison remains a separately frozen protocol requiring
explicit authorization; it is not inferred from this batch.
