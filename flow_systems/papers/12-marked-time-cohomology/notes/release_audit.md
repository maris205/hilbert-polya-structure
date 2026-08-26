# Paper 12 independent final release audit

Audit date: **2026-08-15 (Asia/Shanghai)**  
Audit role: **independent ARS release, integrity, citation, formatter, PDF,
visual, trace, Route, and reproducibility auditor**  
Disposition: **PASS — REVIEW FREEZE 2 exact lock; C0/M0/m0**

This was a read-only audit of the frozen Paper-12 candidate. No manuscript,
bibliography, figure, PDF, README, proof, source, control, result, or Route
artifact was edited. Controls were not launched in this lane, and no Git
operation was run. The only workspace write made by this audit is this
report.

The PASS is a technical release-candidate verdict on the exact bytes below.
It is not public-release authorization, journal acceptance, or evidence that
a real repository/archive synchronization has already occurred. Human,
companion-identity, venue, and real-publication-system conditions are
separated in Section 11 and are not counted as defects in the reviewed
candidate.

## 1. Exact final binding

The verdict applies only to this tuple, recomputed after both prerequisite
independent reports were frozen.

| Artifact | SHA-256 |
|---|---|
| `paper/manuscript.tex` | `c6ad0f8c22d68840198d744a615da06e8b062d5ccdbeedb7f4ee76bf35073163` |
| `paper/references.bib` | `e1f4d0f6589ce0710173bad1c0089b5d6746d09010cc448d6d387ad8c9e17dcf` |
| `paper/figures/same_carrier_diagonal.tex` | `a83148600d497dd1b91510f5707a1b1a9402c35689013a1fa904978206ff5cf1` |
| `paper/figures/packet_four_way_firewall.tex` | `9a52c273e91878d4dd74f96bd27fe299be39d98cdbebdda6bc800d89184b6908` |
| `paper/paper.pdf` | `3fda5ae01fd3b7a78ddbefb11a62befa4d2ab50906b112b39e3c48e89901a294` |
| `paper/README.md` | `149bb1c9177f629fd5e04defa48ce17716cad85ea9d51dd0a8135e79b2214a7f` |
| project `README.md` | `a156deefbb059d840f73bfd6d76d468300158ad0e8c8bffef81b7a355c2cec51` |
| `notes/peer_review_round1.md` | `e1f1558e170831457685a4a5c8c4d77f061b405d6c499867b6ce4f91bea6dc2b` |
| `notes/citation_audit.md` | `f599dfbf67026b0985ee0e09b4e41bb24e3fe94709a1cd5e03ba657fb2a4fcaf` |
| `pdftotext -layout paper/paper.pdf` output | `8f9715f37f1a6d87d71855cdfb3656e2c5102f69fb2b184c24d15c76119d22d9` |

The two README hashes include the final receipt-only normalization of the
abstract counts. It changed no manuscript, bibliography, figure, or PDF
byte.

Principal frozen evidence also re-hashed exactly:

| Evidence | SHA-256 |
|---|---|
| `notes/composition_blueprint.md` | `b343dd47d4a4e2fc7b8570c33eb3270542732a4062142b1ef79530393000e107` |
| `notes/pre_manuscript_citation_audit.md` | `3a15bb9496b2cc949eb3e05f9b7cf8e73950ad77d491b39a207da740ef405564` |
| `notes/phase3_orbitwise_standardization_h1_proofs.md` | `77258319c1e1cbcc08501e33e3c60a03acd71a62342898f3535375e6159f77e8` |
| `notes/proof_audit.md` | `c2b0fc4ce4764b476de8623c7a1b37e33d51da4a1c318c133313956abf4af6ab` |
| `notes/route_audit.md` | `2baf2b1ea63e5573f4b2673da6329520163ec67d76b002cb6f84fcf45c0ac102` |
| `results/manifest.json` | `7cbce9303393fcd755dda785312e26165656301e5dfbcab53b611e71c6204e95` |

## 2. Acceptance and severity rule

- **Critical:** invalidates a central theorem, owner boundary, integrity
  conclusion, or release-candidate identity.
- **Major:** requires substantive repair of a proof, claim, citation/source
  contract, reproducibility result, Route conclusion, or release boundary.
- **Minor:** requires a local manuscript, citation, trace, visual, build, or
  packaging repair.

No finding at any of these severities remains in the exact tuple.

## 3. Independent isolated build

A new temporary directory was populated with only the final TeX, BibTeX,
and two native TikZ sources. The documented sequence was run exactly:

