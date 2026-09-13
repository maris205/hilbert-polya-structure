# Finalization-Stage Scope

## Authority, candidate, and present lifecycle

This document governs a possible local anonymous release of Paper 14 after
the completed source, plan, publication, build, revision, and manuscript-review
chain. It is a governance artifact. It is not a source revision, build,
release, submission, upload, venue communication, or terminal integrity
review.

The candidate identifier is exactly:

**henon_four_step_torus_escape_v1**

The safe title is exactly:

**Four-Step Escape from Finite-Rank Tori for Monomial Henon Maps**

The governance date is 2026-08-17 UTC. Before an independent finalization
review returns the exact positive verdict specified below, the state is
exactly:

**FINALIZATION_STAGE_LOCKED / PENDING_INDEPENDENT_FINALIZATION_REVIEW / NO_FINALIZATION / NO_RELEASE**

This scope and experiments/finalization_lock.json are the current
finalization-stage authority. All earlier statuses remain immutable
provenance. No earlier pass verdict independently authorizes finalization,
release, submission, upload, identity disclosure, or venue communication.

## Exact 29-file pre-governance identity gate

Immediately before this scope was written, the Paper 14 project root
papers/14-henon-four-step-torus-escape contained exactly 29 regular files,
zero symbolic links, and the four directories experiments, notes, paper, and
refine-logs. Every file was re-read and rehashed. Define F29 to be exactly the
following path-sorted set.

| ID | Project-relative path | Bytes | SHA-256 |
|---|---|---:|---|
| F01 | experiments/EXPERIMENT_PLAN.md | 5,522 | 709b32fa83e7cf1502e57393e4b46daf33c83ccb88832a498e223d084eabbd95 |
| F02 | experiments/EXPERIMENT_TRACKER.md | 2,139 | da117759e1e6a95579fcae16f27c3c868bd67b6d0b8b5d98e936b456a9354a97 |
| F03 | experiments/publication_lock.json | 23,141 | b8719f81f32fd33a54d419cf89d7165a871c19e6751e1b5287d613dbf708dc18 |
| F04 | experiments/source_lock.json | 10,716 | f2077d20262f6a068da58a2227c405573dd34fa8b844461b3d057da94e9eaa0c |
| F05 | notes/CITATION_VERIFICATION.md | 12,919 | 0c9b08f566eedb1e9f344f6fb07dfcf0c87015daa566435d0c989ac722d4e2af |
| F06 | notes/CLAIMS_EVIDENCE_MATRIX.md | 5,902 | d1887968e8626c1a8e30c9cb1675a13277c76662ca0fee8834ea024123650f6e |
| F07 | notes/INDEPENDENT_CITATION_PRECISION_AUDIT.md | 21,470 | 7e625c593267545088320459b65e990fdea5e347ed779416a6ce334d5a131f17 |
| F08 | notes/INDEPENDENT_MANUSCRIPT_REVIEW_R1.md | 18,211 | f24d481c9ad58d606f1da250198892058c5683245cbef64d221c49541e7e91f5 |
| F09 | notes/INDEPENDENT_MANUSCRIPT_REVIEW_R2.md | 24,046 | 03499cc92c6a5a6b7010f75ba5fd879082dcd4abb61709722fab081bc709fe1b |
| F10 | notes/INDEPENDENT_PAPER_PLAN_REVIEW.md | 7,992 | 0d1bbb1104e2f709312e1cfe0b3c449eb3bd706654c58f87eaf5b621a3ea5596 |
| F11 | notes/INDEPENDENT_PUBLICATION_STAGE_REVIEW.md | 14,371 | 81444cb4d89c4797352b3f4558f4d64dacf4cb733ee6014be5b0e9335243b0d4 |
| F12 | notes/INDEPENDENT_SOURCE_DESIGN_REVIEW.md | 18,618 | e3dc9864c72d150e0f7a69d08aad9f4e24f0dde1c6115fe3d428b129ade4573c |
| F13 | notes/INDEPENDENT_SOURCE_DESIGN_REVIEW_R2.md | 12,836 | 8bde838d4bd18426f291eb793f5c822fbd6d70d604fc7097c5761c02bb309ef0 |
| F14 | notes/INDEPENDENT_SOURCE_LOCK_REVIEW.md | 12,934 | ea6d13c1ec74bbad0ac8c6cd850d0f0b8c33992d05b5e428308eef3347a18308 |
| F15 | notes/NOVELTY_ASSESSMENT.md | 8,660 | 2fafbef234a7e7cc8fbe10b25e0b920188b3c35472538fcbaf023da8d357bac1 |
| F16 | notes/PROOF_PACKAGE.md | 13,728 | c43d8377707e0ee69aa6447984b77c2b5ef6d1d79bc1d56c6b5ab72ea4c8f5aa |
| F17 | notes/PUBLICATION_STAGE_SCOPE.md | 23,830 | 156dff2466f42704fd6f1e65f6374d21a097adb98632d7a5125984caceb9d447 |
| F18 | notes/RESEARCH_QUESTION.md | 6,371 | 782b48dfec973d877bf87c964a3bdd7227b52a21101b68a9a576929441bedb9c |
| F19 | paper/BUILD_RECEIPT_R0.json | 21,053 | b377031ee9961dd506322d6bd721e0832663b4da44ac56c028bff403b8dbb529 |
| F20 | paper/BUILD_RECEIPT_R1.json | 28,315 | 37baf7a8e49e4b45c4ba41d19b62c9cfb2656d83a022114f63595b115daaae6e |
| F21 | paper/PAPER_PLAN.md | 30,112 | 6a0e16e3688714c43c9e9d87054c501d44989e59a523c6ff084eac4c9db3a88f |
| F22 | paper/SOURCE_REVISION_RECEIPT_R1.json | 11,437 | 0f8a9d0e9ca9aa7bb13b63016ab14148fd6a29c2a086d532c539e876abd9de1c |
| F23 | paper/main.tex | 47,961 | 415f1395f07153ccb158e69cb70051e95e719802d0a1c3315df88be7ccfab538 |
| F24 | paper/main_round0.pdf | 384,084 | 4e17ebdfec4aed386e57f0e5bb3b39a6f24ed6809db0fb379a598fe143041414 |
| F25 | paper/main_round1.pdf | 384,084 | 4e17ebdfec4aed386e57f0e5bb3b39a6f24ed6809db0fb379a598fe143041414 |
| F26 | paper/references.bib | 2,666 | 816fd8211b7c5ad91dc227ac71b90444cdf5c3b713b60dd9a70fbdd1a8d419bc |
| F27 | refine-logs/FINAL_PROPOSAL.md | 7,814 | 719214a159f1e36676d059c626dcefab7fe11b012e44146243db8aa500eb38a0 |
| F28 | refine-logs/INITIAL_PROPOSAL.md | 4,045 | ecb3a5151c75dba6ac4b8415d000f9a9a3c36ff80af5b651b9de7ecbad7a6e22 |
| F29 | refine-logs/REVIEW_SUMMARY.md | 6,383 | ac2a75bb0f393de1255958705bbcd2e75fa1e0800805d420f048cb0f72c5d54f |

