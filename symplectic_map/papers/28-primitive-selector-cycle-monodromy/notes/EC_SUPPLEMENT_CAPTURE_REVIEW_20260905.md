# Paper28 EC supplement: independent pre-execution review

Date: 2026-09-05. Decision: `EC_SUPPLEMENT_CAPTURE_REVIEW_PASS`.

Scope: the exact supplement script and plan were read fully, together with the
current `BATCH_07_CONTEXT.md`. The user-confirmed action is one demonstrated EC
metric capture, within the unchanged original 2 GiB limit, without manuscript or
old control changes. This review approves only that bounded capture controller.

## Findings

- The target is exactly
  `/usr/share/texlive/texmf-dist/fonts/tfm/jknappen/ec/ecrm1095.tfm`.
  The budget is 4096 content bytes; admission additionally requires the supplied
  diagnostic size of 3584 bytes, a regular file, mode 0644 and root uid/gid.
  The reviewer did not independently access that host file or its metadata.
- The controller exclusively creates the new output directory. It writes and
  fsyncs intent, the bound independent review and an attempt record before host
  traversal/open. All physical target ancestors use directory descriptors with
  `O_NOFOLLOW`; the leaf is inspected without following links, admitted before
  opening, opened with `O_NOFOLLOW`, and checked again by descriptor metadata.
- The read loop requests only the admitted remaining count, never a speculative
  extra byte. Pre/post descriptor metadata is compared. A normal exception
  preserves the fresh root and already written artifacts and reports counted
  bytes without retry, deletion, alternate search or repair. In-memory buffers
  from an interrupted/failed read are not promised as saved failure artifacts.
- Script/plan bytes and SHA-256, and the actual manuscript trio bytes, SHA-256 and
  LF counts, match the accompanying JSON. The controller binds the review hash
  before capture and rechecks manuscript and control identities afterwards.
- There are no subprocesses, dependency enumeration, installs, network calls,
  font generation, source edits, old-build reads or successor builds in the
  capture script. The fresh outcome seals preceding outputs without self-hashing.
  The 4096-byte allowance does not enlarge the original budget; current BATCH
  records the existing CAPTURE2 content total as 314,923,719 bytes.

## Tests actually performed

The exact script compiled in memory using administrative Python with `-I -S -B`.
Its definitions were loaded without calling `main` or `run`. `open_target` was
then exercised with entirely in-memory replacements for open/stat/fstat/close:
one valid record was admitted; symlink, directory, FIFO, zero size, wrong size
below budget, over-budget size, negative size, wrong mode, wrong uid and wrong
gid were all rejected before the simulated leaf open. All simulated physical
opens also required `O_NOFOLLOW`, and ancestors required `O_DIRECTORY`.
Result: 11/11 cases passed. No real host target open/stat/read occurred.

## Review scope deviation

The initial discovery command was overbroad (`rg --files papers`) and
unintentionally enumerated paths in old build roots. This was immediately
reported to the main agent, and broad discovery stopped. No old artifact content
was read or modified; no host target was accessed. The path listing is not
evidence for this review and supplies no authority for subsequent old-root
access. Remaining checks used exact designated local files only.

## Boundary

No blocking controller defect was found for the confirmed one-file action.
Only the two new review files were authored. This is not evidence that capture
has run, that the completed capture has recording integrity, or that a build or
PDF passes. The main agent owns capture execution; any completed supplement
still needs the planned independent recording-integrity review.
