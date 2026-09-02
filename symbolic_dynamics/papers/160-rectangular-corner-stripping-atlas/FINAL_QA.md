# Final cold QA — P160 rectangular-corner stripping atlas

**QA date:** 2026-09-02 UTC  
**Role:** independent artifact-level cold QA after Review B  
**Disposition:** PASS / ACCEPT_INTERNAL / HOLD_EXTERNAL  
**Findings:** 0 Critical / 0 Major / 0 Minor

This pass treated main_round2.pdf as the frozen canonical object. I was the
Review-A reader but did not participate in either author repair pass. I did not
edit main.tex, references.bib, any PDF, verifier, review artifact, ledger, or
build log. The only repository writes made by this pass are FINAL_QA.md and the
regenerated SHA256SUMS. No Git operation or external release action was taken.

## 1. Frozen PDF invariant

The final current PDF and Round-2 freeze are byte-identical:

| Artifact | Pages | Bytes | SHA-256 |
|---|---:|---:|---|
| main.pdf | 4 | 316,629 | ce59fbfca3f50ee917089175817885fc5630b807483b7a16a5d291c69292e352 |
| main_round2.pdf | 4 | 316,629 | ce59fbfca3f50ee917089175817885fc5630b807483b7a16a5d291c69292e352 |
| main_round1.pdf | 4 | 294,530 | 3bbbb6f3243171d612f86a17cd88b58f56bc5ec80c3533dc30464343931def03 |
| main_round0_original.pdf | 4 | 295,886 | 2be90261ae3b636aa8db684597896f7e7d549363879936b3f6539877577f7d08 |

Round 0 and Round 1 therefore remain present under their recorded names, sizes,
and complete hashes. Neither historical PDF equals the current Round-2 object,
as expected.

The layout-preserving text diff between main_round1.pdf and main_round2.pdf has
exactly one added content line:

    This artifact remains HOLD_EXTERNAL.

No theorem, proof, formula, coefficient, source subtraction, citation, or
bibliography text changes between those two frozen PDFs. The sole
post-Review-B source change is therefore the requested visible lifecycle
sentence.

## 2. Exact-verifier replay

All replays were fresh processes writing only to a newly created temporary
directory.

### 2.1 Author verifier

Program: verify_p160.py

- script SHA-256:
  efa26a5b27158dd803636a40d1f8a6cbfc95deadab93264f1c3248989faab6fa
- frozen transcript SHA-256:
  3e1b83ff586795fc80fc01882d545fff270f9106471145b39c0f0ca51bd3a778
- exact assertions per run: 3,462,895
- fresh runs: 2/2 PASS
- run 1 versus verification_output.txt: byte-identical
- run 2 versus verification_output.txt: byte-identical
- run 1 versus run 2: byte-identical

Both fresh outputs have SHA-256
3e1b83ff586795fc80fc01882d545fff270f9106471145b39c0f0ca51bd3a778.

### 2.2 Independent Review-A verifier

Program:
docs/papers157_161_sequence/reviews/p160_rcs_a/verify_p160_rcs_review_a.py

- script SHA-256:
  b886846853762cf13c755f7569f465bd6a5eab23d61765e0c687266c77569a49
- canonical transcript SHA-256:
  971bcfccf205a590d08246f7266b73f38d088bfc79c571e92b209a936359ef9f
- exact assertions per run: 7,332,616
- fresh runs: 2/2 PASS
- each run versus CANONICAL.txt: byte-identical
- run 1 versus run 2: byte-identical

Both fresh outputs have SHA-256
971bcfccf205a590d08246f7266b73f38d088bfc79c571e92b209a936359ef9f.

This verifier imports no author code and uses a literal Ferrers-cell crop.

### 2.3 Independent Review-B verifier

Program:
docs/papers157_161_sequence/reviews/p160_rcs_b/verify_p160_review_b.py

- script SHA-256:
  589a737b8371e46aba51caabbb431fb00b4ab9531fc4bd48805eb2cc62adeea9
- frozen run SHA-256:
  b6034231aa620d0de80a56bfcda69f8ddfe047e343498896426699252b918b8a
- exact assertions per run: 11,287,366
- fresh runs: 2/2 PASS
- each run versus VERIFIER_RUN_1.txt: byte-identical
- VERIFIER_RUN_1.txt versus VERIFIER_RUN_2.txt: byte-identical
- fresh run 1 versus fresh run 2: byte-identical

Both fresh outputs have SHA-256
b6034231aa620d0de80a56bfcda69f8ddfe047e343498896426699252b918b8a.

The three verifier implementations and transcripts remain distinct evidence
lanes. Their finite agreement is falsification pressure, not a replacement for
the symbolic proof or source subtraction.

## 3. Two source-only cold builds

Two new temporary build directories were independently populated with only:

- main.tex
- references.bib

Each directory ran the complete settled sequence:

    pdflatex -interaction=nonstopmode -halt-on-error main.tex
    bibtex main
    pdflatex -interaction=nonstopmode -halt-on-error main.tex
    pdflatex -interaction=nonstopmode -halt-on-error main.tex

