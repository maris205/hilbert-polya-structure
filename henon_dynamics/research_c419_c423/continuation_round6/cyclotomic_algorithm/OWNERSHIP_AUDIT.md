# AF5-C: coordinator's bounded ownership and novelty audit

2026-09-08 UTC. Scope: the unchanged all-integer-parameter terminating
cyclotomic periodic-point procedure in [the proof](PROOF_PACKAGE.md).
This audit separates mathematical closure from independent paper-level
substance. It is not a global novelty certificate or external peer review.

## Core claims and closest-source deductions

| Claim tested | Primary prior art actually inspected | Residual after deduction |
| --- | --- | --- |
| A computable fixed-length torus represents all required periodic coordinates | Malik–Stan–Zaharescu's prime and prime-power trace identities, alongside the Loxton representation literature; the local full length lemma supplies a coarse explicit formula by those classical identities | A fully specified sufficient constant, not a new theory of cyclotomic integers or an independent slot |
| Exact torsion solutions and a descending torsion correspondence can be computed until stabilization | KKPR §7 already gives a general effective torsion-closure algorithm and a Noetherian termination proof; JXZ §3 Step 3 already descends along a fixed torsion correspondence and stabilizes by Noetherianity | The fact that these individual mechanisms exist is source-covered, not new |
| For every integer $c$, starting from the known whole torus yields the complete finite cyclotomic periodic list and its least native periods | JXZ Theorem 1.8 supplies non-density; the inherited classical curve argument supplies finiteness; neither inspected statement is itself an all-points output algorithm | The exact all-point-preserving combination, its stopping test, fixed-field periodicity argument, and list extraction; assess as a natural effective-corollary synthesis, not as an invented descent mechanism |

The first two rows have **low independent novelty**. The third is a
mathematically meaningful change from qualitative finiteness to a terminating
procedure, but has **high short-corollary/substance risk** after all closest
inputs are deducted. No numerical score is treated as a calibrated measure
of priority or publication prospects. The independent review and coordinator
admission decision, not the absence of an exact-title search hit, decide the
batch disposition.

## Actual primary-source reading by the coordinator

### 1. Ji–Xie–Zhang, arXiv:2511.13443v2

