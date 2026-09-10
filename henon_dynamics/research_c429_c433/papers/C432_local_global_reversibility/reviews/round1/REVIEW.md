# C432 — actual manuscript review, pass 1

Current-team nonauthor internal mathematics review, 2026-09-09 UTC.
This pass reviews the actual eight-page article, not only the earlier
R5 proof package or admission decision.

## 1. Outcome and ranked findings

**No required repair identified.** The frozen manuscript contains a
complete proof of its stated all-place counterexample and its supporting
number-field family classification. Compression into the article has
not removed the whole-group, translation-image, scalar-component, or
original-field arguments on which exhaustiveness depends.

| Severity | Open actionable findings |
| --- | --- |
| Critical | None identified. |
| Major | None identified. |
| Minor | None requiring an author change identified. |

There is no recommendation to invent a revision merely to give this
review loop a changed version. This is a first-pass mathematical and
source-applicability finding, not a publication score, human peer review,
acceptance, formal Route-A evaluation, final-release certificate, or the
coordinator's adjudication. The separately required second actual
manuscript pass remains pending.

## 2. Exact inputs and actual read extent

Paths in this first table are relative to the manuscript directory.
Every listed source file was read completely. The current PDF was
independently extracted with `pdftotext -layout` and read on all eight
pages, in separate pages 1–4 and pages 5–8 calls after an initial combined
tool response was truncated. No unread truncation is counted as a read.

| Input | Extent | SHA256 |
| --- | --- | --- |
| `main.pdf` | All 8 pages of extracted text; 341,782 bytes | `d1f0c9bcab429d955b8700c2ce5bcc811f40f1f77f9bf7655ab8a4af0942a9aa` |
| `main.tex` | All 53 lines | `e83ee44b45b9a4be1e98a150ec05514a3f47fcbc3f87342da90cfed55d3201c8` |
| `sections/00_abstract.tex` | All 15 lines | `ef3ccceef4dedb08c052bf56563f6976100ac9d38b8a87419c71c543760d3ed8` |
| `sections/01_introduction.tex` | All 129 lines | `68852fd93b21c6c7322bd9230170db19f142281d3d7d6dd4c5419d51b80dafc9` |
| `sections/02_axis.tex` | All 154 lines | `f49282b52048a15046c3bb2be8644f252ef77e8f6e0df3b48f6e5eac41acecb0` |
| `sections/03_centralizer.tex` | All 95 lines | `a5eb22a9144d4893e896aae6f222e917d5f337a2315a5d7b8f2a4af99f0fad56` |
| `sections/04_descent.tex` | All 86 lines | `15e6b2f06402a64c62e4c2bb7cd787b47f4acb4a80cb26f4c92a9a85da1cb930` |
| `sections/05_places.tex` | All 86 lines | `da4035fc48b59bad0e1a4f64f9c79bab2f05400f5e85496449f15c800eaf7ed7` |
| `sections/06_control.tex` | All 50 lines | `7bc226b0cfab97680f02b82e5e26efa648ce1d2ee3f4c4ae98e2fa3b2beca21f` |
| `figures/TABLE_local_places.tex` | All 21 lines | `102a0dac97aff1519c20e53122b731543ff0380f9a9ffa7568a42c33a1bcc7fb` |
| `references.bib` | All 46 lines | `a4ce6daf2a069c51bece1a08c45ad8f241c8cfca74b20fede1d6e5cac8b564b7` |
| `BUILD_RECORD.md` | All 173 lines | `343d6c01c11989d514c0bb760aca7dfbc840afc3418dc66bc0a8acfb0ee1f0dc` |
| `SOURCES.md` | All 102 lines | `04813dc535c7d6fc4d10140f7bd5f3a4483db05dbd240c2609422239128ef5d1` |
| `PAPER_PLAN.md` | All 49 lines | `30f3364801b0b7dbab2bd56c94eb45b7d93f62e45558452332011246618856ae` |

I also reread the complete following accepted R5 inputs, including the
actual proof and the preserved source/substantiality counterargument:

| Input relative to the batch | Lines | SHA256 |
| --- | ---: | --- |
| `continuation_round5/c4_reversor_local_global/PROOF_PACKAGE.md` | 491 | `99bf7efa1486df5a685347aac3bfa6d2c79ab45f241dc1b94c6a5a69b181143e` |
| `continuation_round5/reviews/e5_reversor_local_global/REVIEW.md` | 404 | `bb369ff50bac71a548207466c5b89e9fa93b2944d06a6fe767863e64792b81a2` |
| `continuation_round5/reviews/b1_reversor_admission/REVIEW.md` | 378 | `5cafc9a0f0e315e1959fb4db2a5ebf49a0379ca5fd31a5495010c8eb9dd5631b` |

