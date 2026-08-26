# Stage 4 REV-001 research record: bounded literature positioning

Search run: **2026-08-25 (UTC)**  
Revision item: **REV-001**  
Permitted manuscript target: **B0022 only**  
Status: **evidence package for later author-side revision; no manuscript or
patch has been changed**

## 1. Question and claim boundary

This update asks only whether a primary or authoritative record available by
the cutoff supplies either:

1. a direct post-source answer to Deninger's additive lifting question for
   the sheaf epimorphism
   \(\omega\colon\Zsh\twoheadrightarrow\Wsh\) on the finite-flat or fppf
   site; or
2. a proposition-level comparison close enough to delimit the present
   presentation, kernel-preservation, or descent-obstruction contribution.

The exact source is Christopher Deninger, *Rational Witt Vectors and
Associated Sheaves*, arXiv `2508.05329v1`.  The official arXiv record checked
on 2026-08-25 still lists only version 1, submitted 7 August 2025.  Its final
open question asks whether the sheafified Verschiebung admits a lift for the
`fp` or fppf topology.  In the source, `fp` means the **finite-flat** topology:
on p. 23, covers are defined as jointly surjective families of finite flat
morphisms.  It does not mean a finite-presentation topology.

This owner and version boundary is load-bearing.  Papers about p-typical
Witt vectors, spherical Witt vectors, arithmetic jet spaces, K-theory of
endomorphisms (KEnd), TR, or Grothendieck--Witt theory were not treated as
direct precedents merely because they use Frobenius or Verschiebung.

Primary source records:

- Deninger source and current version history:
  <https://arxiv.org/abs/2508.05329>
- Deninger v1 full text:
  <https://arxiv.org/html/2508.05329v1>
- Deninger--Mellit publisher record:
  <https://ems.press/journals/rsmup/articles/16288>
- Dotto--Krause--Nikolaus--Patchkoria publisher record:
  <https://www.cambridge.org/core/journals/compositio-mathematica/article/witt-vectors-with-coefficients-and-characteristic-polynomials-over-noncommutative-rings/26F8B8A6E4C4EBFAE28DB8B0B88F02C3>

## 2. Reproducible search protocol

### 2.1 Surfaces searched

The update used the following primary or authoritative surfaces:

- the current arXiv abstract/version record, arXiv HTML full text, and the
  official arXiv API;
- DataCite's DOI record for `10.48550/arXiv.2508.05329`;
- exact-DOI and exact-title queries in OpenAlex;
- Crossref DOI records for the two journal comparators;
- the EMS Press and Cambridge University Press article records and primary
  article full text;
- targeted web discovery only to locate the foregoing official records.

The search was run through the stated cutoff date.  The post-source arXiv
window was 7 August 2025 through 25 August 2026.  Result counts below are the
counts returned on the run date; they are an audit trail, not stable
bibliometric facts.

### 2.2 Inclusion and exclusion rule

A work entered the direct comparison only if inspection of its official
abstract and, where potentially relevant, primary full text showed one of
the following:

- the same sheafified reduced-monoid-algebra-to-rational-Witt morphism and a
  finite-flat/fppf additive lift or nonlift;
- an explicit algebraic presentation of a sufficiently close
  monoid-algebra-to-Witt quotient; or
- a proposition-level proof that Frobenius/Verschiebung descends through a
  stated kernel or quotient, retained only as a mechanism comparator.

Title-only overlap was insufficient.  Different p-typical, spherical,
arithmetic-jet, KEnd/TR, Galois-cohomological, derived, or
Grothendieck--Witt owners were excluded from the direct-precedent set.  No
claim is made about unpublished, unindexed, non-public, or future work.

### 2.3 Query ledger

The exact arXiv API query clusters and dispositions were:

| Query | Hits on 2026-08-25 | Disposition |
|---|---:|---|
| `all:"Rational Witt vectors" AND all:sheaf` | 1 | Deninger `2508.05329`; exact source only. |
| `all:Verschiebung AND all:fppf` | 0 | No indexed direct-title/abstract hit. |
| `all:"reduced monoid algebra" AND all:Verschiebung` | 0 | No indexed direct-title/abstract hit. |
| `all:Verschiebung AND all:sheafification` | 0 | No indexed direct-title/abstract hit. |
| `all:Witt AND all:"finite flat" AND all:sheaf` | 1 | Deninger `2508.05329`; exact source only. |
| `all:"rational Witt" AND all:Verschiebung` | 0 | No indexed hit under this exact field query. |
| `all:Verschiebung AND all:"monoid algebra"` | 0 | No indexed hit under this exact field query. |
| `all:Verschiebung AND all:descent` | 1 | `1710.10631`, a profinite-group/Galois lifting paper; owner mismatch. |
| `all:"monoid algebra" AND all:Witt` | 5 | Source plus nearby algebraic/homotopical owners; screened individually below. |
| `all:Verschiebung AND all:Witt AND submittedDate:[202508070000 TO 202608252359]` | 2 | `2601.22591` and `2601.20536`; both change owner, as recorded below. |
| `all:Witt AND all:descent AND submittedDate:[202508070000 TO 202608252359]` | 4 | Logarithmic Cartier, Witt-type algebra, Dold--Gauss, and Grothendieck--Witt hits; none uses the exact source morphism. |

