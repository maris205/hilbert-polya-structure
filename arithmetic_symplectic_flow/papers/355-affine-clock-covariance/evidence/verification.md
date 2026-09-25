# Batch B — artifact verification, not a scientific experiment

Batch `CLOCK-COUPLING-20260921-B`; packages355–359.
Final execution status: **PASS — ALL FIVE FINAL PACKAGES CHECKED**.

Run from `arithmetic_symplectic_flow`:

```bash
node papers/355-affine-clock-covariance/evidence/verify-batch.cjs --brief
```

Omit `--brief` to print each current Markdown input's exact line count and
SHA-256. The script is read-only and uses Node's standard library only.
It verifies every relative Markdown file target in the five new packages
and this batch's overview blocks, paired code fences and trailing newlines,
the four candidate/audit ID and current-status surfaces in each package,
and each original frozen card's exact line-prefix SHA. The358 clarification
and later outcomes are appended; original definitions are not overwritten.

Preservation checks recursively hash ALL files in old348–354 using sorted
relativePath TAB fileSHA LF bundle records, comparing with the opening
anchors in the [batch log](../batch-log.md). Four guidance/contract files
are checked byte-for-byte against their opening hashes. For root readme and
paper registry, remove ONLY the new batch block and restore the old first
heading's label; reconstructed archive hashes must equal the opening files.
Thus old prose is protected even though the current overview is updated.

The script does not validate an infinite mathematical claim, infer novelty,
check external URLs, or treat builds/review counts as proofs. There are no
new local-fragment links to validate. Mathematical methods, exact inputs and
limits are in the papers; input hashes/EOF and internal review limitations
are in their own evidence files. No scientific numerical experiment ran.

Intermediate executions:355–357 passed22 Markdown/41 links and frozen
packages/rule anchors;355–358 passed29 Markdown/55 package links and both
overview archives. Counts change when later summary/overview files are added;
the final execution below, not an earlier count, defines the handoff check.

## Final execution result

The displayed command completed with exit0 after all fifteen per-round
ARS checkpoints and the five original-card derivations were integrated:

```json
{
  "result": "PASS",
  "packages": 5,
  "markdown": 38,
  "relativeLinks": 94,
  "preservedPackages": 7,
  "preservedAnchors": 4,
  "preservedOverviewArchives": 2
}
```

This includes20 ID/status surfaces and five exact original-card prefixes.
Reporting-only additions to this file and the batch log were then checked
for formatting and existing relative links; no mathematical input changed.
Read-only Git status retained the four known tracked paths (AGENTS, plan and
both overviews); byte-preservation checks confirm that AGENTS/plan and all
seven old packages remain unchanged from this batch's opening state.
No branch, commit, staging, reset or other Git mutation was performed.