The two PDF identities in F24 and F25 are equal byte for byte. No future
finalization artifact was present at this gate.

## Complete source-to-R2 dependency DAG

The finalization gate binds the complete provenance graph rather than only
its terminal PDF.

1. The source-design roots are F01, F02, F05--F07, F12, F13, F15, F16, F18,
   and F27--F29. They record the proof-only question, proof package, citation
   precision, novelty boundary, design reviews, and historical experiment
   governance with no scientific execution.
2. F04 is the canonical source lock. It binds the exact theorem, proof
   dependencies, citation boundaries, source-design roots, and upstream batch
   provenance. F14 independently returns SOURCE_LOCK_PASS.
3. F21 is the frozen proof-first paper plan derived from the passed source
   design. F10 independently returns PAPER_PLAN_PASS.
4. F17 and F03 are the human-readable and canonical publication-stage
   governance pair. They bind the passed source and plan chain. F11
   independently returns PUBLICATION_STAGE_PASS.
5. F23 and F26 are the anonymous manuscript and verified bibliography
   produced under that pass. Their identities never change in the later DAG.
6. F19 binds F03, F04, F05--F07, F10--F18, F21, F23, F26, and F27 together
   with the exact Round-0 deterministic toolchain, environment, two clean
   runs, validations, and persisted PDF F24.
7. F08 independently reviews the Round-0 chain and returns
   MANUSCRIPT_R1_PASS with zero blockers and zero required repairs.
8. F22 binds F08 and identical pre/post identities for F23 and F26. It
   records change_count zero, an empty change list, accepted cosmetics with no
   action, and consumption of the only source-revision window.
