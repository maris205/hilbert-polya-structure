# Paper 15 Finalization-Stage Scope and Local-Release Contract

## Authority, candidate, and present state

This document and `experiments/finalization_lock.json` are the complete
finalization-stage governance pair for Paper 15. The machine-readable lock is
controlling where prose and JSON could be read differently; this scope explains
the same closed contract for a human reviewer.

- Canonical project root:
  `/root/autodl-tmp/symplectic_map/papers/15-henon-quartic-trace-fibers`
- Safe public title: *Low-Period Trace Fibers of Quartic Generalized Hénon Maps*
- Governance date: 2026-08-17 UTC
- Current lifecycle:
  `FINALIZATION_STAGE_LOCKED_PENDING_INDEPENDENT_REVIEW`
- Current release effect: `NO_RELEASE`

Every earlier pass is provenance, not present authority. In particular,
`PUBLICATION_STAGE_PASS`, `R0_BUILD_PASS`, `MANUSCRIPT_R1_PASS`,
`R1_SOURCE_REVISION_NO_OP_PASS`, `R1_BUILD_PASS`, and
`MANUSCRIPT_R2_PASS` do not create `paper/main.pdf`, do not authorize a release
manifest, and do not release anything. Only the fresh gates defined below can
change the lifecycle. Submission, upload, public distribution, identity
disclosure, and external messaging remain false at every stage in this
contract.

## Exact pre-governance universe F27

Immediately before this pair was authored, the canonical root contained the
following path-sorted set of exactly 27 regular files. Each SHA-256 is over raw
file bytes. `LF bytes` counts byte value `0x0a`, including in PDFs; it is not a
claim that a PDF is line-oriented.

