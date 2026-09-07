# C417 nonauthor manuscript review

Status: **PASS — no manuscript mathematical, source-attribution or
proof-completeness blocker identified.** This is a current-team,
nonauthor manuscript review of the actual article and author PDF. It is
not human peer review, a global-priority certificate, a fresh execution
of the frozen arithmetic certificates, or the final release gate.

Reviewed on 2026-09-07 UTC. The reviewer did not author C417's manuscript,
producer or frozen proof. Only this review file was written in C417 by
this review pass; the author's manuscript and mathematical inputs were
left unchanged.

## 1. Actual inputs and review scope

Read completely:

- `main.tex`, `math_commands.tex`, all ten included section files, and
  `references.bib`: all twelve TeX files and the bibliography, totaling
  1,246 source lines. This includes the complete certificate appendix,
  not just the main theorem and abstract.
- All 17 pages of the actual PDF's extracted text, read through its
  references; all five tables and all three pseudocode listings were
  included in that read.
- `CITATION_AUDIT.md` and `AUTHOR_HANDOFF.md`.
- The complete frozen `../../cubic_arithmetic/PROOF_PACKAGE.md`,
  `SOURCE_AUDIT.md` and `REVIEW_CUBIC_ROOT.md`; the complete producer
  `certify_cubic.py` was also read, without executing it.

The reviewed `main.pdf` is 17 pages, 392,206 bytes, and is identical
to `build_author/main.pdf`. Both files were freshly hash-checked:

```text
0615b9fb914114f8acc8aa37631a1c946862f3e245529334b62f6f64e2c21313
```

The research-review skill was used for an adversarial claim/evidence
and source-ownership audit. Its legacy external-model default was
superseded by the coordinator's explicit current-team review scope.
No external model, unpublished-manuscript upload, or new research
candidate was introduced.

## 2. Infinite-family reduction and coexistence

**Pass.** The theorem is stated for every monic cubic
`f(t)=t^3+bt^2+ct+a` with `a,b,c` integral, on all rational points of
`H_f(x,y)=(y,f(y)-x)`, determinant +1. Neither a rational-coefficient
family nor a determinant-minus-one map is silently substituted.

The maximal-prime-adic-coordinate argument establishes integrality.
The real escape bound is common to every cycle of one fixed polynomial,
so the union of its integral periodic points is finite *before* its
global coordinate extrema are chosen. Thus the later diameter belongs
to the entire periodic set, not to a selected cycle. This is the key
logical prerequisite for the eleven-point coexistence conclusion.

After the integer translation, the endpoint constraints give integral
`q` between -2 and 2 and the integral third root `r=-B-D`.
The secant bound `|t(t-D)(t-r)| <= 2D` applies to every coordinate
of every coexisting cycle. The factor two, endpoint value constraints
and translation convention are correct.

Empty, one-symbol and diameter-one cases are explicitly separated.
The affine-root case has at most nine ordered pairs; its two parabolic
traces receive actual periodicity arguments rather than an unsupported
finite-order assertion. In particular trace two forces `A=0`, and
periodicity then removes the constant first difference. The separate
two-symbol bound is at most four.

For diameter at least ten, the excluded interior range and the four
possible nonroot endpoint symbols force the five lower third-root
cases or their reflections. The reflection formula
`A_tilde=(2-q)D-A`, `r_tilde=D-r` preserves the family and ordinary
time. The stated large alphabets cover every required symbol.

For diameter at least sixteen, every edge discrepancy is affine in
`D`, and its constant part has magnitude at most fourteen. The strict
inequality `14 < D` proves that a numerical edge is equivalent to an
affine-polynomial identity. The ninety symbolic graphs therefore cover
all such diameters, not a sample at a chosen large diameter. The five
row counts and all 29 endpoint-using patterns are present in the PDF.

The article correctly distinguishes at most three coordinate values
*per cycle* from a false global three-value assertion. Its explicit
coexisting four-value example and the warning that endpoint filtering
is only necessary protect the proof from those two natural mistakes.
In particular, a retained auxiliary graph is never assumed to exclude
all cycles outside its interval; the global-extrema argument supplies
the required containment for the actual map.

## 3. Finite complement and certificate transcription

**Pass, with computational-proof provenance retained.** For
`2 <= D <= 15`, an interior coordinate gives the complete bound
`-3 <= r <= D+3`. The additional ranges for `A,q` and
`0 <= A+qD <= 2D` follow from endpoint values. These are normalized
parameters after a proved reduction, not cutoffs on the original
coefficients.

Every relevant graph cycle is an actual orbit and every cycle of an
actual global-extrema tuple is included. The displayed counts
`(D+7)(4D+5)` account for all 9,373 endpoint-compatible tuples.
All fourteen manuscript table rows agree exactly with the frozen
proof, including the 1,235 retained tuples, period sets and per-row
maxima. The unique maximizing tuple is `(D,r,A,q)=(4,2,6,-1)`.

The appendix specifies the whole cycle extractor, both finite input
loops, endpoint filters, point counts, period/symbol statistics and
all-maximizer updates. The extractor's termination and no-loss/no-double-
count proof is supplied. Ordinary cyclic rotation merely changes the
starting coordinate; reversal is not used to merge cycles.

