# Paper 11 independent release audit

Audit date: **2026-08-15 (Asia/Shanghai)**  
Audit role: **independent ARS release, visual, integrity, and reproducibility auditor**  
Disposition: **PASS — C0/M0/m0 at the exact byte tuple in Section 1**

This was a read-only audit of the frozen citation-only manuscript candidate.
No manuscript, bibliography, figure, PDF, README, lock, proof note, Route
record, source manifest, code file, or result was edited. The only repository
write made by this audit is this report.

The PASS is a technical release-candidate verdict. It is not a declaration
that the paper has already been synchronized, archived, submitted, or
standalone-released. The remaining human and publication-system conditions
are separated in Section 11 and are not counted as defects in the reviewed
bytes.

## 1. Exact final binding

The verdict applies only to the following exact files.

| Artifact | SHA-256 |
|---|---|
| `paper/manuscript.tex` | `eb1aa4d7060cf1aa53a729e7c7be89a5724a6133ef3bf000cb800bf786de1002` |
| `paper/paper.pdf` | `15d207568a61590852697511df2faf4cb06fd06047574c3dc3413e352c14840d` |
| `paper/references.bib` | `33afa817ff529cd0d98a791e4ea68c0e4a34bd57158774a6c51c43174b72d877` |
| `paper/README.md` | `86d87e66417ba387f0fc1ed8c4d7b037519f22bb72932b0b18f22d3d5e4625b6` |
| `paper/figures/convention_split.tex` | `fe816b5c5f8cea2e3ee94380773cb3d452e3af05e639a8ced2a290a1ead073b4` |
| `paper/figures/proxy_action_blind.tex` | `8cc369786047490df518e61c37d232fdc29b49fde7a81da440b7b6c713652c64` |
| project `README.md` | `5d1df0d898ae95bceb45e02eb0612bcd6af2c736061f80102567cd6bf54ca61f` |
| `notes/peer_review_round1.md` | `864f102b2b4dbadc3ff36807d0fec564375e6235e5a0319e26dcb2de5487dc36` |
| `notes/citation_audit.md` | `23bc34be1d21a61cead4e982c6d86749ab34470c0efc274be1bec047e54a6179` |

The tuple was recomputed at audit start and again immediately before this
report was created. All nine values matched the frozen locks on both reads.

Principal immutable evidence also re-hashed exactly:

| Evidence | SHA-256 |
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
| controls manifest | `de55c58ad7efc133b0d0865f392a30b52f6b05f89f64878cea0910b7eab557ea` |

## 2. Acceptance and severity rule

- **Critical:** a release blocker or defect invalidating a central result,
  owner boundary, or integrity conclusion.
- **Major:** a substantive repair required in a central proof, claim,
  citation/source contract, reproducibility result, or release boundary.
- **Minor:** a local manuscript, citation, visual, trace, or packaging repair.

No finding at any of these severities remains in the exact tuple.

## 3. Isolated build and retained-artifact equivalence

A new temporary build directory was populated with only the final TeX,
BibTeX, and two native TikZ sources. The documented four commands were run:

```text
xelatex -interaction=nonstopmode -halt-on-error manuscript.tex
bibtex manuscript
xelatex -interaction=nonstopmode -halt-on-error manuscript.tex
xelatex -interaction=nonstopmode -halt-on-error manuscript.tex
```

All four returned zero. The final pass had no undefined citation or reference,
missing target, duplicate label, missing character, overfull/underfull box,
LaTeX error, or fatal error. Its only warnings were the known package-level
`unicode-math`/`mathtools` command-ownership notices.

The fresh PDF SHA-256 was
`e109b89b662763a12059bfc83bcaa2a35cd3f901183a972cd6adda5f57f21e84`.
It is not expected to equal the retained PDF byte-for-byte because XeLaTeX/
xdvipdfmx emits creation and subset-serialization metadata. The substantive
comparisons were exact:

- retained and fresh `pdftotext -layout` outputs were byte-identical, SHA-256
  `89743a4df0788d988b7c09a625e8761d30bda1d39590ef9c11492e6ed95096fc`;
- the extracted layout had 52,385 characters and 6,730 whitespace-delimited
  tokens, with zero U+FFFD characters and zero unresolved/undefined
  sentinels; and
- independent 150-dpi renders of all pages were byte-identical for **16/16**
  retained/fresh page pairs.

Thus the final source rebuild reproduces the retained text and complete page
appearance even though incidental PDF serialization bytes differ.

## 4. PDF structure, fonts, hygiene, and visual inspection

