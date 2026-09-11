# LFCTR is the exact old Q01: counting correction

2026-09-05 UTC. **EXACT_HISTORICAL_CONTROL / ZERO_NEW_BREADTH_WEIGHT**.
This corrects a historical-repeat classification, not a mathematical theorem
or MCT admission. Preserve the original replacement ledger, all accepted
candidate/review packages, and all earlier snapshots unchanged.

The independent MCT reviewer flagged this while auditing the root's new
adjudication. Root then freshly read the complete old Q01 Section4.9 in
`docs/papers147_151_sequence/scouting/combinatorial/SCOUT.md` (508--575),
the current LFCTR row in `scouting/replacement_lane/BREADTH_AND_KILL_LEDGER.md`
and its actual `verify_replacement_lane.py` tournament setup/update.

Both carriers are all labelled tournaments on the same ordered vertices.
Both select the lexicographically first cyclic triple, reverse all three
arcs simultaneously, and hold if none exists. In the upper-pair encoding,
both eligibility predicates are x_ab=x_bc!=x_ac. The current code enumerates
triples in increasing lexicographic order and XORs precisely their three
edge bits. The identity map on labelled tournaments therefore intertwines
the full updates at every size. This is exact historical equality, not
just ownership of the local move, a same-name suspicion, or bounded census
agreement. The recorded n=6 profile agrees as a secondary sanity check.

The earlier central note saying 'existing local move with changed scheduler'
was wrong relative to Q01: the old scheduler already was lexleast. The
original lane's 'nine new literal maps' is preserved as historical wording,
not used as a current deduplicated total. Q01 remains KILL_OWNER_THIN; LFCTR
does not reopen it and is reclassified as KILL_EXACT_INTERNAL_Q01.

Immediately before this correction, adding MCT produced a provisional58
attempts with5selected+3reserve+50killed and17historical+8WIP. That exact
TSV/reconciliation now survive in breadth_snapshots/mct_provisional58_20260905/.
Move LFCTR's same row from current-failed weight1 to historical-control
weight0. The corrected state is **57=5selected+3reserve+49killed**, plus
**18 historical controls and8 code-only WIP**, still **83 total records**.
This new57 is not the preceding second-replacement57 snapshot, which had
4selected/3reserve/50killed and lacked MCT. Equal totals do not mean equal
record sets. MCT itself still contributes exactly one new attempted literal.

The correction neither changes the five eligible contracts
P197/P199/P200/P202/P203 nor certifies completion of P203. MCT's nonblocking
historical intermediate-code archival finding remains unrepaired. All
manuscript zero-open-finding and HOLD_EXTERNAL requirements are unchanged.
