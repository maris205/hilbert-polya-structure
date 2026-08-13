# Author response to Independent Manuscript Review — Round 1

**Manuscript:** *Rational Periodic Multiplier Moduli under Good Reduction: A
Hénon Certificate and Exact Audit*  
**Response date:** 2026-08-14  
**Round-1 verdict:** `PASS_WITH_MINORS`  
**Repair status:** all three minor comments implemented

The reviewed inputs remain immutable: `paper/paper_pre_review.pdf` has SHA-256
`450eae555f09faf7071efbd476f34c570b288166a067d81ddbeac9e6c225010f`,
and the Round-1 review has SHA-256
`93199422647307a9356dd294271a3aa25fdd06deaa612eb6eeb6f93dd7f848b8`.
The revised output is `paper/paper_round1_revised.pdf`, an 11-page PDF with
SHA-256
`f7368ecfa03929143311516303bb1c7a1a97e77869cb245f47e82e8e91a63156`.

## Point-by-point response

| Comment | Response and exact change | Status |
|---|---|---|
| M1: expose the two compressed algebraic implications | In Lemma 3.4, the proof now states that the two roots are integral over $\overline R$, invokes that $\overline R/R$ is integral, and uses transitivity to place both roots, including the determinant-one reciprocal $\lambda^{-1}$, in $\overline R$. In Lemma 3.5, it now states that every $W\notin T$ lies above a rational prime outside $S_{\mathbf Q}$, restricts outside $S$, and that integrality of both $\lambda$ and $\lambda^{-1}$ forces $v_W(\lambda)=0$. See `paper/manuscript.tex`, Lemmas 3.4--3.5. | Resolved |
| M2: reconcile Silverman and Kawaguchi metadata | `silverman_1994` now records *Math. Z.* 215(2), 237--250 in both `references.bib` and the citation-verification ledger. The Kawaguchi 2013 entry in `notes/NOVELTY_AUDIT.md` now records 1225--1252. The DOI identifiers remain unchanged and agree with the publisher records cited in the ledger. | Resolved |
| M3: remove byte `0x08` | The corrupted integrity-table token was replaced by literal Markdown math `$\bar\lambda$`; a repository-local text scan over this paper now finds no disallowed C0 control byte. | Resolved |

No theorem, experiment, cutoff, control, figure, route decision, source lock, or
official result JSON was changed. The experiment passport and figure package
remain byte-identical because their frozen inputs and outputs are unaffected;
their SHA-256 values remain, respectively,
`7ca3ed260ac67ff2a6c34e4f686124de3dd7887437263b28543c9b31fef43265`
and
`a91eaf58ffe7acfde07d1dcadf9288379732244d478aca9d2d17a87abdc51d1e`.

## Verification after repair

- `PYTHONPATH=code pytest -q`: 39/39 passed.
- Two consecutive executions of `paper/build.sh` produced the same PDF hash.
- The revised PDF has 11 letter-size pages; all fonts are embedded and subset.
- The final LaTeX log has zero errors, warnings, undefined references or
  citations, and zero overfull or underfull boxes.
- Citation-key closure remains 12/12 with no missing or unused entry.
- The official result manifest still closes at 41/41, while
  `experiments/source_lock.json` and `results/final_result_manifest.json`
  retain SHA-256 values
  `3ae1623304b2cc68403cfc20de545edce7cea6af6e2df9c1cd56d4ae8f38d269`
  and
  `e47c93ccc49cf37ffa5bab63bed758be9c1288500f459d539de806d7e4229863`.
- No external prime table, Riemann-zero data, or other forbidden target data
  was accessed.

## Author-side self-check boundary

The author-side check confirms only that M1--M3 were applied, the dependency
hashes were refreshed, and the revised package builds and validates cleanly.
It is **not** an independent Round-2 review and makes no submission-readiness
claim. Independent verification against the Round-1 comments remains the next
review gate.

