# Consolidated hostile review — P124 round 2

Status: **ROUND2 GO_INTERNAL / EXTERNAL HOLD**.

## Consolidated decision

The internal mathematical, computational, and artifact gate is **GO**.
There is no internal STOP condition.  Public posting, submission, novelty or
priority language, and external release remain **HOLD** pending a separate,
dated direct-owner search.

| Review stage | CRITICAL | MAJOR | MINOR | Decision |
|---|---:|---:|---:|---|
| Hostile Review A | 0 | 0 | 2 | GO_INTERNAL after two support repairs; external HOLD |
| Hostile Review B | 0 | 0 | 0 | GO_INTERNAL; external HOLD |
| Round-2 open findings | **0** | **0** | **0** | **GO_INTERNAL / EXTERNAL HOLD** |

Review A's two findings are closed:

1. the sharp square/non-square depth claim now points to Theorem 3.2, and the
   layer identity plus terminal ballot formula point to Theorem 5.1;
2. CONTROL_RESULTS.md and NARRATIVE_REPORT.md now state the explicit P107/P104
   internal collision firewall.

## Mathematical disposition

Review B independently checked the literal quotient-ring colon rule,
staircase update, sourced diagonal decomposition, path lemma, recurrent
classification, sharp entrance depths, first-trace basin theorem including
phase, four-mask contact transfer, reflection formulas, and complexity
claim.  The audit covered the strip, square, nonsquare, `m=1`, `m=2`,
`r=1`, `r=m-1`, `r=m`, zero ideal, unit ideal, endpoint-source, and
transposition boundaries.  It found no counterexample, missing case, phase
offset, or off-by-one error.

The retained claim ceiling is narrow: credit may attach only to the exact
cross-colon scheduler's local rule, recurrent family, sharp depths,
first-trace basin partition, phase, and contact-transfer enumeration.
Monomial staircases, colon arithmetic, OR-path dynamics, generic basin
language, ballot/reflection, rowmotion/toggle vocabulary, and finite-state
dynamic programming receive zero contribution credit.

## Computational disposition

The two paper-local programs are implementation-independent: the basin lane
does not import the core lane and reimplements literal quotient arithmetic.
Fresh round-2 executions reproduce the canonical transcripts byte-for-byte.

| Lane | Assertions | Canonical SHA-256 | Result |
|---|---:|---|---|
| core dynamics | 1,469,669 | `b924e05c5e9ac71a25fb668d5bc2033f6ab58c325c7c73642a4dd0b096d67deb` | PASS, byte-identical |
| basins/transfer | 265,987 | `bdfd3e041b9f641101436c40918adbba59fd14b1f1381d77fa943ce00c0c76ff` | PASS, byte-identical |
| **combined** | **1,735,656** | — | **PASS** |

These finite checks are falsification controls and do not replace the
all-parameter proofs or establish ownership.

## Build and PDF disposition

A fresh isolated directory containing only `main.tex` and `references.bib`
completed pdflatex, bibtex, pdflatex, pdflatex with no effective warnings,
undefined citations/references, box warnings, rerun request, or error.  Its
PDF is byte-identical to the frozen artifact:

- 5 A4 pages;
- 293,617 bytes;
- SHA-256
  `3dd3316a0abbc504a65c6214bc52d4a439a4e16f8290ca655b7fcece2b501f81`;
- 9/9 bibliography entries resolved;
- 23/23 font rows embedded, subsetted, and Unicode-mapped;
- blank Author, Title, Subject, and Keywords metadata;
- no metadata stream, custom metadata, embedded files, forms, JavaScript,
  encryption, or signatures;
- all five rendered pages visually clean and anonymous.

`main_round0_original.pdf`, `main_round1.pdf`, `main.pdf`, and
`main_round2.pdf` are byte-for-byte identical.

## Internal-project firewall

P107's map is `I -> Ann(I)^r` on ideals of `Z/NZ` and is governed by CRT
valuations and clipped reflection.  P104 is a random `2 x 2` contraction
cocycle.  Neither supplies P124's truncated bivariate monomial-ideal carrier,
crossed colons, sourced OR diagonals, checker basins, or four-state contact
transfer.  Their generic vocabulary receives zero credit.

## External hold

The bounded direct-owner search found no exact owner of the literal operator
and theorem package, but a non-hit is not a novelty certificate.  Search
coverage, alternate terminology, unpublished work, and later publications
remain uncontrolled.  The external HOLD is therefore mandatory and is not an
internal correctness defect.

## Final gate

- **Internal correctness:** GO.
- **Proof and boundary coverage:** GO.
- **Canonical controls:** GO.
- **Build, PDF, fonts, references, metadata, and anonymity:** GO.
- **Review-A repair closure:** GO.
- **Open internal findings:** 0.
- **External novelty/priority clearance:** HOLD.

**Final consolidated decision: ROUND2 GO_INTERNAL / EXTERNAL HOLD.**
