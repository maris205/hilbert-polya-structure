# Source-first audit: round 4 nonconservative arithmetic lane

Date: 2026-09-08 UTC. This is bounded, AI-generated source verification
for DH1 and DH2, not a comprehensive novelty search, external referee
opinion, proof of priority, or new-paper evaluation. The two exact
[contracts](FROZEN_CONTRACTS.md) were frozen before their full proof
write-up and before any mathematical code; no mathematical code was
ultimately needed. [Complete short proofs](COMPLETE_SHORT_PROOFS.md)
give the mathematical closure and classical deduction.

## Outcome and nearest-ownership map

| Candidate | What is actually covered | Residual and decision |
| --- | --- | --- |
| DH1, all integer $c$ and all rational periodic points of $H_c=(y,y^2+c-2x)$ | Local integral escape and contracting-cycle lifting are classical. Inspected C412 and Ingram statements have different determinants; neither inspected Hutz paper is a Hénon period atlas. | Exact all-$c$ classification closes in a short elementary proof. Literal-table novelty was not established, and no substantial increment remains. Not admitted. |
| DH2, fixed $H_0$, $P=(0,1)$, full-time return gcd | Question 47 of the 2024 problem list owns the broad question. Matsuzawa's 2025 general result also applies after the map-specific checks. | An even shorter inverse-congruence proof closes this instance without the general theorem. Not admitted; do not label it an unresolved Vojta gap. |

The DH1 map has forward Jacobian $2$, not $1/2$; the inverse has
Jacobian $1/2$. The native forward clock was retained. For DH2,
the second dynamical degree is $1$, not the numerical Jacobian $2$.

## Actual new query receipt

The following **20 query strings** were submitted this round, not
proposed for future work. Queries 1–16 were submitted at approximately
02:23–02:33 UTC; 17–20 followed during the same proof/source closeout.
Four queries used `recency:183`, covering a requested roughly
six-month discovery window as implemented by the search service.
This filter is not a guarantee of complete coverage or correct
publication dating by the search index.

| No. | Actual query | Filter or role |
| --- | --- | --- |
| 1 | `Hutz Ingram rational periodic points Henon maps integer coefficients determinant 2` | Broad nearest-owner discovery |
| 2 | `"Hénon" "periodic" "integer" "Jacobian"` | Map/coefficient boundary |
| 3 | `"Henon" "rational periodic points" 2026` | `recency:183` |
| 4 | `"Hénon" "integer coefficients" periodic Pezda` | Local-period predecessor search |
| 5 | `"Henon" "determinant" "2" "rational points"` | Exact determinant lead |
| 6 | `"Hénon" "rational periodic" "2026"` | `recency:183` |
| 7 | `"Hénon" "gcd" "2026"` | `recency:183` |
| 8 | `"Henon" "greatest common divisor" height` | DH2 discovery |
| 9 | `"Huang" "gcd" "polynomial orbits" Vojta` | Conditional/split boundary |
| 10 | `"dynamical" "gcd" "Hénon"` | Non-split boundary |
| 11 | `"gcd heights" "rational maps" "2026"` | `recency:183` |
| 12 | `"Hénon divisibility" theorem` | Return-ideal ownership |
| 13 | `"Matsuzawa" "generalized greatest common divisors"` | Recent general theorem |
| 14 | `Matsuzawa "greatest common divisors" "rational maps"` | Exact primary-source recovery |
| 15 | `Matsuzawa "UPPER BOUND" "generalized gcd"` | Bound/correction check |
| 16 | `Huang "Generalized greatest common divisors for orbits under rational functions"` | Exact primary-source recovery |
| 17 | `Bell Ghioca Tucker dynamical Mordell Lang étale maps theorem 1.3 arxiv` | Genericity dependency check |
| 18 | `"Hénon" "gcd" "inverse"` | Short-proof ownership check |
| 19 | `"Henon" "gcd" "backward"` | Short-proof ownership check |
| 20 | `"Hénon" "divisibility" "height"` | Original question/assumption check |

Some results were unrelated encryption papers, mirrors, abstracts,
or bibliographic aggregators. They were not promoted to evidence for
technical claims. Queries with no relevant new owner do not certify
the absence of one. The inverse/backward queries did not identify a
literal primary theorem for the exact elementary DH2 argument; this
does not turn a short reconstruction into an admissible paper.

