# Author Response to Independent Round 1

**Review verdict:** `PASS_WITH_MINORS`  
**Review SHA-256:**
`d9dffa9c37fd4eb4151f7953583100c0974407ffefd0eb104672bf8b463bab14`  
**Revision date:** 2026-08-14  
**Status:** both required minors implemented; author-side verification only,
not an independent Round-2 review

## M1 — projective-affine scheme statement

**Response: accepted and repaired.**  Section 5.2 and Appendix B.1 no longer
argue through constant global functions on connected components.  They now
state the scheme-valid result: after algebraic-closure base change, absence of
geometric points at infinity makes the finite-type cyclic scheme both proper
and affine; a finite-type affine scheme proper over a field is finite, or
equivalently has finite-dimensional coordinate algebra.  The text explicitly
allows nilpotents and then invokes descent of finiteness.  This proves finite
scheme structure, not only zero-dimensional reduced support.

No source-lock or official-result change was required: the mathematical
conclusion and the frozen dependency ID M002 are unchanged; only its manuscript
justification was made scheme-theoretically precise.

## M2 — use of “sharp” and provenance

**Response: accepted and weakened.**  The abstract now says
“rank-plus-support capacity bound,” not “sharp capacity bound.”  Remark 4.2 is
renamed “Edge cases and abstract attainability” and limits K001 to attainability
of the bare rank contribution.  It states explicitly that deliberate labels
are target injection and do not establish arithmetic emergence or intrinsic-
provenance optimality.  Definition 3.2 is followed by a new sentence separating
the target-independence provenance condition from the logical inputs used once
valid certificates have been supplied.

Figure 1 was regenerated so that K001 reads “formal rank attainment” rather
than “formal sharpness.”  All nine figure outputs were regenerated twice; the
only changed outputs are the three Figure-1 formats, and both generations are
byte-identical.

## Optional float-placement polish

The manuscript now loads `placeins` and places a `\FloatBarrier` after Table 1.
The related-work table therefore appears before Section 3 begins.  This adds no
scientific claim.

## Revision verification

- revised source SHA-256:
  `2be0a171cf94b54a58e447bb1922a14880e69c4f80733df5a0882f0302978cb4`;
- revised PDF SHA-256:
  `9c3b395a9d4ec704fb54951bd69d5d0fd6d9db7bb6c857f8fb45ee6e5b69c0f8`;
- revised PDF: 12 pages; conclusion ends on page 9;
- two consecutive deterministic builds have the same PDF hash;
- final log: zero errors, warnings, undefined citations/references, or box
  warnings;
- all fonts remain embedded and subset;
- all 12 revised pages and the revised Figure 1 passed author-side visual
  inspection;
- original pre-review PDF remains immutable at
  `1be29012762238bd469a2b5e86cbc32a76e9c951ed6e524917c99bf05c0a2810`;
- official source lock, registered result, registry, result manifest, JUnit,
  proof ledger, scope ledger, and upstream bindings are unchanged.

A fresh reviewer must perform Round 2.  This response and its checks are not an
independent acceptance decision.
