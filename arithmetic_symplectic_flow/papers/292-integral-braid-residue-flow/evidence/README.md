# Evidence — integral refactorization and full returns

Candidate ID: `ANG-20260920-BRF01`.
Status: `OWNED REFACTORIZATION CLOCK; COMPOSITE PRIMITIVES AND MISSING ODD-PRIME TIMES — STOP / FORK`.

## Input freeze and exact proof method

The original [candidate card](../candidate-card.md), before its outcome
appendix, has SHA-256

    c6a64634a95a0cbcae762b80450deeec84768a6ab84c450fd11a56ac3dddc3d0

The frozen inputs are all positive roots, full Z_hat² seeds, joint
root-Haar measure, the two integrality conditions, fixed residue update,
retained-lag partial-tail convention and exact time-extension recipe.
There is no finite list of primes, prescribed roof or target data.
Neighboring cards provide definition comparisons only: no old theorem
serves as a mathematical dependency for this new clock or ledger.

Reproduction is by the exact arguments in [paper.md](../paper.md):

1. Multiply the two 3 by 3 unipotent words and compare their three
   upper entries. Invert each actual root/digit branch explicitly.
2. Decompose the inverse seed map into an integer unimodular shear,
   one multiplication by d and a translation. Compose its joint-Haar
   IMAGE law, then cancel common terminal prefixes in branch pairs.
3. Sum the actual nonnegative digit increments around any cycle.
   Check the zero-digit involution and the integer inverse matrix
   P=B_d B_b, tr P=db+d+b, det P=db.
4. Exclude every nonzero periodic profinite seed via nonzero integer
   det(P^m-I) and injectivity of integer multiplication on Z_hat.
5. Cancel transient prefixes in isotropy clocks; count entire core
   cycles, not their phase representatives or preimages. Parametrize
   roots by g,k,alpha,gamma to check odd-prime-square multiplicity.
6. Apply the two separately frozen control laws with their OWN branch
   measures. Do not substitute an algorithmic step count for real time.

No scientific computation, numerical precision, orbit cutoff, modulus
census or parameter fit was run. The integer m ranges over all positive
periods in an exact proof. No external literature expansion or novelty
claim is involved. Finite displayed roots are exact counterexamples,
not numerical evidence for an infinite classification.

## Review, controls and output boundary

The [scout record](scout-record.md) distinguishes definition authorship
from mathematical review. Root writes the paper and integrates all
companions; the [reviewer](independent-review.md) writes only its report.
ARS provides raw-card, manuscript-comparison and adverse final checkpoints.
The review checks all seeds, actual index-clock signs, primitive versus
repeat multiplicity and the scope of the separate controls. Shared
model/context review is not external peer review, formal verification
or independent-error evidence.

The final manuscript SHA-256 is

    574c7c45d48ee1899c4e913fe697d4d5150932738ec219089cadfb7e988c1929

The frozen internal review SHA-256 is

    0be8d6c7c4bd5395d1d6a1ddf575357a8ca0bd2b3dc372480455e6775ea7fddf

The manuscript comparison initially read hash
afbe09586ffbbd5d5ef66c94077fc75a4b7590a6fcedc3ca633812637e49ac0f.
Two wording corrections then distinguished terminal main STATES from
root fibres and made the finite-preimage bound relative to each fixed
core cycle and depth. The reviewer checked those changed passages at
the final hash; no formula, result, control or frozen rule changed.
The odd-prime count and extra FEEDBACK-OFF fixed seeds were manuscript
stage checks, not retroactively called blind raw findings. No outstanding
blocking issue remains within the internal review's stated scope.

The composite fixed-core counterexample is decisive before a broad
period census. The same short identities happen to give the full
main return classification, so no further orbit search or T3 work is
performed. FEEDBACK-OFF higher-period seeds and the full coarse topology
remain unclassified. Strong naturalness stays OPEN despite genuine
integer divisibility and owned time. No zero/noninteger/null/terminal
state was removed, no packet with an inconvenient period was selected
away, and no clock was adjusted after the result.

Only this new Markdown package and registry summaries are written.
Old packages/mirrors untouched; 241/242 paused; programme active.
Classical fields NOT APPLICABLE; formal UNASSIGNED; B NOT INVOKED.
No PDF/LaTeX, commit, upload, publication or quantum/analytic operator.

## Verification receipt — 2026-09-20

Root's read-only Python check covered all seven package Markdown files
and the two new registry entries. Result: **41 package-local links +
2 new registry links resolved; 7 primary identity/status records
matched; 3 hash locks matched; 0 issues**. Every new file decoded as
UTF-8, ended in a newline, contained no NUL/tab and had trailing spaces
of only zero or two characters.

Identity/status inputs were paper.md, candidate-card.md, claim-ledger.md,
package README.md, evidence/README.md and both registries. Expected:
ANG-20260920-BRF01 and OWNED REFACTORIZATION CLOCK; COMPOSITE PRIMITIVES
AND MISSING ODD-PRIME TIMES — STOP / FORK. Relative inline Markdown
targets were resolved against each file's parent directory.

The three byte-level SHA-256 locks bind the original card prefix,
final paper and final review. The prefix was obtained by splitting
at the first newline followed by `## Appended audit outcome`; it
still matches the original freeze. No old result was a proof input
requiring a new mathematical dependency lock.

| Final artifact | Lines | SHA-256 |
|---|---:|---|
| paper.md | 307 | 574c7c45d48ee1899c4e913fe697d4d5150932738ec219089cadfb7e988c1929 |
| candidate-card.md with outcome | 194 | a126bdf8b04cb72bff12147663c73798345a640e9e2c609c28f107410b9ce8e7 |
| evidence/independent-review.md | 152 | 0be8d6c7c4bd5395d1d6a1ddf575357a8ca0bd2b3dc372480455e6775ea7fddf |

Exact whitespace command, from the workspace root:

```sh
git diff --check -- readme.md papers/README.md papers/292-integral-braid-residue-flow
```

Exit zero, no output. The separate Python check explicitly covered
untracked Markdown, unlike Git diff alone. Session outputs are summarized
here; no standalone validator or scientific output file was created.
After this receipt only its changed content/whitespace and the scoped
Git diff were checked. Integrity QA is not a mathematical proof,
Route evaluation or external peer review.