```text
XeLaTeX -> BibTeX -> XeLaTeX -> XeLaTeX -> XeLaTeX -> copy -> cmp
```

All commands returned zero. The additional final XeLaTeX pass cleared the
transient reference-stabilization warning, and `cmp -s` verified that the
fresh release copy was byte-identical to that run's `manuscript.pdf`.

The final pass contains no undefined citation/reference, rerun request,
BibTeX warning, duplicate label, overfull/underfull box, missing glyph,
LaTeX error, or fatal error. Its only warning-class output is the standard
`unicode-math`/`mathtools` command-ownership notice.

The fresh PDF has 18 A4 pages and reproduces the locked layout text exactly,
with SHA-256
`8f9715f37f1a6d87d71855cdfb3656e2c5102f69fb2b184c24d15c76119d22d9`.
Independent 144-dpi rendering gave **18/18 byte-identical retained/fresh page
pairs**. The regenerated PDF container need not have the retained binary
hash because XeLaTeX/xdvipdfmx creation and font-subset serialization
metadata vary across builds; exact source identity, stabilized text, and
complete rendered appearance are the substantive build checks.

## 4. PDF structure, fonts, text, and visual inspection

The retained PDF is 18 unrotated A4 pages, PDF 1.5, unencrypted, and reports
`Suspects: no`, no form, no JavaScript, no custom metadata, and no metadata
stream. `pdfdetach` finds zero embedded files; `pdfimages` finds zero raster
images; Ghostscript parses all pages successfully.

`pdffonts` reports eight used fonts. Every font is embedded, subsetted, and
Unicode mapped: TeX Gyre Termes bold/regular/italic, TeX Gyre Termes Math,
Noto Serif CJK bold/regular, and TeX Gyre Cursor regular/italic.

The extracted layout text has 8,327 whitespace tokens and 68,035 bytes, with
zero U+FFFD characters, zero `??`/undefined sentinels, and no leaked local
path, retained-source basename, TeX/Bib source name, or 64-hex internal
digest. A binary-string scan likewise finds no local path, attachment, or
active-content marker.

All 18 retained pages were rendered and inspected individually. The English
and Simplified-Chinese abstracts, contents, theorem/proof sequence,
equations, both figures, all three tables, declarations, and all 14
references are legible and unclipped. No collision, bad wrap, empty page,
missing glyph, broken link text, caption contradiction, or semantic-unit
split remains. In particular:

- Figure 1 precedes and does not interrupt Corollary 8.2;
- Figure 2 does not interrupt the 3,252/3,151-row control sentence;
- the Route table remains in Section 9.2 before limitations, declarations,
  and references; and
- the former visible `quad`/`qquad` tokens, duplicated cleveref nouns,
  missing locator parenthesis, grammar defect, and duplicated companion
  years are absent.

The final `paper/` package contains exactly six regular files: one
manuscript, one bibliography, two TikZ sources, one README, and the sole PDF
`paper.pdf`. It contains no build auxiliary, `manuscript.pdf`, symlink,
cache, or bytecode artifact.

## 5. Labels, citation closure, and bilingual lock

The manuscript has 82 labels, all unique. Its cross-reference graph has 35
unique targets and zero missing target. The final citation graph, independently
verified in the citation audit, has 27 commands, 31 key occurrences, and 14
unique keys; `references.bib` has exactly the same 14 records. There are zero
dangling citations, orphan bibliography records, duplicate keys, or
unresolved rendered citations.

The bibliography is the frozen minimum: 11 external records and three
honest `@unpublished` companion records. All eight journal-article records
have their verified DOI; the three web records use honest `n.d.` year values
with access dates; the companion records have no DOI or URL and render their
14/15 August 2026 dates once. The final citation/source-integrity report
binds every manifestation, locator, owner ceiling, and claim context and
returns **PASS — C0/M0/m0**.

The abstract counts reproduce under their declared methods:

- English: **205** whitespace-delimited prose words after `detex`, with
  displayed mathematics omitted;
- Simplified Chinese: **370** Unicode Han code points.

Both are within the 200--260 and 300--500 targets. Independent comparison
against the twelve-slot composition ledger confirms the same fact order,
quantifiers, qualifications, and negative boundaries without sentence-level
translation dependence.

## 6. Mathematical, owner, topology, category, and status closure

The independent peer report adjudicates every theorem-like result and
returns **ACCEPT / exact-lock PASS — C0/M0/m0, confidence 5/5**. This audit
confirms that the final manuscript retains the central v4 comparison and all
of its ceilings:

