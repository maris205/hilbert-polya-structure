# P69 Stage 2.5 correction round 1

Date: 2026-08-26 (UTC)  
Authority: explicit Stage-2.5 correction request  
Posture: author-side correction and deterministic QA, not independent review  
External release: **HOLD**

## 1. Correction disposition

Correction round 1 is **PASS** for the authorized scope.  It resolves the Klug
pinpoint and the four specified related-work / owner-subtraction omissions without
changing the main theorem, any formula, any proof step, or the finite-control code.
The prior audit's search-bounded priority posture is preserved: no global priority,
specialist clearance, or release authorization is asserted.

## 2. Canonical changes

| File and current locator | Change | Result |
|---|---|---|
| `sections/2_background.tex:55-59` | corrected Klug “Theorem 3” to “Theorem 3.1”; added Snyder as a separate lattice-TQFT derivation of both surface formulas | RESOLVED |
| `sections/1_introduction.tex:33-43` | added Ward's partial and Roettger's completed periodic-data classification for finite-abelian-parameter Ledrappier-type algebraic `Z^2` Markov shifts | RESOLVED |
| `sections/1_introduction.tex:45-51` | stated that Snyder already owns the lattice-TQFT route and that the classical formulas are not P69 contributions | RESOLVED |
| `sections/5_moment_recovery.tex:83-89` | identified `sum_chi chi(1)^(-t)` as the standard character-degree zeta expression and cited Liebeck–Shalev | RESOLVED |
| `sections/7_scope_controls.tex:13-33` | consolidated owner subtraction for Klug/Snyder, character-degree zeta values, elementary Vandermonde inversion, and Ward/Roettger; retained bounded-search/no-certificate wording | RESOLVED |
| `references.bib:42-85` | added four fully specified, cited records; made Snyder's arXiv identifier and direct URL visible under `plainnat` | RESOLVED |

The Ward/Roettger distinction is explicit rather than implicit.  Their family is an
abelian algebraic `Z^2` Ledrappier-type group shift and their periodic data recover the
finite abelian parameter up to isomorphism.  P69 instead uses a nonorientable surface
group, nonabelian edge-label flat connections, two selected surface-cover families,
and recovery of the order plus the character-degree/Frobenius–Schur-indicator
multiset.  Ward and Roettger are therefore prior owners of the periodic-data
classification principle in their family and conceptual nearest neighbors, not an
exact collision with the P69 theorem.

## 3. Added-source re-verification

Each new record was checked by exact title/author/DOI or arXiv search against a DOI
resolver, publisher record, arXiv, or an author/institutional page.  Direct URLs are
listed below.

### `Snyder2007`

- Noah Snyder, *Mednykh's Formula via Lattice Topological Quantum Field Theories*.
- arXiv record: <https://arxiv.org/abs/math/0703073>
- arXiv/DataCite DOI: <https://doi.org/10.48550/arXiv.math/0703073>
- Verified fields: author, title, 2007 first submission, identifier
  `math/0703073`, primary class `math.QA`.
- Source-content check: the abstract explicitly describes orientable Mednykh and
  nonorientable Frobenius–Schur formulas and a lattice-TQFT/topological-combinatorial
  proof of both.
- Verdict: **VERIFIED**.

### `LiebeckShalev2005`

- Martin W. Liebeck and Aner Shalev, *Character Degrees and Random Walks in Finite
  Groups of Lie Type*.
- DOI: <https://doi.org/10.1112/S0024611504014935>
- Publisher record: <https://www.cambridge.org/core/journals/proceedings-of-the-london-mathematical-society/article/abs/character-degrees-and-random-walks-in-finite-groups-of-lie-type/971082D1033B8B0372ECA3FDEE82F5ED>
- Author-hosted text: <https://www.ma.imperial.ac.uk/~mwl/chardeg3.pdf>
- Verified fields: authors, title, *Proceedings of the London Mathematical Society*,
  volume 90, issue 1, pages 61–86, 2005, DOI.
