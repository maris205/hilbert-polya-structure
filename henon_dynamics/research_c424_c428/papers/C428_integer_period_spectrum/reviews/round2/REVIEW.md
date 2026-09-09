# C428 — actual second manuscript review

2026-09-09 UTC. Reviewer: coordinator `/root`, not the IH6 proof or
C428 manuscript author. This is current-team, nonblind, AI-assisted
internal review, not human peer review or an external-model service.

## Decision

**PASS: P1 and P2 closed; no remaining must-fix item and no new optional
change requested.** The author's additional T1 typography correction
is verified. No further manuscript edit or artificial third source
version is required. Final fresh-directory builds and release checks
are separate gates, not awarded by this report.

## Actual inputs and read scope

The first actual review is [round 1](../round1/C428_REVIEW.md), SHA256
`1bfe9d8b9396e78711f1970268381af170d74693b47023b0e7c81c642868f6f7`.
I read the complete author improvement log, complete three-file revision
diff, complete revised Appendix A source, and both other changed inputs
(`references.bib` and `sections/01_theorem_sources.tex`). The diff is
`papers/C428_integer_period_spectrum/reviews/round1/source_changes.diff`,
SHA256 `8bf5c669abf9687f51b20022981bcf2e48d8572b9cc02509b84afb55cee31ed9`.

The actual revised `main.pdf`, `main_round1.pdf` and
`builds/round1_revised_03/main.pdf` all have SHA256
`cf02bdd886584949847f2583904601bb2734010a5f9d9cafbcbe749ddb0553af`:
16 pages, 389314 bytes. The `_03/source.tar` SHA256 is
`aa8d95083804dc7f226be3b72eb901aede362c5f347959e01ca4b5ec131c6171`.
Read-only `tar -xOf | cmp` compared all 15 active TeX/bibliography inputs
with that archive; all matched. All 12 inputs outside the declared
three-file change matched the saved original source byte for byte.

This is a focused second pass after the first pass's full source,
proof, text and 16-page visual review. I read the full original-to-revised
PDF text diff, rechecked the revised pseudocode and reflowed Appendix B
and references, and visually inspected the six affected rendered pages
2 and 12–16. I do not claim another full 16-page visual pass here.
Fresh `pdftotext -layout main.pdf - | cmp` confirms the inspected revised
text belongs to the active PDF. The full diff shows no other proof,
table, witness or theorem-content change. The required all-page final
visual pass remains the final builder's separate task.

## P1 — coordinate-keyed algorithm migration

The original small-certificate pseudocode passed an ordered values list
to a function that indexed by an actual integer letter. The revised
small-certificate caller explicitly forms
`v = {e[j]: values[j] for 0 <= j < k}`. `FULL_CYCLES` now specifies
coordinate-keyed values and compares coordinate support with `set(E)`.
For the previously problematic alphabet `(0,2)`, a state with second
coordinate 2 now reads the assigned value at key 2, not a nonexistent
third positional list entry. This closes the concrete first-pass issue.

The same representation is followed through the complete large branch:

- `eta[b]` is explicitly an endpoint-distance value; on the right it
  is assigned to the affine letter `D-b`, while on the left it is
  assigned to `b`. The map `h` is keyed by those actual affine letters.
- Endpoint values of `h` are zero placeholders multiplying the zero
  secant-remainder factor, not restrictions on the original polynomial.
- `V` is explicitly a dictionary on `U`. For left and right interiors,
  `b=abs(beta)` gives `u(u-D)=-bD+b*b`; the endpoint `D=(1,0)` correctly
  has zero factor. Distinct template letters stay distinct for `D>=10`.
- The explicit loop over every `z in U` supplies both identity arrows
  and all nonidentity edge roots. There is no free unbound `z`.
- At each exceptional integer `D0`, the caller forms both the evaluated
  alphabet and the map `{u(D0): V[u](D0) for u in U}`. It does not pass
  coefficient pairs or a positional array to `FULL_CYCLES`.
- The optional pruning iterates over `V.values()`, not dictionary keys.
  A nonempty finite allowed-root intersection invokes the exact graphs
  there; the unrestricted branch includes the identity graph and all
  exceptional edge roots. No unproved maximum diameter was introduced.

I rechecked the finite partial-function traversal: a path either exits,
joins previously processed states, or repeats on its own path; only the
last suffix contributes a cycle, and full support is tested on actual
coordinate letters. Starting at every unprocessed state does not impose
an orbit-length cutoff. Newton divisibility and endpoint-template
generation remain the previously proved reductions.

The frozen author's actual implementation already used a coordinate map
and the independent reconstruction used its separate justified encoding.
The issue concerned their manuscript pseudocode migration, not a failed
execution or a gap in the infinite analytic reduction. No mathematical
script was changed, imported or rerun for this review; the existing exact
certificate receipts remain the computational evidence, not these byte
comparisons or the hand-checked `(0,2)` example.

## P2, T1 and document checks

Both internal IH6 references now render one year after “9 September”;
the adjacent duplicated years are gone. All seven source identities and
their AI-assisted/internal status remain explicit. The bibliography
diff removes only those two duplicate date fragments. T1 joins the
source-broken `secant- affine` into the correct rendered `secant-affine`
on page 2, without altering the reduction statement.

All 19 font resources in the active PDF are embedded. The converged
`_03/main.log` and `.blg` have no Warning/Error/undefined/Overfull/Underfull
diagnostics (`rg` returned 1 for no matches). This is not a claim that
initial unconverged passes had no warnings. A second manuscript-input
list lookup found no standalone manifest; the 15-member archive check
above uses the explicit active `main.tex`, bibliography, sections and
tables instead. No absent file is counted as a successful check.

Pages 12–14 retain a readable continued pseudocode layout, page 15 has
the unchanged reconstruction proof, and page 16 resolves all seven
references. No clipped formula, missing code line, unresolved reference
or new visual blocker was found on the affected pages.

## Boundaries retained

The theorem is the two family-union integer least-period spectra for
`p in Z[t]`, arbitrary degree at least two, with the native one-step
map. It is not the claim that each polynomial realizes every period,
not an integer-valued rational-coefficient theorem, not a rational-point
resolution of Ingram's quadratic conjecture, and not a sharp point-count
bound. The classical Pezda bound, C412/C417 ownership and finite
computer-assisted dependency remain explicit. No target Euler factor,
root number, automorphy or spectral correspondence is established.

No fresh literature search, mathematical computation, PDF rebuild,
formal evaluation, seal or Git operation was performed by this review.
