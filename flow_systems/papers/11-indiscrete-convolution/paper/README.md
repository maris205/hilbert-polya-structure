# Paper 11 manuscript package

This folder contains the submission-draft manuscript for **Continuous
Convolution Collapse on Indiscrete Arithmetic Orbit Groupoids** by Liang Wang.
The main text is English and the English and Simplified Chinese abstracts were
composed independently against the same frozen fact ledger. This package is a
reviewable manuscript, not a declaration of standalone public release.

## Package contents

- `manuscript.tex`: manuscript source, including theorem statements, the
  convention/applicability table, the exact seven Route tuples, declarations,
  and prose equivalents for both figures.
- `references.bib`: manifestation-specific bibliography. Paper 9 is described
  honestly as a companion manuscript; its immutable public identity remains
  `AUTHOR TO CONFIRM` before standalone release.
- `figures/convention_split.tex`: native TikZ convention split.
- `figures/proxy_action_blind.tex`: native TikZ proxy and action-blindness map.
- `paper.pdf`: compiled A4 review PDF (the sole retained build artifact).

## Reproducible build

From this directory, run:

```sh
xelatex -interaction=nonstopmode -halt-on-error manuscript.tex
bibtex manuscript
xelatex -interaction=nonstopmode -halt-on-error manuscript.tex
xelatex -interaction=nonstopmode -halt-on-error manuscript.tex
```

The release build uses XeLaTeX because the package contains an independently
written Simplified Chinese abstract. It uses TeX Gyre Termes/Heros/Cursor,
TeX Gyre Termes Math, and Noto Serif/Sans/Mono CJK SC; the final font audit
must report every font embedded and subsetted.

The deterministic control suite is independent of typesetting. From the
parent Paper-11 directory, run `./experiments/reproduce.sh`. The frozen receipt
is 57/57 tests, 12 CSVs with 642 rows, 5/5 intentional negatives, and manifest
SHA-256 `de55c58ad7efc133b0d0865f392a30b52f6b05f89f64878cea0910b7eab557ea`.
The controls are finite witnesses and regression guards, not proofs of the
universal theorems.

## Evidence binding

The manuscript is bound to these immutable audit inputs:

| Artifact | SHA-256 |
|---|---|
| `notes/proof_audit.md` | `03f17606b0c9d69b496d2766c0a404b0d090698101150a800de4c2108ddc6b28` |
| `notes/composition_blueprint.md` | `4b6bfa27c83f72858ac5f0d03c0b9964f93e914fc1d4fdfced619327bcdfc30b` |
| `notes/phase3_core_proofs.md` | `4e79446d4a9bb861211186ffd3aa3b42899bc382fbf215a5a453495e5fbb0a66` |
| `notes/phase3_proxy_ownership_proofs.md` | `46603a1c2185cec1ffb3e7a2cb0f70873abf995edcc104977ac3d360d76e6401` |
| `notes/phase3_peer_review.md` | `b16027be916e4e6b8787bce8692dd8461f1e79fb29ea73b9b1d67f530341ad5c` |
| `notes/route_audit.md` | `9203d37cfaa28a45a7548a9864de614c81bf6ea199b4a6736e1c5aaa84335011` |
| `notes/phase2_framework_source_audit.md` | `a2345046972cc00d3031abdc214442359d0f78c7c0daf7d513ea26f924fb7439` |
| `notes/phase2_owner_proxy_audit.md` | `18116cf52c2359a840c9996fb6424fae56260f590990fac79704c040245fa761` |
| `notes/pre_manuscript_citation_audit.md` | `f9781bf65cec6ec4a29890164ea08c8dda4e6c152ebe2388ef56945b0e66e8ef` |

The convention boundary is binding: only the author-defined global-QC fibre
convolution, author unit-regular reduced record, and separately transported
full completion are positive actual-topology constructions. Raw HOpen zero is
`DIAGNOSTIC_ONLY`; retained standard frameworks on the actual owner are
`NOT_APPLICABLE`; the standard-circle proxy comparison ends at a proper
test-function image and defines no completion arrow.

## Figure and table trace

The following machine-readable ledger has **exactly six top-level keys per
artifact**: `artifact_id`, `source_data`, `transformation`, `caption_claim`,
`supported_manuscript_claims`, and `limitations`.

