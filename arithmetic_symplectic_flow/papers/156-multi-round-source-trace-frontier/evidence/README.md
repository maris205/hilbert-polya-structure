# Evidence index — ASFS-FRONTIER-20260915-12

**Date:** 2026-09-15  
**Status:** PORTFOLIO ADVANCE — FULL-MAP FLAT TRACES ESTABLISHED; TARGET CLOCK AND FREDHOLM OWNER OPEN.

This is an integration evidence index, not a new proof, numerical experiment,
source lock or Route evaluation. The frozen authority is the
[portfolio card](../candidate-card.md); the authoritative integration prose is
the [paper](../paper.md).

## Exact mathematical owners

| Contract | Full proof and reproducibility | Bounded model-review receipt |
| --- | --- | --- |
| ANG-20260915-LSG01 | [146 paper](../../146-localization-scaling-groupoid/paper.md), [evidence](../../146-localization-scaling-groupoid/evidence/README.md) | [Review](../../146-localization-scaling-groupoid/evidence/review.md) |
| ASFS-20260915-SDC01 | [147 paper](../../147-saturated-drift-cotangent-sieve/paper.md), [evidence](../../147-saturated-drift-cotangent-sieve/evidence/README.md) | [Review](../../147-saturated-drift-cotangent-sieve/evidence/review.md) |
| ANG-20260915-SDC01 | [148 paper](../../148-saturated-divisibility-chain-shift/paper.md), [evidence](../../148-saturated-divisibility-chain-shift/evidence/README.md) | [Review](../../148-saturated-divisibility-chain-shift/evidence/review.md) |
| ASFS-20260915-CCS01 | [149 paper](../../149-coupled-convex-cotangent-sieve/paper.md), [evidence](../../149-coupled-convex-cotangent-sieve/evidence/README.md) | [Review](../../149-coupled-convex-cotangent-sieve/evidence/review.md) |
| ASFS-20260915-WKC01 | [150 paper](../../150-witness-kicked-cylinder/paper.md), [evidence](../../150-witness-kicked-cylinder/evidence/README.md) | [Review](../../150-witness-kicked-cylinder/evidence/review.md) |
| ASFS-20260915-CWT01 | [151 paper](../../151-convex-witness-natural-trace-audit/paper.md), [evidence](../../151-convex-witness-natural-trace-audit/evidence/README.md) | [Review](../../151-convex-witness-natural-trace-audit/evidence/review.md) |
| ASFS-20260915-CHE01 | [152 paper](../../152-coupled-witness-henon-escape/paper.md), [evidence](../../152-coupled-witness-henon-escape/evidence/README.md) | [Review](../../152-coupled-witness-henon-escape/evidence/review.md) |
| ASFS-20260915-SFT01 | [153 paper](../../153-saturated-sieve-flat-trace/paper.md), [evidence](../../153-saturated-sieve-flat-trace/evidence/README.md) | [Review and addressed control clarification](../../153-saturated-sieve-flat-trace/evidence/review.md) |
| ASFS-20260915-AWH01 | [154 paper](../../154-algebraic-witness-henon-sieve/paper.md), [evidence](../../154-algebraic-witness-henon-sieve/evidence/README.md) | [Review](../../154-algebraic-witness-henon-sieve/evidence/review.md) |
| ASFS-20260915-DRC01 | [155 paper](../../155-derivative-roof-completeness-test/paper.md), [evidence](../../155-derivative-roof-completeness-test/evidence/README.md) | [Review](../../155-derivative-roof-completeness-test/evidence/review.md) |

The parent integration reads package summaries and claim ledgers, full relevant
proofs and review evidence. Review records are separate model invocations with
shared task context; they do not establish independent error processes, human
peer review, calibrated correctness or publication readiness. Author
adjudications remain in their owning packages. This index does not silently
amend a source proof or re-score its claims.

## What was checked here

The integration checks exact candidate IDs, changed-map versus changed-owner
relationships, complete versus selected periodic ledgers, clock ownership,
and the distinction among ordinary products, flat traces and Fredholm
determinants. A separate read-only identity check was delegated while the
integration was written. It found ten unique complete IDs and agreement of
the final card, README and claim-ledger statuses in all ten packages; it
confirmed the seven/two/one identity classification and the distinction
between ASFS-20260915-SDC01 and ANG-20260915-SDC01. This is an additional
bookkeeping check, not a new mathematical result. No target data, prime table, orbit cutoff or numerical
precision parameter is used in this integration.

The ten packages' exact proofs, not their finite regression outputs, support
their infinite/full-state claims. Any arithmetic command, limit and output
belongs to the evidence record linked in its row. Standard flat-trace source
provenance is recorded in 153, without importing a compact Anosov theorem
into its noncompact map. This index performs no external source expansion.

## Verification receipt

Package-local Markdown links, ID/status consistency and whitespace are checked
after writing. The parent integrator owns the final cross-package link/count
receipt and registry synchronization; no successful global count is asserted
before that run. The root README and registry are outside this author's write
scope.

