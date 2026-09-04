# P191 author improvement log

## Pre-freeze proof pressure

The composition-cut implementation was separated from the literal tuple
update before Round 0. Boundary carriers `N=1,2,3`, the final untested
endpoint, the unique `N-3` extremizer, every time in its orbit, every labelled
target fibre, image positivity, and mass were all registered explicitly. The
global path recurrence was then factored across mandatory target intervals,
providing a second exact inverse description rather than only a scalar count.

## Hostile Review A and Round 1

The formal process-separated reviewer used recursive composition tuples,
direct merge-and-flush updates, global inverse binning, backward interval DP,
and brute interval refinements. Complete carriers through `N=18` produced
2,864,221 reviewer assertions and no mathematical counterexample. It opened
one Minor companion-ledger issue: `SOURCE_VERIFICATION.md` had mistaken an
OEIS database-wide footer date for the latest A398023 entry revision. The
ledger alone was corrected to 22 July 2026, and the original reviewer process
returned `PASS_DELTA_ACCEPTED` with final open counts `0/0/0`.

No manuscript, theorem, proof, reference, or PDF delta was requested.
`main_round1.pdf` is an intentional byte-identical receipt of the accepted
Round-0 manuscript, with SHA-256
`d8675928ecfe528b950af5402097b5f69657efc9cba7c8eb0bb5c27ec96df78b`.

## Hostile Review B and Round 2

Review B reopened the inverse theorem from interval-local deleted-cut subset
grammars. Instead of Review A's recursive composition tuples plus backward
interval DP, it kept the cut-mask carrier and enumerated deleted cuts
explicitly inside each target interval. Its 164,049 exact assertions
rechecked the fixed-state recurrence, sharp `N-3` clock, unique deepest
composition, every-target fibre product, exact image criterion, and fibre
mass, with `Critical 0 / Major 0 / Minor 0`.

No source or PDF delta was requested. `main_round2.pdf` is a byte-identical
receipt of Round 0 and Round 1, with SHA-256
`d8675928ecfe528b950af5402097b5f69657efc9cba7c8eb0bb5c27ec96df78b`.
Terminal QA on 2026-09-04 completed two source-only cold builds, final
manifests, and all author/reviewer replays. The bounded owner search has not
changed, and `OWNER_AMBER / HOLD_EXTERNAL` remains binding.
