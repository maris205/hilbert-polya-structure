# P183 improvement log

## Round 0 → Round 1

Review A used unordered-pair four-state coordinates and direct history
partitions, separately rechecking conflict deletion, the independent-set
absorption CDF, ordered endpoints, and both inverse censuses.  Its 1,509,739
assertions found zero Critical, Major, or Minor issue.  Round 1 is an
intentional byte-identical receipt of Round 0.

## Round 1 → Round 2

Review B switched to immutable directed-arc relations, weighted Markov dynamic
programming, inclusion--exclusion, closed-SCC classification, and direct target
star families.  Its 1,274,441 assertions again found zero issue.  Round 2 is
therefore byte-identical to both earlier rounds with SHA-256
`6834170a0ee554a9f4c75040aad762326e24fa5a532e7987c57025be02bd235b`.
Two source-only cold builds reproduce the final PDF.  External status remains
`OWNER_AMBER / HOLD_EXTERNAL`.
