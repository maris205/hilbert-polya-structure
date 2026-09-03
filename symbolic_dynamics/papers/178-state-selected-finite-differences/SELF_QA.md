# P178 author Round-2 self-QA

**Decision:** `ROUND2_DUAL_REVIEW_FREEZE / OWNER_THIN`  
**External state:** `HOLD_EXTERNAL`  
**Hostile review:** two process-separated passes; zero open findings

## Mathematical claim audit

- [x] The carrier is all functions
  \(\mathbb F_p\to\mathbb F_p\), with \(p\) prime; no prime-power
  extension is silently claimed.
- [x] The literal update evaluates the current state at zero before choosing
  the translation direction.
- [x] The binomial functions form a basis and Pascal's identity is applied
  over the whole cyclic prime field, including the wrap at \(p-1\).
- [x] \(J^i\) has dimension \(p-i\), and the constant kernel belongs to
  every \(J^i\) used in the inverse induction.
- [x] For \(a\ne0\), the factor \(U_a(N)\) has nonzero constant coefficient,
  is invertible, preserves each flag layer, and leaves the kernel line
  invariant.
- [x] The anchored-lift lemma states both surjectivity and uniqueness.
  Evaluation at zero is nonzero on the constant kernel, so no hidden factor
  of \(p\) remains.
- [x] Every history ending at a nonzero target has only nonzero selected
  directions; its direction word is recoverable from the forward orbit.
- [x] The zero fibre is obtained after counting every nonzero target in
  \(J^t\), and the formula includes the \(t=p\) boundary.
- [x] The sharp witness selects direction one at each of its \(p\) updates.
- [x] Depth \(d\) is the difference of two proved cumulative zero fibres;
  both \(d=1\) and \(d=p\) satisfy the displayed formula.
- [x] The functional graph has one recurrent root because \(T^p=0\), and
  the immediate indegrees distinguish zero, nonzero \(J^1\), and targets
  outside \(J^1\).
- [x] The deterministic operator convention \(Pe_f=e_{T(f)}\) is fixed
  before ranks are used.
- [x] \(E=P^p\) is a commuting rank-one idempotent, and
  \(P^t(\ker E)=\operatorname{im}P^t\cap\ker E\) is justified rather than
  assumed.
- [x] The nilpotent ranks are \(p^{p-t}-1\); their second differences give
  the stated blocks and exactly \(p-1\) top \(J_p(0)\) blocks.
- [x] The \(p=2\) image sizes, depths, and Jordan blocks are stated
  explicitly.

## Exact-verification audit

- [x] `verify_p178.py` uses only the Python standard library and imports no
  scout or historical verifier.
- [x] Literal states are tuples of function values, an organization separate
  from the lane's integer encoding but still author-side.
- [x] Every source, every target, and every time is checked for
  \(p=2,3,5\).
- [x] Each nonzero target/direction-word pair is checked for one anchored
  source.
- [x] Direct depth, immediate indegree, zero fibre, sharp witness, image
  layer, and Jordan-rank identities are all checked.
- [x] The separate matrix pass verifies the binomial ladder, all flag ranks,
  every nonzero direction rank, and every anchor-augmented rank through
  \(p=19\).
- [x] Two fresh outputs are byte-identical: 44,689 assertions, 3,156 literal
  arrows, stable edge digest, and `RESULT=PASS`.
- [x] The manuscript labels finite checks as falsification evidence, not
  proof.

## Ownership and citation audit

- [x] Aichinger–Moosbauer receives credit for translation differences,
  augmentation powers, and functional-degree nilpotence.
- [x] Hernández Toledo receives credit for fixed linear finite dynamical
  systems and their nilpotent/bijective decomposition.
- [x] A05 and P164 are named, and their fixed-difference flags, affine
  fibres, clocks, and Jordan machinery earn zero separation credit.
- [x] The retained claim is limited to repeated state selection, observable
  direction words, uniquely anchored lifts, and their simultaneous atlas.
- [x] Both bibliography records were verified against primary publisher or
  manuscript surfaces and DOI metadata.
- [x] Both bibliography entries are cited; no uncited or unresolved record
  remains.
- [x] Bounded search nonhits are never called novelty, priority, or
  clearance.

## Manuscript, build, and visual audit

- [x] Anonymous `amsart`, A4, 10pt, 24 mm margins.
- [x] Volatile PDF metadata are suppressed; visible author is only
  “Anonymous.”
- [x] The abstract begins with the literal object and reports quantitative
  image, fibre, clock, and Jordan results.
- [x] All theorem items are proved in the three-page main text; no appendix
  or hidden proof obligation remains.
- [x] `FIGURE_PLAN.md` completes the no-figure phase, and the manuscript has
  no figure reference or asset dependency.
- [x] The settled pass has no warning, bad box, unresolved label/citation,
  rerun request, or error.
- [x] All 24 fonts are embedded, subsetted, and Unicode mapped.
- [x] All three rendered pages were visually inspected with no clipping,
  collision, missing glyph, blank page, or stranded heading.
- [x] Two source-only cold builds and the frozen Round-0 copy match
  `main.pdf` byte for byte.

## Review and lifecycle guard

- [x] Review-A provenance terminology finding repaired without theorem change.
- [x] Round-0 and byte-identical Round-1 receipts are both preserved.
- [x] Formal Reviewer-A delta and process-separated Reviewer-B closeout.
- [x] `main.pdf == main_round2.pdf`; two source-only cold builds and 3/3
  final rendered pages pass.
- [x] No release, upload, submission, author contact, or external-message
  action was taken.
- [x] Every active package document retains `OWNER_THIN / HOLD_EXTERNAL`.
