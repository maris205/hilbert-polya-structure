# C431 actual manuscript review — pass 2

## Verdict

**PASS on the frozen revision-1 manuscript. Main theorem: PROVABLE AS
STATED.** The first-pass requested clarification R1 is resolved. Both
accepted optional suggestions O1–O2 are implemented correctly. No new
critical, major or minor mathematical, transcription, exposition or
layout must-fix was found in this pass. No further manuscript revision
is requested by this reviewer.

The reviewed article is *Haar limits of optimal wild cycles*, with
`main.pdf = main_round1.pdf = revision1/main.pdf`, 12 pages, 384227
bytes, SHA256
`dba1f729d54b44b12cd800273041e3a514846613a4cdad0cd2454d9aa28a0915`.
This is an actual second manuscript pass in the same reviewer thread,
after the author's actual first revision, not a renamed proof review
or an assumed second-round improvement.

This verdict is internal mathematical manuscript review. It is not
external peer review, a numerical acceptance score, journal-readiness
certification, an exhaustive literature/status clearance, formal route
evaluation, a final reproducibility build or a release seal. Those
separate processes retain their own evidence and coordinator ownership.

## Review scope and actual read extent

The reviewer read the complete current `main.tex`, all seven included
section files and `references.bib`: 904 lines in total. The entire
revised PDF text was extracted and read in three page groups, 1–4,
5–8 and 9–12. Every supplied revision-1 page image, 1 through 12,
was actually opened and visually inspected. The old top-level
`inspection/` images were not substituted for the revised renders.

The following complete records were also read: the 382-line original
round-1 review, the 266-line original citation audit, the 153-line
author improvement log, the 73-line state record, the 216-line current
source/build record, and the 388-line batch plan. The applicable
repository, Henon and batch instructions and the required review,
proof-checking and batch-workflow skill instructions were read in full.
An initially truncated combined record read was recovered before
completion; no truncated record is counted as fully read.

The complete source delta from the original baseline was inspected.
Only the bibliography and Sections 1–2 have source changes. Current
source files were byte-compared with their `revision1/` counterparts.
Theorem 1.1's complete environment was separately byte-compared with
the original; its statement, title and label are unchanged. Sections
3–7 and the master file are byte-identical to their original source
versions, and were nonetheless read as part of this actual full
manuscript pass.

The accepted A1 and D1 proof packages were read in full during pass 1;
their hashes were rechecked here and remain unchanged. This pass does
not claim another full read of those old packages or repeat their old
literature searches. Its substantive regression check reads the actual
typeset proof chain in the current manuscript, not merely its hashes.
No new source-applicability risk requiring a further literature search
was identified. The separate bounded citation-delta audit is not
represented as a second mathematical manuscript review or as work
performed by this reviewer.

Only this new `reviews/round2/REVIEW.md` was written. No source,
bibliography, PDF, original review, citation report, author log/state,
baseline, shared record, evaluator or Git object was changed. No
compilation, rendering, mathematics program, external-model upload,
new agent or external notification was run. Read-only PDF inspection, text
extraction, source comparisons and hashes are artifact checks, not
mathematical experiments.

## First-pass disposition and actual revised passages

| Finding | Actual revision inspected | Pass-2 disposition |
| --- | --- | --- |
| R1 / overlapping C431-CIT-2 | `sections/1_introduction.tex:111`, PDF page 3, now restricts the finite-quotient inverse-limit background to minimal equicontinuous Cantor systems. The next sentence retains this article's own cyclic-partition proof, including the finite alternative. | **Closed.** The unqualified extension to every compact minimal equicontinuous system has been removed without changing a theorem or proof. |
| O1, optional and accepted | `sections/1_introduction.tex:21`, PDF page 1, defines the integer valuation $v_p(a)$ separately from the field valuation $v$, and defines $\mathbb Z_p=\varprojlim_{n\ge1}\mathbb Z/p^n\mathbb Z$ with its usual inverse-limit topology. | **Implemented correctly.** These definitions agree with the native-time formula and finite-quotient coding. No isometric or analytic conjugacy is introduced. |
| O2, optional and accepted | `sections/2_coefficients.tex:17`, PDF page 3, repeats the Lindahl–Rivera-Letelier Theorem C / $q=1$ citation immediately after equation (2.2). | **Implemented correctly.** Minimal ramification remains a source input; the formula and the following coefficient-field proof are unchanged. |

