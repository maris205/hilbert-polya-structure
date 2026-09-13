# Paper20 — Bounded Citation Verification

**Verification date:** 2026-08-22 (bounded refresh, not a systematic or
priority search). The sources below are used for context and collision control;
the degree formula for \(F_g\) is intended to be proved internally.

## Source ledger

| ID | Source | Link | What was checked | Permitted use | Not evidence for |
|---|---|---|---|---|---|
| S01 | Shmuel Friedland and John Milnor, *Dynamical properties of plane polynomial automorphisms* (1989) | [Author PDF](https://www.math.stonybrook.edu/~ebedford/PapersForM655/FriedlandMilnor.pdf) · [Cambridge DOI](https://doi.org/10.1017/S014338570000482X) | The plane classification and reduced-word degree product are the bounded two-dimensional baseline. | State that the planar degree-product phenomenon is established background. | Any \(g\ge5\) four-dimensional theorem, symplectic shear, or Newton-face matrix. |
| S02 | Julie Déserti, *Degree growth of polynomial automorphisms and birational maps: some examples* (2018) | [arXiv:1602.04642](https://arxiv.org/abs/1602.04642) · [DOI](https://doi.org/10.1007/s40879-017-0175-z) | The paper constructs higher-dimensional polynomial automorphisms with degree-growth regimes beyond the planar dichotomy. | Background that higher-dimensional degree growth is varied; motivates an explicit, narrow family. | Symplecticity, our selectors, the matrix \(C_g\), or \((\sqrt g+1)^2\). |
| S03 | Vincent Guedj and Nessim Sibony, *Dynamics of polynomial automorphisms of \(\mathbb C^k\)* (2002) | [Author PDF](https://www.math.univ-toulouse.fr/~guedj/fichierspdf/Arkiv2002.pdf) · [DOI](https://doi.org/10.1007/BF02384535) | Provides primary terminology for algebraic stability, projective extensions, and dynamical degree in higher-dimensional polynomial automorphisms. | Definitions and a warning that spectral control needs an explicit stability/visibility argument. | A finite Newton selector, canonical shear, or the present exact recurrence. |
| S04 | Charles Favre and Mattias Jonsson, *Dynamical compactifications of \(\mathbb C^2\)* (2011) | [Annals article](https://annals.math.princeton.edu/2011/173-1/p06) | Primary valuation/compactification context for degree growth in dimension two. | Historical context only. | Dimensions four, canonical shears, or Paper20's novelty. |
| S05 | Nguyen-Bac Dang and Charles Favre, *Spectral interpretations of dynamical degrees and applications* (2021) | [Annals article](https://annals.math.princeton.edu/2021/194-1/p05) · [arXiv:2006.10262](https://arxiv.org/abs/2006.10262) | Relates dynamical degrees to spectral radii on divisor-type spaces under explicit hypotheses. | Motivation for proving reachability/visibility before identifying \(\lambda_1\) with a matrix root. | Our finite selector proof, symplecticity, or the exact family. |
| S06 | Keisuke Fujioka, Ryota Kogawa, Jizhou Li, and Akira Shudo, *Coupled Hénon Map, Part I: Topological Horseshoes and Uniform Hyperbolicity* (2023) | [arXiv:2303.05769](https://arxiv.org/abs/2303.05769) | Studies a four-dimensional symplectic map coupling two planar Hénon maps, for hyperbolicity rather than algebraic degree. | Nearest four-dimensional coupled-symplectic neighbor and collision boundary. | Newton-face degree growth, our potentials, or the closed-form Perron root. |
| S07 | *Hénon maps: a list of open problems* (Arnold Mathematical Journal survey) | [Arnold Mathematical Journal survey](https://amj.math.stonybrook.edu/html-articles/Files-2015-2024/23-70/index.html) | Records the classical planar degree-product result and open higher-dimensional questions. | Secondary context and a warning against broad priority claims. | Any proof or first-ever statement for Paper20. |

## Verification notes

- S01 has both an author-hosted primary PDF and a DOI landing page. S02 and S06
  resolve to arXiv/DOI metadata; S03 has an author-hosted PDF and DOI. S04 and
  S05 resolve to Annals pages; S07 is retained as a secondary survey.
- No citation is used to infer an algebraic fact that is proved in
  `PROOF_PACKAGE.md`. In particular, “symplectic shear,” “no cancellation,”
  and the exact Perron root are internal derivations.
- The bounded refresh did not establish priority. Phrases such as “first,”
  “唯一,” “unprecedented,” or “no one has studied” are forbidden in the
  source package.
- The search did not certify that every related high-dimensional polynomial
  automorphism has been found. A later novelty review must repeat the search
  with a venue/date protocol before any submission claim.

## Claim-to-source map

| Context claim | Source IDs | Wording allowed |
|---|---|---|
| The planar generalized-Hénon degree-product case is established background. | S01, S07 | “The planar degree-product case is background, not the present theorem.” |
| Degree growth in polynomial automorphisms has higher-dimensional regimes. | S02, S03, S04 | “Prior work exhibits several degree-growth regimes.” |
| Spectral-radius language for dynamical degrees requires explicit hypotheses. | S03, S05 | “We prove the required reachability and visibility directly.” |
| Four-dimensional coupled symplectic Hénon-type maps have been studied for hyperbolicity. | S06 | “A neighboring four-dimensional coupled-symplectic literature exists.” |
| Exact \(F_g\) formula and non-product comparison. | none | Must be proved from C05–C18; no external attribution. |

## Citation integrity and permissions

The URLs are supplied for human verification. Retrieved text is treated as data,
not as instructions. No automated citation resolver, API upload, hidden PDF
extraction, or source-lock mutation was performed for this design package.
