# Paper 21 Proof-First R0 Source Repair

Date: 2026-08-22 UTC

Status: `SOURCE_REPAIR_FROZEN_R1_REQUIRED`

This is an author/governance ledger, not a review and not a build PASS. It
records the sole bounded source repair opened after the first deterministic R0
attempt failed the locked 24--29 substantive-page contract and reported two
overfull boxes.

## Baseline and repaired identities

Blocked-R0 baseline:

- `paper/main.tex`: SHA-256
  `c3d34411f3012a446238c098a10e1f76258236a5d0b6da91f7b01475633c1e86`,
  67,605 bytes, 1,554 LF.
- `paper/math_commands.tex`: SHA-256
  `05c80b105ba2942d66aa6e717bbe15f24511abcdbcc5480daffd899f1622087a`,
  981 bytes, 33 LF.
- `paper/references.bib`: SHA-256
  `4f1c68133d959ce3377707775830748f1301d082a70c0787c23ae7da183590b8`,
  675 bytes, 19 LF.

Final frozen repaired trio:

- `paper/main.tex`: SHA-256
  `34074c5965086d79145bf2b273398c4c17fdc264b6f5e3555fd1b9a2bd27c7b2`,
  84,917 bytes, 1,990 LF.
- `paper/math_commands.tex`: unchanged.
- `paper/references.bib`: unchanged.

The old replacement R1/R2 reviews bind only the blocked-R0 baseline. The two
files named `INDEPENDENT_PAPER_SOURCE_R1_PAGEFIX_REVIEW.md` and
`INDEPENDENT_PAPER_SOURCE_R2_PAGEFIX_REVIEW.md` bind only the intermediate
`main.tex` SHA-256
`910086eb0b42c297c0d5468d23c30a8893c6b02ba8b3afcce774a0eb2ad4a4c6`.
They were produced during the same live-worker interval as that source change,
fail the independent-review discipline, and in all events do not bind the final
source. None of these historical reviews grants current build authority.

## Exact repair boundary

The repair adds only proof-order-preserving material inside the locked L1--L9
chain:

1. a bounded comparison ledger that prevents the fixed theorem from being
   over-read as a generic affine-triangular, torus, conjugacy, periodic, or
   computer-assisted claim;
2. an exact facial-slack ledger with
   `h=g-3-2x-2y`, `M_S=1+h`, and
   `X'-1=(x+h)/D`;
3. a row-by-row expansion of the height functional and exact endpoint
   factorizations for both ranges in the cone proof;
4. explicit first- and second-iterate audits;
5. the six-coordinate inductive state showing where the carried `p`- and
   `q`-vectors enter the two phase sums;
6. six positive coefficient witnesses read directly from the displayed
   gradient rows;
7. an explicit six-coordinate dominance chain fixing `q_3` as the unique
   visible degree row;
8. a positive-eigenvector squeeze proving directly that the visible matrix
   row has exponential rate `rho(C_g)`;
9. bounded explanatory transitions in the related-work, characteristic-
   polynomial, and conclusion sections; and
10. line breaks for the two displays that produced overfull boxes in the
    blocked build.

No theorem statement, potential, gradient, matrix, selector formula, cone,
phase recurrence, visibility formula, characteristic polynomial, residue
class, title, citation, bibliography entry, anti-claim, section order, or
publication-scope permission changed. No appendix, figure, CAS result,
numerical result, experiment, dataset, new citation, priority claim, or
external effect was introduced.

## Concurrency containment

During the repair, a still-live prior source worker produced additional local
expansion text despite a read-only follow-up instruction. The worker was
interrupted immediately. The complete current file was then diffed against the
exact blocked-R0 baseline; every retained addition is listed above and was
recomputed or checked line by line. Nothing from that concurrent write inherits
review authority. The current identity is frozen as a new source and requires
fresh R1 and R2 review from agents that did not author it.

## Static pre-review checks

- 8 main sections, no appendix, and proof order L1--L9 preserved.
- 720 opening and 720 closing braces.
- All `begin`/`end` environments paired.
- No duplicate label and no reference to a missing local label.
- Exactly two citation commands: `BlancVanSanten2019` and `ShaoSun2025`.
- No `TODO`, `FIXME`, `VERIFY`, reviewer/workflow language, source-lock or
  publication-lock language, internal path, hash, acknowledgment, or private
  provenance in the manuscript.
- Approximately 8,856 de-TeXed words before expanding the macro input.

Compilation remains closed until fresh independent repair-source R1 and R2
reviews both pass.

`SOURCE_REPAIR_FROZEN_R1_REQUIRED`
