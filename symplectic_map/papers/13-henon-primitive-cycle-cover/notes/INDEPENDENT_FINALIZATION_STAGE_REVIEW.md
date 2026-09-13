# Independent Finalization-Stage Gate Review

## Review identity and authority boundary

- Candidate: `henon_primitive_cycle_cover_v1`
- Review date: 2026-08-16 UTC
- Review role: fresh independent finalization-stage gate reviewer
- Project read authority: the exact 34-file gate allowlist in the frozen lock
- Metadata-only checks: the five exact future/error paths authorized for this role
- Sole project write: this review file
- Compilation, scientific recomputation, R100 invocation, network access, upload,
  messaging, release, and submission: none

I did not author the finalization scope or finalization lock and did not act as
the release-manifest author or terminal integrity reviewer. I read no project
content outside the gate allowlist. In particular, I did not read source-lock,
code, preexecution, refine-log, runtime, raw-result, web, external-metadata, or
other-paper content. Before this passing review was written, the audit was
strictly zero-write.

## Bound author outputs

The two author outputs were rehashed both during the audit and immediately
before this sole write:

| Path | SHA-256 | Bytes | Lines | Result |
|---|---|---:|---:|---|
| `notes/FINALIZATION_STAGE_SCOPE.md` | `db940ce493818deabe1501e40e686e1f093ecdff9541c074b8a29d3522bdaf29` | 13,847 | 123 | exact |
| `experiments/finalization_lock.json` | `c8111706009d8f6fb393e1de21353216fb29fb545d03db6965413cb24c74750d` | 19,124 | 1 | exact |

The lock has schema `P13_FINALIZATION_STAGE_LOCK_V1`, candidate
`henon_primitive_cycle_cover_v1`, and state
`FINALIZATION_STAGE_LOCKED / PENDING_INDEPENDENT_FINALIZATION_REVIEW /
NO_RELEASE`. Its binding to the scope is exact. Its own final hash is absent
from its bytes, consistently with `self_hash_excluded=true`.

## Strict JSON and frozen-input audit

I independently parsed every JSON object in the 34-file gate read-set with
duplicate-key rejection, nonfinite-number rejection, strict UTF-8 validation,
and recursive key-order canonicalization. All seven JSON objects are sorted,
compact, newline-terminated, one-line canonical JSON:

1. `experiments/finalization_lock.json`
2. `experiments/manuscript_lock.json`
3. `experiments/publication_lock.json`
4. `paper/BUILD_RECEIPT_R0.json`
5. `paper/BUILD_RECEIPT_R1.json`
6. `paper/DRAFT_ARTIFACT_MANIFEST.json`
7. `results/INDEPENDENT_RESULT_REVIEW.json`

The frozen-input array contains exactly 32 entries. Its paths are safe,
lexicographically sorted, unique, project-relative, and free of empty, dot, or
parent components. Every entry is a regular non-symlink file with no symlink
component. All 32 byte counts and SHA-256 bindings match. The 32-row table in
the scope is itself sorted and is exactly equal to the lock's path/hash/size
set.

The prior publication lock's integrity-role allowlist is the same unique
31-path set obtained by removing the later independent draft-integrity review
from these 32 inputs. Thus the finalization lock adds exactly that review and
does not silently add a scientific, runtime, or unlisted source.

## Read, write, and role closure

The role sets close exactly as follows:

| Role | Exact project reads | Exact project write |
|---|---:|---|
| lock author | 32 frozen inputs, with only the two active author paths rereadable | scope and lock only |
| gate reviewer | 32 frozen inputs plus scope and lock = 34 | this review only |
| release-manifest author | the 34 gate inputs plus this review = 35 | `paper/FINAL_RELEASE_MANIFEST.json` only |
| terminal reviewer | the 35 release-manifest inputs plus that manifest = 36 | `paper/reviews/final_integrity_review.md` only |

Every list is unique and closed; the three downstream read lists are
lexicographically sorted. The lock author is stopped and is not authorized to
act in either reviewer role. Unlisted writes and modification or deletion of
any existing artifact are false.

The gate has a single passing-verdict path and a single write path. Failure is
fail-closed and zero-write. A gate pass activates only authorship of the final
release manifest; it does not activate local release or terminal review. The
terminal review becomes eligible only after a valid canonical release
manifest.

`paper/reviews` is absent at this gate. Its creation is reserved exclusively
as the necessary parent of the terminal review, after which it must contain
exactly that one file and zero other entries. Neither this gate nor the
release-manifest author may create it.

## Review, revision, receipt, and PDF DAG

The frozen draft-integrity review is 11,960 bytes at SHA-256
`328f971a54a4cff6f1d45139f6409159157b5b2158890296c9b464487b9ebde3`.
Its canonical draft-integrity verdict occurs once and has effect
`ANONYMOUS_REVIEWED_DRAFT_INTEGRITY_ONLY_NOT_FINALIZATION_OR_SUBMISSION`.

The Round-2 manuscript review is 17,090 bytes at SHA-256
`10e7e5ef1ca92a348c70495bb9c631e02af055c27c017d219e46736d35a028fd`.
Its manuscript-review verdict occurs exactly once as the final nonempty line.
The manifest records exactly two review rounds and one bounded revision:
Round 1 requires bounded revision, the sole revision receipt records completion,
and Round 2 passes. All three review/revision bindings match.

