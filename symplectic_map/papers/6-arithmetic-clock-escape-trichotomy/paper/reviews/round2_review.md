# Independent Manuscript Review — Round 2

**Paper:** *Finite Arithmetic Capacity under Additive Locally Constant,
Good-Reduction Multiplier, and Algebraic-Action Readouts*  
**Review date:** 2026-08-14  
**Reviewed revised-source SHA-256:**
`2be0a171cf94b54a58e447bb1922a14880e69c4f80733df5a0882f0302978cb4`  
**Reviewed Round-1-revision PDF SHA-256:**
`9c3b395a9d4ec704fb54951bd69d5d0fd6d9db7bb6c857f8fb45ee6e5b69c0f8`  
**Reviewed Round-1 review SHA-256:**
`d9dffa9c37fd4eb4151f7953583100c0974407ffefd0eb104672bf8b463bab14`  
**Reviewed author-response SHA-256:**
`739e851904976b967c774d0ce43737f0f5f13aa04a18428006728bfcde4175c9`  
**Reviewed revision-integrity SHA-256:**
`a89d1e4c5a38d7d79bf9c38cfba9fd1ff9a634e1f9a77fb31dda60b3355f524b`  
**Independence statement:** I did not author or revise the manuscript,
mathematical package, code, official results, figures, citations, response, or
integrity records. The only file created in this round is this review. I did
not inspect prime tables or Riemann-zero data and did not execute a candidate
search.

## Verdict

**PASS**  
**Overall score:** 9.0/10  
**Confidence:** 0.97  
**Mathematical status:** `PROVABLE AS STATED`  
**Finalization decision:** `YES — MAY FINALIZE WITHOUT FURTHER SCIENTIFIC REVISION`

Both required Round-1 minors are fully closed, the optional float repair is
effective, and I found no regression in the main theorem, L/M/A source
certificates, scope boundary, official evidence, citations, figures, build,
or visual presentation.

## Closure of required minors

### M1 — projective-affine Class-M lemma: CLOSED

Section 5.2 and Appendix B.1 now use the correct scheme-theoretic argument.
After base change to an algebraic closure, separate-degree homogenization and
monicity leave no geometric point on the hyperplane at infinity. The finite-
type cyclic projective scheme is therefore contained as a closed subscheme in
an affine chart, hence is both proper and affine. A finite-type affine scheme
proper over a field is finite; equivalently its coordinate algebra is finite-
dimensional. The text explicitly permits nilpotents, does not assume
reducedness, and invokes descent of finiteness. Thus the argument proves a
finite scheme, and consequently algebraic periodic coordinates, rather than
merely proving that the reduced support is zero-dimensional. The faulty
“only constant global functions” sentence is absent.

### M2 — sharpness, attainability, and provenance: CLOSED

The abstract now calls the result a **rank-plus-support capacity bound** and
does not call it sharp. Remark 4.2 limits the construction to abstract
attainability of the bare rank contribution: deliberately inserted independent
labels are explicitly identified as target injection, not arithmetic
emergence or intrinsic-provenance optimality. Figure 1 likewise says “formal
rank attainment” and “target injection: yes.” Immediately after Definition
3.2, the manuscript separately states that target independence is a
provenance condition; once valid certificates are supplied, it is not used in
the linear-independence proof. This is the correct claim boundary.

### Optional Table-1 placement: CLOSED

The related-context table now appears at the start of page 4 and is completed
before Section 3 begins on that same page. The `FloatBarrier` therefore fixes
the Round-1 continuity issue without disturbing the narrative.

## Regression audit

The additive theorem and its proof remain correct. For one arbitrarily
selected valid certificate per distinct outside-support prime, a rational
dependence among the `v_p` terms is cleared to an integer relation and yields
`log R = beta` with positive algebraic `R` and real algebraic `beta`.
Hermite--Lindemann forces `beta=0`; real-exponential injectivity gives `R=1`;
squaring exposes only certified `q_p^2` factors; and a place over each distinct
outside prime isolates and annihilates its coefficient. The finite-subfamily
argument still handles an initially infinite hit set. Positivity, rational
and negative powers, `q=1`, repeated-hit set semantics, representation
selection, and finite-extension invariance remain explicit.

The three source certificates also remain in scope and internally consistent:

- Class L uses higher-block recoding only for fixed finite-memory locally
  constant readouts and excludes general Hölder roofs.
- Class M retains cyclic-neighbor multiplicity, the repaired proper-affine
  finiteness step, the non-Archimedean maximum argument, determinant-one
  monodromy and inverse integrality, and normal-extension saturation before
  using `q^2=lambda*conjugate(lambda)`; it never identifies conjugate with
  reciprocal.
- Class A retains regular algebraic evaluation and the full endpoint gauge
  ledger, while distinguishing algebraicity from canonical gauge invariance.

The selector remains a corollary. Certificate escapes remain necessary only,
not exclusive, exhaustive, or sufficient. The paper still expressly excludes
a universal symplectic no-go theorem, infinite-dimensional necessity,
historical priority, approximate matching, algebraic-irrational multiplier-log
mixing, and Riemann-zero/trace-formula/determinant/quantization/Route-B
progress. Positive Deninger and Connes--Consani architectures are correctly
treated as outside-class boundary examples.

## Independent evidence and reproducibility checks

I rehashed the immutable official package and recovered the declared values:

- official result:
  `9f9878247dc821d15b503abe5a3df713d5bde0f3c76690493dc1b4a98091ace4`;
- registered-run record:
  `4ebec117a2254dc4502c7afd4094e833bc751b8a7e3bffcc16496dd0fd0ea5e3`;
- exclusive result manifest:
  `21d6910ec1e8e2995d4141f264dce06902f7d1787dea6f28d82346ebd54e3d79`;
- source lock:
  `2d27abceb65cd0ad39612b287e27e2bbdb0b097a67e3bff4d4d6e280e6e4e3fc`;
- reviewed code tree:
  `10fd57b1f99616799f05c3b6a4ce11a9e8ea747d33bb50299aac618948482fb7`;
- official JUnit:
  `34915053371701fafd147dd39986b7a5eb157ff09c44f425edfd88f0a8ac17da`.

The records agree on `CAPACITY_BOUND_CERTIFIED`, nine of nine gates, 20 proof
IDs with zero cycles, 10 admitted and 9 excluded operations, 6 exact controls,
12 scanned executable files with zero findings, and two closed upstream
packages. They record one static registered run, zero numerical candidate
runs, zero target matches, and false prime-table, target-array, numerical-log,
and Riemann-zero flags. I independently reran the noncandidate test suite:
**51/51 passed**.

In an isolated temporary copy, I regenerated all three figures in PDF/SVG/PNG.
All nine outputs and the reproducibility record matched their frozen hashes,
including revised Figure 1. Two consecutive clean paper builds both reproduced
the revised PDF hash
`9c3b395a9d4ec704fb54951bd69d5d0fd6d9db7bb6c857f8fb45ee6e5b69c0f8`.
The final LaTeX log contained no error, warning, undefined citation/reference,
or box warning; all fonts are embedded and subset. The bibliography has 18
cited entries, with zero missing and zero unused keys.

Original-resolution inspection of the three figure masters and a rendered
contact sheet of all 12 pages found no clipping, collision, illegible label,
broken glyph, or misplaced float. The conclusion still ends on page 9.

## Final recommendation

Accept and finalize this revision. No further mathematical repair, experiment,
target computation, source-lock amendment, figure change, citation addition,
or claim weakening is required. Finalization may copy the reviewed revision to
the final immutable PDF and update only the retrospective final-integrity and
pipeline indexes.
