# C421 — first independent full-manuscript review

2026-09-08 UTC. Reviewer: current-team spectral-lane agent, not the
author of C421, IR1's analytic proof, either finite-core implementation
or its original mathematical reviews. This is internal AI-assisted
review, not blind review, human peer review, an external GPT-5.4 call,
a calibrated acceptance score, or a Route A evaluation.

## Verdict

**PASS for round-one manuscript transcription and mathematical
presentation, with zero mandatory corrections.**

No critical or major weakness, counterexample, missing signed branch,
incorrect table row, lost degenerate parameter, orientation quotient,
unsupported all-level finite-count assertion, or missing central proof
was found in the actual manuscript. The three suggestions below are
optional precision/readability improvements; none requires a new
mathematical run.

The appropriate next state is ready for the separately required second
full-text review, after the author/coordinator disposes of any chosen
editorial changes. This is not a final-release or submission-ready
verdict. The final two-directory builds, all-final-page visual gate,
formal evaluation and release checks have not been performed here.

No numerical paper score is assigned: there is no selected journal or
ML venue, and the batch expressly separates internal manuscript review
from formal evaluation. No increasing score or fictitious revision is
needed to record this genuinely clean first scientific pass.

## Actual review input and access

All paths in line locators below are relative to
papers/C421_integral_return/ unless explicitly stated otherwise.

The actual review PDF was main_round0_original.pdf, 18 pages,
473416 bytes, SHA-256:

    7fcfe7c00da4590cc44565d2343a5d3e37f233c5ece4798971891e9f145b5e1d

The reviewer read every actual production TeX/Bib file in full:
main.tex, math_commands.tex, references.bib, all ten files under
sections/, all three table files and figures/latex_includes.tex.
The last file is an include index, not a second production inclusion
of the tables. The full 139-line Python source reached through
the appendix's listing was also read in full.

All 17 current TeX/Bib files passed a read-only
sha256sum comparison with BASELINE_SOURCE_SHA256SUMS.txt.
That manifest has SHA-256:

    41fbb8062fbd91e57d04a34bd5082ada3990b8d81257e44410fcf9cb3e0daf53

Selected production identifiers:

| Input | SHA-256 |
| --- | --- |
| main.tex | 8d7cd8949cd8b635705b1f451a372286899f477904abf5b2a7e4f4a1b94995dd |
| references.bib | 40f2c5f4780b1f2ef6d57800c99f957ef2f2ecf122fffe305ebca7636abc9177 |
| sections/04_large_difference.tex | 4e37506f595f0d071aec7750e86e77a139a20270f391dfc08795ae6078d70a0a |
| sections/05_finite_certificate.tex | c4db267df7da3398fae89f4fbc3da3a8335f62a93fb87abfaa70ed6170c39f9a |
| sections/06_least_periods.tex | 0fcd94899b859302114111ae7989e534b67d521b485ef91f19235680867896ec |
| sections/07_level_counts.tex | f765363a097e6229df9d21155662bb4b718c6f6bd10a1a247e9d510fa304932a |
| figures/TABLE_classification.tex | a85240157e024eee9baf49b77320f19f60ada2aa6822ef4423b0b126a5108a45 |
| sections/appendix_certificate.tex | dca39f1b81e668cc083c319c9cb744b49aa7f1d74649c72f791960d309b0e1eb |

The complete PDF text was independently extracted directly from the
review PDF to standard output and read in page groups 1–6, 7–12 and
13–18, through the final line of the source listing. This was not
merely a reading of the author's textual summary or of the earlier
Markdown proof.

The reviewer also actually opened the existing baseline page images
for pages 3, 6, 9, 12, 17 and 18: classification table, signed
branches, finite receipt, level/zeta formulas and source-listing
continuation. Those pages are readable, without observed clipping or
overlap. This is a six-page auxiliary baseline check, not a claim
that this reviewer visually inspected all 18 pages or any future
final PDF. The actual baseline final TeX log was searched and had
no Warning/Overfull/Underfull/undefined/Error match; its search exit
1 means no match, not a failed build. No compiler was invoked here.