| ID | Project-relative path | Bytes | LF bytes | SHA-256 |
|---|---|---:|---:|---|
| F01 | `experiments/EXPERIMENT_PLAN.md` | 8,354 | 375 | `c30436a0389c88df8f51fe6e226347bfe108aa84b5032841ec0033ffa7a987fb` |
| F02 | `experiments/EXPERIMENT_TRACKER.md` | 2,955 | 71 | `d0e46a2c9a691c33e6f6e523f85367f00e8060c124044e2f011016c0a68f9efb` |
| F03 | `experiments/publication_lock.json` | 42,917 | 1 | `3de5a4c14af5846bcb05998303f8928c9f0500b28c720a961dd7a70b8088d063` |
| F04 | `experiments/source_lock.json` | 26,920 | 1 | `802fc883cde85cd6312e8a31e0728dc01b493c640c8918d9eacc497f44cac7be` |
| F05 | `notes/CITATION_VERIFICATION.md` | 13,630 | 339 | `d84f4b523a7fee3e8f5fa8f2c4c898dbf62e3fd9528154fdd991d82c150c3609` |
| F06 | `notes/CLAIMS_EVIDENCE_MATRIX.md` | 9,343 | 125 | `928f0923bbfddd9294508a427bfcbcbd259591cac4c136bd4effb15bd86ed109` |
| F07 | `notes/INDEPENDENT_MANUSCRIPT_REVIEW_R1.md` | 20,036 | 312 | `4421d852bf7a2491a9d5911e2ab46dd0558ed0e8e73899255fa5df34e024a407` |
| F08 | `notes/INDEPENDENT_MANUSCRIPT_REVIEW_R2.md` | 23,170 | 424 | `82c2c6151b627f738f126fa80c5825e924db7841f2da83a5ad017876814842b4` |
| F09 | `notes/INDEPENDENT_PAPER_PLAN_REVIEW.md` | 13,961 | 227 | `ce2f6ba64b971d26b2ed472d2417c018461632cb1d54d6db53004f25b2d435ac` |
| F10 | `notes/INDEPENDENT_PUBLICATION_STAGE_REVIEW.md` | 16,132 | 288 | `21aaf6cac736851a2ace894cc617e4d6b1367e292e4fe8eb8084c17685422abc` |
| F11 | `notes/INDEPENDENT_SOURCE_DESIGN_REVIEW.md` | 12,529 | 228 | `55789c4a7c62e4577b655399e7fe8247fe641381e50876d6ebad9bce1f0e8b6e` |
| F12 | `notes/INDEPENDENT_SOURCE_LOCK_REVIEW.md` | 12,014 | 211 | `39ef31d1dac337fe9856fd9d8f40f756b30730a683db43c1d9b7e183236c6f63` |
| F13 | `notes/NOVELTY_ASSESSMENT.md` | 9,878 | 251 | `c0b7a102d0d63dcb71d58bdbe460e59988fbf303a10f540a0221275fd34c5eb2` |
| F14 | `notes/PROOF_PACKAGE.md` | 29,436 | 1,347 | `f99d14bc18bd160e5d55e6254e4a2957dda40adbc2a680970506a6ecca5a42ed` |
| F15 | `notes/PUBLICATION_STAGE_SCOPE.md` | 31,395 | 600 | `23ec6c825aaccd157b20b018e7e77c014ce8f94a841996850b22f586d685ea31` |
| F16 | `notes/RESEARCH_QUESTION.md` | 8,641 | 293 | `a287da2bebfa89b02dd7a83d13129e442b51d5780ccbc01c90eca93ad169e082` |
| F17 | `paper/BUILD_RECEIPT_R0.json` | 24,931 | 1 | `171f9f185b6387c8dc828299f5b4465187209b4aea8242c39888096aa28e6c66` |
| F18 | `paper/BUILD_RECEIPT_R1.json` | 37,459 | 1 | `463fbd8fb25829629240240e8cff069ce9bba76bec5ea2494d7b27e5d9871a95` |
| F19 | `paper/PAPER_PLAN.md` | 45,894 | 739 | `1b70ec0c37d9d587aa56b97b175c6da2f44e114d9414bf31c9f70534dd209e08` |
| F20 | `paper/SOURCE_REVISION_RECEIPT_R1.json` | 6,718 | 1 | `75ea38cb4dbb6e2890a7ce789ef015acfad721b4dc05f027393a52dba20dfd71` |
| F21 | `paper/main.tex` | 90,370 | 1,988 | `faa8f60bc7c51c2310b2e48450599823386e8d339fc92feeaf43161d247210d5` |
| F22 | `paper/main_round0.pdf` | 459,764 | 2,594 | `278263a4b10e617ab18fddfb2457cccc5477e89e135341a958f379dad8f081ca` |
| F23 | `paper/main_round1.pdf` | 459,764 | 2,594 | `278263a4b10e617ab18fddfb2457cccc5477e89e135341a958f379dad8f081ca` |
| F24 | `paper/references.bib` | 2,235 | 72 | `f79dda3d93d77de0d36d69d5130d71d0c6ab847cdcb359a575a3ee5646cd08fa` |
| F25 | `refine-logs/FINAL_PROPOSAL.md` | 9,331 | 395 | `97daded29a79a1b19b828c4704187fa9c70bdac7448382a72b1df8c0f773ab21` |
| F26 | `refine-logs/INITIAL_PROPOSAL.md` | 4,842 | 178 | `043ca69894386ab5040099138780cc6801ba39ff0b088a2ba3f274ef263cb1a0` |
| F27 | `refine-logs/REVIEW_SUMMARY.md` | 7,112 | 202 | `ab479b99e6fbf1b8f66b719df01d8abfbc97da30a8feb1c0fb1b77bab16ac0bb` |

At that boundary, the only child directories were `experiments`, `notes`,
`paper`, and `refine-logs`; there were four child directories in total and no
symbolic links anywhere beneath the root. The six future paths named later in
this document were absent.

## Bound source-to-R2 dependency chain

The finalization review must replay the chain rather than infer it from the
last verdict.