The draft manifest is strict canonical JSON, 15,322 bytes at SHA-256
`a4ff87715f0849c039764be2bf5bce4880d2214551d02cc455c003edc860665e`.
Its 30 artifact entries equal the finalization frozen set after excluding the
manifest itself and the later draft-integrity review. Its self hash and byte
count are excluded. It records no compile, network read, R100 invocation, or
scientific recomputation during manifest creation.

The build-receipt bindings are exact:

- Round 0 receipt: SHA-256
  `1e05beda50a07fc120c40d4568aa54f9bf51b4c212682b3248a30efb78c38548`,
  with preserved Round-0 PDF SHA-256
  `f9bb3e4c08215e91d0baf3e278ee1802b88a1d77c8e08515b61b51fb5850118d`.
- Round 1 receipt: SHA-256
  `5480ab22ebc7c9676395f9309baae15aa406f73f0cfa3e4901f288fb3e94ca51`,
  with all current source and output bindings matching the frozen files.
- Both receipts are canonical, exclude their own hash and byte count, record
  two clean builds, use the prescribed four-command sequence and deterministic
  environment, and record no forbidden mode.

The three revised source hashes are exact:

- `paper/main.tex`:
  `f62f72ad129bc371d0e76d1daf48b0a2df82cf60d0d1e750d6c0f049047539ce`
- `paper/references.bib`:
  `005edd30410ffd8b9b9851e9008636aed9bcddba3195af550bd6daed0529a19b`
- `paper/figures/architecture.tex`:
  `eabb9c99296c39a3744a57aaa7484522d20175e42dc7577a6e658dc732fed9b9`

The existing `paper/main.pdf` is 519,969 bytes at SHA-256
`4f69c395ffc06c3d3282c09127a520385ff741428cea7083cb1a7618e347df09`
and is byte-identical to `paper/main_round1.pdf`. No source, auxiliary, log,
receipt, snapshot, or PDF was changed by this review.

As a read-only corroboration of the sealed record, the current PDF reports the
exact safe title, empty Author/Subject/Keywords fields, fixed pdfLaTeX/pdfTeX
tool identifiers, A4 format, 27 pages, 30 embedded fonts, and zero nonembedded
fonts. The frozen log has eight hyperref PDF-string warnings and zero undefined
references, undefined citations, missing glyphs, overfull boxes, or underfull
boxes. The BibTeX log has zero warnings and zero errors. These checks are
integrity corroboration only, not a substitute for the later terminal audit.

## Isolated-build and terminal-review protocol

Only the terminal reviewer may create the two required roots using exactly
`mktemp -d /tmp/p13-paper13-final-XXXXXXXX`. The contract requires two
independent, reviewer-owned, non-symlink direct children of `/tmp`, each empty
at creation. Each root admits exactly three rehashed source copies
(`main.tex`, `references.bib`, and `figures/architecture.tex`) and six derived
files (`main.aux`, `main.bbl`, `main.blg`, `main.log`, `main.out`, and
`main.pdf`), with zero unexpected entries.

Each build uses `TZ=UTC`, `SOURCE_DATE_EPOCH=1786838400`, and
`FORCE_SOURCE_DATE=1`, followed by exactly pdfLaTeX, BibTeX, pdfLaTeX, and
pdfLaTeX with the locked flags. `latexmk`, Biber, shell escape, networked
tooling, and every project-tree build write are forbidden. The two temporary
PDFs must be mutually byte-identical and equal to the two frozen Round-1 PDFs
at the hash and size above.

Cleanup is authorized only after exact path, parent, prefix, ownership,
non-symlink, and inventory revalidation. Absence must then be verified; unsafe
cleanup may not broaden its deletion target and instead requires exact retained
root disclosure. I did not create, build in, inspect, or delete a temporary
build root in this gate review.

## Release, identity, and theorem firewalls

The only eventual effect is `LOCAL_ANONYMOUS_RELEASE_ONLY` for the already
existing frozen `paper/main.pdf`. The lock grants no new PDF or release copy,
submission, upload, preprint or repository deposit, supplementary archive,
external announcement or message, author identity, affiliation, ORCID,
acknowledgment, funding disclosure, or other external distribution.

The release conjunction remains four-part: this gate, a valid canonical final
release manifest, the terminal integrity verdict, and terminal release
confirmation. Neither this review alone nor the future manifest alone has a
release effect.

The theorem/science firewall is closed: registered count remains one; R100 is
sealed, not rerunnable, and not invocable; machine proof authority is false;
scientific and theorem recomputation are false; runtime is not theorem input;
and build, PDF, receipt, manifest, and integrity evidence are never theorem
evidence. The sole theorem authority remains the proof package conjoined with
the source-lock pass.

## Future-path and zero-mutation audit

Immediately before this write, all four future paths were absent:

- this gate-review path;
- `paper/FINAL_RELEASE_MANIFEST.json`;
- `paper/reviews`;
- `paper/reviews/final_integrity_review.md`.

The mistaken workspace-root path `/root/autodl-tmp/symplectic_map/paper` also
remained absent. No sibling access was inferred from that metadata check.

All frozen inputs, the scope, and the lock passed their final pre-write rehash.
Accordingly, the gate may authorize only the next role-separated creation of
the canonical final release manifest under the frozen contract. It does not
authorize terminal review before that manifest, and it does not authorize any
release or external action.

FINALIZATION_STAGE_PASS
