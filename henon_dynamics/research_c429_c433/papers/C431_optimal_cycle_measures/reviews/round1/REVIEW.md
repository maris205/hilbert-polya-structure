# C431 actual manuscript review — pass 1

## Verdict and review boundary

**Main theorem: PROVABLE AS STATED on the inspected manuscript.**
No critical or major mathematical defect was found. The full odd-prime,
arbitrary-field, fixed-multiplier, full-sequence claim survives this pass.
There is one **minor requested source-scope clarification**, R1 below,
and two optional presentation suggestions. R1 does not invalidate a
theorem, change its hypotheses, or require a new mathematical argument.

This is a nonauthor review of the actual first typeset C431 manuscript,
*Haar limits of optimal wild cycles*, not a relabeling of the earlier
research/admission review. The reviewer read the complete current
sources and bibliography, the entire extracted 12-page PDF, and all
twelve supplied page images. The accepted arithmetic and topology
proofs were read in their actual files and compared with the typeset
arguments. Source claims were also checked against primary passages.

The assigned scope is pass 1 only. The coordinator must adjudicate R1
and optional suggestions before author changes. A later same-thread
pass 2 must inspect the actual revised source and PDF. This report is
not a second review, a formal route evaluation, a release seal, an
external peer review, or a journal-readiness certification.

The full auto-paper-improvement-loop, research-review and proof-writer
instructions were applied as internal mathematical review guidance.
The current task explicitly overrides their external-model, upload,
ML-score, experiment and automatic-author-edit defaults. No external
review API, new agent, mathematics program, source edit, recompilation,
Git mutation, shared-record edit or evaluation action was performed.
The only file written by this pass is this review.

## Severity-ranked findings

### R1 — MINOR, requested: qualify the finite-inverse-limit background

Location: `sections/1_introduction.tex:107`, especially lines 108–110;
the background paragraph on PDF page 3.