The three local revisions satisfy the precise checks in the original
review. R1's closure does not rely on applying the Cantor source to a
finite space: the manuscript still proves its finite alternative
directly. The two optional changes improve readability without adding
an assumption or a new dependency.

The accompanying bibliography delta was also read in the actual source
and rendered PDF. All four existing journal DOI URLs are now visible
in entries [2]–[5], and all five original version URLs remain present.
The printed numbering is still the same alphabetical order. There are
eight citation commands using the same five keys; the extra occurrence
is the repeated source citation following (2.2). No unresolved citation,
unused entry, duplicated key or unintended bibliography expansion was
found.

The Baker entry retains the lecture-notes manifestation and explicitly
distinguishes the 2007 lectures from the linked PDF's recorded first
publication in University Lecture Series 45 (2008), as requested in the
original citation audit. No notes DOI or separate PDF revision date has
been invented. This pass checked that authorized clarification against
the full original audit and real author response, and checked its actual
rendering; it did not independently reopen that primary PDF again.

Retraction-database and complete article-update clearance remain
**UNCHECKED** in the author's records. Nothing in the revised article
converts unavailable status checks into zero retractions, verified
current-open status or worldwide priority. This review closes its own
manuscript findings; the coordinator retains the separate citation-delta
report and its precise limitations.

## Full theorem and proof regression assessment

### Scope, observables and companion boundary

The abstract, setup, Theorem 1.1 and completion paragraph retain every
odd prime, every complete algebraically closed ultrametric field of
characteristic $p$, every fixed $0<|\lambda-1|<1$, and the full sequence
of real uniform probabilities on the unique cycles of ordinary least
period $p^e$. There is no discretely valued field restriction, formal
field replacement, selected subsequence, or measure on all periodic
points. The explicitly dated Problem 1.3 remains the question answered.

The metric is still the classical absolute-value metric. The Hausdorff
and transport distances are defined before the theorem. The containing
closure $C$ and the limit support $\mathcal A$ remain distinct in the
theorem, explanatory paragraph and comparison table. Only the latter
is claimed uniquely ergodic. The adding-machine conjugacy remains a
homeomorphism with the defined inverse-limit topology, not a metric
isometry or an analytic linearization.

The article still uses no C430 full-inertia theorem, oriented
Artin–Schreier character stabilization or field nesting. Its
coefficient-field construction is a proof device inside arbitrary
$K$. Theorem 1.1's interface is unchanged, so the accepted direction
from C431 to a later C430 consequence does not become circular.
No target Euler-factor, root-number, automorphy or Hilbert–Pólya claim
has been added.

### Arithmetic-to-contact chain

The realization of $k_0((t))$ in $K$ still proves convergence, the
leading-term norm, preservation of operations and injectivity before
transporting the coprime Hensel factors. The use of a discrete
coefficient ring does not restrict the ambient field. The source cycle's
$p^e$ distinct points and the degree-$p^e$ small factor still give its
exact simple root product and a unit complementary factor.

Residue-one native isometry and the telescoping argument still justify
the $v_p(a)$ displacement index and its multiplicities. The newly added
definition of $v_p$ agrees with exactly this use. The weighted Gauss
valuation and characteristic-$p$ operator identity still give
$\delta_j\ge(p^j+1)r$, including $j=0$ and real nondiscrete valuations.

The differentiated level-$d$ factor still proves $m_d-1\ne0$ before
division by the higher return derivative. The adjacent-level boundary
$e=d+1$ is explicitly handled. The exact contact identity remains

