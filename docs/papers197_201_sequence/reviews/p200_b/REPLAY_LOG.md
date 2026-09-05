# P200 Review B: two actual fresh replays

2026-09-05 UTC. Final verifier SHA256:
`5d1125297099de10cf0ed781786224dc9c5ce8b2343f3bf645322b4bbec37df1`.
Canonical stdout SHA256:
`81f9d15c1605311c49e45e505744d5c5a6dedb89dc377ec4bf2f20617e2355cb`.

Command for both actual processes, from repository root:

```sh
python3 docs/papers197_201_sequence/reviews/p200_b/verify_independent.py
```

## Replay 1

A new Python process was launched after the complete development check.
Its tool execution session was18457, and it exited0. All stdout chunks
were retained in the orchestrator, including the initial banner and all
nineteen box rows. It completed4,026,047 assertions on314,512 full-carrier
states plus46 wide witness configurations. The full retained stdout is
`CANONICAL.txt`. A subsequent complete read of that file was compared
against the captured Replay1 output: byte equality was true.

## Replay 2

A separate fresh Python process, session21874, independently ran the
unchanged verifier and exited0. Its full stdout was separately captured.
It completed the same4,026,047 assertions, all314,512 states and46
witnesses. Captured Replay2 stdout equalled Replay1 stdout byte-for-byte.
After writing and rereading `CANONICAL.txt`, a second independent byte
comparison of Replay2 stdout against the retained canonical file was
also true. No prior output was substituted for this actual execution.

## Scope and independence

The19 complete boxes are $2\times s$ for $2\le s\le8$;
$3\times s$ for $2\le s\le5$; $4\times s$ for $2\le s\le4$;
$5\times2$, $5\times3$, $6\times2$, $7\times2$, $8\times2$.
All targets, not just image points, are checked against their complete
actual predecessor sets. Every fixed self-fibre, recurrent iff, pivot,
partner bound, margin, maximum and all equality targets are checked.
Each witness for $2\le r\le24$, at widths $r+1,r+7$, is checked through
its entire selector itinerary including first recurrent entry.

The data representation is a tuple of column-incidence frozensets; the
selector is derived from cross-column row classes. Two-pass SCC
decomposition plus reverse multi-source BFS computes the functional
graph recurrence and distances. A separate sign-word/ternary-comparison
decoder produces complete inverse sets without calling the forward
selector on reconstructed sources. No author or Review-A verifier code
was read before construction, and neither was read or imported later.
The author canonical transcript was read only after this verifier had
been completed and its final replays launched, to audit the manuscript's
stated author-control counts.

The reviewer is an actual process-separated subagent, not a fictional
second persona. No cross-model or external-model endorsement is claimed.
The earlier development process passed the same code but is not counted
as Replay1 or Replay2. Replays are bounded counterexample pressure, not
substitutes for `PROOF_REDERIVATION.md`. HOLD_EXTERNAL remains in force.
