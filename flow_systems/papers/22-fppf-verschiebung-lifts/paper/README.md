# Paper 22 manuscript package

## Primary artifacts

- [manuscript.tex](manuscript.tex) — LaTeX source
- [references.bib](references.bib) — three verified bibliography records
- [paper.pdf](paper.pdf) — reproducible Stage-5 final PDF

## Rebuild

For a byte-reproducible build, set
`SOURCE_DATE_EPOCH=1787702400`, `FORCE_SOURCE_DATE=1`, and `TZ=UTC`, then run
the following commands in a clean temporary directory containing the source
and bibliography:

    lualatex -interaction=nonstopmode -halt-on-error -jobname=paper '\pdfvariable suppressoptionalinfo 512\relax\input{manuscript.tex}'
    bibtex paper
    lualatex -interaction=nonstopmode -halt-on-error -jobname=paper '\pdfvariable suppressoptionalinfo 512\relax\input{manuscript.tex}'
    lualatex -interaction=nonstopmode -halt-on-error -jobname=paper '\pdfvariable suppressoptionalinfo 512\relax\input{manuscript.tex}'

The source uses TeX Gyre Termes for Latin and mathematics and Droid Sans
Fallback for the Chinese abstract. The working environment requires the
LuaLaTeX font loader.

## Finalization status

This is the Stage-5 final research manuscript with a validated continuous
two-round revision-evidence bundle.  It is not a venue-specific submission package.  The
six-item Round-1 roadmap was applied in one authorized 13-operation patch and
verified in Stage 3′ as 6/6 `FULLY_ADDRESSED`.  A separately hash-authorized
two-operation integrity correction then synchronized the title date and
finalized the materials-on-request policy.  Stage 4.5 was rerun from scratch:
3/3 references, 21/21 citation contexts, 16/16 consistency families, 37/74
sampled body paragraphs, and 49/49 registered claims through 63 replay-valid
evidence rows.  The exact result is `PASS` with
`SERIOUS=0 / MEDIUM=0 / MINOR=0`; the current 13-page PDF contains both
authorized corrections.
Liang Wang's byline, affiliation/contact email, contribution statement,
no-funding status, and no-competing-interests status were explicitly confirmed
by the human author.  The email is displayed as a contact address; no
corresponding-author designation was inferred.  The source-sensitive author
note remains explicitly UNSENT.  On 2026-08-26 the scholar entered Stage 5 and
locked the current `natbib[numbers,sort&compress] + plainnat` numeric profile.
The scholar supplied the separate in-stage content confirmation.  Two
independent builds produced byte-identical final PDF SHA
`e030259bb34c6d92af8fd53af80dce0e43200133c9bbdc91efb4f54e8f6c761a`;
its extracted text is identical to the confirmed content proof.  Citation,
font, build, and 13/13-page render checks pass.  Stage 5 is complete; Stage 6
has not been entered.  Submission, release, Git action, external contact, and
Route advancement remain unauthorized.

## Roadmap classification

The exact crosswalk is maintained in
[composition_blueprint.md](../notes/composition_blueprint.md). Paper 22 is a
pure algebraic obstruction result:

- Route A: NOT TESTABLE; no A0--A4 tuple; no advancement.
- Route B: invocation and entry are unauthorized; NOT TESTABLE; no B1--B5
  tuple is assigned.
- Gates A--E: not reached.

The sheaf-theoretic term “lift” is unrelated to Route-A quantization.
