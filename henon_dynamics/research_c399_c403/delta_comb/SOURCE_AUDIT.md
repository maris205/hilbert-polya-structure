# Primary-source ownership audit: harmonic delta-comb

Audit date: 2026-09-05. Scope: the fixed-positive-finite-coupling claims in
[PROOF_PACKAGE.md](PROOF_PACKAGE.md), SHA256
`7a63727caee39ba2926e2fe93dd249df17ea9ec4ba5ddf7b760432f02898b0af`.
This is a bounded current-team literature check, not a global novelty or
present-day-open-problem certificate. It does not perform a Route A evaluation.
`NO_BAD_EULER_OR_ROOT_NUMBER` remains in force.

## Ownership conclusion

The harmonic chain, finite-positive-coupling compactness/strict positivity,
strong-resolvent Dirichlet limit, and Dirichlet divisor spectrum are classical
results of Egger né Endres and Steiner. They cannot be presented as the new
contribution. The candidate's proposed increment is its fixed finite
coupling two-term count with an explicit linear coefficient and controlled
`O_kappa(log k)` remainder, and the stated consequences of that count.
No matching formula was found in the specific passages and searches below.
That negative search result is weaker than proving that no earlier formula exists.

The norm-resolvent upgrade is derived in the candidate using compact domination.
That is a standard operator-theoretic mechanism, not a new general theorem.
Heat/zeta/Schatten consequences should likewise be identified as deductions from
the counting law, not as separate discoveries of their general transform methods.

## Accessed primary sources

### 1. Original model paper

