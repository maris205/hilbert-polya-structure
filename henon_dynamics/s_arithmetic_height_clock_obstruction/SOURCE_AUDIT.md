# Source and novelty audit

**Source lock:** 2026-08-07

**Scope:** compact quaternionic real/$p$-adic dynamics, periodic flats,
higher-rank zetas, Hecke spectra, and the local Hénon baseline.

## Local project boundary

The local HCS-C01--C15 project records were checked before HCS-C16 was frozen.
Within that local corpus, no earlier package used this particular quaternion
algebra, order, split prime, and pair of $S$-unit generators. That is a local
provenance statement, not a claim of priority in the mathematical literature.

Earlier project metadata identifies Liang Wang, *An Area-Preserving Hénon-Map
Model for the Riemann Zeros* (2026), at
`henon_dynamics/docs/prior_work/papers/5-An Area-Preserving Henon-Map Model.pdf`.
The PDF is present in this checkout and was read as the foundational local
baseline. It gives an area-preserving Hénon model and numerical spectral
motivation, while its continuum regularization and effective scale remain
model choices and it does not derive the global determinant/operator bridge
required here. HCS-C16 therefore changes the phase space rather than treating
that baseline as established Hilbert--Pólya structure.

## Directly relevant prior art

1. **Quaternion arithmetic.** John Voight, *Quaternion Algebras*, Graduate
   Texts in Mathematics 288, Springer (2021):
   <https://doi.org/10.1007/978-3-030-56694-4>. This supplies the standard
   local classification, order, embedding, and arithmetic-group background.

2. **Real/$p$-adic homogeneous dynamics.** Manfred Einsiedler and Dmitry
   Kleinbock, *Measure rigidity and $p$-adic Littlewood-type problems*,
   *Compositio Mathematica* 143 (2007), 689--702:
   <https://arxiv.org/abs/math/0506514>. Dmitry Kleinbock and George Tomanov,
   *Flows on $S$-arithmetic homogeneous spaces and applications to metric
   Diophantine approximation*, *Commentarii Mathematici Helvetici* 82 (2007),
   519--581: <https://doi.org/10.4171/CMH/102>.

3. **Higher-rank prime geodesics and periodic flats.** Anton Deitmar,
   *A prime geodesic theorem for higher rank spaces*, *Geometric and
   Functional Analysis* 14 (2004), 1238--1266:
   <https://arxiv.org/abs/math/0208206>. Nguyen-Thi Dang and Jialun Li,
   *Equidistribution and counting of periodic tori in the space of Weyl
   chambers*, *Commentarii Mathematici Helvetici* 101 (2026), 47--113:
   <https://doi.org/10.4171/CMH/594> (preprint:
   <https://arxiv.org/abs/2305.17070>; related predecessor:
   <https://arxiv.org/abs/2202.08323>). These works directly establish that
   regular higher-rank dynamics is organized by periodic maximal flat tori and
   that counting requires the corresponding higher-rank framework.

4. **Lefschetz and higher-rank $p$-adic zetas.** Anton Deitmar,
   <https://arxiv.org/abs/math/0508642> and
   <https://arxiv.org/abs/math/0505405>; Anton Deitmar and Ming-Hsuan Kang,
   *Geometric zeta functions for higher rank $p$-adic groups*:
   <https://arxiv.org/abs/1303.6848>. These are antecedents for torus actions,
   Lefschetz weights, and multivariable building zetas.

5. **Hecke correspondence trace theory.** Shigeki Akiyama and Yoshio
   Tanigawa, *The Selberg trace formula for modular correspondences*:
   <https://doi.org/10.1017/S0027763000001823>. Fixed Hecke double-coset
   coefficients and their trace formulas are established objects.

6. **Joint Laplace--Hecke asymptotics.** Pablo Ramacher and Satoshi
   Wakatsuki, *Asymptotics for Hecke eigenvalues of automorphic forms on
   compact arithmetic quotients*, *Advances in Mathematics* 404 (2022),
   108372: <https://arxiv.org/abs/2002.03263>. This is directly relevant to the
   compact spectral baseline.

7. **Periodic arithmetic torus packets.** Ilya Khayutin, *Arithmetic of
   double torus quotients and the distribution of periodic torus orbits*:
   <https://doi.org/10.1215/00127094-2019-0016>.

8. **Current Hecke--Ruelle boundary.** Yanli Song's June 2026 talk abstract,
   *Hecke Operator and Ruelle Dynamical Zeta Function*:
   <https://indico.imapp.ru.nl/event/342/page/103-abstracts>, announces a
   related program. At the source-lock date, this record was treated only as
   an announced overlap risk, not as a verified published theorem. Related
   preprints include <https://arxiv.org/abs/2502.16100> and
   <https://arxiv.org/abs/2303.00312>.

## Modest novelty conclusion

This was a targeted, search-bounded audit, not a systematic or exhaustive
literature review. The project therefore makes no priority claim for periodic
flats, higher-rank zetas, Hecke--Ruelle theory, Weil-height constructions in
general, or quaternionic $S$-arithmetic dynamics.

The defensible contribution is narrower: an explicit arithmetic example with

- a specified quaternion algebra, order, split prime, and two generators;
- an explicit rank-two local clock and primitive/repetition calculation;
- an arithmetic near-wall sequence showing failure of one real-only, one-flat
  class-product specialization;
- a Weil-height identity and proper scalarization on that centralizer;
- a geometry-of-numbers asymptotic for primitive directions on that one flat;
- a scoped bounded-Hecke Weyl assessment of the full compact-surface baseline.

Even this combination should be described as a worked example and scoped
Route-A assessment, not as a new general theory or a comprehensive no-go
theorem. The Dang--Li result makes the periodic-flat prior-art boundary
especially explicit.
