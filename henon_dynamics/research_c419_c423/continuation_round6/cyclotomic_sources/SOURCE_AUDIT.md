# AF5-C effective length and algorithm-ownership source audit

Date: 2026-09-08 UTC. This is the bounded source audit assigned by
[SCOUT_PLAN.md](../SCOUT_PLAN.md), not a new candidate, manuscript,
admission, or certification that no earlier theorem exists. The original
all-integer-parameter, all-cyclotomic-periodic-point contract is unchanged.

## Conclusions that can be used now

The required root-of-unity length is genuinely effective: the accompanying
[complete auxiliary proof](EFFECTIVE_LENGTH_LEMMA.md) gives, for every
integer $H\geq1$,

$$L_H=H\left(\prod_{p\leq4H}(p-1)\right)(2H)^{2H},\qquad M_H=L_H+2.$$

It covers zero, arbitrary containing cyclotomic fields, repeated roots,
and exact-length padding. Taking $H=2|c|+4$ covers the inherited Hénon
house bound. This removes the need to extract an unspecified constant
from Loxton. It does not establish a conductor bound or practical runtime.

The source audit does **not** support presenting effective torsion closure,
torus lifting, or Noetherian descent by itself as a new method. The closest
verified sources below already contain those ingredients. The possible
increment is the complete input-to-output procedure in the coordinator's
[global proof](../cyclotomic_algorithm/PROOF_PACKAGE.md): a computable
full-torus initialization, exact successor pruning, a detected fixed point,
and extraction of every point with its least native period. Whether this
combination is a substantial independent contract needs the separate
non-author proof/source/increment review. None of the auxiliary lemmas is
a separate paper slot.

## Scope, source standards, and actual access

Research-lit, novelty-check, proof-writer, and the bounded ARS source
verification instructions governed this work. The proof-writer action was
to replace the missing numerical input with a fully stated and proved
coarse bound; the literature skills required inspection of actual
hypotheses and algorithm bodies instead of title-based attribution.
The full ARS/Socratic/manuscript pipeline and legacy paid-model/GPU
defaults were not activated. Named Zotero/Obsidian tools and the relevant
local source helper were unavailable in this workflow; primary websites
were used. No mathematical program or old census was run. Source retrieval
and document reading are not experiment evidence.

`BODY READ` below means the identified relevant theorem/proof sections
were actually inspected, not that every page of a paper was read.
`METADATA ONLY` and `ACCESS FAILED` are not full-text validation.
All links were accessed or attempted on the date above. Search snippets
and secondary aggregators were discovery aids only. Version dates below
come from official records or the inspected author's PDF, not a search
engine's relative publication date. No local archival PDF checksum is
claimed; these are URL/version/locator receipts.

## 1. Root-length inputs and exclusions

### S1. Loxton 1972 — original bound, body not recovered

