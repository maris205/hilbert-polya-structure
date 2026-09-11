# Root zigzag lane — pre-pilot contract

2026-09-08 UTC. Author: root. Scouting only; no paper number, admission,
independent review or strict terminal-replay claim. This contributor cannot
review any resulting paper. Project workflow and current batch scope apply.

For a permutation of length n, greedily split from left to right into the
longest nonoverlapping factors whose consecutive comparison signs alternate.
The first sign of each factor is unrestricted. A nonfinal factor has length
at least two. Reverse every factor simultaneously, concatenate, and recompute
the factorization at each epoch. This defines ZGR on every S_n, including the
fixed empty and one-letter words. It is not fixed-position alternating-descent
factorization, maximal monotone runs, or overlapping runs at turning points.

One exact CPU pilot is authorized here: complete S_n for 0 <= n <= 8, within
60 seconds, no random search or subsequent cutoff enlargement. Test the
literal update against an independently enumerated longest-prefix definition;
measure complete functional graphs and every indegree, preserving explicit
cycle/height witnesses. These observations do not prove any all-n assertion.

Collision inputs actually inspected: P117 main.tex lines 1–300 (binary odd
constant-run bit flips and boundary erosion); P122 main.tex lines 1–330
(record-block parity reversal, sharp clock and admissible-cut inverse; one
combined display truncated, so do not claim a complete manuscript read);
P185 main.tex complete (prefix diversity feedback and delay). None is a
literal identity to ZGR. Generic factor reversal, cut decoders, boundary
coalescence, finite-graph census and short periods receive no novelty credit.
The broad original-text search was a discovery aid, not a complete history
proof. Further mechanism subtraction is required if any signal survives.

Primary search leads on 2026-09-08: Yan Zhuang, Counting permutations by
alternating descents, arXiv:1408.1886 / EJC 21(4), P4.23; and Counting
permutations by runs, arXiv:1505.02308. Search excerpts distinguish fixed
parity alternating descents from unrestricted greedy zigzag factors. Their
full relevant arguments are not yet read, and no source clearance is claimed.
Recent 2025–2026 search also returned permutation-language generation, which
is not this update by the exposed definition. Non-hits do not prove novelty.

Proof status before the pilot: NOT CURRENTLY JUSTIFIED. In particular there
is no proved global period classification, sharp clock or separate inverse
extremal theorem. The pilot is only for early rejection or proof direction.

Runtime uses isolated Python with site disabled and an empty environment
apart from PATH and LC_ALL. The source prints its hash, full loaded Python
and native-library path hashes, and all finite-box results. These pins are
after-only runtime observations, not a complete before/after closure or a
strict reusable paper execution capsule. Native exit and combined output
are separately retained via the actual execution receipt. No historical
manuscript or accepted evidence is modified.
