# Optimal-cycle measures: coordinator's bounded novelty check

2026-09-09 UTC. Current-team internal synthesis, not a priority certificate.
This record is for one proposed measure contract, not three paper slots.
Admission remains a separate independent-review/coordinator decision.

## Proposed result and three technical claims

For every odd prime p, every complete algebraically closed ultrametric
field K of characteristic p, and every s with 0 < |s| < 1, put
P(z)=(1+s)z+z². Let Π_e be its unique ordinary p^e-cycle in the open
unit disk. Normalize v(s)=1 and set r=(p−1)/p.

1. **MC1, divergent all-higher-level contact.** For every β in Π_d and
   every e>d, the real average of v(β−α), α in Π_e, equals
   c_d=(p−1)p^(−d−1)v((P^(p^d))′(β)−1), with
   c_d ≥ d r³+r²(1+1/p). The derivative is proved different from one.
   The bound is uniform in all e>d and valid over every K above.
2. **MC2, the original measure question.** The uniform real probability
   measures on Π_e converge along the full sequence on the Berkovich
   projective line. The union of their supports has compact closure
   inside the classical field, and the cycles converge in Hausdorff
   distance. There is an explicit coupling bound |s|^(c_d).
3. **MC3, identification of the limit.** The limiting support A, distinct
   from the closure of the entire union, is an aperiodic minimal system
   conjugate to translation by one on Z_p. The limit is nonatomic Haar
   probability under this conjugacy. The compact isometric inverse-limit
   mechanism itself is classical; the candidate increment is proving its
   hypotheses and aperiodicity for these particular polynomial cycles.

The coordinator has read both full A1/D1 proofs, their reports, and both
full E2/E1 mathematical reviews. Those reviews have zero open mathematical
or source-applicability must-fixes. This synthesis does not turn their
proof verdicts into a claim of publication priority.

## Closest prior work and exact subtraction