- actual `H^1_cnv = R[c]` and actual `B^1_cnv = 0`;
- common-lattice, section-free same-carrier standardization, full and
  faithful with global indiscretization as the declared strict inverse;
- canonical abstract automorphism extension with choice-dependent
  surjectivity and noncanonical splitting;
- standardized degree-one `H^1_cnv = R^Q` as the full algebraic Cartesian
  product, with generally nonzero standardized boundaries;
- continuous `J:G_std -> G_actual`, contravariant `J*`, and the constant
  diagonal equal to strict time-preserving automorphism invariants;
- strict/scaled/unmarked category separation and the explicit weaker-
  category non-descent controls;
- distinct actual packet, standardized packet, actual quotient, and
  discrete component-index records, with only a nonempty bare orbit set
  shared where stated; and
- no higher standardized cohomology, cohomology topology, orbit count,
  measure, topology transfer, cross-prime/full-suspension theorem, trace,
  determinant, analytic continuation, quantization, or operator lift.

The scientific disposition remains exactly `STANDALONE_PASS`. The bounded
novelty status remains exactly
`SUPPORTED_WITHIN_SEARCH through 2026-08-15`. Neither status is presented as
journal acceptance, absolute priority, or public-release authorization.

## 7. Deterministic controls without a duplicate run

This release-audit lane did **not** rerun controls. It binds the peer
reviewer's reserved, serialized final reproduction:

- exit status zero and **122/122 tests**;
- **11 CSV files / 3,486 rows**;
- **14/14 intentional negatives**;
- checked-in, fresh-one, and fresh-two generated outputs byte-identical;
- recursive-entry/no-cache gates PASS, with no cache or bytecode residue;
  and
- manifest unchanged at
  `7cbce9303393fcd755dda785312e26165656301e5dfbcab53b611e71c6204e95`.

A separate read-only recount in this lane confirms 11 manifest artifacts,
3,486 data rows, all 11 artifact hashes, `regression_status: PASS`, 14
negatives, and zero negative failures. The manuscript correctly treats the
controls as finite witnesses and falsifiers, never as proofs of universal,
real, arbitrary-`Q`, choice, topology, source, or arithmetic claims.

## 8. Strict six-key bidirectional figure/table trace

The manuscript contains exactly two figures and three tables. The YAML
ledger in `paper/README.md` contains exactly those five artifacts. Each
entry has exactly the six mandatory top-level keys, in the declared order
and with no seventh key:

```text
artifact_id -> source_data -> transformation -> caption_claim ->
supported_manuscript_claims -> limitations
```

All 30 mandatory fields are present. Every hash-qualified source pointer
matches its current bytes; every figure source matches the frozen tuple;
every limitations field is nonempty and surfaced in the caption or adjacent
prose. Forward tracing from artifact to claim and reverse tracing from every
substantive manuscript use return the same unique ledger entry. There is no
untraced figure/table, unsupported caption claim, omitted reverse use, or
empty-limitation advisory.

## 9. Route closure

Read-only parsing finds exactly eight Stage-12 Route-A records and zero
Stage-12 Route-B records. Their ID-to-tuple and ID-to-verdict maps agree with
`notes/route_audit.md` and manuscript Table 3:

- six `ROUTE_A_EXPLORATORY` and two `ROUTE_A_REJECTED`;
- every A2, A3, and A4 coordinate fails;
- every owner uses
  `NONE_BY_DESIGN_NO_DETERMINANT_OBJECT`;
- all eight `route_b_invocation_allowed` fields are false; and
- no coordinate is spliced across owners.

“Exploratory” remains a scoped negative prior, not weak positive evidence
for a determinant, explicit formula, spectral object, or operator program.
Route B is closed.

## 10. Source integrity, package exclusion, and Git boundary

`sha256sum -c notes/sources/coh-sources.sha256` returns **10/10 OK** for the
five retained research PDFs and five preflight sidecars. The source
directory's adjacent `.gitignore` excludes `*.pdf` while retaining the
preflight JSON files.

The five research-source PDFs exist only as internal verification bytes
under `notes/sources/`. None is in `paper/`, named by the manuscript/BibTeX
as a payload path, embedded in `paper.pdf`, or exposed in extracted PDF
text. Both READMEs and the manuscript explicitly distinguish those excluded
research bytes from the generated project output `paper/paper.pdf`.