The retained PDF is 16 unrotated A4 pages, PDF 1.5, unencrypted, and reports
`Suspects: no`, no form, no JavaScript, no metadata stream, and no custom
metadata. Its title, subject, keywords, author, and producer fields agree with
the manuscript package. `pdfdetach` found zero embedded files, `pdfimages`
found no raster images, a targeted object-string scan found no active-content
marker, and Ghostscript rendered the complete file to `nullpage` with status
zero.

`pdffonts` reported seven fonts. Every row was embedded, subsetted, and
Unicode mapped: TeX Gyre Termes bold/regular/italic, TeX Gyre Termes Math,
Noto Serif CJK bold/regular, and TeX Gyre Cursor.

The locked candidate pages 1--16 were all inspected at original render detail.
The two citation-relock surfaces on pp. 3 and 11 were checked specifically for
line wrapping, margin safety, collisions, and readable physical/printed-page
locators. Pages 4 and 12, containing the two vector figures, were additionally
rendered and inspected at 300 dpi (2481 x 3508 pixels). The two tables on pp.
10 and 14, the English and Chinese text, equations and number placement, and
the references on p. 16 are legible. No clipping, overlap, empty page, missing
glyph, broken text, unreadable element, or caption/artifact contradiction was
found. The Young term on p. 8 renders the intended centered dot in
`\zeta(\,\cdot-v)`.

The final `paper/` package contains exactly these six regular files:

```text
README.md
figures/convention_split.tex
figures/proxy_action_blind.tex
manuscript.tex
paper.pdf
references.bib
```

It has exactly one PDF, zero symlinks/nonregular entries, zero auxiliary TeX
build files, and no Python bytecode or cache directory.

## 5. Labels and citation graph

The manuscript has 56 labels, all unique. Forty source cross-reference
targets were extracted and every target exists. All 26 `eq:*` labels are in
numbered mathematical environments: 22 in `equation` and four in `align`.

The citation graph independently recounts to:

- 21 citation commands;
- 22 cited-key uses;
- 10 distinct in-text keys; and
- 10 distinct BibTeX entries, with exactly the same key set.

There is no missing, dangling, orphan, decorative, or uncited bibliography
entry. Both uses of each final proxy-ladder source carry the required exact
locator:

- Green, Proposition 3, physical p. 13 / printed p. 203;
- Muhly--Renault--Williams, Theorem 2.8, physical p. 8 / printed p. 10; and
- Brown--Green--Rieffel, Theorem 1.2, physical p. 4 / printed p. 351.

MRW Theorem 3.1 is correctly absent because the manuscript does not claim
that separate tensor route. The existing BHM and Williams locators remain
distinct from the Morita and stable-isomorphism results.

The final ARS citation/source-integrity report, SHA-256
`23bc34be1d21a61cead4e982c6d86749ab34470c0efc274be1bec047e54a6179`,
binds the exact tuple and returns **PASS — C0/M0/m0** after complete
reference/context and source-strength verification.

## 6. Deterministic controls and byte reproducibility

The official `experiments/reproduce.sh` was executed in a fresh temporary
copy of the final Paper-11 directory. It returned zero and reported:

- **57/57** unit tests passed;
- **12 CSVs / 642 data rows**;
- **5/5** intentional negatives detected, comprising three wrong-time-sign
  cases and two wrong-source/range raw probes;
- strict verify-only passed for checked-in results and two fresh generations;
- all **13 generated artifacts** were byte-identical across checked-in,
  fresh-one, and fresh-two;
- manifest SHA-256 remained
  `de55c58ad7efc133b0d0865f392a30b52f6b05f89f64878cea0910b7eab557ea`;
  and
- the forbidden bytecode/cache scan passed.

The controls remain correctly described as finite witnesses and regression
guards, not proofs of the universal mathematical results.

## 7. Strict figure/table trace

The YAML ledger in `paper/README.md` parses to exactly four artifacts:

1. `fig:convention-split`;
2. `fig:proxy-action-blind`;
3. `tab:framework-applicability`; and
4. `tab:route-ledger`.

Every entry has exactly the six required top-level keys, in the declared
order, and no seventh key: `artifact_id`, `source_data`, `transformation`,
`caption_claim`, `supported_manuscript_claims`, and `limitations`.

The strict forward and reverse audit passed:

- the four trace IDs equal the complete set of two figure and two table labels
  in the manuscript, with no untraced or extra artifact;
- all 13/13 supported-claim items have nonempty concrete claim text and a
  manuscript locator;
- all 14/14 label locators named by those claims exist;
- all 6/6 hash-qualified trace sources match their bytes;
- both native TikZ files map to the exact manuscript inputs; and
- reverse reading of every caption and adjacent substantive prose returns one
  unique trace entry with a visible, nonempty limitation.

Both figures also have prose equivalents, and both table boundaries are
stated in their captions or adjacent prose.

