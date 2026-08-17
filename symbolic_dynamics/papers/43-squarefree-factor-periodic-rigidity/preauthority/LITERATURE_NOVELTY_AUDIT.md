# Literature and novelty audit

## Audit date and scope

Search date: `2026-08-17 UTC`.

The search targeted five collision classes:

1. the squarefree admissible shift and squarefree flow;
2. proximality of \(\mathscr B\)-free systems;
3. preservation of proximality under topological factors;
4. periodic points and Artin--Mazur zeta of factors;
5. recent factor rigidity for power-free admissible shift spaces.

Queries combined `squarefree flow`, `admissible shift`, `B-free`,
`proximal`, `topological factor`, `periodic point`, `fixed point`, and
`Artin-Mazur zeta`. Primary arXiv, publisher, DOI, and institutional sources
were preferred. Search-result absence is not treated as proof of novelty.

## Primary-source chronology

### 1965: Artin--Mazur periodic-point zeta

M. Artin and B. Mazur introduced the periodic-point framework used by the
fixed-point exponential. The original article is *On Periodic Points*,
*Annals of Mathematics* 81 (1965), 82--99,
[DOI 10.2307/1970384](https://doi.org/10.2307/1970384).

Relevance: determinant convention only. It gives no squarefree factor theorem.

### 2011: squarefree admissibility and proximality

Peter Sarnak's institutional lecture notes identify the squarefree flow with
the admissible-support system and state proximality with the zero system as
the unique minimal subsystem:
[IAS record](https://publications.ias.edu/sarnak/paper/506) and
[lecture PDF](https://publications.ias.edu/sites/default/files/MobiusFunctionsLectures%282%29.pdf).

Relevance: direct collision with source identity and proximality. Those
components receive zero novelty credit. The notes use a one-sided
presentation; the present two-sided CRT proof is supplied locally rather than
transferred without proof.

### 2013--2015: broader \(\mathscr B\)-free context

E. H. El Abdalaoui, M. Lemańczyk, and T. de la Rue develop the dynamical
viewpoint for pairwise-coprime \(\mathscr B\)-free integers in
[arXiv:1311.3752](https://arxiv.org/abs/1311.3752), later published in IMRN
with [DOI 10.1093/imrn/rnu164](https://doi.org/10.1093/imrn/rnu164).

Relevance: source context, pattern measures, and chronology. It is not an
exact all-topological-factor periodic-ledger theorem in the audited scope.

### 2015--2018: general proximality classification

A. Bartnicka, S. Kasjan, J. Kułaga-Przymus, and M. Lemańczyk prove in the
two-sided \(\mathscr B\)-free setting that proximality is characterized by an
infinite coprime subset of \(\mathscr B\):
[arXiv:1509.08010](https://arxiv.org/abs/1509.08010), published as
*\(\mathscr B\)-free sets and dynamics*, *Transactions of the AMS* 370
(2018), 5425--5489,
[DOI 10.1090/tran/7132](https://doi.org/10.1090/tran/7132).

For \(\mathscr B=\{p^2:p\in\mathbb P\}\), the pairwise-coprime condition is
immediate. This is the strongest direct collision with the proof's central
property. The local CRT proof is still useful for exact auditability but not
novel.

### 2017: window characterization

S. Kasjan, G. Keller, and M. Lemańczyk characterize proximality of
\(\mathscr B\)-free systems through the associated window in
[arXiv:1702.02375](https://arxiv.org/abs/1702.02375).

Relevance: an independent broader route to known proximality. It further
lowers any source-property novelty claim.

### 2024--2025: power-free factor rigidity

F. Gundlach and J. Klüners study symmetries, morphisms, and factor systems of
power-free admissible shift spaces in
[arXiv:2407.08438v2](https://arxiv.org/abs/2407.08438), revised 2 June 2025.
Their Theorem 1.4 states rigidity for factor maps between power-free systems
\(\mathbb D_{K,k}\) and \(\mathbb D_{L,l}\), while Section 5 develops a
broader sieve-factor framework.

This is the nearest recent factor collision. In the audited HTML, searches for
`periodic`, `proximal`, and `fixed point` returned no theorem matching the
present arbitrary-factor periodic-ledger conclusion. Their target is another
admissible shift with a compatible acting-group morphism; the present target
is an arbitrary compact metrizable \(\mathbb Z\)-factor and the conclusion is
only its periodic ledger. This distinction is real but does not establish
novelty.

## Known versus locally assembled

| Component | Status | Novelty credit |
|---|---|---|
| squarefree admissible source | known | 0 |
| source proximality | explicitly known | 0 |
| factors preserve proximality | elementary general permanence | 0 |
| proximal system has at most one periodic point, necessarily fixed | elementary corollary | 0 |
| singleton fixed counts give \((1-z)^{-1}\) | immediate Artin--Mazur calculation | 0 |
| one-dimensional matrix \([1]\) realizes \(1-z\) | elementary | 0 |
| typed source-specific closure with repairs and Route verdict | program assembly | at most minimal |

## Exact collision result

The bounded search did not locate a primary source explicitly packaging the
following exact sentence with the same quantifiers:

> Every continuous surjective equivariant compact metrizable factor of the
> two-sided squarefree admissible shift has exactly one periodic point and
> Artin--Mazur zeta \((1-z)^{-1}\).

This is a bounded search result, not a proof that the sentence is unpublished.
Because every ingredient is known or elementary, an exact collision is
plausible and must remain a `STOP_DUPLICATE` condition.

## Novelty scorecard

| Axis | Score out of 10 | Reason |
|---|---:|---|
| source/object novelty | 0 | classical squarefree flow |
| theorem-mechanism novelty | 0 | known proximality plus elementary permanence |
| determinant novelty | 0 | singleton Artin--Mazur ledger |
| internal program closure | 2 | closes the C02 factor loophole with strict typing |
| standalone publication novelty | 1 | likely too elementary without a larger synthesis |

The score is intentionally conservative.

## Decision

`PROCEED_ONLY_AS_INTERNAL_EXACT_CLOSURE_TO_INDEPENDENT_DA`.

Do not advertise a new proximality theorem, a new factor theorem in general
topological dynamics, or a new arithmetic determinant. If independent review
finds the exact source-specific statement in primary literature, change the
decision to `STOP_DUPLICATE` while retaining the package as an internal audit
note.

## Chronology statement

All cited source facts, Session-4 outcomes, and the local theorem chain were
known before this final package freeze. The retrospective selector and the
package freeze confer no prospective, outcome-independent, novelty, priority,
ranking, or authorization credit.

