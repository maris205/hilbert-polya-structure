# Bounded local contrast/diversity intake

2026-09-06 UTC, root. Four new literal maps, all on the labelled ternary
cycle, with initial full boxes fixed at $3\le n\le9$. No candidate or
paper number is assigned. Weak results end a row without a larger cutoff.

For cyclic triple $(a,b,c)=(x_{i-1},x_i,x_{i+1})$:

1. LDC: number of distinct values in the triple minus one.
2. LRG: $\max(a,b,c)-\min(a,b,c)$, the local range.
3. MDE: $|b-\operatorname{median}(a,b,c)|$, median deviation.
4. MNC: $\min(|b-a|,|b-c|)$, minimum adjacent contrast.

All four map the full ternary box into itself, without an invented cap or
parameter restriction. MDE and MNC agree on binary states but differ on
monotone ternary triples; they are not asserted independent mechanisms.
LDC and LRG differ on a two-level triple using both 0 and 2. Known range,
median, contrast, finite-language and elementary-CA primitives receive no
ownership credit. The literal time/target inverse conjunction must survive
source/old-system gates before any admission.

The nearby centre-equality count was desk-eliminated without a pilot:
if $e_i=\mathbf1_{x_i=x_{i+1}}$, its output is $e_{i-1}+e_i$, and the
next equality mask is $1\oplus e_{i-1}\oplus e_{i+1}$. This is a full
linear binary-mask feedback primitive, not an extra executed candidate.
Relabelling the three local multiplicity types does not make new families.

Internal initial search covered distinct-neighborhood/triple/window counts,
local diversity, rainbow feedback and three-letter diversity in manuscript
and killed-scout originals; there was no supported exact literal hit.
That bounded nonhit is not a novelty finding. Dedicated source/mechanism
checks follow only for surviving proof signals. The pilot imports the
existing local `pilot.profile` census helper; it is scouting, not a
standalone author or independent reviewer verifier.
