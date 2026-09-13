# Citation Verification

## Verification policy

The literature check was bounded, primary-source-first, and closed on
**2026-08-17**. Technical claims are tied to original articles, author-posted
preprints, or publisher records. Search results are used only to locate primary
texts. A negative search result is reported as such and never converted into a
priority claim.

Only Laurent's theorem is indispensable to the proof. Every other source gives
map provenance or a closest-scope comparison.

## The unique external proof input

### Michel Laurent, 1984

**Primary journal source**

- Michel Laurent, “Equations diophantiennes exponentielles,” *Inventiones
  mathematicae* 78 (1984), 299--327.
- DOI: `10.1007/BF01388597`.
- Publisher record:
  <https://link.springer.com/article/10.1007/BF01388597>.
- EuDML journal record/full-text identifier:
  <https://eudml.org/doc/143175>.

The Springer primary record verifies the author, title, journal, volume, pages,
June 1984 date, and DOI. The mathematical scope was checked against Laurent's
primary text and his contemporaneous author summary:

- Michel Laurent, “Equations diophantiennes exponentielles,” *Séminaire de
  Théorie des Nombres de Bordeaux* 13 (1983--1984), 1--8,
  <https://eudml.org/doc/182179> and
  <https://www.jstor.org/stable/44165476>.

The Bordeaux item is **not** the Inventiones article; it is a separate
same-author seminar account. The project must not reuse the old mistaken
EuDML identifier `182179` as the journal paper.

### Exact scope used

Laurent treats a commutative algebraic group over `C` without an additive
algebraic subgroup and a subgroup of finite rank, defined by containment up to
torsion over a finitely generated subgroup. Specializing to a torus gives the
statement needed here:

> For a closed subvariety `X` of a complex torus and the division group
> `Lambda^div` of a finitely generated subgroup, `X intersect Lambda^div` is a
> finite union of intersections with torus cosets contained in `X`.

The proof package uses only the immediate qualitative consequence that the
intersection is finite when `X` contains no positive-dimensional torus coset.
It does not use a quantitative unit-equation bound, an effective exceptional
set, or an algorithm.

### Arbitrary-field and torsion verification

The source theorem is complex. The project does not cite a stronger theorem
over an arbitrary large field. Instead, it proves the bridge:

1. an arbitrary finite-rank `Gamma` lies in the division hull of a finitely
   generated `Gamma_0`;
2. arbitrary torsion, including `mu_infinity`, is automatically in that
   division hull;
3. the field generated over `Q` by the finitely many map coefficients and
   generators of `Gamma_0` is finitely generated and embeds in `C`; and
4. every element of `Gamma` is algebraic over that field.

Thus the exact complex theorem suffices for arbitrary characteristic-zero
ground fields. This reduction is proved internally in `PROOF_PACKAGE.md`; no
second Diophantine theorem is hidden in the field extension.

## Shift-like map provenance

### Bedford--Pambuccian

- Eric Bedford and Victoria Pambuccian, “Dynamics of shift-like polynomial
  diffeomorphisms of C^N,” *Conformal Geometry and Dynamics* 2 (1998), 45--55.
- DOI: `10.1090/S1088-4173-98-00027-7`.
- Publisher DOI: <https://doi.org/10.1090/S1088-4173-98-00027-7>.

The primary paper introduces the higher-dimensional shift-like polynomial
diffeomorphism family and studies filtration and potential-theoretic dynamics.
It supports terminology and the standard type range `1<=nu<=k-1`. It does not
state finite-rank torus-window or torus-coset dimension results.

### Bera and Bera--Verma

- Sayani Bera, “Polynomial shift--like maps in C^k,” arXiv:1805.03142v3,
  <https://arxiv.org/abs/1805.03142>.
- Sayani Bera and Kaushal Verma, “Some aspects of shift-like automorphisms of
  C^k,” arXiv:1309.3392,
  <https://arxiv.org/abs/1309.3392>.

The arXiv primary records and abstracts were checked. Bera studies degeneration
as `a` tends to zero and Fatou components for polynomial shift-like maps;
Bera--Verma studies entire mappings, Fatou--Bieberbach domains, unstable
manifolds, and a Yoccoz-type inequality. These are complex-dynamical provenance
and boundary sources, not arithmetic torus-intersection theorems.

No priority statement is made from the fact that Bedford--Pambuccian or Bera
uses the same map class.

## Closest arithmetic/dynamical sources checked

