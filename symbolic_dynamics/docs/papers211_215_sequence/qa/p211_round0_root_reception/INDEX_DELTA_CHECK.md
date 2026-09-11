# Index-only post-reception check

The batch index was refreshed before the stream recovery index. The live paper
README was not edited: its already accepted lifecycle points to the current
batch index. No frozen or scientific file changed.

Actual native `sha256sum -c SHA256SUMS` in the physical `frozen_round0`
returned exit 0 (chunk f3612f), with all 32 payload names explicitly OK and
no omitted manifest entries. A separate read-only check (chunk 209fbb,
exit 0) read all 32 live payloads against the pre-freeze byte/SHA-256 key,
checked all 117 local link occurrences in the two updated indices and root
reception, and rechecked both saved control originals against their historical
mapping. Result: PASS_ROUND0_INDEX_ONLY_CHANGE, 32 unchanged paper payloads,
117 valid local links, two unchanged physical historical controls, zero science.

The old central-index pins now route only to those exact saved originals.
No claim is made that the newest lifecycle text equals its earlier version.
The full before/after scientific replay/build evidence remains accepted under
its recorded dependency keys; this was not a fresh scientific/build/view gate.
