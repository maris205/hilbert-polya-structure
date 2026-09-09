# C425 revised manuscript: second-pass handoff

2026-09-09 UTC. **AUTHOR STOP-WRITE — pending_round2.**
The sole coordinator-adopted P1 abstract correction is implemented.
This is an author revision receipt, not a second review or release gate.

- [Revised complete PDF](main.pdf): 12 pages, 378223 bytes.
- SHA-256: `e7330f65920c40c566b01ee0d864d9f5a023c70010954e8af633c325f92c1dcb`.
- [Improvement log](PAPER_IMPROVEMENT_LOG.md) and
  [machine-readable state](PAPER_IMPROVEMENT_STATE.json).
- [All thirteen revised input hashes](ROUND1_INPUT_MANIFEST.sha256),
  [complete source diff](ROUND1_SOURCE_DIFF.patch),
  [full raw round-1 review](ROUND1_REVIEW_RAW.md).
- Successful real build: `build_round1_01/`; its engine, bibliography,
  complete compile log, recorder and revised source snapshot are retained.
- Full 614-line PDF text and every one of twelve separately inspected
  page images are retained in that build directory. Final logs are clean;
  all 23 Type 1 font resources are embedded.

Only the two-line abstract substitution changed among the thirteen
active inputs. It now states containment in a finite union of whole
periodic lines, agreeing with Theorem 1.1 and Proposition 5.3 while
allowing an orbit to travel between lines. No new mathematics, execution,
citation or quantitative bound was added. The original baseline and all
first-build history are preserved without change; see the improvement
log for their exact identity and historical-document boundary.

The assigned nonauthor reviewer may now check the actual revised PDF,
the P1 regression and unchanged proof/source boundaries, then write only
the coordinator-specified round-2 report. The author will make no further
paper edits until expressly authorized. Formal evaluation, shared files,
final release and Git remain coordinator-owned.