## Original-source access and applicability

### S1. Ingram: actual Hénon source, restricted concrete period family

Patrick Ingram, [Canonical heights for Hénon maps, arXiv:1111.3609v1](https://arxiv.org/pdf/1111.3609v1).
The PDF endpoint returned 32 pages. Actually inspected the abstract,
introduction, Theorems 1.1, 1.2, 1.4 and nearby conjectural period
discussion in the first four pages, and the targeted Lemma 7.2 passage.
This is selected theorem-level access, not a full proof audit of all
32 pages. The version identifier is retained even though the PDF
itself also contains a later internal compilation date.

Its general canonical-height framework concerns Hénon maps, but its
specific detailed quadratic period/denominator discussion uses
$(y,x+y^2+b)$, with determinant $-1$. Its height statements and
period conjecture are not a necessary-and-sufficient all-parameter
atlas for DH1's determinant-$2$ map. We do not convert a numerical
check of a conjecture into a theorem.

### S2. Hutz–Ingram: one variable, not coupled Hénon dynamics

Benjamin Hutz and Patrick Ingram,
[On Poonen's conjecture concerning rational preperiodic points of quadratic maps, arXiv:0909.5050v2](https://arxiv.org/pdf/0909.5050v2).
The endpoint returned nine pages; the first two pages, including the
abstract and main conjecture/setup, were inspected. The map is
$z\mapsto z^2+c$ on the projective line. A parameter-height-bounded
verification is evidence for the one-variable conjecture, not a
Hénon all-$c$ classification. No later sections or code were run.

### S3. Hutz: projective morphisms, not this rational compactification

Benjamin Hutz,
[Rational periodic points for degree two polynomial morphisms on projective space, arXiv:0811.3225v2](https://arxiv.org/pdf/0811.3225v2).
Inspected the first two pages: abstract, projective polynomial-morphism
definition, and initial construction. Its objects are everywhere-defined
projective morphisms. The projective extension of our Hénon map has
indeterminacy, so the source cannot be invoked as a direct period
classification here. This was a source-scope rejection, not a claim
that projective morphism theory is irrelevant in general.

### S4. Original problem list: ownership of the broad return-gcd question

[Hénon maps: a list of open problems, journal HTML](https://armj.math.stonybrook.edu/html-articles/Files-2015-2024/23-70/index.html).
Inspected Section 11's arithmetic setup, Conjectures 2–5, return-ideal
definition, Theorems 6–7 and Question 47, plus the relevant reference
entries. This does not amount to reading every other section of the
problem list. Its return ideals are taken over an $S$-integer ring with
good reduction outside $S$. Question 47 includes both a growth question
and a separate infinitely-often bounded-ideal question. DH2 freezes
one growth instance only; the latter question is not answered here.

### S5. Huang: explicit conditional and split hypotheses

Keping Huang,
[Generalized Greatest Common Divisors for Orbits under Rational Functions, arXiv:1702.03881v2](https://arxiv.org/pdf/1702.03881v2).
The PDF endpoint returned 18 pages. The final targeted access displayed
the introduction, Theorem A, height setup and Theorem 2.9; these were
inspected. No full 18-page proof verification is claimed.

The accessed theorems assume Vojta's conjecture and split iterates of
two one-variable rational functions, with additional orbit/target
conditions. DH2 is coupled and asks for an unconditional statement.
These theorems were not applied to it. The source is used to prevent
the earlier conditional framework from being confused with either
the 2025 theorem or the elementary inverse proof.

### S6. Matsuzawa: recent unconditional ownership cross-check

Yohsuke Matsuzawa,
[Growth of generalized greatest common divisors along orbits of self-rational maps on projective varieties, arXiv:2507.05027v1](https://arxiv.org/html/2507.05027v1),
submitted 7 July 2025. The abstract record and the 24-page PDF were
accessed. Actual reading used the HTML introduction, Definitions
1.1–1.4, Theorem 1.5 and its caveats, Lemma 2.1 statement, Proposition
2.12 and the final proof of Theorem 1.5, Examples 3.1–3.3, Proposition
3.4 with its proof, and the adjacent examples/context. The whole
chain of intermediate algebraic-geometry lemmas was not independently
reproved. A guessed HTML version-2 endpoint failed; **no version 2
was verified**, and the report relies only on the accessed version 1.

The [proof note](COMPLETE_SHORT_PROOFS.md) explicitly checks the exact
map, affine inverse locus, codimension-two point target, degrees,
escape and genericity. The resulting source implication is not merely
conditional on Vojta. DH2 nevertheless has a shorter elementary proof
which does not depend on this preprint.

### S7. Barrios: a genuine recent correction, not a silent extra axiom

Benjamín Barrios,
[Correction to “An upper bound for the generalised greatest common divisor of rational points”](https://www.cambridge.org/core/journals/bulletin-of-the-australian-mathematical-society/article/correction-to-an-upper-bound-for-the-generalised-greatest-common-divisor-of-rational-points/BCCD71C21EC41114392A4B2EE858D19E),
DOI 10.1017/S0004972726101543. The publisher explicitly dates online
publication to **22 July 2026**, inside the six-month window. Actually
read the introduction, corrected Theorem 3.2 and its proof passage,
and references identifying the earlier article and Matsuzawa source.
The intervening preliminary lemmas were only partially inspected;
no complete independent audit of the four-page correction is claimed.

The correction adds ample normal bundle to the earlier
positive-dimensional result and acknowledges Matsuzawa's separate
inequality. The earlier general bound cannot be treated as unconditional
without that repair. Neither version is a proof input in our elementary
argument; the correction is not evidence that Matsuzawa's theorem is
itself retracted or needs the same extra assumption.

### S8. Bell–Ghioca–Tucker: precise étale genericity source

Jason P. Bell, Dragos Ghioca and Thomas J. Tucker,
[The dynamical Mordell–Lang problem for étale maps, arXiv:0808.3266v1](https://arxiv.org/pdf/0808.3266v1).
The PDF has 19 pages. Read the introductory setup and Theorem 1.3 /
Corollary 1.4 on printed page 3. The latter supplies genericity from
Zariski density for an étale map. It is used only in the optional
Matsuzawa hypothesis cross-check; our polynomial automorphism over
$\mathbb Q$ is indeed étale. The p-adic proof in later sections was
not independently audited. Search-engine “4 months ago” labels on
old hosted PDFs were not misreported as new 2026 theorem dates.

## Local nearest-neighbour deductions actually inspected

- [C412 introduction and main theorem](../../../continuation_c409_c413_round2/papers/C412_integer_henon/sections/1_introduction.tex):
  determinant-one family; not literally the DH1 coefficient pair.
  Only read; no accepted proof or mathematical program was reopened.
- [C109 route research question](../../../henon_dissipative_route_a/RESEARCH_QUESTION.md)
  and [its source audit](../../../henon_dissipative_route_a/SOURCE_AUDIT.md):
  fixed map $(x^2-91/16-y,x/2)$ with Jacobian $1/2$ and low-period
  witnesses, not an all-parameter rational atlas. Only read.

The broader repository text search reached for `rg` first and was
restricted to source/question/proof/introduction-type files. It was
not a claim that the whole repository or every historical source had
been exhaustively revalidated.

## Skill and authority boundary

This turn the main scout read the applicable `research-lit`,
`idea-creator`, and `proof-writer` skills in full; repository root and
Hénon instructions; the requested batch skill/workflow; and current
state relevant to the 3/5 continuation. ARS was restricted to bounded
source verification using its selected workflow, source-verification
agent instructions, and required quality/failure/argument/cross-agent
references. It was not a full deep-research or Socratic pipeline.

These skills influenced the work by requiring frozen quantifiers,
source-scope rejection, exact proof status, and a stop after classical
deduction. Historical paid-model/GPU examples were not executed;
the current internal team supplied the collaboration context.
No paid API, external model upload, Git change, evaluator, manuscript,
new C-number, or global admission-state write was performed by this lane.

## Claim boundary

There is no general absence-of-prior-art certificate and no claim
that the literal DH1 table or elementary DH2 proof has never appeared.
Both mathematical statements are proved as frozen; both are rejected
as substantial new-paper candidates. No source, reduction, or gcd
calculation is used to infer target Euler factors, root numbers,
automorphy, target zeros, or a Hilbert–Pólya realization.
