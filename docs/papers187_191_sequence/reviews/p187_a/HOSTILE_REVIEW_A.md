# P187 process-separated hostile Review A

## Verdict

`PROVABLE AS STATED / ZERO FINDINGS / ACCEPTED_NO_CHANGE / HOLD_EXTERNAL`

The frozen Round-0 paper survives the mathematical, source-boundary,
collision, build, and artifact attacks in this package.  No file in
`papers/187-cyclic-divisor-quotient/` was modified.  The separation is a
process separation between author and reviewer; it is not a claim that their
errors are statistically independent.

## Frozen input and control binding

| object | SHA-256 | disposition |
|---|---|---|
| `main.tex` | `e4dd2c5afb6381563476c6b6735f94c932403492165b8f21adeee6a448f7b83d` | reviewed read-only |
| `main_round0_original.pdf` | `399ee1fd64a569ef3076e1049a5151e5b4b07d03d2c1592f84c5b2a811fbb8a1` | reviewed read-only |
| author `code/verify_p187.py` | `bb171bd84a5f614b868c6fd6e6008c646a282045bef484d4552081967743cf1e` | bound, not imported |
| author `code/CANONICAL.txt` | `b48c1753908ca9b168803cb6406499945bb59a82ac16d0f1f87e9ef278f8bb8d` | bound; 278,456 assertions |
| `PROOF_PACKAGE.md` | `095d2370f9c4f4b5d62e909a773f9a2fc05f2577ea8313b39472843b6071955d` | cross-checked against theorem text |
| `SOURCE_VERIFICATION.md` | `cdf97a65b4df3ac1f1ea4a3c8959d2db0ffc367777d3e00080c8c9bd854eedac` | owner status retained |
| reviewer `verify_review_a_p187.py` | `70088e5a5b47a58057b64b5ce61ff29d409b9c4297cd5e444b3f314ec1bc9467` | new, no author import |
| reviewer `CANONICAL.txt` | `596ec6ebf0c61042499f51b802a3014f384345ef16d275e8bb41bb324538539c` | two fresh replays required |

`PINNED_INPUTS.sha256` is the executable six-row author-input receipt.  The
package-level `SHA256SUMS` binds all reviewer artifacts and intentionally does
not list itself.

## Independent attack route

The author enumerates exponent tuples and evaluates general matrix products.
The reviewer instead packs words as base-`q` integers, regards a prescribed
output as a circular sequence of oriented edge constraints, and reconstructs
its lifts by a closed-walk transfer.  Only after that independent count is
obtained is it compared with the displayed trace.  The forward proof is
attacked directly at the frozen-peak/residual identity, not inferred from a
depth histogram.

The control covers 36 exponent boxes (`0 <= a <= 5`, `1 <= m <= 6`), 82,200
exponent states, and 20 composite boxes on `N in {1,8,12,20,72}`, totalling
26,072 divisor states.  It records exactly **1,444,819** successful assertions.
This bounded computation is counterexample pressure only; the all-parameter
proof is the reason for the verdict, and the control supplies neither proof
nor novelty evidence.

## Hostile conclusions

- The `p`-adic conjugacy is exact coordinate by coordinate, including the
  empty prime product at `N=1`.
- A height-`h` output forces the source edge `(h,0)`.  Its two output
  neighbours vanish even when several peak collars overlap cyclically.  The
  residual split persists under every later iterate and closes the induction.
- The sharp witness `(0,...,0,h,1)` has tail exactly `h` for every `m>=3`.
  The self-neighbour case `m=1` and two-site case `m=2` instead have sharp
  tail one when `N>1`; the unique `N=1` state has tail zero.
- Fixed prime supports are exactly cyclic independent supports.  The weight
  `a` per occupied site gives the stated polynomial, including `I_1=1`,
  `I_2=1+2a`, the closed coefficient formula, and its recurrence.
- With rows labelled by the present exponent `u` and columns by the next
  exponent `v`, the entry `1[(u-v)_+=b]` is the correct oriented constraint.
  Closed edge walks reproduce every fibre.  The local matrices genuinely do
  not all commute, so the order convention was checked rather than assumed.
- Each ordered pair `(u,v)` chooses exactly one output `b`; hence
  `sum_b L_b=J`, `tr(J^m)=(a+1)^m`, and prime multiplication recovers all
  divisor-word mass.  Empty fibres, the all-one target, the common-prime
  obstruction, and every `m=1,2` branch agree with direct enumeration.

The full derivation and counterexample ledger are in
`PROOF_REDERIVATION.md`; sources and historical collisions are treated in
`SOURCE_OWNER_COLLISION_AUDIT.md`; cold builds and PDF checks are in
`BUILD_PDF_QA.md`.

## Finding ledger

| severity | open | closed | finding IDs |
|---|---:|---:|---|
| Critical | 0 | 0 | none |
| Major | 0 | 0 | none |
| Minor | 0 | 0 | none |

No repair is requested.  `DELTA.md` is a standalone `PASS` /
`ACCEPTED_NO_CHANGE` receipt.  A byte-identical Round-1 lifecycle receipt is
permitted; any theorem, citation, source, or control change reopens this
review.  Review B must independently reopen every kill switch.

## Replay

From repository root:

```bash
sha256sum -c docs/papers187_191_sequence/reviews/p187_a/PINNED_INPUTS.sha256
PYTHONDONTWRITEBYTECODE=1 python3 docs/papers187_191_sequence/reviews/p187_a/verify_review_a_p187.py \
  | cmp - docs/papers187_191_sequence/reviews/p187_a/CANONICAL.txt
(cd docs/papers187_191_sequence/reviews/p187_a && sha256sum -c SHA256SUMS)
```

Acceptance requires three zero exit codes.  External circulation remains
blocked by `OWNER_AMBER / HOLD_EXTERNAL`.