Local receipt (2026-09-15): a Node.js filesystem walk over this package's
five Markdown files checked every non-HTTP/non-mail/non-anchor Markdown
target for existence, required the exact portfolio ID and status string in
every file, and checked trailing whitespace while permitting Markdown's
two-space hard breaks. Result: 5 files, 81 local links, 0 missing links,
0 ID/status errors, 0 whitespace errors. This structural verification does
not certify any mathematical theorem. No finite numerical experiment was
performed by this integration author.

## Root integration receipt — 2026-09-15

The root integrated the current-state summary and eleven result/registry rows
in the stream README and paper registry, and added a recovery pointer in
108's README without changing its historical candidate claims. The checked
scope is exactly the 65 Markdown files in packages 146--156 plus those three
navigation files. No other stream, source snapshot, AGENTS.md or plan.md was
edited by this integration pass. Existing unrelated worktree changes remain.

The following read-only structural command is run from the stream directory.
It checks target existence, not web availability or Markdown anchor validity;
it permits two-space hard breaks and ignores bold markup around status fields.
An initial harness treated those formatting variations as status differences;
inspection found no substantive disagreement, and the corrected check below
compares the actual status text. This is not a mathematical proof checker.

```bash
node <<'NODE'
const fs = require('fs'), path = require('path');
const dirs = fs.readdirSync('papers')
  .filter(p => /^(14[6-9]|15[0-6])-/.test(p)).sort().map(p => 'papers/' + p);
const files = [];
function walk(d) {
  for (const e of fs.readdirSync(d, {withFileTypes:true})) {
    const p = path.join(d, e.name);
    if (e.isDirectory()) walk(p); else files.push(p);
  }
}
dirs.forEach(walk);
const nonMarkdownFiles = files.filter(p => !p.endsWith('.md'));
const packageMarkdownFiles = files.length;
files.push('readme.md', 'papers/README.md',
  'papers/108-source-action-frontier-cycle-11/README.md');
const errors = [], ids = [];
let localLinks = 0, coreIdentityStatusChecks = 0;
for (const p of files) {
  const s = fs.readFileSync(p, 'utf8');
  if (/[\t ]+\n/.test(s.replace(/ {2}\n/g, '\n')))
    errors.push([p, 'whitespace']);
  if (/\|[^\n]*\n\s*\n\|/.test(s)) errors.push([p, 'table break']);
  for (const m of s.matchAll(/\[[^\]]*\]\(([^\s)]+)\)/g)) {
    const t = m[1];
    if (/^(https?:|mailto:|#)/.test(t)) continue;
    localLinks++;
    const target = decodeURIComponent(t.split('#')[0]);
    if (!fs.existsSync(path.resolve(path.dirname(p), target)))
      errors.push([p, 'missing target', t]);
  }
}
const registry = fs.readFileSync('papers/README.md', 'utf8');
for (const d of dirs) {
  const read = fs.readFileSync(d + '/README.md', 'utf8');
  const id = (read.match(/(?:ASFS-FRONTIER|ASFS|ANG)-\d{8}-(?:[A-Z]+\d+|\d+)/) || [])[0];
  const statusLine = read.split('\n').map(x => x.replace(/\*\*/g, '').trim())
    .find(x => x.startsWith('Status: '));
  const status = statusLine && statusLine.slice(8);
  if (!id || !status) { errors.push([d, 'missing ID/status']); continue; }
  ids.push(id);
  for (const name of ['README.md', 'paper.md', 'candidate-card.md', 'claim-ledger.md']) {
    coreIdentityStatusChecks++;
    const s = fs.readFileSync(d + '/' + name, 'utf8');
    if (!s.includes(id) || !s.includes(status))
      errors.push([d, name, 'ID/status mismatch']);
  }
  const slug = path.basename(d);
  const row = registry.split('\n').find(x => x.startsWith('| ' + slug.slice(0, 3) + ' |'));
  if (!row || !row.includes(id) || !row.includes(status.replace(/\.$/, ''))
      || !row.includes(slug + '/README.md')) errors.push([d, 'registry mismatch']);
}
if (new Set(ids).size !== ids.length) errors.push(['duplicate ID']);
console.log(JSON.stringify({packages:dirs.length, packageMarkdownFiles,
  checkedFiles:files.length, localLinks, coreIdentityStatusChecks,
  nonMarkdownFiles, errors}, null, 2));
if (errors.length || nonMarkdownFiles.length) process.exitCode = 1;
NODE
```

The root also runs `git diff --check` on these exact navigation and package
paths. Because the new packages are untracked, that Git check alone would not
inspect their contents; the filesystem check above supplies that coverage.
No prior mathematical check is rerun merely because this index is updated.

Final command output (exit 0):

```json
{
  "packages": 11,
  "packageMarkdownFiles": 65,
  "checkedFiles": 68,
  "localLinks": 660,
  "coreIdentityStatusChecks": 44,
  "nonMarkdownFiles": [],
  "errors": []
}
```

The exact-path Git whitespace check also exited 0 with no output. Appending
this plain-text receipt adds no file, Markdown link, ID or status change.
This receipt assigns no Route credit, peer-review status or infinite
numerical claim.
