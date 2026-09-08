# IR1 independent finite-core review plan

Frozen 2026-09-07 UTC before this reviewer's reconstruction run.

## Exact bounded assignment

Independently verify the computational part of the proposed classification
of integral periodic points of
`T_a(x,y,z)=(y,z,yz+a-x)` for every integer `a`. The finite verification
is conditional on the separately reviewed analytic reduction in
`integral_return/IR1_PROOF.md`, Sections 1–4: outside the listed channels,
every cycle has difference amplitude `1 <= D <= 100` and all coordinates
between `-3D-1` and `3D-1`.

The original author run, code, output and accepted M1/AS2 contracts remain
untouched. Only this `finite_core` directory may be written. No author
enumeration function is imported or executed. Hashes identify inspected
inputs; they do not establish mathematical coverage or correctness.

## Independent reconstruction

1. Retain both extremal signs `delta = -D, +D` directly. Do not normalize
   by reversing a word and do not merge reverse-oriented cycles.
2. Enumerate the right difference `q` first. For a center
   `s in {-3,-2,-1,0,1}`, define the left difference
   `p=(s+1)delta-q`. Intersect explicit integer intervals for the first
   coordinate `u` using the two height bounds and the inequalities
   `|(u+1)p| <= 2D`, `|(u+delta+1)q| <= 2D`.
3. Recover the parameter from
   `a=q-s(u+delta)+u+s`. Iterate the inverse map
   `T_a^{-1}(x,y,z)=(xy+a-z,x,y)` with exact Python integers.
4. Stop only at a proved box/difference exit or the first repeated
   state. Injectivity requires a repeat to be the initial state. A
   visited-state set detects a violation explicitly; no period cutoff
   is installed.
5. Identify an oriented cycle by its parameter and its least
   lexicographic triple. Reconstruct its native forward word from that
   state and verify both directions. For fixed `a`, deterministic
   injective dynamics ensures distinct cycles have disjoint state sets.
6. Match complete sets of oriented triple states with independently
   generated terminal-family words; do not copy the author's
   rotation-pattern classifier. Check all family recurrence identities
   as polynomial identities over the integers, independently of the
   finite-core run.
7. Only after independent discovery, compare full native cycle sets,
   periods, parameter values and family labels with the author's
   JSONL evidence. Retain every mismatch, not only exceptional counts.

## Expected evidence and honest limits

The author reports 74,866 positive-difference seeds and two exceptional
cycles. These are comparison targets, not filters in the independent
search. The independent program must publish actual seed/exit/return
counts, the complete discovered oriented-cycle output and the result of
full set comparison. It must verify reversal closure without quotienting
by reversal.

The review will separately state mathematical coverage, code review,
actual execution, terminal-family matching, any must-fix issues, and the
dependency on the analytic reviewer. It cannot certify global novelty,
target Euler/root-number claims or an entire paper merely by passing
this finite computation. This is internal AI-assisted non-author review.