## 8. Route and source-integrity ledgers

The workspace contains exactly seven `evaluations/route_a/*/2026-08-15-stage11.yaml`
records and zero Stage-11 Route-B records. Independent parsing and re-hashing
confirmed that all seven file hashes, candidate IDs, A0--A4 tuples, outcomes,
and `route_b_invocation_allowed` fields agree with both the manuscript and
`notes/route_audit.md` in both directions. All 51/51 hash-qualified YAML
artifact references resolve to the expected bytes.

The aggregate is exact: three `ROUTE_A_EXPLORATORY` negative priors, four
`ROUTE_A_REJECTED` records, all seven with `A4_FAIL`, all seven Route-B flags
false, and no Route-B record. No A-coordinate is spliced across owners.

From `notes/sources`, `sha256sum -c framework_sources.sha256` passed 10/10:
five retained research PDFs and their five preflight JSON sidecars. This is a
read-integrity result, not permission to redistribute those PDF bytes.

## 9. Temporary Git payload/index dry run

Because the shared workspace is not itself a Git worktree, a disposable Git
index and archive were constructed outside the repository from the frozen
Paper-11 candidate plus the seven Stage-11 Route-A YAML files. The test used
`git add`, `write-tree`, and `git archive`; the temporary tree was
`16626c85349918a5ff663b95c5ec3f092af50199`.

The index and archive each contained the same 63-file pre-report payload.
Mechanical enumeration showed:

- `notes/sources/*.pdf`: **0 in the index and 0 in the archive**;
- all five preflight JSON sidecars: present;
- `notes/sources/.gitignore`, `framework_source_manifest.md`, and
  `framework_sources.sha256`: present;
- the manuscript `paper/paper.pdf`: present; and
- all seven Stage-11 Route-A YAML records: present.

`git check-ignore -v` attributed exclusion of all five retained framework PDFs
to `notes/sources/.gitignore` and its `*.pdf` rule. The disposable index/archive
therefore proves the proposed-payload exclusion mechanism without altering
the workspace. It does not claim that an actual remote synchronization or
fresh public clone has already occurred.

## 10. Independent review binding and final findings

The peer-review report, SHA-256
`864f102b2b4dbadc3ff36807d0fec564375e6235e5a0319e26dcb2de5487dc36`,
contains a final citation-only re-lock addendum binding the exact tuple in
Section 1 and returns **PASS — C0/M0/m0**. It preserves the prior mathematical,
owner, bilingual, visual, Route, control, trace, and packaging findings after
the pinpoint-only citation change.

The citation/source-integrity report is independently bound in Section 5 and
also returns **PASS — C0/M0/m0**. This release audit reproduces the principal
build, rendering, control, label/citation-graph, trace, Route, source-checksum,
and proposed-payload checks rather than merely inheriting those verdicts.

| Severity | Count |
|---|---:|
| Critical | **0** |
| Major | **0** |
| Minor | **0** |

## 11. External prerequisites, not current candidate defects

The following remain explicit standalone-release or submission conditions.
They do not change the C0/M0/m0 finding because the manuscript discloses them
and does not fabricate their values:

1. Human confirmation of the final author list, affiliation formatting,
   corresponding-author status, CRediT roles, funding, conflicts,
   acknowledgments, venue, licence, repository identity/tag, archive/DOI,
   release date, and venue-specific AI-assistance wording.
2. Assignment of Paper 9's real immutable public repository/release/archive
   identity after the coordinated batch synchronization; no DOI or URL may be
   invented.
3. In the actual Git/publication worktree, enumeration of tracked and staged
   files, execution of the real synchronization, and inspection of a fresh
   clone/export proving that retained research-source PDFs were neither
   staged nor uploaded. The disposable dry run in Section 9 is not this
   external-state check.
4. Submission-day refresh of correction/retraction, DOI, Williams-errata, and
   chosen-venue policy checks.

Until these conditions are closed, the technically accepted bytes remain a
reviewed release candidate rather than a declaration of standalone public
release.

## 12. Final disposition

**PASS — technically release-ready at the exact tuple in Section 1, with
C0/M0/m0 and no open candidate repair.** Any subsequent byte change to a
bound manuscript, bibliography, figure, PDF, README, peer-review report, or
citation report invalidates this tuple-specific verdict and requires a new
audit. Standalone release labeling remains conditional on Section 11.

## 13. Status-only correction-freeze release relock