The paragraph credits the inverse-limit description and invariant
measure of compact minimal equicontinuous systems to Hurder–Lukina.
In the surrounding discussion of finite cyclic partitions, the class
needs a totally disconnected qualification. The cited author-version
Sections 2.2–2.3 concern equicontinuous Cantor actions and their finite
quotients, not all compact minimal equicontinuous spaces.
[Checked primary version](https://arxiv.org/html/2205.06285v2).

For example, an irrational circle rotation is a compact minimal
equicontinuous system, but its connected circle cannot be an inverse
limit of finite discrete spaces. This does not challenge Proposition
6.1: the manuscript proves that proposition on a compact ultrametric
space by explicit clopen partitions. The issue is the scope of the
background attribution, not the self-contained proof.

Requested fix: replace the unrestricted phrase with, for example,
“The finite-quotient inverse-limit description and invariant measure
of minimal equicontinuous Cantor systems are classical,” retaining
the following sentence that the article supplies the cyclic-partition
proof, including the finite alternative. Alternatively qualify the
statement as compact totally disconnected minimal equicontinuous
systems and identify the cited source as its Cantor setting.

Acceptance check: the introductory attribution should no longer
suggest that finite discrete quotients model every compact minimal
equicontinuous system. No theorem, proof, quantitative bound, field
quantifier or companion interface should change.

### O1 — OPTIONAL: define the two conventional p-adic notations

Locations: Theorem 1.1(iv), `sections/1_introduction.tex:71`, and the
native-time formula in `sections/3_displacements.tex:40`.

The uses of $\mathbb Z_p$ and $v_p(a)$ are conventional and consistent.
For a self-contained article addressed beyond ultrametric dynamics,
one short definition would help: $\mathbb Z_p=\varprojlim_n
\mathbb Z/p^n\mathbb Z$ with its usual inverse-limit topology, and
$v_p(a)$ is the exponent of $p$ dividing the positive integer $a$.
This also distinguishes $v_p$ from the real field valuation $v$.
Do not strengthen the conjugacy into an isometry or an analytic
conjugacy; the theorem correctly promises a homeomorphism only.

### O2 — OPTIONAL: repeat the minimal-ramification citation at use

Location: `sections/2_coefficients.tex:11`, equation (2.2) and the
sentence immediately following it.

The minimal ramification of $z+z^2$ is explicitly labeled a source
input, and Section 1 already identifies Lindahl–Rivera-Letelier's
optimal-cycle theorem and $q=1$ discussion. Thus this is not an
uncited premise or a missing proof. Repeating that citation next to
(2.2), with the checked minimal-ramification definition and $q=1$
discussion if desired, would make the boundary between imported and
proved statements easier to audit. No extra proof of the source
theorem is requested.

No other must-fix source, notation, bibliography or layout issue was
identified. No numerical referee score is assigned.

## Exact theorem and dependency checks

The abstract, Theorem 1.1, completion paragraph and scope section agree
on every odd prime $p$, every complete algebraically closed real-valued
ultrametric field $K$ of characteristic $p$, and each multiplier with
$0<|\lambda-1|<1$. The cycles have ordinary least periods $p^e$.
The real probabilities are not formal characteristic-$p$ coefficients.
The theorem concerns the entire sequence, not a chosen subsequence.
It does not assert uniformity as $|\lambda-1|$ approaches one.

The metric is explicitly $|x-y|$ on classical points. Hausdorff,
$W_1$ and $W_\infty$ are defined before the theorem. The containing
closure $C$ and the limit $\mathcal A$ are kept separate, including in
the table: $C$ contains old periodic cycles and their atomic invariant
measures, whereas unique ergodicity is asserted only on $\mathcal A$.

The mathematical dependency chain in the article is:

1. Source-owned small-cycle geometry and minimal ramification give the
   canonical small factor through a coefficient-field construction.
2. Residue-one native isometry and the substitution-operator bound
   control within-cycle displacements at all anchor depths.
3. Differentiating the small factor and every higher return quotient
   gives a finite exact mean contact with a growing lower bound.
4. An aligned native-orbit coupling controls the entire higher cycle,
   yielding a compact classical closure and full-sequence limits.
5. Finite clopen cyclic quotients identify the limit as either finite
   or a $p$-adic adding machine. The finite contact upper bound excludes
   every finite alternative and gives nonatomic Haar probability.

### Sections 2–4: arithmetic and arbitrary-field scope

The coefficient-field realization does not assume that $K$ is a
Laurent-series field, discretely valued, locally compact, or has a
specified residue field. The subfield $k_0$ of elements algebraic
over $\mathbb F_p$ is an algebraic closure of $\mathbb F_p$ inside
$K$; its nonzero elements have norm one. Laurent series evaluated at
$s=\lambda-1$ converge by completeness. The leading-term norm proves
injectivity and isometry, and finite truncations justify the ring
operations. This correctly embeds the coefficient field as a proof
device inside every allowed $K$.

Coprime Hensel factorization is applied over the complete discrete
valuation ring $k_0[[t]]$, where it is justified, and then transported.
Minimal ramification makes the small factor degree exactly $p^e$.
The already known $p^e$ distinct points of actual least period $p^e$
belong to it, so degree gives the full simple root product. The unit
factor remains a unit at every point of positive valuation. No Galois
irreducibility or extra separability premise has been substituted.

For native time $a=kp^j$, $p\nmid k$, the telescoping difference
quotients all have residue one; their sum has nonzero residue $k$.
This proves the valuation identity indexed by $v_p(a)$, including its
multiplicity count. It does not assume different indices give different
valuation values.

The weighted Gauss bound $w_r(\Delta H)\ge w_r(H)+r$ applies to
arbitrary polynomials over the stated field. Characteristic $p$ gives
$\Delta^{p^j}=U^{p^j}-I$, so evaluation at a point of valuation $r$
gives $\delta_j\ge(p^j+1)r$. This bound is stronger than a merely
linear-in-$j$ estimate and supplies the needed unbounded anchor-depth
conclusion without discrete-valuation assumptions.

The nonvanishing of $m_d-1$, where $m_d=(P^{\circ p^d})'(\beta)$,
is proved before any division. The differentiated level-$d$ factor
has three nonzero factors: the preceding return by least period, the
simple small-factor derivative, and the unit factor. At every higher
level the denominator is then nonzero, also when $e=d+1$.
The manuscript obtains the exact identities

$$
A_d=\delta_{d-1}+\sum_{j=0}^{d-1}(p-1)p^{d-j-1}\delta_j,
\qquad
\frac1{p^e}\sum_{\alpha\in\Pi_e}v(\beta-\alpha)
=\frac{p-1}{p^{d+1}}A_d=c_d.
$$

The multiplier product is independent of the anchor by cyclic
permutation of its factors. The displayed finite geometric sum gives
$c_d\ge d r^3+r^2(1+1/p)$ with the stated constants. The higher-level
uniformity is explicit, not an inference from a fixed pair of levels.

A single contact at least the real average selects a close pair.
Native isometry and $p^e$ matched iterates then produce a coupling:
each lower point occurs $p^{e-d}$ times. This gives both marginals
and both directed Hausdorff bounds; compatible phases across all
levels are unnecessary.

### Sections 5–6: compactness, support and aperiodicity

The exact finite-cycle distance lemma is proved by an lcm-length
coupling and the global minimum distance lower bound. In particular,
using a nearest pair rather than a supremal contact is legitimate
because one orbit covers each single cycle isometrically.

The uniform all-higher-level hypothesis gives a finite net for the
whole union after finitely many earlier cycles are added. Completeness
and total boundedness give compactness of its classical closure.
Surjectivity on that closure follows from its compact image containing
the dense union, not from assumed surjectivity on the ambient disk.
The tail-intersection construction and both directed estimates prove
Hausdorff convergence to a nonempty compact set and invariance in
both directions.

The modulus-of-continuity bound makes integrals Cauchy for every
continuous test on the compact classical closure. Riesz representation
therefore gives the full measure sequence. The auxiliary subsequence
used for couplings on the compact product does not weaken that result:
its marginals are the already established limits, and the continuous
nonnegative excess-cost function passes the uniform cost bound to a
limiting coupling. This proves the claimed $W_\infty$ estimate.

The classical evaluation-seminorm map is continuous and injective into
the Hausdorff Berkovich projective line. Restricted to compact $C$ it
is a homeomorphism onto a closed compact image. Restriction of every
continuous Berkovich test to $C$ proves the stated weak convergence.
No global metrizability of that line, ambient classical compactness,
or countable subsequence test class is assumed.

Minimality is obtained by approximating two limit points by points on
one finite cycle and using isometry. The clopen ultrametric partitions
are finite, refining and of vanishing mesh. Minimality makes each
induced permutation one cycle; sufficiently close $p^e$-cycles map
onto it equivariantly, so its size divides $p^e$. The basepoint coding,
nested-cell surjectivity and finite/cofinal alternatives are all given
in the manuscript. Uniform masses on these partitions determine the
unique invariant probability and identify it with Haar probability.

The finite alternative is not excluded merely from growing periods.
For a fixed old anchor, one fraction $p^{-d}$ of the higher orbit has
the same contact $h$, and every other contact is at least $r$.
The exact mean therefore gives

$$
h\le U_d=p^d c_d-(p^d-1)r<\infty.
$$

This separates the limit from every fixed old cycle. Any finite
$p^k$-cycle with $k\ge1$ would be the unique source cycle $\Pi_k$;
the singleton alternative would be $0$ or $-s$, neither on the
prescribed sphere. Thus the infinite adding machine, nonatomicity,
and exact type-I support follow. The argument correctly establishes
only a topological conjugacy, not an analytic or metric one.

## Primary-source ownership and literature boundaries

The specific question is Problem 1.3 in the explicitly versioned
26 May 2015 Lindahl–Rivera-Letelier text. Its odd-characteristic,
arbitrary complete algebraically closed field and multiplier range
match the manuscript. The source's Theorem C and $q=1$ discussion
provide the cycle geometry, and its minimal-ramification discussion
provides the reduction input. The new article does not claim those
inputs as its own. The checked version identifies the requested
measure sequence itself, not the separate minimal-ramification
conjecture. [Primary version](https://arxiv.org/html/1311.4478v3).

The Jacobs comparison is correctly a distinction between measures,
not characteristic. The actual v2 PDF's definition assigns crucial
weights away from type-I support, and Theorem 2 concerns the associated
crucial measures rather than uniform measures on the selected small
cycles. This pass read the definition and theorem statement; it did
not claim a fresh full reread of the long theorem proof. The earlier
source audit's fuller proof read remains a separate record.
[Versioned PDF](https://arxiv.org/pdf/1409.4808v2).

Nordqvist–Rivera-Letelier's Theorem 3 concerns periodic-point norm
bounds for ramified multiplier-one series. Its inspected statement
does not supply the all-higher-level selected-cycle mean-contact
identity or this measure limit. This pass checked the relevant
introductory/theorem scope, not every proof in the article.
[Primary version](https://arxiv.org/html/1904.04494v3).

Hurder–Lukina Sections 2.2–2.3 were read for finite-quotient and
invariant-measure background in the Cantor setting; that source scope
is the reason for R1. The specific finite cyclic quotient proof is
included in C431 and is not being delegated to this citation.
[Primary version](https://arxiv.org/html/2205.06285v2).

Baker's actual lecture-note PDF was checked for the needed seminorm
topology, compact-Hausdorff spectrum result and analytification
background in Sections 2.3–2.4. The manuscript does not extract a
general metrizability assertion from it. [Lecture notes](https://swc-math.github.io/aws/2007/BakerNotesMarch21.pdf).

All five bibliography entries are used and identifiable. Primary DOI
metadata and available publisher issue records support the listed
journal data. In particular, the Lindahl–Rivera-Letelier journal issue
is 2016, distinct from its 2015 online publication; Hurder–Lukina's
issue is 2025, pages 57–74. Version-specific notes correctly avoid
the title discrepancy on the Jacobs abstract page. Some publisher
full-page retrievals failed; successful DOI metadata and actual
author versions were used without claiming publisher proof access.
[LRL issue record](https://www.cambridge.org/core/journals/compositio-mathematica/article/abs/optimal-cycles-in-ultrametric-dynamics-and-minimally-ramified-power-series/83B7D75267327F3D0B76E9E6B47BE8F7),
[Hurder–Lukina issue record](https://www.mathsoc.jp/publication/JMSJ/onlineindex/77-1.htm).

The frozen coordinator source synthesis and X1 source report were
also read in full. Their bounded-search limitations remain in force.
This pass is not a fresh exhaustive forward-citation, retraction,
unpublished-work or worldwide-priority audit. The manuscript's own
scope paragraph makes the same limitation and claims a positive
answer to the identified question version, not certified firstness.

The typeset dependency chain was compared directly with accepted A1
and D1. C431 imports no full-inertia, oriented Artin–Schreier character,
or splitting-field nesting result from C430/UL4. The coefficient-field
lemma does not conceal such an import. No C430 circularity was found.

## Actual source, PDF and build-evidence inspection

Read in full: `main.tex`; all seven section files; `references.bib`;
the 160-line `SOURCE_BUILD_RECORD.md`; the full 388-line `BATCH_PLAN.md`;
the applicable repository, Henon and batch instructions; the accepted
470-line A1 and 286-line D1 proof packages; the 140-line coordinator
source synthesis and 102-line X1 report. Relevant admission and prior
review records supplied context, not replacements for these reads.

All 12 PDF text pages were read, including a separate recovery of the
middle pages after an initially truncated combined tool response.
All supplied images `inspection/page-01.png` through `page-12.png`
were actually opened and viewed by this reviewer. The theorem,
equations, contact proof, compactness proof, adding-machine proof,
comparison table and bibliography were legible. No clipping, overlap,
missing glyph, broken reference, unreadable cell or mathematical
transcription error was found. The table's ordinary floating position
does not obstruct the argument and is not recorded as a defect.

The PDF is 12 pages, 382004 bytes, US Letter, PDF 1.5. Font inspection
shows 22 embedded subset Type 1 fonts with Unicode mappings and no
Type 3 fonts. The final `main.log` and `main.blg` have no matching
warning, undefined-reference/citation, missing-character, overfull,
underfull or error messages. The earlier `build_initial.log` is real
historical build output and is not confused with the final clean log.
The recorded source-date epoch agrees with the PDF's UTC timestamp.

This reviewer did not rebuild or rerender the article. Inspection used
the actual frozen output and existing page renders. Byte comparisons
showed that all nine current source files equal `baseline/src/`, the
source/build record equals its baseline copy, and all three original
PDF copies are identical. The following hashes were freshly checked
and remained unchanged at report finalization.

## Frozen input bindings

Paths in the first table are relative to
`papers/C431_optimal_cycle_measures/`.

| Input | SHA256 |
| --- | --- |
| `main.tex` | `665ecb1d163a5345d5871bb5c8155ca99eb0a30f5e367840d600d52c65ab1c81` |
| `references.bib` | `5e0975227644cc458dbf3d40e011f4a11cb9c0d76819f3043cc39f6bcc730bf2` |
| `sections/1_introduction.tex` | `d9e36e1bb5239457a6a8e3c32a47217ce8b25b8f340505000718c191198f1c34` |
| `sections/2_coefficients.tex` | `b5eb44fc34ee02d951855ae51989d0b329f85e4ead8b79bd100b67eeeaaa34f8` |
| `sections/3_displacements.tex` | `6f63fde2fc55ab4fda11d55e1952306cfc7dca0b9caed1781e3e5a1abae9aad4` |
| `sections/4_contacts.tex` | `c6203fdd3985c273cc6211f536887e9273a94be5e92cfe7e2d2464ccd0d03873` |
| `sections/5_compact_limit.tex` | `3eaf9f89737f7d62791a4ec83a95afccd470afcc77cf914dfdc781f58b8e938c` |
| `sections/6_adding_machine.tex` | `a665bb19ca294784768d01353c35b83f92db3be4def838bb67b7818a75be3c8b` |
| `sections/7_scope.tex` | `eeed8f29f17238f77f265cc43bf179af32abbe52184b1ff9d03ef5c8a537c174` |
| `SOURCE_BUILD_RECORD.md` | `a6559476e391193f64454fff0d016299b0259723fbc30530bbf6eecb915065af` |
| `main.pdf` = `main_round0_original.pdf` = `baseline/main.pdf` | `989f18747d96648d7ebbeaed4b8e1bba7002e3cb407a21748d60a4b64107a4e6` |
| `main.log` = `baseline/main.log` | `6867988ca20316e1b106299fac3d94d96a6b1c996066b0cb019bc12881d26a1f` |
| `main.blg` | `3dd80052e3eef4b4492042028709a4402c93c933a2ac558ed32d4f76113f887a` |
| `build_initial.log` | `ef708a5172e83c90b1d91d5e349ef16276328a602ea57ff5ccf7c7134450242d` |

Accepted proof and source inputs, relative to the batch directory:

| Input | SHA256 |
| --- | --- |
| `continuation_round4/a1_optimal_cycle_measures/PROOF_PACKAGE.md` | `038cdb412d1b83b94c1ebcfb742090e3937251225077a0f6842d7933c458174e` |
| `continuation_round4/d1_isometric_cycle_limit/PROOF_PACKAGE.md` | `e2daa9770024c62e7b7fb09855d4c23eaa0c4cd0aa5416ad268288dbe569aedd` |
| `continuation_round4/NOVELTY_CHECK_OPTIMAL_MEASURES.md` | `41844d9fa96a16b29490e60a687d494747046caee569b0607ed70af836f649fb` |
| `continuation_round4/x1_optimal_measure_sources/REPORT.md` | `ceffdf93f36997f2aa13b074221ec995722b47856ab6d4c6ed775af17f7e4aec` |

## Handoff and stop condition

Pass 1 is complete after full report readback and unchanged-input
verification. Main-theorem correctness: pass. Critical mathematical
must-fixes: zero. Major mathematical must-fixes: zero. Requested minor
source-scope clarifications: one, R1. Optional suggestions: O1–O2.

Freeze this report as the actual round-1 record. The coordinator should
adjudicate the findings, have any accepted source changes rebuilt and
preserved as a real next version, and then request the separate actual
round-2 review. No review round, fix, build, evaluation or release
completion beyond this report is represented as already performed.
