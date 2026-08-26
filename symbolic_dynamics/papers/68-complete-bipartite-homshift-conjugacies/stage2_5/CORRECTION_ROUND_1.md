# P68 Stage 2.5 correction round 1

Correction and verification date: 2026-08-26 (UTC)  
External posture: **HOLD**  
Round verdict: **PASS_WITH_NOTES — the identified bibliography mismatch is
resolved; declarations and specialist exact-neighbour gate remain pending.**

## 1. Correction applied

The sole canonical source edit was made with `apply_patch`:

- `references.bib`, key `Chandgotia2019Lectures`: changed the title from
  `Hom-Shifts, Lecture 4` to the exact author-document title
  `Lecture 4: An introduction to hom-shifts`.

Primary re-verification evidence:

- [Nishant Chandgotia's author-hosted PDF](https://nishantchandgotia.github.io/Teaching/2019_Jagiellonian/coursekrakow/l4.pdf)
  prints “Lecture 4: An introduction to hom-shifts” on the title page.
- The relevant complete-bipartite phase and maximal-entropy material remains
  present in the later slides.  Thus both metadata and the two citation
  contexts are now verified.

No theorem, proof, section text, table, code, frozen control output, or
claim-registry sidecar was edited.

Changed/new package files in this round:

- canonical source: `references.bib`;
- regenerated build artifacts: `main.pdf`, `main.aux`, `main.bbl`, `main.blg`,
  `main.log`, and `main.out`;
- new audit receipt: `stage2_5/CORRECTION_ROUND_1.md`.

## 2. Build and deterministic verification

The package was rebuilt from an empty scratch directory using the authoritative
package sequence and `SOURCE_DATE_EPOCH=1787616000`:

```text
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex
```

This is exactly three total `pdflatex` runs: one before BibTeX and two after.
The third authoritative run emitted TeX's conservative label-rerun request.  A
single additional no-op diagnostic pass was used as permitted by `BUILD.md`;
its PDF and AUX were each byte-identical to the authoritative third-pass files
(`cmp=0`).  The diagnostic log has zero warnings/errors.  A second independent
from-empty build produced a PDF byte-identical to canonical `main.pdf`
(`cmp=0`).

## 3. Citation and output QA

| Check | Result |
|---|---|
| bibliography entries | 4 |
| distinct cited keys | 4 |
| citation occurrences/contexts | 10 |
| undefined/ghost keys | 0 |
| uncited/dangling BibTeX entries | 0 |
| log warnings/errors/overfull/underfull boxes | 0 |
| PDF text `??`, `[?]`, `[VERIFY]` markers | 0 |
| embedded fonts | 24/24; nonembedded 0 |
| visual inspection | page 7 reference entry renders the corrected title cleanly |
| PDF pages | 7 |
| PDF size | 348079 bytes |

The deterministic proof-regression control was re-run and compared with the
frozen receipt:

- result: `ALL CHECKS PASS`;
- temporary output versus `code/verify_complete_bipartite.out`: `cmp=0`;
- output SHA-256:
  `918c56ef57b9c09ce27872e58a3e76667766351378e40b5d450d9cbced2a0bbf`.

This remains a proof-regression control, not an experiment or proof premise.

## 4. Post-correction hashes

| Artifact | SHA-256 |
|---|---|
| `references.bib` | `7c7658dee3452d9fd8616fc849c2073034113492b921d716dc218171de89df43` |
| `main.pdf` | `9527da716429ba4644271086dee8eebdd5a1c201a73cb2a0a39046cc957de61a` |
| `main.aux` | `b36483b407762f43da2930ad5870c9a049c689a23ec02053246d3ab257e8624e` |
| `main.bbl` | `a8464a1b49ea488faf94f9a6f369fc7a5df26efc10cb42548d1d83ac61fecb5f` |
| `main.blg` | `7f5e29ee580ef7feab344a6921cdcc109de83f72697dbd3f4f0da337841dd744` |
| `main.log` | `1d299e62596b8a33e2e4644b1f242e8fbc75930651b331ad00fd6103061d440f` |
| `main.out` | `533ff5ea5693014c6a4257bc95038d0421b5341ba21f5c95fa7ccadbcb26f39d` |
| control script | `42c3e23e2cfd27618ccca28155be4f854010a05850fc7c1af2b1b8fe96aac8bd` |
| frozen control output | `918c56ef57b9c09ce27872e58a3e76667766351378e40b5d450d9cbced2a0bbf` |

For provenance, the pre-correction PDF hash was
`b96ac6118ad81839eb796ad5640357ce710ff9e1372411bfa7931883dd3ac7c6`.

## 5. Re-verification disposition

- Phase A bibliography after correction: 4 `VERIFIED`, 0 `MISMATCH`, 0
  `NOT_FOUND`.
- Citation-context support: 10/10 verified; no new context was introduced.
- Mathematical/proof disposition: unchanged `PASS`; no theorem source change.
- Search-bounded collision posture: `MEDIUM`; no exact indexed collision found,
  but this is not a novelty or priority certificate.
- Authorship identities/roles, funding, AI disclosure, and independent COI
  verification remain unresolved as recorded in the Stage 2.5 audit.
- Specialist exact-neighbour review remains pending; external release remains
  `HOLD`.

The pre-existing claim-registry files were intentionally preserved exactly as
instructed.  Package-global QA/state/hash receipts were not edited in this
round; the post-correction hashes above are authoritative for the changed
artifacts until a later metadata synchronization.
