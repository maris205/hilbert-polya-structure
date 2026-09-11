# LBR: complete elementary deductions, no promotion

Author: `nineteenth_finite_scout`; 2026-09-07 UTC. The helper did not
contribute to these LBR proofs. These are author mathematics for a killed
desk, not an independent gate or manuscript review. No state enumeration
was used in obtaining or checking them.

Write `T_n` for the map defined in `INTAKE.md`, with positions `1,...,n`.
An occurrence of a three-letter pattern is indexed by its starting
position. Empty prefixes satisfy every avoidance condition below.

## 1. Recurrent set and sharp global entry time

Let `z(w)` be the number of zero letters. Every nonidentity step changes
`010` to `101`, reducing `z` by exactly one. Such a step requires at least
two zeros and at least one one. It also leaves at least one zero, namely
the middle letter of the new `101`. Therefore any active orbit makes at
most `z(w)-1 <= n-2` nonidentity steps. For `n<=2`, every word is fixed.

The fixed words are exactly those avoiding `010`. Since `z` strictly
decreases at every nonidentity step, no nontrivial cycle exists. Thus the
recurrent set is exactly this fixed set, for every `n`.

The upper bound is sharp. For `n>=3`, start from `0^(n-2)10`. At epoch
`t`, for `0<=t<=n-2`, the word is

`0^(n-2-t) 1 0 1^t`.

To verify the formula, if the leading zero block has positive length,
the only `010` starts at its last zero: the preceding positions are zero,
and the suffix after the displayed middle zero consists only of ones.
Its replacement yields the next formula. At `t=n-2`, the word is
`101^(n-2)` and avoids `010`. The entry time is consequently `n-2`.

Hence, writing `tau` for first entrance into the recurrent set,

`max_{w in {0,1}^n} tau(w) = max(0,n-2)`.

This proves the sharp global bound, not a closed formula for each source's
normal form or entry time in terms of a new invariant. The mechanism is
the generic strictly decreasing letter count.

## 2. Complete nonredundant target-local inverse

Fix any target `y=y_1...y_n`. Define `A(y)` to contain exactly the indices
`i in {1,...,n-2}` satisfying all three conditions:

1. `y_i y_(i+1) y_(i+2) = 101`;
2. the prefix `y_1...y_(i-1)` avoids `010`;
3. if `i>=3`, then `y_(i-2)y_(i-1) != 01`.

For `i in A(y)`, obtain `x^(i)` by replacing the indicated `101` in `y`
by `010`. Then the full predecessor set is the disjoint union

`T_n^(-1)(y) = {y : y avoids 010} disjoint_union {x^(i) : i in A(y)}`.

Proof. Any nonfixed predecessor replaces one particular occurrence,
so reversing that edit forces `x=x^(i)` and condition 1. To make the
redex at `i` leftmost, it is necessary and sufficient to forbid every
earlier start. Starts at most `i-3` are unchanged and are excluded exactly
by condition 2. At `i-2`, the reconstructed triple ends in zero and is
`010` precisely when `y_(i-2)y_(i-1)=01`, giving condition 3. The triple
at `i-1`, if it exists, has middle letter zero and last letter one, so
cannot be `010`. These exhaust the earlier starts. Thus all listed
sources and only those sources map to `y`.

Distinct accepted indices yield distinct sources: if `i<j`, the source
edited at `i` has zero in position `i`, while the source edited at `j`
still has `y_i=1`. None equals `y`. The fixed predecessor is available
if and only if `y` avoids `010`. This proves completeness and
nonredundancy independently of a forward functional-graph table.

In particular,

`|T_n^(-1)(y)| = 1[y avoids 010] + |A(y)|`.

## 3. Sharp maximum one-step fibre

For every `n>=0`,

`max_y |T_n^(-1)(y)| = floor((n+1)/4)+1`.

Proof of the spacing bound. Let accepted indices be
`i_1<...<i_m`. Two occurrences of `101` cannot start one position
apart. A gap of three is impossible for accepted indices: the earlier
occurrence forces the two letters preceding the later start to be
`01`, violating inverse condition 3. A gap of two forces the substring
`10101`, so `y` then contains `010` beginning one position after the
earlier start. Every further occurrence starts at least two positions
after the later one, and its preceding prefix contains this `010`;
condition 2 therefore forbids every further accepted index. Consequently
all gaps are at least four, except possibly a single gap of two between
the last two indices.

If `y` is fixed, it has no `010`, so the exceptional gap is impossible.
For `m>=1`, its last accepted triple ends at a position at least
`1+4(m-1)+2=4m-1`. Hence `m<=floor((n+1)/4)`. Adding the fixed parent
gives the asserted bound.

If `y` is not fixed, there is no fixed parent. For `m>=2`, the spacing
bound gives `n>=1+4(m-2)+2+2=4m-3`, so
`m<=floor((n+3)/4) <= floor((n+1)/4)+1`. For `m<=1` the same desired
upper bound is immediate. These cases prove the bound for every target.

For sharpness, if `n<=2`, all words are fixed and every fibre has size
one, which is the displayed value. If `n>=3`, put
`m=floor((n+1)/4)>=1`, and form

`y=(1011)^(m-1) 101 1^(n-(4m-1))`.

The exponent in the final block is nonnegative. The zeros in this word
are separated by three ones, so `y` avoids `010`. Each of the `m`
displayed `101` blocks starts at `1,5,...,4m-3`; its preceding prefix
avoids `010`, and every existing preceding pair is `11`, not `01`.
All these indices are accepted, giving `m` edited parents and the fixed
parent. The bound is attained. No uniqueness or complete maximizer
classification is asserted.

## 4. Exact old adapter and source boundary

Let `c` complement all bits. For every legal one-step edit at index `i`,

`c( replace_i(w,010,101) ) = replace_i(c(w),101,010)`.

Complementation also preserves the ordering of starting indices. Thus
`c T_n c` is exactly the **leftmost deterministic selection** of the
old stochastic S24 legal rewrite relation. The original S24 instead
chooses an active index uniformly. A deterministic map and that Markov
kernel are not being equated or called conjugate. The exact conclusion
is equality of the underlying labeled rewrite graphs under complement,
followed by the stated schedule selection.

This distinction matters because the relation is nonconfluent:
`01010` can be rewritten to either `10110` or `01101`, and both avoid
`010`. This is a symbolic two-branch witness, not a numerical pilot.
Choosing the left branch makes an autonomous map, but does not create a
new termination engine. With `a=0,b=1`, its local edit is the literal
classical `aba -> bab` one-rule Semi-Thue example in the inspected Klop
primary text. That source comparison claims the relation, not that Klop
proved the leftmost scheduling extremum above.

The local inverse and its packing bound are a separate elementary
description, but the temporal ingredient remains the exact old relation
with a priority selector and letter-count loss. Under the current gate,
this does not supply the required fresh two-axis residual. Final status:
**NO_PROMOTION / KILL_OLD_REWRITE_SCHEDULE**.
