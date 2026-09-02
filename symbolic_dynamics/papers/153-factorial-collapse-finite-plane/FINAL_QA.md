# Final QA

Status: **ROUND-2 INTERNAL ACCEPT / HOLD_EXTERNAL**
Surviving severity: **0 Critical / 0 Major / 0 Minor**

Hostile Review A returned 0 Critical / 0 Major / 2 Minor, both closed in
Round 1.  Hostile Review B returned 0 Critical / 0 Major / 2 Minor: the
remaining `t=0` proof notation and the persistent microtype font-expansion
warning are both closed in Round 2.

## Manuscript and build

- Anonymous amsart, 10pt, A4, five pages.
- Four-step pdflatex/BibTeX build exits successfully.
- Settled main.log has zero Overfull boxes, zero Underfull boxes, zero
  undefined citations or references, and zero rerun warnings.
- Accepted current/Round-2 PDF: five pages, 392,821 bytes, SHA-256
  ef8c82be2935ed23c406a7c688138400d9c76924d11f9d5c089893e8747049a5.
- Two fresh source-only directories, each containing only `main.tex` and
  `references.bib`, completed the four-command build. Their PDFs were
  byte-identical to one another and to `main.pdf`.
- `main_round2.pdf` is byte-identical to `main.pdf`.
- Historical `main_round1.pdf` remains unchanged: five pages, 394,720 bytes,
  SHA-256
  81e56c67a1029add2bc93aaf67add40cbc68016a82e8eb2a1b7025cad2d3bb7a.
- `main_round0_original.pdf` remains unchanged at SHA-256
  8940cc2979406cd788e9a1c2ed23cb76422c50ff92fe99723608d0cfcb8dfd77.

## PDF and visual inspection

- Page size is A4; no clipping, collisions, orphaned headings, or misplaced
  floats were found in the five rendered pages.
- Title and author metadata fields are empty. CreationDate and ModDate are
  absent. The visible author is Anonymous.
- All fonts reported by pdffonts are embedded and subset.
- PDF text contains no workspace path, email address, affiliation, ORCID,
  acknowledgement, or corresponding-author marker.
- All five Round-2 pages were freshly rasterized and inspected. The indexed
  empty-set boundary in both statement and proof and all seven declaration
  paragraphs are legible; no
  clipping, collision, corrupt glyph, or displaced float was found.

## Mathematics and evidence

- The main theorem states the iterate, full labelled graph, temporal
  polynomial, every-target fibres, images, identifiability, fixed counts, and
  zeta.
- The proof dependency graph is in the paper body.
- The composite-ring counterexample and the owner/internal collision
  firewall are explicit.
- Cold-process replay gives 18,942,551 passing assertions.
- Fresh stdout is byte-identical to CANONICAL.txt.
- Fresh stdout is also byte-identical to verification_output.txt; transcript
  SHA-256 is
  fd900d9d0c1233a265834ce7efc25c43e2c9360a5cb3bbb5eaef4d125f67d6f9.
- The paper-local profile SHA is
  b44a7815c886a98409b5f56a0c26ce24f8644fa4f6b57a238d5a50d8a2d83810.

## Review-B closure

- The Corollary 3 proof now uses the same indexed root set
  `{-j: 0 <= j < t}` as its statement and says explicitly that it is empty
  at `t=0`; no interval-style empty-list ambiguity remains.
- Microtype font expansion is disabled while protrusion remains enabled.
  Fresh local and source-only logs contain no expansion-initialization
  warning and no other LaTeX/package warning.
- Neither repair changes the theorem ceiling, verifier, transcripts,
  bibliography, or historical Round-0/Round-1 PDFs.

## Artifact and policy checks

README, BUILD, PAPER_PLAN, NARRATIVE_REPORT, CLAIMS_EVIDENCE,
CONTROL_RESULTS, SOURCE_VERIFICATION, IMPROVEMENT_LOG, both raw internal
reviews, all three round freezes, references, verifier, canonical transcript,
and verification output are present.  Source and manuscript scans contain no
first-to language.  No external model review was run, by task instruction.
The package is accepted internally and scoped repository synchronization is
governed by the standing batch authorization; posting, circulation, author
contact, and submission remain unauthorized.