J. H. Loxton, *On the maximum modulus of cyclotomic integers*,
Acta Arithmetica 22 (1972), 69–85,
[publisher record](https://www.impan.pl/en/publishing-house/journals-and-series/acta-arithmetica/all/22/1/98202/on-the-maximum-modulus-of-cyclotomic-integers),
DOI [10.4064/aa-22-1-69-85](https://doi.org/10.4064/aa-22-1-69-85).

Status: **METADATA ONLY / ORIGINAL BODY ACCESS FAILED**. The publisher
download endpoint `/shop/en/publication/transaction/download/product/98202`
returned HTTP 403. EuDML record 205146 did not provide a readable body in
the bounded attempts. Theorem 1 and §6 are locators supplied by S3, not
locators independently checked in Loxton's original pages. Consequently
this audit does not claim to have extracted an explicit constant there.

### S2. Loxton 1974 — effectivity attribution, body not recovered

J. H. Loxton, *On two problems of E. M. Robinson about sums of roots of
unity*, Acta Arithmetica 26 (1974), 159–174,
[publisher record](https://www.impan.pl/en/publishing-house/journals-and-series/acta-arithmetica/all/26/2/100167/on-two-problems-of-e-m-robinson-about-sums-of-roots-of-unity),
DOI [10.4064/aa-26-2-159-174](https://doi.org/10.4064/aa-26-2-159-174).
The title above follows the publisher record; spelling variants in search
queries are preserved in the query ledger rather than silently corrected.

Status: **METADATA ONLY / ORIGINAL BODY ACCESS FAILED**. The corresponding
publisher download endpoint for product 100167 returned HTTP 403; EuDML
record 205303 did not yield the body. The proof of Theorem 5 is S3's
effectivity locator, not a claim of direct inspection here. Neither S1
nor S2 is an indispensable unverified inequality in the local proof.

### S3. Bajpai–Das–Kedlaya–Le–Lee–Leudière–Mello 2025

*The exceptional set in Cassel's theorem on small cyclotomic integers*,
[arXiv:2510.20435v1](https://arxiv.org/abs/2510.20435v1), submitted
23 October 2025; inspected [PDF](https://arxiv.org/pdf/2510.20435v1)
has 44 pages and an internal date of 24 October 2025. The official record
exposes v1, not a verified v2. Status: **BODY READ / PREPRINT**.

**Format-date discrepancy, rechecked during coordination:** the served
HTML labels itself v1, 23 October 2025, but its body displays 24 August
2026 and the title spelling “Cassels’s”; the served v1 PDF still displays
24 October 2025. No explanation or byte identity is established. The
locators below distinguish PDF and HTML; the shared identifier is not
treated as proof that the served bodies are identical. The local length
proof and the independently checked S4 identities do not depend on
resolving this provenance discrepancy.

Read Theorem 1.3 on PDF page 3, its effectivity attribution to S1/S2,
and [§§2.3–2.4](https://arxiv.org/html/2510.20435v1), Remark 2.9,
Lemmas 2.10 and 2.12, equations (7) and (9), including the proof of
Lemma 2.12(c). Theorem 1.3 states an effectively computable positive
constant for each $k>\log2$ in a lower bound for mean square in terms of
root-sum length. The inspected statement does not supply a numerical
value usable immediately as our initial torus dimension.

Its classical trace identities and largest equal-coefficient-class
normalization informed the auxiliary proof. The local proof rederives
them for a specified containing field, avoiding an unjustified
minimal-conductor inference. No novelty of these identities is claimed.

### S4. Malik–Stan–Zaharescu 2014

Amita Malik, Florin Stan, Alexandru Zaharescu, *The Siegel norm, the length
function and character values of finite groups*, Indagationes Mathematicae
25(3) (2014), 475–486,
[publisher record](https://www.sciencedirect.com/science/article/pii/S0019357713000979),
DOI [10.1016/j.indag.2013.12.001](https://doi.org/10.1016/j.indag.2013.12.001).
Status: **BODY READ** in the 13-page
[author-hosted PDF](https://sites.math.rutgers.edu/~am2365/MSZ.pdf).

Relevant locators: Lemmas 2.1 and 2.2, PDF page 4, give the prime and
prime-power integral decompositions and mean-square trace identities for
a containing cyclotomic field. Corollary 1 in §3, PDF page 8, gives the
expanded nonzero-coefficient identity. The algorithms in §3, PDF pages
8–9, enumerate bounded-Siegel-norm integers in a **fixed** cyclotomic
field; §4, PDF pages 10–11, addresses length for a supplied integer.
Lemma 4.2 is an additional field-dependent length estimate.

These are verified classical building blocks. Fixed-field enumeration
alone does not supply a uniform length bound over the cyclotomic closure.
The local proof explicitly supplies that missing uniform argument and
does not attribute its coarse displayed formula to S4.

### S5. Beli–Stan–Zaharescu 2018 — wrong meaning of rank for this task

*An effective bound for the cyclotomic Loxton–Kedlaya rank*, Glasgow
Mathematical Journal 60(1) (2018),
[publisher page](https://www.cambridge.org/core/journals/glasgow-mathematical-journal/article/an-effective-bound-for-the-cyclotomic-loxtonkedlaya-rank/236DA3BF43E3C8215627F8CEE957CEE8),
DOI [10.1017/S0017089516000586](https://doi.org/10.1017/S0017089516000586).
Status: **BODY READ** in the
[publisher PDF](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/236DA3BF43E3C8215627F8CEE957CEE8/S0017089516000586a.pdf/an_effective_bound_for_the_cyclotomic_loxtonkedlaya_rank.pdf).

Definitions on journal pages 97–98 and Proposition 1 in §5, page 104,
concern the multiplicative rank of a group of cyclotomic Weil numbers
modulo roots of unity. This is not the additive minimum number of roots
of unity representing an arbitrary bounded-house cyclotomic integer.
It is excluded as input (E); a matching name and the word effective do
not justify changing those hypotheses or conclusions.

### S6. Mello 2019 — related extension, not needed

[arXiv:1912.09010v1](https://arxiv.org/abs/1912.09010v1),
[official PDF](https://arxiv.org/pdf/1912.09010v1), introduction and
Theorem 1.1: **BODY READ, BOUNDED COMPARISON ONLY**. The Loxton-type
Kummer-extension result there was checked as a possible alternate source.
No explicit numerical constant was imported, and the local proof has no
dependency on this paper. This is distinct from the withdrawn affine
dynamics preprint S10 below.

## 2. Closest verified algorithm and dynamical sources

### S7. Ji–Xie–Zhang v2 — closest dynamical proof

*Cyclotomic integral points for affine dynamics*,
[arXiv:2511.13443v2](https://arxiv.org/abs/2511.13443v2),
20 January 2026. Status: **BODY READ / PREPRINT** in the
[official HTML](https://arxiv.org/html/2511.13443v2).
Relevant inspected locators: §1.4; §2, Theorem 2.1 and Corollary 2.2;
§3, Theorem 1.2 proof, Steps 1–4; Definition 1.7, Theorem 1.8 and its
§4 application, already audited for the fifth-pass finiteness helper.

Step 1 forms torus lifts from a pre-existing invariant set and discards
an exceptional subset. Step 2 forms its torsion correspondence. Step 3
already iterates a correspondence on a torus and explicitly uses a
decreasing sequence of torsion cosets and Noetherian stabilization, in
the paragraph defining $\psi^{\circ k}(Y)$ immediately before Step 4.
Thus claiming a new generic Noetherian torsion-correspondence mechanism
would overstate the increment.

The inherited finite-set theorem uses Theorem 1.8 plus the separately
proved absence of periodic affine curves; Theorem 1.8 alone is a
non-density statement. No claim that S7 itself prints the exact all-$c$
terminating atlas procedure was found in the inspected sections.

### S8. Aliev–Smyth — older effective torsion-coset algorithm

Iskander Aliev and Chris Smyth, *Solving algebraic equations in roots of
unity*, [arXiv:0704.1747v3](https://arxiv.org/abs/0704.1747v3),
official revision date 1 February 2008. Status: **BODY READ** in the
[official PDF](https://arxiv.org/pdf/0704.1747v3). The retrieved PDF
contains an internal 23 October 2018 date; that does not change the
official version history and is not silently relabeled a new submission.

Read introduction, PDF pages 1–4, and the complete §6 algorithm,
PDF pages 20–22: hypersurface steps H1–H4 and general-variety steps
V1–V2 determine maximal torsion cosets. This directly defeats any claim
that computing those cosets is new to AF5-C. Earlier algorithms cited
there are leads, not bodies verified here. The current kernel is instead
proved locally using rational Mann relations and exact integer algebra;
see its own [proof](../torsion_kernel/PROOF_PACKAGE.md) and
[source audit](../torsion_kernel/SOURCE_AUDIT.md).

### S9. Kedlaya–Kolpakov–Poonen–Rubinstein — explicit torsion closure

Kiran S. Kedlaya, Alexander Kolpakov, Bjorn Poonen, Michael Rubinstein,
*Space vectors forming rational angles*, inspected
[author-hosted PDF](https://math.mit.edu/~poonen/papers/space_vectors.pdf),
31 pages, internal date 19 May 2021. Status: **BODY READ** in §7,
PDF pages 10–12, including Definitions 7.1–7.2, Lemma 7.4,
Algorithm 7.5, Theorem 7.6 and its proof, and Remark 7.8.

Algorithm 7.5 takes a closed subscheme of a torus over a specified
cyclotomic field. Theorem 7.6 proves it returns its torsion closure and
proves recursive termination, using reductions of the field and
Noetherianity. Remark 7.8 reports an implemented SageMath variant and
practical dimensional limitations. The proof package does not rely on
or run that implementation. This is a verified independent prior
effective-closure source, not merely a qualitative torsion theorem.
The subsequent dynamical exhaustion and native-period extraction must
therefore carry any AF5-C increment; the generic closure subroutine cannot.

### S10. Mello affine preperiodicity — withdrawn version excluded

Jorge Mello, *Cyclotomic preperiodic points for morphisms in affine spaces
and preperiodic points with bounded house and height*,
[official arXiv record](https://arxiv.org/abs/2009.00947).
**VERSION WARNING:** v4, dated 24 November 2025, is withdrawn; the author
states that the old unpublished version has technical problems.
The historical [v3 PDF](https://arxiv.org/pdf/2009.00947v3), dated
2 December 2020, was read only for comparison: Definition 2.4,
Lemmas 2.6–2.7, and Theorem 3.1/proof, PDF pages 4–9. Its non-density
argument uses root-sum representations and torus equations under
property (*) and a no-common-zero hypothesis on the projective lift.
It is not accepted as a proof input.

The author's [publications page](https://www.jorgemello.org/publications)
separately lists a 2022 Functiones et Approximatio publication. Its
published body was not recovered or matched to v3 here. Withdrawal of
the old arXiv version is not evidence that the journal paper was retracted.
Independently, our map's homogenization
$[YZ:Y^2+cZ^2-XZ:Z^2]$ vanishes at $[1:0:0]$; thus the inspected
no-common-zero hypothesis cannot simply be applied to this Hénon family.

## 3. Ownership and residual increment assessment

The following is this audit's mathematical assessment, not an assertion
by any cited author. The auxiliary length proof is elementary classical
trace bookkeeping with a coarse explicit constant; the kernel is a
classical exact-algebra implementation. Their being fully spelled out
repairs proof dependencies but does not make them independent discoveries.

After subtracting those inputs, the coordinator's proposed full contract
still requires all of the following connected arguments:

1. A single computably sized torus encodes every sought orbit, including
   zero coordinates, without knowing the orbit set or a conductor cap.
2. Restricting the graph to both current endpoint sets, taking torsion
   closure, and projecting preserves exactly the torsion-successor
   condition. Closed projection alone is insufficient; torsion lifting
   is essential. The non-author review supplied the equivalent fixed
   correspondence form in global equation (4.5): compute
   $\Gamma=\operatorname{TC}(R)$ once, then intersect
   $\Gamma\cap(V\times V)$ and project. Repeated torsion-closure
   computation is neither necessary nor a claimed increment.
3. The computed descending closed sets have decidable equality. An
   equality test and a proof of eventual equality are distinct obligations.
4. At a fixed point, the image orbit lies in its original finite number
   field with a uniform integral house bound even when its root-of-unity
   representations use larger fields. Invertibility converts finite
   forward orbit to genuine periodicity.
5. All desired periodic points survive, while external finiteness makes
   each surviving connected-coset image constant; the resulting exact
   finite list carries the map's native permutation and least periods.

These are meaningful differences between an existence/non-density
argument and the stated terminating input-to-output algorithm. However,
their ingredients are very close to established methods. The correct
novelty-risk classification at this source stage is **HIGH ROUTINE-
EFFECTIVE-COMBINATION RISK; NO EXACT DUPLICATE LOCATED IN THIS BOUNDED
SEARCH**, not “novel proved” and not “the full theorem is false.”
The separate non-author review must decide whether the integrated
exhaustion proof, rather than isolated subroutines or extra pages, clears
the repository's substantial-independent-increment threshold.

This audit supplies no point list, runtime experiment, new cutoff census,
closed-form period bound, paper-level admission, formal evaluation, A2
promotion, target Euler factor, or root-number identification.
`NO_BAD_EULER_OR_ROOT_NUMBER` remains unchanged.

## 4. Reproducible bounded query ledger

Exactly **32 fresh keyword queries** were issued by this source worker
in this sixth pass. Reopening primary records, following links, finding
within bodies, and the kernel worker's separate queries are not counted
as additional queries here. Query 30 used a 190-day recency filter; other
queries had no recency filter. These queries cover alternate terminology,
classical sources, algorithmic analogues, exact-title searches, and recent
work. They do not constitute an exhaustive global novelty certificate.

1. `"Beli" "Loxton" "rank" pdf`
2. `"Loxton" "maximum modulus" "effective" roots unity`
3. `"cyclotomic integers" "length" "explicit" Loxton`
4. `"The exceptional set in Cassel" arxiv`
5. `"Loxton-Kedlaya" "rank" "Weil" bound`
6. `"On two problems of R. M. Robinson" Loxton theorem 5`
7. `site.arxiv.org "exceptional set" "cyclotomic"`
8. `"On the maximum modulus of cyclotomic integers" pdf`
9. `"On two problems" "Loxton" "impan"`
10. `"Siegel norm, the length function" pdf`
11. `"Loxton" "159" "174" pdf 1974`
12. `"Loxton" "69-85" pdf 1972`
13. `"On two problems" "Loxton" site:impan.pl`
14. `"Loxton" "aa22" pdf`
15. `"Loxton" "aa26" pdf`
16. `"On the maximum modulus of cyclotomic integers" "download"`
17. `"Hénon" "cyclotomic" "algorithm"`
18. `"Noetherian" "torsion" "periodic points" algorithm`
19. `"cyclotomic" "invariant sets" "effective" polynomial maps`
20. `"Hénon" "cyclotomic" "effective" 2026`
21. `"Henon" "abelian" "algorithm" periodic`
22. `"torsion cosets" "descending" "dynamics"`
23. `"Loxton" "Noetherian"`
24. `"Cyclotomic integral points for affine dynamics" effective algorithm`
25. `"cyclotomic" "periodic points" "terminating"`
26. `"torsion" "greatest fixed point" algebraic dynamics`
27. `"maximal invariant" "torsion cosets"`
28. `"cyclotomic" "periodic points" "algorithm" 2024 2025 2026`
29. `"Noetherian" "torsion" "algorithm" "invariant"`
30. `"cyclotomic integral points" 2026 algorithm effective` (recency 190 days)
31. `"Cyclotomic preperiodic points for morphisms in affine spaces" Mello arxiv`
32. `"Cyclotomic preperiodic points" "259" "279" DOI`

Fresh primary checks verified the official S3 and S7 versions, located
the actual S8/S9 algorithms, and exposed S10's withdrawal rather than
treating a search-result upload date as a current theorem. Access failures
for S1/S2 and the unmatched S10 journal body remain visible. This is an
AI-assisted source/proof audit, not a human-read attestation or external
peer-review receipt.
