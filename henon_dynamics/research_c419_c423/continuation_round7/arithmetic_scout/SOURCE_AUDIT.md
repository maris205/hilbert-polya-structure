# Source audit for AP7, TR7 and FC7

Access date: 2026-09-08 UTC. This is a bounded source/ownership screen, not a
systematic review of the entire literature. All three questions are
AI-generated. Statements used and unresolved body-access comparisons are
separated in [SCOUT_REPORT.md](SCOUT_REPORT.md).

## 1. Local-first audit

Read the repository and Hénon `AGENTS.md` instructions, the batch skill and
workflow, the latest current-state checkpoint, and the selected research-lit,
idea-creator, novelty-check, and bounded ARS source-verification instructions.
No external-model run was requested or made. Zotero/Obsidian tools were not
available. The named `literature/`, `tools/`, and legacy arXiv-fetch helper
fallbacks were absent. Filename-filtered source discovery did not find a
relevant local source library for these exact questions.

Targeted Markdown collision inspection included:

- [round-seven plan](../SCOUT_PLAN.md);
- [AF5 arithmetic report](../../continuation_round5/arithmetic_frontier/SCOUT_REPORT.md)
  and the frozen retirement of AF5-C in the round-seven plan;
- CT1's frozen contract, proof package, and source audit in
  `continuation_round2/congruence_towers/`;
- [C394 question](../../../henon_padic_symplectic_analytic_interpolation_route_a/RESEARCH_QUESTION.md);
- [C409–C413 arithmetic scout §D](../../../research_c409_c413/arithmetic/SCOUT_REPORT.md);
- [P62 README](../../../henon_full_horseshoe_algebraic_exhaustion/README.md);
- [primitive coordinate-height question](../../../henon_primitive_coordinate_height_flat_pressure/RESEARCH_QUESTION.md);
- [C03 finite-field protocol](../../../next_paper_henon_candidate_search/code/c03_PROTOCOL.md).

One initial search named two nonexistent registry/current filenames; this
was corrected using `rg --files`. A broad filename/text discovery was
followed by bounded reads, not interpreted as a full corpus read. The
important collision is AP7's possible transfer to the scalar theory already
rejected in C409–C413. The distinction in Jacobian does not automatically
clear that collision.

## 2. Actual source access

