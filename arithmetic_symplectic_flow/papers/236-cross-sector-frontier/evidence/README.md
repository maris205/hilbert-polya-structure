# Evidence index — ANG-20260918-SDT01

**Scope ID:** `ASFS-SCOUT-20260918-CSF01`  
**Paper ID:** `236-cross-sector-frontier`  
**Status:** `T0 ESTABLISHED; MIXED-PRIME PERIODIC PACKET — STOP / FORK`.  
**Formal Route coordinates:** `UNASSIGNED`. **Route B:** `NOT INVOKED`.

## Inputs and exact methods

- [Version-1 scope and SDT01 short card](../candidate-card.md): entire
  complex ell-squared unit sphere, L_n=log n, ordered quartic coefficients
  (ab)^(-2), actual physical time, no phase quotient.
- [Full derivation](../paper.md): summable real derivatives produce the
  full Hilbert gradient; interaction-frame Picard iteration and its gauge
  identity establish globality on all mild states. No Galerkin cutoff is used.
- The complete span{e2,e3,e6} is proved invariant before its compact
  energy maximum is used. Its critical point solves the original equation
  in every coordinate; lambda and the least return are derived exactly.
- [Claim ledger](../claim-ledger.md): proof/evidence classification and
  naturalness, full-periodic and later-owner limitations.

All mathematical inputs and output statements are available as Markdown.
There are no numerical experiments, fit parameters, floating-point tolerances,
external data, PDFs or generated publication artifacts. Elementary comparison,
finite-dimensional compactness, contraction and Lagrange-multiplier arguments
are spelled out sufficiently to audit the stated scope. Finite invariant
subspace calculations prove a trajectory in the full flow only because the
outside equations and whole-space uniqueness are proved explicitly.

## Bounded source / collision record

The read-only scout compared selected local packets 186, 192, 193, 233--235
and searched the local 18x, 19x, 22x and 23x paper/card files for quartic,
self-catalytic, gauge-invariant, unary, catalytic and related transfer terms.
This was a bounded architecture-collision check, not a literature review or
proof of novelty. No external references were retrieved or cited. The
separate [237 frozen card](../../237-unary-divisor-coherence/candidate-card.md)
is linked solely to distinguish its ownership; its proof is not a dependency.

## Verification boundary

Author self-check on 2026-09-18 covered paper.md, README.md, candidate-card.md,
claim-ledger.md and this evidence/README.md. In the stream directory, a Bash
loop consumed `rg -H -o '\]\([^)]*\)'` on those five exact paths; stripped
the Markdown delimiters and any fragment; skipped empty, HTTP(S) and mailto
targets; and tested each remaining path relative to its source file with
`[[ -e "$(dirname "$task_source")/$task_target" ]]`. The links in this
package have no fragment anchors, so this check does not purport to validate
external URLs or Markdown-anchor normalization.

Four `rg -q` tests per file checked the exact SDT01 ID, the common status
`T0 ESTABLISHED; MIXED-PRIME PERIODIC PACKET — STOP / FORK`, `UNASSIGNED`,
and `NOT INVOKED`. Observed output:

```text
CHECK files=5 local_links=31 missing_links=0 consistency_failures=0
```

## Observed technical review — 2026-09-18

A separate read-only reviewer first received the raw SDT01 card and checked
its gradient, whole-space owner and first periodic discriminator. Subsequent
readback covered all five written files. It found no mathematical or scope
error requiring correction: the factors 1/2 in the full gradient, the norm
identity on all mild states, the full-equation invariant probe, v6 nonzero,
lambda>=log6 and the exact least physical return were checked explicitly.
The written-proof receipt bound paper.md to SHA-256
`b1ceefc1841d524ec2d5a259c5dce8e46f35e22130f3f1348d64d6a981d0c372`.

Root then appended only the separate-lane Section 7 and updated the README's
237 outcome link. The same reviewer checked those limited deltas against
237 and confirmed the different stop mechanisms and absence of cross-owner
credit. The final paper.md SHA-256 is
`44fd2007c20223c03740633d4550ff9ed362dcecf0aca0dd65bb9c25e39fd750`.
No original proof was expanded or re-scored during that delta check.

This is same-runtime model checking, not external peer review or a
correctness certificate. It does not settle naturalness or assert a
literature-wide novelty result. Mechanical integration checks below are
separate from mathematical review.

## Root integration receipt — 2026-09-18

A read-only Node here-document in the stream directory used fs.readFileSync,
path.resolve and fs.existsSync on the five named Markdown files in each of
236 and 237, plus readme.md and papers/README.md. It removed fenced code,
inline code and indented code before extracting Markdown link targets;
HTTP(S), mailto and empty targets were skipped, and local fragments were
stripped before path existence checks. It did not check remote URLs or
anchor spelling. Each package file was tested for its exact candidate ID,
common current status, UNASSIGNED, NOT INVOKED, final newline and absence
of CR bytes. Both indexes were tested for both IDs and package links.

Observed result:

```text
package_files=10
package_local_links=60
index_files=2
index_local_links=451
errors=[]
```

`git diff --check -- readme.md papers/README.md` exited 0 without diagnostics.
`sha256sum papers/236-cross-sector-frontier/paper.md papers/237-unary-divisor-coherence/paper.md`
matched the final technical-review receipts for both papers. The new package
files are untracked, so they were read explicitly rather than assumed covered
by git diff. Existing unrelated changes and earlier packages were preserved.
These are local integrity checks, not a theorem certificate or Route result.