| Primary source | Exact checked scope | Why it does not supply or collide with the proposed theorem |
|---|---|---|
| Bell--Ghioca, “Intersections of orbits of self-maps with subgroups in semiabelian varieties,” arXiv:2210.03152, <https://arxiv.org/abs/2210.03152> | For one fixed orbit and a finitely generated subgroup, the time set is arithmetic progressions plus a Banach-density-zero set; a regular-map clause gives a stronger conclusion. | Paper17 varies all initial torus states, uses arbitrary finite rank, and proves exact finite-window coset geometry. |
| Ji--Xie--Zhang, “Cyclotomic integral points for affine dynamics,” arXiv:2511.13443, <https://arxiv.org/abs/2511.13443> | Rigidity from Zariski-dense cyclotomic preperiodic points, with applications to Hénon-type periodic points. | Cyclotomic periodic non-density/rigidity is not finite-rank finite-window cardinality or the support resonance classification. |
| Mello--Yasufuku, “On higher dimensional integrality and multiplicative dependence in semigroup algebraic dynamics,” arXiv:2604.03745, <https://arxiv.org/abs/2604.03745> | Higher-dimensional semigroup-orbit multiplicative dependence linked to non-density of integral points and conditional Vojta input. | It fixes semigroup orbits and asks density/dependence questions, not all-initial-state survivor varieties or exact torus-coset dimensions. |
| Karimov--Kelmendi--Ouaknine--Worrell, “Multiple Reachability in Linear Dynamical Systems,” arXiv:2403.06515, <https://arxiv.org/abs/2403.06515> | Decidability/undecidability of multiple reachability for real linear systems and semialgebraic targets; a torus-subvariety method appears in a linear rotation case. | The system is linear/real and algorithmic; it neither treats sparse polynomial shift-like recurrences nor the constant-anchor phase. |
| Kaur, “Two remarks on transcendental shift-like maps on C^N,” arXiv:2604.27832, <https://arxiv.org/abs/2604.27832> | Transcendental shift-like complex dynamics and Julia-set questions. | No finite-rank arithmetic intersection or sparse recurrence classification. |

The search also inspected citation trails and current arXiv title/abstract
matches for “shift-like,” “finite-rank,” “torus coset,” “sparse recurrence,”
“multiplicative dependence,” and “Hénon cyclotomic” through the cutoff date.
No direct theorem-level collision was found.

## Paper16 local-source verification

The exact predecessor boundary was read from the following terminal local
sources under `papers/16-henon-support-size-torus-escape`:

| File | SHA-256 |
|---|---|
| `notes/RESEARCH_QUESTION.md` | `43b7f965dc04db33c1f00e45880466730d7ee2a25d84f117e91cace71b26a928` |
| `notes/PROOF_PACKAGE.md` | `b44c1f164c97fb5d383cbef941fdef88be4e702066e40efcfb18543be0c4bdf8` |
| `notes/NOVELTY_ASSESSMENT.md` | `83c9ab497211c7b5cd5d11b7061a292aba4fb258976a01ec8b9216b11226b96b` |
| `notes/CITATION_VERIFICATION.md` | `6ec31651060c148d3110856d8709206f60c36ea990b6c433fa9ab0e0944bab24` |
| `refine-logs/REVIEW_SUMMARY.md` | `20256b3f6915781c07dadb6beec26fa69529c5c7d0660b0171c14d460656c55a` |
| `paper/reviews/final_integrity_review.md` | `e355172b4533011d549453d02ee9939fb2dabc16fef035206ad4911fdf18eb76` |

The terminal review records a PASS. Paper16 owns the explicit planar
`c!=0,s>=2` `T_2` bound with `T_1` sharpness and the absorbed support-one
`T_4/T_3` theorem originating in Paper14. Paper14 is already fully absorbed by
Paper16. Paper17 cites this boundary but does not use Paper16 as an external
proof input, reproduce its quantitative proof, revive Paper14, or claim to
improve either result.

## Search-log summary

| Date | Query families | Sources opened | Result |
|---|---|---|---|
| 2026-08-17 | Laurent title/DOI, finite-rank torus division group | Springer primary record; EuDML journal and author-note records; JSTOR author note | Exact bibliographic identity and finite-rank/division-group scope fixed; no quantitative claim. |
| 2026-08-17 | Bedford Pambuccian type `nu` shift-like | DOI/publisher record and primary paper metadata | Map provenance only. |
| 2026-08-17 | Bera shift-like polynomial maps | arXiv:1805.03142 and arXiv:1309.3392 | Complex-dynamics scope only. |
| 2026-08-17 | Hénon cyclotomic, orbit subgroup, multiplicative dependence | arXiv:2210.03152, 2511.13443, 2604.03745 | Adjacent orbit/density questions, no collision. |
| 2026-08-17 | multiple reachability torus coset sparse recurrence | arXiv:2403.06515 and current title/abstract results | Linear-algorithmic problem, no collision. |
| 2026-08-17 | current shift-like 2026 | arXiv:2604.27832 and citation trails | Transcendental complex dynamics, no collision. |

## Claims citations cannot support

None of the verified sources supports any of the following, and the project
must not cite them as if they did:

- an effective bound for the proposed `T_k`, `T_2`, or `T_3` sets;
- the Part A relation-independence theorem;
- the Part B unique resonance locus;
- a positive-characteristic or rational-map extension;
- classification of all equality cosets;
- a claim that resonance meets every finite-rank group infinitely; or
- a global first/priority statement.

## Citation-stage conclusion

The one indispensable theorem is verified at the needed qualitative scope;
the arbitrary-field, division-group, and infinite-torsion bridge is internal.
All other references are correctly limited to provenance or closest-work
comparison.

**CITATION STATUS: VERIFIED FOR AUTHOR SOURCE DESIGN / REFRESH REQUIRED AT ANY
FUTURE SOURCE-LOCK DATE.**
