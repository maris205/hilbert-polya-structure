# Claims and evidence ledger — P160 RCS Round 2

**Status:** `ANONYMOUS ROUND-2 / INTERNAL ACCEPT / HOLD_EXTERNAL`

The symbolic proof is dispositive. Computation is bounded counterexample
pressure, and source records define subtraction rather than priority.

| ID | Claim interface | Symbolic evidence | Exact pressure | Zero-credit boundary |
|---|---|---|---|---|
| A1 | exact fixed-`(a,b)` rank-`t` crop formula | cell-coordinate induction | literal iteration in both verifiers | static rectangle language |
| A2 | point clock, unique recurrence, sharp capped height | corner cell, strict loss, rectangle witness | exhaustive clocks/heights | Durfee decrement and generalized rectangles |
| A3 | exact absorbed series and shells | disjoint `lambda_(h+1)` slices | every empty-fibre coefficient | static hook/bounded products |
| B1 | every-time fibre of every prescribed nonempty target, with distinct empty branch | forced-core inverse bijection | all audited targets/times | static two-boundary symbol/decomposition and two-Pochhammer factorization |
| B2 | exact cap threshold and every weight above it | for excess `d`, use `gamma=(d)`, `beta=empty`; at `d=0` both are empty | exhaustive zero/nonzero support | elementary coefficient positivity |
| B3 | coefficient, image-count, and mass identities | coefficient extraction and fibre partition | exact mass conservation | generic generating-function algebra |
| C1 | conjugation exchanges `a,b` | coordinate transposition | conjugate parameter cases | Ferrers conjugation |
| C2 | three support probes recover ordered `(a,b)` | substitution and subtraction | all audited parameter pairs | arithmetic rearrangement |

## Mandatory sentinels

- `N=0`: height is zero on `{empty}`.
- `t=0`: the nonempty fibre is the singleton target at its exact weight.
- Empty target uses `E_(h,w)` and never undefined `mu_1` or `ell(mu)`.
- Positive-time support uses the one-part witness `gamma=(d)`, which has at
  most `h` parts because `h>=1`; `gamma=(1^d)` is not used.
- Conjugation does not erase ordered recovery.

## Evidence hierarchy

1. `main.tex` and `PROOF_PACKAGE.md`: all-parameter proof.
2. `verify_p160.py`: author exact control; 3,462,895 assertions.
3. Review-A verifier under `docs/.../reviews/p160_rcs_a/`: independent exact
   control; 7,332,616 assertions.
4. Review-B verifier under `docs/.../reviews/p160_rcs_b/`: independent exact
   control; 11,287,366 assertions; output SHA-256 `b6034231...b8a`.
5. `SOURCE_VERIFICATION.md`: metadata, definition-level inspection, and
   zero-credit boundary.

`HOSTILE_REVIEW_A.md` is preserved as the independent Round-0 review, not
rewritten as an author artifact.

Review B accepted with `0 Critical / 0 Major / 0 Minor`. The Round-2 visible
`HOLD_EXTERNAL` sentence is lifecycle consistency only and changes no claim,
proof, source boundary, verifier, or finding disposition.
