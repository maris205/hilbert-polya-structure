# Response to Reviewers — Round 1

We thank the review panel for the careful and constructive assessment.  All
six items in the immutable revision roadmap were authorized and addressed in
one bounded patch round.  The deterministic apply report and manual semantic-
drift audit confirm that the changes landed at the stated blocks without
altering unauthorized content.

**Summary:** 6 resolved; 0 deliberate limitations; 0 unresolvable; 0 reviewer
disagreements.  Canonical marker-excluded word-count delta: **+520**.  New
bibliography entries: **0**.

## REV-001 — RESOLVED

**Reviewer comment.** The manuscript does not yet support its originality and
broader significance with a sufficiently developed, reproducible comparison
to the closest relevant work.

**Response.** We expanded the Introduction's literature-positioning block with
proposition-level comparisons to the exact source, the nearest algebraic
presentation result, and the general sheaf and extension formalism already
cited in the manuscript.  The revision records the 25 August 2026 search
surfaces, query clusters, post-source date boundary, inclusion rule, and
nearest-hit dispositions.  It states only that no direct post-source solution
was located within that declared search and expressly disclaims a global
priority claim.  No new bibliography key was introduced.

**Changes.** Introduction and main results, blocks B0022, B0103, and B0104.

## REV-002 — RESOLVED

**Reviewer comment.** The conclusion contains unexplained project-internal
Route and Gate terminology that interrupts the standalone mathematical scope
statement.

**Response.** We removed the project-internal Route-A, Route-B,
Route-coordinate, and Gate A--E paragraph.  The surrounding public
mathematical scope statement and conclusion remain intact.

**Changes.** Scope, controls, and conclusion; block B0091 deleted.

## REV-003 — RESOLVED

**Reviewer comment.** Authorship, contribution, funding, and
competing-interest metadata still contain unresolved confirmation
placeholders.

**Response.** We replaced the title-block placeholder with the confirmed Liang
Wang byline, affiliation, and contact email, identifying the email only as
Contact because corresponding-author status was not designated.  We also
inserted the author's explicitly confirmed contribution sentence and the
confirmed statements that the work received no specific funding and that the
author has no competing interests.  The scientific title and draft date are
unchanged, and these metadata edits do not alter the mathematical claims.

**Changes.** Title block and Declarations, blocks B0005, B0096, B0097, and
B0098.

## REV-004 — RESOLVED

**Reviewer comment.** The extension class, kernel sheaf, and Ext group are
written without topology indices even though the fppf and finite-flat
statements live in different abelian categories.

**Response.** We quantified the topology over the fppf and finite-flat sites,
introduced the topology-indexed kernel and extension class, and placed each
class in the Ext group of the matching abelian category.  The corollary,
Section 5 setup, and proof now use the same indexed notation, with an explicit
local abbreviation for the untouched continuation of the proof.

**Changes.** Blocks B0019, B0020, B0069, and B0073.

## REV-005 — RESOLVED

**Reviewer comment.** The finite-flat covering-family convention is not
defined when that topology is introduced and contrasted with fppf.

**Response.** We defined a finite-flat cover as a jointly surjective family of
finite flat morphisms, identified the corresponding affine ring maps as finite
locally free, and stated the subcanonicity property used for the structure
sheaf and descent.  The finite-flat theorem remains logically separate from
the fppf theorem.

**Changes.** Introduction and main results, block B0016.

## REV-006 — RESOLVED

**Reviewer comment.** The reusable categorical descent-obstruction pattern
remains implicit rather than being separated from the Witt-specific arithmetic
and site-dependent inputs.

**Response.** We separated the conditional categorical template from its
arithmetic and site-specific instantiation.  The template fixes the
endomorphism, source section, and selected target, and explains why an inducing
middle map would supply the forbidden global preimage before invoking the
pushout--pullback criterion.  The conclusion retains the exact bound (N>1),
lists the non-formal proof inputs, and describes the four finite-algebra
calculations only as the explicit computational core rather than the entire
verification.

**Changes.** Blocks B0023, B0105, B0092, and B0106.

## Verification receipt

- official patch: 13 operations, authorization PASS;
- original blocks preserved byte-identical: 89/102;
- structural flags: none;
- manual semantic-drift review: OVERALL PASS;
- complete LuaLaTeX/BibTeX build: PASS, 13 A4 pages;
- undefined citations/references, overfull boxes, missing glyphs, fatal errors:
  all zero.

This response is a Stage-4 revision artifact, not a submission or publication
authorization.