1. F16, F14, F05, F06, F13, and F25--F27 establish the research question,
   proof package, citation audit, evidence boundary, novelty boundary, and
   refined proposal.
2. F11 independently accepted the source design. F04 is its canonical source
   lock, and F12 independently accepted that lock.
3. F19 is the accepted paper plan; F09 is the independent plan review.
4. F15 and F03 close the publication-stage prose and canonical lock. F10 ends
   with `PUBLICATION_STAGE_PASS` and activated only the manuscript-author
   stage described there.
5. F21 and F24 are the sole manuscript source and bibliography. F17 records
   `R0_BUILD_PASS` and binds F22. F07 ends with `MANUSCRIPT_R1_PASS`.
6. F20 records `R1_SOURCE_REVISION_NO_OP_PASS`: the only accepted R1 item was
   cosmetic sentence case for the Stacks title and the already-frozen source
   and bibliography needed no byte change.
7. F18 records `R1_BUILD_PASS` and binds F23. F22 and F23 are byte-identical.
   F08 independently reviewed the final chain and its last nonempty line is
   exactly `MANUSCRIPT_R2_PASS`.

The source identity is permanently F21, 90,370 bytes, SHA-256
`faa8f60bc7c51c2310b2e48450599823386e8d339fc92feeaf43161d247210d5`.
The bibliography identity is permanently F24, 2,235 bytes, SHA-256
`f79dda3d93d77de0d36d69d5130d71d0c6ab847cdcb359a575a3ee5646cd08fa`.
The accepted PDF identity is permanently 459,764 bytes, SHA-256
`278263a4b10e617ab18fddfb2457cccc5477e89e135341a958f379dad8f081ca`.
No finalization role may revise scientific content, prose, bibliography,
metadata, layout, or PDF bytes.

## Frozen theorem and evidence boundary

The manuscript's three dependent parts remain one indivisible result.

1. Part A is over an arbitrary algebraically closed characteristic-zero field.
   For the formal fixed-trace characteristic polynomial
   `C_f(T)=det(T-M_(p') on k[x]/(p-(1-a)*x))`, it proves
   `C_f'(1-a)=0`. A fixed trace multiset therefore leaves at most `d-1`
   Jacobian candidates and at most three in degree four. The pure trace map is
   not supplied the Jacobian.
2. Part B is only over `C` and only for the normalized single-factor space
   `H^1_4`. Its exact non-quasi-finite locus is
   `E={(a,p): a=1, p(x)=(x^2-L)^2, L in C}`. Along E, the formal lower traces
   are `Trace_1=0` with multiplicity 4 and `Trace_2=2` with multiplicity 12.
   The residual quotient is `E/mu_3=A^1` with coordinate `L^3`.
3. Part C is only over `C`. Formal pure traces through period three are
   quasi-finite on `H^1_4` and its finite residual quotient `M^1_4`; traces
   through period two are not. On the already-isolated E, the pointwise
   formal-period-three second moment is
   `-1296000-1572864*L^3`. After formal subtraction, the pointwise length is
   60 and division by three gives the cyclewise moment
   `-432000-524288*L^3`.

The formal-period degrees are exactly 4, 12, and 60 for periods one, two, and
three. Scheme-theoretic multiplicity is essential. Reduced periodic support
cannot substitute for the formal zero-cycles.

The following 14 exclusions remain binding:

1. The Jacobian is derived as a finite output candidate; it is not an input to
   the pure trace map.
2. Quasi-finiteness is not injectivity, global uniqueness, generic degree one,
   or an exact fiber count.
3. No exact map degree, generic degree, or branch divisor is claimed.
4. The theorem does not cover compositions, arbitrary loxodromic
   automorphisms, unnormalized spaces, or multifactored moduli.
5. Part A has the stated characteristic-zero base; Parts B and C remain over
   `C` only.
6. No positive-characteristic analogue is claimed.
7. Formal zero-cycles with scheme multiplicity cannot be replaced by reduced
   periodic points.
