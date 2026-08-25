# C139 paper improvement log

No external reviewer, numerical review score, acceptance prediction, or venue
claim was used.  Two genuine internal proof/claim/presentation audits were
followed by source edits, fixed-epoch recompilation, and retained PDFs.

## Round 0: baseline

- Artifact: `paper/main_round0_original.pdf`
- SHA-256: `6b04104ab5d2e7ea1ff3d6cab245a38d60d6375a276ee7d03e8f8b45e6ea4e47`
- Pages: 2

The baseline stated the eight-state determinant, all-period trace/product,
minimal-memory pair, residual collision, and strict boundary.  The first
internal audit found that the higher-block determinant reduction, analytic
meaning of the specialization, five-radical independence, and primitive-pair
status were too compressed for a standalone certificate.

## Round 1: proof-completeness revision

- Artifact: `paper/main_round1.pdf`
- SHA-256: `270ca5c48fbd8b87a438b338d71284f916edb5720559ee7737c39de7c027c4b5`
- Pages: 2

The revision added the closed-path bijection behind the `y=1` reduction, an
explicit convergence condition, the automorphism/subfield proof excluding
`sqrt(5)`, and the distinct-necklace statement.  It also expanded the
cofactor discussion.  A second independent internal audit then found a real
MAJOR writing defect: the determinant value was correct, but the listed
“forced transitions” did not constitute a valid cofactor derivation.  It also
requested a self-contained primitivity check and a fixed-nonzero-specialization
qualification for the imaginary-period statement.

## Round 2: exact cofactor and boundary revision

- Artifacts: `paper/main_round2.pdf`, `paper/main.pdf`
- SHA-256: `abd5a3ca4d98b181eb8bfe6c1fd30cc9728ca98510e4a021177a57b26dd493d5`
- Pages: 2

The invalid verbal cofactor path was removed.  The final paper displays the
five-by-five residual matrix `Q` obtained from the actual seven-by-seven
cofactor and performs the row/Laplace reduction `det(Q)=-x01*x11`, proving the
sign and monomial.  `THEOREM_PACKAGE.md` records the complete seven-by-seven
minor.  The final revision also proves primitivity by excluding the divisors
`1,2,3` of period six, uses the marker count to exclude rotation, and limits
the imaginary-period control to fixed `z=1`.

The final source passes two fresh isolated fixed-epoch builds byte for byte.
Every font is embedded; both final logs are free of warnings, overfull or
underfull boxes, undefined references/citations, and multiply defined labels.
Both rendered pages were visually inspected without clipping, overlap,
truncation, broken formulas, or unintended blank pages.