Read-only structural checks parsed all three displayed Python listings
successfully and compared the fourteen small-table rows to the frozen
Markdown table. No extracted function was executed. Semantic inspection
also checked the affine-pair encoding, endpoint-sum compatibility,
no-cancellation statistic and initial maximum of minus one: eleven is
an output of the specified enumeration, not a prescribed input.

The numeric evaluation remains the frozen exact computational part of
the proof. The separate root admission review records an independent
checker using periodic-vertex isolation, a whole-square small graph and
a different affine representation, with matching tables and maximizer.
That historical evidence was read and its scope preserved; it is not
presented as an execution by this manuscript reviewer. No producer,
cross-checker, independent frozen checker, coefficient scan or old
certificate was rerun. This is not proof-assistant verification.

## 4. Templates, equality and ordinary returns

**Pass.** Once the established period and per-cycle alphabet restrictions
are used, the word argument exhausts the two-symbol possibilities and
the three-symbol periods three, four and six. The six-word argument
handles both the absence of adjacent repeats and every position of the
third symbol after an adjacent double. It does not infer exhaustion
from a few examples.

The reciprocal lemma is valid for distinct nonzero integers and is
applied to the integral quadratic coefficient of the interpolant.
It forces the midpoint conditions in the centered four- and six-cycle
rows. All seven polynomial identities match the recurrence; parameter
ranges exclude lower-period degeneracies. The two orientations of a
three-distinct-symbol three-cycle are explicitly counted as two ordinary
cycles. The original quadratic coefficient in `R_{u,v}` is retained,
and the three-distinct-symbol identity does not leave a spurious free
quadratic coefficient.

The unique normalized maximizer yields
`g(t)=(t-2)^3-5(t-2)+4`. Undoing the translation gives exactly
`f(t)=(t-h)^3-5(t-h)+2h`, with integral `h`, and coefficient equations
`b=-3h`, `c=3h^2-5`, `a=-h^3+7h`. No exceptional coefficient branch
is dropped. Conversely the five displayed cycles of lengths
`1,2,2,3,3` are disjoint and give eleven points. The already proved
upper bound then excludes any further cycles; this sufficiency argument
is not circular.

The return-series corollary counts actual rational points with unit
weight and ordinary iterate time. The equality-family product
`1/((1-z)(1-z^2)^2(1-z^3)^2)` follows directly from those five cycles.
No scheme length, alternate return clock or reversal quotient enters.
No Euler-factor, root-number, automorphy or Hilbert–Pólya consequence
is claimed. `NO_BAD_EULER_OR_ROOT_NUMBER` remains unconditional.

## 5. Citation ownership and bounded novelty

**Pass within the explicit accessed-source boundary.** All five cited
keys have bibliography entries, with no extra unused key or unresolved
citation. The source comparison is actually in the article, not solely
in a sidecar audit.

The reviewer independently reaccessed Pezda's original journal record
and read the relevant original PDF through a read-only text stream,
including printed pages 95–97 and Theorem 2.1. The cycle-length list
is correctly distinguished from a bound on the entire periodic set.
The manuscript makes no false attribution of the cubic eleven-point
theorem. See the [original Pezda record](https://dml.cz/handle/10338.dmlcz/120574).

The relevant Section 11 of the [journal-hosted question survey](https://amj.math.stonybrook.edu/html-articles/Files-2015-2024/23-70/index.html)
was also read in this review. Its interpolation questions, determinant
scope and broader rational-coefficient boundedness questions are not
presented as having been solved here. The registered collective author
and bibliographic metadata are retained.

The current-batch primary checks of Ingram's actual v1 text and the
specified Kim–Krieger–Postolache–Szeto v2 support the article's careful
sign/coefficient distinctions. Ingram's verified journal metadata is
not represented as a new full read of that published text. The
integer-valued cubic `(t^3-7t)/6` is neither monic nor in `Z[t]`, and
sharing determinant +1 is not treated as equality of families.
Version and publication-date qualifications remain visible.

The local C412 title and anonymous author block were checked. Its
non-journal repository status and ownership of the quadratic result,
integrality, coordinate encoding and finite-complement methodology
are expressly credited. The residual claim is the full cubic
coexistence closure, exact templates and sharp equality locus, not a
claim that those general methods are new. No whole-literature priority
guarantee is asserted or supplied by this review.

## 6. Actual artifact checks and remaining release work

Read-only source checks found 45 unique labels, 76 reference uses and
five cited keys with matching entries. The actual final author engine
and bibliography logs contain no warning/error, unresolved-reference,
unresolved-citation, underfull or overfull matches; the no-match search
exit status is the normal value one, not a build failure. All twenty
listed font objects are embedded Type 1 fonts.

The reviewer actually viewed the retained rendered images of pages
**2, 3, 7, 15 and 16**. The template/comparison tables and arithmetic
listings were readable with no clipping or overlap. Page 7's float
spacing is not a content or legibility blocker. The full PDF text was
read, but these five images are a selected-page visual inspection,
not a claim that all seventeen rendered pages have been inspected.

**No author revision is required by this review.** The author PDF and
all mathematical claims are approved for the coordinator's subsequent
gates. Formal pinned evaluation, two fresh deterministic final builds,
every final page's visual inspection, final hash/manifest checks,
indexes and Git integration remain the coordinator's responsibility.
This PASS does not silently mark any of those gates complete.
