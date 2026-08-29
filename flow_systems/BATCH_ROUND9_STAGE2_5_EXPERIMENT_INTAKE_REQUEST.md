# Round 9 Stage 2.5 experiment-intake checkpoint

Date: 2026-08-29 (UTC)

Scope: Papers 24--28, frozen at source commit
`21c4755dba399dff8245e15d0ba43ca9eb27fa27`.

## Why this checkpoint is required

All five manuscripts report project-owned computational results and point to
local source, tests, frozen inputs, result ledgers, and reproducibility
receipts.  Stage 2.5 replay independently passed 372/372 historical tests and
80/80 Round-8 tests.  Therefore `no_experiments_declared` would contradict the
manuscripts.

The current ARS Material Passport contract requires the experiment-intake
choice to be made by the scholar.  An agent may inventory the existing files
and check their hashes, but may not infer or sign
`experiment_intake_declaration.declared_by = scholar`.  No such explicit
declaration is currently present for Papers 24--28.  The fail-closed result is
stable issue `R9-IL-SERIOUS-EXP-DECL-1`.

This issue is procedural provenance, not a detected mathematical error.  It
does not change any theorem, numerical count, Route-A verdict, or frozen paper
byte.  It does block Stage 2.5 passage until explicitly closed.

## Exact declaration requested from the scholar

Please confirm or reject the following complete statement:

> Papers 24--28 each report computational experiments or exact computational
> certificates actually executed for this project.  I authorize their
> Material Passports to record
> `experiment_intake_declaration.status = experiments_declared`,
> `declared_by = scholar`, and the confirmation time as `declared_at`.  I also
> authorize the existing Round-2 through Round-8 source files, frozen inputs,
> result ledgers, tests, validation notes, and reproducibility receipts to be
> transcribed into the corresponding `experiment_provenance[]` entries.  To my
> knowledge, no additional own-experiment result used by these five
> manuscripts is omitted from those repository artifacts.

If confirmed, the next integrity-only patch will populate and schema-check the
five provenance arrays, run claim-to-result alignment, close
`R9-IL-SERIOUS-EXP-DECL-1`, and reissue the Stage 2.5 decisions.  It will not
edit the manuscripts, bibliographies, PDFs, or scientific Route-A verdicts.

