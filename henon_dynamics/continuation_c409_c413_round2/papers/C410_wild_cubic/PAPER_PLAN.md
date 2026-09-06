# C410 paper plan: wild cubic inverse-image towers

2026-09-06. Implements the frozen [batch outline](../../BATCH_PLAN.md),
including R2. Anonymous English mathematical article, 11pt, one-inch
margins, no imposed venue or page limit. This is one paper, not a group
paper plus a ramification paper.

One-sentence contribution: for every field k of characteristic three and
every a∈k*, the generic inverse-image tower of X³+aX² realizes the
classical signature-constrained ternary group, with exact geometric branch
data explained by maximal global and rank-one local Artin–Schreier classes.

## Claims and evidence

| Claim | Complete proof source | Manuscript location |
|---|---|---|
| Compatible arithmetic/geometric group E_n and regularity over arbitrary k | Frozen WILD_CUBIC_PROOF §§2–7; REVIEW_WILD_CUBIC_ROOT | Statements; normal form; tree constraint; simultaneous induction and descent |
| Exact geometric Kummer relations and global AS rank, versus local rank one | Frozen proof §§4–6; same non-author review | Kummer section; AS section |
| Branch set {0,∞}, e/d values and geometric genus | Frozen proof §§4,6,8 | Zero-place lemma; final ramification section |

All source paths above refer to `../../../research_c409_c413/`, with the
proof under `positive_characteristic/` and the review at that tree's root.
No unchanged mathematical check is rerun. The final article contains the
full arguments, not links replacing proofs.

## Sections

0. Abstract: scope, classical group attribution, global/local rank distinction,
   group order and second-level genus; no citation-dependent statement.
1. Introduction: precise problem and contribution; classical PCF/Belyi group
   ownership; explicit limitations of the recent characteristic-coprime scope.
2. Statements: compatible labelled tree; arbitrary-base theorem; separately
   geometric rank and ramification theorems; proof dependency order.
3. Cubic normal form and local tools: explicit roots and field recovery,
   separability/irreducibility; self-contained radical degree facts and the
   precise local facts used later.
4. Signature constraints: one compatible labelling, classical E_n order,
   bottom A_3 actions; no assumed next-level equality.
5. Zero-place valuations and Kummer rank: tame root cover and closure,
   parity-vector span, exact sibling relations, distinct characters.
6. Local and global Artin–Schreier induction: split Kummer completion,
   pole-order nonvanishing, character projections, local pole cancellation,
   degree equality and descent to arbitrary k.
7. Different and genus: derivative calculation in the root completion,
   tame quadratic comparison and Riemann–Hurwitz.
8. Conclusion and scope: what the uniform result establishes; no finite
   specialization, forward-period, extension-degree or target-zeta inference.

No decorative illustration or new numerical experiment is needed. All
technical arguments remain in the main article. Source literature is
organized by role, not as a list of unrelated abstracts.

## Citation plan and ownership

Use the verified Benedetto–Faber–Hutz–Juul–Yasufuku 2017 article for the
classical E_n definition/order and characteristic-zero cubic realization;
Bouw–Ejder–Karemaker 2021 and Ejder 2022 for Belyi context; the inspected
2025 preprints by Adams–Hyde and Hlushchanka–Lukina–Wardell for precisely
limited characteristic scope. Stichtenoth's second edition is a general
reference for classical function-field tools, not a claimed exact owner of
this tower. Details and read scopes are in CITATION_AUDIT.md.

The group, its order, elementary radical theories, Hensel lifting, tame local
extensions, different formulas and Riemann–Hurwitz are classical. No global
priority statement or target arithmetic theorem is included.

## Review and build handoff

The frozen batch outline has already had a non-author outline review.
After drafting, perform a reverse-outline/scope check and initial compilation
of this new article only. Record engine, commands, warnings and PDF metadata
in BUILD_REPORT.md. A different team member must read the actual manuscript
and citations before release; root retains final double-clean-build, complete
page inspection, evaluation, payload and Git ownership.