9. F20 binds the prior chain, F22, the unchanged sources, the exact Round-1
   deterministic two-clean-build protocol, and persisted PDF F25.
10. F09 independently binds the exact twenty-three-path R2 read set, proves
    the source, receipt, toolchain, PDF, citation, anonymity, page, and
    theorem identities, and returns MANUSCRIPT_R2_PASS with no required
    repairs and no new defect.

The terminal source identities are therefore:

- paper/main.tex: 47,961 bytes,
  415f1395f07153ccb158e69cb70051e95e719802d0a1c3315df88be7ccfab538;
- paper/references.bib: 2,666 bytes,
  816fd8211b7c5ad91dc227ac71b90444cdf5c3b713b60dd9a70fbdd1a8d419bc;
- paper/main_round0.pdf and paper/main_round1.pdf: each 384,084 bytes,
  4e17ebdfec4aed386e57f0e5bb3b39a6f24ed6809db0fb379a598fe143041414.

No edge in this DAG authorizes another source revision or persistent build.

## Frozen theorem, evidence, and limitation boundary

Let \(K\) be an arbitrary field of characteristic zero, let \(d\ge2\), let
\(a,b,c\in K^\ast\), and let \(\Gamma\le K^\ast\) have finite rank \(r\).
Finite generation and coefficient membership are not assumed. For

\[
H(x,y)=(b x^d+a y+c,x)
\]

and

\[
T_m(H,\Gamma)=
\{P\in\Gamma^2:H^j(P)\in\Gamma^2\text{ for every }0\le j\le m\},
\]

the locked principal bound is

\[
\#T_4(H,\Gamma)
\le4d\exp\!\bigl(18^9(3r+1)\bigr)+81d^2.
\]

Here \(T_4\) contains five states and four transitions. The co-primary
sharpness statement is that, for every \(d\ge2\), a number-field example with
rank-one \(\Gamma\) has infinitely many points in \(T_3(H,\Gamma)\). The
subordinate periodic corollary bounds
\(\sum_{n\ge1}nC_n^\Gamma(H)\) only for exact-period orbits wholly contained
in \(\Gamma^2\).

The sole imported proof theorem remains Evertse--Schlickewei--Schmidt,
published Theorem 1.1. Its variable group is \(\Gamma^3\) of rank \(3r\);
\(1/c,-b/c,-a/c\) remain fixed coefficients. The \(A,B,C\) labels, all nine
forward transitions, the \(BA\) and \(CB\) free chains, exceptional \(CBA\)
closure, simultaneous-label cover, short-period argument, and \(81d^2\)
bound remain frozen.

All nine limitations and all citation-range boundaries remain those in F03,
F04, F05, F07, F09, F13, F15--F18, F21, and F27. There is no theorem
expansion, empirical evidence, computation, experiment, figure, dataset,
height bound, effective enumeration, general-polynomial extension, or
absolute priority claim.

## Anonymous local-only firewall

Every source and PDF remains anonymous. Visible authorship is exactly
Anonymous; PDF author metadata is empty. No name, affiliation, email,
acknowledgment, funding identity, repository identity, or identity-revealing
self-citation may be added.

This finalization stage can produce only a local anonymous release candidate
and, after a successful terminal review, a local anonymous release. It
never authorizes:

- source, bibliography, theorem, citation, or layout modification;
- a new persistent build or a camera-ready transformation;
- identity disclosure or de-anonymization;
- submission to a journal, conference, repository, or preprint server;
- upload, network transfer, publication, DOI registration, or public release;
- communication with a venue, editor, reviewer, or third party; or
- code, experiment, result, figure, supplementary, data, or promotional
  artifact creation.

All release-effect flags are false before the exact terminal pass described
below.

## Current and future exact path sets

The companion lock defines the following exact set increments.

- F29 is the path-sorted 29-file table above.
- G31 is F29 plus notes/FINALIZATION_STAGE_SCOPE.md and
  experiments/finalization_lock.json.
- P32 is G31 plus notes/INDEPENDENT_FINALIZATION_STAGE_REVIEW.md.
- R34 is P32 plus paper/main.pdf and paper/FINAL_RELEASE_MANIFEST.json.
- T35 is R34 plus paper/reviews/final_integrity_review.md.

These definitions are exact. No role may add a path, replace a path with a
symlink, follow a symlink, read a wrong-root lookalike, or widen a set by
directory traversal.

