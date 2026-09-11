# Gate-side documentation diagnostics

These are not KIP scientific executions and are separate from the author's
preserved runtime-audit failure.

1. An initial lookup of
   `.agents/skills/symbolic-dynamics-research/references/WORKFLOW.md` returned
   exit 2 because that path does not exist. The correct complete
   `docs/research_state/WORKFLOW.md` was then read.
2. Both browser screenshots of Higgins PDF pages 12 and 13 returned
   `Internal Error` with `TimeoutError`; no HTTP status was reported.
   Native retrieval and rendering were subsequently attempted, with their
   own full streams in `native/04*` through `native/06*`.
3. A read-only JSON extraction merged identical line numbers from different
   source pages. It was not accepted as a missing source segment. The
   actual Stein II author HTML was reopened and section 4.2 was read.
4. The first invocation of `python .../kip_candidate_gate/evidence.py historical`
   returned exit 1: the collector mistakenly expected an author
   `SHA256SUMS`, whereas the sealed author package uses `MANIFEST.json`.
   The returned exception was `FileNotFoundError` at `checked_manifest`.
   The fifteen old byte copies and two inherited-contract copies were
   already made; their contents were unchanged. The collector was corrected
   to parse the actual JSON schema with the same exhaustive membership,
   size and hash requirements. The complete author `capture.py` was read
   before its read-only `verify` command was used. No author file, schema,
   historical evidence or scientific producer was changed.

The own collector's documentation re-invocation does not consume or repeat
the author's sole scientific invocation. Gate checks must not be described
as universal exit-0 tool history; these failures are explicit.

The complete read-only `diff -u` between the author's failed v1 diagnostic
and preserved v2 returned exit 1 because the files differ, as expected;
this is not an execution failure of either script. It showed the two-file
comparison and distinct output directory without a change to frozen audit
or scientific producer.