8. Cantat--Dujardin's general rigidity, unspecified cutoff, exceptional
   family, and lower-period blindness are prior work.
9. Classical residues, formal dynatomic methods, Friedland--Milnor normal
   forms, Sugiyama, Huguin, and fixed-point identities receive no novelty
   claim here.
10. The absorbed Paper 12 exceptional-curve classification, formal
    subtraction, coefficient ledgers, and period-three moment receive no new
    novelty credit.
11. No all-degree `P(d)=3` theorem, effective universal cutoff, or universal
    coefficient nonvanishing is claimed.
12. The period-three second power sum separates only E after the lower fiber
    is known; it is not a global classifier of `H^1_4`.
13. Code, CAS, computation, parameter scans, experiments, and numerical checks
    are not theorem evidence.
14. No absolute priority, first-result, newly discovered exceptional-family,
    or absence-of-unpublished-work claim is authorized.

The overlapping Paper 12 material is absorbed as frozen internal provenance,
not a black-box premise and not a parallel publication. Paper 15 is
self-contained and is the only possible external vehicle for the overlap.
This finalization stage performs no mathematics, CAS work, experiment,
simulation, numerical test, or scientific reinterpretation.

## Anonymous local-only firewall

The only potentially positive terminal effect is
`LOCAL_ANONYMOUS_RELEASE_ONLY`: an immutable local candidate at the canonical
project root. It never means submission or public release. Throughout all
stages below, each of these permissions is false:

- upload, preprint posting, public hosting, repository push, or publication;
- journal, conference, editor, referee, venue, or collaborator communication;
- DOI registration, submission packaging, archival deposit, or signing;
- author-name insertion, affiliation, email, ORCID, acknowledgments, funding,
  contribution statements, identity-bearing metadata, or deanonymization;
- camera-ready revision, source revision, bibliography revision, PDF rewrite,
  supplementary material, or release-scope expansion.

The safe title above is the only public-facing identity string authorized in
the local artifact. Anonymous manuscript text and blank author metadata must
remain exact.

## Exact staged universes and path-set proof

Let `F27` be exactly the 27 path-sorted entries F01--F27 above. Define four
pairwise disjoint increments:

- `D_G={notes/FINALIZATION_STAGE_SCOPE.md,
  experiments/finalization_lock.json}`;
- `D_P={notes/INDEPENDENT_FINALIZATION_STAGE_REVIEW.md}`;
- `D_R={paper/main.pdf, paper/FINAL_RELEASE_MANIFEST.json}`;
- `D_T={paper/reviews/final_integrity_review.md}`.

The exact staged universes are:

- `G29 = F27 union D_G`;
- `P30 = G29 union D_P`;
- `R32 = P30 union D_R`;
- `T33 = R32 union D_T`.

No increment path occurs in F27, and the four increments are mutually
disjoint. Therefore the cardinalities are respectively 27, 29, 30, 32, and
33. Conversely, membership in a stage is exhausted by its displayed union;
there is no implicit wildcard, directory expansion, cache, receipt, log, or
auxiliary file. This establishes the exact path sets, not merely lower bounds.

F27, G29, P30, and R32 each have exactly the four existing child directories
`experiments`, `notes`, `paper`, and `refine-logs`. T33 has exactly those four
plus `paper/reviews`, which may be created only as the parent of its one
terminal report. Every staged member is a regular file; every stage has zero
symbolic links.

At the governance-author stop, the root must be exactly G29: 29 regular files,
four child directories, zero symlinks. `D_P`, `D_R`, `D_T`, and the
`paper/reviews` directory must all be absent.

## Fresh independent finalization-stage gate

The sole project write permitted after a stable G29 stop is
`notes/INDEPENDENT_FINALIZATION_STAGE_REVIEW.md`. Its author must be fresh and
independent of all prior researchers, governance authors, manuscript authors,
builders, source reviewers, plan reviewers, publication reviewers, R1/R2
reviewers, and this governance-pair author. The reviewer cannot review an
artifact they authored and cannot delegate the review.

