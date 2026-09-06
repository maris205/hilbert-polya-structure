# LNR independent source and collision audit

2026-09-06 UTC. Assessor: `batch197_lzk_gate`, current configured model in a
separate process from both proof authors. Scope: candidate gate only.
Verdict: **HOLD_SOURCE**, not a novelty certificate and not a mathematical
counterexample. No paper number, reserve, external review or release.

## Decisive direct owner: the rank transform is prior

Ramin Zabih and John Woodfill, *Non-parametric Local Transforms for Computing
Visual Correspondence*, ECCV 1994, pp. 151–158, DOI
[10.1007/BFb0028345](https://doi.org/10.1007/BFb0028345).
The [author's publication list](https://www.cs.cornell.edu/~rdz/rdz-papers.html)
links the actual [author-hosted PDF](https://www.cs.cornell.edu/~rdz/Papers/ZW-ECCV94.pdf).
Downloaded as `sources/ZabihWoodfill1994.pdf`; all eight PDF pages were read
as layout text, including the complete Section 3 definition, examples,
related-work section and references. The definition counts neighboring
pixels with intensity strictly below the center, not a median or rank-order
filter. LNR is precisely its two-neighbor, one-dimensional cyclic ternary
specialization. The map itself receives zero novelty credit. The inspected
paper establishes image matching properties; it does not state the claimed
three-step dynamics or the arbitrary-target ternary cyclic fibre maximum.
That last observation concerns this inspected paper, not the full literature.

## Unresolved direct temporal owner: Mukherjee 2011

Jayanta Mukherjee, *Local rank transform: Properties and applications*,
Pattern Recognition Letters 32(7), 1001–1008 (2011), DOI
[10.1016/j.patrec.2011.02.005](https://doi.org/10.1016/j.patrec.2011.02.005).
Actually read the [publisher preview](https://www.sciencedirect.com/science/article/abs/pii/S0167865511000420):
abstract, introduction, the visible beginning of Definition 2.1, and
conclusion. It explicitly claims a proof of convergence under iteration
and says the main definition/property discussion is one-dimensional.
The visible rank definition uses strict lower values. **The convergence
theorem statement and proof are not visible and have not been read.**
Consequently neither complete temporal overlap nor a new sharp three-step
refinement is certified here.

Ordinary public retrieval was pursued without an external upload, purchase,
login bypass or author contact:

- The publisher PDF endpoint returned HTTP 403 (`curl --fail`, exit 22).
  It did not create a usable paper PDF.
- The public Elsevier article endpoint succeeded, but returned only 1,802
  bytes of metadata with `openaccess=false`. The exact response is retained
  as `sources/Mukherjee2011_elsevier_attempt.xml`; this is not full text.
- The actual [author homepage](https://facweb.iitkgp.ac.in/~jay/),
  [journal list](https://facweb.iitkgp.ac.in/~jay/pubjournals.html) and
  [LRT download page](https://facweb.iitkgp.ac.in/~jay/LRT_public/README.htm)
  were read. The journal title points to a generic `echo_abs.html` rather
  than a paper PDF. The LRT page identifies the 2011 paper and links
  [LRT_public.zip](https://facweb.iitkgp.ac.in/~jay/LRT_public/LRT_public.zip).
  The ZIP was downloaded and its entire 21-entry listing checked: MATLAB
  functions, images and README documents, no paper PDF. No MATLAB source
  file was read, imported or executed for the independent checker.
- Exact-title searches, DOI/PII searches, author/institution searches and
  the ResearchGate record did not yield an accessible primary body. The
  latter explicitly offers a full-text request; no request was sent.

The missing comparison is specific: neighborhood multiplicity and boundary
conventions; strict versus weak ties; synchronous versus another iteration;
alphabet assumptions; the actual stabilization bound and fixed-state
description. This is an admission-blocking source obligation, not grounds
to invent an unseen theorem or declare the mathematics false.

## Related reconstruction paper is not the same iteration

P. Raj Bhagath, Kallol Mallick, Jayanta Mukherjee and Sudipta Mukhopadhyay,
*Low-complexity feedback-channel-free distributed video coding using Local
Rank Transform*, primary preprint [arXiv:1607.07697v1](https://arxiv.org/abs/1607.07697v1),
later IET Image Processing 11(2), 126–134 (2017).
Downloaded `sources/BhagathEtAl2017.pdf`; PDF pp. 1–4 were actually read,
including Section 2 and Algorithm 1. Its literal local-rank definition is
consistent with the 2011 reference. Reconstruction iteratively increments
or decrements an image estimate against a *fixed target rank image*, using
side information and a stopping criterion. This is not repeated application
of the autonomous map $x\mapsto F(x)$ and is not an exact enumeration of
all finite ternary sources. It does not resolve the missing 2011 theorem.

## Classical inverse adapters: fully deducted

For a source define $s_i=\operatorname{sign}(x_{i+1}-x_i)$. Then
$b_i=\mathbf1_{s_{i-1}=+1}+\mathbf1_{s_i=-1}$. Contract every zero-sign
edge. A directed cycle of strict inequalities is infeasible; otherwise
transitive closure gives a poset and sources in this stratum are precisely
its strict order-preserving maps to three colors. Expanding contractions
recovers original labeled coordinates. The all-zero sign word is a single
block with three choices. Recovering signs from a source proves the strata
are disjoint. This is a full all-target static representation, not a new
mechanism. The eight kernels are a convenient low-alphabet evaluation of
this old primitive and likewise receive no separate novelty credit.

For $(02)^m$, mark a valley iff its source height is one and a peak iff its
source height is one. Two adjacent marks are exactly the forbidden failure
of a strict valley-to-peak inequality. Thus the entire alternating fibre
is bijective to independent sets of the labeled cycle $C_{2m}$, with
inverse heights 0/1 on valleys and 2/1 on peaks. Its Lucas count is wholly
classical. Repeating one valley supplies the odd unique-$00$ family;
repeating one peak supplies the odd unique-$11$ family. Deleting the
repeated coordinate is inverse. For the latter, other $2$ runs force the
boundary heights into $\{0,1\}$, excluding the otherwise possible local
source strings $12,21$. Therefore **the complete source sets and counts
of every proposed maximizing family are already explained by classical
adapters**, not only by a coincident recurrence.

The residual question is narrower: comparison of the *sum of stratum
sizes* for every target, including mixed kernels, and proof that no other
target attains the bound. Neither a source-set adapter for the attainers
nor a generic order-polynomial expression for a given target alone answers
that optimization question. No complete earlier adapter for this residual
was established in the sources actually inspected below. This is not a
positive priority assertion.

## Primary inverse/extremal sources actually inspected

| Source | Exact inspected context | Transfer and limit |
|---|---|---|
| J. D. Currie and T. I. Visentin, [*The number of order-preserving maps of fences and crowns*](https://link.springer.com/article/10.1007/BF00383399), Order 8, 133–142 (1991) | Publisher bibliographic record and abstract; body remains subscription-only | Earlier exact fence/crown enumeration; no unseen theorem is invoked. |
| T. Lundström and L. Saud Maia Leite, [*Order polytopes of crown posets*](https://doi.org/10.1016/j.ejc.2025.104304), EJC 133 (2026), 104304; [institutional PDF](https://aaltodoc.aalto.fi/bitstreams/60f3b401-6e20-4160-9e07-3fc8d95a545e/download) | `sources/Crown2026.pdf`, PDF pp. 1–4 and 12–15, especially Corollary 3.9 and Theorem 4.2 with its full proof | Lucas/independent-set identification and crown order-polynomial recursion. A fixed crown is not the union of the various sign-posets compatible with a general LNR target. |
| R. Ehrenborg and S. Mahajan, [*Maximizing the descent statistic*](https://www.ms.uky.edu/~jrge/Papers/Maximizing.pdf), Annals of Combinatorics 2 (1998), 111–129 | `sources/EhrenborgMahajan.pdf`, PDF pp. 1–3; Definition 1.1, Theorem 1.2, scope of the main run-balancing theorem as stated in introduction | Exact descent sets of linear permutations with distinct labels. It is not already a maximum theorem for cyclic three-letter words with ties and local-rank aggregation. No full adapter was supplied. Initial IITB mirror failed certificate validation; the author's Kentucky mirror succeeded normally. |
| Erica Jen, [*Enumeration of Preimages in Cellular Automata*](https://content.wolfram.com/sites/13/2018/02/03-5-2.pdf), Complex Systems 3 (1989), 421–456 | `sources/Jen1989.pdf`, PDF pp. 1–5 and 29–30; general recurrence (2.1), binary-rule scope, and complete Section 5.4/5.5 page contexts | Generic predecessor recurrence is old. The displayed maxima concern binary elementary rules and finite output blocks with longer predecessor boundaries, not the ternary cyclic carrier without a rule/conjugacy adapter. |
| P. C. Huang, [*Bernstein Transfers and Greedy Records for Fence and Circular-Fence Order Polynomials*](https://arxiv.org/html/2607.22767v2), 31 July 2026 | Primary HTML abstract/introduction, cycle orientation conventions, Proposition 4.1 and its complete proof; Definition 7.2 and Lemma 7.4 statement | Ordinary comparison-matrix trace and record-set/linear-extension identification are prior. These inspected statements fix an orientation or permutation-record set; they do not state the maximum of all LNR target union sizes. Later body not represented as fully reviewed. |
| Joel A. Tropp, [*ACM 204: Matrix Analysis*](https://www.tropp.caltech.edu/notes/Tro22-Matrix-Analysis-LN.pdf), Caltech CMS Lecture Notes 2022-01 | Author package's pinned primary PDF/layout text, citation page and printed pp. 49–52, including Example 6.18 and Theorem 6.32 with its proof sketch | Standard unitarily invariant norm Hölder inequality; the author's exponent induction is valid. Entire analytic tool receives zero originality credit. |

## Internal collision checks

Selected original scientific files are pinned in `INPUT_PINS.sha256`.
P112 `main.tex` definition/abstract/introduction and earlier bounded energy
context were actually read. Its tournament map orients all unequal-score
pairs and *retains the old orientation on ties*. LNR has numeric heights on
a cycle and suppresses equal-value comparisons; these literal carriers and
tie rules are not identified by the obvious score analogy. This is not a
proof excluding every possible graph factor.

P186's complete short `PROOF_PACKAGE.md` was read: it acts on subset
supports with sorted gaps, decreasing positive gaps before support
compression. Its clock and inverse gap-slot factorization are not LNR's
local two-neighbor rule. A targeted `rg` search of manuscript/proof files
for local rank / strict-neighbor / rank-transform keys returned no extra
literal collision. Such a text nonhit is not an all-history uniqueness
certificate. The inverse author's full classical adapter was read and
deducted; no historical source was edited.

## Search scope and method limits

Three claim groups were kept distinct: temporal stabilization/fixed states,
all-target inverse enumeration, and global maximum/all equality targets.
Actual query families included:

- `"local rank transform" convergence "Theorem"`,
  `"local rank transform" "iterations" 2011`,
  `"local rank transform" convergence 2024 2025 2026`;
- `"Local rank transform" "Properties and applications" filetype:pdf`,
  `"S0167865511000420" pdf`, author-name/institution/publication queries;
- `"local rank transform" "preimages"`,
  `"rank transform" "maximum" "preimage"`,
  `"rank transform" "preimage" maximum cyclic`;
- `"local rank" "Lucas"`,
  `"rank transform" alternating Lucas 0202`,
  `"order-preserving maps" crown maximal three colors cycle orientation`;
- `"cellular automata" "local rank" maximum preimages 2024 2025 2026`
  and strict-smaller-neighbor/ternary-cycle variants;
- direct arXiv, Google Scholar and Semantic Scholar domain queries;
  a recent-183-day arXiv query, and the actual July 2026 Huang primary text.

Several queries produced no results or irrelevant rank/algebra/SEO hits;
these were not used as evidence. This is finite discrete mathematics, so
the generic skill's ML venue checklist is not substituted for the direct
image-processing and combinatorial owners. The installed novelty skill's
requested external Codex-MCP cross-model step was unavailable; tool
discovery found no callable such reviewer. The project's authorized
current-model process-separated source/proof audit was used instead and
is **not** described as an external or cross-model review.

## Source disposition

`LNR-S1` remains open: obtain and inspect Mukherjee's 2011 actual convergence
statement/proof, then give a literal full adapter or a precise residual
sharp theorem. An abstract is enough to expose this risk but not enough to
resolve it. Current result is **MATH_VALID / HOLD_SOURCE / NO_ADMISSION**.
The meaningful all-target extremal comparison has not been eliminated by
the inspected classical sources; it is also not a substitute for the
missing temporal-owner comparison. All external dissemination remains held.
