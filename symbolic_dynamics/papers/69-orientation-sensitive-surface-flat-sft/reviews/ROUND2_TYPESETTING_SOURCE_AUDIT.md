# Round 2 typesetting and source-role audit

**Trigger:** external internal-gate feedback after the first compiled draft.  
**External-release status:** HOLD.

## Critical typesetting finding

Six source formulas contained a literal comma at the start of an exponent,
for example `nu_chi^(comma n+2)` and `d_chi^(comma 2-2g)`.  LaTeX accepts this syntax,
so compilation alone did not flag it; the PDF printed the comma as
mathematical content.  A source-level exact-text search for the literal
three-character sequence “caret, left brace, comma” located every occurrence
in the abstract, introduction, background, and
fixed-law section.

## Source-role finding

One configuration note called Klug a “modern primary source.”  The formulas
are classical and belong to Mednykh and Frobenius--Schur.  Klug is the modern
source/account used for exact normalization and theorem-location verification,
not the original owner.

## Required gate

- Replace every malformed exponent by a plain exponent such as `^{n+2}` or
  `^{2-2g}`.
- Search the entire non-binary package and require zero matches for that
  three-character sequence.
- Correct the Klug role in configuration, claims/evidence, citation audit, and
  improvement log.
- Recompile from source and inspect extracted PDF text for `nu_chi^(n+2)` and
  `d_chi^(2-2g)` without commas.
- Regenerate visual QA images.
