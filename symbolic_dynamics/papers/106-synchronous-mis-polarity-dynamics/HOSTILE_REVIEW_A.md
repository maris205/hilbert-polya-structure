# Cross-hostile review A — P106

Date: 2026-08-29 UTC.  Reviewer role: independent of the P106 author.

Verdict: **internal GO after repairs / external HOLD**.  There is no
mathematical CRITICAL finding.  The cubic identity, closed-set census,
bipartite square law, path recurrence, and zeta formulas survive independent
reconstruction.  Two owner/citation defects, one visible typesetting defect,
and one non-evidentiary control loop were repaired before this A freeze.

## Scope and method

The review reconstructed the map from the open-neighborhood definition and
checked the theorem in three independent coordinate systems:

1. the symmetric antitone polarity on `2^V`;
2. the two one-sided Galois closures of a bipartition; and
3. literal Boolean-state orbits for empty, isolated, path, complete, and
   general small graphs.

It also verified every DOI against its publisher/Crossref metadata, searched
for a direct owner of the path recurrence, inspected the verifier for dead or
circular lanes, replayed its stored output, and rendered every PDF page.

## Hostile findings and repairs

### CRITICAL

None.

### MAJOR 1 — wrong conjunctive-network bibliographic identity

The former entry `Richard2018` gave Adrien Richard and Lilian Salinas,
*JCSS* 95 (2018), 44--66, DOI
`10.1016/j.jcss.2018.01.003`.  That DOI actually resolves to
*k-distinct in- and out-branchings in digraphs* by Gutin, Reidl, and
Wahlstr\"om, pages 86--97.  It did not support the owner-subtraction sentence.

**Repair.**  The citation is now the actual direct record:
Julio Aracena, Adrien Richard, and Lilian Salinas,
*Fixed Points in Conjunctive Networks and Maximal Independent Sets in Graph
Contractions*, *Journal of Computer and System Sciences* 88 (2017),
145--163, DOI `10.1016/j.jcss.2017.03.016`.  The key in `main.tex` and the
owner paragraph in `CLAIMS_EVIDENCE.md` were updated.  This was a source
integrity MAJOR, not a defect in the polarity proof.

### MAJOR 2 — direct path owner missing from the initial source boundary

The initial draft correctly said the maximal-independent-set path recurrence
was not claimed in isolation, but supplied no direct path-counting owner.

**Repair.**  The path section now explicitly calls the Padovan recurrence
classical and cites Euler--Oleksik--Skupie\'n,
*Counting Maximal Distance-Independent Sets in Grid Graphs*,
*Discussiones Mathematicae Graph Theory* 33 (2013), 531--557,
DOI `10.7151/dmgt.1707`, Remark 2.2.  The short proof remains only to fix the
empty-path convention and feed the dynamical zeta specialization.

### MINOR 1 — visible path-formula typo

The initial source contained the literal token `qquad` twice in the initial
values display.  LaTeX treated it as mathematical letters rather than
spacing.

**Repair.**  Both tokens are now `\qquad`.  The repaired formula renders as
`m_0=m_1=1, m_2=2, m_n=m_(n-2)+m_(n-3)` with the intended spacing.

### MINOR 2 — dead verifier loop

The initial path lane recomputed six iterates inside the first state loop,
assigned an unused `expected_fixed`, and made no assertion.  A later,
separately coded loop already performs and asserts every odd/even fixed-count
comparison.

**Repair.**  The no-assertion loop was removed.  The registered assertion
count remains exactly **6,462,317**, and fresh stdout is byte-identical to the
stored output.  No theorem coverage or asserted lane was removed.

## Formula-by-formula reconstruction

- Antitonicity and symmetry give `A subset F^2(A)`; applying antitonicity and
  extensivity again gives both inclusions in `F^3(A)=F(A)`.  The undirected
  hypothesis and use of open neighborhoods are explicit.
- `F^3=F` implies `im(F)=Fix(F^2)`, preperiod at most one, and periods only one
  or two.  A fixed support is independent and dominating, hence maximal
  independent, with the converse immediate.
- Odd iterates equal `F` and even positive iterates equal `F^2`.  The fixed
  sequence therefore alternates `m(G),c(G)`, and the involution on closed
  configurations gives `(c-m)/2` two-cycles and the stated zeta factors.
- For `V=X union Y`, the update splits as
  `(P,Q)->(beta(Q),alpha(P))`.  Full closed configurations are the Cartesian
  product of the two one-sided closure systems.  `alpha` and `beta` are
  inverse anti-isomorphisms on their closed elements, whose common size is
  exactly the number of fixed pairs.  Thus `c(G)=m(G)^2`, including empty
  sides and isolated vertices.
- The two first-vertex cases on a path give `m_(n-2)` and `m_(n-3)` with
  bases `m_0=m_1=1,m_2=2`; the displayed generating function follows.

## Reproducibility and PDF gate

- Fresh stable-tree exact control: **PASS**, 6,462,317 assertions.
- Stored stdout comparison: byte-for-byte **PASS**.
- Coverage: all simple graphs through six vertices, all bipartite graphs
  through `3+3`, every path state through 17 vertices, plus `K_2/K_3`
  sentinels.
- Four stages: **PASS** (`pdflatex`, `bibtex`, `pdflatex`, `pdflatex`).
- PDF: 4 A4 pages, 299,003 bytes, PDF 1.5.
- Final log: zero undefined citations/references, package warnings,
  multiply-defined labels, or over/underfull boxes.
- Fonts: 23/23 embedded, subsetted, and Unicode-mapped.
- Extracted text contains no `??`, `[?]`, TODO, FIXME, XXX, VERIFY, or stray
  `qquad` token.
- All four rendered pages visually inspected: **PASS**.

## Residual risk

The cubic law and one-sided closure anti-isomorphism are classical polarity
mechanisms and receive no novelty credit.  The residual object is only their
explicit synchronous finite-dynamical/zeta packaging.  A bounded search is
not an exhaustive owner certificate; external release, submission, contact,
novelty, and priority claims remain **HOLD**.
