# Paper 12 manuscript package

This folder contains the release-candidate manuscript for **Marked Time
Cohomology and Orbitwise Standardization of Indiscrete Arithmetic Action
Groupoids**. The main text is English; the Simplified-Chinese abstract was
composed independently against the same frozen fact ledger. The package is
reviewable but is not yet authorized for standalone public release.

## Contents

- `manuscript.tex`: theorem statements, complete direct proofs, the exact
  comparison direction, three manuscript tables, declarations, and prose
  equivalents for both figures.
- `references.bib`: the frozen 14-record minimum bibliography: 11 external
  records and three honest, URL-free `@unpublished` companion records.
- `figures/same_carrier_diagonal.tex`: native TikZ topology/cohomology map.
- `figures/packet_four_way_firewall.tex`: native TikZ owner/topology firewall.
- `paper.pdf`: the sole retained typesetting artifact after the clean build.

## Build

Run the following exact cycle in a clean copy of this directory:

```sh
xelatex -interaction=nonstopmode -halt-on-error manuscript.tex
bibtex manuscript
xelatex -interaction=nonstopmode -halt-on-error manuscript.tex
xelatex -interaction=nonstopmode -halt-on-error manuscript.tex
xelatex -interaction=nonstopmode -halt-on-error manuscript.tex
cp manuscript.pdf paper.pdf
cmp -s manuscript.pdf paper.pdf
```

The first four commands are the required XeLaTeX/BibTeX/XeLaTeX$\times2$
cycle. On this manuscript, the additional XeLaTeX pass stabilizes the table
of contents, floats, and bibliography page references and removes the
transient `Label(s) may have changed` warning. The final two commands perform
and verify the explicit release copy from the build name to the retained
artifact name; a nonzero `cmp` result fails the package build.

XeLaTeX is required for the Simplified-Chinese abstract. The intended fonts
are TeX Gyre Termes/Heros/Cursor, TeX Gyre Termes Math, and Noto Serif/Sans/
Mono CJK SC. The final PDF gate requires all used fonts to be embedded,
subsetted, and Unicode mapped.

The control suite is separate from typesetting. From the parent Paper-12
directory, run `./experiments/reproduce.sh` once, serialized. Its frozen
receipt is 122/122 tests, 11 CSVs with 3,486 rows, 14/14 intentional
negatives, and manifest SHA-256
`7cbce9303393fcd755dda785312e26165656301e5dfbcab53b611e71c6204e95`.
The controls are finite witnesses and falsifiers, not proofs.

## Frozen evidence binding

- Composition blueprint: `b343dd47d4a4e2fc7b8570c33eb3270542732a4062142b1ef79530393000e107`.
- Pre-manuscript citation audit: `3a15bb9496b2cc949eb3e05f9b7cf8e73950ad77d491b39a207da740ef405564`.
- Final v4 proof: `77258319c1e1cbcc08501e33e3c60a03acd71a62342898f3535375e6159f77e8`.
- Integrated proof audit: `c2b0fc4ce4764b476de8623c7a1b37e33d51da4a1c318c133313956abf4af6ab`.
- Route audit: `2baf2b1ea63e5573f4b2673da6329520163ec67d76b002cb6f84fcf45c0ac102`.
- Controls manifest: `7cbce9303393fcd755dda785312e26165656301e5dfbcab53b611e71c6204e95`.

The central mathematical status is `STANDALONE_PASS`. The bounded search
status is `SUPPORTED_WITHIN_SEARCH through 2026-08-15`. Neither is a
publication, acceptance, citation, or public-release authorization.

## Figure and table trace

Every manuscript figure and table has the exact six required top-level keys
below. `supported_manuscript_claims` points back to explicit manuscript
labels, while each labelled caption points forward to the artifact described
here; this supplies the required bidirectional linkage.

