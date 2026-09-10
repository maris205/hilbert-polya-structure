# C433 — actual manuscript review, pass 1

2026-09-09 UTC, current-team internal nonauthor review by E8.
This reviews the actual first LaTeX/PDF manuscript, not a relabeling
of the earlier research-proof review. It is not external peer review,
publication acceptance, or a final reproducibility seal.

## 1. Disposition

**The central theorem and its complete typeset proof pass. The frozen
baseline manuscript requires three targeted minor repairs before it
can be treated as issue-free.**

- Critical issues: **0**.
- Major issues: **0**.
- Required minor issues: **3**, identified as M1–M3 below.
- Mathematical proof or body-theorem repairs: **0**.
- Citation applicability or bibliographic corrections required by this
  review: **0**.
- M1 is a mandatory mathematical-scope clarification in the abstract,
  not an optional stylistic preference. Its minor classification reflects
  that the formal theorem and proof already retain the missing condition.
- No numerical venue score, invented experiment, figure quota, artificial
  revision, or claim that a second manuscript pass has occurred is made.

The precise result remains the four-way equivalence

\[
 \mathrm{(CP)}
 \ \Longleftrightarrow\ I_g\ne(0)
 \ \Longleftrightarrow\ S_*\in I_g
 \ \Longleftrightarrow\
 F_n\mid S_*H_n\quad(1\le n\le6b^2+1),
\]