At the author stop for this governance stage, G31 must contain exactly 31
regular files and zero symbolic links. The paths added after G31 are absent.
The paper/reviews directory is also absent.

## Independent finalization-stage review gate

The sole next project write after this author stop is:

**notes/INDEPENDENT_FINALIZATION_STAGE_REVIEW.md**

The reviewer read allowlist is exactly G31. The reviewer write universe is
exactly the one path above. The reviewer must be fresh and independent of
every bound source-design author, source reviewer, plan author, plan reviewer,
publication-governance author and reviewer, manuscript drafter, Round-0
builder, Round-1 manuscript reviewer, bounded revision author, Round-1
builder, Round-2 manuscript reviewer, and this finalization-governance
author. The reviewer may not author or alter a bound input or any later
release artifact.

The reviewer must:

1. resolve the canonical Paper 14 root and reject any wrong-root or
   path-escape condition;
2. rehash every path in F29 and both governance artifacts;
3. prove the exact G31 inventory, regular-file type, and zero-symlink state;
4. strictly validate the finalization lock as canonical UTF-8 JSON with
   duplicate-key and nonfinite-number rejection, recursive Unicode-key
   ordering, no insignificant whitespace, and exactly one terminal LF;
5. replay the entire source-to-R2 DAG, all pass verdicts, source identities,
   source-revision exhaustion, two build receipts, and R0/R1 PDF equality;
6. replay the theorem, citation, limitation, zero-evidence, safe-title,
   anonymity, local-only, and no-submission firewalls;
7. verify that the release-author and terminal-review contracts below are
   closed before this gate and exact rather than self-expandable; and
8. confirm that paper/main.pdf, paper/FINAL_RELEASE_MANIFEST.json,
   paper/reviews, and every stray finalization or build artifact are absent.

Only the exact verdict

**FINALIZATION_STAGE_PASS**

activates the release-manifest author. A missing review, any other verdict,
any hash or inventory mismatch, a noncanonical lock, a reviewer independence
failure, or an unauthorized path leaves finalization and release false.

A failure review, if the reviewer elects to write one, remains at the sole
review path and must not contain FINALIZATION_STAGE_PASS. It grants no later
permission.

## Conditional release-manifest author

After and only after exact FINALIZATION_STAGE_PASS, one release-manifest
author receives the exact read allowlist P32. That author may write exactly:

1. paper/main.pdf;
2. paper/FINAL_RELEASE_MANIFEST.json.

No other path or directory creation is authorized. The author may not
compile, edit a source, edit a PDF, normalize PDF metadata, optimize,
linearize, rasterize, convert, sign, attach, encrypt, or contact a network.

paper/main.pdf must be a byte-exact local copy of paper/main_round1.pdf. It
must have exactly 384,084 bytes and SHA-256
4e17ebdfec4aed386e57f0e5bb3b39a6f24ed6809db0fb379a598fe143041414.
Before writing the manifest, the author must prove with both a byte comparison
and SHA-256 that paper/main.pdf, paper/main_round1.pdf, and
paper/main_round0.pdf are identical.

paper/FINAL_RELEASE_MANIFEST.json must be strict compact canonical UTF-8 JSON
with recursive Unicode-code-point key order, duplicate keys forbidden,
nonfinite numbers forbidden, no insignificant whitespace, and exactly one
terminal LF. Its own hash and byte count are excluded. It must bind, in
project-relative path order, every artifact in P32 and paper/main.pdf by
path, bytes, and SHA-256. It must also bind the safe title, source identities,
R0/R1 PDF equality, full DAG, finalization review verdict and identity,
local-only firewall, exact downstream terminal-review contract, and exact
postwrite 34-file/zero-symlink inventory.

The manifest state must be exactly:

**LOCAL_ANONYMOUS_RELEASE_CANDIDATE_PENDING_FINAL_INTEGRITY_REVIEW**

Its release effect is exactly false. Neither creation of main.pdf nor the
manifest confirms release. After a stable release-author stop, no release
author may make a second write or amend the manifest.

## Fresh terminal integrity reviewer

The terminal reviewer activates only after a stable release-author stop with
exact identities for paper/main.pdf and paper/FINAL_RELEASE_MANIFEST.json.
The reviewer must be fresh and independent of every earlier author, builder,
reviewer, the independent finalization reviewer, and the release-manifest
author.

The terminal reviewer read allowlist is exactly R34. The sole project file
write is:

**paper/reviews/final_integrity_review.md**

