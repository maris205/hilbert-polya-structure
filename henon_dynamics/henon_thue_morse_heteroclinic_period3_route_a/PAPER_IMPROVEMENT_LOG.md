# C154 paper improvement log

No external reviewer transport or numeric score was used.  Both passes were
genuine internal proof, definition, scope, and presentation audits followed
by compilation.

## Round 0 to round 1

Findings:

- The first draft stated only that positive and negative shifts approach the
  two source components; it did not prove the converses or exhaust bounded
  shift sequences.
- The unique interface pair was used informally without turning its cylinder
  into an isolation and wandering proof.
- Exact-period points and primitive cycles were compressed into one sentence.

Repairs:

- Added uniform-recurrence/diagonal realization of every `X_TM` point,
  residue-class realization of all three periodic phases, and the unbounded
  subsequence exhaustion.
- Added the singleton-cylinder proof and orbit injectivity.
- Inserted Möbius inversion before division by period.

## Round 1 to round 2

Findings:

- “Dense orbit” had been used as if it implied standard forward topological
  transitivity.  This is false here because each interface point is isolated
  and visited once by the forward orbit.
- The equality for the nonwandering set needed both inclusions stated.
- The Thue--Morse periodic-point exclusion needed an all-window bridge, not a
  mismatch only at the seed.
- The release draft lacked a Chinese abstract, bilingual keyword sets, and
  the workflow-required declarations.

Repairs:

- Replaced the claim by the precise dense full two-sided `Z`-orbit statement
  and added the forward counterexample `U={sigma x}`, `V={x}`.
- Proved the two limit components nonwandering and the interface complement
  wandering.
- Restored the aligned-block, arbitrary-window aperiodicity argument.
- Added independently structured English/Chinese abstracts, six keywords in
  each language, and transparent data, ethics, contribution, conflict,
  funding, and AI-use declarations; switched the final build to LuaLaTeX for
  embedded CJK glyphs.

Final internal audit: no unresolved issue remains inside the frozen scope.

## Final typography cross-review

The release cross-review found that a document-wide `small` declaration made
the theorem page unnecessarily dense and left the declarations page sparse.
The global reduction was removed; the tuple and scope boundary were broken
into display blocks to preserve clean line breaking at the normal 10-point
body size.  No mathematical content changed.
