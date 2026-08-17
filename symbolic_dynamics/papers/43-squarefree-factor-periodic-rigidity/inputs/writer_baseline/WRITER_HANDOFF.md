# Paper 43 writer handoff

## Status

`WRITER_DRAFT_DIAGNOSTIC_COMPILE_CLEAN`

This directory is a future writer scaffold only.  It contains no authority
publication, experiment implementation, evaluation, canonical result block,
result count, result hash, PDF, or auxiliary build file.  The frozen research
package and its independent DA report were read-only inputs and were not
modified.  A diagnostic PDF was built only in a clean out-of-tree copy and was
not installed here.

## Frozen research provenance

- Research package portable authority input:
  `preauthority/` (sealed by `preauthority/SHA256SUMS.txt`)
- Package manifest SHA-256:
  `f35b469d6a438d9a9e1f03e0682d85590b1010dd2acfe82b4f2ceef677d68d8f`
- Research lock SHA-256:
  `b8d05c2407e2d7b7a6b8c435cf7d757420f627b64f9d44e328443079b923adb0`
- Source lock SHA-256:
  `c46818edd12a488c70858b40c4caf82310ccdd2fda25186285f867a169b1ba08`
- Proof package SHA-256:
  `a8cf6b31aab739c85cd49f6eab5152471a16da0df31e423b18c2be84ecb9ffc3`
- Literature audit SHA-256:
  `f7dfa7f27d17ad1d66fb0a16997125ed2ffb22532afd281b2de3465bf5ae90e1`
- Route expectation SHA-256:
  `d4fc1f7bfcd7024929b6eec28679ed39d456dde4f3eeb77d79a5349885d6da7a`
- Final independent DA portable authority input:
  `independent_da/paper43_DA_REPORT.md`
- DA report SHA-256:
  `925c1490c3eab0b8fcb502f72f8da635a41aa19ad96433869cb6c2942fc61ed3`
- DA sidecar SHA-256:
  `4a8b32bcd58d9e45ebe757190062eca40286a5aae9aa6a84ec13a6af0f15e0ea`
- DA disposition: `DA_ACCEPT_PREAUTHORITY`

These are research-provenance hashes, not canonical experiment results.

## Scientific claim lock

The manuscript preserves the following exact scope:

1. The source is the two-sided all-rational-prime-square admissible shift.
2. The theorem quantifies over every continuous surjective equivariant map to
   an arbitrary compact metrizable Z-system whose action is a homeomorphism.
3. Every lawful factor has exactly one periodic point, the fixed image of the
   all-zero source point.
4. Every fixed count is one; the Artin--Mazur zeta is `1/(1-z)` and the
   inverse determinant is `1-z`.
5. The single primitive factor orbit and its traversals are not rational-prime
   atoms.
6. The finite-P0 sharpness proof has both branches: nonempty P0 uses the exact
   least-period-Q witness, while empty P0 uses two distinct fixed points.
7. Known squarefree/B-free proximality receives zero novelty credit.  The
   standalone novelty score remains `1/10`, with `2/10` only for internal
   typed closure.
8. The selector is retrospective; all outcomes and proof/literature facts
   were known.  It supplies no prospective, priority, ranking, novelty, or
   authorization evidence.
9. The Route tuple is exactly
   `(A0_FAIL, A1_FAIL, A2_ANALYTIC_DETERMINANT, A3_FAIL, A4_FAIL)`, the overall
   verdict is `ROUTE_A_REJECTED`, and Route B invocation is false.
10. `STOP_DUPLICATE` remains live if a primary source with the exact theorem
    and quantifiers is located.

## Writer file architecture

- `main.tex` is the only document root.
- `abstract.tex` is separate.
- `sections/` contains exactly seven numbered scientific sections.
- `appendices/` contains exactly two appendices.
- `figures/` contains exactly three pure TikZ figures; there are no raster
  assets or external figure scripts.
- `references.bib` contains six cited and metadata-checked records.
- `PAPER_PLAN.md` contains the claim/evidence map, page budget, citation map,
  and non-negotiable wording.
- `SHA256SUMS.txt` is sorted, unique, and self-excluding.

The repaired draft compiles to 15 A4 pages, within the subsequently approved
14--15-page diagnostic range.  It remains deliberately proof-heavy rather
than padded with generic background.

## Bibliography verification and caveats

The six entries were checked against the frozen literature audit and the
primary/institutional records linked there.

- Artin--Mazur: journal, volume, issue, pages, year, and DOI are complete.
- Sarnak: retained as a 2011 IAS institutional lecture-note record; no journal
  venue or invented pagination is supplied.  The IAS record spells the title
  with `Mobius`, which is preserved in BibTeX.
- El Abdalaoui--Lemańczyk--de la Rue: IMRN volume/year, issue, pages, DOI, and
  arXiv identifier are complete.
- Bartnicka--Kasjan--Kułaga-Przymus--Lemańczyk: journal, volume, pages, DOI,
  and arXiv identifier are complete; the frozen audit gives author initials,
  so the BibTeX does not invent unverified given names.
- Kasjan--Keller--Lemańczyk: title, IMRN year/issue/pages, DOI, and arXiv
  identifier are complete.
- Gundlach--Klüners: retained as arXiv:2407.08438, version 2, revised
  2 June 2025.  The frozen audit does not bind final journal volume/pages, so
  no such fields are inserted.

No general determinant reference was added: the only operator calculation is
the elementary one-dimensional identity `det(I-z[1])=1-z`, while the zeta
convention is cited directly to Artin--Mazur.

## Diagnostic compile and visual audit

The `paper-compile` workflow was run on a clean out-of-tree copy using
`pdflatex`, `bibtex`, and three final `pdflatex` passes.  The stable diagnostic
artifact is external to this writer draft.

- PDF SHA-256:
  `9336e894b18f0b9490c1bacd0f34467157f0d407b4cf0161156deafd7f1ac892`
- PDF size and format: 423,159 bytes; 15 A4 pages.
- Final log: zero errors, warnings, undefined citations/references,
  overfull boxes, underfull boxes, and rerun requests.
- Bibliography: six of six entries cited and resolved.
- Fonts: 26 of 26 PDF fonts embedded and subset.
- Text scan: zero `??`, `[?]`, `TODO`, `FIXME`, `VERIFY`, `PENDING`, or host
  path markers.
- Visual audit: all 15 pages inspected in a contact sheet; pages 7, 10,
  13--15 were additionally inspected at full resolution.  All three TikZ
  figures are legible, the repaired labels do not overlap boxes or arrows,
  the Route tuple remains within the text block, Appendix B.2 stays adjacent
  to its table, and the bibliography has no isolated final entry.

The compile also confirms that the earlier `Negative labelwidth`, float
placement, and figure underfull warnings are gone.  No diagnostic PDF or
auxiliary file is part of the writer seal.  A future authority task must still
perform its own clean build before installing any publication artifact.
