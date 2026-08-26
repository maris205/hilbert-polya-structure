# P71 Stage 2.5 correction round 1

Correction and verification date: 2026-08-26 (UTC)  
External posture: **HOLD**  
Round verdict: **PASS_WITH_NOTES — the bibliography/source-boundary findings
are corrected; HIGH pressure-collision risk and the specialist gate remain.**

## 1. Corrections applied

All canonical text-source edits were made with `apply_patch`.

### 1.1 Bibliography

- `MehdipourSalarinoghabiGibrim2026`: added AIP article number
  `pages = {015201}`.
- Added `LameiMehdipourVargas2025`, arXiv:2510.12980, *S-Expansiveness and
  Zip Shift Maps in Symbolic Dynamics*.
- Added `MehdipourUFVProject2024`, the official UFV researcher-profile entry
  for the 2024–present project *Formalismo Termodinâmico para Mapas Zip Shift*.

Primary re-verification evidence:

- [AIP publisher page](https://pubs.aip.org/aip/adv/article/16/1/015201/3376058/Zip-cellular-automata)
  identifies article 015201.
- [arXiv:2510.12980](https://arxiv.org/abs/2510.12980) verifies the title,
  authors S. Lamei, P. Mehdipour, W. Vargas, year, identifier, class, abstract,
  and the S-expansiveness/shadowing/factor scope.
- The [official UFV profile](https://nit.ufv.br/pesquisador/pouya-mehdipour/)
  lists the named project as 2024–present and states its objective of studying
  and formulating thermodynamic formalism for zip shifts, principally to show
  that the maps represent systems with phase transitions.

### 1.2 Current-work boundary

`sections/7_scope.tex` now:

1. expressly assigns the S-expansiveness and shadowing results for the full zip
   shifts considered in the cited preprint, and its factor theorem under the
   authors' stated hypotheses, to Lamei–Mehdipour–Vargas;
2. states that P71 does not claim those results;
3. identifies and cites the official UFV 2024–present thermodynamic-formalism
   project and its phase-transition objective;
4. states that the profile contains a project objective, not theorem text, so
   no theorem-level comparison is possible from that page;
5. retains search-bounded language, records `HIGH` collision risk for the
   pressure portion, and preserves the specialist exact-neighbour gate and
   external `HOLD`.

No theorem, proof, table, code, or frozen control output was changed.

Changed/new package files in this round:

- canonical sources: `references.bib` and `sections/7_scope.tex`;
- regenerated build artifacts: `main.pdf`, `main.aux`, `main.bbl`, `main.blg`,
  `main.log`, and `main.out`;
- new audit receipt: `stage2_5/CORRECTION_ROUND_1.md`.

## 2. Build and deterministic verification

A from-empty scratch build used `SOURCE_DATE_EPOCH=1787616000` and the
authoritative package sequence:

```text
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex
```

This is exactly three total `pdflatex` runs.  The final log is clean.  A second
independent from-empty build produced a PDF byte-identical to canonical
`main.pdf` (`cmp=0`).

## 3. Citation and output QA

| Check | Result |
|---|---|
| bibliography entries | 9 |
| distinct cited keys | 9 |
| citation occurrences/contexts | 19 |
| undefined/ghost keys | 0 |
| uncited/dangling BibTeX entries | 0 |
| log warnings/errors/overfull/underfull boxes | 0 |
| PDF text `??`, `[?]`, `[VERIFY]` markers | 0 |
| embedded fonts | 28/28; nonembedded 0 |
| visual inspection | pages 8–9 render the expanded boundary and all nine references cleanly |
| PDF pages | 9 |
| PDF size | 409426 bytes |

The two newly introduced contexts were rechecked against the cited primary
pages, so post-correction context support is 19/19.

The deterministic proof-regression control was re-run:

- result: `ALL CHECKS PASS`;
- temporary output versus `code/verify_degree_pressure.out`: `cmp=0`;
- output SHA-256:
  `4ade498585b0750acea4b487dec11b7c19b2e322f8a5ef1d4262d6c4f39f2aba`.

This is proof-regression evidence, not an experiment or proof premise.

## 4. Post-correction hashes

| Artifact | SHA-256 |
|---|---|
| `references.bib` | `66e274980a6d32bb25c9ff6c3a82b732856f105df9a2d2e3debe11b704a42e90` |
| `sections/7_scope.tex` | `c7507fe96bb83c8260bf6c012d9614495da510ed05334dc36957e03ab45098b1` |
| `main.pdf` | `971b33083dc14ceb99831f94786167c1186bf9b8365557472fb2a9f493174a9e` |
| `main.aux` | `b968261e179dc26d4db6fd42b904bdf619d8b87050b745ab4f41aac98d8b704a` |
| `main.bbl` | `104e70ad4090033c75998c9e91a9d5b7f35dbbeb89a5741377695dd1d30df68a` |
| `main.blg` | `2ace8418f24587fded8b970036fcaa763b2c14c06c8c7e3d8b0713b4e0d17607` |
| `main.log` | `2aee2e0cd391ba14c31fdc29f9b66e250df8a59966e65a8db60a897d4fca3960` |
| `main.out` | `5462c6be1e27d7e4fa08885d00a67d705129e7f412125eda5ed01fa915571ea2` |
| control script | `6de6496c78ca610d955f7b6a4aa08d31f162b0c7ad3bfcbaf80bcb787119aab2` |
| frozen control output | `4ade498585b0750acea4b487dec11b7c19b2e322f8a5ef1d4262d6c4f39f2aba` |

For provenance, the pre-correction PDF hash was
`ff85975c69b7848ff8675edde2e753ed9deb6cd377f37aeeb60669d403026bcf`.

## 5. Re-verification disposition

- Phase A bibliography after correction: 9 `VERIFIED`, 0 `MISMATCH`, 0
  `NOT_FOUND`.
- Citation-context support after the two added citations: 19/19 verified.
- The owner subtraction is now explicit for S-expansiveness, shadowing, the
  factor theorem, and the public UFV project objective.
- The project page exposes no theorem statement.  The audit therefore neither
  claims collision nor treats the absence of theorem text as evidence of no
  collision.
- Mathematical/proof disposition: unchanged `PASS`; no theorem source change.
- Search-bounded collision posture: `HIGH` for the pressure portion.
- Authorship identities/roles, funding, AI disclosure, and independent COI
  verification remain unresolved.
- Specialist exact-neighbour comparison remains mandatory; external release
  remains `HOLD`.

The pre-existing claim-registry files were intentionally left untouched.  In
particular, because `sections/7_scope.tex` changed, those sidecars are a
pre-correction snapshot and must not be described as hash-synchronized to this
post-correction manuscript.  Package-global QA/state/hash receipts were not
edited in this round; the hashes above are authoritative for changed artifacts
until a later metadata synchronization.