## Accepted proof/evidence comparison actually performed

The following original inputs were read in full, independently of
their earlier PASS labels:

| Input relative to research_c419_c423/ | Read extent and role |
| --- | --- |
| continuation_round2/integral_return/IR1_PROOF.md | All 260 lines: global analytic reduction and seed/stopping proof |
| continuation_round2/integral_return/IR1_CLASSIFICATION.md | All 159 lines: ten rows, disjointness, periods and level counts |
| continuation_round2/integral_return_review/REVIEW_LEMMAS.md | All 257 lines: signed analytic review and explicit reversal closure |
| continuation_round2/integral_return_review/finite_core/REVIEW.md | All 292 lines: independent exact finite reconstruction and semantic comparison receipt |
| continuation_round2/integral_return_review/COORDINATOR_REVIEW.md | All 179 lines: complete-contract adjudication and separate symbolic receipt |
| Both original SOURCE_AUDIT.md files in those two directories | Complete: source ownership, exact action/parameter distinctions and access limits |

The full independent 325-line certifier and separate 66-line symbolic
checker in the supplement were additionally read, not executed.
The primary summary was read completely. The independent summary's
result, input-identity, comparison, environment and observed-bound
fields were read; its entire per-amplitude block was not manually
re-read. The corresponding complete review already records the
historical semantic comparison. CITATION_PREPARATION.md,
BASELINE_REPORT.md, the relevant evidence-preparation material and
supplement/README.md were inspected for provenance consistency.

The original analytic proof's actual hash is
5dcc9c6a84e4219a24fa177399ee1e7292e7217d8b83ab3dda4a90ceebd17e5d;
the final classification's is
e07855ea457056387c471677fffe0c0414bb6773e3583a3bfb1eb4a4f58a5336.
The copied proof/classification have those same identifiers.
The analytic review, coordinator review and finite review respectively
have hashes:

    4dfcf0c86ebdc2b1b3c85330fc771d6094c39c4d4d72989b44c0398a16814064
    fb1ce2d2a0acc8eaedeefa6fcb8f7882b039e7bf781a8724ede06368b894ba20
    68756fd37e79c5617ab4f35d0b98056b226e63a9f8c6efb199c95c2847ffa006

All six historical evidence identifiers printed in the appendix were
checked against the actual copied files. They agree:

| Evidence | Actual SHA-256 |
| --- | --- |
| Primary certifier | 750b4dbb54cacd1df11cc3929ed436cf8de9877048545f212cecc9bc03b75330 |
| Primary cycle JSONL | 352ffd5b5b188e32c347a4083559680e5d1bad12c8e6c6d7cd3dad6324935805 |
| Primary summary | 7000a021df6d38d82e14f6a22b3b764026e9545881aa4b7247cd041e5cf4af0b |
| Independent certifier | 8bd343b599f9ed6c605b255dfe60b544a81375975083fd5d7ffb2b18a1d6c7c3 |
| Independent cycle JSONL | 0432cd5d8c35fe3cf9fdc0027451bf2e85d04eb880da6da1c03457571fffe35b |
| Separate symbolic checker | be9ca47f3b7c8f94b43b25d6857f823f35f004407eff71807770dadf6dac40bd |

A read-only line count found 25851 records in each JSONL. No record
enumeration, output parser, symbolic checker or semantic comparison
was rerun. In particular, the historical 25851 individual comparisons
are credited to the preserved independent execution, not falsely
claimed as new reviewer execution or manual reading of every record.

## Mathematical audit

### 1. Object, quantifiers and invariant

Locations: sections/01_introduction.tex:4–15;
sections/02_classification.tex:4–38 and 44–63.

The map, inverse and invariant are consistent. With
\(w=yz+a-x\), the displayed factorization
\((w-x)(w+x-yz-a)\) is precisely the invariant difference.
The scalar recurrence determines both time directions, so its least
word period is exactly the first triple return. Cyclic rotation
alone defines an oriented orbit; reversal is explicitly not a
general quotient. The theorem quantifies every integer forcing
parameter and all integer triples, including singular ordinary
points. The union of possible periods is not mistaken for a
finite-order statement on the full polynomial phase space.

