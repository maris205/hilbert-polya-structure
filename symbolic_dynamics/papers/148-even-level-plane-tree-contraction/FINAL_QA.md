# Final QA — P148

**Status: ROUND-2 INTERNAL REVIEW ACCEPTED / HOLD_EXTERNAL.**

## Review closure

- Hostile Review A: **1 Critical / 0 Major / 2 Minor**.
- Critical repair: disclosed Soo--Khoussainov--Linz
  arXiv:2111.13238v4, Definition 6.6, as the exact unordered one-step owner;
  proved the forgetful equivalence; reopened the owner gate.
- Minor repairs: exposed the recursive global `F_U` bijection and corrected
  Höner/2021 metadata.
- Independent Hostile Review B: **0 Critical / 0 Major / 0 Minor, ACCEPT**.

`HOSTILE_REVIEW_A.md` and author-side `SELF_QA.md` are preserved as
historical pre-closure checkpoints.  Their then-pending/critical language is
superseded for current status by `HOSTILE_REVIEW.md` and this final QA record.

## Final ownership ceiling

The direct owner equivalence is

```text
For(E(T)) ≅ OutContr(For(T), root(T)).
```

The unordered rule, partition-tree interpretation, generic promotion, bare
height compression, and every cheap unordered all-rank depth/clock
consequence receive zero contribution credit.  The temporal theorems remain
proved supporting analysis only.

The sole residual claim is the conjunction

```text
ordered every-target size-refined inverse
+ exact-layer image criterion
+ algebraic image series.
```

The reopened literature audit is bounded.  Its non-hits do not prove novelty,
priority, ownership completeness, or release freedom.

## Mathematical QA

| Interface | Result | Basis |
|---|---|---|
| finite self-map on `PT_{<=N}` versus source layer `PT_n` | PASS | literal vertex deletion; exact-layer convention explicit |
| all-rank survivor skeleton and clock | PASS / zero credit | labelled induction, deepest path, path extremizer |
| local block-and-gap factor | PASS | reversible productive-block/empty-gap construction |
| global target fibre | PASS | `F_U=A_d product_j F_{U_j}`; injective, surjective, coefficientwise finite |
| exact-size image criterion | PASS / residual | nonvanishing exact fibre coefficient |
| algebraic image series | PASS / residual | target minimum-source-weight specification |
| singleton, leaf, `d=0`, `d>0`, equality threshold | PASS | explicit derivation and exact pressure |

`PROOF_PACKAGE.md` remains **PROVABLE AS STATED**.  Computation is not used
as proof.

## Exact-control QA

- Cold replay result: `P148_THEOREM_INTERFACES_PASS`.
- Assertions: 216,905.
- Enumerated carrier pressure: all 23,714 plane rooted trees through 11
  vertices.
- Generated transcript is byte-identical to `verification_output.txt`.
- Coverage includes labelled iterates, clocks, every target/source-size
  fibre, local factors, image sets, and algebraic coefficients.

## Artifact QA

| Check | Accepted value |
|---|---|
| Current round-2 PDF | `main.pdf` |
| Pages / size | 5 A4 pages / 357,397 bytes |
| SHA-256 | `5c681793e5e97abb0ad718f876a2e0af11bd2d41585d860dc0c5b8c3992ed957` |
| References | 5/5 cited and resolved |
| Visual inspection | 5/5 pages accepted |
| Isolated build | source-only build byte-identical to `main.pdf` |
| Final log | no unresolved citation/reference, rerun request, error, or bad box |
| Fonts | embedded and subsetted |
| Anonymity | anonymous presentation and blank title/author metadata |

The required Limitations, Data Availability, Ethics Statement, Author
Contributions, Conflict of Interest, and Funding sections are present.

## Final decision

P148 passes the round-2 internal proof, owner, exact-control, reproducibility,
and visual gates under the narrow residual above.  It remains
`HOLD_EXTERNAL`: no release, posting, submission, specialist contact,
novelty/priority assertion, or Git action is authorized.
