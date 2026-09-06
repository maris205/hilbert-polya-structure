# C410 author-side citation audit

Date: 2026-09-06. Status: **PASS FOR THE CLAIMS ACTUALLY CITED**.
This is the manuscript author's source check, not an independent referee report
and not a claim of exhaustive priority clearance. The final independent review
remains a separate gate.

## Claim-to-source ledger

| BibTeX key | Verified primary record and inspected material | What the manuscript uses | Boundary |
|---|---|---|---|
| `benedetto2017cubic` | [Publisher full article](https://link.springer.com/article/10.1007/s40993-017-0092-8); introduction, Theorem 1.1, Corollary 1.3, Section 2 definition and Proposition 2.2, including its order recurrence | Attribution of the classical groups `E_n`, their orders, the number-field cubic realization, and the geometric characteristic-zero realization | Does not transfer its number-field arithmetic hypotheses, prime-density consequences, or its proof to the characteristic-three family |
| `bouw2021belyi` | [Publisher article](https://link.springer.com/article/10.1007/s00229-020-01204-3); Theorem 2.3.1 and its normalized dynamical Belyi setting | Broader characteristic-zero Belyi context for the already known groups | Does not assert that the theorem treats wild characteristic three; no complete proof read is claimed |
| `ejder2022arithmetic` | [Primary author preprint](https://arxiv.org/pdf/2201.09005); Definitions 2.1 and 2.2, Theorems 4.1, 4.2 and 6.1 were inspected; publication metadata verified from [DOI record](https://doi.org/10.1090/conm/779/15677) | The product-sign description in Definition 2.2 and arithmetic-monodromy context | No import of the arithmetic/geometric index result to arbitrary characteristic-three fields |
| `adams2025unicritical` | [Pinned primary version 1](https://arxiv.org/html/2504.13028v1); abstract, introduction and Theorem 1.1, including the explicit degree/characteristic hypothesis | Only the scope comparison: unicritical power polynomials with degree coprime to the characteristic | Bibliography explicitly pins `v1`; no claim to cover every later version or to establish exhaustive novelty |
| `hlushchanka2025cubic` | [Pinned primary version 1](https://arxiv.org/html/2507.05033v1); abstract, introduction, Theorem 1.5 and Remark 1.6 | Only the scope comparison: number-field results, with an expected extension discussed for characteristics prime to 2 and 3 | The expected extension is not described as a proved theorem; characteristic three is not included; bibliography explicitly pins `v1` |
| `stichtenoth2009function` | [Publisher book record and contents](https://link.springer.com/book/10.1007/978-3-540-76878-4); second edition, GTM 254, 2009, and Chapter 3 title/range verified | General attribution for classical Kummer, Artin--Schreier, different and Riemann--Hurwitz tools | This is not a claim to have read a subscription-only full chapter or verified an uninspected theorem number. The radical-degree and local facts actually needed are proved directly in Section 3 |

The two version-pinned comparisons were checked again against their primary
HTML texts during manuscript assembly. They are deliberately modest comparisons
of stated hypotheses, not negative conclusions drawn from search failure.

## Bibliographic metadata

- Benedetto, Faber, Hutz, Juul and Yasufuku: *Research in Number Theory* 3
  (2017), Article 29, 21 pages. DOI `10.1007/s40993-017-0092-8`.
- Bouw, Ejder and Karemaker: *Manuscripta Mathematica* 165(1--2) (2021),
  1--34. DOI `10.1007/s00229-020-01204-3`. The publication year in the
  bibliography is the issue year 2021; the online-first date is in 2020.
- Ejder: *Arithmetic, Geometry, Cryptography, and Coding Theory 2021*,
  Contemporary Mathematics 779 (2022), 91--102, AMS.
  DOI `10.1090/conm/779/15677`.
- Adams and Hyde: arXiv `2504.13028v1` (2025). No unverified journal,
  volume or page details were supplied.
- Hlushchanka, Lukina and Wardell: arXiv `2507.05033v1` (2025). No
  unverified journal, volume or page details were supplied.
- Stichtenoth: second edition, Graduate Texts in Mathematics 254, Springer,
  Berlin--Heidelberg, 2009. DOI `10.1007/978-3-540-76878-4`.

DOI content-negotiation/Crossref records were used to check authors, titles and
publication details; primary publisher pages resolved article numbering and
the online-first versus issue-year distinction. The bibliography has six
entries, and all six are cited. No placeholder citation keys remain.

## Attribution versus the present argument

The manuscript explicitly assigns the abstract groups, their recursive
definition, and their order formula to prior literature. The short group-order
proof is included for the degree comparison, not offered as a new theorem.
The normal form, the compatible Vandermonde construction, the zero-place
parity calculation, the mixed-radical induction, descent, and the geometric
different/genus calculations are written out in full.

No external paper is used as an undocumented replacement for one of those
proofs. The field `k` is allowed to be imperfect in the arithmetic statement;
only geometric completions are used in the local rank and genus statements.
The paper contains no claim to have constructed a Riemann-zeta model, a target
Euler product, a functional equation, or a Hilbert--Polya operator.

## Limits of this receipt

The audit verifies the narrow citations present in this manuscript and keeps
the inherited ownership boundary visible. It is neither a global novelty
certificate nor a fresh literature search covering all papers published after
the explicitly cited versions. It also does not replace independent checking
of the new proof or final batch reproducibility testing.
