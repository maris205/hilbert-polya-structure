# C413 paper plan

Title: **Integral periodic points of the Fibonacci trace map**.
Type: self-contained mathematical classification, anonymous research manuscript.
Venue: unspecified; standard 11pt `article`, no artificial page target.
Date: 2026-09-06. Batch authority: [five-contract plan](../../BATCH_PLAN.md).

One sentence: the classical 4-, 6-, and 12-periodic families, together with
the special fixed points and 3-cycle, exhaust the integral periodic locus of
`T(x,y,z)=(y,z,yz-x)` on all invariant levels.

## Claim–evidence map

| Claim | Complete evidence | Manuscript location |
|---|---|---|
| All integer periodic points lie in six displayed orbit types, with exact periods and no height cutoff | Proof package §§3–5; non-author root review | Main theorem in §1, full existence and exclusion in §§2–3 |
| A bounded half-orbit is periodic; other points escape every bounded set in both directions | Discrete bijection argument, proof §6 | §4 |
| Exact return and zeta formulas on every integer level; supports overlap only at level 4 | Proof §7, including checked positive-factor clarification | §4 |
| The integer and single-map hypotheses cannot be silently enlarged | Rational 2-cycle and non-axis level-8 example; primary whole-group theorem | §5 |

The primary proof is
[PROOF_PACKAGE.md](../../nonlinear_geometry/PROOF_PACKAGE.md), with
[independent review](../../REVIEW_TRACE_ROOT.md) and
[source ledger](../../nonlinear_geometry/SOURCE_LEDGER.md).
Finite exact checks are supplementary, not the source of exhaustiveness.

## Front matter and sections

`sections/0_abstract.tex`: approximately 170–200 words. State the integer
classification first, the exact period set and level support explicitly,
then the maximal-coordinate proof idea. State that the displayed families
are classical; the contribution is their arithmetic exhaustiveness.
Do not imply a rational-point theorem, new periodic curves, a global
finite-count zeta, or a target Riemann statement.

`sections/1_introduction.tex`: define `T,K,S_k`, put the main theorem and
orbit-family table before technical details, explain the distinction between
known real/complex families and their complete integral intersection.
Related work is organized by (i) single-map curves and escape,
(ii) finite orbits of a whole group, and (iii) integer levels and residual
periodicity. Credit the specific classical statements and delimit all claims.

`sections/2_itineraries.tex`: scalar recurrence, polynomial inverse and
invariant, cyclic scalar words and the complete 12-triple table. Prove exact
periods including `m=1`, disjointness, and heights. No numerical dependency.

`sections/3_exhaustiveness.tex`: maximal coordinate; neighbours of modulus 2
with complete equality argument; two zeros; one zero and the `M^2-1`
contradiction; four signed nonzero-neighbour cases; full unit-cube remainder.
Every step of the main proof appears here, not in an external supplement.

`sections/4_level_arithmetic.tex`: boundedness/proper escape, exact-period
counts, fixed-point formula, source dynamical zeta, intersection of the two
level families, and the complete per-level point-count table. Explain why
`Fix(T^6;Z^3)` is infinite before making any whole-lattice zeta inference.

`sections/5_scope.tex`: exact rational counterexample and whole-group
counterboundary; describe the finite graph/identity diagnostics with their
actual finite scope; conclude with the proved integer classification and
the remaining rational and target-arithmetic limits. The manuscript claims
neither an escape growth rate nor complete literature priority.

## Tables and citations

Tables carry exact mappings: orbit type/least period/height/level; the
twelve-point itinerary; neighbour-sign cases; complete level point counts.
These make actual classifications easier to read. No decorative hero image,
data plot, or image-generation skill is needed.

Only five planned citations, all with primary text and verified metadata:
Roberts–Baake 1994, Roberts 1996, Humphries 2016 v1, Ghosh–Sarnak 2022,
Vishkautsan 2016. DOI content negotiation returned all five real bibliography
records on 2026-09-06. The manuscript's Humphries citation pins arXiv v1;
no journal is invented. Use references only for attribution/context, since
the full mathematical argument is elementary and self-contained.

The detailed root source read ranges are in the independent review; the
proof does not presuppose every cited paper was read end to end. Source
comparison does not support an unsupported “first” claim.

## Review and completion

This is a concrete instantiation of the batch outline, pending its non-author
review. Once frozen, write all six section files and complete `main.tex`,
notation and cited-only bibliography. Apply a reverse-outline/clarity pass.
Another team member must review the actual C413 manuscript; the root review
of the author's earlier proof does not count as independent review of a
manuscript authored by the root.

Build and final-release checks follow the batch plan. Reuse unchanged exact
proof-check receipts with their limits. The bibliography and final manuscript
will be checked on their actual final inputs. No PDF or manuscript-level
review has been completed at the time this plan is written.
