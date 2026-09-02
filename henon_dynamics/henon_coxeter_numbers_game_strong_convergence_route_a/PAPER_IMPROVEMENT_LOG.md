# Paper improvement log

The paper-writing workflow was applied as one baseline plus two substantive
mathematical revisions.  The pure-theory figure phase concluded that a figure
would not clarify the proof beyond the boundary and claim--evidence tables, so
no decorative figure was added.

## Round 0 -- finite convention and strict chamber

The baseline froze the Cartan transpose, positive firing condition, and left
product convention.  It proved the root-sign lemma and the strictly dominant
theorem: legal words are reduced, terminate at `w_0`, and have `|Phi^+|`
moves.  Classical ownership and the sign-convention issue were stated rather
than hidden.

- artifact: `paper/main_round0_original.pdf`
- pages: 2
- SHA-256:
  `baa01816e5a604b684a9ae067ff2c1fbf4b3a8bbac2b18c736ab5f1b7d479300`

## Round 1 -- parabolic quotient and boundary closure

The first substantive revision replaced a strict-chamber-only result with the
all-wall theorem.  It introduced `J`, `W_J`, `Phi_J`, and `W^J`; proved the
quotient-lifting lemma; identified `w_0w_J` both as the unique shortest
representative of `w_0W_J` and the maximum of `W^J`; and proved the exact
length loss `|Phi_J^+|`.  It then closed the zero vector, arbitrary walls,
disconnected products, positive/zero rank one, the strict `>0` gate, and the
finite-only stopping boundary.

- artifact: `paper/main_round1.pdf`
- pages: 3
- SHA-256:
  `5a248cb37dfb8eb26b3b698fd9ae0d2f23375dd0018c93bec9cf4d90ba4b7bab`

## Round 2 -- independent evidence and claim firewall

The second substantive revision added the producer-independent positive-root,
Weyl, inversion, longest-element and parabolic reconstruction; exact evidence
scale and hostile controls; verified primary/monograph metadata; mechanism-
level collision comparisons; finite-type nonclaims; and the strict all-fail
Route-A/Route-B-false conclusion.  It explicitly separated terminating
reduced words from primitive periodic or arithmetic data.

- artifact and final: `paper/main_round2.pdf = paper/main.pdf`
- pages: 4
- SHA-256:
  `3a3684fe15c61d0e6fa76b46a0719a80e3e63d1a6a2a6091028f11d95a92e518`

For every round, two builds in different fresh paths, with two LuaLaTeX passes
per build, reproduced the archived PDF byte for byte.  The three hashes are
pairwise distinct, so the revision archive cannot collapse to one cosmetic
build.

## Post-review release hardening

The final executable section was hardened without changing the theorem.  The
checker now rejects duplicate JSON keys at every depth, checks every analytic
obligation/nonclaim/collision sentence exactly, enforces strict scalar and row
types, and proves completeness and uniqueness of every finite grid.  The
hostile suite grew from 54 to 84 attacks, including raw duplicate keys,
unknown/missing fields, same-size drop-replace controls, and bool--integer type
confusions.  The release gate now repeats these exact contracts independently
and extracts text from all three archived rounds.  The collision scan is
retained as a hashed package-local snapshot rather than a brittle live
dependency on shared registries that legitimately grow in later batches.