| Source | Actual accessed locator | Use and limitation |
| --- | --- | --- |
| [Allen–DeMark–Petsche, Non-Archimedean Hénon maps, attractors, and horseshoes](https://arxiv.org/pdf/1610.04271) | Current arXiv PDF, 31 pages; Theorem 1; §4.2 Theorem 18; Proposition 19; §4.3 Theorem 20 and parts of its proof/Lemma 21; Theorem 22; §4.4 | Primary AP7 ownership. Numbering is from the accessed current PDF: the infinite Q3 family is Theorem **20**, not Theorem 22 in the older v1 search snippet. No full-paper read claimed. |
| [Fan–Fan–Liao–Wang, Minimality of p-adic rational maps with good reduction](https://arxiv.org/pdf/1511.04856) | §3.2, equations (3.2)–(3.3); Propositions 3.3–3.4; Corollaries 3.5–3.6; Theorems 3.7–3.8 locator and reference entries [14], [16] | Primary source containing the scalar decomposition framework and explicitly attributing the underlying convergent-series result. Original [16] was not separately body-read in this pass. |
| [Lee, The equidistribution of small point for strongly regular pairs of polynomial maps](https://arxiv.org/pdf/1203.1224) | Introduction Theorems A–B; generic/small definition; §7 Corollary 7.5, Corollary 7.6, Theorem 7.7 | Primary TR7 input. Genericity and height normalization must remain explicit. No strong all-point totally-real theorem is attributed to it. |
| [Smillie–Buzzard, Complex dynamics in several variables](https://library.slmath.org/books/Book31/files/smillie.pdf) | Theorem 14.2, proof, immediately following discussion, and bibliography entries for BLS 1993a/b | Author survey actually read for the real-support/maximal-entropy equivalence. It is transparently a survey, not falsely labelled the original proof. |
| [Bedford–Smillie, Real polynomial diffeomorphisms with maximal entropy: Tangencies](https://annals.math.princeton.edu/2004/160-1/p01) | Publisher metadata; PDF located and initially indexed; targeted opening of introductory body timed out | Original primary paper identified. No newly verified original theorem number is claimed for the equivalence used through the survey above. |
| [Ostafe–Shparlinski, On the degree growth in some polynomial dynamical systems and nonlinear pseudorandom number generators](https://arxiv.org/pdf/0902.3884) | arXiv v3 PDF; introduction; §2.1 equations (1)–(4); §2.2 degree growth; §3.2 Theorem 4 and opening proof | Primary FC7 comparator. Its triangular hypotheses are not discarded. |
| [Ostafe–Pelican–Shparlinski, On pseudorandom numbers from multivariate polynomial systems](https://doi.org/10.1016/j.ffa.2010.05.002) | Publisher search-indexed metadata/abstract; [author list entry 57](https://web.maths.unsw.edu.au/~alinaostafe/); direct publisher body open failed | **Hard unresolved comparison:** exact general theorem, hypotheses and length threshold not body-verified. Repeated title/PDF/theorem queries did not retrieve the needed primary body. No novelty clearance. |
| [Roberts–Vivaldi, A combinatorial model for reversible rational maps over finite fields](https://arxiv.org/pdf/0905.4135) | Introduction Theorem A and conditions (5); scaling (12); Theorem B locator; discussion linking finite Hénon cycles and polynomial roots | Primary ownership of the random-involution model, not a deterministic theorem about each orbit. |
| [Irokawa, Hybrid dynamics of Hénon mappings](https://arxiv.org/abs/2212.10851) | arXiv abstract/metadata only | Adjacent recent-literature lead. It was not used to assert a local attractor classification or absence thereof. |

Other discovery results included the 2026 title *Forward Julia sets for a
class of p-adic Henon like maps* and the August 2026 preprint *Computability of
Julia sets for complex Hénon maps: The role of attracting and neutral cycles*.
The relevant original bodies were not inspected. Thus AP7's current novelty
status is deliberately unresolved, not a claim that no post-2016 work exists.
Unrelated search results and a malformed stray arXiv open were discarded;
no claim relies on them. No secondary aggregator was used as a substitute
for an unaccessed theorem.

## 3. Complete search-bearing query ledger

**12 search-bearing calls, 38 query strings.** Two queries used a 190-day
recency filter. Queries below are literal inputs; publication dates, not
crawl-age snippets, govern any temporal claim. The ledger includes early
eliminated leads. Opens/finds and shell searches are not counted as query
calls. No result-free query is treated as proof of novelty.

### Call 1 — initial arithmetic alternatives (3)

1. `Hénon map p-adic parabolic fixed point local cycles prime powers Igusa`
2. `Hénon maps primitive prime divisors dynamical divisibility sequences`
3. `Hénon maps arithmetic orbit correlations finite fields exponential sums`

The first lead collided with CT1; the primitive-divisor lead was not pursued
as a fourth contract.

### Call 2 — local and correlation follow-up (4)

1. `"Non-Archimedean" "Hénon" attractors horseshoes`
2. `"Hénon" "p-adic" "parabolic"`
3. `"polynomial automorphisms" "exponential sums" finite fields`
4. `"Hénon" "correlations" arithmetic finite fields` — recency 190 days

### Call 3 — TR7 discovery (3)

1. `"Hénon" "totally real" periodic points`
2. `"polynomial automorphism" "Bogomolov" "totally real"`
3. `"Hénon" "maximal entropy" "all periodic points" real`

### Call 4 — TR7 height follow-up (4)

1. `"totally real" "canonical height" "Hénon"`
2. `"totally real" "regular polynomial automorphisms"`
3. `"Hénon" "height gap" "2025"`
4. `"Hénon" "height" "Bogomolov"`

### Call 5 — AP7 focused primary-source retrieval (2)

1. `Allen DeMark Petsche non Archimedean Hénon attractors horseshoes p adic odometer 1610.04271`
2. `Hénon map p-adic attractor minimal decomposition parameters Qp Allen DeMark Petsche`

### Call 6 — TR7 and FC7 ownership (3)

1. `"Hénon" "totally real" canonical height Bogomolov`
2. `"polynomial automorphism" "totally real" height`
3. `"Hénon" "exponential sums" finite fields orbit correlations`

### Call 7 — FC7 primary-author search (3)

1. `Henon maps finite fields exponential sums Shparlinski polynomial orbits`
2. `"Hénon" "finite fields" distribution orbit`
3. `"Henon" "totally" "height"`

### Call 8 — TR7 equidistribution/entropy sources (3)

1. `"Hénon" "Bogomolov" totally real`
2. `"canonical heights" "strongly regular pairs" Lee equidistribution 2013`
3. `Bedford Smillie real polynomial diffeomorphisms maximal entropy all periodic points real`

### Call 9 — all three source updates (3)

1. `"non-Archimedean Hénon" attractors classification 2025 2026`
2. `"equidistribution of small points for strongly regular pairs" arxiv`
3. `"Roberts" "Vivaldi" "finite fields" reversible maps cycle statistics`

### Call 10 — FC7 exact comparator discovery (4)

1. `"polynomial automorphisms" "exponential sums"`
2. `"Hénon" "character sums"`
3. `"Henon" "equidistribution" "finite" orbit`
4. `"polynomial dynamical systems" "exponential sums" orbits`

### Call 11 — primary bodies and recent AP7 leads (3)

1. `"On pseudorandom numbers from multivariate polynomial systems" pdf`
2. `"non-archimedean and hybrid dynamics of Hénon mappings" arxiv`
3. `"Forward Julia Sets" "Henon" 2026`

### Call 12 — unresolved comparator and final recency check (3)

1. `"On pseudorandom numbers" "Pelican" filetype:pdf`
2. `"On pseudorandom numbers from multivariate polynomial systems" "Theorem"`
3. `"Hénon" "height gap" "totally real" 2026` — recency 190 days

Each frozen candidate has at least three targeted primary-source query
strings, actual source access, and an explicit ownership deduction. That
minimum does **not** mean that each candidate has passed novelty review:
AP7's analytic reduction and recent-body comparison, TR7's strong-height
mechanism, and FC7's broader 2010 comparator remain material limitations.

## 4. Execution and provenance receipt

Mathematical program executions: **0**. New proof packages: **0**. Old
mathematical reruns, finite-field censuses, conductor searches, GPUs, paid
APIs, and Git writes: **0**. No mathematical CPU receipt is fabricated for
administrative document work. No source PDFs or manuscripts were saved.

Only this directory's Markdown report and audit were created with
`apply_patch`. Existing user/coordinator files were read but not edited.
Team communication supplied provisional candidates and then explicitly
down-ranked AP7 after the scalar-theory collision. No outside peer review
or formal A-grade is claimed.
