# Evidence — ASFS-20260915-DRC01

**Date:** 2026-09-15  
**Status:** STOP — POSITIVE DERIVATIVE ROOF HAS FINITE-TIME ESCAPE.

## Frozen inputs and exact method

The [version-1 card](../candidate-card.md) preceded the audit. The complete
input is its all-integer cotangent map and the new roof
tau(q)=log(1+(1/2)sech²q). The full [paper](../paper.md) supplies the
definitions and proof; no numerical or externally sourced theorem is used.

Exact test domain: n=2, k=1, arbitrary q_0>0 and p_0 in R. Define
c=(1/2)tanh q_0. The proof establishes q_j>=q_0+cj, bounds every roof
by 2 exp(-2q_0-2cj), and sums this geometric majorant. It then constructs
a continuous function on the actual endpoint quotient that diverges as
the finite total time is approached. This last step excludes an endpoint
without incorrectly identifying raw q across a gluing seam.

No executable numerical command, cutoff, finite-state enumeration,
precision budget, prime table, target-zero comparison, data split or
analytic continuation is involved. The result covers an infinite
one-parameter family exactly; finite observations are not used to prove it.

## Controls and scope

- The separate unit-roof comparator admits only finitely many crossings
  during any finite time.
- Explicit central prime cycles have positive repeated roof sums, but
  cannot remove the escaping noncentral states from the frozen carrier.
- The same bound applies to every initial momentum.
- The source failure test uses an empty divisor block: no prime search
  or composite enumeration is needed.
- Roof positivity is distinguished from the required non-Zeno property.

This package awards no A1, A2 or operator result. Formal Route coordinates
remain UNASSIGNED and Route B remains NOT INVOKED.

## Verification record

The initial author check used a Node standard-library filesystem traversal
of this exact package. It read each Markdown file, resolved local link
destinations relative to the containing file, checked trailing whitespace,
and required the same candidate ID and current status in README, paper,
card and claim ledger. Result: 5 Markdown files, 16 local destinations,
zero errors. The scoped command git diff --check --
papers/155-derivative-roof-completeness-test also returned no errors;
the filesystem check, not Git alone, covered newly created files.

The [independent bounded model review](review.md) checked the infinite
majorant and the quotient endpoint argument and found no mathematical
blocker. It also supplied a closed-section topological cross-check. The
author and reviewer exchanged the endpoint arguments, so this is separate
model review, not blind review, external peer review or a claim of
independent model error processes. A cosmetic proposition locator was
corrected without changing the argument.

External URLs and other packages were not revalidated.

After linking the review, the same exact package-local check reported
6 Markdown files, 22 local destinations, zero errors, with the four core
candidate IDs and status strings consistent. No mathematical computation
or proof rerun was needed for the locator and navigation edits.