Git metadata is absent from this workspace snapshot, and this audit ran no
Git operation. Consequently, actual index, staged-delta, repository-tree,
archive, upload-manifest, attachment-list, hidden-path, remote-sync, and
fresh-clone exclusion cannot honestly be declared complete here. Closing
those checks in the real publication repository is an external release
condition, not a hidden defect in the frozen package.

## 11. Independent-report binding and external conditions

The prerequisite reports are independently frozen on the exact candidate:

| Report | Verdict | SHA-256 |
|---|---|---|
| `notes/peer_review_round1.md` | ACCEPT / exact-lock PASS; C0/M0/m0; confidence 5/5 | `e1f1558e170831457685a4a5c8c4d77f061b405d6c499867b6ce4f91bea6dc2b` |
| `notes/citation_audit.md` | PASS — final citation/source integrity; C0/M0/m0 | `f599dfbf67026b0985ee0e09b4e41bb24e3fe94709a1cd5e03ba657fb2a4fcaf` |

This release audit reproduces the principal hashes, build, rendered-page,
font, text, label/citation, trace, manifest, Route, source-checksum, and
package-exclusion checks rather than inheriting those verdicts without
inspection.

The following are explicit human or external-state prerequisites, not
current candidate defects:

1. Confirm the final author list, academic unit, institution spelling and
   address, corresponding status/email/ORCID, CRediT roles, funding,
   competing interests, acknowledgments, and venue-specific ethics wording.
2. Select the venue/article type and confirm its current template, citation,
   AI-disclosure, data/code-availability, and submission requirements.
3. Bind each load-bearing companion dependency to an honest immutable public
   identity for the audited bytes, or replace that dependency with a
   self-contained premise/proof; do not invent a DOI or URL.
4. Human-confirm the public repository, immutable tag/archive, license, DOI
   if any, release date, exact release bytes, and release authorization.
5. In the real repository/publication environment, complete the index,
   stage, tree, archive, upload, attachment, hidden-path, remote, and fresh-
   clone checks proving that no retained `notes/sources/*.pdf` byte is public.
6. Refresh DOI/version/correction/retraction, authoritative-web, and chosen-
   venue policy checks on the actual submission date.
7. Re-run exact-byte review if any bound manuscript, bibliography, figure,
   PDF, README, trace, declaration, peer-review, or citation-audit byte
   changes.

Until these conditions are closed, the candidate is technically accepted
but must not be labeled as a completed standalone public release or journal
submission.

## 12. Final disposition

| Severity | Count |
|---|---:|
| Critical | **0** |
| Major | **0** |
| Minor | **0** |

**PASS — technically release-ready as REVIEW FREEZE 2 at the exact tuple in
Section 1, with C0/M0/m0 and no open candidate repair.**

```text
RELEASE_CANDIDATE_INTEGRITY=PASS
CURRENT_CANDIDATE_DEFECT_COUNT=0
PUBLIC_RELEASE_AUTHORIZED=false
PUBLIC_RELEASE_HOLD=human declarations + immutable companion identity or self-contained replacement + real Git/publication-system exclusion + venue/submission confirmation
```

The `PUBLIC_RELEASE_AUTHORIZED=false` line records external conditions; it
does not downgrade the exact-byte release-candidate PASS. Any later change
to a bound artifact invalidates this tuple-specific verdict and requires a
new audit.

## 13. Correction Freeze append-only final release relock

Added: **2026-08-15 (Asia/Shanghai)**  
Mode: **independent ARS final release, integrity, reproducibility, package,
source-exclusion, and prerequisite-report relock**  
Candidate: **CORRECTION FREEZE**

This section is append-only. Immediately before it was added, the complete
historical release audit above was exactly **16,229 bytes** with SHA-256
`53403b3ea8c44f30b6941653e2809432ad0e6b99f5cf983f0d929aa9d5c2760d`.
Those bytes remain verbatim as this file's prefix. No historical statement,
hash, finding, or verdict was silently rewritten.

### 13.1 Retired old tuple and closed historical Minor

The old Review Freeze 2 release tuple is retired. It bound a bibliography
whose Stacks Project Tag `0B1W` record displayed the false title
“Topological colimits,” and it bound peer and citation reports that missed
that error. Therefore the honest historical release-candidate ledger was
**C0/M0/m1**, not the C0/M0/m0 asserted in the prefix.

