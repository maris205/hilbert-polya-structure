# Paper28 manuscript/validator successor: independent exact-profile review

Date: 2026-09-05. Decision: `EXECUTABLE_PROFILE_REVIEW_PASS`.
No unresolved blocking finding in the authorized successor delta.

The machine-consumed review is
[HERMETIC_BUILD_SUCCESSOR_REVIEW_20260905.json](HERMETIC_BUILD_SUCCESSOR_REVIEW_20260905.json),
11,203 bytes, SHA-256
`b31e863e82ae31265ad1e9ae295c659aff8765623004fcb4e9834f30d5dd5ee2`.
It binds the exact final controls, separate publication/capture sources,
CAPTURE2 audit/outcome and unchanged complete EC-supplement object.

## Final bindings and actual evidence

- Controller: 47,340 bytes, SHA-256
  `bdf7a8acdf3155612f4e190c2ea41295a9e9ee322ccababef5794097a242c611`.
- Successor plan: 6,406 bytes, SHA-256
  `512cfb2dc14e56174741330e1aedf8ee38a06c58acd3381c2dad79790e08dba3`.
- Successor validator: 50,632 bytes, SHA-256
  `af6125f5c7499e437f9e56aa54197bcadd3402e3a33d4607a9a1319a3e72f464`.
- The unchanged loader and the completed independent source review are the
  other two administrative bindings. The source review is 12,750 bytes,
  SHA-256 `a6c4c4de718dfab8afba7c19026678eb0a4241878e969c403606b722de04b76d`,
  and reports `SOURCE_SUCCESSOR_REVIEW_PASS` for the exact new manuscript.
- The supplied actual
  [preflight](HERMETIC_BUILD_SUCCESSOR_PREFLIGHT_20260905.json) is 9,167 bytes,
  SHA-256 `5c06c96b025f280b36758260563b4e466d34f605e9bc842fdeb85c37acf8049f`,
  with decision `PREFLIGHT_PASS_NOT_EXECUTED`. It was executed by the main
  agent, not this reviewer. Its inventory is 6,838 base members plus one EC
  snapshot, 6,051 regular files and 199 PAX-path members.

This reviewer independently checked these actual file hashes and lengths,
both actual source trios with byte/LF counts, the frozen predecessor code and
plans, and the small CAPTURE2/EC outcome and audit anchors. The base archive,
censuses and unchanged dependency inventory were not redundantly rescanned;
their current validation is supplied by that exact actual preflight.

## Controller and provenance review

The final controller diff was read against the hash-checked frozen EC
predecessor, with a function-level AST comparison. The only changed functions
are the eight expected source/binding/materialization/run/self-test functions;
archive validation, no-follow helpers, snapshot, loader, isolation, privilege
drop, process ownership and final-log checking retain their original AST.
The finalization changes the two explicit pending pins and clarifies the
inherited supplemental-input comment; it introduces no new execution logic.

The two source roles are separate throughout:

- `capture_sources` is the original `paper/` trio. Its main file remains
  73,733 bytes, LF1605, SHA-256
  `bdc7a1edc06b3f8cfc75c6b47a8c24180883d24eef878c70d857588d19f1762e`.
  Only this binding is compared with the CAPTURE2 manifest and EC outcome.
- `sources` is the reviewed `paper-successor-20260905/` trio. Its main file is
  84,983 bytes, LF1855, SHA-256
  `7beb4f783cd370dc4b0d9d1e9178e3e48ce1ef9ed1497e0e9883b10739d4a1f9`.
  Only this trio is copied to `/source` and consumed by publication commands
  and the new validator. Macro and bibliography identities remain unchanged.

Both roles are checked before/after each child and at final binding. Failure
records separately attempt to rebind each role and the historical EC input.
The review gate requires five controls, both source roles and the unchanged
capture/supplement evidence. No historical source review is represented as a
review of the successor, and no capture is relabelled as having captured it.

Fixed commands/passes, environment, limits, auxiliary convergence, log
predicates, readonly namespace checks and full raw cross-root work comparison
remain. The sole new root is `build-capsule-successor-20260905`, exclusively
created after preflight and review binding. This reviewer did not probe it or
any old root. No retry, old-root repair, recapture, host fallback, installation,
budget expansion or external effect is added.