for every prime \(p\), every \(f\in\overline{\mathbb F}_p[x]\) of degree
\(d\ge2\) with \(f'=0\), and every nonzero rational weight \(g=A/B\)
in coprime form, where
\(b=\lceil m/(d-1)\rceil+1\), \(m=\max(\deg A,\deg B)\).
The visible native-period bound \(D=2b^2\) is conditional on (CP).
The result is a finite periodic-data decision, not a transfer-existence
theorem.

## 2. Inputs, read extent, and frozen identity

All manuscript paths below are relative to the C433 paper directory.
The following were actually read in full:

- main.tex, all 63 lines, and all eight included section files:
  54, 107, 114, 95, 146, 115, 61, and 33 lines respectively, totaling
  725 section lines.
- references.bib, all 31 lines; BUILD_RECORD.md, all 115 lines;
  and SOURCE_AUDIT.md, all 91 lines.
- The complete text of the actual 11-page main.pdf, including the
  development paragraph and both references on page 11.
- All 11 existing page renders in build/third/visuals/, individually
  viewed. This reviewer did not create substitute renders or a new PDF.
- The actual final R10 author report, all 713 lines, for the
  transcription, hypothesis, and proof-completeness comparison:
  ../../continuation_round10/a3_inseparable_finite_cp/REPORT.md.
  Its SHA256 is
  34a773edfce1e02e3dbe39f967888d4e49ba50d1384040f07d350c1e79779f1c.
  The earlier accepted E8 research review remains unchanged at
  6074afa280e6ac735074b1da70532b2d9adc38e0d6a56d16a209b920117c0951;
  that prior verdict was not used as a substitute for reading this
  manuscript.
- Applicable repository/batch instructions, the full BATCH_PLAN.md,
  and the full auto-paper-improvement-loop skill. The assigned
  current-team internal review and exclusive write scope supersede the
  skill's legacy external-model, ML-venue, scoring, and automatic-edit
  examples. This is pass 1 only.

The actual source/bibliography and section copies agree with the
immutable snapshots/v1_baseline copies. The actual main.pdf agrees
byte-for-byte with build/third/main.pdf, the original-round PDF, and
the baseline PDF. Recomputed input hashes are:

| Actual input | SHA256 |
| --- | --- |
| main.pdf / original-round baseline PDF | 8e58c361b89fe132183451f08b4817699ac02164e224a8cc6589d62e3bdb99f7 |
| main.tex | a8bc69d20c0e71385fbaed7e3a9c16987226af49b49d60142a407cbe5ee16dbf |
| references.bib | 89c47eaeca9645bc2579504a9edb789f5ef6225d67b868da13b07ece4f44d128 |
| sections/01_introduction.tex | 057a027bfd646613a80dcdd9f1375f7ffa061d39d9664ddec2486dddae10f682 |
| sections/02_statement.tex | 3d6d5d65a715adb9a0c98f6257ab4f122491f02e81d9ff6e7458c8a0217b9f2a |
| sections/03_cycles.tex | 49bccc2a0ba02bb8634b78cdc69cd38fa217691db0df7df27ea4ab47e6f2486c |
| sections/04_extractor.tex | 20fc9ff6342288314cd71efcbdc1f9388455245b8186bf749809c103e662cb69 |
| sections/05_transfer.tex | d56317d4ec6ad9375b564472a48564fbeef60c314e4e533d2671fc94d891769e |
| sections/06_rank.tex | 53141c1b73f968333b4af2c180c678a50967df211c78f8190d95935b254fcc88 |
| sections/07_decision.tex | 88b84763f2ab5919de79d8d31b73ff40f6cfd06664b03e308dfb01c6b9477f4c |
| sections/08_conclusion.tex | d3b4d85628883a31ada3e68e211528cdf70ac9350f3d453128e3195a178d8ffb |
| BUILD_RECORD.md | e1e865cb14033b81014b0c93281cc3c4c65e0f0eff347580ab30022dc21069bc |
| SOURCE_AUDIT.md | fc5a379ed7889cb256aa0195e4b95988f3445a6446ad5c9238a3c8c77687104c |

The review binds these inputs. Later repairs require an explicit
response/change record and a newly identified manuscript snapshot.

## 3. Required repairs

### M1 — minor but mandatory: qualify the abstract's visible-period bound

**Location:** main.tex, lines 47–49, abstract on PDF page 1.
Also make the corresponding introduction summary at
sections/01_introduction.tex, lines 19–21, explicit for consistency.

The abstract says that each product-visible exceptional cycle has
native period at most \(D\), without explicitly saying that (CP)
holds. “Exceptional” is not defined there as a conditional hypothesis.
The body is correct: Theorem 2.1 says “If these conditions hold,”
and Proposition 6.2 assumes \(I_g\ne(0)\). The abstract should not
leave a reader to supply that essential condition.

This is necessary, not merely a preference for more cautious wording.
For a hand-checked counterexample to an unconditional reading, take

\[
 p=3,\qquad f(x)=x^3,\qquad g=-1,\qquad A=-1,\quad B=1.
\]

Here \(f'=0\), \(m=0\), \(b=1\), and \(D=2\). The polynomial
\(F_3=x^{27}-x\) has 27 distinct roots, of which precisely the
three roots of \(F_1=x^3-x\) are fixed. Since 3 is prime, the
remaining 24 points have ordinary least period 3. At every such point,

\[
 H_3=(-1)^3-1=-2=1\quad\text{in characteristic }3.
\]

Thus these cycles are product-visible with native period \(3>D\).
All are admissible because the weight is a nonzero constant.
There is no counterexample to the manuscript's actual theorem:
(CP) fails. Indeed, for every odd prime \(q\), the \(3^q-3\)
nonfixed roots of \(x^{3^q}-x\) give cycles of least period \(q\)
and native product \(-1\).

**Action:** make the abstract read, for example:
“Whenever this condition holds, each product-visible exceptional cycle
has native period at most \(D\) ...”.
In the introduction, say that the rank argument bounds each such
period “under the cofinite product condition.” Preserve the current
distinction from cycles on which both whole products vanish.
No theorem, constant, proof, or additional hypothesis needs changing.

**Closure check:** read the new abstract and introduction in both source
and rebuilt PDF; retain the explicit conditions already present in
Theorem 2.1 and Proposition 6.2. No new mathematical run is needed.

### M2 — minor: use the declared diagonal operator in the two block matrices

**Location:** sections/05_transfer.tex, lines 52 and 54,
equation (5.7), PDF page 7.

Both occurrences are bare diag(...), which TeX renders as a product
of italic letters rather than the intended operator. The correctly
declared \(\backslash\mathrm{diag}\) command already exists in main.tex,
line 24, and is used correctly in Section 6.

**Action:** replace just these two occurrences with the existing
LaTeX command \diag followed by the arguments.
The mathematical meaning is clear from context, so this is a
notation/typesetting repair, not a defect in the two-product argument.

**Closure check:** inspect equation (5.7) in the rebuilt PDF and ensure
the final LaTeX log remains free of unresolved references and errors.

### M3 — minor: explicitly disclose the actual internal nonauthor review

**Location:** sections/08_conclusion.tex, lines 22–33,
“Development and verification,” PDF pages 10–11.

The paragraph accurately discloses AI-assisted preparation, preceding
internal arguments, the coordinator's prior sketch and constants, and
the lack of an independent-origination claim. It does not explicitly
disclose the current team's internal nonauthor review, which
BATCH_PLAN.md, lines 17–23, requires separately from AI assistance.
The source/audit file records that earlier review, but that separate
record does not put the disclosure in the article.

**Action:** add a short truthful sentence, for example:
“The underlying argument also underwent current-team internal
nonauthor mathematical review; this was not external peer review or
publication acceptance.”
An equivalent accurate formulation is acceptable. Do not claim that
two actual manuscript passes or final release checks had already
finished when they had not.

**Closure check:** read the revised paragraph as printed, preserve the
existing shared-development acknowledgment, and ensure that preparation,
internal review, and external acceptance remain distinct.

## 4. Complete mathematical and transcription audit

The manuscript is self-contained at its stated scope. The following
checks concern the actual typeset argument, not a proposed repair.

### 4.1 Statement, clock, conjugacy, and the annihilator ideal

Section 2 retains every hypothesis and quantifier of the accepted
R10 theorem: all primes; all derivative-zero polynomials, not only
monomials or degrees that are powers of \(p\); nonmonic inputs;
arbitrary coprime nonzero numerator and denominator; unequal degrees;
unrestricted multiplicities; and \(m=0\).
Ordinary primitive cycles count each distinct point once. The clock
is the original map, and no native period divisible by \(p\) is
discarded. Definitions of \(F_n,H_n,S_*,I_g\), admissibility, and
product visibility are complete.

The new skew-map description gives the actual one-step domain
\(U\times\mathbb G_m\to\mathbb A^1\times\mathbb G_m\), explicitly
not a self-map of a presumed invariant \(U\). Its iterate formula is
only asserted along an admissible cycle.

Lemma 2.2 uses the genuine conjugacy \(x=ty\), with
\(c_dt^{d-1}=1\), and correctly transports
\(\widetilde F_n=t^{-1}F_n(ty)\),
\(\widetilde H_n=H_n(ty)\), and
\(\widetilde S_*=t^{-D}S_*(ty)\).
Scalar units preserve divisibility; there is no substitution of a
different dynamical clock.

Section 3 retains \(F_n'=-1\) at every return. Consequently all
return roots are simple, including when \(p\mid n\), and the
annihilator ideal is exactly the vanishing ideal of
\(\mathcal B=\bigcup_n\{F_n=0,H_n\ne0\}\).
The proof that (CP) is equivalent to its finiteness keeps the whole
products and observes native bad products at their native return.
Only finitely many cycles meet \(V(AB)\); their full union is finite
without an unsupported period or cardinality estimate.

### 4.2 Added derivative-filtered interface

The local criterion (3.5) is independently checked. If
\(F=(X-x_0)^eV\) with \(V(x_0)\ne0\), then for \(p\nmid e\)
the derivative has order \(e-1\), and local divisibility of
\(SF'H\) by \(F\) is equivalent to \(S(x_0)H(x_0)=0\).
For \(p\mid e\), the derivative is divisible by \((X-x_0)^e\)
and imposes no additional local condition. Thus the single formula
\(eS(x_0)H(x_0)=0\) in \(k\) is correct.

The text does not replace that criterion by pointwise \(F'H\).
It separates product visibility, derivative-filtered visibility at a
return, and native Jacobian visibility. The comparison table labels
its middle row as a local interface, not a general all-level
ordinary-product theorem.

Example 3.2 is correct: in characteristic three with \(f=x^2\),
\(F_2=x(x-1)^3\), \(F_2'=(x-1)^3\), and a constant weight
with \(c^2\ne1\) gives the claimed one-return distinction with
\(S=x\). Such a \(c\) exists in \(k^\times\).
The fixed point 1 has multiplicity one at its native return and
three at return 2. The text explicitly avoids claiming an all-return
counterexample, and the example is outside \(f'=0\) and not an
input to Theorem 2.1.

### 4.3 Digit algebra and locally finite coefficient extraction

Section 4 retains the actual cyclic quotient, total-degree reduction,
and monic triangular degree argument covering all \(d^n\) digit
monomials. The coefficient pairing is proved nondegenerate by
multiplying a degree-\(q\) nonzero remainder by
\(x^{d^n-1-q}\), rather than by an inappropriate trace argument.

For each input monomial, equation (4.6)

\[
 J_0-n(d-1)=(d-1)\sum_iq_i+\sum_i u_i
\]

bounds every nonnegative Laurent-expansion index. This supplies the
needed local finiteness. Cancellation of a defining relation
telescopes in those same locally finite expansions and leaves no
negative power of the canceled variable. The \(n=1\) case is
explicitly retained. The top digit coefficient is one and all other
digit coefficients are zero for this functional. No analytic
convergence, integer division, or characteristic-zero theorem has
silently entered.

### 4.4 Transfer states and all fixed-\(S\) returns

Section 5 retains the necessary bound
\(ds\le r+\deg h-d+1\), the exact incoming/outgoing indexing,
and the two whole products with exactly one minus sign.
The maximal-index argument bounds all cyclic states by
\(R=a+\ell\), where \(\ell=\deg S\).

Bulk paths satisfy \(s-a\le(r-a)/d\). The closed range \(0,\ldots,a\)
and the strict inequality \(d^{k_S}>\ell\) for positive \(\ell\)
give the claimed contraction, also when \(\ell\) is an exact power
of \(d\). The \(\ell=0\) convention is correct.

For \(n\ge k_S+1\), both endpoints of the distinguished prefix
are low; all high intermediate states remain in the prefix matrix
product. The reduction does not delete those paths.
The span of words of length at most \(j\) starts in dimension one,
stabilizes as soon as one step has no growth, and lies in
\(\operatorname{Mat}_{2b}(k)\) of dimension \(4b^2\).
Words through length \(4b^2-1\) therefore span all words.
Together with the prefix length and the explicit short-return cases,
this proves exactly the fixed-\(S\) horizon \(k_S+4b^2\).
No degree bound on an unknown exceptional polynomial is assumed.
M2 does not affect any of these mathematical steps.

### 4.5 Both evaluation ranks and individual-cycle persistence

Section 6 correctly improves the split-array rank bound to
\(\dim(\operatorname{Mat}_b(k)\oplus\operatorname{Mat}_b(k))=2b^2=D\).
This is a vector-space factorization, not a claim of nondegenerate
trace pairing.

Lagrange interpolation and \(F_n'=-1\) give the exact diagonal
factorization \(V\operatorname{diag}(-H_n(x))W^{\mathsf T}\)
over \(\mathcal B_n\). Both evaluation matrices have full column
rank when their digit-degree ranges are long enough. In particular,
the second map is evaluated at \(f^{\circ h}(x)\), and
\(f^{\circ h}\) permutes the ordinary finite set \(\mathcal B_n\)
even though \(f\) is inseparable. The left inverse of \(V\) and
right inverse of \(W^{\mathsf T}\) justify equality with
\(|\mathcal B_n|\); a mere upper rank estimate would not suffice.

The persistence step fixes one visible point and writes
\(H_{qn_0}(x)=\alpha^q-\beta^q\). Finite multiplicative orders
of its nonzero values permit arbitrarily large \(q=1+jM\),
including the one-sided-zero case. Finiteness of the already given
\(\mathcal B\) then permits both evaluation halves to be made
long enough. Each such \(\mathcal B_n\) contains the entire chosen
native cycle. Applying this separately gives its period at most
\(D\), with no assertion of simultaneous visibility or
\(|\mathcal B|\le D\). Proposition 6.2 states its hypothesis
correctly; only the abstract summary requires M1.

### 4.6 Unknown exceptions, final horizon, and boundaries

Section 7 uses the individual period bound to put every point of
\(\mathcal B\) in the zero set of
\(S_*=\prod_{r=1}^D F_r\).
Its degree is \(\sum_{r=1}^D d^r<d^{D+1}\), so
\(k_{S_*}\le D+1\) and the fixed-\(S_*\) horizon is at most
\(D+1+4b^2=3D+1=6b^2+1\).
Both directions of the finite equivalence are present.

The text correctly exempts support cycles having both a numerator
and denominator zero: both whole products vanish, and their periods
are not bounded by this argument. A one-sided support cycle is
visible and is covered conditionally. No individual support
multiplicity is reduced modulo \(p\), and no rational factor is
required separately to satisfy (CP).

The \(m=0\) constants \(a=0,b=1,D=2,N=7\), characteristic two
where \(-1=1\ne0\), and every return integer through \(N\) are
retained. A nontrivial constant phase is not removed from the
two-product matrices. The stated computation is a finite algebraic
decision over a finite field containing the coefficients, not a
field-size-independent runtime, optimal cutoff, or implemented census.
The conclusion makes no rational/algebraic transfer-existence,
MS6, general separable-map, Euler-factor, or root-number claim.

## 5. Actual source applicability and attribution

Only the two actual bibliography entries were checked for their
precise use. No new broad literature search was performed, and
worldwide priority is not certified by this manuscript review.

For Cattani–Dickenstein–Sturmfels, the actual primary preprint was
read for its setup and the complete relevant Section 4 normal-form
argument, including Lemma 4.2 and Theorems 4.3 and 4.9.
The article's references to Section 4 explicitly identify the
preprint version. This source provides classical ownership/context,
not the positive-characteristic extractor used in the proof.
The manuscript proves that extractor directly. The published
chapter's authors, title, book, volume 143, pages 135–164, year 1996,
and DOI were checked against publisher metadata; no claim to have
read its paywalled publisher PDF is made.
[Primary preprint](https://arxiv.org/pdf/alg-geom/9404011);
[publisher chapter record](https://link.springer.com/chapter/10.1007/978-3-0348-9104-2_8).

For Kiefer–Murawski–Ouaknine–Wachter–Worrell, the actual Section 3
setup and Proposition 3.1 were read in the publisher-linked primary
arXiv PDF, pages 4–5. They explicitly allow an arbitrary field and
give the finite word-span/witness principle. Although the paper's
title and complexity results concern rational weights, the cited
proposition is not restricted to characteristic zero. The manuscript's
matrix-space span proof is included in full and imports no Gram,
positivity, or complexity conclusion. Publisher metadata and the
actual BibTeX export agree with the manuscript's bibliography and
printed reference. Attempts to use the TUM copy and to reopen the
publisher PDF encountered retrieval errors; the linked primary arXiv
copy provided the required passage, so access to that passage is not
being inferred from a search snippet.
[Primary paper, Section 3 and Proposition 3.1](https://arxiv.org/pdf/1302.2818);
[publisher record](https://lmcs.episciences.org/908);
[publisher bibliography export](https://lmcs.episciences.org/908/bibtex).

No additional reference is required to repair the proof as written.
This precise applicability check is separate from the coordinator's
source/substantiality adjudication. Shared-development provenance is
already honestly acknowledged; M3 concerns explicit review disclosure,
not a hidden mathematical dependency or a fabricated citation.

## 6. Actual PDF and build inspection

The inspected PDF has 11 pages and 374341 bytes and is an anonymous
English 11 pt article with one-inch margins. All 11 existing rendered
pages were viewed; the theorem, equations, comparison table, prose,
and references are legible, with no clipping or overlap observed.
Equation (5.7)'s italic bare diag is visible and is recorded in M2.
The full theorem fits on page 3. The conclusion/development paragraph
continues onto page 11 before the references; there is no missing
appendix or untypeset central proof.

The actual final engine and bibliography logs were checked for
warnings, overfull/underfull boxes, undefined items, and errors:
no matching final-log entries were found. The actual pdffonts
output lists 22 font entries, all embedded, subsetted, and with
Unicode mappings. The complete PDF text was read for resolved
references and citations. The audit distinguishes those final logs
from the preserved cumulative output of earlier unsuccessful or
intermediate author passes.

The documented first failed build and subsequent successful baseline
attempts are not recast as final clean reproducibility builds.
The deterministic PDF timestamp is not represented as an actual
wall-clock build time. This reviewer neither compiled nor modified
a source/PDF file and does not certify a later release gate.

## 7. Handoff and remaining work

The coordinator should adjudicate M1–M3, then have the author make
the scoped changes, record them against this frozen input, and
produce the revised source/PDF for an explicitly assigned pass 2.
The abstract's (CP) qualifier is necessary even though no change
to the main proof is needed.

This review does not itself apply the repairs, authorize broader
research, or claim final acceptance. The only new file written by
this reviewer is this allocated pass-1 report. Mathematical
programs/experiments: zero. New agents: zero. External-model/API
review calls: zero. New compilation/rendering, package installation,
Git, evaluator, old/shared-file, author-source, or PDF edits: zero.
Read-only file inspection and precise primary-source browsing were
used. All baseline and earlier proof artifacts remain frozen.

**Final pass-1 disposition: body theorem and proof PASS; manuscript
requires the three listed minor repairs. No other mandatory issue
was found within the actual full-read scope.**