For current-lock purposes this addendum supersedes the header disposition,
the tuple and prerequisite-report hashes in Section 1, the old
bibliographic-metadata conclusion in Section 5, the old report binding in
Section 11, and the old-tuple disposition in Section 12. The prefix remains
an intact historical record; supersession does not erase the missed Minor
or retroactively make the false title acceptable.

The corrected BibTeX and rendered reference [11] now use the official title
**“Colimits of spaces.”** The corrected citation and peer relocks explicitly
acknowledge the old Minor and independently close it. The corrected
candidate's current open-finding ledger is **C0/M0/m0**.

### 13.2 Corrected exact release binding

Every corrected candidate and prerequisite-report hash was recomputed from
the workspace and matched:

| Artifact | Corrected SHA-256 | Relock result |
|---|---|---|
| Paper-12 root `README.md` | `3f30055125e5f6593b4f8806c75ab3349675112e574f69e7238d9f7bd2ef9428` | exact |
| `paper/README.md` | `18eea91a1ed775cc03a14614af4662e3967be3aec66dd6bd58fc09819932db25` | exact |
| `paper/manuscript.tex` | `c6ad0f8c22d68840198d744a615da06e8b062d5ccdbeedb7f4ee76bf35073163` | exact; unchanged |
| `paper/references.bib` | `b763e9c07e3265d878bfc8b4caf44fb6c92ef12e7fac59b8af0bdeb703876175` | exact; corrected title |
| `paper/figures/same_carrier_diagonal.tex` | `a83148600d497dd1b91510f5707a1b1a9402c35689013a1fa904978206ff5cf1` | exact; unchanged |
| `paper/figures/packet_four_way_firewall.tex` | `9a52c273e91878d4dd74f96bd27fe299be39d98cdbebdda6bc800d89184b6908` | exact; unchanged |
| retained `paper/paper.pdf` | `9d6747e9f33c6ab3724beb35daedbb0efaff73691ed344374366f2392541ec15` | exact; 18 pages |
| retained `pdftotext -layout` output | `38adf39f29ac54af206f5c23537025f81a2b00fae1bed294bc4098a257fc10d4` | exact |
| `notes/citation_audit.md` | `79089b2487b6b21c10c1f10a4918fb29602d265877483d7a325634d15ec70a3a` | exact; Correction Freeze PASS |
| `notes/peer_review_round1.md` | `f3eaef077677144470e3f0417cb418009f0d340a8cd2856ac6cff74cf337438a` | exact; Correction Freeze ACCEPT/PASS |

The exact transition from the retired tuple is:

| Artifact | Retired hash | Corrected hash | Change class |
|---|---|---|---|
| Paper-12 root `README.md` | `a156deefbb059d840f73bfd6d76d468300158ad0e8c8bffef81b7a355c2cec51` | `3f30055125e5f6593b4f8806c75ab3349675112e574f69e7238d9f7bd2ef9428` | correction receipt/history |
| `paper/README.md` | `149bb1c9177f629fd5e04defa48ce17716cad85ea9d51dd0a8135e79b2214a7f` | `18eea91a1ed775cc03a14614af4662e3967be3aec66dd6bd58fc09819932db25` | correction receipt/history |
| manuscript | `c6ad0f8c22d68840198d744a615da06e8b062d5ccdbeedb7f4ee76bf35073163` | same | no byte change |
| bibliography | `e1f4d0f6589ce0710173bad1c0089b5d6746d09010cc448d6d387ad8c9e17dcf` | `b763e9c07e3265d878bfc8b4caf44fb6c92ef12e7fac59b8af0bdeb703876175` | one title line |
| both native figures | tuple hashes above | same | no byte change |
| retained PDF | `3fda5ae01fd3b7a78ddbefb11a62befa4d2ab50906b112b39e3c48e89901a294` | `9d6747e9f33c6ab3724beb35daedbb0efaff73691ed344374366f2392541ec15` | rebuilt reference [11] |
| layout extraction | `8f9715f37f1a6d87d71855cdfb3656e2c5102f69fb2b184c24d15c76119d22d9` | `38adf39f29ac54af206f5c23537025f81a2b00fae1bed294bc4098a257fc10d4` | corrected title plus harmless final-page whitespace |
| citation report | `f599dfbf67026b0985ee0e09b4e41bb24e3fe94709a1cd5e03ba657fb2a4fcaf` | `79089b2487b6b21c10c1f10a4918fb29602d265877483d7a325634d15ec70a3a` | append-only correction/relock |
| peer report | `e1f1558e170831457685a4a5c8c4d77f061b405d6c499867b6ce4f91bea6dc2b` | `f3eaef077677144470e3f0417cb418009f0d340a8cd2856ac6cff74cf337438a` | append-only correction/relock |

