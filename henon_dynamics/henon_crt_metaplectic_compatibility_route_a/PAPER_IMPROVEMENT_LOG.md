# Paper improvement log — HCS-C136

The three payload PDF snapshots are genuine successive drafts.  No external
reviewer score, acceptance prediction, or novelty judgment is represented.
Each round used a structured theorem/proof and scope audit, followed by source
edits and a fresh fixed-epoch compilation.  Two additional internal
release-hardening reviews were applied before regenerating the Round-2 payload.

## Round 0 — complete baseline

Snapshot: `paper/main_round0_original.pdf`

SHA-256: `d7547df486ccd4c4808c92b068aa63d1c593c5cd0770b6e850f7889f9b3cb275`

The baseline contained the generalized-character Egorov statement, exact
two-factor CRT theorem, finite-factor induction, `(3,5)` control, evidence
totals, and Route-A boundary.  Review exposed three presentation risks:

1. the inverse-scaled character was stated but its entrywise phase identity
   was not visually isolated;
2. the Weyl proof did not foreground the essential `Q_r^(c q)` exponent;
3. the `(3,5)` Fourier mismatch alone did not explicitly prove the claimed
   no-scalar statement for the unitary itself.

## Round 1 — convention and obstruction audit

Snapshot: `paper/main_round1.pdf`

SHA-256: `0b082ac82dbdea999ab1c51f32fef76a53b946bcce28bde4c488d68470d2fa0f`

Implemented fixes:

- promoted the inverse-scaled phase decomposition to a numbered equation;
- displayed the separate `Q` and `P` conjugations under canonical CRT;
- stated positive square-root normalization as the reason no hidden scalar
  remains;
- added a universal canonical-CRT proposition proving that the standard
  `c=1` unitary tensor cannot be repaired by a scalar;
- turned `(3,5)` into a three-column exact exponent control;
- named the canonical tensor associator in the coherence theorem.

The second review found no formula error, but identified two remaining scope
risks: “coherence” might be misread as a claim about corrected standard
characters, and finite receipts might be misread as the basis of the universal
quantifier.

## Round 2 — hostile scope and reproducibility audit

Snapshot and final release PDF: `paper/main_round2.pdf`, `paper/main.pdf`

SHA-256: `ab83e92b78e5857946d501c579bc3d53ca233ea5d32bf1c1865506ce776a460d`

Implemented fixes:

- restricted monoidal language to the generalized-character fibers and
  canonical residue-basis maps;
- explicitly withheld associativity for any correction back to `c=1`;
- separated the algebraic proof from finite replay sentinels;
- reported the independent checker, 96,449 symbolic checks, and 83+1 mutation
  split;
- added raw-residue, noncoprime, and even-convention controls;
- limited the standard-family obstruction to the canonical identification and
  withheld a classification of other local Clifford corrections;
- sharpened the progress statement over C131 without changing the strict
  Route-A tuple.
- replaced an over-broad phrase about character restriction by the precise
  statement that the global character need not be standard on every factor.

### Release-hardening review 1 — antiunitary and quantifier audit

The first new internal review scored the live draft `7/10`: the bounded CRT
formulas passed, but `A4_NATURAL_QUANTIZATION` lacked package-local
antiunitary evidence and one theorem-package sentence overreached beyond the
tested leaf order.  The repair:

- defined `Theta_[r,c]=F_[r,c] K_r` for every odd level and unit character;
- proved and certified `Theta^2=I`, exact evolution reversal, and the Weyl
  coordinate swap;
- proved canonical CRT compatibility using the real residue-basis permutation;
- extended producer, independent checker, SymPy, replay, and repaired-hash
  mutation coverage;
- restricted multifactor coherence to binary split schedule and
  parenthesization for fixed ordered leaves, explicitly excluding permutation,
  braiding, and symmetric-monoidal claims.

The fixed-epoch repair draft compiled without a final warning as a five-page
PDF with SHA-256
`0eafe2acc457217dec6ed628c7db02ace72af64d6fe42f8c94f6573a91fb814e`.

### Release-hardening review 2 — formalization and release consistency

The second internal review returned no formula or quantifier blocker.  It
requested one formal clarification and identified stale release artifacts.
The final repair therefore:

- defined the anti-tensor first on pure tensors and extended it
  conjugate-linearly to the full ordered tensor product;
- regenerated the evidence and reran every exact path;
- condensed only receipt prose and the conclusion to remove an otherwise
  nearly blank fifth page, without deleting a theorem, proof, count, or scope
  boundary;
- rebuilt `main_round2.pdf` and `main.pdf` twice in isolated fixed-epoch
  directories and refreshed every recorded hash.

Final format inspection found four complete pages, embedded/subset fonts, and
no layout, reference, citation, or label warning.  The final rendered-page
audit found no clipping, collision, truncation, malformed formula, or blank
page.
