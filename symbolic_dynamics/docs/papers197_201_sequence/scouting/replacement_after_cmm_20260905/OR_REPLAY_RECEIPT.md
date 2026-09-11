# Author Stage1 replay receipt

2026-09-05 UTC. Status: AUTHOR_CONTROL_PASS / OWNER_GATE_PENDING /
NO_PAPER_NUMBER / HOLD_EXTERNAL. This is not an independent review and
not a finished manuscript.

Command, run twice in separate fresh Python processes from repository root:

```sh
python3 docs/papers197_201_sequence/scouting/replacement_after_cmm_20260905/verify_or_ternary.py
```

Both processes exited0. Their complete captured stdout was compared
byte-for-byte in the tool orchestrator and matched exactly. The retained
stdout is `OR_CANONICAL.txt`. Each actual run made3,518,531 assertions.
An earlier n≤8 development run also passed70,553 assertions but is not
substituted for either full replay.

The full replay checks all3^n inputs and all targets for every1≤n≤12,
including absent targets; independent literal/table updates; functional
graph peeling and actual cycle census; complete recurrent iff; sharp
global tails; all maximum-fibre targets; the run recurrence on every
nonconstant image point; and exact parking entry on every twice-image
point. Complete source reconstruction is additionally checked for every
supported target through n7. Temporal fixed counts are tested for every
1≤t≤2n+3 against the actual cycle census, not against a second copy of
the same closed expression.

Separate exhaustive transport controls cover all8,708 weak-composition
configurations with1≤k≤4 and0≤M≤5, including the zero-mass boundary,
mass conservation, permanent occupancy and attained sharp bound. Large
explicit witnesses check every n3..150 and n300,301,302,1000. The largest
full carrier is531,441 states at n12; witnesses at n1000 are structured
examples, not a claim to exhaustive enumeration at that length.

The code uses only Python's standard library and imports no historical
paper/scouting verifier. Its independent table update is distinct from
the comparison-based literal rule. Finite checks support the printed
all-length proof but do not establish all-length validity by themselves.

The complete three-rule pilot was also actually rerun and its stdout
retained in `PILOT_CANONICAL.txt`; it is one bounded scouting run, not
mistaken for two independent controls or an extra theorem axis.

Source/code/proof and canonical file hashes are pinned in the adjacent
`STAGE1_AUTHOR_INPUT_SHA256SUMS`, after the final source memo was written.
The independently authored hostile gate will have its own implementation,
actual replay evidence and decision. It has not been written by this author.