Opened the [official v2 HTML](https://arxiv.org/html/2511.13443v2), including
the exact Hénon definition and Theorem 1.8, §1.4, the full proof of
Theorem 1.2 in §3, and the adjacent proof of Theorem 1.3. This version is
dated 20 January 2026. In particular, §3 Step 3 explicitly defines a
decreasing sequence of torsion-coset images of a fixed correspondence and
invokes Noetherianity to stabilize it. The proof also uses Noetherianity
earlier to remove exceptional subsets from a preassigned dense point set.

This reading corrects the initial draft's overly broad emphasis on an
“added descending construction.” The source owns torus lifts, torsion
correspondences, and this stabilization mechanism. Our proof differs in
its known initial torus, exact retention of all periodic representatives,
and complete effective output. These are comparisons made here, not claims
quoted from the authors. The preprint is an explicit mathematical input,
not a claimed peer-reviewed certification.

### 2. Kedlaya–Kolpakov–Poonen–Rubinstein

Opened the author-hosted
[Space vectors forming rational angles PDF](https://math.mit.edu/~poonen/papers/space_vectors.pdf),
dated 19 May 2021, and read the relevant complete §7 algorithm, correctness
and termination argument (printed pages 10–12). Algorithm 7.5 accepts a
closed subscheme of a torus over a cyclotomic field; Theorem 7.6 proves
that it returns its torsion closure. Remark 7.8 reports a SageMath variant
and warns about computational difficulty. This is direct prior art for
effective torsion closure, not merely a qualitative existence theorem.

The local Mann/Smith-normal-form proof is a different exhaustive classical
implementation, not an independently new kernel. No claim that KKPR's
published software was run here is made.

### 3. Malik–Stan–Zaharescu

Opened the author-hosted
[The Siegel norm, the length function and character values of finite groups PDF](https://sites.math.rutgers.edu/~am2365/MSZ.pdf).
Read its introduction and the two exact trace statements, Lemmas 2.1 and
2.2, on printed page 4. These permit integral coefficient decompositions
in a containing cyclotomic field and supply the identities used by the
local explicit length proof. The paper's bounded-Siegel-norm enumeration
is stated for a fixed cyclotomic field; that does not alone give a uniform
root-length bound over all conductors.

The coordinator separately read all 321 lines of the local effective
length proof, rather than using its author's favorable summary.
The root-length formula is supported by that complete argument, not by an
unspecified asymptotic constant or a confusion with multiplicative rank.

### 4. Other source leads and exclusions

Opened the official HTML of
[Bajpai et al., arXiv:2510.20435v1](https://arxiv.org/html/2510.20435v1)
for metadata/introduction only; no coordinator full-paper reading is claimed.
The separate arithmetic source audit owns the detailed trace-identity
comparison. The page's version label and displayed body date are reported
as encountered there, not used to infer new theorem priority.

The search lead *Cyclotomic preperiodic points for morphisms in affine spaces
and preperiodic points with bounded house and height* was resolved to
[Mello's official arXiv record](https://arxiv.org/abs/2009.00947).
That record marks v4 withdrawn on 24 November 2025 and states that the old
unpublished version has technical problems. It is **not a proof input**.
This observation does not establish that any separately published version
is retracted or invalid; that broader assertion is not made.

The original 1965 Mann full proof was not obtained by the kernel source
owner. The coordinator read its entire 515-line local kernel proof and
144-line source audit; the needed rational indexed-subsum bound is proved
there in full, with the partial original-source access explicitly retained.
This removes a proof gap without pretending that inaccessible source pages
were read.

## Review-driven simplification and the remaining increment

The non-author reviewer observed that the torsion closure need only be
computed once. If $R$ is the known full lifted graph and
$\Gamma=\operatorname{TC}(R)$, then for every finite torsion-coset union $V$,

$$\operatorname{TC}\bigl(R\cap(V\times V)\bigr)
=\Gamma\cap(V\times V).$$

The right-hand side is already a finite torsion-coset union, is contained
in the left input set, and has exactly its torsion points; density proves
the identity. The revised algorithm uses the fixed-correspondence operation
$V\mapsto\pi_1(\Gamma\cap V^2)$. Thus recomputed torsion closure is also
removed as a proposed new mechanism. The revision simplifies the proof
without changing the original all-$c$, all-points, least-period contract.

No source statement in the inspected primary texts was identified that
literally gives this final Hénon output list algorithm. That bounded
observation is not enough to assert a substantial new paper. In particular,
changing a qualitative construction into its natural effective combination
can still leave only a short corollary once all ingredients are credited.

## Search methods, scope and exact coordinator query ledger

`research-lit`, bounded ARS source verification, and `novelty-check` govern
this audit. Current repository/runtime instructions use the selected team
for the non-author review, overriding the skills' older-model/external-MCP
defaults. No external model, paid API, GPU, human review, or cross-model
verification is claimed. Mathematical primary papers replace irrelevant
ML-conference/RCT evidence templates. Zotero/Obsidian and a relevant local
PDF/helper collection were unavailable in the actual preflight. Browser
search and primary source retrieval were used; Google Scholar and Semantic
Scholar were queried only through the displayed web-index formulations,
not through a database API or a claimed exhaustive database export.

The coordinator submitted these **18** search formulations during the
sixth pass. The first three preceded the proof draft; the following nine
tested the three core claim families; the last six supplied a recent-window
check and further output/extraction formulations.

1. `Loxton cyclotomic integer house bounded sum roots unity effective bound theorem`
2. `Mann theorem effective torsion cosets Laurent polynomial algorithm`
3. `Henon cyclotomic periodic points effective algorithm torsion cosets` (183-day filter)
4. `"cyclotomic periodic points" "algorithm"`
5. `"Hénon" "cyclotomic" "effective" 2025 2026`
6. `site:scholar.google.com cyclotomic periodic points effective computation Henon`
7. `"torsion cosets" "invariant" "algorithm" dynamics`
8. `"torsion" "Noetherian" "periodic points"`
9. `site:semanticscholar.org "cyclotomic" "periodic" "algorithm"`
10. `"maximal invariant" "torsion" "algebraic"`
11. `"cyclotomic" "descending" "correspondence" 2024 2025 2026`
12. `site:arxiv.org "cyclotomic" "periodic points" "effective" 2026`
13. `"cyclotomic" "periodic" "algorithm"` (183-day filter)
14. `"torsion cosets" "dynamical" "effective"` (183-day filter)
15. `"cyclotomic integral points" "computable"` (183-day filter)
16. `"bounded house" "periodic points" "algorithm"`
17. `"cyclotomic" "periodic points" "effective computation"`
18. `"torsion" "successor" "periodic" "Noetherian"`

Search results contained irrelevant finite-field sequence, dynatomic and
other similarly named topics; a recency filter did not reliably exclude
old publications. Publication/version dates were therefore checked on the
primary records. A combined result display was truncated, so this ledger
certifies submitted formulations, not complete reading of every result.
The ownership findings above rely on the separately opened primary texts.
Direct opens, source finds and PDF page retrievals are not additional
search queries or mathematical executions.

A bounded local collision search within this batch found the earlier AF5-C
finiteness attempt and the current work, without a separate admitted
cyclotomic algorithm. This is not a full-repository novelty certification.
The other owners' source ledgers are separate; overlapping searches are not
independent replication of a theorem.

## Decision boundary

The explicit all-$c$ procedure now has a complete source-dependent proof.
There is no implementation benchmark or practical parameter atlas in this
pass. The full non-author review and coordinator adjudication must keep
correctness, source ownership and sufficient independent substance separate.
No manuscript, admission, formal Route A evaluation, A2 promotion, Euler
factor, root number or target-zero correspondence is established by this
audit. `NO_BAD_EULER_OR_ROOT_NUMBER` is unchanged.