The actual admission Section 5, complete batch outline, manuscript plan,
and applicable repository instructions supplied the contract, not the
proof of the typeset claims. The old author report was previously read
during R5; it was not separately reread in this manuscript pass and is
not needed in place of any typeset argument.

Read-only `cmp` checks found the current, baseline, and attempt-01 PDFs
byte-identical. The current main source and bibliography agree with
their baseline copies, and recursive read-only comparisons of the
section and table directories found no differences. These comparisons
identify the reviewed bytes; they are not mathematical evidence.

## 3. Statement and quantifier preservation

Theorem 1.1 uses exactly

$$
K=\mathbb Q(\sqrt7),\qquad
F=H_{4,7}H_{1/16,15}H_{16,15}H_{1/4,7},\qquad
H_{c,d}(x,y)=(y,cy^d-x),
$$

with rightmost-first composition. Each factor has inverse
$(cx^d-y,x)$ and determinant one. This is a nonempty allowed Hénon
word. Rational coefficients do not replace its specified base field
by $\mathbb Q$. One application of the full word is used throughout.

The original implication asks about every finite and infinite place
and arbitrary polynomial automorphisms as prospective reversors.
The local maps are allowed to vary with the place. The global negative
statement imposes no degree bound, order bound, affine restriction,
or involution restriction. The explicit affine involutions are the
constructed local witnesses, not an assumption on a hypothetical
global witness.

Theorem 1.2 retains every number field $L$, every $a\in L^\times$,
all integers $j$, and the exact equality

$$
\operatorname{Rev}_L(F_a)
=\{F_a^jR_t:j\in\mathbb Z,\ t\in L^\times,\ t^8=a^2\},
\qquad R_t=(t^{-1}y,tx).
$$

The abstract, theorem statements, subsequent proofs, and conclusion
have these same scopes. The notation $F_0$ is expressly the monic
word, equal to $F_a$ at $a=1$, not evaluation at an excluded zero
parameter. The distinction between the reversor coset and the union
of reversors with the centralizer is also explicit.

## 4. Full polynomial group, intrinsic turns, and native powers

Article Section 2 includes the decisive proof rather than a reference
to an unpublished Markdown supplement.

The imported equality is the Jung–van der Kulk amalgam for the entire
$\operatorname{Aut}_{\mathbb C}(\mathbb A^2)$. The coset graph is
connected, and a non-backtracking circuit contradicts the stated
reduced-word theorem. It is therefore a tree; vertex-type preservation
excludes edge inversions. No smaller ansatz group is substituted.

The eight alternating syllables of
$F_0=\tau e_7\tau e_{15}\tau e_{15}\tau e_7$ are cyclically reduced.
The prefix edges and their signed native translates join without
backtracking. Their line has native displacement eight. The displacement
formula $d(z,F_0z)=8+2d(z,\mathcal L)$ proves that it is the complete
minimal-displacement set. Consequently every centralizer member
preserves it. A reflection cannot commute with its nonzero translation,
and vertex types force an even integral displacement.

Lemma 2.2 checks each source of ambiguity in the turn label:
vertex representative, the two right edge representatives, exchange
of the two edges, and arbitrary left group action. In particular,
triangular affine multiplication cannot cancel the leading degree
of a nonlinear elementary map. The label is intrinsic to the turn,
not merely to the author's displayed word.

The repeated sequence $(7,15,15,7)$ has least positive shift four:
shifts one and two fail at the first entry, and shift three at the
second. Thus the full translation image is contained in eight-edge
multiples. The original $F_0$ attains eight, so it generates that
image. Proposition 2.3 legitimately removes a signed native power
from every commuting polynomial automorphism. A hidden shorter root
or twisted root cannot supply an additional translation component.

## 5. Exhaustive centralizer and reversing coset

Section 3 begins with the actual remaining pointwise-axis centralizer.
The stabilizers of $\mathcal B$ and $\tau\mathcal B$ force a diagonal
linear part but initially retain both translations. The additional
prefix-edge pairs force every conjugate $P_i^{-1}h_0P_i$ to be diagonal
affine, including the pair in the next segment at $i=4$.

The displayed identity

$$
H_d^{-1}(\alpha x+c,\beta y+e)H_d
=((\alpha y+c)^d-\beta y^d+\beta x-e,\alpha y+c)
$$

has the correct order and signs. The degree-$d$ term gives
$\beta=\alpha^d$; the next coefficient kills $c$ in characteristic
zero. The following factor kills $e$. Neither translation was
silently normalized away.

