# P166 narrative report

## The question

The paper studies a state-dependent translation on a cyclic cube.  At each
step, the number of nonzero coordinates is added to every coordinate.  The
feedback is nonlinear at the word level, while the update moves only along
a diagonal translation orbit.  The central question is whether that tension
leaves a complete, nontrivial finite dynamics rather than just a change of
coordinates.

## The organizing mechanism

Fix a target `y` and record the symbol multiplicities
`m_j=#{i:y_i=j}`.  The diagonal orbit consists of `X_j=y-j1`, and direct
calculation gives

```text
T(X_j) = X_{j+m_j}.
```

Thus every literal orbit is exactly conjugate to the functional graph of a
weak composition of `n`.  This is not only a reduction for forward orbits:
it gives the target-local all-time inverse oracle
`|(T^t)^-1(y)|=#{j:g_m^t(j)=0}`.

## Temporal result

A nontrivial phase cycle has positive increments whose sum is a positive
multiple of `n`, but the entire composition has mass `n`.  The cycle must
therefore consume all mass and wind once; its positive entries are its
clockwise gaps.  This yields every exact-period count and the zeta product.

Transient paths have a different geometry.  Before first reaching a zero
bin, their ordinary partial sums are strictly increasing and remain below
`n`.  Summing the forced positive occupancies and the free unvisited mass
gives the full exact-depth formula

```text
D_(n,d) = d! sum_{s=d}^{n-1} binom(n,s) S(s,d)
                    (n-d-1)^(n-s),      1 <= d <= n-2.
```

The maximum tail is `n-2`.  Equality forces one zero, one double occupancy,
and ones elsewhere, with one forbidden relative placement.  The last shell
has `(n-1)n!/2` states.

## Independent inverse result

Every source of a fixed target differs from it by one of the `n` diagonal
shifts.  Separating the two integer-weight branches that become the same
residue shift gives an exact one-step fibre formula.  Multinomially marking
the corresponding occupancy events produces a global indegree EGF.  A
triangular-number budget gives the sharp maximum fibre and its equality
criterion.

This axis does not use the transient-path census.  Conversely, the depth
formula does not use target indegrees; the common input is only the literal
phase conjugacy.

## Contribution ceiling

The exact binary member is the parity-controlled complement map of
Meyer--Pommersheim and receives zero credit.  Hamming terminology, diagonal
group actions, siteswap neighbours, occupancy/parking language, Stirling
and ordered-Bell identities, and generic zeta conversion also receive zero
credit.  The source search is bounded and does not certify novelty.  The
all-time result is only a target-local phase oracle, not a closed global
all-time fibre census.

Independent Hostile Review A accepted the complete package with
`0 Critical / 0 Major / 0 minor` after `11,795,304` assertions.  Fresh
Review B then returned `ACCEPT_INTERNAL`, again with zero findings, after
`14,005,344` assertions.  Rounds 1 and 2 are both no-change freezes.

External lifecycle: **`HOLD_EXTERNAL`**.
