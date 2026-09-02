# P158 Hostile Review A — original report

**Review date:** 2026-09-02 UTC  
**Calibration:** `NOT_CALIBRATED`  
**Criteria binding:** `criteria_binding_unavailable`; no venue-fit claim is
made.  
**Execution boundary:** one role-separated adversarial review, not evidence of
independent error processes.  I did not consult a Review B.  No P158 author
file was modified during this review; this report is the only new paper-local
file, and the reviewer verifier is stored under the sequence review directory.

## Verdict

**REVISE — 0 Critical / 0 Major / 2 Minor.**

The theorem statement, the mandatory `n=5,t=2` zero-fibre boundary, the
every-target fibre law, both EGFs, the absorption CDF and first-hit law, the
tail/mean formulas, source subtraction, anonymity, `HOLD_EXTERNAL` status,
author verifier, and four-page PDF all survive independent audit.  The two
required repairs are local: replace one comma that currently appears where a
multiplication separator is intended in the mandatory boundary formula, and
either add a genuinely independent literal-update lane to the author verifier
or narrow its docstring's claim that this interface is checked.  Neither issue
changes a theorem, proof, table entry, or numerical conclusion.

## Strongest counter-argument

The strongest objection is not a mathematical counterexample but a
contribution-density and ownership challenge.  Once graph cuts, binary
histories, inclusion--exclusion, labelled EGFs, complete bipartite components,
and bicluster graphs are all assigned zero credit, the mechanism becomes a
short occupancy argument on antipodal binary words.  A skeptical reader could
therefore view the absorption CDF as merely the empty-target specialization of
the fibre formula and the image EGF as routine labelled-species bookkeeping,
leaving only the resource-sensitive every-target atlas as a plausible residual.
The current three references bound broad neighbourhoods, not the literal
history process; a direct owner using antipodal-code, cut-space, separating-
family, or intersection-of-cut-graphs terminology could still collapse that
residual.

This objection does not refute the manuscript as frozen.  The exact fibre
contains information absent from a static bicluster classification: component-
to-pair injection, component orientation, isolate occupancy, and the sharp
`r=R,z>0` obstruction.  The author also avoids novelty, priority, and complete-
ownership language and visibly retains `HOLD_EXTERNAL`.  Thus the correct
response is continued owner screening and conservative framing, not deletion
of a theorem that is internally valid and exactly checked.

## Independent theorem audit

| Interface | Independent reconstruction / attack | Verdict |
|---|---|---|
| literal process | Successive intersection with the `t` cut masks retains `uv` exactly when the two endpoint bits differ at every coordinate, equivalently when the two length-`t` words are complements. | PASS |
| `A_R(m)` | A complementary pair contributes `1+2(e^x-1)=2e^x-1`; multiplication over `R` distinguished pairs and binomial expansion give both forms of `A_R(m)`, including the printed zero-size conventions. | PASS |
| absorption / first hit | `G_t` is empty exactly when every word pair is one-sided.  Monotone edge deletion identifies this with `{T<=t}`, and consecutive CDF differences give the first-hit mass with the correct `F_0=0` offset. | PASS |
| tail / mean | One fixed edge survives with probability `2^{-t}`.  The union bound gives the displayed tail; the positive-integer tail identity gives `E T=1+sum_(t>=1)(1-F_t)` and the geometric upper bound. | PASS |
| image condition | Each two-sided pair forms one connected complete bipartite component; different pairs have no cross edges.  Components require distinct pairs, and an isolate cannot occupy a consumed pair, so `r<=R` and `z=0 or r<R` are necessary and sufficient. | PASS |
| every-target fibre | Inject the fixed labelled components into the `R` word pairs in `(R)_r` ways, orient their unique bipartitions in `2^r` ways, then place isolates one-sidedly on the unused pairs in `A_(R-r)(z)` ways.  The decoding is unique. | PASS |
| image EGF | A nontrivial labelled complete bipartite component has EGF `B(x)=(e^x-1)^2/2`.  Sets of fewer than `R` components allow arbitrary isolates; the exactly-`R` term must omit `e^x`. | PASS |

The theorem, abstract, proof, claims ledger, and frozen Stage-1 contract agree
on all these interfaces.  In particular, the fibre formula is not silently
claimed for `r>R`; those targets are separately assigned zero mass.

## Mandatory boundary attack

At `n=5,t=2`, there are `R=2` complementary word pairs.  Every graph made of
two disjoint labelled edges and one isolate has `r=2,z=1`.  The two edges must
consume both word pairs, after which either word offered to the isolate is
adjacent to the occupied opposite side of one component.  Hence no history
exists and

```text
(2)_2 * 2^2 * A_0(1) = 0.
```

There are 15 such labelled targets: five choices of isolate and three perfect
matchings of the other four vertices.  The reviewer verifier checks all 15,
not only one representative, and every observed and predicted fibre is zero.
The mathematical boundary is correct; the printed separator defect is Minor
finding m1 below.

## Exact-control audit

The paper-local verifier was cold-replayed twice with bytecode disabled.  Both
runs match `verification_output.txt` byte for byte, report **35,278 exact
assertions**, and preserve transcript SHA-256
`728c32e557e920c46022f3fe8d24fce1e5e303a3d43d823b6d22ae20d7a85fe8`.
It does enumerate every labelled simple target, including unobserved targets,
in all seven frozen boxes; compares the full fibre dictionary; checks the
empty state, image count, first edge moment, CDF monotonicity, and tail bound;
and uses exact standard-library integer arithmetic.

