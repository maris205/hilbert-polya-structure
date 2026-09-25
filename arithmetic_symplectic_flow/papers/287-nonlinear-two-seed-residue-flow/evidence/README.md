# Evidence — nonlinear two-seed residue flow

Candidate ID: `ANG-20260920-NRF01`.
Status: `OWNED NONLINEAR CLOCK; UNCOUNTABLE PRIME-PACKET MULTIPLICITY — STOP / FORK`.

## Frozen inputs and manuscript

The original [version-1 card](../candidate-card.md) was frozen before
the main candidate's theorem claims or computation, SHA-256:

    451eb56764544d77e21ece5458e2a465bdcec756d23aca37aaa4a9b0e5cfd362

The [paper](../paper.md) supplied after the completed raw-card checkpoint
has SHA-256:

    1e47a06e6080d2f08e745c9c059ba86bbb344630f44078d72b9c2728adaa45dd

Inputs are exactly full K² at every integer root n>=2, joint additive
Haar, actual standard digit j, g(n+j), the fixed Q(y)=y(1-y), all tail
arrows and their retained lag. The NONLINEAR-OFF owner was separately
precommitted in the same card, with only its fixed-state scope authorized.

Methods: explicit inverse branches; Haar-preserving shear/swap followed
by index scaling; exact Borel IMAGE laws; synchronous tail refinement;
the full equation pz²=z; compatible prime-power idempotents; and complete
fixed-core isotropy. No numerical run, finite prime/modulus cutoff,
precision choice, target zeros, fitted parameter or external search is used.

## Controls and stop

All composite roots stay despite missing incoming branches. Integer
solutions are distinguished from the complete profinite fixed set;
the p=2 boundary is included uniformly. The fixed cores are null but
retain the unique continuous full-point clock. Distinct cores never
share a full forward tail and cannot be merged by their identical time.

The result is a positive nonsingular nonlinear clock construction and
a decisive negative multiplicity result: uncountably many different
least-log-p fixed-core packets for each prime. Higher periods are
unexamined. Q=0 has only one fixed core per prime; its higher periods
and full target fit are also unexamined, and it is not a repaired owner.

The [ledger](../claim-ledger.md) separates those exact scopes. The
[scout record](scout-record.md) preserves prior-template identity and a
separate untested active-pair proposal. Neither supplies transferred
proof, clock, Route credit or authorization for the present candidate.

## Review and handoff

The [internal review](independent-review.md) starts from the frozen
card before reading the manuscript, then checks full proofs and adverse
scope. Native agents inherit model settings and share project context.
These checks are not external peer review, formal verification or
independent-error guarantees. AI assistance and the ARS bounded freeze
and adverse-check workflow are disclosed.

Portfolio: **stop / fork**. T0/scoped T1 owned, naturalness OPEN,
T2 target FAIL; T3 NOT SUPPLIED / NOT PURSUED, classical A0/A1/A2
NOT APPLICABLE, formal UNASSIGNED, Route B NOT INVOKED. Same-object
ledger intact; 278/285/286 unchanged, 241/242 paused; programme active.
No old package, source mirror, model setting, PDF, LaTeX, commit,
upload or external publication is changed.

## Document verification receipt — 2026-09-20

Root read the complete frozen 129-line internal review. No mathematical
revision was requested. Report SHA-256:

    6e577d0c4a5ff3bf506906fa70dc34dfd8bb9e8db13f391f98b1f03c4f56af25

The final manuscript is 291 lines, with the bound paper hash above.
The 172-line card, including its appended administrative outcome, has
SHA-256:

    9d9c0c812103c32d2332def6e902649435c56079d6d9a6f2cfd7af9694788590

The original prefix before the newline introducing `## Appended audit
outcome` still matches the version-1 hash. The 278, 285 and 286 papers
also retain their previously bound hashes; they were not edited.

A read-only Python check from the workspace root used pathlib, re,
hashlib and json. It resolved every package-local Markdown target and
the new 287 registry links; checked candidate ID and status in five
primary package records and two registries; and verified UTF-8, final
newline, no NUL/tab, and trailing spaces of zero or a Markdown two-space
break. Actual paper, report, full-card and frozen-prefix hashes were
checked against their bytes. Result:

    markdown_files: 7
    local_links_checked: 42
    identity_status_files: 7
    unchanged_prior_papers: 3
    issues: []

The scoped command

    git diff --check -- readme.md papers/README.md papers/287-nonlinear-two-seed-residue-flow

returned exit 0 without diagnostics. The new package is untracked, so
the explicit byte/link checks, not Git alone, cover its contents. Existing
dirty-worktree changes are preserved and not attributed to this turn.

Appending this receipt changes no checked link, identity, proof, review
or frozen-card binding. Receipt hygiene and the scoped Git check are
verified after the append; unchanged mathematical inputs are not rerun.
