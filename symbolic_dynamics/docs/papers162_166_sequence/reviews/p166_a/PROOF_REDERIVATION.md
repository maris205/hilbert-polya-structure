# P166 Hostile Review A: independent proof rederivation

**Status:** `PROVABLE AS STATED`.  **Severity:** `0C / 0M / 0m`.  
**External state:** `HOLD_EXTERNAL`.

This document starts from the literal map

\[
T_n(x)=x+\operatorname{wt}(x){\bf1}\quad\text{on }(\mathbb Z/n\mathbb Z)^n,
\qquad n\ge2,
\]

with the weight taken in the integer interval `[0,n]`.  It does not use the
author verifier.

## 1. Free diagonal phase reduction

For fixed `y`, put `X_j=y-j1` and let `m_j` be the multiplicity of symbol
`j` in `y`.  The diagonal action is free: `X_j=X_k` forces `j=k`.  The zero
coordinates of `X_j` are precisely the coordinates at which `y_i=j`, so

\[
T_n(X_j)=X_{j+m_j}.
\]

Coordinate differences are invariant under `T_n`; hence every source that
lands at `y` lies among the `n` states `X_j`.  Induction gives the all-time
oracle

\[
T_n^t(X_j)=X_{g_m^t(j)},\qquad
|(T_n^t)^{-1}(y)|=|\{j:g_m^t(j)=0\}|.
\]

At `t=0` the right side is one, as required.  This is a target-local finite
oracle, not a closed aggregate census.

## 2. Recurrent phases and exact periods

On a nontrivial phase cycle every used increment is in `{1,...,n-1}`.  An
integer lift of one circuit has increment sum a positive multiple of `n`.
The cycle vertices are distinct and their occupancies are part of a profile
of total mass `n`, so the sum is at most `n`; it is therefore exactly `n`.
Thus the cycle uses every positive occupancy and each occupancy is the
clockwise gap to the next support point.  This also proves the converse and
excludes two nontrivial cycles.

A fixed literal state has weight zero or `n`, giving

\[
P_{n,1}=1+(n-1)^n.
\]

For exact period `k>=2`, the positive occupancies along the phase-zero cycle
are a positive ordered composition of `n` into `k` parts.  A composition
`a_1+...+a_k=n` has `n!/(a_1!...a_k!)` labelled lifts.  Summation is the
surjection count

\[
P_{n,k}=k!\left\{\begin{matrix}n\\k\end{matrix}\right\}.
\]

The recurrent census, exact cycle count, divisor formula for fixed iterates,
and zeta product then follow without an additional dynamical assumption.

## 3. Exact preperiods and the last shell

Lift a transient phase path starting at zero until its first zero-occupancy
endpoint.  Its positive increments `a_1,...,a_d` have strictly increasing
partial sums and total `s<n`; total `n` would return to the start and a larger
total cannot be supported by the profile mass.  The visited bins have the
specified positive occupancies, the endpoint bin has occupancy zero, and the
remaining `n-s` coordinate labels may occupy the other `n-d-1` bins.  For a
fixed increment composition the labelled count is

\[
\frac{n!}{a_1!\cdots a_d!}\frac{(n-d-1)^{n-s}}{(n-s)!}.
\]

Summing positive ordered compositions gives exactly

\[
D_{n,d}=d!\sum_{s=d}^{n-1}\binom ns
 \left\{\begin{matrix}s\\d\end{matrix}\right\}(n-d-1)^{n-s}.
\]

The apparently possible value `d=n-1` is excluded: the endpoint is a zero
bin, all other bins would already be visited positive bins, while the total
mass `n` leaves positive mass with no remaining bin.  Hence the cap is
`n-2`.

Equality at `n>=3` forces one zero at `z`, one two at `e`, and ones elsewhere.
If `e=z-1`, the double step skips the zero and closes a recurrent cycle.  In
every other placement, `z+1` has depth `n-2`; the only second deepest phase
is `z+2`, and it occurs exactly for `e=z+1`.  Counting anchor--phase pairs
and dividing by the `n` choices of anchor yields

\[
D_{n,n-2}=\frac{(n-1)n!}{2}.
\]

For `n=2` the literal map is a permutation and the maximum depth is zero.

## 4. One-step inverse atlas and marked distribution

Every possible source of `y` is `y-k1`.  It has `m_k` zeros and integer
weight `n-m_k`.  For `1<=k<n` it lands at `y` exactly when `m_k=n-k`.
Integer weights zero and `n` both reduce to the same residue shift but are
disjoint branches: weight zero occurs only for `y=0`, while weight `n`
occurs exactly for `m_0=0`.  Therefore the displayed fibre formula is exact.

Marking the event `m_0=0` and the events `m_k=n-k` in the multinomial EGF
gives the manuscript product.  Its generic marking assigns degree zero to
the all-zero target, and the additive correction `u-1` moves that single
target to degree one.  Thus the image extraction is correctly oriented.

If `h` middle conditions hold, their distinct prescribed positive counts
have mass at least `1+...+h`.  Hence `h<=h_n`.  For `n>=3`, prescribe counts
`1,...,h_n` in their corresponding bins.  With
`R=n-h_n(h_n+1)/2`, maximality gives `0<=R<=h_n`.  If `R>0`, bin 1 is unused,
and `R<n-1`, so placing the remainder there creates no unintended condition.
This proves the maximum `1+h_n` and its equality criterion.  The construction
fails exactly at the separately handled binary boundary, where the map is a
permutation.

## 5. Independent exact controls

`verify_review_a.py` independently checks:

- every literal state for `2<=n<=7`, including full functional graphs,
  periods, depths, fixed iterates, and every one-step target;
- the all-time oracle for every target through `n=6` and a deterministic
  7,000-target slice at `n=7`;
- every weak composition through `n=11`, including cycle exhaustion,
  last-shell phases, weighted censuses, and fibre equality cases;
- an independent labelled-bin expansion of the marked EGF through `n=30`;
- every triangular-remainder boundary through `n=256` and every one-zero /
  one-two last-shell placement through `n=64`;
- explicit `n=2`, `t=0`, prime/composite, weight-zero, and weight-`n`
  sentinels.

The frozen result is `11,795,304` assertions, `PASS`; two fresh executions
are byte-identical to `CANONICAL.txt`.