```yaml
figure_table_trace:
  - artifact_id: "fig:same-carrier-diagonal"
    source_data:
      - "notes/phase3_core_proofs.md@sha256:9ab5c860f2ceceba27aa820ddd66564f9a7be2f2ee21bc06ea7110d1c38c16cd"
      - "notes/phase3_orbitwise_standardization_h1_proofs.md@sha256:77258319c1e1cbcc08501e33e3c60a03acd71a62342898f3535375e6159f77e8"
      - "notes/proof_audit.md@sha256:c2b0fc4ce4764b476de8623c7a1b37e33d51da4a1c318c133313956abf4af6ab"
      - "paper/figures/same_carrier_diagonal.tex@sha256:a83148600d497dd1b91510f5707a1b1a9402c35689013a1fa904978206ff5cf1"
    transformation: "Native TikZ logical diagram transcribing the proved one-sided identity, contravariant pullback, slope isomorphism, boundary contrast, and invariant equality; no numerical inference."
    caption_claim: "The constructed orbitwise-standard groupoid maps continuously to the actual indiscrete groupoid, while cohomology pulls back to the constant diagonal, exactly the strict-automorphism invariants."
    supported_manuscript_claims:
      - "Actual H^1 and zero boundaries — manuscript.tex, Theorem label thm:actual-h1."
      - "Standardized full-product H^1 and generally nonzero boundaries — manuscript.tex, Theorem label thm:standard-h1 and equation label eq:boundaries-warning."
      - "J direction, constant diagonal, and strict invariants — manuscript.tex, equations labels eq:J, eq:constant-diagonal, and eq:invariants."
    limitations: "Common nonempty cocompact lattice only; standardized degree one only; full algebraic product with no topology; strict time-preserving automorphisms only; reverse identity is not continuous."
  - artifact_id: "fig:packet-four-way-firewall"
    source_data:
      - "notes/phase3_marked_packet_proofs.md@sha256:3cf4a29d97499e1875d8f5bbfb1124d88e45e972ad3dbadbe6b8fffb5a3e6d49"
      - "notes/phase3_orbitwise_standardization_h1_proofs.md@sha256:77258319c1e1cbcc08501e33e3c60a03acd71a62342898f3535375e6159f77e8"
      - "paper/figures/packet_four_way_firewall.tex@sha256:9a52c273e91878d4dd74f96bd27fe299be39d98cdbebdda6bc800d89184b6908"
    transformation: "Native TikZ owner-and-topology diagram transcribing the source chain, constructed same-set standardization, two quotient records, and strict/scaled/unmarked boundary; no source figure is copied."
    caption_claim: "The fixed-prime application combines source-owned flow and stabilizer data, companion-owned actual topology, and Paper-12 standardization while keeping actual and discrete quotient topologies distinct."
    supported_manuscript_claims:
      - "Every-unit marked packet period — manuscript.tex, Corollary label cor:packet-period."
      - "Strict/scaled/unmarked boundary — manuscript.tex, equations labels eq:scaled-covariance, eq:dilation, and eq:orientation-reversal."
      - "Four-way fixed-prime comparison — manuscript.tex, Corollary label cor:packet-comparison and Table label tab:packet-types."
    limitations: "No orbit count or enumeration; no measure or local triviality; no actual-topology transport; no cross-prime or full-suspension claim; no arithmetic selectivity from the generic construction."
  - artifact_id: "tab:packet-types"
    source_data:
      - "notes/composition_blueprint.md@sha256:b343dd47d4a4e2fc7b8570c33eb3270542732a4062142b1ef79530393000e107"
      - "notes/phase3_orbitwise_standardization_h1_proofs.md@sha256:77258319c1e1cbcc08501e33e3c60a03acd71a62342898f3535375e6159f77e8"
    transformation: "Direct four-row transcription of the frozen owner/type ledger into a native LaTeX table."
    caption_claim: "The actual packet, standardized packet, actual quotient, and discrete component index are four distinct typed records."
    supported_manuscript_claims:
      - "Definitions and topology firewall — manuscript.tex, Table label tab:packet-types."
      - "Application without topology transfer — manuscript.tex, Section label sec:four-way."
    limitations: "Only the bare orbit set is shared where stated; no count, enumeration, measure, local triviality, or topology is transferred."
  - artifact_id: "tab:controls"
    source_data:
      - "results/manifest.json@sha256:7cbce9303393fcd755dda785312e26165656301e5dfbcab53b611e71c6204e95"
      - "notes/phase3_v4_controls_review.md@sha256:886a2648473035bb4d3600a03474680d3f692b1bdca08034096c6e7eebd664e6"
    transformation: "Lossless grouping of the 11 frozen CSV row counts into four readable manuscript rows, preserving the 3,486 total and 122/122 plus 14/14 receipt."
    caption_claim: "The deterministic package passes its frozen checks and intentional negatives."
    supported_manuscript_claims:
      - "Exact control receipt and role boundaries — manuscript.tex, Table label tab:controls and Section label sec:controls-route."
    limitations: "Finite regression witnesses and falsifiers only; no proof of universal, real, arbitrary-Q, ZFC, topology, source, or arithmetic claims."
  - artifact_id: "tab:route"
    source_data:
      - "notes/route_audit.md@sha256:2baf2b1ea63e5573f4b2673da6329520163ec67d76b002cb6f84fcf45c0ac102"
      - "eight Stage-12 Route-A YAMLs bound by that audit"
    transformation: "Direct transcription of each owner, its complete A0--A4 tuple, and overall verdict; serialization-only fields and hashes remain in the audit ledger."
    caption_claim: "Six Route-A records are exploratory, two are rejected, every A2--A4 coordinate fails, and no owner permits Route B."
    supported_manuscript_claims:
      - "Exact eight-owner tuple table — manuscript.tex, Table label tab:route."
      - "No determinant object, no coordinate splicing, and Route B closed — manuscript.tex, Section label sec:controls-route immediately after Table label tab:route."
    limitations: "Exploratory is a scoped negative prior, not weak determinant, explicit-formula, operator, or spectral evidence; zero Route-B files."
```