| Primary source | Actual overlap and boundary |
| --- | --- |
| Lindahl–Rivera-Letelier, *Optimal cycles in ultrametric dynamics and minimally ramified power series*, preprint 2013, v3 2015; Compositio 152 (2016), 187–222 | Problem 1.3 asks exactly this selected-cycle convergence question. Theorem C and minimal ramification supply existence, uniqueness, and the common sphere. These inputs are fully credited. They do not supply MC1 or conclude MC2/MC3. [Primary text](https://arxiv.org/html/1311.4478v3), [publisher](https://doi.org/10.1112/S0010437X15007575). |
| Jacobs, *Equidistribution of the crucial measures in non-Archimedean dynamics*, arXiv:1409.4808v2 (2017) | Theorem 2 allows general complete algebraically closed non-Archimedean K. Its measures have reduction-dependent weights at type II points, with zero weights at types I/III/IV. These are not the equal-weight type I measures on Π_e. The exact convergence proof uses resultant/Laplacian estimates. The exclusion is the measure definition, not characteristic. [Primary text](https://arxiv.org/pdf/1409.4808). |
| Nordqvist–Rivera-Letelier, *Residue fixed point index and wildly ramified power series*, arXiv:1904.04494v3 (2020) | Theorem 3 bounds norms of non-fixed periodic points for tangent-to-identity q-ramified series, 1≤q<p. Its proof uses explicit iterate coefficients and a periodic norm bound. This is not selected-cycle convergence; later progress on LRL Conjecture 1.2 is not a solution to Problem 1.3. [Primary text](https://arxiv.org/pdf/1904.04494). |
| Kallal–Kirkpatrick, *Ramification of Wild Automorphisms of Laurent Series Fields*, arXiv:1611.01077v3 (2019) | X1 checked Theorem 1.6 and §4: a finite-coefficient ramification criterion under p>b² and periodic norm applications, not MC2. The coordinator relies on the separately attributed X1 read for this branch; no coordinator full-proof read is claimed. [Primary text](https://arxiv.org/pdf/1611.01077). |
| Hurder–Lukina, *Essential holonomy of Cantor actions*, 2023 manuscript, §§2.2–2.3 | Classical clopen-quotient inverse-limit coding and the unique invariant measure obtained from finite uniform measures/Haar measure. This broader mechanism is subtracted from MC3, not presented as new. The candidate must establish the actual polynomial limit and exclude finite cycles itself. [Primary text](https://homepages.math.uic.edu/~hurder/papers/93manuscript.pdf). |
| Baker, Berkovich lecture notes, Theorem 2.3.2 and §2.4 | Established seminorm topology, compact Hausdorff spectra, and the classical-point embedding. No ambient local compactness of K or metrizability of its entire Berkovich line is used. Compactness of the particular classical cycle closure is a separate proved conclusion. [Primary notes](https://swc-math.github.io/aws/2007/BakerNotesMarch21.pdf). |

The coordinator read the original question and relevant cycle theorem,
Jacobs's definition, Theorem 2 and complete proof on printed pp. 24–25,
Nordqvist–Rivera-Letelier's Theorem 3 and complete §4.2 proof, and the
Hurder–Lukina and Baker passages named above. X1's independently written
[source report](x1_optimal_measure_sources/REPORT.md) has also been read
in full, including its precise retrieval limitations.

## Search coverage: executed formulations, not invented database access

The coordinator used the following three formulations for MC1:

- `"optimal cycles" "average" contact multiplier`
- `"quadratic" "periodic" "interlevel" "valuation"`
- `"Lindahl" "Rivera-Letelier" "multiplier" measures`

For MC2:

- `"Lindahl" "Rivera-Letelier" "Problem 1.3" measures`
- `"optimal cycles" "weak" convergence`
- `"quadratic" "positive characteristic" "periodic cycles" "measure"`

For MC3:

- `"optimal cycles" "odometer"`
- `"optimal cycles" "Haar"`
- `"quadratic" "positive characteristic" "adding machine"`

A further MC3 pass used `"optimal cycles" "adding machine"`,
`"Lindahl" "Rivera-Letelier" "odometer"`, and
`"quadratic" "characteristic p" "Haar" "periodic"`.
Broad queries returned substantial irrelevant material; this is recorded
as poor retrieval specificity, not evidence for novelty.

The coordinator's additional arXiv-restricted pass used
`"optimal cycles" ultrametric convergence 2024 2025 2026`,
`"Rivera-Letelier" periodic measures` with 184-day recency, and
`"ultrametric" "odometer" "cycles"` with 184-day recency.
Returned hits included old papers; their publication dates were checked
and were not relabeled recent on the basis of crawl metadata. The intended
recent interval was approximately 9 March–9 September 2026. No matching
new theorem was identified, but the search engine is not an exhaustive
arXiv date-range export.

X1 separately records additional exact-question/equidistribution queries,
2024–2026 and recent-six-month arXiv queries, Scholar and Semantic Scholar
discoverability attempts, the failed direct Scholar/graph retrieval, and
unavailable Cambridge cited-by data. None is represented as an exhaustive
forward-citation graph or zero citations. ML conference proceedings are
not a relevant primary venue for this arithmetic-dynamics theorem; no
ICLR/ICML/NeurIPS database coverage is claimed. No configured library
connector or unavailable tool is represented as having been used.

Local collision checks covered the current admission ledger, the prior
batch admission ledger, and R3 material. R3 supplies arithmetic motivation
and a displacement tool, not an already admitted selected-measure theorem.

## Independent increment and risks

MC1 has **medium-to-high apparent surviving novelty**, bounded by this
search. Its product/derivative algebra is elementary in isolation; the
essential new content is the finite, uniform all-anchor identity together
with a divergent bound covering the original full family.

MC2 has **high apparent substantive distinction**, conditional only on the
bounded source conclusion: it answers the precise public convergence
question with the original parameters and proves compact classical support.
It is not a reinterpretation of a known all-periodic-point or crucial-measure
equidistribution theorem.

MC3 has **low novelty as an abstract mechanism, medium as an established
feature of this concrete limit**. It belongs to the same measure paper.
The aperiodicity proof uses the finite average identity to separate the
limit from every fixed old cycle; generic invariant-measure theory does
not by itself supply that input.

Heuristic synthesis: **7/10, PROCEED WITH CAUTION**. This is not a calibrated
probability, mathematical evidence, or publication prediction. The chief
risk is an inaccessible/unindexed later solution, or an antecedent contact
identity under different terminology. The primary theorem claims and the
new proof must be positioned narrowly without asserting “first,” “currently
open,” or a universal priority conclusion.

The proposed question is not the already admitted UL4 field-transitivity
question: it ranges over arbitrary K and λ and concerns a real measure
and its limit dynamics. Neither full local Galois transitivity nor oriented
AS quotient stability is a premise of its standalone convergence proof.
Shared Hensel/displacement inputs must be cited once and not sold twice as
new work. Independence/substantiality is submitted to E7 for a separate
actual-file adjudication; the final paper count is the coordinator's.

The novelty-check skill supplied the three-claim search/subtraction format.
Its old external GPT-5.4 example is replaced by the user-authorized current
team review under the repository workflow; no external model review or
upload occurred. There were zero mathematical executions for this check.