The manuscript and both native figures remain byte-identical. The corrected
candidate content delta is the Stacks title line in the bibliography and
its rendered reference; the README and audit changes are transparent
receipt/history updates. No proof, mathematical claim, owner boundary,
control, Route record, lock, pipeline state, or source manifestation changed.

### 13.3 Prerequisite citation and peer PASS binding

The corrected citation addendum was read in full. It preserves the old
34,843-byte citation report as an exact prefix, independently verifies all
14 records and the 27-command/31-occurrence/14-key citation graph, closes the
Stacks title Minor, rechecks retained manifestations and claim ceilings, and
returns **PASS — CORRECTION FREEZE CITATION/SOURCE-INTEGRITY RELOCK** with
current C0/M0/m0. Its later checksum-transcription correction gives the
actual Farsi--Huang--Kumjian--Packer sidecar hash without changing evidence
bytes. The controlling full-file hash is
`79089b2487b6b21c10c1f10a4918fb29602d265877483d7a325634d15ec70a3a`.

The corrected peer addendum was also read in full. It preserves the old
34,758-byte peer report as an exact prefix, independently repeats the
mathematics, owner, domain, standalone, Route, controls, citation, trace,
build, PDF, visual, and package/source-boundary reviews, explicitly records
the historical m1, and returns **ACCEPT / CORRECTION FREEZE exact-lock PASS
— C0/M0/m0, confidence 5/5**. Its controlling full-file hash is
`f3eaef077677144470e3f0417cb418009f0d340a8cd2856ac6cff74cf337438a`.

These corrected reports agree on the exact tuple in Section 13.2 and on the
external release hold. This final release relock does not silently inherit
their old verdicts or bind either historical report hash as current.

### 13.4 Existing independent build and visual receipts

This release lane did **not** run a third manuscript build or page-rendering
pass. It read and re-hashed the two already-completed independent corrected-
candidate receipts:

- the citation relock's five-stage build produced fresh PDF
  `63e44de891a32706b03ac4f23670d9b0eb4c040d368f59d201a3a911797ba497`,
  exact retained/fresh layout and normal-flow text equality, and 18/18
  byte-identical retained/fresh 144-dpi page pairs;
- the peer relock's separate five-stage build produced fresh PDF
  `54d7a381edae3136da0eb175eb6f199a7fac014d9f5caab664197f2d309e7639`,
  the same exact layout and normal-flow text equality, and 18/18
  byte-identical retained/fresh 160-dpi page pairs; and
- both receipts give layout
  `38adf39f29ac54af206f5c23537025f81a2b00fae1bed294bc4098a257fc10d4`
  and normal-flow text
  `e25b4c50dab8272241cc6c7953302082d2f57885e9aa43f3c6927435e27fa7ef`.

Both final logs are clean apart from the standard
`unicode-math`/`mathtools` ownership notices. Both visual passes inspect all
18 pages; both find no clipping, collision, float escape, broken glyph, or
blank artifact. Page 18 was inspected at original raster resolution and
visibly reads “Colimits of spaces,” Tag `0B1W`, with the official URL.

The retained PDF currently re-hashes to the Section 13.2 value. It remains
18-page A4, unencrypted, with zero embedded files and zero raster images;
all eight fonts are embedded, subsetted, and Unicode mapped. The build and
visual receipts therefore cover the corrected bytes without manufacturing
binary identity between independently generated PDF containers.

### 13.5 Six-file package and retained-source boundary

Fresh read-only enumeration finds exactly six regular files under `paper/`:
the manuscript, bibliography, two native figure sources, README, and
generated `paper.pdf`. There is exactly one PDF in that package, no symlink,
and no build auxiliary, `manuscript.pdf`, cache, or bytecode residue.

The full Paper-12 tree has exactly six PDFs: the generated manuscript and
five internal verification sources under `notes/sources/`. Running
`sha256sum -c coh-sources.sha256` in that directory again returned 10/10 OK
for the five PDFs and five preflight sidecars. The ledger and source
manifest remain respectively
`4a64a9de52d6f2b0b192778afc19b183929818aea3698f3afb9043fab12c20a4`
and
`77adde8e38853b4623212eaf60aee68f5c0d76112d859c643c061fb5b2fddb22`.
The local `.gitignore` remains exactly `*.pdf` plus
`!*.preflight.json`, at
`87edb0df613805bc3ea528a3f3c13f7cca93498cc92a48a4612c66fc4a0ac465`.