## Release and declaration boundary

The author list, academic unit, institution spelling, address if required,
corresponding status, email, ORCID, CRediT roles, funding, competing
interests, acknowledgments, venue-specific ethics wording, venue and AI
policy, public repository/tag/archive/license/DOI, and release authorization
remain `AUTHOR TO CONFIRM` where the workspace has no authoritative value.

The three companion bibliography records remain unpublished and URL-free.
Before standalone public release, each load-bearing companion dependency must
either be bound to an honest immutable public identity for the audited bytes
or be supplied self-containedly as an explicit premise or proof.

All retained research-source PDF files, including open-access source bytes,
are internal verification material and must be excluded from every public
index, staged delta, repository tree, archive, upload manifest, attachment
list, and fresh clone. The generated `paper/paper.pdf` is a project output
and is not a research-source PDF. The final real repository must run the Git/index,
archive, attachment, hidden-path, and fresh-clone gates described in the
frozen citation audit; Git metadata is absent from this workspace snapshot,
so those gates cannot be declared closed here.

## Correction Freeze audit receipt

`CORRECTION FREEZE` is the stable candidate after the official title of
Stacks Project Tag `0B1W` was corrected from the legacy seed wording
“Topological colimits” to “Colimits of spaces.”  The manuscript and both
figure sources are unchanged.  The completed citation/source-integrity report
(`79089b2487b6b21c10c1f10a4918fb29602d265877483d7a325634d15ec70a3a`)
and peer report
(`f3eaef077677144470e3f0417cb418009f0d340a8cd2856ac6cff74cf337438a`)
each return `CORRECTION FREEZE` PASS with C0/M0/m0.  The technical release
audit also returns PASS with C0/M0/m0; its SHA-256
`53afb3642812e981d0bb38b7166982c8818b7ef7085d96277dddd8f632d8d99b`
is the historical pre-status receipt, not a self-binding of these corrected
README bytes.  The append-only downstream release audit binds these
status-corrected README bytes; this README omits that report's digest to avoid
a hash cycle.  This receipt is not a public-release declaration, and
`PUBLIC_RELEASE_AUTHORIZED=false`.

The non-self-referential corrected artifact tuple is:

- `manuscript.tex`: `c6ad0f8c22d68840198d744a615da06e8b062d5ccdbeedb7f4ee76bf35073163`;
- `references.bib`: `b763e9c07e3265d878bfc8b4caf44fb6c92ef12e7fac59b8af0bdeb703876175`;
- `figures/same_carrier_diagonal.tex`:
  `a83148600d497dd1b91510f5707a1b1a9402c35689013a1fa904978206ff5cf1`;
- `figures/packet_four_way_firewall.tex`:
  `9a52c273e91878d4dd74f96bd27fe299be39d98cdbebdda6bc800d89184b6908`;
- `paper.pdf`: `9d6747e9f33c6ab3724beb35daedbb0efaff73691ed344374366f2392541ec15`.

The documented clean build produced 18 A4 pages and the retained PDF is
byte-identical to the build output.  Its layout-text SHA-256 is
`38adf39f29ac54af206f5c23537025f81a2b00fae1bed294bc4098a257fc10d4`.
The final log has no unresolved citation/reference, BibTeX metadata, box, or
missing-glyph warning; the only warning-class lines are the standard
`unicode-math` command-overwrite notices.  All eight used fonts are embedded,
subsetted, and Unicode mapped; Ghostscript parses the file; it contains zero
embedded raster images.  The 18 pages, including both figures, all three
tables, declarations, and references, were inspected at rendered resolution.
The citation graph closes 14 unique keys against exactly 14 bibliography
records, and the trace has five entries with all six mandatory keys.  After
removing TeX markup with `detex`, the English abstract has 205
whitespace-delimited prose words (displayed mathematics excluded).  The
reproducible Chinese convention counts Unicode `Script=Han` code points only:
PCRE `\p{Han}` on the prose body at `manuscript.tex` line 150 gives 353, and
the keyword values after the label on line 153 add 32, for 385 combined.  The
two abstracts follow the same frozen fact order and qualifications.  The
serialized controls receipt remains 122/122 tests, 11 CSVs/3,486 rows, 14/14
intentional negatives, and exact three-way generated-byte identity.  The
`CORRECTION FREEZE` citation and peer exact-byte relocks and technical release
audit all record PASS with C0/M0/m0.  All human, companion-identity, venue,
and real-publication-system release conditions above remain open.