## Validator correction review

1. Named links are accepted only when kind4 supplies a nonempty `nameddest`,
   its resolved destination is an in-range integer local page, and that page
   agrees exactly with the link record. This is not permission for PDF Named
   actions, unresolved destinations or external URI/file actions.
2. `OpenAction` stays in the global unsafe-key set. Only the actual catalog's
   own key is exempted after resolving an unchained local GoTo to a real page
   object and validating the view kind, arity and finite numeric parameters.
   URI, JavaScript, Launch, remote/Named actions, Next chains, non-page
   references, reference cycles and malformed views remain rejected. Nested
   or other catalog-shaped dictionaries do not inherit that exception.
3. The physical-envelope check uses the producer's single classic-xref and
   direct-Length stream profile. Exact indexed objects cover the physical
   body; opaque stream spans may contain CMap EOF bytes. The separate LF/CRLF
   endstream delimiter, physical terminal trailer, startxref offset and xref
   closure are checked. Prev/XRefStm, appended documents or xrefs, unindexed
   gaps, trailing data and offset/identity/Length inconsistencies fail. The
   parsed physical trailer must also agree with MuPDF's trailer.

The old generic object grammar is preserved in its default mode. Its new
prefix mode returns the exact value end without swallowing a trailing comment
on behalf of the envelope checker. The author's initially exposed Length+1
delimiter ambiguity was fixed in code, with both negative tests retained.

The 22--30 inclusive content-page requirement and exact terminal/References
boundary remain. Title/anonymity, metadata, provenance, bibliography/URL
closure, 8+32 heading/bookmark correspondence, page geometry, font embedding,
rendering, visual disposition and final-integrity obligations are not lowered.
This is a fixed-producer check, not a general PDF compatibility promise.

## Tests and independence

This reviewer read the test implementation, then independently ran its default
memory-only mode with administrative Python `-I -S -B`: exit0, **97/97 PASS**,
no recorded fixture access, no file writes, no PyMuPDF/fitz import, and no
validator `run` or build invocation. The exact test script is 20,509 bytes,
SHA-256 `20ed9a29da6eca1151acfcb4680cf4b2e33df70424516150ab6c9606d454cb7b`.

Six further reviewer-authored in-memory cross-checks also passed: named page0;
indirect destination array; destination-reference cycle rejection; nested
catalog exception rejection; separate CRLF stream delimiter acceptance; and
lone-CR delimiter rejection under the fixed profile. These checks imported
only source definitions and the synthetic fixture constructor. They neither
read an actual PDF nor wrote a file.

The author's separate **103/103 PASS** report is supplied evidence, not a claim
that this reviewer reran preserved-artifact cases. Its
[JSON](PDF_ACCEPTANCE_SUCCESSOR_TEST_REPORT_20260905.json) SHA-256 is
`0abbddcb8f6943ece3f11d36d6b1ebb9898ea7c1ec46e237283d468a144409d7`;
its [narrative](PDF_ACCEPTANCE_SUCCESSOR_TEST_REPORT_20260905.md) SHA-256 is
`a0257916acc7ce6a36b4e1c3f84f2c4a7c0d75e759d038165231819a9a9ef42e`.
That report's six additional exact-artifact/source regressions cover all 163
recorded named links, the local startup view, 21 stream EOF markers, unchanged
object/URI safety, the reviewed source and retention of the genuine
20-content-page failure. The reviewer read and hash-bound that report without
accessing its old build-root fixtures.

## Verdict boundary

The reviewer is independent of the controller, validator and source authors;
only the two new review documents were written. No controller, preflight,
capture, validator pipeline, renderer or build was run by this reviewer, and
no old build root or live-host publication dependency was accessed. The
completed mathematical source review was bound, not rerun or replaced.

`EXECUTABLE_PROFILE_REVIEW_PASS` permits only the exact reviewed one-shot
profile under the user's existing confirmation and inherited contract. It is
not proof that a future dependency cannot be missing, not a new build/PDF or
visual PASS, not a Route A/B evaluation, and not final local acceptance or
external-release authority. Actual fresh-root execution and all remaining
acceptance checks still have to succeed; a failure remains preserved without
automatic retry.