### 2. Uniform analytic reduction

Locations: sections/03_differences.tex:4–68;
sections/04_large_difference.tex:12–222.

The reviewer rederived the parameter-free identity from two adjacent
scalar recurrences and checked that two adjacent zero differences
propagate without dividing by a possibly zero center coefficient.
At a high coordinate, both neighboring entries really are \(m+e\);
the manuscript retains the corrected same sign. Integrality then
forces the claimed zero differences and the exact F4 channel.

For \(D>100\), the five centers are exhaustive. The endpoint cases
force an interval of length two. At \(s=-1\), the sign inequalities
exclude positive E; the negative case gives \(1\le\kappa\le4\),
and the sum of two later differences excludes 3 and 4. The
\(\kappa=1\) quadratic estimate is valid at every integer \(D>100\),
not only asymptotically. In the \(\kappa=2\) case, applying the key
identity with coefficients \(u+a+2\) and \(v+a+2\), whose difference
is D, gives \(|a|\le2\), including \(a=0\). The displayed later
differences exclude exactly \(a=1,2,-2\). The surviving \(a=-1,0\)
triples occur in F8 and F12; the printed F12 phase index 9 is correct.

For \(s=0,-2\), the second reversal need not preserve a positive
extremum. The manuscript correctly retains \(\varepsilon=\pm1\),
then uses \(|p|\ge L/2\), \(-5\le u\le3\), and integral
\(|q|<3\). The sign restrictions on p and q follow from their
sum and the two absolute bounds. All r=0,1,2 branches were checked,
including the two late contradictions for \(s=-2,\varepsilon=-1\).
The conservative product estimate in that r=2 branch is
\(2L^2-41L+138>L\) throughout the stated range. In the r=1 branch,
the small-coordinate possibilities are exhausted before using
\(|d_6|<3\), and \(u=0\) indeed gives \(d_7=2L-7>L\).

Reversal closure in lines 196–205 correctly restores the original
orientation, including the nontrivial parameter involution in F5.
The residual conclusion \(1\le D\le100\) and
\(-3D-1\le x_i\le3D-1\) follows from the proved alternatives.
No old unforced theorem is left as an unprinted proof step.

### 3. Complete finite algorithm, stopping and honest execution boundary

Locations: sections/05_finite_certificate.tex:11–160;
sections/appendix_certificate.tex:4–29 and 70–76.

The positive-extremum seed ranges include all equality cases. The
recovered a is forced algebraically, not a guessed scan interval.
The printed bounds match the actual primary code's interval
optimization, including \(u=-1\) or \(v=-1\), where no division
constraint may be imposed. Its orbit walk has only the proved
height/difference exits and an actual first return; it has no
iteration cutoff. On a finite nonexiting state set, injectivity
forces any first repeat to be the initial state. Thus the
termination proof applies to the actual loop.

The primary code restores both reversals and canonicalizes only by
rotation. The manuscript's independent algorithm retains both
extremal signs directly, uses the correct zero-coefficient interval
rules, traverses the inverse bijection, and reconstructs the
ordinary forward word. A complete triple-state set at fixed a
determines its directed transitions, so its identifier does not
silently quotient by reversal.

The family proposal method is sufficient: relevant parameters are
fixed by a, occur among the word's coordinates, or are its maximum
absolute coordinate for the standard F12 range. The primary and
independent F5 parameterizations differ by a rotation and
\(t\mapsto-1-t\), but both candidate rules cover exactly the
applicable family matches; this is not an orientation merger.
Independent parsing/comparison occurs only after discovery. The
appendix correctly states that removable Python assertions require
ordinary execution without optimization and that reproduction
should use a scratch copy because the historical scripts write
their outputs beside their sources.

Locations: figures/TABLE_certificate.tex:10–15;
sections/05_finite_certificate.tex:162–191.

All displayed partitions, family totals, two exceptions, reversal
counts and observed bounds match the historical summaries/review.
The 12/18 observed lengths are not called input cutoffs; the forcing
range is not an imposed parameter interval. The forward/inverse
nine-seed exit-category exchange is correctly explained. The
finite output is not substituted for the unbounded global families.