The four surviving conditions are precisely
$\beta=\alpha^7$, $\alpha=\beta^{15}$,
$\beta=\alpha^{15}$, $\alpha=\beta^7$.
They are equivalent to $\alpha^8=1$ and $\beta=\alpha^{-1}$.
Conversely each corresponding $S_\zeta$ really commutes with the
four-factor word: each factor inverts its diagonal parameter.
Together with Proposition 2.3 this proves the full centralizer
equality, not only a commuting subgroup. Its direct-product assertion
uses the nonzero displacement of every nontrivial native power.

The palindromic word and $\tau H_d\tau=H_d^{-1}$ give one geometric
reversor. Multiplication by that involution identifies every reversor
with a member of the computed centralizer. This proves Corollary 3.2
without assuming any order or degree for the original reversor.

## 6. Scalar twist and every original-field component

Both alternating identities in (4.1) are correct. With $u^8=a$,
their four-factor product gives $A_u^{-1}F_0A_u=F_a$, including
the ordered degree-fifteen coefficients $a^{-2}$ and $a^2$.
The conjugated swap is $R_{u^2}$.

The identity $S_\zeta R_{u^2}=R_{\zeta^{-1}u^2}$ supplies all eight
roots of $t^8=a^2$. The article explicitly keeps the roots with
$t^4=-a$; it does not accidentally replace the criterion by $t^4=a$.
Because the geometric centralizer equality was exhaustive, the
resulting equality (4.4) is exhaustive as well.

For any $L$-defined reversor $R=F_a^jR_t$, the operation
$F_a^{-j}R=R_t$ stays within $\operatorname{Aut}_L(\mathbb A^2)$
for either sign of $j$. Reading its second-coordinate coefficient
forces $t\in L^\times$. This rules out coefficient cancellation as
an escape in a high-degree component. Conversely every such root
gives an $L$-defined reversor and all its native-power translates.
This proves Theorem 1.2 for the stated entire number-field family.

Lemma 4.1 separately proves sufficiency over any characteristic-zero
field by algebraic identities in an algebraic closure, followed by
descent of an identity whose coefficients are already in the field.
It does not invoke the complex classification over a completion or
require an embedding of that completion into $\mathbb C$.

## 7. Every place and the nonlinear control

Proposition 5.1's arithmetic is complete in the actual article:

- At every odd rational prime, the quadratic-character argument gives
  a nonzero square among $2,-2,-1$. The simple-root Hensel lift gives
  an eighth root of $16$ already in $\mathbb Q_p$, and hence in every
  $K_v$ above it. The ramified prime seven is included.
- At two, $7$ is nonsquare, so there is one actual dyadic completion.
  The strict strong-Hensel inequality for $X^2+7$ at $1$ is $3>2$,
  giving $b^2=-7$ in $\mathbb Q_2$. Then $\sqrt7/b$ is an element
  of that same completion with square $-1$. Thus $1+i$ is the needed
  root in $K_v=\mathbb Q_2(\sqrt7)=\mathbb Q_2(i)$; no extension
  of a deficient completion has been substituted.
- Both infinite completions are $\mathbb R$ and contain $\sqrt2$.
  There are no complex places.
- A global root would be $\pm\sqrt2$ in the real field $K$.
  Squaring $b+c\sqrt7$ forces $bc=0$ and a rational square equal
  to $2$ or $2/7$, impossible by valuation parity.

The place table agrees with these proofs and does not replace them.
Combining this exact arithmetic with Theorem 1.2 and Lemma 4.1 proves
Theorem 1.1 with every original completion retained.

The Section 6 control also survives compression. For
$T=H_{4,7}H_{1/4,7}$, the displayed nonlinear involutions satisfy
$T=E_2E_1$ and $E_1TE_1=T^{-1}$ over $K$.
The second coordinate of $R_tTR_t$ is $(t^8/4)x^7-y$, while that
of $T^{-1}$ is $4x^7-y$. Thus failure of the selected affine
equation $t^8=16$ is compatible with genuine global nonlinear
reversibility. The control is not mislabelled a counterexample and
explains why component exhaustion matters for the four-factor word.

## 8. Source applicability and ownership

The following primary-source passages and metadata were independently
accessed in this pass, in addition to reading the manuscript's source
record. This is bounded checking of its four cited works, not a fresh
worldwide novelty search.