Results:

| Check | Build 1 | Build 2 |
|---|---|---|
| completed all four commands | PASS | PASS |
| PDF SHA-256 | ce59fbfca3f50ee917089175817885fc5630b807483b7a16a5d291c69292e352 | ce59fbfca3f50ee917089175817885fc5630b807483b7a16a5d291c69292e352 |
| equals main_round2.pdf byte-for-byte | YES | YES |
| equals the other cold build byte-for-byte | YES | YES |
| final-pass warnings/errors | 0 | 0 |
| BibTeX diagnostics | 0 | 0 |

The two final pdflatex logs are byte-identical, with SHA-256
7d9368728ced1a60e52dc1697c06f536c042f80d7b0fb06daefb0422046ed209.
The two BibTeX logs are byte-identical, with SHA-256
7b0a0a8d2f1749b44546479273ee9d474d9656cc2a276630ff83cc8a72044dc9.

The settled-log scan found no real LaTeX or package warning, undefined
reference, undefined citation, rerun request, overfull box, underfull box, TeX
error, emergency stop, or fatal error. Bootstrap-pass unresolved references
were not counted as final diagnostics and are absent from the settled pass.

## 4. PDF, fonts, references, and anonymity

pdfinfo reports:

- PDF 1.5;
- 4 pages;
- A4 media box, 595.276 by 841.89 points;
- 316,629 bytes;
- no encryption;
- no forms;
- no JavaScript;
- no suspect flag;
- blank Title, Author, Subject, and Keywords;
- no custom metadata or metadata stream.

pdfdetach reports zero embedded files, and pdfimages reports no embedded raster
or vector images.

pdffonts reports **23 font rows**. Every row is embedded, subsetted, and
Unicode-mapped. The twenty-third row is the subsetted Latin Modern monospaced
face used by the visible HOLD_EXTERNAL lifecycle token.

The bibliography contains exactly five entries, main.bbl contains exactly five
resolved items, and the auxiliary citation keys cover all five:

1. Andrews (1971);
2. Andrews–Eriksson (2004);
3. Barnes–Savage (1995);
4. Chen–Ji–Zang (2015);
5. Gordon–Houten (1968).

There is no unresolved citation marker. Source and extracted-PDF scans found no
TODO, FIXME, XXX, VERIFY marker, question-mark reference, email, ORCID,
affiliation, personal acknowledgement, funding statement, username, or machine
path. The visible byline is ANONYMOUS. Names in the bibliography are expected
source metadata and do not compromise manuscript anonymity.

The source contains one lifecycle occurrence written as HOLD\_EXTERNAL; the
rendered PDF contains one visibly extractable HOLD_EXTERNAL occurrence.

## 5. 144 dpi visual inspection

All four pages of main_round2.pdf were rasterized at exactly 144 dpi to fresh
1191 by 1684 pixel PNGs and inspected individually.

- Page 1: title, anonymous byline, abstract, source discussion, equations
  (1)–(4), and the transition into Section 2 are legible and unclipped.
- Page 2: the four-row source-subtraction table, Theorem 1, its proof, and the
  opening of Theorem 2 are aligned, readable, and within the page boundary.
- Page 3: the full target-fibre proof, repaired \(\gamma=(d)\) witness,
  coefficient formula, worked fibre, image size, and mass identity render
  correctly.
- Page 4: conjugation, three-probe recovery, control statement, visible
  HOLD_EXTERNAL sentence, and all five references are clean and readable.

No page has clipping, overlap, margin excursion, malformed glyph, broken rule,
or orphaned display. The reference DOI line wraps are readable. The modest
lower-page whitespace after the bibliography is harmless.

## 6. Manifest closure

The final SHA256SUMS is regenerated after this report and excludes itself. It
covers every other paper-local regular file, including FINAL_QA.md, all three
frozen PDFs, author source, auxiliary files, build logs, both hostile reviews,
the improvement record, and executable evidence.

- manifest entries: **42**
- duplicate paths: 0
- missing paths: 0
- untracked paper-local regular files outside the manifest: 0
- sha256sum -c result: **42/42 OK**

## Final disposition

All final artifact invariants pass:

- main.pdf equals main_round2.pdf byte-for-byte;
- Round 0 and Round 1 retain their exact historical hashes;
- the only Round-1-to-Round-2 text addition is the visible HOLD_EXTERNAL
  lifecycle sentence;
- six fresh independent verifier runs match their frozen outputs;
- two source-only builds reproduce the canonical PDF byte-for-byte;
- settled logs, metadata, fonts, references, anonymity, and all four rendered
  pages pass;
- the complete paper-local manifest verifies.

**FINAL QA: PASS / ACCEPT_INTERNAL / HOLD_EXTERNAL.**

This internal artifact acceptance does not authorize novelty or priority
claims, posting, circulation, submission, author contact, specialist contact,
or any other external action.