Sebastian Egger né Endres and Frank Steiner, *An exact trace formula and zeta
functions for an infinite quantum graph with a non-standard Weyl asymptotics*,
Journal of Physics A: Mathematical and Theoretical **44**(18), 185202 (2011),
44 published pages. [DOI](https://doi.org/10.1088/1751-8113/44/18/185202),
[arXiv record](https://arxiv.org/abs/1104.1364),
[arXiv v1 PDF](https://arxiv.org/pdf/1104.1364v1).

Access: arXiv metadata and actual PDF text, especially Section 2, Theorems
2.1--2.2, equations (28)--(30), the final paragraph before Section 3, and
the start of Section 3. The accessed preprint has 50 pages; its page numbers
must not be confused with the 44-page version of record. Publisher-deposited
[Crossref metadata](https://api.crossref.org/works/10.1088/1751-8113/44/18/185202)
confirmed journal, volume, issue, article number and DOI; the publisher full
text itself was not retrieved.

The chain has lengths `pi/n`; identifying consecutive intervals with the
half-line places its interactions at `pi H_n`. Theorems 2.1--2.2 prove
compactness and the positive discrete spectrum for every positive coupling.
Equations (28)--(30) give the increasing-form/strong-resolvent Dirichlet
limit. Section 3 supplies the decoupled divisor spectrum. At printed
preprint p.10, the authors defer high-energy finite-coupling asymptotics to
a future publication. This establishes the scope of that paper only,
not that the problem remains open in 2026.

### 2. Egger dissertation: title/year and scope resolved

Sebastian Egger (title page: Sebastian Egger geb. Endres), *The solution of
the "constant term problem" and the zeta-regularized determinant for quantum
graphs*, dissertation, Universität Ulm. [DOI](https://doi.org/10.18725/OPARU-1951),
[repository item](https://oparu.uni-ulm.de/items/85bfa3c7-67a9-46f4-81b6-1ddefe00f428),
[official text extraction](https://oparu.uni-ulm.de/server/api/core/bitstreams/444820b4-8f1a-4e70-a22b-b6884cd41c6d/content).

Access: DOI redirects, the repository's public item/bundle metadata and its
own extracted full text via HTTPS. Inspected the title/front matter,
contents, introduction pp.3--4, Chapter 2 p.17, relevant keyword contexts
and bibliography; this was not a line-by-line review of all thesis proofs.
The browser could not render the repository PDF, so no PDF-visual inspection
is claimed. The official text, not the third-party transcript surfaced in
search, supports this assessment.

Metadata distinction: title page and `dc.date.created` say **2011**;
the defense date is 2012-02-16, the legacy availability is 2012-03-29,
the migrated record was accessioned in 2016, and DataCite's
`publicationYear` is 2016. Cite as a 2011 dissertation with defense/date
clarification if needed, not as a new 2016 finite-comb result.

The introduction attributes the infinite-chain results to its reference
[15] and says that work is outside the thesis. Chapter 2 explicitly
excludes graphs with infinitely many edges/vertices from its treatment.
Thus finite-graph constant-term or determinant statements there do not
by themselves establish the present finite-coupling infinite-chain formula.

### 3. Bifulco--Kerner infinite-graph comparison paper

Patrizio Bifulco and Joachim Kerner, *Some spectral comparison results on
infinite quantum graphs*, Journal of Mathematical Physics **65**(7),
073502 (2024). [DOI](https://doi.org/10.1063/5.0178226),
[arXiv record](https://arxiv.org/abs/2308.16869),
[arXiv v1 PDF](https://arxiv.org/pdf/2308.16869v1).

Access: actual arXiv v1 text (11 pages, dated 2023-08-31), particularly
Section 5 pp.6--7, equation (11), Theorem 11 and its following discussion;
publisher-deposited [Crossref metadata](https://api.crossref.org/works/10.1063/5.0178226)
verified the 2024 publication details. The version of record was not
retrieved, and its later theorem numbers are not attributed to arXiv v1.

Section 5 returns to the same harmonic chain, credits the 2011 paper,
and fixes `sigma=infinity` in Theorem 11's modified local Weyl law.
It mentions comparing two positive couplings as a possible question,
but the inspected theorem is not a two-term counting law at finite
coupling. The separate finite-volume graph results are different
contracts and do not close the present infinite-volume question.

### 4. Bifulco dissertation: later harmonic-chain sections checked

Patrizio Bifulco, *Contributions to the Diffusion on Graphs and Networks:
Regularity of Heat Kernels and a Heat Content Formula, Faber--Krahn
inequality for the Heat Content, p-Torsional Rigidity, Spectral Comparison
Results for Schrödinger Operators*, dissertation, FernUniversität in Hagen,
submitted 2025-06-25. [German National Library full text](https://d-nb.info/1388406829/34).

Access: actual PDF text (290 pages), title page, Sections 6.3.3 and 6.3.5
and relevant references; not the entire dissertation. Printed
pp.221--222 correspond to PDF pages 242--243. Section 6.3.3 writes the
harmonic-chain model in (6.3.27), explicitly labels (6.3.28) with
`sigma=infinity`, and fixes that value in Theorem 6.3.14. Section 6.3.5,
printed pp.229--230, treats bounded/integrable potential perturbations
while still taking `sigma=infinity`; see (6.3.48) and Theorem 6.3.19.
Those passages do not supply the candidate's finite-coupling law.
The nearby open question about more complicated comb *graphs* should
not be confused with this chain of point interactions.

### 5. Special-function inputs

Actual NIST DLMF pages inspected:
[10.25.2--3](https://dlmf.nist.gov/10.25),
[10.27.4](https://dlmf.nist.gov/10.27.E4),
[10.40.1](https://dlmf.nist.gov/10.40.E1), and
[5.11.1--2](https://dlmf.nist.gov/5.11).
They supply the modified-Bessel series/decaying and growing solutions, connection
identity, and sectorial Gamma/digamma expansions. The candidate itself
derives the compact-parameter uniform series bounds and root-counting
offset control needed when `a=1+/-1/k`; the DLMF references are not
cited as an already uniform finite-comb theorem. The Bessel solution
is for the exponential comparator only.

## Bounded search record and remaining gaps

Local filename search under the project `papers/` and `literature/`
found no specifically named Egger/Endres/Steiner/Bifulco or harmonic
delta-comb paper. No Zotero/Obsidian integration was available.
External discovery used author/title/DOI searches and targeted strings,
including `"finite" "coupling" "1104.1364"`,
`"Egger" "Steiner" "finite" "asymptotics" quantum graph`,
`"harmonic" "delta" "Weyl" spectrum coupling`,
`"quantum graph" "log(4" "kappa"`, and
`"pi/n" "delta" "eigenvalue asymptotics"`.
The searches did not identify the displayed finite-coupling two-term
formula. Search snippets and unrelated hits were not treated as
proof of either novelty or collision.

An additional independent current-team
[broader-source check](../reviews/DELTA_BROADER_SOURCE_CHECK.md)
subsequently inspected the Kostenko--Malamud shrinking-spacing/Jacobi
paper and the authors' later review of the Albeverio--Kostenko--Malamud
form criterion. Those sources also own qualitative discreteness
information applicable here; no matching explicit two-term count was
confirmed in their inspected statements. The original AKM 2010 form
paper remained abstract/metadata-only access. This audit did not itself
reread those additional papers; the linked report records their exact
access, theorem locators and boundary-condition distinctions.

This audit did not exhaust citation descendants, non-English literature,
general point-interaction asymptotic theorems, or all papers of the named
authors. In particular the broader Albeverio--Kostenko--Malamud
Sturm--Liouville literature cited by Bifulco--Kerner was not read in full
here (the additional report narrows that gap, without claiming full
access to the 2010 form paper). The finite-coupling formula remains a **proposed increment not
found in this bounded source set**. A prior complete formula discovered
later would change the paper-level novelty judgment without invalidating
the present derivation. No target Euler product, zero/divisor
correspondence, root number, or Hilbert--Pólya realization follows from
this ownership check.