### 4. Full ten-row table, least periods and disjointness

Locations: figures/TABLE_classification.tex:20–32;
sections/06_least_periods.tex:4–90.

Every word, forcing relation, invariant formula and range matches
the accepted classification. Direct polynomial substitutions and
the printed recurrence suffice for the family-existence assertions;
the old symbolic receipt is additional disclosed checking, not an
unprinted mathematical premise.

| Row(s) | Guard/identification checked in the actual manuscript |
| --- | --- |
| F1/F2 | Equality versus strict ordering of alternating entries; one ordering of each genuine two-cycle |
| F3 | Only \(t=-2\) is fixed; a determines t uniquely |
| F4 | Only \(2t=a+1\) has shorter period; the two-step exchange is removed by the strict smaller-root convention, including extra occurrences of -1 |
| F5 | Never constant; the only duplicate parameters are 0 and -1; generic reversal is retained as a distinct cycle |
| E5 | Prime least period five, forcing -13 distinct from F5, reverse is rotation by one |
| F6 | \(t=0\) is excluded; nonzero t excludes periods 1,2,3; sign exchange is rotation by three |
| F8 | Only \(t=-1\) collapses to F4; \(t\ge0\) chooses one of the four-step exchanges |
| E9 | Entries at positions 0 and 3 exclude periods 1,3; reverse is rotation by six |
| F12 | Every proper divisor is explicitly excluded, including m=1; strict increase of its level on \(m\ge1\) proves parameter uniqueness |

Different least periods cannot overlap, and the two length-five rows
have different a. The F12 least-period proof is actually printed,
not delegated to the anonymous predecessor.

### 5. Exact per-level counts and native zeta

Locations: sections/07_level_counts.tex:15–97 and 99–136.

The two-cycle quadratic in \(P=uv\) together with the positive
square/parity test recovers every unordered pair and deduplicates
repeated roots. It does not divide by \(u-1\), so \(a=1\) is safe.
The four-cycle discriminant and smaller-root convention correctly
give one cycle rather than two. The F5 k=0 duplicate and k>0
oriented pair are correctly counted; all other positive-square
conditions exclude their degenerate endpoints. For F12, the parity
of a square equal to \(4k-7\) is automatic.

As adversarial hand checks, not executed tests:

- At \((a,k)=(1,0)\), the two-cycle quadratic has roots P=0,2,
  yielding the distinct pairs (0,1) and (1,2). Both are retained.
- At \((a,k)=(1,-1)\), its repeated root P=1 has zero
  discriminant, so no two-cycle is counted; the fixed point r=1
  is counted once.
- F3's excluded \(a=-8,t=-2,k=-28\) is exactly the fixed row.
- At \(a=-1,k=0\), F5 has one cycle, whereas \(k=2\)
  gives the two distinct parameters 1 and -2.
- At \(a=-1,k=1\), the degenerate F8 value contributes no
  eight-cycle and is already the F4 cycle.
- The \(m=1\) F12 word is genuinely period twelve at \(a=0,k=2\).

Finiteness is proved only after fixing both a and k. The ordinary
fixed-point formula weights each cycle by its length, and the
formal logarithmic identity gives exactly the stated finite
dynamical product. The last paragraph correctly rules out the
unrestricted all-level finite-count zeta, since F4 supplies
infinitely many four-cycles at every fixed a.

## Sources, ownership and bibliography

Locations: sections/01_introduction.tex:30–68;
figures/TABLE_ownership.tex:12–22; references.bib:1–55.

All six BibTeX entries are cited in the actual PDF. The paper
deducts the classical cubic/trace framework, the known four-step
family and the entire a=0 classification. Whole-group orbit
quantifiers are not exchanged for this one fixed forced map.
Hone's multiplicative coefficient is not renamed additive forcing.
The anonymous C413 manuscript is explicitly an internal manuscript,
not a fabricated journal publication; its proof is not a hidden
dependency here. No worldwide-priority claim or additional
contribution count is asserted.

