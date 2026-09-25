# Evidence — nonlinear full-residue clock admission

**Record ID:** `ASFS-SCOUT-20260920-NRC01`  
**Status:** `NONLINEAR HAAR IMAGE SINGULAR; CONSERVATIVE LIFT CLOCK ZERO — STOP / FORK`.

## Exact inputs and methods

The [version-1 card](../candidate-card.md) fixes two separate owners:
Q(x)=x(1−x) on full K with h, and H(x,y)=(y,y(1−y)−x) on full K²
with h×h. No finite quotient replaces either carrier. The original
card SHA-256 is

    4638196a40f85ff7716c3a4c27c0d1d0295a225e95c3fb3f4dce880212a35e58

The [256-line manuscript](../paper.md) supplied to the reviewer has
SHA-256

    0a8fb297083345d5eb4ed41640b39b0232935a4f76d7b62e34f026a879fb2db9

Checkpoint 2 requested two precision edits: describe x and 1−x by
their sum being 1, and explicitly restrict the null-saturation
interpretation to the intended countable / second-countable étale
measure class. Neither changes a proof or conclusion. The resulting
257-line final manuscript has SHA-256

    50429784fc1f634da86aa6aae1aac1b0e109b7fcc82a6169a68bb80a5bf95d38

For NRC-L, the proof counts the exact odd-prime image by an involution,
uses CRT and arbitrary finite collections of congruence cylinders to
deduce a zero full Haar measure, and solves the entire zero fibre by
compatible prime-power residues. The source-fibre count and null-set
saturation disprove the frozen second-countable étale / nonsingular
Haar recipe. No time-return conclusion is substituted for that failure.

For NRC-H, direct inverse identities and finite-quotient permutations
give full Borel product-Haar invariance. This derives the actual
joint IMAGE J=1; its full continuous version is fixed by full support.
The resulting all-state time groups are {0}, independently of discrete
periodicity. Each proof belongs only to its named owner.

## Controls and limits

Controls retain finite versus full residue images, integer versus
full idempotent fibres, and discrete versus time isotropy. The
Hénon-form replacement is a different recurrence, not a repair of
Q. No scalar parameter, roof, measure or seed domain is altered.
The [scout record](scout-record.md) preserves two other definitions
without treating them as consequences of the main theorems.

No scientific code, orbit census, cutoff, precision, prime table,
zero fitting, external reference expansion or novelty claim is used.
The arbitrary-N bound is a proof, not extrapolation from finitely many
primes. The prime-indexed idempotent description is a solved fibre,
not a supplied prime-packet list. Other measures, non-étale carriers
and physical clocks are outside this negative conclusion.

## Review and handoff scope

The [internal review](independent-review.md) records raw-card checking
before manuscript access, the exact manuscript binding and final
adverse review. It is same-model scrutiny with shared-context limits,
not external peer review, formal verification or an independent-error
guarantee. AI assistance and ARS workflow use are disclosed.

Portfolio: **STOP both supplied clock admissions / FORK**. Same-object
comparison intact, no main candidate admitted. No T0–T3 coordinates
assigned; classical A0/A1/A2 NOT APPLICABLE, formal UNASSIGNED,
Route B NOT INVOKED. The [claim ledger](../claim-ledger.md) preserves
unavailable NRC-L time, zero NRC-H time and open prime/naturalness fields.
Old packages unchanged, 241/242 paused, programme goal active.

## Final document verification — 2026-09-20

Root read the complete frozen 132-line internal report. The two
precision edits were incorporated; no blocking issue remains. The
final paper is the 257-line version bound above. Report SHA-256:

    c560f44d18e9ba1e82f8c8e7589e13041632229aa0f3b0ab15ea0586812f66c9

The original-card prefix, extracted before the newline introducing
`## Appended audit outcome`, still matches the version-1 hash above.
The full 164-line card including its administrative outcome has SHA-256

    b2b5fe0279bccaf479d57a27371d618ea75b317ae63287d81d31f83130736d58

From the workspace root, read-only Python using `pathlib`, `re`,
`hashlib` and `json` enumerated all package Markdown files, resolved
their local Markdown links relative to the containing file, and checked
the new 283 links in both registries. It checked exact ID/status in
five primary package records and the two registries; package-file
checks covered UTF-8, final newline, no NUL/tab and trailing spaces
limited to zero or the two-space Markdown break. Actual result:

    markdown_files: 7
    local_links_checked: 37
    identity_status_files: 7
    issues: []

The paper, report and original-card bindings were checked against the
actual bytes. `git diff --check -- readme.md papers/README.md papers/283-nonlinear-residue-clock-screen`
returned exit 0 without diagnostics. The new package is untracked;
its contents were covered by the explicit file checks, not that Git
command alone. No commit, upload or publication action was taken.
Pre-existing dirty-worktree changes are not attributed to this turn.

This receipt introduces no new link, identity, mathematical claim or
change to the bound paper/report/card. After appending it, receipt
hygiene and the scoped Git check are rerun; unchanged mathematical
inputs are not re-audited.
