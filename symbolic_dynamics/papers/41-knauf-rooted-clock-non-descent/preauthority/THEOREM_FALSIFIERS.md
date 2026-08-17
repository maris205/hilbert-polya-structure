# Theorem targets and falsifiers

## T0 — convention fidelity

Target: the matrix definition reproduces the frozen recursion.

Defeat the package if independent calculation finds any word `u` for which

```text
h(u0) != h(u)
or
h(u1) != h(u) + h(complement(u)).
```

The claimant must not repair a failure by transposing matrices or reversing
word order without issuing a new source lock.

## T1 — direct-limit append-one non-descent

Target: the canonical map `[w] -> [w1]` is not well defined on the colimit
under `w -> w0`.

Falsifier: give a valid proof that `[1]=[01]` in the frozen colimit while
preserving the colimit-invariant `h`, or show that the frozen direct-system
embedding is not right trailing-zero extension.

Non-falsifiers: defining an action on full matrices, choosing a representative,
or enlarging the state.  Those change the contract.

## T2 — cyclic clock and repetition failure

Target: `h` does not descend to necklaces and `log h` is not additive on word
powers.

Falsifier: recompute, in the frozen convention, either

```text
h(01) = h(10)
or
h(11) = h(1)^2.
```

Non-falsifiers: replacing `h` with `tr(M_w)`, a spectral radius, a derivative
multiplier, or an asymptotically equivalent free-energy clock.

## T3 — Liouville orbit-character failure

Target: `lambda(h(w))` is neither cyclic nor power-compatible.

Falsifier: recompute the generated labels or Liouville values so that both

```text
lambda(h(001)) = lambda(h(010))
and
lambda(h(11)) = lambda(h(1))^2.
```

The first equality alone does not defeat the power witness, and the second
alone does not defeat the cyclic witness.

Non-falsifiers: a matrix-valued/history-dependent cocycle on a new state space
or an externally imposed arithmetic phase.

## T4 — inventory trace/determinant separation

Target: on `Re(s)>2`, `Tr(Q_s)=zeta(s-1)/zeta(s)` but the owned Fredholm
determinant has all higher `u` coefficients and vanishes at `u=1`.

Falsifier: show one of the following within the frozen operator definition:

- the full stable multiplicity is not `phi(n)`;
- `Q_s` is not trace class for some asserted `Re(s)>2`;
- `Tr(Q_s^r)` is not `zeta(rs-1)/zeta(rs)`;
- the eigenvalue-one state does not exist;
- the trace-log series is asserted outside its stated `|u|<1` domain.

The theorem should be narrowed, not cosmetically defended, if a domain issue
is found.

## Novelty falsifier

The proposed paper is not worth integrating if a primary source is located
that explicitly states and proves the same exact conjunction for the same
rooted label:

```text
trailing-zero append-one non-descent
+ h(01) != h(10)
+ h(11) != h(1)^2
+ Liouville cyclic/power failure.
```

A paper on the cyclic matrix-trace Farey chain, equal limiting free energy, or
a different transfer operator is a collision to cite, not this falsifier.

## Route falsifier

The expected strict tuple is defeated if independent review supplies
same-object evidence upgrading any of A1, A2, or A4 under the frozen object,
clock, marker, and function space.  Evidence from a changed trace model or
Gauss/Mayer operator cannot move those coordinates.