```yaml
figure_table_trace:
  - artifact_id: "fig:convention-split"
    source_data:
      - "notes/proof_audit.md#P11-3"
      - "notes/proof_audit.md#P11-6"
      - "paper/figures/convention_split.tex; sha256=fe816b5c5f8cea2e3ee94380773cb3d452e3af05e639a8ced2a290a1ead073b4"
    transformation: "Native TikZ logical branch by frozen function convention on the exact actual owner."
    caption_claim: "Global-QC is nonzero and canonically C_c(R), while raw HOpen is zero."
    supported_manuscript_claims:
      - "Author global-QC has the canonical nonzero *-algebra model C_c(R) — manuscript.tex, Section 4, Theorem label thm:phi and equation label eq:intertwining."
      - "The raw Hausdorff-open span is exactly zero and DIAGNOSTIC_ONLY — manuscript.tex, Section 6, Proposition label prop:hopen and equation label eq:hopen-zero."
      - "The two actual-owner records are a genuine function-convention split, not alternative names for one standard algebra — manuscript.tex, Section 6, paragraph immediately before label tab:framework-applicability."
    limitations: "HOpen is DIAGNOSTIC_ONLY; named retained actual frameworks are NOT_APPLICABLE because audited hypotheses fail, not because no theory can exist."
  - artifact_id: "fig:proxy-action-blind"
    source_data:
      - "notes/proof_audit.md#P11-7"
      - "notes/proof_audit.md#P11-8"
      - "results/indiscrete_convolution_controls_manifest.json; sha256=de55c58ad7efc133b0d0865f392a30b52f6b05f89f64878cea0910b7eab557ea"
      - "paper/figures/proxy_action_blind.tex; sha256=8cc369786047490df518e61c37d232fdc29b49fde7a81da440b7b6c713652c64"
    transformation: "Native TikZ one-sided topology map plus owner-preserving reduction of generic controls."
    caption_claim: "I has the proper test-function image A_const, and distinct actions yield the same global analytic records."
    supported_manuscript_claims:
      - "J is not continuous whereas J^{-1} is continuous — manuscript.tex, Section 6, Theorem label thm:J and equation label eq:J-direction."
      - "I is a test-function *-monomorphism with the proper image A_const and no completion extension — manuscript.tex, Section 6, Theorem label thm:I and the Completion stop paragraph following it."
      - "Every nonempty indiscrete R-action has the same author global algebra, fibre formulas, unit-regular family, and transported records — manuscript.tex, Section 7, Theorem label thm:action-blind."
      - "For the rational-Witt fixed-orbit application, p, a, L_p, action, orbit decomposition, and stabilizer do not survive in the analytic output — manuscript.tex, Section 7, Corollary label cor:rational-witt."
    limitations: "Test-function level only; no norm or completion arrow; no arithmetic promotion."
  - artifact_id: "tab:framework-applicability"
    source_data:
      - "notes/phase2_framework_source_audit.md; sha256=a2345046972cc00d3031abdc214442359d0f78c7c0daf7d513ea26f924fb7439"
      - "notes/pre_manuscript_citation_audit.md; sha256=f9781bf65cec6ec4a29890164ea08c8dda4e6c152ebe2388ef56945b0e66e8ef"
    transformation: "Manual transcription of audited theorem domains followed by exact hypothesis comparison with the actual owner."
    caption_claim: "The named source frameworks do not apply to the actual owner at their retained hypotheses."
    supported_manuscript_claims:
      - "Tu, Muhly--Williams, Exel, and Buss--Holkar--Meyer are NOT_APPLICABLE on the actual owner at their retained hypotheses — manuscript.tex, Section 6, Table label tab:framework-applicability."
      - "GLOB-FIBRE-FAMILY and Ind_x remain author-defined direct records, group-R results apply only after transport, and standard results remain proxy-only — manuscript.tex, Section 6, Table label tab:framework-applicability, final three rows."
      - "The finite table does not establish universal nonexistence of every non-Hausdorff convolution theory — manuscript.tex, Section 6, table caption and paragraph immediately following label tab:framework-applicability."
    limitations: "Finite named-framework audit only; no universal nonexistence statement."
  - artifact_id: "tab:route-ledger"
    source_data:
      - "evaluations/route_a/*/2026-08-15-stage11.yaml; seven immutable owner records"
      - "notes/route_audit.md; sha256=9203d37cfaa28a45a7548a9864de614c81bf6ea199b4a6736e1c5aaa84335011"
    transformation: "Direct transcription of candidate ID, complete SHA-256, A0--A4 tuple, overall status, and route_b_invocation_allowed."
    caption_claim: "Three Route-A records are exploratory negative priors, four are rejected, and Route B is false."
    supported_manuscript_claims:
      - "The manuscript contains the exact seven immutable candidate hashes and exact A0--A4 tuples — manuscript.tex, Section 7, Table label tab:route-ledger and the ordered hash/tuple ledgers immediately following it."
      - "Exactly three records are exploratory negative priors and four are rejected; exploratory is not a weak positive arithmetic result — manuscript.tex, Section 7, subsection Typed Route ledger."
      - "Every record has A4_FAIL, Route B is false, and no Route-B record exists — manuscript.tex, Section 7, final paragraph of subsection Typed Route ledger."
    limitations: "No A-coordinate splicing; every A2--A4 failure is NOT_TESTABLE; every Route-B flag is false."
```

