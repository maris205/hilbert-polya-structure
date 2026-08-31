# P128 improvement log

## Round1: implementation of Hostile Review A

Date: 2026-08-31 UTC.  The three MINOR findings in
`HOSTILE_REVIEW_A.md` were implemented without changing the theorem ceiling
or the external release state.

| review item | repair | evidence |
|---|---|---|
| A1: fixed-cut uniqueness was implicit | The cyclic-transfer proof now fixes the labelled coordinate cut, defines the forced state before every coordinate, and states explicitly that the trace neither quotients by rotations nor recounts a vector by its zeros. | `main.tex`, Lemma 3.1 proof; visible in `main_round1.pdf` |
| A2: verifier did not construct `M_t` | `code/verify.py` now constructs the truncated polynomial matrix `M_t(y/(1-y))`, computes its `p`th power, extracts the trace, and compares every coefficient with direct residual-vector enumeration for `p=2,3`, all five possible `(p,t)` cases, and weights `0..9`. | 50 new exact assertions; canonical total `180453`; fresh stdout/canonical `cmp` status 0 |
| A3: analytic ambiguity in “Euler product” | Manuscript and support prose now consistently use the exact term **formal orbit Euler product**. | terminology scan of current package |

The immutable `main_round0_original.pdf` is preserved.  The repaired PDF is
frozen separately as `main_round1.pdf`.  External status remains
`HOLD_EXTERNAL`; no Review B or final-QA conclusion is created by this pass.

## Round1 freeze

```text
main.tex                 fa1c10facf18dbb215896da5d4e6b36af446ce60f85208c1a632159f4d0ee1c7
code/verify.py           1b58fb8f71ac74082fb0ed9131a555a2ed4b7716da035e731ee9e5da0ac4a2fe
verification_output.txt  3b5e5bbbe94ec7ed7e689ff6a2cfeb2dc04a1ebc1ce9686c44194518ac1b1204
main.pdf/main_round1.pdf  f49d7c850e6c607130b96ff80f409ac642bae21ecae80203857262f831677439
main_round0_original.pdf  e2c063e17ce35249978a5729d27194c9223a893865b62ef11ce8f90c2435d667
```

## Review B and round2 sign-off

Independent Review B returned critical 0, major 0, minor 0 and
`GO_INTERNAL / HOLD_EXTERNAL`.  It independently reconstructed the local
trace, formal orbit Euler product, full target law, and all owner firewalls;
it also inspected the actual polynomial-matrix code, reran the 180,453-
assertion canonical verifier, reproduced the PDF in isolation, and audited
all four pages, fonts, and anonymous metadata.

No theorem, source, code, reference, or support correction was requested.
`main_round2.pdf` is therefore byte-identical to `main_round1.pdf` and
`main.pdf`, SHA-256
`f49d7c850e6c607130b96ff80f409ac642bae21ecae80203857262f831677439`.
Paper-local final QA is complete: fresh canonical output matched byte for
byte, an isolated four-stage build reproduced the reviewed PDF, and the
round-two package is frozen by `SHA256SUMS`.  The terminal status is
`GO_INTERNAL / HOLD_EXTERNAL`.