The reviewer's exact project read allowlist is G29. The exact project write
allowlist is the single review path. The reviewer may use local read-only
hashing and strict JSON validation but may not compile, create a temporary
build, access a network, install a package, rasterize a PDF, invoke CAS, rerun
science, or alter any G29 member.

Before passing, the reviewer must record all of these checks:

1. resolve the canonical root and reject path escape, wrong-root lookalikes,
   symlink components, nonregular members, and aliases;
2. recompute SHA-256, byte count, and LF-byte count for every F27 member;
3. bind this scope by its postwrite identity and strictly parse the companion
   lock, rejecting duplicate keys, nonfinite numbers, non-UTF-8 data,
   noncanonical key order, whitespace, or a terminal-newline error;
4. prove that the inventory is exactly G29, with 29 regular files, four child
   directories, and zero symlinks;
5. replay the full dependency DAG, every bound verdict, the no-op R1 revision,
   immutable source/bibliography identities, both receipts, and the byte-equal
   R0/R1 PDFs;
6. confirm the theorem, formal-cycle, limitation, citation, absorption,
   no-empirical-evidence, safe-title, anonymity, and local-only boundaries;
7. prove that all later role permissions are inactive and that their
   allowlists are exact and temporally closed; and
8. prove `paper/main.pdf`, `paper/FINAL_RELEASE_MANIFEST.json`,
   `paper/reviews`, the terminal review, and all stray build or release
   artifacts absent.

Only a review whose last nonempty line is exactly

`FINALIZATION_STAGE_PASS`

activates the release-manifest author. A missing review, a different final
line, a failed independence check, an extra path, or any identity/canonical
mismatch leaves `NO_RELEASE` and all later permissions false. A reviewer may
instead write one failure review at the same sole path; it must not contain the
pass token and creates no authority.

## Conditional release-copy and manifest author

After, and only after, an exact independent `FINALIZATION_STAGE_PASS`, one new
release author receives the exact project read allowlist P30. This author may
write exactly two project files, in this order:

1. `paper/main.pdf`;
2. `paper/FINAL_RELEASE_MANIFEST.json`.

The author may not create any other path or directory, compile, revise source,
modify or regenerate a PDF, normalize metadata, optimize, linearize,
rasterize, convert, encrypt, attach, sign, inspect through a network, or run
scientific/CAS work.

`paper/main.pdf` must be a raw byte-for-byte local copy of
`paper/main_round1.pdf`, not a render or reconstructed PDF. Its required
identity is 459,764 bytes and SHA-256
`278263a4b10e617ab18fddfb2457cccc5477e89e135341a958f379dad8f081ca`.
Before the manifest write, both byte comparison and SHA-256 must show
`paper/main_round0.pdf`, `paper/main_round1.pdf`, and `paper/main.pdf`
identical.

The manifest must be strict compact canonical UTF-8 JSON: object keys ordered
recursively by Unicode code point, array order significant, duplicate keys and
nonfinite numbers rejected, no insignificant whitespace, and exactly one
terminal LF. It must exclude its own SHA-256 and byte count. In exact
project-relative path order, it must bind by path, byte count, and SHA-256 all
30 artifacts in P30 plus `paper/main.pdf`: exactly 31 non-self artifact
records. It must additionally bind the safe title, complete DAG, theorem and
firewalls, immutable source and bibliography, three-way persistent PDF
identity, the finalization review identity/verdict, the exact R32 inventory,
and the complete terminal-review protocol below.

Its lifecycle string must be exactly
`LOCAL_ANONYMOUS_RELEASE_CANDIDATE_PENDING_FINAL_INTEGRITY_REVIEW`, and its
release effect must be false. Once the stable R32 stop is reached, the release
author has exhausted their authority and cannot rewrite either output.