Creation of paper/reviews is authorized solely as the parent directory for
that file. No second file in that directory and no other project write is
authorized.

### Exact two-directory build protocol

The terminal reviewer must create exactly two distinct temporary directories
using the literal templates

- /tmp/p14-paper14-final-XXXXXXXX
- /tmp/p14-paper14-final-XXXXXXXX

with a secure mktemp-style operation that replaces all eight X characters.
Before copying any file, the reviewer must resolve each directory, prove that
it is a real directory rather than a symlink, prove that its resolved path
matches the prefix /tmp/p14-paper14-final- with exactly eight generated
suffix characters, prove that the two paths differ, and prove that each is
empty. A wrong prefix, unresolved variable, preexisting content, symlink, or
third temporary root is a terminal failure.

Into each directory, copy exact bytes of only paper/main.tex and
paper/references.bib, naming them main.tex and references.bib. The copies
must be byte-identical to F23 and F26. Use the exact environment on every
command:

    TZ=UTC
    LC_ALL=C
    LANG=C
    SOURCE_DATE_EPOCH=1786838400
    FORCE_SOURCE_DATE=1

The only compilation commands, in this exact order in each directory, are:

    /usr/bin/pdflatex -interaction=nonstopmode -halt-on-error -file-line-error -no-shell-escape main.tex
    /usr/bin/bibtex main
    /usr/bin/pdflatex -interaction=nonstopmode -halt-on-error -file-line-error -no-shell-escape main.tex
    /usr/bin/pdflatex -interaction=nonstopmode -halt-on-error -file-line-error -no-shell-escape main.tex

All eight process exit codes must be zero. The executable identities must
remain:

| Invocation | Resolved executable | Bytes | SHA-256 |
|---|---|---:|---|
| /usr/bin/pdflatex | /usr/bin/pdftex | 1,802,504 | 01a7ab54ebf2fd89865aa0743ae9eaeec37ba4be75ca7cd254631cba6fb76cf9 |
| /usr/bin/bibtex | /usr/bin/bibtex.original | 117,128 | c9ecb71856a3e6a597fceaaa22d624efe9ba46506c90a6609149abf9f22ad18f |

The pdflatex version transcript must remain 555 bytes with SHA-256
5ed4d12bfc8b37387ea53ec9537396e987ec3dd557bcc1a766c2e515bd6b15b0.
The bibtex version transcript must remain 383 bytes with SHA-256
622b6e09c4ef724829b6a0fda40776b10aa28deea4be1a788aa92ea1b3d27d90.

The allowed per-directory inventory is exactly the two source files plus the
emitted subset of main.aux, main.bbl, main.blg, main.log, main.out, main.toc,
and main.pdf. No transcript file, cache, downloaded package, figure, image,
shell-escape output, or third-party asset may be stored.

There is no network access, package installation, rasterization, screenshot,
image conversion, image extraction, or image write. PDF inspection must use
read-only stdout-producing metadata, font, text, attachment, signature,
destination, and image-list operations only.

### Terminal equality and integrity gates

Before any pass report, the reviewer must establish all of the following:

- both temporary main.pdf files are byte-identical to each other;
- both are byte-identical to paper/main.pdf, paper/main_round1.pdf, and
  paper/main_round0.pdf;
- both main.bbl files are byte-identical and have the locked 1,710-byte
  identity from the build receipts;
- all canonical JSON artifacts, including both finalization JSON files, pass
  strict duplicate/nonfinite-safe canonical round trips;
- every DAG edge and every bound path identity is exact;
- the pre-review inventory is exactly R34: 34 regular files, zero symlinks,
  no extra directory except the authorized existing project directories;
- all eight exits are zero, with zero LaTeX/BibTeX error, undefined reference,
  undefined citation, missing character, missing font, or overfull box;
- all 17 US-letter pages are nonempty, mathematical content reaches page 17,
  references begin on page 17, and the page envelope remains satisfied;
- all 21 fonts are embedded, subset, and Unicode-mapped;
- the title and subject metadata are exact and author metadata is empty;
- there is no image object, embedded file, signature, form, JavaScript,
  custom metadata, metadata stream, identity marker, unresolved marker,
  empirical asset, or external source input;
- the two accepted cosmetic diagnostics and no unclassified warning are the
  only diagnostics; and
- no upload, submission, venue communication, identity disclosure, or
  external release action occurred.

### Safe file-by-file cleanup

