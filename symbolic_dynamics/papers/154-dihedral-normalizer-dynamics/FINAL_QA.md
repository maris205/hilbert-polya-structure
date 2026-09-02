# Final QA

Status: **ROUND-2 INTERNAL ACCEPT / HOLD_EXTERNAL**

Hostile Review A: 0 Critical / 0 Major / 3 Minor, all closed in Round 1.
Hostile Review B: `ACCEPT_INTERNAL`, 0 Critical / 0 Major / 0 Minor.
Review B requested no mathematical repair. A subsequent independent final
cold-QA found a latent pdfTeX font-expansion warning; Round 2 closes it with a
build-only preamble change (`microtype` expansion disabled, protrusion
retained). No theorem, proof, bibliography, verifier, or transcript changed.

## Manuscript and build

- Anonymous amsart, 10pt, A4, five pages.
- The settled five-command pdflatex/BibTeX build exits successfully.
- Settled main.log has zero Overfull boxes, zero Underfull boxes, zero
  undefined citations or references, and zero rerun warnings.
- Current and Round-2 PDFs: byte-identical, five pages, 373,090 bytes,
  SHA-256
  72b99fe5f4813434cccb3aef9f8a023d0e7ca471029ce9831b4228dfe8db90cd.
- Round-1 remains preserved as a distinct five-page, 375,182-byte artifact at
  SHA-256
  aafab23ed519a68e3d03df44999aa8dc525db0f3e2a860abb67825e556fd839b.
- Two fresh source-only directories, each containing only `main.tex` and
  `references.bib`, completed the five-command build. Their PDFs were
  byte-identical to one another and to `main.pdf`; the final logs had no
  cross-reference rerun request.
- `main_round2.pdf` is byte-identical to `main.pdf`; `main_round1.pdf`
  preserves the pre-fix Review-A/Review-B artifact.
- `main_round0_original.pdf` remains unchanged at SHA-256
  45901bc68e404cd387c48c848b87ce98d24ead5d60c9ec52b7d584fcb34e60f3.

## PDF and visual inspection

- Page size is A4; no clipping, collisions, orphaned headings, or misplaced
  floats were found in the five rendered pages.
- Title and author metadata fields are empty. CreationDate and ModDate are
  absent. The visible author is Anonymous.
- All 26 fonts reported by pdffonts are embedded, subsetted, and Unicode
  mapped.
- PDF text contains no workspace path, email address, affiliation, ORCID,
  acknowledgement, or corresponding-author marker.
- All five final Round-2 pages were freshly rerasterized and inspected after
  the build-only microtype repair.  The added quantifier lines and the full
  bibliography are legible; no clipping, collision, corrupt glyph, or
  displaced float was found.

## Mathematics and evidence

- The main theorem states the owned bridge, full iterated forest, depth
  polynomial, all-time images, every-target fibres, exact graph signature,
  and the 33/35 collision with all power-of-two lifts.
- The repaired tau recovery uses the total-vertex remainder and covers the
  one-root case.
- The proof dependency graph, 15/23 sharpness example, owner subtraction, and
  internal collision firewall are in the paper body.
- Cold-process replay gives 29,590 passing assertions.
- Fresh stdout is byte-identical to CANONICAL.txt.
- Fresh stdout is also byte-identical to verification_output.txt; transcript
  SHA-256 is
  25ab2e157715ddce077402e8f9383a7d52c261401d6579035eb43e8e945e9219.
- The paper-local profile SHA is
  6eed12ce0c63f2d20f734ac1fa67634ce445140372dfc53e779a389de023b782.

## Artifact and policy checks

README, BUILD, PAPER_PLAN, NARRATIVE_REPORT, CLAIMS_EVIDENCE,
CONTROL_RESULTS, SOURCE_VERIFICATION, IMPROVEMENT_LOG, both review-round
freezes, the Round-2 freeze, references, verifier, canonical transcript, and
verification output are present. The article-printed `Hader Baqer Shelash`
citation and its
`Hayder`/`Ameen` variants are explicitly reconciled in the source ledger.
Source and manuscript scans contain no first-to language. No external model
review was run, by task instruction. Internal Review B accepted the complete
package with zero findings. The post-review build-only warning was then closed
in Round 2, whose five-command log has zero warnings and bad boxes. The
external state remains `HOLD_EXTERNAL`; this acceptance does not authorize
posting, circulation, specialist contact, submission, novelty, or priority
claims.