## Fresh terminal integrity reviewer

The terminal reviewer activates only at a stable exact R32 stop. This reviewer
must be fresh and independent of every earlier researcher, author, builder,
reviewer, governance-pair author, finalization reviewer, and release author.
The exact project read allowlist is R32. The only project-file write is
`paper/reviews/final_integrity_review.md`; creation of `paper/reviews` is
permitted solely as that file's parent. No other project mutation is allowed.

### Exactly two isolated deterministic builds

The reviewer must create exactly two distinct temporary directories, each by
a secure mktemp-style operation using the literal template
`/tmp/p15-paper15-final-XXXXXXXX`. Each resolved path must match
`^/tmp/p15-paper15-final-[A-Za-z0-9]{8}$`, reside directly under `/tmp`, be
newly created for this review, be owned by the reviewer, be a real empty
directory rather than a symlink, and differ from the other path. An unresolved
template, a preexisting entry, an unapproved suffix, or a third build root is a
terminal failure.

Into each root, copy exact bytes of only F21 and F24, named `main.tex` and
`references.bib`. Their copied identities must equal the frozen source and
bibliography before the first command and again after the last command.

Each command runs with exactly this environment:

```text
FORCE_SOURCE_DATE=1
LANG=C
LC_ALL=C
SOURCE_DATE_EPOCH=1786924800
TZ=UTC
```

In each root, run exactly this ordered four-command sequence and no other
compilation command:

```text
/usr/bin/pdflatex -interaction=nonstopmode -halt-on-error -file-line-error -no-shell-escape main.tex
/usr/bin/bibtex main
/usr/bin/pdflatex -interaction=nonstopmode -halt-on-error -file-line-error -no-shell-escape main.tex
/usr/bin/pdflatex -interaction=nonstopmode -halt-on-error -file-line-error -no-shell-escape main.tex
```

All eight exits must be zero. The build executables are frozen as follows:

| Invocation | Resolved executable | Bytes | SHA-256 |
|---|---|---:|---|
| `/usr/bin/pdflatex` | `/usr/bin/pdftex` | 1,802,504 | `01a7ab54ebf2fd89865aa0743ae9eaeec37ba4be75ca7cd254631cba6fb76cf9` |
| `/usr/bin/bibtex` | `/usr/bin/bibtex.original` | 117,128 | `c9ecb71856a3e6a597fceaaa22d624efe9ba46506c90a6609149abf9f22ad18f` |

Their complete version strings must equal those bound in F17 and F18. No
separate version-transcript byte identity is invented by this scope.

The only entries allowed in either temporary root are `main.tex`,
`references.bib`, and the emitted subset of `main.aux`, `main.bbl`, `main.blg`,
`main.log`, `main.out`, `main.toc`, and `main.pdf`. Command transcripts may be
captured only in memory or read-only stdout orchestration outside the build
roots; no transcript file, helper script, cache, package, image, figure,
download, or external source may enter either root.

Network access, package installation, shell escape, CAS, scientific
computation, rasterization, screenshotting, PDF rendering, image extraction,
image conversion, and image writing are forbidden. PDF validation is limited
to read-only, stdout-producing structural, metadata, font, text, link,
attachment, form, JavaScript, destination, and image-list inspection.

### Frozen build and PDF identities

For each new build, concatenate merged stdout/stderr command bytes in command
order. The expected transcript identities are:

| Object | Bytes | SHA-256 |
|---|---:|---|
| command 1 | 19,633 | `ff6cae2e7700aa1083f5889db1583600370539c2c1f8175f2fbd60ea3b317020` |
| command 2 | 155 | `fd9a13dc2ce58e3d773115b95a63c6bc23e005f41b8676999cb6efad4baa0822` |
| command 3 | 8,193 | `822e9bd03510430062225bb67b3cf8d12800a5dc944262d8532fe5cd20d722f4` |
| command 4 | 6,689 | `727da208655e9e8556574022b150bb9833576204960867cb0a64416918b740ea` |
| combined transcript | 34,670 | `b8e2d413644ac4b53a74705539f677a4bdba64ca3ec18921a9e0ee5953b5f22b` |
| final `main.log` | 25,364 | `cd365cebb384cb4d6e9dac9e0dc6499baa2e230f2c8fc56fab601127ed179184` |
| final `main.bbl` | 1,785 | `95e34a27a06ba06d4c27e419f4381fb4811048ccd5d7925acddf9d4baa44cdb6` |

Commands 1 and 3 may contain only the already-classified clean-bootstrap
citation/reference/rerun diagnostics: exactly 147 warning lines in command 1
and 18 in command 3. Commands 2 and 4 have zero warning lines; every command
has zero error lines; the final log is warning-free. Any unclassified
diagnostic fails the gate.

The reviewer must establish one five-way byte identity among:

1. temporary build A `main.pdf`;
2. temporary build B `main.pdf`;
3. `paper/main_round0.pdf`;
4. `paper/main_round1.pdf`;
5. `paper/main.pdf`.

Every one must have the frozen 459,764-byte PDF identity above. The two new
BBLs, command transcripts, combined transcripts, and final logs must also be
pairwise identical and have their frozen identities.

### Source, canonical, inventory, anonymity, and security gates

Before writing a passing report, the terminal reviewer must also prove:

- every source, bibliography, receipt, review, scope, lock, release artifact,
  and DAG edge in R32 has its bound identity and role provenance;
- every JSON file in R32, especially `source_lock.json`,
  `publication_lock.json`, `finalization_lock.json`, all three receipts, and
  `FINAL_RELEASE_MANIFEST.json`, passes a duplicate-key/nonfinite-safe strict
  parse and exact canonical round trip under its applicable contract;
- the pre-report universe is exactly R32: 32 regular files, the four expected
  child directories, zero symlinks, and no unbound artifact;
- all 35 US-letter pages are nonempty; main content occupies pages 1--24,
  references begin on page 25, and appendices A--E begin on pages 26, 27, 28,
  32, and 33 respectively;
- the eight bibliography keys are exactly those bound in F18, all 101 labels
  are unique, all 129 references resolve, and the PDF text has no unresolved
  citation or `??` marker;
- all 22 fonts are embedded, subset, and Unicode-mapped;
- the PDF title is exactly the safe title; author, creator, producer, subject,
  keywords, creation/modification dates, and identity-bearing metadata are
  blank or absent as frozen; no trailer ID is present;
- there are zero images, embedded files, signatures, forms/widgets,
  JavaScript, launch actions, rich media, attachments, metadata streams,
  external source inputs, unresolved editorial markers, and shell-escape
  products; and
- no network, upload, submission, public release, venue communication,
  identity disclosure, or other external action occurred.

The canonical `pdftotext` stdout stream must remain 77,095 bytes with SHA-256
`1c7627aa629e7a2bc00c70e565fbd619eb88cef0b9c6fc39bf68654ec9b33e1c`.
Read-only validation executable identities must match F18; drift is a failure,
not permission to substitute or install tools.

### Safe cleanup of both temporary roots

Cleanup is required after success or failure. Before deletion, freeze both
validated absolute paths as literal values and repeat the exact-prefix,
eight-character suffix, ownership, directory, non-symlink, and distinctness
checks. A destructive target may never be a glob, recursive path, unresolved
variable, command substitution, symlink, path outside the two roots, `/tmp`
itself, the project root, or a parent directory.

For each validated root separately, inspect the complete entry set. If an
unlisted entry exists, fail and stop cleanup rather than deleting that entry.
For each of the following literal basenames, delete it only if it is a regular
file and never follow a symlink:

- `main.aux`
- `main.bbl`
- `main.blg`
- `main.log`
- `main.out`
- `main.pdf`
- `main.tex`
- `main.toc`
- `references.bib`