Cleanup is mandatory on success and failure. Before cleanup, freeze the two
validated absolute temporary paths as distinct literal values and repeat the
prefix, suffix-length, non-symlink, and ownership checks. Never use a glob,
recursive deletion, an unresolved environment variable, a command
substitution as a destructive target, or any path outside the two validated
roots.

For each validated root separately, remove only these explicit entries if
they are regular files and never follow a symlink:

- main.aux
- main.bbl
- main.blg
- main.log
- main.out
- main.pdf
- main.tex
- main.toc
- references.bib

Reject any unlisted entry instead of deleting it. After all listed files are
absent, remove the now-empty validated directory with a nonrecursive rmdir.
Prove both directories absent before writing a terminal pass report.

### Terminal pass and failure semantics

A passing review must bind the entire R34 chain, both temporary build
identities, all equality and integrity checks, exact safe cleanup, and the
postwrite T35 inventory. Its last two nonempty lines must be exactly, in this
order:

FINAL_INTEGRITY_PASS
RELEASE_CONFIRMED

Only that exact terminal form changes the effect to:

**LOCAL_ANONYMOUS_RELEASE_ONLY**

It does not authorize submission, upload, public hosting, repository push,
preprint posting, DOI registration, venue communication, or identity
disclosure.

On any failure, the reviewer must not write a pass report. The reviewer may
either stop without a project write or write a failure report at the sole
review path whose last nonempty line is FINAL_INTEGRITY_FAIL. A failure
report must not contain RELEASE_CONFIRMED. Release effect remains false.

## Role read/write closure

The exact role contracts are:

| Role | Activation | Read allowlist | Project write universe |
|---|---|---|---|
| finalization-governance author | this task only | F29 | notes/FINALIZATION_STAGE_SCOPE.md; experiments/finalization_lock.json |
| independent finalization reviewer | stable governance-author stop | G31 | notes/INDEPENDENT_FINALIZATION_STAGE_REVIEW.md only |
| release-manifest author | exact FINALIZATION_STAGE_PASS | P32 | paper/main.pdf; paper/FINAL_RELEASE_MANIFEST.json only |
| fresh terminal integrity reviewer | stable release-author stop | R34 | paper/reviews/final_integrity_review.md only |

No role may self-sign a gate, author an object it reviews, alter a bound
input, expand its own read or write universe, or delegate a write. The
terminal reviewer is the only role permitted to compile, and then only in
the two validated temporary roots. The temporary files are not project
writes.

## Wrong-root, stray-artifact, and inventory checks

At every gate, resolve the project root itself and require every
project-relative path to remain beneath that root with no symlink component.
Reject a same-named file under another paper, a path containing dot-dot, an
absolute replacement for a bound project path, a hard-linked replacement
with changed identity, a nonregular bound file, or any inventory count that
does not equal the applicable exact set.

Before the independent finalization review, these future paths must be
absent:

- notes/INDEPENDENT_FINALIZATION_STAGE_REVIEW.md
- paper/main.pdf
- paper/FINAL_RELEASE_MANIFEST.json
- paper/reviews
- paper/reviews/final_integrity_review.md

Before the release-manifest author, only the finalization review may have
been added to G31. Before the terminal reviewer, only main.pdf and the
manifest may have been added to P32.

At all stages reject project copies of main.aux, main.bbl, main.blg,
main.log, main.out, main.toc, compile logs, temporary build directories,
dash-named image artifacts, caches, source backups, release archives,
submission packages, signatures, attachments, or unbound files. No
scientific code, experiment, result, data, figure, or supplementary directory
may appear.

## Exhaustion after terminal review

After an exact terminal pass, the Paper 14 sources, bibliography, governance,
receipts, PDFs, manifest, and terminal review are immutable. No further source
revision, bibliography revision, persistent build, finalization pass,
manifest rewrite, PDF rewrite, terminal-review rewrite, camera-ready change,
identity change, release expansion, submission, or upload is authorized by
this scope.

Any future action beyond the local anonymous release would require a new
external-scope governance decision and cannot derive permission from
FINALIZATION_STAGE_PASS, FINAL_INTEGRITY_PASS, or RELEASE_CONFIRMED.

## Governance-author stop

The finalization-governance author may write only this scope and the canonical
companion lock. After both are written, canonicalized, rehashed, and the exact
31-file/zero-symlink inventory is proved, the author must stop. The author
must not write the independent review, main.pdf, the release manifest, the
terminal review, or any build artifact.