- Gómez–Meiss: the author-hosted published PDF's first-page metadata,
  Section 2.1 and Theorem 3, Section 2.2's conjugacy statement and proof,
  and the relevant Theorem 1/Theorem 7/Corollary 9 subgroup statements
  support the claimed group input and prior normal-form ownership.
  The article does not mistake the commuting-subgroup inclusion for
  its needed centralizer equality.
  [Published PDF](https://amath.colorado.edu/faculty/jdm/papers/Reversors.pdf).
- Baake–Roberts: the arXiv record confirms Nonlinearity 18 (2005),
  791–816 and DOI 10.1088/0951-7715/18/2/017. The primary preprint's
  Section 2 Facts 1–2 and Proposition 1 with its proof give the
  whole-group reduced-word input. Theorem 2 and Corollary 1 require
  only two roots of unity for their simpler later conclusions; the
  manuscript correctly does not apply that hypothesis over $\mathbb C$.
  [Record](https://arxiv.org/abs/math/0501151),
  [preprint](https://arxiv.org/pdf/math/0501151v1).
- Cantat–Dujardin: the publisher record and final Section 2.2 example,
  including its full-centralizer explanation, support the explicit
  deduction of the scalar-root and original-field conjugacy mechanism.
  Taking its exponent eight and coefficient sixteen over the Wang
  field gives an analogous arbitrary-pair all-place obstruction;
  this is an inference from the displayed mechanism, not a theorem
  stated in the source. The manuscript's wording makes this distinction
  and retains only the constrained inverse-pair realization as its
  increment. [Publisher article](https://londmathsoc.onlinelibrary.wiley.com/doi/10.1112/blms.13164).
- Song Wang: the publisher record confirms the 2015 Science China
  Mathematics citation, volume 58, 1589–1606 and its DOI. The actual
  mathematical passage read is Section 2.1, Proposition 2.1 and the
  following printed-page-7 remark in the accessible 2014 preprint.
  It identifies precisely $\mathbb Q(\sqrt7)$, exponent eight, and
  class sixteen. Damaged extraction of the exceptional-set symbol
  is not used to prove any local claim; the article supplies its own
  full place calculation.
  [Publisher metadata](https://link.springer.com/article/10.1007/s11425-015-4977-5),
  [preprint passage](https://arxiv.org/pdf/1401.0389v1).

All four BibTeX records agree with these checked primary records.
All four are actually cited. No new attribution problem appeared
when comparing the abstract, introduction, proof dependencies,
limitations, and bibliography with the accepted R5 source deductions.

This reviewer does not claim a new reading of the original 1948/1950
Wang papers, of all proofs in the four cited works, or of B1's other
source papers. B1's readings are not relabelled as this pass's own.
No dedicated correction/retraction audit or current-open-status claim
is made. No source PDF was saved, and no private manuscript was uploaded.

## 9. Presentation, disclosure, and artifact boundary

The extracted PDF includes all six numbered sections, the abstract,
the exact table, all central arguments, and all four references.
The typeset statements and equations agree with the source audit above.
There is no dependence on a local working-note link for a new proof.
The text does not claim a minimal degree, a shortest word, a universal
classification of reversible words, or a novel Wang obstruction or
twisting method.

Reversibility is defined algebraically. The article makes no physical
time-reversal, quantum, Euler-factor, root-number, automorphy, or
Hilbert–Pólya claim. Its preparation paragraph accurately distinguishes
AI assistance and internal review from external peer review and
publication acceptance; the previously completed R5 reviews make that
historical internal-review statement meaningful even at this baseline.

`pdfinfo` independently confirms eight pages and the supplied size.
This pass read the author build/visual-inspection record but did not
rerun compilation, fonts, logs, or page rendering and did not perform
an independent all-page visual inspection. It therefore does not
certify final visual QA or the two fresh deterministic release builds.
Those separate gates remain with the coordinator's workflow.

## 10. Execution and handoff

The complete auto-paper-improvement-loop entry instructions governed
this actual first manuscript pass and the later same-thread follow-up.
The research-review framework supplied the critical proof audit, and
research-lit supplied bounded primary-source/ownership checking.
The repository's current-team anonymous mathematics contract overrides
legacy external-model, ML-venue, experiment, score, and automatic
notification examples. No skill default expands this review's write
ownership or authorizes a rewrite.

There were no configured Zotero/Obsidian tools in the callable list.
A bounded filename scan returned no specialist source PDF/fetch-script
match in the existing checked paths; the separate `literature/` path
was absent and that scan returned an error for it. Actual source access
used the exact cited primary URLs and within-source lookups, not an
unreported broad search or an arXiv download. That diagnostic error
does not affect the source passages actually read above.

Only this allocated `reviews/round1/REVIEW.md` was written. No author
source, PDF, baseline, build output, old proof/review, shared state,
evaluation, Git object, or release record was changed. No mathematical
program, computer-algebra test, nested agent, external model/API,
GPU run, or publication action was performed.

The review is ready for coordinator adjudication, with zero open
required repairs. After full report readback and final hash checks,
these review bytes are to remain frozen. The author baseline remains
unchanged; pass 2 is not started or claimed by this document.