After proving those entries absent and the root empty, remove that exact empty
directory with nonrecursive `rmdir`. Both validated roots must be proved absent
before a passing project report is written.

### Terminal verdict and effect

A passing terminal report binds all 32 R32 inputs, both isolated builds, the
five-way PDF identity, canonical/source/DAG/inventory/anonymity/security
checks, cleanup, and the final T33 inventory. Its last two nonempty lines must
be exactly, consecutively and in this order:

```text
FINAL_INTEGRITY_PASS
RELEASE_CONFIRMED
```

Only that exact terminal form changes the effect to
`LOCAL_ANONYMOUS_RELEASE_ONLY`. It still does not authorize submission,
upload, public hosting, repository push, preprint posting, DOI registration,
venue communication, external messaging, or identity disclosure.

On any failure, the reviewer writes no pass report. They may stop without a
project write or use the sole report path for a failure report whose last
nonempty line is `FINAL_INTEGRITY_FAIL`; it must not contain
`RELEASE_CONFIRMED`. The release effect then remains false.

## Temporally closed role allowlists

| Role | Activation boundary | Exact project reads | Exact project writes |
|---|---|---|---|
| finalization-governance author | this task, exact F27 | F27 | `notes/FINALIZATION_STAGE_SCOPE.md`; `experiments/finalization_lock.json` |
| independent finalization reviewer | stable exact G29 | G29 | `notes/INDEPENDENT_FINALIZATION_STAGE_REVIEW.md` only |
| release-copy/manifest author | exact `FINALIZATION_STAGE_PASS`, stable P30 | P30 | `paper/main.pdf`, then `paper/FINAL_RELEASE_MANIFEST.json` only |
| fresh terminal integrity reviewer | stable exact R32 | R32 | `paper/reviews/final_integrity_review.md` only |

Activation never works retroactively. A role cannot expand, inherit, or
delegate its write authority; self-sign a gate; amend a reviewed input; or
read a later-stage project artifact. The terminal reviewer alone may compile,
and only inside the two validated temporary roots. Temporary build entries are
not project writes and do not enlarge R32 or T33.

## Wrong-root, stray-path, and failure closure

At each stage, resolve the canonical root and every parent component without
following a symlink. Reject `..`, absolute substitution for a project-relative
member, another paper's same-named path, a nonregular member, changed hard-link
content, a wrong count, or a directory not listed for that stage.

Before the finalization review, all of D_P, D_R, D_T and `paper/reviews` must
be absent. Before the release author, only D_P may have been added to G29.
Before the terminal reviewer, only D_R may have been added to P30. Before the
terminal report, D_T must be absent.

Every stage rejects project copies of `main.aux`, `main.bbl`, `main.blg`,
`main.log`, `main.out`, `main.toc`, command transcripts, temporary build
roots, helper scripts, caches, backups, archives, submission packages,
signatures, attachments, figures, images, data, result files, scientific code,
supplement directories, and all other unbound paths.

Any failed prerequisite, missing verdict, conflicting verdict, hash drift,
canonicalization failure, source change, extra file, extra directory, symlink,
wrong root, incomplete cleanup, or role-independence failure closes the
downstream gate. It never grants a repair write under this contract.

## Exhaustion and governance-author stop

After an exact terminal pass, all T33 artifacts are immutable. No further
source, bibliography, PDF, manifest, receipt, review, identity, camera-ready,
submission, upload, or release-expansion action derives authority from this
contract. Any action beyond local anonymous release requires a new external
governance decision.

The present governance author writes only this scope and
`experiments/finalization_lock.json`. After the companion lock binds this
scope, both files are rehashed, strict canonical form is verified, and exact
G29 inventory is proved, the author stops. This author does not compile, edit
source, copy `main.pdf`, create the manifest, write either independent review,
create `paper/reviews`, or generate any build artifact.
