# Evidence — gcd-normalized residue flow

**Candidate ID:** `ANG-20260920-GNR01`  
**Status:** `OWNED GCD-RESIDUE CLOCK; ONLY ONE LOG-TWO PACKET — STOP / FORK`.

## Mathematical inputs and outputs

Inputs are exactly the [version-1 card](../candidate-card.md): all
positive integer pairs, full K=Z_hat, current gcd/residue feedback,
normalized additive Haar on every root, the entire retained-lag
T-tail groupoid, its Borel IMAGE derivative and the complete real
extension. The immutable original-card prefix has SHA-256

    bc7e24440bbadd31bcdbd2b37c2fe3b8f9709555a5ce30da859b79e47c18de2b

The [328-line manuscript](../paper.md) reviewed at checkpoints 2–3
has SHA-256

    a640a3aee9a3fb9003b42f5b4aa3d5c6c53388692109521714fc902e54a3aa93

Proof methods are compatible residues, finite-cylinder Haar scaling
extended to Borel sets, full inverse-branch composition, the extremal
affine seed equation and cyclic recurrence inequalities. The output
is a full-state classification: one periodic state (2,2,0), no other
eventual preimages, one least-log-2 packet with repeats r log 2, and
no odd-prime packet. The full non-onto source and all null points are
retained. The [ledger](../claim-ledger.md) distinguishes owned-clock
success from prime-family failure and from open naturalness.

## Controls, limits and reproducibility

The mathematical controls were frozen before the proof: coprime
sector, all diagonal roots, zero/minus-one seeds, contrasting actual
seeds 0 and 1 at (2,2), GCD-OFF and FEEDBACK-OFF. The first altered
owner has no packet; the second has two distinct least-log-2 packets.
Formal root loops are not substituted for full arithmetic returns.
No comparator changes the main candidate.

There is no scientific numerical code, cycle enumeration, sample
size, cutoff, precision setting, prime table, externally fitted clock
or zero data. The proofs apply to all frozen states; document hashes
and link checks are administrative verification, not mathematical
verification. No embedded-circle, coarse-Hausdorffness or general
nonperiodic convergence theorem is claimed. PROVES_TOO_MUCH concerns
remain a possible design issue, not a new universal-encoding theorem.

The [scout record](scout-record.md) gives definition provenance and
the separate nonadmitted divisor-sum/history lane. No new external
literature is used. This record does not claim external novelty.

## Review and authority

The [three-checkpoint report](independent-review.md) records the
raw-card audit before manuscript access, the exact manuscript binding
and the final adverse check. These are internal same-model checks
with shared-context limitations, not external peer review, formal
verification or an independent-error guarantee. AI assistance and
ARS workflow use are disclosed in the paper and scout record.

Portfolio: **STOP prime-family promotion / FORK**. Same-object ledger
intact. T0 and scoped T1 retained; T2 ledger established but ordinary-
prime coverage FAIL. T3 NOT SUPPLIED / NOT PURSUED; classical A0/A1/A2
NOT APPLICABLE, formal UNASSIGNED, Route B NOT INVOKED. Old packages
unchanged; 241/242 paused; programme goal remains active.

## Document verification receipt — 2026-09-20

After the reviewer froze its report, root read all 210 report lines;
no mathematical revision was requested or made. Root then appended
the outcome to the card and updated only this new package and the
two current-workflow registries for integration. This statement does
not attribute pre-existing dirty-worktree changes to the current turn.

A read-only Python standard-library check used `pathlib`, `re`,
`hashlib` and `json` from the workspace root. It enumerated the package's
Markdown files, resolved all local Markdown targets against their
containing directories, checked the new 282 links in both registries,
and checked exact candidate ID/status strings in the five primary
package records plus both registries. It also checked UTF-8, final
newlines, absence of NUL/tab characters, and trailing spaces of only
zero or the Markdown hard-break pair. Observed output:

    markdown_files: 7
    local_links_checked: 43
    identity_status_files: 7
    issues: []

The original card is recovered by splitting the final bytes at the
first newline followed by `## Appended audit outcome`. Its SHA-256
matches the frozen value above. The final 179-line appended card is

    604672749b2dce56097e49950391728d7ca7dd64d8d2068e2dd12f9f3042e155

The 328-line paper remains bound to the hash above; the 210-line
review report has SHA-256

    97d9bb824f682cee0bceb3671a71c13579011969ed5217e5c5cf46a92b2e49ca

`git diff --check -- readme.md papers/README.md papers/282-gcd-normalized-residue-flow`
returned exit 0 with no diagnostics. The new package was untracked,
so the explicit file-level checks above, not that Git command alone,
covered its contents. No commit, upload, publication or scientific
calculation was performed. Appending this receipt changes no checked
link, identity, proof, review binding or frozen card. Receipt hygiene
and the scoped Git check are checked once more after this append.