The generated PDF has no attachment. Direct extracted-text and binary-string
screens found no retained-source path, basename, checksum, preflight name,
local absolute path, `.tex`/`.bib` filename, or active-content token. No
research-source PDF is inside the candidate package.

Git metadata is absent from this workspace snapshot and this lane did not
run Git. Therefore index, staged-delta, repository-tree, archive, upload,
attachment-set, hidden-path, remote-sync, and fresh-clone exclusion remain
external checks rather than claims made by this report.

### 13.6 Controls and write boundary

Controls were **not rerun**. The correction is outside the controls package;
the unchanged manifest still re-hashes to
`7cbce9303393fcd755dda785312e26165656301e5dfbcab53b611e71c6204e95`.
Its 122-test, 11-CSV/3,486-row, and 14-negative receipt remains bound through
the corrected peer review's read-only integrity check and the historical
serialized reproduction. No duplicate control execution is claimed.

This release relock edited no candidate, citation, peer, control, result,
Route, lock, pipeline, Git, source-manifestation, or source-PDF byte. Its
only write is this append-only section of `notes/release_audit.md`.

### 13.7 Final Correction Freeze disposition

| Severity | Retired old tuple | Current corrected tuple |
|---|---:|---:|
| Critical | 0 | **0** |
| Major | 0 | **0** |
| Minor | 1 missed source-title error | **0** |

**PASS — CORRECTION FREEZE final release-candidate exact lock; C0/M0/m0.**

```text
RELEASE_CANDIDATE_INTEGRITY=PASS
CURRENT_CANDIDATE_DEFECT_COUNT=0
PUBLIC_RELEASE_AUTHORIZED=false
PUBLIC_RELEASE_HOLD=human declarations + immutable companion identity or self-contained replacement + real Git/publication-system exclusion + venue/submission confirmation
```

The external holds in Section 11 remain unchanged: human declarations,
venue and submission-policy confirmation, immutable public companion
identities or self-contained replacement premises, human release-byte and
archive authorization, real publication-system source-PDF exclusion, and a
submission-day source/policy refresh. They do not downgrade the corrected
technical candidate PASS, but none may be inferred as complete.

Any later change to a bound candidate, citation, or peer artifact invalidates
this tuple-specific release verdict and requires a new audit.

## 14. Append-only status and bilingual-count release relock

Added: **2026-08-15 (Asia/Shanghai)**  
Mode: **terminal receipt-only status/count release relock**

This section preserves the complete preceding release report byte for byte.
Immediately before this append, that prefix was exactly **27,739 bytes / 520
lines**, with SHA-256
`53afb3642812e981d0bb38b7166982c8818b7ef7085d96277dddd8f632d8d99b`.
It remains an immutable historical pre-status technical receipt. This lane
changed no candidate, README, citation, peer, proof, source, control, result,
Route, lock, pipeline-state, Git, or public-system byte. Its only write is
this append to `notes/release_audit.md`; it ran no build, control suite, Git
command, or public synchronization.

### 14.1 Current exact terminal binding

Every current identity below was recomputed directly before the append:

| Artifact | Current SHA-256 | Binding result |
|---|---|---|
| Paper-12 project `README.md` | `0026d84cf0a342f1da097dc8212cca7b80a532bc1d1f8cdcf2b40317967ebb20` | exact; 6,182 bytes / 124 lines |
| `paper/README.md` | `f8d7228452fc389e0b26b0de1314f77a270dd7b39ee00590851f2154c2ccfb91` | exact; 13,852 bytes / 202 lines |
| `paper/manuscript.tex` | `c6ad0f8c22d68840198d744a615da06e8b062d5ccdbeedb7f4ee76bf35073163` | exact; unchanged |
| `paper/references.bib` | `b763e9c07e3265d878bfc8b4caf44fb6c92ef12e7fac59b8af0bdeb703876175` | exact; unchanged |
| `paper/figures/same_carrier_diagonal.tex` | `a83148600d497dd1b91510f5707a1b1a9402c35689013a1fa904978206ff5cf1` | exact; unchanged |
| `paper/figures/packet_four_way_firewall.tex` | `9a52c273e91878d4dd74f96bd27fe299be39d98cdbebdda6bc800d89184b6908` | exact; unchanged |
| retained `paper/paper.pdf` | `9d6747e9f33c6ab3724beb35daedbb0efaff73691ed344374366f2392541ec15` | exact; unchanged 18-page PDF |
| `notes/citation_audit.md` | `19772ee4e6a779aea17924714f0f00bf4fff9f481255fb35b60c5b61edeaa6bf` | exact; status/count PASS C0/M0/m0 |
| `notes/peer_review_round1.md` | `72307244d55a403cb4913fa08f72bb418d039b4a2109718870391dec9e14dbb0` | exact; status/count ACCEPT/PASS C0/M0/m0 |

