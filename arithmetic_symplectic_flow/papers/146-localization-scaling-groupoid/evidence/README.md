# Evidence — ANG-20260915-LSG01

**Status:** STOP — EXACT LOCALIZATION CLOCKS; FULL PRIMITIVE-PACKET PRODUCT UNSUPPORTED.

## Inputs and methods

The only mathematical inputs are the [frozen version-1 card](../candidate-card.md):
all n>=2, E_n, actual localizations A_n, positive rational multiplication
units, and real translation. The [paper](../paper.md) contains the complete
derivation using unique factorization, a displayed pigeonhole argument,
and elementary groupoid and quotient-topology checks.

No numerical search, cutoff, floating-point output, external prime table,
target data, external source theorem or borrowed flow was used. Prime
support appears only as the proof classification of all input integers.
The proof methods establish all-localization statements directly.

## Adverse and ownership controls

The no-localization comparator, duplicate-label check, mixed-support check,
fixed-time infinite component count, sector-selection control and
Hausdorff-replacement control are recorded in Section 6 of the paper.
The ordinary groupoid point isotropy / time-return stabilizer distinction
is made in Proposition 2.

## Verification

Mathematical verification is by the explicit proofs, not by file checks.
Scoped Markdown-link and identity checks are recorded after package
completion. Independent model review is a separate, bounded verification
step and is not human peer review.

The [independent derivation and bounded model review](review.md) found
no mathematical blocker for the stated results or scoped stop. It used
a separate inherited-model agent, with shared task context and advance
knowledge of the hypotheses; it was not blinded or cross-model review.

Initial package check, 2026-09-15: a Node.js stdin script recursively read
every .md file in this package using fs/path, resolved every Markdown
local-link target relative to its source, skipped web/mail/fragment-only
links, and checked the four core files for the exact candidate ID and
status. It also checked trailing whitespace, allowing Markdown two-space
line endings. Output was 5 files, 18 local links, 0 problems.

The separate command

~~~sh
git diff --check -- papers/146-localization-scaling-groupoid
~~~

returned successfully with no diagnostics. Because new untracked files
are not covered by Git's diff check, the direct filesystem checks above
were used for the actual new package. These checks do not certify proofs.

After adding the review and its navigation links, the direct filesystem
link/whitespace check reported 6 Markdown files, 22 local links, 0 problems.
The candidate ID and common status in the four core files were unchanged.
