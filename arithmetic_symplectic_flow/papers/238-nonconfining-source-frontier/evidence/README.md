# Evidence record — reversible divisor-scan control

**Scope ID:** `ASFS-SCOUT-20260918-NCF01`  
**Candidate ID:** `ANG-20260918-RDS01`  
**Status:** `FULL REVERSIBLE OWNER; PRIME SCAN CLOCK — STOP / FORK`.  
**Formal Route coordinates:** `UNASSIGNED`. **Route B:** `NOT INVOKED`.

## Frozen inputs and exact method

Root froze the RDS01 subcard in the [candidate card](../candidate-card.md)
before this proof audit and writing task. Inputs are the full discrete set
X={(n,d):n≥2,1≤d<n}, the complete cyclic phase scan R, the three branches
of h, the divisor-hit map C, the composition F=C∘R and the fixed unit roof.
There is no prime table, numerical parameter, data fit or external clock.

The [paper](../paper.md) gives self-contained exact proofs:

1. Partition the images of h and write its inverse on all three classes.
2. Partition X into divisor-hit fibres {(dk,d):k≥2} and their complement.
   Compose C⁻¹ with the predecessor scan in the correct reverse order.
3. Verify the symbolic source-change witness F(4,1)=(8,2) and its inverse.
4. Decompose the full suspension by complete F-orbits, deriving lines or
   circles and the actual return subgroup mZ with the unit physical clock.
5. Restrict to each entire prime fibre and count its cyclic phases; handle
   p=2 explicitly. Integral comparisons give log p<p−1 and
   (p−1)/log p≥(√p+1)/2, excluding even a fixed logarithmic-scale multiplier.

No orbit enumeration, numerical run, spectral computation, cutoff or
precision assumption was used. There is no generated dataset, PDF or LaTeX
artifact. The witness in step 3 is a hand derivation from the frozen formula,
not a finite computation offered as evidence for an infinite classification.

## Scope and controls

The selected local comparison cards were 219, 221, 226 and 229. The prior-work
guide supplied the symbolic-lineage frame; no external literature campaign,
novelty claim, bibliographic verification or historical theorem transfer was
performed. The source update, no-hit prime fibre, zero-update comparator,
roof-owner boundary and invertibility/naturalness distinction are explicit
in paper section 5. Composite recurrence is not classified.

Root's portfolio section additionally records two read-only lanes. The
completed BFT01 proof is owned by 239, not a dependency of RDS01. A third
scout compared local 024, 061, 136 and 146 and proposed compatible residue
registers with dilation arrows. No new exact card, proof or computation
was admitted for that proposal. Its disposition is an architectural
admission decision, not a new theorem about a profinite system. Root
verified the linked local comparison summaries before integration.

ARS argument-building guidance was applied to keep every claim attached to
its proof and retain the strongest relevant objection: h's chain does not
control recurrence of F. This was a bounded local theorem note, not the full
publication pipeline, a venue review or an external-model run.

## Checks and provenance

Author self-check: the displayed inverse covers 2, every odd j≥3 and every
even j≥4; hit images stay in the hit subset; the F inverse uses the current
post-hit n when undoing C and the recovered n when undoing R. The flow formula
was checked against the frozen endpoint relation. The p=2 boundary was
checked as a suspension circle, and equation (5) proves a strict all-prime
clock mismatch. These are author checks, not independent peer review.

A bounded native mathematical checker read the frozen card and returned a
separate analytic check of the inverse, suspension and prime-time statements.
It found no correction to those statements and specifically confirmed the
disjoint image classes, hit/complement separation, inverse composition order,
one prime packet rather than one per phase, and the p=2 circle. It asked that
the discrete and continuous transformation groupoids be distinguished; the
paper names both explicitly. This was a same-runtime model check with shared
scouting context, not a blind, cross-model or human peer review. It did not
claim to classify composite cycles or review the final written package.

Root's additional raw-card check prompted the explicit sector boundary:
hit outputs and inverse outputs are composite, so source updates do not
dynamically generate prime labels. This is proved in paper section 3 and
does not alter the frozen action or clock.

At `2026-09-18T13:24:41.979Z`, the author ran a read-only `node` stdin
validator from the ASFS workspace against exactly README.md,
candidate-card.md, paper.md, claim-ledger.md and evidence/README.md. It
required the exact candidate ID and final status in every file, a final
newline and no ASCII control bytes other than tab/newline/carriage return;
it resolved every relative inline Markdown file-link target against the
containing file's directory. The command exited 0 and returned
`{"files":5,"links":28,"errors":[]}`. The only subsequent evidence edit
replaced the pending-check text with this actual receipt; no mathematical
inputs or link targets changed. `git diff --check` also exited 0, but these
new untracked files were chiefly checked by the explicit five-file read.

This is document consistency evidence, not a mathematical or Route
certificate. Root owns registry and cross-candidate portfolio integration;
the author writes only this package and does not assign results to 239.

## Final written review — 2026-09-18

Root's separate reviewer first received the raw frozen card without the
author draft or peer answer. After its independent derivation, it read all
five written files, including the later portfolio section. It found no
mathematical blocking issue. In particular it checked the full inverse,
the bidirectional composite-sector boundary, the scale estimate
log p<=2(sqrt p-1), the diverging ratio, the p=2 suspension circle and
the absence of cross-owner result transfer in Section 7.

The reviewed final paper.md SHA-256 is
`ea773da13f35092e16f5e16faf552ee3d98c6da4c2940a3d822466c4468bce86`.
This is actual same-runtime model checking, not external peer review or a
correctness certificate. The earlier five-file/28-link result above is
the author's pre-integration snapshot, not a receipt for root's appended
portfolio. Final mechanical integration is recorded separately below.

## Root final integration receipt — 2026-09-18

Root's read-only Node stdin check explicitly read the five standard files
of each of 238 and 239, plus readme.md and papers/README.md. It checked
exact IDs, current status strings, UNASSIGNED, NOT INVOKED, final LF and
absence of CR. After removing fenced/inline/indented code, it resolved
local Markdown link paths relative to each file, stripping fragments and
skipping HTTP(S), mailto and empty targets. It checked both package IDs
and links in both indexes. Remote URLs and fragment anchors were not
validated by this mechanical pass.

After repairing two formatting CR bytes in 239, the observed result was
10 package files, 59 package-local links, two index files, 457 index-local
links and zero errors. This covers the final Section 7/portfolio additions,
unlike the earlier author snapshot. `git diff --check -- readme.md papers/README.md`
exited 0 without diagnostics. sha256sum confirmed the 238 final-paper hash
above. The new untracked files were checked explicitly, and other work was
preserved. No mathematical claim follows merely from these receipts.