Both figures have a caption and an immediately following prose equivalent in
`manuscript.tex`. Both tables carry explicit boundary text in their captions
or adjacent prose.

## Release boundary and declarations

No retained research-source PDF may be synchronized publicly. In particular,
exclude `notes/sources/*.pdf`, inherited Deninger bytes, and inherited optional
proxy-source PDFs. Public material may include manuscript source/PDF, code,
results, textual manifests, checksum ledgers, preflight JSON, and canonical
source links, subject to the eventual repository license and release decision.

The author list, affiliation formatting, corresponding-author status, CRediT
roles, funding, conflicts, acknowledgments, venue, license, public repository
identity, archive/DOI, release date, and venue-specific AI disclosure remain
neutral `AUTHOR TO CONFIRM` items where the workspace has no authoritative
value. No DOI, grant, archive, license, or immutable Paper-9 identity is
fabricated.

## Final package audit receipt

The 2026-08-15 release-candidate audit produced the following stable artifact
tuple (the README hash is intentionally reported by the parent package after
this section is frozen):

| Artifact | SHA-256 |
|---|---|
| `manuscript.tex` | `eb1aa4d7060cf1aa53a729e7c7be89a5724a6133ef3bf000cb800bf786de1002` |
| `references.bib` | `33afa817ff529cd0d98a791e4ea68c0e4a34bd57158774a6c51c43174b72d877` |
| `figures/convention_split.tex` | `fe816b5c5f8cea2e3ee94380773cb3d452e3af05e639a8ced2a290a1ead073b4` |
| `figures/proxy_action_blind.tex` | `8cc369786047490df518e61c37d232fdc29b49fde7a81da440b7b6c713652c64` |
| `paper.pdf` | `15d207568a61590852697511df2faf4cb06fd06047574c3dc3413e352c14840d` |

The clean build was executed in a new temporary directory using
XeLaTeX/BibTeX/XeLaTeX/XeLaTeX and returned zero. The final round reported no
missing citation, missing reference, overfull box, or underfull box; the only
messages were the standard `unicode-math`/`mathtools` command-ownership
warnings. The PDF has 16 A4 pages, reports no suspect content or JavaScript,
and all seven used fonts are embedded, subsetted, and Unicode mapped. The
complete 16-page candidate had already passed full visual inspection; after
the narrow equation-label revision, every affected equation/cross-reference
page (pp. 4--13) was rendered again and inspected for clipping, overlap,
number placement, and correct ``equation(s)'' references. All 26 `eq:*` labels
now resolve with cleveref type `equation`: 22 are in numbered `equation`
environments and four retain their numbered `align` environments. The Young
inequality renders the intended translation `\zeta(\,\cdot-v)`.
The final citation-locator pass bound both Green uses to Proposition 3
(physical p. 13 / printed p. 203), both MRW uses to Theorem 2.8 (physical p. 8
/ printed p. 10), and both Brown--Green--Rieffel uses to Theorem 1.2 (physical
p. 4 / printed p. 351). It added no MRW Theorem 3.1 locator and preserved the
existing BHM and Williams locators. Final affected pages 3 and 11 were rendered
and visually checked for locator wrapping and margin safety.
`pdftotext` extracted 6,730 whitespace-delimited tokens without replacement
characters or unresolved-reference sentinels. The paper directory contains
exactly one PDF (`paper.pdf`) and no auxiliary build files. The ten-entry
source checksum verification passed 10/10, while those retained source PDFs
remain outside the proposed public synchronization set.
