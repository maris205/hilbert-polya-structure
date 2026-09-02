# P166 source verification and subtraction log

Status: **Reviews A-B accepted source boundary / no novelty certificate /
`HOLD_EXTERNAL`**.  
Metadata rechecked: 2026-09-03.

## Cited records

| Key | Verified record | Verification surface | Role and subtraction |
|---|---|---|---|
| `Hamming1950` | R. W. Hamming, “Error Detecting and Error Correcting Codes,” *Bell System Technical Journal* 29(2), 147–160 (1950), DOI `10.1002/j.1538-7305.1950.tb00463.x` | publisher DOI metadata | Hamming-weight/code terminology: zero contribution |
| `MeyerPommersheim2010` | D. A. Meyer and J. Pommersheim, “Single-Query Learning from Abelian and Non-Abelian Hamming Distance Oracles,” *Chicago Journal of Theoretical Computer Science* 2010(13), DOI `10.4086/cjtcs.2010.013`, arXiv:0912.0583 | journal record, authors' paper, arXiv record | exact `n=2` parity-controlled complement map: zero contribution |
| `BuhlerEtAl1994` | J. Buhler, D. Eisenbud, R. Graham, C. Wright, “Juggling Drops and Descents,” *American Mathematical Monthly* 101(6), 507–519 (1994), DOI `10.1080/00029890.1994.11996984` | publisher DOI metadata | one-ball siteswap/weight-dependent cyclic neighbour: zero contribution |
| `KonheimWeiss1966` | A. G. Konheim and B. Weiss, “An Occupancy Discipline and Applications,” *SIAM Journal on Applied Mathematics* 14(6), 1266–1274 (1966), DOI `10.1137/0114101` | SIAM DOI metadata | classical occupancy/parking background: zero contribution |
| `LacknerPanholzer2016` | M.-L. Lackner and A. Panholzer, “Parking Functions for Mappings,” *JCTA* 142, 1–28 (2016), DOI `10.1016/j.jcta.2016.03.001` | publisher DOI metadata | parking on functional digraphs: zero contribution |
| `MeylesEtAl2023` | L. C. Meyles et al., “Unit-Interval Parking Functions and the Permutohedron,” arXiv:2305.15554 (2023) | arXiv author/title record | ordered-Bell/Fubini parking connection: zero contribution |

All six cited entries occur in the manuscript, and the BibTeX build reports
no missing entry or warning.

## Direct binary overlap

For binary words, Meyer--Pommersheim define the transformation that fixes a
word of even weight and complements a word of odd weight.  Over `F_2` this
is exactly

```text
x -> x + (wt(x) mod 2) 1.
```

Thus the coupled family's entire `n=2` member is directly owned background.
The manuscript says this explicitly, assigns it zero contribution credit,
and uses it only as a boundary check.

## Neighbour subtraction

- Siteswaps: weight-dependent cyclic motion is established background, but
  the carrier and update are different.  The paper claims no siteswap
  theorem.
- Parking and occupancy: weak compositions, cyclic occupancy encodings,
  multinomials, and ordered Bell numbers are standard ingredients and are
  assigned zero contribution.
- Generic functional graphs and zeta functions: cycle/tree vocabulary,
  divisor summation, and the zeta product conversion receive zero credit.
- Hamming weight and diagonal translations: terminology and group-action
  facts receive zero credit.

## Bounded non-hit and claim ceiling

A bounded search did not locate the literal coupled family
`(Z/nZ)^n`, `x -> x+wt(x)1`, for general `n`, nor its exact occupancy phase
map `j -> j+m_j`.  This is a non-hit, not evidence of novelty.  The residual
object under study is only the conjunction of the `n>=3` temporal census
and the target-resolved one-step inverse atlas.  External circulation
remains **`HOLD_EXTERNAL`**.

Independent Hostile Review A re-ran the owner and portfolio-collision audit
and returned no finding.  This is a Round-1 no-change source freeze, not an
expansion of the contribution claim.

Fresh Hostile Review B independently subtracted the exact binary boundary,
siteswap landing permutations and gap vectors, occupancy/parking language,
ordered-Bell/Stirling identities, and generic zeta conversion.  It found no
direct owner or internal two-axis collision and returned zero findings.
Round 2 is also a no-change source freeze; the bounded non-hit remains
novelty-neutral.

## Stable links

- <https://doi.org/10.1002/j.1538-7305.1950.tb00463.x>
- <https://doi.org/10.4086/cjtcs.2010.013>
- <https://arxiv.org/abs/0912.0583>
- <https://doi.org/10.1080/00029890.1994.11996984>
- <https://doi.org/10.1137/0114101>
- <https://doi.org/10.1016/j.jcta.2016.03.001>
- <https://arxiv.org/abs/2305.15554>
