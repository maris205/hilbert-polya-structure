# Paper 22 Stage-2 independent proof and source audit

Date: **2026-08-24**

## Proof audit verdict

**PASS WITH MINOR WORDING FIXES; all fixes applied before the final build.**

An independent proof audit found no fatal gap in the all-index fppf
obstruction, the separately checked finite-flat argument, the extension
criterion, or the counterexample to the version-1 sectionwise assertion.
It checked the following load-bearing steps:

1. abelian sheafification preserves the integer-multiplication
   monomorphism and identifies the actual kernel sheaf;
2. the fppf and finite-flat domain refinements over a Dedekind domain use
   flat going down and torsion-free implies flat;
3. the root cover is finite free of rank N;
4. the roots-of-unity product and characteristic-q power identity give the
   stated local preimage;
5. Dedekind injectivity forces that preimage uniquely in the sheaf section
   group;
6. the overlap-to-truncated-ring specialization is well defined;
7. the big-Witt detector is applied first to the inner section y, and
   integer torsion-freeness is then applied to its q-power multiple;
8. the final multiple is a genuine nonzero rational-kernel section;
9. the pushout/pullback orientation in the Ext criterion is correct; and
10. the overlap is used only as a necessary descent detector, not as an
    unproved computation of all sheaf Ext.

The audit required two scope corrections. The manuscript now uses a
universe-small noetherian-affine owner in Deninger's sense rather than an
arbitrary skeleton, and it does not extend the already-sheaf identification
of the rational Witt target to all affine schemes.

## Source audit verdict

**PASS for Stage 2.**

The official arXiv record and local version-1 PDF were checked. The source
PDF has 31 pages, passed the local 31/31-page preflight, and has SHA-256

    19870cbdddbde82526939eb801c2ce14707dc7b48e54a7bc81f4a84400505002

Verified locators are Theorem 3.4 on p. 19, Proposition 4.3 on p. 21,
Example 4.4 on p. 22, Proposition 4.5 on pp. 22--23, Corollary 4.6 on p. 23,
Corollary 4.7 on p. 24, and the lifting question on p. 25. The
Deninger--Mellit DOI and the cited Stacks tags were also checked against
official records.

## Source-sensitive disposition

- The manuscript preserves Propositions 4.3 and 4.5 and Example 4.4 as
  independent valid inputs.
- It limits the correction to the objectwise-surjectivity assertion in
  Corollary 4.6 as stated in version 1.
- It uses “appears to use” and “does not hold as stated,” and does not claim
  author agreement.
- The author-contact note remains marked UNSENT. No external contact was
  made.

## Audit boundary

This is an independent mathematical/source audit within Stage 2. It is not
the formal Stage-2.5 citation-integrity workflow and does not authorize
submission, release, or contact.
