# Five actual final-page views after raw terminal-pair equality

Root actually viewed pages1–5 from cold_build_1 at original resolution using
five distinct view_image calls, after all six actual native raw comparisons
passed: the two complete PDFs and every corresponding page PNG. Full actual
view requests and complete returned image data URLs are retained individually.
The displayed PNG bytes were then decoded and compared byte-for-byte with
the immutable corresponding source image. This is five actual views, not
ten: the byte-identical second PDF/render set reuses those same visual results.
It is not an inference from PNG existence or hashes alone.

The first auxiliary byte-binding check wrongly expected the data-URL MIME
image/png and failed before decoding the first image. The actual tool uses
application/octet-stream around the unchanged PNG bytes. That failure is
retained in VIEW_BINDING_NATIVE.json. The corrected check in
VIEW_BINDING_NATIVE02.json verifies that exact actual MIME, PNG signature
and whole decoded byte equality for all five images. It is metadata closure,
not a second set of views or a modification of the displayed images.

Both actual PDF files are301007 bytes, SHA256
532b8c462e907878c3d75829b2c4ff86de7d59c137efa91b61ebc80717a077dc.
Each has five actual recorded pages,21 embedded fonts and references on p5.

Page1: centered two-line title and ANONYMOUS label are legible. Abstract,
opening definitions and equations(1.1)–(1.2) fit; superscripts, subscripts,
ceilings and set symbols are present. Body and footer do not collide. The
last paragraph continues normally to p2; no clipped text or missing glyph
was visible at the inspected resolution.

Page2: the two-column established-ingredient/contribution table remains
within the margins with readable row/column alignment. Its wrapped static-
retraction entry has ordinary hyphenation, not overlap. Lemma2.1, equations
(2.1)–(2.2), proof and final paragraph are legible; QED and running header
are properly separated. No overflow, collision or missing symbol visible.

Page3: Lemma3.1 and Theorems3.2–3.3 are clearly distinguished; the two-case
entrance-time formula, ceiling clock, strict-pair lists and proof displays
fit. Equation labels, braces, math scripts and QED boxes are intact. The
sharpness proof continues to p4 normally; no clipped or colliding text seen.

Page4: the even-size proof completes clearly. Theorem4.1's three numbered
construction steps and the Laurent/binomial, product and gap-exclusion
formulas are legible. Dense sum limits remain separated from the binomial
and exponent. All displays and the lower proof block fit without visible
overlap or dropped glyphs.

Page5: inverse-count proof and Section5 are readable and complete. The
verification/runtime limitations and old failed-pilot boundary are visible.
All three references, including accented author names, arXiv/version data
and journal text, fit within the page; no unresolved placeholder, collision
or clipping is visible. The final page has a normal lower margin.

Visual decision: no visible page-level defect identified in these five actual
views. This does not prove every internal font-expansion setting operated as
intended. The actual lowercase pdfTeX font-expansion warning missed by the
original capital-Warning diagnostic matcher remains an explicit diagnostic-
census issue; the two underfull messages are also retained. No warning-free
claim, silent warning deletion, source repair or rebuild is made here.
The independent complete log/FLS/BibTeX/font/cold-artifact audit and root
diagnostic reconciliation remain required before terminal/paper acceptance.
OWNER_AMBER / HOLD_EXTERNAL; no science, manuscript review, Git or external
action is supplied by this visual record.