This addendum performs the required tuple-specific relock after the Paper-11
project `README.md` status paragraph was corrected. It is append-only and does
not rewrite the original release report: the exact 14,712-byte, 305-line
historical report above is preserved verbatim as a prefix with SHA-256
`fc3527d42bcbf20446f91e55ef440f875d52457c329d3a58671a2affd20ebf5b`.
The superseded project-README, citation-audit, and peer-review hashes in
Section 1 remain visible as historical receipts; only their active release
bindings are replaced below. Every paper-package row in Section 1 is unchanged.

### 13.1 Status-only delta and corrected receipt truth

The current project `README.md` is 3,525 bytes and 56 lines, SHA-256
`1380928a1d9e46e4a82395a2a3059bc1c1a8a33a9450ecd6d7e31adfb1a86a64`.
Byte-level comparison finds exactly one unified-diff hunk: the prior five-line
status paragraph is replaced by the current five-line status paragraph and no
other byte changes. Inverting only that hunk reconstructs the 3,461-byte,
56-line prior README exactly at SHA-256
`5d1df0d898ae95bceb45e02eb0612bcd6af2c736061f80102567cd6bf54ca61f`.

The corrected paragraph is accurate. The final citation/source-integrity
relock is **PASS — C0/M0/m0** at SHA-256
`c7be95522abe4ab4c92494da7458b15319a838de6a391820c1f0f201bbed2498`,
and the receipt-only peer relock is **PASS — C0/M0/m0** at SHA-256
`6f949e0f98baf68e27bbf9bac8623c437e601cafdbc2a7a7138d7a71e28f79e8`.
The historical technical release audit preserved above is itself **PASS —
C0/M0/m0**. The status correction therefore records completed technical gates;
it does not assert that any external publication action occurred.

### 13.2 Exact corrected release tuple

Independent re-hashing binds this addendum to the following bytes:

| Artifact | SHA-256 |
|---|---|
| project `README.md` | `1380928a1d9e46e4a82395a2a3059bc1c1a8a33a9450ecd6d7e31adfb1a86a64` |
| `paper/README.md` | `86d87e66417ba387f0fc1ed8c4d7b037519f22bb72932b0b18f22d3d5e4625b6` |
| `paper/manuscript.tex` | `eb1aa4d7060cf1aa53a729e7c7be89a5724a6133ef3bf000cb800bf786de1002` |
| `paper/references.bib` | `33afa817ff529cd0d98a791e4ea68c0e4a34bd57158774a6c51c43174b72d877` |
| `paper/figures/convention_split.tex` | `fe816b5c5f8cea2e3ee94380773cb3d452e3af05e639a8ced2a290a1ead073b4` |
| `paper/figures/proxy_action_blind.tex` | `8cc369786047490df518e61c37d232fdc29b49fde7a81da440b7b6c713652c64` |
| `paper/paper.pdf` | `15d207568a61590852697511df2faf4cb06fd06047574c3dc3413e352c14840d` |
| `notes/citation_audit.md` | `c7be95522abe4ab4c92494da7458b15319a838de6a391820c1f0f201bbed2498` |
| `notes/peer_review_round1.md` | `6f949e0f98baf68e27bbf9bac8623c437e601cafdbc2a7a7138d7a71e28f79e8` |

The paper package still contains exactly six regular files, exactly one PDF
(`paper.pdf`), and no symlink, research-source PDF, build auxiliary, or cache.
The ten retained framework-source checksum entries again pass 10/10, while the
`*.pdf` source-exclusion rule and source manifest remain unchanged. The
candidate lock and pipeline-state bytes are also unchanged.

Because the corrected project status is outside `paper/` and every manuscript,
bibliography, figure, trace README, and retained-PDF hash is identical, the
complete isolated-build, text/raster/font/PDF-structure, visual, mathematics,
owner/Route, strict-trace, citation-graph, controls, and source-boundary
receipts in Sections 3--10 remain applicable without qualification. A new build
or controls run would test the same bytes and is not required for this
status-only receipt; neither was run. No candidate lock, citation report, peer
report, pipeline record, paper artifact, evidence file, control, source file,
or Git state was edited, and no Git command was run. This addendum changes only
`notes/release_audit.md`.

### 13.3 Public boundary and disposition

`PUBLIC_RELEASE_AUTHORIZED=false`. The technically accepted tuple remains a
reviewed release candidate until the following external gates are actually
closed: human declarations and publication metadata; Paper 9's immutable
public identity; the chosen venue and then-current policy checks; and a real
public synchronization/fresh-export inspection proving research-source PDF
exclusion. The disposable dry run described in Section 9 is not that real
synchronization check.

| Severity | Count |
|---|---:|
| Critical | **0** |
| Major | **0** |
| Minor | **0** |

**Status-only release relock: PASS at the exact corrected tuple in Section
13.2 (C0/M0/m0), with public release authorization remaining false.** Any
later byte change to a bound artifact requires another tuple-specific audit.
