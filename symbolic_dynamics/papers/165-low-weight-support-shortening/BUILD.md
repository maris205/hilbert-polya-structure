# P165 build and verification ledger

**Artifact:** `papers/165-low-weight-support-shortening`  
**Status:** `ROUND-2 ACCEPT_INTERNAL / 0C-0M-0m TWICE / HOLD_EXTERNAL`.

## Independent exact replay

The paper-local standard-library verifier was adapted from the accepted
scout into a self-contained author control.  It imports neither that scout
nor any other repository code, removes the killed poset candidate, adds
`F_4` and `F_5` boxes, checks every-source lower bounds and equality
structure, and adds theorem-statement boundary sentinels.

```text
command: PYTHONDONTWRITEBYTECODE=1 python3 code/verify.py
assertions: 605,733
status: PASS
canonical SHA-256: 0fc0aac73b62b039fb9e82918a141927b33fb2aecb8b1f28ae3940c1481590bd
verifier SHA-256: 391c47dd3be9931c4b525025722ade224bd3b583c75d5da8564f6b75f347bcaf
fresh byte-identical replays: 2/2
```

## Settled build

Toolchain: pdfTeX `3.141592653-2.6-1.40.22` and BibTeX `0.99d`.

```bash
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

The four retained logs are `build_pdflatex_1.log`, `build_bibtex.log`,
`build_pdflatex_2.log`, and `build_pdflatex_3.log`.  The settled final log
has zero LaTeX/package warnings, undefined references or citations, rerun
requests, overfull boxes, underfull boxes, and fatal errors.  BibTeX reports
three used entries and zero warnings.

Two further cold builds were run in separate fresh directories containing
only `main.tex` and `references.bib`.  Both completed the same four-command
sequence, settled without any listed warning or bad box, and produced PDFs
byte-identical to `main.pdf`.  Their final logs are retained as
`build_cold1_settled.log` and `build_cold2_settled.log`; those logs are also
byte-identical.

## Round-0 PDF freeze

```text
canonical PDF: main.pdf
frozen copy: main_round0_original.pdf
pages: 4
bytes: 288,837
page box: A4, 595.276 x 841.89 pt
PDF version: 1.5
PDF SHA-256: f974ff2a1f43f875c26f4ad754655801336fbb77ec317df69b0c5bdc2f144b5a
round-copy byte match: YES
font rows: 23
unembedded/unsubsetted/non-Unicode font rows: 0
encrypted: no
forms: none
JavaScript: no
```

Title, author, subject, keywords, creator, and producer metadata are empty.
Extracted text has an anonymous byline and running head, no personal or local
identifier, and a visible `HOLD_EXTERNAL` marker.  All four pages were
rendered at 144 dpi and inspected without clipping, collision, overflow, or
illegible elements.

## Frozen core hashes

```text
bf245d0d0e968edf921af76bae15a77fc8068c3e196b0e880f48ec2a4e3275e4  main.tex
4e91997ae671fcade364a1057c31a7751aef863850f87df52e6277628df4b2a1  references.bib
532ed8807a44f9f26f8ba6974b1f98862ba2cdb1e684aceaecca0113b4e035d8  PAPER_PLAN.md
92301f4905d2aae00e4f611eea389d1f731a1b2787c2013a85a78b712ec3c664  CLAIMS_EVIDENCE.md
73b6fedefb94a776f1ba32296808fce4c5e469f3375b90e6d7b4967dd0ce4140  NARRATIVE_REPORT.md
1072dce85c2737df411f66c40775d757a03b6978175be3c3ff0511295ea6107f  PROOF_PACKAGE.md
3acc19be4bc09b19fc49d11c23d7d4bd678ac0862a98d7313ff38b7d5206767e  SOURCE_VERIFICATION.md
391c47dd3be9931c4b525025722ade224bd3b583c75d5da8564f6b75f347bcaf  code/verify.py
0fc0aac73b62b039fb9e82918a141927b33fb2aecb8b1f28ae3940c1481590bd  code/CANONICAL.txt
f974ff2a1f43f875c26f4ad754655801336fbb77ec317df69b0c5bdc2f144b5a  main.pdf
f974ff2a1f43f875c26f4ad754655801336fbb77ec317df69b0c5bdc2f144b5a  main_round0_original.pdf
```

## Round 1 freeze

Hostile Review A returned `ACCEPT_INTERNAL` with
`0 Critical / 0 Major / 0 minor`; therefore the manuscript source and PDF
required no repair.

```text
current PDF: main.pdf
Round-1 copy: main_round1.pdf
pages: 4
bytes: 288,837
PDF SHA-256: f974ff2a1f43f875c26f4ad754655801336fbb77ec317df69b0c5bdc2f144b5a
Round-0/current/Round-1 byte match: YES
Review-A assertions: 1,574,098
Review-A verifier SHA-256: f6399e25007c147f78f83799f825c14fb19419b1ad4a0467ea17618ea592e27f
Review-A canonical SHA-256: 66de01f2399047e6a32d9b22d508be9eab56fd14b62b3e766991d0b28d5b25e7
Review-A fresh byte-identical replays: 2/2
```

The review independently enumerated 32,805 code states over `F_2`, `F_3`,
and a true `F_4` implementation, including 43,357 simultaneous-equality
sources.  Its two source-only cold builds matched the frozen PDF byte for
byte; all 23 fonts remained embedded, subsetted, and Unicode mapped, all
four pages passed visual/anonymity QA, and the settled warning/error count
was zero.  The artifact remained `HOLD_EXTERNAL`; the independent
Hostile Review B recorded below then completed the second gate.

## Round 2 freeze

Hostile Review B returned `ACCEPT_INTERNAL` with
`0 Critical / 0 Major / 0 minor`; therefore the manuscript source and PDF
again required no repair.

```text
current PDF: main.pdf
Round-2 copy: main_round2.pdf
pages: 4
bytes: 288,837
PDF SHA-256: f974ff2a1f43f875c26f4ad754655801336fbb77ec317df69b0c5bdc2f144b5a
Round-0/current/Round-1/Round-2 byte match: YES
Review-B assertions: 1,220,460
Review-B verifier SHA-256: 987e913be21a91d7f612bf158f14d84c0b597950e215a870c4d0405280685b54
Review-B canonical SHA-256: 3a593364f3a30a18bf76fe1611dad2a8330a57772cd466afd8d672cda238da04
Review-B fresh byte-identical replays: 2/2
```

The second reviewer independently enumerated 37,193 labelled codes and
215,030 target--time interfaces, replayed the author and Review-A controls,
and ran two source-only cold builds.  Both PDFs matched the canonical PDF;
all 23 fonts, all four pages, metadata, anonymity, references, warnings,
and the visible `HOLD_EXTERNAL` marker passed.
