# ZGR bounded pilot execution receipt

The same frozen pilot source and the same complete boxes 0 <= n <= 8 were
executed twice. No cutoff, hypothesis, map or implementation was enlarged.
Both native exits were zero. The first tool-native output was fully displayed
but not captured directly to a local raw file; it remains a provenance
limitation and is not presented as a locally byte-compared first run.

Command (both invocations), from the workspace root:

    /usr/bin/timeout 60 /usr/bin/env -i PATH=/usr/bin:/bin LC_ALL=C /usr/bin/python3.10 -I -S -B docs/papers211_215_sequence/scouting/root_zigzag/pilot.py

First actual receipt: chunk 4442db, exit 0, wall 0.917250374 seconds.
Second native receipt: ec1b4d, exit 0, wall 0.921035796 seconds.
The second tool-returned combined output string is persisted in
replay02_combined.txt via apply_patch. It is not a separate stdout/stderr
capture; apply_patch may add its final newline. No byte-equality claim between
the two physical invocations is made. Both displayed science totals were
46,234 states and 138,702 assertions. Runtime pins remain after-only.

The second invocation repairs local output retention, not mathematical
evidence at a larger size and not a strict terminal replay obligation.
No all-size theorem, admission or manuscript-review gate is established by
either run. Period, depth and fibre observations are exactly the nine BOX
records in the retained output.
