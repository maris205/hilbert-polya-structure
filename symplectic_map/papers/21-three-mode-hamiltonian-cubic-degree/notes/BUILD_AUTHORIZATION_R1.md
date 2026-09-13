# Paper 21 Deterministic R1 Build Authorization

Date: 2026-08-22 UTC

The canonical repaired R0 receipt is SHA-256
`3899ee597562861623bd161a00063fc683f5f998499c677fd7e85e842f1a6e96`.
Fresh replacement build R1 review SHA-256
`62511dd572fa14bdea670df85eb6a48fc54e081a916af5935fdca8f870531bdd`
ends `BUILD_R1_R0_REPAIR_REPLACEMENT_PASS` with zero findings. The sole
revision window is consumed by strict-canonical no-op receipt SHA-256
`441c1cc5e7b3372bbe1d7f05e34ac19461f109bcb0de1e9f7cd4e23db6ba8d42`,
status `R1_NO_OP_REVISION_PASS`.

The unchanged authorized source trio is:

- `paper/main.tex` SHA-256
  `34074c5965086d79145bf2b273398c4c17fdc264b6f5e3555fd1b9a2bd27c7b2`;
- `paper/math_commands.tex` SHA-256
  `05c80b105ba2942d66aa6e717bbe15f24511abcdbcc5480daffd899f1622087a`;
- `paper/references.bib` SHA-256
  `4f1c68133d959ce3377707775830748f1301d082a70c0787c23ae7da183590b8`.

Exactly two fresh independent roots may run the fixed
`pdflatex -> bibtex -> pdflatex -> pdflatex` sequence with the same fixed
date, locale, timezone, and PATH as R0. Acceptance requires all root outputs
and command logs to be byte-identical to one another and the final PDF to be
byte-identical to the R0 PDF SHA-256
`b02785a088008c3938652c28857347246dbf15e800d71269be7fdcd987e65fe3`.
All R0 validation gates remain conjunctive.

Only `paper/main_round1.pdf`, refreshed current build outputs,
`paper/BUILD_METADATA_R1.json`, and `paper/BUILD_RECEIPT_R1.json` may be
persisted after PASS. Source edits, CAS/numerics/science, figures, release,
transport, upload, submission, external messaging, and identity disclosure
remain unauthorized.

`BUILD_AUTHORIZATION_R1`
