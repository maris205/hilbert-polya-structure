# Paper20 page-fix deterministic build retry authorization

Date: 2026-08-22 UTC

This note supersedes the consumed wrapper invocation documented in
`BUILD_HARNESS_FAILURE_PAGEFIX.md` and authorizes exactly one retry in two new
isolated roots.  The retry must execute every child with its root as the
working directory; the prior roots are forbidden for reuse.  The frozen
source, page-fix source authorization, and fresh R1/R2 source-review hashes
are unchanged.  The exact four-command sequence and five-variable
deterministic environment are those in `BUILD_AUTHORIZATION_R1_PAGEFIX.md`.

No source edit, CAS run, experiment, transport, publication, or upload is
authorized.  A successful retry must produce only the separately persisted
`paper/main_round1.pdf` and `paper/BUILD_RECEIPT_R1.json` after independent
read-only build reviews; any failed retry consumes its roots and requires a
new governance note.

`BUILD_AUTHORIZATION_R1_PAGEFIX_RETRY`
