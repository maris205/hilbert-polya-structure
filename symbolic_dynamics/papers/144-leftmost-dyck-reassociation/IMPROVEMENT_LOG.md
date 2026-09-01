# Improvement log — P144

**Date:** 2026-09-01 UTC
**Input:** `HOSTILE_REVIEW_A.md`
**Round-1 disposition:** every required owner/source and planning repair was
implemented before independent round-2 review.  External status remains
**HOLD_EXTERNAL**.

## Required-fix closure

### 1. Direct rotation and comb sources

Added and cited three verified primary records:

- Jean Marcel Pallo, “Rotational Tree Structures on Binary Trees and
  Triangulations,” *Acta Cybernetica* 17(4) (2006), 799--810.  The University
  of Szeged repository PDF was inspected at article pp. 802--803 for the unique
  leftmost left-rotation, rooted directed tree, grading, and distance.
- Jean Marcel Pallo, “Right-Arm Rotation Distance between Binary Trees,”
  *Information Processing Letters* 87(4) (2003), 173--177, DOI
  10.1016/S0020-0190(03)00283-7.  The official Elsevier record was verified;
  Chapoton's primary text supplies the explicit comb-order attribution.
- Frédéric Chapoton, “Some Properties of a New Partial Order on Dyck Paths,”
  *Algebraic Combinatorics* 3(2) (2020), 433--463, DOI 10.5802/alco.98.  The
  official Centre Mersenne PDF was inspected at Section 1.2, p. 438 for the
  statement that comb covers are precisely the Tamari covers whose moved
  subpath lies at height zero.

Stanley's *Catalan Numbers*, Theorem 1.5.1, was reverified from the official
Cambridge excerpt as the source for the standard Dyck-path/ordered-plane-tree
contour carrier.

### 2. Literal comparison completed

The manuscript and source ledger now compare all three move descriptions.

- Every nonfixed `Phi_n` edge is a height-zero comb/Tamari cover; `Phi_n`
  selects the one at the leftmost ground return.
- Pallo's 2006 deterministic leftmost map is genuinely different.  After its
  terminal root is fixed it has one fixed state, whereas `Phi_n` has
  `Cat_(n-1)` fixed states.  For `n>=3`, fixed-point count excludes equality or
  conjugacy, including mirror/reversal conjugacy.
- Pallo's 2003/Chapoton's comb relation is a cover family rather than a
  deterministic map; `Phi_n` is a selector within that family.

No literal ownership was inferred beyond what these comparisons establish.

### 3. Ordered-plane-tree conjugacy added

Under the contour bijection, primitive factors are the ordered subtrees at the
root children.  The update is now displayed as

```text
(T_1,T_2,T_3,...,T_k)
  -> (T_1 with T_2 appended as its rightmost child,T_3,...,T_k).
```

The text also identifies the inverse: over a terminal root with unique child
`S`, the depth-`d` source lifts the last `d` children of `S`, in order, to root
level.  Root degree minus one is the same clock as primitive-factor count minus
one.  The contour carrier, graft/lift operation, and root-degree clock are all
assigned zero standalone contribution credit.

### 4. Search ledger made reproducible

`SOURCE_VERIFICATION.md` now records repositories/databases, exact query
families, search date, bounds, inspected pages, supported roles, and separating
invariants.  The grafting/FCNS search non-hit is explicitly labelled a search
limitation, never novelty or priority evidence.

### 5. Residual shrunk and synchronized

The following now receive zero standalone credit throughout the manuscript and
supporting artifacts:

- deterministic leftmost rotation and scheduler structure;
- ground-level comb/Tamari covers;
- primitive decomposition and component/ballot census;
- contour plane-tree carrier, root-child graft, suffix lift, and root-degree
  clock;
- Catalan enumeration and generic coefficient extraction.

The only retained internal residual is the exact conjunction, for the specific
literal selector, of the all-time iterate formula with the target-indexed
statement that every feasible depth has one specified source.  The fibre
polynomial and extremal target are retained only as consequences.  This
residual is owner-unresolved and carries no novelty claim.

Synchronized files:

- `main.tex`
- `references.bib`
- `SOURCE_VERIFICATION.md`
- `CLAIMS_EVIDENCE.md`
- `NARRATIVE_REPORT.md`
- `PAPER_PLAN.md`
- `README.md`
- `BUILD.md`

`PAPER_PLAN.md` now targets 5--6 pages including references rather than 7--9.
The delivered round-1 manuscript has 6 pages.

## Round 2

An independent hostile reviewer accepted the owner-repaired theorem and
artifact package with zero critical, zero major, and one nonblocking minor.
The review reconstructed the full orbit, clock/layers, and every-target
depth-source theorem; rechecked the Pallo/Chapoton/Stanley subtraction; replayed
all 6,005,502 canonical assertions; reproduced the PDF from source only; and
inspected every historical/current page.

The sole minor was closed by restricting the abstract's component-indexed
iterate sentence to `0 <= t <= k-1` and explicitly stating that the endpoint
is fixed thereafter.  No theorem, proof, verifier, transcript, or ownership
boundary changed.  The rebuilt artifact is frozen as `main_round2.pdf`; status
remains **OWNER-THIN / HOLD_EXTERNAL**.

## Build and control closure

- Full `pdflatex -> bibtex -> pdflatex -> pdflatex` build: PASS.
- Final settled repeat build: byte-identical.
- Pages: 6; PDF size: 328,154 bytes.
- Bibliography: 7/7 entries cited and resolved.
- Undefined references/citations, bad boxes, or remaining warnings: 0.
- Fonts: all embedded; author/title metadata blank; volatile PDF metadata
  suppressed.
- Six-page visual inspection: PASS.
- Canonical verifier replay: byte-identical, 6,005,502 assertions,
  `STATUS=PASS`.

Artifact hashes:

```text
main_round0_original.pdf  f30d0145385d226ac66b75c280db956672f714d27e1e3c65169e37273c8baf26
round1 build (then main.pdf) 24a483f852b5c2fd29e5acf8ccc19aafe218928d7b5efb247a640444e1ef050c
main_round1.pdf           24a483f852b5c2fd29e5acf8ccc19aafe218928d7b5efb247a640444e1ef050c
```

The round-0 artifact was preserved unchanged.  This block records only the
round-1 remediation; round-2 closure is recorded below.
