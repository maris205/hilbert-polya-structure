# Same-A delta artifact roles

This new layer supersedes only the initial pending delta state. REPORT.md,
FINDINGS.json, ARTIFACT_ROLES.md and all other initial evidence keep their
original bytes and initial-time scope. DELTA.md is the actual same-process
decision; CURRENT_FINDINGS.json retains the complete E1 finding with the
current exact census. No root or author file was changed here.

Only two initial roles need historical resolution. Resolve an original
`reviews/p210_a/DELTA.md` input to `history/initial_before_delta/DELTA.md`, and
the original review `SHA256SUMS` to `history/initial_before_delta/SHA256SUMS`.
Those copies were made and compared before modifying either original path.
All other 483 initial payloads stay in place. The old manifest's entries
remain review-directory-relative, NOT relative to its new history folder.
INITIAL_PRESERVED_PINS.sha256 is an explicit 485-entry review-relative
projection: all 484 old payloads, mapping DELTA only, plus the old seal.
It is not an overwritten old manifest or the new whole-review seal.

The four actual preservation commands are in execution/delta_preserve_delta01,
delta_preserve_seal01, delta_cmp_initial_delta01 and delta_cmp_initial_seal01.
They use the unchanged safe whitelist recorder under an explicit cleared
ENV4 launcher. Every complete stdout/stderr and native result is retained;
no inherited platform credential value is logged.

check_delta.py is a minimal no-change/preservation adapter. Its before/after
commands and complete outputs are in execution/delta_before01 and
execution/delta_after01. DELTA_INPUTS_BEFORE.json.gz and
DELTA_INPUTS_AFTER.json.gz are lossless complete dictionaries of 119,881
consumed physical keys, each with digest, byte count, resolved path and
symlink value. Their dictionary equality and end-of-phase uncached rereads
are checked. Only the two precisely declared original documentary inputs
use preserved aliases in root's old strict runtime key. Neither science
nor runtime source bytes are exempted.

The adapter binds the exact response and root acceptance, unchanged paper/
Round0/author/initial-A packages, all reviewed inputs, the selected A pair
and build keys, and root strict pair keys. It compares entire archived raw
canonical outputs and selected PDF bytes. These are current evidence reads
and comparisons, not new scientific or TeX executions, proof reviews or
page views. It does not rerun the initial-only auditor against a grown
review directory, or pretend to rediscover the entire resource membership.
Root's accepted originals and strict gates stand; final complete original
audit-key and resource-membership closure remains root-owned.

The final directory-relative nonself SHA256SUMS covers all retained initial
and new delta artifacts, including native command records and the original
seal copy. Its own digest is reported outside itself. The seal operation is
performed only after complete native preservation and after-key checks.
The final verifier is read-only and can be executed without writing back
into the sealed package.

E1's unavailable source/prehash, three unavailable start times, four limited
parent reconstructions, source failures, Robbins caveat and exact own-output
role of the original audit ledger are not changed. Initial pending prose is
historical rather than a current blocker. No global or external acceptance
is inferred: OWNER_AMBER / HOLD_EXTERNAL.