The metadata/index checks were:

| Surface and query | Result | Permitted inference |
|---|---|---|
| arXiv abstract/version history for `2508.05329` | only `[v1]`, submitted 2025-08-07 | The searched source version had not been revised by the cutoff. |
| DataCite DOI lookup `10.48550/arXiv.2508.05329` | exact v1 metadata; `citationCount` reported as 0 and no citation-relation entries | A bounded index observation only; not evidence that no citing work exists. |
| OpenAlex exact DOI and exact-title queries | no work record returned | A coverage gap; no negative citation inference is licensed. |
| Crossref DOI lookups `10.4171/RSMUP/32` and `10.1112/S0010437X22007254` | exact journal metadata returned | Bibliographic verification of the two comparators, not a completeness search. |

## 3. Nearest-hit dispositions

| Primary work | What was verified | REV-001 disposition |
|---|---|---|
| Deninger, arXiv `2508.05329v1` (2025) | Exact morphism, finite-flat/fppf sites, and open lift question; official history still v1. | **Include as exact owner and version boundary.** The present paper also flags separately that the v1 sectionwise Corollary 4.6 requires correction; that issue must not be confused with the literature result. |
| Deninger--Mellit, *ZR and Rings of Witt Vectors \(W_S(R)\)*, RSMUP 142 (2019), Thm. 1.1 | An explicit kernel formula for a localized monoid-algebra map to truncated \(S\)-Witt vectors. | **Include as the closest algebraic-presentation comparator.** Its quotient is different and it does not treat sheafification or finite-flat/fppf descent. |
| Dotto--Krause--Nikolaus--Patchkoria, *Witt Vectors with Coefficients and Characteristic Polynomials over Non-Commutative Rings*, Compos. Math. 158 (2022), Prop. 1.39 | In their Witt-vectors-with-coefficients construction, Frobenius and Verschiebung descend to truncated quotients after the relevant kernels are shown to be preserved. | **Include as a kernel-preservation/descent mechanism comparator only.** It neither uses Deninger's morphism nor answers the finite-flat/fppf lift question. |
| *Witt vector rings and quotients of monoid algebras*, arXiv `1606.00482v2` | A p-typical quotient `ZR/I^n` for perfect \(\mathbf F_p\)-algebras. | **Screened; exclude from the direct set.** It is a farther algebraic comparator than Deninger--Mellit and changes both quotient and owner. |
| *An Alternative to Spherical Witt Vectors*, arXiv `2405.09606v2` | A completed spherical monoid-algebra construction. | **Screened; exclude from the direct set.** Homotopical/spherical owner, no exact sheaf epimorphism. |
| *Kernels of Arithmetic Jet Spaces and Frobenius Morphism*, arXiv `2601.22591v1` | Post-source work on kernels for arithmetic jet spaces and shifted \(\pi\)-typical Witt vectors. | **Most recent exact broad-query hit; exclude from the direct set.** Different arithmetic-jet and \(\pi\)-typical owner. |
| *A universal construction of \(p\)-typical Witt vectors of associative rings*, arXiv `2601.20536v1` | Post-source construction for associative-ring p-typical Witt vectors. | **Most recent exact broad-query hit; exclude from the direct set.** Different p-typical/noncommutative owner and no finite-flat/fppf sheaf lift. |
| *Lifting Theorems and Smooth Profinite Groups*, arXiv `1710.10631v1` | Module lifting over truncated Witt rings in a profinite/Galois-cohomological setting. | **Screened; exclude from the direct set.** The word “lifting” refers to a different object and obstruction problem. |
| KEnd/TR and Grothendieck--Witt hits already catalogued in the Phase-2 screen | Frobenius/Verschiebung operations or Witt terminology in stable, trace, or quadratic owners. | **Retain only as owner-substitution controls.** They are not direct precedents and do not bear the negative exact-owner search conclusion. |

## 4. Bounded conclusion and contribution subtraction

Within the declared public, primary/authoritative search surfaces, no direct
post-7-August-2025 solution to Deninger's finite-flat/fppf additive lifting
question was located by 2026-08-25.  The official source remained v1.

This is a reproducible bounded negative result, **not** a global novelty or
priority claim.  In particular, DataCite's zero citation count cannot be
used as a completeness claim, and the absence of an OpenAlex record weakens
rather than strengthens citation-coverage inference.

After subtracting the two closest precedents, the manuscript's safely
stateable addition is narrow:

