# P202 Review A — new cold build and all-page visual QA

2026-09-05 UTC. An actual new cold build was executed by this reviewer in
qa/cold_source/. The directory was checked empty before copying only
the frozen main.tex and references.bib. No old .aux, .bbl, PDF, author
code or gate code was supplied. The exact script qa/cold_build.sh performs
pdfLaTeX, BibTeX, pdfLaTeX, pdfLaTeX with fail-fast handling. Every command
and the final cmp exited zero; all generated logs remain in that directory.
No rebuild was simulated by copying the author's PDF.

Result: the new PDF and frozen PDF are byte-identical, SHA-256
e1ca5021ff1ac74cff118d0d571fa0f3f74db32cc8b6ba5e7cd557fb69d88f8a.
Cold main.tex SHA is bcb24151784b52a27d846dd564ab6a0b438381e617575e6064c698f69683fa1a;
cold bibliography SHA is 56077d3271a58dc9ca3d22b4710c1790a52fbb242d1587da9a443b6455ad2fb0.

The final TeX log and BibTeX log contain no Warning, Overfull, Underfull,
undefined, Error or Citation match. First-pass citation warnings are normal
before BibTeX and are retained rather than misrepresented as a final issue.
Poppler reports four A4 pages, 312,997 bytes, PDF 1.5, no encryption,
JavaScript, forms, custom metadata or metadata stream. Author, title,
subject, keywords, creator and producer fields are empty. There are 25
embedded/subset/Unicode font entries, all Type 1 and none Type 3. Page text,
metadata and font listing are retained.

The four fresh 110-dpi page PNGs were opened with the image-view tool and
actually inspected, not merely created or sampled:

| Page | Actual visual observations |
|---|---|
| 1 | Anonymous title and abstract readable. Local rule (1), full inverse theorem, fibre cases and odd-target forms (3) fit; no clipped symbols. Standard amsart first-page abstract/title spacing is intentional. |
| 2 | Full inverse proof, run coordinates, all three run/parking equations and both clearance cases visible. The final equality example ends above the bottom margin; no omitted proof line or overlap. |
| 3 | Recurrent-language definitions, core/time theorem, all three sharp-witness words and matrix/count statement readable. Count proof begins at the foot and continues normally; no lost equation number or cropped matrix. |
| 4 | Count proof continuation, verification/provenance limitations, HOLD_EXTERNAL and all five references visible. DOI wraps are legible; no unresolved citations, blank final page or orphaned reference page. |

ARS pdf_read_preflight was actually run against the newly built PDF.
Its hashed sidecar is qa/pdf_read_preflight.json: verdict UNAVAILABLE
because pypdf is not installed. This is explicitly not a structural
preflight PASS. Independent Poppler parsing, byte comparison and actual
all-page viewing supply the QA evidence used here. No venue-specific
accessibility, PDF/A, submission-format or blind-review policy compliance
is claimed beyond the project's anonymous short-amsart convention.

No source or visual repair was needed. All frozen author artifacts remain
untouched. Nested QA files have their own complete nonself manifest;
the top review manifest covers top-level review files, not a misleading
partial sampling of nested artifacts.