- Source-content check: the abstract/text defines the finite-group character-degree
  zeta expression `zeta^H(t)=sum_{chi in Irr(H)} chi(1)^(-t)`.
- Verdict: **VERIFIED**.

### `Ward1998`

- Thomas Ward, *A Family of Markov Shifts (Almost) Classified by Periodic Points*.
- DOI: <https://doi.org/10.1006/jnth.1998.2242>
- Publisher page: <https://www.sciencedirect.com/science/article/pii/S0022314X98922429>
- Institutional record: <https://research-portal.uea.ac.uk/en/publications/a-family-of-markov-shifts-almost-classified-by-periodic-points/>
- Verified fields: author, title, *Journal of Number Theory*, volume 71, issue 1,
  pages 1–11, 1998, DOI.
- Source-content check: the abstract treats a two-dimensional topological Markov shift
  parameterized by a finite group and proves recovery up to isomorphism for finite
  abelian parameters subject to the stated arithmetic exceptions.
- Verdict: **VERIFIED**.

### `Roettger2005`

- C. G. J. Roettger, *Periodic Points Classify a Family of Markov Shifts*.
- DOI: <https://doi.org/10.1016/j.jnt.2004.11.012>
- Author publication page: <https://faculty.sites.iastate.edu/roettger/publications>
- Verified fields: author, title, *Journal of Number Theory*, volume 113, issue 1,
  pages 69–83, 2005, DOI.
- Source-content check: the abstract identifies the Ledrappier-type algebraic `Z^2`
  shift over a finite abelian group and states that its periodic-point data determine
  the group up to isomorphism, extending Ward.
- Verdict: **VERIFIED**.

This verification confirms bibliographic existence and the specific citation claims.
It is not a retraction certificate, specialist reading attestation, or global novelty
search.

## 4. Citation reconciliation

| Metric | Pre-correction | Post-correction |
|---|---:|---:|
| bibliography entries | 3 | 7 |
| citation commands/contexts | 5 | 12 |
| citation-key mentions | 5 | 14 |
| unique citation keys | 3 | 7 |
| ghost citations | 0 | 0 |
| dangling bibliography entries | 0 | 0 |
| undefined compiled citations | 0 | 0 |
| undefined compiled cross-references | 0 | 0 |

All four new entries occur in the manuscript.  Snyder has three contexts,
Liebeck–Shalev two, and Ward/Roettger two paired contexts each.  The visible PDF
bibliography includes Snyder's arXiv identifier and direct URL; the three journal DOI
records print their DOI values.

## 5. Build and control receipt

The package's authoritative deterministic sequence was rerun with
`SOURCE_DATE_EPOCH=1787616000`:

```bash
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

Build result:

| Item | Result |
|---|---|
| `main.pdf` | 11 A4 pages, 377,379 bytes |
| PDF SHA-256 | `93462a17e92207d9dfbccc55d6ac543391c55a8950d5057a50e9a3b9996c2766` |
| deterministic one-pass replay | same PDF SHA-256 before and after |
| LaTeX/BibTeX fatal errors | 0 |
| undefined citations/references | 0 |
| overfull/underfull boxes in final `main.log` | 0 |
| literal `[?]` or `??` in extracted PDF text | 0 |
| fonts not embedded/subset | 0 |
| affected-page visual inspection | pages 1, 2, 3, 7, 9, 10, 11; no clipping or collision found |

Exact proof-regression control:

```bash
python3 code/verify_surface_flat_sft.py
diff -u code/verify_surface_flat_sft.out qa/control_replay.txt
```

The diff is empty, the terminal line is `ALL CHECKS PASS`, and the replay/frozen
output SHA-256 is
`c8a56e4e9f692fa4bb97a535b2a683f2d220489f4e94d1dd99d5d01c87ed482d`.
These are proof-regression controls, not experiments and not a proof of the general
theorem.

## 6. Source fingerprints

| Canonical file | Pre-correction SHA-256 | Post-correction SHA-256 |
|---|---|---|
| `references.bib` | `242f9c9dc4c565b82509426d2ce8f22d9dc9af514972f0850aa8ddbacfc06f22` | `9eab29c4ae62a26087be3a4e6ec51e519656c28d0fc2fc0d13b3b0ec72779a03` |
| `sections/1_introduction.tex` | `3da03f879fa0633c3073338d66bc3e9da0a1a031d018f071ecb77a423cd7f19b` | `62b2fe7c149c753536952f2482c2e387cc43c5f0f5ba1c4c84a0556286e377d8` |
| `sections/2_background.tex` | `1f6d305aa02a689e3859c85c8d31e1fd49f96e4ce9f951cf094e3d3f76b63317` | `ae97df53f892a5a7bd97b3cb623e1ba7744a4d290903827b239f56981bff40f1` |
| `sections/5_moment_recovery.tex` | `57a03e6e89e3c1b630f2361051eb9d794098a4a8cc1e11b1eca4d08f80a28e97` | `9d0b3a10bbe8d40ba69831a03c8200d52731ac74cb8c9a2c0997f8627941a84b` |
| `sections/7_scope_controls.tex` | `f1ee3f875b6f61e36685dd4da74187e740bc3f22d84020f839703a9bf2c1a6f2` | `03e5a8fba9d39e4c9cac8b605f30dcf74adef51710c786ba27bdb036f86ad2a5` |
| `main.pdf` | `09216444bcc5abd911b88d3ac28416ca5a547efe236b0a22b5fc39781a676b08` | `93462a17e92207d9dfbccc55d6ac543391c55a8950d5057a50e9a3b9996c2766` |

No other canonical manuscript section was edited.

## 7. Claim-registry sidecar preservation

The root-created registry/probe sidecars were deliberately not edited or deleted.
Their post-correction hashes remain the pre-correction hashes:

| Sidecar | SHA-256 |
|---|---|
| `stage2_5/claim_registry.json` | `8a2371d2a814dab24b659b4a5a343e66d43274a33996b0bbdb7fea6042b63629` |
| `stage2_5/claim_registry_candidate_probe.json` | `8e5a38b7fba98eb263bb5ac7e786981218da6c767689ba3faff4c1fcae6837a8` |
| `stage2_5/claim_registry_coverage.json` | `86f3a918f875c45e67ef5edae4545ccfd65e223bda6827e1448efcc48969e288` |
| `stage2_5/claim_registry_probe.json` | `fe207ac208f95e73154c5727e69a6b8d7a4ec22f78aef648a1042f19174f30bb` |
| `stage2_5/draft_for_claim_registry.md` | `cf7f3e04ac14152a0144a9ffed61ee9f9e926e4e8c1a867093711034d67f675c` |

Because the canonical manuscript now contains additional related-work prose and
citations, those preserved sidecars describe the pre-correction extraction surface.
Any downstream use that requires current exact-span coverage must refresh them in a
separate authorized registry step; this correction round does not silently rewrite
root-owned state.

## 8. Final round-1 state

- Authorized correction scope: **PASS**.
- Core mathematical content: unchanged.
- Added-source existence and context fidelity: **4/4 VERIFIED**.
- Citation reconciliation: **PASS, zero ghost/dangling/undefined records**.
- Build, fonts, text, visual, and control QA: **PASS**.
- Search-bounded priority wording: preserved.
- Root claim-registry sidecars: preserved byte-for-byte; refresh pending if current
  exact-span coverage is required.
- Global package state: not updated in this round.  In particular, `BUILD.md`,
  `FINAL_QA.md`, `PAPER_IMPROVEMENT_STATE.json`, and the package-wide
  `SHA256SUMS` remain the prior Round-2 baseline and must not be read as receipts for
  this corrected `main.pdf`; historical named PDF snapshots are likewise unchanged.
- External release: **HOLD**.
