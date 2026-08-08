# HCS-C21 two-round manuscript review

**Review date:** 2026-08-08
**Protocol:** independent mathematical, citation, and publication-readiness
passes; reviewers made no file edits

## Round 1: REVISE

The first manuscript pass found no counterexample to the central theorem,
but it did identify release-blocking proof, attribution, and typesetting
issues:

1. five missing TeX backslashes printed literal `qquad` in central formulas;
2. the base-changed splitting field was not named before the geometric
   Galois group was written;
3. the sheet involution needed an explicit splitting-field construction;
4. cross-sheet distinctness needed the exact resultant
   \(\operatorname{Res}_X(f_\eta,f_{-\eta})=8\eta^3\);
5. certificate threshold keys were broader than the declared component
   scope;
6. the Hénon 1969 DOI was wrong, Paper 5 lacked a rendered stable link, and
   several prior-work locators were absent;
7. the Traditional-Chinese locale, PDF metadata, fresh-clone commands, table
   captions, and source/PDF freshness needed repair; and
8. the checked-in PDF predated several source fixes.

All eight issue groups were closed.  The producer and independent checker
were strengthened rather than merely reworded: the resultant is now a
certificate field, three independent checks bind it, and a new mutation test
fails closed when it is altered.

## Round 2: acceptance gate

The mathematical reviewer returned **ACCEPT** with no blocking or major
issue.  The publication-readiness reviewer also returned **ACCEPT** and
verified the bilingual rendering, embedded fonts, tables, quotient diamond,
metadata, source freshness, and release instructions.

The citation reviewer initially returned **REVISE** because three internal
theorem locators used section-style numbering and because the future
`hcs-c21-v1` data URL could not resolve before release.  The numbering dispute
was settled by inspecting the compiled HCS-C19 and HCS-C20 PDFs directly:
their theorem counters are global.  The locators were corrected to HCS-C19
Prop. 1, Thm. 2, Cor. 3 and HCS-C20 Thms. 1 and 3.  The tagged data URL is
closed by the release procedure at the provenance commit.

## Final review verdict

**ACCEPT FOR REPOSITORY RELEASE**, subject only to executing the recorded
source-commit/provenance-commit/tag/push sequence.

The final accepted claim boundary remains:

- exact theorem for the twelve-state ordered cover of the unique period-six
  chiral doublet;
- existential comparison with one adopted HCS-C20 period-seven component;
- period-one explanation of the coarse quadratic marker coincidence;
- no full exact-period classification, multivalued-correspondence
  obstruction, determinant, Riemann divisor, or Hilbert--Pólya operator.

## Accepted verification ledger

- producer certificate SHA-256:
  `5386c95cbc65e6a4323cfcf230de6b41f353be909d197818f9c4fbf0a75a96fc`;
- independent report SHA-256:
  `0f14332f36f2f7df0ab238954c5a8531bcb9d759f8feeac60bc7bcc197452985`;
- independent checker: `PASS`, 133 named checks;
- test suite: 14/14 PASS, including 10 fail-closed mutations;
- artifact hash ledger: PASS;
- final manuscript: 17 pages, SHA-256
  `984ad0bc7cd0fe8840ce6a6f442dd377f930127e28836137ca814a2dd30847e1`;
- PDF defects: zero undefined citations/references, missing glyphs, or
  overfull boxes; all fonts embedded.

The 18 bibliography underfull notices caused by immutable long URLs are
cosmetic, visually inspected, and recorded in `COMPILE_REPORT.md`.