The citation report preserves its exact 56,028-byte / 823-line prefix at
`79089b2487b6b21c10c1f10a4918fb29602d265877483d7a325634d15ec70a3a`.
The peer report preserves its exact 50,887-byte / 821-line prefix at
`f3eaef077677144470e3f0417cb418009f0d340a8cd2856ac6cff74cf337438a`.
The enlarged reports explicitly bind the current README bytes, the unchanged
scholarly tuple, the corrected count convention, and the continuing external
release hold. Their dependency direction is acyclic: citation binds the
READMEs, peer binds citation, and this terminal release append binds both;
none embeds this enlarged release report's as-yet-unavailable self-hash.

The status-only README delta is also fully reversible. Two guarded
current-to-predecessor substitutions reconstruct the project README at 5,693
bytes / 115 lines and SHA-256
`3f30055125e5f6593b4f8806c75ab3349675112e574f69e7238d9f7bd2ef9428`.
Two corresponding substitutions reconstruct the package README at 13,199
bytes / 192 lines and SHA-256
`18eea91a1ed775cc03a14614af4662e3967be3aec66dd6bd58fc09819932db25`.
Those predecessor hashes remain historical receipts, not current status.

### 14.2 Superseded 370-count/status receipt

The prefix's status and bilingual-count statements are superseded only for
the current lock. The old **370** value came from the wider
`Script_Extensions=Han` property, which counts 17 Chinese-context punctuation
code points along with the prose characters. Under the now-explicit
`Script=Han` code-point convention, the unchanged manuscript has **353** Han
code points in the Chinese prose body at line 150. Removing the
`中文关键词：` label and TeX wrapper from line 153 gives **32** Han code
points in the six keyword values, so the separately named combined total is
**385**.

The enlarged citation and peer reports reproduce these counts independently
and record the old metric/status receipt as one resolved historical **Minor
(m1)**. Both 353 and 385 satisfy the required 300--500 interval. The English
205-word result, twelve-slot bilingual fact order and parity, manuscript
content, rendering, bibliography, citation graph, claim ceilings, trace,
Route receipt, controls receipt, and package/source boundary are unchanged.
Thus the correction changes neither a scholarly claim nor any technical
release result.

### 14.3 No-rebuild inheritance and final disposition

Because the manuscript, bibliography, both native figures, and retained PDF
are unchanged, no third build, raster pass, control run, or source download
was necessary. The two independent corrected-candidate build/visual receipts
and the full technical checks in Sections 13.3--13.6 remain applicable:
closed 14-record citation graph, clean five-stage builds, retained/fresh text
and raster equality, complete 18-page visual inspection, embedded/subsetted/
Unicode-mapped fonts, zero attachments, six-file package, five-source
checksum ledger, eight Route-A and zero Route-B records, and the frozen
122/122-control receipt. This append claims no new execution of those gates.

| Severity | Historical status/count receipt | Current bound tuple |
|---|---:|---:|
| Critical | 0 | **0** |
| Major | 0 | **0** |
| Minor | 1 receipt/metric-status defect | **0** |

**PASS — STATUS/COUNT FINAL RELEASE EXACT LOCK; C0/M0/m0.**

```text
RELEASE_CANDIDATE_INTEGRITY=PASS
CURRENT_CANDIDATE_DEFECT_COUNT=0
PUBLIC_RELEASE_AUTHORIZED=false
PUBLIC_RELEASE_HOLD=human declarations + immutable companion identity or self-contained replacement + venue/submission-day confirmation + real Git/archive/upload/fresh-clone source-PDF exclusion + explicit human release authorization
```

The status/count Minor is closed for the exact current bindings above, but
the external conditions are not. No journal acceptance, Git synchronization,
archive/upload check, source-PDF-exclusion check in a real release system, or
human authorization is inferred. This enlarged report deliberately cannot
self-record its own full-file digest; that digest belongs in a downstream
batch receipt without a reverse hash edge here.
