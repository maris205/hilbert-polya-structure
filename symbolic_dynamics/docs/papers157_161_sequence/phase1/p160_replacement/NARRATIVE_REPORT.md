# Narrative report — rectangular-corner stripping

## One-sentence contribution

Deleting fixed row and column bands from Ferrers diagrams has an exact
all-time dynamics in which rectangle survival controls the clock while two
independent boundary partitions control every target fibre and reveal the
ordered deletion parameters.

## What is established

For positive `a,b`, the map deletes the first `a` rows and first `b` columns
of an integer partition.  A cell-coordinate induction gives every iterate.
The absorption clock is the first time the southeast corner cell
`(at+1,bt+1)` is missing, and the maximum clock among partitions of weight at
most `N` is the first `t` for which the required rectangle has area greater
than `N`.

The inverse result is target-resolved.  For a nonempty target `mu` at rank
`t`, every source consists of a forced copy of `mu`, a forced rectangle, an
arbitrary top excess partition with at most `at` parts, and an arbitrary
bottom partition with largest part at most `bt`.  This gives one monomial and
two reciprocal Pochhammer factors.  The empty target is a separate hook-shaped
class with an explicit finite sum.  Coefficient positivity yields the exact
image threshold under any weight cap.

The thresholds are informative rather than merely enumerative.  The one-cell,
two-cell row, and two-cell column targets recover `a,b` by two differences.
Ferrers conjugation swaps the two parameters, explaining why row and column
probes are both necessary.

## Source subtraction

Barnes--Savage receive credit for one-row/one-column deletion and its Durfee
decrement. Gordon--Houten and Andrews (1971) are directly recorded for
generalized rectangular and rational-slope Durfee viewpoints. Chen--Ji--Zang
are directly recorded for the static `m`-Durfee rectangle symbol, right/below
boundary partitions, and area-plus-boundary weight decomposition.
Andrews--Eriksson provide standard Ferrers and bounded-product background.
Thus every generalized rectangle, static two-boundary decomposition, and
two-Pochhammer factorization receives zero contribution credit. The residual
starts only with fixed `(a,b)` literal cropping at all times, arbitrary target,
separate empty branch, exact cap support, and ordered recovery. No novelty or
priority language is permitted.

## Portfolio separation

RCS is not a tree/word selector or local pruning rule. It uses a global
coordinate window on a Ferrers ideal. P113 acts on principal-hook partition
data, P126 splits composition parts and grows rank, P129 is a stochastic
rootward pile coalescent, and P148 uses local plane-tree promotion. Static
Durfee language is not a portfolio distinction; the all-time literal crop,
arbitrary-target/empty split, cap support, and ordered recovery are.

## Evidence boundary

The theorem is deductive.  Exact enumeration checks coefficients and boundary
cases but does not prove the theorem.  The owner search is bounded, and all
external actions remain on hold.
