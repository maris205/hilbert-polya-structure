# Paper 5 citation and source-integrity audit

Audit date: 2026-08-13  
Decision: **ACCEPT**  
Frozen PDF SHA-256:
`802ad1a1169be166d5a82da2e0247a92e6c848113303c7d70818bbdfd90acef5`

## Scope and method

Every bibliography key was mapped to its use in the manuscript, checked
against the source matrix, and compared with a primary publisher/archive
record or the locally acquired authoritative artifact.  Candidate-specific
claims were required to have a proof in the manuscript rather than an
analogy citation.  The final BibTeX run has no warning, every one of the ten
entries is cited, and there is no undefined citation.

## Identity and role checks

| Key | Identity check | Permitted role | Result |
|---|---|---|---|
| `Koopman1931` | “Hamiltonian Systems and Transformations in Hilbert Space,” PNAS 17(5), 315--318; DOI `10.1073/pnas.17.5.315` | historical Hilbert-space representation of dynamics | pass; plural title corrected from the original scan |
| `Stone1932` | *Annals of Mathematics* 33(3), 643--648; DOI `10.2307/1968538` | historical one-parameter-unitary-group theorem | pass |
| `TerElstLemanczyk2017` | ETDS 37(5), 1635--1656; DOI `10.1017/etds.2015.111` | modern Koopman-group convention and context | pass |
| `Teschl2009` | AMS GSM 99 (2009), ISBN 978-0-8218-4660-5, DOI `10.1090/gsm/099` | direct sums, Stone framework, spectral terminology | pass; first edition correctly cited |
| `NiederreiterXing2009` | Princeton chapter, pp. 1--29; DOI `10.1515/9781400831302-002` | exact irreducible-polynomial count | pass |
| `Deligne1974` | PMIHES 43, 273--307; DOI `10.1007/BF02684373` | closed-point/Frobenius dictionary and graded determinant | pass |
| `Bornemann2010` | *Mathematics of Computation* 79, 871--915; DOI `10.1090/S0025-5718-09-02280-7` | ordinary trace-class Fredholm determinant boundary | pass |
| `Kostant1970` | LNM 170, pp. 87--208; DOI `10.1007/BFb0079068` | historical geometric-quantization context only | pass; pages added from publisher contents |
| `WangTraceBridge2026` | local companion Paper 3 | same-object certificate provenance | pass; internal unpublished record |
| `WangFrobenius2026` | local companion Paper 4 | frozen classical positive-control provenance | pass; internal unpublished record |

## Claim-to-source boundary

- Teschl's direct-sum theorem is used only for the operator framework and
  spectrum closure; it is not cited as the source of the arithmetic degree
  ledger, dense rational spectrum, or multiplicity theorem.
- Deligne's determinant remains a finite-dimensional graded étale-
  cohomological determinant.  The manuscript does not relabel it as a
  determinant of the Koopman generator.
- Bornemann is used to delimit the ordinary trace-class Fredholm determinant,
  not to rule out all possible relative or regularized constructions.
- Kostant is non-load-bearing historical context.  No physical-quantization
  impossibility theorem is attributed to it.
- The point spectrum, infinite multiplicity, essential spectrum, noncompact
  resolvent, and heat-trace failure are proved directly for the frozen
  operator.

## Artifact integrity

The five acquired PDFs have the hashes recorded in `source_matrix.md`.
`pdfinfo` and `pdftotext` succeeded for each.  The ARS parser preflight was
unavailable because `pypdf` was absent, so the paper appropriately cites
stable section/theorem/equation locators rather than claiming reader-page
anchors.  This limitation is disclosed and does not affect the reproduced
candidate-specific proofs.

No citation or source-integrity revision remains required for release.