- beyond Deninger--Mellit's different algebraic quotient, it gives an
  explicit all-index obstruction for the sheaf epimorphism actually posed by
  Deninger;
- beyond Dotto et al.'s positive kernel-preservation mechanism in another
  Witt-vector owner, it exhibits a concrete failure of global descent for
  the distinguished rational Witt sections and derives the corresponding
  extension-class consequence; and
- it addresses additive lifts of \(V_N\), not Frobenius lifts, a compatible
  system of Witt operations, or ring endomorphisms.

## 5. Exact English replacement draft for B0022

The following is a copy-ready replacement candidate.  It deliberately keeps
the search and originality claims bounded.  It is not applied here.

```tex
The exact source remains Deninger's version-1 preprint, whose final question
asks whether the sheafified Verschiebung admits an additive lift for the
finite-flat (his \(fp\)) or fppf topology
\cite[p.~25]{Deninger2025Rational}.  The closest earlier algebraic
presentation result is Deninger--Mellit's explicit kernel computation for a
localized monoid-algebra map to truncated \(S\)-Witt vectors
\cite[Thm.~1.1]{DeningerMellit2019}.  A separate mechanism comparator is
Dotto--Krause--Nikolaus--Patchkoria: for their Witt vectors with
coefficients, Frobenius and Verschiebung descend to truncated quotients after
the relevant kernels are preserved
\cite[Prop.~1.39]{DottoKrauseNikolausPatchkoria2022}.  These results are
retained respectively as presentation and kernel-preservation precedents;
neither concerns the epimorphism \(\omega\colon\Zsh\twoheadrightarrow\Wsh\)
or finite-flat/fppf descent for that owner.

A bounded update completed on 25 August 2026 searched the current arXiv
record, version history, and API; DataCite and exact DOI/title queries in
OpenAlex; Crossref; and the relevant EMS Press and Cambridge University
Press records.  Exact query clusters paired ``Verschiebung'' with ``fppf'',
``sheafification'', ``rational Witt'', ``reduced monoid algebra'', ``finite
flat'', and ``descent'', and a post-7-August-2025 query screened broader Witt
hits against the exact source owner.  Inclusion required either a direct
answer for that sheaf morphism or a proposition-level presentation,
kernel-preservation, or descent comparison.  The nearest recent hits instead
concern arithmetic jet spaces and p-typical associative Witt vectors;
spherical, KEnd/TR, Galois-lifting, and Grothendieck--Witt results likewise
change the owner and were excluded from the direct-precedent set.  Within
this declared scope, the source remained at version 1 and no direct
post-source solution to the finite-flat/fppf additive lifting question was
located.  This bounded negative result is not a claim of global priority.

Our contribution is correspondingly narrow: we answer the additive lifting
question for \(V_N\), compute a concrete all-index descent obstruction for
the stated sheaf epimorphism, and record its formal extension consequence.
We do not construct a lift of Frobenius, a compatible system of Witt
operations, or a ring endomorphism.
```

## 6. Fully verified new BibTeX, if the comparator is adopted

The manuscript bibliography was not edited.  Cambridge University Press and
Crossref agree on the following metadata:

```bibtex
@article{DottoKrauseNikolausPatchkoria2022,
  author  = {Dotto, Emanuele and Krause, Achim and Nikolaus, Thomas and
             Patchkoria, Irakli},
  title   = {Witt Vectors with Coefficients and Characteristic Polynomials
             over Non-Commutative Rings},
  journal = {Compositio Mathematica},
  volume  = {158},
  number  = {2},
  pages   = {366--408},
  year    = {2022},
  doi     = {10.1112/S0010437X22007254},
  url     = {https://doi.org/10.1112/S0010437X22007254}
}
```

## 7. Risks to carry into author-side revision

1. **Bounded negative only.** Public arXiv/index/publisher coverage cannot
   exclude unpublished, unindexed, non-public, or differently worded work.
2. **Index asymmetry.** DataCite's reported zero citations is not a citation
   guarantee; OpenAlex did not return the exact source record.  Neither fact
   may be promoted into evidence of absence.
3. **Version sensitivity.** The exact owner is explicitly `v1` as of the
   cutoff.  A later source revision would require rechecking both the open
   question and the manuscript's separate correction of Corollary 4.6.
4. **Comparator overreach.** Dotto et al. is useful only for the abstract
   kernel-preservation mechanism.  It must not be described as solving or
   nearly solving Deninger's finite-flat/fppf sheaf problem.
5. **Owner substitution.** KEnd/TR, p-typical, spherical, arithmetic-jet,
   and Grothendieck--Witt papers must remain exclusions, not evidence for a
   direct historical chain.
6. **Citation dependency.** If the proposed B0022 text is adopted, the new
   BibTeX entry must be inserted and the proposition locator checked in the
   compiled bibliography; this research task intentionally does neither.