An independently written verifier is stored at
`docs/papers157_161_sequence/reviews/p158_a/verify_p158_review_a.py`.  It does
not import or call the author program.  It first runs the successive literal
intersections and only then compares the result with complementation.  It
checks every labelled target in six boxes, including the new `(n,t)=(3,2)`,
`(5,4)`, and `(6,3)` boxes; derives both EGF coefficients with exact rational
polynomial arithmetic; couples first-hit and CDF counts in one horizon sample
space; checks the positive-time mean offset; and exhausts all 15 mandatory
boundary targets.  It performs **1,351,844 exact assertions**.  Two cold runs
match `CANONICAL.txt` byte for byte.  Reviewer transcript SHA-256:
`e3d00b592cfd0118c6f6c06a460555aa4ab761ee03603037611cd6d4e2af4bbf`.

Finite enumeration remains counterexample pressure only.  Neither verifier is
proof, owner clearance, novelty evidence, or release authorization.

## Source and ownership audit

The three bibliography records and their uses are accurate:

- The [Elsevier record](https://www.sciencedirect.com/science/article/pii/S0012365X96001240)
  confirms Erdős--Pyber, *Discrete Mathematics* 170(1--3), 249--251 (1997),
  DOI `10.1016/S0012-365X(96)00124-0`; it studies complete-bipartite edge
  coverings, not the cumulative random process.
- The [Springer chapter record](https://link.springer.com/chapter/10.1007/978-3-540-79228-4_39)
  confirms Guo--Hüffner--Komusiewicz--Zhang, TAMC 2008, LNCS 4978, 445--456,
  and states that Bicluster Editing targets vertex-disjoint unions of complete
  bipartite subgraphs.
- The [primary arXiv record](https://arxiv.org/abs/1409.6021) and DOI metadata
  confirm Zhao--Yağan--Gligor, ANALCO 2015, 1--15, DOI
  `10.1137/1.9781611973761.1`.  Its edge rule is shared-item incidence, not
  exact complementarity of complete history words.

A bounded alternate-term screen for intersections of cut graphs, antipodal
binary labels, complementary codewords, and random cut absorption did not
locate the literal update together with the every-target fibre law.  This is
only a bounded non-hit.  The manuscript correctly assigns zero contribution
credit to the standard ingredients and does not turn the screen into a
novelty, priority, or ownership-completeness claim.

## Anonymity, external status, and PDF audit

The TeX source uses `\author{Anonymous}`.  PDF title, author, subject,
keywords, and custom metadata are blank; no identifying metadata, form,
JavaScript, or encryption is present.  `HOLD_EXTERNAL` is visible in the
paper and throughout the support package, and no text authorizes posting,
circulation, submission, or author contact.

Two isolated source-only builds using
`pdflatex -> bibtex -> pdflatex -> pdflatex` are byte-identical to each other,
`main.pdf`, and `main_round0_original.pdf`.  The artifact has four A4 pages,
352,360 bytes, and SHA-256
`bbe961298aa62adc54d34f15cc546ff3f14d7d4d29fd90dee2dcc6e2fff2e892`.
All 27 font rows are embedded, subsetted, and Unicode mapped.  The settled
build has no unresolved reference/citation, rerun request, BibTeX warning,
box warning, duplicate label, or error.  It emits one benign pdfTeX font-
expansion ordering warning already disclosed in `BUILD.md`.  All four pages
were rasterized and visually inspected; apart from m1's mathematical
separator, there is no clipping, overlap, malformed glyph, unreadable table,
or broken layout.

## Findings

### Critical

None.

### Major

None.

### Minor

#### m1 — The mandatory boundary display uses a comma instead of multiplication

- **Evidence anchor:** equation: Remark 2 after Equation (9), source line 141
  and PDF page 2 display `(2)_2, 2^2 A_0(1)=0`.
- **Confidence:** 5/5 — direct TeX and rendered-PDF inspection.
- **Why it matters:** the surrounding prose and final zero make the intended
  argument recoverable, so the theorem is unaffected.  Nevertheless, this is
  the mandatory sentinel formula that prevents the known false shorthand; it
  should not contain a punctuation mark that can be read as separating two
  expressions.
- **Minimum repair:** replace `(2)_2,2^2A_0(1)=0` by
  `(2)_2\,2^2A_0(1)=0` (or insert `\cdot` separators), then rebuild the PDF.

#### m2 — The author verifier claims a pathwise check that it defines rather than tests

- **Evidence anchor:** text: `verify_p158.py` docstring says “checks the
  pathwise complement representation”; function `graph_mask` constructs the
  observed graph directly from the XOR-complement condition.
- **Confidence:** 5/5 — line-by-line code audit and independent reimplementation.
- **Why it matters:** all target, fibre, EGF, and CDF checks are real, but this
  particular lane cannot detect an error between the successive update
  `G_s=G_(s-1) intersect C_s` and its word-complement compression because it
  uses only the compressed rule.  The proof is elementary and correct, so the
  defect is coverage wording, not mathematical evidence failure.
- **Minimum repair:** either add an independently coded successive-cut
  intersection and compare it against `graph_mask` for every enumerated
  history, or narrow the docstring and any control claim so they say that the
  complement representation is the enumeration interface rather than a
  separately verified identity.

## Required repair and re-review target

1. Correct the multiplication separator in the `n=5,t=2` boundary display.
2. Add a literal sequential-update lane to `verify_p158.py`, or narrow the
   verifier's pathwise-coverage claim.
3. Rebuild and confirm that the author transcript remains deterministic; if
   the verifier is enhanced, freeze a new transcript and update its assertion
   count and SHA consistently.

After those local repairs, Review A supports **PASS_INTERNAL / HOLD_EXTERNAL**,
subject to an independent Review B and continued direct-owner screening.  This
report does not authorize external posting, circulation, submission, author
contact, novelty, or priority claims.
