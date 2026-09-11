# Explicit P203 terminal-schema adapter

2026-09-05 UTC. QA_ENGINEERING_ONLY / NOT_PAPER_REVIEW.
The P203 temporal coauthor implements these mechanical adapters, not a new
research review. Only `audit_batch.py` and these new QA records change.
No author/review source, canonical, manifest, frozen snapshot, old coverage
output, recovery index or Git state is changed. P203 remains absent from
`PAPERS` and `AUTHOR` until the parent registers its real terminal Round2.

Auditor SHA-256:
`e3e4d8fc990c7c9532e5575ea672a88c1c4149842f1bade464c20db237fb3b8b`.

## Author layout and exact legacy footer

`author_filenames` has one explicit P203 override:
`verify_p203.py`, `CANONICAL.txt`, both relative to the paper directory.
The active-author registry, required paper payloads and frozen-round core
requirements derive from this same function. All existing papers retain
`code/verify.py` and `code/CANONICAL.txt`; no immutable P203 file is moved,
copied or renamed to fit those older layouts.

P203's author-only footer/count branch requires the exact label `P203 author`,
code SHA-256
`77e7be9b6dc57a156010c6543ff41415415f833119e5a7116ffcef53cc5e1d7d`,
canonical SHA-256
`6a672bcfa97f09c1575aa89bb4e2ca52aa8284315706ec90abbd6d35995dbf00`,
and the complete line
`PASS_AUTHOR_BOUNDED_CHECKS / ALL_N_THEOREMS_REQUIRE_PROOFS`.
It requires exactly seven `assertions=` box counts, a single
`TOTAL_ASSERTIONS=374812`, and equality between their sum and 374,812.
The observed box values are 7, 7, 12, 52, 641, 11,386 and 362,707.
This is not a global relaxation permitting multiple unexplained totals or
author PASS lines to authorize Review A/B. Existing full stdout equality,
two physical replays, normal status forms and all review severity gates
remain unchanged.

## Real build-log provenance

P203's diagnostic-log override is exactly
`qa_final/cold_build_2/main.log`; other papers use `main.log`.
That physical path becomes a required, hash-covered artifact. No root-level
log is manufactured and no old Round0 author build is recycled as final QA.
The unchanged `cold_gate` additionally requires both final cold builds and
checks each build's source, bibliography and PDF against live artifacts,
along with its real logs and the final visual pages. Selecting a diagnostic
log does not bypass those bindings.

The existing Round0 `qa/cold_build1` and `qa/cold_build2` remain historical
author evidence. The new terminal `qa_final` builds and full P203 terminal
audit were not performed by this adapter task; they await the proper stage.

## Historical original-PDF HOLD exception

`pdf_gate` now receives an explicit role, defaulting to `current`. The only
HOLD exception requires every one of:

- paper number 203;
- role `round0_original`;
- the exact workspace path
  `papers/203-monochromatic-triangle-complementation/main_round0_original.pdf`;
- SHA-256
  `617cea5d4f8b50a9946d05bafc2cfbf6fb01bbe45dab754813b07f4f12cc1167`.

Only the missing HOLD marker is exempted. All PDF size, A4, rotation,
metadata, encryption/form/JavaScript, font embedding/Unicode and unresolved
token checks still execute. Symlink PDFs are rejected. The paper gate passes
the original role only for the original PDF, and distinct Round1/2 roles for
their PDFs. The current PDF has the default current role. Even byte-identical
old PDFs fail in a current/Round1/Round2 role or at another path.

The real original and frozen-copy PDFs both retain the exact old digest and
lack HOLD. The current repaired PDF inspected here has SHA-256
`0738965406c046662618ec999474738c064c363fa66ba587e7b33a377f89b47d`
and contains HOLD. This adapter does not grant the repaired version paper
acceptance; its actual reviewer/delta/freeze workflow remains separate.

## Physical current-input coverage

`current_input_gate` parses `CURRENT_INPUTS_SHA256SUMS` relative to the
paper/snapshot directory and requires its targets to equal all physical
files under that directory's `current_inputs`. No fixed count is hard-coded;
there are 11 at the inspected version. Both live P203 and every P203 frozen
round use this check, in addition to complete package manifests.

`HISTORICAL_TEMPORAL_INPUT_PINS.sha256` is one explicitly supplied historical
document. Its own bytes must match their recorded hash, but its obsolete
external targets are not recursively executed as current input requirements.
This preserves the disclosed missing historical-program finding rather than
pretending that hashing the pin-list file repaired it.

## Actual tests and scope

`P203_ADAPTER_CHECKS.txt` records two real completed tool processes. The
first validated both 11-file input sets, fully checked the four-page old
PDF under its original role, fully checked the four-page current repaired
PDF, and invoked `replay` on the authentic P203 author code/canonical.
That invocation ran two fresh Python processes; each returned 374,812 and
complete stdout matched the canonical and the other run. It is an author
reproducibility check, not an independent review or all-size proof.

The second process performed 16 rejection controls. Actual old PDF bytes
were rejected in current/Round1/Round2 roles, at the frozen-copy path, and
under another paper number. An in-memory altered digest was rejected;
injected metadata also failed despite the historical role. The P203 author
footer failed under another author and either review role, with either
wrong pinned digest, or with incorrect/duplicate totals or a wrong box sum.
An unlisted current-input file was rejected. Digest/text/metadata corruption
and unlisted-file controls used in-memory mocks, not physical mutations.
The actual-PDF cases still called the real PDF inspection commands.

Finally, actual hash/coverage/frozen-round checks were repeated for retained
P197/P199/P200/P202, all passing. Their previous author parser formats were
also checked with stubbed outputs; those stubbed parser tests are not new
mathematical replays. The active terminal registry remains exactly those
four papers. Full five-paper globals, zero-open Review A/B findings,
accepted deltas, current/Round1/Round2 HOLD and genuine terminal builds all
remain required. Prior coverage/audit transcripts retain their old code
hashes and counts without rewriting.
