# Evidence index — ALF-20260915-OHL01

**Paper ID:** 169-ordered-cover-leafwise-symplectic-lift  
**Candidate ID:** ALF-20260915-OHL01  
**Status:** ADVANCE — COMPLETE LEAFWISE SYMPLECTIC PRIME-LOG LIFT; DECLARED DESIGN; NATURALNESS OPEN.  
**Formal Route coordinates:** UNASSIGNED. **Route B:** NOT INVOKED.

## Mathematical inputs, method and limits

The [version-1 card](../candidate-card.md) was the first file created for the
candidate, before the new lift's proof. Its full Y, full planes, reciprocal
cocycle, integer quotient and uniform exponential time law were unchanged
throughout the audit. The [paper](../paper.md) contains all five exact proofs.

Inputs and controls use all positive rational divisibility covers, weak
numerical order, rational products, all real plane/scale values, and elementary
topological and algebraic arguments. There is no prime list, zero data,
numerical experiment, precision choice or finite orbit census. Bounds on
finite-time packets are consequences of the full proof, not sample evidence.

The key reproducible calculations are K^m in equation (4), the globally
well-defined coordinates (qr,p/r) in (7), the all-state closing equations
(10), and the plane derivative (9)--(11). Ordinary product convergence and
its exact boundary are independently proved in Proposition 5. No trace
regularization or operator formula is used.

Relevant read-only local comparisons were the entire 163 paper/card and 052
geometric control, the short 033/034 obstructions, and the prior-work README.
Their limits are stated in Section 2. No comprehensive external literature
search or first-novelty claim was attempted, and no remote source is needed
for the new proofs. See the [claim ledger](../claim-ledger.md).

## Review and author handling

A different native invocation,
/root/research_controller/ordered_leafwise_lift/leafwise_owner_review,
was dispatched after the card to derive owner/topology/period equations while
the author wrote the paper. It inherited the current model and surrounding
context, so this is not blind review or a certificate of independent errors.
The actual completed assessment belongs in [review.md](review.md), not in a
pending checklist. The author does not write that file.

During draft checking both the author and reviewer found escaped math-format
defects: missing backslashes before several qquad commands and two embedded
carriage-return characters in roman-label commands. They were repaired by
targeted apply_patch edits without changing the candidate or mathematics.
The root acceptance check requested explicit acknowledgment of the global
product/no-feedback interpretation; this is now stated after Proposition 3
and in the summary/ledger, not hidden as a stronger coupling claim.

The completed actual review reports SUPPORTED WITH EXPLICIT TYPE AND
NATURALNESS LIMITS; NO OPEN MATHEMATICAL BLOCKER. Its formula-rendering
finding M1 is ADDRESSED, including the last missing spacing-command
backslash. It records all-state topology, gauge, return signs, multiplicity,
repetitions, monodromy, ordinary-product scope and the 052 collision limit.
Review uses bounded ARS claim/evidence/counterargument discipline, not the
full publication pipeline.

## Completed mechanical verification

On 2026-09-15 the author ran a read-only `node -` here-document using Node's
fs/path modules, recursively reading only this package's Markdown files.
The method was: resolve each ordinary Markdown local-link target relative
to its source file after removing any fragment; test target existence;
check the exact candidate ID and final status literal in each of the five
core files; scan for control characters other than newline/tab; and scan
display-math blocks for spacing commands missing their backslash.

Actual result after the separate review file existed:

~~~text
Markdown files: 6
Local file links checked: 39
Core candidate-ID / final-status pairs: 5
Display-math blocks checked for spacing-command defects: 21
Issues: []
~~~

A preliminary check before the review was written found its three pending
links, not completed evidence. Its initial spacing-word regex also matched
the prose discussion of a corrected command; the final syntax scan was
restricted to display-math blocks. No mathematical success was inferred
from either check. The completed review was read in full, including its
final 76-line condensation. That condensation retained three local links
and the same findings; its targeted link/control-character/final-receipt
check returned no issues. The first attempt at that targeted command had
one extra closing parenthesis and stopped with a syntax error before any
check; the corrected read-only command completed. The metadata and links
of this appended evidence receipt were also checked after editing. No
mathematical proof or frozen object changed during these document checks.

## Verification boundary

Only the five assigned Markdown core paths are author-owned. Review.md is
owned by the separate reviewer. No historical package, root navigation,
script, TeX/PDF, Git state or external-model/API endpoint is modified.
Read-only filesystem checks use shell reads and an in-memory Node command;
no persistent verification script is created. Mechanical link/identity
checks do not prove mathematical claims.
