# Claims-to-evidence map — P126

Status: **ROUND-2 FINAL FREEZE / EXACT CONTROLS PASS / GO_INTERNAL /
HOLD_EXTERNAL**.

| ID | Claim | Proof anchor | Mechanical evidence | Credit ceiling |
|---|---|---|---|---|
| C1 | Codeword length, terminal marker, pointwise and sharp global clock | Lemma 2.1; Proposition 2.2 | all compositions through weight 18; codewords through `m=256,t=8` | balanced divide-and-conquer clock zero-credit |
| C2 | Cumulative and exact depth counts are bounded-part composition counts | Corollary 2.3 | exhaustive depth census through weight 18 | restricted-composition enumeration zero-credit |
| C3 | `N_K(a)=N_K(b)` iff `Phi^t(a)=Phi^t(b)` | Theorem 3.1 | both directions checked over every source through weight 15 for `t<=5` | core residual kernel theorem |
| C4 | Canonical code is suffix-decodable; decoder exactly recognizes the image | Theorem 3.1 | decoder on every literal image and every target through weight 15; code sentinels through `t=8` | generic code theory zero-credit; literal code residual |
| C5 | Every nonempty iterated fibre is a product over canonical one-runs | Theorem 4.1 | literal fibres compared with both normal-form product and independent factorization DP for all targets through weight 15, `t<=5` | core pointwise residual |
| C6 | Maximum `t`-fibre is `R_(2^t)(n)` and equals the cumulative depth count | Theorem 4.1 | exact maxima and all-one extremizer through weight 15 | bounded-part count itself zero-credit; dynamical duality residual |
| C7 | Complete `t`-image OGF and recurrence | Theorem 5.1 | literal image sets through weight 15; OGF recurrence through weight 90, `t<=8` | parts-in-a-set OGF zero-credit; image bijection residual |
| C8 | Garden count is total compositions minus the image count | Theorem 5.1 | exact literal image complements in exhaustive range | bookkeeping consequence |

The verifier makes **8,756,710** exact assertions using only deterministic
standard-library integer operations.  Finite controls are falsification
evidence and do not prove all-parameter statements or ownership.

## Pre-paper proof-spike provenance

The phase-one gate was pinned to three immutable inputs; these are historical
proof-spike hashes, not hashes of the current paper-local verifier:

- `proof_spikes/BALANCED_COMPOSITION_REFINEMENT_REPORT.md`:
  `fe4796bb730ac51c40e3ce2dd36f898ef13910da6ece50561b6a13eacc9f32b7`;
- `proof_spikes/verify_balanced_composition_refinement.py`:
  `fba237ac83d1a6f470f890824406a52b8a6eaa6189d02dca8f31bcfcd12999a2`;
- `proof_spikes/BALANCED_COMPOSITION_REFINEMENT_CANONICAL.txt`:
  `c04de425fd715d549cdd2bfec5a4dc3a7eaf2c49719076059f2e9fc78b15c3f1`.

The gate records a fresh run of the pinned source with stdout compared
byte-for-byte against the pinned results: `fresh_stdout_byte_compare_exit=0`.