New bounded primary access in this manuscript review was:

- The [official Cantat–Loray publisher record](https://aif.centre-mersenne.org/item/AIF_2009__59_7_2927_0/),
  including actual author/title/volume/issue/pages/year/DOI metadata.
- [Cantat–Loray arXiv v2](https://arxiv.org/html/0711.1579v2),
  specifically the located Theorem C and surrounding group-action
  wording. The manuscript's explicit version locator avoids
  assigning that theorem number to the shorter journal layout.
- [Hone's primary preprint](https://arxiv.org/html/math/0601324v1),
  Proposition 1 and equations (11)–(14), which confirm the
  multiplicative product coefficient used in the comparison.
- [Humphries's version record](https://arxiv.org/abs/1611.02743v1),
  author/title/submission/version metadata and abstract. This was
  not a new full Theorem 1 or whole-paper reading.

The Roberts/Roberts–Baake metadata and body-attribution support,
Humphries's full theorem scope, and local predecessor metadata are
retained through the expressly read source/preparation receipts;
they are not claimed as new complete primary reads by this reviewer.
No new missing reference is required for a used theorem. There was
no fresh literature-search query, no source-PDF save, no manuscript
upload and no paid/external review API call.

The scientific limits in sections/08_scope.tex:4–41 correctly
separate ordinary integer dynamics from rational/scheme/group
questions and dynamical cycle factors from target Euler factors,
L-functions and root numbers. Internal AI review is not described
as human peer review.

## Optional improvements, not mandatory corrections

### O1 — Write the shifted center coefficients explicitly

Locator: sections/04_large_difference.tex:78–81, PDF page 5.

The centers are stated as \(u+a+1\) and \(v+a+1\), and the next
sentence refers compactly to bounds on their products with 2a.
Strictly, equation (7) bounds the products of 2a with the
centers plus one. The intended and valid calculation is

\[
 |2a(u+a+2)|,\ |2a(v+a+2)|\le2D.
\]

One of those two coefficients has magnitude at least D/2, hence
\(|a|\le2\). Printing this line would remove the small verbal
ambiguity. It does not change any branch or conclusion; the
correct shift is already determined by the preceding key identity.

### O2 — Qualify the first sentence of the finite section

Locator: sections/05_finite_certificate.tex:4, PDF page 7.

Suggested wording: “For an orbit remaining after the listed
channels have been removed, the bound D <= 100 is now a theorem.”
The present context and immediately preceding corollary already
make this meaning clear, but the unqualified first sentence could
be misread in isolation as bounding all symbolic-family amplitudes.

### O3 — Use the exact reversal conclusion in the positive-level case

Locator: sections/07_level_counts.tex:82–85, PDF page 12.

At k>0 the two F5 roots are always distinct reversed oriented
cycles, by the uniqueness proof in Section 6. Replacing
“generally the two reversed oriented cycles” with “the two
distinct reversed oriented cycles” would make the local statement
as precise as the already correct count. The weaker current
wording does not introduce an incorrect count.

No new experiment, plot, page-count compression, artificial
related-work quota, anonymous-author identity change or additional
reviewer model call is requested.

## Round-one handoff and limitations

This report is the full raw output of this independent first
manuscript review, not a summary of an unavailable outside
conversation. The auto-paper-improvement-loop and research-review
skills were read in full and applied using the approved current-team
mathematical-paper fallback. They require preserving genuine
versions and later review/recompile gates; they do not justify
inventing a flaw, an execution, a numerical score or an ML-venue
requirement.

The reviewer wrote only this assigned report. Author manuscript
files, baseline PDFs, historical mathematical evidence and global
state were not edited. No mathematical program, compiler, Git
mutation or release checker was run. The old mathematical PASS
labels were not treated as manuscript-transcription approval:
the actual complete new TeX/Bib/listing and PDF text were read,
and the critical branches and arithmetic identities were separately
checked as recorded above.

Remaining mandatory scientific corrections in this review: **0**.
Remaining workflow gates: author disposition and first-round
compilation, the second actual full-text review/recompile pass, then final
reproducibility, visual and release checks under coordinator ownership.