$$
\frac1{p^e}\sum_{\alpha\in\Pi_e}v(\beta-\alpha)
=c_d=\frac{p-1}{p^{d+1}}v\!\left((P^{\circ p^d})'(\beta)-1\right)
\ge d r^3+r^2(1+1/p),\qquad e>d.
$$

Finiteness, anchor independence, the real division by $p^e$ and the
uniformity in every higher level remain justified. The aligned orbit
coupling still repeats each lower point $p^{e-d}$ times, so its two
marginals and support-distance bound are unchanged.

### Compactness, all-test convergence and aperiodicity

The lcm coupling proves the exact finite-cycle metric comparison. The
uniform all-higher-level estimate still provides finite nets for the
whole cycle union and hence compactness of its classical closure.
Surjectivity is proved on that compact closure and on the limit set;
it is not assumed on the ambient disk.

The Riesz argument uses convergence of the integrals for every real
continuous test on the compact classical closure. The auxiliary
subsequence of couplings has the already determined full-sequence
measure limit as its marginal and preserves the distance bound by a
continuous nonnegative excess-cost function. Thus it does not reduce
the main theorem to subsequential convergence. The compact classical
embedding into the Hausdorff Berkovich line still passes every
continuous Berkovich test to that closure without assuming global
metrizability or local compactness of the classical field.

The finite clopen partitions still prove minimality, exact support,
unique ergodicity, and the finite-$p$-power-cycle/$\mathbb Z_p$ alternative.
The new inverse-limit notation does not alter the cofinality argument.
The finite upper contact bound
$U_d=p^d c_d-(p^d-1)r$ still follows from the repeated contact on an
orbit fraction $p^{-d}$ and separates the limit from each old cycle.
Uniqueness of the old cycles excludes every finite nontrivial
alternative; the fixed points $0,-s$ are off the prescribed sphere.
Consequently the nonatomic Haar conclusion and exact type-I support
remain proved. Growing periods alone are still explicitly not used
as an aperiodicity argument.

No mathematical weakening, missing case, circular inference or
typesetting-induced change was found in this complete reread.

## Revised PDF and build-evidence checks

All twelve revised page images were inspected. The new definitions on
page 1, the whole theorem on page 2, the narrowed background and added
citation on page 3, the coefficient and displacement arguments on
pages 3–5, the contact proof on pages 6–7, compactness and measure proof
on pages 7–9, adding-machine/separation proof on pages 9–10, and the
table, scope and bibliography on pages 11–12 are legible. No clipped
content, colliding equation, missing glyph, lost reference or unreadable
table/URL was found. Ordinary page breaks and the table's floating
position are not defects.

Read-only `pdfinfo -rawdates` and `pdffonts` confirm the stated 12-page,
384227-byte US Letter PDF 1.5 output, both source-date timestamps
`D:20260909000000Z`, and 22 embedded subset Type 1 font entries with
Unicode mappings; no Type 3 font is listed. A scan of the actual
`revision1/main.log` and `revision1/main.blg` found no warning,
undefined-reference/citation, missing-character, overfull, underfull or
compiler-error message. The top-level final log, BibTeX log and
bibliography output equal their revision-1 copies byte for byte.

These observations inspect the author's actual revision build. This
reviewer neither compiled nor rerendered the paper and does not count
that existing build as either required final clean release build.
Reader output and visual inspection are not represented as a separate
structural-PDF certification. The full original baseline and raw reports
remain preserved, with the hashes below.

The author state record was read as an author-stage lifecycle snapshot,
not as authority superseding the coordinator's separately accepted
formal route evaluations. This review does not repeat or alter those
evaluations. Later lifecycle reconciliation, final deterministic builds
and sealing remain coordinator-owned tasks, not mathematical findings
against this manuscript.

## Frozen input bindings

Paths below are relative to the C431 article directory. Every hash was
computed from the actual inspected file. All nine current TeX/BibTeX
files equal their `revision1/` copies. The original baseline source
hashes were separately rechecked against the preserved round-1 record.

| Current source / record | SHA256 |
| --- | --- |
| `main.tex` | `665ecb1d163a5345d5871bb5c8155ca99eb0a30f5e367840d600d52c65ab1c81` |
| `references.bib` | `67164b9f8489c3d99cc3219ae13372659dd2aac1b618d2f572e1950375e00da5` |
| `sections/1_introduction.tex` | `40d85d94398f31bb838c5a9779f7533f22523b7de141763b4e73506b524e1308` |
| `sections/2_coefficients.tex` | `8359d9a98f5bd1da20fca07e2ab4c59074e9b36dcab7e29f04a8b99701468432` |
| `sections/3_displacements.tex` | `6f63fde2fc55ab4fda11d55e1952306cfc7dca0b9caed1781e3e5a1abae9aad4` |
| `sections/4_contacts.tex` | `c6203fdd3985c273cc6211f536887e9273a94be5e92cfe7e2d2464ccd0d03873` |
| `sections/5_compact_limit.tex` | `3eaf9f89737f7d62791a4ec83a95afccd470afcc77cf914dfdc781f58b8e938c` |
| `sections/6_adding_machine.tex` | `a665bb19ca294784768d01353c35b83f92db3be4def838bb67b7818a75be3c8b` |
| `sections/7_scope.tex` | `eeed8f29f17238f77f265cc43bf179af32abbe52184b1ff9d03ef5c8a537c174` |
| `SOURCE_BUILD_RECORD.md` | `0fa72b6c86386f28e3f8af11fb3434794010ecc5ba417d1ba438323ef0023d50` |
| `PAPER_IMPROVEMENT_LOG.md` | `f8308863e66d1cfa05c112633ba365814961efb8d600133f53a9421949b79ce2` |
| `PAPER_IMPROVEMENT_STATE.json` | `2fe85e74ff1f94994c1656a846e6573ddc2586461ad3f2cd6d2cc6bde79a366c` |
| `reviews/round1/REVIEW.md` | `78964f384e3b1b4c822448a787c57bbb09a56fe5cc0d0cbe6ae0f8cf90ca0703` |
| `reviews/citations/REPORT.md` | `289e6d4e48726877f6231b0c49f11ca2902d4eb1579c916f9ab3bfaed27723e4` |
| `baseline/SOURCE_BUILD_RECORD.md` | `a6559476e391193f64454fff0d016299b0259723fbc30530bbf6eecb915065af` |

| Actual output | SHA256 |
| --- | --- |
| `main.pdf` = `main_round1.pdf` = `revision1/main.pdf` | `dba1f729d54b44b12cd800273041e3a514846613a4cdad0cd2454d9aa28a0915` |
| `main_round0_original.pdf` = `baseline/main.pdf` | `989f18747d96648d7ebbeaed4b8e1bba7002e3cb407a21748d60a4b64107a4e6` |
| `revision1/main.log` | `78319d8176d8e383bc5f1d883117fc7811bf9b5c7ec2bf224125f83680336aec` |
| `revision1/main.blg` | `2869df80311b1a366eafb1f3521178afc6dcc628264e742964e979b9cb9e66e2` |
| `revision1/main.txt` | `dd24807e31a05470e0ad35d1dd3f08b39694b1af5b5bbb6985c20478b59ab417` |

Actual visually inspected images, under `revision1/inspection/`:

| Image | SHA256 |
| --- | --- |
| `page-01.png` | `2f5852936acafa1cfcbed822486a78099bee41d54a466e354744f3a14b4856d8` |
| `page-02.png` | `08cdf7240459fa57a682728c5794f1690d961dd171c5726f9503a0e52d7c6b1c` |
| `page-03.png` | `9f82968b61bc1ca20c015a8d49663b402ba6f0c0868c7942f4904d3966deb54d` |
| `page-04.png` | `8808b19aeb17a67339d0031e4a893694067e673be4cd668868f684d53212b053` |
| `page-05.png` | `6c66b6ef52ade30623c2d9e35aca327114b4f72d9d62b7512b54deabb145a55c` |
| `page-06.png` | `17bc1405a546b86927d1dd0ebad5693925d5edfdec7b2baae16e5f7c97373d47` |
| `page-07.png` | `6aa013aa073c2ebf595dc91979685041ebb56081117a7307381ba06ea2c4c321` |
| `page-08.png` | `03fc27dd06e6288ffd696551d851f35f8ac88307d0f905a4a2283b35818b8e09` |
| `page-09.png` | `9ae262e040596a8b66cfa72e4a6b38a09c81632f693fa4f2a49bb2c2a0ba541b` |
| `page-10.png` | `78346899518e8104c6b68d613066290b2058fb3ae75e6679f923baf23387574c` |
| `page-11.png` | `e2d855e503d1c0750a9b5592d7026ad84356dc204d3730395013de0d60e857f5` |
| `page-12.png` | `afac245e42173209c6e5843b1a54b9124c45ac9bc88fe7c9d6a3a8cf779a111f` |

Unchanged accepted proof bindings, relative to the batch directory:

- `continuation_round4/a1_optimal_cycle_measures/PROOF_PACKAGE.md`:
  `038cdb412d1b83b94c1ebcfb742090e3937251225077a0f6842d7933c458174e`.
- `continuation_round4/d1_isometric_cycle_limit/PROOF_PACKAGE.md`:
  `e2daa9770024c62e7b7fb09855d4c23eaa0c4cd0aa5416ad268288dbe569aedd`.

## Final disposition and handoff

Pass 2 is complete after full report readback and frozen-input
verification. R1 is closed; O1–O2 are resolved as accepted optional
improvements. There are zero new critical, major or minor manuscript
must-fixes. The main theorem and full mathematical scope survive
unchanged, and no extra author revision is required by this report.

Freeze this as the actual second manuscript-review record. The
coordinator should adjudicate it together with the separate citation
delta and continue the authorized final-build and release gates. This
review does not claim those gates have already been completed and does
not manufacture a second revised PDF when no new revision is needed.
